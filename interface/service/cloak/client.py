import asyncio
import base64
import json
import logging
import time
from dataclasses import dataclass, field

import httpx

from config import (
    CLOAK_URL,
    MANIFEST_TOKEN,
    CLOAK_DISABLED,
    SERVICE_ID,
    SERVICE_TYPE,
    SERVICE_VERSION,
    CAPABILITIES,
    SSE_RECONNECT_MAX_ATTEMPTS,
    SSE_RECONNECT_BASE_DELAY,
    SSE_RECONNECT_MAX_DELAY,
)
from cloak.models import CloakRegistrationRequest, CloakRegistrationResponse, HaltEvent

logger = logging.getLogger("episteme.cloak")


@dataclass
class CloakState:
    session_id: str | None = None
    signing_key: bytes | None = None
    halted: bool = False
    halt_reason: str | None = None
    registered: bool = False
    start_time: float = field(default_factory=time.time)


async def register_with_cloak(state: CloakState) -> str:
    """Register with Cloak and populate state. Returns halt_stream_url.

    Raises RuntimeError if registration fails (service must not start).
    """
    if CLOAK_DISABLED:
        logger.warning("Cloak disabled — skipping registration")
        state.registered = True
        state.session_id = "dev-session"
        return ""

    payload = CloakRegistrationRequest(
        service_id=SERVICE_ID,
        service_type=SERVICE_TYPE,
        version=SERVICE_VERSION,
        capabilities=CAPABILITIES,
    )

    try:
        async with httpx.AsyncClient(timeout=10.0) as client:
            resp = await client.post(
                f"{CLOAK_URL}/cloak/services/register",
                json=payload.model_dump(),
                headers={"Authorization": f"Bearer {MANIFEST_TOKEN}"},
            )
            resp.raise_for_status()
    except httpx.HTTPStatusError as e:
        raise RuntimeError(
            f"Cloak registration rejected (HTTP {e.response.status_code}): {e.response.text}"
        ) from e
    except httpx.ConnectError as e:
        raise RuntimeError(f"Cannot reach Cloak at {CLOAK_URL}: {e}") from e

    data = CloakRegistrationResponse(**resp.json())
    state.session_id = data.session_id
    state.signing_key = base64.b64decode(data.signing_key)
    state.registered = True
    logger.info("Registered with Cloak (session=%s)", state.session_id)
    return data.halt_stream_url


async def listen_halt_stream(state: CloakState, halt_stream_url: str) -> None:
    """Persistent SSE listener for halt and key_rotation signals.

    Reconnects with exponential backoff. After max consecutive failures,
    self-halts (fail closed).
    """
    if CLOAK_DISABLED or not halt_stream_url:
        return

    consecutive_failures = 0
    delay = SSE_RECONNECT_BASE_DELAY

    while True:
        try:
            async with httpx.AsyncClient(timeout=None) as client:
                async with client.stream(
                    "GET",
                    halt_stream_url,
                    headers={"Authorization": f"Bearer {MANIFEST_TOKEN}"},
                ) as stream:
                    consecutive_failures = 0
                    delay = SSE_RECONNECT_BASE_DELAY
                    logger.info("SSE halt channel connected")

                    async for line in stream.aiter_lines():
                        line = line.strip()
                        if not line or line.startswith(":"):
                            continue
                        if line.startswith("data: "):
                            raw = line[6:]
                            _handle_sse_event(state, raw)

        except asyncio.CancelledError:
            logger.info("SSE halt listener cancelled")
            return
        except Exception as e:
            consecutive_failures += 1
            logger.warning(
                "SSE connection lost (attempt %d/%d): %s",
                consecutive_failures,
                SSE_RECONNECT_MAX_ATTEMPTS,
                e,
            )

            if consecutive_failures >= SSE_RECONNECT_MAX_ATTEMPTS:
                state.halted = True
                state.halt_reason = "sse_channel_lost"
                logger.error(
                    "SSE reconnect limit reached — self-halting (fail closed)"
                )
                return

            await asyncio.sleep(delay)
            delay = min(delay * 2, SSE_RECONNECT_MAX_DELAY)


def _handle_sse_event(state: CloakState, raw: str) -> None:
    try:
        event = HaltEvent(**json.loads(raw))
    except (json.JSONDecodeError, Exception) as e:
        logger.warning("Failed to parse SSE event: %s", e)
        return

    if event.type == "halt":
        state.halted = True
        state.halt_reason = event.reason or "operator"
        logger.warning("HALT received: %s", state.halt_reason)

    elif event.type == "key_rotation":
        if event.new_key:
            state.signing_key = base64.b64decode(event.new_key)
            logger.info("Signing key rotated")
        else:
            logger.warning("key_rotation event missing new_key")

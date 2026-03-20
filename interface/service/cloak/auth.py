import hmac
import hashlib
import json
import logging
from typing import Callable

from fastapi import Depends, HTTPException, Request

from config import CLOAK_DISABLED
from cloak.models import TokenClaims

logger = logging.getLogger("episteme.auth")

# Operation class hierarchy: admin > write > read
_OP_CLASS_LEVEL = {"read": 0, "write": 1, "admin": 2}


async def verify_token(request: Request) -> TokenClaims:
    """FastAPI dependency that extracts and verifies the bearer token.

    In CLOAK_DISABLED mode, returns a permissive dev token.
    """
    if CLOAK_DISABLED:
        return TokenClaims(
            job_id="dev",
            agent_class="dev",
            operation_class="admin",
            resources=["*"],
        )

    cloak_state = request.app.state.cloak

    if cloak_state.halted:
        raise HTTPException(
            status_code=503,
            detail={
                "error": "service_halted",
                "detail": f"Service halted: {cloak_state.halt_reason}",
                "service": "episteme",
                "halted": True,
            },
        )

    auth_header = request.headers.get("Authorization", "")
    if not auth_header.startswith("Bearer "):
        raise HTTPException(
            status_code=401,
            detail={
                "error": "missing_token",
                "detail": "Authorization header with Bearer token required",
                "service": "episteme",
            },
        )

    token = auth_header[7:]
    claims = _verify_and_decode(token, cloak_state.signing_key)

    # Find episteme service scope in token claims
    episteme_scope = None
    for svc in claims.get("services", []):
        if svc.get("service") == "episteme":
            episteme_scope = svc
            break

    if not episteme_scope:
        raise HTTPException(
            status_code=403,
            detail={
                "error": "service_not_in_scope",
                "detail": "Token does not grant access to episteme",
                "service": "episteme",
            },
        )

    return TokenClaims(
        job_id=claims.get("job_id", ""),
        agent_class=claims.get("agent_class", ""),
        operation_class=episteme_scope.get("operation_class", "read"),
        resources=episteme_scope.get("resources", []),
    )


def _verify_and_decode(token: str, signing_key: bytes | None) -> dict:
    """Verify token signature and decode claims.

    Uses HMAC-SHA256. Token format: base64(claims).base64(signature)
    Swap this function to change the signing algorithm (e.g. Ed25519).
    """
    if not signing_key:
        raise HTTPException(
            status_code=503,
            detail={
                "error": "no_signing_key",
                "detail": "Service has no signing key (registration may have failed)",
                "service": "episteme",
            },
        )

    parts = token.rsplit(".", 1)
    if len(parts) != 2:
        raise HTTPException(
            status_code=401,
            detail={
                "error": "malformed_token",
                "detail": "Token must be in format: payload.signature",
                "service": "episteme",
            },
        )

    payload_b64, signature_b64 = parts

    # Verify signature
    expected_sig = hmac.new(
        signing_key, payload_b64.encode(), hashlib.sha256
    ).hexdigest()

    if not hmac.compare_digest(expected_sig, signature_b64):
        raise HTTPException(
            status_code=401,
            detail={
                "error": "invalid_signature",
                "detail": "Token signature verification failed",
                "service": "episteme",
            },
        )

    # Decode claims
    try:
        import base64
        claims_json = base64.urlsafe_b64decode(payload_b64 + "==")
        return json.loads(claims_json)
    except (json.JSONDecodeError, Exception) as e:
        raise HTTPException(
            status_code=401,
            detail={
                "error": "invalid_token_payload",
                "detail": f"Cannot decode token claims: {e}",
                "service": "episteme",
            },
        )


def require_operation_class(required: str) -> Callable:
    """Returns a FastAPI dependency that enforces a minimum operation class.

    Usage:
        @app.post("/endpoint")
        def handler(token: TokenClaims = Depends(require_operation_class("write"))):
            ...
    """
    required_level = _OP_CLASS_LEVEL.get(required, 0)

    async def _check(token: TokenClaims = Depends(verify_token)) -> TokenClaims:
        actual_level = _OP_CLASS_LEVEL.get(token.operation_class, -1)
        if actual_level < required_level:
            raise HTTPException(
                status_code=403,
                detail={
                    "error": "insufficient_operation_class",
                    "detail": f"Requires '{required}' access, token has '{token.operation_class}'",
                    "service": "episteme",
                    "required": required,
                    "actual": token.operation_class,
                },
            )
        return token

    return _check

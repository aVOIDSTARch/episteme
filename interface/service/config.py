import os
import logging
from pathlib import Path

logger = logging.getLogger("episteme")

SERVICE_ID = "episteme"
SERVICE_TYPE = "knowledge"
SERVICE_VERSION = "0.1.0"
SERVICE_PORT = int(os.environ.get("EPISTEME_PORT", "8100"))

CLOAK_URL = os.environ.get("CLOAK_URL", "http://cloak.tailnet:8300")
MANIFEST_TOKEN = os.environ.get("EPISTEME_MANIFEST_TOKEN", "")
CLOAK_DISABLED = os.environ.get("CLOAK_DISABLED", "").lower() in ("true", "1", "yes")

CAPABILITIES = ["tree", "file", "search", "metadata", "agent_query",
                "skills", "projects", "ideas", "guides", "docs"]

IDEAS_ROOT = Path(os.environ.get("IDEAS_ROOT", str(Path.home() / "ideas")))

SSE_RECONNECT_MAX_ATTEMPTS = int(os.environ.get("SSE_RECONNECT_MAX_ATTEMPTS", "5"))
SSE_RECONNECT_BASE_DELAY = float(os.environ.get("SSE_RECONNECT_BASE_DELAY", "1.0"))
SSE_RECONNECT_MAX_DELAY = float(os.environ.get("SSE_RECONNECT_MAX_DELAY", "30.0"))


def validate_config() -> None:
    if CLOAK_DISABLED:
        logger.warning(
            "*** CLOAK_DISABLED=true — authentication is OFF. "
            "This must NEVER be used in production. ***"
        )
        return
    if not MANIFEST_TOKEN:
        raise RuntimeError(
            "EPISTEME_MANIFEST_TOKEN environment variable is required. "
            "Set CLOAK_DISABLED=true for local development only."
        )

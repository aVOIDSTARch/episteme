from typing import Optional
from pydantic import BaseModel


class CloakRegistrationRequest(BaseModel):
    service_id: str
    service_type: str
    version: str
    capabilities: list[str]


class CloakRegistrationResponse(BaseModel):
    session_id: str
    signing_key: str  # base64-encoded
    halt_stream_url: str


class TokenClaims(BaseModel):
    job_id: str
    agent_class: str
    operation_class: str  # "read" | "write" | "admin"
    resources: list[str]


class HaltEvent(BaseModel):
    type: str  # "halt" | "key_rotation"
    service_id: Optional[str] = None
    reason: Optional[str] = None
    new_key: Optional[str] = None  # base64-encoded, for key_rotation events

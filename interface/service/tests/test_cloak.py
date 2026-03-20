"""Tests for Cloak client: registration, SSE events, halt handling."""

import asyncio
import base64
import json

import pytest

from cloak.client import CloakState, _handle_sse_event, register_with_cloak


# ---------------------------------------------------------------------------
# SSE event handling
# ---------------------------------------------------------------------------

class TestSSEEventHandling:
    def test_halt_event(self):
        state = CloakState()
        assert state.halted is False
        _handle_sse_event(state, json.dumps({
            "type": "halt",
            "service_id": "episteme",
            "reason": "operator-shutdown",
        }))
        assert state.halted is True
        assert state.halt_reason == "operator-shutdown"

    def test_halt_event_default_reason(self):
        state = CloakState()
        _handle_sse_event(state, json.dumps({
            "type": "halt",
            "service_id": "episteme",
        }))
        assert state.halted is True
        assert state.halt_reason == "operator"

    def test_key_rotation_event(self):
        state = CloakState()
        old_key = b"old-key"
        state.signing_key = old_key
        new_key = b"new-signing-key-for-rotation"
        new_key_b64 = base64.b64encode(new_key).decode()
        _handle_sse_event(state, json.dumps({
            "type": "key_rotation",
            "new_key": new_key_b64,
        }))
        assert state.signing_key == new_key
        assert state.signing_key != old_key

    def test_key_rotation_missing_key(self):
        state = CloakState()
        original_key = b"original"
        state.signing_key = original_key
        _handle_sse_event(state, json.dumps({
            "type": "key_rotation",
        }))
        # Key should be unchanged
        assert state.signing_key == original_key

    def test_unknown_event_type(self):
        state = CloakState()
        _handle_sse_event(state, json.dumps({
            "type": "unknown_event",
        }))
        assert state.halted is False

    def test_malformed_json(self):
        state = CloakState()
        _handle_sse_event(state, "not valid json{{{")
        assert state.halted is False

    def test_empty_event(self):
        state = CloakState()
        _handle_sse_event(state, "")
        assert state.halted is False


# ---------------------------------------------------------------------------
# Registration (CLOAK_DISABLED mode)
# ---------------------------------------------------------------------------

class TestRegistrationDisabled:
    @pytest.mark.asyncio
    async def test_register_disabled(self):
        """When CLOAK_DISABLED=true, registration succeeds immediately."""
        state = CloakState()
        result = await register_with_cloak(state)
        assert result == ""
        assert state.registered is True
        assert state.session_id == "dev-session"


# ---------------------------------------------------------------------------
# CloakState
# ---------------------------------------------------------------------------

class TestCloakState:
    def test_defaults(self):
        state = CloakState()
        assert state.session_id is None
        assert state.signing_key is None
        assert state.halted is False
        assert state.halt_reason is None
        assert state.registered is False
        assert state.start_time > 0

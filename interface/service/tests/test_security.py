"""Tests for security: path traversal, authentication, authorization, halt state."""

from conftest import SIGNING_KEY, auth_header, make_token


# ---------------------------------------------------------------------------
# Path traversal prevention
# ---------------------------------------------------------------------------

class TestPathTraversal:
    def test_tree_traversal(self, client):
        r = client.get("/api/v1/framework/tree", params={"path": "../../etc"})
        assert r.status_code == 403

    def test_file_traversal(self, client):
        r = client.get("/api/v1/framework/file", params={"path": "../../etc/passwd"})
        assert r.status_code == 403

    def test_file_traversal_encoded(self, client):
        r = client.get("/api/v1/framework/file", params={"path": "agent-docs/../../etc/passwd"})
        assert r.status_code == 403

    def test_metadata_traversal(self, client):
        # Metadata GET with traversal path — should return 404 (not found)
        # since it looks up in DB, not filesystem. But the upsert should
        # not allow storing metadata for paths outside the framework.
        r = client.get("/api/v1/framework/metadata", params={"path": "../../etc/passwd"})
        assert r.status_code == 404


# ---------------------------------------------------------------------------
# Token authentication
# ---------------------------------------------------------------------------

class TestTokenAuth:
    def test_missing_token(self, authed_app):
        client, _, _ = authed_app
        r = client.get("/api/v1/framework/tree")
        assert r.status_code == 401
        assert r.json()["error"] == "missing_token"

    def test_valid_token_read(self, authed_app):
        client, _, _ = authed_app
        r = client.get("/api/v1/framework/tree", headers=auth_header("read"))
        assert r.status_code == 200

    def test_invalid_signature(self, authed_app):
        client, _, _ = authed_app
        r = client.get(
            "/api/v1/framework/tree",
            headers={"Authorization": "Bearer payload.invalidsignature"},
        )
        assert r.status_code == 401
        assert r.json()["error"] == "invalid_signature"

    def test_malformed_token(self, authed_app):
        client, _, _ = authed_app
        r = client.get(
            "/api/v1/framework/tree",
            headers={"Authorization": "Bearer no-dot-in-this-token"},
        )
        assert r.status_code == 401
        assert r.json()["error"] == "malformed_token"

    def test_token_wrong_service(self, authed_app):
        client, _, _ = authed_app
        token = make_token(service="cerebro")
        r = client.get(
            "/api/v1/framework/tree",
            headers={"Authorization": f"Bearer {token}"},
        )
        assert r.status_code == 403
        assert r.json()["error"] == "service_not_in_scope"

    def test_health_no_auth_required(self, authed_app):
        client, _, _ = authed_app
        r = client.get("/health")
        assert r.status_code == 200

    def test_no_signing_key(self, authed_app):
        import main
        client, _, _ = authed_app
        # Temporarily remove signing key
        original_key = main.app.state.cloak.signing_key
        main.app.state.cloak.signing_key = None
        r = client.get(
            "/api/v1/framework/tree",
            headers=auth_header("read"),
        )
        assert r.status_code == 503
        assert r.json()["error"] == "no_signing_key"
        main.app.state.cloak.signing_key = original_key


# ---------------------------------------------------------------------------
# Operation class enforcement
# ---------------------------------------------------------------------------

class TestOperationClass:
    def test_read_can_read(self, authed_app):
        client, _, _ = authed_app
        r = client.get("/api/v1/framework/tree", headers=auth_header("read"))
        assert r.status_code == 200

    def test_read_cannot_write(self, authed_app):
        client, _, _ = authed_app
        r = client.post(
            "/api/v1/framework/metadata",
            json={"path": "test.md", "title": "Test"},
            headers=auth_header("read"),
        )
        assert r.status_code == 403
        assert r.json()["error"] == "insufficient_operation_class"

    def test_write_can_write(self, authed_app):
        client, _, _ = authed_app
        r = client.post(
            "/api/v1/framework/metadata",
            json={"path": "test.md", "title": "Test"},
            headers=auth_header("write"),
        )
        assert r.status_code == 200

    def test_write_cannot_admin(self, authed_app):
        client, _, _ = authed_app
        r = client.post("/api/v1/framework/reindex", headers=auth_header("write"))
        assert r.status_code == 403

    def test_admin_can_reindex(self, authed_app):
        client, _, _ = authed_app
        r = client.post("/api/v1/framework/reindex", headers=auth_header("admin"))
        assert r.status_code == 200

    def test_admin_can_do_everything(self, authed_app):
        client, _, _ = authed_app
        headers = auth_header("admin")
        # Read
        r = client.get("/api/v1/framework/tree", headers=headers)
        assert r.status_code == 200
        # Write
        r = client.post(
            "/api/v1/framework/metadata",
            json={"path": "test.md", "title": "Test"},
            headers=headers,
        )
        assert r.status_code == 200
        # Admin
        r = client.post("/api/v1/framework/reindex", headers=headers)
        assert r.status_code == 200


# ---------------------------------------------------------------------------
# Halted state
# ---------------------------------------------------------------------------

class TestHaltState:
    def test_halted_rejects_authed_requests(self, authed_app):
        import main
        client, _, _ = authed_app
        main.app.state.cloak.halted = True
        main.app.state.cloak.halt_reason = "test-halt"
        r = client.get(
            "/api/v1/framework/tree",
            headers=auth_header("admin"),
        )
        assert r.status_code == 503
        assert r.json()["error"] == "service_halted"
        # Restore
        main.app.state.cloak.halted = False
        main.app.state.cloak.halt_reason = None

    def test_health_still_works_when_halted(self, authed_app):
        import main
        client, _, _ = authed_app
        main.app.state.cloak.halted = True
        r = client.get("/health")
        assert r.status_code == 200
        assert r.json()["status"] == "halted"
        main.app.state.cloak.halted = False

"""Tests for all API endpoints — happy paths and error cases."""

from sqlmodel import Session

from models import FileMetadata


# ---------------------------------------------------------------------------
# Health
# ---------------------------------------------------------------------------

class TestHealth:
    def test_healthy(self, client):
        r = client.get("/health")
        assert r.status_code == 200
        data = r.json()
        assert data["status"] == "healthy"
        assert data["service_id"] == "episteme"
        assert data["halted"] is False
        assert data["framework_root_exists"] is True
        assert "uptime_seconds" in data

    def test_halted(self, test_app):
        client, _, _ = test_app
        import main
        main.app.state.cloak.halted = True
        main.app.state.cloak.halt_reason = "operator"
        r = client.get("/health")
        assert r.status_code == 200
        data = r.json()
        assert data["status"] == "halted"
        assert data["halted"] is True
        assert data["halt_reason"] == "operator"
        # Restore
        main.app.state.cloak.halted = False
        main.app.state.cloak.halt_reason = None

    def test_degraded_missing_framework(self, test_app):
        client, _, fw_dir = test_app
        import helpers
        original = helpers.FRAMEWORK_ROOT
        helpers.FRAMEWORK_ROOT = fw_dir / "nonexistent"
        r = client.get("/health")
        assert r.status_code == 200
        assert r.json()["status"] == "degraded"
        helpers.FRAMEWORK_ROOT = original


# ---------------------------------------------------------------------------
# Tree
# ---------------------------------------------------------------------------

class TestTree:
    def test_root_tree(self, client):
        r = client.get("/api/v1/framework/tree")
        assert r.status_code == 200
        data = r.json()
        names = [n["name"] for n in data]
        # Dirs come first, then files, hidden excluded
        assert "agent-docs" in names
        assert "my-skills" in names
        assert "overview.md" in names
        assert ".hidden-dir" not in names
        assert ".hidden-file" not in names

    def test_subdirectory(self, client):
        r = client.get("/api/v1/framework/tree", params={"path": "agent-docs"})
        assert r.status_code == 200
        names = [n["name"] for n in r.json()]
        assert "meta-agent.md" in names
        assert "README.md" in names

    def test_tree_not_found(self, client):
        r = client.get("/api/v1/framework/tree", params={"path": "nonexistent"})
        assert r.status_code == 404

    def test_tree_on_file(self, client):
        r = client.get("/api/v1/framework/tree", params={"path": "overview.md"})
        assert r.status_code == 400

    def test_node_types(self, client):
        r = client.get("/api/v1/framework/tree")
        data = r.json()
        dirs = [n for n in data if n["type"] == "dir"]
        files = [n for n in data if n["type"] == "file"]
        assert len(dirs) >= 2
        assert len(files) >= 1
        for f in files:
            assert f["size"] > 0
            assert f["modified_at"] > 0


# ---------------------------------------------------------------------------
# File
# ---------------------------------------------------------------------------

class TestFile:
    def test_read_file(self, client):
        r = client.get("/api/v1/framework/file", params={"path": "overview.md"})
        assert r.status_code == 200
        data = r.json()
        assert data["type"] == "file"
        assert "Episteme is a knowledge framework" in data["content"]
        assert data["size"] > 0
        assert data["path"] == "overview.md"

    def test_read_nested_file(self, client):
        r = client.get("/api/v1/framework/file", params={"path": "agent-docs/meta-agent.md"})
        assert r.status_code == 200
        assert "meta-agent document" in r.json()["content"]

    def test_file_not_found(self, client):
        r = client.get("/api/v1/framework/file", params={"path": "nonexistent.md"})
        assert r.status_code == 404

    def test_file_is_directory(self, client):
        r = client.get("/api/v1/framework/file", params={"path": "agent-docs"})
        assert r.status_code == 400

    def test_binary_file(self, client):
        r = client.get("/api/v1/framework/file", params={"path": "binary.bin"})
        assert r.status_code == 200
        assert "binary file content not renderable" in r.json()["content"]

    def test_file_with_metadata(self, test_app):
        client, engine, _ = test_app
        with Session(engine) as session:
            meta = FileMetadata(
                path="overview.md",
                title="Overview Doc",
                tags=["core", "intro"],
                category="documentation",
            )
            session.add(meta)
            session.commit()
        r = client.get("/api/v1/framework/file", params={"path": "overview.md"})
        assert r.status_code == 200
        data = r.json()
        assert data["metadata"] is not None
        assert data["metadata"]["title"] == "Overview Doc"
        assert data["metadata"]["tags"] == ["core", "intro"]

    def test_file_strips_slashes(self, client):
        r = client.get("/api/v1/framework/file", params={"path": "/overview.md/"})
        assert r.status_code == 200
        assert r.json()["path"] == "overview.md"


# ---------------------------------------------------------------------------
# Metadata CRUD
# ---------------------------------------------------------------------------

class TestMetadata:
    def test_get_metadata_not_found(self, client):
        r = client.get("/api/v1/framework/metadata", params={"path": "overview.md"})
        assert r.status_code == 404

    def test_upsert_and_get_metadata(self, client):
        # Create
        r = client.post(
            "/api/v1/framework/metadata",
            json={"path": "overview.md", "title": "Overview", "tags": ["core"]},
        )
        assert r.status_code == 200
        assert r.json()["status"] == "ok"

        # Read back
        r = client.get("/api/v1/framework/metadata", params={"path": "overview.md"})
        assert r.status_code == 200
        data = r.json()
        assert data["title"] == "Overview"
        assert data["tags"] == ["core"]

    def test_upsert_partial_update(self, client):
        # Create
        client.post(
            "/api/v1/framework/metadata",
            json={"path": "overview.md", "title": "Original", "category": "docs"},
        )
        # Partial update — only change title
        client.post(
            "/api/v1/framework/metadata",
            json={"path": "overview.md", "title": "Updated"},
        )
        r = client.get("/api/v1/framework/metadata", params={"path": "overview.md"})
        data = r.json()
        assert data["title"] == "Updated"
        assert data["category"] == "docs"  # unchanged

    def test_upsert_with_all_fields(self, client):
        r = client.post(
            "/api/v1/framework/metadata",
            json={
                "path": "my-skills/skill-one.md",
                "title": "Skill One",
                "description": "A Python skill",
                "tags": ["python", "skill"],
                "category": "skills",
            },
        )
        assert r.status_code == 200
        r = client.get("/api/v1/framework/metadata", params={"path": "my-skills/skill-one.md"})
        data = r.json()
        assert data["title"] == "Skill One"
        assert data["description"] == "A Python skill"
        assert data["tags"] == ["python", "skill"]
        assert data["category"] == "skills"
        assert data["updated_at"] is not None


# ---------------------------------------------------------------------------
# Reindex
# ---------------------------------------------------------------------------

class TestReindex:
    def test_reindex(self, client):
        r = client.post("/api/v1/framework/reindex")
        assert r.status_code == 200
        data = r.json()
        assert data["status"] == "ok"
        assert data["count"] >= 4  # overview.md + 2 agent-docs + 2 skills + binary


# ---------------------------------------------------------------------------
# Agent query
# ---------------------------------------------------------------------------

class TestAgentQuery:
    def test_agent_query(self, client):
        r = client.post(
            "/api/v1/framework/agent/query",
            json={"query": "python"},
        )
        assert r.status_code == 200
        data = r.json()
        assert "results" in data
        assert len(data["results"]) > 0

    def test_agent_query_with_scope(self, client):
        r = client.post(
            "/api/v1/framework/agent/query",
            json={"query": "skill", "scope": "my-skills"},
        )
        assert r.status_code == 200
        results = r.json()["results"]
        for result in results:
            assert result["path"].startswith("my-skills")

    def test_agent_query_no_results(self, client):
        r = client.post(
            "/api/v1/framework/agent/query",
            json={"query": "zzzznonexistentzzzz"},
        )
        assert r.status_code == 200
        assert r.json()["results"] == []

    def test_agent_query_max_results(self, client):
        r = client.post(
            "/api/v1/framework/agent/query",
            json={"query": "skill", "max_results": 1},
        )
        assert r.status_code == 200
        assert len(r.json()["results"]) <= 1


# ---------------------------------------------------------------------------
# Error response format
# ---------------------------------------------------------------------------

class TestErrorFormat:
    def test_404_structured(self, client):
        r = client.get("/api/v1/framework/file", params={"path": "no-such-file.md"})
        assert r.status_code == 404
        data = r.json()
        assert data["service"] == "episteme"
        assert data["status_code"] == 404
        assert "error" in data
        assert "detail" in data

    def test_400_structured(self, client):
        r = client.get("/api/v1/framework/file", params={"path": "agent-docs"})
        assert r.status_code == 400
        data = r.json()
        assert data["service"] == "episteme"


# ---------------------------------------------------------------------------
# OpenAPI
# ---------------------------------------------------------------------------

class TestOpenAPI:
    def test_openapi_has_operation_ids(self, client):
        r = client.get("/openapi.json")
        assert r.status_code == 200
        spec = r.json()
        operation_ids = set()
        for path_obj in spec["paths"].values():
            for method_obj in path_obj.values():
                if "operationId" in method_obj:
                    operation_ids.add(method_obj["operationId"])
        expected = {
            "episteme_list_tree",
            "episteme_read_file",
            "episteme_search",
            "episteme_get_metadata",
            "episteme_upsert_metadata",
            "episteme_reindex",
            "episteme_agent_query",
            "episteme_health",
        }
        assert expected.issubset(operation_ids)

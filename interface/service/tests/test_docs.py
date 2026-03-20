"""Tests for the docs domain router (agent-docs, project-documentation, config-files)."""


class TestAgentDocs:
    def test_list_agent_docs(self, client):
        r = client.get("/api/v1/framework/docs/agent")
        assert r.status_code == 200
        docs = r.json()
        names = [d["name"] for d in docs]
        assert "meta-agent.md" in names
        assert "README.md" in names
        for doc in docs:
            assert doc["section"] == "agent"

    def test_get_agent_doc(self, client):
        r = client.get("/api/v1/framework/docs/agent/meta-agent.md")
        assert r.status_code == 200
        assert "Meta Agent" in r.json()["content"]

    def test_get_nonexistent_agent_doc(self, client):
        r = client.get("/api/v1/framework/docs/agent/nope.md")
        assert r.status_code == 404


class TestProjectDocs:
    def test_list_project_docs(self, client):
        r = client.get("/api/v1/framework/docs/project")
        assert r.status_code == 200
        docs = r.json()
        assert len(docs) > 0
        for doc in docs:
            assert doc["section"] == "project"

    def test_get_project_doc(self, client):
        r = client.get("/api/v1/framework/docs/project/README.temp.md")
        assert r.status_code == 200
        assert "Project Docs" in r.json()["content"]


class TestConfigFiles:
    def test_list_configs(self, client):
        r = client.get("/api/v1/framework/docs/config")
        assert r.status_code == 200
        docs = r.json()
        assert len(docs) > 0
        for doc in docs:
            assert doc["section"] == "config"

    def test_get_config(self, client):
        r = client.get("/api/v1/framework/docs/config/project-wide/settings.md")
        assert r.status_code == 200
        assert "Settings" in r.json()["content"]

    def test_get_nonexistent_config(self, client):
        r = client.get("/api/v1/framework/docs/config/nope.md")
        assert r.status_code == 404

"""Tests for the skills domain router."""


class TestListSkills:
    def test_list_skills(self, client):
        r = client.get("/api/v1/framework/skills/")
        assert r.status_code == 200
        skills = r.json()
        names = [s["name"] for s in skills]
        assert "test-skill" in names
        assert "another-skill" in names

    def test_skill_has_trigger(self, client):
        r = client.get("/api/v1/framework/skills/")
        skills = r.json()
        test_skill = next(s for s in skills if s["name"] == "test-skill")
        assert test_skill["trigger"] is not None
        assert "tests" in test_skill["trigger"].lower()


class TestGetSkill:
    def test_get_skill(self, client):
        r = client.get("/api/v1/framework/skills/TEST_SKILL")
        assert r.status_code == 200
        data = r.json()
        assert data["name"] == "test-skill"
        assert data["folder"] == "TEST_SKILL"
        assert "metadata" in data
        assert data["metadata"]["name"] == "test-skill"
        assert "description" in data["metadata"]
        assert len(data["body"]) > 0
        assert len(data["raw"]) > 0

    def test_get_nonexistent_skill(self, client):
        r = client.get("/api/v1/framework/skills/DOES_NOT_EXIST")
        assert r.status_code == 404


class TestSkillTree:
    def test_skill_tree(self, client):
        r = client.get("/api/v1/framework/skills/TEST_SKILL/tree")
        assert r.status_code == 200
        names = [n["name"] for n in r.json()]
        assert "SKILL.md" in names
        assert "extra-file.md" in names

    def test_skill_tree_nonexistent(self, client):
        r = client.get("/api/v1/framework/skills/NOPE/tree")
        assert r.status_code == 404


class TestSkillSearch:
    def test_search_by_name(self, client):
        r = client.get("/api/v1/framework/skills/search", params={"query": "test"})
        assert r.status_code == 200
        results = r.json()
        assert len(results) > 0
        folders = [res["name"] for res in results]
        assert "TEST_SKILL" in folders

    def test_search_by_content(self, client):
        r = client.get("/api/v1/framework/skills/search", params={"query": "unit testing"})
        assert r.status_code == 200
        assert len(r.json()) > 0

    def test_search_no_results(self, client):
        r = client.get("/api/v1/framework/skills/search", params={"query": "zzzznonexistent"})
        assert r.status_code == 200
        assert r.json() == []


class TestSkillDefinition:
    def test_get_definition(self, client):
        r = client.get("/api/v1/framework/skills/definition")
        assert r.status_code == 200
        assert "Skill Definition" in r.json()["content"]


class TestSkillsIndex:
    def test_get_index(self, client):
        r = client.get("/api/v1/framework/skills/index")
        assert r.status_code == 200
        assert "Skills Index" in r.json()["content"]

"""Tests for the projects domain router."""


class TestListProjects:
    def test_list_projects(self, client):
        r = client.get("/api/v1/framework/projects/")
        assert r.status_code == 200
        projects = r.json()
        slugs = [p["slug"] for p in projects]
        assert "test-project" in slugs

    def test_project_has_files(self, client):
        r = client.get("/api/v1/framework/projects/")
        projects = r.json()
        test_proj = next(p for p in projects if p["slug"] == "test-project")
        assert test_proj["file_count"] == 2
        assert "000-project-brief.md" in test_proj["files"]


class TestGetProject:
    def test_get_project(self, client):
        r = client.get("/api/v1/framework/projects/test-project")
        assert r.status_code == 200
        names = [n["name"] for n in r.json()]
        assert "000-project-brief.md" in names
        assert "001-planning.md" in names

    def test_get_nonexistent_project(self, client):
        r = client.get("/api/v1/framework/projects/no-such-project")
        assert r.status_code == 404


class TestGetProjectFile:
    def test_read_project_file(self, client):
        r = client.get("/api/v1/framework/projects/test-project/000-project-brief.md")
        assert r.status_code == 200
        assert "Test Project Brief" in r.json()["content"]

    def test_read_nonexistent_file(self, client):
        r = client.get("/api/v1/framework/projects/test-project/nope.md")
        assert r.status_code == 404


class TestPhases:
    def test_list_phases(self, client):
        r = client.get("/api/v1/framework/projects/phases")
        assert r.status_code == 200
        names = [n["name"] for n in r.json()]
        assert "schema.md" in names


class TestExampleProject:
    def test_example_project(self, client):
        r = client.get("/api/v1/framework/projects/example")
        assert r.status_code == 200
        names = [n["name"] for n in r.json()]
        assert "000-example.md" in names


class TestProjectSearch:
    def test_search_projects(self, client):
        r = client.get("/api/v1/framework/projects/search", params={"query": "planning"})
        assert r.status_code == 200
        results = r.json()
        assert len(results) > 0
        assert any("planning" in res["path"].lower() or
                    (res["snippet"] and "planning" in res["snippet"].lower())
                    for res in results)

    def test_search_no_results(self, client):
        r = client.get("/api/v1/framework/projects/search", params={"query": "zzzznonexistent"})
        assert r.status_code == 200
        assert r.json() == []

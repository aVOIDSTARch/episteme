"""Tests for the guides domain router."""


class TestListCategories:
    def test_list_categories(self, client):
        r = client.get("/api/v1/framework/guides/")
        assert r.status_code == 200
        categories = r.json()
        names = [c["category"] for c in categories]
        assert "test-category" in names
        assert "another-category" in names

    def test_category_has_count(self, client):
        r = client.get("/api/v1/framework/guides/")
        categories = r.json()
        test_cat = next(c for c in categories if c["category"] == "test-category")
        assert test_cat["guide_count"] == 2


class TestListByCategory:
    def test_list_guides(self, client):
        r = client.get("/api/v1/framework/guides/category/test-category")
        assert r.status_code == 200
        guides = r.json()
        names = [g["name"] for g in guides]
        assert "python-guide.ai" in names
        assert "typescript-guide.ai" in names

    def test_nonexistent_category(self, client):
        r = client.get("/api/v1/framework/guides/category/no-such-category")
        assert r.status_code == 404


class TestGetGuide:
    def test_read_guide(self, client):
        r = client.get("/api/v1/framework/guides/category/test-category/python-guide.ai")
        assert r.status_code == 200
        assert "snake_case" in r.json()["content"]

    def test_read_nonexistent_guide(self, client):
        r = client.get("/api/v1/framework/guides/category/test-category/nope.ai")
        assert r.status_code == 404


class TestPersonalized:
    def test_list_personalized(self, client):
        r = client.get("/api/v1/framework/guides/personalized")
        assert r.status_code == 200
        guides = r.json()
        assert len(guides) > 0
        assert any(g["name"] == "markdown.ai" for g in guides)

    def test_get_personalized(self, client):
        r = client.get("/api/v1/framework/guides/personalized/markdown/markdown.ai")
        assert r.status_code == 200
        assert "Custom rules" in r.json()["content"]


class TestGuideSources:
    def test_get_sources(self, client):
        r = client.get("/api/v1/framework/guides/sources")
        assert r.status_code == 200
        assert "Guide Sources" in r.json()["content"]


class TestGuideSearch:
    def test_search_guides(self, client):
        r = client.get("/api/v1/framework/guides/search", params={"query": "snake_case"})
        assert r.status_code == 200
        results = r.json()
        assert len(results) > 0

    def test_search_no_results(self, client):
        r = client.get("/api/v1/framework/guides/search", params={"query": "zzzznonexistent"})
        assert r.status_code == 200
        assert r.json() == []

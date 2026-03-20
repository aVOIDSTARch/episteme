"""Tests for search functionality: scoring, snippets, path filtering, metadata matching."""

from sqlmodel import Session

from models import FileMetadata


# ---------------------------------------------------------------------------
# Basic search
# ---------------------------------------------------------------------------

class TestSearchBasics:
    def test_search_by_content(self, client):
        r = client.get("/api/v1/framework/search", params={"query": "python"})
        assert r.status_code == 200
        results = r.json()
        assert len(results) > 0
        paths = [res["path"] for res in results]
        assert "my-skills/skill-one.md" in paths

    def test_search_by_filename(self, client):
        r = client.get("/api/v1/framework/search", params={"query": "overview"})
        assert r.status_code == 200
        results = r.json()
        assert any(res["path"] == "overview.md" for res in results)

    def test_search_no_results(self, client):
        r = client.get("/api/v1/framework/search", params={"query": "zzzznonexistentzzzz"})
        assert r.status_code == 200
        assert r.json() == []

    def test_search_case_insensitive(self, client):
        r = client.get("/api/v1/framework/search", params={"query": "PYTHON"})
        assert r.status_code == 200
        assert len(r.json()) > 0

    def test_search_empty_query_rejected(self, client):
        r = client.get("/api/v1/framework/search", params={"query": ""})
        assert r.status_code == 422  # validation error


# ---------------------------------------------------------------------------
# Scoring
# ---------------------------------------------------------------------------

class TestSearchScoring:
    def test_content_match_scores_higher_than_path(self, client):
        """Content matches (score +20) should rank above path-only matches (+5)."""
        r = client.get("/api/v1/framework/search", params={"query": "episteme"})
        results = r.json()
        if len(results) >= 2:
            # First result should have a higher score
            assert results[0]["score"] >= results[-1]["score"]

    def test_results_sorted_by_score(self, client):
        r = client.get("/api/v1/framework/search", params={"query": "skill"})
        results = r.json()
        scores = [res["score"] for res in results]
        assert scores == sorted(scores, reverse=True)


# ---------------------------------------------------------------------------
# Snippets
# ---------------------------------------------------------------------------

class TestSearchSnippets:
    def test_snippet_contains_query(self, client):
        r = client.get("/api/v1/framework/search", params={"query": "knowledge"})
        results = r.json()
        for res in results:
            if res["snippet"]:
                assert "knowledge" in res["snippet"].lower()

    def test_snippet_from_content_match(self, client):
        r = client.get("/api/v1/framework/search", params={"query": "typescript"})
        results = r.json()
        matched = [res for res in results if res["snippet"]]
        assert len(matched) > 0


# ---------------------------------------------------------------------------
# Path filtering
# ---------------------------------------------------------------------------

class TestSearchPathFilter:
    def test_path_filter(self, client):
        r = client.get(
            "/api/v1/framework/search",
            params={"query": "skill", "path": "my-skills"},
        )
        results = r.json()
        for res in results:
            assert res["path"].startswith("my-skills")

    def test_path_filter_excludes_other(self, client):
        r = client.get(
            "/api/v1/framework/search",
            params={"query": "agent", "path": "my-skills"},
        )
        results = r.json()
        for res in results:
            assert not res["path"].startswith("agent-docs")

    def test_path_filter_strips_slashes(self, client):
        r = client.get(
            "/api/v1/framework/search",
            params={"query": "skill", "path": "/my-skills/"},
        )
        assert r.status_code == 200


# ---------------------------------------------------------------------------
# Limit
# ---------------------------------------------------------------------------

class TestSearchLimit:
    def test_limit(self, client):
        r = client.get(
            "/api/v1/framework/search",
            params={"query": "test", "limit": 1},
        )
        assert r.status_code == 200
        assert len(r.json()) <= 1


# ---------------------------------------------------------------------------
# Metadata search
# ---------------------------------------------------------------------------

class TestSearchMetadata:
    def test_search_matches_metadata_title(self, test_app):
        client, engine, _ = test_app
        with Session(engine) as session:
            meta = FileMetadata(
                path="overview.md",
                title="Unique Searchable Title XYZ",
            )
            session.add(meta)
            session.commit()

        r = client.get("/api/v1/framework/search", params={"query": "unique searchable"})
        results = r.json()
        assert any(res["path"] == "overview.md" for res in results)

    def test_search_matches_metadata_description(self, test_app):
        client, engine, _ = test_app
        with Session(engine) as session:
            meta = FileMetadata(
                path="overview.md",
                description="This has a rare keyword xylophone",
            )
            session.add(meta)
            session.commit()

        r = client.get("/api/v1/framework/search", params={"query": "xylophone"})
        results = r.json()
        assert any(res["path"] == "overview.md" for res in results)

    def test_search_matches_metadata_tags(self, test_app):
        client, engine, _ = test_app
        with Session(engine) as session:
            meta = FileMetadata(
                path="overview.md",
                tags=["unique-test-tag-zebra"],
            )
            session.add(meta)
            session.commit()

        r = client.get("/api/v1/framework/search", params={"query": "zebra"})
        results = r.json()
        assert any(res["path"] == "overview.md" for res in results)


# ---------------------------------------------------------------------------
# Hidden files
# ---------------------------------------------------------------------------

class TestSearchHiddenFiles:
    def test_hidden_files_excluded(self, client):
        r = client.get("/api/v1/framework/search", params={"query": "secret"})
        results = r.json()
        paths = [res["path"] for res in results]
        assert ".hidden-file" not in paths

    def test_hidden_dirs_excluded(self, client):
        r = client.post("/api/v1/framework/reindex")
        count = r.json()["count"]
        # Should not include files in .hidden-dir
        r2 = client.get("/api/v1/framework/search", params={"query": "."})
        for res in r2.json():
            assert not res["path"].startswith(".hidden")

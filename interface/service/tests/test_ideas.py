"""Tests for the ideas domain router."""

import pytest


class TestListTopics:
    def test_list_topics(self, client, ideas_dir):
        r = client.get("/api/v1/framework/ideas/topics")
        assert r.status_code == 200
        topics = r.json()
        names = [t["name"] for t in topics]
        assert "test-topic" in names
        assert "empty-topic" in names

    def test_list_topics_empty(self, client, tmp_path, test_app):
        """When ideas dir doesn't exist, returns empty list."""
        import config as config_module
        original = config_module.IDEAS_ROOT
        config_module.IDEAS_ROOT = tmp_path / "no-ideas"
        r = client.get("/api/v1/framework/ideas/topics")
        assert r.status_code == 200
        assert r.json() == []
        config_module.IDEAS_ROOT = original


class TestGetTopic:
    def test_get_topic(self, client, ideas_dir):
        r = client.get("/api/v1/framework/ideas/topics/test-topic")
        assert r.status_code == 200
        data = r.json()
        assert "test-topic" in data["content"]

    def test_get_nonexistent_topic(self, client, ideas_dir):
        r = client.get("/api/v1/framework/ideas/topics/nope")
        assert r.status_code == 404


class TestAddIdea:
    def test_add_idea(self, client, ideas_dir):
        r = client.post(
            "/api/v1/framework/ideas/topics/test-topic",
            json={"body": "This is a new idea for testing."},
        )
        assert r.status_code == 200
        assert r.json()["status"] == "ok"

        # Verify content was appended
        content = (ideas_dir / "test-topic.md").read_text()
        assert "This is a new idea for testing." in content
        assert "Added:" in content

    def test_add_idea_nonexistent_topic(self, client, ideas_dir):
        r = client.post(
            "/api/v1/framework/ideas/topics/nonexistent",
            json={"body": "Should fail."},
        )
        assert r.status_code == 404


class TestCreateTopic:
    def test_create_topic(self, client, ideas_dir):
        r = client.post(
            "/api/v1/framework/ideas/topics",
            json={"name": "new-topic"},
        )
        assert r.status_code == 200
        assert r.json()["status"] == "ok"
        assert (ideas_dir / "new-topic.md").exists()
        content = (ideas_dir / "new-topic.md").read_text()
        assert "new-topic" in content

    def test_create_duplicate_topic(self, client, ideas_dir):
        r = client.post(
            "/api/v1/framework/ideas/topics",
            json={"name": "test-topic"},
        )
        assert r.status_code == 409

    def test_create_topic_traversal(self, client, ideas_dir):
        r = client.post(
            "/api/v1/framework/ideas/topics",
            json={"name": "../escape"},
        )
        # Should be sanitized (slashes replaced) or blocked
        assert r.status_code in (200, 403)


class TestIdeasSchema:
    def test_get_schema(self, client):
        r = client.get("/api/v1/framework/ideas/schema")
        assert r.status_code == 200
        assert "Idea File Schema" in r.json()["content"]

    def test_get_instructions(self, client):
        r = client.get("/api/v1/framework/ideas/instructions")
        assert r.status_code == 200
        assert "Agent Instructions" in r.json()["content"]

    def test_get_template(self, client):
        r = client.get("/api/v1/framework/ideas/template")
        assert r.status_code == 200
        assert "{{topic-name}}" in r.json()["content"]

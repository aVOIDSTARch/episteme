"""Shared fixtures for the Episteme service test suite.

Sets CLOAK_DISABLED before any service module is imported, creates an
isolated temporary framework directory and in-memory SQLite DB per test.
"""

import base64
import hashlib
import hmac
import json
import os
import sys
import time

# Set env vars BEFORE any service code is imported
os.environ["CLOAK_DISABLED"] = "true"

import pytest
from pathlib import Path

# Ensure the service package is importable
sys.path.insert(0, str(Path(__file__).resolve().parent))

from fastapi.testclient import TestClient
from sqlmodel import Session, SQLModel, create_engine

import helpers
from cloak.client import CloakState


# ---------------------------------------------------------------------------
# Temporary framework directory
# ---------------------------------------------------------------------------

@pytest.fixture()
def framework_dir(tmp_path):
    """Create a small temporary framework directory with known files."""
    root = tmp_path / "episteme-framework"
    root.mkdir()

    # Top-level dirs
    (root / "agent-docs").mkdir()
    (root / "my-skills").mkdir()
    (root / ".hidden-dir").mkdir()

    # Files
    (root / "agent-docs" / "meta-agent.md").write_text(
        "# Meta Agent\nThis is the meta-agent document for testing."
    )
    (root / "agent-docs" / "README.md").write_text(
        "# Agent Docs\nIndex of all agent documentation."
    )
    (root / "my-skills" / "skill-one.md").write_text(
        "# Skill One\nA test skill about Python programming."
    )
    (root / "my-skills" / "skill-two.md").write_text(
        "# Skill Two\nA test skill about TypeScript programming."
    )
    (root / "overview.md").write_text(
        "# Overview\nEpisteme is a knowledge framework."
    )
    # Hidden file (should be excluded)
    (root / ".hidden-file").write_text("secret")
    # Binary file
    (root / "binary.bin").write_bytes(b"\x80\x81\x82\x83")

    # ----- Domain-specific structures for router tests -----

    # Skills (episteme-skills with SKILL.md)
    skills_root = root / "my-skills" / "episteme-skills"
    skills_root.mkdir(parents=True)
    test_skill = skills_root / "TEST_SKILL"
    test_skill.mkdir()
    (test_skill / "SKILL.md").write_text(
        "# TEST_SKILL\n\n"
        "## Name\n\ntest-skill\n\n"
        "## Description\n\nA test skill for unit testing.\n\n"
        "## When to use\n\n- When running tests\n\n"
        "## Instructions\n\n1. Do the test thing.\n\n"
        "## Location\n\n`my-skills/episteme-skills/TEST_SKILL/`\n"
    )
    (test_skill / "extra-file.md").write_text("# Extra\nSupporting file.")
    second_skill = skills_root / "ANOTHER_SKILL"
    second_skill.mkdir()
    (second_skill / "SKILL.md").write_text(
        "# ANOTHER_SKILL\n\n"
        "## Name\n\nanother-skill\n\n"
        "## Description\n\nAnother skill for testing search.\n\n"
        "## When to use\n\n- When you need another skill\n\n"
        "## Instructions\n\n1. Do another thing.\n"
    )
    (root / "my-skills" / "000-my-skills-index.md").write_text(
        "# Skills Index\n\nMaster index of all skills."
    )
    skill_def = root / "my-skills" / "skill-definition"
    skill_def.mkdir()
    (skill_def / "_skill-definition.md").write_text(
        "# Skill Definition Standard\n\nHow to write a SKILL.md."
    )

    # Projects
    projects_dir = root / "projects"
    projects_dir.mkdir()
    test_project = projects_dir / "test-project"
    test_project.mkdir()
    (test_project / "000-project-brief.md").write_text(
        "# Test Project Brief\n\nA test project for unit testing."
    )
    (test_project / "001-planning.md").write_text(
        "# Planning\n\nPlanning document for test project."
    )
    example_project = projects_dir / "example-project"
    example_project.mkdir()
    (example_project / "000-example.md").write_text("# Example\nSample project.")
    tracking = projects_dir / "tracking-system" / "01-project-schemas"
    tracking.mkdir(parents=True)
    (tracking / "schema.md").write_text("# Phase Schema\nProject phase definitions.")

    # Ideas engine
    ideas_engine = root / "ideas-engine"
    ideas_engine.mkdir()
    (ideas_engine / "AGENT-INSTRUCTIONS.md").write_text(
        "# Agent Instructions\n\nHow agents should manage ideas."
    )
    (ideas_engine / "_idea-file-schema.md").write_text(
        "# Idea File Schema\n\nFormat for idea entries."
    )
    (ideas_engine / "template-topic.md").write_text(
        "# {{topic-name}}\n\nIdeas about {{topic-name}}.\n"
    )

    # Language style guides
    guides_dir = root / "language-style-guides"
    guides_dir.mkdir()
    master = guides_dir / "public" / "master"
    master.mkdir(parents=True)
    test_category = master / "test-category"
    test_category.mkdir()
    (test_category / "python-guide.ai").write_text(
        "Python Style Guide\n\nUse snake_case for functions."
    )
    (test_category / "typescript-guide.ai").write_text(
        "TypeScript Style Guide\n\nUse camelCase for functions."
    )
    another_cat = master / "another-category"
    another_cat.mkdir()
    (another_cat / "rust-guide.ai").write_text(
        "Rust Style Guide\n\nUse snake_case everywhere."
    )
    personalized = guides_dir / "personalized"
    personalized.mkdir()
    personal_md = personalized / "markdown"
    personal_md.mkdir()
    (personal_md / "markdown.ai").write_text(
        "Personalized Markdown Guide\n\nCustom rules."
    )
    (guides_dir / "code-guide-sources.md").write_text(
        "# Guide Sources\n\nWhere guides come from."
    )

    # Project documentation
    project_docs = root / "project-documentation"
    project_docs.mkdir()
    (project_docs / "README.temp.md").write_text("# Project Docs\nTemporary readme.")

    # Config files
    config_files = root / "config-files"
    config_files.mkdir()
    project_wide = config_files / "project-wide"
    project_wide.mkdir()
    (project_wide / "settings.md").write_text("# Settings\nProject-wide config.")

    return root


@pytest.fixture()
def ideas_dir(tmp_path, test_app):
    """Create a temporary ideas directory and patch IDEAS_ROOT."""
    import config as config_module

    ideas_root = tmp_path / "ideas"
    ideas_root.mkdir()
    (ideas_root / "test-topic.md").write_text(
        "# test-topic\n\nIdeas about testing.\n"
    )
    (ideas_root / "empty-topic.md").write_text(
        "# empty-topic\n\n"
    )

    original = config_module.IDEAS_ROOT
    config_module.IDEAS_ROOT = ideas_root

    yield ideas_root

    config_module.IDEAS_ROOT = original


# ---------------------------------------------------------------------------
# Test app with isolated DB and framework root
# ---------------------------------------------------------------------------

@pytest.fixture()
def test_app(framework_dir):
    """Create a TestClient with isolated DB and framework root."""
    import main

    # Patch FRAMEWORK_ROOT and engine to use temp dirs
    original_root = helpers.FRAMEWORK_ROOT
    original_engine = main.engine

    test_db_path = framework_dir.parent / "test_metadata.db"
    test_engine = create_engine(f"sqlite:///{test_db_path}", connect_args={"check_same_thread": False})
    SQLModel.metadata.create_all(test_engine)

    helpers.FRAMEWORK_ROOT = framework_dir
    main.engine = test_engine

    # Override the session dependency
    def get_test_session():
        with Session(test_engine) as session:
            yield session

    main.app.dependency_overrides[main.get_session] = get_test_session

    # Set up cloak state for the app
    main.app.state.cloak = CloakState(start_time=time.time())
    main.app.state.cloak.registered = True
    main.app.state.cloak.session_id = "test-session"

    client = TestClient(main.app, raise_server_exceptions=False)

    yield client, test_engine, framework_dir

    # Restore
    helpers.FRAMEWORK_ROOT = original_root
    main.engine = original_engine
    main.app.dependency_overrides.clear()


@pytest.fixture()
def client(test_app):
    """Shorthand for just the test client."""
    return test_app[0]


@pytest.fixture()
def test_engine(test_app):
    """Shorthand for the test DB engine."""
    return test_app[1]


# ---------------------------------------------------------------------------
# Token helpers
# ---------------------------------------------------------------------------

SIGNING_KEY = b"test-signing-key-32-bytes-long!!"


def make_token(
    operation_class: str = "admin",
    service: str = "episteme",
    resources: list | None = None,
    job_id: str = "test-job",
    agent_class: str = "test-agent",
) -> str:
    """Create a valid HMAC-SHA256 signed token for testing."""
    claims = {
        "job_id": job_id,
        "agent_class": agent_class,
        "services": [
            {
                "service": service,
                "operation_class": operation_class,
                "resources": resources or ["*"],
            }
        ],
    }
    payload_b64 = base64.urlsafe_b64encode(json.dumps(claims).encode()).rstrip(b"=").decode()
    signature = hmac.new(SIGNING_KEY, payload_b64.encode(), hashlib.sha256).hexdigest()
    return f"{payload_b64}.{signature}"


def auth_header(operation_class: str = "admin", **kwargs) -> dict:
    """Return an Authorization header dict with a valid token."""
    return {"Authorization": f"Bearer {make_token(operation_class=operation_class, **kwargs)}"}


@pytest.fixture()
def authed_app(test_app):
    """Test app with auth enabled (CLOAK_DISABLED overridden).

    Returns (client, engine, framework_dir, signing_key).
    """
    import main
    from cloak import auth as auth_module

    client_obj, engine, fw_dir = test_app

    # Enable auth by patching the module-level flag
    original_disabled = auth_module.CLOAK_DISABLED
    auth_module.CLOAK_DISABLED = False

    # Set signing key on cloak state
    main.app.state.cloak.signing_key = SIGNING_KEY
    main.app.state.cloak.halted = False

    yield client_obj, engine, fw_dir

    auth_module.CLOAK_DISABLED = original_disabled

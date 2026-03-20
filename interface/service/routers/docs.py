"""Domain router for documentation: agent-docs, project-documentation, config-files."""

from typing import List

from fastapi import APIRouter, Depends, HTTPException

from cloak.auth import verify_token
from cloak.models import TokenClaims
from helpers import is_hidden, list_dir, read_file_contents
import helpers
from schemas import DocFile, FileContent

router = APIRouter(prefix="/api/v1/framework/docs", tags=["docs"])

AGENT_DOCS_DIR = "agent-docs"
PROJECT_DOCS_DIR = "project-documentation"
CONFIG_FILES_DIR = "config-files"


def _doc_files(rel_dir: str, section: str) -> List[DocFile]:
    """List files in a framework subdirectory as DocFile objects."""
    root = helpers.FRAMEWORK_ROOT / rel_dir
    if not root.exists():
        return []
    results = []
    for f in sorted(root.rglob("*")):
        if f.is_dir() or is_hidden(f):
            continue
        stat = f.stat()
        rel_path = f"{rel_dir}/{f.relative_to(root)}"
        results.append(DocFile(
            name=f.name,
            path=rel_path,
            size=stat.st_size,
            modified_at=stat.st_mtime,
            section=section,
        ))
    return results


def _read_doc(rel_path: str) -> FileContent:
    """Read a doc file and return FileContent."""
    try:
        content = read_file_contents(rel_path)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Document not found")
    except IsADirectoryError:
        raise HTTPException(status_code=400, detail="Path is a directory")
    full = helpers.FRAMEWORK_ROOT / rel_path
    return FileContent(
        path=rel_path, content=content, type="file",
        size=full.stat().st_size, metadata=None,
    )


# ---------------------------------------------------------------------------
# Agent docs
# ---------------------------------------------------------------------------

@router.get(
    "/agent",
    response_model=List[DocFile],
    operation_id="episteme_list_agent_docs",
    summary="List agent documents",
    description="Returns all files in the agent-docs/ directory.",
)
def list_agent_docs(_token=Depends(verify_token)):
    return _doc_files(AGENT_DOCS_DIR, "agent")


@router.get(
    "/agent/{filename:path}",
    response_model=FileContent,
    operation_id="episteme_get_agent_doc",
    summary="Read an agent document",
    description="Returns the content of a specific agent documentation file.",
)
def get_agent_doc(filename: str, _token=Depends(verify_token)):
    return _read_doc(f"{AGENT_DOCS_DIR}/{filename}")


# ---------------------------------------------------------------------------
# Project documentation
# ---------------------------------------------------------------------------

@router.get(
    "/project",
    response_model=List[DocFile],
    operation_id="episteme_list_project_docs",
    summary="List project documentation",
    description="Returns all files in the project-documentation/ directory.",
)
def list_project_docs(_token=Depends(verify_token)):
    return _doc_files(PROJECT_DOCS_DIR, "project")


@router.get(
    "/project/{filename:path}",
    response_model=FileContent,
    operation_id="episteme_get_project_doc",
    summary="Read a project document",
    description="Returns the content of a specific project documentation file.",
)
def get_project_doc(filename: str, _token=Depends(verify_token)):
    return _read_doc(f"{PROJECT_DOCS_DIR}/{filename}")


# ---------------------------------------------------------------------------
# Config files
# ---------------------------------------------------------------------------

@router.get(
    "/config",
    response_model=List[DocFile],
    operation_id="episteme_list_configs",
    summary="List configuration files",
    description="Returns all files in the config-files/ directory tree.",
)
def list_configs(_token=Depends(verify_token)):
    return _doc_files(CONFIG_FILES_DIR, "config")


@router.get(
    "/config/{path:path}",
    response_model=FileContent,
    operation_id="episteme_get_config",
    summary="Read a configuration file",
    description="Returns the content of a specific configuration file.",
)
def get_config(path: str, _token=Depends(verify_token)):
    return _read_doc(f"{CONFIG_FILES_DIR}/{path}")

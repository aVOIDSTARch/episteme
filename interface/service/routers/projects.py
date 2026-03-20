"""Domain router for projects (projects/)."""

from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException, Query

from cloak.auth import verify_token
from cloak.models import TokenClaims
from helpers import is_hidden, list_dir, read_file_contents
import helpers
from schemas import FileContent, FileNode, ProjectSummary, SearchResult

router = APIRouter(prefix="/api/v1/framework/projects", tags=["projects"])

PROJECTS_DIR = "projects"


def _projects_root():
    return helpers.FRAMEWORK_ROOT / "projects"


def _list_project_folders() -> List[str]:
    root = _projects_root()
    if not root.exists():
        return []
    return sorted(
        child.name for child in root.iterdir()
        if child.is_dir() and not is_hidden(child)
    )


@router.get(
    "/",
    response_model=List[ProjectSummary],
    operation_id="episteme_list_projects",
    summary="List all projects",
    description="Returns all project folders with their document counts.",
)
def list_projects(_token=Depends(verify_token)):
    results = []
    for slug in _list_project_folders():
        project_path = _projects_root() / slug
        files = sorted(
            f.name for f in project_path.iterdir()
            if f.is_file() and not is_hidden(f)
        )
        results.append(ProjectSummary(slug=slug, files=files, file_count=len(files)))
    return results


@router.get(
    "/search",
    response_model=List[SearchResult],
    operation_id="episteme_search_projects",
    summary="Search project documents",
    description="Full-text search across all project documents.",
)
def search_projects(
    query: str = Query(..., min_length=1),
    limit: int = Query(20),
    _token=Depends(verify_token),
):
    q = query.lower()
    candidates: List[SearchResult] = []
    for slug in _list_project_folders():
        project_path = _projects_root() / slug
        for f in sorted(project_path.rglob("*")):
            if f.is_dir() or is_hidden(f):
                continue
            rel_path = f"{PROJECTS_DIR}/{f.relative_to(_projects_root())}"
            score = 0
            snippet = None
            if q in f.name.lower():
                score += 10
            if q in rel_path.lower():
                score += 5
            try:
                content = read_file_contents(rel_path)
                if q in content.lower():
                    score += 20
                    idx = content.lower().find(q)
                    if idx >= 0:
                        snippet = content[max(0, idx - 40): min(len(content), idx + 120)].replace("\n", " ")
            except Exception:
                pass
            if score > 0:
                candidates.append(SearchResult(
                    path=rel_path, name=f.name, type="file",
                    snippet=snippet, score=float(score),
                ))
    candidates.sort(key=lambda r: r.score, reverse=True)
    return candidates[:limit]


@router.get(
    "/phases",
    response_model=List[FileNode],
    operation_id="episteme_list_phases",
    summary="List phase schemas",
    description="Returns the project phase schema structure from tracking-system/01-project-schemas/.",
)
def list_phases(_token=Depends(verify_token)):
    schemas_dir = f"{PROJECTS_DIR}/tracking-system/01-project-schemas"
    try:
        return list_dir(schemas_dir)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Phase schemas not found")


@router.get(
    "/example",
    response_model=List[FileNode],
    operation_id="episteme_get_example_project",
    summary="List example project files",
    description="Returns the contents of the example-project/ directory.",
)
def get_example_project(_token=Depends(verify_token)):
    example_dir = f"{PROJECTS_DIR}/example-project"
    try:
        return list_dir(example_dir)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Example project not found")


@router.get(
    "/{project_slug}",
    response_model=List[FileNode],
    operation_id="episteme_get_project",
    summary="List project documents",
    description="Returns all documents in a specific project folder.",
)
def get_project(project_slug: str, _token=Depends(verify_token)):
    project_dir = f"{PROJECTS_DIR}/{project_slug}"
    try:
        return list_dir(project_dir)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail=f"Project not found: {project_slug}")


@router.get(
    "/{project_slug}/{filename:path}",
    response_model=FileContent,
    operation_id="episteme_get_project_file",
    summary="Read a project document",
    description="Returns the content of a specific document in a project.",
)
def get_project_file(project_slug: str, filename: str, _token=Depends(verify_token)):
    file_path = f"{PROJECTS_DIR}/{project_slug}/{filename}"
    try:
        content = read_file_contents(file_path)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="File not found")
    except IsADirectoryError:
        raise HTTPException(status_code=400, detail="Path is a directory")
    full_path = helpers.FRAMEWORK_ROOT / file_path
    return FileContent(
        path=file_path, content=content, type="file",
        size=full_path.stat().st_size, metadata=None,
    )

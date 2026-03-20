"""Domain router for ideas (ideas-engine/ schema + ~/ideas/ topic files)."""

from datetime import datetime, timezone
from typing import List

from fastapi import APIRouter, Depends, HTTPException, Query

from cloak.auth import require_operation_class, verify_token
from cloak.models import TokenClaims
from helpers import is_hidden, read_file_contents, safe_resolve
import helpers
from config import IDEAS_ROOT
from schemas import (
    CreateTopicRequest,
    FileContent,
    IdeaEntry,
    SearchResult,
    StatusResponse,
    TopicSummary,
)

router = APIRouter(prefix="/api/v1/framework/ideas", tags=["ideas"])

IDEAS_ENGINE_DIR = "ideas-engine"


def _ideas_root():
    """Return the current IDEAS_ROOT (patchable in tests)."""
    from config import IDEAS_ROOT as _root
    return _root


def _ensure_ideas_dir():
    root = _ideas_root()
    if not root.exists():
        root.mkdir(parents=True, exist_ok=True)


@router.get(
    "/topics",
    response_model=List[TopicSummary],
    operation_id="episteme_list_topics",
    summary="List idea topics",
    description="Returns all topic files in the ideas directory.",
)
def list_topics(_token=Depends(verify_token)):
    root = _ideas_root()
    if not root.exists():
        return []
    topics = []
    for f in sorted(root.iterdir(), key=lambda c: c.name.lower()):
        if f.is_file() and f.suffix == ".md" and not is_hidden(f):
            stat = f.stat()
            topics.append(TopicSummary(
                name=f.stem,
                filename=f.name,
                size=stat.st_size,
                modified_at=stat.st_mtime,
            ))
    return topics


@router.get(
    "/schema",
    response_model=FileContent,
    operation_id="episteme_ideas_schema",
    summary="Get idea file schema",
    description="Returns the _idea-file-schema.md defining the idea entry format.",
)
def get_schema(_token=Depends(verify_token)):
    path = f"{IDEAS_ENGINE_DIR}/_idea-file-schema.md"
    try:
        content = read_file_contents(path)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Idea schema not found")
    full = helpers.FRAMEWORK_ROOT / path
    return FileContent(
        path=path, content=content, type="file",
        size=full.stat().st_size, metadata=None,
    )


@router.get(
    "/instructions",
    response_model=FileContent,
    operation_id="episteme_ideas_instructions",
    summary="Get agent instructions for ideas",
    description="Returns AGENT-INSTRUCTIONS.md with guidance for idea management.",
)
def get_instructions(_token=Depends(verify_token)):
    path = f"{IDEAS_ENGINE_DIR}/AGENT-INSTRUCTIONS.md"
    try:
        content = read_file_contents(path)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Agent instructions not found")
    full = helpers.FRAMEWORK_ROOT / path
    return FileContent(
        path=path, content=content, type="file",
        size=full.stat().st_size, metadata=None,
    )


@router.get(
    "/template",
    response_model=FileContent,
    operation_id="episteme_ideas_template",
    summary="Get topic template",
    description="Returns template-topic.md for creating new topic files.",
)
def get_template(_token=Depends(verify_token)):
    path = f"{IDEAS_ENGINE_DIR}/template-topic.md"
    try:
        content = read_file_contents(path)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Topic template not found")
    full = helpers.FRAMEWORK_ROOT / path
    return FileContent(
        path=path, content=content, type="file",
        size=full.stat().st_size, metadata=None,
    )


@router.post(
    "/topics",
    response_model=StatusResponse,
    operation_id="episteme_create_topic",
    summary="Create a new topic",
    description="Creates a new topic file from the template. Requires write access.",
)
def create_topic(
    req: CreateTopicRequest,
    _token=Depends(require_operation_class("write")),
):
    _ensure_ideas_dir()
    root = _ideas_root()
    # Sanitize name
    safe_name = req.name.strip().replace("/", "-").replace("\\", "-")
    if not safe_name:
        raise HTTPException(status_code=400, detail="Topic name cannot be empty")
    filename = f"{safe_name}.md" if not safe_name.endswith(".md") else safe_name
    target = (root / filename).resolve()
    if not target.is_relative_to(root):
        raise HTTPException(status_code=403, detail="Access denied")
    if target.exists():
        raise HTTPException(status_code=409, detail=f"Topic already exists: {filename}")
    # Try to use template
    template_path = f"{IDEAS_ENGINE_DIR}/template-topic.md"
    try:
        template_content = read_file_contents(template_path)
        content = template_content.replace("{{topic-name}}", safe_name)
    except FileNotFoundError:
        content = f"# {safe_name}\n\n"
    target.write_text(content, encoding="utf-8")
    return StatusResponse(status="ok", path=filename)


@router.get(
    "/topics/{topic_name}",
    response_model=FileContent,
    operation_id="episteme_get_topic",
    summary="Read a topic file",
    description="Returns the full content of an idea topic file.",
)
def get_topic(topic_name: str, _token=Depends(verify_token)):
    root = _ideas_root()
    filename = f"{topic_name}.md" if not topic_name.endswith(".md") else topic_name
    target = (root / filename).resolve()
    if not target.is_relative_to(root):
        raise HTTPException(status_code=403, detail="Access denied")
    if not target.exists():
        raise HTTPException(status_code=404, detail=f"Topic not found: {topic_name}")
    content = target.read_text(encoding="utf-8")
    return FileContent(
        path=f"ideas/{filename}", content=content, type="file",
        size=target.stat().st_size, metadata=None,
    )


@router.post(
    "/topics/{topic_name}",
    response_model=StatusResponse,
    operation_id="episteme_add_idea",
    summary="Add an idea to a topic",
    description="Appends a new idea entry to an existing topic file. Requires write access.",
)
def add_idea(
    topic_name: str,
    entry: IdeaEntry,
    _token=Depends(require_operation_class("write")),
):
    root = _ideas_root()
    filename = f"{topic_name}.md" if not topic_name.endswith(".md") else topic_name
    target = (root / filename).resolve()
    if not target.is_relative_to(root):
        raise HTTPException(status_code=403, detail="Access denied")
    if not target.exists():
        raise HTTPException(status_code=404, detail=f"Topic not found: {topic_name}")
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    separator = f"\n\n---\n\n**Added: {timestamp}**\n\n"
    with open(target, "a", encoding="utf-8") as f:
        f.write(separator)
        f.write(entry.body.rstrip())
        f.write("\n")
    return StatusResponse(status="ok", path=filename)

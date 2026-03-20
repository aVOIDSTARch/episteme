"""Shared helpers for path resolution, file reading, and search.

Extracted from main.py so routers can reuse without circular imports.
"""

import logging
from pathlib import Path
from typing import List, Optional

from fastapi import HTTPException
from sqlmodel import Session

from models import FileMetadata
from schemas import FileNode, SearchResult

logger = logging.getLogger("episteme")

ROOT = Path(__file__).resolve().parents[1]
FRAMEWORK_ROOT = (ROOT / ".." / "episteme-framework").resolve()


# ---------------------------------------------------------------------------
# Path helpers
# ---------------------------------------------------------------------------

def _get_root(root: Optional[Path] = None) -> Path:
    """Return the given root or fall back to the current FRAMEWORK_ROOT."""
    if root is not None:
        return root
    return FRAMEWORK_ROOT


def safe_resolve(path_rel: str, root: Optional[Path] = None) -> Path:
    """Resolve a relative path under root, raising 403 on traversal attempts."""
    r = _get_root(root)
    resolved = (r / path_rel).resolve()
    if not resolved.is_relative_to(r):
        raise HTTPException(status_code=403, detail="Access denied")
    return resolved


def is_hidden(path: Path) -> bool:
    return any(part.startswith(".") for part in path.parts)


def build_node(path: Path, root: Optional[Path] = None) -> FileNode:
    r = _get_root(root)
    stat = path.stat()
    return FileNode(
        path=str(path.relative_to(r)).replace("\\", "/"),
        name=path.name,
        type="dir" if path.is_dir() else "file",
        size=stat.st_size,
        modified_at=stat.st_mtime,
    )


def list_dir(path_rel: str = "", root: Optional[Path] = None) -> List[FileNode]:
    r = _get_root(root)
    target = safe_resolve(path_rel, r)
    if not target.exists():
        raise FileNotFoundError(f"Directory does not exist: {path_rel}")
    if not target.is_dir():
        raise NotADirectoryError(f"Not a directory: {path_rel}")
    nodes: List[FileNode] = []
    for child in sorted(target.iterdir(), key=lambda c: (not c.is_dir(), c.name.lower())):
        if is_hidden(child):
            continue
        nodes.append(build_node(child, r))
    return nodes


def read_file_contents(path_rel: str, root: Optional[Path] = None) -> str:
    r = _get_root(root)
    full_path = safe_resolve(path_rel, r)
    if not full_path.exists():
        raise FileNotFoundError(path_rel)
    if full_path.is_dir():
        raise IsADirectoryError(path_rel)
    try:
        return full_path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return "[binary file content not renderable]"


def index_all_files(root: Optional[Path] = None) -> List[FileNode]:
    r = _get_root(root)
    all_nodes: List[FileNode] = []

    def recurse(path: Path) -> None:
        if is_hidden(path):
            return
        if path.is_dir():
            for child in path.iterdir():
                recurse(child)
        else:
            all_nodes.append(build_node(path, r))

    recurse(r)
    return all_nodes


def search_all(
    query: str,
    engine,
    path_prefix: Optional[str] = None,
    limit: int = 50,
    root: Optional[Path] = None,
) -> List[SearchResult]:
    q = query.lower()
    candidates: List[SearchResult] = []
    nodes = index_all_files(root)
    with Session(engine) as session:
        for node in nodes:
            if path_prefix and not node.path.startswith(path_prefix):
                continue
            score = 0
            if q in node.name.lower():
                score += 10
            if q in node.path.lower():
                score += 5
            content: Optional[str] = None
            try:
                content = read_file_contents(node.path, root)
                if q in content.lower():
                    score += 20
            except Exception:
                pass
            meta = session.get(FileMetadata, node.path)
            if meta:
                if meta.title and q in meta.title.lower():
                    score += 10
                if meta.description and q in meta.description.lower():
                    score += 10
                if meta.tags and any(q in t.lower() for t in meta.tags):
                    score += 5
            if score > 0:
                snippet = None
                if content is not None:
                    content_lower = content.lower()
                    idx = content_lower.find(q)
                    if idx >= 0:
                        snippet = content[max(0, idx - 40): min(len(content), idx + 120)].replace("\n", " ")
                candidates.append(SearchResult(
                    path=node.path, name=node.name, type=node.type,
                    snippet=snippet, score=float(score),
                ))
    sorted_candidates = sorted(candidates, key=lambda r: r.score, reverse=True)
    return sorted_candidates[:limit]

from contextlib import asynccontextmanager
from datetime import datetime, timezone
from pathlib import Path
from typing import List, Optional

from fastapi import Depends, FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import Session, SQLModel, create_engine

from models import FileMetadata
from schemas import (AgentQueryRequest, AgentQueryResponse, FileContent, FileNode,
                     MetadataPayload, MetadataRecord, SearchResult, StatusResponse)

ROOT = Path(__file__).resolve().parents[1]
FRAMEWORK_ROOT = ROOT / ".." / "episteme-framework"
FRAMEWORK_ROOT = FRAMEWORK_ROOT.resolve()
DB_PATH = ROOT / "metadata.db"

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield


app = FastAPI(title="Episteme Universal Knowledge Service",
              version="0.1.0",
              description="API service to browse and annotate episteme-framework knowledge files.",
              lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

engine = create_engine(f"sqlite:///{DB_PATH}", echo=False, connect_args={"check_same_thread": False})


def init_db() -> None:
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session


def safe_resolve(path_rel: str) -> Path:
    """Resolve a relative path under FRAMEWORK_ROOT, raising 403 on traversal attempts."""
    resolved = (FRAMEWORK_ROOT / path_rel).resolve()
    if not resolved.is_relative_to(FRAMEWORK_ROOT):
        raise HTTPException(status_code=403, detail="Access denied")
    return resolved


def is_hidden(path: Path) -> bool:
    return any(part.startswith(".") for part in path.parts)


def build_node(path: Path) -> FileNode:
    stat = path.stat()
    return FileNode(
        path=str(path.relative_to(FRAMEWORK_ROOT)).replace("\\", "/"),
        name=path.name,
        type="dir" if path.is_dir() else "file",
        size=stat.st_size,
        modified_at=stat.st_mtime,
    )


def list_dir(path_rel: str = "") -> List[FileNode]:
    target = safe_resolve(path_rel)
    if not target.exists():
        raise FileNotFoundError(f"Directory does not exist: {path_rel}")
    if not target.is_dir():
        raise NotADirectoryError(f"Not a directory: {path_rel}")
    nodes: List[FileNode] = []
    for child in sorted(target.iterdir(), key=lambda c: (not c.is_dir(), c.name.lower())):
        if is_hidden(child):
            continue
        nodes.append(build_node(child))
    return nodes


def read_file_contents(path_rel: str) -> str:
    full_path = safe_resolve(path_rel)
    if not full_path.exists():
        raise FileNotFoundError(path_rel)
    if full_path.is_dir():
        raise IsADirectoryError(path_rel)
    try:
        return full_path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return "[binary file content not renderable]"


def index_all_files() -> List[FileNode]:
    all_nodes: List[FileNode] = []

    def recurse(path: Path) -> None:
        if is_hidden(path):
            return
        if path.is_dir():
            for child in path.iterdir():
                recurse(child)
        else:
            all_nodes.append(build_node(path))

    recurse(FRAMEWORK_ROOT)
    return all_nodes


def search_all(query: str, path_prefix: Optional[str] = None, limit: int = 50) -> List[SearchResult]:
    q = query.lower()
    candidates: List[SearchResult] = []
    nodes = index_all_files()
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
                content = read_file_contents(node.path)
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
                candidates.append(SearchResult(path=node.path, name=node.name, type=node.type, snippet=snippet, score=float(score)))
    sorted_candidates = sorted(candidates, key=lambda r: r.score, reverse=True)
    return sorted_candidates[:limit]



@app.get("/api/v1/framework/tree", response_model=List[FileNode])
def get_tree(path: str = ""):
    try:
        return list_dir(path)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Path not found")
    except NotADirectoryError:
        raise HTTPException(status_code=400, detail="Path is not a directory")


@app.get("/api/v1/framework/file", response_model=FileContent)
def get_file(path: str, session: Session = Depends(get_session)):
    normalized = path.strip("/")
    full_path = safe_resolve(normalized)
    if not full_path.exists():
        raise HTTPException(status_code=404, detail="File not found")
    if full_path.is_dir():
        raise HTTPException(status_code=400, detail="Requested path is a directory")
    content = read_file_contents(normalized)
    meta = None
    record = session.get(FileMetadata, normalized)
    if record:
        meta = MetadataRecord(
            title=record.title,
            description=record.description,
            tags=record.tags,
            category=record.category,
            updated_at=record.updated_at.isoformat(),
        )
    return FileContent(path=normalized, content=content, type="file", size=full_path.stat().st_size, metadata=meta)


@app.get("/api/v1/framework/search", response_model=List[SearchResult])
def search(query: str = Query(..., min_length=1), path: Optional[str] = None, limit: int = 50):
    if path:
        path = path.strip("/")
    return search_all(query=query, path_prefix=path, limit=limit)


@app.get("/api/v1/framework/metadata", response_model=MetadataRecord)
def get_metadata(path: str, session: Session = Depends(get_session)):
    normalized = path.strip("/")
    record = session.get(FileMetadata, normalized)
    if not record:
        raise HTTPException(status_code=404, detail="Metadata not found")
    return record


@app.post("/api/v1/framework/metadata", response_model=StatusResponse)
def upsert_metadata(payload: MetadataPayload, session: Session = Depends(get_session)):
    normalized = payload.path.strip("/")
    record = session.get(FileMetadata, normalized)
    if not record:
        record = FileMetadata(path=normalized)
    if payload.title is not None:
        record.title = payload.title
    if payload.description is not None:
        record.description = payload.description
    if payload.tags is not None:
        record.tags = payload.tags
    if payload.category is not None:
        record.category = payload.category
    record.updated_at = datetime.now(timezone.utc)
    session.add(record)
    session.commit()
    session.refresh(record)
    return {"status": "ok", "path": record.path}


@app.post("/api/v1/framework/reindex", response_model=StatusResponse)
def reindex():
    nodes = index_all_files()
    return {"status": "ok", "count": len(nodes)}


@app.post("/api/v1/framework/agent/query", response_model=AgentQueryResponse)
def agent_query(req: AgentQueryRequest):
    results = search_all(query=req.query, path_prefix=req.scope, limit=req.max_results or 20)
    return AgentQueryResponse(results=results)


@app.get("/health", response_model=StatusResponse)
def healthcheck():
    return {"status": "ok", "framework_root": str(FRAMEWORK_ROOT)}

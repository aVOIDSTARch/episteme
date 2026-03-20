import asyncio
import logging
import time
from contextlib import asynccontextmanager
from datetime import datetime, timezone
from pathlib import Path
from typing import List, Optional

import uvicorn
from fastapi import Depends, FastAPI, HTTPException, Query, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from sqlmodel import Session, SQLModel, create_engine

from cloak.auth import require_operation_class, verify_token
from cloak.client import CloakState, listen_halt_stream, register_with_cloak
from cloak.models import TokenClaims
from config import SERVICE_VERSION, SERVICE_ID, SERVICE_PORT, validate_config
import helpers
from helpers import (
    build_node,
    index_all_files,
    is_hidden,
    list_dir,
    read_file_contents,
    safe_resolve,
    search_all,
)
from models import FileMetadata
from schemas import (
    AgentQueryRequest,
    AgentQueryResponse,
    ErrorResponse,
    FileContent,
    FileNode,
    HealthResponse,
    MetadataPayload,
    MetadataRecord,
    SearchResult,
    StatusResponse,
)

logger = logging.getLogger("episteme")

ROOT = Path(__file__).resolve().parents[1]
DB_PATH = ROOT / "metadata.db"

engine = create_engine(
    f"sqlite:///{DB_PATH}", echo=False, connect_args={"check_same_thread": False}
)


def init_db() -> None:
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session


# ---------------------------------------------------------------------------
# Lifespan: DB init, Cloak registration, SSE halt listener
# ---------------------------------------------------------------------------

@asynccontextmanager
async def lifespan(app: FastAPI):
    validate_config()
    init_db()

    cloak_state = CloakState(start_time=time.time())
    app.state.cloak = cloak_state

    halt_stream_url = await register_with_cloak(cloak_state)

    sse_task = None
    if halt_stream_url:
        sse_task = asyncio.create_task(listen_halt_stream(cloak_state, halt_stream_url))

    yield

    if sse_task:
        sse_task.cancel()
        try:
            await sse_task
        except asyncio.CancelledError:
            pass


app = FastAPI(
    title="Episteme Universal Knowledge Service",
    version=SERVICE_VERSION,
    description="API service to browse and annotate episteme-framework knowledge files.",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount domain routers
from routers.skills import router as skills_router
from routers.projects import router as projects_router
from routers.ideas import router as ideas_router
from routers.guides import router as guides_router
from routers.docs import router as docs_router

app.include_router(skills_router)
app.include_router(projects_router)
app.include_router(ideas_router)
app.include_router(guides_router)
app.include_router(docs_router)


# ---------------------------------------------------------------------------
# Structured error handler
# ---------------------------------------------------------------------------

@app.exception_handler(HTTPException)
async def structured_http_exception_handler(request: Request, exc: HTTPException):
    if isinstance(exc.detail, dict):
        body = {
            "error": exc.detail.get("error", "unknown"),
            "detail": exc.detail.get("detail", str(exc.detail)),
            "service": "episteme",
            "status_code": exc.status_code,
        }
    else:
        body = {
            "error": "request_error",
            "detail": exc.detail,
            "service": "episteme",
            "status_code": exc.status_code,
        }
    return JSONResponse(status_code=exc.status_code, content=body)


# ---------------------------------------------------------------------------
# Endpoints
# ---------------------------------------------------------------------------

@app.get(
    "/api/v1/framework/tree",
    response_model=List[FileNode],
    operation_id="episteme_list_tree",
    summary="List directory contents",
    description="Returns immediate children of a directory in the episteme-framework tree.",
    tags=["episteme"],
)
def get_tree(
    path: str = Query("", description="Repo-relative directory path (empty for root)"),
    _token: TokenClaims = Depends(verify_token),
):
    try:
        return list_dir(path)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Path not found")
    except NotADirectoryError:
        raise HTTPException(status_code=400, detail="Path is not a directory")


@app.get(
    "/api/v1/framework/file",
    response_model=FileContent,
    operation_id="episteme_read_file",
    summary="Read file content",
    description="Returns the raw text content and metadata of a single file.",
    tags=["episteme"],
)
def get_file(
    path: str = Query(..., description="Repo-relative file path"),
    session: Session = Depends(get_session),
    _token: TokenClaims = Depends(verify_token),
):
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
    return FileContent(
        path=normalized, content=content, type="file",
        size=full_path.stat().st_size, metadata=meta,
    )


@app.get(
    "/api/v1/framework/search",
    response_model=List[SearchResult],
    operation_id="episteme_search",
    summary="Search knowledge files",
    description="Full-text search across file paths, content, and metadata.",
    tags=["episteme"],
)
def search(
    query: str = Query(..., min_length=1, description="Search query string"),
    path: Optional[str] = Query(None, description="Path prefix to restrict scope"),
    limit: int = Query(50, description="Maximum results to return"),
    _token: TokenClaims = Depends(verify_token),
):
    if path:
        path = path.strip("/")
    return search_all(query=query, engine=engine, path_prefix=path, limit=limit)


@app.get(
    "/api/v1/framework/metadata",
    response_model=MetadataRecord,
    operation_id="episteme_get_metadata",
    summary="Get file metadata",
    description="Returns stored metadata (tags, description, category) for a file.",
    tags=["episteme"],
)
def get_metadata(
    path: str = Query(..., description="Repo-relative file path"),
    session: Session = Depends(get_session),
    _token: TokenClaims = Depends(verify_token),
):
    normalized = path.strip("/")
    record = session.get(FileMetadata, normalized)
    if not record:
        raise HTTPException(status_code=404, detail="Metadata not found")
    return MetadataRecord(
        title=record.title,
        description=record.description,
        tags=record.tags,
        category=record.category,
        updated_at=record.updated_at.isoformat(),
    )


@app.post(
    "/api/v1/framework/metadata",
    response_model=StatusResponse,
    operation_id="episteme_upsert_metadata",
    summary="Create or update file metadata",
    description="Upserts metadata (tags, description, category) for a file. Requires write access.",
    tags=["episteme"],
)
def upsert_metadata(
    payload: MetadataPayload,
    session: Session = Depends(get_session),
    _token: TokenClaims = Depends(require_operation_class("write")),
):
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


@app.post(
    "/api/v1/framework/reindex",
    response_model=StatusResponse,
    operation_id="episteme_reindex",
    summary="Rebuild file index",
    description="Re-walks the episteme-framework directory. Requires admin access.",
    tags=["episteme"],
)
def reindex(
    _token: TokenClaims = Depends(require_operation_class("admin")),
):
    nodes = index_all_files()
    return {"status": "ok", "count": len(nodes)}


@app.post(
    "/api/v1/framework/agent/query",
    response_model=AgentQueryResponse,
    operation_id="episteme_agent_query",
    summary="Agent knowledge query",
    description="Structured search endpoint optimized for agent consumption.",
    tags=["episteme"],
)
def agent_query(
    req: AgentQueryRequest,
    _token: TokenClaims = Depends(verify_token),
):
    results = search_all(query=req.query, engine=engine, path_prefix=req.scope, limit=req.max_results or 20)
    return AgentQueryResponse(results=results)


@app.get(
    "/health",
    response_model=HealthResponse,
    operation_id="episteme_health",
    summary="Health check",
    description="Returns service health status for Cortex FSM. No authentication required.",
    tags=["system"],
)
def healthcheck():
    cloak_state = app.state.cloak
    if cloak_state.halted:
        status = "halted"
    elif not helpers.FRAMEWORK_ROOT.exists():
        status = "degraded"
    else:
        status = "healthy"
    return HealthResponse(
        status=status,
        service_id=SERVICE_ID,
        version=SERVICE_VERSION,
        halted=cloak_state.halted,
        halt_reason=cloak_state.halt_reason,
        framework_root_exists=helpers.FRAMEWORK_ROOT.exists(),
        session_id=cloak_state.session_id,
        uptime_seconds=time.time() - cloak_state.start_time,
    )


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=SERVICE_PORT)

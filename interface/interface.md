# Episteme Universal Knowledge Interface — Design & Implementation Plan

## Goal
Build a separate service that provides:
1. Universal API over `episteme-framework/` file content + metadata + organization.
2. Fast TypeScript OpenAPI-compliant frontend with file browsing, search, tagging, and metadata editing.
3. CLI + web + agent support.
4. Clean structured endpoints and local persistent metadata.
5. Full integration as a Cortex downstream service (`:8100`).

## Architecture

### System Context
Episteme is a registered downstream service in the Cortex infrastructure:
```
Cortex :9000 → (proxy) → Episteme :8100
Cloak  :8300 ← (registration + SSE halt channel) ← Episteme
```

All external requests arrive through Cortex, which validates tokens via Cloak before forwarding. Episteme also verifies token signatures locally using a signing key received from Cloak at startup.

### Services
- **Knowledge Service (Python FastAPI)** in `interface/service/`
  - Runs on port **8100** (Cortex-assigned).
  - Registers with Cloak at startup (fail-closed if registration fails).
  - Maintains SSE connection to Cloak for halt/key-rotation signals.
  - Verifies agent token signatures locally (HMAC-SHA256).
  - Indexes all non-hidden files under `episteme-framework/`.
  - Persistent SQLite metadata (`metadata.db`) for tags, notes, categories.
  - Structured REST API endpoints under `/api/v1/framework/`.
  - OpenAPI docs at `/docs` with `operation_id`s for Cortex MCP tool generation.
  - CLI integration endpoint for agent/CLI use.
- **Frontend (TypeScript React with Vite)** in `interface/frontend/`
  - Uses OpenAPI/Swagger generated endpoint definitions from backend.
  - Provides file tree, search, file content viewer, tag editor.
  - Uses lightweight, fast UI and direct REST.

### Service Modules
```
interface/service/
├── main.py              # FastAPI app, lifespan, endpoints
├── models.py            # SQLModel FileMetadata table
├── schemas.py           # Pydantic request/response schemas
├── config.py            # Env-var configuration
├── cli.py               # CLI client
├── requirements.txt
└── cloak/               # Thin Python Cloak SDK
    ├── __init__.py
    ├── client.py        # Registration + SSE halt listener
    ├── auth.py          # Token verification FastAPI dependencies
    └── models.py        # Cloak protocol Pydantic models
```

## Cortex Integration

### Cloak Registration (startup)
1. POST `/cloak/services/register` with manifest token (from `EPISTEME_MANIFEST_TOKEN` env var).
2. Receive `session_id`, `signing_key`, `halt_stream_url`.
3. Store signing key in memory only.
4. Open persistent SSE connection to halt stream.
5. If registration fails → service does not start (fail closed).

### Halt Signal Handling
- SSE `halt` event → stop accepting requests, return 503.
- SSE `key_rotation` event → atomic swap of signing key.
- SSE connection lost after 5 retries → self-halt (fail closed).

### Token Verification
All endpoints except `/health` require a valid Bearer token. Tokens are verified locally using the signing key from Cloak. Token claims specify:
- `operation_class`: `read`, `write`, or `admin`
- `resources`: list of allowed paths or `"*"`

### Operation Class Mapping

| Endpoint | Method | Operation Class |
|---|---|---|
| `/api/v1/framework/tree` | GET | `read` |
| `/api/v1/framework/file` | GET | `read` |
| `/api/v1/framework/search` | GET | `read` |
| `/api/v1/framework/metadata` | GET | `read` |
| `/api/v1/framework/metadata` | POST | `write` |
| `/api/v1/framework/reindex` | POST | `admin` |
| `/api/v1/framework/agent/query` | POST | `read` |
| `/health` | GET | **none** |

### Health Endpoint (Cortex FSM)
`GET /health` returns structured status for Cortex's health state machine:
- `healthy` — fully operational
- `halted` — operator-stopped via Cloak
- `degraded` — framework directory missing

### MCP Tool Generation
Each endpoint has an `operation_id` prefixed with `episteme_` (e.g., `episteme_search`, `episteme_read_file`). Cortex reads `/openapi.json` at startup to auto-generate MCP tools.

### Error Response Format
All errors return a standardized envelope:
```json
{
    "error": "error_code_snake_case",
    "detail": "Human-readable message",
    "service": "episteme",
    "status_code": 404
}
```

## Data Model

### FileNode
- `path` (string, repo-relative under episteme-framework)
- `type` (dir|file)
- `name`
- `size`
- `modified_at`

### Metadata record
- `path` (primary key)
- `title`
- `description`
- `tags` (json list)
- `category`
- `updated_at`

## API Contract

Base path: `/api/v1/framework`

### Endpoints

- `GET /api/v1/framework/tree` (`episteme_list_tree`)
  - Query: `path` (optional, default root)
  - Auth: `read`
  - Returns directory children and metadata summary.

- `GET /api/v1/framework/file` (`episteme_read_file`)
  - Query: `path` required file path
  - Auth: `read`
  - Returns raw text content, file metadata, and stored tags.

- `GET /api/v1/framework/search` (`episteme_search`)
  - Query: `query` required, `path` optional, `limit` optional
  - Auth: `read`
  - Returns matching file nodes by path/title/content/metadata.

- `GET /api/v1/framework/metadata` (`episteme_get_metadata`)
  - Query: `path` required
  - Auth: `read`
  - Returns metadata record for file or directory.

- `POST /api/v1/framework/metadata` (`episteme_upsert_metadata`)
  - Body: `path`, `title?`, `description?`, `tags?`, `category?`
  - Auth: `write`
  - Upserts metadata record.

- `POST /api/v1/framework/reindex` (`episteme_reindex`)
  - Auth: `admin`
  - Rebuild in-memory index and refresh search data.

- `POST /api/v1/framework/agent/query` (`episteme_agent_query`)
  - Body: `query`, `scope?`, `max_results?`
  - Auth: `read`
  - Returns structured knowledge results for agents.

- `GET /health` (`episteme_health`)
  - Auth: **none** (Cortex health polling)
  - Returns service health status for Cortex FSM.

### OpenAPI + CLI
- Backend uses FastAPI OpenAPI schema at `/openapi.json`.
- All endpoints have `operation_id`, `summary`, `description`, and `tags` for MCP tool generation.
- Frontend will fetch this for type-safe client generation (or typed endpoint wrappers).
- CLI script (`interface/service/cli.py`) calls API on `localhost:8100`.

## Configuration

All config via environment variables:

| Variable | Default | Required | Description |
|---|---|---|---|
| `EPISTEME_PORT` | `8100` | No | Service port |
| `CLOAK_URL` | `http://cloak.tailnet:8300` | No | Cloak service URL |
| `EPISTEME_MANIFEST_TOKEN` | — | Yes* | Pre-provisioned Cloak manifest token |
| `CLOAK_DISABLED` | `false` | No | Dev-only: skip auth entirely |

*Required unless `CLOAK_DISABLED=true`.

## Frontend UX

Main screens:
1. **Explorer** (tree browser), showing `episteme-framework` sections.
2. **File viewer** (content + metadata + edit tags).
3. **Search** (global search across content and metadata).
4. **Ideas/skills cards** (derived from known subfolder categories).

### URL routes
- `/` — file browser
- `/file?path=...` — content view
- `/search?q=...` — search results

## Deployment

### Local development (no Cloak)
```bash
cd interface/service
export CLOAK_DISABLED=true
python -m venv .venv && pip install -r requirements.txt
uvicorn main:app --reload --port 8100
```

### Production (with Cortex)
```bash
cd interface/service
export EPISTEME_MANIFEST_TOKEN=<token-from-infisical>
export CLOAK_URL=http://cloak.tailnet:8300
python -m main
```

Run frontend:
```bash
cd interface/frontend && npm install && npm run dev
```

## Implementation Status

### Completed
1. FastAPI backend with SQLModel + SQLite metadata storage.
2. File tree browsing, file reading, search, and metadata CRUD endpoints.
3. Agent query endpoint.
4. CLI script for tree/file/search operations.
5. Vite React TypeScript app scaffolded (no UI components yet).
6. Cloak SDK (Python): registration, SSE halt listener, token verification.
7. Auth middleware with operation class enforcement (read/write/admin).
8. Structured health endpoint for Cortex FSM.
9. Standardized error responses.
10. OpenAPI operation_ids and field descriptions for MCP tool generation.
11. Path traversal security guard on all file-access endpoints.

### Not Yet Implemented
- Frontend UI components (explorer, file viewer, search, cards).
- OpenAPI client generation for frontend.
- Frontend routing (`/`, `/file?path=...`, `/search?q=...`).

## Future Enhancements
- Add incremental file-watcher updates.
- Build a persistent search index (current search scans all files per request).
- Add vector search over file text using local embeddings (via Datastore/pgvector).
- Add direct agent prompt executor.
- Swap to Ed25519 token verification when Cortex spec finalizes signing algorithm.

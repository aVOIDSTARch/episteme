# Episteme Universal Knowledge Interface — Design & Implementation Plan

## Goal
Build a separate service that provides:
1. Universal API over `episteme-framework/` file content + metadata + organization.
2. Fast TypeScript OpenAPI-compliant frontend with file browsing, search, tagging, and metadata editing.
3. CLI + web + agent support.
4. Clean structured endpoints and local persistent metadata.

## Architecture

### Services
- **Knowledge Service (Python FastAPI)** in `interface/service/`
  - Indexes all non-hidden files under `episteme-framework/`.
  - Persistent SQLite metadata (`metadata.db`) for tags, notes, categories.
  - Structured REST API endpoints under `/api/v1/framework/`.
  - OpenAPI docs auto-generated at `/docs`.
  - CLI integration endpoint for agent/CLI use.
- **Frontend (TypeScript React with Vite)** in `interface/frontend/`
  - Uses OpenAPI/Swagger generated endpoint definitions from backend.
  - Provides file tree, search, file content viewer, tag editor.
  - Uses lightweight, fast UI and direct REST.

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

- `GET /api/v1/framework/tree`
  - Query: `path` (optional, default root)
  - Returns directory children and metadata summary.

- `GET /api/v1/framework/file`
  - Query: `path` required file path
  - Returns raw text content, file metadata, and stored tags.

- `GET /api/v1/framework/search`
  - Query: `query` required, `path` optional, `limit` optional
  - Returns matching file nodes by path/title/content/metadata.

- `GET /api/v1/framework/metadata`
  - Query: `path` required
  - Returns metadata record for file or directory.

- `POST /api/v1/framework/metadata`
  - Body: `path`, `title?`, `description?`, `tags?`, `category?`
  - Upserts metadata record.

- `POST /api/v1/framework/reindex`
  - Rebuild in-memory index and refresh search data.

- `POST /api/v1/framework/agent/query`
  - Body: `query`, `scope?`, `max_results?`
  - Returns structured knowledge results for agents.

### OpenAPI + CLI
- Backend uses FastAPI OpenAPI schema at `/openapi.json`.
- Frontend will fetch this for type-safe client generation (or typed endpoint wrappers).
- CLI script (`interface/service/cli.py`) will call API to query/list/read.

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

Run knowledge service:
- `cd interface/service && python -m venv .venv && pip install -r requirements.txt && uvicorn main:app --reload`

Run frontend:
- `cd interface/frontend && npm install && npm run dev`

## Implementation Status

### Completed
1. FastAPI backend with SQLModel + SQLite metadata storage.
2. File tree browsing, file reading, search, and metadata CRUD endpoints.
3. Agent query endpoint.
4. CLI script for tree/file/search operations.
5. Vite React TypeScript app scaffolded (no UI components yet).

### Not Yet Implemented
- Frontend UI components (explorer, file viewer, search, cards).
- OpenAPI client generation for frontend.
- Frontend routing (`/`, `/file?path=...`, `/search?q=...`).

## Future Enhancements
- Add incremental file-watcher updates.
- Build a persistent search index (current search scans all files per request).
- Add vector search over file text using local embeddings.
- Add user auth + roles for multi-user.
- Add direct agent prompt executor.

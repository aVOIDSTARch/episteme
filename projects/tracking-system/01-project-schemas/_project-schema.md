# PROJECT SCHEMAS

#### LEADING UNDERSCORE DOCUMENT CONCEPT SUMMARY

**Schema for the schema.** Defines what every PROJECT SCHEMA in this folder must contain. Setup only—what to gather and record—not implementation or planning. `_` docs = schema, enums, conventions, REQUIRED_SKILLS only; no skill descriptions or engineering. Skill behavior → notes file (see Conventions).

---

## Purpose

**PROJECT SCHEMA** = minimum metadata and context for an agent: high-level understanding + which skills to pull to build project context. Human-readable, agent-centric, low-token. One file per project; lives in this folder, reference only.

---

## What This Is Not

Not a plan, design, or task list; not a substitute for `002-*` planning or progress docs. Only “what this project is at setup.” Out of scope, dependencies, and success criteria → planning doc; agent gathers them during planning.

---

## Required Information

MUST include these. One line or short list per field.

| Section | Content | Example / notes |
|--------|---------|------------------|
| **Project** | Name or slug (machine- and human-friendly). | `my-app`, `docs-site` |
| **Summary** | One-line description. What is this project? | “CLI tool to sync env files.” |
| **Owner** | Who this project is for (user, team, or “personal”). | User name or “personal.” |
| **Type** | Project type from your taxonomy. | e.g. `blank`, `standard-starter`, `app`, `lib`, `docs` |
| **Stack** | Primary language/runtime and key tech (short list). | `TS`, `Node 20`, `React` |
| **Created** | Date the schema was created (YYYY-MM-DD). | For ordering and reference. |

---

## Optional Information

Include when relevant; omit to save tokens.

| Section | Content | When to use |
|--------|---------|-------------|
| **Deployment** | **Confirmed** and **Possible** arrays. Use enum below. | When known; keeps terms consistent. |
| **Dev environment** | OS, editor, runtimes, tooling (short list). | **Agent-observed.** |
| **Agents / models** | Host and model (e.g. Cursor, Claude Opus). | **Agent-observed.** |
| **Constraints** | Hard rules (e.g. no backend, must use Vitest). | When they affect skills/context. |
| **Repo path** | Path or URL to repo/workspace. | When not “this folder” or agent needs to open/clone. |
| **Project state** | One value from enum below. | Plan-from-zero vs explore-first. **Ask at schema time.** |
| **Read first** | Paths or docs to read before planning/exploration. | When known; else agent discovers or user adds later. |
| **Entry points** | Where the app/code starts (main file, app root). | When known; else agent discovers or user adds later. |
| **REQUIRED_SKILLS** | Skill name + location per row. See below. | Pull for context; user or agent may add over time. |
| **Project-specific enums** | Optional section: name + table (value, meaning). | When this project needs its own controlled vocab (e.g. statuses, types) beyond framework enums. |
| **Project vocabulary** | Optional: term → one-line definition. | When domain/team jargon or overloaded terms would confuse the next agent or human. Keep short. |
| **Schema version** | Schema format version (e.g. `1`). | If you version the spec. |

### Project state (enum)

One value. Plan-from-zero vs explore-first.

| Value | Meaning |
|-------|---------|
| Greenfield   | New project; no code yet. → Planning. |
| Existing     | Joining or changing a codebase. Explore (Read first, Entry points) then plan. |
| Enhancement  | Existing project; additive phase. Explore then plan changes. |
| Migration    | Rewriting or moving from existing. Explore source then plan. |

### Deployment environments (enum)

Use these terms. **Confirmed** = definite; **Possible** = maybe/future.

| Term                  | Meaning                                                                     |
|-----------------------|-----------------------------------------------------------------------------|
| Website               | Static or simple site (marketing, landing, docs).                           |
| Web Application       | Web app (SPA, full-stack).                                                  |
| iOS App               | iPhone / iPad (native or cross-platform).                                   |
| Android App           | Android (native or cross-platform).                                         |
| Desktop Application   | Desktop app (Electron, native, etc.).                                       |
| CLI                   | Command-line tool or script.                                                |
| API / Backend Service | Backend API, serverless, or service.                                        |
| Library / Package     | Package or library (npm, crate, etc.).                                      |
| Other                 | None of the above; add a short note in parentheses if helpful.              |

### Dev environment (agent-observed)

Agent infers from context: OS, editor, runtimes, tooling. Short list. Omit if not detectable.

### Agents / models (agent-observed)

Agent notes own host and model from context. One line or short list.

### REQUIRED_SKILLS

Always stored in the schema. Table: skill name + location (path or URL to pull). Agent pulls these to build context before planning/code review. May start empty; user or agent may add or amend at any point in the full lifecycle when a skill is needed or created—saves the next agent time. One row per skill.

---

## Conventions

- **Naming:** Instance: `<project-slug>-schema.md`; optional prefix `NNN-` for ordering. Leading `_` = meta-docs (this file).
- **Location:** Schema files stay in this folder; they are the durable setup record.
- **Skill behavior:** SETUP_NEW_PROJECT (gathering, UX) → `ai-docs/project-schema-setup-skill-notes.md`. This doc = schema + REQUIRED_SKILLS only.
- **Format:** Markdown; required sections as level-2 headings. Tables or short lists; no long prose. Project-specific enums: optional section for this project’s own controlled vocab; framework enums (Deployment, Project state) stay in this _doc.
- **Agent use:** Gather required (and optional) from user; write once. Agent fills agent-observed fields from context. REQUIRED_SKILLS: amend anytime in the lifecycle when a skill is needed or created. No duplicates.

---

## Minimal Example Structure

```markdown
# PROJECT: <project-slug>

## Project
<slug>

## Summary
<one line>

## Owner
<who>

## Type
<type>

## Stack
<short list>

## Created
YYYY-MM-DD

## Deployment
**Confirmed:** [e.g. Web Application, iOS App]
**Possible:** [e.g. Android App]

## Dev environment
[e.g. macOS, Cursor, Node 20, pnpm]

## Agents / models
[e.g. Cursor, Claude Opus]

## Project state
[Greenfield | Existing | Enhancement | Migration]

## Read first
[e.g. README.md, docs/ARCHITECTURE.md] or none

## Entry points
[e.g. src/index.ts, app/]

## Project-specific enums
(Optional. e.g. **Status**: draft, active, done — one table or list per enum.)

## Project vocabulary
(Optional. e.g. **ticket** = work item; **ship** = deploy to staging — term → one line.)

## REQUIRED_SKILLS
| Skill name | Location |
|------------|----------|
| SETUP_NEW_PROJECT | (path or URL to SKILL.md) |
```

Optional sections: same heading style. One line or short list per section.

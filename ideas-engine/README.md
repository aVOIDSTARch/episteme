# Ideas engine

**Purpose:** Defines the Ideas System used by the meta-agent: storage format, slash commands, and future-app invariants. This folder is the canonical spec and documentation; the actual idea files live in `~/ideas/` (or `IDEAS_ROOT`) per user.

**Audience:** Agents (Claude, Cursor, etc.) and humans. The meta-agent (e.g. `meta-agent.md`) points here for Ideas System behavior.

---

## 1. What it is

- **Ideas** are user-sourced raw text (“verbatim”) plus an agent interpretation (implications, connections). They are stored as markdown files, **one topic per file**, under a single directory (default `~/ideas/`).
- **Topics** are thematic buckets (e.g. “AI tools”, “side projects”, “learning”). Each topic file contains one or more idea entries. The agent can suggest merging or splitting topics occasionally.
- **Slash commands** (from meta-agent): `/ideas` (browse topics and entries; optionally **Synthesize** a topic into project ideas) and `/add-idea <text>` (append a new idea to a matching or new topic).

---

## 2. Location

| Context        | Default path   | Override / note |
|----------------|----------------|------------------|
| User home      | `~/ideas/`     | Set `IDEAS_ROOT` or project-specific path if needed. |
| Episteme repo  | (optional)     | Repo can host a copy or symlink for portability; meta-agent still uses `~/ideas/` unless configured otherwise. |

All topic files are `*.md` under that directory. No subfolders required; flat list of topic files.

---

## 3. File format (topic file)

See **[_idea-file-schema.md](_idea-file-schema.md)** for the full schema. Summary:

- **One file per topic;** filename = topic slug (e.g. `ai-tools.md`, `side-projects.md`).
- **Per entry:** `**Verbatim:** "exact user text"` and `**Claude:**` (or agent name) interpretation. Verbatim is immutable once written.
- **Optional but recommended:** `id` (sequential per file), `created_at` (ISO date or timestamp) for future app migration.
- **Append-only:** Do not edit or delete existing entries; only add new ones. Suggest topic merge/split in commentary, not by rewriting history.

---

## 4. Slash commands (agent behavior)

Defined in meta-agent; implemented by the agent using this spec.

### `/ideas`

1. Scan all `*.md` files in the Ideas root (`~/ideas/` or `IDEAS_ROOT`).
2. Present a **menu of topic names** (derived from filenames or first heading).
3. On topic selection, show that topic’s idea list (Verbatim + interpretation for each entry).
4. Offer: **Synthesize** (extended thinking: e.g. turn this topic into 10–15 project ideas; show inline, then return), **Return to topic list**. Always include “Return to prompt”.

### `/add-idea <text>`

1. Take the text after `/add-idea`.
2. **Match** an existing topic file (by title/slug or content) or **propose a new topic name**; confirm with user before creating a new file.
3. **Append** one new entry: `**Verbatim:** "<exact text>"` and `**Claude:**` (or agent) interpretation (implications, connections to existing ideas in that file).
4. Confirm what was added and where.

---

## 5. Future-app invariants

Keep these true so the format can be migrated to an app or DB later:

- **Per entry:** `id`, `topic`, `verbatim` (immutable), `claude_interpretation` (or `agent_interpretation`), `created_at`.
- **Storage:** 1:1 topic file ↔ topic page; append-only writes.
- **API:** TypeScript-first backend (tRPC or REST) with markdown as initial data source; optional export/import from `~/ideas/*.md`.

---

## 6. Files in this folder

| File | Purpose |
|------|--------|
| **README.md** (this file) | Overview, location, format summary, slash commands, future invariants. |
| **_idea-file-schema.md** | Formal schema for topic files (structure, required/optional fields). |
| **AGENT-INSTRUCTIONS.md** | Step-by-step instructions for agents implementing `/ideas` and `/add-idea`. |
| **template-topic.md** | Template for a new topic file (copy to `~/ideas/<topic>.md`). |
| **list-topics.sh** | Optional script: list topic filenames and titles from Ideas root (`IDEAS_ROOT` or `~/ideas/`). |

---

## 7. Relation to meta-agent

The **meta-agent** (e.g. `meta-agent.md` or `episteme-framework/agent-docs/meta-agent.example.md`) is the cross-project agent doc. It defines `/menu`, `/ideas`, `/add-idea`, and points to the Ideas System. This folder (**ideas-engine**) is the single source of truth for how that system works: format, commands, and invariants. When in doubt, this folder wins on spec; meta-agent wins on when to invoke the commands (e.g. from `/menu` → Ideas).

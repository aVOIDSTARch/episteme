# Idea file schema

**Purpose:** Formal specification for topic files in the Ideas System. Agents and future apps use this to parse, validate, and append entries. Underscore prefix = schema/convention doc.

---

## 1. Scope

- **One file per topic.** Filename = topic slug (e.g. `ai-tools.md`, `side-projects.md`). Use lowercase, hyphens for spaces.
- **Append-only.** Existing entries are never edited or deleted. New ideas are appended. Topic merge/split is done by creating new files and optionally archiving old ones; do not rewrite history.

---

## 2. File structure

```markdown
# Topic Name

Optional one-line description of what this topic covers.

---

## Entry 1

**Verbatim:** "Exact text as the user wrote it."
**Claude:** Interpretation — implications, connections to other ideas. (Or **Agent:** if not Claude.)

Optional: `id: 1` · `created_at: 2026-03-03T12:00:00Z`

---

## Entry 2

**Verbatim:** "Next idea..."
**Claude:** ...
```

- **Level-1 heading** (`#`) = topic title (once per file).
- **Optional** short description after the title, before the first `---`.
- **Separator** `---` between entries.
- **Level-2 heading** (`##`) = entry label. Can be "Entry N" or a short slug (e.g. `## idea-about-ai-tools`). Used for anchors and optional `id` consistency.
- **Required per entry:** `**Verbatim:** "..."` and `**Claude:**` (or `**Agent:**`) interpretation.
- **Optional per entry:** `id` (integer, sequential per file), `created_at` (ISO 8601). Recommended for future app import.

---

## 3. Field rules

| Field | Required | Mutable | Format / notes |
|-------|----------|---------|------------------|
| **Verbatim** | Yes | No | Exact user text in double quotes. Never rewrite or “fix” spelling. |
| **Claude** / **Agent** | Yes | No after write | Interpretation: what the idea implies, connections to other ideas. |
| **id** | No | No | Sequential integer per file. Assign on append. |
| **created_at** | No | No | ISO 8601 (e.g. `2026-03-03T12:00:00Z`). Set on append. |

---

## 4. Parsing notes (for agents and scripts)

- **List topics:** Enumerate `*.md` in Ideas root; topic name = first `# ` line or filename-without-extension.
- **List entries in a topic:** Split file by `---`; each block with `**Verbatim:**` and `**Claude:**` (or `**Agent:**`) is one entry. Heading `## …` is the entry label.
- **Append entry:** Add `---` then a new `## Entry N` (or slug) block with Verbatim and Claude/Agent lines; optionally add `id` and `created_at`.

---

## 5. Future-app invariants

These are fixed for compatibility with a future TypeScript app or DB:

- **id** — unique per file, sequential.
- **topic** — derived from filename or first heading.
- **verbatim** — immutable string.
- **claude_interpretation** (or **agent_interpretation**) — text of the interpretation.
- **created_at** — ISO 8601, set once.

Topic files map 1:1 to “topic” entities; each entry maps to an “idea” row. Append-only writes ensure a clean migration path.

# _Docs Design (Reference)

**Succinct design document for underscore-prefixed (`_`) docs.** *(This is the design reference for _docs; it lives in `ai-docs` and is not itself a _doc—it has no folder of instance docs.)* For full discussion and open points see `_docs-format-and-design-notes.md`.

---

## What _Docs Are

- **Name:** `_<foldername or document type contained within>.md` (e.g. `_project-schema.md`, `_planning-docs.md`).
- **Role:** Schema for the folder. Defines what instance docs in that folder must or may contain. Meta to instance files (e.g. `sample-project-schema.md` follows `_project-schema.md`).
- **Scope:** Schema, enums, conventions, REQUIRED_SKILLS only. No implementation, no skill behavior, no planning. Skill behavior → separate notes file.
- **Audience:** Humans and agents. Low-token, scannable: tables and short lists over prose.

---

## Naming

| What | Pattern | Example |
|------|---------|---------|
| _Doc | `_<foldername or doc type>.md` | `_planning-docs.md` |
| Instance file | `<project-slug>-<doc-type>.md` | `sample-project-planning-doc.md` |

**Tracking-system folders:** 01-project-schemas, 02-planning-docs, 03-progress-docs, 04-completed, 05-after-action. Numbering (e.g. `001-`) is optional and project-specific.

---

## Template Structure (every _doc)

1. **H1** — UPPERCASE title (e.g. `# PROJECT SCHEMAS`).
2. **H4** — Leading underscore document concept summary (2–4 sentences: what this _doc is; _docs = schema/enums/conventions/REQUIRED_SKILLS only; where skill behavior lives).
3. `---`
4. **## Purpose** — One short paragraph.
5. **## What This Is Not** — Short scope clarification.
6. **## Required Information** — Table: Section | Content | Example/notes.
7. **## Optional Information** — Table: Section | Content | When to use.
8. **Enums** — One ### per enum; intro + table (value | meaning). Framework enums live in this _doc.
9. **Agent-observed** — If any, mark in table and Conventions.
10. **## Conventions** — Bullets: Naming, Location, Skill behavior (pointer), Format, Agent use.
11. **## REQUIRED_SKILLS** (if applicable) — Table: Skill name | Location. Stored in schema; add/amend anytime in lifecycle.
12. **## Minimal Example Structure** — Fenced markdown skeleton of an instance doc.

---

## Design Principles

- **Low token:** Tables and bullets; one line or short list per field.
- **Agent-centric:** Explicit Required vs Optional; parseable section names and headers.
- **Single source of truth:** _Doc is the only definition for that folder’s schema.
- **Enums:** Framework enums in the _doc (separation of concerns). Instance docs may add optional project-specific enums or project vocabulary.
- **No implementation in _doc:** What and how to write only; how to gather/implement → notes/SKILL.

---

## Instance Extensions (e.g. project schema)

Instance docs that follow a _doc may include **optional** sections not in the _doc itself when the schema allows it (e.g. project schema): **Project-specific enums**, **Project vocabulary** (term → one-line definition). Framework enums stay in the _doc.

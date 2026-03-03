# _Docs: Description, Format & Design Language

**Purpose:** One place to define what underscore-prefixed (`_`) docs are, which folders they live in, their preferred format, and a consistent design aesthetic. *(This file is a notes doc about _docs; it is not itself a _doc—it lives in `ai-docs` and describes the pattern.)* **Succinct design reference:** `ai-docs/_docs-design.md`. This file holds discussion, open points, and elaboration.

---

## 1. What Are _Docs?

- **Naming:** Filename starts with `_`, then **&lt;foldername or document type contained within&gt;** (e.g. `_project-schema.md`, `_planning-docs.md`). Not necessarily `-schema`; use the folder or doc type name (e.g. next folder → `_planning-docs.md`). See §6 for full naming conventions.
- **Role:** They are **schema-for-the-folder**: they define what documents in that folder must or may contain. They are **meta** relative to the instance docs (e.g. `sample-project-schema.md` follows `_project-schema.md`).
- **Scope:** Schema, enums, conventions, and (where applicable) REQUIRED_SKILLS **only**. No implementation, no skill behavior descriptions, no planning or task content. Skill behavior and “how to gather” live in separate notes files (e.g. `ai-docs/project-schema-setup-skill-notes.md`).
- **Consumers:** Humans and agents. Optimized for **agent-centric, low-token** reading: scannable, one line or short list per field, tables over long prose.
- **Lifecycle:** _Docs stay in their folder as long as that document type exists; they are the single source of truth for “what goes in this folder.”

---

## 2. Which Folders Get a _Doc?

| Folder (current or planned) | _Doc name | Instance files (examples) |
|-----------------------------|-----------|---------------------------|
| `projects/tracking-system/01-project-schemas/` | `_project-schema.md` | `sample-project-schema.md`, `<slug>-schema.md` |
| `projects/tracking-system/02-planning-docs/` | `_planning-docs.md` | `sample-project-planning-doc.md`, `<slug>-planning-doc.md` |
| `projects/tracking-system/03-progress-docs/` | `_progress-docs.md` | `sample-project-progress.md`, `<slug>-progress.md` |
| `projects/tracking-system/04-completed/` | `_completed-report.md` | `<slug>-completed.md`; project-named subfolder holds planning + progress + completed |
| `projects/tracking-system/05-after-action/` | `_after-action.md` | `sample-project-after-action.md`, `<slug>-after-action.md` |

**Rule of thumb:** One _doc per “document type” folder. Name the _doc **`_<foldername or document type contained within>.md`** (e.g. `_planning-docs.md` for a folder that contains planning docs). Instance files in that folder: **`<project-slug>-<doc-type>.md`** (e.g. `sample-project-schema.md`, `sample-project-planning-doc.md`).

---

## 3. Preferred Format (Template Structure)

Derived from `_project-schema.md` and reusable across _docs.

1. **H1 — Title**  
   UPPERCASE short title for the document type (e.g. `# PROJECT SCHEMAS`).

2. **H4 — Leading underscore document concept summary**  
   One short block (2–4 sentences) that states:
   - What this _doc is (schema for what).
   - That `_` docs = schema, enums, conventions, REQUIRED_SKILLS only; no skill/engineering.
   - Where skill behavior lives (pointer to notes file).

3. **Horizontal rule** `---`

4. **## Purpose**  
   One short paragraph: what documents in this folder are for, who they’re for, and constraints (e.g. “one file per project,” “reference only”).

5. **## What This Is Not**  
   Short clarification of scope: not a plan, not implementation, not a substitute for other doc types. Where out-of-scope content lives (e.g. “→ planning doc”).

6. **## Required Information**  
   Table: `| Section | Content | Example / notes |`. One line or short list per field. “MUST include these.”

7. **## Optional Information**  
   Same table style; add “When to use” or “Example / notes” column. “Include when relevant; omit to save tokens.”

8. **Enums / fixed sets**  
   If the schema uses controlled vocabularies, one **###** per enum: name, short intro, then table (value | meaning). Use same terms in instance docs.

9. **Agent-observed fields**  
   If any section is filled by the agent from context, say so in the table (e.g. “Agent-observed”) and optionally one short sentence in Conventions.

10. **## Conventions**  
    Short bullets: Naming, Location, Skill behavior (pointer only), Format (e.g. one line or short list), Agent use (how to gather/amend).

11. **## REQUIRED_SKILLS** (if applicable)  
    Always stored in the schema. Purpose: list skills (name + location) the agent should pull for context. Format: table (Skill name | Location). Can be added or amended at any point in the full lifecycle when a skill is needed or created—saves the next agent time.

12. **## Minimal Example Structure**  
    Fenced code block with markdown skeleton of an instance doc. Optional closing line: “Optional sections: same heading style. One line or short list per section.”

---

## 4. Design Language & Aesthetic

- **Low token:** Prefer tables and bullets over paragraphs. One line or short list per field in tables.
- **Agent-centric:** Section names and table headers are parseable; “Required” vs “Optional” is explicit; enums use consistent terms.
- **Human-readable:** No jargon without a one-line explanation. “What This Is Not” and “Purpose” stay in plain language.
- **Single source of truth:** The _doc is the only place that defines the schema for that folder; instance docs and skills reference it.
- **Enums:** Framework enums in their particular _doc; separation of concerns, minimal overlap. Instance docs (e.g. project schema) may have optional project-specific enums section.
- **Stable structure:** Same order of sections across _docs (Purpose → What This Is Not → Required → Optional → Enums → Conventions → Example) so agents and humans know where to look.
- **No implementation in _doc:** How to gather data, UX, or which skill does what → separate notes/SKILL files. _Doc = *what* to gather and *how it’s written*, not *how to implement*.

---

## 5. External Patterns We Align With (Discussion)

- **Schema.md (schema.md):** Markdown as single source of truth for structure; one-sentence purpose per entity; tables for definitions; business context in short form; versionable, diff-able, AI-parseable. We apply the same “one place, tables, short text” idea to *document* schemas instead of DB schemas.
- **Frontmatter (YAML/TOML):** Metadata at the top, structured and scannable. We don’t require YAML in _docs, but the idea of “metadata first, then structure” matches our H1 → summary → Purpose → Required/Optional.
- **“What it is / What it isn’t”:** Clarifying scope (Purpose + What This Is Not) reduces misuse and keeps agent context tight. Common in good API/spec docs.
- **MD_FILES (satirical) takeaway:** Proliferation of ad-hoc config formats is costly; having one consistent pattern per doc type (one _doc per folder, same structure) reduces cognitive load and keeps behavior predictable.

---

## 6. Naming Conventions (for later reference)

- **_Doc filename:** `_<foldername or document type contained within>.md` — e.g. `_project-schema.md`, `_planning-docs.md`. Matches the folder or the kind of document the folder holds.
- **Instance files in the folder:** `<project-slug>-<doc-type>.md` — e.g. `sample-project-schema.md`, `sample-project-planning-doc.md` (or `...-planning-docs.md`). No leading number in this convention; numbering (e.g. `001-`, `002-`) is optional and project-specific.

---

## 7. Open Points for Discussion

- **Numbering:** Use `NNN-<slug>-<doc-type>.md` (e.g. `001-sample-project-schema.md`) in some flows vs. plain `<slug>-<doc-type>.md`?
- **Enums:** Framework enums live in their particular _doc (separation of concerns). We don’t expect much overlap; handle overlap structurally when it arises.
- **REQUIRED_SKILLS:** Always in the schema (not only at setup). Can be added or amended anytime in the full lifecycle when a skill is needed or created—saves the next agent time. When we add `_planning-docs.md` or progress _docs, decide if they also declare REQUIRED_SKILLS or only the “entry” schema.
- **Schema version:** Add optional “Schema version” (or similar) line to _docs for traceability.
- **Minimal example:** Keep a markdown code block in the _doc; also keep generic samples in `example-project`. A separate small real project (heavily annotated) will live in the framework as a **living example**—not just abstraction—to test and build out the system.

---

## 8. Where This Lives and How to Use It

- **Succinct design doc:** `ai-docs/_docs-design.md` (reference only; no open points).
- **This file:** `ai-docs/_docs-format-and-design-notes.md` (elaboration, discussion, open points).
- **Use:** When adding a new folder type (e.g. `02-planning-docs/`), create its _doc using the naming convention `_<foldername or doc type>.md` (e.g. `_planning-docs.md`) and follow §3 and §4. Instance files in that folder: `<project-slug>-<doc-type>.md` (e.g. `sample-project-planning-doc.md`). When in doubt, match `_project-schema.md` structure and wording style. Update this notes file if we change the pattern or add new _doc types.
- **Samples vs living example:** Keep `example-project` generic (minimal, abstract samples). A **living example** will be a small real project of ours, heavily annotated and left in the framework to test and build out the system—concrete reference, not just abstraction.
- **Later:** Can be turned into a RULE or a SKILL that tells an agent how to create or validate _docs from this design language.

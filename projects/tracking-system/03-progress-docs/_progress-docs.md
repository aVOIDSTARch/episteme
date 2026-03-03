# PROGRESS DOCS

#### LEADING UNDERSCORE DOCUMENT CONCEPT SUMMARY

**Schema for progress docs.** Defines what every PROGRESS DOC in this folder must contain: stages completed, rationales (decisions made), and enough context so the next or returning agent knows exactly what to do next on the enumerated phased plan. `_` docs = schema, enums, conventions only; no skill behavior.

---

## Purpose

**PROGRESS DOC** = record of work done and where the project stands. Documents which phases/stages from the planning doc (002) are completed, key decisions and rationales, and the explicit “what to do next” so any agent can continue without re-reading everything. One or more progress docs per project (e.g. one file updated over time, or one per session/milestone).

---

## What This Is Not

Not the plan (002) or the completed report (004) or after-action (005). Only progress: what’s done, why we decided as we did, and what’s next.

---

## Required Information

MUST include enough that the next agent can continue from the plan.

| Section | Content | Example / notes |
|--------|---------|------------------|
| **Project** | Name or slug (matches schema and planning doc). | `sample-project` |
| **Planning doc** | Path or reference to the planning doc (002) for this project. | `02-planning-docs/sample-project-planning-doc.md` |
| **Stages completed** | Which phases/stages from the planning doc’s phased plan are done. | “Phase 1, Phase 2”; or “Stage 1.1, 1.2, 2.1.” Reference the enumerated plan. |
| **Decisions / rationales** | Key decisions made and why (enough context not covered elsewhere). | Short list: decision → rationale. So the next agent doesn’t re-debate. |
| **What to do next** | Explicit next step(s) on the enumerated phased plan. | “Start Phase 3: …” or “Complete step 2.2 in planning doc.” Unambiguous for returning agent. |
| **Commits by stage** | For each completed phase/stage: git commit timestamp and message when that section was tested and committed. | One line or short table per stage (e.g. Phase 1: `YYYY-MM-DD HH:MM` — "message"). Ties progress to repo history. |
| **Test names by stage** | For each milestone: array of test names that apply to that phase. | e.g. Phase 1: `[ "test_init", "test_parse" ]` or bullet list. |
| **Test run results by stage** | For each milestone: result of running the tests (e.g. passed/failed, count, or summary). | e.g. Phase 1: all passed; Phase 2: 3 passed, 1 skipped. |

---

## Optional Information

| Section | Content | When to use |
|--------|---------|-------------|
| **Schema doc** | Path or reference to the project schema (01) for this project. | So the next agent can pull schema and REQUIRED_SKILLS. |
| **Session or date** | When this progress was recorded (e.g. YYYY-MM-DD or session id). | For ordering or audit. |
| **Blockers / open items** | Current blockers or open items that affect “what to do next.” | When they exist. |
| **Context not elsewhere** | Brief context the next agent needs that isn’t in the plan or schema. | When it’s essential and not obvious from code/docs. |

---

## Conventions

- **Naming:** `_progress-docs.md` = this _doc. Instance: `<project-slug>-progress.md` or `<project-slug>-progress-<date>.md` (e.g. `sample-project-progress.md`). Prefer one progress file per project, updated as work completes; use multiple files only if needed for history.
- **Location:** Progress docs live in this folder (03-progress-docs). When project is completed, see 004 for moving into a project-named folder.
- **Format:** Markdown; required sections as level-2 headings. “What to do next” must map clearly to a phase/step in the planning doc.
- **Agent use:** Update after meaningful work. When a phase/stage is tested and committed, add under Commits by stage (timestamp + message), Test names by stage (array of test names for that milestone), and Test run results by stage (run results for that milestone). Always set “What to do next” so the next agent (or same agent later) can continue without re-deriving from the plan.

---

## Minimal Example Structure

```markdown
# PROGRESS: <project-slug>

## Project
<slug>

## Planning doc
<path to 002 planning doc>

## Schema doc
<path to 001 project schema> (optional)

## Stages completed
- Phase 1: <name> — done
- Phase 2: <name> — done

## What to do next
Start Phase 3: <name>. First step: ...

## Commits by stage
- Phase 1: <timestamp> — <commit message>
- Phase 2: <timestamp> — <commit message>

## Test names by stage
- Phase 1: [ <test name>, <test name>, ... ]
- Phase 2: [ <test name>, ... ]

## Test run results by stage
- Phase 1: <e.g. all passed / 2 passed, 1 skipped>
- Phase 2: <result summary>

## Decisions / rationales
- Decision: Use X instead of Y. Rationale: ...
- Decision: ...

## Session / date
YYYY-MM-DD (optional)

## Blockers / open items
(optional)

## Context not elsewhere
(optional; only if needed for next agent)
```

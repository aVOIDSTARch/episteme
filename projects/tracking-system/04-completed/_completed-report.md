# COMPLETED REPORT

#### LEADING UNDERSCORE DOCUMENT CONCEPT SUMMARY

**Schema for the completed report.** Defines the comprehensive, standardized report for a finished project. When a project is completed, planning doc (002), progress doc(s) (003), and this completed report live in a folder named after the project. The report captures issues not in planning, agent shortcomings, token usage, and other learnings so we can improve the system after every project. `_` docs = schema, enums, conventions only.

---

## Purpose

**COMPLETED REPORT** = standardized wrap-up for a project. One file per project when the project is done. Create when the project is marked done (e.g. success criteria met or user confirms). Includes what went wrong or surprised us (issues not in planning), agent limitations, token usage, and other metrics or notes—so we can improve process, skills, and docs. Human- and agent-readable; feeds into after-action (005) for recommendations and ideas.

---

## What This Is Not

Not the plan (002), progress (003), or after-action (005). Only the factual report on how the project finished and what we learned. After-action uses this to suggest improvements, related projects, and new skills.

---

## Required Information

MUST include these so every project contributes to system improvement.

| Section | Content | Example / notes |
|--------|---------|------------------|
| **Project** | Name or slug (matches schema, planning, progress). | `sample-project` |
| **Completed date** | When the project was marked completed (YYYY-MM-DD). | For ordering and metrics. |
| **Outcome summary** | One short paragraph: what was delivered vs. plan; overall result. | Did we meet success criteria? |
| **Issues not in planning** | Problems, surprises, or gaps that weren’t in the plan. | Short list; what we’d add to planning next time. |
| **Agent shortcomings** | Where the agent(s) fell short: wrong assumptions, missed context, poor suggestions, etc. | Short list; improves prompts, skills, or docs. |
| **Token usage** | Token usage if available (total, by phase, or rough estimate). | Helps tune context and doc size. |

---

## Optional Information

| Section | Content | When to use |
|--------|---------|-------------|
| **Planning doc** | Path to the planning doc (002) for this project. | So the completed bundle is self-describing; 005 can resolve. |
| **Progress doc(s)** | Path(s) to the progress doc(s) (003) for this project. | So the completed bundle is self-describing. |
| **Deviations from plan** | What we did differently from the phased plan and why. | When significant. |
| **Final test summary** | Final test run status (e.g. all passing, coverage note). | Quality snapshot at completion. |
| **Release version or tag** | Git tag, version number, or release id when shipped. | When project is released or versioned. |
| **What worked well** | Process or tooling that helped. | For reuse. |
| **Recommendations for next project** | Quick wins to carry forward. | Feeds 005. |
| **References** | Links to planning doc, progress docs, repo, completed report. | When useful for 005 or audit. |

---

## Conventions

- **Naming:** `_completed-report.md` = this _doc. Instance: `<project-slug>-completed.md` (e.g. `sample-project-completed.md`).
- **Location:** When a project is completed, create a folder named after the project (e.g. under `04-completed/sample-project/`). Move or copy the planning doc (002), progress doc(s) (003), and this completed report into that folder. So the project-named folder contains: planning doc, progress doc(s), and `<project-slug>-completed.md`.
- **Format:** Markdown; required sections as level-2 headings. Keep lists short and scannable.
- **Agent use:** Fill when closing a project. Use for retrospectives and as input to after-action (005).

---

## Minimal Example Structure

```markdown
# COMPLETED: <project-slug>

## Project
<slug>

## Completed date
YYYY-MM-DD

## Outcome summary
<one short paragraph: delivered vs. plan; overall result>

## Issues not in planning
- Issue 1
- Issue 2

## Agent shortcomings
- Shortcoming 1 (e.g. missed X, assumed Y)
- Shortcoming 2

## Token usage
<total or by phase if available; or “not tracked”>

## Deviations from plan
(optional)

## What worked well
(optional)

## Recommendations for next project
(optional)
```

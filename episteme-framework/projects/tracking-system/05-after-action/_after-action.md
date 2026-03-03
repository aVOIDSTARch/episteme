# AFTER-ACTION

#### LEADING UNDERSCORE DOCUMENT CONCEPT SUMMARY

**Schema for the after-action doc.** Defines what every AFTER-ACTION doc must contain: project improvements, related projects that could be started, and new SKILLs to develop. Used to generate more productivity and ideas after a project is completed. `_` docs = schema, enums, conventions only.

---

## Purpose

**AFTER-ACTION** = forward-looking summary after a project is done. One doc per completed project. Recommends project improvements, related projects to start, and new SKILLs to develop. Input: completed report (004) and planning (002). Output: actionable ideas and next steps so we improve the system and spawn follow-on work.

---

## What This Is Not

Not the completed report (004)—that’s factual. After-action is recommendations and ideas. Not a new plan; it suggests directions and skills, not a phased plan for one project.

---

## Required Information

MUST include these so every completed project feeds productivity and ideas.

| Section | Content | Example / notes |
|--------|---------|------------------|
| **Project** | Name or slug of the completed project. | `sample-project` |
| **Completed report** | Path or reference to the completed report (004) for this project. | `04-completed/sample-project/sample-project-completed.md` or project folder path. |
| **Project improvements** | Recommendations to improve this project (code, docs, process, or product). | Short list; actionable. |
| **Related projects to start** | Projects that could be started that relate to this one. | Short list; one line each or brief description. Generates ideas. |
| **New SKILLs to develop** | SKILLs.md that should be created or extended based on this project. | Name + one-line purpose; e.g. “SETUP_NEW_PROJECT — create project schema from user input.” |

---

## Optional Information

| Section | Content | When to use |
|--------|---------|-------------|
| **Other ideas** | Ideas that don’t fit above: tools, workflows, docs. | When worth capturing. |
| **Priorities** | Which of the above to do first (if any). | When ordering matters. |
| **References** | Links to completed report, planning, repo. | When useful. |

---

## Conventions

- **Naming:** `_after-action.md` = this _doc. Instance: `<project-slug>-after-action.md` (e.g. `sample-project-after-action.md`).
- **Location:** After-action docs can live in this folder (05-after-action) or in the project-named folder alongside the completed report; decide per workflow. Reference the completed report so agents have context.
- **Format:** Markdown; required sections as level-2 headings. Keep lists short; focus on actionable items and ideas.
- **Agent use:** Create after the completed report (004) exists. Use completed report + planning as input. Prefer to derive Project improvements and New SKILLs from 004’s Recommendations and Issues not in planning. Output feeds backlog, skills-to-make-first, or idea lists.

---

## Minimal Example Structure

```markdown
# AFTER-ACTION: <project-slug>

## Project
<slug>

## Completed report
<path to 004 completed report>

## Project improvements
- Improvement 1
- Improvement 2

## Related projects to start
- Project idea 1: one-line description
- Project idea 2: ...

## New SKILLs to develop
- SKILL name: one-line purpose (e.g. path or scope)
- SKILL name: ...

## Other ideas
(optional)

## Priorities
(optional)
```

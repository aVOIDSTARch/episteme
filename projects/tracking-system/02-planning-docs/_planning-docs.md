# PLANNING DOCS

#### LEADING UNDERSCORE DOCUMENT CONCEPT SUMMARY

**Schema for the planning doc.** Defines what every PLANNING DOC in this folder must contain: one well-organized planning and design document per project, with required structure and addenda (open questions, recommendations, concerns). `_` docs = schema, enums, conventions only; no skill behavior. Skill behavior for creating/updating planning docs → notes or SKILL if added.

---

## Purpose

**PLANNING DOC** = the single planning and design document for a project. One file per project. Create after the project schema (01) exists and scope is agreed. Contains the enumerated phased plan the next agent uses to know what to do; out of scope, dependencies, success criteria; and addenda for open questions, recommendations, concerns. Human- and agent-readable; enough structure that progress docs (003) and completion (004) can reference phases and decisions.

---

## What This Is Not

Not the project schema (that’s 01). Not progress updates (those are 003) or the completed report (004) or after-action (005). Only the plan and design for the work.

---

## Required Information

MUST include these. One doc per project; well-organized sections.

| Section | Content | Example / notes |
|--------|---------|------------------|
| **Project** | Name or slug (matches schema). | `sample-project`, `my-app` |
| **Plan summary** | One short paragraph: what we’re building and why. | High-level goal and outcome. |
| **Out of scope** | What this project explicitly does not cover. | Short list; avoids scope creep. |
| **Phased plan** | Enumerated phases/stages with enough detail for the next agent to know what to do next. | Numbered phases; each phase: name, goal, key deliverables or steps. 003 progress docs reference these. |
| **Dependencies** | What this project depends on (other projects, systems, decisions). | Short list or table. |
| **Success criteria** | How we know the project is done. | Short list; testable or checkable. |

---

## Optional Information

Include when relevant.

| Section | Content | When to use |
|--------|---------|-------------|
| **Assumptions** | Assumptions about env, scope, or constraints. | When they affect the plan. |
| **Risks / mitigations** | Known risks and how we’ll handle them. | When worth recording. |
| **References** | Links or paths to schema, specs, external docs. | When agents need to pull context. |
| **Project vocabulary** | Term → one-line definition (if not in schema). | When plan uses domain jargon. |

---

## Addenda (end of doc)

After the main structure, include these subsections so nothing is lost. Short bullets or lists.

| Subsection | Content |
|------------|---------|
| **Open questions** | Unresolved questions that need an answer during the project. |
| **Recommendations** | Suggestions (tech, process, or product) to consider. |
| **Concerns** | Worries, blockers, or caveats worth tracking. |

---

## Conventions

- **Naming:** `_planning-docs.md` = this _doc. Instance: `<project-slug>-planning-doc.md` (e.g. `sample-project-planning-doc.md`).
- **Location:** Planning docs live in this folder (02-planning-docs). When a project is completed, see 004 for moving into a project-named folder.
- **Format:** Markdown; required sections as level-2 headings. Phased plan is enumerated (e.g. Phase 1, Phase 2) so 003 progress can reference “Phase 2” or “Stage 3.”
- **Agent use:** Create or update from schema + user/agent discussion. Progress docs (003) refer to phases in this plan; completed report (004) summarizes outcomes against this plan.

---

## Minimal Example Structure

```markdown
# PLAN: <project-slug>

## Project
<slug>

## Plan summary
<one short paragraph>

## Out of scope
- Item 1
- Item 2

## Phased plan
### Phase 1: <name>
- Goal: ...
- Deliverables / steps: ...

### Phase 2: <name>
...

## Dependencies
- Dependency 1
- Dependency 2

## Success criteria
- Criterion 1
- Criterion 2

---

## Addenda

### Open questions
- Question 1
- Question 2

### Recommendations
- Recommendation 1

### Concerns
- Concern 1
```

Optional sections: same heading style. One line or short list per item.

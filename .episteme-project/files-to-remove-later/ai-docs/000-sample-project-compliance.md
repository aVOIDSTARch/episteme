# Sample project: compliance & adherence review

Review of `example-project/` files against the tracking-system _doc schemas (01–05). Reference: `projects/tracking-system/0X-*/_*.md` and `ai-docs/_docs-design.md`.

---

## 001-sample-project-schema.md (vs 01-project-schemas / _project-schema.md)

| Requirement | Status | Notes |
|-------------|--------|--------|
| **Required:** Project, Summary, Owner, Type, Stack, Created | ✓ | All present; one line or short list. |
| **Optional:** Deployment, Dev environment, Agents/models, Project state, Read first, Entry points, REQUIRED_SKILLS, Project-specific enums, Project vocabulary, Schema version | ✓ | All used; appropriate for example. |
| Deployment uses framework enum terms | ✓ | "CLI", "Web Application" from _project-schema enum. |
| Project state from enum | ✓ | Greenfield. |
| REQUIRED_SKILLS table (name + location) | ✓ | Three skills with paths. |
| Section order / format | ✓ | Matches minimal example; level-2 headings. |

**Adherence:** Compliant.

---

## 002-sample-project-planning-doc.md (vs 02-planning-docs / _planning-docs.md)

| Requirement | Status | Notes |
|-------------|--------|--------|
| **Required:** Project, Plan summary, Out of scope, Phased plan, Dependencies, Success criteria | ✓ | All present. |
| Phased plan enumerated (Phase 1–4) with goal + deliverables | ✓ | Each phase has name, goal, deliverables/steps. |
| **Addenda:** Open questions, Recommendations, Concerns | ✓ | All three subsections at end of doc. |
| Section order / format | ✓ | Main structure then Addenda with ###. |

**Adherence:** Compliant.

---

## 003-sample-project-progress-reporting.md (vs 03-progress-docs / _progress-docs.md)

| Requirement | Status | Notes |
|-------------|--------|--------|
| **Required:** Project, Planning doc, Stages completed, Decisions/rationales, What to do next, Commits by stage, Test names by stage, Test run results by stage | ✓ | All present. |
| **Optional:** Schema doc, Session/date, Blockers, Context not elsewhere | ✓ | All present. |
| "What to do next" placement | ✓ | Immediately after Stages completed (agent re-entry). |
| Planning doc path | ✓ | Points to 002. |
| Commits by stage (timestamp + message) | ✓ | One per phase. |
| Test names / results by stage | ✓ | Phase 1 empty; Phase 2 and 3 populated. |
| What to do next maps to plan | ✓ | "Start Phase 4: Tests & polish" with first step. |

**Adherence:** Compliant.

---

## 004-sample-project-completed.md (vs 04-completed / _completed-report.md)

| Requirement | Status | Notes |
|-------------|--------|--------|
| **Required:** Project, Completed date, Outcome summary, Issues not in planning, Agent shortcomings, Token usage | ✓ | All present. |
| **Optional:** Planning doc, Progress doc(s), Deviations, Final test summary, Release version or tag, What worked well, Recommendations for next project | ✓ | All used. |
| Completed date YYYY-MM-DD | ✓ | 2025-02-16. |
| Outcome references success criteria | ✓ | "Success criteria met." |

**Adherence:** Compliant.

---

## 005-sample-project-after-action-report.md (vs 05-after-action / _after-action.md)

| Requirement | Status | Notes |
|-------------|--------|--------|
| **Required:** Project, Completed report, Project improvements, Related projects to start, New SKILLs to develop | ✓ | All present. |
| **Optional:** Other ideas, Priorities | ✓ | Both present. |
| Completed report path | ✓ | Points to 004. |
| New SKILLs (name + purpose) | ✓ | CARGO_FUZZ_SKILL, RUST_README_COMPLIANCE with one-line purpose. |

**Adherence:** Compliant.

---

## 000-sample-project.md

No schema; folder index. Lists file names and short summaries. ✓

---

## Cross-cutting checks

| Check | Status |
|-------|--------|
| Project slug consistent across docs | ✓ | "widget-control-program" in 001–005. |
| Phase names match between 002 and 003 | ✓ | Phase 1–4 same names (Scaffold & types, Core control logic, CLI & I/O, Tests & polish). |
| 003 references 002; 004 references 002 and 003; 005 references 004 | ✓ |
| One line or short list per field (low-token) | ✓ |
| No long prose; tables/lists where appropriate | ✓ |

---

## Naming note (no change required)

Instance file names use **sample-project** (e.g. `001-sample-project-schema.md`) as the example placeholder; **content** uses project slug **widget-control-program** throughout. The _doc convention is `<project-slug>-<doc-type>.md` (e.g. `widget-control-program-schema.md`). For a real project in its own folder, files would typically be named after the slug; here the "sample-project" prefix keeps the example generic and the numbering (001–005) clear. Documented for clarity only.

---

## Summary

All five instance docs (001–005) comply with their respective _doc schemas. Required sections present; optional sections used appropriately; cross-references and phase alignment correct; "What to do next" placement in 003 supports agent re-entry. No fixes required.

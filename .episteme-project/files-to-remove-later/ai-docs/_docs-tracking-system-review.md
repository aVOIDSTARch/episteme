# Progressive Review: Tracking-System _Docs

**Purpose:** Step-by-step review of all _docs in `projects/tracking-system/` (01–05) for design/format adherence, project-timeline and agent logic, process duplication, and software-engineering coverage. Findings and fixes.

---

## 1. Design & Format Adherence

**Reference:** `ai-docs/_docs-design.md` (template: H1 → H4 summary → Purpose → What This Is Not → Required table → Optional table → Enums → Conventions → REQUIRED_SKILLS if applicable → Minimal Example).

| _Doc | H1 | H4 | Purpose | What Not | Req/Opt tables | Enums | Conventions | REQUIRED_SKILLS | Minimal Ex | Notes |
|------|----|----|---------|----------|----------------|-------|-------------|-----------------|------------|--------|
| 01 _project-schema | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ (Project state, Deployment; agent-observed separate) | ✓ | ✓ (### not ##) | ✓ | REQUIRED_SKILLS is ### under Optional; design says ##. Acceptable. |
| 02 _planning-docs | ✓ | ✓ | ✓ | ✓ | ✓ | — | ✓ | — | ✓ | Addenda (Open questions, Recommendations, Concerns) are instance-level; not in template. OK. |
| 03 _progress-docs | ✓ | ✓ | ✓ | ✓ | ✓ | — | ✓ | — | ✓ | — |
| 04 _completed-report | ✓ | ✓ | ✓ | ✓ | ✓ | — | ✓ | — | ✓ | — |
| 05 _after-action | ✓ | ✓ | ✓ | ✓ | ✓ | — | ✓ | — | ✓ | — |

**F1 — Naming consistency (01):** Conventions say instance naming `NNN-<project-slug>-schema.md`; design says numbering is optional. **Fix:** In 01 Conventions, state that `NNN-` is optional (e.g. "Instance: `<project-slug>-schema.md`; optional prefix `NNN-` for ordering").

---

## 2. Information Grouping for Project Timeline

**Intended flow:** 01 (setup) → 02 (plan) → 03 (progress) → 04 (completed report) → 05 (after-action).

| Handoff | Documented? | Gap / fix |
|---------|--------------|-----------|
| 01 → 02 | Schema has Read first, Entry points, Constraints. | ✓ Plan is created from schema + discussion. |
| 02 → 03 | Plan has Phased plan; 03 references "planning doc" path. | ✓ Stages completed and "What to do next" reference phases. |
| 03 → 04 | Progress has commits, tests by stage. | ✓ Completed report has Outcome summary, Issues, Agent shortcomings. |
| 04 → 05 | 05 requires "Completed report" path. | ✓ After-action uses 004 as input. |

**F2 — When to create 002 / 004:** No explicit trigger. **Fix:** In 02 Purpose or Conventions add: "Create after project schema (01) exists and scope is agreed." In 04 Purpose or Conventions add: "Create when project is marked done (e.g. success criteria met or user confirms)."

**F3 — 003 file strategy:** "One or more progress docs" is ambiguous (one file updated vs many). **Fix:** In 03 Conventions add: "Prefer one progress file per project, updated as work completes; use multiple files only if needed for history (e.g. `<slug>-progress-<date>.md`)."

---

## 3. Information Grouping for Agent Design Logic

**Re-entry goal:** Agent opening a project should quickly get (1) context (schema), (2) plan (002), (3) current state and next action (003).

| Check | Status | Gap / fix |
|-------|--------|-----------|
| 003 "What to do next" discoverable | In Required table and example. | **F4:** In 03 minimal example, put **What to do next** immediately after **Stages completed** (and before Commits/Tests/Decisions) so the re-entering agent sees the next action first. |
| Cross-references | 03 → 02 path. 05 → 04 path. | **F5:** 003 Optional: add "Schema doc" path so agent can pull 001. 004 Required or Optional: add "Planning doc" and "Progress doc(s)" paths so the completed bundle is self-describing; 005 can then resolve planning from 004. |
| Single identity | Project/slug in every doc. | ✓ Good. |

---

## 4. Process Duplication

| Concept | Where it appears | Verdict |
|---------|------------------|--------|
| Project / slug | 01, 02, 03, 04, 05 | Required in each; no duplication issue. |
| Recommendations | 02 Addenda "Recommendations"; 004 "Recommendations for next project"; 005 "Project improvements" + "New SKILLs" | 002 = in-plan suggestions. 004 = quick wins (factual). 005 = structured output. Mild overlap 004/005; keep both: 004 captures raw, 005 turns into actions. |
| Out of scope | 02 only | ✓ |
| Success criteria | 02 only; 004 Outcome summary implies comparison | ✓ |
| Decisions | 03 only | ✓ |

No harmful duplication. Optional: in 005 Conventions add "Prefer to derive Project improvements and New SKILLs from 004’s Recommendations and Issues not in planning."

---

## 5. Software Engineering Processes: Coverage & Gaps

| Process | Where addressed | Gap / recommendation |
|---------|------------------|------------------------|
| **Testing** | 003: Test names by stage, Test run results by stage | ✓ Good. **F6:** 004 Optional: add "Final test summary" (e.g. all tests passing, coverage note) so completed report has a test/quality snapshot. |
| **Version control / commits** | 003: Commits by stage (timestamp + message) | ✓ Good. Optional: "Branch or PR by stage" if workflows use branches; not required. |
| **Definition of done** | 002: Success criteria. 003: test results per stage. 004: Outcome summary | ✓ Good. |
| **Dependencies** | 002: Dependencies. 001: Repo path, Constraints | ✓ Good. |
| **Risks** | 002 Optional: Risks / mitigations | ✓ Good. |
| **Code review** | Not mentioned | Optional in 003 (e.g. "Review status by stage") or 004 ("Review completed") for team workflows; omit for agent-only if desired. |
| **Rollback / reversibility** | Not mentioned | Optional in 002 (e.g. under Risks or "Rollback plan" for critical releases). Low priority. |
| **Security** | 001: Constraints can include security. 004: Issues not in planning can capture security issues | Acceptable. Optional: 002 "Assumptions" or "Constraints" could explicitly mention security if needed. |
| **Performance / observability** | Not mentioned | Optional in 002 (e.g. performance criteria in Success criteria or Assumptions) or 004 (if discovered). Low priority. |
| **Documentation** | 001: Read first. 002: References. 004: Outcome summary can mention docs | Optional: 002 Phased plan could encourage "deliverables: docs" where relevant. |
| **Release / version tag** | Not mentioned | **F7:** 004 Optional: add "Release version or tag" (e.g. git tag, version number) when project is shipped. |

---

## 6. Summary of Fixes to Apply

| Id | _Doc | Change |
|----|------|--------|
| F1 | 01 | Conventions: instance naming — state `NNN-` optional. |
| F2 | 02, 04 | 02: When to create (after 01 + scope agreed). 04: When to create (when project marked done). |
| F3 | 03 | Conventions: prefer one progress file per project, updated over time. |
| F4 | 03 | Minimal example: move "What to do next" block immediately after "Stages completed." |
| F5 | 03, 04 | 03 Optional: "Schema doc" path. 04 Optional: "Planning doc" and "Progress doc(s)" paths. |
| F6 | 04 | Optional table: "Final test summary" (and/or coverage). |
| F7 | 04 | Optional table: "Release version or tag." |

---

## 7. Fixes Applied (this pass)

| Id | Applied |
|----|---------|
| F1 | 01 Conventions: instance naming now states optional `NNN-` prefix. |
| F2 | 02 Purpose: "Create after project schema (01) exists and scope is agreed." 04 Purpose: "Create when project is marked done (e.g. success criteria met or user confirms)." |
| F3 | 03 Conventions: "Prefer one progress file per project, updated as work completes; use multiple files only if needed for history." |
| F4 | 03 Minimal example: "What to do next" moved immediately after "Stages completed" for agent re-entry. |
| F5 | 03 Optional: "Schema doc" path added. 04 Optional: "Planning doc" and "Progress doc(s)" paths added; "Final test summary" and "Release version or tag" added. |
| F6 | 04 Optional: "Final test summary" added. |
| F7 | 04 Optional: "Release version or tag" added. |
| — | 05 Conventions: "Prefer to derive Project improvements and New SKILLs from 004's Recommendations and Issues not in planning." |

---

## 8. Checklist for Future _Doc Additions

- [ ] Follow template order (Purpose, What This Is Not, Required, Optional, Conventions, Minimal Example).
- [ ] Ensure at least one cross-reference to predecessor doc (path or "see 0X") where the timeline depends on it.
- [ ] For agent re-entry: put "what to do next" or equivalent high in instance structure.
- [ ] Avoid requiring the same field in two _docs without designating one as canonical (e.g. project slug is identity in each; planning doc path is canonical in 03).
- [ ] Consider optional slots for: final test/quality snapshot (004), release version (004), schema path when progress doc is opened (003).

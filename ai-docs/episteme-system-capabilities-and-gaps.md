# Episteme: system capabilities, should-do list, and gaps

**Purpose:** Single checklist of everything the episteme system is intended to do (from meta-agent, tracking system, ideas-engine, language-style-guides, my-skills). Mark complete vs not-yet so we can vet and prioritize. **Cascading EPISTEME_SKILLS** → [EPISTEME_SKILLS_TREE.md](EPISTEME_SKILLS_TREE.md).

**Audience:** Humans and agents. Use when deciding what to build next or whether something is in scope.

---

## 1. Meta-agent & navigation

| # | Capability | Status | Notes / source |
|---|------------|--------|----------------|
| 1.1 | **/menu** — Main nav: Projects (slash commands, new project, back), Ideas, Something else → prompt | Not automated | meta-agent; agent implements |
| 1.2 | **/incompletes** — Menu of projects with incomplete items; offer to continue or return | Not automated | Scan `~/completed-projects/*-appendix.md` |
| 1.3 | **/do-more** — Menu of projects with next/enhancement ideas; propose plan or return | Not automated | meta-agent |
| 1.4 | **/whats-next** — Combined [INCOMPLETE] and [ENHANCEMENT] by project; then act or return | Not automated | meta-agent |
| 1.5 | Cross-project guidance in one place; project CLAUDE.md points to canonical repo (episteme) | Doc only | meta-agent |
| 1.6 | Language/project-type guides: `<language>/<project-slug>.md` or skill `language-project-slug`; pull for project | Partial | Some guides in episteme; skills not all created |
| 1.7 | Conventions: paths (~/ vs root), /% commentary resolution, AskUserQuestion menus | Doc only | meta-agent |

---

## 2. Skills marketplace & safety

| # | Capability | Status | Notes / source |
|---|------------|--------|----------------|
| 2.1 | Consult skilsmp.com for unfamiliar tools/techniques; follow skill standard (folder + SKILL.md, YAML, etc.) | Doc only | meta-agent |
| 2.2 | Before install: ask permission, describe use | Doc only | meta-agent |
| 2.3 | Assess risks in `~/skill.md`: security, trust, dependencies, conflicts; present summary | Doc only | meta-agent |
| 2.4 | If significant risk: suggest alternatives/sandbox; install only after explicit approval | Doc only | meta-agent |
| 2.5 | Optionally keep assessments in local markdown (future: skills-assessment repo) | Not done | meta-agent |

---

## 3. Project workflow (planning, progress, handoff)

| # | Capability | Status | Notes / source |
|---|------------|--------|----------------|
| 3.1 | **Planning** — Agent chooses structure; goals, approach, decisions, files, risks, open questions | Schema only | _planning-docs.md; agent implements |
| 3.2 | **Progress** — At milestones: git commit + append to progress artifact; entry = done + left | Schema only | _progress-docs.md |
| 3.3 | **Handoff** — Copy plan to completed-projects; appendix with incomplete items and next steps | Doc only | meta-agent |
| 3.4 | File-system artifacts as source of truth (plans, progress, completed-projects, ideas) | Doc only | meta-agent |

---

## 4. Project tracking system (schemas & docs)

| # | Capability | Status | Notes / source |
|---|------------|--------|----------------|
| 4.1 | **Project schema (001)** — Gather and record: Project, Summary, Owner, Type, Stack, Created; optional Deployment, Dev env, Agents, Constraints, Repo path, Project state, Read first, Entry points, REQUIRED_SKILLS | Schema done | _project-schema.md |
| 4.2 | **SETUP_NEW_PROJECT** — Create/update schema from user input + agent-observed data; multiple choice, confirm observed, sanity-check, divergent pathways (name suggestion, set up env later) | Not done (skill) | project-schema-setup-skill-notes.md, skills-to-make-first |
| 4.3 | **Planning doc (002)** — One plan per project: plan summary, out of scope, phased plan, dependencies, success criteria; addenda (open questions, recommendations, concerns) | Schema done | _planning-docs.md |
| 4.4 | **Progress doc (003)** — Stages completed, decisions/rationales, what to do next, commits by stage, test names/results by stage | Schema done | _progress-docs.md |
| 4.5 | **Completed report (004)** — When project done: outcome summary, issues not in planning, agent shortcomings, token usage; move planning + progress + completed into project-named folder | Schema done | _completed-report.md |
| 4.6 | **After-action (005)** — From completed report + planning: project improvements, related projects to start, new SKILLs to develop, other ideas | Schema done | _after-action.md |
| 4.7 | **TRACKING_SYSTEM_COMPLIANCE** — Check project docs 001–005 vs _docs; report compliance | Not done (skill) | skill-creation-notes §5, skills-to-make-first |

---

## 5. Ideas system

| # | Capability | Status | Notes / source |
|---|------------|--------|----------------|
| 5.1 | **Location** — `~/ideas/*.md` (or IDEAS_ROOT); one topic per file | Spec done | ideas-engine/README, meta-agent |
| 5.2 | **Format** — Verbatim (immutable) + Claude/Agent interpretation; append-only; optional id, created_at | Schema done | _idea-file-schema.md |
| 5.3 | **/ideas** — Menu of topics → show entries; option **Synthesize** (e.g. 10–15 project ideas from topic); Return to topic list / Return to prompt | Not automated | ideas-engine/AGENT-INSTRUCTIONS |
| 5.4 | **/add-idea <text>** — Match or create topic; append Verbatim + interpretation; confirm | Not automated | ideas-engine/AGENT-INSTRUCTIONS |
| 5.5 | Suggest topic merge/split occasionally | Doc only | ideas-engine, meta-agent |
| 5.6 | Future-app invariants: id, topic, verbatim, claude_interpretation, created_at; 1:1 topic files; TypeScript API with markdown as source | Doc only | ideas-engine, meta-agent |
| 5.7 | **list-topics.sh** — Optional script to list topics from Ideas root | Done | ideas-engine/list-topics.sh |

---

## 6. Language / code style guides

| # | Capability | Status | Notes / source |
|---|------------|--------|----------------|
| 6.1 | **Code guide master format** — Each code-guide-*.ai: Overview (incl. guide quality rating), Sources table, Code guide (Consensus + Per-source), Notes for agent, optional Appendix | Spec done | code-guide-master-file.md |
| 6.2 | **Guide quality rating** — Required 1–5 (or star) + synopsis at top of Overview; re-score when sources/conflicts change | Spec done | code-guide-master-file, format-analysis |
| 6.3 | **Navigate to right guide** — Resolve language/framework to code-guide-<topic>.ai from public/master/ layout | Doc only | code-guide-format-analysis §4 |
| 6.4 | **Apply consensus first, then per-source** when repo states a style; cite sources; suggest refresh if stale | Doc only | code-guide-format-analysis §4 |
| 6.5 | **Scrape/merge** — scrape_guides.py, merge_google_into_master.py; populate raw content; clean and merge into master .ai files | Scripts done | language-style-guides/ |
| 6.6 | **Transform raw guide to master format** — Overview, Sources, Consensus, Per-source, Notes, Appendix (or archive) | Partial | C#, ObjC transformed; others not |
| 6.7 | **BUILD_LANG_GUIDES_COLLECTION** (or equivalent) — High-level: ensure guides exist, transformed, scored; orchestrate navigate → confirm match → apply | Not done (skill) | Inferred from format-analysis |

---

## 7. My-skills (skill definition, standard, imported, episteme)

| # | Capability | Status | Notes / source |
|---|------------|--------|----------------|
| 7.1 | **Skill definition schema** — SKILL.md: Name, Description, When to use, Instructions; optional Read first, Inputs/outputs, Original source URI, Integrity hash | Schema done | _skill-definition.md |
| 7.2 | **Skill standard** — Folder design, structure rules, provenance/integrity | Schema done | _skill-standard.md |
| 7.3 | **CREATE_OR_VALIDATE_SKILL** — Create or validate skill folder vs definition + standard | Not done (skill) | skill-creation-notes §2, skills-to-make-first |
| 7.4 | **IMPORTED_SKILL_META_DOC** — Meta-doc per imported skill: Original source URI, Location, Risk assessment, Conversation notes, Integrity hash | Not done (skill) | _imported-skills.md, skill-creation-notes §3 |
| 7.5 | **EPISTEME_SKILL_SCAFFOLD** — Scaffold episteme skill folder + SKILL.md stub | Not done (skill) | _episteme-skills.md, skill-creation-notes §4 |
| 7.6 | **SKILL_INTEGRITY_CHECK** — Recompute hash; compare to stored; report tampering/prompt-injection risk | Future | skills-to-make-first |
| 7.7 | **SKILL_STANDARD_SYNC** — Compare local skill-standard to website; report drift | Future | skill-creation-notes §6 |
| 7.8 | At project end: add SKILL(s) per skilsmp.com when appropriate; ask when ready | Doc only | meta-agent |

---

## 8. Working style & coding standards

| # | Capability | Status | Notes / source |
|---|------------|--------|----------------|
| 8.1 | Ask clarifying questions; suggest improvements before non-trivial work; get buy-in | Doc only | meta-agent |
| 8.2 | TypeScript for new code; TypeDoc; structured logging; user-facing errors; comments (why); modularity; tests (vitest); docs; markdown ToC + linter | Doc only | meta-agent |
| 8.3 | After each change: linter, style, fix errors, buildable; user agreement; suggest commit message after small logical changes | Doc only | meta-agent |

---

## 9. Ai-docs review: gaps and missing pieces

| Gap | Severity | Suggestion |
|-----|----------|------------|
| **skills-to-make-first.md** lives in `.episteme-project/files-to-remove-later/ai-docs/` | Medium | Move or copy to `ai-docs/` so it’s in main tree; or keep single source in ai-docs and deprecate the copy. |
| **skill-creation-notes.md** same location | Medium | Same as above; central place for “how to create SKILLs.” |
| **project-schema-setup-skill-notes.md** same location | Medium | Referenced by _project-schema; should be discoverable (ai-docs or next to schema). |
| **_docs-format-and-design-notes.md**, **_docs-design.md**, **_docs-tracking-system-review.md** in files-to-remove-later | Low | If these define _doc design and compliance, consider moving to ai-docs or projects/tracking-system so agents find them. |
| **Single “index” of all _docs** (project schema, planning, progress, completed, after-action, idea-file, skill-definition, episteme-skills, etc.) | Low | One ai-docs index file listing each _doc and path would help agents. |
| **Code guide “apply to file”** — No explicit skill for “apply code guide to this file” (load guide → check relevance → apply consensus/per-source) | Low | Could be a leaf skill under BUILD_LANG_GUIDES_COLLECTION or ANALYZE_CODE_STYLE. |

---

## 10. Summary for vetting

- **Done / in place:** Schemas (_project-schema, _planning-docs, _progress-docs, _completed-report, _after-action, _idea-file-schema, _skill-definition, _skill-standard, _episteme-skills, _imported-skills); code-guide master format and analysis; ideas-engine spec and list-topics.sh; scrape/merge scripts; meta-agent and ideas slash-command spec; example project and FLIP_WIDGET.
- **Not done (skills):** SETUP_NEW_PROJECT, EPISTEME_DESIGN, Meta-agent template, Set up environment, CREATE_OR_VALIDATE_SKILL, IMPORTED_SKILL_META_DOC, EPISTEME_SKILL_SCAFFOLD, TRACKING_SYSTEM_COMPLIANCE, SKILL_STANDARD_SYNC, SKILL_INTEGRITY_CHECK; high-level BUILD_LANG_GUIDES_COLLECTION / MANAGE_PROJECT / MANAGE_IDEAS as orchestrating skills.
- **Not automated:** /menu, /incompletes, /do-more, /whats-next, /ideas, /add-idea (agent-implemented from spec; no dedicated script).
- **Vet together:** Confirm this list matches intent; add/remove rows; then refine [EPISTEME_SKILLS_TREE.md](EPISTEME_SKILLS_TREE.md) and skills-to-make-first.

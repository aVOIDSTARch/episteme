# Master production archive

**Purpose:** Single file containing **all** Episteme work, ideas, and process: design and implementation chronicle, TODOs, scrape reports, processed state, and the **full verbatim content** of every research-docs/ai-docs source. One place only; no need to keep separate folders. This file is the only process record in `.episteme-project/`.

**Last consolidated:** 2026-03.

---

## Table of contents

| Part | Content |
|------|---------|
| **A** | Structure and scope review (infrastructure, working docs, research-docs list) |
| **B** | Design and implementation chronicle (goal, phases, key decisions) |
| **C** | User comments and intent; verbatim inline notes |
| **D** | Full checklist snapshot (TODO-MIND-MACHINE-BASE) |
| **E** | Incremental completion log (todo-2) |
| **F** | Scrape and processed state |
| **I** | **Full verbatim — research-docs/ai-docs** (every source doc in full) |
| **G** | Sources consolidated (safe to delete) |
| **H** | Final production file map |

---

## Part A: Structure and scope review

### Primary infrastructure (keep in place)

These belong in the repo for production; they are not working docs.

| Location | Contents |
|----------|----------|
| **Repo root** | AGENTS.md, README.md, SECRETS.md, .cursorrules, .cursor/rules/episteme-bootstrap.mdc |
| **episteme-framework/** | INDEX.md, MANIFEST.md |
| **episteme-framework/agent-docs/** | README.md (ai-docs index), LIBRARY-MAP.md, meta-agent.example.md, OVERRIDES.md, NEW-PROJECT.md, LOAD-CONTEXT.md |
| **episteme-framework/my-skills/** | episteme-skills/ (SKILLS_TREE.md, README.md, per-skill SKILL.md), skill-definition/ (_skill-definition, skill-standard, example-files), imported-skills/, 000-my-skills-index.md |
| **episteme-framework/projects/** | tracking-system/ (_docs 01–05), example-project/ (001–005 samples) |
| **episteme-framework/ideas-engine/** | README.md, _idea-file-schema.md, AGENT-INSTRUCTIONS.md, template-topic.md, sample/ (getting-started.md, README) |
| **episteme-framework/language-style-guides/** | code-guide-sources.md, public/master/ (code-guide-master-file.md, code-guide-*.ai), public/google|peps|dart|android/ (scraped .md), scripts/ (scrape_guides.py, scrapers/, sources_config.py, README, requirements-scrape.txt) |
| **episteme-framework/scripts/** | generate_manifest.py |
| **episteme-framework/project-documentation/** | README.temp.md (project README template) |

### Working / process docs (content preserved below; originals can be deleted)

| Path | Description |
|------|-------------|
| episteme-framework/agent-docs/TODO-MIND-MACHINE-BASE.md | Main checklist §1–§8, comments, summary. |
| episteme-framework/agent-docs/todo-2.md | Incremental remaining-work list; all items completed. |
| episteme-framework/language-style-guides/scrape-report-20260303-173853.md | One scrape run report (16 sources, 16 OK). |
| episteme-framework/language-style-guides/public/google/PROCESSED.md | Mapping of Google scraped files to master code-guide-*.ai. |
| .episteme-project/todo-2.md | Duplicate of agent-docs/todo-2. |
| .episteme-project/TODO-MIND-MACHINE-BASE.md | Duplicate of agent-docs TODO. |

### Research-docs (working and reference)

Located in **`.episteme-project/research-docs/`** — not in the shipped framework; used during design and implementation. Content preserved in **Part I** below.

| Location | Contents |
|----------|----------|
| **research-docs/ai-docs/** | episteme-system-capabilities-and-gaps.md, code-guide-format-analysis.md, _docs-format-and-design-notes.md, _docs-design.md, _docs-tracking-system-review.md, skills-to-make-first.md, skill-creation-notes.md, project-schema-setup-skill-notes.md, meta-agent-template-process-notes.md, meta-agent.md, 000-sample-project-compliance.md, TODO-MIND-MACHINE-BASE.md (duplicate) |
| **research-docs/archived-ai-docs/** | markdown.ai, claude-universal.md, project-ideas.ai, start.ai (legacy/archived) |

Nothing else in the framework is “disparate working doc”; README.temp is a template, not process history.

---

## Part B: Design and implementation chronicle

### Goal

Complete the repo as a passive “Super Library” base that an agent can fork and personalize: infinitely perusable, file-based, read-first; clear entry points, structures, data, and agent interface. No running server. Audience: maintainers and agents vetting “what’s missing” before release or fork.

### Phases (as executed)

1. **Agent interface and entry points** — Single bootstrap at repo root (AGENTS.md); Cursor integration (.cursor/rules/episteme-bootstrap.mdc, .cursorrules); “Library map” for perusal (LIBRARY-MAP.md); meta-agent as default context.
2. **Structures and schemas** — Root README updated for episteme-framework layout; ai-docs stripped of references to episteme-system-capabilities-and-gaps and code-guide-format-analysis; all .episteme-project references refactored to in-framework paths; _docs and leading-underscore convention documented in LIBRARY-MAP. .gitignore updated (e.g. .venv, .env, .episteme-local, project-ideas.ai, comprehensive project-specific ignores).
3. **Data and content** — Ideas: ideas-engine/sample/ with one sample topic file (getting-started.md + README). Code-guide-sources: language-style-guides/code-guide-sources.md. Tracking sample, code guides (master + raw), and skills already present.
4. **Functions and automation** — Load-context helper (agent-docs/LOAD-CONTEXT.md: minimal context set + exemplar blurb). Menu/insert-from-file: INSERT_IDEAS_FROM_FILE skill; MANAGE_IDEAS and meta-agent and ideas AGENT-INSTRUCTIONS updated. Integrity/sync: SKILL_INTEGRITY_CHECK and SKILL_STANDARD_SYNC instructions fleshed out (stub). Scrape/merge: language-style-guides/scripts/ (scrape_guides.py, site-specific scrapers for Google, PEP, Dart, Android; sources_config; README); run produces public/<group>/*.md and scrape-report-<timestamp>.md.
5. **Passive library** — Top-level index (episteme-framework/INDEX.md). Manifest: MANIFEST.md generated by scripts/generate_manifest.py (list of all _*.md, SKILL.md, code-guide-*.ai).
6. **Personalization** — OVERRIDES.md (IDEAS_ROOT, completed-projects, .episteme-local, env vars); SECRETS.md at repo root (protecting secrets locally, avoid push); NEW-PROJECT.md (what to copy into a new project).

### Key decisions

- Single bootstrap at root; meta-agent is the single source of universal behavior; projects copy or point to it and personalize in one place.
- Leading underscore = schema/convention doc; skill behavior lives in SKILL.md.
- Scrape output: public/google, public/peps, public/dart, public/android; one timestamped report per run in language-style-guides.
- Framework is self-contained: no dependency on .episteme-project or on external docs (capabilities, format-analysis); optional docs can be added locally when personalizing.
- **Skills tree:** EPISTEME_SKILLS_TREE was moved from ai-docs/ to my-skills/episteme-skills/SKILLS_TREE.md and pruned to a “map with legend” plus flat list; “creation stuff” (mapping to skills-to-make-first, how-to-use) kept behind the curtain so the shipped tree is a clean reference only.
- **Implementation order:** Group 1 (agent interface: bootstrap, Cursor rules, LIBRARY-MAP) → Group 2 (structures: root README, ai-docs refs, .episteme-project refactor) → todo-2 immediate (3.1 ideas sample, 3.4 code-guide-sources, 6.2 overrides+SECRETS, 6.3 new-project, 5.1 INDEX) → next (4.4 load-context, 4.1 menu/insert-from-file, 4.5 integrity/sync) → last (4.3 scrape scripts) → optional (5.5 MANIFEST).

---

## Part C: User comments and intent (“Comments through §6”)

Intent from user comments, for implementation or §7/§8 update:

- **3.1** — Do example: add `ideas-engine/sample/` with one sample topic file.
- **3.4** — Implement: add code-guide-sources doc (style-guide URLs).
- **4.1** — Implement: skill or skill collection for the menu; add ability to specify a file by path and insert each line/item as an idea (blank lines as separators).
- **4.3** — Do scrape/merge last: move to end of priority order.
- **4.4** — Generate load-context helper and add blurb on why it's the exemplar.
- **4.5** — Implement: SKILL_INTEGRITY_CHECK / SKILL_STANDARD_SYNC (or stub).
- **5.1** — Implement: top-level index (sitemap). LIBRARY-MAP is the perusal map; sitemap links all major sections from one place.
- **5.5** — Clarify: we have the skills map (SKILLS_TREE + LIBRARY-MAP). This item is the optional manifest/INDEX (all _*.md, SKILL.md, code-guide-*.ai) for programmatic listing.
- **6.2** — Implement: document where to put overrides; add SECRETS.md explaining how to protect secrets locally and avoid pushing to repos.
- **6.3** — Implement: short doc on what to copy into a new project.

### Verbatim inline comments from TODO Notes (original /% instructions)

These were the exact user instructions in the Notes column of TODO-MIND-MACHINE-BASE before implementation; preserved so no wording is lost.

| Item | Verbatim Note (/% … %/) |
|------|-------------------------|
| 3.1 | /% do example %/ |
| 3.4 | /% implement %/ |
| 4.1 | /% write a skill or skill collection that implements the menu as we discussed. also add the ability to specify a file by path and insert each item in the file as an idea using blank lines as separatorsn %/ |
| 4.3 | /% we will do this last move ot end %/ |
| 4.4 | /% generate one and add a blurb about why this one should be the exemplar %/ |
| 4.5 | /% implement %/ |
| 5.1 | /% implement %/ |
| 6.2 | /% implement; add SECRETS.md explaining how to protect secrets locally and avoid pushing them to repos %/ |
| 6.3 | /% implement %/ |

---

## Part D: Full checklist snapshot (from TODO-MIND-MACHINE-BASE)

### §1 Agent interface and entry points

| # | Item | Status | Notes |
|---|------|--------|-------|
| 1.1 | Single bootstrap at repo root | Done | AGENTS.md at repo root: states Episteme, points to agent-docs/README and meta-agent.example, onboarding. |
| 1.2 | Cursor integration | Done | .cursor/rules/episteme-bootstrap.mdc (alwaysApply) + .cursorrules at root. |
| 1.3 | “Library map” (perusal entry) | Done | agent-docs/LIBRARY-MAP.md. |
| 1.4 | Meta-agent as default context | Done | Bootstrap states projects copy or point to meta-agent. |

### §2 Structures and schemas

| # | Item | Status | Notes |
|---|------|--------|-------|
| 2.1 | Root README vs framework | Done | Root README describes episteme-framework layout, AGENTS.md, Cursor rules. |
| 2.2 | ai-docs inside framework | Done | Refs to capabilities/format-analysis removed; index in-framework only. |
| 2.3 | Refs to .episteme-project | Done | Refactored out; all paths in-framework. |
| 2.4 | _docs and schema coverage | OK | Tracking 001–005, ideas, skills _docs present. |
| 2.5 | Leading-underscore convention | OK | Documented in LIBRARY-MAP. |

### §3 Data files and content

| # | Item | Status | Notes |
|---|------|--------|-------|
| 3.1 | Ideas data | Done | ideas-engine/sample/ + spec, template, list-topics. |
| 3.2 | Tracking sample | OK | example-project 001–005; tracking-system _docs. |
| 3.3 | Code guides | OK | Master + raw; public/google and scraped (peps, dart, android). |
| 3.4 | Code guide sources list | Done | language-style-guides/code-guide-sources.md. |
| 3.5 | Skills | OK | episteme-skills, skill-definition, FLIP_WIDGET, indexes. |

### §4 Functions and automation

| # | Item | Status | Notes |
|---|------|--------|-------|
| 4.1 | Slash commands | Done | meta-agent; INSERT_IDEAS_FROM_FILE; SHOW_MENU + MANAGE_IDEAS. |
| 4.2 | list-topics.sh | OK | ideas-engine/list-topics.sh. |
| 4.3 | Scrape/merge scripts | Done | language-style-guides/scripts (scrape_guides, scrapers, README). |
| 4.4 | Load context helper | Done | agent-docs/LOAD-CONTEXT.md. |
| 4.5 | Integrity/sync (skills) | Done | SKILL_INTEGRITY_CHECK, SKILL_STANDARD_SYNC stubs. |

### §5 Passive “Super Library” affordances

| # | Item | Status | Notes |
|---|------|--------|-------|
| 5.1 | Top-level index (sitemap) | Done | episteme-framework/INDEX.md. |
| 5.2 | Per-section README or _doc | OK | Each area has README or _doc. |
| 5.3 | Discoverability of code guides | OK | master/README; MANIFEST.md. |
| 5.4 | Discoverability of skills | OK | SKILLS_TREE, episteme-skills/README, 000-my-skills-index. |
| 5.5 | Manifest or INDEX | Done | MANIFEST.md; scripts/generate_manifest.py. |

### §6 Personalization and fork hygiene

| # | Item | Status | Notes |
|---|------|--------|-------|
| 6.1 | Placeholder for “your repo” | OK | meta-agent.example placeholders. |
| 6.2 | Where to put overrides | Done | OVERRIDES.md; SECRETS.md at repo root. |
| 6.3 | What to copy into new project | Done | NEW-PROJECT.md. |

### §7 Summary (must-have for “complete” base)

- **Agent interface:** Done. Bootstrap + .cursor/rules + .cursorrules; LIBRARY-MAP; meta-agent as default.
- **Structures:** Done. Root README; capabilities/format-analysis refs removed; .episteme-project refactored out.
- **Data:** Done. Code-guide-sources.md; ideas-engine/sample/; language-style-guides/scripts (scrape + report).
- **Passive library:** Done. INDEX.md; MANIFEST.md.
- **Personalization:** Done. OVERRIDES.md; SECRETS.md; NEW-PROJECT.md.

### §8 File checklist (final)

| File or folder | Location | Action |
|----------------|----------|--------|
| AGENTS.md | Repo root | Done. |
| .cursor/rules, .cursorrules | Repo root | Done. |
| LIBRARY-MAP.md | episteme-framework/agent-docs | Done. |
| code-guide-sources.md | episteme-framework/language-style-guides | Done. |
| Scrape/merge scripts | episteme-framework/language-style-guides/scripts | Done. |
| INDEX.md | episteme-framework | Done. |
| README.md | Repo root | Done. |
| Override/config doc | agent-docs + SECRETS at root | Done: OVERRIDES.md, SECRETS.md. |
| New project one-pager | agent-docs | Done: NEW-PROJECT.md. |
| MANIFEST.md | episteme-framework | Done; regenerate with scripts/generate_manifest.py. |
| episteme-system-capabilities-and-gaps.md | episteme-framework/agent-docs | N/A — references removed; add locally when personalizing if desired. |
| code-guide-format-analysis.md | episteme-framework/agent-docs | N/A — references removed; code-guide-master-file.md is the in-repo reference. |

---

## Part E: Incremental completion log (from todo-2)

**Status:** All items complete.

**Done (no action):** §1 Agent interface; §2 Structures; §3.1 Ideas sample, §3.4 Code guide sources; §4.2 list-topics; §4.4 Load-context, §4.1 Menu/insert-from-file, §4.5 Integrity/sync, §4.3 Scrape scripts; §5.1 Index, §5.5 Manifest; §6.2 Overrides + SECRETS, §6.3 New-project one-pager.

**Remaining:** None.

**File checklist (all done)** — full table from todo-2:

| File or folder | Location | Action |
|----------------|----------|--------|
| ~~code-guide-sources.md~~ | language-style-guides/ | Done. |
| ~~INDEX.md~~ | episteme-framework/ | Done. |
| ~~Override/config doc~~ | agent-docs/OVERRIDES.md | Done. |
| ~~SECRETS.md~~ | Repo root | Done. |
| ~~"New project" one-pager~~ | agent-docs/NEW-PROJECT.md | Done. |
| ~~Load-context doc~~ | agent-docs/LOAD-CONTEXT.md | Done. |
| ~~Scrape/merge scripts~~ | language-style-guides/scripts/ | Done: scrape_guides.py, scrapers, README; report in language-style-guides/scrape-report-*.md. |

---

## Part F: Scrape and processed state

### Scrape report (2026-03-03)

- **Run:** 2026-03-03T17:38:53Z
- **Sources:** 16
- **Result:** 16 OK, 0 failed.

| Slug | URL | Bytes |
|------|-----|-------|
| google-cpp | https://google.github.io/styleguide/cppguide.html | 207047 |
| google-csharp | https://google.github.io/styleguide/csharp-style.html | 18044 |
| google-go | https://google.github.io/styleguide/go/ | 6610 |
| google-java | https://google.github.io/styleguide/javaguide.html | 40052 |
| google-javascript | https://google.github.io/styleguide/jsguide.html | 116673 |
| google-typescript | https://google.github.io/styleguide/tsguide.html | 102739 |
| google-python | https://google.github.io/styleguide/pyguide.html | 92969 |
| google-shell | https://google.github.io/styleguide/shellguide.html | 37299 |
| google-objc | https://google.github.io/styleguide/objcguide.html | 69334 |
| google-r | https://google.github.io/styleguide/Rguide.html | 3055 |
| google-markdown | https://google.github.io/styleguide/docguide/style.html | 23755 |
| google-htmlcss | https://google.github.io/styleguide/htmlcssguide.html | 22501 |
| google-angularjs | https://google.github.io/styleguide/angularjs-google-style.html | 9572 |
| pep8 | https://peps.python.org/pep-0008/ | 47863 |
| effective-dart | https://dart.dev/guides/language/effective-dart | 15992 |
| kotlin-android | https://developer.android.com/kotlin/style-guide | 24566 |

Output: public/google/, public/peps/, public/dart/, public/android/ (one .md per source). Report file: language-style-guides/scrape-report-20260303-173853.md.

### PROCESSED (Google → master)

Generated: 2026-03-03T06:49:49.919224+00:00. Google files merged or already present in public/master/:

| Google file | Status | Master file |
|-------------|--------|-------------|
| python.md | already_present | scripting-dynamic/code-guide-python.ai |
| cpp.md | already_present | c-family/code-guide-c-plus-plus.ai |
| csharp.md | already_present | c-family/code-guide-c-sharp.ai |
| java.md | already_present | jvm-languages/code-guide-java.ai |
| javascript.md | already_present | typescript-javascript/code-guide-ts-js.ai |
| typescript.md | already_present | typescript-javascript/code-guide-ts-js.ai |
| shell.md | already_present | tooling/code-guide-shell.ai |
| r.md | already_present | data-science/code-guide-r.ai |
| markdown.md | already_present | markup-and-data/code-guide-markdown.ai |
| htmlcss.md | already_present | markup-and-data/code-guide-web.ai |
| objective-c.md | already_present | c-family/code-guide-objective-c.ai |
| angularjs.md | already_present | frontend-frameworks/code-guide-angular.ai |
| go.md | already_present | systems-languages/code-guide-go.ai |

---

## Part I: Full verbatim — research-docs/ai-docs

The following is the **full verbatim content** of each file in `.episteme-project/research-docs/ai-docs/`. Everything in one file.

### episteme-system-capabilities-and-gaps.md

# Episteme: system capabilities, should-do list, and gaps

**Purpose:** Single checklist of everything the episteme system is intended to do (from meta-agent, tracking system, ideas-engine, language-style-guides, my-skills). Mark complete vs not-yet so we can vet and prioritize. **Episteme skills map** → [my-skills/episteme-skills/SKILLS_TREE.md](../my-skills/episteme-skills/SKILLS_TREE.md).

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
- **Vet together:** Confirm this list matches intent; add/remove rows; then refine the skills map ([episteme-skills/SKILLS_TREE.md](../my-skills/episteme-skills/SKILLS_TREE.md)) and skills-to-make-first as needed.


---

### code-guide-format-analysis.md

# Code guide file format: analysis and usage

**Purpose:** This document summarizes the analysis of the `code-guide-*.ai` format (as applied to C# in `public/master/c-family/code-guide-c-sharp.ai`) for **future agent use** when analyzing and improving code style for a language. It is an AGENT RESOURCE.

**Reference:** Structure is defined in `language-style-guides/public/master/code-guide-master-file.md`. The C# file is the first full transformation example.

---

## 1. Format summary

Each code guide file has four main sections in order:

| Section | Role |
|--------|------|
| **Overview** | Brief description, best use cases, contraindications, ecosystem. Lets the agent decide if the guide is relevant. |
| **Sources** | Table: source name, URL, last accessed. Canonical list for traceability and re-crawl. |
| **Code guide** | **Consensus** (rules shared across sources) first; then **Per-source** (unique or conflicting rules by source). |
| **Notes for the agent** | When to use, caveats, tooling, how to resolve conflicts. |

Raw scraped content may live in an **Appendix** for traceability; the normalized Consensus + Per-source text is what the agent should apply.

---

## 2. What works well (for agent use)

- **Scannable relevance:** Overview (use cases, contraindications) makes it easy to decide “use this guide / skip” without reading the full file.
- **Clear application order:** Consensus first → then Per-source when context is known (e.g. “Google C#” codebase). Reduces ambiguity.
- **Traceability:** Sources table + optional appendix preserve where rules came from; supports re-crawl and “cite source” behavior.
- **Conflict handling:** “(Unique)” and “(Conflicts with …)” in Per-source give the agent an explicit way to prefer one source when the repo states a style (e.g. README says “Google C#”).
- **Actionable agent notes:** “When to use,” “Caveats,” “Tooling,” “Conflicts” tell the agent when and how to apply the guide and what to suggest (e.g. `dotnet format`, EditorConfig).
- **Single-file scope:** One `.ai` file per language/topic keeps context local and easy to load.

---

## 3. Gaps and improvements

- **Single-source consensus:** With only one scraped source (e.g. Google for C#), “Consensus” is effectively “that one source.” The file should state this (e.g. “Derived from the single scraped source (Google); treat as baseline until more sources are merged”). As more sources are merged, consensus should be re-derived and the note updated.
- **Guide quality rating (required):** Every guide must include a small rating (e.g. 1–5 or star-like) for trustworthiness/completeness, with concrete metrics and a short synopsis of why it scored that way. Store at the top of Overview; re-score when sources or conflicts change.
- **Appendix size and archive:** Keeping full raw scrapes in-file can make files very large. Prefer archiving raw scrapes in a **scraping archive folder** in a formatted, pruned form that is easy to traverse later; keep only the Sources table and normalized guide in the `.ai` file (or a truncated appendix plus "full scrape in archive").
- **Per-source density (codified):** Per-source subsections must stay concise: only rules that are **unique** or **conflicting**. Do not restate consensus in Per-source. This is a standing convention for all code guides.
- **Tooling links:** Include direct links to linter/formatter config (e.g. EditorConfig, StyleCop docs) for copy-paste or “suggest this config.”
- **Version/date in Overview:** Add “Style guide last updated: YYYY-MM-DD” (or “Sources last merged: …”) to Overview so agents can decide whether to suggest a refresh.
---

## 4. How to use this format to analyze and improve code style (C# and other languages)

**When asked to analyze or improve code style for a language:**

1. **Load the right guide.**
   Resolve language/framework to the corresponding `code-guide-<topic>.ai` (see `public/master/README.md` for layout). Open that file.

2. **Check relevance.**
   Read **Overview**. If the task (e.g. “backend C# service”) matches “Best for” and does not match “Avoid for,” treat the guide as applicable.

3. **Apply consensus first.**
   Use **Code guide → Consensus** as the default set of rules. When suggesting edits (formatting, naming, structure), align with these bullets. Prefer citing the guide: “Per this project’s C# style guide (consensus): ….”

4. **Apply Per-source when context is known.**
   If the repo or user states a style (e.g. “we follow Google C#” or “Microsoft conventions”), use the **Per-source** subsection for that source and prefer it where it conflicts with consensus. Label suggestions: “Per Google C# style guide: ….”

5. **Use Notes for the agent.**
   - **When to use:** Only suggest style changes when the guide is in scope (e.g. editing `.cs` files, or user asked for style).
   - **Caveats:** Do not override existing repo conventions (e.g. “legacy uses 2 spaces”) unless the user asks to modernize; prefer “new code: consensus; existing: match file.”
   - **Tooling:** Suggest enabling `dotnet format`, EditorConfig, or StyleCop when improving style, and point to the Tools line in the guide.
   - **Conflicts:** If sources disagree and the repo does not state a style, apply consensus and optionally note: “Google C# recommends X; we’re applying the shared rule Y.”

6. **Cite sources when useful.**
   For non-obvious or strict rules, cite the **Sources** table (e.g. “Google C# Style Guide”) so the user can look up the original.

7. **Refresh when appropriate.**
   If the **Sources** table shows old “Last accessed” dates or the guide is clearly outdated, suggest re-running the scrape/merge (see `code-guide-master-file.md` §3) rather than inventing rules.

---

## 5. Recommendations for future improvements

- **Merge more sources for C#:** Run crawler/merge for Microsoft and Goat C# so Consensus can be derived from multiple sources and Per-source can list real differences (e.g. Microsoft vs Google on line length or brace placement).
- **Add “Last updated” to Overview:** One line with the date of the last merge or scrape so agents can decide when to suggest a refresh.
- **Optional: separate raw scrapes:** Keep a single “Sources” table and normalized Consensus/Per-source in the `.ai` file; store full raw scrapes in `public/raw/` or similar to limit file size while preserving traceability.
- **Replicate format for other languages:** Use the C# file as the template: transform one well-populated `.ai` per language (e.g. Python, TypeScript/JS, Go) into this structure, then use this analysis doc to drive consistent behavior across languages.

---

## 6. Quick reference: file locations

| Asset | Path |
|-------|------|
| Master design | `language-style-guides/public/master/code-guide-master-file.md` |
| C# guide (transformed) | `language-style-guides/public/master/c-family/code-guide-c-sharp.ai` |
| This analysis | `ai-docs/code-guide-format-analysis.md` |
| Scrape/merge scripts | `language-style-guides/scrape_guides.py`, `merge_google_into_master.py` |

When analyzing or improving code style for a language: **open the corresponding `code-guide-<topic>.ai`, follow §4 above, and use this document for consistent interpretation of the format.**


---

### _docs-format-and-design-notes.md

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


---

### _docs-design.md

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


---

### skills-to-make-first.md

# Skills to Make First

Running list of skills to create so none are lost. Add to this file as new skills are identified; check off or move to a "done" section when implemented. **Collected notes for creating SKILLs:** `ai-docs/skill-creation-notes.md`.

---

## List

| # | Skill name | Purpose / notes | Source / reference |
|---|-------------|-----------------|--------------------|
| 1 | **SETUP_NEW_PROJECT** | Create or update a project schema from user input + agent-observed data; follows `_project-schema.md` and gathering process in notes. | `projects/tracking-system/01-project-schemas/_project-schema.md`, `ai-docs/project-schema-setup-skill-notes.md` |
| 2 | **EPISTEME_DESIGN** | Encode episteme’s document design language: _docs format, naming conventions, template structure, design aesthetic. Agents use it to create or validate _docs and instance docs consistently. | `ai-docs/_docs-format-and-design-notes.md` |
| 3 | **Meta-agent template** | Turn a project/user-specific agent doc (e.g. `meta-agent.md`) into a reusable, project/user-agnostic template (e.g. `meta-agent.example.md`). | `ai-docs/meta-agent-template-process-notes.md` (or equivalent in repo) |
| 4 | **Set up environment** | Optional follow-up to schema setup: set up runtimes, tooling (Node, pnpm, etc.). User can defer from SETUP_NEW_PROJECT. | `ai-docs/project-schema-setup-skill-notes.md` (divergent pathway “set up environments later”) |

| 5 | **CREATE_OR_VALIDATE_SKILL** | Create or validate skill folder vs skill-definition and skill-standard. Folder name = skill name. | `ai-docs/skill-creation-notes.md` §2, `my-skills/skill-definition/` |
| 6 | **IMPORTED_SKILL_META_DOC** | Meta-doc for imported skill: location, risk assessment, conversation notes. | `ai-docs/skill-creation-notes.md` §3, `my-skills/imported-skills/_imported-skills.md` |
| 7 | **EPISTEME_SKILL_SCAFFOLD** | Scaffold episteme skill folder + SKILL.md stub. | `ai-docs/skill-creation-notes.md` §4, `my-skills/episteme-skills/_episteme-skills.md` |
| 8 | **TRACKING_SYSTEM_COMPLIANCE** | Check project docs (001–005) vs _docs; report compliance. | `ai-docs/skill-creation-notes.md` §5, `_docs-tracking-system-review.md` |
| 9 | **SKILL_STANDARD_SYNC** | (Future.) Compare local skill-standard to website; report drift. | `ai-docs/skill-creation-notes.md` §6 |
| 10 | **SKILL_INTEGRITY_CHECK** | (Future.) Recompute integrity hash of skill content; compare to stored value; report tampering / prompt-injection risk. | `_skill-definition.md`, `_imported-skills.md` (Integrity hash) |

---

## Done

*(Move rows here when a SKILL.md exists and is linked.)*

---

*Add new rows to the table above. Keep “Purpose / notes” and “Source / reference” brief so the list stays scannable.*


---

### skill-creation-notes.md

# Notes for creating SKILLs (collected)

**Purpose:** Central notes to create SKILLs from later. Each section summarizes purpose, inputs/outputs, key references, and behavior so a future agent or human can author the SKILL.md. **Running list of candidates:** `ai-docs/skills-to-make-first.md`.

---

## 1. Project schema & tracking system (existing)

| Skill | Notes location | Summary |
|-------|----------------|--------|
| **SETUP_NEW_PROJECT** | `ai-docs/project-schema-setup-skill-notes.md` | Schema: `_project-schema.md`. Behavior: user inputs, multiple choice, confirm observed data, sanity-check freeform, divergent pathways (name suggestions, set up environment later). |
| **EPISTEME_DESIGN** | `ai-docs/_docs-format-and-design-notes.md`, `ai-docs/_docs-design.md` | _Docs design language: template structure, naming, design principles. Skill: create or validate _docs and instance docs. |
| **Set up environment** | `ai-docs/project-schema-setup-skill-notes.md` (pathway) | Deferrable from SETUP_NEW_PROJECT; set up runtimes, tooling (Node, pnpm, etc.). |
| **Meta-agent template** | `ai-docs/meta-agent-template-process-notes.md` (or equivalent) | Turn project/user-specific agent doc into reusable template. |

---

## 2. My-skills: create or validate a skill

**Potential SKILL name:** CREATE_OR_VALIDATE_SKILL (or CREATE_SKILL, VALIDATE_SKILL split).

**Purpose:** Create a new skill folder (episteme or example) or validate an existing skill against the skill-definition and skill-standard. Folder name = skill name; one small to small–medium skill per folder; complex skills = constellation of simpler skills.

**Inputs:** User or task: skill name, description, when to use, instructions (or path to existing skill to validate). Optional: copy from FLIP_WIDGET or another example.

**Outputs:** A skill folder with SKILL.md (and optional content) that conforms to `_skill-definition.md` and `skill-standard/`; or a validation report (missing sections, non-conformant layout).

**Key references:**
- `my-skills/skill-definition/_skill-definition.md` (required/optional sections)
- `my-skills/skill-definition/skill-standard/_skill-standard.md` (folder design, structure rules)
- `my-skills/skill-definition/skill-example-files/FLIP_WIDGET/` (example)
- `my-skills/skill-definition/skill-example-files/_skill-example-files.md`
- Website for canonical skill standard

**Behavior notes:** Check website for standard. Enforce: skill = folder, folder name = skill name. Keep scope small to small–medium; for complex workflows, use REQUIRED_SKILLS to compose. **Provenance & integrity:** Every skill should have **Original source URI** (required for imported; recommended for episteme). When verification is needed, include **Integrity hash** (algorithm + hash of SKILL.md or normalized folder); verify before use to detect tampering, meddling, or prompt injection. Optionally offer “copy from FLIP_WIDGET” or “validate only.”

---

## 3. My-skills: imported skill meta-doc

**Potential SKILL name:** IMPORTED_SKILL_META_DOC (or RECORD_IMPORTED_SKILL).

**Purpose:** When an imported skill (from website or other source) is added or updated, create or update its meta-doc with location, risk assessment, and conversation notes (AGENT with other ENTITIES).

**Inputs:** Skill name/source; where it’s located; risk assessment (security, trust, dependencies, conflicts; summary; alternatives/sandbox if significant risk); relevant conversation notes.

**Outputs:** A meta-doc (e.g. META.md or `<skill-name>-meta.md`) in the skill’s folder (or in imported-skills index) with required sections.

**Key references:**
- `my-skills/imported-skills/_imported-skills.md` (required: Name, Original source URI, Location, Risk assessment, Conversation notes, Integrity hash)
- Risk flow from meta-agent: ask permission, assess risks (security, trust, dependencies, conflicts), present summary, suggest alternatives/sandbox if needed, keep assessments in markdown

**Behavior notes:** Risk assessment is required in the meta-doc. **Original source URI** = canonical URI for provenance. **Integrity hash** = algorithm + hash; recompute and compare before use when security matters (tampering, meddling, prompt injection). Conversation notes = relevant notes from AGENT with other ENTITIES about this skill. One folder per imported skill; folder name = skill name.

---

## 4. My-skills: episteme skill scaffold

**Potential SKILL name:** EPISTEME_SKILL_SCAFFOLD (or SCAFFOLD_EPISTEME_SKILL).

**Purpose:** Scaffold a new episteme (framework) skill: create folder (folder name = skill name), SKILL.md stub conforming to skill-definition, optional README or placeholder. For framework navigation; not for general use outside episteme.

**Inputs:** Skill name (slug), short description, when to use (trigger). Optional: REQUIRED_SKILLS (constellation of simpler skills).

**Outputs:** `my-skills/episteme-skills/<skill-name>/` with SKILL.md (Name, Description, When to use, Instructions placeholder) and optional content.

**Key references:**
- `my-skills/episteme-skills/_episteme-skills.md`
- `my-skills/skill-definition/_skill-definition.md`
- `my-skills/skill-definition/skill-example-files/FLIP_WIDGET/` (structure reference)

**Behavior notes:** One small to small–medium skill per folder. If the skill is complex, instruct “use REQUIRED_SKILLS to list simpler skills and keep this skill as process/orchestration with singleness of purpose.”

---

## 5. Tracking system: compliance check

**Potential SKILL name:** TRACKING_SYSTEM_COMPLIANCE (or CHECK_PROJECT_DOCS_COMPLIANCE).

**Purpose:** Check that a set of project docs (schema, planning, progress, completed, after-action) complies with the tracking-system _docs. Report missing sections, wrong order, or non-conformant content.

**Inputs:** Path to project folder or list of doc paths (001–005 style). Optional: which _doc set (tracking-system 01–05).

**Outputs:** Compliance report (per-doc and cross-cutting), with fixes or suggestions.

**Key references:**
- `ai-docs/_docs-tracking-system-review.md` (review criteria)
- `projects/tracking-system/01-project-schemas/_project-schema.md` through `05-after-action/_after-action.md`
- `projects/example-project/000-sample-project-compliance.md` (example report)

**Behavior notes:** Re-use logic from the sample-project compliance review: required sections present, cross-refs correct, “What to do next” placement (003), naming consistency.

---

## 6. Skill standard sync (future)

**Potential SKILL name:** SKILL_STANDARD_SYNC (or CHECK_SKILL_STANDARD).

**Purpose:** Compare local skill-definition and skill-standard docs to the website’s canonical standard; report drift or suggest updates. Optional: one-way “adopt website standard” helper.

**Inputs:** Path to skill-standard doc(s); optional website URL or fetched spec.

**Outputs:** Diff or report: local vs website; suggested edits.

**Key references:**
- `my-skills/skill-definition/skill-standard/_skill-standard.md`
- Website (to be specified)

**Behavior notes:** Defer until website standard is stable and fetchable; note here so we don’t forget.

---

## How to use this file

- **When adding a new skill idea:** Add a row to `skills-to-make-first.md` and a section above with purpose, inputs, outputs, references, behavior notes.
- **When creating a SKILL.md:** Open this file and the relevant _docs; use the section as the spec for the skill’s instructions and scope.
- **Existing deep-dive notes:** SETUP_NEW_PROJECT and meta-agent template have their own process notes; this file points to them and adds my-skills and tracking-system so nothing is lost.


---

### project-schema-setup-skill-notes.md

# Process notes: Project schema & SETUP_NEW_PROJECT SKILL

**Purpose:** Notes for creating the SETUP_NEW_PROJECT SKILL.md. The schema spec lives in `projects/tracking-system/01-project-schemas/_project-schema.md` and defines *what* to gather; this file captures *how* the skill should behave (gathering process, UX, divergent pathways). Underscore-prefixed docs (`_project-schema.md`) do not contain skill descriptions or engineering—only the schema structure and REQUIRED_SKILLS. Skill behavior lives here.

---

## Gathering process (for SETUP_NEW_PROJECT SKILL)

The SKILL that creates or updates project schemas from the schema spec should follow these behaviors. They ensure good data, minimal friction, and room for creative interaction.

### 1. User inputs

Gather from the user only what they can reasonably supply (Project name/slug, Summary, Owner, Type, Stack, Deployment when known, Constraints, Repo path). Do not require the user to fill agent-observed fields.

### 2. Multiple choice when possible

Where the schema or the spec defines a fixed set (e.g. **Deployment** enum, **Type** taxonomy), present choices as a multiple-choice menu or list instead of freeform. Reduces errors and keeps values consistent.

### 3. Confirmation of observed data

For **agent-observed** fields (Dev environment, Agents / models), the agent infers values from context, then **presents them to the user for confirmation**. Example: “I detected: macOS, Cursor, Node 20. Confirm, or tell me what to change.” Record only after the user confirms or corrects.

### 4. Type check and sanity-check freeform text

For freeform fields (e.g. Summary, project name, Constraints), the agent should:

- **Check** input for relevance and sanity (e.g. project name looks like a slug; summary is one line and on-topic).
- **Suggest corrections gently** when something seems off: e.g. “I see you said *X*. I believe you may mean *Y* (e.g. [brief reason]). May I record it as *Y*, or would you prefer your exact input *X*?”
- Always offer **“record your exact input”** so the user can keep their wording. Never overwrite without explicit choice.

### 5. Divergent pathways (creative interaction)

Offer optional branches so the user can go deeper or defer:

| Pathway | Behavior |
|--------|----------|
| **Project name from prompt** | If the user describes the project but hasn’t given a name/slug, offer: “Would you like me to suggest a project name/slug from your description?” Then propose one or two options; user picks or supplies their own. |
| **Suggest language / stack / dev env from concept** | From the user’s summary or type (e.g. “web app”, “CLI”), suggest a plausible stack or dev env (e.g. “This sounds like a web app—consider TypeScript, React, Node. Use these, edit, or skip for now?”). User can accept, edit, or leave blank. |
| **Set up environments later** | Offer: “You can set up runtimes and tooling (Node, pnpm, etc.) now or later via a separate **Set up environment** SKILL. Proceed with schema only, or run environment setup after?” Lets the user defer environment setup to another SKILL.md without blocking schema creation. |

These pathways are **optional**: the user may answer directly, accept suggestions, or choose a divergent path. The skill should feel supportive, not prescriptive.

---

## For the future SETUP_NEW_PROJECT SKILL.md

1. **Goal:** Create or update a project schema file from the spec in `_project-schema.md`, gathering required and optional fields, with good UX and optional divergent pathways.
2. **Inputs:** User (for user-supplied fields); agent context (for agent-observed fields); schema spec (`_project-schema.md`) and enums/conventions there; REQUIRED_SKILLS from the schema or project so the agent knows which other skills to pull.
3. **Output:** A project schema file (e.g. `NNN-<slug>-schema.md`) in `01-project-schemas/`, and optionally amendments to REQUIRED_SKILLS as the project progresses or the user requests.

---

## File locations (this repo)

- **Schema spec (no skill/engineering):** `projects/tracking-system/01-project-schemas/_project-schema.md`
- **Skill notes (this file):** `ai-docs/project-schema-setup-skill-notes.md`


---

### meta-agent-template-process-notes.md

# Process notes: Meta-agent template (meta-agent.example.md)

**Purpose:** Notes for creating a SKILL.md that teaches how to turn a project- and user-specific agent doc (e.g. `meta-agent.md`) into a reusable, project/user-agnostic template (e.g. `meta-agent.example.md`). Use this when the user asks for a SKILL about this process.

---

## What we did

1. **Source:** `meta-agent.md` — cross-project guidance for an agent, with project- and user-specific references (episteme, CLAUDE.md, skilsmp.com, paths, model names, etc.).

2. **Target:** `ai-docs/meta-agent.example.md` — template containing only **project- and user-agnostic** content, with placeholders and generic wording so others can fork and fill in their own repo, paths, and tools.

3. **Process:**
   - Read the full source doc.
   - Identified **specific** elements: canonical repo name (episteme), main doc name (CLAUDE.md), specific URLs (skilsmp.com), specific paths (~/ideas/ai.md), specific model names (claude-opus-4-6), and project-only sections (e.g. “Episteme (optional)” at the end).
   - Kept **universal** structure and logic: cross-project guidance, doc chain, conventions (paths, /%, /menu), context & progression, Skills Marketplace *concept*, Working Style, Coding Standards (generalized), Project Workflow, Slash Commands, Ideas System.
   - Replaced specifics with: generic descriptions, “[Your …]” placeholders, or “e.g.” examples.
   - Removed the final project-specific “Ideas” paragraph entirely.
   - Added a short template-purpose intro and “Your setup” so users know what to replace.

4. **Output:** One template file (`meta-agent.example.md`) that preserves logical sections and instructions without naming the original repo, user, or external sites. One process-notes file (this document) for future SKILL authoring.

---

## Criteria used: agnostic vs specific

- **Agnostic (kept / generalized):** Rules that apply to any project or user (e.g. “ask clarifying questions,” “one logger per project,” “plan → progress → handoff,” “Verbatim + interpretation” for ideas). Paths like `~/plans/` kept as *examples* of a convention, not as the only option.
- **Specific (removed / placeholder):** Names of repos, files, or products (episteme, CLAUDE.md), specific URLs, specific model names, and paragraphs that only describe one project’s next steps.

---

## For the future SKILL.md

The SKILL should explain:

1. **Goal:** Produce a template (e.g. `*.example.md`) from a source agent doc so that only project- and user-agnostic content remains, with clear placeholders and section structure.
2. **Inputs:** A meta-agent (or similar) doc that mixes universal guidance with project/user specifics.
3. **Steps:** (a) Read source; (b) List specific vs universal content; (c) Copy universal + generalized structure into the template; (d) Replace or remove specifics; (e) Add a short “template purpose” and “Your setup” intro; (f) Optionally add inline “[Template note: …]” where helpful.
4. **Output:** One template file that others can copy and customize; optionally a process-notes doc (like this) for SKILL authoring or reuse.

---

## File locations (this repo)

- **Source (specific):** `meta-agent.md` (root)
- **Template (agnostic):** `ai-docs/meta-agent.example.md`
- **Process notes:** `ai-docs/meta-agent-template-process-notes.md` (this file)


---

### _docs-tracking-system-review.md

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


---

### 000-sample-project-compliance.md

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


---

### meta-agent.md

# meta-claude.md

Cross-project guidance for Claude/Cursor/agents. Consolidates rules from this repo's `CLAUDE.md` and `claude-universal.md`. Project-specific details stay in each repo's `CLAUDE.md`. Legacy docs (e.g. start.ai, markdown.ai) may live in an archive folder for reference.

**Required:** Part of project minimum template. Apply in every situation; repo main doc (e.g. `CLAUDE.md`) holds only environment/project-specific items and points the agent here so the chain stays unbroken.

**Canonical repo:** **episteme** — fork and personalize. Holds CLAUDE file collections, slash-command and ideas directory structures, and language/project-type guides (below). Each project has a small bootstrap file that tells the agent how to get episteme (or the fork), open PRs for the project, and return files/changes as required.

**Language / project-type guides:** In episteme, `<language>/<project-slug>.md` (e.g. `js/blank.md`, `ts/standard-starter.md`) holds rules for that project type (blank, standard template starter, etc.). For JS/TS projects, rules may instead live in a skill: name `language-project-slug` (e.g. `js-blank`, `ts-standard-starter`) per the skill standard; pull in the appropriate guide for the project or document. With user permission, the agent may adjust or amend these guides as it learns the user's style. All such docs live in episteme.

**Conventions:** Paths: `~/` = user home; no prefix = project root where applicable; if unclear, ask (home vs root). Use project-root paths when the project or tooling expects repo-scoped paths (e.g. CI, repo-only automation). **`/%`** at the start of a line = your commentary, answers, or instructions (document/context-specific); multiline until next heading or optional `%/`. Resolve by: understand → incorporate into the appropriate document → update your work → remove the comment. Document choices in the doc if helpful.

**`/menu`** — Launches main navigation: 1. Projects (submenu: slash commands, new project, back) 2. Ideas 3. Something else → plain prompt.

**Context & progression:** Use the file system to keep context and progression over time in any Claude/Cursor/agent setup (plans, progress, completed-projects, ideas, skills assessments). Prefer written artifacts over in-session-only state.

---

## Skills Marketplace

**https://www.skilsmp.com** — consult for unfamiliar tools/techniques. The site provides the skill standard (link/spec there): folder + `SKILL.md`, YAML frontmatter (name, description), optional scripts/references; common location `.skills/<name>/SKILL.md` or tool-specific.

Before installing any skill: (1) Ask permission, describe use. (2) Assess risks in `~/skill.md`: security, trust, dependencies, conflicts. (3) Present summary; if significant risk, suggest alternatives/sandbox. (4) Optionally keep assessments in local markdown (future: skills-assessment repo). Install only after explicit approval.

---

## Working Style

Ask clarifying questions and suggest improvements/alternatives before non-trivial work. Get affirmative buy-in from the user for changes as you described them before proceeding. Prefer full-featured solutions unless security, complexity, or fit justify less; then explain why. Use `AskUserQuestion` menus for options and trade-offs.

---

## Coding Standards

- **TypeScript** — New code in TypeScript; for JS-only repos, propose migration first. Use TypeDoc for TS projects (install early, document as you go).
- **Logging** — Structured (debug/info/warn/error), one logger per project.
- **Errors** — User-facing messages: what went wrong + how to fix; no raw stacks.
- **Comments** — Why, not what; keep current.
- **Modularity** — One concern per module; small composable units.
- **AI tools** — Per module: suggest tool interface (typed I/O, side-effects). See `~/ideas/ai.md`.
- **Tests** — Build as you go; central suite in `tests/` (vitest preferred); coverage before “done”; use project framework or propose one.
- **Docs** — Use a documentation system appropriate to the codebase; keep `docs/` for web-viewable output (e.g. html/css) when applicable.
- **Markdown** — Linked table of contents at top; run a markdown linter (project style or standard) after generation. Legacy markdown preferences may be in project archive.
- **SKILLS** — At project end, add SKILL(s) per [skilsmp.com](https://www.skilsmp.com) standard when appropriate; ask when ready.

**After each code change:** Run linter and fix; apply style guide; fix errors; verify buildable; get user agreement before next step. After small, logical changes in a single area, pause for user to git commit and offer a suggested commit message.

---

## Project Workflow

Paths: `~/` = user home; project-scoped paths (e.g. `~/plans/`, `~/progress/`, `~/completed-projects/`) are under home unless the project defines a project-root convention. File-system artifacts are the source of truth for context and progression across sessions. The planning system (artifacts, structure) is up to the agent; ensure the plan is agreed and clear before asking to begin.

1. **Planning** — Agent chooses structure; goals, approach, decisions, files, risks, open questions. Use headings, tables, code blocks where helpful.
2. **Progress** — At milestones: git commit + append to progress artifact (same base name as plan). Entry = what’s done + what’s left. Get user agreement before next step.
3. **Handoff** — Copy plan to completed-projects; add appendix with incomplete items and recommended next steps (enough context for a new session).

---

## Slash Commands

All scan `~/completed-projects/*-appendix.md` and use `AskUserQuestion` menus. Always include “Return to prompt”.

- **`/incompletes`** — Menu of projects with incomplete items → show list, offer to continue or return.
- **`/do-more`** — Menu of projects with next/enhancement ideas → propose plan or return.
- **`/whats-next`** — Combined menu: `[INCOMPLETE]` and `[ENHANCEMENT]` by project; then act or return.

---

## Ideas System

**Location:** `~/ideas/*.md` — one topic per file, structured for future app/db.

**Format per entry:** `**Verbatim:** "user text"` + `**Claude:**` interpretation (implications, connections). Never rewrite Verbatim. Suggest topic merge/split occasionally.

- **`/ideas`** — Menu of topics → show entries; options: **Synthesize** (extended thinking, e.g. `claude-opus-4-6` → 10–15 project ideas from topic; show inline, then return), **Return to topic list**.
- **`/add-idea <text>`** — Match or create topic file; append Verbatim + Claude interpretation; confirm.

**Future-app invariants:** `id`, `topic`, `verbatim` (immutable), `claude_interpretation`, `created_at`; 1:1 topic files; append-only; TypeScript API (tRPC/REST) with markdown as source.

**Full spec and agent instructions:** See **ideas-engine/** in this repo (README, schema, AGENT-INSTRUCTIONS, template). Use for format details, `/ideas` and `/add-idea` steps, and future-app invariants.

---

## Ideas

**Episteme (optional, not migration):** For the episteme repo, consider adding a minimal CLAUDE.md template and a short README or bootstrap snippet so forkers know how to point their projects at episteme. Those are new content for episteme, not migrations from an existing project.


---

### TODO-MIND-MACHINE-BASE.md (research-docs/ai-docs)

Duplicate of the main TODO checklist. Content fully preserved in **Part D** and **Part B**.

### archived-ai-docs

Legacy or archived agent/idea docs: markdown.ai, claude-universal.md, project-ideas.ai, start.ai. Not embedded here; retain in `research-docs/archived-ai-docs/` for reference if needed.


---

## Part G: Sources consolidated (safe to delete)

After this archive is in place, the following have their content preserved above and can be **deleted** from the primary structure (or kept only here in .episteme-project if you prefer a single copy):

| Path | Content preserved in |
|------|------------------------|
| episteme-framework/agent-docs/TODO-MIND-MACHINE-BASE.md | Part D, §7, §8; Part B chronicle. |
| episteme-framework/agent-docs/todo-2.md | Part E; Part D. |
| episteme-framework/language-style-guides/scrape-report-20260303-173853.md | Part F (Scrape report). |
| episteme-framework/language-style-guides/public/google/PROCESSED.md | Part F (PROCESSED table). |
| .episteme-project/todo-2.md | Part E (duplicate of agent-docs/todo-2). |
| .episteme-project/TODO-MIND-MACHINE-BASE.md | Part D (duplicate of agent-docs). |
| .episteme-project/research-docs/ai-docs/*.md (all listed below) | Part I (full verbatim). |

**Recommendation:** Framework paths and .episteme-project root duplicates: delete as above. **research-docs/ai-docs:** Full verbatim content of every file is in Part I; the folder can be deleted—everything is in this single file. **archived-ai-docs:** Not embedded; keep or delete per preference. Update agent-docs/README.md to remove index entries for TODO/todo-2.

---

## Part H: Final production file map

Quick reference for where each deliverable lives (from repo root):

| Deliverable | Path |
|-------------|------|
| Bootstrap | AGENTS.md |
| Cursor rules | .cursor/rules/episteme-bootstrap.mdc, .cursorrules |
| Secrets | SECRETS.md |
| Ai-docs index | episteme-framework/agent-docs/README.md |
| Library map | episteme-framework/agent-docs/LIBRARY-MAP.md |
| Meta-agent | episteme-framework/agent-docs/meta-agent.example.md |
| Overrides | episteme-framework/agent-docs/OVERRIDES.md |
| New project | episteme-framework/agent-docs/NEW-PROJECT.md |
| Load context | episteme-framework/agent-docs/LOAD-CONTEXT.md |
| Sitemap | episteme-framework/INDEX.md |
| Manifest | episteme-framework/MANIFEST.md (generate: episteme-framework/scripts/generate_manifest.py) |
| Skills tree | episteme-framework/my-skills/episteme-skills/SKILLS_TREE.md, README.md |
| Tracking _docs | episteme-framework/projects/tracking-system/ (01–05) |
| Example project | episteme-framework/projects/example-project/ |
| Ideas spec + sample | episteme-framework/ideas-engine/ (_idea-file-schema, AGENT-INSTRUCTIONS, sample/) |
| Code guide sources | episteme-framework/language-style-guides/code-guide-sources.md |
| Code guide master | episteme-framework/language-style-guides/public/master/code-guide-master-file.md |
| Scrape scripts | episteme-framework/language-style-guides/scripts/ |

---

*End of master production archive.*

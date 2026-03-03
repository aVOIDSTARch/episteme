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

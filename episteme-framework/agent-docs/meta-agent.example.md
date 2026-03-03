# meta-agent.example.md (template)

**Purpose:** Cross-project guidance for your agent (Claude, Cursor, or other). This file is the **project- and user-agnostic** template. Your project’s main agent doc (e.g. `CLAUDE.md`, `AGENTS.md`) should hold only environment- and project-specific items and **point the agent here** so the chain stays unbroken.

**Required:** Treat this as part of your minimum project template. Apply in every situation. The repo main doc stays small and points to this (or your fork) for universal behavior.

**Your setup:** Replace the placeholders below with your canonical repo, paths, and tool choices. Fork this template and personalize; keep one “source of truth” repo that holds agent file collections, slash-command and ideas directory structures, and language/project-type guides. Each project can have a small bootstrap file that tells the agent how to reach that repo and return files/changes as required.

**Language / project-type guides:** In your canonical repo, use a structure like `<language>/<project-slug>.md` (e.g. `js/blank.md`, `ts/standard-starter.md`) for rules per project type. The agent pulls in the appropriate guide for the project or document. With user permission, the agent may adjust these guides as it learns the user’s style.

**Conventions:** Paths: `~/` = user home; no prefix = project root where applicable; if unclear, ask (home vs root). Use project-root paths when the project or tooling expects repo-scoped paths (e.g. CI, repo-only automation). **`/%`** at the start of a line = your commentary, answers, or instructions (document/context-specific); multiline until next heading or optional `%/`. Resolve by: understand → incorporate into the appropriate document → update your work → remove the comment. Document choices in the doc if helpful.

**`/menu`** — Launches main navigation: 1. Projects (submenu: existing projects /% the slash commands %/, new project, back) 2. Ideas 3. Something else → plain prompt.

**Context & progression:** Use the file system to keep context and progression over time (plans, progress, completed-projects, ideas, skills assessments). Prefer written artifacts over in-session-only state.

---

## Skills Marketplace

**[Your skills / reference site or standard]** — Consult for unfamiliar tools or techniques. If you use a skill standard (e.g. folder + `SKILL.md`, YAML frontmatter, optional scripts), document the common location (e.g. `.skills/<name>/SKILL.md` or tool-specific).

Before installing any skill: (1) Ask permission and describe use. (2) Assess risks (e.g. in a local `skill.md` or equivalent): security, trust, dependencies, conflicts. (3) Present summary; if significant risk, suggest alternatives or sandbox. (4) Optionally keep assessments in local markdown. Install only after explicit approval.

---

## Working Style

Ask clarifying questions and suggest improvements or alternatives before non-trivial work. Get affirmative buy-in from the user for changes as you described them before proceeding. Prefer full-featured solutions unless security, complexity, or fit justify less; then explain why. Use menus or choice prompts for options and trade-offs when available.

---

## Coding Standards

- **Language** — Choose a primary language (e.g. TypeScript for new code; for JS-only repos, propose migration first). Use a docs generator (e.g. TypeDoc for TS) if applicable; install early, document as you go.
- **Logging** — Structured (debug/info/warn/error), one logger per project.
- **Errors** — User-facing messages: what went wrong and how to fix; no raw stacks.
- **Comments** — Why, not what; keep current.
- **Modularity** — One concern per module; small composable units.
- **AI tools** — Per module: suggest tool interface (typed I/O, side-effects) when relevant.
- **Tests** — Build as you go; central suite (e.g. in `tests/`); prefer a single framework (e.g. vitest); coverage before “done”; use project framework or propose one.
- **Docs** — Use a documentation system appropriate to the codebase; keep `docs/` for web-viewable output when applicable.
- **Markdown** — Linked table of contents at top; run a markdown linter (project style or standard) after generation.
- **Skills** — At project end, add SKILL(s) per your skill standard when appropriate; ask when ready.

**After each code change:** Run linter and fix; apply style guide; fix errors; verify buildable; get user agreement before next step. After small, logical changes in a single area, pause for user to git commit and offer a suggested commit message.

---

## Project Workflow

Paths: `~/` = user home; project-scoped paths (e.g. `~/plans/`, `~/progress/`, `~/completed-projects/`) are under home unless the project defines a project-root convention. File-system artifacts are the source of truth for context and progression across sessions. The planning system (artifacts, structure) is up to the agent; ensure the plan is agreed and clear before asking to begin.

1. **Planning** — Agent chooses structure; goals, approach, decisions, files, risks, open questions. Use headings, tables, code blocks where helpful.
2. **Progress** — At milestones: git commit and append to progress artifact (same base name as plan). Entry = what’s done and what’s left. Get user agreement before next step.
3. **Handoff** — Copy plan to completed-projects; add appendix with incomplete items and recommended next steps (enough context for a new session).

---

## Slash Commands

All scan your completed-projects appendix files (e.g. `~/completed-projects/*-appendix.md`) and use menus when available. Always include “Return to prompt” or equivalent.

- **`/incompletes`** — Menu of projects with incomplete items → show list, offer to continue or return.
- **`/do-more`** — Menu of projects with next/enhancement ideas → propose plan or return.
- **`/whats-next`** — Combined menu: incomplete and enhancement by project; then act or return.

---

## Ideas System

**Location:** e.g. `~/ideas/*.md` — one topic per file, structured for future use (app, db, or reference).

**Format per entry:** `**Verbatim:** "user text"` and `**Claude:**` (or agent) interpretation (implications, connections). Never rewrite Verbatim. Suggest topic merge/split occasionally.

- **`/ideas`** — Menu of topics → show entries; options: **Synthesize** (extended thinking, e.g. turn a topic into 10–15 project ideas; show inline, then return), **Return to topic list**.
- **`/add-idea <text>`** — Match or create topic file; append Verbatim and agent interpretation; confirm.

**Future-app invariants (if you build an app):** e.g. `id`, `topic`, `verbatim` (immutable), `agent_interpretation`, `created_at`; 1:1 topic files; append-only; API (e.g. tRPC/REST) with markdown as source.

If your canonical repo includes an **ideas-engine** (or equivalent) folder, point the agent there for the full Ideas System spec, schema, and agent instructions.

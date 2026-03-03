# Load-context: minimal context set

**Purpose:** Exact file paths for a “minimal context set” so an agent (or human) can load the smallest useful subset of the framework and start acting. Use this when token or context limits matter, or when onboarding a new agent quickly.

---

## Minimal context set (paths from repo root)

**Portal:** Paths assume the Episteme **repository root** (the directory containing `AGENTS.md` and `episteme-framework/`). If your entry point is a clone, fork, or submodule, use that root; then the paths below are correct as given.

Load these in order when you need to bootstrap with minimal reads:

| Order | Path | Why |
|-------|------|-----|
| 1 | `episteme-framework/agent-docs/meta-agent.example.md` | Cross-project behavior, slash commands (/menu, /ideas, /add-idea, /incompletes, /do-more, /whats-next), working style, coding standards, project workflow. Single source of “how to behave.” |
| 2 | `episteme-framework/my-skills/episteme-skills/SKILLS_TREE.md` | Map of all episteme skills: tree, legend, flat list. Tells you which skill to run for a given task (onboarding, project setup, ideas, code guides, menu, etc.). |
| 3 | `episteme-framework/projects/tracking-system/01-project-schemas/_project-schema.md` | Schema for project 001 (project schema doc). Needed when creating or validating a new project or when interpreting existing 001 files. |

**Optional fourth (project-specific):** If the user has an active project, add the project’s 001 schema file (e.g. `projects/example-project/001-sample-project-schema.md`) or the tracking _docs folder so you know the local layout.

---

## Why this set is the exemplar

- **Meta-agent** — Defines *what* to do (slash commands, workflows, conventions) and *when* to delegate to skills. Without it, the agent doesn’t know the menu or how to progress.
- **Skills tree** — Defines *which* skill to run for each kind of task. Without it, the agent must guess or read many SKILL.md files.
- **Project schema** — Defines the shape of project artifacts (001–005). Without it, the agent can’t create or validate project docs correctly.

Together these three (plus optional project 001) give “behavior + skill routing + project shape” in a minimal number of files. For perusal only (no acting), use [LIBRARY-MAP.md](LIBRARY-MAP.md) or [INDEX.md](../INDEX.md) instead.

---

## One-line list (copy-paste)

```
episteme-framework/agent-docs/meta-agent.example.md
episteme-framework/my-skills/episteme-skills/SKILLS_TREE.md
episteme-framework/projects/tracking-system/01-project-schemas/_project-schema.md
```

Optional: append the path to the current project’s 001 file if known.

# Overrides and local configuration

**Purpose:** Where to set paths and options so the framework (and your agent) use your preferred locations. Nothing here is required; defaults work if you don’t set anything.

---

## Override locations

| What | Default | How to override |
|------|---------|------------------|
| **Ideas root** | `~/ideas/` | Set env var `IDEAS_ROOT` to a directory path. The Ideas System (e.g. ideas-engine, list-topics.sh, /ideas) uses this. |
| **Completed projects** | `~/completed-projects/` | Described in meta-agent for /incompletes, /do-more, /whats-next. Use that path or document your own in your project’s agent doc. |
| **Local scratch / config** | (none) | Use a folder **.episteme-local/** at repo root for files you don’t want committed. It’s in .gitignore. Put local config, scratch notes, or overrides there and point the agent at them if needed. |
| **Project ideas file** | (none) | **project-ideas.ai** at repo root is in .gitignore; use it for personal idea drafts if you like. |

---

## Env vars (optional)

- **IDEAS_ROOT** — Directory containing idea topic files (`*.md`). Default: `~/ideas/`.
- Any other vars (e.g. API keys, paths) should stay in env or a **local-only** file; see [SECRETS.md](../../SECRETS.md) (at repo root) so they never get pushed.

---

## Meta-agent and your repo

The meta-agent template ([meta-agent.example.md](meta-agent.example.md)) has placeholders for “your canonical repo” and paths. When you fork or personalize, fill those in and keep one copy of the meta-agent as the source of truth; point each project’s AGENTS.md or CLAUDE.md at it.

# Episteme — agent bootstrap

This repository is the **Episteme** library and framework: a file-based, passive “Super Library” of document concepts, schemas, skills, and guides that agents can pull in à la carte to build project context and personalize behavior.

---

## Portal and paths

**Where is the portal?** All paths in this repo assume the **repository root** is the portal: the directory that contains `AGENTS.md` (this file) and the `episteme-framework/` folder. If you are given a link or path to this repo (e.g. a clone, fork, or submodule), treat that root as the base. Paths in docs are from repo root unless stated otherwise (e.g. LOAD-CONTEXT and the table below). Overrides (IDEAS_ROOT, completed-projects, etc.) are in [episteme-framework/agent-docs/OVERRIDES.md](episteme-framework/agent-docs/OVERRIDES.md).

---

## Start here

1. **Canonical agent entry** — Read **[episteme-framework/agent-docs/README.md](episteme-framework/agent-docs/README.md)** (ai-docs index), then **[episteme-framework/agent-docs/meta-agent.example.md](episteme-framework/agent-docs/meta-agent.example.md)** for cross-project behavior, slash commands, and conventions.
2. **Onboarding** — If you are new to this repo, run the **ONBOARD_AGENT_TO_EPISTEME** skill (see [episteme-framework/my-skills/episteme-skills/ONBOARD_AGENT_TO_EPISTEME/](episteme-framework/my-skills/episteme-skills/ONBOARD_AGENT_TO_EPISTEME/)) or read: ai-docs index → meta-agent → [skills tree](episteme-framework/my-skills/episteme-skills/SKILLS_TREE.md).
3. **Peruse only** — To explore the library without acting, use **[episteme-framework/agent-docs/LIBRARY-MAP.md](episteme-framework/agent-docs/LIBRARY-MAP.md)** for a map of all sections and links.

---

## For your own projects

Copy or link this bootstrap (or a `CLAUDE.md` with the same content) into a project and **point the meta-agent path** to this repo’s `episteme-framework/agent-docs/meta-agent.example.md`—or to your fork. Keep project-specific overrides in one place (e.g. your project’s AGENTS.md or CLAUDE.md); the meta-agent stays the single source of universal behavior.

---

## Paths (from repo root)

| What | Where |
|------|--------|
| Framework index (sitemap) | `episteme-framework/INDEX.md` |
| Ai-docs index | `episteme-framework/agent-docs/README.md` |
| Meta-agent (template) | `episteme-framework/agent-docs/meta-agent.example.md` |
| Library map (perusal) | `episteme-framework/agent-docs/LIBRARY-MAP.md` |
| Skills tree + list | `episteme-framework/my-skills/episteme-skills/SKILLS_TREE.md`, `README.md` |
| Tracking system (_docs) | `episteme-framework/projects/tracking-system/` |
| Ideas engine (spec) | `episteme-framework/ideas-engine/` |
| Code guides (master) | `episteme-framework/language-style-guides/public/master/` |
| Overrides (paths, env) | `episteme-framework/agent-docs/OVERRIDES.md` |
| Load-context (minimal set) | `episteme-framework/agent-docs/LOAD-CONTEXT.md` |
| Config / templates | `episteme-framework/config-files/`, `episteme-framework/project-documentation/` |

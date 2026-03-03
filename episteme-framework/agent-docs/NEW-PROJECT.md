# New project: what to copy

**Purpose:** Minimal steps to give a new codebase Episteme agent context. Use this when you start a project and want the agent to use the meta-agent, skills, and (optionally) tracking.

---

## Required (minimal)

1. **Bootstrap at project root**
   - Add **AGENTS.md** or **CLAUDE.md** at the new project’s repo root.
   - Content: state that the agent should read the Episteme meta-agent for behavior and slash commands, and give the **path to the meta-agent** (this repo or your fork).
   - Example: *“Read [path-to-episteme]/episteme-framework/agent-docs/meta-agent.example.md for slash commands and conventions. Point to that file (or your fork’s copy).”*
   - You can copy the “Start here” and “Paths” sections from this repo’s [AGENTS.md](../../AGENTS.md) and adjust paths so they point to Episteme (same repo, submodule, or fork).

2. **Meta-agent path**
   - Set the meta-agent URL/path once (in that AGENTS.md/CLAUDE.md). The meta-agent is the single source for: /menu, /ideas, /add-idea, /incompletes, /do-more, /whats-next, working style, and when to call which skills.
   - If Episteme is a submodule or sibling repo, use a relative path (e.g. `../episteme/episteme-framework/agent-docs/meta-agent.example.md`) or absolute path; agents resolve from project root.

---

## Optional

3. **Tracking (_docs + sample 001)**
   - To use the project-tracking system (001–005 schemas, planning, progress, completed, after-action): copy or link the **_docs** from `episteme-framework/projects/tracking-system/` (e.g. `01-project-schemas/`, `02-planning/`, …) into your project (e.g. `docs/tracking/` or `_docs/`).
   - Optionally copy **one sample 001** (e.g. from `episteme-framework/projects/example-project/`) so the agent sees the schema in use. Then create your own 001 for the new project.
   - Skills like SETUP_NEW_PROJECT and MANAGE_PROJECT expect these _docs; see [projects/tracking-system/](../projects/tracking-system/) and the skills tree.

4. **Ideas**
   - Ideas live in `~/ideas/` (or IDEAS_ROOT) by default; no need to copy anything into the project. Point the agent at the meta-agent; /ideas and /add-idea use IDEAS_ROOT. See [OVERRIDES.md](OVERRIDES.md).

5. **Code guides**
   - For language-specific style: the agent can read from Episteme’s `language-style-guides/public/master/` via the path you set in the bootstrap. No copy into the project required.

---

## Checklist

| Step | Action |
|------|--------|
| 1 | Create AGENTS.md or CLAUDE.md at project root. |
| 2 | In it, point to the meta-agent file (this repo or fork). |
| 3 | (Optional) Copy tracking _docs and one sample 001 if you want project tracking. |
| 4 | (Optional) Set IDEAS_ROOT if not using ~/ideas. See OVERRIDES.md. |

After that, the agent can use the meta-agent and skills from Episteme without duplicating the whole framework into the project.

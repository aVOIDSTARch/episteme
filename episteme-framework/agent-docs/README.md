# ai-docs

**Purpose:** Agent- and human-facing docs for the episteme framework: skills map (episteme-skills), code guide usage, and references to schemas elsewhere.

---

## Index

| Doc | Purpose |
|-----|---------|
| **Episteme skills map** | [my-skills/episteme-skills/SKILLS_TREE.md](../my-skills/episteme-skills/SKILLS_TREE.md) — tree, legend, and flat list of episteme skills. See also [episteme-skills/README.md](../my-skills/episteme-skills/README.md). |
| **[LIBRARY-MAP.md](LIBRARY-MAP.md)** | Passive perusal map: links to ai-docs, skills, tracking, ideas-engine, code guides, config. No actions; to act use meta-agent + skills. |
| **[INDEX.md](../INDEX.md)** | Framework sitemap: one doc linking every major section (agent-docs, my-skills, projects, ideas-engine, language-style-guides). |
| **[MANIFEST.md](../MANIFEST.md)** | Programmatic list of all _*.md, SKILL.md, code-guide-*.ai (regenerate with `scripts/generate_manifest.py`). |
| **[OVERRIDES.md](OVERRIDES.md)** | Where to set IDEAS_ROOT, completed-projects path, .episteme-local; env vars. |
| **[NEW-PROJECT.md](NEW-PROJECT.md)** | What to copy into a new project (AGENTS.md/CLAUDE.md, point to meta-agent; optional tracking _docs). |
| **[LOAD-CONTEXT.md](LOAD-CONTEXT.md)** | Minimal context set: exact file paths (meta-agent, skills tree, project schema) + why this set; for token-limited or quick bootstrap. |

---

## Related (in framework)

- **Meta-agent:** [meta-agent.example.md](meta-agent.example.md) — cross-project behavior, slash commands, conventions.
- **Schemas (_docs):** [projects/tracking-system/](../projects/tracking-system/) (01–05); [ideas-engine/_idea-file-schema.md](../ideas-engine/_idea-file-schema.md); [my-skills/skill-definition/](../my-skills/skill-definition/), [episteme-skills/](../my-skills/episteme-skills/), [imported-skills/](../my-skills/imported-skills/).
- **Code guide master:** [language-style-guides/public/master/code-guide-master-file.md](../language-style-guides/public/master/code-guide-master-file.md).
- **Ideas engine:** [ideas-engine/](../ideas-engine/) (README, schema, AGENT-INSTRUCTIONS, template).

**When personalizing:** You can add locally (e.g. in your fork or project) optional docs such as a capabilities checklist, skill-creation notes, project-schema-setup notes, or _docs design notes; the base framework does not depend on them.

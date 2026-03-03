# The Episteme Project

A file-based, passive “Super Library” of document concepts, schemas, skills, and guides that agents can pull in à la carte to build project context with bespoke personalization.

---

## Project Information

- **Project Author(s):** The Fail Academy
- **Creation Date:** March 2, 2026
- **Purpose of Project:** To provide an intellectual framework of interchangeable parts that an agent can pull in à la carte to build a context for a project with bespoke personalization and ease heretofore unheard of in the artificial intelligence pantheon.
- **Primary Content:** Directory structure, document concepts, episteme-framework (agent-docs, skills, tracking system, ideas-engine, language-style-guides, config).
- **Repository URL:** https://github.com/aVOIDSTARch/episteme.git

---

## Project Structure

```
episteme/
├── AGENTS.md                 # Agent bootstrap — start here
├── README.md                 # This file
├── .cursorrules              # Cursor: read AGENTS.md + framework
├── .cursor/rules/            # Cursor rules (episteme-bootstrap.mdc)
├── episteme-framework/       # Framework content (library + agent docs)
│   ├── agent-docs/           # Ai-docs index, meta-agent, library map, TODO
│   ├── my-skills/            # Skill definition, episteme-skills, examples
│   ├── projects/             # Tracking system (_docs) + example-project
│   ├── ideas-engine/         # Ideas spec, schema, AGENT-INSTRUCTIONS
│   ├── language-style-guides/# Master code guides + public scraped
│   ├── config-files/         # .gitignore universal, etc.
│   └── project-documentation/# README template
├── LICENSE
└── .gitignore
```

---

## For agents

**Start here:** Read [AGENTS.md](AGENTS.md) at repo root. It points to the canonical agent entry ([episteme-framework/agent-docs/README.md](episteme-framework/agent-docs/README.md)), the meta-agent template, and the library map for perusal.

---

## License

MIT License — see [LICENSE](LICENSE) for details.

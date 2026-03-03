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

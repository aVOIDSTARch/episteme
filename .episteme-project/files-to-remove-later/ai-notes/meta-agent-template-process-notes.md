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

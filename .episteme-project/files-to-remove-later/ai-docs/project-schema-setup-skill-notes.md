# Process notes: Project schema & SETUP_NEW_PROJECT SKILL

**Purpose:** Notes for creating the SETUP_NEW_PROJECT SKILL.md. The schema spec lives in `projects/tracking-system/01-project-schemas/_project-schema.md` and defines *what* to gather; this file captures *how* the skill should behave (gathering process, UX, divergent pathways). Underscore-prefixed docs (`_project-schema.md`) do not contain skill descriptions or engineering—only the schema structure and REQUIRED_SKILLS. Skill behavior lives here.

---

## Gathering process (for SETUP_NEW_PROJECT SKILL)

The SKILL that creates or updates project schemas from the schema spec should follow these behaviors. They ensure good data, minimal friction, and room for creative interaction.

### 1. User inputs

Gather from the user only what they can reasonably supply (Project name/slug, Summary, Owner, Type, Stack, Deployment when known, Constraints, Repo path). Do not require the user to fill agent-observed fields.

### 2. Multiple choice when possible

Where the schema or the spec defines a fixed set (e.g. **Deployment** enum, **Type** taxonomy), present choices as a multiple-choice menu or list instead of freeform. Reduces errors and keeps values consistent.

### 3. Confirmation of observed data

For **agent-observed** fields (Dev environment, Agents / models), the agent infers values from context, then **presents them to the user for confirmation**. Example: “I detected: macOS, Cursor, Node 20. Confirm, or tell me what to change.” Record only after the user confirms or corrects.

### 4. Type check and sanity-check freeform text

For freeform fields (e.g. Summary, project name, Constraints), the agent should:

- **Check** input for relevance and sanity (e.g. project name looks like a slug; summary is one line and on-topic).
- **Suggest corrections gently** when something seems off: e.g. “I see you said *X*. I believe you may mean *Y* (e.g. [brief reason]). May I record it as *Y*, or would you prefer your exact input *X*?”
- Always offer **“record your exact input”** so the user can keep their wording. Never overwrite without explicit choice.

### 5. Divergent pathways (creative interaction)

Offer optional branches so the user can go deeper or defer:

| Pathway | Behavior |
|--------|----------|
| **Project name from prompt** | If the user describes the project but hasn’t given a name/slug, offer: “Would you like me to suggest a project name/slug from your description?” Then propose one or two options; user picks or supplies their own. |
| **Suggest language / stack / dev env from concept** | From the user’s summary or type (e.g. “web app”, “CLI”), suggest a plausible stack or dev env (e.g. “This sounds like a web app—consider TypeScript, React, Node. Use these, edit, or skip for now?”). User can accept, edit, or leave blank. |
| **Set up environments later** | Offer: “You can set up runtimes and tooling (Node, pnpm, etc.) now or later via a separate **Set up environment** SKILL. Proceed with schema only, or run environment setup after?” Lets the user defer environment setup to another SKILL.md without blocking schema creation. |

These pathways are **optional**: the user may answer directly, accept suggestions, or choose a divergent path. The skill should feel supportive, not prescriptive.

---

## For the future SETUP_NEW_PROJECT SKILL.md

1. **Goal:** Create or update a project schema file from the spec in `_project-schema.md`, gathering required and optional fields, with good UX and optional divergent pathways.
2. **Inputs:** User (for user-supplied fields); agent context (for agent-observed fields); schema spec (`_project-schema.md`) and enums/conventions there; REQUIRED_SKILLS from the schema or project so the agent knows which other skills to pull.
3. **Output:** A project schema file (e.g. `NNN-<slug>-schema.md`) in `01-project-schemas/`, and optionally amendments to REQUIRED_SKILLS as the project progresses or the user requests.

---

## File locations (this repo)

- **Schema spec (no skill/engineering):** `projects/tracking-system/01-project-schemas/_project-schema.md`
- **Skill notes (this file):** `ai-docs/project-schema-setup-skill-notes.md`

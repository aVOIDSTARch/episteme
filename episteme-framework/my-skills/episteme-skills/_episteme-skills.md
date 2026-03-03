# EPISTEME SKILLS

#### LEADING UNDERSCORE DOCUMENT CONCEPT SUMMARY

**Schema for episteme-native skills.** Defines how skills unique to this framework are organized: one folder per skill (folder name = skill name), small to small-medium scope, with complex skills as a constellation of simpler skills. `_` docs = schema, enums, conventions only. These skills are necessary to navigate the framework efficiently; they are not likely of much use to AGENTS outside this context.

---

## Purpose

**Episteme skill** = a skill authored and maintained in this repo, unique to the episteme framework. It is necessary for agents to navigate the framework efficiently but is not likely of broad use outside this context. Each skill is a **folder** with content files and subfolders; **folder name = skill name**. One small to small-medium sized skill per folder. Complex SKILLs combine a constellation of simpler SKILLs into a process-like skill that still has singleness of purpose.

---

## What This Is Not

Not the skill-definition schema (that’s in skill-definition/). Not imported skills (those are in imported-skills/). Only the organization and requirements for *episteme-native* skills.

---

## Required Information (per skill)

Each skill in this folder MUST be a folder whose name is the skill name. The folder MUST contain (per skill-definition and skill-standard):

| Section | Content | Example / notes |
|--------|---------|------------------|
| **Name** | Skill slug; must match folder name. | `setup-new-project` → folder `setup-new-project/` |
| **Description** | One or two sentences; when to use. | As in skill-definition. |
| **When to use** | Trigger for the agent. | As in skill-definition. |
| **Instructions** | What the agent does. | Main body of SKILL.md. |

---

## Optional Information (per skill)

| Section | Content | When to use |
|--------|---------|-------------|
| **Read first** | Paths or docs. | As in skill-definition. |
| **REQUIRED_SKILLS** | Other skills to pull first (constellation). | When this skill composes simpler skills. |
| **Examples / reference** | Links or subdocs. | As in skill-definition. |
| **Meta-doc** | Meta-doc for this skill (as for imported skills). | When we add meta-docs for all skills; particularly important for imported, but can be used for episteme skills too. |

---

## Conventions

- **Naming:** `_episteme-skills.md` = this _doc. Each skill = one subfolder; **folder name = skill name**. Skill content (SKILL.md and other files) lives inside that folder.
- **Location:** Episteme skills live in this folder (episteme-skills). Each skill is `episteme-skills/<skill-name>/` with SKILL.md and any content files or subfolders.
- **Size:** One small to small-medium sized skill per folder. Complex skills: combine a constellation of simpler skills into one process-like skill that still has singleness of purpose (e.g. one SKILL.md that references REQUIRED_SKILLS and orchestrates steps).
- **Format:** SKILL.md and folder layout follow `my-skills/skill-definition/_skill-definition.md` and `skill-definition/skill-standard/`. Check the website for the standard. Meta-docs can be added for all skills (particularly for imported ones).
- **Agent use:** When creating a new episteme skill, add a subfolder here with the skill name; put SKILL.md and any content inside. Reference from project schemas or skills-to-make-first as needed. Use REQUIRED_SKILLS to compose simpler skills when building a process-like skill.

---

## Minimal Example Structure

One folder per skill; folder name = skill name:

```
episteme-skills/
├── _episteme-skills.md          (this _doc)
├── setup-new-project/
│   ├── SKILL.md
│   └── (other content files/folders as needed)
└── episteme-design/
    ├── SKILL.md
    └── (other content as needed)
```

Each SKILL.md: see `my-skills/skill-definition/_skill-definition.md`. Folder design and structure: see `skill-definition/skill-standard/` and the website.

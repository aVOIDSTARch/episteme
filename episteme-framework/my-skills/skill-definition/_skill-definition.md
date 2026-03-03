# SKILL DEFINITION

#### LEADING UNDERSCORE DOCUMENT CONCEPT SUMMARY

**Schema for skill definitions.** Defines what every skill definition in this system must or may contain: the structure for SKILL.md (or equivalent) so agents and humans know how to create, read, and reference skills. `_` docs = schema, enums, conventions only; no implementation. Skill behavior and authoring flow → notes or SKILL if added.

---

## Purpose

**Skill definition** = the schema for a single skill: name, description, when to use, instructions, and optional references. A skill is always a **folder** with content files and subfolders; **folder name = skill name**. One definition per skill; the canonical form is SKILL.md (and other content) inside that folder. Check the website for the standard. Meta-docs are used for all skills, particularly imported ones. Human- and agent-readable; ensures consistent structure across episteme and imported skills.

---

## What This Is Not

Not the skill standard (that may live in skill-standard/). Not the list of imported or episteme skills (those are in imported-skills/, episteme-skills/). Only the structure of one skill definition.

---

## Required Information

MUST include these so a skill is identifiable and usable.

| Section | Content | Example / notes |
|--------|---------|------------------|
| **Name** | Machine-friendly slug (e.g. for folder or ID). | `setup-new-project`, `rust-clippy-lint` |
| **Description** | One or two sentences: what the skill does and when to use it. | “Create or update a project schema from user input; use when starting a new project.” |
| **When to use** | Trigger: when should an agent pull or apply this skill? | Short list or one paragraph; e.g. “User asks to set up a project; agent needs to gather schema fields.” |
| **Instructions** | What the agent must do (steps, rules, or reference to doc). | Main body; can be sections. How to perform the skill. |

---

## Optional Information

Include when relevant.

| Section | Content | When to use |
|--------|---------|-------------|
| **Read first** | Paths or docs the agent should read before executing. | When skill depends on schema, spec, or other docs. |
| **Inputs / outputs** | What the skill expects and produces. | When clarifying contract. |
| **REQUIRED_SKILLS** | Other skills the agent should pull first (name + location). | When this skill depends on others. |
| **Examples** | Short usage examples or links. | When examples reduce ambiguity. |
| **Location** | Path or URL to this skill’s SKILL.md or folder. | When the definition doc is not the canonical file. |
| **Original source URI** | Canonical URI for where this skill originated (e.g. `https://...`, registry URL, or `file://...`). | Required for imported; recommended for episteme. Provenance and citation; detect unauthorized copies or drift. |
| **Integrity hash** | Hash (e.g. SHA-256) of skill content (e.g. SKILL.md or normalized folder) + algorithm name. | When verification is needed: detect tampering, meddling, or prompt injection. Verify before use when security matters. |
| **Schema version** | Version of this skill-definition schema (e.g. `1`). | If you version the spec. |

---

## Conventions

- **Naming:** `_skill-definition.md` = this _doc. Each skill = a folder; folder name = skill name. Instance: skill’s `SKILL.md` (and content) inside that folder.
- **Location:** Skills live as folders under episteme-skills/ or imported-skills/; folder name = skill name. Skill-definition schema applies to the content of each skill folder.
- **Format:** Markdown; required sections as level-2 headings. YAML frontmatter (name, description) is common for SKILL.md; this schema can be satisfied with or without frontmatter.
- **Agent use:** When creating or validating a skill, ensure required sections exist. When referencing a skill (e.g. in REQUIRED_SKILLS), use name + location.

---

## Minimal Example Structure

```markdown
# <Skill display name>

## Name
<slug>

## Description
<one or two sentences; when to use in plain language>

## When to use
<trigger: when should the agent pull or apply this skill?>

## Instructions
<steps, rules, or “See …” reference. Main body of the skill.>

## Read first
(optional; paths or docs)

## REQUIRED_SKILLS
(optional; table: Skill name | Location)

## Location
(optional; path to SKILL.md or folder)

## Original source URI
(optional; canonical URI for provenance; required for imported skills)

## Integrity hash
(optional; e.g. algorithm + hash of SKILL.md or folder; for verification, tampering / prompt-injection detection)
```

Optional sections: same heading style. One line or short list per section.

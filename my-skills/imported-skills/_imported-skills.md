# IMPORTED SKILLS

#### LEADING UNDERSCORE DOCUMENT CONCEPT SUMMARY

**Schema for imported-skill meta-docs.** Defines what we record for each skill imported from the website or other external sources: location, risk assessment, and relevant conversation notes the AGENT has with other ENTITIES. `_` docs = schema, enums, conventions only. One meta-doc per imported skill.

---

## Purpose

**Imported skill** = a skill from outside this repo (e.g. from the website, a registry, or another repo). This folder holds a **meta-doc** per imported skill. The meta-doc contains where the skill lives, the full risk assessment (security, trust, dependencies, conflicts), and any relevant conversation notes between the AGENT and other ENTITIES. Meta-docs are required for all imported skills.

---

## What This Is Not

Not the skill definition schema (that’s skill-definition/). Not episteme-native skills (those are in episteme-skills/). Only the meta-documentation for *imported* skills.

---

## Required Information

Each imported skill MUST have a meta-doc that includes:

| Section | Content | Example / notes |
|--------|---------|------------------|
| **Name** | Skill name or slug as we reference it. | `create-rule`, `rust-clippy-lint` |
| **Original source URI** | Canonical URI for where this skill came from (website, registry, repo). | `https://...`, registry URL. Required for provenance and verification. |
| **Location** | Path in this workspace (or where we use it). Folder name = skill name. | `my-skills/imported-skills/<skill-name>/` or “use from Cursor skills”. |
| **Risk assessment** | Security, trust, dependencies, conflicts; summary; alternatives or sandbox if significant risk. | As discussed: assess before use; document in meta-doc. |
| **Conversation notes** | Relevant notes from the AGENT’s conversations with other ENTITIES about this skill (decisions, caveats, usage). | Short bullets or summary; keep updated as needed. |
| **Integrity hash** | Hash (e.g. SHA-256) of skill content + algorithm. Verify before use to detect tampering, meddling, or prompt injection. | Algorithm + hash value; recompute and compare when in doubt. |

---

## Optional Information

| Section | Content | When to use |
|--------|---------|-------------|
| **Source** | Same as Original source URI; short label if kept alongside. | When you want a duplicate field. |
| **Version / date** | Version or import date. | When tracking updates. |
| **Description** | One-line reminder of what the skill does. | When the name isn’t enough. |
| **References** | Link to skill-definition or SKILL.md. | When we want to point to the actual skill content. |

---

## Conventions

- **Naming:** `_imported-skills.md` = this _doc. Each imported skill = one subfolder named after the skill (folder name = skill name), containing the skill content and a meta-doc (e.g. `META.md` or `<skill-name>-meta.md`).
- **Location:** Meta-docs and (if copied) skill content live in this folder (imported-skills). One folder per imported skill; folder name = skill name.
- **Format:** Markdown; required sections as level-2 headings. Risk assessment can be a subsection with Security, Trust, Dependencies, Conflicts, Summary, Alternatives/sandbox.
- **Agent use:** When adding an imported skill, create the skill folder and meta-doc. Run risk assessment (security, trust, dependencies, conflicts); document in meta-doc. Record relevant conversation notes with other ENTITIES in Conversation notes.

---

## Minimal Example Structure

```markdown
# IMPORTED: <skill-name>

## Name
<slug>

## Original source URI
<canonical URL or registry URI>

## Location
<path in this workspace; folder name = skill name>

## Risk assessment
- **Security:** …
- **Trust:** …
- **Dependencies:** …
- **Conflicts:** …
- **Summary:** …
- **Alternatives / sandbox:** (if significant risk)

## Conversation notes
<relevant notes from AGENT with other ENTITIES>

## Integrity hash
<algorithm> <hash value> (verify before use)

## Version / date
(optional)
```

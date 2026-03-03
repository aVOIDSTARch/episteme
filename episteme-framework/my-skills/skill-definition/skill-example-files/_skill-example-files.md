# SKILL EXAMPLE FILES

#### LEADING UNDERSCORE DOCUMENT CONCEPT SUMMARY

**Schema for skill example files.** Defines what goes in this folder: example skills that conform to skill-definition and skill-standard. Examples are abstract and agnostic (e.g. **FLIP_WIDGET**). `_` docs = schema, conventions only. Each example is a folder (folder name = skill name) with SKILL.md and optional content.

---

## Purpose

**Skill example files** = sample skills used as templates or references. This folder holds one or more example skills so agents and humans can copy or adapt structure. Each example is a **folder** (folder name = skill name) with content; examples conform to `_skill-definition.md` and `skill-standard/`. We use **FLIP_WIDGET** as the abstract, agnostic example—applicable to any context where “flip” (state or view) applies.

---

## What This Is Not

Not the schema (that’s _skill-definition.md). Not the standard (that’s skill-standard/). Not live skills (those are in episteme-skills/ or imported-skills/). Only examples.

---

## Required Information (per example)

Each example in this folder SHOULD:

| Section | Content | Example / notes |
|--------|---------|------------------|
| **Be a folder** | Folder name = skill name. Contains SKILL.md and any optional content. | Same layout as real skills. |
| **Conform to skill-definition** | SKILL.md has Name, Description, When to use, Instructions (or clear placeholder). | So the example is valid. |
| **Be clearly an example** | Folder or SKILL.md indicates it’s a sample (e.g. lives in skill-example-files; title can say “Example”). | So it isn’t mistaken for a live skill. |
| **Be abstract / agnostic** | Content is generic enough to apply across contexts (e.g. FLIP_WIDGET: flip a widget state or view). | So it’s reusable as a template. |

---

## Optional Information

| Section | Content | When to use |
|--------|---------|-------------|
| **Index** | A short index doc listing examples and what each demonstrates. | When there are several examples. |

---

## Conventions

- **Naming:** `_skill-example-files.md` = this _doc. Each example = one subfolder; folder name = skill name (e.g. `FLIP_WIDGET/`).
- **Location:** This folder (skill-definition/skill-example-files). Examples only; real skills live in episteme-skills/ or imported-skills/.
- **Format:** Each example folder contains SKILL.md (and optionally other files) following the skill-definition and skill-standard. FLIP_WIDGET is the reference abstract, agnostic example.
- **Agent use:** When creating a new skill, copy or adapt from an example here (e.g. FLIP_WIDGET); ensure result conforms to _skill-definition.md and skill-standard.

---

## Minimal Example Structure

This folder contains one or more example **folders**. Each folder:

- Name = skill name (e.g. `FLIP_WIDGET`)
- Contains `SKILL.md` with at least: Name, Description, When to use, Instructions
- Is abstract/agnostic where possible (FLIP_WIDGET)

Optional: index file (e.g. `000-index.md`) listing examples and what they show.

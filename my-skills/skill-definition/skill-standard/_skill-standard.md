# SKILL STANDARD

#### LEADING UNDERSCORE DOCUMENT CONCEPT SUMMARY

**Schema for the skill standard document.** Defines the rules, regulations, folder design, and structure design rules for a SKILL. All skills (episteme and imported) conform to this standard. `_` docs = schema, conventions only. **Check the website for the canonical standard;** this _doc defines what the standard document(s) in this folder must contain.

---

## Purpose

**Skill standard** = the rules and regulations for skills: how a skill folder is designed and structured (folder name = skill name, required files, layout), what goes in SKILL.md, and any tool- or org-specific rules. Instance doc(s) in this folder state the canonical standard; refer to the website for the full spec. All skills follow this folder design and structure.

---

## What This Is Not

Not the skill-definition schema (that’s the parent _skill-definition.md). Not individual skill content. Only the standard document(s) that define rules, folder design, and structure.

---

## Required Information

The standard document(s) in this folder MUST state:

| Section | Content | Example / notes |
|--------|---------|------------------|
| **Scope** | What this standard applies to (all skills, episteme, imported, tool). | One short paragraph. |
| **Folder design** | Rules for the skill folder: folder name = skill name; what files/subfolders are required or allowed. | So every skill is a folder with a defined layout. |
| **Structure design rules** | Rules for SKILL.md and other content: required/optional sections, frontmatter, naming. Include **Original source URI** (required for imported; recommended for all) and **Integrity hash** (for verification; detect tampering, meddling, prompt injection). | Can reference skill-definition; add regulations (e.g. YAML keys, section order). |
| **Location / layout** | Where skills live (episteme-skills/, imported-skills/) and how they are organized. | So agents and humans know where to find skills. |

---

## Optional Information

| Section | Content | When to use |
|--------|---------|-------------|
| **Version** | Standard version (e.g. `1`). | When you version the standard. |
| **References** | Link to website, skill-definition, tool docs. | When useful. |

---

## Conventions

- **Naming:** `_skill-standard.md` = this _doc. Instance: one doc (e.g. `skill-standard.md`) or a small set that together form the standard.
- **Location:** This folder (skill-definition/skill-standard). Defines the standard; actual skills live in episteme-skills/ or imported-skills/.
- **Format:** Markdown; required sections as level-2 headings.
- **Agent use:** When creating or validating a skill, check the website for the standard and ensure the skill folder and content follow this folder design and structure design rules.

---

## Minimal Example Structure

```markdown
# Skill standard

## Scope
<what this standard applies to>

## Folder design
<rules: folder name = skill name; required/allowed files and subfolders>

## Structure design rules
<rules for SKILL.md and content; required/optional sections; frontmatter>

## Location / layout
<where skills live; episteme-skills/, imported-skills/>
```

Reference the website for the full standard.

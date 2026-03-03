# Notes for creating SKILLs (collected)

**Purpose:** Central notes to create SKILLs from later. Each section summarizes purpose, inputs/outputs, key references, and behavior so a future agent or human can author the SKILL.md. **Running list of candidates:** `ai-docs/skills-to-make-first.md`.

---

## 1. Project schema & tracking system (existing)

| Skill | Notes location | Summary |
|-------|----------------|--------|
| **SETUP_NEW_PROJECT** | `ai-docs/project-schema-setup-skill-notes.md` | Schema: `_project-schema.md`. Behavior: user inputs, multiple choice, confirm observed data, sanity-check freeform, divergent pathways (name suggestions, set up environment later). |
| **EPISTEME_DESIGN** | `ai-docs/_docs-format-and-design-notes.md`, `ai-docs/_docs-design.md` | _Docs design language: template structure, naming, design principles. Skill: create or validate _docs and instance docs. |
| **Set up environment** | `ai-docs/project-schema-setup-skill-notes.md` (pathway) | Deferrable from SETUP_NEW_PROJECT; set up runtimes, tooling (Node, pnpm, etc.). |
| **Meta-agent template** | `ai-docs/meta-agent-template-process-notes.md` (or equivalent) | Turn project/user-specific agent doc into reusable template. |

---

## 2. My-skills: create or validate a skill

**Potential SKILL name:** CREATE_OR_VALIDATE_SKILL (or CREATE_SKILL, VALIDATE_SKILL split).

**Purpose:** Create a new skill folder (episteme or example) or validate an existing skill against the skill-definition and skill-standard. Folder name = skill name; one small to small–medium skill per folder; complex skills = constellation of simpler skills.

**Inputs:** User or task: skill name, description, when to use, instructions (or path to existing skill to validate). Optional: copy from FLIP_WIDGET or another example.

**Outputs:** A skill folder with SKILL.md (and optional content) that conforms to `_skill-definition.md` and `skill-standard/`; or a validation report (missing sections, non-conformant layout).

**Key references:**
- `my-skills/skill-definition/_skill-definition.md` (required/optional sections)
- `my-skills/skill-definition/skill-standard/_skill-standard.md` (folder design, structure rules)
- `my-skills/skill-definition/skill-example-files/FLIP_WIDGET/` (example)
- `my-skills/skill-definition/skill-example-files/_skill-example-files.md`
- Website for canonical skill standard

**Behavior notes:** Check website for standard. Enforce: skill = folder, folder name = skill name. Keep scope small to small–medium; for complex workflows, use REQUIRED_SKILLS to compose. **Provenance & integrity:** Every skill should have **Original source URI** (required for imported; recommended for episteme). When verification is needed, include **Integrity hash** (algorithm + hash of SKILL.md or normalized folder); verify before use to detect tampering, meddling, or prompt injection. Optionally offer “copy from FLIP_WIDGET” or “validate only.”

---

## 3. My-skills: imported skill meta-doc

**Potential SKILL name:** IMPORTED_SKILL_META_DOC (or RECORD_IMPORTED_SKILL).

**Purpose:** When an imported skill (from website or other source) is added or updated, create or update its meta-doc with location, risk assessment, and conversation notes (AGENT with other ENTITIES).

**Inputs:** Skill name/source; where it’s located; risk assessment (security, trust, dependencies, conflicts; summary; alternatives/sandbox if significant risk); relevant conversation notes.

**Outputs:** A meta-doc (e.g. META.md or `<skill-name>-meta.md`) in the skill’s folder (or in imported-skills index) with required sections.

**Key references:**
- `my-skills/imported-skills/_imported-skills.md` (required: Name, Original source URI, Location, Risk assessment, Conversation notes, Integrity hash)
- Risk flow from meta-agent: ask permission, assess risks (security, trust, dependencies, conflicts), present summary, suggest alternatives/sandbox if needed, keep assessments in markdown

**Behavior notes:** Risk assessment is required in the meta-doc. **Original source URI** = canonical URI for provenance. **Integrity hash** = algorithm + hash; recompute and compare before use when security matters (tampering, meddling, prompt injection). Conversation notes = relevant notes from AGENT with other ENTITIES about this skill. One folder per imported skill; folder name = skill name.

---

## 4. My-skills: episteme skill scaffold

**Potential SKILL name:** EPISTEME_SKILL_SCAFFOLD (or SCAFFOLD_EPISTEME_SKILL).

**Purpose:** Scaffold a new episteme (framework) skill: create folder (folder name = skill name), SKILL.md stub conforming to skill-definition, optional README or placeholder. For framework navigation; not for general use outside episteme.

**Inputs:** Skill name (slug), short description, when to use (trigger). Optional: REQUIRED_SKILLS (constellation of simpler skills).

**Outputs:** `my-skills/episteme-skills/<skill-name>/` with SKILL.md (Name, Description, When to use, Instructions placeholder) and optional content.

**Key references:**
- `my-skills/episteme-skills/_episteme-skills.md`
- `my-skills/skill-definition/_skill-definition.md`
- `my-skills/skill-definition/skill-example-files/FLIP_WIDGET/` (structure reference)

**Behavior notes:** One small to small–medium skill per folder. If the skill is complex, instruct “use REQUIRED_SKILLS to list simpler skills and keep this skill as process/orchestration with singleness of purpose.”

---

## 5. Tracking system: compliance check

**Potential SKILL name:** TRACKING_SYSTEM_COMPLIANCE (or CHECK_PROJECT_DOCS_COMPLIANCE).

**Purpose:** Check that a set of project docs (schema, planning, progress, completed, after-action) complies with the tracking-system _docs. Report missing sections, wrong order, or non-conformant content.

**Inputs:** Path to project folder or list of doc paths (001–005 style). Optional: which _doc set (tracking-system 01–05).

**Outputs:** Compliance report (per-doc and cross-cutting), with fixes or suggestions.

**Key references:**
- `ai-docs/_docs-tracking-system-review.md` (review criteria)
- `projects/tracking-system/01-project-schemas/_project-schema.md` through `05-after-action/_after-action.md`
- `projects/example-project/000-sample-project-compliance.md` (example report)

**Behavior notes:** Re-use logic from the sample-project compliance review: required sections present, cross-refs correct, “What to do next” placement (003), naming consistency.

---

## 6. Skill standard sync (future)

**Potential SKILL name:** SKILL_STANDARD_SYNC (or CHECK_SKILL_STANDARD).

**Purpose:** Compare local skill-definition and skill-standard docs to the website’s canonical standard; report drift or suggest updates. Optional: one-way “adopt website standard” helper.

**Inputs:** Path to skill-standard doc(s); optional website URL or fetched spec.

**Outputs:** Diff or report: local vs website; suggested edits.

**Key references:**
- `my-skills/skill-definition/skill-standard/_skill-standard.md`
- Website (to be specified)

**Behavior notes:** Defer until website standard is stable and fetchable; note here so we don’t forget.

---

## How to use this file

- **When adding a new skill idea:** Add a row to `skills-to-make-first.md` and a section above with purpose, inputs, outputs, references, behavior notes.
- **When creating a SKILL.md:** Open this file and the relevant _docs; use the section as the spec for the skill’s instructions and scope.
- **Existing deep-dive notes:** SETUP_NEW_PROJECT and meta-agent template have their own process notes; this file points to them and adds my-skills and tracking-system so nothing is lost.

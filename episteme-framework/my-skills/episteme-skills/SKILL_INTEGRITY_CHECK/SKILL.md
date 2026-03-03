# SKILL_INTEGRITY_CHECK


## Name

skill-integrity-check


## Description

Recompute integrity hashes for skills and compare to stored values.


## When to use

- You need to detect tampering, meddling, or prompt injection in skill content.


## Instructions

1. Read the documents listed in **Read first** to understand the schema (Integrity hash field, algorithm).
2. **Scope:** Determine which skills to check (e.g. one skill folder, all under episteme-skills/, or a user-specified list). If unclear, ask.
3. **For each skill in scope:**
   - Read the skill’s SKILL.md (and optionally all files in the folder). Normalize for hashing: e.g. strip the “Integrity hash” line (and any “Last verified” line) so the stored hash is not part of the content being hashed; use a single canonical format (e.g. UTF-8, LF line endings).
   - Compute the integrity hash (e.g. SHA-256) of the normalized content. Algorithm should match what the skill-definition or standard specifies (e.g. SHA-256).
   - If the skill’s SKILL.md has an **Integrity hash** field with a value: compare computed hash to stored value. Report: **Match** or **Mismatch** (possible tampering or prompt injection; recommend review).
   - If the skill has no stored hash or it says “(To be filled…)”: report **No hash stored**; optionally offer to write the computed hash into the SKILL.md for future checks.
4. **Report:** Summarize per-skill result (match / mismatch / no hash). If any mismatch, recommend manual review before trusting the skill.
5. Summarize what you did and what to do next so the next agent can continue.


## Read first

- my-skills/skill-definition/_skill-definition.md
- my-skills/imported-skills/_imported-skills.md


## REQUIRED_SKILLS


(optional; none yet)


## Location

`my-skills/episteme-skills/SKILL_INTEGRITY_CHECK/`


## Original source URI

file:///Users/louisc/my-progs/episteme/my-skills/episteme-skills/SKILL_INTEGRITY_CHECK/SKILL.md


## Integrity hash

(To be filled once the skill is stable and hashed.)

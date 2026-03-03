# SKILL_STANDARD_SYNC


## Name

skill-standard-sync


## Description

Compare local skill-standard docs to the canonical website; report drift.


## When to use

- You need to know whether local skill standards have diverged from the canonical source.


## Instructions

1. Read the documents listed in **Read first** to understand the skill standard schema and where the canonical source lives (e.g. website URL if documented).
2. **Local baseline:** Read the local skill-standard doc(s) in this repo (e.g. `my-skills/skill-definition/skill-standard/_skill-standard.md` and any instance docs in that folder). Note structure, required sections, and key rules.
3. **Canonical source:** If a canonical website or URL for the skill standard is documented (in the _skill-standard, README, or project docs), fetch that content (e.g. via HTTP). If no URL is documented, report **Local only** — no remote to compare; list the local paths you read.
4. **Compare:** If canonical content was fetched: diff or compare structure and key rules (scope, folder design, structure design rules, location/layout). Report **In sync** or **Drift** with a short list of differences (e.g. “Local has extra paragraph under Structure design rules”; “Remote adds new required section X”).
5. **Report:** Summarize: in sync / drift / local only. If drift, suggest updating local _skill-standard or instance docs to match canonical (with user approval).
6. Summarize what you did and what to do next so the next agent can continue.


## Read first

- my-skills/skill-definition/skill-standard/_skill-standard.md


## REQUIRED_SKILLS


(optional; none yet)


## Location

`my-skills/episteme-skills/SKILL_STANDARD_SYNC/`


## Original source URI

file:///Users/louisc/my-progs/episteme/my-skills/episteme-skills/SKILL_STANDARD_SYNC/SKILL.md


## Integrity hash

(To be filled once the skill is stable and hashed.)

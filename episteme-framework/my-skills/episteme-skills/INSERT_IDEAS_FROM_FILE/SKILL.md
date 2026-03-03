# INSERT_IDEAS_FROM_FILE

## Name

insert-ideas-from-file

## Description

Read a file at a given path; treat each block (paragraphs separated by blank lines) as one idea; insert each into the Ideas System as Verbatim with a short agent interpretation. Target topic is chosen or created (MATCH_OR_CREATE_TOPIC); each block is appended via APPEND_VERBATIM_AND_INTERPRETATION.

## When to use

- User asks to import ideas from a file (e.g. a list, notes, or menu dump).
- /menu or Ideas flow offers “Insert from file” and the user supplies a path.

## Instructions

1. Read **Read first** to understand the idea-file schema and append behavior.
2. Obtain the **file path** (user-provided or from context). Resolve relative to project root or home as appropriate; confirm the file exists and is readable.
3. Obtain the **target topic** (existing or new). If not specified, use MATCH_OR_CREATE_TOPIC to let the user pick or create a topic (e.g. “imported-notes” or a name derived from the filename).
4. Read the file. Split content into **items** by blank lines (one or more consecutive newlines = separator). Trim each block; skip empty blocks.
5. For each non-empty block in order:
   - Use the block text as **Verbatim** (quote as-is in the schema).
   - Add a short **Agent** interpretation (e.g. “Imported from file; no additional interpretation.” or one sentence of implication).
   - Call APPEND_VERBATIM_AND_INTERPRETATION (or perform the append per _idea-file-schema): append to the chosen topic file with `---`, `## Entry N`, `**Verbatim:** "..."`, `**Agent:** ...`, and optional `id` / `created_at`.
6. Confirm how many ideas were added and to which topic file. Summarize for the next agent or user.

## Read first

- ideas-engine/_idea-file-schema.md
- my-skills/episteme-skills/APPEND_VERBATIM_AND_INTERPRETATION/SKILL.md
- my-skills/episteme-skills/MATCH_OR_CREATE_TOPIC/SKILL.md

## REQUIRED_SKILLS

| Skill name | Location |
|-----------|----------|
| MATCH_OR_CREATE_TOPIC | my-skills/episteme-skills/MATCH_OR_CREATE_TOPIC/ |
| APPEND_VERBATIM_AND_INTERPRETATION | my-skills/episteme-skills/APPEND_VERBATIM_AND_INTERPRETATION/ |

## Location

`my-skills/episteme-skills/INSERT_IDEAS_FROM_FILE/`

## Original source URI

file:///Users/louisc/my-progs/episteme/my-skills/episteme-skills/INSERT_IDEAS_FROM_FILE/SKILL.md

## Integrity hash

(To be filled once the skill is stable and hashed.)

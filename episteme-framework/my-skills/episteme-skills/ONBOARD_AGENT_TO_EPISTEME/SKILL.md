# ONBOARD_AGENT_TO_EPISTEME

## Name

onboard-agent-to-episteme

## Description

Orchestrate onboarding for a naive agent: run INTRO_TO_EPISTEME for system-level context, then ORIENT_TO_CURRENT_PROJECT (if applicable) for local project state and next steps.

## When to use

- A naive agent is starting work in this repository and needs orientation.
- The meta-agent or user explicitly requests onboarding to the episteme framework.

## Instructions

1. Read the documents listed in **Read first** to understand the episteme framework and current context.
2. When the trigger in **When to use** occurs, decide whether this skill applies; ask clarifying questions when necessary to reduce unnecessary work.
3. When appropriate, call the skills listed in **REQUIRED_SKILLS** (if any) to perform sub-steps.
4. Apply the conventions from the referenced _docs or notes when creating or updating files.
4. Summarize what you did and what to do next so the next agent can continue.

## Read first

- ai-docs/README.md
- ai-docs/episteme-system-capabilities-and-gaps.md
- my-skills/episteme-skills/SKILLS_TREE.md
- .episteme-project/files-to-remove-later/meta-agent.md
- episteme-framework/agent-docs/meta-agent.example.md

## REQUIRED_SKILLS

| Skill name | Location |
|-----------|----------|
| INTRO_TO_EPISTEME | my-skills/episteme-skills/INTRO_TO_EPISTEME/ |
| ORIENT_TO_CURRENT_PROJECT | my-skills/episteme-skills/ORIENT_TO_CURRENT_PROJECT/ |

## Location

`my-skills/episteme-skills/ONBOARD_AGENT_TO_EPISTEME/`

## Original source URI

file:///Users/louisc/my-progs/episteme/my-skills/episteme-skills/ONBOARD_AGENT_TO_EPISTEME/SKILL.md

## Integrity hash

(To be filled once the skill is stable and hashed.)

---
name: flip-widget
description: Flip a widget (state or view) in an abstract, context-agnostic way. Use when the user or task requires toggling, inverting, or flipping some discrete state or view—e.g. on/off, visible/hidden, A/B.
---

# FLIP_WIDGET (Example Skill)

Abstract, agnostic example skill. Use as a template for small, single-purpose skills.

---

## Name

flip-widget

---

## Description

Flip a widget: toggle, invert, or flip one discrete state or view (e.g. on/off, visible/hidden, option A vs B). The skill is context-agnostic—the “widget” can be a UI element, a config flag, a mode, or any binary or two-option state. The agent applies the flip according to the current context (codebase, UI, config, etc.).

---

## When to use

- User asks to “flip,” “toggle,” “switch,” or “invert” something (e.g. a setting, a view, a state).
- Task requires changing one of two states or views and the codebase (or spec) uses “widget” or an equivalent concept.
- You need a minimal example of a small, single-purpose skill for structure reference.

---

## Instructions

1. **Identify the widget** in context: what thing (state, view, flag, mode) is to be flipped? Ask the user if ambiguous.
2. **Determine current state** (e.g. on/off, A/B) from code, config, or UI.
3. **Apply the flip**: make the change that moves to the other state (edit file, toggle UI, swap value). Prefer the minimal change that achieves the flip.
4. **Confirm** the new state (e.g. one-line summary or “Flipped X from … to …”).

Keep the change small and single-purpose. If the “widget” is part of a larger flow, consider whether another skill (or a constellation of skills) should own that flow; this skill stays focused on the flip.

---

## Read first

(Optional. None for this example.)

---

## REQUIRED_SKILLS

(Optional. None for this minimal example.)

---

## Location

`my-skills/skill-definition/skill-example-files/FLIP_WIDGET/` (example only; not a live skill).

---

## Original source URI

(Example: `file:///path/to/episteme/my-skills/skill-definition/skill-example-files/FLIP_WIDGET` or repo URL. Required for imported; recommended for all skills for provenance.)

---

## Integrity hash

(Example: `SHA-256` + hash of SKILL.md or normalized folder content. Verify before use to detect tampering, meddling, or prompt injection.)

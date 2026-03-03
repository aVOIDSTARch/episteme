# PROGRESS: widget-control-program

## Project
widget-control-program

## Planning doc
`example-project/002-sample-project-planning-doc.md`

## Schema doc
`example-project/001-sample-project-schema.md`

## Stages completed
- Phase 1: Scaffold & types — done
- Phase 2: Core control logic — done
- Phase 3: CLI & I/O — done

## What to do next
Start Phase 4: Tests & polish. First step: add integration test with golden file for `wcp-cli -i fixtures/sample.json --tick 3`, then run `cargo clippy -- -D warnings` and fix any lints. Update README with “Design language compliance” subsection pointing to `docs/WIDGET_DESIGN_LANGUAGE.md`.

## Commits by stage
- Phase 1: 2025-02-14 10:23 — feat: scaffold crate, add WidgetState and WcpEvent enums
- Phase 2: 2025-02-14 14:41 — feat(lib): state machine and transition logic with unit tests
- Phase 3: 2025-02-15 09:17 — feat(cli): clap args, stream parsing, JSON event output

## Test names by stage
- Phase 1: [ ]
- Phase 2: [ `test_transition_idle_to_calibrating`, `test_transition_calibrating_to_active`, `test_transition_active_to_fault`, `test_emit_tick_event`, `test_serialization_roundtrip` ]
- Phase 3: [ `test_cli_stdin_to_stdout`, `test_cli_file_input`, `test_invalid_descriptor_exits_nonzero` ]

## Test run results by stage
- Phase 1: (no tests yet)
- Phase 2: 5 passed
- Phase 3: 3 passed

## Decisions / rationales
- Decision: Use `serde_json` for both descriptor input and event output. Rationale: WIDGET_SPEC says “JSON on the wire”; keeps one dependency and matches the (fake) design doc.
- Decision: Binary name `wcp-cli` instead of `widget-control-program`. Rationale: Shorter for scripts; project name stays widget-control-program for the crate.
- Decision: State machine lives in `src/lib.rs` with no I/O. Rationale: Pure logic is testable and fuzzable; CLI is a thin wrapper (recommendation from planning addenda).

## Session / date
2025-02-15

## Blockers / open items
None. Ready for Phase 4.

## Context not elsewhere
The imaginary `docs/WIDGET_SPEC.md` is referenced in code comments; when we run “design language compliance” in Phase 4, we’ll add a short README section that says we follow it (even though the doc doesn’t exist—it’s the thought that counts).

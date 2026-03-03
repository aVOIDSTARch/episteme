# PROJECT: widget-control-program

## Project
widget-control-program

## Summary
A Rust CLI that talks to the Widget Control Protocol (WCP): parse widget descriptors, drive state machines, and emit events. “The little program that could (and did, with zero unsafe).”

## Owner
personal

## Type
app

## Stack
Rust 1.75+, cargo, serde, clap, tokio (async runtime for future WCP-over-the-wire)

## Created
2025-02-14

## Deployment
**Confirmed:** CLI
**Possible:** Web Application (future WCP dashboard)

## Dev environment
macOS, Cursor, rustup 1.76, cargo-nextest

## Agents / models
Cursor, Claude Opus

## Project state
Greenfield

## Read first
`docs/WIDGET_DESIGN_LANGUAGE.md`, `docs/WIDGET_SPEC.md` (both imaginary; see project vocabulary)

## Entry points
`src/main.rs`, `src/lib.rs`

## Project-specific enums
**WidgetState:** Idle | Calibrating | Active | Fault | Unknown  
**WcpEvent:** Attach | Detach | Tick | Halt

## Project vocabulary
**widget** = a logical unit in the WCP spec; has a state machine and emits events.  
**WCP** = Widget Control Protocol; the (fake) wire format we implement.  
**twiddle** = internal term for “apply one state transition”; don’t use in user-facing docs.  
**ship** = publish a release (e.g. `cargo publish` or tag).

## REQUIRED_SKILLS
| Skill name | Location |
|------------|----------|
| SETUP_NEW_PROJECT | (path or URL to SKILL.md) |
| RUST_CLIPPY_LINT | ~/.cursor/skills/rust-clippy-lint/SKILL.md |
| WIDGET_SIMULATOR_SKILL | episteme/skills/widget-simulator/SKILL.md |

## Schema version
1

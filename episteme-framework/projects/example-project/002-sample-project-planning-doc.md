# PLAN: widget-control-program

## Project
widget-control-program

## Plan summary
Build a minimal Rust CLI that implements the (imaginary) Widget Control Protocol: parse widget descriptors from stdin or a file, run a tiny state machine per widget, and output WCP events. No network yet—just enough to prove the design language and pass a first battery of tests. “Parse, twiddle, emit.”

## Out of scope
- Real hardware or device drivers; we’re simulating with in-memory state.
- WCP-over-the-wire, TLS, or async I/O in v1 (stub only).
- GUI or TUI; CLI only.
- Formal verification (maybe later in a “Widget Control Program, Q.E.D.” follow-up).

## Phased plan

### Phase 1: Scaffold & types
- Goal: Crate layout, `WidgetState` and `WcpEvent` enums, and a no-op binary that exits 0.
- Deliverables / steps: `cargo init` (lib + bin), add serde + clap to Cargo.toml, define enums in `src/lib.rs` with `#[derive(Serialize, Deserialize)]`, `main` reads one arg (path or `-` for stdin) and exits. Reference `docs/WIDGET_SPEC.md` for enum values.

### Phase 2: Core control logic
- Goal: One widget state machine: parse a single widget descriptor (e.g. JSON or our minimal DSL), apply transitions on “tick” events, emit WCP events.
- Deliverables / steps: `Widget` struct, `transition(state, event) -> (new_state, Option<WcpEvent>)`, unit tests for all state transitions. No I/O yet—logic only.

### Phase 3: CLI & I/O
- Goal: End-to-end: read descriptor(s) from file or stdin, run state machine(s), write events to stdout (one JSON line per event).
- Deliverables / steps: clap for `-i`/`--input` and `--tick`, stream parsing, integration test with a golden file.

### Phase 4: Tests & polish
- Goal: Test matrix green, clippy clean, README and a “Design language compliance” note.
- Deliverables / steps: Expand tests (roundtrip, invalid input handling), run `cargo clippy -- -D warnings`, document in README how this aligns with `docs/WIDGET_DESIGN_LANGUAGE.md`.

## Dependencies
- `docs/WIDGET_SPEC.md` (authoritative enum and message shapes; imaginary).
- `docs/WIDGET_DESIGN_LANGUAGE.md` (design language for state-machine and naming; imaginary).
- Rust 1.75+ and std only for now (no tokio in v1).

## Success criteria
- `cargo build --release` succeeds; `cargo test` and `cargo clippy` pass.
- One widget descriptor in → one state machine → events out to stdout.
- README explains how to run the binary and points to the (fake) design docs.

---

## Addenda

### Open questions
- Do we want a `--dry-run` that only parses and validates descriptors without emitting?
- Naming: `widget-control-program` vs `wcp-cli` for the binary?

### Recommendations
- Keep Phase 2 pure (no I/O) so we can fuzz the state machine later with a CARGO_FUZZ_SKILL.
- Add a “Design language compliance” subsection to README so future agents know we’re following WIDGET_DESIGN_LANGUAGE.

### Concerns
- The spec doc is fictional; if we ever plug in a real WCP, we’ll need a migration note for any divergence (e.g. new states).

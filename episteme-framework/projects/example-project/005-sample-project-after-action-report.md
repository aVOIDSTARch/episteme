# AFTER-ACTION: widget-control-program

## Project
widget-control-program

## Completed report
`example-project/004-sample-project-completed.md`

## Project improvements
- Add a `CHANGELOG.md` (keep a hip, one-line-per-version style) so the next contributor knows what shipped.
- Document the “golden file = sorted keys” convention in the main README, not just in the test module.
- Consider `cargo dist` or a minimal release workflow so v0.2.0 can be “one command to tag and build artifacts.”

## Related projects to start
- **wcp-dashboard**: A tiny web UI that consumes the same JSON event stream (e.g. over stdin or a socket). “Widget Control Program, now with blinky lights.”
- **widget-control-program-qed**: Formal model of the state machine (e.g. TLA+ or a Rust model check) to prove we never reach Fault from Idle in one step. The compsci book sequel.
- **wcp-fuzz**: Fuzz the transition logic using the existing CARGO_FUZZ_SKILL; no new product, just a fuzz target in this repo or a sibling.

## New SKILLs to develop
- **CARGO_FUZZ_SKILL**: One-pager for “add a fuzz target for this crate’s core logic”; references cargo-fuzz and our pattern (lib-only, no I/O). Feeds the “fuzz the state machine” recommendation from the completed report.
- **RUST_README_COMPLIANCE**: Skill that checks README has “how to build, test, run” and optionally “design language / spec compliance” section. Would have caught the “put compliance in README” item earlier.

## Other ideas
- A “Widget Control Program: The Comic” zine that explains the state machine with stick figures. (We’re only half kidding.)
- If WIDGET_SPEC ever becomes real, add a CI job that diffs our enums against the spec repo’s schema and fails if we drift.

## Priorities
1. CHANGELOG and README golden-file note (low effort, high clarity).
2. CARGO_FUZZ_SKILL (unblocks wcp-fuzz and future Rust projects).
3. wcp-dashboard or wcp-fuzz as the next fun side project.

# ClankerKit Skills Index

## How to use this index

Each entry answers in plain English: what this skill helps an agent do.

## Governance

- `truthforge`
Why it helps: Stops fake confidence by requiring runtime-relevant proof and explicit risk classification.
- `truth-recovery-program`
Why it helps: Runs one parent program to audit merged truth, intent drift, and queue quality.
- `orchestrator-hardening`
Why it helps: Hardens session orchestration so lane routing and escalation are deterministic.
- `skill-intake-gate`
Why it helps: Screens contributed skills for safety, determinism, and quality before merge.
- `deterministic-gate`
Why it helps: Enforces merge and release decisions against explicit gate criteria.
- `evidence-contract`
Why it helps: Forces claims to include structured evidence and proof boundaries.
- `escalation-and-blockers`
Why it helps: Standardizes when to continue, escalate, pause, or block.

## Validation

- `runtime-proof`
Why it helps: Tests whether runtime-visible claims are proven outside synthetic harnesses.
- `completion-claim-audit`
Why it helps: Verifies that "done" claims match real implementation and evidence.
- `test-surface-skeptic`
Why it helps: Audits test coverage quality and detects synthetic masking patterns.
- `evidence-research-flywheel`
Why it helps: Turns research inputs into confidence-scored, executable outputs.

## Repo Understanding

- `map-the-system`
Why it helps: Builds a practical map of entrypoints, dependencies, and risky boundaries.
- `find-the-real-entrypoints`
Why it helps: Locates runtime entrypoints that matter, not just test or scaffold paths.
- `blast-radius-scan`
Why it helps: Estimates change impact before broad edits land.

## Debugging

- `trace-the-failure`
Why it helps: Reproduces and traces failures across real execution boundaries.

## Delivery

- `definition-of-done-check`
Why it helps: Confirms that delivery artifacts and evidence meet done criteria.
- `safe-pr-prep`
Why it helps: Prepares PRs with high-signal summaries, risks, and validation receipts.
- `deterministic-execution-lane`
Why it helps: Runs long tasks with resumable checkpoints and explicit stop reasons.
- `merge-train-governor`
Why it helps: Governs lane selection, gating, and promotion decisions.

## Hardening

- `production-readiness-pass`
Why it helps: Audits resilience, observability, rollback, and operational readiness.

## Documentation

- `operator-handoff`
Why it helps: Produces clear runbooks and handoff artifacts for humans operating the system.

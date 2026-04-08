---
name: "deterministic-execution-lane"
category: "delivery"
description: "Execution super skill for resumable, fail-closed, checkpoint-driven implementation lanes that continue until done or a concrete blocker."
status: "provisional"
recommended-modes:
  - implementation
  - remediation
  - long-running-lane
allowed-tools:
  - git
  - rg
  - python
  - pytest
  - repo-tools
tags:
  - delivery
  - checkpoints
  - resumable
  - fail-closed
---

# Deterministic Execution Lane

**Tagline:** Keep shipping with checkpoints, not memory.

## Purpose

Execute multi-phase work deterministically with resumable checkpoints and strict stop reasons.

## Use when

1. work spans multiple phases or sessions
2. interruptions are likely
3. evidence must be durable and replayable
4. you need safe continuation until done or blocked

## Do not use when

Do not use for one-shot edits that do not require persistent execution state.

## Inputs

- objective and acceptance criteria
- constraints and safety rules
- ordered phase list
- command or validator set for each phase
- artifact root path

## Outputs

- run state file
- per-phase checkpoints
- artifact ledger
- explicit stop reason
- done or blocked verdict

## Core contract

1. define phase contract before execution
2. write checkpoint at every phase boundary
3. fail closed on missing required artifacts
4. resume from next incomplete valid phase
5. stop only on completion or explicit blocker

## Stop reasons

- `done`
- `queue_empty`
- `blocked_missing_spec`
- `blocked_needs_approval`
- `blocked_validation_failure`
- `blocked_missing_artifact`
- `blocked_safety_risk`

## Procedure

### Phase 1: initialize lane

1. define objective and done conditions
2. define dependency-ordered phases
3. persist initial state

### Phase 2: execute

1. run next unblocked phase
2. persist material artifacts
3. emit phase checkpoint with status and evidence paths

### Phase 3: verify and gate

1. run required validators
2. fail closed on required check failure
3. record pass/fail in checkpoint

### Phase 4: resume or conclude

1. on interruption, load state and continue
2. on completion, emit terminal summary
3. on blocker, emit concrete blocker contract

## Proof requirements

- each successful phase must have material evidence artifacts
- evidence paths must resolve at checkpoint time
- completion requires validator pass state when validators are required

## Common failure patterns

1. marking phases done without durable artifacts
2. skipping failed phases without rationale and ownership
3. using chat logs as execution state
4. rerunning full workflows when only one phase failed

## Adaptation notes

- frontend repos: include screenshot or UI smoke artifact checkpoints
- backend repos: include route or job runtime artifacts
- data repos: include query, migration, and validation artifacts
- restricted toolchains: lower automation scope, keep contract identical

## Handoff format

```text
Deterministic Execution Lane Report

Lane objective:
Acceptance criteria:
Phase plan:

Checkpoint ledger:
Validator results:
Artifacts:

Current status:
Stop reason:
Next action:
```

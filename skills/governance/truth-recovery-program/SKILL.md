---
name: "truth-recovery-program"
category: "governance"
description: "Repo-wide governance super skill that runs merged-truth, intent-drift, and queue-rebaseline audits under one parent program with deterministic classifications and finding dispositions."
status: "provisional"
recommended-modes:
  - repo-truth-recovery
  - incident
  - governance-reset
allowed-tools:
  - git
  - rg
  - python
  - pytest
  - playwright
  - repo-tools
tags:
  - governance
  - truth-recovery
  - evidence
  - queue-rebaseline
---

# Truth Recovery Program

**Tagline:** One parent program that recovers truth across code, intent, and queue.

## Purpose

Run a repository-wide truth recovery pass as a governed program, not scattered one-off audits.

## Use when

1. Runtime trust is low even when CI is green.
2. Merged code quality and project direction are unclear.
3. Open queue artifacts no longer match current strategy.
4. You need one parent artifact that can drive real remediation work.

## Do not use when

Do not use for tiny isolated fixes where local scope is obvious and governance reset is unnecessary.

## Inputs

- target repo and audit window
- architecture intent sources (docs, roadmaps, prior plans)
- merged history scope (time window or PR range)
- queue source (issues, tickets, tasks, or workpackets)
- available environments and runtime constraints

## Outputs

- one parent truth-recovery report
- three required audit sections
- merged-code classifications
- queue classifications
- per-finding disposition state
- fix-now lane and deferred lane outputs

## Required audits

1. `Merged Code Truth Audit`
2. `Intent Drift Audit`
3. `Open Queue Rebaseline`

## Merged-code classifications

- `SAFE`
- `PARTIAL`
- `FALSE_CONFIDENCE_RISK`
- `BROKEN_IN_RUNTIME_RISK`

## Queue classifications

- `KEEP`
- `RESCOPE`
- `SUPERSEDED`
- `RETIRE`
- `SPLIT`

## Finding dispositions

- `fixed_now`
- `child_wp`
- `superseded_closed`
- `rescoped_new_wp`
- `audited_safe_no_action`

## Procedure

### Phase 1: Program setup

1. Create one parent artifact.
2. Normalize tracker nouns into one queue model.
3. Define bounded domain profile for this repo.

### Phase 2: Run the three audits

1. audit merged behavior versus evidence quality
2. audit inception intent versus current optimization
3. audit open queue alignment and actionability

### Phase 3: Classify and dispose

1. classify every finding
2. assign one disposition state per finding
3. route each finding to fix-now or deferred lane

### Phase 4: Publish remediation contract

1. list completed remediations
2. list child artifacts with owner and links
3. publish explicit not-ready conditions if present

## Proof requirements

- runtime-visible claims need runtime-relevant evidence
- boundary-sensitive claims need failure-mode evidence
- missing proof must degrade confidence explicitly

## Common failure patterns

1. treating green tests as proof while critical dependencies are mocked
2. accepting queue items with stale or false problem statements
3. keeping superseded work alive without explicit closure
4. mixing findings across audits so ownership disappears

## Adaptation notes

- frontend-only repos: emphasize browser runtime proof and API contract drift
- backend repos: emphasize route, job, worker, and startup path evidence
- monorepos: partition domains by package boundaries before scoring
- restricted environments: downgrade confidence and record missing proof

## Handoff format

```text
Truth Recovery Program Report

Parent artifact:
Domain profile:
Audit window:

Merged Code Truth Audit:
Intent Drift Audit:
Open Queue Rebaseline:

Merged-code classifications:
Queue classifications:
Finding dispositions:

Fixed now:
Deferred child work:
Superseded or closed:
Rescoped artifacts:
Audited-safe findings:

Program verdict:
- READY
- READY WITH EXPLICIT RISK
- NOT READY
```

---
name: "trace-the-failure"
category: "debugging"
description: "Debugging skill for deterministic reproduction and boundary-by-boundary tracing of failures until root cause or concrete blocker is identified."
status: "provisional"
recommended-modes:
  - incident
  - bug-hunt
  - regression-triage
allowed-tools:
  - git
  - rg
  - python
  - pytest
  - playwright
  - repo-tools
tags:
  - debugging
  - failure-tracing
  - reproduction
  - root-cause
---

# TraceTheFailure

**Tagline:** Reproduce first, then trace where reality breaks.

## Purpose

TraceTheFailure isolates failures with deterministic reproduction, evidence capture, and boundary-level tracing.

## Use when

1. a bug is reported but root cause is unclear
2. CI and local behavior diverge
3. errors cross multiple boundaries (UI, API, service, filesystem, subprocess)

## Do not use when

Do not invoke for trivial syntax or lint errors with obvious single-file fixes.

## Inputs

- observed failure behavior
- expected behavior
- branch, diff, or release context
- reproduction environment details
- available logs or traces

## Outputs

- deterministic reproduction steps
- failing path trace by boundary
- root cause hypothesis ranking
- confirmed cause or blocked reason
- remediation recommendation

## Procedure

### Phase 1: reproduce

1. define expected and observed behavior
2. create deterministic reproduction steps
3. capture baseline artifacts

### Phase 2: trace boundaries

1. trace user-facing boundary
2. trace internal service boundaries
3. trace host dependencies and environment assumptions

### Phase 3: isolate cause

1. narrow suspect set
2. verify with targeted checks
3. eliminate non-causes with evidence

### Phase 4: conclude

1. return confirmed cause or concrete blocker
2. define smallest safe remediation
3. list tests or checks that prevent recurrence

## Proof requirements

- reproduction must be repeatable
- each boundary claim must include artifact evidence
- root cause claims must include elimination evidence

## Common failure patterns

1. jumping to fixes before reproduction is stable
2. relying on one log line without path trace
3. blaming environment without assumption validation
4. closing incident with hypothesis only

## Adaptation notes

- frontend repos: emphasize browser and network path traces
- backend repos: emphasize route and service call traces
- monorepos: isolate package boundary before deep tracing

## Handoff format

```text
TraceTheFailure Report

Observed behavior:
Expected behavior:
Reproduction steps:

Boundary trace:
Confirmed evidence:
Eliminated hypotheses:

Root cause status:
- CONFIRMED
- LIKELY
- BLOCKED

Remediation recommendation:
Preventive checks:
```

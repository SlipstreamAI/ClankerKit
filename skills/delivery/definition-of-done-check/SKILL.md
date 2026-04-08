---
name: "definition-of-done-check"
category: "delivery"
description: "Delivery skill for validating that implementation, evidence, docs, and operational handoff meet explicit definition-of-done criteria."
status: "provisional"
recommended-modes:
  - pre-merge
  - release-readiness
allowed-tools:
  - git
  - rg
  - python
  - pytest
  - repo-tools
tags:
  - delivery
  - done-criteria
  - readiness
---

# DefinitionOfDoneCheck

**Tagline:** Done means criteria met, not effort spent.

## Purpose

DefinitionOfDoneCheck verifies that all required completion criteria are satisfied before merge or release.

## Use when

1. a change is proposed as complete
2. handoff quality matters for operators
3. release criteria need deterministic confirmation

## Do not use when

Do not invoke for draft work that has not reached candidate completion.

## Inputs

- explicit done criteria
- diff or PR
- validation outputs
- docs and handoff artifacts

## Outputs

- criteria pass/fail matrix
- missing completion elements
- readiness verdict

## Procedure

### Phase 1: map criteria

1. list required done criteria
2. map each criterion to verification method

### Phase 2: verify

1. verify code implementation criteria
2. verify validation criteria
3. verify documentation and handoff criteria

### Phase 3: decide

1. classify completion status
2. list required remaining work

## Proof requirements

- each criterion must map to concrete evidence
- failed criteria must include remediation action
- readiness verdict must align with pass/fail matrix

## Common failure patterns

1. tests pass but docs and handoff missing
2. done criteria not explicit before verification
3. required runtime checks skipped

## Adaptation notes

- product repos: include rollout and rollback criteria
- platform repos: include operational and observability criteria

## Handoff format

```text
DefinitionOfDoneCheck Report

Done criteria:
Verification matrix:
Missing elements:

Verdict:
- READY
- READY WITH EXPLICIT RISK
- NOT READY

Required remaining work:
```

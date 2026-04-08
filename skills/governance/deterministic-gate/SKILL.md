---
name: "deterministic-gate"
category: "governance"
description: "Governance skill for defining and enforcing explicit gate criteria for merge, release, or promotion decisions."
status: "provisional"
recommended-modes:
  - pre-merge
  - release-readiness
allowed-tools:
  - git
  - rg
  - python
  - repo-tools
tags:
  - governance
  - gates
  - determinism
  - readiness
---

# DeterministicGate

**Tagline:** No merge by mood.

## Purpose

DeterministicGate replaces ambiguous readiness decisions with explicit, testable gate criteria.

## Use when

1. merge or release decisions are inconsistent
2. high-risk changes need explicit proof thresholds
3. reviewers need a shared readiness contract

## Do not use when

Do not invoke for exploratory branches with no merge or release intent.

## Inputs

- target change scope
- claim type and risk profile
- required validations and evidence classes
- local policy constraints

## Outputs

- gate definition table
- pass/fail result per gate
- block reasons
- required actions to pass

## Procedure

### Phase 1: define gates

1. define gates by risk and claim type
2. map required evidence per gate

### Phase 2: execute gates

1. gather validation results
2. evaluate criteria deterministically

### Phase 3: decide

1. emit readiness verdict
2. list blocking criteria and actions

## Proof requirements

- gate criteria must be explicit and measurable
- high-risk claims require runtime-relevant evidence
- failures must produce actionable block output

## Common failure patterns

1. gate language too vague to enforce
2. pass status inferred from incomplete evidence
3. risk level not reflected in gate strength

## Adaptation notes

- teams can tune thresholds, but not remove explicit criteria
- keep criteria stable within a release cycle for comparability

## Handoff format

```text
DeterministicGate Report

Gate table:
Gate results:
Blocking criteria:
Required actions:

Verdict:
- READY
- READY WITH EXPLICIT RISK
- NOT READY
```

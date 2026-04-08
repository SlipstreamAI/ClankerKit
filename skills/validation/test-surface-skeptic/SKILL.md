---
name: "test-surface-skeptic"
category: "validation"
description: "Validation skill for assessing whether test coverage proves meaningful behavior across real risk surfaces or only synthetic wiring."
status: "provisional"
recommended-modes:
  - pr-audit
  - test-audit
allowed-tools:
  - git
  - rg
  - python
  - pytest
  - repo-tools
tags:
  - validation
  - tests
  - skepticism
  - coverage-quality
---

# TestSurfaceSkeptic

**Tagline:** Coverage count is not behavior proof.

## Purpose

TestSurfaceSkeptic evaluates test surface quality and identifies where synthetic coverage masks runtime risk.

## Use when

1. test coverage is high but runtime confidence is low
2. critical dependencies are heavily mocked
3. regressions escape despite green checks

## Do not use when

Do not invoke for pure logic modules with no external boundaries unless risk indicators exist.

## Inputs

- changed files and tests
- test execution results
- dependency and boundary map
- risk profile for touched surfaces

## Outputs

- test-surface map
- synthetic masking findings
- missing failure-mode coverage
- coverage quality classification

## Procedure

### Phase 1: map surfaces

1. list touched boundaries
2. map tests to boundaries
3. identify untested or indirectly tested boundaries

### Phase 2: inspect masking

1. locate heavy mocks and stubs
2. check whether risk dependencies are bypassed
3. note assertions that validate shape not behavior

### Phase 3: classify and remediate

1. classify each boundary as `proven`, `partial`, or `synthetic-heavy`
2. define required real-path and failure-mode additions

## Proof requirements

- risky boundaries require at least one non-synthetic proof path
- failure-mode coverage must exist for high-risk dependencies
- test claims must map to behavior, not only structure

## Common failure patterns

1. endpoint tests replace full service path
2. happy-path-only assertions
3. missing env or dependency failure tests
4. test doubles hiding integration defects

## Adaptation notes

- frontend repos: include data-load and error-state assertions
- backend repos: include real handler-to-service path checks
- infra repos: include startup and config failure-mode tests

## Handoff format

```text
TestSurfaceSkeptic Report

Touched boundaries:
Test-surface map:
Synthetic masking:
Failure-mode gaps:

Boundary classifications:
- proven
- partial
- synthetic-heavy

Required test additions:
Coverage-quality verdict:
```

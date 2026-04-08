---
name: "completion-claim-audit"
category: "validation"
description: "Validation skill for auditing completion claims against actual code changes, runtime behavior, and delivery artifacts."
status: "provisional"
recommended-modes:
  - pr-audit
  - release-audit
allowed-tools:
  - git
  - rg
  - python
  - pytest
  - repo-tools
tags:
  - validation
  - done-claims
  - audit
  - evidence
---

# CompletionClaimAudit

**Tagline:** Verify that "done" means done in reality, not in narration.

## Purpose

CompletionClaimAudit checks whether completion language matches implementation, tests, runtime proof, and required handoff artifacts.

## Use when

1. a PR or issue says work is complete
2. release readiness depends on multiple claims
3. historical over-claiming has reduced trust

## Do not use when

Do not invoke for WIP commits or exploratory branches that do not claim completion.

## Inputs

- completion claim text
- changed files or PR diff
- validation outputs
- runtime proof artifacts where applicable
- expected done criteria

## Outputs

- claim-to-evidence matrix
- missing done criteria
- confidence classification
- required remediation actions

## Procedure

### Phase 1: parse claims

1. extract explicit completion statements
2. map each statement to expected evidence

### Phase 2: verify evidence

1. verify code-level implementation evidence
2. verify validation and proof artifacts
3. verify docs and handoff requirements

### Phase 3: classify

1. mark each claim as `substantiated`, `partial`, or `unsupported`
2. summarize overall completion confidence

## Proof requirements

- every completion claim maps to a concrete evidence artifact
- runtime-visible claims include runtime-relevant evidence
- unsupported claims are explicitly listed

## Common failure patterns

1. completion claims tied only to green CI
2. feature claim without runtime proof
3. docs and handoff omitted from done criteria
4. partial implementation narrated as complete

## Adaptation notes

- docs-heavy repos: weight artifact completeness
- runtime-heavy repos: weight runtime proof classes
- monorepos: verify claim impact by package

## Handoff format

```text
CompletionClaimAudit Report

Completion claims:
Claim-to-evidence matrix:
Missing criteria:

Claim status:
- substantiated
- partial
- unsupported

Overall classification:
- READY
- READY WITH EXPLICIT RISK
- NOT READY

Required remediation:
```

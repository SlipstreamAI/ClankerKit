---
name: "safe-pr-prep"
category: "delivery"
description: "Delivery skill for preparing high-signal pull requests with explicit risk framing, proof receipts, and reviewer-ready context."
status: "provisional"
recommended-modes:
  - pre-merge
  - pr-prep
allowed-tools:
  - git
  - rg
  - python
  - pytest
  - repo-tools
tags:
  - delivery
  - pull-request
  - reviewer-experience
---

# SafePRPrep

**Tagline:** Make reviews faster by making risk and proof obvious.

## Purpose

SafePRPrep assembles a reviewer-ready PR package with clear scope, risk summary, validation receipts, and explicit open assumptions.

## Use when

1. preparing a PR for human review
2. change risk is non-trivial
3. review throughput is slowed by missing context

## Do not use when

Do not invoke for throwaway branches that are not intended for review.

## Inputs

- branch diff
- functional claim
- validation artifacts
- risk and impact notes

## Outputs

- PR summary draft
- risk table
- validation receipt list
- open assumptions list
- reviewer checklist

## Procedure

### Phase 1: summarize scope

1. summarize what changed
2. summarize why it changed
3. bound what is out of scope

### Phase 2: attach proof

1. attach tests and runtime checks
2. classify evidence strength
3. list failure-mode coverage

### Phase 3: frame review

1. list key reviewer focus points
2. list open assumptions and known limits
3. provide merge readiness recommendation

## Proof requirements

- all validation claims include artifact paths or command outputs
- runtime-visible claims include runtime-relevant evidence
- limitations are explicit

## Common failure patterns

1. narrative summaries with no receipts
2. no risk framing for high-impact changes
3. hidden assumptions that surprise reviewers

## Adaptation notes

- strict repos: include gate IDs and required reviewer roles
- fast repos: keep summary short, receipts precise

## Handoff format

```text
SafePRPrep Report

Scope summary:
Out-of-scope:
Risk table:
Validation receipts:
Failure-mode coverage:
Open assumptions:
Reviewer focus checklist:

Recommendation:
- READY
- READY WITH EXPLICIT RISK
- NOT READY
```

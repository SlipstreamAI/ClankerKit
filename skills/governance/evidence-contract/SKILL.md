---
name: "evidence-contract"
category: "governance"
description: "Governance skill for defining a minimum evidence contract that all claims, audits, and readiness decisions must satisfy."
status: "provisional"
recommended-modes:
  - governance-reset
  - pr-audit
allowed-tools:
  - git
  - rg
  - python
  - repo-tools
tags:
  - governance
  - evidence
  - contracts
---

# EvidenceContract

**Tagline:** Claims require explicit evidence contracts.

## Purpose

EvidenceContract standardizes what evidence must exist before claims can be treated as credible.

## Use when

1. teams disagree on what counts as proof
2. readiness decisions vary by reviewer
3. reports lack consistent evidence structure

## Do not use when

Do not invoke if a strong evidence contract is already in place and stable.

## Inputs

- claim types in scope
- risk model
- available environments
- validation capabilities

## Outputs

- evidence class policy
- claim-to-proof requirement matrix
- missing-evidence policy
- confidence downgrade rules

## Procedure

### Phase 1: define claim types

1. internal-only
2. runtime-visible
3. boundary-sensitive
4. security-sensitive

### Phase 2: map required proof

1. define minimum evidence classes per claim type
2. define required failure-mode coverage where needed

### Phase 3: define downgrade policy

1. define confidence downgrade when evidence is missing
2. define block thresholds for high-risk claims

## Proof requirements

- every claim type has explicit minimum proof class
- missing evidence triggers deterministic downgrade behavior
- high-risk claims cannot pass on synthetic-only evidence

## Common failure patterns

1. one proof standard for all claim types
2. no downgrade rules for missing evidence
3. evidence lists without class semantics

## Adaptation notes

- allow local evidence sources, keep contract semantics stable
- preserve class names across repos for report comparability

## Handoff format

```text
EvidenceContract Report

Claim types:
Evidence classes:
Requirement matrix:
Downgrade policy:
Block thresholds:
Adoption recommendations:
```

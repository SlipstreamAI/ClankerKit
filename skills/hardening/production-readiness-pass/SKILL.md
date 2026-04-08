---
name: "production-readiness-pass"
category: "hardening"
description: "Hardening skill for auditing operational readiness across resilience, observability, rollback, and runtime assumption integrity."
status: "provisional"
recommended-modes:
  - release-readiness
  - hardening-pass
allowed-tools:
  - git
  - rg
  - python
  - pytest
  - repo-tools
tags:
  - hardening
  - production-readiness
  - resilience
---

# ProductionReadinessPass

**Tagline:** Confirm operational readiness before production confirms it for you.

## Purpose

ProductionReadinessPass audits whether a change is operationally ready under real runtime conditions.

## Use when

1. preparing production or high-stakes release
2. runtime assumptions changed
3. resilience and rollback confidence is uncertain

## Do not use when

Do not invoke for local-only prototypes with no deployment intent.

## Inputs

- target release scope
- deployment and runtime constraints
- monitoring and alerting context
- rollback strategy

## Outputs

- readiness checklist result
- resilience and failure-mode coverage summary
- observability gap list
- rollback confidence status

## Procedure

### Phase 1: runtime assumptions

1. verify env and dependency assumptions
2. verify startup and deployment path assumptions

### Phase 2: resilience checks

1. verify degraded-path behavior
2. verify critical dependency failure handling

### Phase 3: observability and rollback

1. verify logging and signal coverage for new risk areas
2. verify rollback path clarity and trigger conditions

## Proof requirements

- high-risk assumptions must be explicitly validated or marked unresolved
- failure-mode evidence must exist for critical dependencies
- rollback path must include trigger and owner

## Common failure patterns

1. happy-path validation only
2. no rollback ownership
3. insufficient observability for new risk surfaces

## Adaptation notes

- SaaS repos: include incident response integration
- internal tools: include operator ownership clarity even without full SRE stack

## Handoff format

```text
ProductionReadinessPass Report

Scope:
Runtime assumptions:
Resilience coverage:
Observability gaps:
Rollback readiness:

Verdict:
- READY
- READY WITH EXPLICIT RISK
- NOT READY

Required hardening actions:
```

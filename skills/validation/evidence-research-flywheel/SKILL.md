---
name: "evidence-research-flywheel"
category: "validation"
description: "Validation skill for evidence-first research, claim scoring, and bounded planning handoff without losing source traceability."
status: "provisional"
recommended-modes:
  - research
  - planning
  - strategy-refresh
allowed-tools:
  - git
  - rg
  - python
  - browser
  - repo-tools
tags:
  - research
  - evidence
  - planning
  - traceability
---

# Evidence Research Flywheel

**Tagline:** Research that can be audited and executed.

## Purpose

Convert source material into evidence-backed conclusions, then into bounded delivery slices with clear uncertainty and traceability.

## Use when

1. strategy or architecture decisions need evidence refresh
2. external inputs must be translated into repo-fit actions
3. you need repeatable research-to-delivery handoff

## Do not use when

Do not use when the task is already well-scoped implementation work with no research uncertainty.

## Inputs

- objective and constraints
- source corpus (docs, transcripts, links, notes, issues)
- repository context and current architecture state
- planning horizon and risk tolerance

## Outputs

- source-indexed findings
- confidence-scored claims
- contradiction and unknown register
- prioritized, bounded implementation slices
- handoff-ready prompt or work specification

## Procedure

### Phase 1: intake and normalize

1. gather source artifacts
2. normalize formats and metadata
3. assign stable source IDs

### Phase 2: extract and score

1. extract candidate claims
2. score each claim by evidence strength and relevance
3. mark unknowns and contradictions explicitly

### Phase 3: converge on accretive additions

1. generate bounded candidate additions
2. score impact, safety fit, and deployability
3. keep only candidates that pass acceptance thresholds

### Phase 4: handoff to delivery

1. produce bounded implementation slices
2. add acceptance tests and evidence requirements
3. publish execution-ready handoff artifacts

## Proof requirements

- every major claim must cite source IDs
- unknowns must remain explicit until resolved
- recommendations must include confidence and reason codes

## Common failure patterns

1. no source lineage for major claims
2. blending speculation with evidence without flags
3. producing broad plans with no bounded slices
4. dropping contradictions to maintain narrative simplicity

## Adaptation notes

- policy-heavy domains: elevate contradiction handling and citation density
- fast-moving domains: shorten refresh window and increase unknown tracking
- sparse-source repos: lower confidence and prioritize discovery slices

## Handoff format

```text
Evidence Research Flywheel Report

Objective:
Source corpus:
Coverage summary:

Claim inventory:
Confidence scoring:
Unknowns and contradictions:

Accepted additions:
Rejected additions:
Bounded implementation slices:

Handoff readiness:
- READY
- READY WITH EXPLICIT RISK
- NOT READY
```

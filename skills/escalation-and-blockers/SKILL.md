---
name: escalation-and-blockers
description: "Sets explicit escalation triggers, blocker definitions, and pause boundaries. Use when an agent must decide whether to continue, stop, or hand the work to a human."
license: Apache-2.0
compatibility: "Claude Code, Cursor, Codex, Grok Build, and GitHub Copilot. Needs git and a search tool such as rg."
allowed-tools: Bash Read Grep
metadata:
  category: governance
  status: provisional
  tags: "governance, escalation, stop"
  modes: "incident, pr-audit, execution"
  version: "1.0.0"
  author: SlipstreamAI
---

# EscalationAndBlockers

**Tagline:** Make pause and escalation explicit before failure forces it.

## Purpose

EscalationAndBlockers defines deterministic rules for when an agent can continue, when it must escalate, and when it must stop.

## Use when

1. workflows continue too far on weak assumptions
2. teams disagree on blocker severity
3. incident handling lacks pause boundaries

## Do not use when

Do not invoke if a clear, enforced escalation policy already exists.

## Inputs

- risk model
- orchestration lanes
- proof requirements
- operator approval boundaries

## Outputs

- escalation trigger matrix
- blocker taxonomy
- continuation authority rules
- stop and pause conditions

## Procedure

### Phase 1: define blocker taxonomy

1. missing spec or requirements
2. missing proof for risk level
3. unresolved contradiction
4. security or irreversible risk
5. missing required reviewer lane

### Phase 2: define escalation matrix

Map each blocker type to required escalation lane and operator involvement.

### Phase 3: define continuation authority

Set explicit conditions for implicit continuation versus mandatory pause.

## Proof requirements

- blocker classes must be explicit and non-overlapping
- escalation paths must map to concrete owner lanes
- high-risk blockers must force pause until resolved

## Common failure patterns

1. soft language around hard blockers
2. hidden operator decisions in chat only
3. escalation handled as optional suggestion

## Adaptation notes

- tune thresholds per repo, keep blocker classes stable
- include environment constraints in continuation policy

## Handoff format

```text
EscalationAndBlockers Report

Blocker taxonomy:
Escalation matrix:
Continuation authority:
Pause conditions:
Stop conditions:
Adoption risks:
```

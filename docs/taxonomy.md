# ClankerKit Taxonomy

## Purpose

The taxonomy keeps skills discoverable and prevents category drift.

## Categories

## `debugging`

Focus: reproduce, isolate, and explain failures with traceable evidence.

Typical outputs:

- failure path map
- root cause candidates
- confirmed fix path

## `validation`

Focus: verify whether a claimed outcome is actually proven.

Typical outputs:

- claim versus proof matrix
- evidence class map
- confidence classification

## `governance`

Focus: enforce quality gates, escalation rules, and merge readiness policy.

Typical outputs:

- gate verdict
- explicit risk acceptance or block
- tracked follow-up requirements

## `repo-understanding`

Focus: identify entrypoints, boundaries, ownership, and blast radius before edits.

Typical outputs:

- system map
- real entrypoint list
- risk-ranked change surfaces

## `delivery`

Focus: prepare high-signal PRs and enforce definition-of-done quality.

Typical outputs:

- merge readiness checklist
- docs and rollout completeness
- release notes and operator notes

## `hardening`

Focus: reduce production risk through resilience, observability, and failure coverage.

Typical outputs:

- readiness gaps
- mitigation actions
- evidence of resilience checks

## `documentation`

Focus: produce operator and maintainer handoff artifacts that reduce ambiguity.

Typical outputs:

- runbook updates
- handoff packets
- change impact summaries

## Classification guidance

Choose category by dominant operating intent:

- if the skill decides trust and merge safety, it is governance
- if the skill evaluates proof quality, it is validation
- if the skill maps unknown repo behavior, it is repo-understanding

## Stability labels

- `provisional`: expected to evolve quickly
- `stable`: shape and contract are field-tested
- `deprecated`: maintained only for compatibility

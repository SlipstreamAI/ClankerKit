---
name: "operator-handoff"
category: "documentation"
description: "Documentation skill for producing operational handoff artifacts that let another human or agent safely continue work without hidden context."
status: "provisional"
recommended-modes:
  - handoff
  - post-merge
  - incident-close
allowed-tools:
  - git
  - rg
  - python
  - repo-tools
tags:
  - documentation
  - handoff
  - operations
---

# OperatorHandoff

**Tagline:** Preserve the context that prevents repeat incidents.

## Purpose

OperatorHandoff creates clear handoff artifacts so ownership can transfer without losing critical context, assumptions, or safety boundaries.

## Use when

1. handing work from one owner to another
2. closing incidents with follow-up work
3. finishing non-trivial implementation lanes

## Do not use when

Do not invoke for trivial edits where no operational context changes.

## Inputs

- change summary
- validation and evidence artifacts
- open assumptions and risks
- next actions and ownership

## Outputs

- concise handoff packet
- operational risk summary
- unresolved items with owner
- next-step command or workflow references

## Procedure

### Phase 1: summarize outcomes

1. summarize what changed
2. summarize what was validated

### Phase 2: capture risk and limits

1. list open assumptions
2. list known failure modes and boundaries

### Phase 3: transfer control

1. assign owners for deferred work
2. define immediate next actions
3. attach artifact links

## Proof requirements

- handoff claims must link to evidence
- unresolved risks must include owner and expected action
- next actions must be executable

## Common failure patterns

1. status narrative with no actionable next steps
2. no owner on deferred risk
3. hidden assumptions not captured in handoff

## Adaptation notes

- small teams: keep packet concise but explicit
- larger orgs: include escalation paths and on-call ownership

## Handoff format

```text
OperatorHandoff Packet

What changed:
What was validated:
Open assumptions:
Known limits:

Deferred work and owners:
Next actions:
Artifact references:
```

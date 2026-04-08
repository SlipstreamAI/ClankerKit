# ClankerKit Authoring Guide

## Goal

Write skills that are reusable, inspectable, and operationally honest.

## Authoring rules

- start with one operating problem, not a broad domain
- define explicit use and non-use boundaries
- set a deterministic handoff format
- separate synthetic evidence from runtime-relevant proof
- include failure patterns that happen in real repos
- explain adaptation for constrained environments

## Required skill sections

Every skill should include:

- metadata frontmatter
- purpose
- use when
- do not use when
- inputs
- outputs
- procedure
- proof requirements
- common failure patterns
- adaptation notes
- example invocation
- handoff format

Use [`templates/skill-template.md`](/C:/DEV2/ClankerKit/templates/skill-template.md).

## Writing style

- precise over poetic
- practical over abstract
- concise over verbose
- direct language over reassurance language

## Proof discipline

If a claim is runtime-visible, default to runtime-relevant evidence.
If environment limits block stronger proof, downgrade confidence and state missing evidence.

## Taxonomy fit

Place skills by operating identity, not by keyword overlap.

- governance: truth enforcement, gates, escalation, merge policy
- validation: claim testing, evidence quality, runtime proof
- repo-understanding: mapping systems and entrypoints
- debugging: fault isolation and reproduction
- delivery: merge prep and done criteria
- hardening: production risk reduction
- documentation: operator-facing handoffs

## Quality bar before merge

1. Is the scope narrow enough to be reusable?
2. Is the output format deterministic?
3. Are failure patterns concrete?
4. Are proof requirements proportional to risk?
5. Could a team run this skill with no additional context?

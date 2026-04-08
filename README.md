# ClankerKit

Skills for agents that ship real software.

ClankerKit is a public kit of reusable skills for coding agents to build, validate, debug, and harden real software.

## What is a skill?

A skill is a reusable operating unit that tells an agent how to do one specific kind of work with clear scope, evidence standards, and handoff output. It is not just a prompt. A good skill is inspectable, testable, adaptable, and safe to run across repositories.

## What this repo is for

This repository provides practical, repo-agnostic building blocks for:

- understanding an unfamiliar codebase before broad edits
- tracing failures through real execution paths
- validating runtime-visible claims with runtime-relevant proof
- enforcing deterministic merge gates
- preventing fake progress and proofless completion claims

## Who this is for

- solo developers using coding agents in real projects
- small teams that want tighter agent governance without heavy process
- maintainers who need stronger merge-readiness confidence

## Design principles

- Claims need receipts.
- Real proof beats synthetic confidence.
- Deterministic beats vibes.
- Repo understanding comes before broad edits.
- Skills should be inspectable and composable.
- Production is different, so proof standards should be stronger.
- Governance belongs inside the agent loop, not only after incidents.

## Public status disclaimer

ClankerKit is public and usable now, but still early. Expect iteration in skill shape, taxonomy, and quality gates as real usage uncovers gaps. Stability labels in each skill are authoritative.

## Suggested consumption model

1. Start with one workflow, not the whole repo.
2. Pick a validation or governance skill and wire it into your PR or incident loop.
3. Keep local adaptations near the consuming repo and track the delta.
4. Promote only when a skill proves useful across multiple incidents or PRs.

## Directory map

- `skills/` reusable skills organized by operating domain
- `checks/` short skeptical checklists for review and gating
- `patterns/` durable operating patterns for loops and gates
- `templates/` canonical writing templates for new skills and checks
- `examples/` concrete invocation and loop examples
- `docs/` taxonomy, authoring, and consumption guidance

## Stability model

- `provisional`: useful now, expected to change quickly
- `stable`: field-tested shape with lower churn
- `deprecated`: kept for compatibility, do not extend

Each skill should declare status in frontmatter and document compatibility expectations.

## Contribution guidance

Contributions should stay content-first and operationally concrete.

- keep scope tight to one claim or one operating problem
- encode proof requirements and failure patterns explicitly
- avoid abstraction unless it removes real repetition
- include realistic examples and deterministic handoff formats
- keep language crisp and avoid hype

## Philosophy

ClankerKit exists to help agents avoid fake progress, weak validation, shallow repo understanding, brittle edits, and confidence without runtime proof.

This repo does not optimize for comfort language. It optimizes for trustworthy outcomes.

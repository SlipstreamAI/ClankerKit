---
name: "skill-intake-gate"
category: "governance"
description: "Governance skill for screening contributed skills for safety, determinism, and quality before they are accepted into a shared repository."
status: "provisional"
recommended-modes:
  - contribution-review
  - security-review
allowed-tools:
  - git
  - rg
  - python
  - repo-tools
tags:
  - governance
  - contribution
  - safety
  - determinism
---

# SkillIntakeGate

**Tagline:** Contributions are welcome, unsafe skills are not.

## Purpose

SkillIntakeGate evaluates contributed skills before merge to prevent malicious, unsafe, or low-quality additions from entering the library.

## Use when

1. reviewing new skill submissions
2. reviewing major skill rewrites
3. validating external contributor PRs

## Do not use when

Do not invoke for unrelated documentation-only edits that do not affect skill behavior or policy.

## Inputs

- contributed files and diff
- target category and intended use
- repository contribution policy
- automated lint and gate outputs

## Outputs

- intake decision (`accept`, `accept_with_changes`, `reject`)
- policy violations
- safety concerns
- determinism concerns
- required remediation list

## Procedure

### Phase 1: structure validation

1. validate frontmatter and required sections
2. validate category fit and naming clarity
3. validate deterministic handoff contract

### Phase 2: safety screening

1. scan for unsafe instruction patterns
2. scan for auth-bypass or exfiltration guidance
3. scan for destructive defaults without guardrails

### Phase 3: quality screening

1. verify scope clarity
2. verify proof requirements and failure patterns
3. verify adaptation notes for repo-agnostic usage

### Phase 4: decision

1. return intake decision
2. list required edits if not accepted
3. classify severity for each finding

## Proof requirements

- acceptance must be backed by gate outputs
- safety findings must include exact matching lines
- rejection decisions must include actionable remediation

## Common failure patterns

1. broad prompts without operating boundaries
2. unsafe language hidden in examples
3. nondeterministic output contracts
4. no proof requirements for high-risk usage

## Adaptation notes

- apply stricter thresholds to governance and validation categories
- require owner approval for category-critical changes

## Handoff format

```text
SkillIntakeGate Report

Contribution scope:
Policy checks:
Safety checks:
Determinism checks:
Quality checks:

Decision:
- accept
- accept_with_changes
- reject

Required remediation:
Severity summary:
```

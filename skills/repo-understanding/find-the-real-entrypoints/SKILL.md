---
name: "find-the-real-entrypoints"
category: "repo-understanding"
description: "Repo-understanding skill for locating true runtime entrypoints and separating them from test scaffolds, demos, and dead paths."
status: "provisional"
recommended-modes:
  - discovery
  - pre-implementation
allowed-tools:
  - git
  - rg
  - python
  - repo-tools
tags:
  - repo-understanding
  - entrypoints
  - runtime-paths
---

# FindTheRealEntrypoints

**Tagline:** Edit where runtime starts, not where convenience points.

## Purpose

FindTheRealEntrypoints identifies the actual execution entrypoints used in real runs and distinguishes them from non-authoritative paths.

## Use when

1. a repo has multiple startup scripts or wrappers
2. runtime behavior is inconsistent across environments
3. proposed edits may target the wrong path

## Do not use when

Do not invoke when runtime entrypoint is already single and verified.

## Inputs

- repository root
- known run commands and environments
- observed runtime behavior
- startup and deployment docs if present

## Outputs

- canonical runtime entrypoint list
- non-authoritative path list
- confidence level per entrypoint
- validation recommendations

## Procedure

### Phase 1: enumerate candidates

1. list startup scripts and command wrappers
2. map referenced executables or module entry files

### Phase 2: validate authority

1. compare local, CI, and deployment invocation paths
2. identify which paths are actually used in routine operations

### Phase 3: classify

1. mark `canonical`, `conditional`, or `non-authoritative`
2. record assumptions and unresolved ambiguities

## Proof requirements

- canonical entrypoints must be supported by execution evidence
- conditional entrypoints must specify trigger conditions
- ambiguous entrypoints must not be treated as canonical

## Common failure patterns

1. editing test bootstrap as if it were runtime bootstrap
2. assuming README commands represent production invocation
3. missing wrapper scripts that mutate environment assumptions

## Adaptation notes

- frontend repos: include build and serve path distinction
- backend repos: include worker and job entrypoints
- monorepos: map per-package entrypoints with ownership notes

## Handoff format

```text
FindTheRealEntrypoints Report

Entrypoint candidates:
Canonical runtime entrypoints:
Conditional entrypoints:
Non-authoritative paths:

Evidence and confidence:
Unresolved assumptions:
Recommended validations:
```

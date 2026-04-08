---
name: "map-the-system"
category: "repo-understanding"
description: "Repo-understanding skill for building a practical map of entrypoints, boundaries, dependencies, and blast radius before broad edits."
status: "provisional"
recommended-modes:
  - discovery
  - pre-implementation
  - incident
allowed-tools:
  - bash
  - git
  - rg
  - python
  - repo-tools
tags:
  - repo-understanding
  - system-mapping
  - entrypoints
  - blast-radius
---

# MapTheSystem

**Tagline:** A repo-understanding skill that maps the real system before edits expand risk.

## Purpose

MapTheSystem builds an actionable model of how the target repository actually runs.

It helps agents avoid broad edits based on guessed architecture by identifying:

- real entrypoints
- execution boundaries
- high-risk collaborators
- likely blast radius

## Use when

Invoke MapTheSystem when:

1. Entering an unfamiliar repository.
2. Planning a non-trivial feature or refactor.
3. Debugging failures that may cross package or service boundaries.
4. You need a risk map before touching runtime-visible surfaces.

## Do not use when

Do not invoke MapTheSystem for a tiny isolated edit where the relevant file and call path are already clear.

## Inputs

- target objective or claimed change
- repo root path
- changed files if available
- known runtime commands and environment constraints
- existing docs or runbooks if present

If objective is missing, MapTheSystem should infer likely focal surfaces from recent diffs and state assumptions.

## Outputs

MapTheSystem must return:

- system map summary
- real entrypoints and startup paths
- boundary map (API, auth, storage, subprocess, external services)
- dependency risk list
- blast radius estimate
- unknowns and assumptions
- recommended next skills

## Procedure

### Phase 1: Locate execution anchors

1. Find startup scripts, app entry modules, and primary command paths.
2. Identify test harness entrypoints separately from runtime entrypoints.
3. Distinguish operator surfaces from internal modules.

### Phase 2: Trace boundaries

1. Identify API routes, handlers, and service boundaries.
2. Locate auth and permission boundaries.
3. Locate filesystem, subprocess, and network boundaries.
4. Identify deployment and startup configuration dependencies.

### Phase 3: Build risk map

1. Rank touched surfaces by blast radius.
2. Highlight irreversible or state-mutating operations.
3. Flag boundaries where synthetic tests often mask risk.

### Phase 4: Define verification plan

1. Propose minimal runtime-relevant paths to validate.
2. Propose failure-mode checks for top-risk assumptions.
3. Recommend follow-up skills by risk profile.

## Common failure patterns

1. Treating docs as canonical while entrypoints drifted.
2. Confusing test bootstrap paths with runtime startup paths.
3. Missing side effects in shell calls, env reads, or file IO.
4. Editing shared modules without blast radius assessment.
5. Ignoring deployment scripts when claiming runtime behavior.

## Adaptation notes

- frontend-only repos: map rendering and data-fetch entrypoints plus build/runtime config split
- backend repos: map route-to-service and job-to-worker execution paths
- monorepos: map package ownership and cross-package contracts before edits
- restricted local environments: mark unknown boundaries and lower confidence

## Handoff format

```text
MapTheSystem Report

Objective:
Repository scope:

Runtime entrypoints:
Test entrypoints:
Operator-visible surfaces:

Boundary map:
- API:
- Auth:
- Filesystem:
- Subprocess:
- External services:
- Deployment/startup:

Blast radius estimate:
Top risk surfaces:
Unknowns and assumptions:

Recommended next skills:
- ...
```

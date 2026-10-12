---
name: blast-radius-scan
description: "Estimates change impact across code, runtime boundaries, and operational workflows. Use when a diff looks small but shared types, config, or data paths may spread the effect."
license: Apache-2.0
compatibility: "Claude Code, Cursor, Codex, Grok Build, and GitHub Copilot. Needs git and a search tool such as rg."
allowed-tools: Bash Read Grep
metadata:
  category: repo-understanding
  status: provisional
  tags: "impact, risk, diff"
  modes: "pre-edit, pr-audit"
  version: "1.0.0"
  author: SlipstreamAI
---

# BlastRadiusScan

**Tagline:** Measure impact before you ship impact.

## Purpose

BlastRadiusScan estimates the likely impact surface of a change and flags cross-boundary risk before implementation or merge.

## Use when

1. changes touch shared modules or core boundaries
2. refactors may affect multiple subsystems
3. rollback cost is high

## Do not use when

Do not invoke for isolated edits with no dependency fan-out.

## Inputs

- target diff or intended change set
- dependency map or import graph if available
- runtime and deployment boundaries
- known critical surfaces

## Outputs

- impacted component inventory
- boundary-risk map
- blast radius level (`low`, `medium`, `high`, `critical`)
- recommended safeguards

## Procedure

### Phase 1: map direct impact

1. list files and modules touched
2. identify direct dependents

### Phase 2: map boundary impact

1. trace API, auth, IO, and deployment boundaries
2. identify operational surfaces affected

### Phase 3: classify and guard

1. assign blast radius level
2. define minimum validation and rollback requirements

## Proof requirements

- high and critical levels require explicit rollback path
- boundary-sensitive impacts require failure-mode checks
- assumptions affecting impact level must be explicit

## Common failure patterns

1. underestimating shared utility changes
2. ignoring deployment or startup side effects
3. no rollback plan for critical paths

## Adaptation notes

- monorepos: include cross-package consumer map
- service architectures: include upstream and downstream dependency effects
- frontend repos: include routing and data contract fan-out

## Handoff format

```text
BlastRadiusScan Report

Change scope:
Impacted components:
Boundary-risk map:
Blast radius level:

Required safeguards:
Rollback requirements:
Unverified assumptions:
```

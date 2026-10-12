---
name: dependency-upgrade
description: "Plans and verifies a dependency bump, including majors, using the changelog and the project's tests. Use when upgrading a direct dependency, especially across a major version, and you need a rollback path."
license: Apache-2.0
compatibility: "Claude Code, Cursor, Codex, Grok Build, and GitHub Copilot. Needs git and a search tool such as rg."
allowed-tools: Bash Read Grep
metadata:
  category: delivery
  status: experimental
  tags: "dependencies, upgrade, maintenance"
  modes: "maintenance, pre-merge"
  version: "0.1.0"
  author: SlipstreamAI
---

# Dependency Upgrade

**Tagline:** Bump on purpose, with the changelog and the tests.

## Purpose

Dependency Upgrade keeps a bump small enough to explain. One major at a time, changelog notes that affect this repo, tests that actually ran, and a lockfile revert as the rollback.

## Use when

1. A direct dependency needs a minor, patch, or major bump.
2. A transitive security fix forces a lockfile change.
3. You need to know whether the bump changes runtime behavior.

## Do not use when

- Rewriting the application to a different framework in the same change.
- Blindly updating every dependency in the lockfile.

## Inputs

- Package name and target version.
- Manifest and lockfile paths.
- Test or build command that should stay green.

## Outputs

- Current version, target version, and whether the bump is major.
- Changelog items that affect this repo, each marked confirmed or not applicable.
- Commands run and results.
- Rollback step.

See [bump checklist](references/bump-checklist.md).

## Procedure

### Phase Pin the jump

1. Record the installed version and the target.
2. If the major version changes, do not combine it with unrelated majors.
3. Read the upstream changelog or release notes between those versions.

### Phase Map breakages to this repo

1. Search call sites of renamed or removed APIs.
2. Note transitive packages that move with the bump.
3. Ignore changelog items that this repo cannot hit, and say why.

### Phase Apply and test

1. Update the manifest and refresh the lockfile using the project's package manager.
2. Run the targeted tests plus the build or typecheck if the repo has one.
3. If tests fail, fix the call site or stop and report the upstream break. Do not pin past the failure silently.

### Phase Leave a rollback

1. The rollback is reverting the manifest and lockfile commits.
2. Call out data-format or migration changes that a revert would not undo.

## Proof requirements

- Versions before and after are in the handoff.
- Relevant changelog lines are quoted or summarized with a link or version tag.
- The test command output is recorded, or the gap is marked unmeasured.

## Common failure patterns

- A lockfile refresh that also upgrades unrelated packages with no mention.
- Claiming compatibility without reading the major changelog.
- Deleting a test that failed because of the bump.

## Adaptation notes

- Python: prefer the repo's lock or constraints file over a floating install.
- JavaScript: commit the lockfile the package manager actually produced.
- No network in the environment: prepare the edit and mark the install unmeasured.

## Example invocation

```text
Use dependency-upgrade.

Package: react-router
Target: 7.x
Tests: npm test

Return changelog impacts, test receipt, and rollback.
```

## Handoff format

```text
Dependency Upgrade Report

Status: success | partial | blocked | failed
Package:
From version:
To version:
Changelog impacts:
Commands and results:
Unrelated lockfile drift:
Rollback:
Residual risk:
```

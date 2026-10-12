---
name: release-notes-and-changelog
description: "Drafts release notes and a changelog from merged commits or pull requests, and makes a semver call with reasons. Use when cutting a release or updating a changelog and the notes must match the history."
license: Apache-2.0
compatibility: "Claude Code, Cursor, Codex, Grok Build, and GitHub Copilot. Needs git and a search tool such as rg."
allowed-tools: Bash Read Grep
metadata:
  category: documentation
  status: experimental
  tags: "release, changelog, semver"
  modes: "release"
  version: "0.1.0"
  author: SlipstreamAI
---

# Release Notes and Changelog

**Tagline:** Notes from the commits that actually merged.

## Purpose

Release Notes and Changelog writes user-facing notes from merged history. Internal chores stay out of the user section unless the repo's policy says otherwise. The version bump is a decision with a reason.

## Use when

1. You are preparing a tagged release.
2. A changelog entry is missing for user-visible work.
3. You need a semver recommendation grounded in the diff, not in the branch name.

## Do not use when

- Inventing marketing copy for work that did not merge.
- API compatibility review by itself. Use api-contract-check, then feed the result here.

## Inputs

- The previous release tag or commit.
- The commit or PR list since then.
- Who the notes are for: users, operators, or library consumers.

## Outputs

- Grouped notes: breaking, added, fixed, internal.
- Semver call and the commit that forced it.
- Changelog text ready to paste.

List subjects since a ref with [commits_since.py](scripts/commits_since.py).

## Procedure

### Phase Collect history

1. Run `python scripts/commits_since.py <previous-tag>` from this skill directory inside the target repo, or pass `--repo`.
2. Drop merge noise only if the merged PR titles remain.
3. Open the diffs for anything user-visible that the subject line does not explain.

### Phase Sort for the audience

1. Breaking: removed or changed behavior a caller must handle.
2. Added and fixed: things a user or operator can observe.
3. Internal: refactors and chores. Keep them in a separate section or omit them if the changelog policy says so.

### Phase Call the version

1. Major if a breaking change exists for the public contract.
2. Minor if behavior is added compatibly.
3. Patch if only fixes land.
4. Name the commit or PR that determined the call.

### Phase Paste-ready text

1. Write the changelog in the repo's existing style.
2. Do not claim a migration that api-contract-check or db-migration-safety did not establish. Point at the gap.

## Proof requirements

- Every user-facing bullet maps to a commit or PR.
- The semver call cites the change that forced it.

## Common failure patterns

- Notes written from memory of the sprint.
- A breaking API change listed as a patch.
- Internal rename described as a user feature.

## Adaptation notes

- Libraries: lead with breaking changes and the version.
- Apps: lead with what users can do differently, and put operator steps in their own list.

## Example invocation

```text
Use release-notes-and-changelog since v1.4.0.

Audience: library consumers.

Return grouped notes and a semver call.
```

## Handoff format

```text
Release Notes and Changelog Report

Status: success | partial | blocked | failed
Range:
Breaking:
Added:
Fixed:
Internal omitted:
Semver:
Because:
Changelog draft:
```

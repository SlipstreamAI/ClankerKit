---
name: write-real-tests
description: "Adds behavior tests that fail for a real reason before the fix and pass after it. Use when a change needs coverage that proves behavior, especially when existing tests only assert mocks, snapshots, or implementation details."
license: Apache-2.0
compatibility: "Claude Code, Cursor, Codex, Grok Build, and GitHub Copilot. Needs git and a search tool such as rg."
allowed-tools: Bash Read Grep
metadata:
  category: validation
  status: experimental
  tags: "testing, behavior, coverage"
  modes: "bugfix, feature, pr-audit"
  version: "0.1.0"
  author: SlipstreamAI
---

# Write Real Tests

**Tagline:** Add tests that fail when the behavior breaks.

## Purpose

Write Real Tests finds the public behavior in a change and adds a check that would go red if that behavior disappeared. Pair it with test-surface-skeptic when you need to judge a suite that already exists.

## Use when

1. A bug fix or feature has no test that exercises the behavior a caller sees.
2. Existing tests pass by stubbing the function under test.
3. You need a failing test recorded before the code change, or a characterization test before a refactor.

## Do not use when

- Generating a large snapshot suite with no asserted behavior.
- Load or performance testing. Use performance-profile for measurements.

## Inputs

- The behavior claim, in one sentence.
- Diff or target files.
- How the project runs tests.
- Optional base ref. Defaults to the working tree versus HEAD.

## Outputs

- Changed surfaces with and without a nearby test.
- The new or updated test name.
- The command run, and whether it failed before and passed after.
- What the test would still miss.

Run [list_changed_surfaces.py](scripts/list_changed_surfaces.py) to list changed files and nearby tests.

## Procedure

### Phase Name the behavior

1. Restate the claim as an observable outcome, not a function call.
2. Run `python skills/write-real-tests/scripts/list_changed_surfaces.py` from a checkout of this skill, or the copy under the installed skill directory, against the consuming repo.
3. Pick the boundary a real caller hits: exported function, HTTP route, CLI, job, or component behavior.

### Phase Write the failing check

1. Add the smallest test that fails if the behavior is wrong.
2. Assert the outcome. Do not assert that a mock was constructed.
3. Run the test and record the failure reason. A failure caused by a typo in the test is not a red receipt.

### Phase Prove the pass

1. Apply or confirm the implementation.
2. Re-run the same command and record the pass.
3. If you cannot run the test, the handoff status is partial and the test is not proof.

### Phase State the gap

1. Name one adjacent case the new test does not cover.
2. Do not raise coverage numbers as the result. The result is the behavior that now fails when removed.

## Proof requirements

- The handoff includes the test command and the observed fail and pass, or an explicit reason the run did not happen.
- The assertion matches the behavior claim.
- The test does not replace the subject with a fake that returns the expected value.

## Common failure patterns

- A test that passes on the broken code.
- Snapshot or mock-call assertions standing in for the user-visible outcome.
- Reporting coverage percent as proof.

## Adaptation notes

- Frontend: assert rendered result or network payload, then use frontend-ui-verify for visual proof.
- Libraries: test the public API, not private helpers.
- No test runner available: write the test anyway and mark the run unmeasured.

## Example invocation

```text
Use write-real-tests.

Claim: an empty cart total is zero, not null.
Command: pytest tests/test_cart.py -q

Return the test name, the red output, and the green output.
```

## Handoff format

```text
Write Real Tests Report

Status: success | partial | blocked | failed
Behavior claim:
Boundary tested:
Test name:
Command:
Red result:
Green result:
Still untested:
Unverified assumptions:
```

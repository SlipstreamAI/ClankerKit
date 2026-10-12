---
name: fix-flaky-test
description: "Reproduces a flaky test, classifies the cause, and proves a de-flake with repeated runs. Use when a test fails intermittently and quarantine or a rerun is being treated as the fix."
license: Apache-2.0
compatibility: "Claude Code, Cursor, Codex, Grok Build, and GitHub Copilot. Needs git and a search tool such as rg."
allowed-tools: Bash Read Grep
metadata:
  category: debugging
  status: experimental
  tags: "tests, flake, debugging"
  modes: "ci, bugfix"
  version: "0.1.0"
  author: SlipstreamAI
---

# Fix Flaky Test

**Tagline:** Reproduce the flake, name the class, then fix it.

## Purpose

Fix Flaky Test refuses to call a rerun a fix. It gets the failure to happen, classifies it, changes the cause, and shows a repeat run that stayed green.

## Use when

1. CI fails on a test that passes locally, or passes on rerun.
2. A test depends on time, order, shared state, network, or a race.
3. Someone proposed skipping the test.

## Do not use when

- A test that fails every time. Use trace-the-failure.
- Product bugs that a stable test already catches. Fix the product with the stable test as the receipt.

## Inputs

- Test name and command.
- A failing log, if one exists.
- How many repeats you can afford.

## Outputs

- Reproduction rate before the fix.
- Classification of the flake.
- The change and a repeat count that stayed green.
- Quarantine only if a tracked follow-up exists.

## Procedure

### Phase Reproduce

1. Run the test in a loop. Start with 20 repeats if the suite is cheap, fewer if it is not, and record the count.
2. If it never fails, vary order, timezone, CPU count, or a clean workspace and say what you tried.
3. Keep the failing output. A flake you cannot reproduce stays partial.

### Phase Classify

1. Time or clock: timeouts, sleeps, midnight, locale.
2. Order: leaks from another test, shared database, global singleton.
3. Race: async completion assumed.
4. Resource: port, file lock, temp directory collision.
5. External: network or a live service that the test should not need.

### Phase Fix the cause

1. Remove the shared mutable state, freeze the clock, or wait on the real condition instead of a sleep.
2. Do not raise a timeout as the only change unless you show the previous timeout was below a measured duration.
3. Quarantine only with an owner and a tracked follow-up, and say the flake is not fixed.

### Phase Prove stability

1. Re-run the same loop.
2. Report passes out of attempts.
3. If any failure remains, the status is failed or partial, not success.

## Proof requirements

- Before and after repeat counts are numbers, not 'seems stable'.
- The classification matches the code change.

## Common failure patterns

- Retry logic in CI treated as a de-flake.
- A longer sleep with no measurement.
- Deleting the assertion that flickered.

## Adaptation notes

- Browser tests: isolate storage and freeze time before blaming the network.
- Shared CI runners: reproduce with the same flags the runner uses, if they are known.

## Example invocation

```text
Use fix-flaky-test on tests/test_queue.py::test_drain.

CI failed once in 14 runs.
Loop locally 30 times before and after the change.
```

## Handoff format

```text
Fix Flaky Test Report

Status: success | partial | blocked | failed
Test:
Reproduction before:
Classification:
Change:
Repeats after:
Quarantine:
Follow-up:
```

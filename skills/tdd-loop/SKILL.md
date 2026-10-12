---
name: tdd-loop
description: "Runs a red-green-refactor loop and records the command receipt for each step. Use when implementing a behavior and you want the test to fail for the right reason before production code changes."
license: Apache-2.0
compatibility: "Claude Code, Cursor, Codex, Grok Build, and GitHub Copilot. Needs git and a search tool such as rg."
allowed-tools: Bash Read Grep
metadata:
  category: delivery
  status: experimental
  tags: "testing, tdd, implementation"
  modes: "feature, bugfix"
  version: "0.1.0"
  author: SlipstreamAI
---

# TDD Loop

**Tagline:** Red, green, refactor, with the commands written down.

## Purpose

TDD Loop keeps implementation behind a failing test. The receipt is the red run, the green run, and a refactor run that stays green. It is the execution loop; write-real-tests is the narrower skill for adding a missing behavior test.

## Use when

1. You are about to implement a new behavior or a bug fix.
2. A previous attempt jumped to code and the tests were written afterward.
3. You need a resumable checkpoint between red, green, and refactor.

## Do not use when

- Exploratory spikes where the behavior is still unknown. Time-box the spike, then start the loop once the claim is one sentence.
- Large refactors with no behavior change. Use refactor-safely.

## Inputs

- One behavior sentence.
- Test command.
- Where new tests belong in this repo.

## Outputs

- Red command and the assertion that failed.
- Green command after the smallest code change.
- Refactor command, still green, or an explicit skip.
- Files touched in each step.

## Procedure

### Phase Red

1. Write the behavior as one sentence a reviewer can check.
2. Add a test that fails because the behavior is absent or wrong.
3. Run it. Stop if the failure is a syntax error, missing fixture, or a passing test.

### Phase Green

1. Change production code only enough to make that test pass.
2. Do not add neighboring features in this step.
3. Re-run the same test command and record the pass.

### Phase Refactor

1. Clean names and structure only while the same tests stay green.
2. Re-run the tests after the cleanup. If you skip refactor, say so.
3. If a refactor changes behavior, go back to red. That is a new loop.

### Phase Hand off

1. List commands and results in order.
2. Note any test you could not run.
3. Stop when the behavior sentence is true and evidenced, or when you are blocked.

## Proof requirements

- Red output shows the intended assertion failing.
- Green output is the same command after the code change.
- No production behavior was added that the new test does not speak to, unless it is called out as unverified.

## Common failure patterns

- Writing the code first and weakening the test until it passes.
- A red failure that is an import error rather than the behavior.
- Refactor mixed with a feature so the receipt no longer maps to one claim.

## Adaptation notes

- Slow suites: run the targeted test during the loop, then the broader command once at the end and record both.
- UI behavior: the red test can be a component or route test; visual proof is a separate frontend-ui-verify pass.

## Example invocation

```text
Use tdd-loop.

Behavior: duplicate email registration returns 409.
Test command: npm test -- registration.test.ts

Return red, green, and refactor receipts.
```

## Handoff format

```text
TDD Loop Report

Status: success | partial | blocked | failed
Behavior:
Red command:
Red evidence:
Green command:
Green evidence:
Refactor command:
Files by step:
Unverified assumptions:
```

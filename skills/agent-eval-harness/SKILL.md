---
name: agent-eval-harness
description: "Sets up an evaluation harness for an agent or LLM feature with explicit cases and graders. Use when an agent prompt, tool, or model change needs a repeatable pass rate instead of a single impressive example."
license: Apache-2.0
compatibility: "Claude Code, Cursor, Codex, Grok Build, and GitHub Copilot. Needs git and a search tool such as rg."
allowed-tools: Bash Read Grep
metadata:
  category: validation
  status: experimental
  tags: "evals, agents, llm"
  modes: "feature, regression"
  version: "0.1.0"
  author: SlipstreamAI
---

# Agent Eval Harness

**Tagline:** Grade agent behavior with cases, not vibes.

## Purpose

Agent Eval Harness turns 'it seemed better' into cases with inputs, expected outcomes, and a grader you can rerun. A handful of smoked examples can seed the set. They are not the result.

## Use when

1. You changed a prompt, tool list, or model for an agent feature.
2. Failures are anecdotal and need a regression set.
3. You need a pass rate recorded before and after a change.

## Do not use when

- Evaluating a human's writing taste with no rubric.
- A benchmark leaderboard project. This skill builds the smallest harness the change needs.

## Inputs

- The behavior under test.
- At least a few real or realistic inputs, including one failure you care about.
- How a case passes: exact match, rubric, tool called, or schema-valid output.

## Outputs

- Case file.
- Grader command.
- Pass rate before and after, or a single baseline if there is no before.
- Cases that failed, with the actual output summarized.

Start from [the case template](assets/case-template.json).

## Procedure

### Phase Write cases

1. Each case has an id, input, expected outcome, and grader type.
2. Include the failure that motivated the change.
3. Keep a couple of cases out of the prompt-editing loop so you are not only training on the set you stare at.

### Phase Grade honestly

1. The grader is code or a rubric with yes/no checks, not a fresh impression.
2. Partial credit must be defined. Otherwise a case passes or fails.
3. Do not hide a failure by editing the expected value after seeing a wrong answer, unless the expected value was actually wrong. Record that edit.

### Phase Run

1. Run the harness on the unchanged behavior if you still can.
2. Run it again after the change.
3. Report passes over total, plus the failed ids.

### Phase Limit the claim

1. The claim is about these cases, not about all future inputs.
2. Name cases you wanted and did not have data for.

## Proof requirements

- The case file path and the command are in the handoff.
- Pass counts are numbers.
- Failed cases are listed.

## Common failure patterns

- One chat transcript offered as an evaluation.
- A grader that always returns pass.
- Editing failing cases out of the set to raise the rate.

## Adaptation notes

- Tool-using agents: grade the tool name and arguments as well as the final text.
- No model access in the environment: commit the cases and mark the run blocked.

## Example invocation

```text
Use agent-eval-harness.

Behavior: the triage agent chooses ci-failure-triage for a red check log.
Cases: 8 transcripts.
Grader: expected skill name.

Return the pass rate and failed ids.
```

## Handoff format

```text
Agent Eval Harness Report

Status: success | partial | blocked | failed
Behavior:
Case file:
Grader:
Before:
After:
Failed ids:
Held-out cases:
Claim limited to:
```

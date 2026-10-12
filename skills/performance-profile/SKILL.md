---
name: performance-profile
description: "Measures a performance claim before and after a change, using the same workload. Use when someone wants a speed or cost improvement and the only evidence so far is a feeling or a single anecdote."
license: Apache-2.0
compatibility: "Claude Code, Cursor, Codex, Grok Build, and GitHub Copilot. Needs git and a search tool such as rg."
allowed-tools: Bash Read Grep
metadata:
  category: validation
  status: experimental
  tags: "performance, benchmark, measurement"
  modes: "optimization, pr-audit"
  version: "0.1.0"
  author: SlipstreamAI
---

# Performance Profile

**Tagline:** Measure, then change one thing, then measure again.

## Purpose

Performance Profile blocks optimizations that have no baseline. One workload, one change, numbers from a command you can rerun.

## Use when

1. A PR claims a faster endpoint, query, render, or job.
2. You are about to rewrite a hot path.
3. A regression is suspected and needs a number, not a hunch.

## Do not use when

- Micro-optimizing code outside a measured hot path.
- Load testing a production system you are not allowed to touch.

## Inputs

- The claim, including the metric: latency, throughput, CPU, queries, or bundle size.
- A workload you can repeat.
- The change under test.

## Outputs

- Baseline command and numbers.
- After command and numbers.
- What else changed in the environment.
- Whether the claim is supported.

## Procedure

### Phase Define the metric

1. Pick one primary number. Extra numbers are context.
2. Write the workload: input size, concurrency, and warm versus cold.
3. If you cannot run it, stop with status blocked rather than estimating.

### Phase Baseline

1. Run the workload on the unchanged code at least three times when it is cheap, once when it is expensive, and record each result.
2. Note machine, dataset, and caches.
3. Save the command line.

### Phase Change one thing

1. Apply the optimization without unrelated refactors.
2. Repeat the same command.
3. If the number does not move, say so. Do not stack more changes until you know.

### Phase Judge the claim

1. Compare the numbers to the claim.
2. Call out variance that swallows the difference.
3. Do not generalize from one endpoint to the whole system.

## Proof requirements

- Both commands and their outputs are in the handoff.
- The workload is the same before and after.

## Common failure patterns

- A flame graph with no before number.
- Benchmarking a mock.
- Changing the workload between runs.

## Adaptation notes

- SQL: include the query plan only as support for the timing number.
- Frontend: measure the same page build or a recorded browser trace, and name the network conditions.

## Example invocation

```text
Use performance-profile.

Claim: invoice list p95 drops below 200ms on 1000 rows.
Workload: local API, seeded fixture, 20 requests.

Return before and after numbers.
```

## Handoff format

```text
Performance Profile Report

Status: success | partial | blocked | failed
Metric:
Workload:
Baseline:
After:
Environment:
Claim supported: yes | no | unclear
Not measured:
```

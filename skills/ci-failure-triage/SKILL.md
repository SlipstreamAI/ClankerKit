---
name: ci-failure-triage
description: "Reads a failing CI log, separates infrastructure failures from product failures, and proposes the smallest fix. Use when a pull request or main branch check is red and the log is the evidence you have."
license: Apache-2.0
compatibility: "Claude Code, Cursor, Codex, Grok Build, and GitHub Copilot. Needs git and a search tool such as rg."
allowed-tools: Bash Read Grep
metadata:
  category: debugging
  status: experimental
  tags: "ci, triage, logs"
  modes: "ci, bugfix"
  version: "0.1.0"
  author: SlipstreamAI
---

# CI Failure Triage

**Tagline:** Read the failing job, isolate the cause, fix the smallest thing.

## Purpose

CI Failure Triage starts from the log, not from a guess about the last commit. It identifies the failing job, the first relevant error, and whether the fix belongs in product code, the workflow, or a rerun.

## Use when

1. A required check is red.
2. The log is long and the author cannot see the first real error.
3. You must decide between a code fix, a workflow fix, and a rerun.

## Do not use when

- Flakes already reproduced locally. Use fix-flaky-test.
- Rewriting the pipeline when one command failed.

## Inputs

- A log file, a pasted log, or a URL you have already saved locally.
- The job name and the commit SHA if known.
- Whether the same job passed on the parent commit.

## Outputs

- Failing job and the first relevant error.
- Class: product, test, workflow, environment, or unknown.
- Smallest fix, or the rerun justification.
- What remains unverified if you cannot rerun the job.

Extract the error tail with [extract_failure.py](scripts/extract_failure.py).

## Procedure

### Phase Isolate the job

1. Name the failing check. Ignore later jobs that failed because an earlier one failed, unless they have their own error.
2. Run `python scripts/extract_failure.py path/to/log` from this skill directory.
3. Find the first error, not the last cascade.

### Phase Classify

1. Product: assertion or runtime error in repo code.
2. Test: the check itself is wrong or outdated.
3. Workflow: bad path, missing dependency install, wrong trigger.
4. Environment: runner out of disk, network to a package host, expired credential. Do not print secret values from the log.

### Phase Choose the smallest fix

1. If the parent commit passed and the diff explains the error, fix the diff.
2. If the log shows an environment fault and the same SHA passed elsewhere, say rerun, and why that is not hiding a product bug.
3. Do not expand the change to neighboring refactors.

### Phase Verify

1. Re-run the same job or the same command locally.
2. If you cannot rerun, status is partial and the fix is a hypothesis.

## Proof requirements

- The handoff quotes the first relevant error line.
- The classification and the fix agree.
- A rerun is justified with evidence, not used as a default.

## Common failure patterns

- Fixing a downstream cascade and missing the first error.
- Copying secret material from logs into the handoff or the repo.
- Declaring CI green without a new run when you changed code.

## Adaptation notes

- Matrix builds: name the exact cell that failed.
- Required checks you cannot rerun: point to the command a maintainer should click or run.

## Example invocation

```text
Use ci-failure-triage on the saved log at /tmp/ci-job.log.

Job: test
SHA: abc123
Parent: green

Return the first error, the class, and the smallest fix.
```

## Handoff format

```text
CI Failure Triage Report

Status: success | partial | blocked | failed
Job:
SHA:
First relevant error:
Class: product | test | workflow | environment | unknown
Fix:
Verification:
Secrets omitted:
```

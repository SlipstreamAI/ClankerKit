---
name: security-review
description: "Reviews a diff for secrets, injection sinks, and missing authorization on new entrypoints. Use when a change touches auth, user input, queries, shell, files, deserialization, or dependencies and needs severity-ranked findings."
license: Apache-2.0
compatibility: "Claude Code, Cursor, Codex, Grok Build, and GitHub Copilot. Needs git and a search tool such as rg."
allowed-tools: Bash Read Grep
metadata:
  category: hardening
  status: experimental
  tags: "security, review, owasp"
  modes: "pr-audit, pre-merge"
  version: "0.1.0"
  author: SlipstreamAI
---

# Security Review

**Tagline:** Review the diff for trust-boundary mistakes.

## Purpose

Security Review is a reviewer pass over a diff. It names the trust boundary, the finding, and a safe fix. It does not write exploit procedures.

## Use when

1. A PR adds an entrypoint, query, file path, HTML sink, or privileged action.
2. Secrets or tokens might have been committed.
3. You need findings ranked blocker, high, medium, or note before merge.

## Do not use when

- A full application penetration test.
- Dependency CVE triage with no code change. Use dependency-upgrade for a bump, and this skill if the bump touches call sites.

## Inputs

- Diff or PR.
- Who the attacker is in one sentence: anonymous user, authenticated user, or insider with a stolen token.
- Auth model of the app, if known.

## Outputs

- Trust boundaries touched.
- Findings with severity, location, and a fix that does not include an exploit.
- Residual risk and what was not reviewed.

Scan the diff locally with [scan_diff.py](scripts/scan_diff.py). Treat its hits as leads, then confirm them in the source.

## Procedure

### Phase Map trust boundaries

1. List new or changed entrypoints and what data crosses them.
2. Note where identity is established and where authorization is checked.
3. Run `python scripts/scan_diff.py` from this skill directory, pointing `--repo` at the target checkout.

### Phase Check the risky sinks

1. Queries built with string concatenation or formatters.
2. Shell, filesystem paths, outbound requests, HTML, and deserialization of untrusted bytes.
3. Authorization that is present on the old route but missing on the new one.
4. Secrets, tokens, or private keys in the diff or in files the diff adds.

### Phase Rank findings

1. Blocker: unauthenticated or wrongly authorized access, or a committed secret.
2. High: injection or unsafe deserialization on a reachable path.
3. Medium: defense missing but not obviously reachable. Note: hardening with no current path.
4. Every finding gets a file location and a fix stated as the control to add.

### Phase Limit the claim

1. Say which paths you did not review.
2. Do not mark the PR secure. Mark the reviewed diff as clear, blocked, or accepted-risk.

## Proof requirements

- Each finding cites a file and the missing or weak control.
- Scanner output is attached or summarized, including a clean run.
- The verdict names what was out of scope.

## Common failure patterns

- A rubber stamp because CI is green.
- Findings with no location.
- Turning the review into exploit steps.

## Adaptation notes

- Frontend-only diffs: focus on token storage, HTML sinks, and open redirects.
- Infrastructure diffs: focus on public exposure, IAM, and secrets in build logs.

## Example invocation

```text
Use security-review on the current branch versus main.

Attacker: authenticated user of another account.
Focus: the new invoice export route.

Return ranked findings and a merge recommendation.
```

## Handoff format

```text
Security Review Report

Status: success | partial | blocked | failed
Scope reviewed:
Trust boundaries:
Scanner result:
Findings:
Out of scope:
Verdict: clear | blocked | accepted-risk
Required fixes:
```

---
name: onboard-to-repo
description: "Produces a first-hour orientation of a repository: how it starts, how it is tested, and which entrypoints are real. Use when an agent or human is new to a repo and needs a map before editing."
license: Apache-2.0
compatibility: "Claude Code, Cursor, Codex, Grok Build, and GitHub Copilot. Needs git and a search tool such as rg."
allowed-tools: Bash Read Grep
metadata:
  category: repo-understanding
  status: experimental
  tags: "onboarding, repo-map, entrypoints"
  modes: "onboarding, pre-edit"
  version: "0.1.0"
  author: SlipstreamAI
---

# Onboard to Repo

**Tagline:** A first-hour map with unknowns labeled.

## Purpose

Onboard to Repo is the first hour, not the deep audit. It wraps the questions in map-the-system and find-the-real-entrypoints into one orientation page. Unknowns stay labeled unknown.

## Use when

1. You just cloned a repository and need to change it safely.
2. A session is about to edit code without a map of how to run or test it.
3. You need a short brief for the next agent.

## Do not use when

- A multi-day architecture study. Use map-the-system for the deeper pass.
- Hunting a specific bug. Use trace-the-failure.

## Inputs

- Repository root.
- The task you expect to do next, if known.
- Time box. Default to reading docs and entrypoints, not running a full suite, unless the suite is the documented check.

## Outputs

- How to install, run, and test, each marked verified or unverified.
- Real entrypoints versus scaffolds.
- Risk notes for the upcoming task.
- Pointers to map-the-system or find-the-real-entrypoints if the hour is not enough.

## Procedure

### Phase Read the front door

1. Read the README, contributing guide, and agent instructions if present.
2. Write down the documented install, run, and test commands.
3. Do not invent flags that the docs do not show.

### Phase Check the doors that actually open

1. Find process entrypoints: servers, CLIs, workers, scheduled jobs, and framework routes.
2. Separate tests, examples, and generated clients from those entrypoints.
3. If a documented command is cheap and safe, run it and record the result. If not, mark it unverified.

### Phase Point at the upcoming change

1. Given the next task, list the files and boundaries it likely touches.
2. Name the test command that should be run for that area.
3. Call blast-radius-scan if the task already has a diff.

### Phase Leave the page

1. One page. Every claim is verified or unverified.
2. List the next skill to run if the map is still too thin.

## Proof requirements

- Commands are copied from repo files or from a run you performed.
- Entrypoints cite a file.
- Unverified items are not written as facts.

## Common failure patterns

- A tour of every directory with no run or test command.
- Treating the example app as the production server.
- Filling gaps with guesses and no label.

## Adaptation notes

- Monorepos: orient to the package the task names, and note the workspace tool.
- Private or broken installs: document the blocker instead of skipping the run section.

## Example invocation

```text
Use onboard-to-repo.

Next task: change the invoice email sender.
Time box: first hour.

Return run, test, entrypoints, and unknowns.
```

## Handoff format

```text
Onboard to Repo Report

Status: success | partial | blocked | failed
Install:
Run:
Test:
Real entrypoints:
Scaffolds ignored:
Likely blast radius:
Unverified:
Next skill:
```

---
name: docs-from-code
description: "Updates README or API docs so the commands and interfaces match the code. Use when docs drift from flags, routes, or setup steps, or when a change needs docs that were verified by running them."
license: Apache-2.0
compatibility: "Claude Code, Cursor, Codex, Grok Build, and GitHub Copilot. Needs git and a search tool such as rg."
allowed-tools: Bash Read Grep
metadata:
  category: documentation
  status: experimental
  tags: "docs, readme, accuracy"
  modes: "pr-audit, documentation"
  version: "0.1.0"
  author: SlipstreamAI
---

# Docs from Code

**Tagline:** Document the command that actually runs.

## Purpose

Docs from Code refuses to invent flags. Every command in the doc is either run, or marked unverified. API descriptions cite the handler, type, or schema they came from.

## Use when

1. A README setup step fails or names a script that does not exist.
2. A PR changes a CLI flag, env var, or route and the docs still describe the old one.
3. You are writing docs for a surface you can inspect in the repo.

## Do not use when

- Marketing pages with no operational claims.
- Release notes. Use release-notes-and-changelog.

## Inputs

- The doc file and the code it claims to describe.
- Commands you are allowed to run.

## Outputs

- Doc edits.
- Commands run and their results.
- Sentences left unverified, with the reason.

## Procedure

### Phase Extract claims

1. List commands, flags, env vars, and routes the doc asserts.
2. Find the code or script that should implement each one.
3. A claim with no code counterpart is a doc bug, not a prompt to invent the feature.

### Phase Check the ones you can run

1. Run install, help, or example commands that are safe and local.
2. Record the exit and any mismatch.
3. If a command needs secrets or production, do not run it. Mark it unverified.

### Phase Edit to the evidence

1. Change the doc to the flag and path that exist.
2. Remove steps you cannot justify.
3. Keep the repo's heading structure.

### Phase Show the remainder

1. List claims you did not run.
2. Do not write 'verified' on the whole page if one command was not run.

## Proof requirements

- Each edited command cites a script, `--help` output, or a file path.
- Unverified sentences are listed.

## Common failure patterns

- Copying a command from memory.
- Documenting a flag because it would be nice.
- A green prose review with no command or file citation.

## Adaptation notes

- API references: generate from the schema if the repo already does, then diff the result.
- Monorepos: name the package directory in every command.

## Example invocation

```text
Use docs-from-code on README.md setup.

Check npm scripts against package.json and run npm test if dependencies are installed.

Return edits and unverified lines.
```

## Handoff format

```text
Docs from Code Report

Status: success | partial | blocked | failed
Doc:
Claims checked:
Commands run:
Edits:
Unverified:
Removed claims:
```

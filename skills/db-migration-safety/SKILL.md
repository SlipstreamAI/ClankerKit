---
name: db-migration-safety
description: "Reviews a database migration for lock risk, expand-contract safety, and a reversible or forward-fix plan. Use when a pull request adds SQL or a migration framework change that alters tables, indexes, or backfills."
license: Apache-2.0
compatibility: "Claude Code, Cursor, Codex, Grok Build, and GitHub Copilot. Needs git and a search tool such as rg."
allowed-tools: Bash Read Grep
metadata:
  category: hardening
  status: experimental
  tags: "database, migrations, safety"
  modes: "pre-merge, release"
  version: "0.1.0"
  author: SlipstreamAI
---

# DB Migration Safety

**Tagline:** Ship schema changes that can roll forward without locking the table shut.

## Purpose

DB Migration Safety keeps schema changes from taking a surprise lock or deleting data as a convenience. Expand and contract are separate. Backfills are separate from the lock-holding DDL when the table is large.

## Use when

1. A migration adds, drops, renames, or retypes a column or table.
2. An index is created on a hot table.
3. A backfill walks existing rows.

## Do not use when

- Query tuning with no schema change. Use performance-profile if you are measuring.
- Choosing a brand-new database product.

## Inputs

- The migration file and the framework.
- Approximate table size or an explicit unknown.
- How the app is deployed relative to the migration.

## Outputs

- Lock and rewrite risks.
- Expand versus contract ordering.
- Backfill plan.
- Rollback or forward-fix plan.

Use [lock and backfill notes](references/lock-and-backfill.md) before calling a migration safe.

## Procedure

### Phase Read the operation

1. Identify each DDL and DML statement.
2. Classify it: add nullable column, add constraint, create index, rewrite table, drop, or backfill.
3. Unknown table size stays unknown. Do not assume a table is small.

### Phase Order expand and contract

1. Expand first: new nullable structures the current app can ignore.
2. Deploy the app that writes both shapes before you enforce a new constraint or drop the old one.
3. Do not rename a column in one step if old and new app versions overlap.

### Phase Separate the backfill

1. Large backfills run in batches outside a single open transaction.
2. A NOT NULL constraint waits until the backfill is done.
3. Destructive deletes are a separate reviewed step, not a default in the same migration as an add.

### Phase Plan the undo

1. Prefer a forward fix when a rollback would lose data written in the new shape.
2. If a down migration exists, say what data it does not restore.
3. Call out indexes that should be created concurrently when the engine supports it and the framework allows it.

## Proof requirements

- Each statement has a lock or rewrite note, even if the note is unknown.
- The deploy order of app and migration is explicit.
- Destructive steps are called out rather than folded into a squash.

## Common failure patterns

- Adding a column with a default that rewrites a large table, unremarked.
- Dropping a column in the same release that stops writing it, while old instances still run.
- A down migration that claims reversibility after a destructive delete.

## Adaptation notes

- Postgres: mention concurrent index creation and validate-not-valid constraints when relevant.
- MySQL: call out online DDL limits instead of assuming Postgres behavior.
- SQLite or local dev databases: say the production engine may differ.

## Example invocation

```text
Use db-migration-safety on db/migrate/20261012_invoice_void.sql.

Table size: unknown.
Deploy: migration runs before rolling app restart.

Return lock risk, ordering, and undo plan.
```

## Handoff format

```text
DB Migration Safety Report

Status: success | partial | blocked | failed
Statements:
Lock or rewrite risk:
Expand/contract order:
Backfill:
Undo plan:
Unknowns:
Verdict: safe-to-ship | reorder | blocked
```

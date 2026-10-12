# Lock and backfill notes

Treat these as review prompts. Confirm them against the engine you actually run.

- Adding a nullable column without a default is usually safer than a default that rewrites rows.
- A new NOT NULL constraint needs existing rows filled first.
- Index builds can lock writes unless the engine has a concurrent option and the migration uses it.
- A table rewrite holds a stronger lock than a metadata-only change. If you do not know which you have, say unknown.
- Backfills belong in batches with a progress condition, not one unbounded transaction.
- Renames need a compatibility window if two app versions run together.
- Drops come last, after the old code is gone.

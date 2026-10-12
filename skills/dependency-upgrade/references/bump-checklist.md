# Bump checklist

- Current version recorded from the lockfile, not memory.
- Target version is a real release, not a branch name.
- Major bumps are isolated from other majors.
- Changelog scanned for removed APIs, default changes, and peer dependency shifts.
- Call sites of removed APIs searched in this repo.
- Lockfile diff reviewed for unexpected packages.
- Tests or build command recorded.
- Rollback is a revert, plus any data caveat.

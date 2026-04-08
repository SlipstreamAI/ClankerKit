# ClankerKit Consumption Guide

## Start small

Do not import every skill at once. Pick a narrow loop with frequent pain, then attach one skill that raises proof quality.

For a fast start, use [`quickstart-consumers.md`](/C:/DEV2/ClankerKit/docs/quickstart-consumers.md) and [`skills-index.md`](/C:/DEV2/ClankerKit/docs/skills-index.md).

Good starting choices:

- runtime-proof for claim validation
- map-the-system before first broad edits
- truthforge for skeptical PR governance

## Suggested rollout model

1. Baseline current behavior
   - record current merge misses, rollback frequency, and incident classes
2. Add one skill in advisory mode
   - keep outputs visible but non-blocking for one to two weeks
3. Promote to gated mode
   - block merge or promotion when verdict fails required standard
4. Track outcomes
   - compare defect escape and mean-time-to-trust before and after

## Integration points

- PR review comments
- pre-merge jobs
- incident triage flows
- release readiness checks
- operator handoff docs

## Local adaptation model

Keep a lightweight adapter file near your repo that defines:

- available environments
- prohibited tools
- sensitive surfaces
- required evidence class for critical changes

Do not modify core skills for local policy unless you plan to maintain a fork.

## Output handling

Treat skill output as structured evidence, not prose.

- archive reports in PR or incident artifacts
- track recurring open assumptions
- convert deferred remediation into explicit work items

## Anti-patterns

- treating green CI as enough for runtime-visible claims
- suppressing skill output because it is inconvenient
- forcing all changes through heavy governance
- running skills with missing inputs and not lowering confidence

## Success criteria

ClankerKit adoption is working when:

- merge decisions reference evidence class, not only test count
- unverified assumptions are explicit and tracked
- runtime incidents from synthetic confidence decrease
- teams trust agent outputs more because receipts are visible

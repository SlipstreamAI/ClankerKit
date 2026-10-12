## Summary

Describe what changed and why.

## Change type

- [ ] New skill
- [ ] Skill update
- [ ] Check or pattern update
- [ ] Docs only
- [ ] Tooling, site, or CI gate update

## Skill quality checklist

- [ ] Frontmatter matches the Agent Skills spec (`name`, `description` with `Use when`, string `allowed-tools`, custom fields under `metadata`)
- [ ] `name` matches `skills/<name>/`
- [ ] Required sections are present, including a text handoff
- [ ] Proof requirements name an artifact or an explicit gap
- [ ] Common failure patterns are concrete
- [ ] Adaptation notes are repo-agnostic
- [ ] `python scripts/validate_skills.py` passes
- [ ] `python scripts/build_skill_catalog.py` was run if skills or bundles changed

## Safety checklist

- [ ] No guidance for skipping authentication or safety controls
- [ ] No destructive default behavior
- [ ] No guidance for moving secrets off the host
- [ ] Escalation and stop boundaries are explicit
- [ ] New scripts were read with `skill-security-scan` or an equivalent pass

## Notes for reviewers

Add assumptions, edge cases, and any areas where confidence is lower. Status promotions need the real uses that justify them.

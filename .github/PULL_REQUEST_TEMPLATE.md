## Summary

Describe what changed and why.

## Change type

- [ ] New skill
- [ ] Skill update
- [ ] Check or pattern update
- [ ] Docs only
- [ ] Tooling or CI gate update

## Skill quality checklist

- [ ] Frontmatter is valid and complete
- [ ] Required sections are present
- [ ] Output contract is deterministic
- [ ] Proof requirements are explicit
- [ ] Common failure patterns are concrete
- [ ] Adaptation notes are repo-agnostic

## Safety checklist

- [ ] No auth-bypass or unsafe guidance
- [ ] No destructive default behavior
- [ ] No exfiltration guidance
- [ ] Escalation and stop boundaries are explicit

## Validation

- [ ] `python scripts/validate_skills.py`
- [ ] `python scripts/build_skill_catalog.py --check`

## Notes for reviewers

Add assumptions, edge cases, and any areas where confidence is lower.

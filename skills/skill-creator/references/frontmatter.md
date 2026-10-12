# Frontmatter rules

Required top-level keys:

- `name`: matches the directory, `^[a-z0-9]+(-[a-z0-9]+)*$`, at most 64 characters.
- `description`: at most 1024 characters. Say what it does and include `Use when`.
- `license`
- `compatibility`
- `allowed-tools`: space-separated string.
- `metadata`: map of strings. ClankerKit requires `category`, `status`, `tags`, `modes`, `version`, `author`.

Do not put category, status, or tags at the top level. Do not use YAML lists for tools or tags.

Status values: `experimental`, `provisional`, `stable`, `deprecated`.

Categories: `debugging`, `validation`, `governance`, `repo-understanding`, `delivery`, `hardening`, `documentation`.

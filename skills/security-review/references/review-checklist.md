# Security review checklist

Confirm or mark not-applicable. Do not treat a checked box as proof without a file reference.

- New entrypoint has an authorization check comparable to its neighbors.
- Object access is scoped to the caller's tenant or owner.
- Untrusted strings are bound as query parameters, not concatenated.
- File paths cannot escape the intended root.
- HTML and markdown rendering does not treat user text as markup.
- Outbound requests do not take an unrestricted URL from the caller.
- Deserialization uses a safe loader.
- Logs and error bodies omit secrets and session tokens.
- The diff adds no long-lived credential.

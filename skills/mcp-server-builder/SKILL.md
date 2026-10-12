---
name: mcp-server-builder
description: "Builds or changes an MCP server and proves a tool call against a local transport. Use when adding an MCP tool, resource, or prompt and you need a schema plus a real invocation receipt."
license: Apache-2.0
compatibility: "Claude Code, Cursor, Codex, Grok Build, and GitHub Copilot. Needs git and a search tool such as rg."
allowed-tools: Bash Read Grep
metadata:
  category: delivery
  status: experimental
  tags: "mcp, tools, agents"
  modes: "feature, integration"
  version: "0.1.0"
  author: SlipstreamAI
---

# MCP Server Builder

**Tagline:** Build an MCP server and prove one tool call.

## Purpose

MCP Server Builder ships a tool an agent can call. The receipt is a schema, a local start command, and one successful or intentionally failed tool call. Secrets stay in the environment.

## Use when

1. You are adding or changing an MCP server.
2. A tool's input schema drifted from the handler.
3. You need to show that a client can list tools and call one.

## Do not use when

- Wrapping an API you are not allowed to call.
- A general agent design with no server.

## Inputs

- The tools or resources to expose.
- Transport: stdio or HTTP.
- How a caller authenticates, if at all.

## Outputs

- Tool names and input schema.
- Start command.
- One tool-call transcript with secrets redacted.
- Auth story.

## Procedure

### Phase Define the tools

1. Name each tool with a verb and a bounded job.
2. Write an input schema that rejects missing required fields.
3. Describe side effects. Read-only tools should not write.

### Phase Implement the transport

1. Use the repo's MCP library if one is already chosen.
2. Read tokens and keys from the environment. Do not commit them.
3. Fail with a clear error when required config is missing.

### Phase Prove a call

1. Start the server locally.
2. List tools.
3. Call one tool with a fixture input and record the result, redacted.
4. Call it once with an invalid input and record the validation error.

### Phase Document the boundary

1. Say which tools were not invoked.
2. State the auth model: none, local user, or token.
3. If you could not start the server, the status is partial and there is no success claim.

## Proof requirements

- A transcript or command output for list and call.
- The schema file or code location is cited.
- No secret value appears in the handoff.

## Common failure patterns

- A README that shows a tool which the server does not register.
- A success claim from unit tests that mock the entire handler and skip schema validation.
- Committed connection strings.

## Adaptation notes

- Stdio servers: show the client command that spawned the process.
- HTTP servers: include the listen address you actually used, which should be local unless a sandbox says otherwise.

## Example invocation

```text
Use mcp-server-builder.

Tool: list_invoices, read-only, input customer_id.
Transport: stdio.

Return schema path, start command, and one call transcript.
```

## Handoff format

```text
MCP Server Builder Report

Status: success | partial | blocked | failed
Tools:
Schema:
Start command:
List result:
Call result:
Invalid input result:
Auth:
Not invoked:
```

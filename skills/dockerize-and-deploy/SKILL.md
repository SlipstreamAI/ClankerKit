---
name: dockerize-and-deploy
description: "Prepares a container build and deploy checklist with a smoke-test receipt. Use when adding a Dockerfile or shipping an image and you need build, run, and rollback evidence."
license: Apache-2.0
compatibility: "Claude Code, Cursor, Codex, Grok Build, and GitHub Copilot. Needs git and a search tool such as rg."
allowed-tools: Bash Read Grep
metadata:
  category: delivery
  status: experimental
  tags: "docker, deploy, smoke-test"
  modes: "release, delivery"
  version: "0.1.0"
  author: SlipstreamAI
---

# Dockerize and Deploy

**Tagline:** A container that builds, starts, and answers a smoke check.

## Purpose

Dockerize and Deploy treats an image as unproven until it builds and a smoke check hits a running process. The image should not contain secrets and should not need to run as root for a normal start.

## Use when

1. A service needs a Dockerfile or an image update.
2. A deploy change needs a local or preview smoke test.
3. You need a rollback note before promoting an image.

## Do not use when

- Cluster platform design.
- Deploying to production without the environment's approval gate.

## Inputs

- Dockerfile and build context.
- The command the process should serve.
- A smoke check: HTTP path, CLI command, or health endpoint.

## Outputs

- Build command and result.
- Run command and smoke result.
- Secret and user findings.
- Rollback: previous image or previous config.

## Procedure

### Phase Read the image

1. Find the Dockerfile, base image tag, and exposed port or entry command.
2. Confirm secrets are not copied from build args into layers that remain in the image.
3. Prefer a non-root user when the process can run as one. If it cannot, say why.

### Phase Build

1. Build with the repo's documented command.
2. Record the image id or tag.
3. If the build fails, stop and report the error. Do not call deploy ready.

### Phase Smoke

1. Run the container with the env it needs, using placeholders rather than production secrets.
2. Hit the health or smoke command.
3. Record the response. A container that only starts and exits is not a pass for a server.

### Phase Rollback

1. Name the previous image tag or the config revert.
2. Note migrations that a container rollback would not undo. Point at db-migration-safety if schema changed.

## Proof requirements

- Build and smoke commands are in the handoff with results.
- If Docker is unavailable, status is blocked or partial, not a imagined success.

## Common failure patterns

- A Dockerfile with no build attempt when Docker is available.
- Secrets baked into ENV from a local file.
- Health defined as the container process existing, for a server that should answer a request.

## Adaptation notes

- Multi-stage builds: confirm the runtime stage does not copy the toolchain or secret files.
- Jobs rather than servers: the smoke check is a successful dry run or `--help`, and you say it is not a full job execution.

## Example invocation

```text
Use dockerize-and-deploy.

Dockerfile: ./Dockerfile
Smoke: GET /health on port 8080.

Return build, smoke, and rollback.
```

## Handoff format

```text
Dockerize and Deploy Report

Status: success | partial | blocked | failed
Image:
Build command:
Build result:
Run command:
Smoke result:
User and secrets:
Rollback:
Schema caveat:
```

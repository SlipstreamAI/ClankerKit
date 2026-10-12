#!/usr/bin/env bash
# Collect a local evidence inventory for TruthForge. No network calls.
set -euo pipefail

if ! git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  echo "Not a git checkout. Inventory tests and logs manually." >&2
  exit 2
fi

echo "HEAD $(git rev-parse --short HEAD)"
echo
echo "## status"
git status --short
echo
echo "## diff stat"
if git rev-parse --verify HEAD >/dev/null 2>&1; then
  git diff --stat HEAD
else
  echo "(no HEAD commit)"
fi
echo
echo "## mock-heavy files"
git grep -n -I -E 'mock|stub|monkeypatch|MagicMock|unittest.mock' -- . ':!skills' || true
echo
echo "## candidate test files"
git ls-files | grep -E '(test_|_test\.|\.spec\.|\.test\.)' || true

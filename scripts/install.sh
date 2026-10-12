#!/usr/bin/env bash
# Copy ClankerKit skills into an agent skills directory.
# Usage: scripts/install.sh <skill-or-bundle> [--agent claude|cursor|codex|grok|copilot|all] [--dest DIR] [--user]
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TARGET="${1:-}"
if [[ $# -gt 0 ]]; then
  shift
fi

AGENT="all"
DEST=""
SCOPE="project"

usage() {
  cat <<'EOF'
Usage: scripts/install.sh <skill-or-bundle> [--agent claude|cursor|codex|grok|copilot|all] [--dest DIR] [--user]

Copies skill directories. Does not run remote scripts.
Agents:
  claude   Claude Code     project .claude/skills     user ~/.claude/skills
  cursor   Cursor          project .cursor/skills     user ~/.cursor/skills
  codex    Codex           project .agents/skills     user ~/.codex/skills
  grok     Grok Build      project .grok/skills       user ~/.grok/skills
  copilot  GitHub Copilot  project .github/skills     user ~/.copilot/skills
  all      every agent above
EOF
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --agent)
      AGENT="${2:-}"
      shift 2
      ;;
    --dest)
      DEST="${2:-}"
      shift 2
      ;;
    --user)
      SCOPE="user"
      shift
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      echo "Unknown argument: $1" >&2
      usage >&2
      exit 2
      ;;
  esac
done

if [[ -z "$TARGET" ]]; then
  usage >&2
  exit 2
fi

SKILL_NAMES=()
if [[ -f "$ROOT/bundles/$TARGET/bundle.json" ]]; then
  mapfile -t SKILL_NAMES < <(python3 - "$ROOT/bundles/$TARGET/bundle.json" "$ROOT/skills" <<'PY'
import json, sys
from pathlib import Path
bundle = json.loads(Path(sys.argv[1]).read_text())
skills = bundle["skills"]
root = Path(sys.argv[2])
if skills == "*" or skills == ["*"]:
    names = sorted(p.name for p in root.iterdir() if (p / "SKILL.md").is_file())
else:
    names = list(skills)
print("\n".join(names))
PY
)
elif [[ -f "$ROOT/skills/$TARGET/SKILL.md" ]]; then
  SKILL_NAMES=("$TARGET")
else
  echo "No skill or bundle named '$TARGET'." >&2
  exit 1
fi

agent_dir() {
  local agent="$1"
  local base="${DEST:-$PWD}"
  if [[ "$SCOPE" == "user" ]]; then
    base="$HOME"
  fi
  case "$agent" in
    claude) printf '%s/.claude/skills\n' "$base" ;;
    cursor) printf '%s/.cursor/skills\n' "$base" ;;
    codex) printf '%s/.agents/skills\n' "$base" ;;
    grok) printf '%s/.grok/skills\n' "$base" ;;
    copilot) printf '%s/.github/skills\n' "$base" ;;
    *)
      echo "Unknown agent: $agent" >&2
      exit 2
      ;;
  esac
}

AGENTS=()
if [[ "$AGENT" == "all" ]]; then
  AGENTS=(claude cursor codex grok copilot)
else
  AGENTS=("$AGENT")
fi

for agent in "${AGENTS[@]}"; do
  dest="$(agent_dir "$agent")"
  mkdir -p "$dest"
  for name in "${SKILL_NAMES[@]}"; do
    if [[ ! -f "$ROOT/skills/$name/SKILL.md" ]]; then
      echo "Missing skill directory: $name" >&2
      exit 1
    fi
    rm -rf "$dest/$name"
    cp -a "$ROOT/skills/$name" "$dest/$name"
    echo "installed $name -> $dest/$name"
  done
done

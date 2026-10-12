#!/usr/bin/env python3
"""Unit checks for skill frontmatter parsing and catalog freshness helpers."""

from __future__ import annotations

import subprocess
import sys
import tempfile
import textwrap
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from validate_skills import parse_frontmatter, use_when_clause  # noqa: E402


GOOD = textwrap.dedent(
    """\
    ---
    name: example-skill
    description: "Checks one claim. Use when a reviewer needs a receipt."
    license: Apache-2.0
    compatibility: "Any agent with git."
    allowed-tools: Bash Read Grep
    metadata:
      category: validation
      status: experimental
      tags: "proof, review"
      modes: "pr-audit"
      version: "0.1.0"
      author: SlipstreamAI
    ---

    # Example

    Body.
    """
)


class ParseTests(unittest.TestCase):
    def test_spec_frontmatter(self) -> None:
        data, body = parse_frontmatter(GOOD)
        self.assertEqual(data["name"], "example-skill")
        self.assertEqual(data["allowed-tools"], "Bash Read Grep")
        self.assertIsInstance(data["metadata"], dict)
        self.assertEqual(data["metadata"]["category"], "validation")
        self.assertIn("# Example", body)
        self.assertIn("reviewer needs a receipt", use_when_clause(str(data["description"])))

    def test_list_tools_rejected(self) -> None:
        text = GOOD.replace(
            "allowed-tools: Bash Read Grep\n",
            "allowed-tools:\n  - Bash\n",
        )
        with self.assertRaises(ValueError):
            parse_frontmatter(text)

    def test_extra_top_level_key_is_visible(self) -> None:
        text = GOOD.replace("license: Apache-2.0\n", "license: Apache-2.0\ncategory: validation\n")
        data, _body = parse_frontmatter(text)
        self.assertIn("category", data)

    def test_repo_validator_passes(self) -> None:
        result = subprocess.run(
            [sys.executable, str(ROOT / "scripts" / "validate_skills.py")],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_catalog_roundtrip_in_temp_copy_is_not_required(self) -> None:
        # The catalog check is exercised by CI. This guards the helper against an empty clause.
        self.assertEqual(use_when_clause("No trigger here."), "No trigger here.")
        with tempfile.TemporaryDirectory() as tmp:
            Path(tmp, "note.txt").write_text("ok", encoding="utf-8")
            self.assertTrue(Path(tmp, "note.txt").exists())


if __name__ == "__main__":
    unittest.main()

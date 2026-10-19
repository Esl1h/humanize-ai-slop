"""Regression tests for scripts/slop_scan.py on English text."""
from __future__ import annotations

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
import slop_scan  # noqa: E402


def kinds(text: str, severity: str | None = None) -> list[str]:
    return [
        f.kind
        for f in slop_scan.scan_text(text)
        if severity is None or f.severity == severity
    ]


class FlagsSlop(unittest.TestCase):
    def test_banned_word_inflections(self) -> None:
        self.assertEqual(kinds("We leveraged it, utilizing a streamlined flow."), ["banned"] * 3)

    def test_dashes(self) -> None:
        self.assertEqual(kinds("Fast \u2014 and cheap -- mostly."), ["dash", "dash"])

    def test_bold_label_list(self) -> None:
        self.assertIn("bold_label", kinds("- **Speed:** fast"))

    def test_title_case_heading(self) -> None:
        self.assertEqual(kinds("## Our Big New Launch Plan"), ["title_case"])

    def test_emoji_in_heading_and_list_is_fix(self) -> None:
        self.assertEqual(kinds("## \U0001F680 Launch\n- \u2705 done", "fix"), ["decoration"] * 2)

    def test_emoji_in_body_is_watch(self) -> None:
        self.assertEqual(kinds("We shipped it \U0001F680", "watch"), ["emoji"])

    def test_mixed_quotes_points_at_minority(self) -> None:
        findings = slop_scan.scan_text('a "b"\nc "d"\ne \u201Cf\u201D')
        self.assertEqual([(f.kind, f.line) for f in findings], [("mixed_quotes", 3)])

    def test_hyphen_stack(self) -> None:
        self.assertEqual(kinds("A user-facing, high-level, real-time API."), ["hyphen_stack"])

    def test_watch_phrases(self) -> None:
        self.assertEqual(
            kinds("Here's what nobody tells you. I hope this helps!", "watch"),
            ["phrase", "phrase"],
        )

    def test_binary_contrast(self) -> None:
        self.assertEqual(kinds("This isn't just an update. It's a reinvention."), ["contrast"])

    def test_horizontal_rule(self) -> None:
        self.assertEqual(kinds("One.\n\n---\n\nTwo."), ["rule"])


class LeavesHumanTextAlone(unittest.TestCase):
    def test_quoted_words(self) -> None:
        self.assertEqual(kinds('My boss says "leverage synergies" a lot.'), [])

    def test_code_frontmatter_and_urls(self) -> None:
        text = "---\ntitle: x\n---\n`leverage` [doc](https://x.com/a--b) https://y.com/c--d\n"
        self.assertEqual(kinds(text), [])

    def test_hyphenated_tokens_that_are_not_jargon(self) -> None:
        self.assertEqual(kinds("On 2026-10-19 GPT-4 sent an e-mail to a co-op."), [])

    def test_dialogue_dash(self) -> None:
        self.assertEqual(kinds("\u2014 I won't, she said."), [])

    def test_plain_negation(self) -> None:
        self.assertEqual(kinds("The bus is not late, but the train is."), [])

    def test_sentence_case_heading(self) -> None:
        self.assertEqual(kinds("## How the six options compare"), [])


if __name__ == "__main__":
    unittest.main()

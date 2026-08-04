from __future__ import annotations

import unittest

from scripts.check_profile import PROFILE, check_local


class ProfileTruthTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.profile = PROFILE.read_text(encoding="utf-8")

    def test_current_profile_passes(self) -> None:
        self.assertEqual(check_local(self.profile), [])

    def test_hidden_doi_does_not_replace_visible_link(self) -> None:
        changed = self.profile.replace(
            "https://doi.org/10.5281/zenodo.21659634",
            "https://example.com/not-the-paper)<!-- 10.5281/zenodo.21659634 -->",
            1,
        )
        self.assertTrue(check_local(changed))

    def test_retargeted_title_fails(self) -> None:
        changed = self.profile.replace("The Generative Horizon", "A Different Paper", 1)
        self.assertTrue(check_local(changed))

    def test_hidden_duplicate_doi_fails(self) -> None:
        changed = self.profile.replace(
            "## Upstream engineering",
            "<!-- 10.5281/zenodo.21659634 -->\n\n## Upstream engineering",
            1,
        )
        self.assertTrue(check_local(changed))

    def test_changed_tool_set_fails(self) -> None:
        changed = self.profile.replace(
            "https://github.com/hermes-labs-ai/agent-gorgon",
            "https://github.com/hermes-labs-ai/hermes-jailbench",
            1,
        )
        self.assertTrue(check_local(changed))


if __name__ == "__main__":
    unittest.main()

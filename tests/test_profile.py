from __future__ import annotations

import unittest

from scripts.check_profile import EXPECTED_DOIS, PROFILE, check_local, compare_site_dois


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

    def test_stale_displayed_version_fails(self) -> None:
        changed = self.profile.replace("lintlang 0.4.1", "lintlang 0.3.8", 1)
        self.assertTrue(check_local(changed))

    def test_stale_install_pin_fails(self) -> None:
        changed = self.profile.replace("hermes-rubric==1.1.0", "hermes-rubric==1.0.2", 1)
        self.assertTrue(check_local(changed))

    def test_duplicate_tool_row_fails(self) -> None:
        row = next(
            line
            for line in self.profile.splitlines()
            if "](https://github.com/hermes-labs-ai/lintlang)" in line
        )
        duplicate = row.replace("lintlang 0.4.1", "lintlang 0.3.8").replace(
            "lintlang==0.4.1", "lintlang==0.3.8"
        )
        changed = self.profile.replace(row, f"{row}\n{duplicate}", 1)

        self.assertIn(
            "https://github.com/hermes-labs-ai/lintlang appears 2 times; expected one row",
            check_local(changed),
        )

    def test_live_index_allows_additional_version_dois(self) -> None:
        self.assertEqual(compare_site_dois(EXPECTED_DOIS | {"10.5281/zenodo.99999999"}), [])

    def test_live_index_missing_profile_doi_fails(self) -> None:
        missing = set(EXPECTED_DOIS)
        missing.pop()
        self.assertTrue(compare_site_dois(missing))


if __name__ == "__main__":
    unittest.main()

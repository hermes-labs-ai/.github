from __future__ import annotations

import unittest
import urllib.error
from email.message import Message
from unittest.mock import patch

from scripts.check_profile import (
    EXPECTED_DOIS,
    PROFILE,
    check_local,
    check_pypi_currentness,
    compare_site_dois,
)


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
        changed = self.profile.replace("lintlang 0.5.3", "lintlang 0.4.1", 1)
        self.assertTrue(check_local(changed))

    def test_stale_install_pin_fails(self) -> None:
        changed = self.profile.replace("hermes-rubric==1.2.1", "hermes-rubric==1.0.2", 1)
        self.assertTrue(check_local(changed))

    def test_duplicate_tool_row_fails(self) -> None:
        row = next(
            line
            for line in self.profile.splitlines()
            if "](https://github.com/hermes-labs-ai/lintlang)" in line
        )
        duplicate = row.replace("lintlang 0.5.3", "lintlang 0.4.1").replace(
            "lintlang==0.5.3", "lintlang==0.4.1"
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


class PypiCurrentnessTests(unittest.TestCase):
    def setUp(self) -> None:
        self.pinned = {"https://github.com/hermes-labs-ai/lintlang": ("lintlang", "0.5.3")}

    def test_matching_version_passes(self) -> None:
        with patch("scripts.check_profile.pypi_latest_version", return_value="0.5.3"):
            errors, warnings = check_pypi_currentness(self.pinned)
        self.assertEqual(errors, [])
        self.assertEqual(warnings, [])

    def test_stale_pin_fails_closed(self) -> None:
        with patch("scripts.check_profile.pypi_latest_version", return_value="0.6.0"):
            errors, warnings = check_pypi_currentness(self.pinned)
        self.assertEqual(warnings, [])
        self.assertEqual(len(errors), 1)
        self.assertIn("lintlang==0.5.3", errors[0])
        self.assertIn("PyPI latest is 0.6.0", errors[0])

    def test_registry_5xx_is_a_warning_not_a_stale_pin_error(self) -> None:
        http_error = urllib.error.HTTPError(
            url="https://pypi.org/pypi/lintlang/json",
            code=503,
            msg="Service Unavailable",
            hdrs=Message(),
            fp=None,
        )
        with patch("scripts.check_profile.pypi_latest_version", side_effect=http_error):
            errors, warnings = check_pypi_currentness(self.pinned)
        self.assertEqual(errors, [])
        self.assertEqual(len(warnings), 1)
        self.assertIn("HTTP 503", warnings[0])

    def test_registry_404_is_a_warning_not_a_stale_pin_error(self) -> None:
        http_error = urllib.error.HTTPError(
            url="https://pypi.org/pypi/lintlang/json",
            code=404,
            msg="Not Found",
            hdrs=Message(),
            fp=None,
        )
        with patch("scripts.check_profile.pypi_latest_version", side_effect=http_error):
            errors, warnings = check_pypi_currentness(self.pinned)
        self.assertEqual(errors, [])
        self.assertEqual(len(warnings), 1)
        self.assertIn("not a confirmed stale pin", warnings[0])

    def test_network_failure_is_a_warning_not_a_stale_pin_error(self) -> None:
        with patch(
            "scripts.check_profile.pypi_latest_version",
            side_effect=urllib.error.URLError("temporary failure in name resolution"),
        ):
            errors, warnings = check_pypi_currentness(self.pinned)
        self.assertEqual(errors, [])
        self.assertEqual(len(warnings), 1)
        self.assertIn("temporarily unavailable", warnings[0])

    def test_malformed_registry_response_is_a_warning(self) -> None:
        with patch("scripts.check_profile.pypi_latest_version", side_effect=KeyError("info")):
            errors, warnings = check_pypi_currentness(self.pinned)
        self.assertEqual(errors, [])
        self.assertEqual(len(warnings), 1)

if __name__ == "__main__":
    unittest.main()

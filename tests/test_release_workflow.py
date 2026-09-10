"""Fixture tests for the exact-tag checkout contract in reusable-python-release.yml.

The shell steps are extracted from the workflow file and run against throwaway git
repositories. `checkout_commit` mirrors how actions/checkout (src/ref-helper.ts)
resolves its `ref` input: an unqualified name prefers a same-named branch over a tag.
"""

from __future__ import annotations

import os
import re
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path

WORKFLOW = Path(__file__).resolve().parents[1] / ".github" / "workflows" / "reusable-python-release.yml"
TAG = "v1.2.3"
# Keep fixture git independent of the developer's hooks, signing, and templates.
GIT_ENV = {**os.environ, "GIT_CONFIG_GLOBAL": os.devnull, "GIT_CONFIG_NOSYSTEM": "1"}


def build_steps() -> list[str]:
    lines = WORKFLOW.read_text(encoding="utf-8").splitlines()
    start = lines.index("  build:")
    end = lines.index("  publish:")
    steps: list[list[str]] = []
    for line in lines[start:end]:
        if line.startswith("      - "):
            steps.append([line])
        elif steps:
            steps[-1].append(line)
    return ["\n".join(step) for step in steps]


def step(name: str) -> str:
    for text in build_steps():
        if text.startswith(f"      - name: {name}\n"):
            return text
    raise AssertionError(f"workflow has no build step named {name!r}")


def run_block(step_text: str) -> str:
    lines = step_text.splitlines()
    begin = lines.index("        run: |") + 1
    return "\n".join(line[10:] for line in lines[begin:]) + "\n"


def checkout_ref() -> str:
    match = re.search(r"^          ref: (.+)$", step("Check out release tag"), re.MULTILINE)
    assert match, "checkout step has no ref"
    return match.group(1).replace("${{ inputs.release-tag }}", TAG)


def git(cwd: Path, *args: str) -> str:
    return subprocess.run(
        ["git", *args], cwd=cwd, env=GIT_ENV, check=True, capture_output=True, text=True
    ).stdout.strip()


def commit(repo: Path, message: str) -> str:
    git(repo, "commit", "--allow-empty", "-q", "-m", message)
    return git(repo, "rev-parse", "HEAD")


def checkout_commit(origin: Path, ref: str) -> str:
    if ref.startswith("refs/tags/"):
        return git(origin, "rev-parse", f"{ref}^{{commit}}")
    if not ref.startswith("refs/"):
        if git(origin, "branch", "--list", ref):
            return git(origin, "rev-parse", f"refs/heads/{ref}")
        return git(origin, "rev-parse", f"refs/tags/{ref}^{{commit}}")
    raise AssertionError(f"unexpected checkout ref {ref!r}")


class ReleaseTagContractTests(unittest.TestCase):
    def setUp(self) -> None:
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.origin = Path(tmp.name) / "origin"
        self.work = Path(tmp.name) / "work"
        self.origin.mkdir()
        git(self.origin, "init", "-q", "-b", "main")
        git(self.origin, "config", "user.email", "fixture@example.invalid")
        git(self.origin, "config", "user.name", "fixture")
        self.tagged = commit(self.origin, "release 1.2.3")
        self.later = commit(self.origin, "unreleased work")

    def require(self, release_tag: str, trigger_ref: str) -> subprocess.CompletedProcess[str]:
        script = run_block(step("Require the triggering release tag"))
        env = {**os.environ, "RELEASE_TAG": release_tag, "TRIGGER_REF": trigger_ref}
        return subprocess.run(["bash", "-eo", "pipefail", "-c", script], env=env, capture_output=True, text=True)

    def build_checkout(self, trigger_sha: str) -> tuple[str, subprocess.CompletedProcess[str]]:
        """Clone origin as the runner would, check out the workflow ref, run the verify step."""
        target = checkout_commit(self.origin, checkout_ref())
        git(self.origin.parent, "clone", "-q", str(self.origin), str(self.work))
        git(self.work, "checkout", "-q", "--detach", target)
        script = run_block(step("Verify exact release tag checkout"))
        env = {**GIT_ENV, "RELEASE_TAG": TAG, "TRIGGER_SHA": trigger_sha}
        result = subprocess.run(
            ["bash", "-eo", "pipefail", "-c", script], cwd=self.work, env=env, capture_output=True, text=True
        )
        return target, result

    def test_tag_push_builds_the_tagged_commit(self) -> None:
        git(self.origin, "tag", TAG, self.tagged)
        self.assertEqual(self.require(TAG, f"refs/tags/{TAG}").returncode, 0)
        target, result = self.build_checkout(self.tagged)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertEqual(target, self.tagged)

    def test_annotated_tag_object_sha_is_accepted(self) -> None:
        git(self.origin, "tag", "-a", TAG, "-m", TAG, self.tagged)
        tag_object = git(self.origin, "rev-parse", f"refs/tags/{TAG}")
        self.assertNotEqual(tag_object, self.tagged)
        for trigger_sha in (self.tagged, tag_object):
            with self.subTest(trigger_sha=trigger_sha):
                shutil.rmtree(self.work, ignore_errors=True)
                _, result = self.build_checkout(trigger_sha)
                self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_same_named_branch_cannot_replace_the_tag(self) -> None:
        git(self.origin, "tag", TAG, self.tagged)
        git(self.origin, "branch", TAG, self.later)
        target = checkout_commit(self.origin, checkout_ref())
        self.assertEqual(target, self.tagged, "checkout resolved to the same-named branch, not the tag")
        _, result = self.build_checkout(self.tagged)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_tag_moved_after_trigger_fails(self) -> None:
        git(self.origin, "tag", TAG, self.later)
        _, result = self.build_checkout(self.tagged)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("::error title=Release tag contract::", result.stdout)
        self.assertIn("moved after the trigger", result.stdout)

    def test_checkout_not_at_tag_fails(self) -> None:
        git(self.origin, "tag", TAG, self.tagged)
        git(self.origin.parent, "clone", "-q", str(self.origin), str(self.work))
        git(self.work, "checkout", "-q", "--detach", self.later)
        script = run_block(step("Verify exact release tag checkout"))
        env = {**GIT_ENV, "RELEASE_TAG": TAG, "TRIGGER_SHA": self.tagged}
        result = subprocess.run(["bash", "-eo", "pipefail", "-c", script], cwd=self.work, env=env, capture_output=True, text=True)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn(f"but {TAG} points to {self.tagged}", result.stdout)

    def test_non_tag_trigger_fails_before_checkout(self) -> None:
        cases = {
            "branch push": (TAG, "refs/heads/main"),
            "same-named branch": (TAG, f"refs/heads/{TAG}"),
            "different tag": (TAG, "refs/tags/v1.2.4"),
            "branch name as tag": ("main", "refs/heads/main"),
            "unsafe tag text": (f"{TAG};true", f"refs/tags/{TAG};true"),
            "empty tag": ("", "refs/tags/"),
        }
        for label, (release_tag, trigger_ref) in cases.items():
            with self.subTest(label):
                result = self.require(release_tag, trigger_ref)
                self.assertNotEqual(result.returncode, 0)
                self.assertIn("::error title=Release tag contract::", result.stdout)

    def test_contract_steps_wire_the_trigger_context_and_precede_the_build(self) -> None:
        names = [re.match(r"      - name: (.+)", s).group(1) for s in build_steps()]
        self.assertEqual(
            names[:4],
            [
                "Require the triggering release tag",
                "Check out release tag",
                "Verify exact release tag checkout",
                "Set up Python",
            ],
        )
        self.assertIn("TRIGGER_REF: ${{ github.ref }}", step("Require the triggering release tag"))
        self.assertIn("TRIGGER_SHA: ${{ github.sha }}", step("Verify exact release tag checkout"))
        self.assertIn("persist-credentials: false", step("Check out release tag"))
        self.assertTrue(checkout_ref().startswith("refs/tags/"))


if __name__ == "__main__":
    unittest.main()

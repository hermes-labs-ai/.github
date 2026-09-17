#!/usr/bin/env python3
"""Check that the public organization profile preserves its proof spine."""

from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROFILE = ROOT / "profile" / "README.md"
RESEARCH_URL = "https://hermes-labs.ai/research"
CATALOG_URL = "https://hermes-labs.ai/open-source"
PYPI_URL_TEMPLATE = "https://pypi.org/pypi/{package}/json"

EXPECTED_PAPERS = [
    (
        "Tool Differentia: Relational Static Analysis for AI Agent Tool Descriptions",
        "10.5281/zenodo.21817243",
    ),
    (
        "Behavioral Canarying for Prompt Injection: Powerless Model Probes with Explicit Coverage Semantics",
        "10.5281/zenodo.21818564",
    ),
    ("The Generative Horizon", "10.5281/zenodo.21659634"),
    ("Precise Records, Unstable Meanings", "10.5281/zenodo.21652317"),
    ("A Taxonomy of Epistemic Failure Modes in Large Language Models", "10.5281/zenodo.19042469"),
    ("The Asymmetric Burden of Proof", "10.5281/zenodo.18867694"),
]
EXPECTED_DOIS = {doi for _, doi in EXPECTED_PAPERS}
DOI_PATTERN = re.compile(r"10\.5281/zenodo\.\d+")
PAPER_LINK_PATTERN = re.compile(
    r"^- \*\*\[(?P<title>[^]]+)\]\(https://doi\.org/(?P<doi>10\.5281/zenodo\.\d+)\)\.\*\*",
    re.MULTILINE,
)


def section(markdown: str, heading: str) -> str:
    pattern = re.compile(
        rf"^## {re.escape(heading)}\s*$\n(?P<body>.*?)(?=^## |\Z)",
        re.MULTILINE | re.DOTALL,
    )
    match = pattern.search(markdown)
    if not match:
        raise ValueError(f"missing section: {heading}")
    return match.group("body")


def check_local(markdown: str) -> list[str]:
    errors: list[str] = []
    try:
        research = section(markdown, "Research behind the engineering")
        tools = section(markdown, "Open-source reliability tools")
    except ValueError as exc:
        return [str(exc)]

    papers = [(match["title"], match["doi"]) for match in PAPER_LINK_PATTERN.finditer(research)]
    if papers != EXPECTED_PAPERS:
        errors.append(
            f"visible research links differ: expected {EXPECTED_PAPERS}, got {papers}"
        )

    for doi in EXPECTED_DOIS:
        count = research.count(doi)
        if count != 1:
            errors.append(f"research DOI {doi} appears {count} times; expected once")

    badge = "[![Research](https://img.shields.io/badge/research-six%20papers-1682D4)]"
    if f"{badge}({RESEARCH_URL})" not in markdown:
        errors.append("research badge does not describe and link to the six-paper index")

    front_matter = markdown.split("## What we do", maxsplit=1)[0]
    catalog_cta = f"**[Browse the open-source catalog]({CATALOG_URL})**"
    if catalog_cta not in front_matter:
        errors.append("front matter does not provide the canonical open-source catalog CTA")

    return errors


def site_dois() -> set[str]:
    request = urllib.request.Request(RESEARCH_URL, headers={"User-Agent": "hermes-profile-check/1"})
    with urllib.request.urlopen(request, timeout=15) as response:
        body = response.read().decode("utf-8")
    return set(DOI_PATTERN.findall(body))


def compare_site_dois(live_dois: set[str]) -> list[str]:
    """Require every profile paper on the live index, allowing extra versions."""
    missing = EXPECTED_DOIS - live_dois
    if not missing:
        return []
    return [
        "live research DOI set is missing profile links: "
        f"{sorted(missing)}"
    ]


def pypi_latest_version(package: str, timeout: int = 15) -> str:
    request = urllib.request.Request(
        PYPI_URL_TEMPLATE.format(package=package),
        headers={"User-Agent": "hermes-profile-check/1"},
    )
    with urllib.request.urlopen(request, timeout=timeout) as response:
        body = json.loads(response.read().decode("utf-8"))
    return body["info"]["version"]


def check_pypi_currentness(
    pinned: dict[str, tuple[str, str]],
) -> tuple[list[str], list[str]]:
    """Compare each pinned package/version against the live PyPI release.

    Returns (errors, warnings). A confirmed version mismatch is an error
    (fail closed: the profile is stale and must be corrected). A registry or
    network failure is a warning, not an error, since it means currentness
    could not be verified this run rather than that a pin is confirmed stale.
    """
    errors: list[str] = []
    warnings: list[str] = []
    for tool_url, (package, version) in sorted(pinned.items()):
        try:
            latest = pypi_latest_version(package)
        except urllib.error.HTTPError as exc:
            message = f"{package}: PyPI registry returned HTTP {exc.code}"
            if 500 <= exc.code < 600:
                warnings.append(message)
            else:
                warnings.append(f"{message} (registry lookup failed, not a confirmed stale pin)")
        except (OSError, UnicodeError, urllib.error.URLError, TimeoutError) as exc:
            warnings.append(f"{package}: PyPI registry temporarily unavailable: {exc}")
        except (KeyError, ValueError) as exc:
            warnings.append(f"{package}: unexpected PyPI response, could not read version: {exc}")
        else:
            if latest != version:
                errors.append(
                    f"{tool_url} pins {package}=={version} but PyPI latest is {latest}"
                )
    return errors, warnings


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--compare-site",
        action="store_true",
        help="also compare the profile DOI set with the live Hermes research index",
    )
    parser.add_argument(
        "--check-pypi-currentness",
        action="store_true",
        help="also compare explicitly supplied pinned tool versions with the live PyPI registry",
    )
    args = parser.parse_args()

    markdown = PROFILE.read_text(encoding="utf-8")
    errors = check_local(markdown)
    warnings: list[str] = []
    if args.compare_site:
        try:
            live_dois = site_dois()
        except urllib.error.HTTPError as exc:
            message = f"live research index returned HTTP {exc.code}"
            if 500 <= exc.code < 600:
                warnings.append(message)
            else:
                errors.append(message)
        except (OSError, UnicodeError, urllib.error.URLError) as exc:
            warnings.append(f"live research index temporarily unavailable: {exc}")
        else:
            errors.extend(compare_site_dois(live_dois))

    if args.check_pypi_currentness:
        warnings.append("no pinned package versions are maintained in the organization profile")

    if errors:
        for error in errors:
            print(f"FAIL: {error}", file=sys.stderr)
        return 1

    for warning in warnings:
        print(f"WARN: {warning}", file=sys.stderr)

    modes = ["local"]
    if args.compare_site:
        modes.append("live research index")
    if args.check_pypi_currentness:
        modes.append("live PyPI currentness")
    print(f"PASS: organization profile proof spine ({' + '.join(modes)})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Check that the public organization profile preserves its proof spine."""

from __future__ import annotations

import argparse
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROFILE = ROOT / "profile" / "README.md"
RESEARCH_URL = "https://hermes-labs.ai/research"

EXPECTED_PAPERS = [
    ("The Generative Horizon", "10.5281/zenodo.21659634"),
    ("Precise Records, Unstable Meanings", "10.5281/zenodo.21652317"),
    ("A Taxonomy of Epistemic Failure Modes in Large Language Models", "10.5281/zenodo.19042469"),
    ("The Asymmetric Burden of Proof", "10.5281/zenodo.18867694"),
]
EXPECTED_DOIS = {doi for _, doi in EXPECTED_PAPERS}
EXPECTED_TOOLS = {
    "https://github.com/hermes-labs-ai/lintlang",
    "https://github.com/hermes-labs-ai/little-canary",
    "https://github.com/hermes-labs-ai/hermeneutic",
    "https://github.com/hermes-labs-ai/agent-gorgon",
}
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

    tool_urls = set(re.findall(r"https://github\.com/hermes-labs-ai/[a-z0-9-]+", tools))
    if tool_urls != EXPECTED_TOOLS:
        errors.append(
            "open-source tool set differs: "
            f"expected {sorted(EXPECTED_TOOLS)}, got {sorted(tool_urls)}"
        )

    badge = "[![Research](https://img.shields.io/badge/research-four%20papers-1682D4)]"
    if f"{badge}({RESEARCH_URL})" not in markdown:
        errors.append("research badge does not describe and link to the four-paper index")

    return errors


def site_dois() -> set[str]:
    request = urllib.request.Request(RESEARCH_URL, headers={"User-Agent": "hermes-profile-check/1"})
    with urllib.request.urlopen(request, timeout=15) as response:
        body = response.read().decode("utf-8")
    return set(DOI_PATTERN.findall(body))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--compare-site",
        action="store_true",
        help="also compare the profile DOI set with the live Hermes research index",
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
            if live_dois != EXPECTED_DOIS:
                errors.append(
                    "live research DOI set differs: "
                    f"expected {sorted(EXPECTED_DOIS)}, got {sorted(live_dois)}"
                )

    if errors:
        for error in errors:
            print(f"FAIL: {error}", file=sys.stderr)
        return 1

    for warning in warnings:
        print(f"WARN: {warning}", file=sys.stderr)

    mode = "local + live research index" if args.compare_site else "local"
    print(f"PASS: organization profile proof spine ({mode})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

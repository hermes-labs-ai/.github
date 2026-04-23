# Hermes Labs

**AI assurance infrastructure for high-stakes systems.**

Technical audit, runtime assurance, signed evidence, and EU AI Act / ISO 42001 / NIST AI RMF readiness for enterprise AI teams shipping agentic and decision-support systems.

[![Site](https://img.shields.io/badge/hermes--labs.ai-visit-4F46E5)](https://hermes-labs.ai)
[![Research](https://img.shields.io/badge/Zenodo-papers-1682D4)](https://doi.org/10.5281/zenodo.18867694)
[![Substack](https://img.shields.io/badge/Substack-LPCI-FF6719?logo=substack&logoColor=white)](https://lpci.substack.com)

---

## What Hermes is

An independent research lab building the audit, runtime, and evidence layer for AI systems that can't afford to fail silently. We study how language models fail structurally — sycophancy, null-result bias, hermeneutic drift, intent exceptionalism — then ship tools and audits that surface those failures before production does.

## Engagement tracks

- **AI Assurance Audit** — pre-deployment prompt, tool, and scaffold audit; adversarial testing; written findings with prioritized fixes
- **Runtime Assurance & Evidence** — input-side prompt-injection sensing, runtime policy enforcement, signed receipts and transcript evidence
- **AI Compliance & Audit Readiness** — technical readiness scoring and evidence packaging mapped across EU AI Act (Annex IV), ISO/IEC 42001, and NIST AI RMF

[Start a conversation →](https://hermes-labs.ai/#contact)

---

## Research

- **[The Asymmetric Burden of Proof](https://doi.org/10.5281/zenodo.18867694)** — 14-page report. LLMs systematically discount negative findings across matched scientific vignettes. 19.6–56.7pp probability gaps across 3 models, directionally consistent in 23 of 24 conditions.
- **[A Taxonomy of Epistemic Failure Modes in LLMs](https://doi.org/10.5281/zenodo.19042469)** — Seven structural failure modes: null-result asymmetry, source-status credibility bias, agency dissolution, performative hedging, constraint evasion, silent instruction relaxation, controversy-truth conflation.

1,500+ controlled adversarial evaluations. 5 US patent filings — 1 non-provisional pending, 4 provisional (Little Canary, Signal Fingerprint, QuickThink, Scaffold Independence).

---

## Open-source contributions

26 PRs merged upstream. Four land in AI frameworks themselves:

| Repo | PR | Fix |
|---|---|---|
| [langchain-ai/langchain](https://github.com/langchain-ai/langchain/pull/35544) | #35544 | Drop forced `tool_choice` when extended thinking is on |
| [microsoft/semantic-kernel](https://github.com/microsoft/semantic-kernel/pull/13610) | #13610 | Fix truncation reducer silently deleting system prompts |
| [pytorch/ignite](https://github.com/pytorch/ignite/pull/3591) | #3591 | Typing modernization in `tqdm_logger` |
| [optuna/optuna](https://github.com/optuna/optuna/pull/6478) | #6478 | Simplify `Union` under `TYPE_CHECKING` |

The other 22 ship with production AI stacks: React Router, Nuxt, Cloudflare Workers, Sentry, Meta jscodeshift, MobX, ngrx, Microsoft TSDoc/Griffel, and more.

---

## Tools

| Tool | What it does | Install |
|---|---|---|
| [**lintlang**](./lintlang) | Static linter for AI agent configs, tool descriptions, and system prompts. Zero LLM calls. | `pip install lintlang` |
| [**little-canary**](./little-canary) | Input-side prompt injection detection via sacrificial canary-model probes. | `pip install little-canary` |
| [**zer0dex**](./zer0dex) | Dual-layer memory for AI agents — compressed index plus vector retrieval. | `pip install zer0dex` |
| [**claude-router**](./claude-router) | Routes prompts to the right Claude tier via local embeddings. | `pip install claude-router` |
| [**suy-sideguy**](./suy-sideguy) | Runtime policy guard for autonomous AI agents. | `pip install suy-sideguy` |
| [**agent-convergence-scorer**](./agent-convergence-scorer) | Score how similar N agent outputs are. | `pip install agent-convergence-scorer` |
| [**hermes-jailbench**](./hermes-jailbench) | Jailbreak regression benchmark for LLM endpoints. | `pip install hermes-jailbench` |
| [**repo-audit**](./repo-audit) | 15-second launch-readiness punch-list for any public GitHub repo. | `pip install repo-audit` |
| [**rule-audit**](./rule-audit) | Static prompt audit CLI for LLM system prompts. | `pip install rule-audit` |
| [**colony-probe**](./colony-probe) | Defensive prompt-confidentiality audit. | `pip install colony-probe` |
| [**quick-gate-js**](./quick-gate-js) / [**quick-gate-python**](./quick-gate-python) | CI quality gate with bounded auto-repair. | `npm i quick-gate` · `pip install quick-gate-python` |
| [**csv-quality-gate**](./csv-quality-gate) | CSV preflight validation for pipeline inputs. | `pip install csv-quality-gate` |
| [**intent-verify**](./intent-verify) | Repo intent verification and spec drift checks. | `pip install intent-verify` |
| [**forgetted**](./forgetted) | Mid-conversation incognito mode for AI agents. | `pip install forgetted` |
| [**zer0lint**](./zer0lint) | Memory extraction diagnostics for `mem0` configs. | `pip install zer0lint` |

---

*Founded by [Rolando Bosch](https://www.linkedin.com/in/rolando-bosch/) · [rbosch@lpci.ai](mailto:rbosch@lpci.ai) · [hermes-labs.ai](https://hermes-labs.ai)*

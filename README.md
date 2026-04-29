# Hermes Labs

**Epistemic engineering for production AI.**

Reliability infrastructure, evals, audits, and open-source tools for teams shipping LLM applications and agents. EU AI Act, ISO/IEC 42001, and NIST AI RMF readiness across the stack.

[![Site](https://img.shields.io/badge/hermes--labs.ai-visit-4F46E5)](https://hermes-labs.ai)
[![Research](https://img.shields.io/badge/Zenodo-papers-1682D4)](https://doi.org/10.5281/zenodo.18867694)
[![Substack](https://img.shields.io/badge/Substack-rolibosch-FF6719?logo=substack&logoColor=white)](https://rolibosch.substack.com)

---

## What Hermes is

An independent research lab building the audit, runtime, and evidence layer for AI systems that can't afford to fail silently. We study how language models fail structurally (sycophancy, null-result bias, hermeneutic drift, intent exceptionalism), then ship tools and audits that surface those failures before production does.

## Engagement tracks

- **AI Assurance Audit** — pre-deployment prompt, tool, and scaffold audit; adversarial testing; written findings with prioritized fixes
- **Runtime Assurance & Evidence** — input-side prompt-injection sensing, runtime policy enforcement, signed receipts and transcript evidence
- **AI Compliance & Audit Readiness** — technical readiness scoring and evidence packaging mapped across EU AI Act (Annex IV), ISO/IEC 42001, and NIST AI RMF

[Start a conversation →](https://hermes-labs.ai/#contact)

---

## Research

- **[The Asymmetric Burden of Proof](https://doi.org/10.5281/zenodo.18867694).** 14-page report. LLMs systematically discount negative findings across matched scientific vignettes. 19.6 to 56.7pp probability gaps across 3 models, directionally consistent in 23 of 24 conditions.
- **[A Taxonomy of Epistemic Failure Modes in LLMs](https://doi.org/10.5281/zenodo.19042469).** Seven structural failure modes: null-result asymmetry, source-status credibility bias, agency dissolution, performative hedging, constraint evasion, silent instruction relaxation, controversy-truth conflation.

1,500+ controlled adversarial evaluations. 5 US patent filings (1 non-provisional pending, 4 provisional).

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

## Reliability stack (flagships)

The current set, all open-source, all installable in seconds.

| Tool | What it does | Install |
|---|---|---|
| [**hermes-rubric**](./hermes-rubric) | Evidence-first structured scoring. Synthesize rubric, collect citations, hedge on thin evidence. Cross-model Cohen's κ = 0.629. | `pip install hermes-rubric` |
| [**fidelis**](./fidelis) | Zero-LLM agent memory. 73.0% end-to-end QA on LongMemEval-S, $0/query, fully local. | `pip install fidelis` |
| [**hermes-blind**](./hermes-blind) | Context-compensation scaffold for LLM evaluation prompts. Disclose, gate on evidence, hedge on thin. | `pip install hermes-blind` |
| [**hermeneutic**](./hermeneutic) | Mine corrections from chat logs; gate the next response before drift ships. | `pip install hermeneutic` |
| [**hermes-prime**](./hermes-prime) | Bootstrap a fresh Claude Code session with conventions and grounding triggers already loaded. Stop re-deriving the same rules at minute 30. | `pip install hermes-prime` |
| [**hermes-ctl**](./hermes-ctl) | Single-pane-of-glass CLI for the reliability stack. | `pip install hermes-ctl` |
| [**repo-readiness**](./repo-readiness) | 15-second launch-readiness audit for GitHub repos. 9 signals, source-backed. | `pip install repo-readiness` |

## Adjacent tools

| Tool | What it does | Install |
|---|---|---|
| [**lintlang**](./lintlang) | Static linter for AI agent configs, tool descriptions, system prompts. Zero LLM calls. | `pip install lintlang` |
| [**little-canary**](./little-canary) | Input-side prompt injection detection via sacrificial canary-model probes. | `pip install little-canary` |
| [**claude-router**](./claude-router) | Routes prompts to the right Claude tier via local embeddings. | `pip install claude-router` |
| [**langquant**](./langquant) | Stateless LLM coherence via refreshing language scaffold (LPCI). | `pip install langquant` |
| [**quickthink**](./quickthink) | Local-first inference control layer for small LLMs. | `pip install quickthink` |
| [**agent-gorgon**](./agent-gorgon) | Stop AI agents from fabricating tool output when a registered tool exists. | `pip install agent-gorgon` |
| [**suy-sideguy**](./suy-sideguy) | Runtime policy guard for autonomous AI agents. | `pip install suy-sideguy` |
| [**zer0dex**](./zer0dex) | Dual-layer memory for AI agents (compressed index plus vector retrieval). | `pip install zer0dex` |
| [**agent-convergence-scorer**](./agent-convergence-scorer) | Score how similar N agent outputs are. | `pip install agent-convergence-scorer` |
| [**hermes-jailbench**](./hermes-jailbench) | Jailbreak regression benchmark for LLM endpoints. | `pip install hermes-jailbench` |
| [**rule-audit**](./rule-audit) | Static prompt audit CLI for LLM system prompts. | `pip install rule-audit` |
| [**colony-probe**](./colony-probe) | Defensive prompt-confidentiality audit. | `pip install colony-probe` |
| [**quick-gate-js**](./quick-gate-js) / [**quick-gate-python**](./quick-gate-python) | CI quality gate with bounded auto-repair. | `npm i quick-gate` · `pip install quick-gate-python` |
| [**csv-quality-gate**](./csv-quality-gate) | CSV preflight validation for pipeline inputs. | `pip install csv-quality-gate` |
| [**intent-verify**](./intent-verify) | Repo intent verification and spec drift checks. | `pip install intent-verify` |
| [**forgetted**](./forgetted) | Mid-conversation incognito mode for AI agents. | `pip install forgetted` |
| [**zer0lint**](./zer0lint) | Memory extraction diagnostics for `mem0` configs. | `pip install zer0lint` |
| [**scaffold-lint**](./scaffold-lint) | Static linter for LLM prompt scaffolds. | `pip install scaffold-lint` |

---

*Founded by Roli Bosch ([Rolando Bosch](https://www.linkedin.com/in/rolando-bosch/) on LinkedIn / academic publications). [rbosch@lpci.ai](mailto:rbosch@lpci.ai) · [hermes-labs.ai](https://hermes-labs.ai)*

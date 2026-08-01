# Hermes Labs

**AI reliability engineering for production agents and LLM applications.**

We find the silent failures standard evaluations miss—dropped instructions, fabricated tool results, distorted memory, and actions no one can reconstruct—then engineer them out in the stack where they occur.

[![Site](https://img.shields.io/badge/hermes--labs.ai-visit-4F46E5)](https://hermes-labs.ai)
[![Research](https://img.shields.io/badge/research-four%20papers-1682D4)](https://hermes-labs.ai/research)
[![Substack](https://img.shields.io/badge/Substack-rolibosch-FF6719?logo=substack&logoColor=white)](https://rolibosch.substack.com)

---

## What we do

Hermes Labs is an AI reliability engineering studio for product and engineering teams shipping systems whose instructions, tools, memory, and evidence must remain reliable under real use.

## How we help

- **Diagnose.** We review prompts, tools, scaffolds, configs, memory, and traces against known failure modes, run controlled adversarial probes, and deliver prioritized findings with fixes.
- **Harden.** We design and integrate runtime controls, anti-fabrication guards, context-integrity protections, and offline-verifiable evidence in your existing stack.

[Bring us a system and a symptom →](https://hermes-labs.ai/#contact)

---

## Research

The four public papers have distinct evidence roles; they do not share one
dataset or validate one another. Read the [research index](https://hermes-labs.ai/research)
for abstracts, hosted copies, and citation exports.

- **[The Generative Horizon](https://doi.org/10.5281/zenodo.21659634).** A conceptual paper on model self-report, recursive interpretive conditioning, and the boundary between measured representations and claims about inner states.
- **[Precise Records, Unstable Meanings](https://doi.org/10.5281/zenodo.21652317).** A measurement-validity audit of claims derived from AI agent telemetry.
- **[A Taxonomy of Epistemic Failure Modes in Large Language Models](https://doi.org/10.5281/zenodo.19042469).** A taxonomy of seven structural epistemic failure modes.
- **[The Asymmetric Burden of Proof](https://doi.org/10.5281/zenodo.18867694).** A matched-vignette study of null-result asymmetry.

---

## Open-source contributions

26 contributions merged upstream. Two remove runtime reliability failures in agent frameworks; the others improve AI, ML, and web tooling:

| Repo | PR | Fix |
|---|---|---|
| [langchain-ai/langchain](https://github.com/langchain-ai/langchain/pull/35544) | #35544 | Drop forced `tool_choice` when extended thinking is on |
| [microsoft/semantic-kernel](https://github.com/microsoft/semantic-kernel/pull/13610) | #13610 | Fix truncation reducer silently deleting system prompts |
| [pytorch/ignite](https://github.com/pytorch/ignite/pull/3591) | #3591 | Typing modernization in `tqdm_logger` |
| [optuna/optuna](https://github.com/optuna/optuna/pull/6478) | #6478 | Simplify `Union` under `TYPE_CHECKING` |

The remaining 22 ship across React Router, Nuxt, Cloudflare Workers, Sentry, Meta jscodeshift, MobX, ngrx, Microsoft TSDoc/Griffel, and more.

---

## Flagship software

Start here. These are free, open-source tools with reverified install and use
paths. They make our methods inspectable and give teams useful building blocks;
Hermes Labs engagements apply, integrate, and harden those methods in a
production system.

| Tool | What it does | Install |
|---|---|---|
| [**lintlang 0.3.1**](https://github.com/hermes-labs-ai/lintlang) | Static analysis for AI agent configs, tool descriptions, and system prompts. Zero LLM calls. | `pip install lintlang==0.3.1` |
| [**little-canary 0.3.3**](https://github.com/hermes-labs-ai/little-canary) | Input-side prompt-injection detection via sacrificial canary-model probes. | `pip install little-canary==0.3.3` |
| [**hermeneutic 0.1.7**](https://github.com/hermes-labs-ai/hermeneutic) | Mine correction triples from chat logs; gate the next response before the same drift ships twice. | `pip install hermeneutic==0.1.7` |
| [**agent-gorgon 0.1.6**](https://github.com/hermes-labs-ai/agent-gorgon) | Runtime policy guard for autonomous agents, with deterministic decisions and forensic evidence. | `pip install agent-gorgon==0.1.6` |

## More from our stack

We keep additional reference implementations and research concepts public so
others can inspect, fork, or develop them. Public does not mean flagship or
production-ready; browse the [full GitHub catalog](https://github.com/hermes-labs-ai)
for each repository's own status and limits.

---

*Founded by Roli Bosch ([Rolando Bosch](https://www.linkedin.com/in/rolando-bosch/) on LinkedIn / academic publications). [roli@hermes-labs.ai](mailto:roli@hermes-labs.ai) · [hermes-labs.ai](https://hermes-labs.ai)*

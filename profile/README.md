# Hermes Labs

**AI reliability engineering for production agents and LLM applications.**

AI systems can pass conventional evaluations and still fail in real use. Instructions get dropped. Tools appear to succeed when they did not. Retrieved context changes meaning. Memory drifts. Policies weaken across long workflows. Evidence no longer explains why an action happened.

Hermes Labs finds these silent failures and engineers them out in the layer where they occur: prompts, tool interfaces, retrieval, memory, policies, runtime controls, and evidence.

[![Site](https://img.shields.io/badge/hermes--labs.ai-visit-4F46E5)](https://hermes-labs.ai)
[![Research](https://img.shields.io/badge/research-six%20papers-1682D4)](https://hermes-labs.ai/research)
[![Open source](https://img.shields.io/badge/open%20source-catalog-0F766E)](https://hermes-labs.ai/open-source)
[![Writing](https://img.shields.io/badge/writing-Substack-FF6719?logo=substack&logoColor=white)](https://hermeslabs.substack.com)

---

## What we do

Hermes Labs is an AI reliability engineering studio for product and engineering teams shipping agents and LLM applications whose behavior must remain dependable, inspectable, and reconstructable under real use.

- **Diagnose.** We review prompts, tools, scaffolds, configurations, memory, retrieval, and traces; run controlled adversarial probes; and deliver prioritized findings with reproducible failure cases and concrete fixes.
- **Harden.** We design and integrate runtime controls, anti-fabrication safeguards, context-integrity protections, policy gates, and offline-verifiable evidence inside the stack you already operate.

[Bring us a system and a symptom →](https://hermes-labs.ai/#contact)

---

## The operational layer

**In agent systems, language is part of the runtime.**

System prompts, tool descriptions, retrieved context, memory, summaries, policies, and evaluation criteria do not merely describe a system. They condition what it notices, chooses, remembers, and does.

We treat this operational layer as an engineering surface: something that can be inspected before deployment, tested under adversarial conditions, controlled at runtime, and verified after an action occurs.

That is where systems can remain technically healthy while silently doing the wrong thing.

---

## Open-source reliability tools

Start here. The active public core is nine repositories, each making one part of our approach inspectable and useful on its own. Hermes Labs engagements apply, integrate, and harden these methods in production systems. Per-tool evidence boundaries are documented on the [open-source catalog](https://hermes-labs.ai/open-source).

| Tool | Reliability role | Start |
|---|---|---|
| [**lintlang 0.5.3**](https://github.com/hermes-labs-ai/lintlang) | Static analysis for agent configurations, tool descriptions, and system prompts. Zero LLM calls. [Used in Character AI's Larch CI](https://github.com/character-ai/larch/blob/main/docs/linting.md). | `pip install lintlang==0.5.3` |
| [**hermeneutic 0.1.12**](https://github.com/hermes-labs-ai/hermeneutic) | Mine correction triples from chat logs and gate the next response before the same drift ships twice. | `pip install hermeneutic==0.1.12` |
| [**fidelis 0.0.95**](https://github.com/hermes-labs-ai/fidelis) | Local-first agent memory that returns your original passages verbatim, with no LLM call in the default retrieval path. | `pip install fidelis-memory==0.0.95` — repo, import name, and CLI stay `fidelis`; the unrelated PyPI package named `fidelis` is not ours |
| [**little-canary 0.3.6**](https://github.com/hermes-labs-ai/little-canary) | Input-side prompt-injection detection through sacrificial canary-model probes. | `pip install little-canary==0.3.6` |
| [**hermes-rubric 1.2.1**](https://github.com/hermes-labs-ai/hermes-rubric) | Evidence-first structured scoring for AI artifacts, with every dimension tied to quoted evidence. | `pip install hermes-rubric==1.2.1` |
| [**hermes-blind 0.2.0**](https://github.com/hermes-labs-ai/hermes-blind) | Recover the original goal of a long Claude Code or Codex session from its own logs, as a compact reorientation anchor. | `pip install hermes-blind==0.2.0` |
| [**agent-kickstart 0.3.0**](https://github.com/hermes-labs-ai/agent-kickstart) | A guided, project-local first project for Claude Code beginners. No prior coding or terminal experience required. | `pip install agent-kickstart==0.3.0` |
| [**zer0dex**](https://github.com/hermes-labs-ai/zer0dex) | Dual-layer local memory for agents: a readable markdown index alongside vector retrieval. Reference implementation. | Read the repository before adoption |
| [**agent-gorgon 0.2.0**](https://github.com/hermes-labs-ai/agent-gorgon) | Deterministic runtime policy decisions for autonomous agents, with forensic evidence for later review. | `pip install agent-gorgon==0.2.0` |

---

## Research behind the engineering

Our public research examines distinct reliability problems from empirical, measurement, and conceptual perspectives. Each paper addresses a different question and should be evaluated on its own evidence.

- **[Tool Differentia: Relational Static Analysis for AI Agent Tool Descriptions](https://doi.org/10.5281/zenodo.21817243).** A bounded deterministic analysis of the distinguishing information neighboring AI-agent tool descriptions do or do not provide; it documents LintLang H1.6 and does not establish semantic distinguishability or runtime-selection correctness.
- **[Behavioral Canarying for Prompt Injection: Powerless Model Probes with Explicit Coverage Semantics](https://doi.org/10.5281/zenodo.21818564).** A technical note on pre-execution prompt-injection sensing that separates routing disposition from evidence that inspection ran; it does not claim universal detection, formal security, or aggregate accuracy for the current release.
- **[The Generative Horizon](https://doi.org/10.5281/zenodo.21659634).** A conceptual paper on model self-report, recursive interpretive conditioning, and the boundary between measured representations and claims about inner states.
- **[Precise Records, Unstable Meanings](https://doi.org/10.5281/zenodo.21652317).** A measurement-validity audit of claims derived from AI agent telemetry.
- **[A Taxonomy of Epistemic Failure Modes in Large Language Models](https://doi.org/10.5281/zenodo.19042469).** A taxonomy of seven structural epistemic failure modes.
- **[The Asymmetric Burden of Proof](https://doi.org/10.5281/zenodo.18867694).** A matched-vignette study of null-result asymmetry.

Read the [research index](https://hermes-labs.ai/research) for abstracts, hosted copies, and citation exports.

Machine-readable publication record: [JSON](https://raw.githubusercontent.com/hermes-labs-ai/hermes-publications/main/publications.json) · [JSON-LD](https://raw.githubusercontent.com/hermes-labs-ai/hermes-publications/main/publications.jsonld) · [BibTeX](https://raw.githubusercontent.com/hermes-labs-ai/hermes-publications/main/CITATION.bib).

---

## Upstream engineering

<!-- hermes-contributions:start -->
The [canonical external contribution record](https://hermes-labs.ai/open-source/contributions) reports current, dated totals and separates merged engineering work, submitted fixes, integrations, documentation, ecosystem listings and research-index submissions. [Structured ledger](https://hermes-labs.ai/contributions.json).

Merged AI/framework fixes contributed by Roli Bosch (roli-lpci), founder of Hermes Labs:

- [microsoft/semantic-kernel #13610](https://github.com/microsoft/semantic-kernel/pull/13610) — Preserve the first system/developer message during Python chat-history truncation and handle the target_count=1 boundary. [Case study](https://hermes-labs.ai/case-studies/fixing-semantic-kernel-deleted-system-prompts).
- [langchain-ai/langchain #35544](https://github.com/langchain-ai/langchain/pull/35544) — Drop forced tool_choice with a warning when Anthropic extended thinking is enabled; preserve auto and unaffected requests. [Case study](https://hermes-labs.ai/case-studies/fixing-langchain-thinking-tools-crash).
- [microsoft/semantic-kernel #13635](https://github.com/microsoft/semantic-kernel/pull/13635) — Use value equality to avoid duplicate null entries in strict JSON Schema type arrays, with three regression tests. [Case study](https://hermes-labs.ai/case-studies/fixing-semantic-kernel-duplicate-null-schema).
- [stanfordnlp/dspy #9978](https://github.com/stanfordnlp/dspy/pull/9978) — Reject an empty Evaluate devset with a descriptive ValueError before metric-summary division, with a regression test. [Case study](https://hermes-labs.ai/case-studies/fixing-dspy-empty-devset).

[Mem0 #5250](https://github.com/mem0ai/mem0/pull/5250) contributed a Redis cosine-distance-to-similarity patch with regression coverage. It closed without merge after a maintainer acknowledged the conversion in a broader sweep. The [case study](https://hermes-labs.ai/case-studies/auditing-mem0-retrieval-scoring) preserves earlier community provenance and the patch’s missing clamp. Other substantive unmerged fixes remain visible in the ledger.

Typing modernization in PyTorch Ignite and Optuna, compatibility work and dependency maintenance remain credited in their own classes. Community-list and research-index submissions do not count as merged code contributions.
<!-- hermes-contributions:end -->

---

## More from our stack

We keep additional reference implementations and research concepts public so others can inspect, test, fork, and develop them.

Public does not automatically mean flagship or production-ready. Browse the [full GitHub catalog](https://github.com/hermes-labs-ai) and each repository's own status, installation instructions, and limitations.

---

*Hermes Labs was founded by Roli Bosch ([Rolando Bosch](https://www.linkedin.com/in/rolibosch/) in professional and academic work). [roli@hermes-labs.ai](mailto:roli@hermes-labs.ai) · [hermes-labs.ai](https://hermes-labs.ai)*

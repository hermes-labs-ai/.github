<div align="center">

<h1>Hermes Labs</h1>

Hermes Labs is an agentic infrastructure company building the reliability layer for autonomous systems.

**Make agent behavior easier to inspect, test, control, and explain.**

[![Site](https://img.shields.io/badge/hermes--labs.ai-visit-4F46E5)](https://hermes-labs.ai)
[![Research](https://img.shields.io/badge/research-six%20papers-1682D4)](https://hermes-labs.ai/research)
[![Open source](https://img.shields.io/badge/open%20source-catalog-0F766E)](https://hermes-labs.ai/open-source)
[![Writing](https://img.shields.io/badge/writing-Substack-FF6719?logo=substack&logoColor=white)](https://hermeslabs.substack.com)

</div>

**[Browse the open-source catalog](https://hermes-labs.ai/open-source)** · **[Try LintLang](https://hermes-labs.ai/lintlang)** · **[See engineering evidence](https://hermes-labs.ai/proof)** · **[Get help with a production failure](https://hermes-labs.ai/services)**

These systems can pass conventional evaluations and still fail silently in production. Instructions get dropped. Tools report success they did not achieve. Retrieved context changes meaning. Memory drifts. Policies weaken across long workflows. Evidence no longer explains why an action happened.

Hermes Labs provides engineering services to diagnose these failures and harden the operational layers where they occur: prompts, tool interfaces, retrieval, memory, policies, runtime controls, and evidence.

---

## What we do

We build reliability infrastructure for agents and LLM applications whose behavior must remain dependable, inspectable, and reconstructable under real use.

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

Choose an installation route: [agent plugins](https://github.com/hermes-labs-ai/plugins) for Claude Code, Codex, or GitHub Copilot; [the shared Homebrew tap](https://github.com/hermes-labs-ai/homebrew-tap) for packaged command-line tools. Each catalog lists its available tools; product repositories retain their source, releases, and issue trackers.

Four useful places to begin:

- [LintLang](https://github.com/hermes-labs-ai/lintlang) — statically check agent instructions, configuration, and tool descriptions before they ship.
- [zer0dex](https://github.com/hermes-labs-ai/zer0dex) — explore a readable local memory index alongside vector retrieval.
- [Little Canary](https://github.com/hermes-labs-ai/little-canary) — probe untrusted input for prompt-injection risk before it reaches the primary workflow.
- [Fidelis](https://github.com/hermes-labs-ai/fidelis) — retrieve original local passages verbatim in the default memory path.

Use the [open-source catalog](https://hermes-labs.ai/open-source) and each repository README for current maturity, installation, limitations, and supporting evidence before adoption.

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

This work may be executed through human-directed autonomous engineering infrastructure. [Rolando Bosch](https://github.com/roli-lpci) is the responsible human contributor and authorizes publication from his GitHub account.

---

## More from our stack

We keep additional reference implementations and research concepts public so others can inspect, test, fork, and develop them.

Public does not automatically mean flagship or production-ready. Browse the [full GitHub catalog](https://github.com/hermes-labs-ai) and each repository's own status, installation instructions, and limitations.

---

*Hermes Labs was founded by Roli Bosch ([Rolando Bosch](https://www.linkedin.com/in/rolibosch/) in professional and academic work). [roli@hermes-labs.ai](mailto:roli@hermes-labs.ai) · [hermes-labs.ai](https://hermes-labs.ai)*

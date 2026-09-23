# Product README orientation

This is the canonical orientation contract for active Hermes Labs software repositories.
Keep each product's identity and shortest path to installation, quickstart, usage, or docs.
This is a bounded first-screen standard, not a README redesign.

## First-screen order

Use a centered opening block with this semantic order:

1. Product H1.
2. Existing hero image, where one exists and remains appropriate. Preserve accessible alt text.
3. One concise, product-specific sentence stating what the product does.
4. Existing “developed by [Hermes Labs](https://hermes-labs.ai)” attribution, preserving its
   product-specific wording. Add equivalent attribution if absent.
5. The canonical company sentence:

   > Hermes Labs is an agentic infrastructure company building the reliability layer for autonomous systems.

6. Relevant existing badges.
7. Close the centered block. Keep technical documentation normally left-aligned.

Standardize semantics and ordering, not identical markup. Do not create hero artwork or add
badges for visual consistency. Preserve existing badges unless they are broken, obsolete,
duplicative, misleading, or unrelated to current repository state.

## Preservation boundaries

- Preserve product wording, maturity and status signals, functional links, accessibility text,
  limitations, and the fastest existing path to use. Do not move a working quickstart deeper
  into the README or rewrite it to fit this standard.
- Limit normalization to the hero/orientation area and directly coupled machine-facing company
  descriptions such as `llms.txt`. On those surfaces, preserve machine-oriented structure and
  product context while making present-tense company positioning semantically consistent.
- Hermes ownership links point to `https://hermes-labs.ai`.
- Do not rewrite README bodies, historical statements, launch history, research papers,
  benchmark/results files, archives, or intentional third-party terminology such as LM Studio.
- If this structure would materially reduce clarity for an unusual repository, preserve its
  better orientation and explain the exception in the change. Organization profiles and meta
  repositories retain their navigation role; they do not need fictional product attribution.

## Verification

Review the diff for preserved product meaning, badges, image alt text, links, and first-use
paths. Run existing repository-native checks appropriate to the changed files. Search the
active orientation surfaces for obsolete present-tense company descriptions (for example,
“studio,” “independent AI-reliability lab,” “research lab,” “audit outfit,” or the old
“studies failure modes” paragraph). Do not manufacture new validation infrastructure.

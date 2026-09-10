# Copilot instructions — Hermes Labs

This is the organization-wide default Copilot custom-instructions file for
[Hermes Labs](https://hermes-labs.ai). GitHub does not auto-inherit this file the way it
inherits `SECURITY.md` or `CONTRIBUTING.md`; copy it to a repository's own `.github/copilot-instructions.md`
only if that repository needs it, and let a repository's own copy override this one.

## Before suggesting or generating code

- Read the repository's `AGENTS.md` first. It states the tool's purpose, key paths, exact
  install/test/lint/build commands, and constraints. Prefer it over guessing conventions.
- Match existing code style and structure; do not introduce a new pattern where one already exists.
- Do not add a dependency, workflow, or abstraction the task does not require.

## Claims and evidence

- Do not add or widen performance, accuracy, security, or production-readiness claims that the
  repository cannot demonstrate with a test or a cited source.
- Do not remove, soften, or widen an existing evidence-boundary or "do not use it for" statement.
- State exactly which commands were run to verify a change, and what was not verified.

## Constraints

- Keep changes scoped to what was asked. Do not refactor unrelated code in the same change.
- Never commit secrets, tokens, or credentials. Flag any file that looks like it might contain one.
- Prefer the smallest coherent diff that satisfies the stated requirement.

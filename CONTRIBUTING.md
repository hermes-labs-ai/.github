# Contributing to Hermes Labs projects

This is the organization-wide default contribution guide for
[Hermes Labs](https://hermes-labs.ai). A repository that publishes its own `CONTRIBUTING.md`
overrides this file.

## Before you open a pull request

1. **Open an issue first** for anything larger than a typo, a broken link, or a one-line fix.
   It is faster to agree on the approach than to rework a finished branch.
2. **Keep the change scoped.** One concern per pull request.
3. **Do not add claims.** These tools carry explicit evidence boundaries — statements about what a
   tool does *not* establish. Do not remove, soften, or widen them, and do not add performance,
   accuracy, security, or production-readiness claims that the repository cannot demonstrate.

## Working on a change

- Match the surrounding code style; the repository's existing conventions win over personal
  preference.
- Add or update tests for behavior you change.
- Run the repository's existing test and lint commands before pushing. Most Python repositories
  use `pytest` and `ruff`; most JavaScript repositories use their `package.json` scripts.
- Update the README only when your change alters documented behavior.

## Pull request expectations

- Explain **what** changed and **why**. Link the issue it resolves.
- State how you verified it — the exact commands and their outcome.
- Note anything you did *not* verify.
- CI must pass. A red build will not be merged.

## Reporting bugs

Open a GitHub issue with the version, the platform, the exact command you ran, what you expected,
and what actually happened. A minimal reproduction is the single most useful thing you can
provide.

## Security issues

Do not open a public issue. See [`SECURITY.md`](SECURITY.md).

## Licensing

Contributions are accepted under the license of the repository you are contributing to (Apache-2.0
or MIT — check the repository's `LICENSE` file). By opening a pull request you agree that your
contribution may be distributed under that license.

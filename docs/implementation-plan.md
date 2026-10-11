# First vertical slice

## Documentation bootstrap

Publish only these original design documents after explicit approval to
initialize the empty public repository. No private source, executable installer,
credentials, or license grant accompanies that publication. Actor open-sourcing
is later, separately authorized work with per-package dependency/license review.

## Canonical contract

Author the installation metadata and management protocol in canonical StarLang
authority. Reuse its generated runtime manifests and the existing server
registry/lifecycle. Select the version change through that authority's release
workflow and generate downstream fixtures/validators. Do not create a parallel
JSON Schema authority in this repository.

## Inert staging proof

Use one synthetic package and one suite referencing it. They contain no actor
implementation or executable hooks. Implement the opt-in Lisp management plugin,
repository settings, private GitHub integration and Actors menu flow in Quasar,
which owns installation. This repository hosts actor package scaffolding,
catalog metadata and, in separately scoped changes, actual actor implementations.

Acceptance evidence must prove:

- Plugin disabled: no package-management mutations are available.
- Catalogs configured by the operator can reference independently hosted sources.
- Missing/private auth denies safely; credentials never reach another origin,
  logs, UI, receipts, build inputs or shared catalog projections.
- Private GitHub fixtures cover successful scoped acquisition; missing, expired,
  denied and insufficient credentials; ambiguous 404s; and rate-limit backoff.
  Each exposes only safe, evidence-supported operator remediation.
- Anonymous public-repository acquisition works, while private/unknown sources
  never fall back anonymously or to another identity after authentication failure.
- Archive redirect fixtures verify approved HTTPS-host routing, rejected
  downgrade/unapproved hosts, stripped authorization/cookies, redacted signed
  URLs and final artifact digest verification.
- Environment, keyring and auth-source adapter tests verify lazy opaque-reference
  resolution and repository/origin binding; missing backends fail explicitly.
- Unknown sources, changed digests, hostile archives and dependency conflicts
  fail before committed installation state.
- Repeated requests are idempotent; failed staging leaves the active generation
  intact; removal protects active and required generations.
- Staging invokes no imports, ASDF load, build commands, hooks or service starts.
- Suite membership is pinned and resolves deterministically.

## Explicit activation proof

After staging is proven, select one existing runtime addon through explicit
operator init configuration and verify its maintained registry readiness.
Keep Python services and Lisp server addons in their existing runtime paths.
Do not rewrite actor implementations or introduce recurring-target scheduling.

Repository integration and full-stack packaging are separate changes. Land
existing dependency fixes through their owning pull requests and do not duplicate
or rewrite those branches as part of this catalog scaffold.

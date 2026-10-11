# StarIntel Actors

Home for StarIntel actor implementations, package scaffolding, and a
repository-neutral actor catalog contract.

Actor implementations hosted here belong under [actors/](actors/README.md).
Actor source can also remain in its own independently maintained repository. A suite
references pinned packages; it does not require copying their source here.
For example, `star-wpa` remains independently hosted; a catalog can reference its
package without relocating its implementation.

Quasar owns the installer UI, repository settings, and private GitHub
authentication integration. Operators can define public or private repositories
through that integration's trusted configuration. Authentication uses an
operator-configured provider reference; catalogs never supply credentials or
access grants. This repository supplies actor packages and their catalog metadata.

## Status

Design and Nix documentation scaffold only. No installer, runtime plugin, downloadable actor package,
credential provider, or executable catalog schema is implemented here yet.
The proposed contract must be authored and generated through canonical StarLang
authority before consumers implement its wire representation.

The [producer-owned flake](docs/producer-flake.md) exports the public docs and
their existing checker, with a committed dependency lock and offline checks.
It does not export an actor runtime. Consumers pin producer revisions and select
named outputs; successful documentation checks do not establish actor readiness.

## Boundaries

- Installing stages verified immutable artifacts. It does not execute code.
- Trusted Lisp management and policy plugins are explicitly enabled by the
  operator's `init.lisp`, using operator-supplied source. They are optional and
  are not automatically downloaded or loaded by catalog discovery.
- Actor activation is a separate explicit `init.lisp` configuration step.
- Lisp, Python, and other supported actor runtimes remain distinct from the
  language used to implement the management plugin.
- Actor source access, provider credentials, and licensing remain operator-owned.
- Hosted entitlement policy is independent of package installation.

Read [the package contract](docs/package-contract.md),
[security boundaries](docs/security.md), and
[the first implementation slice](docs/implementation-plan.md).

## Licensing

Repository licensing has not yet been selected. Public visibility does not
establish an open-source license. Each referenced package retains its own license
and source-access requirements; this catalog grants no additional rights.

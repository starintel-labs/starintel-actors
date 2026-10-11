# Proposed package contract

This describes logical requirements, not an implemented API or wire schema.
Canonical StarLang authority must settle representation, versioning, generated
validators, fixtures, and compatibility before executable consumers are added.

## Repository-neutral ownership

StarIntel Actors can host implementations under `actors/` and catalog entries
for independently hosted implementations. Quasar owns the installer UI,
repository settings and GitHub authentication integration. The shared contract
must work for both local-to-this-repository and external actor packages.

An operator configures one or more catalog repositories in trusted `init.lisp`.
Each has a stable local identity, explicit origin/repository, immutable revision
policy, trust policy, and optional authentication-provider reference. Catalogs
may reference actor packages maintained in other repositories. Package sources
must independently satisfy the operator's source allowlist and credential scope.

Adding a catalog does not authorize every repository or artifact it mentions.
No implicit public fallback, repository substitution, or mutable branch update
is permitted after resolving an installation plan.

## Distinct identities

- Catalog identity and pinned catalog revision/digest.
- Package identity and version, source repository and exact source commit,
  immutable artifact locator and content digest.
- Suite identity and version, with exact package membership and dependency lock.
- Actor semantic identity, version/digest, and resource URI from the maintained
  generated semantic contract. Installation does not rename an actor.

Same identity/version with different bytes is an error. Catalog priority must
not silently decide conflicting identities. Dependency resolution rejects
cycles, unresolved references, incompatible versions, and conflicting providers.

## Package declaration

Logical information includes runtime and controlled entrypoint; generated
semantic manifest identity/digest; supported server, protocol, schema, runtime,
platform and ABI compatibility; package dependencies; requested capabilities;
configuration-schema reference/digest; secret-reference requirements; and
license/source-access information. A suite adds no actor runtime of its own.

Keep configuration values separate from package identity. Public configuration
schemas may describe secret requirements but cannot contain secret values.
Installed package state, active runtime state, and catalog availability are
different facts. Catalog declarations cannot manufacture readiness.

## Management operations

Operation names and transport bindings remain proposals until added through the
existing contract registry. Required meanings:

1. List configured catalogs and visible packages/suites with safe provenance.
2. Plan an install/update: resolve immutable dependencies, validate compatibility
   and policy, display effects and return a plan bound to those exact inputs.
3. Stage installation: fetch permitted artifacts, verify digests, safely unpack,
   atomically commit the staged generation and a credential-free receipt.
4. Stage update: create a new generation while preserving the active generation.
5. Remove an inactive, unreferenced generation; refuse active/dependency-required
   removal and preserve user configuration and collected data.
6. Report catalog, staged, configured, active, failed and runtime-ready state
   separately, using the existing runtime registry for actual observations.

Every mutation is authenticated/authorized, idempotent, generation-checked and
bounded. Plans are invalidated when their inputs or authorizations change.
Retries verify existing artifacts/receipts instead of duplicating effects.
Partial suite failure never silently activates a partial fleet.

## Activation

Install and update do not load ASDF systems, import Python modules, compile source,
execute build/install hooks, or start services. Source builds, if required, are
a separate trusted operator deployment step, not hidden installation behavior.

The operator enables the management plugin and explicitly selects trusted staged
package versions in `init.lisp`. Use the existing addon/runtime lifecycle rather
than a new scheduler or actor registry. Lisp code is trusted process code, not
sandboxed by the addon lifecycle. Stopping an addon does not unload definitions;
clean removal or replacement may require a process restart.

The Actors menu can offer individual and suite staging and show the required
activation configuration, but cannot edit trusted init configuration or turn a
catalog entry into permission to execute it. Runtime controls remain subject to
their existing authorization and lifecycle contract.

## Canonical compatibility

Reuse maintained generated StarLang contracts and SDK boundaries. Each package
declares its actual wire profile; legacy producers remain explicit legacy
producers until genuinely migrated. Never infer compatibility from shape or
rewrite schema versions. Package contract changes follow canonical authoring,
release/version policy, generation, fixture validation, and consumer repinning.

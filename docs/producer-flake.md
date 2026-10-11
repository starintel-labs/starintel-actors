# Producer-owned flake scaffold

This repository exports its existing public documentation and documentation
checker. It contains no actor implementation, actor semantic manifest, installer,
runtime readiness probe, or executable catalog contract. A successful check here
proves documentation integrity only.

## Outputs and dependencies

The supported system is `x86_64-linux`. Other systems are not exported or claimed
as tested. `flake.lock` pins the Nixpkgs source revision and content hash. Python
and the shell/build tools come from that locked Nixpkgs; there are no Python
package downloads or actor dependencies. Use Nix with `nix-command` and `flakes`
enabled.

| Output | Purpose |
| --- | --- |
| `packages.x86_64-linux.docs` (also `default`) | Public Markdown and the existing docs-check source under `share/starintel-actors` |
| `packages.x86_64-linux.docs-check` | Installed `starintel-actors-check-docs` command; checks the packaged docs from any working directory |
| `apps.x86_64-linux.docs-check` (also `default`) | Runs that same documentation command |
| `checks.x86_64-linux.documentation` | Executes the packaged checker against the packaged docs |
| `checks.x86_64-linux.documentation-gate` | Runs the existing mutation tests, including missing docs, broken links, invalid UTF-8 and credential-pattern rejection |

The checker has no actor identity, activation behavior, or runtime protocol. It
is a development utility, not an actor. No repository license has been selected;
these Nix outputs do not grant source or redistribution rights.

## Reproduce validation

Run from a clean checkout of the candidate commit:

```sh
nix flake show --no-update-lock-file
nix eval --no-update-lock-file --json .#packages.x86_64-linux --apply builtins.attrNames
nix build --no-update-lock-file --no-link .#docs .#docs-check
nix flake check --no-update-lock-file --print-build-logs
nix run --no-update-lock-file .#docs-check

# Isolated developer profile, not the Quasar actor installation workflow.
proof_dir=$(mktemp -d)
nix profile install --no-update-lock-file --profile "$proof_dir/profile" .#docs-check
(cd /tmp && "$proof_dir/profile/bin/starintel-actors-check-docs")
git diff --exit-code -- flake.lock
```

Record the exact commit, Nix version, system, exit status, and any unrun checks in
the draft PR. The Nix workflow repeats evaluation, builds, checks and isolated
profile execution against the PR head commit. A workflow definition or queued run
is not execution proof. Actor build, installed-start, protocol compatibility and
readiness tests remain unrun because no approved actor is present.

## Consumer and suite contract

A consumer must pin this producer's exact Git commit and commit its own
`flake.lock`; it must select a named output. Branch names alone are not a release
pin. For this scaffold, use the reviewed candidate/release commit in place of
`<full-40-character-commit>`:

```nix
inputs.publicActors.url =
  "github:starintel-labs/starintel-actors/<full-40-character-commit>";

# Inside the consumer outputs, for the selected supported system:
# docs = publicActors.packages.${system}.docs;
# checker = publicActors.packages.${system}.docs-check;
```

This is an input/output selection example, not a catalog or semantic manifest.
One producer can export several named packages. A suite may select several of
them at one pinned producer revision, as well as packages from other separately
pinned producers. Keep implementations, dependency locks, builds and conformance
tests in their owning repositories. Do not copy source into a consumer or replace
a producer's locked dependencies through an unreviewed `follows` override.

## Manifest and installer handoff

The [package contract](package-contract.md) remains the shared logical design.
Canonical StarLang authority must first release the representation, generated
manifests/validators, compatibility fixtures and version policy. This scaffold
adds no wire fields, document types, registry or manifest schema, and makes no
claim that generated compatibility has passed.

For each later, separately approved actor, its owner must connect the producer
revision/output and artifact digest to the actual generated actor identity,
runtime entrypoint, dependency and compatibility evidence. Repin consumers after
the canonical release and test them against those generated fixtures. Suites
preserve exact membership and do not invent a runtime of their own.

Quasar continues to own installation and repository authentication. Building a
flake is an explicit trusted development/deployment operation. Quasar stages
already built, verified inert artifacts; it must not evaluate or build a flake,
run this checker, load code, or start a service as an installation hook. Activation
remains an explicit trusted operator `init.lisp` step using the existing lifecycle.

The existing actor migration is separately owned and retains its source-isolation,
publication, license and dependency gates. This change moves or deletes no actor
source and includes no private implementations or private catalog membership.

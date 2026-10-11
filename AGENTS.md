# Contributor and agent contract

- This repository hosts actor implementations and catalog/package scaffolding.
  It also references independently hosted packages. Catalog membership does not
  authorize moving or publishing implementations from another repository.
- Quasar owns installer UI, repository settings and private GitHub authentication
  integration; do not implement a second installer in this actor repository.
- Do not copy private code, credentials, internal deployment details, or private
  catalog metadata into this public repository.
- Canonical StarLang specifications, generated contracts, and conformance tests
  own wire semantics. Do not invent document types, hand-edit generated schemas,
  or relabel legacy producers as canonical.
- Proposed logical fields in design documents are not approved wire fields.
- Reuse existing actor identity, registry, runtime, addon lifecycle, transport,
  publisher, and scheduling authorities. Do not introduce parallel authorities.
- Installing means fetching, verifying, and staging inert artifacts. No package
  hooks, ASDF loading, Python imports, shell commands, or services may execute.
- Only trusted operator configuration enables plugins and activates staged
  actors. Catalog content must never grant capabilities or trust itself.
- No literal credentials in configuration examples, catalogs, URLs, logs,
  receipts, Nix expressions, derivations, or store paths.
- Every authenticated fetch must bind credentials to an approved repository and
  origin. Redirects and cross-origin artifact downloads must not inherit them.
- Use issue-backed, focused branches and draft pull requests after bootstrap.
  Verify changes on the exact candidate commit; distinguish passed, failed, and
  unrun checks. Repository initialization requires explicit publication approval.
- Do not select a repository license or migrate existing actors to open source
  without an explicit owner decision.

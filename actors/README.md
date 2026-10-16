# Actor packages

This directory is the home for actor implementations maintained in this
repository. It is intentionally empty of implementations in the documentation
bootstrap. Catalog entries may also reference independently maintained actor
repositories, such as `star-wpa`, without relocating their source.

The [symbolic-investigation design suite](symbolic-investigation/README.md)
records 15 proposed StarLang actors, not runnable packages or generated manifests.
Its reusable Prolog expert belongs in Star-KB.

Each future actor package needs its own reviewed identity, runtime entrypoint,
generated manifest, dependency/compatibility declaration, configuration schema,
license provenance and deterministic conformance tests. Exact package layout and
wire fields follow the canonical contract rather than an invented local schema.

Quasar owns installation, repository settings and private GitHub authentication.
Actor packages must never bundle credentials or self-authorize installation or
activation. Installation stages inert artifacts; the operator activates selected
versions through trusted `init.lisp` configuration.

Moving selected private actors here for open-source release is separate future
work. It requires explicit publication scope and review of source rights,
dependencies, secrets and licensing. No private actor source is included now.

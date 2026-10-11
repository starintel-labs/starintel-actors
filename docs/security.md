# Trust and private-repository access

## Operator authority

These requirements govern Quasar's installer/repository and private GitHub
authentication integration. Actor packages hosted here or elsewhere are inputs
to that integration; they do not own the user's repository credentials.

Trusted operator `init.lisp` configures catalog repositories, allowed package
sources, expected origin/repository identity, authentication-provider references,
management permissions, and staged versions authorized for activation.

The proposed plugin API is not yet implemented; do not present illustrative
configuration as executable supported configuration. Configuration examples must
refer to credentials, never contain literal tokens.

## GitHub authentication

Support an adapter interface for operator-owned OS keyring, environment, or
Emacs auth-source lookup. These are proposed backends, not claims of current
availability. The adapter resolves an opaque credential reference only when an
approved fetch needs it. Catalogs cannot choose or override that reference.

Use the least repository-read permissions sufficient for the exact selected
private repositories. Do not request write/admin access for catalog installation.
Creating credentials, granting repository access, or expanding persistent
permissions is a separate operator action, never part of normal discovery.

Bind each credential to its configured GitHub origin and repository scope.
Validate repository and remote identity before use. Apply credentials only to
the authorized authenticated request. Never forward authorization headers or
cookies across redirects; authenticate a new origin only through its own
explicit approved credential binding. Artifact URLs on other hosts do not inherit
GitHub credentials. Reject credential-bearing repository URLs.

GitHub archive downloads may redirect to a separate artifact host. Follow only
bounded HTTPS redirects permitted by the operator's archive-host policy, reject
downgrades and unapproved destinations, and strip authorization/cookies before
the redirected request. Treat signed artifact URLs as sensitive, short-lived
transport material: never log, persist, expose to the browser, or reuse them as
catalog identity. Always verify the resulting bytes against the pinned digest.

Anonymous acquisition is allowed only for the exact repository explicitly
configured as public and verified readable anonymously. An authenticated failure
for a private or unknown-visibility repository must never trigger anonymous
fallback. Do not infer public visibility from a 401, 403 or 404 response.

Fail closed on missing, expired, denied or insufficient authentication. Do not
silently switch to a similarly named public package, use another account, or
disclose whether an inaccessible private repository exists. Redact error bodies,
URLs, headers and exception text before UI/log propagation.

Give the authorized operator a safe error category and a next step. Missing
credentials should request configuration of the named opaque provider reference;
an invalid/expired credential should request operator renewal or replacement;
insufficient repository access should request review of selected-repository read
permissions and any required organization authorization. Distinguish these only
when the provider supplies reliable evidence: otherwise report unavailable or
unauthorized without guessing token expiry or repository existence. Rate limits
are a separate retryable condition with bounded backoff. No error recovery may
create credentials, expand grants, switch identity, or reveal a token.

Do not place secrets in catalog data, init literals, target documents, command
arguments, receipts, lockfiles, Nix expressions/derivations, or the Nix store.
Resolve them at the authenticated effect boundary; avoid secret-valued build
inputs and persistent caches. Never expose credentials to the browser.

## Private metadata

Private catalogs and installation receipts remain in the authorized operator or
tenant scope. Do not publish them to public catalog mirrors, shared workspaces,
telemetry or cross-user caches. A public suite must not expose private package
names, source URLs or membership without explicit publication authorization.

## Artifact safety

Verify immutable identities and digests before committing a generation. Bound
download size, decompression, entry count and path length; reject traversal,
absolute paths, symlink/hardlink escapes, device/FIFO/socket archive entries and
destination collisions. Stage beneath an
operator-owned directory and atomically commit only complete verified content.

Never interpret manifests as Lisp or executable code. Disable evaluation in any
applicable reader. Reject arbitrary commands and hooks. License acceptance and
source access are independent of artifact integrity and runtime authorization.

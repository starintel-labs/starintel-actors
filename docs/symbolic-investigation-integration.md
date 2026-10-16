# Symbolic investigation actor integration plan

**Status: design-only public actor suite.** Tracks
[starintel-actors #4](https://github.com/starintel-labs/starintel-actors/issues/4)
and [star-kb #29](https://github.com/starintel-labs/star-kb/issues/29).

The [15-role design roster](../actors/symbolic-investigation/design-roster.json)
lists roles, conceptual triggers, already-documented KB reads, initial local
expert predicates, candidate-only outputs and outstanding dependencies. It is
**not** fed to Quasar, Star Server or the StarLang manifest compiler.

## Ownership, not duplication

| Owner | Responsibility |
| --- | --- |
| StarLang | Authoritative actor grammar, normalized IR, generated manifests and message protocol |
| StarIntel public actors | Role implementations and source-side package tests once individually approved |
| Star-KB | Shared read-only predicate/rule semantics, query proof and projection generation |
| StarIntel server | Authenticated scopes, durable state, leases, target admission, canonical document writes and idempotent recovery |
| Quasar | Installer UI, trusted repository configuration and optional activation flow |

The shared KB currently exposes a **limited** remote query surface; its
opt-in `symbolic_investigation.pl` implementation is a local reusable rule
module. Do not label its Prolog exports remote RPCs until the Star-KB service
owner adds and verifies approved named operations with tenant/snapshot pins,
limits, authentication and cancellation behavior.

### Proof/evidence flow (design, not runnable)

```text
trusted canonical document -> StarLang registry/supervised mailbox
    -> LinkWeaver -> bounded Star-KB semantic query
    -> candidate ownership *path*, source Relation IDs, projection generation
    -> ContradictionHunter + EvidenceJudge
    -> HypothesisEngine / FrontierScout proposes missing evidence
    -> human approval and existing server admission
    -> KnowledgeFoundry prepares candidate data
    -> server-owned 0.10.1 validation + provenance + review + conditional write/readback
    -> a new canonical document produces a new projection generation
```

No `related-to` production edges; use meaningful directional typed
predicates. There is no recursive, uncontrolled actor fan-out: actor work must
observe hard step/fan-out/depth/time/byte/budget caps, tenant boundaries,
versioned rules, idempotency keys and ability-specific permissions.

## Priorities and release gates

**P0 proof slice:** LinkWeaver, ContradictionHunter, HypothesisEngine,
FrontierScout, EvidenceJudge, EntityFusion and KnowledgeFoundry. Only the
reusable read-only KB rule primitives are supplied by the companion KB PR.

**P1:** TemporalOracle, RuleSmith, OntologyMiner, ActiveTeacher,
BeliefRevision, GoalDirector, ProofExplainer. Reuse existing Star-KB mining,
the research-gated Aleph/active learning directions, and goal engine #27.

**P2:** RuleTournament, using synthetic corpus fixtures and recorded rule
versions. It does not auto-select or self-promote rules.

Before calling an actor runnable:
1. Approve research/design and any source-rights/publication decision.
2. Generate StarLang actor identity, accepted/produced types and wire fixture
   using the canonical StarLang compiler; do not hand-maintain a shadow schema.
3. Implement real actor handler, mailbox/supervisor boundary and capability
   constraints in this repo without duplicating Star Server's scheduler.
4. Bind only approved named KB operations; supply schema/revision pins and
   provenance with every candidate, without assuming local KB calls are RPC.
5. Wire server-owned conditional writes, review gates, restart, duplicate and
   failure fixtures; prove tests on real StarLang runtime.
6. Export immutable producer-owned Nix package(s) and exact revision/digest,
   with no installer hooks or privileged activation. Update documentation and
   exact-head CI before review/merge.

### Offline checks

```sh
python3 -B -m unittest discover -s scripts -p 'test_*.py' -v
python3 -B scripts/check_docs.py
nix flake check --no-update-lock-file -L   # where Nix is available
```

The tests verify inventory invariants and documentation, **not** runnable
actor conformance. Never claim deployment, ingestion, StarLang compilation or
production Star-KB remote bindings from a green docs job.

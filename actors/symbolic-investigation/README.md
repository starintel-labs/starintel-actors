# Symbolic Investigation — public StarLang actor suite

This directory owns the **15 actor designs** for StarLang + Star-KB symbolic
investigations. It does not implement or activate the actors. The
[design roster](design-roster.json) is editorial input for review and tests:
**not** a StarLang manifest, canonical document, registry, installer catalog,
runtime declaration, package grant, or permission to dispatch targets.

Source of truth:
- Actor behavior, interfaces and packaging: [public actors issue #4](https://github.com/starintel-labs/starintel-actors/issues/4).
- Reusable Prolog semantics: [Star-KB issue #29](https://github.com/starintel-labs/star-kb/issues/29) and the opt-in
  [expert source](https://github.com/starintel-labs/star-kb/blob/rage/29-symbolic-investigation-expert/kb/public/starintel/symbolic_investigation.pl).
- Schema/manifest/actor wire: canonical [StarLang](https://github.com/lost-rob0t/star-lang).
- Goal admission and target scheduling: existing StarIntel server; use
  [Star-KB proactive PR #27](https://github.com/starintel-labs/star-kb/pull/27)
  once reviewed/merged, not a second scheduler.
- Candidate validation, canonical writes and readback: server-owned 0.10.1 path.
  Quasar alone owns actor installation UI/authentication.

## Proposed actor roles

| Actor | Priority | Owns |
| --- | --- | --- |
| LinkWeaver | P0 | Typed multi-edge candidate links with source proofs |
| ContradictionHunter | P0 | Conflicts in relation/evidence claims |
| HypothesisEngine | P0 | Falsifiable candidate hypotheses and missing evidence |
| RuleSmith | P1 | ILP/Horn rule proposals and counterexamples |
| EntityFusion | P0 | Evidence-backed candidate identity matches; no forced merges |
| FrontierScout | P0 | Bounded next questions, never self-authorized targets |
| TemporalOracle | P1 | Time overlap, ordering, and disputed intervals |
| EvidenceJudge | P0 | Corroboration/source review and evidence defects |
| OntologyMiner | P1 | Specific, typed, directional ontology proposals |
| ActiveTeacher | P1 | Uncertain examples for human labeling |
| BeliefRevision | P1 | Non-destructive supersession and disputes |
| GoalDirector | P1 | Operator-scoped symbolic action selection and budgeting |
| KnowledgeFoundry | P0 | Canonical candidate draft handoff for existing review/write pipeline |
| ProofExplainer | P1 | Reproducible explanations with provenance |
| RuleTournament | P2 | Rule evaluations, cost/quality comparisons and regression fixtures |

**No actor may equate a path with a proved identity or ownership control.**
Every derived claim must be reviewable with supporting relation IDs,
provenance, counterevidence, rule identity and projection revision.

## First reviewed vertical slice

1. Trusted StarLang runtime receives a canonical, scoped relation/update through
   its existing actor registry and mailbox. The actual generated wire/manifest
   has not been added here.
2. LinkWeaver uses the **existing bounded KB** semantics, initially via the
   *local* opt-in Star-KB `ownership_path_candidates/3` expert.
3. ContradictionHunter calls `contradiction_cases/3`; EvidenceJudge assesses
   source/evidence linkage and checks that neither finding is trusted truth.
4. HypothesisEngine/FrontierScout can suggest a `frontier_question/4` but
   cannot turn it into a target. GoalDirector hands approved goals to the
   existing server-owned admission/scheduling path.
5. KnowledgeFoundry proposes canonical **candidate** documents through the
   existing validation/provenance/review/write/readback path, after the
   canonical 0.10.1 integration is verified. It does not write directly to KB.

Steps 1, 2-4 remote binding, and 5 production write integration are **not
implemented** by this PR; they require canonical StarLang/StarIntel contracts
and exact-head system conformance, not fabricated wire fixtures.

See [integration and gates](../../docs/symbolic-investigation-integration.md).

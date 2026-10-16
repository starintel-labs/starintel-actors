"""Design-inventory checks; no claim of executable StarLang actor coverage."""

from __future__ import annotations

import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ROSTER = ROOT / "actors" / "symbolic-investigation" / "design-roster.json"

EXPECTED = {
    "link-weaver", "contradiction-hunter", "hypothesis-engine",
    "rule-smith", "entity-fusion", "frontier-scout", "temporal-oracle",
    "evidence-judge", "ontology-miner", "active-teacher",
    "belief-revision", "goal-director", "knowledge-foundry",
    "proof-explainer", "rule-tournament",
}

# Existing named KB tools described by prolog-star-kb; NOT new wire operations.
KB_TOOLS = {
    "kb_document", "kb_neighbors", "kb_path", "kb_explain",
    "kb_timeline", "kb_contradictions", "kb_compare", "kb_sources",
    "kb_why_not", "kb_values", "kb_referrers", "kb_packet",
    "kb_route_reasoning",
}
LOCAL_EXPERT = {
    "ownership_path_candidates", "contradiction_cases",
    "frontier_question", "evidence_coverage",
}


class SymbolicInventoryTests(unittest.TestCase):
    def setUp(self) -> None:
        self.roster = json.loads(ROSTER.read_text(encoding="utf-8"))
        self.actors = self.roster["actors"]

    def test_fifteen_explicit_unique_public_actor_designs(self) -> None:
        ids = [actor["id"] for actor in self.actors]
        self.assertEqual(set(ids), EXPECTED)
        self.assertEqual(len(ids), 15)
        self.assertEqual(len({actor["name"] for actor in self.actors}), 15)
        self.assertEqual(sum(actor["priority"] == "P0" for actor in self.actors), 7)

    def test_design_inventory_never_confers_actor_permission(self) -> None:
        self.assertEqual(self.roster["readiness"], "design_only")
        self.assertIn("NOT a StarLang-generated", self.roster["notice"])
        for actor in self.actors:
            self.assertRegex(actor["id"], r"^[a-z]+(?:-[a-z]+)*$")
            self.assertEqual(actor["activation"], "not_implemented")
            self.assertEqual(actor["candidate_policy"], "never_auto_promote")
            self.assertIn(actor["priority"], {"P0", "P1", "P2"})
            self.assertTrue(actor["trigger"])
            self.assertTrue(actor["purpose"])
            self.assertTrue(actor["proposed_output"])
            self.assertTrue(actor["dependency"])
            self.assertTrue(actor["reads"])
            self.assertTrue(set(actor["reads"]) <= KB_TOOLS)
            self.assertTrue(set(actor["local_expert"]) <= LOCAL_EXPERT)

    def test_no_parallel_wire_schema_or_implied_actor_registry(self) -> None:
        forbidden = {
            "schemaVersion", "service_uri", "handler", "accepts", "produces",
            "actor_manifest", "token", "credentials", "api_key",
        }
        for actor in self.actors:
            self.assertFalse(forbidden.intersection(actor))
            self.assertNotIn("related-to", actor["purpose"])
        self.assertTrue(
            (ROOT / "docs" / "symbolic-investigation-integration.md").is_file()
        )


if __name__ == "__main__":
    unittest.main()

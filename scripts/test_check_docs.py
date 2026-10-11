"""Mutation tests prove the documentation gate rejects meaningful failures."""

from pathlib import Path
import tempfile
import unittest

from check_docs import REQUIRED, check


class DocumentationGateTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        for name in REQUIRED:
            path = self.root / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text("# Document\n", encoding="utf-8")

    def write_readme(self, text):
        (self.root / "README.md").write_text(text, encoding="utf-8")

    def test_valid_repository(self):
        self.write_readme("# Docs\n[Actors](actors/README.md)\n")
        self.assertEqual(check(self.root), [])

    def test_missing_required_document(self):
        (self.root / REQUIRED[-1]).unlink()
        self.assertTrue(any("required document missing" in e for e in check(self.root)))

    def test_broken_relative_link(self):
        self.write_readme("[Missing](absent.md)\n")
        self.assertTrue(any("relative link" in e for e in check(self.root)))

    def test_escaping_relative_link(self):
        self.write_readme("[Escape](../outside.md)\n")
        self.assertTrue(any("escaping" in e for e in check(self.root)))

    def test_missing_newline(self):
        self.write_readme("# Missing newline")
        self.assertTrue(any("newline" in e for e in check(self.root)))

    def test_invalid_utf8(self):
        (self.root / "README.md").write_bytes(b"\xff\n")
        self.assertTrue(any("UTF-8" in e for e in check(self.root)))

    def test_token_pattern_is_redacted(self):
        fake = "gh" + "p_" + "A" * 36
        self.write_readme(fake + "\n")
        errors = check(self.root)
        self.assertTrue(any("credential material" in e for e in errors))
        self.assertNotIn(fake, "\n".join(errors))

    def test_credential_url_is_redacted(self):
        self.write_readme("[Link](https://user:example-secret@github.com/org/repo)\n")
        errors = check(self.root)
        self.assertTrue(any("credential-bearing" in e for e in errors))
        self.assertNotIn("example-secret", "\n".join(errors))

    def test_private_key_pattern(self):
        self.write_readme("-----BEGIN " + "RSA PRIVATE KEY-----\n")
        self.assertTrue(any("credential material" in e for e in check(self.root)))


if __name__ == "__main__":
    unittest.main()

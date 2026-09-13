"""Exercise the checker with temporary repositories, not pinned lesson prose."""

import importlib.util
import os
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("check_content", ROOT / "scripts/check_content.py")
checker = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(checker)


class ContentChecks(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)

    def write(self, path, text):
        target = self.root / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(text, encoding="utf-8")
        return target

    def issues(self):
        return checker.check_repository(self.root)[0]

    def test_local_file_fragment_and_root_relative_links(self):
        self.write("README.md", "# Start\n[unit](examples/example.md#make-it-work)\n")
        self.write("guide.md", "# Guide\n[home](/README.md#start)\n")
        self.write("examples/example.md", "# Make it work\n")
        self.assertEqual([], self.issues())

    def test_missing_path_and_fragment_are_errors_with_line_numbers(self):
        self.write("README.md", "# Start\n[missing](gone.md)\n[section](#absent)\n")
        issues = self.issues()
        self.assertEqual(2, len(issues))
        self.assertIn("README.md:2: missing local file", issues[0])
        self.assertIn("README.md:3: missing heading", issues[1])

    def test_code_fences_comments_inline_code_and_external_links_are_ignored(self):
        self.write("README.md", """# Start
```markdown
[example](missing.md)
```
~~~text
[example](other-missing.md)
~~~
<!-- [hidden](no.md) -->
`[code](no.md)`
[external](https://vendor.example.com/does-not-need-network)
[email](mailto:help@example.com)
""")
        self.assertEqual([], self.issues())

    def test_reference_links_and_undefined_references(self):
        self.write("README.md", "[Read more][Guide]\n[Guide][]\n[Guide]\n\n[guide]: other.md#details\n")
        self.write("other.md", "# Details\n")
        self.assertEqual([], self.issues())
        self.write("README.md", "[Read more][missing]\n")
        self.assertIn("undefined link reference", self.issues()[0])

    def test_broken_reference_definition_is_checked(self):
        self.write("README.md", "[Guide]\n\n[guide]: missing.md\n")
        self.assertTrue(any("missing local file" in issue for issue in self.issues()))

    def test_encoded_spaces_parentheses_images_and_angle_destinations(self):
        self.write("file with spaces.md", "# Go\n")
        self.write("folder/example(one).md", "# One\n")
        self.write("README.md", r"""[space](file%20with%20spaces.md#go)
[angle](<file with spaces.md> "Title")
[parentheses](folder/example(one).md#one)
[escaped](folder/example\(one\).md#one)
![image](diagram.svg)
""")
        self.write("diagram.svg", "<svg/>")
        self.assertEqual([], self.issues())

    def test_duplicate_headings_unicode_and_explicit_html_anchors(self):
        self.write("README.md", """# Überprüfung: `save()`
## Try again
## Try again
## Try again-1
<a id="custom-target"></a>
[unicode](#%C3%BCberpr%C3%BCfung-save)
[repeat](#try-again-1)
[collision](#try-again-1-1)
[html](#custom-target)
""")
        self.assertEqual([], self.issues())

    def test_html_links_are_checked(self):
        self.write("README.md", '<a href="missing.md">Missing</a>\n')
        self.assertIn("missing local file", self.issues()[0])

    def test_hidden_and_private_progress_folders_are_excluded(self):
        self.write("README.md", "# Start\n")
        self.write(".codex/report.md", "[broken](missing.md)\n")
        self.write("learning/local/progress.md", "[private](missing.md)\n")
        self.assertEqual([], self.issues())

    def test_private_targets_are_neither_walked_nor_read_through_links(self):
        private = self.write("learning/local/private-marker.md", "# Private sentinel\n").resolve()
        hidden = self.write(".codex/hidden-marker.md", "# Hidden sentinel\n").resolve()
        (self.root / "alias-marker.md").symlink_to(private)
        self.write("README.md", """[progress](learning/local/private-marker.md#private-sentinel)
[hidden](.codex/hidden-marker.md#hidden-sentinel)
[alias](alias-marker.md#private-sentinel)
""")
        original_read = Path.read_text
        original_scandir = os.scandir
        private_dirs = {private.parent, hidden.parent}

        def guarded_read(path, *args, **kwargs):
            self.assertNotIn(path.resolve(), {private, hidden}, "read an excluded file")
            return original_read(path, *args, **kwargs)

        def guarded_scandir(path):
            self.assertNotIn(Path(path).resolve(), private_dirs, "walked an excluded directory")
            return original_scandir(path)

        with patch.object(Path, "read_text", guarded_read), patch.object(os, "scandir", guarded_scandir):
            issues = self.issues()
        self.assertEqual(3, len(issues))
        self.assertTrue(all("excluded local content" in issue for issue in issues))
        for marker in ("private-marker", "hidden-marker", "alias-marker", "sentinel"):
            self.assertNotIn(marker, "\n".join(issues))

    def test_link_outside_repository_is_rejected(self):
        self.write("README.md", "[outside](../private.md)\n")
        self.assertIn("leaves the repository", self.issues()[0])

    def test_symlink_does_not_allow_reading_outside_repository(self):
        self.write("README.md", "[outside](escape.md#anything)\n")
        (self.root / "escape.md").symlink_to(self.root.parent / "private.md")
        self.assertIn("leaves the repository", self.issues()[0])

    def test_empty_root_fails_instead_of_reporting_success(self):
        self.assertTrue(self.issues())

    def test_complete_unit_and_missing_sections(self):
        unit = """# Make a thing
| | |
|---|---|
| **Prerequisites** | None |
| **Time** | ~15 min |
| **Outcome** | After this unit you can show a working thing. |
| **Last verified** | 2026-09-13 |
## Why this matters
The old thing breaks.
## Do it
Try the next input.
## Done when
- [ ] I checked a result.
## Data note
Use invented data.
## Next
[Start](../README.md)
"""
        self.write("README.md", "# Start\n")
        self.write("tracks/example.md", unit)
        self.assertEqual([], self.issues())
        self.write("tracks/example.md", unit.replace("## Data note", "## Other"))
        self.assertIn("unit is missing section: Data note", self.issues()[0])

    def test_invalid_date_and_non_observable_done_section(self):
        issues = checker.check_unit(Path("tracks/test.md"), """# Unit
| **Last verified** | 2026-02-30 |
## Done when
I understand it.
""")
        self.assertTrue(any("calendar date" in issue for issue in issues))
        self.assertTrue(any("observable checklist" in issue for issue in issues))

    def test_verification_date_requires_the_documented_format(self):
        issues = checker.check_unit(Path("tracks/test.md"), "| **Last verified** | 20260913 |\n")
        self.assertTrue(any("YYYY-MM-DD" in issue for issue in issues))


if __name__ == "__main__":
    unittest.main()

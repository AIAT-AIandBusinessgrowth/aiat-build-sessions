"""Hold the published verification-lab exercise to the release importer's contract.

The page is deployed by an external importer that copies an allowlist of files
and refuses the release if the intentional exercise bug or the agent-guide
heading is gone. The deployed page runs under `default-src 'self'`, so any
resource loaded from another origin fails silently in production. Every check
here fails in this repository instead of at deploy time.
"""

from html.parser import HTMLParser
from pathlib import Path
from typing import NamedTuple
import re
import unittest


LAB = Path(__file__).resolve().parents[1] / "exercises/verification-lab"
PAGES = ("index.html", "notebook-calculator.html")
FONTS = (
    "assets/fonts/Geist-Regular.woff2",
    "assets/fonts/Geist-Medium.woff2",
    "assets/fonts/GeistMono-Regular.woff2",
)
PUBLISHED = (
    "index.html",
    "notebook-calculator.html",
    "agent-guide.md",
    "llms.txt",
    "robots.txt",
    "sitemap.xml",
    "assets/fonts/OFL.txt",
) + FONTS

# The importer greps for `Math.round(people / 4)`; the comment keeps the next
# contributor from "fixing" the calculator that the exercise is built on.
DEFECT = re.compile(
    r"// Intentional exercise bug\.[^\n]*\n"
    r"function packsFor\(people\) \{\s*\n"
    r"\s*return Math\.round\(people / 4\);\s*\n"
    r"\}"
)
# `https://x`, `http://x` and the scheme-relative `//x` all leave this origin.
EXTERNAL_ORIGIN = re.compile(r"\A(?:[a-z][a-z0-9+.\-]*:)?//", re.IGNORECASE)
# Inline payloads are not `'self'` either: `default-src 'self'` blocks all three,
# and each one smuggles a resource past the importer's file allowlist.
INLINE_SCHEME = re.compile(r"\A(?:data|blob|filesystem):", re.IGNORECASE)
# `rel` values that describe the document rather than fetching a subresource.
# Anything else on a <link> — preload, icon, stylesheet, manifest — is a fetch.
METADATA_LINK_RELS = frozenset({"canonical", "alternate"})
# Elements a browser fetches from, and the attribute that carries the URL.
URL_ATTRIBUTE = {
    "script": "src",
    "img": "src",
    "source": "src",
    "iframe": "src",
    "embed": "src",
    "video": "src",
    "audio": "src",
    "track": "src",
    "object": "data",
}


class Resource(NamedTuple):
    tag: str
    url: str
    fetched: bool  # False only for <link> rels that merely describe the document


class ResourceCollector(HTMLParser):
    """Collect every URL the page names, fetched or not."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.resources = []
        self._in_style = False

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        if tag == "style":
            self._in_style = True
        elif tag == "link":
            rel = " ".join((attributes.get("rel") or "").lower().split())
            href = attributes.get("href")
            if href:
                self.resources.append(
                    Resource(f"link rel={rel or '(none)'}", href, rel not in METADATA_LINK_RELS)
                )
        elif tag in URL_ATTRIBUTE and attributes.get(URL_ATTRIBUTE[tag]):
            self.resources.append(Resource(tag, attributes[URL_ATTRIBUTE[tag]], True))

    def handle_endtag(self, tag):
        if tag == "style":
            self._in_style = False

    def handle_data(self, data):
        if self._in_style:
            for match in re.finditer(r"url\(\s*['\"]?([^'\")]+)", data):
                self.resources.append(Resource("style url()", match[1].strip(), True))


def collect(page):
    parser = ResourceCollector()
    parser.feed((LAB / page).read_text(encoding="utf-8"))
    parser.close()
    return parser.resources


class VerificationLabRelease(unittest.TestCase):
    def test_intentional_defect_is_present(self):
        # Without this, a failure prints the whole 40 KB page instead of the reason.
        self.longMessage = False
        for page in PAGES:
            with self.subTest(page=page):
                self.assertRegex(
                    (LAB / page).read_text(encoding="utf-8"),
                    DEFECT,
                    f"{page}: packsFor() must still read `return Math.round(people / 4);` with the "
                    "'Intentional exercise bug' comment on the line above. The release importer "
                    "greps for that literal and refuses to publish a page that no longer has it.",
                )

    def test_agent_guide_heading_is_importer_contract(self):
        text = (LAB / "agent-guide.md").read_text(encoding="utf-8")
        self.assertEqual(
            text.splitlines()[0],
            "# Help someone try AI:AT Build Sessions",
            "the release importer compares this first line byte for byte",
        )

    def test_published_files_exist_and_are_regular(self):
        for relative in PUBLISHED:
            with self.subTest(file=relative):
                path = LAB / relative
                self.assertFalse(path.is_symlink(), f"{relative} must be a regular file, not a link")
                self.assertTrue(path.is_file(), f"{relative} is on the publish allowlist but missing")
        for relative in FONTS:
            with self.subTest(font=relative):
                self.assertEqual(
                    (LAB / relative).read_bytes()[:4],
                    b"wOF2",
                    f"{relative} is not a woff2 file",
                )

    def test_no_external_resource_loads(self):
        self.assertEqual(
            [item.url for item in collect("index.html") if item.tag == "style url()"],
            [
                "assets/fonts/Geist-Regular.woff2",
                "assets/fonts/Geist-Medium.woff2",
                "assets/fonts/GeistMono-Regular.woff2",
            ],
            "index.html must load exactly the three fonts the importer copies",
        )
        offenders = [
            f"{page}: <{item.tag}> {item.url}"
            for page in PAGES
            for item in collect(page)
            # A `data:`/`blob:`/`filesystem:` URL is blocked wherever it appears —
            # even on a rel the CSP would otherwise ignore.
            if INLINE_SCHEME.match(item.url)
            or (item.fetched and EXTERNAL_ORIGIN.match(item.url))
        ]
        self.assertEqual(
            offenders,
            [],
            "the deployed page runs under default-src 'self'; these loads fail silently in production",
        )


if __name__ == "__main__":
    unittest.main()

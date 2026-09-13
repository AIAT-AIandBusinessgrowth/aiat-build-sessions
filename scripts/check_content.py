#!/usr/bin/env python3
"""Offline checks for this repository's Markdown links and learning units.

Uses only the Python standard library. Checks inline/image/reference links,
HTML href/src links, local files and GitHub-style heading anchors. Ignores
code examples, HTML comments, hidden folders and learning/local. This is a
checker for the Markdown used here, not a complete CommonMark renderer.
External URLs are deliberately not fetched: access does not verify a claim.

Run from any folder: python3 /path/to/aiat-build-sessions/scripts/check_content.py
Use --root PATH when checking a copy of the repository.
"""

import argparse
from datetime import date
import html
import os
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit


def blank(match):
    """Hide a match while preserving its source line numbers."""
    return "".join("\n" if char == "\n" else " " for char in match.group())


def visible_markdown(text):
    text = re.sub(r"<!--.*?-->", blank, text, flags=re.S)
    lines = []
    fence = None
    for line in text.splitlines(keepends=True):
        marker = re.match(r"^\s*(`{3,}|~{3,})", line)
        if fence is None and marker:
            fence = marker[1]
            lines.append("\n" if line.endswith("\n") else "")
        elif fence is not None:
            if re.match(r"^\s*" + re.escape(fence[0]) + "{" + str(len(fence)) + r",}\s*$", line):
                fence = None
            lines.append("\n" if line.endswith("\n") else "")
        else:
            lines.append(line)
    return "".join(lines)


def heading_anchors(text):
    """Match the heading spelling used by GitHub, including duplicate suffixes."""
    visible = visible_markdown(text)
    anchors = set(re.findall(r'<[^>]+\b(?:id|name)=["\']([^"\']+)["\']', visible))
    used = set()
    for line in visible.splitlines():
        match = re.match(r"^ {0,3}#{1,6}\s+(.+?)(?:\s+#+)?\s*$", line)
        if not match:
            continue
        title = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", match[1])
        title = re.sub(r"<[^>]+>", "", title)
        title = html.unescape(title).lower()
        base = re.sub(r"[^\w\- ]", "", title).replace(" ", "-")
        anchor = base
        suffix = 0
        while anchor in used:
            suffix += 1
            anchor = f"{base}-{suffix}"
        used.add(anchor)
        anchors.add(anchor)
    return anchors


def destination(text, start):
    """Read a Markdown destination, including angle brackets and parentheses."""
    cursor = start
    while cursor < len(text) and text[cursor].isspace():
        cursor += 1
    if cursor < len(text) and text[cursor] == "<":
        end = text.find(">", cursor + 1)
        return text[cursor + 1:end] if end >= 0 else None
    begin = cursor
    depth = 0
    while cursor < len(text):
        char = text[cursor]
        if char == "\\" and cursor + 1 < len(text):
            cursor += 2
            continue
        if char == "(":
            depth += 1
        elif char == ")":
            if depth == 0:
                break
            depth -= 1
        elif char.isspace():
            break
        cursor += 1
    return text[begin:cursor] if depth == 0 else None


def links(text):
    """Yield (line, destination, reference_error) for visible link syntax."""
    text = visible_markdown(text)
    text = re.sub(r"(`+)([^\n]*?)\1", blank, text)
    definitions = {}
    definition_lines = set()
    for match in re.finditer(r"^ {0,3}\[([^\]\n]+)\]:\s*", text, flags=re.M):
        label = " ".join(match[1].lower().split())
        target = destination(text, match.end())
        line = text.count("\n", 0, match.start()) + 1
        definition_lines.add(line)
        if target is not None:
            definitions[label] = target
            yield line, target, None
    for match in re.finditer(r"(?<!\\)\[[^\]\n]*\]\(", text):
        target = destination(text, match.end())
        if target is not None:
            yield text.count("\n", 0, match.start()) + 1, target, None
    for match in re.finditer(r"(?<!\\)\[([^\]\n]+)\]\[([^\]\n]*)\]", text):
        label = " ".join((match[2] or match[1]).lower().split())
        line = text.count("\n", 0, match.start()) + 1
        if label not in definitions:
            yield line, "", f"undefined link reference: {label}"
    # Shortcut references such as [setup]; ordinary bracketed prose and task
    # checkboxes are only links when a matching definition exists.
    for match in re.finditer(r"(?<![\\\]])\[([^\]\n]+)\](?![\[(])", text):
        label = " ".join(match[1].lower().split())
        line = text.count("\n", 0, match.start()) + 1
        if label in definitions and line not in definition_lines:
            yield line, definitions[label], None
    for match in re.finditer(r'<[^>]+\b(?:href|src)=["\']([^"\']+)["\']', text):
        yield text.count("\n", 0, match.start()) + 1, match[1], None


def excluded_path(path, root):
    """Apply the same private-content boundary to discovery and linked files."""
    parts = path.relative_to(root).parts
    return any(part.startswith(".") for part in parts) or parts[:2] == ("learning", "local")


def markdown_files(root):
    # Prune before descending, rather than enumerating private folder contents
    # and filtering their filenames afterwards. Do not follow directory links.
    for folder, directories, filenames in os.walk(root, topdown=True, followlinks=False):
        parent = Path(folder)
        directories[:] = sorted(
            name for name in directories
            if not excluded_path(parent / name, root) and not (parent / name).is_symlink()
        )
        for name in sorted(filenames):
            path = parent / name
            if path.suffix == ".md" and not excluded_path(path, root) and not path.is_symlink():
                yield path


def check_unit(path, text):
    """Check observable unit structure, without prescribing its prose."""
    kind = path.parts[0]
    if kind not in {"tracks", "diy"}:
        return []
    visible = visible_markdown(text)
    errors = []
    for field in ("Prerequisites", "Time", "Outcome", "Last verified"):
        match = re.search(r"^\|\s*\*\*" + field + r"\*\*\s*\|\s*([^|]+)\|", visible, re.M)
        if not match or not match[1].strip():
            errors.append(f"unit is missing metadata: {field}")
        elif field == "Last verified":
            try:
                if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", match[1].strip()):
                    raise ValueError
                date.fromisoformat(match[1].strip())
            except ValueError:
                errors.append("Last verified must be a calendar date in YYYY-MM-DD format")
    sections = ["Why this matters", "Do it", "Done when"]
    sections += ["Data note", "Next"] if kind == "tracks" else ["Watch out", "Sources"]
    for section in sections:
        if not re.search(r"^## " + section + r"\s*$", visible, re.M):
            errors.append(f"unit is missing section: {section}")
    done = re.search(r"^## Done when\s*\n(.*?)(?=^## |\Z)", visible, re.M | re.S)
    if done and not re.search(r"^\s*- \[[ xX]\] \S", done[1], re.M):
        errors.append("Done when needs an observable checklist")
    return errors


def check_repository(root):
    root = Path(root).resolve()
    issues = []
    files = list(markdown_files(root))
    if not files:
        return ["No Markdown files found in the chosen root."], 0, 0
    anchors = {}
    count = 0
    for path in files:
        relative = path.relative_to(root)
        try:
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeError):
            issues.append(f"{relative}: cannot read UTF-8 Markdown")
            continue
        issues.extend(f"{relative}: {issue}" for issue in check_unit(relative, text))
        for line, target, error in links(text):
            count += 1
            prefix = f"{relative}:{line}: "
            if error:
                issues.append(prefix + error)
                continue
            target = html.unescape(re.sub(r"\\([\\ ()])", r"\1", target))
            try:
                url = urlsplit(target)
            except ValueError:
                issues.append(prefix + "invalid link destination")
                continue
            if url.scheme or url.netloc:
                continue
            decoded = unquote(url.path)
            if not decoded:
                lexical = path
            elif decoded.startswith("/"):
                lexical = root / decoded.lstrip("/")
            else:
                lexical = path.parent / decoded
            # Normalise without filesystem access, then reject excluded targets
            # before checking existence or reading a heading. Repeat after
            # symlink resolution so a public alias cannot expose private files.
            lexical = Path(os.path.abspath(lexical))
            if not lexical.is_relative_to(root):
                issues.append(prefix + "link leaves the repository")
                continue
            if excluded_path(lexical, root):
                issues.append(prefix + "link points to excluded local content")
                continue
            resolved = lexical.resolve()
            if not resolved.is_relative_to(root):
                issues.append(prefix + "link leaves the repository")
            elif excluded_path(resolved, root):
                issues.append(prefix + "link points to excluded local content")
            elif not resolved.exists():
                issues.append(prefix + f"missing local file: {target}")
            elif url.fragment and resolved.suffix == ".md":
                if resolved not in anchors:
                    try:
                        anchors[resolved] = heading_anchors(resolved.read_text(encoding="utf-8"))
                    except (OSError, UnicodeError):
                        issues.append(prefix + f"cannot read linked Markdown: {target}")
                        continue
                if unquote(url.fragment) not in anchors[resolved]:
                    issues.append(prefix + f"missing heading: {target}")
    return issues, len(files), count


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    issues, files, count = check_repository(args.root)
    for issue in issues:
        print(issue, file=sys.stderr)
    print(f"Checked {files} Markdown files and {count} links; {len(issues)} issues.")
    return 1 if issues else 0


if __name__ == "__main__":
    sys.exit(main())

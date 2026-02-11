"""Core conversion logic — Markdown to HTML to PDF."""

from __future__ import annotations

import sys
from pathlib import Path

import markdown
from weasyprint import HTML

# ---------------------------------------------------------------------------
# Default stylesheet – clean, professional, print-friendly
# ---------------------------------------------------------------------------

DEFAULT_CSS = """\
@page {
    size: A4;
    margin: 2.5cm 2cm;
}

body {
    font-family: "Segoe UI", "Helvetica Neue", Arial, sans-serif;
    font-size: 12pt;
    line-height: 1.6;
    color: #1a1a1a;
    max-width: 100%;
}

/* ── Headings ────────────────────────────────────────────────── */
h1, h2, h3, h4, h5, h6 {
    color: #111;
    margin-top: 1.4em;
    margin-bottom: 0.6em;
    line-height: 1.3;
}
h1 { font-size: 2em;   border-bottom: 2px solid #ddd; padding-bottom: 0.3em; }
h2 { font-size: 1.5em; border-bottom: 1px solid #eee; padding-bottom: 0.25em; }
h3 { font-size: 1.25em; }

/* ── Paragraphs & links ──────────────────────────────────────── */
p {
    margin: 0.8em 0;
    text-align: justify;
}
a {
    color: #0366d6;
    text-decoration: none;
}

/* ── Lists ───────────────────────────────────────────────────── */
ul, ol {
    padding-left: 1.8em;
    margin: 0.6em 0;
}
li {
    margin: 0.25em 0;
}

/* ── Code ────────────────────────────────────────────────────── */
code {
    font-family: "Fira Code", "Cascadia Code", "Consolas", monospace;
    font-size: 0.9em;
    background: #f5f5f5;
    padding: 0.15em 0.35em;
    border-radius: 4px;
}
pre {
    background: #f6f8fa;
    border: 1px solid #e1e4e8;
    border-radius: 6px;
    padding: 1em;
    overflow-x: auto;
    line-height: 1.45;
}
pre code {
    background: transparent;
    padding: 0;
}

/* ── Blockquotes ─────────────────────────────────────────────── */
blockquote {
    margin: 1em 0;
    padding: 0.5em 1em;
    border-left: 4px solid #dfe2e5;
    color: #555;
    background: #fafafa;
}

/* ── Tables ──────────────────────────────────────────────────── */
table {
    border-collapse: collapse;
    width: 100%;
    margin: 1em 0;
}
th, td {
    border: 1px solid #dfe2e5;
    padding: 0.6em 1em;
    text-align: left;
}
th {
    background: #f6f8fa;
    font-weight: 600;
}
tr:nth-child(even) {
    background: #fafbfc;
}

/* ── Horizontal rule ─────────────────────────────────────────── */
hr {
    border: none;
    border-top: 1px solid #e1e4e8;
    margin: 2em 0;
}

/* ── Images ──────────────────────────────────────────────────── */
img {
    max-width: 100%;
    height: auto;
}
"""

# Markdown extensions to enable
_MD_EXTENSIONS = [
    "fenced_code",
    "tables",
    "toc",
    "codehilite",
    "smarty",
    "attr_list",
]


# ---------------------------------------------------------------------------
# Conversion helpers
# ---------------------------------------------------------------------------

def md_to_html(md_text: str) -> str:
    """Convert raw Markdown text to an HTML fragment."""
    return markdown.markdown(md_text, extensions=_MD_EXTENSIONS)


def wrap_html(body: str, css: str = DEFAULT_CSS) -> str:
    """Wrap an HTML body fragment in a complete HTML document with CSS."""
    return (
        "<!DOCTYPE html>\n"
        '<html lang="en">\n'
        "<head>\n"
        '  <meta charset="utf-8">\n'
        f"  <style>\n{css}\n  </style>\n"
        "</head>\n"
        f"<body>\n{body}\n</body>\n"
        "</html>"
    )


def _read_md(path: Path) -> str:
    """Read a Markdown file and return its text content."""
    if not path.exists():
        print(f"Error: file not found — {path}", file=sys.stderr)
        sys.exit(1)
    if not path.suffix.lower() == ".md":
        print(f"Error: expected a .md file, got — {path}", file=sys.stderr)
        sys.exit(1)
    return path.read_text(encoding="utf-8")


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

PAGE_BREAK = '<div style="page-break-after: always;"></div>'


def convert_single(input_path: str | Path, output_path: str | Path | None = None) -> Path:
    """Convert a single Markdown file to PDF.

    Parameters
    ----------
    input_path:
        Path to the ``.md`` source file.
    output_path:
        Optional destination path for the PDF.  Defaults to the same
        basename with a ``.pdf`` extension in the current directory.

    Returns
    -------
    Path
        The path to the generated PDF file.
    """
    src = Path(input_path)
    dst = Path(output_path) if output_path else src.with_suffix(".pdf")

    md_text = _read_md(src)
    html_body = md_to_html(md_text)
    full_html = wrap_html(html_body)

    HTML(string=full_html, base_url=str(src.parent)).write_pdf(str(dst))
    print(f"✔  {src}  →  {dst}")
    return dst


def convert_merged(
    input_paths: list[str | Path],
    output_path: str | Path = "merged_output.pdf",
) -> Path:
    """Merge multiple Markdown files into one PDF.

    A CSS page break is inserted between each file's content.

    Parameters
    ----------
    input_paths:
        List of ``.md`` file paths.
    output_path:
        Destination path for the merged PDF.  Defaults to
        ``merged_output.pdf``.

    Returns
    -------
    Path
        The path to the generated PDF file.
    """
    sections: list[str] = []
    base_dir = Path(".")

    for p in input_paths:
        src = Path(p)
        md_text = _read_md(src)
        sections.append(md_to_html(md_text))
        # Use the directory of the first file as the base URL
        if base_dir == Path("."):
            base_dir = src.parent

    combined_body = f"\n{PAGE_BREAK}\n".join(sections)
    full_html = wrap_html(combined_body)
    dst = Path(output_path)

    HTML(string=full_html, base_url=str(base_dir)).write_pdf(str(dst))
    print(f"✔  Merged {len(input_paths)} file(s)  →  {dst}")
    return dst

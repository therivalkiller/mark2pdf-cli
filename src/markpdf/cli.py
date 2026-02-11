"""CLI entry point for markpdf."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from markpdf import __version__
from markpdf.converter import convert_merged, convert_single


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="markpdf",
        description="Convert Markdown files into beautifully styled PDFs.",
        epilog="Examples:\n"
               "  markpdf README.md\n"
               "  markpdf ch1.md ch2.md ch3.md\n"
               "  markpdf ch1.md ch2.md -m -o book.pdf\n",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "files",
        nargs="+",
        help="One or more Markdown (.md) files to convert.",
    )
    parser.add_argument(
        "-m", "--merge",
        action="store_true",
        default=False,
        help="Merge all input files into a single PDF (with page breaks between files).",
    )
    parser.add_argument(
        "-o", "--output",
        type=str,
        default=None,
        help="Output filename. In merge mode defaults to 'merged_output.pdf'; "
             "in separate mode sets the name for a single-file conversion.",
    )
    parser.add_argument(
        "-v", "--version",
        action="version",
        version=f"%(prog)s {__version__}",
    )
    return parser


def main(argv: list[str] | None = None) -> None:
    """Parse arguments and dispatch to the converter."""
    parser = _build_parser()
    args = parser.parse_args(argv)

    # ── Validate inputs ────────────────────────────────────────
    for f in args.files:
        p = Path(f)
        if not p.exists():
            parser.error(f"File not found: {f}")
        if p.suffix.lower() != ".md":
            parser.error(f"Expected a .md file, got: {f}")

    # ── Merge mode ─────────────────────────────────────────────
    if args.merge:
        output = args.output if args.output else "merged_output.pdf"
        convert_merged(args.files, output)
        return

    # ── Separate mode (default) ────────────────────────────────
    if args.output and len(args.files) > 1:
        parser.error("--output can only be used with a single file in separate mode. "
                      "Use --merge to combine files into one PDF.")

    for f in args.files:
        convert_single(f, args.output)


if __name__ == "__main__":
    main()

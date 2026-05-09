<p align="center">
  <h1 align="center">📄 markpdf-cli</h1>
  <p align="center">
    <strong>Convert Markdown to beautifully styled PDFs — from the terminal.</strong>
  </p>
  <p align="center">
    <a href="https://pypi.org/project/markpdf-cli/"><img src="https://img.shields.io/pypi/v/markpdf-cli?color=blue&label=PyPI" alt="PyPI"></a>
    <a href="https://pypi.org/project/markpdf-cli/"><img src="https://img.shields.io/pypi/pyversions/markpdf-cli" alt="Python"></a>
    <a href="https://github.com/therivalkiller/markpdf-cli/blob/main/LICENSE"><img src="https://img.shields.io/badge/license-MIT-green" alt="License"></a>
  </p>
</p>

---

**markpdf-cli** is a lightweight command-line tool that takes your `.md` files and produces clean, print-ready PDF documents with professional styling — no configuration needed..

Built with [`python-markdown`](https://python-markdown.github.io/) for parsing and [`WeasyPrint`](https://weasyprint.readthedocs.io/) for rendering.

---

## ⚡ Quick Start

```bash
pip install markpdf-cli
markpdf README.md
```

That's it. You now have a `README.pdf` with beautiful typography and styling.

---

## 🚀 Installation

### From PyPI

```bash
pip install markpdf-cli
```

### From source

```bash
git clone https://github.com/therivalkiller/markpdf-cli.git
cd markpdf-cli
pip install .
```

### System dependencies

WeasyPrint requires some system libraries. Install them **before** using markpdf:

<details>
<summary><strong>Ubuntu / Debian</strong></summary>

```bash
sudo apt update
sudo apt install -y libpango-1.0-0 libpangocairo-1.0-0 libgdk-pixbuf2.0-0 libffi-dev libcairo2
```

</details>

<details>
<summary><strong>macOS (Homebrew)</strong></summary>

```bash
brew install pango libffi
```

</details>

---

## 📖 Usage

### Convert a single file

```bash
markpdf report.md
# → report.pdf
```

### Custom output name

```bash
markpdf report.md -o final-report.pdf
# → final-report.pdf
```

### Convert multiple files (separate PDFs)

```bash
markpdf ch1.md ch2.md ch3.md
# → ch1.pdf  ch2.pdf  ch3.pdf
```

### Merge multiple files into one PDF

```bash
markpdf ch1.md ch2.md ch3.md --merge
# → merged_output.pdf  (page breaks between each file)
```

### Merge with a custom name

```bash
markpdf ch1.md ch2.md ch3.md -m -o book.pdf
# → book.pdf
```

---

## 🐍 Use as a Python library

You can also import `markpdf` directly in your scripts:

```python
from markpdf.converter import convert_single, convert_merged

# Single file
convert_single("notes.md", "notes.pdf")

# Merge multiple files
convert_merged(["ch1.md", "ch2.md", "ch3.md"], "book.pdf")
```

---

## 🏗️ Project Structure

```
markpdf-cli/
├── pyproject.toml          # Build config & metadata
├── README.md
├── .gitignore
└── src/
    └── markpdf/
        ├── __init__.py     # Version
        ├── cli.py          # CLI entry point (argparse)
        └── converter.py    # Core MD → HTML → PDF logic
```

---

## 🤝 Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

```bash
git clone https://github.com/therivalkiller/markpdf-cli.git
cd markpdf-cli
pip install -e .
```

---

## 📄 License

MIT © [Amritanshu](https://github.com/therivalkiller)

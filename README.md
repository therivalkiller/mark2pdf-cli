# markpdf-cli

A fast, clean CLI tool to convert **Markdown** files into beautifully styled **PDFs**.

Built with [`markdown`](https://python-markdown.github.io/) and [`WeasyPrint`](https://weasyprint.readthedocs.io/).

---

## ✨ Features

- 📄 Convert one or many `.md` files to PDF in one command.
- 🔀 **Merge mode** — combine multiple Markdown files into a single PDF with page breaks.
- 🎨 Professional, print-ready CSS styling out of the box.
- 📦 Installable as a Python package; works as a `markpdf` command.

---

## 📋 Prerequisites

WeasyPrint depends on system libraries. On **Ubuntu / Debian**, install them first:

```bash
sudo apt update
sudo apt install -y libpango-1.0-0 libpangocairo-1.0-0 libgdk-pixbuf2.0-0 libffi-dev libcairo2
```

On **macOS** (Homebrew):

```bash
brew install pango libffi
```

---

## 🚀 Installation

### From PyPI (once published)

```bash
pip install markpdf-cli
```

### From source

```bash
git clone https://github.com/amritanshu/markpdf-cli.git
cd markpdf-cli
pip install .
```

### Development install

```bash
pip install -e .
```

---

## 📖 Usage

### Convert a single file

```bash
markpdf README.md
# → produces README.pdf
```

### Convert a single file with a custom output name

```bash
markpdf README.md -o documentation.pdf
# → produces documentation.pdf
```

### Convert multiple files (separate PDFs)

```bash
markpdf chapter1.md chapter2.md chapter3.md
# → produces chapter1.pdf, chapter2.pdf, chapter3.pdf
```

### Merge multiple files into one PDF

```bash
markpdf chapter1.md chapter2.md chapter3.md --merge
# → produces merged_output.pdf
```

### Merge with a custom output name

```bash
markpdf chapter1.md chapter2.md chapter3.md -m -o book.pdf
# → produces book.pdf
```

### Show version

```bash
markpdf --version
```

---

## 🏗️ Publishing to PyPI

### 1. Build the package

```bash
pip install build
python -m build
```

This creates `dist/markpdf_cli-0.1.0.tar.gz` and `dist/markpdf_cli-0.1.0-py3-none-any.whl`.

### 2. Upload to TestPyPI

```bash
pip install twine
twine upload --repository testpypi dist/*
```

You'll need an API token from [TestPyPI](https://test.pypi.org/manage/account/#api-tokens).

### 3. Verify from TestPyPI

```bash
python -m venv /tmp/test-markpdf && source /tmp/test-markpdf/bin/activate
pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ markpdf-cli
markpdf --version
deactivate
```

### 4. Upload to production PyPI

```bash
twine upload dist/*
```

---

## 📄 License

MIT

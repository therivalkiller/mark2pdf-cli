---
description: How to build and publish the markpdf-cli package to PyPI
---

# Publishing markpdf-cli to PyPI (Ubuntu)

End-to-end guide to build, upload, and verify the package.

## Prerequisites

```bash
# System libraries required by WeasyPrint
sudo apt update
sudo apt install -y libpango-1.0-0 libpangocairo-1.0-0 libgdk-pixbuf2.0-0 libffi-dev libcairo2

# Python packaging tools
pip install build twine
```

## Step 1 — Build the package

// turbo
```bash
cd markpdf-cli
python -m build
```

This generates two artifacts in `dist/`:
- `markpdf_cli-0.1.0.tar.gz` (sdist)
- `markpdf_cli-0.1.0-py3-none-any.whl` (wheel)

## Step 2 — Upload to TestPyPI

1. Create an account on https://test.pypi.org if you don't have one.
2. Generate an API token at https://test.pypi.org/manage/account/#api-tokens.
3. Upload:

```bash
twine upload --repository testpypi dist/*
```

When prompted:
- **Username:** `__token__`
- **Password:** paste your TestPyPI API token

## Step 3 — Verify from TestPyPI

```bash
python -m venv /tmp/test-markpdf
source /tmp/test-markpdf/bin/activate

pip install \
  --index-url https://test.pypi.org/simple/ \
  --extra-index-url https://pypi.org/simple/ \
  markpdf-cli

# Smoke test
markpdf --version

# Clean up
deactivate
rm -rf /tmp/test-markpdf
```

> `--extra-index-url` pulls dependencies (markdown, weasyprint) from the real PyPI since they won't exist on TestPyPI.

## Step 4 — Upload to production PyPI

Once satisfied with the test:

```bash
twine upload dist/*
```

Use your production PyPI token when prompted.

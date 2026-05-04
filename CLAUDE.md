# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a literate programming research project that creates academic documentation about literate programming methodologies. The project uses LaTeX for document preparation and Noweb for literate programming demonstrations.

## Technology Stack

- **LaTeX**: Primary document preparation system (requires `-shell-escape` flag for minted package)
- **Noweb**: Literate programming tool for creating documented code examples
- **Make**: Build system using custom makefiles from the `makefiles/` submodule
- **Python 3**: For code examples and testing (pytest, black formatter)
- **Git**: With submodules for external dependencies

## Build Commands

### Building Documents
```bash
# Build all documents (lpbook.pdf, lpbook-teachers.pdf, slides.pdf)
make

# Build specific documents
make -C src lpbook.pdf
make -C src lpbook-teachers.pdf
make -C src slides.pdf

# Create a release and publish to GitHub.
# NOTE: this also runs `git push --all -u` and creates a `gh release`.
make publish
```

### Testing
```bash
# Run Python tests (uses pytest)
make -C src test
```

### Cleaning
```bash
# Clean all build artifacts
make clean

# Clean only src directory
make -C src clean
```

## Key File Types

### .nw (Noweb) Files
Literate programming source files that combine documentation and code. Structure:
- LaTeX documentation sections with `\section{}`, `\subsection{}`, etc.
- Code chunks defined with `<<chunk name>>=` and ending with `@`
- Code chunks can reference other chunks: `<<another chunk>>`
- Extract code with: `notangle -R"chunk name" file.nw`
- Generate LaTeX with: `noweave file.nw`

**IMPORTANT**: Do not manually edit `.tex` or `.py` files that are generated from `.nw` files. Always edit the source `.nw` file instead.

The `.nw` examples in `src/` each demonstrate a different facet of literate
programming:
- `cppjava.nw` — same `Fraction` example tangled to both C++ and Java
- `doctest.nw` — Python doctest-style literate tests
- `fib.nw` — small first example (Fibonacci)
- `introsort.nw` — only example with extracted `pytest` tests (`test_introsort.py`)
- `merge.nw` — shell-script tangling
- `noweb.mk.nw` — literate version of the project's own makefile rules
- `whatis.nw` — narrative chapter on what literate programming is

A second self-contained example lives in `tutorial-java/Fraction.nw` (with
JUnit) and is built independently from its own Makefile.

### .tex Files
LaTeX document sources. Key files:
- `src/lpbook.tex`: Main book manuscript
- `src/lpbook-teachers.tex`: Teacher's edition with additional content
- `src/slides-intro.tex`: Presentation slides (renamed from `slides.tex` in
  commit `06f9ea8`; the `src/Makefile` target `slides.pdf: slides.tex` is
  currently out of date)
- `src/preamble.tex`: LaTeX package imports and configuration
- `src/contents.tex`: Table of contents structure

## Project Structure

```
├── src/                    # Main source directory
│   ├── *.nw               # Noweb literate programming files
│   ├── *.tex              # LaTeX document sources
│   ├── figs/              # Figure assets
│   └── Makefile           # Build configuration for documents
├── tutorial-java/         # Self-contained Java/JUnit Noweb example (Fraction.nw)
├── makefiles/             # Git submodule with custom build system makefiles
├── didactic/              # Git submodule: LaTeX package for typesetting educational material
├── weblogin/              # Git submodule: Python package written using literate programming (used as example)
├── requirements.txt       # Python deps (weblogin, Pygments, lxml, requests, …)
└── python/                # Python virtual environment populated from requirements.txt (ignored in git)
```

## Noweb Workflow

### Extracting Code from .nw Files
```bash
# Extract specific code chunk
notangle -R"chunk name" file.nw > output-file

# Extract with cpif (copy if different - prevents unnecessary rebuilds)
notangle -R"chunk name" file.nw | cpif output-file
```

### Generating LaTeX from .nw Files
```bash
# Generate LaTeX documentation
noweave file.nw > output.tex
```

### Common Noweb Patterns
Code chunks in .nw files follow this structure:
```
\section{Documentation}
Explanation of what the code does.

<<file.py>>=
"""Module docstring"""
<<imports>>
<<main function>>
@

<<imports>>=
import sys
@

<<main function>>=
def main():
    pass
@
```

## LaTeX Compilation

The project uses `latexmk` with `pdflatex` and the `-shell-escape` flag (required for the minted package for syntax highlighting).

### Common LaTeX Tools
- `pdflatex -shell-escape`: Primary compiler
- `biber`/`bibtex`: Bibliography processing
- `latexmk`: Automated building (handles multiple passes)

## Python Code Standards

- Python 3.x
- Black formatter with line length 79: `black --line-length 79 file.py`
- pytest for testing
- Follow PEP 8 style guidelines

## Makefile System

The project uses a modular makefile system (from the `makefiles/` submodule) inspired by BSD ports:

### Key Variables
- `INCLUDE_MAKEFILES`: Points to the makefiles directory (usually `../makefiles`)
- `INCLUDE_DIDACTIC`: Points to the didactic directory (usually `../didactic`)

### Common Makefile Includes
```makefile
INCLUDE_MAKEFILES=../makefiles
include ${INCLUDE_MAKEFILES}/tex.mk
include ${INCLUDE_MAKEFILES}/noweb.mk
include ${INCLUDE_MAKEFILES}/subdir.mk
```

### Makefile Targets
The makefiles provide standard targets:
- `all`: Build all documents
- `clean`: Remove generated files
- `test`: Run tests (for Python code)

## Adding New Content

To add a new Noweb example, declare it in `src/Makefile` next to the
existing entries — see the `${NOTANGLE}` and `${NOTANGLE.cxx}` rules
(e.g. how `Fraction2.java` and `fracexample2.cpp` are derived from
`cppjava.nw`, and how `test_introsort.py` is extracted from `introsort.nw`)
for the canonical pattern.

Figures live in `src/figs/` and are built by `src/figs/Makefile`; reference
them via `\includegraphics{figs/filename}`. Bibliography entries go in
`src/bibliography.bib` and are cited with `\cite{}` / `\textcite{}`.

## Code Conventions

### LaTeX Conventions
- Use `\input{}` for modular organization (not `\include{}`)
- Use semantic markup over presentational
- Bibliography style: author-year

### Noweb Conventions
- Document all code chunks with clear explanations — explain the *why*
- Use meaningful chunk names that describe functionality
- Even simple chunks should be explained

## Dependencies

Required tools:
- LaTeX distribution (TeXLive recommended)
- Noweb tools (`apt-get install noweb` on Debian/Ubuntu) — provides
  `notangle`, `noweave`, and `cpif`
- GNU Make
- Python 3.x with `pytest` and `black`; install Python deps with
  `pip install -r requirements.txt`
- Git with submodule support

### Submodules
Initialize submodules after cloning (or if `makefiles/`, `didactic/`, or
`weblogin/` appear empty):
```bash
git submodule update --init --recursive
```

## Project-specific gotchas

- **Chunk not defined / tangling errors**: every `<<name>>` reference must
  have a matching `<<name>>=` definition; chunks end with a lone `@` on its
  own line.
- **`slides.pdf` target is currently broken**: `src/Makefile` references
  `slides.tex`, but the source has been renamed to `slides-intro.tex`
  (see issue #40).

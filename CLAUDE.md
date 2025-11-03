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

# Create a release and publish to GitHub
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

### .tex Files
LaTeX document sources. Key files:
- `src/lpbook.tex`: Main book manuscript
- `src/lpbook-teachers.tex`: Teacher's edition with additional content
- `src/slides.tex`: Presentation slides
- `src/preamble.tex`: LaTeX package imports and configuration
- `src/contents.tex`: Table of contents structure

## Project Structure

```
├── src/                    # Main source directory
│   ├── *.nw               # Noweb literate programming files
│   ├── *.tex              # LaTeX document sources
│   ├── figs/              # Figure assets
│   └── Makefile           # Build configuration for documents
├── makefiles/             # Git submodule with custom build system makefiles
├── didactic/              # Git submodule: LaTeX package for typesetting educational material
├── weblogin/              # Git submodule: Python package written using literate programming (used as example)
└── python/                # Python virtual environment (ignored in git)
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

### Adding a New Noweb Example
1. Create `src/example.nw` with literate documentation and code
2. Update `src/Makefile` to add dependencies:
   ```makefile
   SRC+=  example.tex example.py
   example.py: example.nw
       ${NOTANGLE}
   ```
3. Test compilation: `make -C src example.py`
4. If adding tests, update the `test` target

### Adding LaTeX Content
1. Create or modify `.tex` files in `src/`
2. Use `\input{filename}` to include in main documents (without .tex extension)
3. Update main document files (lpbook.tex, slides.tex) to reference new content
4. Test: `make -C src lpbook.pdf`

### Adding Figures
1. Place source files in `src/figs/`
2. Update `src/figs/Makefile` if figure needs processing
3. Reference with `\includegraphics{figs/filename}`
4. Use vector formats (PDF, SVG) when possible

### Adding Citations
1. Add BibTeX entry to `src/bibliography.bib`
2. Use `\cite{key}` or `\textcite{key}` in LaTeX sources
3. Include DOI and URL when available

## Code Conventions

### LaTeX Conventions
- Break lines at 80 columns
- Use `\input{}` for modular organization (not `\include{}`)
- Use semantic markup over presentational
- Maintain consistent bibliography style (author-year)

### Noweb Conventions
- Document all code chunks with clear explanations
- Use meaningful chunk names that describe functionality
- Explain the "why" in documentation, not just the "what"
- Keep documentation and code synchronized
- Even simple chunks should be explained

### File Organization
- All LaTeX sections should be broken into separate files and included via `\input{}`
- Keep source files in `src/` directory
- Figures and assets in appropriate subdirectories
- Use descriptive filenames

## Dependencies

Required tools:
- LaTeX distribution (TeXLive recommended)
- Noweb tools (`apt-get install noweb` on Debian/Ubuntu)
- GNU Make
- Python 3.x with pytest and black
- Git with submodule support
- `cpif` utility (comes with Noweb)

### Submodules
Initialize submodules after cloning:
```bash
git submodule update --init --recursive
```

## Common Issues

### LaTeX Errors
- **Shell escape errors**: Ensure `-shell-escape` flag is used (already configured in Makefiles)
- **Citation undefined**: Run LaTeX twice, or check `bibliography.bib`
- **File not found**: Check file paths and Makefile dependencies

### Noweb Errors
- **Chunk not defined**: Ensure all referenced chunks (e.g., `<<chunk name>>`) are defined somewhere
- **Tangling errors**: Check chunk syntax: `<<chunk name>>=` starts a definition, `@` ends it

### Git Submodule Issues
If makefiles or didactic directories are empty:
```bash
git submodule update --init --recursive
```

## Academic Context

This is an educational/research project focused on:
- Literature survey on literate programming
- Demonstrating literate programming techniques using Noweb
- Teaching software development methodologies
- Academic paper and book preparation

### Citation and Attribution
- Always cite sources properly using BibTeX
- Include version numbers and dates for software tools
- Test all code examples to ensure they work as documented

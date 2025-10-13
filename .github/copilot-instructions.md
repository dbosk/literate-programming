# GitHub Copilot Instructions for Literate Programming Project

## Project Overview
This is a literate programming research project that creates academic documentation about literate programming methodologies. The project uses LaTeX for document preparation and Noweb for literate programming demonstrations.

## Technology Stack
- **LaTeX**: Primary document preparation system for academic papers and books
- **Noweb**: Literate programming tool for creating documented code examples and for extracting compilable source files (e.g. .py) from the literate source files (.nw)
- **Make**: Build system for compiling LaTeX documents to PDF
- **Git**: Version control with submodules for external dependencies

## Project Structure
```
├── src/                    # Main source directory
│   ├── *.tex              # LaTeX document sources
│   ├── *.nw               # Noweb literate programming files
│   └── figs/              # Figure assets
├── makefiles/             # Build system makefiles
├── didactic/              # A LaTeX package for typesetting educational material
├── weblogin/              # A python package written using literate programming. Used as an example
└── README.md              # Project documentation
```

## File Types and Purpose
- **`.tex` files**: LaTeX document sources (main book, slides, abstracts)
- **`.nw` files**: Noweb literate programming examples demonstrating concepts
- **`.bib` files**: Bibliography databases for academic references
- **Makefile**: Build configuration for generating PDFs

## Key Files
- `src/lpbook.tex`: Main book manuscript
- `src/lpbook-teachers.tex`: Teacher's edition with additional content
- `src/slides.tex`: Presentation slides
- `src/bibliography.bib`: Academic reference database
- `src/contents.tex`: Table of contents structure
- `src/preamble.tex`: LaTeX package imports and configuration

## Build Process
The project uses Make to build PDFs from LaTeX sources:

### Building Documents
- `make`: Build all targets (lpbook.pdf, lpbook-teachers.pdf, slides.pdf)
- `make -C src`: Build all documents in the src directory
- `make -C src lpbook.pdf`: Build the main book only
- `make -C src slides.pdf`: Build presentation slides only
- `make publish`: Create release with generated PDFs and push to GitHub

### Testing
- `make -C src test`: Run Python tests (uses pytest for test_introsort.py)
- Test files are generated from Noweb (.nw) files using `notangle`

### Cleaning
- `make clean`: Remove all build artifacts and temporary files
- `make -C src clean`: Clean only the src directory

### Common Build Issues
- **Missing LaTeX packages**: Install TeXLive full distribution
- **Noweb not found**: Install noweb tools (`apt-get install noweb` on Debian/Ubuntu)
- **Shell escape errors**: LaTeX is configured with `-shell-escape` flag for minted package
- **Submodule issues**: Run `git submodule update --init --recursive`

## Coding Patterns and Conventions

### LaTeX Conventions
- Use semantic markup over presentational
- Maintain consistent bibliography style
- Structure documents with clear sections and subsections
- Use `\input{}` for modular document organization

### Noweb Conventions
- Document code chunks with clear explanations
- Use meaningful chunk names that describe functionality
- Maintain consistency between code and documentation
- Include compilation and execution examples

### File Organization
- Keep source files in `src/` directory
- Separate figures and assets in appropriate subdirectories
- Use descriptive filenames that indicate content purpose
- Maintain clean separation between different document types

## Tools and Utilities

### Noweb Commands
- `notangle`: Extract code from `.nw` files (e.g., `notangle -R"chunk name" file.nw`)
- `noweave`: Generate LaTeX documentation from `.nw` files
- `cpif`: Copy if different (prevents unnecessary rebuilds)

### LaTeX Tools
- `pdflatex`: Primary LaTeX compiler (with `-shell-escape` for minted)
- `biber`/`bibtex`: Bibliography processing
- `latexmk`: Automated LaTeX building (handles multiple passes)

### Python Tools (for examples)
- `pytest`: Testing framework for Python code examples
- `black`: Code formatter (line length 79)
- Python 3.x for running examples

## Example Patterns

### Creating a New Literate Program
```noweb
\section{My Feature}
This is the documentation explaining the feature.

<<my-feature.py>>=
#!/usr/bin/env python3
"""Module documentation string."""

<<imports>>
<<main function>>
@

<<imports>>=
import sys
@

<<main function>>=
def main():
    """Main function."""
    pass
@
```

### Adding to Bibliography
```bibtex
@article{AuthorYear,
  title = {Paper Title},
  author = {Author, First and Author, Second},
  journal = {Journal Name},
  year = {2024},
  volume = {1},
  pages = {1--10},
  doi = {10.xxxx/xxxxx},
  URL = {https://example.com/paper},
}
```

### LaTeX Figure Inclusion
```latex
\begin{figure}
  \centering
  \includegraphics[width=0.8\textwidth]{figs/example.pdf}
  \caption{Figure caption explaining the content.}
  \label{fig:example}
\end{figure}
```

## Dependencies and Requirements
- LaTeX distribution (TeXLive or MiKTeX)
- Noweb literate programming tools
- Make build system
- Git with submodule support

## Academic Context
This is an educational/research project focused on:
- Literature survey on literate programming
- Demonstrating literate programming techniques
- Teaching software development methodologies
- Academic paper and book preparation

## Best Practices for Contributions
- Maintain academic writing standards
- Ensure proper citations and references
- Test LaTeX compilation before committing
- Follow established document structure patterns
- Keep code examples functional and well-documented

## Common Tasks
- Adding new literate programming examples
- Updating bibliography with recent research
- Modifying document structure and layout
- Creating educational materials and exercises
- Generating publication-ready PDFs

## Development Workflow

### When Adding New Content
1. Create or modify `.nw` (Noweb) or `.tex` (LaTeX) files in `src/`
2. Update `src/Makefile` to include new dependencies if needed
3. Test compilation: `make -C src <target>.pdf`
4. If adding code examples, extract and test them: `make -C src test`
5. Verify PDF output quality before committing

### When Adding Citations
1. Add BibTeX entry to `src/bibliography.bib`
2. Use `\cite{key}` or `\textcite{key}` in LaTeX sources
3. Ensure consistent citation style (author-year for academic papers)
4. Include DOI and URL when available

### When Adding Figures
1. Place source files in `src/figs/`
2. Update `src/figs/Makefile` if figure needs processing
3. Reference figures with `\includegraphics` and proper labels
4. Use vector formats (PDF, SVG) when possible for scalability

## Testing and Validation

### LaTeX Compilation
- All `.tex` files must compile without errors
- Warnings should be investigated and resolved when possible
- Use `\input{}` for modular organization, not `\include{}`

### Code Examples
- Code chunks in `.nw` files should be executable
- Python code should follow PEP 8 style (black formatter is used)
- Test extracted code with `make -C src test`
- Document expected input/output in literate comments

### Bibliography Validation
- All citations must have corresponding BibTeX entries
- Check for duplicate entries
- Verify URLs are accessible
- Include version numbers for software references

## Error Handling

### Common LaTeX Errors
- **Undefined control sequence**: Missing package or typo in command
- **Missing $ inserted**: Math mode syntax error
- **File not found**: Check file paths and Makefile dependencies
- **Citation undefined**: Run LaTeX twice, or check bibliography.bib

### Noweb-Specific Issues
- **Chunk not defined**: Ensure all referenced chunks exist
- **Tangling errors**: Check chunk syntax `<<chunk name>>=`
- **Weaving errors**: Verify LaTeX compatibility in documentation chunks

## Security and Academic Integrity

### Citations and Attribution
- Always cite sources properly using BibTeX
- Include version numbers and dates for software tools
- Verify license compatibility for included code examples
- Attribute all external figures and diagrams

### Code Examples
- Use placeholder data, not real personal information
- Include copyright notices for substantial code snippets
- Test all code examples to ensure they work as documented
- Document any external dependencies clearly
# GitHub Copilot Instructions for Literate Programming Project

## Project Overview
This is a literate programming research project that creates academic documentation about literate programming methodologies. The project uses LaTeX for document preparation and Noweb for literate programming demonstrations.

## Technology Stack
- **LaTeX**: Primary document preparation system for academic papers and books
- **Noweb**: Literate programming tool for creating documented code examples
- **Make**: Build system for compiling LaTeX documents to PDF
- **Git**: Version control with submodules for external dependencies

## Project Structure
```
├── src/                    # Main source directory
│   ├── *.tex              # LaTeX document sources
│   ├── *.nw               # Noweb literate programming files
│   └── figs/              # Figure assets
├── makefiles/             # Build system makefiles
├── didactic/              # Educational materials
├── weblogin/              # Web-related components
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
- `make`: Build all targets
- `make publish`: Create release with generated PDFs
- Individual targets available in `src/` directory

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
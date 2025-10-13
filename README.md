# Literate Programming Research Project

A comprehensive survey and educational resource on literate programming research and methodologies.

## About
This project contains academic research and educational materials about literate programming, including:
- A comprehensive survey of literate programming techniques
- Practical examples using Noweb
- Educational slides and presentations
- Teacher resources and exercises

## Building
The project uses LaTeX and Make for document generation:

```bash
# Build all documents
make

# Build specific documents
make -C src lpbook.pdf
make -C src slides.pdf

# Create a release
make publish
```

## Structure
- `src/` - Main LaTeX and Noweb source files
- `didactic/` - A LaTeX package for typesetting educational materials
- `weblogin/` - A Python package used to log in to web services. Here it's included as an example, since it's written using literate programming
- `makefiles/` - Build system configuration

## Requirements
- LaTeX distribution (TeXLive recommended)
- Noweb literate programming tools
- Make build system
- Git with submodule support

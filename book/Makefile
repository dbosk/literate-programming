.PHONY: all
all: lpbook.pdf

LATEXFLAGS+=	-shell-escape

SRC+=		preamble.tex
SRC+=		bibliography.bib
SRC+=		abstract.tex contents.tex

DEPENDS+=	../whatis
DEPENDS+=	../introsort

lpbook.pdf: lpbook.tex didactic.sty ${SRC}

${DEPENDS}::
	${MAKE} -C $@ all

BIBLIOGRAPHY+=	../whatis/bibliography.bib
BIBLIOGRAPHY+=	../introsort/bibliography.bib

bibliography.bib: ${BIBLIOGRAPHY}
	${BIBTOOL} ${BIBTOOLFLAGS} -o $@ $^

.PHONY: clean
clean:
	${RM} lpbook.pdf
	${RM} didactic_output_*
	${RM} didactic_code_*


INCLUDE_MAKEFILES=../makefiles
include ${INCLUDE_MAKEFILES}/tex.mk
include ${INCLUDE_MAKEFILES}/noweb.mk
INCLUDE_DIDACTIC=../didactic
include ${INCLUDE_DIDACTIC}/didactic.mk

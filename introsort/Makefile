.PHONY: all
all: notes.pdf slides.pdf

LATEXFLAGS+=	-shell-escape

SRC+=		preamble.tex
SRC+=		abstract.tex contents.tex
SRC+=		introsort.tex introsort.py
SRC+=		test_introsort.py
SRC+=		tests_Makefile

notes.pdf: notes.tex didactic.sty
notes.pdf: ${SRC} ${FIGS}

slides.pdf: slides.tex didactic.sty
slides.pdf: ${SRC} ${FIGS}

contents.tex: introsort.nw
	${NOWEAVE.tex}

${FIGS}::
	${MAKE} -C $(dir $@) $(notdir $@)

tests_Makefile: introsort.nw
	notangle -RMakefile introsort.nw | cpif $@

.PHONY: test
test: test_introsort.py introsort.py
	python3 -m pytest test_introsort.py

test_introsort.py: introsort.nw
	notangle -R"test introsort.py" $< | cpif $@
	black $@

.PHONY: clean
clean:
	${RM} notes.pdf slides.pdf
	${RM} contents.tex
	${RM} introsort.py introsort.tex
	${RM} test_introsort.py tmp_minted_output.py
	${RM} -R __pycache__
	${RM} tests_Makefile
	${RM} didactic_output_*
	${RM} didactic_code_*


INCLUDE_MAKEFILES=../makefiles
include ${INCLUDE_MAKEFILES}/tex.mk
include ${INCLUDE_MAKEFILES}/noweb.mk
INCLUDE_DIDACTIC=../didactic
include ${INCLUDE_DIDACTIC}/didactic.mk

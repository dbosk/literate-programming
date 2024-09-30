.PHONY: all
all: notes.pdf slides.pdf

LATEXFLAGS+=	-shell-escape

SRC+=		preamble.tex
SRC+=		abstract.tex contents.tex
SRC+=		merge.sh merge.tex
SRC+=		foo.bar foo.tex
SRC+=		introsort.tex introsort.py
SRC+=		test_introsort.py
SRC+=		tests_Makefile
SRC+=		cppjava.tex noweb.tex

FIGS+=		figs/pbr.png figs/pbrcover.jpg
FIGS+=		figs/jupyter-lab.png figs/jupyter-notebook.png
FIGS+=		figs/pythontex.pdf figs/web.pdf figs/noweb.pdf

DEPENDS+=	fracexample fractest
SRC+=		fracexample.cpp
SRC+=		fracexample2.cpp

DEPENDS+=	FracExample.class
SRC+=		Fraction2.java

SRC+=		../weblogin/doc/contents.tex

../weblogin/doc/contents.tex: ../weblogin/doc/
	${MAKE} -C $(dir $@) all

fracexample2.cpp: cppjava.nw
	${NOTANGLE.cxx}

Fraction2.java: cppjava.nw
	${NOTANGLE}

notes.pdf: notes.tex didactic.sty
notes.pdf: ${SRC} ${FIGS} ${DEPENDS}

slides.pdf: slides.tex didactic.sty
slides.pdf: ${SRC} ${FIGS} ${DEPENDS}

contents.tex: whatis.nw
	${NOWEAVE.tex}

${FIGS}::
	${MAKE} -C $(dir $@) $(notdir $@)

foo.bar: foo.nw
	${NOTANGLE}

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
	${RM} merge.tex merge.sh
	${RM} merge.aux merge.fdb_latexmk merge.fls merge.log
	${RM} introsort.py introsort.tex
	${RM} test_introsort.py tmp_minted_output.py
	${RM} foo.bar foo.tex
	${RM} -R __pycache__
	${RM} tests_Makefile
	${RM} didactic_output_*
	${RM} didactic_code_*
	${RM} cppfrac.mk
	${MAKE} -C ../weblogin/doc/ clean

frac.mk: cppjava.nw
	${NOTANGLE.mk}

include frac.mk

INCLUDE_MAKEFILES=../makefiles
include ${INCLUDE_MAKEFILES}/tex.mk
include ${INCLUDE_MAKEFILES}/noweb.mk
INCLUDE_DIDACTIC=../didactic
include ${INCLUDE_DIDACTIC}/didactic.mk

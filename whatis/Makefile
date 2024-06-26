.PHONY: all
all: notes.pdf slides.pdf

LATEXFLAGS+=	-shell-escape

SRC+=		preamble.tex
SRC+=		abstract.tex contents.tex
SRC+=		merge.sh merge.tex
SRC+=		foo.bar foo.tex
SRC+=		introsort.tex introsort.py
SRC+=		test_introsort.py

FIGS+=		figs/pbr.png figs/pbrcover.jpg
FIGS+=		figs/jupyter-lab.png figs/jupyter-notebook.png
FIGS+=		figs/pythontex.pdf figs/web.pdf figs/noweb.pdf

notes.pdf: notes.tex didactic.sty
notes.pdf: ${SRC} ${FIGS}

slides.pdf: slides.tex didactic.sty
slides.pdf: ${SRC} ${FIGS}

contents.tex: whatis.nw
	${NOWEAVE.tex}

${FIGS}::
	${MAKE} -C $(dir $@) $(notdir $@)

foo.bar: foo.nw
	${NOTANGLE}

test_introsort.py: introsort.nw
	notangle -R"test introsort.py" $< | cpif $@

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


INCLUDE_MAKEFILES=../makefiles
include ${INCLUDE_MAKEFILES}/tex.mk
include ${INCLUDE_MAKEFILES}/noweb.mk
INCLUDE_DIDACTIC=../didactic
include ${INCLUDE_DIDACTIC}/didactic.mk

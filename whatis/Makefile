.PHONY: all
all: notes.pdf slides.pdf

LATEXFLAGS+=	-shell-escape

SRC+=		preamble.tex
SRC+=		abstract.tex contents.tex
SRC+=		merge.sh merge.tex
SRC+=		foo.bar foo.tex

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

.PHONY: clean
clean:
	${RM} notes.pdf slides.pdf
	${RM} contents.tex
	${RM} merge.tex


INCLUDE_MAKEFILES=../makefiles
include ${INCLUDE_MAKEFILES}/tex.mk
include ${INCLUDE_MAKEFILES}/noweb.mk
INCLUDE_DIDACTIC=../didactic
include ${INCLUDE_DIDACTIC}/didactic.mk

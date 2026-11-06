.PHONY: all
all: notes.pdf slides.pdf

LATEXFLAGS+=	-shell-escape

# The polls run in PythonTeX, which must import mentipy from the deck's own
# venv (made here, never by hand).  The two jobs share ltxobj, so the second
# would otherwise reuse the first job's PythonTeX cache.
TEX_PYTHONTEX=	yes
MENTIPY_VENV=	$(CURDIR)/.venv
PYTHONTEXFLAGS=	--interpreter python:${MENTIPY_VENV}/bin/python3 --rerun=always

${MENTIPY_VENV}/bin/python3:
	mentipy init --venv ${MENTIPY_VENV}

MENTIPY_VERSION=	1.0
MENTIPY_STAMP=	${MENTIPY_VENV}/mentipy-${MENTIPY_VERSION}

# Order-only: the venv must exist, but its timestamp must not trigger an
# upgrade.  The PythonTeX output goes with the upgrade, since latexmk reruns
# PythonTeX only when the code changed.
${MENTIPY_STAMP}: | ${MENTIPY_VENV}/bin/python3
	${MENTIPY_VENV}/bin/python3 -m pip install 'mentipy>=${MENTIPY_VERSION}'
	${RM} ${TEX_OUTDIR}/*.pytxmcr
	touch $@

notes.pdf slides.pdf: ${MENTIPY_STAMP}
# mentipy present rewrites the QR sidecars; the PDFs with polls must follow.
notes.pdf slides.pdf: $(wildcard mentipy-obj/Q-*.pdf_tex)

# The deck is a literate program: contents.nw is the single source.  We use
# noweb.mk's standard weave (tominted, with autolang) and its tangling, so
# root chunks are named <<[[file]]>>.
SRC+=		preamble.tex
SRC+=		abstract.tex contents.tex
SRC+=		sokprotokoll.tex program.tex
SRC+=		ltnotes.bib
# The appendices \input the generated hit-list tables, and the frames show
# files that are tracked as they are.
SRC+=		$(wildcard litteratursokning/*.tex)
SRC+=		$(wildcard excerpts/*)
# The recorded runs are exhibits, kept as the agents wrote them.  They must
# never be remade: noweb.mk's pattern rules would otherwise re-tangle each
# run's .py from its .nw, and the noweb runs name their roots differently.
DEMO_FILES=	$(wildcard demo/*/*/*)
SRC+=		${DEMO_FILES}
${DEMO_FILES}: ;

# One line per tangled example.
EXAMPLES+=	examples/run_demo.sh
EXAMPLES+=	examples/compare_runs.py

contents.tex: contents.nw

examples/%.sh: contents.nw
	@mkdir -p ${@D}
	${NOTANGLE.sh}
	chmod +x $@

examples/%.py: contents.nw
	@mkdir -p ${@D}
	${NOTANGLE.py}

.PHONY: examples
examples: ${EXAMPLES}

notes.pdf: notes.tex didactic.sty
slides.pdf: slides.tex didactic.sty
notes.pdf slides.pdf: ${SRC} ${EXAMPLES}

.PHONY: clean
clean:
	${RM} notes.pdf slides.pdf
	${RM} contents.tex
	${RM} ${EXAMPLES}
	${RM} didactic_output_* didactic_code_*
	${RM} -R mentipy-obj

INCLUDE_MAKEFILES=../makefiles
include ${INCLUDE_MAKEFILES}/tex.mk
include ${INCLUDE_MAKEFILES}/noweb.mk
INCLUDE_DIDACTIC=../didactic
include ${INCLUDE_DIDACTIC}/didactic.mk

# Both jobs share PythonTeX's output files in ltxobj, but latexmk reruns
# PythonTeX only when the job's own code changed.  Without this, a rebuild
# typesets the output of whichever job ran last.  So each job keeps its own
# copy and puts it back before it builds.  We can't force a rerun instead,
# because that regenerates the QR codes from mentipy.base_url and so undoes the
# address that mentipy present just wrote to them.  A job without a copy has no
# output to trust, so it reruns.  Nor has a job whose copy is older than a
# program the deck runs: \runpython's output would be stale, and its file name
# changes with the program, so the copy would point at a missing file.
PYTHONTEX_JOBS=	notes.pdf slides.pdf
PYTHONTEX_OUTPUT=	${TEX_OUTDIR}/py_default_* ${TEX_OUTDIR}/pythontex_data.pkl
# The whole demo tree, directories included: a run directory gains or loses an
# entry without any file in it changing.
PYTHONTEX_COPY_STALE=	find ${EXAMPLES} demo \
			  -newer ${TEX_OUTDIR}/pythontex-$*
${PYTHONTEX_JOBS}: %.pdf: %.tex ${TEX_DOC_PREREQS}
	${RM} ${PYTHONTEX_OUTPUT}
	if [ -d ${TEX_OUTDIR}/pythontex-$* ] && \
	   [ -z "$$(${PYTHONTEX_COPY_STALE} 2>/dev/null)" ]; \
	then cp -p ${TEX_OUTDIR}/pythontex-$*/* ${TEX_OUTDIR}/; \
	else ${RM} ${TEX_OUTDIR}/$*.pytxmcr; fi
	${COMPILE.tex}
	${RM} -R ${TEX_OUTDIR}/pythontex-$*
	mkdir ${TEX_OUTDIR}/pythontex-$*
	cp -p ${PYTHONTEX_OUTPUT} ${TEX_OUTDIR}/pythontex-$*/
	-${LN} ${TEX_OUTDIR}/$@ $@

.PHONY: all
all: lpbook.pdf lpbook-teachers.pdf slides-intro.pdf slides-tutorial-java.pdf

LATEXFLAGS+=	-shell-escape

TEX_PYTHONTEX=	yes

# The makefiles submodule is pinned for its PythonTeX fix (dbosk/makefiles#92),
# which is only on the tominted-default-weave branch.  The rest of that branch
# does not apply here.  Its weave needs features that are not in upstream noweb
# (tominted, -autolang), so we keep the classic flags.  Its tangling looks for
# roots named <<[[fib.py]]>>, whereas our roots are <<fib.py>>; those names are
# what the text teaches (notangle -Rfib.py), so we keep them.  Move the pin to
# master and remove these overrides as far as possible once the fix has landed.
NOWEAVEFLAGS.tex=	${NOWEAVEFLAGS} -x -n -delay -t2
NOWEAVEFLAGS.pdf=	${NOWEAVEFLAGS} -x -t2

NOTANGLE=	notangle ${NOTANGLEFLAGS} -R$(notdir $@) $(filter %.nw,$^) | \
		  ${CPIF} $@ && noroots $(filter %.nw,$^)
# Only for our own makefiles: make also remakes the submodule's included
# tex.mk and noweb.mk with NOTANGLE.mk, and their roots do use the new names.
frac.mk factory.mk: NOTANGLE.mk=notangle ${NOTANGLEFLAGS.mk} -R$(notdir $@) \
		  $(filter %.nw,$^) > $@ && noroots $(filter %.nw,$^)

define plain_root_tangling
NOTANGLE$(1)=	notangle $${NOTANGLEFLAGS$(1)} -R$$(notdir $$@) \
		  $$(filter %.nw,$$^) | $${CPIF} $$@ && noroots $$(filter %.nw,$$^)
endef
$(foreach suffix,.c .cc .cpp .cxx .h .hh .hpp .hxx .hs .py .sty .cls .sh .go,\
	$(eval $(call plain_root_tangling,${suffix})))

SRC+=		preamble.tex
SRC+=		abstract.tex contents.tex
SRC+=		whatis.tex related.tex
SRC+=		doctest.tex
SRC+=		merge.sh merge.tex
SRC+=		fib.py fib.tex
SRC+=		introsort.tex introsort.py
SRC+=		test_introsort.py
SRC+=		tests_Makefile
SRC+=		cppjava.tex noweb.tex
SRC+=		gdb.tex
SRC+=		factory.tex

FIGS+=		figs/pbr.png figs/pbrcover.jpg
FIGS+=		figs/jupyter-lab.png figs/jupyter-notebook.png
FIGS+=		figs/pythontex.pdf figs/web.pdf figs/noweb.pdf

DEPENDS+=	fracexample fractest
SRC+=		fracexample.cpp
SRC+=		fracexample2.cpp

DEPENDS+=	FracExample.class
SRC+=		Fraction2.java

DEPENDS+=	DocumentExample.class DocumentFactoryTest.class
SRC+=		DocumentFactory2.java

SRC+=		weblogin.tex
SRC+=		../weblogin/doc/contents.tex

../weblogin/doc/contents.tex: ../weblogin/doc/
	${MAKE} -C $(dir $@) all

fracexample2.cpp: cppjava.nw
	${NOTANGLE.cxx}

Fraction2.java: cppjava.nw
	${NOTANGLE}

DocumentFactory2.java: factory.nw
	${NOTANGLE}

lpbook.pdf: lpbook.tex didactic.sty
lpbook.pdf: ${SRC} ${FIGS} ${DEPENDS}

lpbook-teachers.pdf: lpbook-teachers.tex didactic.sty
lpbook-teachers.pdf: ${SRC} ${FIGS} ${DEPENDS}

slides-intro.pdf: slides-intro.tex didactic.sty
slides-intro.pdf: ${SRC} ${FIGS} ${DEPENDS}

slides-tutorial-java.pdf: slides-tutorial-java.tex didactic.sty
slides-tutorial-java.pdf: ${SRC} ${FIGS} ${DEPENDS}

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
	${RM} lpbook.pdf lpbook-teachers.pdf slides-intro.pdf slides-tutorial-java.pdf
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

factory.mk: factory.nw
	${NOTANGLE.mk}

include frac.mk
include factory.mk

INCLUDE_MAKEFILES=../makefiles
include ${INCLUDE_MAKEFILES}/tex.mk
include ${INCLUDE_MAKEFILES}/noweb.mk
INCLUDE_DIDACTIC=../didactic
include ${INCLUDE_DIDACTIC}/didactic.mk

FIGS+=	pbrcover.jpg
FIGS+=	jupyter-notebook.png
FIGS+=	jupyter-lab.png
FIGS+= 	beamer.pdf beamer.pdf_tex
FIGS+=	web.pdf web.pdf_tex
FIGS+=	noweb.pdf noweb.pdf_tex
FIGS+=	pythontex.pdf pythontex.pdf_tex

.PHONY: all
all: ${FIGS}

pbrcover.jpg:
	curl -o $@ https://pbrt.org/images/bookcover-4ed.jpg

jupyter-lab.webp:
	curl -o $@ https://jupyter.org/assets/homepage/labpreview.webp

jupyter-notebook.webp:
	curl -o $@ https://jupyter.org/assets/homepage/jupyterpreview.webp

%.png: %.webp
	convert $< $@

.PHONY: clean
clean:
	${RM} ${FIGS}


INCLUDE_MAKEFILES=../../makefiles
include ${INCLUDE_MAKEFILES}/doc.mk

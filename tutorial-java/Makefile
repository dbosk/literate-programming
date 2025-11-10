TARGETS=	Fraction.pdf Fraction.mk

all: ${TARGETS}

Fraction.pdf:	Fraction.tex
	pdflatex Fraction.tex
	pdflatex Fraction.tex

Fraction.tex: Fraction.nw
	noweave -latex Fraction.nw > Fraction.tex

Fraction.mk: Fraction.nw
	notangle -t2 -RFraction.mk Fraction.nw | sed "s/^  /\t/" > Fraction.mk

clean:
	rm ${TARGETS}

include Fraction.mk

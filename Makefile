SUBDIR_GOALS=all clean distclean

SUBDIR+=	src/

date=$(shell date +%Y%m%d-%H%M)
release_files=src/lpbook.pdf src/lpbook-teachers.pdf src/slides.pdf

.PHONY: publish
publish: ${release_files}
	git push --all -u
	gh release create ${date} --title ${date} --generate-notes \
		${release_files}

src/%:
	${MAKE} -C src clean $@

INCLUDE_MAKEFILES=./makefiles
include $(INCLUDE_MAKEFILES)/subdir.mk

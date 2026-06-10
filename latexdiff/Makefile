# Make apply to targets with multiple lines wiht errors
# so they don't silently pass if an earlier line fails
.SHELLFLAGS := -e -o pipefail -c

# Documents to be typeset
.DOCS := old new diff

.PHONY: all clean $(.DOCS)
all: $(.DOCS)
clean:
	latexmk -C $(wildcard $(addsuffix .tex,$(.DOCS)))
	rm -f diff.tex diff.bbl

# Auxiliary targets
diff.tex: old.tex new.tex
	latexdiff $^ > $@
diff.bbl: old.bbl new.bbl
	latexdiff $^ > $@
$(.DOCS): %: %.tex %.bbl
	latexmk -pdf -bibtex- -interaction=nonstopmode $<
	texcount -incbib $<

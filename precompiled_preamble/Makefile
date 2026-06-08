.PHONY: all compile typeset clean purge
all: main.pdf
compile: preamble.fmt
typeset: main.pdf
clean:
	latexmk -c main.tex preamble.tex
purge:
	latexmk -C main.tex preamble.tex

main.pdf: preamble.fmt
	latexmk -pdf -interaction=nonstopmode main.tex

# Pre-compile the static preamble
# https://tex.stackexchange.com/q/79493
preamble.fmt: preamble.tex
	pdflatex -ini -jobname="preamble" "&pdflatex preamble.tex\dump"

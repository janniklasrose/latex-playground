.PHONY: all clean
all:
	latexmk -cd -pdf -interaction=nonstopmode main.tex
	latexmk -cd -pdf -interaction=nonstopmode section/section.tex
	latexmk -cd -pdf -interaction=nonstopmode section/tikz/diagram.tex
clean:
	latexmk -cd -C main.tex section/section.tex section/tikz/diagram.tex

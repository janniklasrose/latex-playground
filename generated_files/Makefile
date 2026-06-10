.PHONY: all clean
all:
	latexmk -pdf -interaction=nonstopmode -use-make main.tex
clean:
	latexmk -C main.tex
purge: clean
	rm -rf generated/

# generate png files from python scripts
.PHONY: venv
.VENV := generated/.venv
venv: requirements.txt
	python3 -m venv $(.VENV)
	$(.VENV)/bin/pip install -r $<

generated/%.png: src/%.py venv
	$(.VENV)/bin/python $< "$@"
generated/%.tex: src/%.py venv
	$(.VENV)/bin/python $< "$@"

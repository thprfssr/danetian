all:
	make content.latex
	make dictionary.pdf

content.latex: parse.py content.liquid words.yaml
	python parse.py > content.latex

dictionary.pdf: content.latex dictionary.latex
	xelatex dictionary.latex

.PHONY: clean
clean:
	rm *.aux *.log dictionary.pdf content.latex

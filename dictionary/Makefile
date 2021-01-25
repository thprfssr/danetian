all:
	python parse.py > dictionary.latex
	#awk NF dictionary.latex > /tmp/dictionary.latex
	#mv /tmp/dictionary.latex .
	xelatex dictionary.latex

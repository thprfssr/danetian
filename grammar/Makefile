all:
	make tables
	make grammar.pdf

compiled/%.table: verbs/%.yaml
	python parse.py $< template.latex.liquid > $@

.PHONY: tables
tables: parse.py
	make compiled/bideti.table
	make compiled/bloti.table
	make compiled/denati.table
	make compiled/doti.table
	make compiled/esti-be.table
	make compiled/esti-eat.table
	make compiled/fekmi.table
	make compiled/iti.table
	make compiled/jekti.table
	make compiled/linepti.table
	make compiled/merti.table
	make compiled/vepti.table
	make compiled/vopeti.table

grammar.pdf: grammar.latex compiled/*.table
	xelatex grammar.latex
	makeglossaries grammar
	xelatex grammar.latex


.PHONY: clean
clean:
	rm compiled/*
	rm *.{aux,glg,glo,gls,ist,log,out,pdf,toc}

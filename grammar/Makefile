all:
	#make tables
	xelatex grammar.latex
	makeglossaries grammar
	xelatex grammar.latex

tables:
	python parse.py verbs/vopeti.yaml verbs/TEMPLATE-FULL.latex.liquid > compiled/vopeti.latex
	python parse.py verbs/doti.yaml verbs/TEMPLATE-FULL.latex.liquid > compiled/doti.latex
	python parse.py verbs/esti-eat.yaml verbs/TEMPLATE-FULL.latex.liquid > compiled/esti-eat.latex
	python parse.py verbs/esti-be.yaml verbs/TEMPLATE-ACTIVE.latex.liquid > compiled/esti-be.latex
	python parse.py verbs/iti.yaml verbs/TEMPLATE-ACTIVE.latex.liquid > compiled/iti.latex
	python parse.py verbs/voide.yaml verbs/TEMPLATE-FULL.latex.liquid > compiled/voide.latex
	python parse.py verbs/bloti.yaml verbs/TEMPLATE-FULL.latex.liquid > compiled/bloti.latex

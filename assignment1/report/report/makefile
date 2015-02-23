all:
	pdflatex main.tex 
	bibtex main.aux
	pdflatex main.tex 
	pdflatex main.tex 
	mv main.pdf bharath.pdf

clean:
	rm bharath.pdf *.aux *.log *.toc *.bbl
	


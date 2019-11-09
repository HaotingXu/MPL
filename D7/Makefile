FILENAME=report
paper: $(FILENAME).tex cites.bib
	xelatex $(FILENAME).tex
	bibtex $(FILENAME)
	xelatex $(FILENAME).tex
	xelatex $(FILENAME)
clean:
	rm -f *.out $(FILENAME).bib *.bbl *.log *.blg  *.aux 

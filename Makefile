filename=physique

#pdf: dvi
#	 dvipdf ${filename}.dvi > /dev/null
pdf:
	gnuplot *.gnuplot||true
	pdflatex ${filename}
	makeindex ${filename}.idx
	pdflatex ${filename}> /dev/null
	pdflatex ${filename}> /dev/null

#ps: dvi
#	dvips -t a4 ${filename}.dvi -o ${filename}.ps > /dev/null

#dvi:
#	gnuplot *.gnuplot||true
#	as *.asy||true
#	latex ${filename}
#	bibtex ${filename}||true
#	makeindex ${filename}.idx
#	latex ${filename}> /dev/null
#	latex ${filename}> /dev/null
#	latex ${filename}> /dev/null

read:
	evince ${filename}.pdf &

aread:
	acroread ${filename}.pdf &

clean:
	rm -f *.ps *.log *.aux *.out *.dvi *.bbl *.blg *.lof *.lot *.toc *.ilg *.idx *.ind *~ ${filename}.m*

backup:
	git add *
	git commit
	git push backupDD master

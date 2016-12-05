SRC="solutions.tex"

all: release

release: rubber clean

debug: pdflatex clean

rubber:
	rubber -d $(SRC)

pdflatex:
	pdflatex $(SRC)

clean:
	find . -type f -regex '\(.*log\|.*aux\|.*toc\|.*out\)' -delete

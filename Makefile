SRCS=$(wildcard *.tex)
OBJS=$(patsubst %.tex,%,$(SRCS))

all: $(OBJS) clean

%: %.tex
	pdflatex $< $@.pdf

clean:
	find . -type f -regex '\(.*log\|.*aux\)' -delete

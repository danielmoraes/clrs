SRCS=$(wildcard *.tex)
OBJS=$(patsubst %.tex,%,$(SRCS))

all: $(OBJS) clean

%: %.tex
	rubber -d $<

clean:
	find . -type f -regex '\(.*log\|.*aux\|.*toc\|.*out\)' -delete

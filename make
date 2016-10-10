#!/bin/sh

pdflatex "$1".tex && rm *.log && rm *.aux

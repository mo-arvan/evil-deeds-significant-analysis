#!/bin/bash

#inkscape -D -z --file=$1 --export-pdf=$1.pdf --export-latex
# FROM https://tex.stackexchange.com/questions/2099/how-to-include-svg-diagrams-in-latex
inkscape -D $1  -o $1.pdf --export-latex
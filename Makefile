all: compile latexcompile clean

compile:
	python3 compile.py

latexcompile:
	@pdflatex *.tex

clean:
	@rm *.log
	@rm *.aux
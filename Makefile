all: build/main.pdf

# hier Python-Skripte:
#build/plot.pdf: plot.py matplotlibrc header-matplotlib.tex | build
#	TEXINPUTS=$$(pwd): python plot.py

# hier weitere Abhängigkeiten für build/main.pdf deklarieren:


build/main.pdf: FORCE | build
	  TEXINPUTS=build: \
	  BIBINPUTS=build: \
	  max_print_line=1048576 \
	latexmk \
	  --lualatex \
	  --output-directory=build \
	  --interaction=nonstopmode \
	  --halt-on-error \
	main.tex
build/gravitation.pdf: obligartorischepythonkacke.py matplotlibrc header-matplotlib.tex csv/gravi.csv | build
	TEXINPUTS=$$(pwd): python obligartorischepythonkacke.py
build/schwingung.pdf: schwingung.py matplotlibrc header-matplotlib.tex csv/schwing.csv | build
	TEXINPUTS=$$(pwd): python schwingung.py
build/praezess.pdf: praezession.py matplotlibrc header-matplotlib.tex csv/schwing.csv | build
	TEXINPUTS=$$(pwd): python praezession.py
build/main.pdf: content/gravi.tex content/gravi2.tex build/gravitation.pdf content/schwing.tex content/schwing2.tex build/schwingung.pdf content/praezess.tex content/praezess2.tex build/praezess.pdf

build:
	mkdir -p build

clean:
	rm -rf build

FORCE:

.PHONY: all clean

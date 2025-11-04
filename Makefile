.ONESHELL:
SHELL = /bin/bash


# Create or update the environment from environment.yml with no activation
.PHONY: env
env:
	source /srv/conda/etc/profile.d/conda.sh
	conda env update -n "myst-hw3" -f "environment.yml" --prune \
	|| conda env create -n "myst-hw3" -f "environment.yml"


# Build html rendering of MyST site
.PHONY: html
html: myst.yml
	myst build --html


# Clean up folders
.PHONY: clean
clean:
	rm -rf figures audio _build
	mkdir -p figures audio

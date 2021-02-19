
SHELL := /bin/bash

# Setup dev environment
install:
	source env/bin/activate; \
	pip3 install -r requirements.txt

# Start the dev server
boot:
	source env/bin/activate; \
	python3 app.py

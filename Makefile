SHELL := /bin/bash


# Setup dev environment
init:
	python3 -m venv env
	source env/bin/activate; \
	pip3 install -r requirements.txt --user
	python3 app.py

# Start the dev server, after your dev env is setup
run:
	source env/bin/activate; \
	python3 app.py

# Rebuild virtualenv
rebuild:
	sudo rm env -r
	python3 -m venv env
	source env/bin/activate; \
	pip3 install -r requirements.txt
	python3 app.py

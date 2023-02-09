PROJECT_NAME := solid-python
PYTHON_VERSION :=  3.9.12
VENV_NAME := $(PROJECT_NAME)-$(PYTHON_VERSION)


.pip:
	python -m pip install pip --upgrade


setup: .pip
	python -m pip uninstall -y typing
	python -m pip install -U setuptools
	python -m pip install -U black
	python -m pip install -r requirements.txt


.create-venv:
	pyenv install -s $(PYTHON_VERSION)
	pyenv uninstall -f $(VENV_NAME)
	pyenv virtualenv $(PYTHON_VERSION) $(VENV_NAME)
	pyenv local $(VENV_NAME)


create-venv: .create-venv setup


.clean-build:
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +


.clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '_pycache_' -exec rm -fr {} +


clean: .clean-build .clean-pyc


run-postgres:
	docker start $(PROJECT_NAME)-postgres 2>/dev/null || docker run --name $(PROJECT_NAME)-postgres -p 5432:5432 -e POSTGRES_PASSWORD='postgres' -d postgres:11-alpine


runserver: clean run-postgres
	python manage.py runserver
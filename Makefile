install:
	pip install --upgrade pip && pip install -r requirements.txt

format:
	black *.py

lint:
	#disable comment to test speed
	#pylint --disable=R,C --ignore-patterns=test_.*?py *.py mylib/*.py
	#ruff linting is 10-100X faster than pylint
	ruff check *.py mylib/*.py

test:
	python -m pytest -cov=main test_main.py

container-lint:
	docker run --rm -i hadolint/hadolint < Dockerfile

refactor: format lint

all: install lint test format deploy

extract:
	python main.py extract

transform_load: 
	python main.py transform_load
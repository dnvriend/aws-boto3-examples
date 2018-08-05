.PHONY: help env info clobber test run_test type_check fmt lint

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

env:		## creates a virtual python environment  for this project
	pipenv install --three --dev

info:		## shows current python environment
	pipenv --venv

clobber:	## remove virtual python environment
	pipenv --rm

test: fmt run_test

run_test:
	pipenv run pytest

fmt:        ## runs code formatter
	#pipenv run yapf --style pep8 --recursive --in-place rules tests
	pipenv run yapf --recursive --in-place examples

type_check:  ## type checks the code
	pipenv run mypy --ignore-missing-imports examples

lint:       ## run python code analysis on rules
	pipenv run pylint examples

lint_test:   ## run python code analysis on test
	pipenv run pylint tests

run:
	pipenv run python determine_cost.py
# @see http://marmelab.com/blog/2016/02/29/auto-documented-makefile.html
.DEFAULT_GOAL := help
.PHONY: help
help: ## provides cli help for this makefile (default)
	@grep -E '^[a-zA-Z_0-9-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: dist
dist:
	python setup.py sdist

.PHONY: tests
tests: ## run unit tests with unittest
	python -u -m unittest discover tsincluder_tests '*_test.py'

.PHONY: coverage
coverage: coverage_run coverage_report

coverage_run :
	coverage run --omit *_test.py,**/*_test.py,**/__init__.py,/usr/local/lib/python2.7/** -m unittest discover tsincluder_tests '*_test.py'

coverage_report:
	coverage report

.PHONY: lint
lint: ## check your application with pylint
	pylint --rcfile .rcfile tsincluder

.PHONY: clean
clean :
	rm -rf dist
	rm -rf venv
	rm -rf venv3
	rm -f .coverage

.PHONY: venv
venv: ## build virtual env for python in ./venv
	virtualenv venv

.PHONY: venv3
venv3: ## build a virtual env for python 3 in ./venv3
	virtualenv venv3 -p /usr/bin/python3

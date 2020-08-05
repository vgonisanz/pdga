.PHONY: docs test help
.DEFAULT_GOAL := help

SHELL := /bin/bash

define PRINT_HELP_PYSCRIPT
import re, sys
print("You can run the following targets (with make <target>): \r\n")
for line in sys.stdin:
	match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
	if match:
		target, help = match.groups()
		print("%-20s %s" % (target, help))
endef
export PRINT_HELP_PYSCRIPT

help:
	@python3 -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

env-create: ## (re)create a development environment using tox
	tox -e pdga --recreate
	@echo -e "\r\nYou can activate the environment with:\r\n\r\n$$ source ./.tox/pdga/bin/activate\r\n"

lint: ## local static doc analysis with markdownlint
	markdownlint --config .markdownlint.json '**/*.md'

clean-dist: clean-env ## clean everything

clean-env: ## remove tox virtual environments
	rm -rf .tox

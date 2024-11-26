.PHONY: help

help: ## Show this help.
	@grep -Fh "##" $(MAKEFILE_LIST) | grep -Fv grep -F | sed -e 's/\\$$//' | sed -e 's/##//'
 
setup: ## Install all python deps (WARNING: this install in the user space with --break-system-packages).
	pip install -r requirements.txt --user --break-system-packages

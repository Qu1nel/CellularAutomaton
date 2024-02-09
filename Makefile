path := .

.DEFAULT_GOAL := help
MAKEFLAGS 	  += --silent --no-print-directory

RED			:= \\033[0;31m
GREEN		:= \\033[1;32m
YELLOW		:= \\033[1;33m
BLUE		:= \\033[0;36m
RESET		:= \\033[0m


# Main
##############################################################################


.PHONY: run
run: update  ## Launch app (run.py)
	poetry run python run.py

.PHONY: update
update:
	poetry install


# Lint
##############################################################################


.PHONY: lint-check lint lints check
lint-check: ruff mypy pyright black  ## Complete code base check with linters and formatters


# Alias
lint: lint-check  ## Alias for 'lint-check'
lints: lint-check  ## Alias for 'lint-check'
check: lint-check  ## Alias for 'lint-check'


.PHONY: ruff
ruff:  # Use 'ruff' utility as linter
	@echo -e
	@echo -e "$(BLUE)Applying ruff..."
	@echo -e "$(GREEN)================$(RESET)"
	@echo -e
	poetry run ruff check $(path) --fix
	@echo -e

.PHONY: mypy
mypy:  # Use 'mypy' utility as linter
	@echo -e
	@echo -e "$(BLUE)Applying mypy..."
	@echo -e "$(GREEN)================$(RESET)"
	@echo -e
	poetry run mypy $(path)
	@echo -e

.PHONY: pyright
pyright:  ## Use 'pyright' utility as linter
	@echo -e
	@echo -e "$(BLUE)Applying pyright..."
	@echo -e "$(GREEN)===================$(RESET)"
	@echo -e
	poetry run pyright $(path)
	@echo -e

.PHONY: black
black:  ## Use 'black' utility as formatter
	@echo -e
	@echo -e "$(BLUE)Applying black..."
	@echo -e "$(GREEN)=================$(RESET)"
	@echo -e
	poetry run black $(path)
	@echo -e


# Clean cache
##############################################################################


.PHONY: clean
clean:  ## Clear linter cache (.mypy_cache .ruff_cache)
	@echo -e "$(RED)Remove:$(RESET) .mypy_cache/"
	@echo -e "$(RED)Remove:$(RESET) .ruff_cache/"
	@rm -rf .mypy_cache
	@rm -rf .ruff_cache


# Other
##############################################################################


.PHONY: help
help:  ## Show this output, i.e. help to use the commands
	grep -E '^[a-zA-Z_-]+:.*?# .*$$' Makefile | awk 'BEGIN {FS = ":.*?# "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'


info-%:
	@make --dry-run --always-make $* | grep -v "info"


print-%:
	@$(info '$*'='$($*)')


.SILENT:

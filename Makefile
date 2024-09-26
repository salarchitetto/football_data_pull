# Makefile

BASE_BRANCH := main
CURRENT_BRANCH := $(shell git branch --show-current)
BASE_COMMIT := $(shell git merge-base $(CURRENT_BRANCH) $(BASE_BRANCH))

setup-postgres-db:
	docker-compose up

# Install Dependencies
install-dependencies:
	pip3 install -r requirements.txt

#Static Checking Local+CI/CD
get-list-of-touched-files:
	@files="$$(git diff --name-only --diff-filter=MACR $(BASE_COMMIT) | grep '\.py$$')"; \
	echo $$files

python-local-static-checking: get-list-of-touched-files
	@FILES="$$(make get-list-of-touched-files)"; \
	echo "$$FILES"; \
	make black-format-fix FILES="$$FILES" && \
	make isort-import-fix FILES="$$FILES" && \
	make ruff-lint-fix FILES="$$FILES" && \
	make ruff-lint-check-local FILES="$$FILES"
#	make mypy-check FILES="$$FILES"

black-format-check:
	black --check --verbose ${FILES}

black-format-fix:
	black --verbose ${FILES}

mypy-type-check:
	mypy ${FILES}

ruff-lint-check-local:
	ruff check --exit-zero ${FILES}

ruff-lint-check:
	ruff check --output-format=github ${FILES}

ruff-lint-fix:
	ruff check --fix-only ${FILES}

isort-import-check:
	isort --check --verbose --diff ${FILES}

isort-import-fix:
	isort ${FILES}

# Actions stuff

generate-changelog:
	gem install github-changelog-generator && \
	github-changelog-generator -o CHANGELOG.md --no-verbose && \
	echo "::set-output name=body::$$$(cat CHANGELOG.md)"


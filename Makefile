.DEFAULT_GOAL:=help

.PHONY: build
build: index icons ## build site
	./scripts/build.py

.PHONY: clean
clean: ## remove build artefacts
	./scripts/clean.py

.PHONY: icons
icons: ## fabricate site icons
	./scripts/icons.py

.PHONY: help
.SILENT: help
help:  ## list make targets
	awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {sub("\\\\n",sprintf("\n%22c"," "), $$2);printf " \033[36m%-20s\033[0m  %s\n", $$1, $$2}' $(MAKEFILE_LIST)

.PHONY: index
index: ## build catalogue
	./scripts/index.py

.PHONY: install
install: ## install dependecies
	bundle install
	pip3 install --requirement requirements.txt

.PHONY: list
.SILENT: list
list: index ## show tools catalogue
	./scripts/list.py

.PHONY: serve
serve: build ## locally serve site
	./scripts/serve.py

.PHONY: tarball
tarball: build ## package site
	./scripts/tarball.py

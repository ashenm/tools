.DEFAULT_GOAL:=help

.PHONY: build
build: index ## build site
	./scripts/build.py

.PHONY: clean
clean: ## remove build artefacts
	./scripts/clean.py

.PHONY: help
.SILENT: help
help:  ## show make targets
	awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {sub("\\\\n",sprintf("\n%22c"," "), $$2);printf " \033[36m%-20s\033[0m  %s\n", $$1, $$2}' $(MAKEFILE_LIST)

.PHONY: index
index: ## build catalogue
	./scripts/index.py

.PHONY: serve
serve: build ## locally serve site
	./scripts/serve.py

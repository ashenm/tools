default:
	$(MAKE) index
	$(MAKE) serve

build:
	./scripts/build.py

index:
	./scripts/index.py

serve:
	./scripts/serve.py

clean:
	./scripts/clean.py

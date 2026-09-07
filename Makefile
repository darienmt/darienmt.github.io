.PHONY: build serve validate clean

build:
	hugo --minify

serve:
	hugo server --buildDrafts --disableFastRender

validate: build
	python3 scripts/check-url-manifest.py public

clean:
	rm -rf public resources

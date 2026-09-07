.PHONY: build serve clean

build:
	hugo --minify

serve:
	hugo server --buildDrafts --disableFastRender

clean:
	rm -rf public resources

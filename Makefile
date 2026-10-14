IMAGE      ?= terralid-vocab
PREVIEW_PORT ?= 4200
SERVE_PORT ?= 8080

DOCKER_RUN = docker run --rm --user $(shell id -u):$(shell id -g) -e HOME=/tmp \
	-v "$(CURDIR)":/repo -w /repo

.PHONY: image markdown build preview serve clean

image:
	docker build -t $(IMAGE) .

markdown: image
	$(DOCKER_RUN) $(IMAGE) python tools/build_site.py --skip-render

build: image
	$(DOCKER_RUN) $(IMAGE) python tools/build_site.py

preview: markdown
	$(DOCKER_RUN) -it -p $(PREVIEW_PORT):$(PREVIEW_PORT) $(IMAGE) \
		quarto preview docs --host 0.0.0.0 --port $(PREVIEW_PORT) --no-browser

serve:
	docker run --rm -p $(SERVE_PORT):80 -v "$(CURDIR)/docs/_site":/usr/share/nginx/html:ro nginx:alpine

clean:
	rm -rf docs/_site docs/.quarto docs/*_files
	find docs -maxdepth 1 \( -name '*.md' -o -name '*.html' \) -delete

# TerraLID Vocabulary

The TerraLID vocabularies ensure coherent data entries for the TerraLID metadata profile, which describes archaeometric data and the materials they are derived from, with a particular focus on lead isotope data. The vocabularies were compiled by the TerraLID Editors and the TerraLID Core Team and implemented in SKOS by Thomas Rose and Katrin J. Westner.

The authoritative source is the SKOS vocabulary in Turtle syntax in [`vocabulary/`](vocabulary/). This repository turns it into a static, searchable HTML site published at **https://vocab.terralid.org**.

## Repository layout

| Path | Content |
|------|---------|
| `vocabulary/*.ttl` | SKOS vocabularies (source of truth) |
| `vocabulary/vocabularies.txt` | Vocabularies to publish: Turtle file name and ConceptScheme URI |
| `docs/` | Quarto website project: `_quarto.yml`, theme (`custom.scss`, `styles.css`), assets |
| `tools/` | Python tools: `build_site.py` (build driver), `vocab2mdCacheV2.py` (Markdown generation), `vocab.py` and `navocab/` (optional SQLite-based SKOS CLI, not used by the build) |
| `Dockerfile`, `Makefile` | Build environment and commands, used both locally and in CI |
| `.github/workflows/deploy.yml` | Build and deployment pipeline |

## How the site is built

**Turtle → rdflib graph → Markdown → HTML (Quarto)**

For every entry in `vocabulary/vocabularies.txt`, `tools/build_site.py` parses the Turtle file into a separate in-memory graph, writes `docs/<name>.md`, and finally renders the Quarto project in `docs/` to `docs/_site/`. The post-render step in `docs/_quarto.yml` copies the main vocabulary page to `index.html`. The build fails if any step fails.

The Markdown generator handles common SKOS patterns: hierarchies via `skos:topConceptOf`/`skos:hasTopConcept` and `skos:broader`, and concepts without `skos:inScheme`.

Generated files (`docs/*.md`, `docs/_site/`, `docs/.quarto/`) are not versioned.

## Local development

Requirements: Docker and GNU Make. Python and Quarto run inside the container (`Dockerfile` pins the Quarto version).

| Command | Purpose |
|---------|---------|
| `make build` | Full build to `docs/_site/` (same as CI) |
| `make preview` | Live preview at http://localhost:4200 with automatic reload |
| `make markdown` | Regenerate `docs/*.md` from the Turtle files only |
| `make serve` | Serve `docs/_site/` with nginx at http://localhost:8080, like production |
| `make clean` | Remove generated files |

What to run for which change:

- **Design** (`docs/custom.scss`, `docs/styles.css`, `docs/_quarto.yml`, assets): keep `make preview` running; the browser reloads on save.
- **Vocabulary content** (`vocabulary/*.ttl`) or **Markdown generator** (`tools/*.py`): run `make markdown`; a running preview picks up the new Markdown.
- **Final check before pushing:** `make build && make serve`.

## Adding a vocabulary

1. Add the `.ttl` file to `vocabulary/`.
2. Add a line `<file name without .ttl> <ConceptScheme URI>` to `vocabulary/vocabularies.txt`.
3. If it should become the start page, adjust the `post-render` copy in `docs/_quarto.yml`.

## Deployment

The workflow `.github/workflows/deploy.yml` runs on every push and pull request to `main`:

1. **build**: `make build`, then uploads `docs/_site/` as an artifact. Pull requests stop here.
2. **deploy** (push to `main` only, environment `production`): syncs the artifact with `rsync --delete` over SSH to the web server and checks that https://vocab.terralid.org responds.

Configuration in the GitHub environment `production`:

| Name | Type | Value |
|------|------|-------|
| `DEPLOY_SSH_KEY` | Secret | Private key of the deploy user |
| `DEPLOY_KNOWN_HOSTS` | Secret | Output of `ssh-keyscan <host>` (verified) |
| `DEPLOY_HOST` | Variable | `d-ws188.server.est1816.de` |
| `DEPLOY_USER` | Variable | Deploy user on the server |
| `DEPLOY_PATH` | Variable | Web root served by nginx |
| `DEPLOY_PORT` | Variable | SSH port (optional, default `22`) |

### Server requirements

The server only serves static files; no application runtime is needed.

- nginx serving `DEPLOY_PATH` for `vocab.terralid.org` over HTTPS, with DNS pointing to the server.
- A deploy user whose key may only write to `DEPLOY_PATH`, ideally restricted to rsync (e.g. `rrsync`), and `rsync` installed.
- SSH reachable from GitHub-hosted runners.

## Acknowledgements

This repository is a fork of [GeoSamples/vocabularies](https://github.com/GeoSamples/vocabularies) by **https://www.geosamples.org/**, licensed under the Apache License 2.0. We are grateful to the original authors for their work.

This work has received funding from the German Research Foundation (DFG) through the grants KL 1259/17-1 and WI 5923/2-1 (project number: 524790825).

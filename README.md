# TerraLID Vocabulary

The TerraLID vocabularies include various vocabularies to ensure coherent data entries for the TerraLID metadata profile, which describes archaeometric data and the materials they are derived from with particular focus on lead isotope data. The authoritative source files are SKOS RDF vocabularies serialized using Turtle syntax, located in the `vocabulary/` directory.

HTML view of vocabularies is available at https://vocab.terralid.org/.

### TerraLId vocabularies (`vocabulary/`)

| File | Description | ConceptScheme URI |
|------|-------------|-------------------|
| `2026_06_12_TerraLID_vocab.ttl` | The TerraLID vocabularies include various vocabularies to ensure coherent data entries for the TerraLID metadata profile | `conceptScheme_a0559f69` |


## Processing pipeline

The repository doubles as a GitHub Action that converts SKOS Turtle files to HTML documentation:

**Turtle (.ttl) → SQLite (navocab/rdflib-sqlalchemy) → Markdown (vocab2mdCacheV2.py) → HTML (Quarto)**

Each vocabulary is processed independently with a fresh SQLite database to prevent data from different vocabularies interfering with each other. This is important for files like the SeaDataNet vocabularies that share the same ConceptScheme URI but have different top concepts.

### SKOS patterns handled

The vocabularies in this repository use several different SKOS patterns. The processing tools handle all of these:

- **Standard hierarchy**: Concepts use `skos:topConceptOf`, `skos:inScheme`, and `skos:broader` to establish hierarchy within a single ConceptScheme.
- **Inverse top concept declaration**: Some vocabularies (GSQ, SeaDataNet) declare top concepts using `skos:hasTopConcept` on the ConceptScheme rather than `skos:topConceptOf` on the concepts.
- **No `skos:inScheme`**: Some vocabularies (GSQ) don't use `skos:inScheme` on individual concepts. The code falls back to following `skos:broader` relationships regardless of scheme membership.
- **Cross-scheme children**: SeaDataNet concepts may have `skos:inScheme` pointing to a different ConceptScheme than their parent. The broader-only fallback handles this.

## GitHub Actions workflows

| Workflow | Trigger | Description |
|----------|---------|-------------|
| **Process vocabularies** (`process_vocab.yml`) | Manual | Generates HTML for all vocabularies |
| **build** (`integration.yml`) | Push to main/develop | Docker build verification and smoke test |
| **Test vocabularies** (`testdocs_process_vocab.yml`) | Manual | Tests pipeline with a small vocabulary subset |

## Adding a new vocabulary

1. Add the `.ttl` file to `vocabulary/` (or `vocabulary/`)
2. Add its filename (without `.ttl` extension) and ConceptScheme URI to the pipe-delimited `inputttl` and `inputvocaburi` lists in `process_vocab.yml`. Order must match between the two lists.
3. Add a section to `docs/readme.md` with links to the HTML page and RDF source file
4. Trigger the "Process vocabularies" workflow from the Actions tab

## Implementation details

- **Docker image**: `python:3.12-slim-bookworm` with Quarto, rdflib, rdflib-sqlalchemy
- **Entry point**: `.github/actions/github_action_main.py`
- **Tools**: `tools/vocab.py` (CLI for DB loading), `tools/vocab2mdCacheV2.py` (markdown generation), `tools/navocab/` (SKOS/rdflib wrapper)
- **Dependencies**: `setuptools<81` is pinned because `rdflib-sqlalchemy` 0.5.4 requires `pkg_resources`
- **GitHub Pages**: Serves from the `/docs` directory on the `gh-pages` branch


## Acknowledgements

This project is a fork of and builds upon the workflows and code originally created by **https://www.geosamples.org/** in the **https://github.com/GeoSamples/vocabularies** project. 

The original work is licensed under the Apache License 2.0. We are incredibly grateful to the original authors for their contributions to the community.

## Generate HTML Documentation

### 1. Build the Docker image

```bash
docker build -t terralid-vocab .

docker run --rm \
  -v $(pwd)/docs:/app/docs \
  -e INPUT_ACTION=docs \
  -e INPUT_PATH=/app \
  -e INPUT_INPUTTTL="2026_06_12_TerraLID_vocab" \
  -e INPUT_INPUTVOCABURI="http://vocab.terralid.org#conceptScheme_a0559f69" \
  terralid-vocab



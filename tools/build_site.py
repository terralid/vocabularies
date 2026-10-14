#!/usr/bin/env python3
"""Build the static vocabulary site: Turtle -> Markdown -> HTML (Quarto).

Vocabularies are listed in vocabulary/vocabularies.txt. Output goes to docs/_site.
"""

import argparse
import pathlib
import subprocess
import sys

import rdflib

from vocab2mdCacheV2 import describeVocabulary

REPO = pathlib.Path(__file__).resolve().parent.parent
VOCAB_DIR = REPO / "vocabulary"
DOCS_DIR = REPO / "docs"
VOCAB_LIST = VOCAB_DIR / "vocabularies.txt"


def read_vocab_list(path):
    entries = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        name, scheme_uri = line.split()
        entries.append((name, scheme_uri))
    if not entries:
        sys.exit(f"No vocabularies listed in {path}")
    return entries


def run(cmd, **kwargs):
    print("+", " ".join(str(c) for c in cmd), flush=True)
    subprocess.run([str(c) for c in cmd], check=True, **kwargs)


def build_markdown(name, scheme_uri):
    # A separate graph per vocabulary keeps schemes sharing a URI from mixing.
    ttl = VOCAB_DIR / f"{name}.ttl"
    md = DOCS_DIR / f"{name}.md"
    print(f"+ {ttl} -> {md}", flush=True)
    graph = rdflib.Graph()
    graph.parse(ttl, format="turtle")
    lines = describeVocabulary(graph, rdflib.URIRef(scheme_uri))
    md.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--skip-render", action="store_true", help="only generate the Markdown files")
    args = parser.parse_args()

    for name, scheme_uri in read_vocab_list(VOCAB_LIST):
        build_markdown(name, scheme_uri)
    if not args.skip_render:
        try:
            run(["quarto", "render", DOCS_DIR])
        except subprocess.CalledProcessError as err:
            sys.exit(f"Build failed: {err}")


if __name__ == "__main__":
    main()

import unittest
from pathlib import Path

import rdflib
from rdflib.namespace import RDF, SKOS

from vocab2mdCacheV2 import describeVocabulary


REPO = Path(__file__).resolve().parents[2]
VOCAB = rdflib.Namespace("http://vocab.terralid.org#")


class CollectionRenderingTests(unittest.TestCase):
    def test_published_collections_and_members(self):
        graph = rdflib.Graph().parse(
            REPO / "vocabulary/2026_06_12_TerraLID_vocab.ttl", format="turtle"
        )
        markdown = "\n".join(describeVocabulary(graph, VOCAB.conceptScheme_a0559f69))
        concepts, collections = markdown.split("\n# Collections\n", 1)

        expected = [
            ("object identifier", "skosCollection_e1958489",
             ["c_ff6b1f44", "c_bb41a882", "c_db36371f", "c_9c7b1aa6"]),
            ("period identifier", "skosCollection_b1dd3bc5",
             ["c_fb11b880", "c_d012defe"]),
            ("person identifier", "skosCollection_05151bf3",
             ["c_ef46e5df", "c_c62b90a7"]),
        ]
        sections = collections.split("\n## ")[1:]
        self.assertEqual(len(sections), 3)
        for section, (label, identifier, members) in zip(sections, expected):
            self.assertTrue(section.lstrip().startswith(f"{label} {{#{identifier}}}\n"))
            self.assertIn("- **Type:** SKOS Collection", section)
            self.assertIn("- **Members:**", section)
            self.assertIn(f'- **Collection URI:** <a href="{VOCAB[identifier]}">', section)
            for member in members:
                self.assertIn(f"](#{member})", section)
                self.assertIn(f"{{#{member}}}", concepts)
        self.assertIn("http://www.wikidata.org/wiki/Q36218176", sections[2])

        for collection in list(graph.subjects(RDF.type, SKOS.Collection)):
            graph.remove((collection, None, None))
        without_collections = "\n".join(
            describeVocabulary(graph, VOCAB.conceptScheme_a0559f69)
        )
        self.assertEqual(concepts.rstrip(), without_collections.rstrip())

    def test_collection_without_scheme_or_labels(self):
        graph = rdflib.Graph().parse(data="""
            @prefix : <https://example.org/> .
            @prefix skos: <http://www.w3.org/2004/02/skos/core#> .
            :scheme a skos:ConceptScheme; skos:prefLabel "Test" .
            :root a skos:Concept; skos:prefLabel "Root";
                skos:topConceptOf :scheme .
            :collection a skos:Collection;
                skos:definition "A selection.";
                skos:member :root, :unlabeled .
            :unlabeled a skos:Concept; skos:broader :root .
            :empty a skos:Collection; skos:prefLabel "Empty" .
        """, format="turtle")
        markdown = "\n".join(
            describeVocabulary(graph, rdflib.URIRef("https://example.org/scheme"))
        )
        self.assertIn("##  `https://example.org/collection` {#collection}", markdown)
        self.assertIn("- **Definition**: A selection.", markdown)
        self.assertIn("  - [`Root`](#root)", markdown)
        self.assertIn("  - [`unlabeled`](#unlabeled)", markdown)
        self.assertIn("##  Empty {#empty}", markdown)
        self.assertLess(markdown.index("{#collection}"), markdown.index("{#empty}"))


if __name__ == "__main__":
    unittest.main()

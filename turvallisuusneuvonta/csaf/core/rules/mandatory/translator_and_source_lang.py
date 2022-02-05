"""6.1.15 Translator

It must be tested that /document/source_lang is present and set if the value translator is used
for /document/publisher/category.

The relevant path for this test is:

    /document/source_lang

Example 54 which fails the test:

  "document": {
    // ...
    "publisher": {
      "category": "translator",
      "name": "CSAF TC Translator",
      "namespace": "https://csaf.io/translator"
    },
    "title": "Mandatory test: Translator (failing example 1)",
    // ...
  }

The required element source_lang is missing.
"""

ID = (6, 1, 15)
TOPIC = 'Translator'

PATHS = (
    '/document/category',
)

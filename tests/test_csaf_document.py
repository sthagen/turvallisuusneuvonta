# -*- coding: utf-8 -*-
# pylint: disable=line-too-long,missing-docstring,reimported,unused-import,unused-variable
from typing import no_type_check

import orjson
import pytest
from pydantic.error_wrappers import ValidationError

import turvallisuusneuvonta.csaf.csaf as csaf

META_OK = {
    'category': '42',
    'csaf_version': '2.0',
    'publisher': {
        'category': 'vendor',
        'name': 'ACME',
        'namespace': 'https://example.com',
    },
    'title': 'a',
    'tracking': {
        'current_release_date': '0001-01-01T00:00:00',
        'id': '0',
        'initial_release_date': '0001-01-01T00:00:00',
        'revision_history': [
            {
                'date': '0001-01-01T00:00:00',
                'number': '1',
                'summary': 'a',
            }
        ],
        'status': 'final',
        'version': '1',
    },
}

DOC_OK = {
    'document': META_OK,
}


def test_doc_empty_meta():
    message = '5 validation errors for DocumentLevelMetaData'
    with pytest.raises(ValidationError, match=message):
        _ = csaf.CommonSecurityAdvisoryFramework(csaf.DocumentLevelMetaData())  # type: ignore


@no_type_check
def _strip(a_map) -> None:
    """Keep only mandatory shape."""
    for key, value in tuple(a_map.items()):
        if isinstance(value, dict):
            _strip(value)
        elif value is None:
            del a_map[key]
        elif isinstance(value, list):
            for v_i in value:
                _strip(v_i)


def test_doc_ok_if_spammy():
    doc = csaf.CommonSecurityAdvisoryFramework(**DOC_OK)  # type: ignore
    strip_me = orjson.loads(doc.json())
    _strip(strip_me)
    assert strip_me == DOC_OK

# -*- coding: utf-8 -*-
# pylint: disable=line-too-long,missing-docstring,reimported,unused-import,unused-variable
from typing import no_type_check

import orjson
import pytest
from pydantic.error_wrappers import ValidationError

import turvallisuusneuvonta.csaf.document as document

META_WRONG_VERSION = {
    'category': '42',
    'csaf_version': '42',
}

META_EMPTY_PUBLISHER = {
    'category': '42',
    'csaf_version': '2.0',
    'publisher': {},
}

META_EMPTY_TITLE = {
    'category': '42',
    'csaf_version': '2.0',
    'publisher': {
        'category': 'vendor',
        'name': 'ACME',
        'namespace': 'https://example.com',
    },
    'title': '',
}

META_EMPTY_TRACKING = {
    'category': '42',
    'csaf_version': '2.0',
    'publisher': {
        'category': 'vendor',
        'name': 'ACME',
        'namespace': 'https://example.com',
    },
    'title': 'a',
    'tracking': {},
}

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


def _subs(count: int) -> str:
    """DRY."""
    return f'{count} validation error{"" if count == 1 else "s"} for DocumentLevelMetaData'


def test_meta_doc_none():
    with pytest.raises(ValidationError, match=_subs(5)) as err:
        _ = document.DocumentLevelMetaData()  # type: ignore
    for prop in ('category', 'csaf_version', 'publisher', 'title', 'tracking'):
        assert f'\n{prop}\n  field required' in str(err.value)


def test_meta_doc_category_empty():
    with pytest.raises(ValidationError, match=_subs(5)) as err:
        _ = document.DocumentLevelMetaData(category='')  # type: ignore
    hint = 'ensure this value has at least 1 character'
    assert f'\ncategory\n  {hint}' in str(err.value)
    for prop in ('csaf_version', 'publisher', 'title', 'tracking'):
        assert f'\n{prop}\n  field required' in str(err.value)


def test_meta_doc_csaf_version_wrong():
    with pytest.raises(ValidationError, match=_subs(4)) as err:
        _ = document.DocumentLevelMetaData(**META_WRONG_VERSION)  # type: ignore
    hint = "value is not a valid enumeration member; permitted: '2.0'"
    assert f'\ncsaf_version\n  {hint}' in str(err.value)
    for prop in ('publisher', 'title', 'tracking'):
        assert f'\n{prop}\n  field required' in str(err.value)


def test_meta_doc_publisher_empty():
    with pytest.raises(ValidationError, match=_subs(5)) as err:
        _ = document.DocumentLevelMetaData(**META_EMPTY_PUBLISHER)  # type: ignore
    for prop in ('publisher -> category', 'publisher -> name', 'publisher -> namespace', 'title', 'tracking'):
        assert f'\n{prop}\n  field required' in str(err.value)


def test_meta_doc_title_empty():
    with pytest.raises(ValidationError, match=_subs(2)) as err:
        _ = document.DocumentLevelMetaData(**META_EMPTY_TITLE)  # type: ignore
    hint = 'ensure this value has at least 1 character'
    assert f'\ntitle\n  {hint}' in str(err.value)
    for prop in ('tracking',):
        assert f'\n{prop}\n  field required' in str(err.value)


def test_meta_doc_tracking_empty():
    with pytest.raises(ValidationError, match=_subs(6)) as err:
        _ = document.DocumentLevelMetaData(**META_EMPTY_TRACKING)  # type: ignore
    host = 'tracking'
    for prop in ('current_release_date', 'id', 'initial_release_date', 'revision_history', 'status', 'version'):
        assert f'\n{host} -> {prop}\n  field required' in str(err.value)


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


def test_meta_doc_ok_if_spammy():
    meta_doc = document.DocumentLevelMetaData(**META_OK)  # type: ignore
    strip_me = orjson.loads(meta_doc.json())
    _strip(strip_me)
    assert strip_me == META_OK

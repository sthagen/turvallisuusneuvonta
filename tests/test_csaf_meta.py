# -*- coding: utf-8 -*-
# pylint: disable=line-too-long,missing-docstring,reimported,unused-import,unused-variable
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


def test_meta_doc_none():
    message = '5 validation errors for DocumentLevelMetaData'
    with pytest.raises(ValidationError, match=message) as err:
        _ = document.DocumentLevelMetaData()  # type: ignore
    for prop in ('category', 'csaf_version', 'publisher', 'title', 'tracking'):
        assert f'\n{prop}\n  field required' in str(err.value)


def test_meta_doc_category_empty():
    message = '5 validation errors for DocumentLevelMetaData'
    with pytest.raises(ValidationError, match=message) as err:
        _ = document.DocumentLevelMetaData(category='')  # type: ignore
    hint = 'ensure this value has at least 1 character'
    assert f'\ncategory\n  {hint}' in str(err.value)
    for prop in ('csaf_version', 'publisher', 'title', 'tracking'):
        assert f'\n{prop}\n  field required' in str(err.value)


def test_meta_doc_csaf_version_wrong():
    message = '4 validation errors for DocumentLevelMetaData'
    with pytest.raises(ValidationError, match=message) as err:
        _ = document.DocumentLevelMetaData(**META_WRONG_VERSION)  # type: ignore
    hint = "value is not a valid enumeration member; permitted: '2.0'"
    assert f'\ncsaf_version\n  {hint}' in str(err.value)
    for prop in ('publisher', 'title', 'tracking'):
        assert f'\n{prop}\n  field required' in str(err.value)


def test_meta_doc_publisher_empty():
    message = '5 validation errors for DocumentLevelMetaData'
    with pytest.raises(ValidationError, match=message) as err:
        _ = document.DocumentLevelMetaData(**META_EMPTY_PUBLISHER)  # type: ignore
    for prop in ('publisher -> category', 'publisher -> name', 'publisher -> namespace', 'title', 'tracking'):
        assert f'\n{prop}\n  field required' in str(err.value)

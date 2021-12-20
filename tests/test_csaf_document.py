# -*- coding: utf-8 -*-
# pylint: disable=line-too-long,missing-docstring,reimported,unused-import,unused-variable
from typing import no_type_check

import orjson
import pytest
from pydantic.error_wrappers import ValidationError

import turvallisuusneuvonta.csaf.csaf as csaf
from tests import conftest


def _subs(count: int, what: str) -> str:
    """DRY."""
    return f'{count} validation error{"" if count == 1 else "s"} for {what}'


def test_doc_empty_meta():
    with pytest.raises(ValidationError, match=_subs(5, 'DocumentLevelMetaData')) as err:
        _ = csaf.CommonSecurityAdvisoryFramework(csaf.DocumentLevelMetaData())  # type: ignore
    assert '\ncategory\n  field required' in str(err.value)
    assert '\ncsaf_version\n  field required' in str(err.value)
    assert '\npublisher\n  field required' in str(err.value)
    assert '\ntitle\n  field required' in str(err.value)
    assert '\ntracking\n  field required' in str(err.value)


@no_type_check
def _strip_and_iso_grace(a_map) -> None:
    """Keep only mandatory shape."""
    for key, value in tuple(a_map.items()):
        if isinstance(value, dict):
            _strip_and_iso_grace(value)
        elif value is None:
            del a_map[key]
        elif isinstance(value, str) and value == '0001-01-01T00:00:00':
            a_map[key] = '0001-01-01 00:00:00'
        elif isinstance(value, list):
            for v_i in value:
                _strip_and_iso_grace(v_i)


def test_doc_ok_if_spammy():
    doc = csaf.CommonSecurityAdvisoryFramework(**conftest.DOC_OK)
    strip_me = orjson.loads(doc.json())
    _strip_and_iso_grace(strip_me)
    assert strip_me == conftest.DOC_OK


def test_doc_vulnerability_empty():
    with pytest.raises(ValidationError, match=_subs(1, 'CommonSecurityAdvisoryFramework')) as err:
        _ = csaf.CommonSecurityAdvisoryFramework(**conftest.DOC_VULN_EMPTY)
    assert '\nvulnerabilities\n  vulnerabilities present but empty' in str(err.value)

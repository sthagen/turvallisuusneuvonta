# -*- coding: utf-8 -*-
# pylint: disable=line-too-long,missing-docstring,reimported,unused-import,unused-variable
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


def test_doc_ok_if_spammy():
    doc = csaf.CommonSecurityAdvisoryFramework(**conftest.DOC_OK)
    strip_me = orjson.loads(doc.json())
    conftest._strip_and_iso_grace(strip_me)
    assert strip_me == conftest.DOC_OK


def test_doc_vulnerability_empty():
    with pytest.raises(ValidationError, match=_subs(1, 'CommonSecurityAdvisoryFramework')) as err:
        _ = csaf.CommonSecurityAdvisoryFramework(**conftest.DOC_VULN_EMPTY)
    assert '\nvulnerabilities\n  vulnerabilities present but empty' in str(err.value)

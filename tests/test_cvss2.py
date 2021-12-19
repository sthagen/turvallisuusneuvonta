# -*- coding: utf-8 -*-
# pylint: disable=line-too-long,missing-docstring,reimported,unused-import,unused-variable
import pytest
from pydantic.error_wrappers import ValidationError

import turvallisuusneuvonta.csaf.cvss2.cvss2 as cvss2

CVSS2_VECTOR_STRING_LOG4J = 'AV:N/AC:M/Au:N/C:C/I:C/A:C'
CVSS2_BASE_SCORE_LOG4J = '10.0'


def test_cvss2_empty():
    message = '3 validation errors for CVSS'
    with pytest.raises(ValidationError, match=message):
        _ = cvss2.CVSS()


def test_cvss2_wrong_version():
    message = '1 validation error for CVSS'
    with pytest.raises(ValidationError, match=message) as err:
        _ = cvss2.CVSS(version='42', vectorString=CVSS2_VECTOR_STRING_LOG4J, baseScore=CVSS2_BASE_SCORE_LOG4J)
    assert '\nversion\n  value is not a valid enumeration member' in str(err.value)

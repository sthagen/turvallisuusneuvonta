# -*- coding: utf-8 -*-
# pylint: disable=line-too-long,missing-docstring,reimported,unused-import,unused-variable
import pytest
from pydantic.error_wrappers import ValidationError

import turvallisuusneuvonta.csaf.cvss31.cvss31 as cvss31

CVSS31_VECTOR_STRING_LOG4J = 'CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H'
CVSS31_BASE_SCORE_LOG4J = '10.0'
CVSS31_BASE_SEVERITY_LOG4J = 'CRITICAL'


def test_cvss31_empty():
    message = '4 validation errors for CVSS'
    with pytest.raises(ValidationError, match=message):
        _ = cvss31.CVSS()


def test_cvss31_wrong_version():
    data = {
        'version': '42',
        'vectorString': CVSS31_VECTOR_STRING_LOG4J,
        'baseScore': CVSS31_BASE_SCORE_LOG4J,
        'baseSeverity': CVSS31_BASE_SEVERITY_LOG4J,
    }
    message = '1 validation error for CVSS'
    with pytest.raises(ValidationError, match=message) as err:
        _ = cvss31.CVSS(**data)
    assert '\nversion\n  value is not a valid enumeration member' in str(err.value)

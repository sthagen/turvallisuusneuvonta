# -*- coding: utf-8 -*-
# pylint: disable=line-too-long,missing-docstring,reimported,unused-import,unused-variable
import pytest
from pydantic.error_wrappers import ValidationError

import turvallisuusneuvonta.csaf.cvss31.cvss31 as cvss31

CVSS31_VECTOR_STRING_LOG4J = 'CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H'
CVSS31_BASE_SCORE_LOG4J = '10.0'
CVSS31_BASE_SEVERITY_LOG4J = cvss31.SeverityType.critical


def test_cvss31_empty():
    message = '4 validation errors for CVSS'
    with pytest.raises(ValidationError, match=message):
        _ = cvss31.CVSS()


def test_cvss31_wrong_version():
    data = {
        'version': '42',
        'vector_string': CVSS31_VECTOR_STRING_LOG4J,
        'base_score': CVSS31_BASE_SCORE_LOG4J,
        'base_severity': CVSS31_BASE_SEVERITY_LOG4J,
    }
    message = '1 validation error for CVSS'
    with pytest.raises(ValidationError, match=message) as err:
        _ = cvss31.CVSS(**data)
    assert '\nversion\n  value is not a valid enumeration member' in str(err.value)


def test_cvss31_log4j_cve_2021_44228():
    data = {
        'version': cvss31.Version.value,
        'vector_string': CVSS31_VECTOR_STRING_LOG4J,
        'base_score': CVSS31_BASE_SCORE_LOG4J,
        'base_severity': CVSS31_BASE_SEVERITY_LOG4J,
    }
    cvss_cve_2021_44228 = cvss31.CVSS(**data)
    assert isinstance(cvss_cve_2021_44228, cvss31.CVSS)
    assert cvss_cve_2021_44228.version == cvss31.Version.value
    assert cvss_cve_2021_44228.vector_string == CVSS31_VECTOR_STRING_LOG4J
    assert cvss_cve_2021_44228.base_score.__root__ == float(CVSS31_BASE_SCORE_LOG4J)
    assert cvss_cve_2021_44228.base_severity.critical == CVSS31_BASE_SEVERITY_LOG4J
    assert cvss_cve_2021_44228.confidentiality_requirement is None

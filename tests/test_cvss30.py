# -*- coding: utf-8 -*-
# pylint: disable=line-too-long,missing-docstring,reimported,unused-import,unused-variable
import pytest
from pydantic.error_wrappers import ValidationError

import turvallisuusneuvonta.csaf.cvss30.cvss30 as cvss30

CVSS30_VECTOR_STRING_LOG4J = 'CVSS:3.0/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H'
CVSS30_BASE_SCORE_LOG4J = '10.0'
CVSS30_BASE_SEVERITY_LOG4J = cvss30.SeverityType.critical


def test_cvss30_empty():
    message = '4 validation errors for CVSS30'
    with pytest.raises(ValidationError, match=message):
        _ = cvss30.CVSS30()


def test_cvss30_wrong_version():
    data = {
        'version': '42',
        'vectorString': CVSS30_VECTOR_STRING_LOG4J,
        'baseScore': CVSS30_BASE_SCORE_LOG4J,
        'baseSeverity': CVSS30_BASE_SEVERITY_LOG4J,
    }
    message = '1 validation error for CVSS30'
    with pytest.raises(ValidationError, match=message) as err:
        _ = cvss30.CVSS30(**data)
    assert '\nversion\n  value is not a valid enumeration member' in str(err.value)


def test_cvss30_log4j_cve_2021_44228():
    data = {
        'version': cvss30.Version.value,
        'vectorString': CVSS30_VECTOR_STRING_LOG4J,
        'baseScore': CVSS30_BASE_SCORE_LOG4J,
        'baseSeverity': CVSS30_BASE_SEVERITY_LOG4J,
    }
    cvss_cve_2021_44228 = cvss30.CVSS30(**data)
    assert isinstance(cvss_cve_2021_44228, cvss30.CVSS30)
    assert cvss_cve_2021_44228.version == cvss30.Version.value
    assert cvss_cve_2021_44228.vector_string == CVSS30_VECTOR_STRING_LOG4J
    assert cvss_cve_2021_44228.base_score.__root__ == float(CVSS30_BASE_SCORE_LOG4J)
    assert cvss_cve_2021_44228.base_severity.critical == CVSS30_BASE_SEVERITY_LOG4J
    assert cvss_cve_2021_44228.confidentiality_requirement is None

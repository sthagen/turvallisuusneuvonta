# -*- coding: utf-8 -*-
# pylint: disable=line-too-long,missing-docstring,reimported,unused-import,unused-variable
import pytest
from pydantic.error_wrappers import ValidationError

from turvallisuusneuvonta.csaf.cvss.cvss import (
    CVSS2,
    CVSS30,
    CVSS31,
    SeverityType as CvssSeverityType,
    Version as CvssVersion,
)

CVSS31_VECTOR_STRING_LOG4J = 'CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H'
CVSS31_BASE_SCORE_LOG4J = '10.0'
CVSS31_BASE_SEVERITY_LOG4J = CvssSeverityType.critical

CVSS30_VECTOR_STRING_LOG4J = 'CVSS:3.0/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H'
CVSS30_BASE_SCORE_LOG4J = '10.0'
CVSS30_BASE_SEVERITY_LOG4J = CvssSeverityType.critical

CVSS2_VECTOR_STRING_LOG4J = 'AV:N/AC:M/Au:N/C:C/I:C/A:C'
CVSS2_BASE_SCORE_LOG4J = '10.0'


def test_cvss2_empty():
    message = '2 validation errors for CVSS2'
    with pytest.raises(ValidationError, match=message) as err:
        _ = CVSS2()  # type: ignore
    assert '\nvector_string\n  field required' in str(err.value)
    assert '\nbase_score\n  field required' in str(err.value)


def test_cvss2_wrong_version():
    data = {
        'version': '42',
        'vector_string': CVSS2_VECTOR_STRING_LOG4J,
        'base_score': CVSS2_BASE_SCORE_LOG4J,
    }
    message = '1 validation error for CVSS'
    with pytest.raises(ValidationError, match=message) as err:
        _ = CVSS2(**data)
    assert '\nversion\n  value is not a valid enumeration member' in str(err.value)


def test_cvss20_log4j_cve_2021_44228():
    data = {
        'version': CvssVersion.two,
        'vector_string': CVSS2_VECTOR_STRING_LOG4J,
        'base_score': CVSS2_BASE_SCORE_LOG4J,
    }
    cvss_cve_2021_44228 = CVSS2(**data)
    assert isinstance(cvss_cve_2021_44228, CVSS2)
    assert cvss_cve_2021_44228.version == CvssVersion.two
    assert cvss_cve_2021_44228.vector_string == CVSS2_VECTOR_STRING_LOG4J
    assert cvss_cve_2021_44228.base_score.__root__ == float(CVSS2_BASE_SCORE_LOG4J)
    assert cvss_cve_2021_44228.confidentiality_requirement is None


def test_cvss30_empty():
    message = '3 validation errors for CVSS30'
    with pytest.raises(ValidationError, match=message) as err:
        _ = CVSS30()  # type: ignore
    assert '\nvector_string\n  field required' in str(err.value)
    assert '\nbase_score\n  field required' in str(err.value)
    assert '\nbase_severity\n  field required' in str(err.value)


def test_cvss30_wrong_version():
    data = {
        'version': '42',
        'vector_string': CVSS30_VECTOR_STRING_LOG4J,
        'base_score': CVSS30_BASE_SCORE_LOG4J,
        'base_severity': CVSS30_BASE_SEVERITY_LOG4J,
    }
    message = '1 validation error for CVSS'
    with pytest.raises(ValidationError, match=message) as err:
        _ = CVSS30(**data)
    assert '\nversion\n  value is not a valid enumeration member' in str(err.value)


def test_cvss30_log4j_cve_2021_44228():
    data = {
        'version': CvssVersion.three_zero,
        'vector_string': CVSS30_VECTOR_STRING_LOG4J,
        'base_score': CVSS30_BASE_SCORE_LOG4J,
        'base_severity': CVSS30_BASE_SEVERITY_LOG4J,
    }
    cvss_cve_2021_44228 = CVSS30(**data)
    assert isinstance(cvss_cve_2021_44228, CVSS30)
    assert cvss_cve_2021_44228.version == CvssVersion.three_zero
    assert cvss_cve_2021_44228.vector_string == CVSS30_VECTOR_STRING_LOG4J
    assert cvss_cve_2021_44228.base_score.__root__ == float(CVSS30_BASE_SCORE_LOG4J)
    assert cvss_cve_2021_44228.base_severity.critical == CVSS30_BASE_SEVERITY_LOG4J
    assert cvss_cve_2021_44228.confidentiality_requirement is None


def test_cvss31_empty():
    message = '3 validation errors for CVSS31'
    with pytest.raises(ValidationError, match=message) as err:
        _ = CVSS31()  # type: ignore
    assert '\nvector_string\n  field required' in str(err.value)
    assert '\nbase_score\n  field required' in str(err.value)
    assert '\nbase_severity\n  field required' in str(err.value)


def test_cvss31_wrong_version():
    data = {
        'version': '42',
        'vector_string': CVSS31_VECTOR_STRING_LOG4J,
        'base_score': CVSS31_BASE_SCORE_LOG4J,
        'base_severity': CVSS31_BASE_SEVERITY_LOG4J,
    }
    message = '1 validation error for CVSS'
    with pytest.raises(ValidationError, match=message) as err:
        _ = CVSS31(**data)
    assert '\nversion\n  value is not a valid enumeration member' in str(err.value)


def test_cvss31_log4j_cve_2021_44228():
    data = {
        'version': CvssVersion.three_wun,
        'vector_string': CVSS31_VECTOR_STRING_LOG4J,
        'base_score': CVSS31_BASE_SCORE_LOG4J,
        'base_severity': CVSS31_BASE_SEVERITY_LOG4J,
    }
    cvss_cve_2021_44228 = CVSS31(**data)
    assert isinstance(cvss_cve_2021_44228, CVSS31)
    assert cvss_cve_2021_44228.version == CvssVersion.three_wun
    assert cvss_cve_2021_44228.vector_string == CVSS31_VECTOR_STRING_LOG4J
    assert cvss_cve_2021_44228.base_score.__root__ == float(CVSS31_BASE_SCORE_LOG4J)
    assert cvss_cve_2021_44228.base_severity.critical == CVSS31_BASE_SEVERITY_LOG4J
    assert cvss_cve_2021_44228.confidentiality_requirement is None

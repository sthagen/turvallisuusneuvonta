# -*- coding: utf-8 -*-
# pylint: disable=line-too-long,missing-docstring,reimported,unused-import,unused-variable
import pytest
from pydantic.error_wrappers import ValidationError

from tests import conftest
from turvallisuusneuvonta.csaf.cvss.cvss import (
    CVSS2,
    CVSS30,
    CVSS31,
    SeverityType as CvssSeverityType,
    Version as CvssVersion,
)

CVSS31_BASE_SEVERITY_LOG4J = CvssSeverityType.critical
CVSS30_BASE_SEVERITY_LOG4J = CvssSeverityType.critical


def test_cvss2_empty():
    message = '2 validation errors for CVSS2'
    with pytest.raises(ValidationError, match=message) as err:
        _ = CVSS2()  # type: ignore
    assert '\nvector_string\n  field required' in str(err.value)
    assert '\nbase_score\n  field required' in str(err.value)


def test_cvss2_wrong_version():
    data = {
        'version': '42',
        'vector_string': conftest.CVSS2_VECTOR_STRING_LOG4J,
        'base_score': conftest.CVSS2_BASE_SCORE_LOG4J,
    }
    message = '1 validation error for CVSS'
    with pytest.raises(ValidationError, match=message) as err:
        _ = CVSS2(**data)
    assert '\nversion\n  value is not a valid enumeration member' in str(err.value)


def test_cvss20_log4j_cve_2021_44228():
    data = {
        'version': CvssVersion.two,
        'vector_string': conftest.CVSS2_VECTOR_STRING_LOG4J,
        'base_score': conftest.CVSS2_BASE_SCORE_LOG4J,
    }
    cvss_cve_2021_44228 = CVSS2(**data)
    assert isinstance(cvss_cve_2021_44228, CVSS2)
    assert cvss_cve_2021_44228.version == CvssVersion.two
    assert cvss_cve_2021_44228.vector_string == conftest.CVSS2_VECTOR_STRING_LOG4J
    assert cvss_cve_2021_44228.base_score.__root__ == float(conftest.CVSS2_BASE_SCORE_LOG4J)
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
        'vector_string': conftest.CVSS30_VECTOR_STRING_LOG4J,
        'base_score': conftest.CVSS30_BASE_SCORE_LOG4J,
        'base_severity': CVSS30_BASE_SEVERITY_LOG4J,
    }
    message = '1 validation error for CVSS'
    with pytest.raises(ValidationError, match=message) as err:
        _ = CVSS30(**data)
    assert '\nversion\n  value is not a valid enumeration member' in str(err.value)


def test_cvss30_log4j_cve_2021_44228():
    data = {
        'version': CvssVersion.three_zero,
        'vector_string': conftest.CVSS30_VECTOR_STRING_LOG4J,
        'base_score': conftest.CVSS30_BASE_SCORE_LOG4J,
        'base_severity': CVSS30_BASE_SEVERITY_LOG4J,
    }
    cvss_cve_2021_44228 = CVSS30(**data)
    assert isinstance(cvss_cve_2021_44228, CVSS30)
    assert cvss_cve_2021_44228.version == CvssVersion.three_zero
    assert cvss_cve_2021_44228.vector_string == conftest.CVSS30_VECTOR_STRING_LOG4J
    assert cvss_cve_2021_44228.base_score.__root__ == float(conftest.CVSS30_BASE_SCORE_LOG4J)
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
        'vector_string': conftest.CVSS31_VECTOR_STRING_LOG4J,
        'base_score': conftest.CVSS31_BASE_SCORE_LOG4J,
        'base_severity': CVSS31_BASE_SEVERITY_LOG4J,
    }
    message = '1 validation error for CVSS'
    with pytest.raises(ValidationError, match=message) as err:
        _ = CVSS31(**data)
    assert '\nversion\n  value is not a valid enumeration member' in str(err.value)


def test_cvss31_log4j_cve_2021_44228():
    data = {
        'version': CvssVersion.three_wun,
        'vector_string': conftest.CVSS31_VECTOR_STRING_LOG4J,
        'base_score': conftest.CVSS31_BASE_SCORE_LOG4J,
        'base_severity': CVSS31_BASE_SEVERITY_LOG4J,
    }
    cvss_cve_2021_44228 = CVSS31(**data)
    assert isinstance(cvss_cve_2021_44228, CVSS31)
    assert cvss_cve_2021_44228.version == CvssVersion.three_wun
    assert cvss_cve_2021_44228.vector_string == conftest.CVSS31_VECTOR_STRING_LOG4J
    assert cvss_cve_2021_44228.base_score.__root__ == float(conftest.CVSS31_BASE_SCORE_LOG4J)
    assert cvss_cve_2021_44228.base_severity.critical == CVSS31_BASE_SEVERITY_LOG4J
    assert cvss_cve_2021_44228.confidentiality_requirement is None

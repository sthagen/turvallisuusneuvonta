# -*- coding: utf-8 -*-
# pylint: disable=line-too-long,missing-docstring,reimported,unused-import,unused-variable
import pytest
from pydantic.error_wrappers import ValidationError

import turvallisuusneuvonta.csaf.cvss31.cvss31 as cvss31


def test_cvss2_empty():
    message = '4 validation errors for CVSS'
    with pytest.raises(ValidationError, match=message):
        _ = cvss31.CVSS()

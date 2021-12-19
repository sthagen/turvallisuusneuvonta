# -*- coding: utf-8 -*-
# pylint: disable=line-too-long,missing-docstring,reimported,unused-import,unused-variable
import pytest
from pydantic.error_wrappers import ValidationError

import turvallisuusneuvonta.csaf.cvss2.cvss2 as cvss2


def test_cvss2_empty():
    message = '3 validation errors for Field0'
    with pytest.raises(ValidationError, match=message):
        _ = cvss2.Field0()

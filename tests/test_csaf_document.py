# -*- coding: utf-8 -*-
# pylint: disable=line-too-long,missing-docstring,reimported,unused-import,unused-variable
import pytest
from pydantic.error_wrappers import ValidationError

import turvallisuusneuvonta.csaf.csaf as csaf


def test_foo():
    message = '5 validation errors for DocumentLevelMetaData'
    with pytest.raises(ValidationError, match=message):
        _ = csaf.CommonSecurityAdvisoryFramework(csaf.DocumentLevelMetaData())

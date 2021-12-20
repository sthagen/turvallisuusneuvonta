# -*- coding: utf-8 -*-
# pylint: disable=line-too-long,missing-docstring,reimported,unused-import,unused-variable
import pytest
from pydantic.error_wrappers import ValidationError

import turvallisuusneuvonta.csaf.csaf as csaf


def test_doc_empty_meta():
    message = '5 validation errors for DocumentLevelMetaData'
    with pytest.raises(ValidationError, match=message):
        _ = csaf.CommonSecurityAdvisoryFramework(csaf.DocumentLevelMetaData())  # type: ignore

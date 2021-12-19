# -*- coding: utf-8 -*-
# pylint: disable=line-too-long,missing-docstring,reimported,unused-import,unused-variable
import pytest
from pydantic.error_wrappers import ValidationError

import turvallisuusneuvonta.csaf.document as document


def test_meta_doc_empty():
    message = '5 validation errors for DocumentLevelMetaData'
    with pytest.raises(ValidationError, match=message):
        _ = document.DocumentLevelMetaData()

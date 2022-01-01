# -*- coding: utf-8 -*-
# pylint: disable=line-too-long,missing-docstring,reimported,unused-import,unused-variable
import turvallisuusneuvonta.csaf.core.rules.mandatory.mandatory as mandatory


def test_mandatory_exists_single_path():
    document = {'exists': 'truthy'}
    claims = {'sartre': ['exists']}
    assert mandatory.exists(document, claims) == (('sartre', 'exists', True),)

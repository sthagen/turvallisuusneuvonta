# -*- coding: utf-8 -*-
# pylint: disable=line-too-long,missing-docstring,reimported,unused-import,unused-variable
import turvallisuusneuvonta.csaf.core.rules.mandatory.mandatory as mandatory


def test_mandatory_exists_single_claim_single_path():
    document = {'exists': 'truthy'}
    claims = {'sartre': ['exists']}
    assert mandatory.exists(document, claims) == (('sartre', 'exists', True),)


def test_mandatory_exists_not_single_claim_single_path():
    document = {'exists': ''}
    claims = {'sartre': ['exists']}
    assert mandatory.exists(document, claims) == (('sartre', 'exists', False),)


def test_mandatory_exists_single_claim_multiple_paths():
    document = {'exists': 'truthy', 'also': True}
    claims = {'sartre': ['exists', 'also']}
    assert mandatory.exists(document, claims) == (
        ('sartre', 'exists', True),
        ('sartre', 'also', True),
    )

# -*- coding: utf-8 -*-
# pylint: disable=line-too-long,missing-docstring,reimported,unused-import,unused-variable
import pytest

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


def test_mandatory_exists_single_claim_multiple_paths_mixed_results():
    document = {'exists': 'truthy', 'also': False}
    claims = {'sartre': ['exists', 'also']}
    assert mandatory.exists(document, claims) == (
        ('sartre', 'exists', True),
        ('sartre', 'also', False),
    )


def test_mandatory_exists_multiple_claims_single_paths():
    document = {'exists': 'truthy', 'also': True}
    claims = {'sartre': ['exists'], 'nirvana': ['also']}
    assert mandatory.exists(document, claims) == (
        ('sartre', 'exists', True),
        ('nirvana', 'also', True),
    )


def test_mandatory_valid_category_name_exempt():
    document = {'name': mandatory.val_cat_nam.STOP_WORDS[0]}
    path = 'name'
    assert mandatory.must_skip(document, path, mandatory.val_cat_nam.STOP_WORDS) == (document['name'], path, True)


def test_mandatory_valid_category_name_not_exempt():
    document = {'name': '=x='.join(mandatory.val_cat_nam.STOP_WORDS)}
    path = 'name'
    assert mandatory.must_skip(document, path, mandatory.val_cat_nam.STOP_WORDS) == (document['name'], path, False)


@pytest.mark.parametrize('category, status', [(w, True) for w in mandatory.val_cat_nam.STOP_WORDS])
def test_mandatory_valid_category_name_ok_profiles(category, status):
    assert mandatory.val_cat_nam.is_valid(category) is status


@pytest.mark.parametrize('category, status', [(w.upper(), False) for w in mandatory.val_cat_nam.STOP_WORDS])
def test_mandatory_valid_category_name_nok_uppercase_profiles(category, status):
    assert mandatory.val_cat_nam.is_valid(category) is status


@pytest.mark.parametrize('category, status', [(w.title(), False) for w in mandatory.val_cat_nam.STOP_WORDS])
def test_mandatory_valid_category_name_nok_titlecase_profiles(category, status):
    assert mandatory.val_cat_nam.is_valid(category) is status

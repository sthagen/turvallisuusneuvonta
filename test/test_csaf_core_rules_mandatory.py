# -*- coding: utf-8 -*-
# pylint: disable=line-too-long,missing-docstring,reimported,unused-import,unused-variable
import json
import pathlib
import string

import pytest
from hypothesis import given, strategies as st

import turvallisuusneuvonta.csaf.core.rules.mandatory.mandatory as mandatory

ENCODING = 'utf-8'
PROFILE_SAFE_LETTERS = ('k', 'j', 'q', 'b', 'g', 'h', 'w', 'z')
PROFILE_MAX_LEN = max(len(profile) for profile in mandatory.val_cat_nam.PROFILES)
LOWER_ASCII = tuple(list(string.ascii_lowercase))


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
    document = {'name': mandatory.val_cat_nam.PROFILES[0]}
    path = 'name'
    assert mandatory.must_skip(document, path, mandatory.val_cat_nam.PROFILES) == (document['name'], path, True)


def test_mandatory_valid_category_name_not_exempt():
    document = {'name': '=x='.join(mandatory.val_cat_nam.PROFILES)}
    path = 'name'
    assert mandatory.must_skip(document, path, mandatory.val_cat_nam.PROFILES) == (document['name'], path, False)


@given(st.text(min_size=1, max_size=2))
def test_mandatory_valid_ok_too_short_for_profile(category):
    incomplete = NotImplemented
    assert mandatory.is_valid({'document': {'category': category}}) is incomplete


@given(st.text(min_size=3, max_size=PROFILE_MAX_LEN))
def test_mandatory_valid_ok_at_least_one_char_separate_from_profile(category):
    incomplete = NotImplemented
    category = PROFILE_SAFE_LETTERS[0] + category[1:]
    assert mandatory.is_valid({'document': {'category': category}}) is incomplete


@given(st.text(alphabet=PROFILE_SAFE_LETTERS, min_size=3, max_size=PROFILE_MAX_LEN))
def test_mandatory_valid_ok_profile_safe_alphabet(category_part):
    incomplete = NotImplemented
    category = category_part + PROFILE_SAFE_LETTERS[0]
    assert mandatory.is_valid({'document': {'category': category}}) is incomplete


@given(st.text(alphabet=LOWER_ASCII, min_size=PROFILE_MAX_LEN + 1, max_size=PROFILE_MAX_LEN + 3))
def test_mandatory_valid_ok_too_long_for_profile(category):
    incomplete = NotImplemented
    assert mandatory.is_valid({'document': {'category': category}}) is incomplete


@pytest.mark.parametrize('category, status', [(' ', True), ('-', True), ('_', True), ('1', True), ('9', True)])
def test_mandatory_valid_ok_irrelevant_and_digits(category, status):
    incomplete = NotImplemented if status is True else False
    assert mandatory.is_valid({'document': {'category': category}}) is incomplete


@pytest.mark.parametrize('category, status', [(w.upper(), False) for w in mandatory.val_cat_nam.PROFILES])
def test_mandatory_valid_nok_uppercase_profiles(category, status):
    incomplete = NotImplemented if status is True else False
    assert mandatory.is_valid({'document': {'category': category}}) is incomplete


@pytest.mark.parametrize('category, status', [(' ', True), ('-', True), ('_', True), ('1', True), ('9', True)])
def test_mandatory_valid_category_ok_irrelevant_and_digits(category, status):
    assert mandatory.is_valid_category({'document': {'category': category}}) is status


@pytest.mark.parametrize('category, status', [(f'abc{w}xyz', True) for w in mandatory.val_cat_nam.PROFILES])
def test_mandatory_valid_category_ok_no_profiles(category, status):
    assert mandatory.is_valid_category({'document': {'category': category}}) is status


@pytest.mark.parametrize('category, status', [(w, True) for w in mandatory.val_cat_nam.PROFILES])
def test_mandatory_valid_category_ok_profiles(category, status):
    assert mandatory.is_valid_category({'document': {'category': category}}) is status


@pytest.mark.parametrize('category, status', [(w.upper(), False) for w in mandatory.val_cat_nam.PROFILES])
def test_mandatory_valid_category_nok_uppercase_profiles(category, status):
    assert mandatory.is_valid_category({'document': {'category': category}}) is status


@pytest.mark.parametrize('category, status', [(w.title(), False) for w in mandatory.val_cat_nam.PROFILES])
def test_mandatory_valid_category_nok_titlecase_profiles(category, status):
    assert mandatory.is_valid_category({'document': {'category': category}}) is status


@pytest.mark.parametrize('category, status', [(f' {w}', False) for w in mandatory.val_cat_nam.PROFILES])
def test_mandatory_valid_category_nok_leading_space_profiles(category, status):
    assert mandatory.is_valid_category({'document': {'category': category}}) is status


@pytest.mark.parametrize('category, status', [(f'{w} ', False) for w in mandatory.val_cat_nam.PROFILES])
def test_mandatory_valid_category_nok_trailing_space_profiles(category, status):
    assert mandatory.is_valid_category({'document': {'category': category}}) is status


@pytest.mark.parametrize('category, status', [(f'-{w}', False) for w in mandatory.val_cat_nam.PROFILES])
def test_mandatory_valid_category_nok_leading_dash_profiles(category, status):
    assert mandatory.is_valid_category({'document': {'category': category}}) is status


@pytest.mark.parametrize('category, status', [(f'{w}-', False) for w in mandatory.val_cat_nam.PROFILES])
def test_mandatory_valid_category_nok_trailing_dash_profiles(category, status):
    assert mandatory.is_valid_category({'document': {'category': category}}) is status


@pytest.mark.parametrize('category, status', [(f'_{w}', False) for w in mandatory.val_cat_nam.PROFILES])
def test_mandatory_valid_category_nok_leading_underscore_profiles(category, status):
    assert mandatory.is_valid_category({'document': {'category': category}}) is status


@pytest.mark.parametrize('category, status', [(f'{w}_', False) for w in mandatory.val_cat_nam.PROFILES])
def test_mandatory_valid_category_nok_trailing_underscore_profiles(category, status):
    assert mandatory.is_valid_category({'document': {'category': category}}) is status


@pytest.mark.parametrize('category, status', [(f'- _{w}', False) for w in mandatory.val_cat_nam.PROFILES])
def test_mandatory_valid_category_nok_leading_irrelevant_profiles(category, status):
    assert mandatory.is_valid_category({'document': {'category': category}}) is status


@pytest.mark.parametrize('category, status', [(f'{w}__  --  _', False) for w in mandatory.val_cat_nam.PROFILES])
def test_mandatory_valid_category_nok_trailing_irrelevant_profiles(category, status):
    assert mandatory.is_valid_category({'document': {'category': category}}) is status


@pytest.mark.parametrize('category, status', [(' ', True), ('-', True), ('_', True), ('1', True), ('9', True)])
def test_mandatory_valid_category_name_ok_irrelevant_and_digits(category, status):
    assert mandatory.val_cat_nam.is_valid(category) is status


@pytest.mark.parametrize('category, status', [(f'abc{w}xyz', True) for w in mandatory.val_cat_nam.PROFILES])
def test_mandatory_valid_category_name_ok_no_profiles(category, status):
    assert mandatory.val_cat_nam.is_valid(category) is status


@pytest.mark.parametrize('category, status', [(w, True) for w in mandatory.val_cat_nam.PROFILES])
def test_mandatory_valid_category_name_ok_profiles(category, status):
    assert mandatory.val_cat_nam.is_valid(category) is status


@pytest.mark.parametrize('category, status', [(w.upper(), False) for w in mandatory.val_cat_nam.PROFILES])
def test_mandatory_valid_category_name_nok_uppercase_profiles(category, status):
    assert mandatory.val_cat_nam.is_valid(category) is status


@pytest.mark.parametrize('category, status', [(w.title(), False) for w in mandatory.val_cat_nam.PROFILES])
def test_mandatory_valid_category_name_nok_titlecase_profiles(category, status):
    assert mandatory.val_cat_nam.is_valid(category) is status


@pytest.mark.parametrize('category, status', [(f' {w}', False) for w in mandatory.val_cat_nam.PROFILES])
def test_mandatory_valid_category_name_nok_leading_space_profiles(category, status):
    assert mandatory.val_cat_nam.is_valid(category) is status


@pytest.mark.parametrize('category, status', [(f'{w} ', False) for w in mandatory.val_cat_nam.PROFILES])
def test_mandatory_valid_category_name_nok_trailing_space_profiles(category, status):
    assert mandatory.val_cat_nam.is_valid(category) is status


@pytest.mark.parametrize('category, status', [(f'-{w}', False) for w in mandatory.val_cat_nam.PROFILES])
def test_mandatory_valid_category_name_nok_leading_dash_profiles(category, status):
    assert mandatory.val_cat_nam.is_valid(category) is status


@pytest.mark.parametrize('category, status', [(f'{w}-', False) for w in mandatory.val_cat_nam.PROFILES])
def test_mandatory_valid_category_name_nok_trailing_dash_profiles(category, status):
    assert mandatory.val_cat_nam.is_valid(category) is status


@pytest.mark.parametrize('category, status', [(f'_{w}', False) for w in mandatory.val_cat_nam.PROFILES])
def test_mandatory_valid_category_name_nok_leading_underscore_profiles(category, status):
    assert mandatory.val_cat_nam.is_valid(category) is status


@pytest.mark.parametrize('category, status', [(f'{w}_', False) for w in mandatory.val_cat_nam.PROFILES])
def test_mandatory_valid_category_name_nok_trailing_underscore_profiles(category, status):
    assert mandatory.val_cat_nam.is_valid(category) is status


@pytest.mark.parametrize('category, status', [(f'- _{w}', False) for w in mandatory.val_cat_nam.PROFILES])
def test_mandatory_valid_category_name_nok_leading_irrelevant_profiles(category, status):
    assert mandatory.val_cat_nam.is_valid(category) is status


@pytest.mark.parametrize('category, status', [(f'{w}__  --  _', False) for w in mandatory.val_cat_nam.PROFILES])
def test_mandatory_valid_category_name_nok_trailing_irrelevant_profiles(category, status):
    assert mandatory.val_cat_nam.is_valid(category) is status


def test_mandatory_valid_category_nok_spec_example():
    path = pathlib.Path('tests/fixtures/rules/invalid/upstream/6-1-26-01.json')
    with open(path, 'rt', encoding=ENCODING) as handle:
        document = json.load(handle)
    assert mandatory.is_valid(document) is False


def test_mandatory_valid_translator_nok_spec_example():
    path = pathlib.Path('tests/fixtures/rules/invalid/upstream/6-1-15-01.json')
    with open(path, 'rt', encoding=ENCODING) as handle:
        document = json.load(handle)
    assert mandatory.is_valid(document) is False


def test_mandatory_defined_product_id_nok_spec_example():
    path = pathlib.Path('tests/fixtures/rules/invalid/upstream/6-1-01-01.json')
    with open(path, 'rt', encoding=ENCODING) as handle:
        document = json.load(handle)
    assert mandatory.is_valid(document) is False


def test_mandatory_defined_group_id_nok_spec_example():
    path = pathlib.Path('tests/fixtures/rules/invalid/upstream/6-1-04-01.json')
    with open(path, 'rt', encoding=ENCODING) as handle:
        document = json.load(handle)
    assert mandatory.is_valid(document) is False


def test_mandatory_unique_product_id_nok_spec_example():
    path = pathlib.Path('tests/fixtures/rules/invalid/upstream/6-1-02-01.json')
    with open(path, 'rt', encoding=ENCODING) as handle:
        document = json.load(handle)
    assert mandatory.is_valid(document) is False


def test_mandatory_is_valid_unique_product_ids_nok_spec_example():
    path = pathlib.Path('tests/fixtures/rules/invalid/upstream/6-1-02-01.json')
    with open(path, 'rt', encoding=ENCODING) as handle:
        document = json.load(handle)
    assert mandatory.is_valid_unique_product_ids(document) is False


def test_mandatory_unique_group_id_nok_spec_example():
    path = pathlib.Path('tests/fixtures/rules/invalid/upstream/6-1-05-01.json')
    with open(path, 'rt', encoding=ENCODING) as handle:
        document = json.load(handle)
    assert mandatory.is_valid(document) is False


def test_mandatory_valid_ok_grow_me():
    document = {'document': {'category': ' ', 'publisher': {'category': 'translator'}, 'source_lang': 'fr'}}
    incomplete = NotImplemented
    assert mandatory.is_valid(document) is incomplete

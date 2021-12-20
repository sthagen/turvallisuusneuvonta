# -*- coding: utf-8 -*-
# pylint: disable=line-too-long,missing-docstring,reimported,unused-import,unused-variable
import copy
import pathlib

import pytest

import turvallisuusneuvonta.turvallisuusneuvonta as tu
from tests import conftest


def test_tu_main():
    inp = str(pathlib.Path('tests', 'fixtures', 'empty', 'advisory.json'))
    assert tu.main(['verify', inp, '']) == 2


def test_tu_verify_request_too_few():
    assert tu.verify_request([1]) == (2, 'received wrong number of arguments', [''])


def test_tu_verify_request_unknown_command():
    assert tu.verify_request(['unknown', 'later', 'does not matter']) == (2, 'received unknown command', [''])


def test_tu_verify_request_falsy_input():
    argv = ['verify', '', '']
    assert tu.verify_request(argv) == (2, 'configuration missing', [''])


def test_what_empty():
    assert tu.peek('') == 'TOO_SHORT'


def test_what_too_short():
    assert tu.peek('1' * (tu.CSAF_MIN_BYTES - 1)) == 'TOO_SHORT'


def test_what_unknown():
    assert tu.peek('1' * tu.CSAF_MIN_BYTES) == 'UNKNOWN'


def test_what_json():
    assert tu.peek(' ' * (tu.CSAF_MIN_BYTES - 1) + '{') == 'JSON'


def test_what_xml():
    assert tu.peek(' ' * (tu.CSAF_MIN_BYTES - 1) + '<') == 'XML'


def test_reader_empty():
    inp = str(pathlib.Path('tests', 'fixtures', 'empty', 'advisory.json'))
    assert next(tu.reader(inp)).strip() == '{}'


def test_verify_json_empty():
    assert tu.verify_json('') == (1, 'advisory is no valid JSON', [])


def test_verify_json_empty_object():
    assert tu.verify_json('{}') == (1, 'missing document property', [])


def test_verify_json_csaf_spam_object():
    message = 'missing document.publisher property (category)'
    assert tu.verify_json(conftest.SPAM_JSON) == (1, message, [])


def test_level_zero_csaf_spam_object():
    message = 'missing document.publisher property (category)'
    assert tu.level_zero(conftest.SPAM) == (1, message)


@pytest.mark.parametrize('prop', ['category', 'csaf_version', 'publisher', 'title', 'tracking'])
def test_level_zero_document_missing_mandatory_key(prop):
    document_missing_publisher = copy.deepcopy(conftest.SPAM)
    parent = 'document'
    del document_missing_publisher[parent][prop]
    assert tu.level_zero(document_missing_publisher) == (1, f'missing {parent} property ({prop})')


@pytest.mark.parametrize('version', ['', '1', '2', '2.', '2.00', '2_0', '2.0.', '2.0.0', ['2.0'], {'en': 'try'}])
def test_level_zero_document_wrong_csaf_version_values(version):
    document_missing_publisher = copy.deepcopy(conftest.SPAM)
    parent, prop = 'document', 'csaf_version'
    document_missing_publisher[parent][prop] = version
    expectation = (1, f'property {parent}.{prop} present but ({version}) not matching CSAF version 2.0')
    if version == '':
        expectation = (1, f'missing {parent} property ({prop})')
    elif version in (['2.0'], {'en': 'try'}):
        expectation = (1, f'property {parent}.{prop} present but no text')
    assert tu.level_zero(document_missing_publisher) == expectation


def test_document_optional_csaf_example_com_123():
    document = copy.deepcopy(conftest.CSAF_WITH_DOCUMENTS['document'])
    message = 'NotImplemented'
    assert tu.document_optional(document) == (0, message)


def test_document_aggregate_severity_csaf_example_com_123():
    document = copy.deepcopy(conftest.CSAF_WITH_DOCUMENTS['document'])
    message = 'NotImplemented'
    assert tu.document_optional(document['aggregate_severity']) == (0, message)


@pytest.mark.parametrize('value', ['en', 'fr', 'de', 'de-ch', 'en_EN', 'talking', 'ok', '', [], {}])
def test_document_optional_csaf_example_com_123_lang(value):
    parent, prop = 'document', 'lang'
    document = copy.deepcopy(conftest.CSAF_WITH_DOCUMENTS[parent])
    document[prop] = value
    expectation = (0, '')
    if value in ('en_EN', 'talking', 'ok'):
        expectation = (1, f'property {parent}.{prop} present but ({value}) is no valid language tag')
    elif value == '':
        expectation = (1, f'property {parent}.{prop} present but empty')
    elif value in ([], {}):
        expectation = (1, f'property {parent}.{prop} present but no text')
    assert tu.document_lang(document[prop]) == expectation


@pytest.mark.parametrize('values', ['', 'a string', [], {}, {'en': 'try'}])
def test_document_optional_csaf_example_com_123_wrong_acknowledgments(values):
    document = copy.deepcopy(conftest.CSAF_WITH_DOCUMENTS['document'])
    prop = 'acknowledgments'
    document[prop] = values
    message = 'optional document property acknowledgments present but '
    message += 'empty' if isinstance(values, list) else 'no array'
    assert tu.document_optional(document) == (1, message)


@pytest.mark.parametrize('values', ['', 'a string', [], {}, {'en': 'try'}])
def test_document_optional_csaf_example_com_123_wrong_acknowledgments_names(values):
    document = copy.deepcopy(conftest.CSAF_WITH_DOCUMENTS['document'])
    prop = 'acknowledgments'
    aspect = 'names'
    document[prop][0][aspect] = values
    message = f'optional properties of document.acknowledgments[0] property {aspect} present but '
    message += 'empty' if isinstance(values, list) else 'no array'
    assert tu.document_optional(document) == (1, message)


@pytest.mark.parametrize(
    'values, what',
    [
        ([''], '[0][0] property names entry present but empty'),
        (['ok', ''], '[0][1] property names entry present but empty'),
        ([{}], '[0][0] property names entry present but no text'),
        ([{'en': 'try'}], '[0][0] property names entry present but no text'),
    ],
)
def test_document_optional_csaf_example_com_123_wrong_acknowledgments_names_entries(values, what):
    document = copy.deepcopy(conftest.CSAF_WITH_DOCUMENTS['document'])
    prop = 'acknowledgments'
    aspect = 'names'
    document[prop][0][aspect] = values
    message = f'optional properties of document.{prop}{what}'
    assert tu.document_optional(document) == (1, message)


@pytest.mark.parametrize('values', ['', 'a string', [], {}, {'en': 'try'}])
def test_document_optional_csaf_example_com_123_wrong_acknowledgments_urls(values):
    document = copy.deepcopy(conftest.CSAF_WITH_DOCUMENTS['document'])
    prop = 'acknowledgments'
    aspect = 'urls'
    document[prop][0][aspect] = values
    message = f'optional properties of document.acknowledgments[0] property {aspect} present but '
    message += 'empty' if isinstance(values, list) else 'no array'
    assert tu.document_optional(document) == (1, message)


@pytest.mark.parametrize(
    'values, what',
    [
        ([''], '[0][0] property urls entry present but empty'),
        (['https://example.com', ''], '[0][1] property urls entry present but empty'),
        (['not ok'], '[0][0] property urls entry present but invalid as URI("not ok" is not a valid URI)'),
        ([{}], '[0][0] property urls entry present but no text'),
        ([{'en': 'try'}], '[0][0] property urls entry present but no text'),
    ],
)
def test_document_optional_csaf_example_com_123_wrong_acknowledgments_urls_entries(values, what):
    document = copy.deepcopy(conftest.CSAF_WITH_DOCUMENTS['document'])
    prop = 'acknowledgments'
    aspect = 'urls'
    document[prop][0][aspect] = values
    message = f'optional properties of document.{prop}{what}'
    assert tu.document_optional(document) == (1, message)


@pytest.mark.parametrize('values', ['', [], ['entry'], {}, {'en': 'try'}])
def test_document_optional_csaf_example_com_123_wrong_acknowledgments_organization(values):
    document = copy.deepcopy(conftest.CSAF_WITH_DOCUMENTS['document'])
    prop = 'acknowledgments'
    aspect = 'organization'
    document[prop][0][aspect] = values
    message = f'optional properties of document.acknowledgments[0] property {aspect} present but '
    message += 'empty' if isinstance(values, str) else 'no text'
    assert tu.document_optional(document) == (1, message)


@pytest.mark.parametrize('values', ['', [], ['entry'], {}, {'en': 'try'}])
def test_document_optional_csaf_example_com_123_wrong_acknowledgments_summary(values):
    document = copy.deepcopy(conftest.CSAF_WITH_DOCUMENTS['document'])
    prop = 'acknowledgments'
    aspect = 'summary'
    document[prop][0][aspect] = values
    message = f'optional properties of document.acknowledgments[0] property {aspect} present but '
    message += 'empty' if isinstance(values, str) else 'no text'
    assert tu.document_optional(document) == (1, message)

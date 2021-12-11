# -*- coding: utf-8 -*-
# pylint: disable=line-too-long,missing-docstring,reimported,unused-import,unused-variable
import copy
import pathlib

import orjson
import pytest

import turvallisuusneuvonta.turvallisuusneuvonta as tu

SPAM = {
    'document': {
        'csaf_version': '2.0',
        'publisher': ' ',
        'title': ' ',
        'tracking': ' ',
        'status': ' ',
        'version': ' ',
        'type': ' ',
    }
}

SPAM_JSON = orjson.dumps(SPAM)


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
    assert tu.verify_json(SPAM_JSON) == (0, 'OK', [])


def test_level_zero_csaf_spam_object():
    assert tu.level_zero(SPAM) == (0, '')


@pytest.mark.parametrize('prop', ['csaf_version', 'publisher', 'title', 'tracking', 'status', 'version', 'type'])
def test_level_zero_document_missing_mandatory_key(prop):
    document_missing_publisher = copy.deepcopy(SPAM)
    parent = 'document'
    del document_missing_publisher[parent][prop]
    assert tu.level_zero(document_missing_publisher) == (1, f'missing {parent} property ({prop})')

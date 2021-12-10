# -*- coding: utf-8 -*-
# pylint: disable=line-too-long,missing-docstring,reimported,unused-import,unused-variable
import pathlib

import turvallisuusneuvonta.turvallisuusneuvonta as tu


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
    assert tu.what('') == 'TOO_SHORT'


def test_what_too_short():
    assert tu.what('1' * 41) == 'TOO_SHORT'


def test_what_unknown():
    assert tu.what('42' * 21) == 'UNKNOWN'


def test_what_json():
    assert tu.what(' ' * 41 + '{') == 'JSON'

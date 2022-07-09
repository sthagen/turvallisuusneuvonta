# -*- coding: utf-8 -*-
# pylint: disable=line-too-long,missing-docstring,reimported,unused-import,unused-variable
import pathlib

import click
import pytest

import turvallisuusneuvonta.cli as cli


def test_main_legacy_ok(capsys):
    inp = str(pathlib.Path('tests', 'fixtures', 'empty', 'advisory.json'))
    assert cli.main(['verify', inp, '']) == 2
    out, err = capsys.readouterr()
    assert not out
    assert 'configuration missing' in err.lower()


def test_callback_version_false(capsys):
    assert cli.callback(version=False) is None
    out, err = capsys.readouterr()
    assert not out
    assert not err.lower()


def test_version_ok(capsys):
    with pytest.raises(click.exceptions.Exit):
        cli.app_version()
    out, err = capsys.readouterr()
    assert 'version' in out.lower()
    assert not err


def test_now_ok(capsys):
    in_path = pathlib.Path('tests', 'fixtures', 'empty', 'advisory.json')
    with pytest.raises(SystemExit) as exec_info:
        cli.verify(conf=str(in_path))
        assert exec_info.value.code == 0
        out, err = capsys.readouterr()
        assert 'would verify advisory' in out.lower()
        assert not err


def test_translate_non_existing_html(capsys):
    in_path = pathlib.Path('does', 'not', 'exist', 'hypothetical.json')
    with pytest.raises(SystemExit) as exec_info:
        cli.verify(conf=str(in_path))
        assert exec_info.value.code == 1
        out, err = capsys.readouterr()
        assert 'source' in out.lower()
        assert 'is no file' in out.lower()
        assert not err

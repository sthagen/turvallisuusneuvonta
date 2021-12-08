#! /usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=line-too-long
"""Commandline API gateway for turvallisuusneuvonta."""
import pathlib
import sys
from typing import List, Union

import typer

import turvallisuusneuvonta
import turvallisuusneuvonta.turvallisuusneuvonta as tu

APP_NAME = 'Security advisory (Finnish: turvallisuusneuvonta) audit tool.'
APP_ALIAS = 'turvallisuusneuvonta'
app = typer.Typer(
    add_completion=False,
    context_settings={'help_option_names': ['-h', '--help']},
    no_args_is_help=True,
)


@app.callback(invoke_without_command=True)
def callback(
    version: bool = typer.Option(
        False,
        '-V',
        '--version',
        help='Display the turvallisuusneuvonta version and exit',
        is_eager=True,
    )
) -> None:
    """
    Security advisory (Finnish: turvallisuusneuvonta) audit tool.
    """
    if version:
        typer.echo(f'{APP_NAME} version {turvallisuusneuvonta.__version__}')
        raise typer.Exit()


@app.command('verify')
def verify(
    source: str = typer.Argument(tu.STDIN),
    inp: str = typer.Option(
        '',
        '-i',
        '--input',
        help='Path to input file (default is reading from standard in)',
        metavar='<sourcepath>',
    ),
    conf: str = typer.Option(
        '',
        '-c',
        '--config',
        help='Path to config file (default is $HOME/.turvallisuusneuvonta.json)',
        metavar='<configpath>',
    ),
) -> int:
    """
    Answer the question if now is a working hour.
    """
    command = 'verify'
    incoming = inp if inp else (source if source != tu.STDIN else '')
    config = conf if conf else pathlib.Path.home() / tu.DEFAULT_CONFIG_NAME
    action = [command, str(incoming), str(config)]
    return sys.exit(tu.main(action))


@app.command('version')
def app_version() -> None:
    """
    Display the turvallisuusneuvonta version and exit
    """
    callback(True)


# pylint: disable=expression-not-assigned
# @app.command()
def main(argv: Union[List[str], None] = None) -> int:
    """Delegate processing to functional module."""
    argv = sys.argv[1:] if argv is None else argv
    return tu.main(argv)

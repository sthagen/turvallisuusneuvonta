# -*- coding: utf-8 -*-
# pylint: disable=expression-not-assigned,line-too-long
"""Security advisory (Finnish: turvallisuusneuvonta) audit tool. API.

Minimal length of CSAF (spam) JSON is 116 bytes:
0        1         2         3         4         5         6         7         8         9         10        11
12345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456
{"document":{"csaf_version":"2.0","publisher":" ","title":" ","tracking":" ","status":" ","version":" ","type":" "}}
"""
import os
import pathlib
import sys
from typing import Iterator, List, Optional, Tuple, Union, no_type_check

import jmespath
import orjson

DEBUG_VAR = 'TURVALLISUUSNEUVONTA_DEBUG'
DEBUG = os.getenv(DEBUG_VAR)

ENCODING = 'utf-8'
ENCODING_ERRORS_POLICY = 'ignore'

DEFAULT_CONFIG_NAME = '.turvallisuusneuvonta.json'

STDIN, STDOUT = 'STDIN', 'STDOUT'
DISPATCH = {
    STDIN: sys.stdin,
    STDOUT: sys.stdout,
}

CSAF_MIN_BYTES = 116


@no_type_check
def level_zero(doc):
    """Most superficial verification."""
    if not doc.get('document'):
        return 1, 'missing document property'

    document = doc['document']
    for prop in ('csaf_version', 'publisher', 'title', 'tracking', 'status', 'version', 'type'):
        if not document.get(prop):
            return 1, f'missing document property ({prop})'

    csaf_version = jmespath.search('document.csaf_version', doc)
    if not csaf_version or csaf_version != '2.0':
        return 1, f'wrong document property csaf_version value ({csaf_version})'

    return 0, ''


def reader(path: str) -> Iterator[str]:
    """Context wrapper / generator to read the lines."""
    with open(pathlib.Path(path), 'rt', encoding=ENCODING) as handle:
        for line in handle:
            yield line


def peek(data: str) -> str:
    """Determine trivial format of data."""
    if len(data) < CSAF_MIN_BYTES:
        return 'TOO_SHORT'
    sample = data[:CSAF_MIN_BYTES].strip()
    if sample.startswith('{'):
        return 'JSON'
    if sample.startswith('<'):
        return 'XML'
    return 'UNKNOWN'


def verify_request(argv: Optional[List[str]]) -> Tuple[int, str, List[str]]:
    """Fail with grace."""
    if not argv or len(argv) != 3:
        return 2, 'received wrong number of arguments', ['']

    command, inp, config = argv

    if command not in ('verify',):
        return 2, 'received unknown command', ['']

    if inp:
        if not pathlib.Path(str(inp)).is_file():
            return 1, 'source is no file', ['']

    if not config:
        return 2, 'configuration missing', ['']

    config_path = pathlib.Path(str(config))
    if not config_path.is_file():
        return 1, f'config ({config_path}) is no file', ['']
    if not ''.join(config_path.suffixes).lower().endswith('.json'):
        return 1, 'config has not .json extension', ['']

    return 0, '', argv


def verify_json(data: str) -> Tuple[int, str, List[str]]:
    """Verify the JSON as CSAF."""
    try:
        doc = orjson.loads(data)
    except orjson.JSONDecodeError:
        return 1, 'advisory is no valid JSON', []

    error, message = level_zero(doc)
    if error:
        return error, message, []
    return 0, 'OK', []


def main(argv: Union[List[str], None] = None) -> int:
    """Drive the lookup."""
    error, message, strings = verify_request(argv)
    if error:
        print(message, file=sys.stderr)
        return error

    command, inp, config = strings

    with open(config, 'rb') as handle:
        configuration = orjson.loads(handle.read())

    print(f'using configuration ({configuration})')
    source = sys.stdin if not inp else reader(inp)
    data = ''.join(line for line in source)

    guess = peek(data)

    if guess == 'TOO_SHORT':
        print('advisory is too short to be valid')
        return 1

    if guess == 'UNKNOWN':
        print('advisory is of unknown format')
        return 1

    if guess == 'JSON':
        error, message, strings = verify_json(data)
        if error:
            print(message, file=sys.stderr)
            return error
        # Later post process the business rules (spec tests) here
        print('OK')
        return 0

    print('advisory may be XML')
    if 'DocumentTitle>' not in data:
        print('advisory is no valid CVRF')
        return 1

    print('advisory may be valid CVRF')
    return 0

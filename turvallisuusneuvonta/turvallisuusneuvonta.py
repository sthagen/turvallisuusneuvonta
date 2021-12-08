# -*- coding: utf-8 -*-
# pylint: disable=expression-not-assigned,line-too-long
"""Working hours (Danish arbejdstimer) or not? API."""
import json
import os
import pathlib
import sys
from typing import Iterator, List, Optional, Tuple, Union

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


def reader(path: str) -> Iterator[str]:
    """Context wrapper / generator to read the lines."""
    with open(pathlib.Path(path), 'rt', encoding=ENCODING) as handle:
        for line in handle:
            yield line


def verify_request(argv: Optional[List[str]]) -> Tuple[int, str, List[str]]:
    """Fail with grace."""
    if not argv or len(argv) != 3:
        return 2, 'received wrong number of arguments', ['']

    command, inp, config = argv

    if command not in ('verify'):
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


def main(argv: Union[List[str], None] = None) -> int:
    """Drive the lookup."""
    error, message, strings = verify_request(argv)
    if error:
        print(message, file=sys.stderr)
        return error

    command, inp, config = strings

    with open(config, 'rt', encoding=ENCODING) as handle:
        configuration = json.load(handle)

    print(f'using configuration ({configuration})')
    source = sys.stdin if not inp else reader(inp)
    data = ''.join(line for line in source)
    try:
        doc = json.loads(data)
    except RuntimeError:
        print('advisory is no valid JSON')
        return 1

    if not doc:
        print('advisory is empty')
        return 1

    print('OK')
    return 0

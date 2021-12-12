# -*- coding: utf-8 -*-
# pylint: disable=expression-not-assigned,line-too-long
"""Security advisory (Finnish: turvallisuusneuvonta) audit tool. API.

Minimal length of CSAF (spam) JSON is 116 bytes:
0        1         2         3         4         5         6         7         8         9
12345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012
{"document":{"category":" ","csaf_version":"2.0","publisher":{},"title":" ","tracking":{}}}}
"""
import os
import pathlib
import sys
from itertools import chain
from typing import Iterator, List, Optional, Tuple, Union, no_type_check

import jmespath
import orjson
from lazr.uri import URI, InvalidURIError  # type: ignore

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

CSAF_MIN_BYTES = 92


@no_type_check
def document_optional_acknowledgments(values):
    """Verify optional properties of document/acknowledgments if present follow rules."""
    parent, prop = 'document', 'acknowledgments'
    if not isinstance(values, list):
        return 1, f'optional {parent} property {prop} present but no array'
    if not values:
        return 1, f'optional {parent} property {prop} present but empty'
    ack_opt_props = ('names', 'organization', 'summary', 'urls')
    min_props, max_props = 1, len(ack_opt_props)
    ack_known_props = {el for el in ack_opt_props}
    for pos, value in enumerate(values):
        jp = f'properties of {parent}.{prop}[{pos}]'
        # print(pos, value)
        ack_found_props = {el for el in value}
        # print(ack_found_props)
        if ack_found_props <= ack_known_props:
            print(f'set of {jp} only contains known properties')
        if ack_found_props < ack_known_props:
            print(f'set of {jp} is a proper subset of the known properties')
        nr_distinct_found_props = len(ack_found_props)
        if nr_distinct_found_props < min_props:
            return 1, f'found too few properties ({nr_distinct_found_props}) for {jp}'
        if max_props < nr_distinct_found_props:
            return 1, f'found too many properties ({nr_distinct_found_props}) for {jp}'

        for what in ('names', 'urls'):
            if what not in ack_found_props:
                continue
            seq = value[what]
            if not isinstance(seq, list):
                return 1, f'optional {jp} property {what} present but no array'
            if not len(seq):
                return 1, f'optional {jp} property {what} present but empty'
            for ndx, text in enumerate(seq):
                jpn = f'{jp}[{ndx}]'
                if not isinstance(text, str):
                    return 1, f'optional {jpn} property {what} entry present but no text'
                if not len(text):
                    return 1, f'optional {jpn} property {what} entry present but empty'
                if what == 'urls':
                    try:
                        _ = URI(text)
                    except InvalidURIError as err:
                        return 1, f'optional {jpn} property {what} entry present but invalid as URI({err})'

        for what in ('organization', 'summary'):
            if what not in ack_found_props:
                continue
            text = value[what]
            if not isinstance(text, str):
                return 1, f'optional {jp} property {what} present but no text'
            if not len(text):
                return 1, f'optional {jp} property {what} present but empty'
    return 0, ''


@no_type_check
def document_optional(document):
    """Verify optional properties of document if present follow rules."""
    norm_props = ('category', 'csaf_version', 'publisher', 'title', 'tracking')
    opt_props = ('acknowledgments', 'aggregate_severity', 'distribution', 'lang', 'notes', 'references', 'source_lang')
    known_props = {el for el in chain(norm_props, opt_props)}
    opt_map = {el: None for el in opt_props}
    parent = 'document'
    for prop in opt_props:
        value = jmespath.search(f'{prop}', document)
        if value is not None:
            opt_map[prop] = value

    prop = 'acknowledgments'
    if opt_map[prop] is not None:
        error, message = document_optional_acknowledgments(opt_map[prop])
        if error:
            return error, message

    found_props = {el for el in document}
    if found_props <= known_props:
        print(f'set of {parent} properties only contains known properties')
    if found_props < known_props:
        print(f'set of {parent} properties is a proper subset of the known properties')

    return 0, 'NotImplemented'


@no_type_check
def level_zero(csaf_doc):
    """Most superficial verification."""
    if not csaf_doc.get('document'):
        return 1, 'missing document property'

    parent = 'document'
    for prop in ('category', 'csaf_version', 'publisher', 'title', 'tracking'):
        if not jmespath.search(f'{parent}.{prop}', csaf_doc):
            return 1, f'missing {parent} property ({prop})'

    parent = 'document'
    prop = 'category'
    if not jmespath.search(f'{parent}.{prop}', csaf_doc).strip():
        print(f'warning - {parent} property {prop} value is space-only')

    parent = 'document'
    prop = 'csaf_version'
    csaf_version = jmespath.search(f'{parent}.{prop}', csaf_doc)
    if not csaf_version or csaf_version != '2.0':
        return 1, f'wrong {parent} property {prop} value ({csaf_version})'

    # Publisher (publisher) is object requires ('category', 'name', 'namespace')
    parent = 'document.publisher'
    for prop in ('category', 'name', 'namespace'):
        if not jmespath.search(f'{parent}.{prop}', csaf_doc):
            return 1, f'missing {parent} property ({prop})'

    parent = 'document'
    prop = 'title'
    if not jmespath.search(f'{parent}.{prop}', csaf_doc).strip():
        print(f'warning - {parent} property {prop} value is space-only')

    # Tracking (tracking) is object requires:
    # ('current_release_date', 'id', 'initial_release_date', 'revision_history', 'status', 'version')
    parent = 'document.tracking'
    for prop in ('current_release_date', 'id', 'initial_release_date', 'revision_history', 'status', 'version'):
        if not jmespath.search(f'{parent}.{prop}', csaf_doc):
            return 1, f'missing {parent} property ({prop})'

    return document_optional(csaf_doc['document'])


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
        return 1, 'config has no .json extension', ['']

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

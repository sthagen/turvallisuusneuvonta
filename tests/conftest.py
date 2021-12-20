# -*- coding: utf-8 -*-
# pylint: disable=line-too-long,missing-docstring,reimported,unused-import,unused-variable
import pathlib
from typing import no_type_check

import orjson

CVSS31_VECTOR_STRING_LOG4J = 'CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H'
CVSS31_BASE_SCORE_LOG4J = '10.0'

CVSS30_VECTOR_STRING_LOG4J = 'CVSS:3.0/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H'
CVSS30_BASE_SCORE_LOG4J = '10.0'

CVSS2_VECTOR_STRING_LOG4J = 'AV:N/AC:M/Au:N/C:C/I:C/A:C'
CVSS2_BASE_SCORE_LOG4J = '10.0'

CWE_ID_352 = 'CWE-352'
CWE_NAME_352 = 'Cross-Site Request Forgery (CSRF)'

PRODUCT_RELATIONSHIP_DATA = {
    'category': 'installed_with',
    'full_product_name': {
        'name': 'wun',
        'product_id': {'value': 'acme-112'},
        'product_identification_helper': None,
    },
    'product_reference': {'value': 'acme-112'},
    'relates_to_product_reference': {'value': 'acme-101'},
}

VULNERABILITY_SCORE_LOG4J = {
    'cvss_v2': None,
    'cvss_v3': {
        'version': '3.1',
        'vector_string': 'CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H',
        'attack_vector': None,
        'attack_complexity': None,
        'privileges_required': None,
        'user_interaction': None,
        'scope': None,
        'confidentiality_impact': None,
        'integrity_impact': None,
        'availability_impact': None,
        'base_score': 10.0,
        'base_severity': 'CRITICAL',
        'exploit_code_maturity': None,
        'remediation_level': None,
        'report_confidence': None,
        'temporal_score': None,
        'temporal_severity': None,
        'confidentiality_requirement': None,
        'integrity_requirement': None,
        'availability_requirement': None,
        'modified_attack_vector': None,
        'modified_attack_complexity': None,
        'modified_privileges_required': None,
        'modified_user_interaction': None,
        'modified_scope': None,
        'modified_confidentiality_impact': None,
        'modified_integrity_impact': None,
        'modified_availability_impact': None,
        'environmental_score': None,
        'environmental_severity': None,
    },
    'products': {'product_ids': [{'value': 'log4j-123'}]},
}


META_WRONG_VERSION = {
    'category': '42',
    'csaf_version': '42',
}

META_EMPTY_PUBLISHER = {
    'category': '42',
    'csaf_version': '2.0',
    'publisher': {},
}

META_EMPTY_TITLE = {
    'category': '42',
    'csaf_version': '2.0',
    'publisher': {
        'category': 'vendor',
        'name': 'ACME',
        'namespace': 'https://example.com',
    },
    'title': '',
}

META_EMPTY_TRACKING = {
    'category': '42',
    'csaf_version': '2.0',
    'publisher': {
        'category': 'vendor',
        'name': 'ACME',
        'namespace': 'https://example.com',
    },
    'title': 'a',
    'tracking': {},
}

META_OK = {
    'category': '42',
    'csaf_version': '2.0',
    'publisher': {
        'category': 'vendor',
        'name': 'ACME',
        'namespace': 'https://example.com',
    },
    'title': 'a',
    'tracking': {
        'current_release_date': '0001-01-01 00:00:00',
        'id': '0',
        'initial_release_date': '0001-01-01 00:00:00',
        'revision_history': [
            {
                'date': '0001-01-01 00:00:00',
                'number': '1',
                'summary': 'a',
            }
        ],
        'status': 'final',
        'version': '1',
    },
}

DOC_OK = {
    'document': META_OK,
}

DOC_VULN_EMPTY = {
    'document': META_OK,
    'vulnerabilities': [],
}

SPAM = {
    'document': {
        'category': ' ',
        'csaf_version': '2.0',
        'publisher': ' ',
        'title': ' ',
        'tracking': ' ',
    }
}

SPAM_JSON = orjson.dumps(SPAM)

CSAF_EXAMPLE_COM_123_PATH = pathlib.Path('tests', 'fixtures', 'example-com', 'example-com-123.json')
with open(CSAF_EXAMPLE_COM_123_PATH, 'rb') as handle:
    CSAF_WITH_DOCUMENTS = orjson.loads(handle.read())


@no_type_check
def _strip_and_iso_grace(a_map) -> None:
    """Keep only mandatory shape."""
    for key, value in tuple(a_map.items()):
        if isinstance(value, dict):
            _strip_and_iso_grace(value)
        elif value is None:
            del a_map[key]
        elif isinstance(value, str) and value == '0001-01-01T00:00:00':
            a_map[key] = '0001-01-01 00:00:00'
        elif isinstance(value, list):
            for v_i in value:
                _strip_and_iso_grace(v_i)

"""Security advisory (Finnish: turvallisuusneuvonta) audit tool."""
# [[[fill git_describe()]]]
__version__ = '2022.8.9+parent.3233165e'
# [[[end]]] (checksum: ec2cc12146ac51673531f0f6ebebef47)
__version_info__ = tuple(
    e if '-' not in e else e.split('-')[0] for part in __version__.split('+') for e in part.split('.') if e != 'parent'
)

from turvallisuusneuvonta.csaf.core.rules.mandatory.mandatory import (
    is_valid,
    is_valid_category,
    is_valid_defined_group_ids,
    is_valid_defined_product_ids,
    is_valid_translator,
    is_valid_unique_group_ids,
    is_valid_unique_product_ids,
)

__all__ = [
    'is_valid',
    'is_valid_category',
    'is_valid_defined_group_ids',
    'is_valid_defined_product_ids',
    'is_valid_translator',
    'is_valid_unique_group_ids',
    'is_valid_unique_product_ids',
]

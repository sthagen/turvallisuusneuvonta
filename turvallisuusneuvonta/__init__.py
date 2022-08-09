"""Security advisory (Finnish: turvallisuusneuvonta) audit tool."""
# [[[fill git_describe()]]]
__version__ = '2022.8.2+parent.4c17cf8f'
# [[[end]]] (checksum: eaa209e5e7a90c217df25f8d1c12f751)
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

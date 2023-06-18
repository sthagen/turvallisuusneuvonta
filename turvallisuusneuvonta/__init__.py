"""Security advisory (Finnish: turvallisuusneuvonta) audit tool."""
# [[[fill git_describe()]]]
__version__ = '2023.6.18+parent.dd252054'
# [[[end]]] (checksum: ed24f138a6c1f4ed1846f228247c7db7)
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

"""Security advisory (Finnish: turvallisuusneuvonta) audit tool."""

# [[[fill git_describe()]]]
__version__ = '2024.12.18+parent.g6d360224'
# [[[end]]] (checksum: f7d4c146c67f04723ac762bc02afa41e)
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

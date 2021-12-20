"""CSAF Product Tree model."""
from __future__ import annotations

from collections.abc import Sequence
from enum import Enum
from typing import Annotated, Optional, no_type_check

from pydantic import BaseModel, Field, validator

from turvallisuusneuvonta.csaf.definitions import (
    FullProductName,
    ListOfBranches,
    ListOfProductIds,
    ReferenceTokenForProductGroupInstance,
    ReferenceTokenForProductInstance,
)


class ProductGroup(BaseModel):
    """
    Defines a new logical group of products that can then be referred to in other parts of the document to address
    a group of products with a single identifier.
    """

    group_id: ReferenceTokenForProductGroupInstance
    product_ids: Annotated[
        Sequence[ReferenceTokenForProductInstance],
        Field(
            description='Lists the product_ids of those products which known as one group in the document.',
            # min_items=2,
            title='List of Product IDs',
        ),
    ]
    summary: Annotated[
        Optional[str],
        Field(
            description='Gives a short, optional description of the group.',
            examples=[
                'Products supporting Modbus.',
                'The x64 versions of the operating system.',
            ],
            min_length=1,
            title='Summary of the product group',
        ),
    ] = None

    @no_type_check
    @validator('product_ids')
    def check_len(cls, v):
        if len(v) < 2:
            raise ValueError('mandatory element present but too few items')
        return v


class ProductStatus(BaseModel):
    """
    Contains different lists of product_ids which provide details on the status of the referenced product related
    to the current vulnerability.
    """

    first_affected: Annotated[
        Optional[ListOfProductIds],
        Field(
            description='These are the first versions of the releases known to be affected by the vulnerability.',
            title='First affected',
        ),
    ] = None
    first_fixed: Annotated[
        Optional[ListOfProductIds],
        Field(
            description=(
                'These versions contain the first fix for the vulnerability but may not be'
                ' the recommended fixed versions.'
            ),
            title='First fixed',
        ),
    ] = None
    fixed: Annotated[
        Optional[ListOfProductIds],
        Field(
            description=(
                'These versions contain a fix for the vulnerability but may not be the recommended fixed versions.'
            ),
            title='Fixed',
        ),
    ] = None
    known_affected: Annotated[
        Optional[ListOfProductIds],
        Field(
            description='These versions are known to be affected by the vulnerability.',
            title='Known affected',
        ),
    ] = None
    known_not_affected: Annotated[
        Optional[ListOfProductIds],
        Field(
            description='These versions are known not to be affected by the vulnerability.',
            title='Known not affected',
        ),
    ] = None
    last_affected: Annotated[
        Optional[ListOfProductIds],
        Field(
            description=(
                'These are the last versions in a release train known to be affected by the vulnerability.'
                ' Subsequently released versions would contain a fix for the vulnerability.'
            ),
            title='Last affected',
        ),
    ] = None
    recommended: Annotated[
        Optional[ListOfProductIds],
        Field(
            description=(
                'These versions have a fix for the vulnerability and are the vendor-recommended versions'
                ' for fixing the vulnerability.'
            ),
            title='Recommended',
        ),
    ] = None
    under_investigation: Annotated[
        Optional[ListOfProductIds],
        Field(
            description=(
                'It is not known yet whether these versions are or are not affected by the vulnerability.'
                ' However, it is still under investigation'
                ' - the result will be provided in a later release of the document.'
            ),
            title='Under investigation',
        ),
    ] = None


class RelationshipCategory(Enum):
    """
    Defines the category of relationship for the referenced component.
    """

    default_component_of = 'default_component_of'
    external_component_of = 'external_component_of'
    installed_on = 'installed_on'
    installed_with = 'installed_with'
    optional_component_of = 'optional_component_of'


class Relationship(BaseModel):
    """
    Establishes a link between two existing full_product_name_t elements, allowing the document producer to define
    a combination of two products that form a new full_product_name entry.
    """

    category: Annotated[
        RelationshipCategory,
        Field(
            description='Defines the category of relationship for the referenced component.',
            title='Relationship category',
        ),
    ]
    full_product_name: FullProductName
    product_reference: Annotated[
        ReferenceTokenForProductInstance,
        Field(
            description=(
                'Holds a Product ID that refers to the Full Product Name element,'
                ' which is referenced as the first element of the relationship.'
            ),
            title='Product reference',
        ),
    ]
    relates_to_product_reference: Annotated[
        ReferenceTokenForProductInstance,
        Field(
            description=(
                'Holds a Product ID that refers to the Full Product Name element,'
                ' which is referenced as the second element of the relationship.'
            ),
            title='Relates to product reference',
        ),
    ]


class ProductTree(BaseModel):
    """
    Is a container for all fully qualified product names that can be referenced elsewhere in the document.
    """

    branches: Optional[ListOfBranches] = None
    full_product_names: Annotated[
        Optional[Sequence[FullProductName]],
        Field(
            description='Contains a list of full product names.',
            # min_items=1,
            title='List of full product names',
        ),
    ] = None
    product_groups: Annotated[
        Optional[Sequence[ProductGroup]],
        Field(
            description='Contains a list of product groups.',
            # min_items=1,
            title='List of product groups',
        ),
    ] = None
    relationships: Annotated[
        Optional[Sequence[Relationship]],
        Field(
            description='Contains a list of relationships.',
            # min_items=1,
            title='List of relationships',
        ),
    ] = None

    @no_type_check
    @validator('full_product_names', 'product_groups', 'relationships')
    def check_len(cls, v):
        if not v:
            raise ValueError('optional element present but empty')
        return v


FullProductName.update_forward_refs()
ProductTree.update_forward_refs()

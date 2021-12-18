"""CSAF Document model."""
from __future__ import annotations

from collections.abc import Sequence
from typing import Annotated, Optional, no_type_check

from pydantic import BaseModel, Field, validator

from turvallisuusneuvonta.csaf.document import DocumentLevelMetaData
from turvallisuusneuvonta.csaf.product import ProductTree
from turvallisuusneuvonta.csaf.vulnerability import Vulnerability


class CommonSecurityAdvisoryFramework(BaseModel):
    """Representation of security advisory information as a JSON document."""

    document: Annotated[
        DocumentLevelMetaData,
        Field(
            description=(
                'Captures the meta-data about this document describing a particular set of security advisories.'
            ),
            title='Document level meta-data',
        ),
    ]
    product_tree: Annotated[
        Optional[ProductTree],
        Field(
            description=(
                'Is a container for all fully qualified product names that can be referenced elsewhere in the document.'
            ),
            title='Product tree',
        ),
    ] = None
    vulnerabilities: Annotated[
        Optional[Sequence[Vulnerability]],
        Field(
            description='Represents a list of all relevant vulnerability information items.',
            # min_items=1,
            title='Vulnerabilities',
        ),
    ] = None

    @no_type_check
    @validator('vulnerabilities')
    def check_len(cls, v):
        if not v:
            raise ValueError('vulnerabilities present but empty')
        return v

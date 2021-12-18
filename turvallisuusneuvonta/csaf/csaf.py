"""CSAF Document model."""
from __future__ import annotations

from collections.abc import Sequence
from typing import Annotated, Optional, no_type_check

from csaf.document import DocumentLevelMetaData  # type: ignore
from csaf.product import ProductTree  # type: ignore
from csaf.vulnerability import Vulnerability  # type: ignore
from pydantic import BaseModel, Field, validator


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

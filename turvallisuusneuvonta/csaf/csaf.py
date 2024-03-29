"""CSAF Document model."""

from __future__ import annotations

from typing import Annotated, List, Optional, no_type_check

from pydantic import BaseModel, Field, field_validator

from turvallisuusneuvonta.csaf.document import Document
from turvallisuusneuvonta.csaf.product import ProductTree
from turvallisuusneuvonta.csaf.vulnerability import Vulnerability


class CSAF(BaseModel):
    """
    Representation of security advisory information as a JSON document.
    """

    document: Annotated[
        Document,
        Field(
            description='Captures the meta-data about this document describing a particular set of'
            ' security advisories.',
            title='Document level meta-data',
        ),
    ]
    product_tree: Annotated[
        Optional[ProductTree],
        Field(
            description='Is a container for all fully qualified product names that can be referenced elsewhere'
            ' in the document.',
            title='Product tree',
        ),
    ] = None
    vulnerabilities: Annotated[
        Optional[List[Vulnerability]],
        Field(
            description='Represents a list of all relevant vulnerability information items.',
            min_length=1,
            title='Vulnerabilities',
        ),
    ] = None

    @no_type_check
    def model_dump_json(self, *args, **kwargs):
        kwargs.setdefault('by_alias', True)
        return super().model_dump_json(*args, **kwargs)

    @classmethod
    @no_type_check
    @field_validator('vulnerabilities')
    def check_len(cls, v):
        if not v:
            raise ValueError('vulnerabilities present but empty')
        return v

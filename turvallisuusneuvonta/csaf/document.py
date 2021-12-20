from __future__ import annotations

"""CSAF Document meta information model."""
from collections.abc import Sequence
from datetime import datetime
from enum import Enum
from typing import Annotated, Optional, no_type_check

from pydantic import AnyUrl, BaseModel, Field, validator

from turvallisuusneuvonta.csaf.definitions import (
    LanguageType,
    ListOfAcknowledgments,
    ListOfNotes,
    ListOfReferences,
    Version,
)


class Revision(BaseModel):
    """
    Contains all the information elements required to track the evolution of a CSAF document.
    """

    date: Annotated[
        datetime,
        Field(description='The date of the revision entry', title='Date of the revision'),
    ]
    number: Version
    summary: Annotated[
        str,
        Field(
            description='Holds a single non-empty string representing a short description of the changes.',
            examples=['Initial version.'],
            min_length=1,
            title='Summary of the revision',
        ),
    ]


class Tracking(BaseModel):
    """
    Is a container designated to hold all management attributes necessary to track a CSAF document as a whole.
    """

    aliases: Annotated[
        Optional[Sequence[AlternateName]],
        Field(
            description='Contains a list of alternate names for the same document.',
            min_items=1,
            title='Aliases',
        ),
    ] = None
    current_release_date: Annotated[
        datetime,
        Field(
            description='The date when the current revision of this document was released',
            title='Current release date',
        ),
    ]
    generator: Annotated[
        Optional[DocumentGenerator],
        Field(
            description=(
                'Is a container to hold all elements related to the generation of the document.'
                ' These items will reference when the document was actually created,'
                ' including the date it was generated and the entity that generated it.'
            ),
            title='Document generator',
        ),
    ] = None
    id: Annotated[
        str,
        Field(
            description=(
                'The ID is a simple label that provides for a wide range of numbering values, types, and schemes.'
                ' Its value SHOULD be assigned and maintained by the original document issuing authority.'
            ),
            examples=[
                'Example Company - 2019-YH3234',
                'RHBA-2019:0024',
                'cisco-sa-20190513-secureboot',
            ],
            min_length=1,
            title='Unique identifier for the document',
        ),
    ]
    initial_release_date: Annotated[
        datetime,
        Field(
            description='The date when this document was first published.',
            title='Initial release date',
        ),
    ]
    revision_history: Annotated[
        Sequence[Revision],
        Field(
            description='Holds one revision item for each version of the CSAF document, including the initial one.',
            # min_items=1,
            title='Revision history',
        ),
    ]
    status: Annotated[
        DocumentStatus,
        Field(
            description='Defines the draft status of the document.',
            title='Document status',
        ),
    ]
    version: Version

    @no_type_check
    @validator('revision_history')
    def check_len(cls, v):
        if not v:
            raise ValueError('mandatory element present but empty')
        return v


class AggregateSeverity(BaseModel):
    """
    Is a vehicle that is provided by the document producer to convey the urgency and criticality with which the one or
    more vulnerabilities reported should be addressed.
    It is a document-level metric and applied to the document as a whole — not any specific vulnerability.
    The range of values in this field is defined according to the document producer's policies and procedures.
    """

    namespace: Annotated[
        Optional[AnyUrl],
        Field(
            description='Points to the namespace so referenced.',
            title='Namespace of aggregate severity',
        ),
    ] = None
    text: Annotated[
        str,
        Field(
            description=(
                'Provides a severity which is independent of - and in addition to - any other standard metric for'
                ' determining the impact or severity of a given vulnerability (such as CVSS).'
            ),
            examples=['Critical', 'Important', 'Moderate'],
            min_length=1,
            title='Text of aggregate severity',
        ),
    ]


class CsafVersion(Enum):
    """
    Gives the version of the CSAF specification which the document was generated for.
    """

    field_2_0 = '2.0'


class LabelOfTlp(Enum):
    """
    Provides the TLP label of the document.
    """

    amber = 'AMBER'
    green = 'GREEN'
    red = 'RED'
    white = 'WHITE'


class TrafficLightProtocolTlp(BaseModel):
    """
    Provides details about the TLP classification of the document.
    """

    label: Annotated[
        LabelOfTlp,
        Field(description='Provides the TLP label of the document.', title='Label of TLP'),
    ]
    url: Annotated[
        Optional[AnyUrl],
        Field(
            description=(
                'Provides a URL where to find the textual description of the TLP version which is used in this'
                ' document. Default is the URL to the definition by FIRST.'
            ),
            examples=[
                'https://www.us-cert.gov/tlp',
                'https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Kritis/Merkblatt_TLP.pdf',
            ],
            title='URL of TLP version',
        ),
    ] = 'https://www.first.org/tlp/'  # type: ignore


class RulesForSharingDocument(BaseModel):
    """
    Describe any constraints on how this document might be shared.
    """

    text: Annotated[
        Optional[str],
        Field(
            description='Provides a textual description of additional constraints.',
            examples=[
                'Copyright 2021, Example Company, All Rights Reserved.',
                'Distribute freely.',
                'Share only on a need-to-know-basis only.',
            ],
            min_length=1,
            title='Textual description',
        ),
    ] = None
    tlp: Annotated[
        Optional[TrafficLightProtocolTlp],
        Field(
            description='Provides details about the TLP classification of the document.',
            title='Traffic Light Protocol (TLP)',
        ),
    ] = None


class CategoryOfPublisher(Enum):
    """
    Provides information about the category of publisher releasing the document.
    """

    coordinator = 'coordinator'
    discoverer = 'discoverer'
    other = 'other'
    translator = 'translator'
    user = 'user'
    vendor = 'vendor'


class Publisher(BaseModel):
    """
    Provides information about the publisher of the document.
    """

    category: Annotated[
        CategoryOfPublisher,
        Field(
            description='Provides information about the category of publisher releasing the document.',
            title='Category of publisher',
        ),
    ]
    contact_details: Annotated[
        Optional[str],
        Field(
            description=(
                'Information on how to contact the publisher, possibly including details such as web sites,'
                ' email addresses, phone numbers, and postal mail addresses.'
            ),
            examples=[
                (
                    'Example Company can be reached at contact_us@example.com,'
                    ' or via our website at https://www.example.com/contact.'
                )
            ],
            min_length=1,
            title='Contact details',
        ),
    ] = None
    issuing_authority: Annotated[
        Optional[str],
        Field(
            description=(
                'Provides information about the authority of the issuing party to release the document,'
                " in particular, the party's constituency and responsibilities or other obligations."
            ),
            min_length=1,
            title='Issuing authority',
        ),
    ] = None
    name: Annotated[
        str,
        Field(
            description='Contains the name of the issuing party.',
            examples=['BSI', 'Cisco PSIRT', 'Siemens ProductCERT'],
            min_length=1,
            title='Name of publisher',
        ),
    ]
    namespace: Annotated[
        AnyUrl,
        Field(
            description=(
                'Contains a URL which is under control of the issuing party and can be used as a'
                ' globally unique identifier for that issuing party.'
            ),
            examples=['https://csaf.io', 'https://www.example.com'],
            title='Namespace of publisher',
        ),
    ]


class AlternateName(BaseModel):
    __root__: Annotated[
        str,
        Field(
            description=(
                'Specifies a non-empty string that represents a distinct optional alternative ID'
                ' used to refer to the document.'
            ),
            examples=['CVE-2019-12345'],
            min_length=1,
            title='Alternate name',
        ),
    ]


class EngineOfDocumentGeneration(BaseModel):
    """
    Contains information about the engine that generated the CSAF document.
    """

    name: Annotated[
        str,
        Field(
            description='Represents the name of the engine that generated the CSAF document.',
            examples=['Red Hat rhsa-to-cvrf', 'Secvisogram', 'TVCE'],
            min_length=1,
            title='Engine name',
        ),
    ]
    version: Annotated[
        Optional[str],
        Field(
            description='Contains the version of the engine that generated the CSAF document.',
            examples=['0.6.0', '1.0.0-beta+exp.sha.a1c44f85', '2'],
            min_length=1,
            title='Engine version',
        ),
    ] = None


class DocumentGenerator(BaseModel):
    """
    Is a container to hold all elements related to the generation of the document.
    These items will reference when the document was actually created,
    including the date it was generated and the entity that generated it.
    """

    date: Annotated[
        Optional[datetime],
        Field(
            description=(
                'This SHOULD be the current date that the document was generated.'
                ' Because documents are often generated internally by a document producer and exist for'
                ' a nonzero amount of time before being released,'
                ' this field MAY be different from the Initial Release Date and Current Release Date.'
            ),
            title='Date of document generation',
        ),
    ] = None
    engine: Annotated[
        EngineOfDocumentGeneration,
        Field(
            description='Contains information about the engine that generated the CSAF document.',
            title='Engine of document generation',
        ),
    ]


class DocumentStatus(Enum):
    """
    Defines the draft status of the document.
    """

    draft = 'draft'
    final = 'final'
    interim = 'interim'


class DocumentLevelMetaData(BaseModel):
    """
    Captures the meta-data about this document describing a particular set of security advisories.
    """

    acknowledgments: Annotated[
        Optional[ListOfAcknowledgments],
        Field(
            description='Contains a list of acknowledgment elements associated with the whole document.',
            title='Document acknowledgments',
        ),
    ] = None
    aggregate_severity: Annotated[
        Optional[AggregateSeverity],
        Field(
            description=(
                'Is a vehicle that is provided by the document producer to convey the urgency and criticality with'
                ' which the one or more vulnerabilities reported should be addressed.'
                ' It is a document-level metric and applied to the document as a whole'
                ' — not any specific vulnerability.'
                ' The range of values in this field is defined according to'
                " the document producer's policies and procedures."
            ),
            title='Aggregate severity',
        ),
    ] = None
    category: Annotated[
        str,
        Field(
            description=(
                'Defines a short canonical name, chosen by the document producer,'
                ' which will inform the end user as to the category of document.'
            ),
            examples=[
                'Example Company Security Notice',
                'generic_csaf',
                'security_advisory',
                'vex',
            ],
            min_length=1,
            title='Document category',
        ),
    ]
    csaf_version: Annotated[
        CsafVersion,
        Field(
            description='Gives the version of the CSAF specification which the document was generated for.',
            title='CSAF version',
        ),
    ]
    distribution: Annotated[
        Optional[RulesForSharingDocument],
        Field(
            description='Describe any constraints on how this document might be shared.',
            title='Rules for sharing document',
        ),
    ] = None
    lang: Annotated[
        Optional[LanguageType],
        Field(
            description='Identifies the language used by this document, corresponding to IETF BCP 47 / RFC 5646.',
            title='Document language',
        ),
    ] = None
    notes: Annotated[
        Optional[ListOfNotes],
        Field(
            description='Holds notes associated with the whole document.',
            title='Document notes',
        ),
    ] = None
    publisher: Annotated[
        Publisher,
        Field(
            description='Provides information about the publisher of the document.',
            title='Publisher',
        ),
    ]
    references: Annotated[
        Optional[ListOfReferences],
        Field(
            description='Holds a list of references associated with the whole document.',
            title='Document references',
        ),
    ] = None
    source_lang: Annotated[
        Optional[LanguageType],
        Field(
            description=(
                'If this copy of the document is a translation then the value of this property describes from'
                ' which language this document was translated.'
            ),
            title='Source language',
        ),
    ] = None
    title: Annotated[
        str,
        Field(
            description=(
                'This SHOULD be a canonical name for the document,'
                ' and sufficiently unique to distinguish it from similar documents.'
            ),
            examples=[
                'Cisco IPv6 Crafted Packet Denial of Service Vulnerability',
                'Example Company Cross-Site-Scripting Vulnerability in Example Generator',
            ],
            min_length=1,
            title='Title of this document',
        ),
    ]
    tracking: Annotated[
        Tracking,
        Field(
            description=(
                'Is a container designated to hold all management attributes necessary to track'
                ' a CSAF document as a whole.'
            ),
            title='Tracking',
        ),
    ]


Tracking.update_forward_refs()

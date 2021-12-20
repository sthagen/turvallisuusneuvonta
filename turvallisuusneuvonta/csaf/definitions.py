"""CSAF Document general definitions."""
from __future__ import annotations

import re
from collections.abc import Sequence
from enum import Enum
from typing import Annotated, Optional, no_type_check

from pydantic import AnyUrl, BaseModel, Field, validator


class Id(BaseModel):
    """
    Gives the document producer a place to publish a unique label or tracking ID for the vulnerability
    (if such information exists).
    """

    system_name: Annotated[
        str,
        Field(
            description='Indicates the name of the vulnerability tracking or numbering system.',
            examples=['Cisco Bug ID', 'GitHub Issue'],
            min_length=1,
            title='System name',
        ),
    ]
    text: Annotated[
        str,
        Field(
            description='Is unique label or tracking ID for the vulnerability (if such information exists).',
            examples=['CSCso66472', 'oasis-tcs/csaf#210'],
            min_length=1,
            title='Text',
        ),
    ]


class NameOfEntityBeingRecognized(BaseModel):
    __root__: Annotated[
        str,
        Field(
            description='Contains the name of a single person.',
            examples=['Albert Einstein', 'Johann Sebastian Bach'],
            min_length=1,
            title='Name of entity being recognized',
        ),
    ]


class Acknowledgment(BaseModel):
    """
    Acknowledges contributions by describing those that contributed.
    """

    names: Annotated[
        Optional[Sequence[NameOfEntityBeingRecognized]],
        Field(
            description='Contains the names of entities being recognized.',
            # min_items=1,
            title='List of acknowledged names',
        ),
    ] = None
    organization: Annotated[
        Optional[str],
        Field(
            description='Contains the name of a contributing organization being recognized.',
            examples=['CISA', 'Google Project Zero', 'Talos'],
            min_length=1,
            title='Contributing organization',
        ),
    ] = None
    summary: Annotated[
        Optional[str],
        Field(
            description=(
                'SHOULD represent any contextual details the document producers wish to make known about'
                ' the acknowledgment or acknowledged parties.'
            ),
            examples=['First analysis of Coordinated Multi-Stream Attack (CMSA)'],
            min_length=1,
            title='Summary of the acknowledgment',
        ),
    ] = None
    urls: Annotated[
        Optional[Sequence[AnyUrl]],
        Field(
            description='Specifies a list of URLs or location of the reference to be acknowledged.',
            # min_items=1,
            title='List of URLs',
        ),
    ] = None

    @no_type_check
    @validator('names', 'organization', 'summary', 'urls')
    def check_len(cls, v):
        if not v:
            raise ValueError('optional element present but empty')
        return v


class ListOfAcknowledgments(BaseModel):
    """
    Contains a list of acknowledgment elements.
    """

    __root__: Annotated[
        Sequence[Acknowledgment],
        Field(
            description='Contains a list of acknowledgment elements.',
            # min_items=1,
            title='List of acknowledgments',
        ),
    ]

    @no_type_check
    @validator('__root__')
    def check_len(cls, v):
        if not v:
            raise ValueError('optional element present but empty')
        return v


class FileHash(BaseModel):
    """
    Contains one hash value and algorithm of the file to be identified.
    """

    algorithm: Annotated[
        str,
        Field(
            description='Contains the name of the cryptographic hash algorithm used to calculate the value.',
            examples=['blake2b512', 'sha256', 'sha3-512', 'sha384', 'sha512'],
            min_length=1,
            title='Algorithm of the cryptographic hash',
        ),
    ]
    value: Annotated[
        str,
        Field(
            description='Contains the cryptographic hash value in hexadecimal representation.',
            examples=[
                (
                    '37df33cb7464da5c7f077f4d56a32bc84987ec1d85b234537c1c1a4d4fc8d09d'
                    'c29e2e762cb5203677bf849a2855a0283710f1f5fe1d6ce8d5ac85c645d0fcb3'
                ),
                '4775203615d9534a8bfca96a93dc8b461a489f69124a130d786b42204f3341cc',
                '9ea4c8200113d49d26505da0e02e2f49055dc078d1ad7a419b32e291c7afebbb84badfbd46dec42883bea0b2a1fa697c',
            ],
            min_length=32,
            regex='^[0-9a-fA-F]{32,}$',
            title='Value of the cryptographic hash',
        ),
    ]


class CryptographicHashes(BaseModel):
    """
    Contains all information to identify a file based on its cryptographic hash values.
    """

    file_hashes: Annotated[
        Sequence[FileHash],
        Field(
            description='Contains a list of cryptographic hashes for this file.',
            # min_items=1,
            title='List of file hashes',
        ),
    ]
    filename: Annotated[
        str,
        Field(
            description='Contains the name of the file which is identified by the hash values.',
            examples=['WINWORD.EXE', 'msotadddin.dll', 'sudoers.so'],
            # min_length=1,
            title='Filename',
        ),
    ]

    @no_type_check
    @validator('file_hashes', 'filename')
    def check_len(cls, v):
        if not v:
            raise ValueError('mandatory element present but empty')
        return v


class SerialNumber(BaseModel):
    __root__: Annotated[
        str,
        Field(
            description='Contains a part, or a full serial number of the component to identify.',
            min_length=1,
            title='Serial number',
        ),
    ]


class StockKeepingUnit(BaseModel):
    __root__: Annotated[
        str,
        Field(
            description=(
                'Contains a part, or a full stock keeping unit (SKU) which is used in the ordering process'
                ' to identify the component.'
            ),
            min_length=1,
            title='Stock keeping unit',
        ),
    ]


class GenericUri(BaseModel):
    """
    Provides a generic extension point for any identifier which is either vendor-specific or
    derived from a standard not yet supported.
    """

    namespace: Annotated[
        AnyUrl,
        Field(
            description=(
                'Refers to a URL which provides the name and knowledge about the specification used or'
                ' is the namespace in which these values are valid.'
            ),
            title='Namespace of the generic URI',
        ),
    ]
    uri: Annotated[AnyUrl, Field(description='Contains the identifier itself.', title='URI')]


class HelperToIdentifyTheProduct(BaseModel):
    """
    Provides at least one method which aids in identifying the product in an asset database.
    """

    cpe: Annotated[
        Optional[str],
        Field(
            description=(
                'The Common Platform Enumeration (CPE) attribute refers to a method for naming platforms external'
                ' to this specification.'
            ),
            min_length=5,
            regex=(
                '^(cpe:2\\.3:[aho\\*\\-](:(((\\?*|\\*?)([a-zA-Z0-9\\-\\._]|'
                '(\\\\[\\\\\\*\\?!"#\\$%&\'\\(\\)\\+,/:;<=>@\\[\\]\\^`\\{\\|\\}~]))+(\\?*|\\*?))|[\\*\\-])){5}'
                '(:(([a-zA-Z]{2,3}(-([a-zA-Z]{2}|[0-9]{3}))?)|[\\*\\-]))(:(((\\?*|\\*?)([a-zA-Z0-9\\-\\._]|'
                '(\\\\[\\\\\\*\\?!"#\\$%&\'\\(\\)\\+,/:;<=>@\\[\\]\\^`\\{\\|\\}~]))+(\\?*|\\*?))|[\\*\\-])){4})|'
                '([c][pP][eE]:/[AHOaho]?(:[A-Za-z0-9\\._\\-~%]*){0,6})$'
            ),
            title='Common Platform Enumeration representation',
        ),
    ] = None
    hashes: Annotated[
        Optional[Sequence[CryptographicHashes]],
        Field(
            description='Contains a list of cryptographic hashes usable to identify files.',
            # min_items=1,
            title='List of hashes',
        ),
    ] = None
    purl: Annotated[
        Optional[AnyUrl],
        Field(
            description=(
                'The package URL (purl) attribute refers to a method for reliably identifying and'
                ' locating software packages external to this specification.'
            ),
            # min_length=7,
            # regex='^pkg:[A-Za-z\\.\\-\\+][A-Za-z0-9\\.\\-\\+]*/.+',
            title='package URL representation',
        ),
    ] = None
    sbom_urls: Annotated[
        Optional[Sequence[AnyUrl]],
        Field(
            description='Contains a list of URLs where SBOMs for this product can be retrieved.',
            # min_items=1,
            title='List of SBOM URLs',
        ),
    ] = None
    serial_numbers: Annotated[
        Optional[Sequence[SerialNumber]],
        Field(
            description='Contains a list of parts, or full serial numbers.',
            # min_items=1,
            title='List of serial numbers',
        ),
    ] = None
    skus: Annotated[
        Optional[Sequence[StockKeepingUnit]],
        Field(
            description='Contains a list of parts, or full stock keeping units.',
            # min_items=1,
            title='List of stock keeping units',
        ),
    ] = None
    x_generic_uris: Annotated[
        Optional[Sequence[GenericUri]],
        Field(
            description=(
                'Contains a list of identifiers which are either vendor-specific or derived from'
                ' a standard not yet supported.'
            ),
            # min_items=1,
            title='List of generic URIs',
        ),
    ] = None

    @no_type_check
    @validator('hashes', 'sbom_urls', 'serial_numbers', 'skus', 'x_generic_uris')
    def check_len(cls, v):
        if not v:
            raise ValueError('optional element present but empty')
        return v

    @no_type_check
    @validator('purl')
    def check_purl(cls, v):
        if not v or len(v) < 7:
            raise ValueError('optional purl element present but too short')
        if not re.match('^pkg:[A-Za-z\\.\\-\\+][A-Za-z0-9\\.\\-\\+]*/.+', v):
            raise ValueError('optional purl element present but is no purl (regex does not match)')
        return v


class FullProductName(BaseModel):
    """
    Specifies information about the product and assigns the product_id.
    """

    name: Annotated[
        str,
        Field(
            description=(
                "The value should be the product's full canonical name, including version number and other attributes,"
                ' as it would be used in a human-friendly document.'
            ),
            examples=[
                'Cisco AnyConnect Secure Mobility Client 2.3.185',
                'Microsoft Host Integration Server 2006 Service Pack 1',
            ],
            min_length=1,
            title='Textual description of the product',
        ),
    ]
    product_id: ReferenceTokenForProductInstance
    product_identification_helper: Annotated[
        Optional[HelperToIdentifyTheProduct],
        Field(
            description='Provides at least one method which aids in identifying the product in an asset database.',
            title='Helper to identify the product',
        ),
    ] = None


class LanguageType(BaseModel):
    __root__: Annotated[
        str,
        Field(
            description=(
                'Identifies a language, corresponding to IETF BCP 47 / RFC 5646.'
                ' See IETF language registry:'
                ' https://www.iana.org/assignments/language-subtag-registry/language-subtag-registry'
            ),
            examples=['de', 'en', 'fr', 'frc', 'jp'],
            regex=(
                '^(([A-Za-z]{2,3}(-[A-Za-z]{3}(-[A-Za-z]{3}){0,2})?|[A-Za-z]{4,8})(-[A-Za-z]{4})?'
                '(-([A-Za-z]{2}|[0-9]{3}))?(-([A-Za-z0-9]{5,8}|[0-9][A-Za-z0-9]{3}))*(-[A-WY-Za-wy-z0-9]'
                '(-[A-Za-z0-9]{2,8})+)*(-[Xx](-[A-Za-z0-9]{1,8})+)?|[Xx](-[A-Za-z0-9]{1,8})+|'
                '[Ii]-[Dd][Ee][Ff][Aa][Uu][Ll][Tt]|[Ii]-[Mm][Ii][Nn][Gg][Oo])$'
            ),
            title='Language type',
        ),
    ]


class ReferenceTokenForProductGroupInstance(BaseModel):
    __root__: Annotated[
        str,
        Field(
            description=(
                'Token required to identify a group of products so that it can be referred to from'
                ' other parts in the document.'
                ' There is no predefined or required format for the product_group_id as long as it uniquely identifies'
                ' a group in the context of the current document.'
            ),
            examples=['CSAFGID-0001', 'CSAFGID-0002', 'CSAFGID-0020'],
            min_length=1,
            title='Reference token for product group instance',
        ),
    ]


class ListOfProductGroupIds(BaseModel):
    """
    Specifies a list of product_group_ids to give context to the parent item.
    """

    __root__: Annotated[
        Sequence[ReferenceTokenForProductGroupInstance],
        Field(
            description='Specifies a list of product_group_ids to give context to the parent item.',
            # min_items=1,
            title='List of product_group_ids',
        ),
    ]

    @no_type_check
    @validator('__root__')
    def check_len(cls, v):
        if not v:
            raise ValueError('mandatory element present but empty')
        return v


class ReferenceTokenForProductInstance(BaseModel):
    value: Annotated[
        str,
        Field(
            description=(
                'Token required to identify a full_product_name so that it can be referred to from other'
                ' parts in the document.'
                ' There is no predefined or required format for the product_id as long as it uniquely'
                ' identifies a product in the context of the current document.'
            ),
            examples=['CSAFPID-0004', 'CSAFPID-0008'],
            min_length=1,
            title='Reference token for product instance',
        ),
    ]


class ListOfProductIds(BaseModel):
    """
    Specifies a list of product_ids to give context to the parent item.
    """

    product_ids: Annotated[
        Sequence[ReferenceTokenForProductInstance],
        Field(
            description='Specifies a list of product_ids to give context to the parent item.',
            # min_items=1,
            title='List of product_ids',
        ),
    ]

    @no_type_check
    @validator('product_ids')
    def check_len(cls, v):
        if not v:
            raise ValueError('mandatory element present but empty')
        return v


class NoteCategory(Enum):
    """
    Choice of what kind of note this is.
    """

    description = 'description'
    details = 'details'
    faq = 'faq'
    general = 'general'
    legal_disclaimer = 'legal_disclaimer'
    other = 'other'
    summary = 'summary'


class Note(BaseModel):
    """
    Is a place to put all manner of text blobs related to the current context.
    """

    audience: Annotated[
        Optional[str],
        Field(
            description='Indicate who is intended to read it.',
            examples=[
                'all',
                'executives',
                'operational management and system administrators',
                'safety engineers',
            ],
            min_length=1,
            title='Audience of note',
        ),
    ] = None
    category: Annotated[
        NoteCategory,
        Field(description='Choice of what kind of note this is.', title='Note category'),
    ]
    text: Annotated[
        str,
        Field(
            description='The contents of the note. Content varies depending on type.',
            min_length=1,
            title='Note contents',
        ),
    ]
    title: Annotated[
        Optional[str],
        Field(
            description='Provides a concise description of what is contained in the text of the note.',
            examples=[
                'Details',
                'Executive summary',
                'Technical summary',
                'Impact on safety systems',
            ],
            min_length=1,
            title='Title of note',
        ),
    ] = None


class ListOfNotes(BaseModel):
    """
    Contains notes which are specific to the current context.
    """

    __root__: Annotated[
        Sequence[Note],
        Field(
            description='Contains notes which are specific to the current context.',
            # min_items=1,
            title='List of notes',
        ),
    ]

    @no_type_check
    @validator('__root__')
    def check_len(cls, v):
        if not v:
            raise ValueError('mandatory element present but empty')
        return v


class ListOfReferences(BaseModel):
    """
    Holds a list of references.
    """

    __root__: Annotated[
        Sequence[Reference],
        Field(
            description='Holds a list of references.',
            min_items=1,
            title='List of references',
        ),
    ]


class CategoryOfReference(Enum):
    """
    Indicates whether the reference points to the same document or vulnerability in focus (depending on scope)
    or to an external resource.
    """

    external = 'external'
    self = 'self'


class Reference(BaseModel):
    """
    Holds any reference to conferences, papers, advisories, and other resources that are related and considered
    related to either a surrounding part of or the entire document and to be of value to the document consumer.
    """

    category: Annotated[
        Optional[CategoryOfReference],
        Field(
            description=(
                'Indicates whether the reference points to the same document or vulnerability in focus'
                ' (depending on scope) or to an external resource.'
            ),
            title='Category of reference',
        ),
    ] = 'external'  # type: ignore
    summary: Annotated[
        str,
        Field(
            description='Indicates what this reference refers to.',
            min_length=1,
            title='Summary of the reference',
        ),
    ]
    url: Annotated[
        AnyUrl,
        Field(description='Provides the URL for the reference.', title='URL of reference'),
    ]


class Version(BaseModel):
    __root__: Annotated[
        str,
        Field(
            description=(
                'Specifies a version string to denote clearly the evolution of the content of the document.'
                ' Format must be either integer or semantic versioning.'
            ),
            examples=['1', '4', '0.9.0', '1.4.3', '2.40.0+21AF26D3'],
            regex=(
                '^(0|[1-9][0-9]*)$|^((0|[1-9]\\d*)\\.(0|[1-9]\\d*)\\.(0|[1-9]\\d*)'
                '(?:-((?:0|[1-9]\\d*|\\d*[a-zA-Z-][0-9a-zA-Z-]*)(?:\\.(?:0|[1-9]\\d*|\\d*[a-zA-Z-][0-9a-zA-Z-]*))*))?'
                '(?:\\+([0-9a-zA-Z-]+(?:\\.[0-9a-zA-Z-]+)*))?)$'
            ),
            title='Version',
        ),
    ]


class CategoryOfTheBranch(Enum):
    """
    Describes the characteristics of the labeled branch.
    """

    architecture = 'architecture'
    host_name = 'host_name'
    language = 'language'
    legacy = 'legacy'
    patch_level = 'patch_level'
    product_family = 'product_family'
    product_name = 'product_name'
    product_version = 'product_version'
    service_pack = 'service_pack'
    specification = 'specification'
    vendor = 'vendor'


class Branch(BaseModel):
    """
    Is a part of the hierarchical structure of the product tree.
    """

    branches: Optional[ListOfBranches] = None
    category: Annotated[
        CategoryOfTheBranch,
        Field(
            description='Describes the characteristics of the labeled branch.',
            title='Category of the branch',
        ),
    ]
    name: Annotated[
        str,
        Field(
            description="Contains the canonical descriptor or 'friendly name' of the branch.",
            examples=[
                '10',
                '365',
                'Microsoft',
                'Office',
                'PCS 7',
                'SIMATIC',
                'Siemens',
                'Windows',
            ],
            min_length=1,
            title='Name of the branch',
        ),
    ]
    product: Optional[FullProductName] = None


class ListOfBranches(BaseModel):
    """
    Contains branch elements as children of the current element.
    """

    __root__: Annotated[
        Sequence[Branch],
        Field(
            description='Contains branch elements as children of the current element.',
            # min_items=1,
            title='List of branches',
        ),
    ]

    @no_type_check
    @validator('__root__')
    def check_len(cls, v):
        if not v:
            raise ValueError('mandatory element present but empty')
        return v


Branch.update_forward_refs()

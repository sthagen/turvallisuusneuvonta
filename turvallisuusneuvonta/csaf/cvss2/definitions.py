"""CVSS 2.0 general definitions."""

from __future__ import annotations

from enum import Enum
from typing import Annotated

from pydantic import BaseModel, Field


class AccessVectorType(Enum):
    network = 'NETWORK'
    adjacent_network = 'ADJACENT_NETWORK'
    local = 'LOCAL'


class AccessComplexityType(Enum):
    high = 'HIGH'
    medium = 'MEDIUM'
    low = 'LOW'


class AuthenticationType(Enum):
    multiple = 'MULTIPLE'
    single = 'SINGLE'
    none = 'NONE'


class CiaType(Enum):
    none = 'NONE'
    partial = 'PARTIAL'
    complete = 'COMPLETE'


class ExploitabilityType(Enum):
    unproven = 'UNPROVEN'
    proof_of_concept = 'PROOF_OF_CONCEPT'
    functional = 'FUNCTIONAL'
    high = 'HIGH'
    not_defined = 'NOT_DEFINED'


class RemediationLevelType(Enum):
    official_fix = 'OFFICIAL_FIX'
    temporary_fix = 'TEMPORARY_FIX'
    workaround = 'WORKAROUND'
    unavailable = 'UNAVAILABLE'
    not_defined = 'NOT_DEFINED'


class ReportConfidenceType(Enum):
    unconfirmed = 'UNCONFIRMED'
    uncorroborated = 'UNCORROBORATED'
    confirmed = 'CONFIRMED'
    not_defined = 'NOT_DEFINED'


class CollateralDamagePotentialType(Enum):
    none = 'NONE'
    low = 'LOW'
    low_medium = 'LOW_MEDIUM'
    medium_high = 'MEDIUM_HIGH'
    high = 'HIGH'
    not_defined = 'NOT_DEFINED'


class TargetDistributionType(Enum):
    none = 'NONE'
    low = 'LOW'
    medium = 'MEDIUM'
    high = 'HIGH'
    not_defined = 'NOT_DEFINED'


class CiaRequirementType(Enum):
    low = 'LOW'
    medium = 'MEDIUM'
    high = 'HIGH'
    not_defined = 'NOT_DEFINED'


class ScoreType(BaseModel):
    __root__: Annotated[float, Field(ge=0.0, le=10.0)]

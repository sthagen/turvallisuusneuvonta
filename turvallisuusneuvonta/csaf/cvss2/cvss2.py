"""CSAF CVSS 2.0 proxy implementation."""

from __future__ import annotations

from enum import Enum
from typing import Annotated, Optional

from pydantic import BaseModel, Field

from turvallisuusneuvonta.csaf.cvss2.definitions import (
    AccessComplexityType,
    AccessVectorType,
    AuthenticationType,
    CiaRequirementType,
    CiaType,
    CollateralDamagePotentialType,
    ExploitabilityType,
    RemediationLevelType,
    ReportConfidenceType,
    ScoreType,
    TargetDistributionType,
)


class Version(Enum):
    """
    CVSS Version
    """

    value = '2.0'


class CVSS(BaseModel):
    version: Annotated[Version, Field(description='CVSS Version')]
    vector_string: Annotated[
        str,
        Field(
            alias='vector_string',
            regex=(
                '^((AV:[NAL]|AC:[LMH]|Au:[MSN]|[CIA]:[NPC]|E:(U|POC|F|H|ND)|RL:(OF|TF|W|U|ND)|RC:(UC|UR|C|ND)|CDP:'
                '(N|L|LM|MH|H|ND)|TD:(N|L|M|H|ND)|[CIA]R:(L|M|H|ND))/)*(AV:[NAL]|AC:[LMH]|Au:[MSN]|[CIA]:[NPC]|E:'
                '(U|POC|F|H|ND)|RL:(OF|TF|W|U|ND)|RC:(UC|UR|C|ND)|CDP:(N|L|LM|MH|H|ND)|TD:(N|L|M|H|ND)|[CIA]R:'
                '(L|M|H|ND))$'
            ),
        ),
    ]
    access_vector: Annotated[Optional[AccessVectorType], Field(alias='access_vector')] = None
    access_complexity: Annotated[Optional[AccessComplexityType], Field(alias='access_complexity')] = None
    authentication: Optional[AuthenticationType] = None
    confidentiality_impact: Annotated[Optional[CiaType], Field(alias='confidentiality_impact')] = None
    integrity_impact: Annotated[Optional[CiaType], Field(alias='integrity_impact')] = None
    availability_impact: Annotated[Optional[CiaType], Field(alias='availability_impact')] = None
    base_score: Annotated[ScoreType, Field(alias='base_score')]
    exploitability: Optional[ExploitabilityType] = None
    remediation_level: Annotated[Optional[RemediationLevelType], Field(alias='remediation_level')] = None
    report_confidence: Annotated[Optional[ReportConfidenceType], Field(alias='report_confidence')] = None
    temporal_score: Annotated[Optional[ScoreType], Field(alias='temporal_score')] = None
    collateral_damage_potential: Annotated[
        Optional[CollateralDamagePotentialType],
        Field(alias='collateral_damage_potential'),
    ] = None
    target_distribution: Annotated[Optional[TargetDistributionType], Field(alias='target_distribution')] = None
    confidentiality_requirement: Annotated[
        Optional[CiaRequirementType], Field(alias='confidentiality_requirement')
    ] = None
    integrity_requirement: Annotated[Optional[CiaRequirementType], Field(alias='integrity_requirement')] = None
    availability_requirement: Annotated[Optional[CiaRequirementType], Field(alias='availability_requirement')] = None
    environmental_score: Annotated[Optional[ScoreType], Field(alias='environmental_score')] = None

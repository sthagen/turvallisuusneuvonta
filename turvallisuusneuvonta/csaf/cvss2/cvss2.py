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

    field_2_0 = '2.0'


class Field0(BaseModel):
    version: Annotated[Version, Field(description='CVSS Version')]
    vector_string: Annotated[
        str,
        Field(
            alias='vectorString',
            regex=(
                '^((AV:[NAL]|AC:[LMH]|Au:[MSN]|[CIA]:[NPC]|E:(U|POC|F|H|ND)|RL:(OF|TF|W|U|ND)|RC:(UC|UR|C|ND)|CDP:'
                '(N|L|LM|MH|H|ND)|TD:(N|L|M|H|ND)|[CIA]R:(L|M|H|ND))/)*(AV:[NAL]|AC:[LMH]|Au:[MSN]|[CIA]:[NPC]|E:'
                '(U|POC|F|H|ND)|RL:(OF|TF|W|U|ND)|RC:(UC|UR|C|ND)|CDP:(N|L|LM|MH|H|ND)|TD:(N|L|M|H|ND)|[CIA]R:'
                '(L|M|H|ND))$'
            ),
        ),
    ]
    access_vector: Annotated[Optional[AccessVectorType], Field(alias='accessVector')] = None
    access_complexity: Annotated[Optional[AccessComplexityType], Field(alias='accessComplexity')] = None
    authentication: Optional[AuthenticationType] = None
    confidentiality_impact: Annotated[Optional[CiaType], Field(alias='confidentialityImpact')] = None
    integrity_impact: Annotated[Optional[CiaType], Field(alias='integrityImpact')] = None
    availability_impact: Annotated[Optional[CiaType], Field(alias='availabilityImpact')] = None
    base_score: Annotated[ScoreType, Field(alias='baseScore')]
    exploitability: Optional[ExploitabilityType] = None
    remediation_level: Annotated[Optional[RemediationLevelType], Field(alias='remediationLevel')] = None
    report_confidence: Annotated[Optional[ReportConfidenceType], Field(alias='reportConfidence')] = None
    temporal_score: Annotated[Optional[ScoreType], Field(alias='temporalScore')] = None
    collateral_damage_potential: Annotated[
        Optional[CollateralDamagePotentialType],
        Field(alias='collateralDamagePotential'),
    ] = None
    target_distribution: Annotated[Optional[TargetDistributionType], Field(alias='targetDistribution')] = None
    confidentiality_requirement: Annotated[
        Optional[CiaRequirementType], Field(alias='confidentialityRequirement')
    ] = None
    integrity_requirement: Annotated[Optional[CiaRequirementType], Field(alias='integrityRequirement')] = None
    availability_requirement: Annotated[Optional[CiaRequirementType], Field(alias='availabilityRequirement')] = None
    environmental_score: Annotated[Optional[ScoreType], Field(alias='environmentalScore')] = None

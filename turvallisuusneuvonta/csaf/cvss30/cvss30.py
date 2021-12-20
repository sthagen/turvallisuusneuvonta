"""CSAF CVSS 3.0 proxy implementation."""

from __future__ import annotations

from enum import Enum
from typing import Annotated, Optional

from pydantic import BaseModel, Field

from turvallisuusneuvonta.csaf.cvss30.definitions import (
    AttackComplexityType,
    AttackVectorType,
    CiaRequirementType,
    CiaType,
    ConfidenceType,
    ExploitCodeMaturityType,
    ModifiedAttackComplexityType,
    ModifiedAttackVectorType,
    ModifiedCiaType,
    ModifiedPrivilegesRequiredType,
    ModifiedScopeType,
    ModifiedUserInteractionType,
    PrivilegesRequiredType,
    RemediationLevelType,
    ScopeType,
    ScoreType,
    SeverityType,
    UserInteractionType,
)


class Version(Enum):
    """
    CVSS Version
    """

    value = '3.0'


class CVSS(BaseModel):
    version: Annotated[Version, Field(description='CVSS Version')]
    vector_string: Annotated[
        str,
        Field(
            alias='vector_string',
            regex=(
                '^CVSS:3[.]0/((AV:[NALP]|AC:[LH]|PR:[UNLH]|UI:[NR]|S:[UC]|[CIA]:[NLH]|E:[XUPFH]|RL:[XOTWU]|RC:[XURC]|'
                '[CIA]R:[XLMH]|MAV:[XNALP]|MAC:[XLH]|MPR:[XUNLH]|MUI:[XNR]|MS:[XUC]|M[CIA]:[XNLH])/)*(AV:[NALP]|'
                'AC:[LH]|PR:[UNLH]|UI:[NR]|S:[UC]|[CIA]:[NLH]|E:[XUPFH]|RL:[XOTWU]|RC:[XURC]|[CIA]R:[XLMH]|'
                'MAV:[XNALP]|MAC:[XLH]|MPR:[XUNLH]|MUI:[XNR]|MS:[XUC]|M[CIA]:[XNLH])$'
            ),
        ),
    ]
    attack_vector: Annotated[Optional[AttackVectorType], Field(alias='attack_vector')] = None
    attack_complexity: Annotated[Optional[AttackComplexityType], Field(alias='attack_complexity')] = None
    privileges_required: Annotated[Optional[PrivilegesRequiredType], Field(alias='privileges_required')] = None
    user_interaction: Annotated[Optional[UserInteractionType], Field(alias='user_interaction')] = None
    scope: Optional[ScopeType] = None
    confidentiality_impact: Annotated[Optional[CiaType], Field(alias='confidentiality_impact')] = None
    integrity_impact: Annotated[Optional[CiaType], Field(alias='integrity_impact')] = None
    availability_impact: Annotated[Optional[CiaType], Field(alias='availability_impact')] = None
    base_score: Annotated[ScoreType, Field(alias='base_score')]
    base_severity: Annotated[SeverityType, Field(alias='base_severity')]
    exploit_code_maturity: Annotated[Optional[ExploitCodeMaturityType], Field(alias='exploit_code_maturity')] = None
    remediation_level: Annotated[Optional[RemediationLevelType], Field(alias='remediation_level')] = None
    report_confidence: Annotated[Optional[ConfidenceType], Field(alias='report_confidence')] = None
    temporal_score: Annotated[Optional[ScoreType], Field(alias='temporal_score')] = None
    temporal_severity: Annotated[Optional[SeverityType], Field(alias='temporal_severity')] = None
    confidentiality_requirement: Annotated[
        Optional[CiaRequirementType], Field(alias='confidentiality_requirement')
    ] = None
    integrity_requirement: Annotated[Optional[CiaRequirementType], Field(alias='integrity_requirement')] = None
    availability_requirement: Annotated[Optional[CiaRequirementType], Field(alias='availability_requirement')] = None
    modified_attack_vector: Annotated[Optional[ModifiedAttackVectorType], Field(alias='modified_attack_vector')] = None
    modified_attack_complexity: Annotated[
        Optional[ModifiedAttackComplexityType], Field(alias='modified_attack_complexity')
    ] = None
    modified_privileges_required: Annotated[
        Optional[ModifiedPrivilegesRequiredType],
        Field(alias='modified_privileges_required'),
    ] = None
    modified_user_interaction: Annotated[
        Optional[ModifiedUserInteractionType], Field(alias='modified_user_interaction')
    ] = None
    modified_scope: Annotated[Optional[ModifiedScopeType], Field(alias='modified_scope')] = None
    modified_confidentiality_impact: Annotated[
        Optional[ModifiedCiaType], Field(alias='modified_confidentiality_impact')
    ] = None
    modified_integrity_impact: Annotated[Optional[ModifiedCiaType], Field(alias='modified_integrity_impact')] = None
    modified_availability_impact: Annotated[
        Optional[ModifiedCiaType], Field(alias='modified_availability_impact')
    ] = None
    environmental_score: Annotated[Optional[ScoreType], Field(alias='environmental_score')] = None
    environmental_severity: Annotated[Optional[SeverityType], Field(alias='environmental_severity')] = None

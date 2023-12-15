# generated by datamodel-codegen:
#   filename:  openapi_full.yaml
#   timestamp: 2023-11-20T08:16:19+00:00

from __future__ import annotations

from enum import IntEnum
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, constr


class AreaOfConcernDto(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None


class CriterionType(IntEnum):
    In = 0
    Out = 1


class ElementType(IntEnum):
    BaseElement = 666
    Alpha = 1
    WorkProduct = 2
    Activity = 3
    ActivitySpace = 4
    Competency = 5
    Pattern = 6
    State = 7
    LevelOfDetail = 8
    CompetencyLevel = 9
    Checkpoint = 10
    DegreeOfEvidence = 11
    PatternAssociation = 12
    RelatedAssociation = 13
    DescribesAssociation = 14
    RequiredCompetencyLevel = 15
    AlphaCriterion = 16
    WorkProductCriterion = 17


class BasicElementDto(BaseModel):
    id: Optional[UUID] = None


class BasicElementLightDto(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None
    elementType: Optional[ElementType] = None
    groupId: Optional[UUID] = None
    areaOfConcern: Optional[AreaOfConcernDto] = None


class CompetencyLevelExpandedDto(BaseModel):
    id: Optional[UUID] = None
    order: Optional[int] = None
    name: Optional[str] = None
    relatedElement: Optional[BasicElementLightDto] = None


class DescribedByAssociationDto(BaseModel):
    isParent: Optional[bool] = None
    relatedElement: Optional[BasicElementLightDto] = None
    lowerBound: Optional[str] = None
    upperBound: Optional[str] = None


class DescribesAssociationDto(BaseModel):
    isParent: Optional[bool] = None
    relatedElement: Optional[BasicElementLightDto] = None
    lowerBound: Optional[str] = None
    upperBound: Optional[str] = None


class LevelOfDetailExpandedDto(BaseModel):
    id: Optional[UUID] = None
    name: Optional[str] = None
    relatedElement: Optional[BasicElementLightDto] = None


class PatternAssociationDto(BaseModel):
    text: Optional[str] = None
    relatedElement: Optional[BasicElementDto] = None


class PatternAssociationElementDto(BaseModel):
    text: Optional[str] = None
    relatedElement: Optional[BasicElementDto] = None


class RelatedToDto(BaseModel):
    relatedElement: Optional[BasicElementLightDto] = None
    isOwned: Optional[bool] = None
    lowerBound: Optional[str] = None
    upperBound: Optional[str] = None


class RequiredCompetencyLevelDto(BaseModel):
    relatedElement: Optional[CompetencyLevelExpandedDto] = None


class StateExpandedDto(BaseModel):
    id: Optional[UUID] = None
    name: Optional[str] = None
    relatedElement: Optional[BasicElementLightDto] = None


class WorkProductCriterionDto(BaseModel):
    orBeyond: Optional[bool] = None
    inOrOut: Optional[CriterionType] = None
    relatedElement: Optional[LevelOfDetailExpandedDto] = None


class AlphaCriterionDto(BaseModel):
    contributesTo: Optional[bool] = None
    orBeyond: Optional[bool] = None
    inOrOut: Optional[CriterionType] = None
    relatedElement: Optional[StateExpandedDto] = None


class MethodDto(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None
    description: Optional[str] = None
    versionId: Optional[UUID] = None
    sourceId: Optional[UUID] = None
    practices: list[PracticeDto] = []
    original_id: Optional[str] = None


class PracticeDto(BaseModel):
    id: Optional[UUID] = None
    name: Optional[str] = None
    description: Optional[str] = None
    areaOfConcern: Optional[AreaOfConcernDto] = None
    methodId: Optional[int] = None
    versionId: Optional[UUID] = None
    sourceId: Optional[UUID] = None
    competencies: list[CompetencyDto] = []
    activities: list[ActivityDto] = []
    alphas: list[AlphaDto] = []
    patterns: list[PatternDto] = []
    work_products: list[WorkProductDto] = []
    original_id: Optional[str] = None


class CompetencyDto(BaseModel):
    id: Optional[UUID] = None
    name: constr(min_length=1)
    description: Optional[str] = None
    elementType: ElementType
    order: Optional[int] = None
    areaOfConcern: AreaOfConcernDto
    groupId: UUID


class ActivityDto(BaseModel):
    id: Optional[UUID] = None
    name: constr(min_length=1)
    description: Optional[str] = None
    elementType: ElementType
    order: Optional[int] = None
    areaOfConcern: AreaOfConcernDto
    groupId: UUID
    relatedTo: Optional[list[RelatedToDto]] = None
    contains: Optional[list[RelatedToDto]] = None
    patterns: Optional[list[PatternAssociationDto]] = None
    inAlphaCriteria: Optional[list[AlphaCriterionDto]] = None
    outAlphaCriteria: Optional[list[AlphaCriterionDto]] = None
    inWorkProductCriteria: Optional[list[WorkProductCriterionDto]] = None
    outWorkProductCriteria: Optional[list[WorkProductCriterionDto]] = None
    requiredCompetencyLevels: Optional[list[RequiredCompetencyLevelDto]] = None
    versionId: Optional[str] = None


class AlphaDto(BaseModel):
    id: Optional[UUID] = None
    name: constr(min_length=1)
    description: Optional[str] = None
    elementType: ElementType
    order: Optional[int] = None
    areaOfConcern: AreaOfConcernDto
    groupId: UUID
    relatedTo: Optional[list[RelatedToDto]] = None
    contains: Optional[list[RelatedToDto]] = None
    patterns: Optional[list[PatternAssociationDto]] = None
    describedBy: Optional[list[DescribedByAssociationDto]] = None


class PatternDto(BaseModel):
    id: Optional[UUID] = None
    name: constr(min_length=1)
    description: Optional[str] = None
    elementType: ElementType
    order: Optional[int] = None
    areaOfConcern: AreaOfConcernDto
    groupId: UUID
    relatedTo: Optional[list[RelatedToDto]] = None
    contains: Optional[list[RelatedToDto]] = None
    patterns: Optional[list[PatternAssociationDto]] = None
    associatedElements: Optional[list[PatternAssociationElementDto]] = None


class WorkProductStateDto(BaseModel):
    id: Optional[UUID] = None
    name: str
    description: Optional[str] = None
    isSufficient: bool = False
    progressing_spem_id: Optional[str] = None


class WorkProductDto(BaseModel):
    id: Optional[UUID] = None
    name: constr(min_length=1)
    description: Optional[str] = None
    elementType: ElementType
    order: Optional[int] = None
    areaOfConcern: AreaOfConcernDto
    groupId: UUID
    relatedTo: Optional[list[RelatedToDto]] = None
    contains: Optional[list[RelatedToDto]] = None
    patterns: Optional[list[PatternAssociationDto]] = None
    describes: Optional[list[DescribesAssociationDto]] = None
    states: list[WorkProductStateDto] = []
    versionId: Optional[str] = None

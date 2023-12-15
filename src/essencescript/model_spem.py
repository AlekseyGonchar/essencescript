from typing import Optional

from pydantic import BaseModel, Field


class UmaMethodLibraryFieldType(BaseModel):
    xmlns_xsi: str = Field(..., alias="xmlns:xsi")
    xmlns_uma: str = Field(..., alias="xmlns:uma")
    name: Optional[str] = None
    briefDescription: Optional[str] = None
    id: Optional[str] = None
    orderingGuide: Optional[str] = None
    presentationName: Optional[str] = None
    suppressed: Optional[str] = None
    authors: Optional[str] = None
    changeDescription: Optional[str] = None
    version: Optional[str] = None
    tool: Optional[str] = None


class MethodElementPropertyItemFieldType(BaseModel):
    name: Optional[str] = None
    value: Optional[str] = None


class MethodElementPropertyItem(BaseModel):
    field_: MethodElementPropertyItemFieldType = Field(..., alias="$")


class MethodPluginItemFieldType(BaseModel):
    name: Optional[str] = None
    briefDescription: Optional[str] = None
    id: Optional[str] = None
    orderingGuide: Optional[str] = None
    presentationName: Optional[str] = None
    suppressed: Optional[str] = None
    authors: Optional[str] = None
    changeDate: Optional[str] = None
    changeDescription: Optional[str] = None
    version: Optional[str] = None
    supporting: Optional[str] = None
    userChangeable: Optional[str] = None


class MethodPackageItemFieldType(BaseModel):
    xsi_type: str = Field(..., alias="xsi:type")
    name: str
    id: str
    briefDescription: Optional[str] = None
    orderingGuide: Optional[str] = None
    presentationName: Optional[str] = None
    suppressed: Optional[str] = None
    global_: Optional[str] = Field(None, alias="global")
    authors: Optional[str] = None
    changeDescription: Optional[str] = None
    version: Optional[str] = None


class ContentCategoryItemFieldType(BaseModel):
    xsi_type: str = Field(..., alias="xsi:type")
    name: Optional[str] = None
    briefDescription: Optional[str] = None
    id: Optional[str] = None
    orderingGuide: Optional[str] = None
    presentationName: Optional[str] = None
    suppressed: Optional[str] = None
    isAbstract: Optional[str] = None
    variabilityType: Optional[str] = None
    nodeicon: Optional[str] = None
    shapeicon: Optional[str] = None
    variabilityBasedOnElement: Optional[str] = None


class PresentationItemFieldType(BaseModel):
    xsi_type: Optional[str] = Field(None, alias="xsi:type")
    name: Optional[str] = None
    briefDescription: Optional[str] = None
    id: Optional[str] = None
    orderingGuide: Optional[str] = None
    presentationName: Optional[str] = None
    suppressed: Optional[str] = None
    authors: Optional[str] = None
    changeDate: Optional[str] = None
    changeDescription: Optional[str] = None
    version: Optional[str] = None
    externalId: Optional[str] = None
    usageGuidance: Optional[str] = None


class SectionItemFieldType(BaseModel):
    name: Optional[str] = None
    briefDescription: Optional[str] = None
    id: Optional[str] = None
    orderingGuide: Optional[str] = None
    presentationName: Optional[str] = None
    suppressed: Optional[str] = None
    sectionName: Optional[str] = None
    variabilityType: Optional[str] = None


class SectionItem(BaseModel):
    field_: SectionItemFieldType = Field(..., alias="$")
    Description: list[str] = []


class PresentationItem(BaseModel):
    field_: PresentationItemFieldType = Field(..., alias="$")
    MainDescription: Optional[list[str]] = None
    KeyConsiderations: Optional[list[str]] = None
    AssignmentApproaches: Optional[list[str]] = None
    Skills: Optional[list[str]] = None
    Synonyms: Optional[list[str]] = None
    ImpactOfNotHaving: Optional[list[str]] = None
    Purpose: Optional[list[str]] = None
    ReasonsForNotNeeding: Optional[list[str]] = None
    BriefOutline: Optional[list[str]] = None
    RepresentationOptions: Optional[list[str]] = None
    Representation: Optional[list[str]] = None
    Notation: Optional[list[str]] = None
    Section: Optional[list[SectionItem]] = None
    Attachment: Optional[list[str]] = None
    Copyright: Optional[list[str]] = None
    AdditionalInfo: Optional[list[str]] = None
    Application: Optional[list[str]] = None
    Background: Optional[list[str]] = None
    Goals: Optional[list[str]] = None
    LevelsOfAdoption: Optional[list[str]] = None
    Problem: Optional[list[str]] = None
    Alternatives: Optional[list[str]] = None
    ExternalDescription: Optional[list[str]] = None
    PackagingGuidance: Optional[list[str]] = None
    HowToStaff: Optional[list[str]] = None
    Scope: Optional[list[str]] = None
    UsageNotes: Optional[list[str]] = None
    RefinedDescription: Optional[list[str]] = None
    Scale: Optional[list[str]] = None
    ProjectCharacteristics: Optional[list[str]] = None
    RiskLevel: Optional[list[str]] = None
    EstimatingTechnique: Optional[list[str]] = None
    ProjectMemberExpertise: Optional[list[str]] = None
    TypeOfContract: Optional[list[str]] = None


class ContentCategoryItem(BaseModel):
    field_: ContentCategoryItemFieldType = Field(..., alias="$")
    Presentation: Optional[list[PresentationItem]] = None
    MethodElementProperty: Optional[list[MethodElementPropertyItem]] = None
    CategorizedElement: list[str] = []
    Role: Optional[list[str]] = None
    SupportingMaterial: Optional[list[str]] = None
    WorkProduct: list[str] = []
    Task: list[str] = []
    ToolMentor: Optional[list[str]] = None


class ContentElementItemFieldType(BaseModel):
    xsi_type: str = Field("uma:Artifact", alias="xsi:type")
    name: str
    briefDescription: Optional[str] = None
    id: str
    orderingGuide: str
    presentationName: str
    suppressed: str
    isAbstract: str
    nodeicon: Optional[str] = None
    shapeicon: Optional[str] = None
    variabilityType: str
    variabilityBasedOnElement: Optional[str] = None


class ContainedArtifactItemFieldType(BaseModel):
    name: str
    briefDescription: Optional[str] = None
    id: str
    orderingGuide: str
    presentationName: str
    suppressed: str
    isAbstract: str
    variabilityBasedOnElement: Optional[str] = None
    variabilityType: str


class ContainedArtifactItem(BaseModel):
    field_: ContainedArtifactItemFieldType = Field(..., alias="$")


class WorkProductDetailLevelModel(BaseModel):
    name: str
    id: str


class ContentElementItem(BaseModel):
    field_: ContentElementItemFieldType = Field(..., alias="$")
    Presentation: Optional[list[PresentationItem]] = None
    MethodElementProperty: Optional[list[MethodElementPropertyItem]] = None
    SupportingMaterial: Optional[list[str]] = None
    Concept: Optional[list[str]] = None
    Checklist: Optional[list[str]] = None
    Template: Optional[list[str]] = None
    Guideline: Optional[list[str]] = None
    Example: Optional[list[str]] = None
    ResponsibleFor: Optional[list[str]] = None
    PerformedBy: Optional[list[str]] = []
    AdditionallyPerformedBy: Optional[list[str]] = []
    ContentReference: list[str] = []
    MandatoryInput: list[str] = []
    Output: list[str] = []
    OptionalInput: list[str] = []
    ToolMentor: list[str] = []
    Fulfill: list[str] = []
    Report: Optional[list[str]] = None
    ActivityReference: Optional[list[str]] = None
    ContainedArtifact: list["ContentElementItem"] = []
    # Ess mapping
    EssAlphaId: Optional[str] = None
    EssAlphaStateId: Optional[str] = None
    EssActivitySpaceId: Optional[str] = None
    WorkProductDetailsLevelNames: list[WorkProductDetailLevelModel] = []
    MainCompetencies: list[str] = []
    AdditionalCompetencies: list[str] = []


class ProcesFieldType(BaseModel):
    xsi_type: str = Field(..., alias="xsi:type")
    name: str
    briefDescription: Optional[str] = None
    id: str
    orderingGuide: Optional[str] = None
    presentationName: str
    suppressed: Optional[str] = None
    isAbstract: Optional[str] = None
    hasMultipleOccurrences: Optional[str] = None
    isOptional: Optional[str] = None
    isPlanned: Optional[str] = None
    prefix: Optional[str] = None
    isEventDriven: Optional[str] = None
    isOngoing: Optional[str] = None
    isRepeatable: Optional[str] = None
    variabilityType: Optional[str] = None
    diagramURI: Optional[str] = None


class BreakdownElementItemFieldType(BaseModel):
    xsi_type: str = Field(..., alias="xsi:type")
    name: Optional[str] = None
    briefDescription: Optional[str] = None
    id: Optional[str] = None
    orderingGuide: Optional[str] = None
    presentationName: Optional[str] = None
    suppressed: Optional[str] = None
    isAbstract: Optional[str] = None
    hasMultipleOccurrences: Optional[str] = None
    isOptional: Optional[str] = None
    isPlanned: Optional[str] = None
    prefix: Optional[str] = None
    isEventDriven: Optional[str] = None
    isOngoing: Optional[str] = None
    isRepeatable: Optional[str] = None
    variabilityType: Optional[str] = None
    isSynchronizedWithSource: Optional[str] = None
    activityEntryState: Optional[str] = None
    activityExitState: Optional[str] = None
    variabilityBasedOnElement: Optional[str] = None


class PredecessorItemFieldType(BaseModel):
    id: str
    linkType: str


class PredecessorItem(BaseModel):
    field_: Optional[str] = Field(None, alias="_")
    field__1: PredecessorItemFieldType = Field(..., alias="$")


class StepItemFieldType(BaseModel):
    name: str
    briefDescription: Optional[str] = None
    id: str
    orderingGuide: str
    presentationName: str
    suppressed: str
    sectionName: str
    variabilityType: str


class StepItem(BaseModel):
    field_: StepItemFieldType = Field(..., alias="$")
    Description: list[str] = []


class BreakdownElementItem(BaseModel):
    field_: BreakdownElementItemFieldType = Field(..., alias="$")
    Presentation: Optional[list[PresentationItem]] = None
    SuperActivity: list[str] = []
    BreakdownElement: list["BreakdownElementItem"] = []
    Predecessor: Optional[list[PredecessorItem]] = None
    Checklist: Optional[list[str]] = None
    Concept: Optional[list[str]] = None
    Guideline: Optional[list[str]] = None
    Task: Optional[list[str]] = []
    OptionalInput: Optional[list[str]] = None
    Output: list[str] = []
    Step: Optional[list[StepItem]] = None
    WorkProduct: Optional[list[str]] = []
    MandatoryInput: Optional[list[str]] = None
    Example: Optional[list[str]] = None
    MethodElementProperty: Optional[list[MethodElementPropertyItem]] = None
    SupportingMaterial: Optional[list[str]] = None
    AdditionallyPerformedBy: Optional[list[str]] = None
    PerformedPrimarilyBy: Optional[list[str]] = None
    Role: Optional[list[str]] = None
    ResponsibleFor: Optional[list[str]] = None


class ProcessItem(BaseModel):
    field_: ProcesFieldType = Field(..., alias="$")
    Presentation: list[PresentationItem] = []
    BreakdownElement: list[BreakdownElementItem] = []
    MethodElementProperty: Optional[list[MethodElementPropertyItem]] = None
    IncludesPattern: Optional[list[str]] = None


class MethodPackageItem(BaseModel):
    field_: MethodPackageItemFieldType = Field(..., alias="$")
    ContentCategory: list[ContentCategoryItem] = []
    ContentElement: list[ContentElementItem] = []
    MethodElementProperty: list[MethodElementPropertyItem] = []
    MethodPackage: list["MethodPackageItem"] = []
    Process: list[ProcessItem] = []
    ProcessElement: list[ProcessItem] = []


class MethodPluginItem(BaseModel):
    field_: MethodPluginItemFieldType = Field(..., alias="$")
    MethodElementProperty: list[MethodElementPropertyItem]
    Copyright: list[str] = []
    ReferencedMethodPlugin: Optional[list[str]] = None
    MethodPackage: list[MethodPackageItem]


class MethodConfigurationItemFieldType(BaseModel):
    name: str
    briefDescription: Optional[str] = None
    id: str
    orderingGuide: str
    presentationName: str
    suppressed: str
    authors: str
    changeDescription: Optional[str] = None
    version: str


class MethodConfigurationItem(BaseModel):
    field_: MethodConfigurationItemFieldType = Field(..., alias="$")
    MethodElementProperty: list[MethodElementPropertyItem]
    MethodPluginSelection: list[str]
    MethodPackageSelection: list[str]
    DefaultView: list[str]
    ProcessView: list[str]


class UmaMethodLibrary(BaseModel):
    field_: UmaMethodLibraryFieldType = Field(..., alias="$")
    MethodElementProperty: list[MethodElementPropertyItem]
    MethodPlugin: list[MethodPluginItem]
    MethodConfiguration: list[MethodConfigurationItem]


class Model(BaseModel):
    uma_MethodLibrary: UmaMethodLibrary = Field(..., alias="uma:MethodLibrary")

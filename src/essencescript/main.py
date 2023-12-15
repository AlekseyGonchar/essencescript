from collections import Counter

import orjson

from essencescript.enums import XsiType
from essencescript.ess_api import EssenceAPI
from essencescript.essence_models import (
    ActivityDto,
    AlphaCriterionDto,
    AreaOfConcernDto,
    BasicElementLightDto,
    CompetencyLevelExpandedDto,
    CriterionType,
    DescribesAssociationDto,
    ElementType,
    LevelOfDetailExpandedDto,
    MethodDto,
    PracticeDto,
    RelatedToDto,
    RequiredCompetencyLevelDto,
    StateExpandedDto,
    WorkProductCriterionDto,
    WorkProductDto,
    WorkProductStateDto,
)
from essencescript.kernel import (
    ActivitySpaceToAlphaInput,
    ActivitySpaceToAlphaOutput,
    Alphas,
    AlphaStates,
    AlphaToAreaOfConcern,
    AreaOfConcern,
    Competency,
    CompetencyLevel,
    CompetencyLevelToCompetency,
    StateToAlpha,
)
from essencescript.model_spem import (
    BreakdownElementItem,
    ContentElementItem,
    MethodPackageItem,
    MethodPluginItem,
    Model,
    ProcessItem,
    UmaMethodLibrary,
    WorkProductDetailLevelModel,
)
from essencescript.openup_mappings import (
    role_to_competencies_main,
    tasks_to_essence_activity_space,
    tasks_to_essence_alpha_state,
)

ess_api = EssenceAPI()
spem_objects = {}
content_objects: dict[str, ContentElementItem] = {}
breakdown_objects: dict[str, BreakdownElementItem] = {}

referenced_tasks: set[str] = set()
referenced_artifacts: set[str] = set()

plugins: dict[str, MethodPluginItem] = {}
practice_to_ids: dict[str, list[str]] = {}
content_id_to_practice: dict[str, str] = {}
practicess: dict[str, ContentElementItem] = {}
practicess_bases: dict[str, ContentElementItem] = {}

delivery_process: dict[str, ProcessItem] = {}
processes: dict[str, ProcessItem] = {}

artifacts: dict[str, ContentElementItem] = {}
artifacts_bases: dict[str, ContentElementItem] = {}
artifacts_bases_without_slots: dict[str, ContentElementItem] = {}

tasks: dict[str, ContentElementItem] = {}
tasks_bases: dict[str, ContentElementItem] = {}
work_products_ess: dict[str, WorkProductDto] = {}

activities: dict[str, BreakdownElementItem] = {}
activities_bases: dict[str, BreakdownElementItem] = {}

iterations: dict[str, BreakdownElementItem] = {}
tasks_descriptors: dict[str, BreakdownElementItem] = {}
phases: dict[str, BreakdownElementItem] = {}

ordered_task_descriptors: list[BreakdownElementItem] = []
ordered_tasks: list[ContentElementItem] = []

spem_to_ess_id = {}


def map_breakdown_element(element: BreakdownElementItem) -> None:
    breakdown_objects[element.field_.id] = element

    match element.field_.xsi_type:
        case XsiType.Activity:
            activities[element.field_.id] = element
        case XsiType.Iteration:
            iterations[element.field_.id] = element
        case XsiType.TaskDescriptor:
            tasks_descriptors[element.field_.id] = element
        case XsiType.Phase:
            phases[element.field_.id] = element

    for breakdown in element.BreakdownElement:
        map_breakdown_element(breakdown)


def map_method_package(package: MethodPackageItem, practice_id: str) -> None:
    spem_objects[package.field_.id] = package

    for category in package.ContentCategory:
        spem_objects[category.field_.id] = category

    for process in package.Process:
        for breakdown in process.BreakdownElement:
            map_breakdown_element(breakdown)

    for element in package.ContentElement:
        spem_objects[element.field_.id] = element
        content_objects[element.field_.id] = element

        match element.field_.xsi_type:
            case XsiType.Task:
                tasks[element.field_.id] = element
            case XsiType.Artifact:
                artifacts[element.field_.id] = element
            case XsiType.Practice:
                practicess[element.field_.id] = element

        for contained in element.ContainedArtifact:
            spem_objects[contained.field_.id] = contained
            content_objects[contained.field_.id] = contained

            match contained.field_.xsi_type:
                case XsiType.Task:
                    tasks[contained.field_.id] = contained
                case XsiType.Artifact:
                    artifacts[contained.field_.id] = contained
                case XsiType.Practice:
                    practicess[contained.field_.id] = contained

    for process in package.Process:
        spem_objects[process.field_.id] = process
        processes[process.field_.id] = process

        if process.field_.xsi_type == XsiType.DeliveryProcess:
            delivery_process[process.field_.id] = process

    for process in package.ProcessElement:
        spem_objects[process.field_.id] = process
        processes[process.field_.id] = process

        if process.field_.xsi_type == XsiType.DeliveryProcess:
            delivery_process[process.field_.id] = process

    for inner_package in package.MethodPackage:
        map_method_package(inner_package, practice_id)


def map_spem_objects(method: UmaMethodLibrary) -> None:
    referenced_practices = (
        method.MethodConfiguration[0].MethodPluginSelection + method.MethodConfiguration[0].MethodElementProperty
    )
    referenced_practices = [plugin for plugin in method.MethodPlugin if plugin.field_.id in referenced_practices]

    for plugin in referenced_practices:
        spem_objects[plugin.field_.id] = plugin
        plugins[plugin.field_.id] = plugin

        for package in plugin.MethodPackage:
            map_method_package(package, plugin.field_.id)


def merge_ids_unique_only(left: list[str] | None, right: list[str] | None) -> None | list[str]:
    match left, right:
        case None, None:
            return None
        case _, None:
            return right
        case None, _:
            return left
        case _, _:
            res = set(left)
            res.update(set(right))
            return list(res)


def merge_content_objects() -> None:
    for key, item in content_objects.items():
        if item.field_.variabilityBasedOnElement:
            base = content_objects[item.field_.variabilityBasedOnElement]
            base.Presentation = base.Presentation or item.Presentation
            base.MethodElementProperty = base.MethodElementProperty or item.MethodElementProperty
            base.SupportingMaterial = base.SupportingMaterial or item.SupportingMaterial
            base.Concept = base.Concept or item.Concept
            base.Checklist = base.Checklist or item.Checklist
            base.Template = base.Template or item.Template
            base.Guideline = base.Guideline or item.Guideline
            base.Example = base.Example or item.Example
            base.ResponsibleFor = merge_ids_unique_only(base.ResponsibleFor, item.ResponsibleFor)
            base.PerformedBy = merge_ids_unique_only(base.PerformedBy, item.PerformedBy)
            base.AdditionallyPerformedBy = merge_ids_unique_only(
                base.AdditionallyPerformedBy,
                item.AdditionallyPerformedBy,
            )
            base.ContentReference = merge_ids_unique_only(base.ContentReference, item.ContentReference)
            base.MandatoryInput = merge_ids_unique_only(base.MandatoryInput, item.MandatoryInput)
            base.Output = merge_ids_unique_only(base.Output, item.Output)
            base.OptionalInput = merge_ids_unique_only(base.OptionalInput, item.OptionalInput)
            base.ToolMentor = base.ToolMentor or item.ToolMentor
            base.Fulfill = merge_ids_unique_only(base.Fulfill, item.Fulfill)
            base.Report = base.Report or item.Report
            base.ActivityReference = merge_ids_unique_only(base.ActivityReference, item.ActivityReference)
            base.ContainedArtifact = base.ContainedArtifact or item.ContainedArtifact

    for key, item in content_objects.items():
        if item.field_.variabilityBasedOnElement:
            base = content_objects[item.field_.variabilityBasedOnElement]
            item.Presentation = item.Presentation or base.Presentation
            item.MethodElementProperty = item.MethodElementProperty or base.MethodElementProperty
            item.SupportingMaterial = item.SupportingMaterial or base.SupportingMaterial
            item.Concept = item.Concept or base.Concept
            item.Checklist = item.Checklist or base.Checklist
            item.Template = item.Template or base.Template
            item.Guideline = item.Guideline or base.Guideline
            item.Example = item.Example or base.Example
            item.ResponsibleFor = merge_ids_unique_only(item.ResponsibleFor, base.ResponsibleFor)
            item.PerformedBy = merge_ids_unique_only(item.PerformedBy, base.PerformedBy)
            item.AdditionallyPerformedBy = merge_ids_unique_only(
                item.AdditionallyPerformedBy,
                base.AdditionallyPerformedBy,
            )
            item.ContentReference = merge_ids_unique_only(item.ContentReference, base.ContentReference)
            item.MandatoryInput = merge_ids_unique_only(item.MandatoryInput, base.MandatoryInput)
            item.Output = merge_ids_unique_only(item.Output, base.Output)
            item.OptionalInput = merge_ids_unique_only(item.OptionalInput, base.OptionalInput)
            item.ToolMentor = item.ToolMentor or base.ToolMentor
            item.Fulfill = merge_ids_unique_only(item.Fulfill, base.Fulfill)
            item.Report = item.Report or base.Report
            item.ActivityReference = merge_ids_unique_only(item.ActivityReference, base.ActivityReference)
            item.ContainedArtifact = item.ContainedArtifact or base.ContainedArtifact


def merge_breakdown(left: list[BreakdownElementItem], right: list[BreakdownElementItem]) -> list[BreakdownElementItem]:
    if not left:
        return right
    if not right:
        return left

    result = right
    right_ids = set(item.field_.id for item in right)

    for item in left:
        if item.field_.id not in right_ids:
            result.append(item)
            right_ids.add(item.field_.id)

    return result


def merge_breakdown_elements() -> None:
    for key, item in breakdown_objects.items():
        if item.field_.variabilityBasedOnElement:
            base = breakdown_objects.get(item.field_.variabilityBasedOnElement)

            if not base:
                base = processes[item.field_.variabilityBasedOnElement]
                base.Presentation = base.Presentation or item.Presentation
                base.BreakdownElement = base.BreakdownElement or item.BreakdownElement
                base.MethodElementProperty = base.MethodElementProperty or item.MethodElementProperty
                continue

            base.Presentation = base.Presentation or item.Presentation
            base.SuperActivity = base.SuperActivity or item.SuperActivity
            base.BreakdownElement = base.BreakdownElement or item.BreakdownElement
            base.Predecessor = base.Predecessor or item.Predecessor
            base.Checklist = base.Checklist or item.Checklist
            base.Concept = base.Concept or item.Concept
            base.Guideline = base.Guideline or item.Guideline
            base.Task = base.Task or item.Task
            base.OptionalInput = base.OptionalInput or item.OptionalInput
            base.Output = base.Output or item.Output
            base.Step = base.Step or item.Step
            base.WorkProduct = base.WorkProduct or item.WorkProduct
            base.MandatoryInput = base.MandatoryInput or item.MandatoryInput
            base.Example = base.Example or item.Example
            base.MethodElementProperty = base.MethodElementProperty or item.MethodElementProperty
            base.SupportingMaterial = base.SupportingMaterial or item.SupportingMaterial
            base.AdditionallyPerformedBy = base.AdditionallyPerformedBy or item.AdditionallyPerformedBy
            base.PerformedPrimarilyBy = base.PerformedPrimarilyBy or item.PerformedPrimarilyBy
            base.Role = base.Role or item.Role
            base.ResponsibleFor = base.ResponsibleFor or item.ResponsibleFor

    for key, item in breakdown_objects.items():
        if item.field_.variabilityBasedOnElement:
            base = breakdown_objects.get(item.field_.variabilityBasedOnElement)

            if not base:
                base = processes[item.field_.variabilityBasedOnElement]
                item.Presentation = item.Presentation or base.Presentation
                item.BreakdownElement = merge_breakdown(item.BreakdownElement, base.BreakdownElement)
                item.MethodElementProperty = item.MethodElementProperty or base.MethodElementProperty
                continue

            item.Presentation = item.Presentation or base.Presentation
            item.SuperActivity = item.SuperActivity or base.SuperActivity
            item.BreakdownElement = merge_breakdown(item.BreakdownElement, base.BreakdownElement)
            item.Predecessor = item.Predecessor or base.Predecessor
            item.Checklist = item.Checklist or base.Checklist
            item.Concept = item.Concept or base.Concept
            item.Guideline = item.Guideline or base.Guideline
            item.Task = item.Task or base.Task
            item.OptionalInput = item.OptionalInput or base.OptionalInput
            item.Output = item.Output or base.Output
            item.Step = item.Step or base.Step
            item.WorkProduct = item.WorkProduct or base.WorkProduct
            item.MandatoryInput = item.MandatoryInput or base.MandatoryInput
            item.Example = item.Example or base.Example
            item.MethodElementProperty = item.MethodElementProperty or base.MethodElementProperty
            item.SupportingMaterial = item.SupportingMaterial or base.SupportingMaterial
            item.AdditionallyPerformedBy = item.AdditionallyPerformedBy or base.AdditionallyPerformedBy
            item.PerformedPrimarilyBy = item.PerformedPrimarilyBy or base.PerformedPrimarilyBy
            item.Role = item.Role or base.Role
            item.ResponsibleFor = item.ResponsibleFor or base.ResponsibleFor


def fill_up_bases() -> None:
    global artifacts_bases
    global tasks_bases
    global activities_bases
    global practicess_bases
    artifacts_bases = {k: v for k, v in artifacts.items() if v.field_.variabilityBasedOnElement is None}
    tasks_bases = {k: v for k, v in tasks.items() if v.field_.variabilityBasedOnElement is None}
    activities_bases = {k: v for k, v in activities.items() if v.field_.variabilityBasedOnElement is None}
    practicess_bases = {k: v for k, v in practicess.items() if v.field_.variabilityBasedOnElement is None}


def create_method(method: UmaMethodLibrary) -> MethodDto:
    ess_method = MethodDto(
        name=method.MethodConfiguration[0].field_.presentationName,
        description=method.MethodConfiguration[0].field_.briefDescription,
        practices=[],
        original_id=method.field_.id,
    )
    created = ess_api.create_method(ess_method)
    spem_to_ess_id[method.field_.id] = ess_method
    return created


def count_pracitce_area_of_concern(ids: list[str]) -> AreaOfConcernDto:
    area_of_concern_hits = {
        AreaOfConcern.Endeavour: 0,
        AreaOfConcern.Solution: 0,
        AreaOfConcern.Customer: 0,
    }

    for id in ids:
        elem = content_objects.get(id)

        if elem:
            states = tasks_to_essence_alpha_state.get(elem.field_.name)
            if states:
                for state in states:
                    alpha = StateToAlpha[state]
                    concern = AlphaToAreaOfConcern[alpha]
                    area_of_concern_hits[concern] += 1

    max_key = max(area_of_concern_hits, key=lambda k: area_of_concern_hits[k], default=AreaOfConcern.Undefined)
    return AreaOfConcernDto(
        id=max_key,
        name=max_key.name,
    )


def create_practices_which_contain_something(method: MethodDto) -> list[PracticeDto]:
    practices_ess = []

    for k, value in practicess_bases.items():
        references = value.ContentReference
        area_of_concern = count_pracitce_area_of_concern(references)

        # for item in references:
        #     if tasks_bases.get(item) or artifacts_bases_without_slots.get(item):
        #         break
        # else:
        #     continue

        new_practice = PracticeDto(
            name=value.field_.presentationName or value.field_.name,
            description=value.field_.briefDescription,
            areaOfConcern=area_of_concern,
            methodId=method.id,
            versionId=method.versionId,
            competencies=[],
            activities=[],
            alphas=[],
            patterns=[],
            work_products=[],
            original_id=value.field_.id,
        )
        created = ess_api.create_practice(practice=new_practice)
        practices_ess.append(created)
        spem_to_ess_id[value.field_.id] = created

    method.practices = practices_ess
    return practices_ess


def add_task_descriptors(breakdown: BreakdownElementItem) -> None:
    global ordered_task_descriptors
    if breakdown.field_.xsi_type == XsiType.TaskDescriptor and breakdown.Task:
        ordered_task_descriptors.append(breakdown)

    for item in breakdown.BreakdownElement:
        add_task_descriptors(item)


def count_work_product_detail_levels() -> None:
    delivery_proc = list(delivery_process.values())[0]

    for item in delivery_proc.BreakdownElement:
        add_task_descriptors(item)

    for item in ordered_task_descriptors:
        ordered_tasks.append(tasks[item.Task[0]])

    for work_product in artifacts.values():
        tasks_outputting_work_product = [
            item.field_.id
            for item in ordered_tasks
            if work_product.field_.id in item.Output and item.field_.id in referenced_tasks
        ]

        lookup = set()
        ls = [item for item in tasks_outputting_work_product if item not in lookup and lookup.add(item) is None]
        progressing_tasks = [tasks[item] for item in ls]

        work_product.WorkProductDetailsLevelNames = [
            WorkProductDetailLevelModel(
                name=progressing_task.field_.presentationName + " done",
                id=progressing_task.field_.id,
            )
            for progressing_task in progressing_tasks
        ]


def get_tasks_which_define_artifact(artifact_id: str) -> list[str]:
    result = []

    for k, v in tasks_bases.items():
        if artifact_id in v.Output:
            result.append(k)

    return result


def get_alpha_states_from_ids(ids: list[str]) -> list[AlphaStates]:
    tasks_names = []

    for id in ids:
        tasks_names.append(tasks[id].field_.name)

    alpha_states = []

    for task in tasks_names:
        states = tasks_to_essence_alpha_state.get(task)

        if states:
            alpha_states.extend(states)

    return alpha_states


def determine_area_of_concern_from_alpha_states(ids: list[str]) -> AreaOfConcernDto:
    alpha_states = get_alpha_states_from_ids(ids)

    counted = {
        Alphas.Stakeholders: 0,
        Alphas.Work: 0,
        Alphas.Opportunity: 0,
        Alphas.Requirements: 0,
        Alphas.Software_System: 0,
        Alphas.Team: 0,
        Alphas.Way_of_Working: 0,
    }

    for state in alpha_states:
        counted[StateToAlpha[state]] += 1

    max_key = max(counted, key=lambda k: counted[k])
    concern = AlphaToAreaOfConcern[max_key]

    return AreaOfConcernDto(
        id=concern,
        name=concern.name,
    )


def get_described_alphas(ids: list[str]) -> list[DescribesAssociationDto]:
    alpha_states = get_alpha_states_from_ids(ids)
    alphas = []

    for state in alpha_states:
        alphas.append(StateToAlpha[state])

    try:
        main_alpha = Counter(alphas).most_common(1)[0][0]
    except:
        return [DescribesAssociationDto(isParent=True, relatedElement=BasicElementLightDto(id=Alphas.Software_System))]

    all_alphas = set(alphas)
    all_alphas.remove(main_alpha)
    result = [DescribesAssociationDto(isParent=True, relatedElement=BasicElementLightDto(id=main_alpha))]
    result.extend(
        DescribesAssociationDto(isParent=False, relatedElement=BasicElementLightDto(id=alpha)) for alpha in all_alphas
    )
    return result


def create_work_products() -> list[WorkProductDto]:
    work_products_ess = []

    for item in artifacts_bases_without_slots.values():
        if item.field_.id not in referenced_artifacts:
            continue

        tasks_which_define_artifact = get_tasks_which_define_artifact(item.field_.id)

        area_of_concern = (
            determine_area_of_concern_from_alpha_states(tasks_which_define_artifact)
            if tasks_which_define_artifact
            else AreaOfConcernDto(id=AreaOfConcern.Solution, name=AreaOfConcern.Solution.name)
        )

        practic = content_id_to_practice.get(item.field_.id)

        for task in tasks_which_define_artifact:
            if not practic:
                practic = content_id_to_practice.get(task)

        if not practic:
            print(f"skipping work product {item.field_.presentationName} id: {item.field_.id}")
            continue

        work_product = WorkProductDto(
            name=item.field_.presentationName,
            description=item.field_.briefDescription,
            elementType=ElementType.WorkProduct,
            areaOfConcern=area_of_concern,
            groupId=spem_to_ess_id[practic].id,
            versionId=str(spem_to_ess_id[practic].versionId),
            states=[
                WorkProductStateDto(
                    id=None,
                    name=state.name,
                    progressing_spem_id=state.id,
                )
                for state in item.WorkProductDetailsLevelNames
            ],
            describes=get_described_alphas(tasks_which_define_artifact)
            if tasks_which_define_artifact
            else [
                DescribesAssociationDto(isParent=True, relatedElement=BasicElementLightDto(id=Alphas.Way_of_Working)),
            ],
        )
        created = ess_api.create_work_product(work_product)
        work_products_ess.append(created)
        spem_to_ess_id[item.field_.id] = created

    return work_products_ess


def get_highest_competencies(competencies: list[CompetencyLevel]) -> list[CompetencyLevel]:
    competencies_cost = {
        CompetencyLevel.Leadership_Assists: 1,
        CompetencyLevel.Leadership_Applies: 2,
        CompetencyLevel.Leadership_Masters: 3,
        CompetencyLevel.Leadership_Adapts: 4,
        CompetencyLevel.Leadership_Innovates: 5,
        CompetencyLevel.Analysis_Assists: 101,
        CompetencyLevel.Analysis_Applies: 102,
        CompetencyLevel.Analysis_Masters: 103,
        CompetencyLevel.Analysis_Adapts: 104,
        CompetencyLevel.Analysis_Innovates: 105,
        CompetencyLevel.Stakeholder_Representation_Assists: 201,
        CompetencyLevel.Stakeholder_Representation_Applies: 202,
        CompetencyLevel.Stakeholder_Representation_Masters: 203,
        CompetencyLevel.Stakeholder_Representation_Adapts: 204,
        CompetencyLevel.Stakeholder_Representation_Innovates: 205,
        CompetencyLevel.Testing_Assists: 301,
        CompetencyLevel.Testing_Applies: 302,
        CompetencyLevel.Testing_Masters: 303,
        CompetencyLevel.Testing_Adapts: 304,
        CompetencyLevel.Testing_Innovates: 305,
        CompetencyLevel.Management_Assists: 401,
        CompetencyLevel.Management_Applies: 402,
        CompetencyLevel.Management_Masters: 403,
        CompetencyLevel.Management_Adapts: 404,
        CompetencyLevel.Management_Innovates: 405,
        CompetencyLevel.Development_Assists: 501,
        CompetencyLevel.Development_Applies: 502,
        CompetencyLevel.Development_Masters: 503,
        CompetencyLevel.Development_Adapts: 504,
        CompetencyLevel.Development_Innovates: 505,
    }
    reversed = {v: k for k, v in competencies_cost.items()}
    competencies_res = {
        Competency.Leadership: 0,
        Competency.Stakeholder_Representation: 0,
        Competency.Analysis: 0,
        Competency.Development: 0,
        Competency.Testing: 0,
        Competency.Management: 0,
    }
    competencies_unique = list(set(competencies))

    for comp in competencies_unique:
        cost = competencies_cost[comp]
        compet = CompetencyLevelToCompetency[comp]
        competencies_res[compet] = max(competencies_res[compet], cost)

    result = [reversed.get(item) for item in competencies_res.values()]
    return [item for item in result if item]


def replace_role_with_competency(ids: list[str]) -> list[CompetencyLevel]:
    result = []

    for id in ids:
        role_obj = spem_objects[id]
        check_id = id

        while role_obj.field_.variabilityBasedOnElement:
            check_id = spem_objects[role_obj.field_.variabilityBasedOnElement].field_.id
            role_obj = spem_objects[role_obj.field_.variabilityBasedOnElement]

        result.extend(role_to_competencies_main[check_id])

    return result


def create_tasks() -> list[ActivityDto]:
    activities_ess = []

    for item in tasks_bases.values():
        if item.field_.id not in referenced_tasks:
            continue

        roles = item.PerformedBy + item.AdditionallyPerformedBy
        set_competencies = get_highest_competencies(replace_role_with_competency(roles))

        work_product_out = []

        for outputted in item.Output:
            if spem_to_ess_id.get(outputted):
                work_prod = spem_to_ess_id.get(outputted)

                if work_prod:
                    detail_level = next(
                        iter(
                            level for level in work_prod.states if level.name == f"{item.field_.presentationName} done"
                        ),
                        None,
                    )
                    if detail_level:
                        work_product_out.append(
                            WorkProductCriterionDto(
                                orBeyond=False,
                                inOrOut=CriterionType.Out,
                                relatedElement=LevelOfDetailExpandedDto(
                                    name="",
                                    relatedElement=BasicElementLightDto(id=detail_level.id),
                                ),
                            ),
                        )

        work_product_in = []

        inputs_ids = item.MandatoryInput + item.OptionalInput

        for inputted in inputs_ids:
            if spem_to_ess_id.get(inputted):
                work_prod = spem_to_ess_id[inputted]

        activity_spaces = tasks_to_essence_activity_space[item.field_.name]
        inputs = []
        outputs = []

        for space in activity_spaces:
            inputs.extend(ActivitySpaceToAlphaInput[space])
            outputs.extend(ActivitySpaceToAlphaOutput[space])

        practice_id = content_id_to_practice.get(item.field_.id)

        for output in item.Output:
            if not practice_id:
                practice_id = content_id_to_practice.get(spem_objects[output].field_.id)

        if not practice_id:
            print(f"skipping activity {item.field_.presentationName} id: {item.field_.id}")
            continue

        activity = ActivityDto(
            name=item.field_.presentationName,
            description=item.field_.briefDescription,
            elementType=ElementType.Activity,
            areaOfConcern=determine_area_of_concern_from_alpha_states([item.field_.id]),
            groupId=spem_to_ess_id[practice_id].id,
            versionId=str(spem_to_ess_id[practice_id].versionId),
            requiredCompetencyLevels=[
                RequiredCompetencyLevelDto(relatedElement=CompetencyLevelExpandedDto(id=str(comp)))
                for comp in set_competencies
            ],
            inWorkProductCriteria=work_product_in,
            outWorkProductCriteria=work_product_out,
            relatedTo=[
                RelatedToDto(
                    relatedElement=BasicElementLightDto(
                        id=space,
                    ),
                    isOwned=True,
                )
                for space in activity_spaces
            ],
            outAlphaCriteria=[
                AlphaCriterionDto(
                    contributesTo=True,
                    inOrOut=CriterionType.Out,
                    relatedElement=StateExpandedDto(id=str(item)),
                )
                for item in outputs
            ],
            inAlphaCriteria=[
                AlphaCriterionDto(
                    contributesTo=False,
                    inOrOut=CriterionType.In,
                    relatedElement=StateExpandedDto(id=str(item)),
                )
                for item in inputs
            ],
        )
        created = ess_api.create_activity(activity)
        activities_ess.append(created)
        spem_to_ess_id[item.field_.id] = created

    return activities_ess


def reverse_practice_dict() -> None:
    global content_id_to_practice

    for k, v in practice_to_ids.items():
        for item in v:
            content_id_to_practice[item] = k


def replace_slots_with_fulfilled_artifacts() -> None:
    replace_map = {}

    for artifact in artifacts_bases.values():
        for fulfill in artifact.Fulfill:
            if replace_map.get(fulfill):
                replace_map[fulfill].append(artifact.field_.id)
            else:
                replace_map[fulfill] = [artifact.field_.id]

    for k, v in artifacts_bases.items():
        if not replace_map.get(k):
            artifacts_bases_without_slots[k] = v

    for task in tasks_bases.values():
        for i, item in enumerate(task.MandatoryInput):
            if replacement := replace_map.get(item):
                task.MandatoryInput.remove(item)
                task.MandatoryInput.extend(replacement)
        for i, item in enumerate(task.OptionalInput):
            if replacement := replace_map.get(item):
                task.OptionalInput.remove(item)
                task.OptionalInput.extend(replacement)
        for i, item in enumerate(task.Output):
            if replacement := replace_map.get(item):
                task.Output.remove(item)
                task.Output.extend(replacement)


def map_content_ref() -> None:
    pass


def fill_up_practice_dict() -> None:
    for k, v in practicess.items():
        key = k

        if v.field_.variabilityBasedOnElement:
            key = v.field_.variabilityBasedOnElement

        practice_to_ids[key] = practice_to_ids.get(key) or []

        for item in v.ContentReference:
            match spem_objects[item].field_.xsi_type:
                case XsiType.Task:
                    practice_to_ids[key].append(item)
                case XsiType.Artifact:
                    practice_to_ids[key].append(item)
                case (XsiType.ContentPackage, XsiType.CustomCategory):
                    for ref in spem_objects[item].CategorizedElement:
                        match spem_objects[ref].field_.xsi_type:
                            case XsiType.Task:
                                practice_to_ids[key].append(ref)
                            case XsiType.Artifact:
                                practice_to_ids[key].append(ref)

                    for ref in spem_objects[item].WorkProduct:
                        match spem_objects[ref].field_.xsi_type:
                            case XsiType.Task:
                                practice_to_ids[key].append(ref)
                            case XsiType.Artifact:
                                practice_to_ids[key].append(ref)

                    for ref in spem_objects[item].Task:
                        match spem_objects[ref].field_.xsi_type:
                            case XsiType.Task:
                                practice_to_ids[key].append(ref)
                            case XsiType.Artifact:
                                practice_to_ids[key].append(ref)


def collect_referneced_task(elem: BreakdownElementItem) -> None:
    referenced_artifacts.update(elem.WorkProduct)
    referenced_tasks.update(elem.Task)

    for item in elem.BreakdownElement:
        collect_referneced_task(item)


def collect_referenced_tasks_and_work_products() -> None:
    proc = list(delivery_process.values())[0]

    for item in proc.BreakdownElement:
        collect_referneced_task(item)


def create_breakdown_element() -> None:
    pass


def create_lifecycle() -> None:
    proc = list(delivery_process.values())[0]


with open("/home/spess/Projects/Personal/Essence/essencescript/src/resources/converted.json", "rb") as file:
    parsed = orjson.loads(file.read())
    converted = Model(**parsed)
    map_spem_objects(converted.uma_MethodLibrary)
    merge_content_objects()
    merge_content_objects()
    merge_content_objects()
    merge_breakdown_elements()
    merge_breakdown_elements()
    merge_breakdown_elements()
    fill_up_bases()
    fill_up_practice_dict()
    reverse_practice_dict()
    replace_slots_with_fulfilled_artifacts()
    collect_referenced_tasks_and_work_products()
    count_work_product_detail_levels()
    method = create_method(converted.uma_MethodLibrary)
    create_practices_which_contain_something(method)
    create_lifecycle()
    create_work_products()
    create_tasks()
    print("1")

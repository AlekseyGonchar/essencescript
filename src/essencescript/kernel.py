from enum import Enum, StrEnum

from essencescript.essence_models import AreaOfConcernDto, PracticeDto


class AreaOfConcern(Enum):
    Undefined = 0
    Solution = 1
    Endeavour = 2
    Customer = 3


class AlphaStates(StrEnum):
    Stakeholders_Recognized = "3a26278f-954b-4318-82dd-1fe2d00a061d"
    Stakeholders_Represented = "cd4b0ea2-7942-4ac6-9060-820741d6913b"
    Stakeholders_Involved = "9aa55cf1-8946-49e7-a601-7d9c98f632b0"
    Stakeholders_In_Agreement = "0eedc018-34b8-4c05-a6f9-39f64fcffd7b"
    Stakeholders_Satisfied_for_Deployment = "f37074cd-6507-437b-aff4-c51b69aedfd3"
    Stakeholders_Satisfied_in_Use = "df90ad95-6692-40c8-9559-e1785dc83d44"
    Work_Initiated = "61904e48-0e8d-44ef-974f-b74a0db55880"
    Work_Prepared = "2494a74d-e1f0-4b1e-8f50-879c475756a9"
    Work_Started = "6afb562c-4c30-44df-932f-9215c7037294"
    Work_Under_Control = "31023c25-31d9-4ea5-bf14-b52653df6d6b"
    Work_Concluded = "787398ac-8a56-40d9-8043-2300526fd511"
    Work_Closed = "b5c06d64-7adc-4bb5-94c7-605445783e4b"
    Opportunity_Identified = "43d16b21-5a1a-4e21-b42d-e4e71a466272"
    Opportunity_Solution_Needed = "8dd9fe66-2f86-4b05-aac3-d096d040d17a"
    Opportunity_Value_Established = "24c7a5ca-d734-4771-b192-4364c4328029"
    Opportunity_Viable = "37c1195d-6910-4da7-a670-ef6297af47f7"
    Opportunity_Addressed = "6eacd031-d392-459b-9d42-4abf58473b14"
    Opportunity_Benefit_Accrued = "8a632b5f-ff1a-4c00-a923-abf76479a047"
    Requirements_Conceived = "d33a65d6-5d2a-4fc8-b804-701236196fba"
    Requirements_Bounded = "fd38b187-ffe5-432a-90ca-ebdce4569a0b"
    Requirements_Coherent = "e9f06e85-d007-4b04-8a9f-f77f0ce1f133"
    Requirements_Acceptable = "1e0cac52-3365-4b1f-9aac-4eff44ba1449"
    Requirements_Addressed = "a58b9ab7-4bb2-4c97-b9b2-62c15dd12de2"
    Requirements_Fulfilled = "e905569b-829c-4c06-9fdf-bb7937bae142"
    Software_System_Architecture_Selected = "a922a8ce-7122-40d1-97e8-900fb8c9aec2"
    Software_System_Demonstrable = "63acae69-9d63-46e3-bef5-7236f42744c6"
    Software_System_Usable = "013dd6b7-7902-4e30-b3d5-9cc3a42aedf8"
    Software_System_Ready = "8befa1c2-1e32-4941-911f-ced8c894f0e8"
    Software_System_Operational = "c2c49b59-4d0f-40eb-af86-f154e530eca7"
    Software_System_Retired = "538b7249-e03b-4d77-b686-36edbc98742a"
    Team_Seeded = "cc2dba9e-5bf8-4cf7-a2a2-20ad182d089f"
    Team_Formed = "753ed6cc-d7f5-4f10-8997-ca722462f155"
    Team_Collaborating = "277eb803-6eee-4be1-a53a-fa137ba4f813"
    Team_Performing = "c68af9bb-820b-491a-b049-ad8e2b98ac70"
    Team_Adjourned = "1c0311b5-b622-46ce-8d0a-37257a7d42d0"
    Way_of_Working_Principles_Established = "521f8e8f-0b34-432c-a148-cc23104f8886"
    Way_of_Working_Foundation_Established = "ed30ece0-23b7-410b-b5b8-4782cfc54548"
    Way_of_Working_In_Use = "2adfd18a-3dda-49d9-bb8a-852980b7bbb9"
    Way_of_Working_In_Place = "487079b1-71df-4505-a217-7ba28882f853"
    Way_of_Working_Working_Well = "a9effbea-7d16-442c-a969-0707ca51436a"
    Way_of_Working_Retired = "39648af8-5359-48aa-ba50-18201758a12e"


class Alphas(StrEnum):
    Stakeholders = "2ccfac3a-4319-4d17-af74-160dee325827"
    Work = "e4eccea2-a0a4-4a9c-b194-185cf7959207"
    Opportunity = "e6b015ac-c0d3-42ca-9e5c-437990405131"
    Requirements = "622c9e0d-c7fc-4fc3-a1b1-5aff61d439c9"
    Software_System = "e6bd190b-38b4-4aa6-a407-b743a203babb"
    Team = "d7faf996-2a93-4c40-8535-d6f1352f8024"
    Way_of_Working = "7482666f-96d4-4a08-b31d-e48adcfb0cb9"


class ActivitySpaces(StrEnum):
    Coordinate_Activity = "ec517376-edf4-4ad4-81a2-c9ac18966cae"
    Shape_the_System = "9106c635-6e70-4e38-823f-b95e9b39389f"
    Support_the_Team = "269f32f7-0fe0-4454-8883-916b4cf5db0c"
    Ensure_Stakeholder_Satisfaction = "ec108ede-2739-458c-b0c0-91d3909a4758"
    Use_the_System = "26f1cbb0-bd5b-46ab-a516-95209f91cb24"
    Understand_the_Requirements = "eb878ed5-cb7c-452e-b336-a13a61d8b56a"
    Understand_Stakeholder_Needs = "7fc17b6e-4807-48eb-9541-dbc8b5c2242e"
    Implement_the_System = "7ad94def-d736-46c4-b5b9-dd8745e88495"
    Explore_Possibilities = "d376a86a-1a5c-40c6-bb1a-6d795e150e0f"
    Track_Progress = "87781cef-6087-4e75-9f49-6ed938de8dc6"
    Prepare_to_do_the_Work = "7671b6c6-3506-4125-a128-70f9fe065df6"
    Test_the_System = "2ee5ec82-9188-42a8-914a-06b30f840ca8"
    Stop_the_Work = "48dd37b7-1e9e-448f-87f8-3c253688ee5b"
    Deploy_the_System = "9f3b85b3-85f3-403d-8266-411e0ac38c77"
    Operate_the_System = "f171d173-8a3d-4d49-84e8-25a4a111bd91"


class Competency(StrEnum):
    Leadership = "92aa4d7b-239c-4788-8660-317c60eb45cf"
    Stakeholder_Representation = "e1831321-c9cf-4514-9807-74f5821ca979"
    Analysis = "00866707-06e1-4035-a5ca-6701b0f64243"
    Development = "d2b6922a-56d5-4d41-b5a1-fbc4ee7bb78f"
    Testing = "6f554e41-47cc-4857-9ed2-93fedfe33a03"
    Management = "30d06766-1414-4030-a369-c59fe17c870c"


class CompetencyLevel(StrEnum):
    Leadership_Assists = "8a6f6cd1-ff6c-4f16-ae65-a133a0434296"
    Leadership_Applies = "fcb1200a-719b-4bcf-8359-c36bca417a5f"
    Leadership_Masters = "5676226c-b750-4bd0-9971-4f5796859704"
    Leadership_Adapts = "54b53b49-60ff-49e2-bfd8-b7bc8da88e68"
    Leadership_Innovates = "c2139d97-4d66-40f5-84dc-c1132a7434eb"
    Analysis_Assists = "8021237b-5591-444d-ad75-726456cf7099"
    Analysis_Applies = "025809ce-c299-45b3-b29d-a734f183cd20"
    Analysis_Masters = "0bfd9443-4620-490e-9574-fc50f5814437"
    Analysis_Adapts = "59e8db7a-66f3-448c-a07f-0efe3d630228"
    Analysis_Innovates = "8b66c11a-8ce0-4316-a431-91837caee9e6"
    Stakeholder_Representation_Assists = "23913f55-507d-4760-960b-69a5b9599582"
    Stakeholder_Representation_Applies = "ca3bb2db-8cde-4dd3-8a8d-4550172a8312"
    Stakeholder_Representation_Masters = "d0420347-c338-4647-a620-987f8bdfbbfe"
    Stakeholder_Representation_Adapts = "b901a120-98eb-4b62-9406-5cd005c5e3ab"
    Stakeholder_Representation_Innovates = "014ccd09-79a3-4e39-9207-07a65308b16f"
    Testing_Assists = "e77717d1-acf6-46ab-a9fe-716e7e01d258"
    Testing_Applies = "70323d9c-e2e1-4e11-8545-b6738899cc01"
    Testing_Masters = "30738a74-9158-49c1-9e2f-a8b13e221df3"
    Testing_Adapts = "a1cb0881-e8aa-4dee-80ae-2395687b5799"
    Testing_Innovates = "391a1fd8-67b9-49f8-991e-c64191355e05"
    Management_Assists = "1bdd09dc-e19d-4e67-9350-ab41cdabe9c3"
    Management_Applies = "11760b61-de03-46ba-8e98-28cc071f395e"
    Management_Masters = "b19dcb14-c8b4-4d71-99a1-5facd02c7f9a"
    Management_Adapts = "bfc0c028-6df8-438b-9788-71bd23026d4f"
    Management_Innovates = "2b66a14c-6805-4836-8c54-ed7dadf3e00b"
    Development_Assists = "ee89e3b3-555e-40e4-8390-33b6d5e7bcef"
    Development_Applies = "f7b0c86b-8105-4a47-b3b3-f19d71cb6f57"
    Development_Masters = "97f43121-026b-4817-9471-44f04544a9b3"
    Development_Adapts = "36962e90-c6d8-46a6-a1da-cd12a8fe1d36"
    Development_Innovates = "b4fe106c-4e41-4a34-abf9-7d40bc2648a5"


class WorkProductDetailLevel(StrEnum):
    Began = "Began"
    PartiallyDone = "PartiallyDone"
    Done = "Done"


AlphaToAreaOfConcern = {
    Alphas.Stakeholders: AreaOfConcern.Customer,
    Alphas.Work: AreaOfConcern.Endeavour,
    Alphas.Opportunity: AreaOfConcern.Customer,
    Alphas.Requirements: AreaOfConcern.Solution,
    Alphas.Software_System: AreaOfConcern.Solution,
    Alphas.Team: AreaOfConcern.Endeavour,
    Alphas.Way_of_Working: AreaOfConcern.Endeavour,
}

AlphaToStates = {
    Alphas.Stakeholders: [
        AlphaStates.Stakeholders_Recognized,
        AlphaStates.Stakeholders_Represented,
        AlphaStates.Stakeholders_Involved,
        AlphaStates.Stakeholders_In_Agreement,
        AlphaStates.Stakeholders_Satisfied_for_Deployment,
        AlphaStates.Stakeholders_Satisfied_in_Use,
    ],
    Alphas.Work: [
        AlphaStates.Work_Initiated,
        AlphaStates.Work_Prepared,
        AlphaStates.Work_Started,
        AlphaStates.Work_Under_Control,
        AlphaStates.Work_Concluded,
        AlphaStates.Work_Closed,
    ],
    Alphas.Opportunity: [
        AlphaStates.Opportunity_Identified,
        AlphaStates.Opportunity_Solution_Needed,
        AlphaStates.Opportunity_Value_Established,
        AlphaStates.Opportunity_Viable,
        AlphaStates.Opportunity_Addressed,
        AlphaStates.Opportunity_Benefit_Accrued,
    ],
    Alphas.Requirements: [
        AlphaStates.Requirements_Conceived,
        AlphaStates.Requirements_Bounded,
        AlphaStates.Requirements_Coherent,
        AlphaStates.Requirements_Acceptable,
        AlphaStates.Requirements_Addressed,
        AlphaStates.Requirements_Fulfilled,
    ],
    Alphas.Software_System: [
        AlphaStates.Software_System_Architecture_Selected,
        AlphaStates.Software_System_Demonstrable,
        AlphaStates.Software_System_Usable,
        AlphaStates.Software_System_Ready,
        AlphaStates.Software_System_Operational,
        AlphaStates.Software_System_Retired,
    ],
    Alphas.Team: [
        AlphaStates.Team_Seeded,
        AlphaStates.Team_Formed,
        AlphaStates.Team_Collaborating,
        AlphaStates.Team_Performing,
        AlphaStates.Team_Adjourned,
    ],
    Alphas.Way_of_Working: [
        AlphaStates.Way_of_Working_Principles_Established,
        AlphaStates.Way_of_Working_Foundation_Established,
        AlphaStates.Way_of_Working_In_Use,
        AlphaStates.Way_of_Working_In_Place,
        AlphaStates.Way_of_Working_Working_Well,
        AlphaStates.Way_of_Working_Retired,
    ],
}

StateToAlpha = {
    AlphaStates.Stakeholders_Recognized: Alphas.Stakeholders,
    AlphaStates.Stakeholders_Represented: Alphas.Stakeholders,
    AlphaStates.Stakeholders_Involved: Alphas.Stakeholders,
    AlphaStates.Stakeholders_In_Agreement: Alphas.Stakeholders,
    AlphaStates.Stakeholders_Satisfied_for_Deployment: Alphas.Stakeholders,
    AlphaStates.Stakeholders_Satisfied_in_Use: Alphas.Stakeholders,
    AlphaStates.Work_Initiated: Alphas.Work,
    AlphaStates.Work_Prepared: Alphas.Work,
    AlphaStates.Work_Started: Alphas.Work,
    AlphaStates.Work_Under_Control: Alphas.Work,
    AlphaStates.Work_Concluded: Alphas.Work,
    AlphaStates.Work_Closed: Alphas.Work,
    AlphaStates.Opportunity_Identified: Alphas.Opportunity,
    AlphaStates.Opportunity_Solution_Needed: Alphas.Opportunity,
    AlphaStates.Opportunity_Value_Established: Alphas.Opportunity,
    AlphaStates.Opportunity_Viable: Alphas.Opportunity,
    AlphaStates.Opportunity_Addressed: Alphas.Opportunity,
    AlphaStates.Opportunity_Benefit_Accrued: Alphas.Opportunity,
    AlphaStates.Requirements_Conceived: Alphas.Requirements,
    AlphaStates.Requirements_Bounded: Alphas.Requirements,
    AlphaStates.Requirements_Coherent: Alphas.Requirements,
    AlphaStates.Requirements_Acceptable: Alphas.Requirements,
    AlphaStates.Requirements_Addressed: Alphas.Requirements,
    AlphaStates.Requirements_Fulfilled: Alphas.Requirements,
    AlphaStates.Software_System_Architecture_Selected: Alphas.Software_System,
    AlphaStates.Software_System_Demonstrable: Alphas.Software_System,
    AlphaStates.Software_System_Usable: Alphas.Software_System,
    AlphaStates.Software_System_Ready: Alphas.Software_System,
    AlphaStates.Software_System_Operational: Alphas.Software_System,
    AlphaStates.Software_System_Retired: Alphas.Software_System,
    AlphaStates.Team_Seeded: Alphas.Team,
    AlphaStates.Team_Formed: Alphas.Team,
    AlphaStates.Team_Collaborating: Alphas.Team,
    AlphaStates.Team_Performing: Alphas.Team,
    AlphaStates.Team_Adjourned: Alphas.Team,
    AlphaStates.Way_of_Working_Principles_Established: Alphas.Way_of_Working,
    AlphaStates.Way_of_Working_Foundation_Established: Alphas.Way_of_Working,
    AlphaStates.Way_of_Working_In_Use: Alphas.Way_of_Working,
    AlphaStates.Way_of_Working_In_Place: Alphas.Way_of_Working,
    AlphaStates.Way_of_Working_Working_Well: Alphas.Way_of_Working,
    AlphaStates.Way_of_Working_Retired: Alphas.Way_of_Working,
}

CompetencyLevelToCompetency = {
    CompetencyLevel.Leadership_Assists: Competency.Leadership,
    CompetencyLevel.Leadership_Applies: Competency.Leadership,
    CompetencyLevel.Leadership_Masters: Competency.Leadership,
    CompetencyLevel.Leadership_Adapts: Competency.Leadership,
    CompetencyLevel.Leadership_Innovates: Competency.Leadership,
    CompetencyLevel.Analysis_Assists: Competency.Analysis,
    CompetencyLevel.Analysis_Applies: Competency.Analysis,
    CompetencyLevel.Analysis_Masters: Competency.Analysis,
    CompetencyLevel.Analysis_Adapts: Competency.Analysis,
    CompetencyLevel.Analysis_Innovates: Competency.Analysis,
    CompetencyLevel.Stakeholder_Representation_Assists: Competency.Stakeholder_Representation,
    CompetencyLevel.Stakeholder_Representation_Applies: Competency.Stakeholder_Representation,
    CompetencyLevel.Stakeholder_Representation_Masters: Competency.Stakeholder_Representation,
    CompetencyLevel.Stakeholder_Representation_Adapts: Competency.Stakeholder_Representation,
    CompetencyLevel.Stakeholder_Representation_Innovates: Competency.Stakeholder_Representation,
    CompetencyLevel.Testing_Assists: Competency.Testing,
    CompetencyLevel.Testing_Applies: Competency.Testing,
    CompetencyLevel.Testing_Masters: Competency.Testing,
    CompetencyLevel.Testing_Adapts: Competency.Testing,
    CompetencyLevel.Testing_Innovates: Competency.Testing,
    CompetencyLevel.Management_Assists: Competency.Management,
    CompetencyLevel.Management_Applies: Competency.Management,
    CompetencyLevel.Management_Masters: Competency.Management,
    CompetencyLevel.Management_Adapts: Competency.Management,
    CompetencyLevel.Management_Innovates: Competency.Management,
    CompetencyLevel.Development_Assists: Competency.Development,
    CompetencyLevel.Development_Applies: Competency.Development,
    CompetencyLevel.Development_Masters: Competency.Development,
    CompetencyLevel.Development_Adapts: Competency.Development,
    CompetencyLevel.Development_Innovates: Competency.Development,
}

ActivitySpaceToAlphaInput = {
    ActivitySpaces.Explore_Possibilities: [],
    ActivitySpaces.Understand_Stakeholder_Needs: [
        AlphaStates.Stakeholders_Recognized,
        AlphaStates.Opportunity_Value_Established,
    ],
    ActivitySpaces.Ensure_Stakeholder_Satisfaction: [
        AlphaStates.Stakeholders_In_Agreement,
        AlphaStates.Opportunity_Value_Established,
    ],
    ActivitySpaces.Use_the_System: [
        AlphaStates.Stakeholders_Satisfied_for_Deployment,
        AlphaStates.Opportunity_Addressed,
    ],
    ActivitySpaces.Understand_the_Requirements: [],
    ActivitySpaces.Shape_the_System: [AlphaStates.Requirements_Coherent],
    ActivitySpaces.Implement_the_System: [AlphaStates.Software_System_Architecture_Selected],
    ActivitySpaces.Test_the_System: [
        AlphaStates.Software_System_Architecture_Selected,
        AlphaStates.Requirements_Acceptable,
    ],
    ActivitySpaces.Deploy_the_System: [AlphaStates.Software_System_Ready],
    ActivitySpaces.Operate_the_System: [AlphaStates.Software_System_Ready],
    ActivitySpaces.Prepare_to_do_the_Work: [],
    ActivitySpaces.Coordinate_Activity: [AlphaStates.Team_Seeded, AlphaStates.Work_Prepared],
    ActivitySpaces.Support_the_Team: [AlphaStates.Team_Formed, AlphaStates.Way_of_Working_Foundation_Established],
    ActivitySpaces.Track_Progress: [
        AlphaStates.Team_Collaborating,
        AlphaStates.Work_Started,
        AlphaStates.Way_of_Working_In_Place,
    ],
    ActivitySpaces.Stop_the_Work: [
        AlphaStates.Team_Performing,
        AlphaStates.Work_Concluded,
        AlphaStates.Way_of_Working_Working_Well,
    ],
}
ActivitySpaceToAlphaOutput = {
    ActivitySpaces.Explore_Possibilities: [
        AlphaStates.Stakeholders_Recognized,
        AlphaStates.Opportunity_Identified,
        AlphaStates.Opportunity_Solution_Needed,
        AlphaStates.Opportunity_Value_Established,
    ],
    ActivitySpaces.Understand_Stakeholder_Needs: [AlphaStates.Work_Prepared],
    ActivitySpaces.Ensure_Stakeholder_Satisfaction: [
        AlphaStates.Stakeholders_Satisfied_for_Deployment,
        AlphaStates.Opportunity_Addressed,
    ],
    ActivitySpaces.Use_the_System: [AlphaStates.Opportunity_Benefit_Accrued, AlphaStates.Stakeholders_Satisfied_in_Use],
    ActivitySpaces.Understand_the_Requirements: [
        AlphaStates.Requirements_Conceived,
        AlphaStates.Requirements_Bounded,
        AlphaStates.Requirements_Coherent,
    ],
    ActivitySpaces.Shape_the_System: [
        AlphaStates.Requirements_Acceptable,
        AlphaStates.Software_System_Architecture_Selected,
    ],
    ActivitySpaces.Implement_the_System: [
        AlphaStates.Software_System_Demonstrable,
        AlphaStates.Software_System_Usable,
        AlphaStates.Software_System_Ready,
    ],
    ActivitySpaces.Test_the_System: [
        AlphaStates.Requirements_Addressed,
        AlphaStates.Requirements_Fulfilled,
        AlphaStates.Software_System_Demonstrable,
        AlphaStates.Software_System_Usable,
        AlphaStates.Software_System_Ready,
    ],
    ActivitySpaces.Deploy_the_System: [AlphaStates.Software_System_Operational],
    ActivitySpaces.Operate_the_System: [AlphaStates.Software_System_Retired],
    ActivitySpaces.Prepare_to_do_the_Work: [
        AlphaStates.Team_Seeded,
        AlphaStates.Work_Initiated,
        AlphaStates.Work_Prepared,
        AlphaStates.Way_of_Working_Principles_Established,
        AlphaStates.Way_of_Working_Foundation_Established,
    ],
    ActivitySpaces.Coordinate_Activity: [
        AlphaStates.Team_Formed,
        AlphaStates.Work_Started,
        AlphaStates.Work_Under_Control,
    ],
    ActivitySpaces.Support_the_Team: [
        AlphaStates.Team_Collaborating,
        AlphaStates.Way_of_Working_In_Use,
        AlphaStates.Way_of_Working_In_Place,
    ],
    ActivitySpaces.Track_Progress: [
        AlphaStates.Team_Performing,
        AlphaStates.Work_Under_Control,
        AlphaStates.Work_Concluded,
        AlphaStates.Way_of_Working_Working_Well,
    ],
    ActivitySpaces.Stop_the_Work: [
        AlphaStates.Team_Adjourned,
        AlphaStates.Work_Closed,
        AlphaStates.Way_of_Working_Retired,
    ],
}


life_cycle_practice = PracticeDto(
    name="RUP lifecycle",
    description="This practice describes lifecycle patterns of RUP",
    areaOfConcern=AreaOfConcernDto(
        id=AreaOfConcern.Undefined,
        name=AreaOfConcern.Undefined.name,
    ),
    methodId=None,
    versionId=None,
    competencies=[],
    activities=[],
    alphas=[],
    patterns=[],
    work_products=[],
    original_id=None,
)

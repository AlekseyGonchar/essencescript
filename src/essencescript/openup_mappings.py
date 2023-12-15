from essencescript.enums import Roles
from essencescript.essence_models import AreaOfConcernDto, PracticeDto
from essencescript.kernel import ActivitySpaces, AlphaStates, AreaOfConcern, CompetencyLevel

tasks_to_essence_activity_space = {
    "develop_technical_vision": [ActivitySpaces.Understand_the_Requirements, ActivitySpaces.Explore_Possibilities],
    "plan_the_project": [ActivitySpaces.Prepare_to_do_the_Work],
    "plan_iteration": [ActivitySpaces.Coordinate_Activity],
    "tailor_process": [ActivitySpaces.Prepare_to_do_the_Work],
    "setup_tools": [ActivitySpaces.Prepare_to_do_the_Work],
    "verify_tool_config_installation": [ActivitySpaces.Prepare_to_do_the_Work],
    "deploy_process": [ActivitySpaces.Prepare_to_do_the_Work],
    "manage_iteration": [ActivitySpaces.Coordinate_Activity],
    "assess_results": [ActivitySpaces.Track_Progress],
    "identify_and_outline_requirements": [ActivitySpaces.Understand_the_Requirements],
    "detail_use_case_scenarios": [ActivitySpaces.Understand_the_Requirements],
    "detail_system_wide_requirements": [ActivitySpaces.Understand_the_Requirements],
    "create_test_cases": [ActivitySpaces.Test_the_System],
    "plan_deployment": [ActivitySpaces.Deploy_the_System],
    "envision_the_arch": [ActivitySpaces.Understand_the_Requirements],
    "design_solution": [ActivitySpaces.Shape_the_System],
    "implement_developer_tests": [ActivitySpaces.Implement_the_System],
    "implement_solution": [ActivitySpaces.Implement_the_System],
    "run_developer_tests": [ActivitySpaces.Implement_the_System],
    "integrate_and_create_build": [ActivitySpaces.Implement_the_System],
    "refine_the_arch": [ActivitySpaces.Shape_the_System],
    "implement_tests": [ActivitySpaces.Test_the_System],
    "run_tests": [ActivitySpaces.Test_the_System],
    "request_change": [ActivitySpaces.Support_the_Team],
    "develop_product_documentation": [ActivitySpaces.Ensure_Stakeholder_Satisfaction],
    "develop_user_documentation": [ActivitySpaces.Ensure_Stakeholder_Satisfaction],
    "develop_support_documentation": [ActivitySpaces.Ensure_Stakeholder_Satisfaction],
    "develop_training_materials": [ActivitySpaces.Ensure_Stakeholder_Satisfaction],
    "review_conform_to_release_controls": [ActivitySpaces.Deploy_the_System],
    "install_validate_infrastructure": [ActivitySpaces.Deploy_the_System],
    "develop_backout_plan": [ActivitySpaces.Deploy_the_System],
    "develop_release_communications": [ActivitySpaces.Ensure_Stakeholder_Satisfaction],
    "deliver_end_user_training": [ActivitySpaces.Stop_the_Work],
    "deliver_support_training": [ActivitySpaces.Stop_the_Work],
    "package_the_release": [ActivitySpaces.Deploy_the_System],
    "execute_deployment_plan": [ActivitySpaces.Deploy_the_System],
    "verify_successful_deployment": [ActivitySpaces.Deploy_the_System],
    "execute_backout_plan": [ActivitySpaces.Operate_the_System],
    "deliver_release_communications": [ActivitySpaces.Ensure_Stakeholder_Satisfaction],
}

tasks_to_essence_alpha_state = {
    "develop_technical_vision": [
        AlphaStates.Stakeholders_Recognized,
        AlphaStates.Stakeholders_Represented,
        AlphaStates.Requirements_Conceived,
    ],
    "plan_the_project": [AlphaStates.Work_Initiated, AlphaStates.Work_Prepared],
    "plan_iteration": [AlphaStates.Work_Prepared],
    "tailor_process": [AlphaStates.Way_of_Working_Principles_Established],
    "setup_tools": [AlphaStates.Way_of_Working_Principles_Established],
    "verify_tool_config_installation": [AlphaStates.Way_of_Working_Principles_Established],
    "deploy_process": [AlphaStates.Way_of_Working_Foundation_Established],
    "manage_iteration": [AlphaStates.Work_Under_Control],
    "assess_results": [AlphaStates.Work_Under_Control],
    "identify_and_outline_requirements": [AlphaStates.Requirements_Conceived],
    "detail_use_case_scenarios": [AlphaStates.Requirements_Bounded],
    "detail_system_wide_requirements": [AlphaStates.Requirements_Coherent],
    "create_test_cases": [AlphaStates.Requirements_Coherent],
    "plan_deployment": [AlphaStates.Work_Prepared],
    "envision_the_arch": [AlphaStates.Software_System_Architecture_Selected],
    "design_solution": [AlphaStates.Software_System_Demonstrable],
    "implement_developer_tests": [AlphaStates.Software_System_Demonstrable],
    "implement_solution": [AlphaStates.Software_System_Demonstrable],
    "run_developer_tests": [AlphaStates.Software_System_Demonstrable],
    "integrate_and_create_build": [AlphaStates.Software_System_Demonstrable],
    "refine_the_arch": [AlphaStates.Software_System_Architecture_Selected],
    "implement_tests": [AlphaStates.Software_System_Demonstrable],
    "run_tests": [AlphaStates.Software_System_Ready],
    "request_change": [AlphaStates.Work_Prepared],
    "develop_product_documentation": [AlphaStates.Stakeholders_Satisfied_for_Deployment],
    "develop_user_documentation": [AlphaStates.Stakeholders_Satisfied_for_Deployment],
    "develop_support_documentation": [AlphaStates.Stakeholders_Satisfied_for_Deployment],
    "develop_training_materials": [AlphaStates.Stakeholders_Satisfied_for_Deployment],
    "review_conform_to_release_controls": [AlphaStates.Work_Prepared],
    "install_validate_infrastructure": [AlphaStates.Work_Prepared],
    "develop_backout_plan": [AlphaStates.Stakeholders_Satisfied_for_Deployment],
    "develop_release_communications": [AlphaStates.Stakeholders_Satisfied_for_Deployment],
    "deliver_end_user_training": [AlphaStates.Stakeholders_Satisfied_for_Deployment],
    "deliver_support_training": [AlphaStates.Stakeholders_Satisfied_for_Deployment],
    "package_the_release": [AlphaStates.Software_System_Ready],
    "execute_deployment_plan": [AlphaStates.Software_System_Operational],
    "verify_successful_deployment": [AlphaStates.Software_System_Operational],
    "execute_backout_plan": [AlphaStates.Software_System_Usable],
    "deliver_release_communications": [AlphaStates.Stakeholders_Satisfied_for_Deployment],
}

role_to_competencies_main = {
    Roles.openup_analyst: [CompetencyLevel.Analysis_Masters, CompetencyLevel.Stakeholder_Representation_Applies],
    Roles.openup_any_role: [],
    Roles.openup_architect: [CompetencyLevel.Development_Adapts, CompetencyLevel.Analysis_Masters],
    Roles.openup_developer: [CompetencyLevel.Development_Masters],
    Roles.openup_project_manager: [CompetencyLevel.Management_Masters, CompetencyLevel.Leadership_Applies],
    Roles.openup_stakeholder: [CompetencyLevel.Stakeholder_Representation_Adapts],
    Roles.openup_tester: [CompetencyLevel.Testing_Masters],
    Roles.openup_process_engineer: [CompetencyLevel.Management_Masters],
    Roles.openup_tool_specialist: [CompetencyLevel.Management_Masters, CompetencyLevel.Development_Adapts],
    Roles.openup_course_developer: [
        CompetencyLevel.Analysis_Applies,
        CompetencyLevel.Stakeholder_Representation_Applies,
    ],
    Roles.openup_technical_writer: [CompetencyLevel.Stakeholder_Representation_Applies],
    Roles.openup_trainer: [CompetencyLevel.Stakeholder_Representation_Applies],
    Roles.openup_deployment_engineer: [CompetencyLevel.Development_Masters],
    Roles.openup_deployment_manager: [CompetencyLevel.Development_Masters, CompetencyLevel.Management_Masters],
    Roles.openup_product_owner: [CompetencyLevel.Stakeholder_Representation_Masters],
}

life_cycle_practice = PracticeDto(
    name="OpenUP lifecycle",
    description="This practice describes lifecycle patterns of OpenUP",
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
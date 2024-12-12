# coding: utf-8

from __future__ import absolute_import

from huaweicloudsdkaos.v1.aos_client import AosClient
from huaweicloudsdkaos.v1.aos_async_client import AosAsyncClient

from huaweicloudsdkaos.v1.model.administration_agency_name_primitive_type_holder import AdministrationAgencyNamePrimitiveTypeHolder
from huaweicloudsdkaos.v1.model.administration_agency_urn_primitive_type_holder import AdministrationAgencyUrnPrimitiveTypeHolder
from huaweicloudsdkaos.v1.model.agencies_primitive_type_holder import AgenciesPrimitiveTypeHolder
from huaweicloudsdkaos.v1.model.agency import Agency
from huaweicloudsdkaos.v1.model.apply_execution_plan_request import ApplyExecutionPlanRequest
from huaweicloudsdkaos.v1.model.apply_execution_plan_request_body import ApplyExecutionPlanRequestBody
from huaweicloudsdkaos.v1.model.apply_execution_plan_response import ApplyExecutionPlanResponse
from huaweicloudsdkaos.v1.model.base_template import BaseTemplate
from huaweicloudsdkaos.v1.model.base_template_version import BaseTemplateVersion
from huaweicloudsdkaos.v1.model.call_identity_primitive_type_holder import CallIdentityPrimitiveTypeHolder
from huaweicloudsdkaos.v1.model.configuration_primitive_type_holder import ConfigurationPrimitiveTypeHolder
from huaweicloudsdkaos.v1.model.configuration_primitive_type_holder_configuration import ConfigurationPrimitiveTypeHolderConfiguration
from huaweicloudsdkaos.v1.model.continue_deploy_stack_request import ContinueDeployStackRequest
from huaweicloudsdkaos.v1.model.continue_deploy_stack_request_body import ContinueDeployStackRequestBody
from huaweicloudsdkaos.v1.model.continue_deploy_stack_response import ContinueDeployStackResponse
from huaweicloudsdkaos.v1.model.continue_rollback_stack_request import ContinueRollbackStackRequest
from huaweicloudsdkaos.v1.model.continue_rollback_stack_request_body import ContinueRollbackStackRequestBody
from huaweicloudsdkaos.v1.model.continue_rollback_stack_response import ContinueRollbackStackResponse
from huaweicloudsdkaos.v1.model.create_execution_plan_request import CreateExecutionPlanRequest
from huaweicloudsdkaos.v1.model.create_execution_plan_request_body import CreateExecutionPlanRequestBody
from huaweicloudsdkaos.v1.model.create_execution_plan_response import CreateExecutionPlanResponse
from huaweicloudsdkaos.v1.model.create_private_hook_request import CreatePrivateHookRequest
from huaweicloudsdkaos.v1.model.create_private_hook_request_body import CreatePrivateHookRequestBody
from huaweicloudsdkaos.v1.model.create_private_hook_response import CreatePrivateHookResponse
from huaweicloudsdkaos.v1.model.create_private_hook_version_request import CreatePrivateHookVersionRequest
from huaweicloudsdkaos.v1.model.create_private_hook_version_request_body import CreatePrivateHookVersionRequestBody
from huaweicloudsdkaos.v1.model.create_private_hook_version_response import CreatePrivateHookVersionResponse
from huaweicloudsdkaos.v1.model.create_private_module_request import CreatePrivateModuleRequest
from huaweicloudsdkaos.v1.model.create_private_module_request_body import CreatePrivateModuleRequestBody
from huaweicloudsdkaos.v1.model.create_private_module_response import CreatePrivateModuleResponse
from huaweicloudsdkaos.v1.model.create_private_module_version_request import CreatePrivateModuleVersionRequest
from huaweicloudsdkaos.v1.model.create_private_module_version_request_body import CreatePrivateModuleVersionRequestBody
from huaweicloudsdkaos.v1.model.create_private_module_version_response import CreatePrivateModuleVersionResponse
from huaweicloudsdkaos.v1.model.create_private_provider_request import CreatePrivateProviderRequest
from huaweicloudsdkaos.v1.model.create_private_provider_request_body import CreatePrivateProviderRequestBody
from huaweicloudsdkaos.v1.model.create_private_provider_response import CreatePrivateProviderResponse
from huaweicloudsdkaos.v1.model.create_private_provider_version_request import CreatePrivateProviderVersionRequest
from huaweicloudsdkaos.v1.model.create_private_provider_version_request_body import CreatePrivateProviderVersionRequestBody
from huaweicloudsdkaos.v1.model.create_private_provider_version_response import CreatePrivateProviderVersionResponse
from huaweicloudsdkaos.v1.model.create_stack_instance_request import CreateStackInstanceRequest
from huaweicloudsdkaos.v1.model.create_stack_instance_request_body import CreateStackInstanceRequestBody
from huaweicloudsdkaos.v1.model.create_stack_instance_response import CreateStackInstanceResponse
from huaweicloudsdkaos.v1.model.create_stack_request import CreateStackRequest
from huaweicloudsdkaos.v1.model.create_stack_request_body import CreateStackRequestBody
from huaweicloudsdkaos.v1.model.create_stack_response import CreateStackResponse
from huaweicloudsdkaos.v1.model.create_stack_set_request import CreateStackSetRequest
from huaweicloudsdkaos.v1.model.create_stack_set_request_body import CreateStackSetRequestBody
from huaweicloudsdkaos.v1.model.create_stack_set_response import CreateStackSetResponse
from huaweicloudsdkaos.v1.model.delete_execution_plan_request import DeleteExecutionPlanRequest
from huaweicloudsdkaos.v1.model.delete_execution_plan_response import DeleteExecutionPlanResponse
from huaweicloudsdkaos.v1.model.delete_private_hook_request import DeletePrivateHookRequest
from huaweicloudsdkaos.v1.model.delete_private_hook_response import DeletePrivateHookResponse
from huaweicloudsdkaos.v1.model.delete_private_hook_version_request import DeletePrivateHookVersionRequest
from huaweicloudsdkaos.v1.model.delete_private_hook_version_response import DeletePrivateHookVersionResponse
from huaweicloudsdkaos.v1.model.delete_private_module_request import DeletePrivateModuleRequest
from huaweicloudsdkaos.v1.model.delete_private_module_response import DeletePrivateModuleResponse
from huaweicloudsdkaos.v1.model.delete_private_module_version_request import DeletePrivateModuleVersionRequest
from huaweicloudsdkaos.v1.model.delete_private_module_version_response import DeletePrivateModuleVersionResponse
from huaweicloudsdkaos.v1.model.delete_stack_enhanced_request import DeleteStackEnhancedRequest
from huaweicloudsdkaos.v1.model.delete_stack_enhanced_request_body import DeleteStackEnhancedRequestBody
from huaweicloudsdkaos.v1.model.delete_stack_enhanced_response import DeleteStackEnhancedResponse
from huaweicloudsdkaos.v1.model.delete_stack_instance_deprecated_request import DeleteStackInstanceDeprecatedRequest
from huaweicloudsdkaos.v1.model.delete_stack_instance_deprecated_response import DeleteStackInstanceDeprecatedResponse
from huaweicloudsdkaos.v1.model.delete_stack_instance_request import DeleteStackInstanceRequest
from huaweicloudsdkaos.v1.model.delete_stack_instance_request_body import DeleteStackInstanceRequestBody
from huaweicloudsdkaos.v1.model.delete_stack_instance_response import DeleteStackInstanceResponse
from huaweicloudsdkaos.v1.model.delete_stack_request import DeleteStackRequest
from huaweicloudsdkaos.v1.model.delete_stack_response import DeleteStackResponse
from huaweicloudsdkaos.v1.model.delete_stack_set_request import DeleteStackSetRequest
from huaweicloudsdkaos.v1.model.delete_stack_set_response import DeleteStackSetResponse
from huaweicloudsdkaos.v1.model.delete_template_request import DeleteTemplateRequest
from huaweicloudsdkaos.v1.model.delete_template_response import DeleteTemplateResponse
from huaweicloudsdkaos.v1.model.delete_template_version_request import DeleteTemplateVersionRequest
from huaweicloudsdkaos.v1.model.delete_template_version_response import DeleteTemplateVersionResponse
from huaweicloudsdkaos.v1.model.deploy_stack_request import DeployStackRequest
from huaweicloudsdkaos.v1.model.deploy_stack_request_body import DeployStackRequestBody
from huaweicloudsdkaos.v1.model.deploy_stack_response import DeployStackResponse
from huaweicloudsdkaos.v1.model.deploy_stack_set_request import DeployStackSetRequest
from huaweicloudsdkaos.v1.model.deploy_stack_set_request_body import DeployStackSetRequestBody
from huaweicloudsdkaos.v1.model.deploy_stack_set_response import DeployStackSetResponse
from huaweicloudsdkaos.v1.model.deployment_id_primitive_type_holder import DeploymentIdPrimitiveTypeHolder
from huaweicloudsdkaos.v1.model.deployment_targets import DeploymentTargets
from huaweicloudsdkaos.v1.model.deployment_targets_primitive_type_holder import DeploymentTargetsPrimitiveTypeHolder
from huaweicloudsdkaos.v1.model.domain_id_filter_type_primitive_type_holder import DomainIdFilterTypePrimitiveTypeHolder
from huaweicloudsdkaos.v1.model.domain_ids_primitive_type_holder import DomainIdsPrimitiveTypeHolder
from huaweicloudsdkaos.v1.model.domain_ids_uri_primitive_type_holder import DomainIdsUriPrimitiveTypeHolder
from huaweicloudsdkaos.v1.model.enable_auto_rollback_primitive_type_holder import EnableAutoRollbackPrimitiveTypeHolder
from huaweicloudsdkaos.v1.model.enable_deletion_protection_primitive_type_holder import EnableDeletionProtectionPrimitiveTypeHolder
from huaweicloudsdkaos.v1.model.encryption_structure import EncryptionStructure
from huaweicloudsdkaos.v1.model.estimate_execution_plan_price_request import EstimateExecutionPlanPriceRequest
from huaweicloudsdkaos.v1.model.estimate_execution_plan_price_response import EstimateExecutionPlanPriceResponse
from huaweicloudsdkaos.v1.model.execution_plan import ExecutionPlan
from huaweicloudsdkaos.v1.model.execution_plan_description_primitive_type_holder import ExecutionPlanDescriptionPrimitiveTypeHolder
from huaweicloudsdkaos.v1.model.execution_plan_diff_attribute import ExecutionPlanDiffAttribute
from huaweicloudsdkaos.v1.model.execution_plan_id_primitive_type_holder import ExecutionPlanIdPrimitiveTypeHolder
from huaweicloudsdkaos.v1.model.execution_plan_item import ExecutionPlanItem
from huaweicloudsdkaos.v1.model.execution_plan_name_primitive_type_holder import ExecutionPlanNamePrimitiveTypeHolder
from huaweicloudsdkaos.v1.model.execution_plan_status_message_primitive_type_holder import ExecutionPlanStatusMessagePrimitiveTypeHolder
from huaweicloudsdkaos.v1.model.execution_plan_status_primitive_type_holder import ExecutionPlanStatusPrimitiveTypeHolder
from huaweicloudsdkaos.v1.model.execution_plan_summary import ExecutionPlanSummary
from huaweicloudsdkaos.v1.model.function_graph_urn_primitive_type_holder import FunctionGraphUrnPrimitiveTypeHolder
from huaweicloudsdkaos.v1.model.function_graph_urn_required_primitive_type_holder import FunctionGraphUrnRequiredPrimitiveTypeHolder
from huaweicloudsdkaos.v1.model.get_execution_plan_metadata_request import GetExecutionPlanMetadataRequest
from huaweicloudsdkaos.v1.model.get_execution_plan_metadata_response import GetExecutionPlanMetadataResponse
from huaweicloudsdkaos.v1.model.get_execution_plan_request import GetExecutionPlanRequest
from huaweicloudsdkaos.v1.model.get_execution_plan_response import GetExecutionPlanResponse
from huaweicloudsdkaos.v1.model.get_stack_metadata_request import GetStackMetadataRequest
from huaweicloudsdkaos.v1.model.get_stack_metadata_response import GetStackMetadataResponse
from huaweicloudsdkaos.v1.model.get_stack_template_request import GetStackTemplateRequest
from huaweicloudsdkaos.v1.model.get_stack_template_response import GetStackTemplateResponse
from huaweicloudsdkaos.v1.model.index_primitive_type_holder import IndexPrimitiveTypeHolder
from huaweicloudsdkaos.v1.model.initial_stack_description_primitive_type_holder import InitialStackDescriptionPrimitiveTypeHolder
from huaweicloudsdkaos.v1.model.items_response import ItemsResponse
from huaweicloudsdkaos.v1.model.kms_structure import KmsStructure
from huaweicloudsdkaos.v1.model.list_execution_plans_request import ListExecutionPlansRequest
from huaweicloudsdkaos.v1.model.list_execution_plans_response import ListExecutionPlansResponse
from huaweicloudsdkaos.v1.model.list_private_hooks_request import ListPrivateHooksRequest
from huaweicloudsdkaos.v1.model.list_private_hooks_response import ListPrivateHooksResponse
from huaweicloudsdkaos.v1.model.list_private_module_versions_request import ListPrivateModuleVersionsRequest
from huaweicloudsdkaos.v1.model.list_private_module_versions_response import ListPrivateModuleVersionsResponse
from huaweicloudsdkaos.v1.model.list_private_modules_request import ListPrivateModulesRequest
from huaweicloudsdkaos.v1.model.list_private_modules_response import ListPrivateModulesResponse
from huaweicloudsdkaos.v1.model.list_stack_events_request import ListStackEventsRequest
from huaweicloudsdkaos.v1.model.list_stack_events_response import ListStackEventsResponse
from huaweicloudsdkaos.v1.model.list_stack_instances_request import ListStackInstancesRequest
from huaweicloudsdkaos.v1.model.list_stack_instances_response import ListStackInstancesResponse
from huaweicloudsdkaos.v1.model.list_stack_outputs_request import ListStackOutputsRequest
from huaweicloudsdkaos.v1.model.list_stack_outputs_response import ListStackOutputsResponse
from huaweicloudsdkaos.v1.model.list_stack_resources_request import ListStackResourcesRequest
from huaweicloudsdkaos.v1.model.list_stack_resources_response import ListStackResourcesResponse
from huaweicloudsdkaos.v1.model.list_stack_set_operations_request import ListStackSetOperationsRequest
from huaweicloudsdkaos.v1.model.list_stack_set_operations_response import ListStackSetOperationsResponse
from huaweicloudsdkaos.v1.model.list_stack_sets_request import ListStackSetsRequest
from huaweicloudsdkaos.v1.model.list_stack_sets_response import ListStackSetsResponse
from huaweicloudsdkaos.v1.model.list_stacks_request import ListStacksRequest
from huaweicloudsdkaos.v1.model.list_stacks_response import ListStacksResponse
from huaweicloudsdkaos.v1.model.list_template_versions_request import ListTemplateVersionsRequest
from huaweicloudsdkaos.v1.model.list_template_versions_response import ListTemplateVersionsResponse
from huaweicloudsdkaos.v1.model.list_templates_request import ListTemplatesRequest
from huaweicloudsdkaos.v1.model.list_templates_response import ListTemplatesResponse
from huaweicloudsdkaos.v1.model.managed_agency_name_primitive_type_holder import ManagedAgencyNamePrimitiveTypeHolder
from huaweicloudsdkaos.v1.model.managed_operation import ManagedOperation
from huaweicloudsdkaos.v1.model.managed_operation_type_holder import ManagedOperationTypeHolder
from huaweicloudsdkaos.v1.model.module_uri_primitive_type_holder import ModuleURIPrimitiveTypeHolder
from huaweicloudsdkaos.v1.model.operation_id_primitive_type_holder import OperationIdPrimitiveTypeHolder
from huaweicloudsdkaos.v1.model.operation_preferences import OperationPreferences
from huaweicloudsdkaos.v1.model.operation_preferences_type_holder import OperationPreferencesTypeHolder
from huaweicloudsdkaos.v1.model.organizational_unit_ids_primitive_type_holder import OrganizationalUnitIdsPrimitiveTypeHolder
from huaweicloudsdkaos.v1.model.parse_template_variables_request import ParseTemplateVariablesRequest
from huaweicloudsdkaos.v1.model.parse_template_variables_request_body import ParseTemplateVariablesRequestBody
from huaweicloudsdkaos.v1.model.parse_template_variables_response import ParseTemplateVariablesResponse
from huaweicloudsdkaos.v1.model.permission_model_primitive_type_holder import PermissionModelPrimitiveTypeHolder
from huaweicloudsdkaos.v1.model.private_hook_create_time_primitive_type_holder import PrivateHookCreateTimePrimitiveTypeHolder
from huaweicloudsdkaos.v1.model.private_hook_default_version_primitive_type_holder import PrivateHookDefaultVersionPrimitiveTypeHolder
from huaweicloudsdkaos.v1.model.private_hook_description_primitive_type_holder import PrivateHookDescriptionPrimitiveTypeHolder
from huaweicloudsdkaos.v1.model.private_hook_id_primitive_type_holder import PrivateHookIdPrimitiveTypeHolder
from huaweicloudsdkaos.v1.model.private_hook_name_primitive_type_holder import PrivateHookNamePrimitiveTypeHolder
from huaweicloudsdkaos.v1.model.private_hook_summary import PrivateHookSummary
from huaweicloudsdkaos.v1.model.private_hook_update_time_primitive_type_holder import PrivateHookUpdateTimePrimitiveTypeHolder
from huaweicloudsdkaos.v1.model.private_hook_version_create_time_primitive_type_holder import PrivateHookVersionCreateTimePrimitiveTypeHolder
from huaweicloudsdkaos.v1.model.private_hook_version_description_primitive_type_holder import PrivateHookVersionDescriptionPrimitiveTypeHolder
from huaweicloudsdkaos.v1.model.private_hook_version_primitive_type_holder import PrivateHookVersionPrimitiveTypeHolder
from huaweicloudsdkaos.v1.model.private_hook_version_summary import PrivateHookVersionSummary
from huaweicloudsdkaos.v1.model.private_module import PrivateModule
from huaweicloudsdkaos.v1.model.private_module_create_time_primitive_type_holder import PrivateModuleCreateTimePrimitiveTypeHolder
from huaweicloudsdkaos.v1.model.private_module_description_primitive_type_holder import PrivateModuleDescriptionPrimitiveTypeHolder
from huaweicloudsdkaos.v1.model.private_module_id_primitive_type_holder import PrivateModuleIdPrimitiveTypeHolder
from huaweicloudsdkaos.v1.model.private_module_name_primitive_type_holder import PrivateModuleNamePrimitiveTypeHolder
from huaweicloudsdkaos.v1.model.private_module_source_primitive_type_holder import PrivateModuleSourcePrimitiveTypeHolder
from huaweicloudsdkaos.v1.model.private_module_summary import PrivateModuleSummary
from huaweicloudsdkaos.v1.model.private_module_update_time_primitive_type_holder import PrivateModuleUpdateTimePrimitiveTypeHolder
from huaweicloudsdkaos.v1.model.private_module_version import PrivateModuleVersion
from huaweicloudsdkaos.v1.model.private_module_version_create_time_primitive_type_holder import PrivateModuleVersionCreateTimePrimitiveTypeHolder
from huaweicloudsdkaos.v1.model.private_module_version_description_primitive_type_holder import PrivateModuleVersionDescriptionPrimitiveTypeHolder
from huaweicloudsdkaos.v1.model.private_module_version_primitive_type_holder import PrivateModuleVersionPrimitiveTypeHolder
from huaweicloudsdkaos.v1.model.private_module_version_summary import PrivateModuleVersionSummary
from huaweicloudsdkaos.v1.model.private_policy_body_primitive_type_holder import PrivatePolicyBodyPrimitiveTypeHolder
from huaweicloudsdkaos.v1.model.private_policy_uri_primitive_type_holder import PrivatePolicyURIPrimitiveTypeHolder
from huaweicloudsdkaos.v1.model.private_provider_description_primitive_type_holder import PrivateProviderDescriptionPrimitiveTypeHolder
from huaweicloudsdkaos.v1.model.private_provider_id_primitive_type_holder import PrivateProviderIdPrimitiveTypeHolder
from huaweicloudsdkaos.v1.model.private_provider_name_primitive_type_holder import PrivateProviderNamePrimitiveTypeHolder
from huaweicloudsdkaos.v1.model.private_provider_source_primitive_type_holder import PrivateProviderSourcePrimitiveTypeHolder
from huaweicloudsdkaos.v1.model.private_provider_version_description_primitive_type_holder import PrivateProviderVersionDescriptionPrimitiveTypeHolder
from huaweicloudsdkaos.v1.model.private_provider_version_primitive_type_holder import PrivateProviderVersionPrimitiveTypeHolder
from huaweicloudsdkaos.v1.model.private_provider_version_required_primitive_type_holder import PrivateProviderVersionRequiredPrimitiveTypeHolder
from huaweicloudsdkaos.v1.model.regions_primitive_type_holder import RegionsPrimitiveTypeHolder
from huaweicloudsdkaos.v1.model.resource_attribute import ResourceAttribute
from huaweicloudsdkaos.v1.model.resource_name_primitive_type_holder import ResourceNamePrimitiveTypeHolder
from huaweicloudsdkaos.v1.model.resource_price_response import ResourcePriceResponse
from huaweicloudsdkaos.v1.model.resource_type_primitive_type_holder import ResourceTypePrimitiveTypeHolder
from huaweicloudsdkaos.v1.model.retain_all_resources_type_holder import RetainAllResourcesTypeHolder
from huaweicloudsdkaos.v1.model.show_private_hook_metadata_request import ShowPrivateHookMetadataRequest
from huaweicloudsdkaos.v1.model.show_private_hook_metadata_response import ShowPrivateHookMetadataResponse
from huaweicloudsdkaos.v1.model.show_private_hook_version_metadata_request import ShowPrivateHookVersionMetadataRequest
from huaweicloudsdkaos.v1.model.show_private_hook_version_metadata_response import ShowPrivateHookVersionMetadataResponse
from huaweicloudsdkaos.v1.model.show_private_hook_version_policy_request import ShowPrivateHookVersionPolicyRequest
from huaweicloudsdkaos.v1.model.show_private_hook_version_policy_response import ShowPrivateHookVersionPolicyResponse
from huaweicloudsdkaos.v1.model.show_private_module_metadata_request import ShowPrivateModuleMetadataRequest
from huaweicloudsdkaos.v1.model.show_private_module_metadata_response import ShowPrivateModuleMetadataResponse
from huaweicloudsdkaos.v1.model.show_private_module_version_content_request import ShowPrivateModuleVersionContentRequest
from huaweicloudsdkaos.v1.model.show_private_module_version_content_response import ShowPrivateModuleVersionContentResponse
from huaweicloudsdkaos.v1.model.show_private_module_version_metadata_request import ShowPrivateModuleVersionMetadataRequest
from huaweicloudsdkaos.v1.model.show_private_module_version_metadata_response import ShowPrivateModuleVersionMetadataResponse
from huaweicloudsdkaos.v1.model.show_stack_instance_request import ShowStackInstanceRequest
from huaweicloudsdkaos.v1.model.show_stack_instance_response import ShowStackInstanceResponse
from huaweicloudsdkaos.v1.model.show_stack_set_metadata_request import ShowStackSetMetadataRequest
from huaweicloudsdkaos.v1.model.show_stack_set_metadata_response import ShowStackSetMetadataResponse
from huaweicloudsdkaos.v1.model.show_stack_set_operation_metadata_request import ShowStackSetOperationMetadataRequest
from huaweicloudsdkaos.v1.model.show_stack_set_operation_metadata_response import ShowStackSetOperationMetadataResponse
from huaweicloudsdkaos.v1.model.show_stack_set_template_request import ShowStackSetTemplateRequest
from huaweicloudsdkaos.v1.model.show_stack_set_template_response import ShowStackSetTemplateResponse
from huaweicloudsdkaos.v1.model.show_template_metadata_request import ShowTemplateMetadataRequest
from huaweicloudsdkaos.v1.model.show_template_metadata_response import ShowTemplateMetadataResponse
from huaweicloudsdkaos.v1.model.show_template_version_content_request import ShowTemplateVersionContentRequest
from huaweicloudsdkaos.v1.model.show_template_version_content_response import ShowTemplateVersionContentResponse
from huaweicloudsdkaos.v1.model.show_template_version_metadata_request import ShowTemplateVersionMetadataRequest
from huaweicloudsdkaos.v1.model.show_template_version_metadata_response import ShowTemplateVersionMetadataResponse
from huaweicloudsdkaos.v1.model.stack import Stack
from huaweicloudsdkaos.v1.model.stack_description_primitive_type_holder import StackDescriptionPrimitiveTypeHolder
from huaweicloudsdkaos.v1.model.stack_event import StackEvent
from huaweicloudsdkaos.v1.model.stack_id_primitive_type_holder import StackIdPrimitiveTypeHolder
from huaweicloudsdkaos.v1.model.stack_instance import StackInstance
from huaweicloudsdkaos.v1.model.stack_instance_status_message_primitive_type_holder import StackInstanceStatusMessagePrimitiveTypeHolder
from huaweicloudsdkaos.v1.model.stack_instance_status_primitive_type_holder import StackInstanceStatusPrimitiveTypeHolder
from huaweicloudsdkaos.v1.model.stack_name_primitive_type_holder import StackNamePrimitiveTypeHolder
from huaweicloudsdkaos.v1.model.stack_output import StackOutput
from huaweicloudsdkaos.v1.model.stack_resource import StackResource
from huaweicloudsdkaos.v1.model.stack_set import StackSet
from huaweicloudsdkaos.v1.model.stack_set_create_time_primitive_type_holder import StackSetCreateTimePrimitiveTypeHolder
from huaweicloudsdkaos.v1.model.stack_set_description_primitive_type_holder import StackSetDescriptionPrimitiveTypeHolder
from huaweicloudsdkaos.v1.model.stack_set_id_primitive_type_holder import StackSetIdPrimitiveTypeHolder
from huaweicloudsdkaos.v1.model.stack_set_name_primitive_type_holder import StackSetNamePrimitiveTypeHolder
from huaweicloudsdkaos.v1.model.stack_set_operation import StackSetOperation
from huaweicloudsdkaos.v1.model.stack_set_operation_action_primitive_type_holder import StackSetOperationActionPrimitiveTypeHolder
from huaweicloudsdkaos.v1.model.stack_set_operation_create_time_primitive_type_holder import StackSetOperationCreateTimePrimitiveTypeHolder
from huaweicloudsdkaos.v1.model.stack_set_operation_id_primitive_type_holder import StackSetOperationIdPrimitiveTypeHolder
from huaweicloudsdkaos.v1.model.stack_set_operation_status_message_primitive_type_holder import StackSetOperationStatusMessagePrimitiveTypeHolder
from huaweicloudsdkaos.v1.model.stack_set_operation_status_primitive_type_holder import StackSetOperationStatusPrimitiveTypeHolder
from huaweicloudsdkaos.v1.model.stack_set_operation_update_time_primitive_type_holder import StackSetOperationUpdateTimePrimitiveTypeHolder
from huaweicloudsdkaos.v1.model.stack_set_stack_name_primitive_type_holder import StackSetStackNamePrimitiveTypeHolder
from huaweicloudsdkaos.v1.model.stack_set_status_primitive_type_holder import StackSetStatusPrimitiveTypeHolder
from huaweicloudsdkaos.v1.model.stack_set_update_time_primitive_type_holder import StackSetUpdateTimePrimitiveTypeHolder
from huaweicloudsdkaos.v1.model.stack_set_vars_uri_content_primitive_type_holder import StackSetVarsURIContentPrimitiveTypeHolder
from huaweicloudsdkaos.v1.model.stack_status_message_primitive_type_holder import StackStatusMessagePrimitiveTypeHolder
from huaweicloudsdkaos.v1.model.stack_status_primitive_type_holder import StackStatusPrimitiveTypeHolder
from huaweicloudsdkaos.v1.model.template import Template
from huaweicloudsdkaos.v1.model.template_body_primitive_type_holder import TemplateBodyPrimitiveTypeHolder
from huaweicloudsdkaos.v1.model.template_uri_primitive_type_holder import TemplateURIPrimitiveTypeHolder
from huaweicloudsdkaos.v1.model.template_version import TemplateVersion
from huaweicloudsdkaos.v1.model.update_private_hook_metadata_request import UpdatePrivateHookMetadataRequest
from huaweicloudsdkaos.v1.model.update_private_hook_metadata_request_body import UpdatePrivateHookMetadataRequestBody
from huaweicloudsdkaos.v1.model.update_private_hook_metadata_response import UpdatePrivateHookMetadataResponse
from huaweicloudsdkaos.v1.model.update_private_module_metadata_request import UpdatePrivateModuleMetadataRequest
from huaweicloudsdkaos.v1.model.update_private_module_metadata_request_body import UpdatePrivateModuleMetadataRequestBody
from huaweicloudsdkaos.v1.model.update_private_module_metadata_response import UpdatePrivateModuleMetadataResponse
from huaweicloudsdkaos.v1.model.update_stack_instances_request import UpdateStackInstancesRequest
from huaweicloudsdkaos.v1.model.update_stack_instances_request_body import UpdateStackInstancesRequestBody
from huaweicloudsdkaos.v1.model.update_stack_instances_response import UpdateStackInstancesResponse
from huaweicloudsdkaos.v1.model.update_stack_request import UpdateStackRequest
from huaweicloudsdkaos.v1.model.update_stack_request_body import UpdateStackRequestBody
from huaweicloudsdkaos.v1.model.update_stack_response import UpdateStackResponse
from huaweicloudsdkaos.v1.model.update_stack_set_request import UpdateStackSetRequest
from huaweicloudsdkaos.v1.model.update_stack_set_request_body import UpdateStackSetRequestBody
from huaweicloudsdkaos.v1.model.update_stack_set_response import UpdateStackSetResponse
from huaweicloudsdkaos.v1.model.update_template_metadata_request import UpdateTemplateMetadataRequest
from huaweicloudsdkaos.v1.model.update_template_metadata_request_body import UpdateTemplateMetadataRequestBody
from huaweicloudsdkaos.v1.model.update_template_metadata_response import UpdateTemplateMetadataResponse
from huaweicloudsdkaos.v1.model.var_overrides_primitive_type_holder import VarOverridesPrimitiveTypeHolder
from huaweicloudsdkaos.v1.model.var_overrides_primitive_type_holder_var_overrides import VarOverridesPrimitiveTypeHolderVarOverrides
from huaweicloudsdkaos.v1.model.variable_response import VariableResponse
from huaweicloudsdkaos.v1.model.variable_validation_response import VariableValidationResponse
from huaweicloudsdkaos.v1.model.vars_body_primitive_type_holder import VarsBodyPrimitiveTypeHolder
from huaweicloudsdkaos.v1.model.vars_structure import VarsStructure
from huaweicloudsdkaos.v1.model.vars_structure_primitive_type_holder import VarsStructurePrimitiveTypeHolder
from huaweicloudsdkaos.v1.model.vars_uri_primitive_type_holder import VarsURIPrimitiveTypeHolder
from huaweicloudsdkaos.v1.model.vars_uri_content_primitive_type_holder import VarsUriContentPrimitiveTypeHolder
from huaweicloudsdkaos.v1.model.void_body import VoidBody


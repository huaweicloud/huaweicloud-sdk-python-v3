# coding: utf-8

from __future__ import absolute_import

# import models into model package
from huaweicloudsdkconfig.v1.model.account_aggregation_source import AccountAggregationSource
from huaweicloudsdkconfig.v1.model.aggregate_compliance_detail_request import AggregateComplianceDetailRequest
from huaweicloudsdkconfig.v1.model.aggregate_discovered_resource_counts_request import AggregateDiscoveredResourceCountsRequest
from huaweicloudsdkconfig.v1.model.aggregate_discovered_resources_request import AggregateDiscoveredResourcesRequest
from huaweicloudsdkconfig.v1.model.aggregate_policy_assignment_detail_request import AggregatePolicyAssignmentDetailRequest
from huaweicloudsdkconfig.v1.model.aggregate_policy_assignments import AggregatePolicyAssignments
from huaweicloudsdkconfig.v1.model.aggregate_policy_assignments_filters import AggregatePolicyAssignmentsFilters
from huaweicloudsdkconfig.v1.model.aggregate_policy_assignments_request import AggregatePolicyAssignmentsRequest
from huaweicloudsdkconfig.v1.model.aggregate_policy_compliance_summary_result import AggregatePolicyComplianceSummaryResult
from huaweicloudsdkconfig.v1.model.aggregate_policy_states_request import AggregatePolicyStatesRequest
from huaweicloudsdkconfig.v1.model.aggregate_resource_config_request import AggregateResourceConfigRequest
from huaweicloudsdkconfig.v1.model.aggregated_source_status import AggregatedSourceStatus
from huaweicloudsdkconfig.v1.model.aggregation_authorization_request import AggregationAuthorizationRequest
from huaweicloudsdkconfig.v1.model.aggregation_authorization_resp import AggregationAuthorizationResp
from huaweicloudsdkconfig.v1.model.channel_config_body import ChannelConfigBody
from huaweicloudsdkconfig.v1.model.collect_all_resources_summary_request import CollectAllResourcesSummaryRequest
from huaweicloudsdkconfig.v1.model.collect_all_resources_summary_response import CollectAllResourcesSummaryResponse
from huaweicloudsdkconfig.v1.model.collect_conformance_pack_compliance_summary_request import CollectConformancePackComplianceSummaryRequest
from huaweicloudsdkconfig.v1.model.collect_conformance_pack_compliance_summary_response import CollectConformancePackComplianceSummaryResponse
from huaweicloudsdkconfig.v1.model.compliance import Compliance
from huaweicloudsdkconfig.v1.model.configuration_aggregator_request import ConfigurationAggregatorRequest
from huaweicloudsdkconfig.v1.model.configuration_aggregator_resp import ConfigurationAggregatorResp
from huaweicloudsdkconfig.v1.model.conformance_pack import ConformancePack
from huaweicloudsdkconfig.v1.model.conformance_pack_compliance import ConformancePackCompliance
from huaweicloudsdkconfig.v1.model.conformance_pack_compliance_detail import ConformancePackComplianceDetail
from huaweicloudsdkconfig.v1.model.conformance_pack_compliance_summary import ConformancePackComplianceSummary
from huaweicloudsdkconfig.v1.model.conformance_pack_request_body import ConformancePackRequestBody
from huaweicloudsdkconfig.v1.model.conformance_pack_score import ConformancePackScore
from huaweicloudsdkconfig.v1.model.conformance_pack_template import ConformancePackTemplate
from huaweicloudsdkconfig.v1.model.count_all_resources_request import CountAllResourcesRequest
from huaweicloudsdkconfig.v1.model.count_all_resources_response import CountAllResourcesResponse
from huaweicloudsdkconfig.v1.model.create_aggregation_authorization_request import CreateAggregationAuthorizationRequest
from huaweicloudsdkconfig.v1.model.create_aggregation_authorization_response import CreateAggregationAuthorizationResponse
from huaweicloudsdkconfig.v1.model.create_configuration_aggregator_request import CreateConfigurationAggregatorRequest
from huaweicloudsdkconfig.v1.model.create_configuration_aggregator_response import CreateConfigurationAggregatorResponse
from huaweicloudsdkconfig.v1.model.create_conformance_pack_request import CreateConformancePackRequest
from huaweicloudsdkconfig.v1.model.create_conformance_pack_response import CreateConformancePackResponse
from huaweicloudsdkconfig.v1.model.create_organization_policy_assignment_request import CreateOrganizationPolicyAssignmentRequest
from huaweicloudsdkconfig.v1.model.create_organization_policy_assignment_response import CreateOrganizationPolicyAssignmentResponse
from huaweicloudsdkconfig.v1.model.create_policy_assignments_request import CreatePolicyAssignmentsRequest
from huaweicloudsdkconfig.v1.model.create_policy_assignments_response import CreatePolicyAssignmentsResponse
from huaweicloudsdkconfig.v1.model.create_stored_query_request import CreateStoredQueryRequest
from huaweicloudsdkconfig.v1.model.create_stored_query_response import CreateStoredQueryResponse
from huaweicloudsdkconfig.v1.model.create_tracker_config_request import CreateTrackerConfigRequest
from huaweicloudsdkconfig.v1.model.create_tracker_config_response import CreateTrackerConfigResponse
from huaweicloudsdkconfig.v1.model.custom_policy import CustomPolicy
from huaweicloudsdkconfig.v1.model.delete_aggregation_authorization_request import DeleteAggregationAuthorizationRequest
from huaweicloudsdkconfig.v1.model.delete_aggregation_authorization_response import DeleteAggregationAuthorizationResponse
from huaweicloudsdkconfig.v1.model.delete_configuration_aggregator_request import DeleteConfigurationAggregatorRequest
from huaweicloudsdkconfig.v1.model.delete_configuration_aggregator_response import DeleteConfigurationAggregatorResponse
from huaweicloudsdkconfig.v1.model.delete_conformance_pack_request import DeleteConformancePackRequest
from huaweicloudsdkconfig.v1.model.delete_conformance_pack_response import DeleteConformancePackResponse
from huaweicloudsdkconfig.v1.model.delete_organization_policy_assignment_request import DeleteOrganizationPolicyAssignmentRequest
from huaweicloudsdkconfig.v1.model.delete_organization_policy_assignment_response import DeleteOrganizationPolicyAssignmentResponse
from huaweicloudsdkconfig.v1.model.delete_pending_aggregation_request_request import DeletePendingAggregationRequestRequest
from huaweicloudsdkconfig.v1.model.delete_pending_aggregation_request_response import DeletePendingAggregationRequestResponse
from huaweicloudsdkconfig.v1.model.delete_policy_assignment_request import DeletePolicyAssignmentRequest
from huaweicloudsdkconfig.v1.model.delete_policy_assignment_response import DeletePolicyAssignmentResponse
from huaweicloudsdkconfig.v1.model.delete_stored_query_request import DeleteStoredQueryRequest
from huaweicloudsdkconfig.v1.model.delete_stored_query_response import DeleteStoredQueryResponse
from huaweicloudsdkconfig.v1.model.delete_tracker_config_request import DeleteTrackerConfigRequest
from huaweicloudsdkconfig.v1.model.delete_tracker_config_response import DeleteTrackerConfigResponse
from huaweicloudsdkconfig.v1.model.disable_policy_assignment_request import DisablePolicyAssignmentRequest
from huaweicloudsdkconfig.v1.model.disable_policy_assignment_response import DisablePolicyAssignmentResponse
from huaweicloudsdkconfig.v1.model.enable_policy_assignment_request import EnablePolicyAssignmentRequest
from huaweicloudsdkconfig.v1.model.enable_policy_assignment_response import EnablePolicyAssignmentResponse
from huaweicloudsdkconfig.v1.model.grouped_resource_count import GroupedResourceCount
from huaweicloudsdkconfig.v1.model.history_item import HistoryItem
from huaweicloudsdkconfig.v1.model.list_aggregate_compliance_by_policy_assignment_request import ListAggregateComplianceByPolicyAssignmentRequest
from huaweicloudsdkconfig.v1.model.list_aggregate_compliance_by_policy_assignment_response import ListAggregateComplianceByPolicyAssignmentResponse
from huaweicloudsdkconfig.v1.model.list_aggregate_discovered_resources_request import ListAggregateDiscoveredResourcesRequest
from huaweicloudsdkconfig.v1.model.list_aggregate_discovered_resources_response import ListAggregateDiscoveredResourcesResponse
from huaweicloudsdkconfig.v1.model.list_aggregation_authorizations_request import ListAggregationAuthorizationsRequest
from huaweicloudsdkconfig.v1.model.list_aggregation_authorizations_response import ListAggregationAuthorizationsResponse
from huaweicloudsdkconfig.v1.model.list_all_resources_request import ListAllResourcesRequest
from huaweicloudsdkconfig.v1.model.list_all_resources_response import ListAllResourcesResponse
from huaweicloudsdkconfig.v1.model.list_all_tags_request import ListAllTagsRequest
from huaweicloudsdkconfig.v1.model.list_all_tags_response import ListAllTagsResponse
from huaweicloudsdkconfig.v1.model.list_built_in_conformance_pack_templates_request import ListBuiltInConformancePackTemplatesRequest
from huaweicloudsdkconfig.v1.model.list_built_in_conformance_pack_templates_response import ListBuiltInConformancePackTemplatesResponse
from huaweicloudsdkconfig.v1.model.list_built_in_policy_definitions_request import ListBuiltInPolicyDefinitionsRequest
from huaweicloudsdkconfig.v1.model.list_built_in_policy_definitions_response import ListBuiltInPolicyDefinitionsResponse
from huaweicloudsdkconfig.v1.model.list_configuration_aggregators_request import ListConfigurationAggregatorsRequest
from huaweicloudsdkconfig.v1.model.list_configuration_aggregators_response import ListConfigurationAggregatorsResponse
from huaweicloudsdkconfig.v1.model.list_conformance_pack_compliance_by_pack_id_request import ListConformancePackComplianceByPackIdRequest
from huaweicloudsdkconfig.v1.model.list_conformance_pack_compliance_by_pack_id_response import ListConformancePackComplianceByPackIdResponse
from huaweicloudsdkconfig.v1.model.list_conformance_pack_compliance_details_by_pack_id_request import ListConformancePackComplianceDetailsByPackIdRequest
from huaweicloudsdkconfig.v1.model.list_conformance_pack_compliance_details_by_pack_id_response import ListConformancePackComplianceDetailsByPackIdResponse
from huaweicloudsdkconfig.v1.model.list_conformance_pack_compliance_scores_request import ListConformancePackComplianceScoresRequest
from huaweicloudsdkconfig.v1.model.list_conformance_pack_compliance_scores_response import ListConformancePackComplianceScoresResponse
from huaweicloudsdkconfig.v1.model.list_conformance_packs_request import ListConformancePacksRequest
from huaweicloudsdkconfig.v1.model.list_conformance_packs_response import ListConformancePacksResponse
from huaweicloudsdkconfig.v1.model.list_organization_policy_assignments_request import ListOrganizationPolicyAssignmentsRequest
from huaweicloudsdkconfig.v1.model.list_organization_policy_assignments_response import ListOrganizationPolicyAssignmentsResponse
from huaweicloudsdkconfig.v1.model.list_pending_aggregation_requests_request import ListPendingAggregationRequestsRequest
from huaweicloudsdkconfig.v1.model.list_pending_aggregation_requests_response import ListPendingAggregationRequestsResponse
from huaweicloudsdkconfig.v1.model.list_policy_assignments_request import ListPolicyAssignmentsRequest
from huaweicloudsdkconfig.v1.model.list_policy_assignments_response import ListPolicyAssignmentsResponse
from huaweicloudsdkconfig.v1.model.list_policy_states_by_assignment_id_request import ListPolicyStatesByAssignmentIdRequest
from huaweicloudsdkconfig.v1.model.list_policy_states_by_assignment_id_response import ListPolicyStatesByAssignmentIdResponse
from huaweicloudsdkconfig.v1.model.list_policy_states_by_domain_id_request import ListPolicyStatesByDomainIdRequest
from huaweicloudsdkconfig.v1.model.list_policy_states_by_domain_id_response import ListPolicyStatesByDomainIdResponse
from huaweicloudsdkconfig.v1.model.list_policy_states_by_resource_id_request import ListPolicyStatesByResourceIdRequest
from huaweicloudsdkconfig.v1.model.list_policy_states_by_resource_id_response import ListPolicyStatesByResourceIdResponse
from huaweicloudsdkconfig.v1.model.list_providers_request import ListProvidersRequest
from huaweicloudsdkconfig.v1.model.list_providers_response import ListProvidersResponse
from huaweicloudsdkconfig.v1.model.list_regions_request import ListRegionsRequest
from huaweicloudsdkconfig.v1.model.list_regions_response import ListRegionsResponse
from huaweicloudsdkconfig.v1.model.list_resources_request import ListResourcesRequest
from huaweicloudsdkconfig.v1.model.list_resources_response import ListResourcesResponse
from huaweicloudsdkconfig.v1.model.list_schemas_request import ListSchemasRequest
from huaweicloudsdkconfig.v1.model.list_schemas_response import ListSchemasResponse
from huaweicloudsdkconfig.v1.model.list_stored_queries_request import ListStoredQueriesRequest
from huaweicloudsdkconfig.v1.model.list_stored_queries_response import ListStoredQueriesResponse
from huaweicloudsdkconfig.v1.model.managed_policy_assignment_metadata import ManagedPolicyAssignmentMetadata
from huaweicloudsdkconfig.v1.model.organization_policy_assignment_detailed_status_response import OrganizationPolicyAssignmentDetailedStatusResponse
from huaweicloudsdkconfig.v1.model.organization_policy_assignment_request import OrganizationPolicyAssignmentRequest
from huaweicloudsdkconfig.v1.model.organization_policy_assignment_response import OrganizationPolicyAssignmentResponse
from huaweicloudsdkconfig.v1.model.organization_policy_assignment_status_response import OrganizationPolicyAssignmentStatusResponse
from huaweicloudsdkconfig.v1.model.page_info import PageInfo
from huaweicloudsdkconfig.v1.model.pending_aggregation_request import PendingAggregationRequest
from huaweicloudsdkconfig.v1.model.policy_assignment import PolicyAssignment
from huaweicloudsdkconfig.v1.model.policy_assignment_request_body import PolicyAssignmentRequestBody
from huaweicloudsdkconfig.v1.model.policy_compliance_summary_unit import PolicyComplianceSummaryUnit
from huaweicloudsdkconfig.v1.model.policy_definition import PolicyDefinition
from huaweicloudsdkconfig.v1.model.policy_definition_default_resource_types import PolicyDefinitionDefaultResourceTypes
from huaweicloudsdkconfig.v1.model.policy_filter_definition import PolicyFilterDefinition
from huaweicloudsdkconfig.v1.model.policy_parameter_definition import PolicyParameterDefinition
from huaweicloudsdkconfig.v1.model.policy_parameter_value import PolicyParameterValue
from huaweicloudsdkconfig.v1.model.policy_resource import PolicyResource
from huaweicloudsdkconfig.v1.model.policy_state import PolicyState
from huaweicloudsdkconfig.v1.model.policy_state_request_body import PolicyStateRequestBody
from huaweicloudsdkconfig.v1.model.query_info import QueryInfo
from huaweicloudsdkconfig.v1.model.query_run_request_body import QueryRunRequestBody
from huaweicloudsdkconfig.v1.model.region import Region
from huaweicloudsdkconfig.v1.model.resource_counts_filters import ResourceCountsFilters
from huaweicloudsdkconfig.v1.model.resource_entity import ResourceEntity
from huaweicloudsdkconfig.v1.model.resource_identifier import ResourceIdentifier
from huaweicloudsdkconfig.v1.model.resource_provider_response import ResourceProviderResponse
from huaweicloudsdkconfig.v1.model.resource_relation import ResourceRelation
from huaweicloudsdkconfig.v1.model.resource_schema_response import ResourceSchemaResponse
from huaweicloudsdkconfig.v1.model.resource_summary_response_item import ResourceSummaryResponseItem
from huaweicloudsdkconfig.v1.model.resource_summary_response_item_regions import ResourceSummaryResponseItemRegions
from huaweicloudsdkconfig.v1.model.resource_summary_response_item_types import ResourceSummaryResponseItemTypes
from huaweicloudsdkconfig.v1.model.resource_type_response import ResourceTypeResponse
from huaweicloudsdkconfig.v1.model.resources_filters import ResourcesFilters
from huaweicloudsdkconfig.v1.model.run_aggregate_resource_query_request import RunAggregateResourceQueryRequest
from huaweicloudsdkconfig.v1.model.run_aggregate_resource_query_response import RunAggregateResourceQueryResponse
from huaweicloudsdkconfig.v1.model.run_evaluation_by_policy_assignment_id_request import RunEvaluationByPolicyAssignmentIdRequest
from huaweicloudsdkconfig.v1.model.run_evaluation_by_policy_assignment_id_response import RunEvaluationByPolicyAssignmentIdResponse
from huaweicloudsdkconfig.v1.model.run_query_request import RunQueryRequest
from huaweicloudsdkconfig.v1.model.run_query_response import RunQueryResponse
from huaweicloudsdkconfig.v1.model.selector_config_body import SelectorConfigBody
from huaweicloudsdkconfig.v1.model.show_aggregate_compliance_details_by_policy_assignment_request import ShowAggregateComplianceDetailsByPolicyAssignmentRequest
from huaweicloudsdkconfig.v1.model.show_aggregate_compliance_details_by_policy_assignment_response import ShowAggregateComplianceDetailsByPolicyAssignmentResponse
from huaweicloudsdkconfig.v1.model.show_aggregate_discovered_resource_counts_request import ShowAggregateDiscoveredResourceCountsRequest
from huaweicloudsdkconfig.v1.model.show_aggregate_discovered_resource_counts_response import ShowAggregateDiscoveredResourceCountsResponse
from huaweicloudsdkconfig.v1.model.show_aggregate_policy_assignment_detail_request import ShowAggregatePolicyAssignmentDetailRequest
from huaweicloudsdkconfig.v1.model.show_aggregate_policy_assignment_detail_response import ShowAggregatePolicyAssignmentDetailResponse
from huaweicloudsdkconfig.v1.model.show_aggregate_policy_state_compliance_summary_request import ShowAggregatePolicyStateComplianceSummaryRequest
from huaweicloudsdkconfig.v1.model.show_aggregate_policy_state_compliance_summary_response import ShowAggregatePolicyStateComplianceSummaryResponse
from huaweicloudsdkconfig.v1.model.show_aggregate_resource_config_request import ShowAggregateResourceConfigRequest
from huaweicloudsdkconfig.v1.model.show_aggregate_resource_config_response import ShowAggregateResourceConfigResponse
from huaweicloudsdkconfig.v1.model.show_built_in_conformance_pack_template_request import ShowBuiltInConformancePackTemplateRequest
from huaweicloudsdkconfig.v1.model.show_built_in_conformance_pack_template_response import ShowBuiltInConformancePackTemplateResponse
from huaweicloudsdkconfig.v1.model.show_built_in_policy_definition_request import ShowBuiltInPolicyDefinitionRequest
from huaweicloudsdkconfig.v1.model.show_built_in_policy_definition_response import ShowBuiltInPolicyDefinitionResponse
from huaweicloudsdkconfig.v1.model.show_configuration_aggregator_request import ShowConfigurationAggregatorRequest
from huaweicloudsdkconfig.v1.model.show_configuration_aggregator_response import ShowConfigurationAggregatorResponse
from huaweicloudsdkconfig.v1.model.show_configuration_aggregator_sources_status_request import ShowConfigurationAggregatorSourcesStatusRequest
from huaweicloudsdkconfig.v1.model.show_configuration_aggregator_sources_status_response import ShowConfigurationAggregatorSourcesStatusResponse
from huaweicloudsdkconfig.v1.model.show_conformance_pack_request import ShowConformancePackRequest
from huaweicloudsdkconfig.v1.model.show_conformance_pack_response import ShowConformancePackResponse
from huaweicloudsdkconfig.v1.model.show_evaluation_state_by_assignment_id_request import ShowEvaluationStateByAssignmentIdRequest
from huaweicloudsdkconfig.v1.model.show_evaluation_state_by_assignment_id_response import ShowEvaluationStateByAssignmentIdResponse
from huaweicloudsdkconfig.v1.model.show_organization_policy_assignment_detailed_status_request import ShowOrganizationPolicyAssignmentDetailedStatusRequest
from huaweicloudsdkconfig.v1.model.show_organization_policy_assignment_detailed_status_response import ShowOrganizationPolicyAssignmentDetailedStatusResponse
from huaweicloudsdkconfig.v1.model.show_organization_policy_assignment_request import ShowOrganizationPolicyAssignmentRequest
from huaweicloudsdkconfig.v1.model.show_organization_policy_assignment_response import ShowOrganizationPolicyAssignmentResponse
from huaweicloudsdkconfig.v1.model.show_organization_policy_assignment_statuses_request import ShowOrganizationPolicyAssignmentStatusesRequest
from huaweicloudsdkconfig.v1.model.show_organization_policy_assignment_statuses_response import ShowOrganizationPolicyAssignmentStatusesResponse
from huaweicloudsdkconfig.v1.model.show_policy_assignment_request import ShowPolicyAssignmentRequest
from huaweicloudsdkconfig.v1.model.show_policy_assignment_response import ShowPolicyAssignmentResponse
from huaweicloudsdkconfig.v1.model.show_resource_by_id_request import ShowResourceByIdRequest
from huaweicloudsdkconfig.v1.model.show_resource_by_id_response import ShowResourceByIdResponse
from huaweicloudsdkconfig.v1.model.show_resource_detail_request import ShowResourceDetailRequest
from huaweicloudsdkconfig.v1.model.show_resource_detail_response import ShowResourceDetailResponse
from huaweicloudsdkconfig.v1.model.show_resource_history_request import ShowResourceHistoryRequest
from huaweicloudsdkconfig.v1.model.show_resource_history_response import ShowResourceHistoryResponse
from huaweicloudsdkconfig.v1.model.show_resource_relations_detail_request import ShowResourceRelationsDetailRequest
from huaweicloudsdkconfig.v1.model.show_resource_relations_detail_response import ShowResourceRelationsDetailResponse
from huaweicloudsdkconfig.v1.model.show_resource_relations_request import ShowResourceRelationsRequest
from huaweicloudsdkconfig.v1.model.show_resource_relations_response import ShowResourceRelationsResponse
from huaweicloudsdkconfig.v1.model.show_stored_query_request import ShowStoredQueryRequest
from huaweicloudsdkconfig.v1.model.show_stored_query_response import ShowStoredQueryResponse
from huaweicloudsdkconfig.v1.model.show_tracker_config_request import ShowTrackerConfigRequest
from huaweicloudsdkconfig.v1.model.show_tracker_config_response import ShowTrackerConfigResponse
from huaweicloudsdkconfig.v1.model.stored_query import StoredQuery
from huaweicloudsdkconfig.v1.model.stored_query_request_body import StoredQueryRequestBody
from huaweicloudsdkconfig.v1.model.tag_detail import TagDetail
from huaweicloudsdkconfig.v1.model.template_parameter_definition import TemplateParameterDefinition
from huaweicloudsdkconfig.v1.model.tracker_config_body import TrackerConfigBody
from huaweicloudsdkconfig.v1.model.tracker_obs_channel_config_body import TrackerOBSChannelConfigBody
from huaweicloudsdkconfig.v1.model.tracker_smn_channel_config_body import TrackerSMNChannelConfigBody
from huaweicloudsdkconfig.v1.model.update_configuration_aggregator_request import UpdateConfigurationAggregatorRequest
from huaweicloudsdkconfig.v1.model.update_configuration_aggregator_response import UpdateConfigurationAggregatorResponse
from huaweicloudsdkconfig.v1.model.update_policy_assignment_request import UpdatePolicyAssignmentRequest
from huaweicloudsdkconfig.v1.model.update_policy_assignment_response import UpdatePolicyAssignmentResponse
from huaweicloudsdkconfig.v1.model.update_policy_state_request import UpdatePolicyStateRequest
from huaweicloudsdkconfig.v1.model.update_policy_state_response import UpdatePolicyStateResponse
from huaweicloudsdkconfig.v1.model.update_stored_query_request import UpdateStoredQueryRequest
from huaweicloudsdkconfig.v1.model.update_stored_query_response import UpdateStoredQueryResponse
from huaweicloudsdkconfig.v1.model.vars_structure import VarsStructure

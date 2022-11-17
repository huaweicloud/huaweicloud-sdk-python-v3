# coding: utf-8

from __future__ import absolute_import

# import SdrsClient
from huaweicloudsdksdrs.v1.sdrs_client import SdrsClient
from huaweicloudsdksdrs.v1.sdrs_async_client import SdrsAsyncClient
# import models into sdk package
from huaweicloudsdksdrs.v1.model.add_protected_instance_nic_request import AddProtectedInstanceNicRequest
from huaweicloudsdksdrs.v1.model.add_protected_instance_nic_response import AddProtectedInstanceNicResponse
from huaweicloudsdksdrs.v1.model.add_protected_instance_tags_request import AddProtectedInstanceTagsRequest
from huaweicloudsdksdrs.v1.model.add_protected_instance_tags_response import AddProtectedInstanceTagsResponse
from huaweicloudsdksdrs.v1.model.attach_protected_instance_replication_request import AttachProtectedInstanceReplicationRequest
from huaweicloudsdksdrs.v1.model.attach_protected_instance_replication_response import AttachProtectedInstanceReplicationResponse
from huaweicloudsdksdrs.v1.model.batch_add_tags_request import BatchAddTagsRequest
from huaweicloudsdksdrs.v1.model.batch_add_tags_request_body import BatchAddTagsRequestBody
from huaweicloudsdksdrs.v1.model.batch_add_tags_response import BatchAddTagsResponse
from huaweicloudsdksdrs.v1.model.batch_create_protected_instances_request import BatchCreateProtectedInstancesRequest
from huaweicloudsdksdrs.v1.model.batch_create_protected_instances_request_body import BatchCreateProtectedInstancesRequestBody
from huaweicloudsdksdrs.v1.model.batch_create_protected_instances_request_params import BatchCreateProtectedInstancesRequestParams
from huaweicloudsdksdrs.v1.model.batch_create_protected_instances_response import BatchCreateProtectedInstancesResponse
from huaweicloudsdksdrs.v1.model.batch_delete_protected_instances_request import BatchDeleteProtectedInstancesRequest
from huaweicloudsdksdrs.v1.model.batch_delete_protected_instances_request_body import BatchDeleteProtectedInstancesRequestBody
from huaweicloudsdksdrs.v1.model.batch_delete_protected_instances_response import BatchDeleteProtectedInstancesResponse
from huaweicloudsdksdrs.v1.model.batch_delete_tags_request import BatchDeleteTagsRequest
from huaweicloudsdksdrs.v1.model.batch_delete_tags_request_body import BatchDeleteTagsRequestBody
from huaweicloudsdksdrs.v1.model.batch_delete_tags_response import BatchDeleteTagsResponse
from huaweicloudsdksdrs.v1.model.create_disaster_recovery_drill_request import CreateDisasterRecoveryDrillRequest
from huaweicloudsdksdrs.v1.model.create_disaster_recovery_drill_request_body import CreateDisasterRecoveryDrillRequestBody
from huaweicloudsdksdrs.v1.model.create_disaster_recovery_drill_request_params import CreateDisasterRecoveryDrillRequestParams
from huaweicloudsdksdrs.v1.model.create_disaster_recovery_drill_response import CreateDisasterRecoveryDrillResponse
from huaweicloudsdksdrs.v1.model.create_protected_instance_request import CreateProtectedInstanceRequest
from huaweicloudsdksdrs.v1.model.create_protected_instance_request_body import CreateProtectedInstanceRequestBody
from huaweicloudsdksdrs.v1.model.create_protected_instance_request_params import CreateProtectedInstanceRequestParams
from huaweicloudsdksdrs.v1.model.create_protected_instance_response import CreateProtectedInstanceResponse
from huaweicloudsdksdrs.v1.model.create_protection_group_request import CreateProtectionGroupRequest
from huaweicloudsdksdrs.v1.model.create_protection_group_request_body import CreateProtectionGroupRequestBody
from huaweicloudsdksdrs.v1.model.create_protection_group_request_params import CreateProtectionGroupRequestParams
from huaweicloudsdksdrs.v1.model.create_protection_group_response import CreateProtectionGroupResponse
from huaweicloudsdksdrs.v1.model.create_replication_request import CreateReplicationRequest
from huaweicloudsdksdrs.v1.model.create_replication_request_body import CreateReplicationRequestBody
from huaweicloudsdksdrs.v1.model.create_replication_request_params import CreateReplicationRequestParams
from huaweicloudsdksdrs.v1.model.create_replication_response import CreateReplicationResponse
from huaweicloudsdksdrs.v1.model.delete_all_server_group_failure_jobs_request import DeleteAllServerGroupFailureJobsRequest
from huaweicloudsdksdrs.v1.model.delete_all_server_group_failure_jobs_response import DeleteAllServerGroupFailureJobsResponse
from huaweicloudsdksdrs.v1.model.delete_disaster_recovery_drill_request import DeleteDisasterRecoveryDrillRequest
from huaweicloudsdksdrs.v1.model.delete_disaster_recovery_drill_response import DeleteDisasterRecoveryDrillResponse
from huaweicloudsdksdrs.v1.model.delete_failure_job_request import DeleteFailureJobRequest
from huaweicloudsdksdrs.v1.model.delete_failure_job_response import DeleteFailureJobResponse
from huaweicloudsdksdrs.v1.model.delete_protected_instance_nic_request import DeleteProtectedInstanceNicRequest
from huaweicloudsdksdrs.v1.model.delete_protected_instance_nic_response import DeleteProtectedInstanceNicResponse
from huaweicloudsdksdrs.v1.model.delete_protected_instance_request import DeleteProtectedInstanceRequest
from huaweicloudsdksdrs.v1.model.delete_protected_instance_request_body import DeleteProtectedInstanceRequestBody
from huaweicloudsdksdrs.v1.model.delete_protected_instance_response import DeleteProtectedInstanceResponse
from huaweicloudsdksdrs.v1.model.delete_protected_instance_tag_request import DeleteProtectedInstanceTagRequest
from huaweicloudsdksdrs.v1.model.delete_protected_instance_tag_response import DeleteProtectedInstanceTagResponse
from huaweicloudsdksdrs.v1.model.delete_protection_group_request import DeleteProtectionGroupRequest
from huaweicloudsdksdrs.v1.model.delete_protection_group_response import DeleteProtectionGroupResponse
from huaweicloudsdksdrs.v1.model.delete_replication_request import DeleteReplicationRequest
from huaweicloudsdksdrs.v1.model.delete_replication_request_body import DeleteReplicationRequestBody
from huaweicloudsdksdrs.v1.model.delete_replication_request_params import DeleteReplicationRequestParams
from huaweicloudsdksdrs.v1.model.delete_replication_response import DeleteReplicationResponse
from huaweicloudsdksdrs.v1.model.delete_resource_tag import DeleteResourceTag
from huaweicloudsdksdrs.v1.model.delete_server_group_failure_jobs_request import DeleteServerGroupFailureJobsRequest
from huaweicloudsdksdrs.v1.model.delete_server_group_failure_jobs_response import DeleteServerGroupFailureJobsResponse
from huaweicloudsdksdrs.v1.model.detach_protected_instance_replication_request import DetachProtectedInstanceReplicationRequest
from huaweicloudsdksdrs.v1.model.detach_protected_instance_replication_response import DetachProtectedInstanceReplicationResponse
from huaweicloudsdksdrs.v1.model.drill_server_params import DrillServerParams
from huaweicloudsdksdrs.v1.model.expand_replication_request import ExpandReplicationRequest
from huaweicloudsdksdrs.v1.model.expand_replication_response import ExpandReplicationResponse
from huaweicloudsdksdrs.v1.model.extend_replication_request_body import ExtendReplicationRequestBody
from huaweicloudsdksdrs.v1.model.extend_replication_request_params import ExtendReplicationRequestParams
from huaweicloudsdksdrs.v1.model.failover_protection_group_request_body import FailoverProtectionGroupRequestBody
from huaweicloudsdksdrs.v1.model.failure_job_params import FailureJobParams
from huaweicloudsdksdrs.v1.model.job_entities import JobEntities
from huaweicloudsdksdrs.v1.model.list_active_active_domains_request import ListActiveActiveDomainsRequest
from huaweicloudsdksdrs.v1.model.list_active_active_domains_response import ListActiveActiveDomainsResponse
from huaweicloudsdksdrs.v1.model.list_api_versions_request import ListApiVersionsRequest
from huaweicloudsdksdrs.v1.model.list_api_versions_response import ListApiVersionsResponse
from huaweicloudsdksdrs.v1.model.list_disaster_recovery_drills_request import ListDisasterRecoveryDrillsRequest
from huaweicloudsdksdrs.v1.model.list_disaster_recovery_drills_response import ListDisasterRecoveryDrillsResponse
from huaweicloudsdksdrs.v1.model.list_failure_jobs_request import ListFailureJobsRequest
from huaweicloudsdksdrs.v1.model.list_failure_jobs_response import ListFailureJobsResponse
from huaweicloudsdksdrs.v1.model.list_protected_instance_tags_request import ListProtectedInstanceTagsRequest
from huaweicloudsdksdrs.v1.model.list_protected_instance_tags_response import ListProtectedInstanceTagsResponse
from huaweicloudsdksdrs.v1.model.list_protected_instances_by_tags_request import ListProtectedInstancesByTagsRequest
from huaweicloudsdksdrs.v1.model.list_protected_instances_by_tags_request_body import ListProtectedInstancesByTagsRequestBody
from huaweicloudsdksdrs.v1.model.list_protected_instances_by_tags_response import ListProtectedInstancesByTagsResponse
from huaweicloudsdksdrs.v1.model.list_protected_instances_project_tags_request import ListProtectedInstancesProjectTagsRequest
from huaweicloudsdksdrs.v1.model.list_protected_instances_project_tags_response import ListProtectedInstancesProjectTagsResponse
from huaweicloudsdksdrs.v1.model.list_protected_instances_request import ListProtectedInstancesRequest
from huaweicloudsdksdrs.v1.model.list_protected_instances_response import ListProtectedInstancesResponse
from huaweicloudsdksdrs.v1.model.list_protection_groups_request import ListProtectionGroupsRequest
from huaweicloudsdksdrs.v1.model.list_protection_groups_response import ListProtectionGroupsResponse
from huaweicloudsdksdrs.v1.model.list_replications_request import ListReplicationsRequest
from huaweicloudsdksdrs.v1.model.list_replications_response import ListReplicationsResponse
from huaweicloudsdksdrs.v1.model.list_rpo_statistics_request import ListRpoStatisticsRequest
from huaweicloudsdksdrs.v1.model.list_rpo_statistics_response import ListRpoStatisticsResponse
from huaweicloudsdksdrs.v1.model.match_params import MatchParams
from huaweicloudsdksdrs.v1.model.metadata_params import MetadataParams
from huaweicloudsdksdrs.v1.model.protected_instance_add_nic_request_body import ProtectedInstanceAddNicRequestBody
from huaweicloudsdksdrs.v1.model.protected_instance_add_tags_request_body import ProtectedInstanceAddTagsRequestBody
from huaweicloudsdksdrs.v1.model.protected_instance_attach_replication_request_body import ProtectedInstanceAttachReplicationRequestBody
from huaweicloudsdksdrs.v1.model.protected_instance_attach_replication_request_params import ProtectedInstanceAttachReplicationRequestParams
from huaweicloudsdksdrs.v1.model.protected_instance_attachment import ProtectedInstanceAttachment
from huaweicloudsdksdrs.v1.model.protected_instance_delete_nic_request_body import ProtectedInstanceDeleteNicRequestBody
from huaweicloudsdksdrs.v1.model.quota_params import QuotaParams
from huaweicloudsdksdrs.v1.model.quota_resource_params import QuotaResourceParams
from huaweicloudsdksdrs.v1.model.replication_attachment import ReplicationAttachment
from huaweicloudsdksdrs.v1.model.replication_cluster_params import ReplicationClusterParams
from huaweicloudsdksdrs.v1.model.replication_record_metadata import ReplicationRecordMetadata
from huaweicloudsdksdrs.v1.model.resize_protected_instance_request import ResizeProtectedInstanceRequest
from huaweicloudsdksdrs.v1.model.resize_protected_instance_request_body import ResizeProtectedInstanceRequestBody
from huaweicloudsdksdrs.v1.model.resize_protected_instance_request_params import ResizeProtectedInstanceRequestParams
from huaweicloudsdksdrs.v1.model.resize_protected_instance_response import ResizeProtectedInstanceResponse
from huaweicloudsdksdrs.v1.model.resource_id import ResourceId
from huaweicloudsdksdrs.v1.model.resource_params import ResourceParams
from huaweicloudsdksdrs.v1.model.resource_tag import ResourceTag
from huaweicloudsdksdrs.v1.model.reverse_protection_group_request_body import ReverseProtectionGroupRequestBody
from huaweicloudsdksdrs.v1.model.reverse_protection_group_request_params import ReverseProtectionGroupRequestParams
from huaweicloudsdksdrs.v1.model.rpo_stattistics_params import RpoStattisticsParams
from huaweicloudsdksdrs.v1.model.security_groups_params import SecurityGroupsParams
from huaweicloudsdksdrs.v1.model.server_info import ServerInfo
from huaweicloudsdksdrs.v1.model.show_active_active_domain_params import ShowActiveActiveDomainParams
from huaweicloudsdksdrs.v1.model.show_api_version_links_params import ShowApiVersionLinksParams
from huaweicloudsdksdrs.v1.model.show_api_version_params import ShowApiVersionParams
from huaweicloudsdksdrs.v1.model.show_disaster_recovery_drill_params import ShowDisasterRecoveryDrillParams
from huaweicloudsdksdrs.v1.model.show_disaster_recovery_drill_request import ShowDisasterRecoveryDrillRequest
from huaweicloudsdksdrs.v1.model.show_disaster_recovery_drill_response import ShowDisasterRecoveryDrillResponse
from huaweicloudsdksdrs.v1.model.show_job_status_request import ShowJobStatusRequest
from huaweicloudsdksdrs.v1.model.show_job_status_response import ShowJobStatusResponse
from huaweicloudsdksdrs.v1.model.show_protected_instance_params import ShowProtectedInstanceParams
from huaweicloudsdksdrs.v1.model.show_protected_instance_request import ShowProtectedInstanceRequest
from huaweicloudsdksdrs.v1.model.show_protected_instance_response import ShowProtectedInstanceResponse
from huaweicloudsdksdrs.v1.model.show_protection_group_params import ShowProtectionGroupParams
from huaweicloudsdksdrs.v1.model.show_protection_group_request import ShowProtectionGroupRequest
from huaweicloudsdksdrs.v1.model.show_protection_group_response import ShowProtectionGroupResponse
from huaweicloudsdksdrs.v1.model.show_quota_request import ShowQuotaRequest
from huaweicloudsdksdrs.v1.model.show_quota_response import ShowQuotaResponse
from huaweicloudsdksdrs.v1.model.show_replication_params import ShowReplicationParams
from huaweicloudsdksdrs.v1.model.show_replication_request import ShowReplicationRequest
from huaweicloudsdksdrs.v1.model.show_replication_response import ShowReplicationResponse
from huaweicloudsdksdrs.v1.model.show_specified_api_version_request import ShowSpecifiedApiVersionRequest
from huaweicloudsdksdrs.v1.model.show_specified_api_version_response import ShowSpecifiedApiVersionResponse
from huaweicloudsdksdrs.v1.model.start_failover_protection_group_request import StartFailoverProtectionGroupRequest
from huaweicloudsdksdrs.v1.model.start_failover_protection_group_response import StartFailoverProtectionGroupResponse
from huaweicloudsdksdrs.v1.model.start_protection_group_request import StartProtectionGroupRequest
from huaweicloudsdksdrs.v1.model.start_protection_group_request_body import StartProtectionGroupRequestBody
from huaweicloudsdksdrs.v1.model.start_protection_group_response import StartProtectionGroupResponse
from huaweicloudsdksdrs.v1.model.start_reverse_protection_group_request import StartReverseProtectionGroupRequest
from huaweicloudsdksdrs.v1.model.start_reverse_protection_group_response import StartReverseProtectionGroupResponse
from huaweicloudsdksdrs.v1.model.stop_protection_group_request import StopProtectionGroupRequest
from huaweicloudsdksdrs.v1.model.stop_protection_group_request_body import StopProtectionGroupRequestBody
from huaweicloudsdksdrs.v1.model.stop_protection_group_response import StopProtectionGroupResponse
from huaweicloudsdksdrs.v1.model.sub_job_entities import SubJobEntities
from huaweicloudsdksdrs.v1.model.sub_job_params import SubJobParams
from huaweicloudsdksdrs.v1.model.tag_params import TagParams
from huaweicloudsdksdrs.v1.model.update_disaster_recovery_drill_name_request import UpdateDisasterRecoveryDrillNameRequest
from huaweicloudsdksdrs.v1.model.update_disaster_recovery_drill_name_request_body import UpdateDisasterRecoveryDrillNameRequestBody
from huaweicloudsdksdrs.v1.model.update_disaster_recovery_drill_name_request_params import UpdateDisasterRecoveryDrillNameRequestParams
from huaweicloudsdksdrs.v1.model.update_disaster_recovery_drill_name_response import UpdateDisasterRecoveryDrillNameResponse
from huaweicloudsdksdrs.v1.model.update_protected_instance_name_request import UpdateProtectedInstanceNameRequest
from huaweicloudsdksdrs.v1.model.update_protected_instance_name_request_body import UpdateProtectedInstanceNameRequestBody
from huaweicloudsdksdrs.v1.model.update_protected_instance_name_request_params import UpdateProtectedInstanceNameRequestParams
from huaweicloudsdksdrs.v1.model.update_protected_instance_name_response import UpdateProtectedInstanceNameResponse
from huaweicloudsdksdrs.v1.model.update_protection_group_name_request import UpdateProtectionGroupNameRequest
from huaweicloudsdksdrs.v1.model.update_protection_group_name_request_body import UpdateProtectionGroupNameRequestBody
from huaweicloudsdksdrs.v1.model.update_protection_group_name_request_params import UpdateProtectionGroupNameRequestParams
from huaweicloudsdksdrs.v1.model.update_protection_group_name_response import UpdateProtectionGroupNameResponse
from huaweicloudsdksdrs.v1.model.update_replication_name_request import UpdateReplicationNameRequest
from huaweicloudsdksdrs.v1.model.update_replication_name_request_body import UpdateReplicationNameRequestBody
from huaweicloudsdksdrs.v1.model.update_replication_name_request_params import UpdateReplicationNameRequestParams
from huaweicloudsdksdrs.v1.model.update_replication_name_response import UpdateReplicationNameResponse


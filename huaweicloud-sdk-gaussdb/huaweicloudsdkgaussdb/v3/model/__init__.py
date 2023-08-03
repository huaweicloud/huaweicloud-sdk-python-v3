# coding: utf-8

from __future__ import absolute_import

# import models into model package
from huaweicloudsdkgaussdb.v3.model.add_database_permission_request import AddDatabasePermissionRequest
from huaweicloudsdkgaussdb.v3.model.add_database_permission_response import AddDatabasePermissionResponse
from huaweicloudsdkgaussdb.v3.model.apply_configuration_request_body import ApplyConfigurationRequestBody
from huaweicloudsdkgaussdb.v3.model.backup import Backup
from huaweicloudsdkgaussdb.v3.model.backup_policy import BackupPolicy
from huaweicloudsdkgaussdb.v3.model.backups import Backups
from huaweicloudsdkgaussdb.v3.model.batch_operate_instance_tag_request_body import BatchOperateInstanceTagRequestBody
from huaweicloudsdkgaussdb.v3.model.batch_tag_action_request import BatchTagActionRequest
from huaweicloudsdkgaussdb.v3.model.batch_tag_action_response import BatchTagActionResponse
from huaweicloudsdkgaussdb.v3.model.cancel_gauss_my_sql_instance_eip_request import CancelGaussMySqlInstanceEipRequest
from huaweicloudsdkgaussdb.v3.model.cancel_gauss_my_sql_instance_eip_response import CancelGaussMySqlInstanceEipResponse
from huaweicloudsdkgaussdb.v3.model.cancel_schedule_task import CancelScheduleTask
from huaweicloudsdkgaussdb.v3.model.cancel_schedule_task_request import CancelScheduleTaskRequest
from huaweicloudsdkgaussdb.v3.model.cancel_schedule_task_response import CancelScheduleTaskResponse
from huaweicloudsdkgaussdb.v3.model.change_gauss_my_sql_instance_specification_request import ChangeGaussMySqlInstanceSpecificationRequest
from huaweicloudsdkgaussdb.v3.model.change_gauss_my_sql_instance_specification_response import ChangeGaussMySqlInstanceSpecificationResponse
from huaweicloudsdkgaussdb.v3.model.change_gauss_my_sql_proxy_specification_request import ChangeGaussMySqlProxySpecificationRequest
from huaweicloudsdkgaussdb.v3.model.change_gauss_my_sql_proxy_specification_response import ChangeGaussMySqlProxySpecificationResponse
from huaweicloudsdkgaussdb.v3.model.close_mysql_proxy_request_body import CloseMysqlProxyRequestBody
from huaweicloudsdkgaussdb.v3.model.configuration_summary import ConfigurationSummary
from huaweicloudsdkgaussdb.v3.model.configuration_summary2 import ConfigurationSummary2
from huaweicloudsdkgaussdb.v3.model.create_configuration_request_body import CreateConfigurationRequestBody
from huaweicloudsdkgaussdb.v3.model.create_database_list import CreateDatabaseList
from huaweicloudsdkgaussdb.v3.model.create_database_user_list import CreateDatabaseUserList
from huaweicloudsdkgaussdb.v3.model.create_database_user_request import CreateDatabaseUserRequest
from huaweicloudsdkgaussdb.v3.model.create_gauss_my_sql_backup_request import CreateGaussMySqlBackupRequest
from huaweicloudsdkgaussdb.v3.model.create_gauss_my_sql_backup_response import CreateGaussMySqlBackupResponse
from huaweicloudsdkgaussdb.v3.model.create_gauss_my_sql_configuration_request import CreateGaussMySqlConfigurationRequest
from huaweicloudsdkgaussdb.v3.model.create_gauss_my_sql_configuration_response import CreateGaussMySqlConfigurationResponse
from huaweicloudsdkgaussdb.v3.model.create_gauss_my_sql_database import CreateGaussMySqlDatabase
from huaweicloudsdkgaussdb.v3.model.create_gauss_my_sql_database_request import CreateGaussMySqlDatabaseRequest
from huaweicloudsdkgaussdb.v3.model.create_gauss_my_sql_database_request_body import CreateGaussMySqlDatabaseRequestBody
from huaweicloudsdkgaussdb.v3.model.create_gauss_my_sql_database_response import CreateGaussMySqlDatabaseResponse
from huaweicloudsdkgaussdb.v3.model.create_gauss_my_sql_database_user_request import CreateGaussMySqlDatabaseUserRequest
from huaweicloudsdkgaussdb.v3.model.create_gauss_my_sql_database_user_response import CreateGaussMySqlDatabaseUserResponse
from huaweicloudsdkgaussdb.v3.model.create_gauss_my_sql_instance_request import CreateGaussMySqlInstanceRequest
from huaweicloudsdkgaussdb.v3.model.create_gauss_my_sql_instance_response import CreateGaussMySqlInstanceResponse
from huaweicloudsdkgaussdb.v3.model.create_gauss_my_sql_proxy_request import CreateGaussMySqlProxyRequest
from huaweicloudsdkgaussdb.v3.model.create_gauss_my_sql_proxy_response import CreateGaussMySqlProxyResponse
from huaweicloudsdkgaussdb.v3.model.create_gauss_my_sql_readonly_node_request import CreateGaussMySqlReadonlyNodeRequest
from huaweicloudsdkgaussdb.v3.model.create_gauss_my_sql_readonly_node_response import CreateGaussMySqlReadonlyNodeResponse
from huaweicloudsdkgaussdb.v3.model.database_permission import DatabasePermission
from huaweicloudsdkgaussdb.v3.model.datastore_result import DatastoreResult
from huaweicloudsdkgaussdb.v3.model.dedicated_compute_info import DedicatedComputeInfo
from huaweicloudsdkgaussdb.v3.model.dedicated_resource import DedicatedResource
from huaweicloudsdkgaussdb.v3.model.dedicated_resource_capacity import DedicatedResourceCapacity
from huaweicloudsdkgaussdb.v3.model.dedicated_storage_info import DedicatedStorageInfo
from huaweicloudsdkgaussdb.v3.model.delete_database_permission import DeleteDatabasePermission
from huaweicloudsdkgaussdb.v3.model.delete_database_permission_request import DeleteDatabasePermissionRequest
from huaweicloudsdkgaussdb.v3.model.delete_database_permission_request_body import DeleteDatabasePermissionRequestBody
from huaweicloudsdkgaussdb.v3.model.delete_database_permission_response import DeleteDatabasePermissionResponse
from huaweicloudsdkgaussdb.v3.model.delete_database_user_request import DeleteDatabaseUserRequest
from huaweicloudsdkgaussdb.v3.model.delete_gauss_my_sql_backup_request import DeleteGaussMySqlBackupRequest
from huaweicloudsdkgaussdb.v3.model.delete_gauss_my_sql_backup_response import DeleteGaussMySqlBackupResponse
from huaweicloudsdkgaussdb.v3.model.delete_gauss_my_sql_configuration_request import DeleteGaussMySqlConfigurationRequest
from huaweicloudsdkgaussdb.v3.model.delete_gauss_my_sql_configuration_response import DeleteGaussMySqlConfigurationResponse
from huaweicloudsdkgaussdb.v3.model.delete_gauss_my_sql_database_request import DeleteGaussMySqlDatabaseRequest
from huaweicloudsdkgaussdb.v3.model.delete_gauss_my_sql_database_request_body import DeleteGaussMySqlDatabaseRequestBody
from huaweicloudsdkgaussdb.v3.model.delete_gauss_my_sql_database_response import DeleteGaussMySqlDatabaseResponse
from huaweicloudsdkgaussdb.v3.model.delete_gauss_my_sql_database_user_request import DeleteGaussMySqlDatabaseUserRequest
from huaweicloudsdkgaussdb.v3.model.delete_gauss_my_sql_database_user_response import DeleteGaussMySqlDatabaseUserResponse
from huaweicloudsdkgaussdb.v3.model.delete_gauss_my_sql_instance_request import DeleteGaussMySqlInstanceRequest
from huaweicloudsdkgaussdb.v3.model.delete_gauss_my_sql_instance_response import DeleteGaussMySqlInstanceResponse
from huaweicloudsdkgaussdb.v3.model.delete_gauss_my_sql_proxy_request import DeleteGaussMySqlProxyRequest
from huaweicloudsdkgaussdb.v3.model.delete_gauss_my_sql_proxy_response import DeleteGaussMySqlProxyResponse
from huaweicloudsdkgaussdb.v3.model.delete_gauss_my_sql_readonly_node_request import DeleteGaussMySqlReadonlyNodeRequest
from huaweicloudsdkgaussdb.v3.model.delete_gauss_my_sql_readonly_node_response import DeleteGaussMySqlReadonlyNodeResponse
from huaweicloudsdkgaussdb.v3.model.delete_node_sql_filter_rule import DeleteNodeSqlFilterRule
from huaweicloudsdkgaussdb.v3.model.delete_node_sql_filter_rule_info import DeleteNodeSqlFilterRuleInfo
from huaweicloudsdkgaussdb.v3.model.delete_sql_filter_rule_req import DeleteSqlFilterRuleReq
from huaweicloudsdkgaussdb.v3.model.delete_sql_filter_rule_request import DeleteSqlFilterRuleRequest
from huaweicloudsdkgaussdb.v3.model.delete_sql_filter_rule_response import DeleteSqlFilterRuleResponse
from huaweicloudsdkgaussdb.v3.model.delete_task_record_request import DeleteTaskRecordRequest
from huaweicloudsdkgaussdb.v3.model.delete_task_record_response import DeleteTaskRecordResponse
from huaweicloudsdkgaussdb.v3.model.enlarge_proxy_request import EnlargeProxyRequest
from huaweicloudsdkgaussdb.v3.model.expand_gauss_my_sql_instance_volume_request import ExpandGaussMySqlInstanceVolumeRequest
from huaweicloudsdkgaussdb.v3.model.expand_gauss_my_sql_instance_volume_response import ExpandGaussMySqlInstanceVolumeResponse
from huaweicloudsdkgaussdb.v3.model.expand_gauss_my_sql_proxy_request import ExpandGaussMySqlProxyRequest
from huaweicloudsdkgaussdb.v3.model.expand_gauss_my_sql_proxy_response import ExpandGaussMySqlProxyResponse
from huaweicloudsdkgaussdb.v3.model.gauss_my_sql_database_info import GaussMySqlDatabaseInfo
from huaweicloudsdkgaussdb.v3.model.gauss_my_sql_database_user import GaussMySqlDatabaseUser
from huaweicloudsdkgaussdb.v3.model.get_job_entities_info_detail import GetJobEntitiesInfoDetail
from huaweicloudsdkgaussdb.v3.model.get_job_info_detail import GetJobInfoDetail
from huaweicloudsdkgaussdb.v3.model.get_job_instance_info_detail import GetJobInstanceInfoDetail
from huaweicloudsdkgaussdb.v3.model.grant_database_permission import GrantDatabasePermission
from huaweicloudsdkgaussdb.v3.model.grant_database_permission_request_body import GrantDatabasePermissionRequestBody
from huaweicloudsdkgaussdb.v3.model.instance_tag_item import InstanceTagItem
from huaweicloudsdkgaussdb.v3.model.invoke_gauss_my_sql_instance_switch_over_request import InvokeGaussMySqlInstanceSwitchOverRequest
from huaweicloudsdkgaussdb.v3.model.invoke_gauss_my_sql_instance_switch_over_response import InvokeGaussMySqlInstanceSwitchOverResponse
from huaweicloudsdkgaussdb.v3.model.list_delete_database_user_request import ListDeleteDatabaseUserRequest
from huaweicloudsdkgaussdb.v3.model.list_gauss_my_sql_configurations_request import ListGaussMySqlConfigurationsRequest
from huaweicloudsdkgaussdb.v3.model.list_gauss_my_sql_configurations_response import ListGaussMySqlConfigurationsResponse
from huaweicloudsdkgaussdb.v3.model.list_gauss_my_sql_database import ListGaussMySqlDatabase
from huaweicloudsdkgaussdb.v3.model.list_gauss_my_sql_database_charsets_request import ListGaussMySqlDatabaseCharsetsRequest
from huaweicloudsdkgaussdb.v3.model.list_gauss_my_sql_database_charsets_response import ListGaussMySqlDatabaseCharsetsResponse
from huaweicloudsdkgaussdb.v3.model.list_gauss_my_sql_database_request import ListGaussMySqlDatabaseRequest
from huaweicloudsdkgaussdb.v3.model.list_gauss_my_sql_database_response import ListGaussMySqlDatabaseResponse
from huaweicloudsdkgaussdb.v3.model.list_gauss_my_sql_database_user import ListGaussMySqlDatabaseUser
from huaweicloudsdkgaussdb.v3.model.list_gauss_my_sql_database_user_request import ListGaussMySqlDatabaseUserRequest
from huaweicloudsdkgaussdb.v3.model.list_gauss_my_sql_database_user_response import ListGaussMySqlDatabaseUserResponse
from huaweicloudsdkgaussdb.v3.model.list_gauss_my_sql_dedicated_resources_request import ListGaussMySqlDedicatedResourcesRequest
from huaweicloudsdkgaussdb.v3.model.list_gauss_my_sql_dedicated_resources_response import ListGaussMySqlDedicatedResourcesResponse
from huaweicloudsdkgaussdb.v3.model.list_gauss_my_sql_instance_detail_info_request import ListGaussMySqlInstanceDetailInfoRequest
from huaweicloudsdkgaussdb.v3.model.list_gauss_my_sql_instance_detail_info_response import ListGaussMySqlInstanceDetailInfoResponse
from huaweicloudsdkgaussdb.v3.model.list_gauss_my_sql_instances_request import ListGaussMySqlInstancesRequest
from huaweicloudsdkgaussdb.v3.model.list_gauss_my_sql_instances_response import ListGaussMySqlInstancesResponse
from huaweicloudsdkgaussdb.v3.model.list_gauss_mysql_database_info import ListGaussMysqlDatabaseInfo
from huaweicloudsdkgaussdb.v3.model.list_immediate_jobs_request import ListImmediateJobsRequest
from huaweicloudsdkgaussdb.v3.model.list_immediate_jobs_response import ListImmediateJobsResponse
from huaweicloudsdkgaussdb.v3.model.list_instance_tags_request import ListInstanceTagsRequest
from huaweicloudsdkgaussdb.v3.model.list_instance_tags_response import ListInstanceTagsResponse
from huaweicloudsdkgaussdb.v3.model.list_lts_error_log_details_request import ListLtsErrorLogDetailsRequest
from huaweicloudsdkgaussdb.v3.model.list_lts_error_log_details_response import ListLtsErrorLogDetailsResponse
from huaweicloudsdkgaussdb.v3.model.list_lts_slowlog_details_request import ListLtsSlowlogDetailsRequest
from huaweicloudsdkgaussdb.v3.model.list_lts_slowlog_details_response import ListLtsSlowlogDetailsResponse
from huaweicloudsdkgaussdb.v3.model.list_project_tags_request import ListProjectTagsRequest
from huaweicloudsdkgaussdb.v3.model.list_project_tags_response import ListProjectTagsResponse
from huaweicloudsdkgaussdb.v3.model.list_schedule_jobs_request import ListScheduleJobsRequest
from huaweicloudsdkgaussdb.v3.model.list_schedule_jobs_response import ListScheduleJobsResponse
from huaweicloudsdkgaussdb.v3.model.lts_log_error_detail import LtsLogErrorDetail
from huaweicloudsdkgaussdb.v3.model.lts_log_error_query_request import LtsLogErrorQueryRequest
from huaweicloudsdkgaussdb.v3.model.lts_log_slow_detail import LtsLogSlowDetail
from huaweicloudsdkgaussdb.v3.model.lts_log_slow_query_request import LtsLogSlowQueryRequest
from huaweicloudsdkgaussdb.v3.model.modify_alias_request import ModifyAliasRequest
from huaweicloudsdkgaussdb.v3.model.modify_bind_eip_request import ModifyBindEipRequest
from huaweicloudsdkgaussdb.v3.model.modify_gauss_my_sql_proxy_route_mode_request import ModifyGaussMySqlProxyRouteModeRequest
from huaweicloudsdkgaussdb.v3.model.modify_gauss_my_sql_proxy_route_mode_request_body import ModifyGaussMySqlProxyRouteModeRequestBody
from huaweicloudsdkgaussdb.v3.model.modify_gauss_my_sql_proxy_route_mode_response import ModifyGaussMySqlProxyRouteModeResponse
from huaweicloudsdkgaussdb.v3.model.modify_internal_ip_request import ModifyInternalIpRequest
from huaweicloudsdkgaussdb.v3.model.modify_ops_window import ModifyOpsWindow
from huaweicloudsdkgaussdb.v3.model.modify_port_request import ModifyPortRequest
from huaweicloudsdkgaussdb.v3.model.modify_proxy_consist_request import ModifyProxyConsistRequest
from huaweicloudsdkgaussdb.v3.model.modify_proxy_route_weight_readonly_node import ModifyProxyRouteWeightReadonlyNode
from huaweicloudsdkgaussdb.v3.model.modify_proxy_weight_readonly_node import ModifyProxyWeightReadonlyNode
from huaweicloudsdkgaussdb.v3.model.modify_security_group_request import ModifySecurityGroupRequest
from huaweicloudsdkgaussdb.v3.model.mysql_backup_policy import MysqlBackupPolicy
from huaweicloudsdkgaussdb.v3.model.mysql_backup_strategy import MysqlBackupStrategy
from huaweicloudsdkgaussdb.v3.model.mysql_change_specification_request import MysqlChangeSpecificationRequest
from huaweicloudsdkgaussdb.v3.model.mysql_charge_info import MysqlChargeInfo
from huaweicloudsdkgaussdb.v3.model.mysql_create_backup_request import MysqlCreateBackupRequest
from huaweicloudsdkgaussdb.v3.model.mysql_create_readonly_node_request import MysqlCreateReadonlyNodeRequest
from huaweicloudsdkgaussdb.v3.model.mysql_datastore import MysqlDatastore
from huaweicloudsdkgaussdb.v3.model.mysql_datastore_with_kernel_version import MysqlDatastoreWithKernelVersion
from huaweicloudsdkgaussdb.v3.model.mysql_engine_version_info import MysqlEngineVersionInfo
from huaweicloudsdkgaussdb.v3.model.mysql_extend_instance_volume_request import MysqlExtendInstanceVolumeRequest
from huaweicloudsdkgaussdb.v3.model.mysql_flavor_info import MysqlFlavorInfo
from huaweicloudsdkgaussdb.v3.model.mysql_flavors_info import MysqlFlavorsInfo
from huaweicloudsdkgaussdb.v3.model.mysql_instance_charge_info import MysqlInstanceChargeInfo
from huaweicloudsdkgaussdb.v3.model.mysql_instance_info_detail import MysqlInstanceInfoDetail
from huaweicloudsdkgaussdb.v3.model.mysql_instance_list_info import MysqlInstanceListInfo
from huaweicloudsdkgaussdb.v3.model.mysql_instance_node_info import MysqlInstanceNodeInfo
from huaweicloudsdkgaussdb.v3.model.mysql_instance_node_volume_info import MysqlInstanceNodeVolumeInfo
from huaweicloudsdkgaussdb.v3.model.mysql_instance_request import MysqlInstanceRequest
from huaweicloudsdkgaussdb.v3.model.mysql_instance_response import MysqlInstanceResponse
from huaweicloudsdkgaussdb.v3.model.mysql_proxy_available import MysqlProxyAvailable
from huaweicloudsdkgaussdb.v3.model.mysql_proxy_compute_flavor import MysqlProxyComputeFlavor
from huaweicloudsdkgaussdb.v3.model.mysql_proxy_flavor_groups import MysqlProxyFlavorGroups
from huaweicloudsdkgaussdb.v3.model.mysql_proxy_info import MysqlProxyInfo
from huaweicloudsdkgaussdb.v3.model.mysql_proxy_node_v3 import MysqlProxyNodeV3
from huaweicloudsdkgaussdb.v3.model.mysql_proxy_nodes import MysqlProxyNodes
from huaweicloudsdkgaussdb.v3.model.mysql_proxy_v3 import MysqlProxyV3
from huaweicloudsdkgaussdb.v3.model.mysql_reset_password_request import MysqlResetPasswordRequest
from huaweicloudsdkgaussdb.v3.model.mysql_resize_flavor import MysqlResizeFlavor
from huaweicloudsdkgaussdb.v3.model.mysql_restore_point import MysqlRestorePoint
from huaweicloudsdkgaussdb.v3.model.mysql_show_proxy_response_v3 import MysqlShowProxyResponseV3
from huaweicloudsdkgaussdb.v3.model.mysql_tags import MysqlTags
from huaweicloudsdkgaussdb.v3.model.mysql_update_backup_policy_request import MysqlUpdateBackupPolicyRequest
from huaweicloudsdkgaussdb.v3.model.mysql_update_instance_name_request import MysqlUpdateInstanceNameRequest
from huaweicloudsdkgaussdb.v3.model.mysql_volume import MysqlVolume
from huaweicloudsdkgaussdb.v3.model.mysql_volume_info import MysqlVolumeInfo
from huaweicloudsdkgaussdb.v3.model.node_sql_filter_rule import NodeSqlFilterRule
from huaweicloudsdkgaussdb.v3.model.node_sql_filter_rule_info import NodeSqlFilterRuleInfo
from huaweicloudsdkgaussdb.v3.model.node_sql_filter_rule_pattern import NodeSqlFilterRulePattern
from huaweicloudsdkgaussdb.v3.model.nodes_weight import NodesWeight
from huaweicloudsdkgaussdb.v3.model.open_mysql_proxy_request_body import OpenMysqlProxyRequestBody
from huaweicloudsdkgaussdb.v3.model.operate_audit_log_request_v3_body import OperateAuditLogRequestV3Body
from huaweicloudsdkgaussdb.v3.model.operate_sql_filter_control_req import OperateSqlFilterControlReq
from huaweicloudsdkgaussdb.v3.model.operate_sql_filter_rule_req import OperateSqlFilterRuleReq
from huaweicloudsdkgaussdb.v3.model.project_quotas import ProjectQuotas
from huaweicloudsdkgaussdb.v3.model.project_tag_item import ProjectTagItem
from huaweicloudsdkgaussdb.v3.model.proxy_transaction_split_request import ProxyTransactionSplitRequest
from huaweicloudsdkgaussdb.v3.model.proxy_update_proxy_connection_pool_type_request import ProxyUpdateProxyConnectionPoolTypeRequest
from huaweicloudsdkgaussdb.v3.model.quota import Quota
from huaweicloudsdkgaussdb.v3.model.reset_database_password import ResetDatabasePassword
from huaweicloudsdkgaussdb.v3.model.reset_database_password_request import ResetDatabasePasswordRequest
from huaweicloudsdkgaussdb.v3.model.reset_gauss_my_sql_database_password_request import ResetGaussMySqlDatabasePasswordRequest
from huaweicloudsdkgaussdb.v3.model.reset_gauss_my_sql_database_password_response import ResetGaussMySqlDatabasePasswordResponse
from huaweicloudsdkgaussdb.v3.model.reset_gauss_my_sql_password_request import ResetGaussMySqlPasswordRequest
from huaweicloudsdkgaussdb.v3.model.reset_gauss_my_sql_password_response import ResetGaussMySqlPasswordResponse
from huaweicloudsdkgaussdb.v3.model.resource import Resource
from huaweicloudsdkgaussdb.v3.model.resource_tag_item import ResourceTagItem
from huaweicloudsdkgaussdb.v3.model.restart_gauss_my_sql_instance_request import RestartGaussMySqlInstanceRequest
from huaweicloudsdkgaussdb.v3.model.restart_gauss_my_sql_instance_response import RestartGaussMySqlInstanceResponse
from huaweicloudsdkgaussdb.v3.model.restart_gauss_my_sql_node_request import RestartGaussMySqlNodeRequest
from huaweicloudsdkgaussdb.v3.model.restart_gauss_my_sql_node_response import RestartGaussMySqlNodeResponse
from huaweicloudsdkgaussdb.v3.model.restart_node_request import RestartNodeRequest
from huaweicloudsdkgaussdb.v3.model.restore_old_instance_request import RestoreOldInstanceRequest
from huaweicloudsdkgaussdb.v3.model.restore_old_instance_response import RestoreOldInstanceResponse
from huaweicloudsdkgaussdb.v3.model.restore_request import RestoreRequest
from huaweicloudsdkgaussdb.v3.model.restore_time_info import RestoreTimeInfo
from huaweicloudsdkgaussdb.v3.model.schedule_task import ScheduleTask
from huaweicloudsdkgaussdb.v3.model.set_gauss_my_sql_proxy_weight_request import SetGaussMySqlProxyWeightRequest
from huaweicloudsdkgaussdb.v3.model.set_gauss_my_sql_proxy_weight_response import SetGaussMySqlProxyWeightResponse
from huaweicloudsdkgaussdb.v3.model.set_gauss_my_sql_quotas_request import SetGaussMySqlQuotasRequest
from huaweicloudsdkgaussdb.v3.model.set_gauss_my_sql_quotas_response import SetGaussMySqlQuotasResponse
from huaweicloudsdkgaussdb.v3.model.set_quota import SetQuota
from huaweicloudsdkgaussdb.v3.model.set_quotas_request_body import SetQuotasRequestBody
from huaweicloudsdkgaussdb.v3.model.set_sql_filter_rule_request import SetSqlFilterRuleRequest
from huaweicloudsdkgaussdb.v3.model.set_sql_filter_rule_response import SetSqlFilterRuleResponse
from huaweicloudsdkgaussdb.v3.model.show_audit_log_request import ShowAuditLogRequest
from huaweicloudsdkgaussdb.v3.model.show_audit_log_response import ShowAuditLogResponse
from huaweicloudsdkgaussdb.v3.model.show_backup_restore_time_request import ShowBackupRestoreTimeRequest
from huaweicloudsdkgaussdb.v3.model.show_backup_restore_time_response import ShowBackupRestoreTimeResponse
from huaweicloudsdkgaussdb.v3.model.show_dedicated_resource_info_request import ShowDedicatedResourceInfoRequest
from huaweicloudsdkgaussdb.v3.model.show_dedicated_resource_info_response import ShowDedicatedResourceInfoResponse
from huaweicloudsdkgaussdb.v3.model.show_gauss_my_sql_backup_list_request import ShowGaussMySqlBackupListRequest
from huaweicloudsdkgaussdb.v3.model.show_gauss_my_sql_backup_list_response import ShowGaussMySqlBackupListResponse
from huaweicloudsdkgaussdb.v3.model.show_gauss_my_sql_backup_policy_request import ShowGaussMySqlBackupPolicyRequest
from huaweicloudsdkgaussdb.v3.model.show_gauss_my_sql_backup_policy_response import ShowGaussMySqlBackupPolicyResponse
from huaweicloudsdkgaussdb.v3.model.show_gauss_my_sql_configuration_request import ShowGaussMySqlConfigurationRequest
from huaweicloudsdkgaussdb.v3.model.show_gauss_my_sql_configuration_response import ShowGaussMySqlConfigurationResponse
from huaweicloudsdkgaussdb.v3.model.show_gauss_my_sql_engine_version_request import ShowGaussMySqlEngineVersionRequest
from huaweicloudsdkgaussdb.v3.model.show_gauss_my_sql_engine_version_response import ShowGaussMySqlEngineVersionResponse
from huaweicloudsdkgaussdb.v3.model.show_gauss_my_sql_flavors_request import ShowGaussMySqlFlavorsRequest
from huaweicloudsdkgaussdb.v3.model.show_gauss_my_sql_flavors_response import ShowGaussMySqlFlavorsResponse
from huaweicloudsdkgaussdb.v3.model.show_gauss_my_sql_instance_info_request import ShowGaussMySqlInstanceInfoRequest
from huaweicloudsdkgaussdb.v3.model.show_gauss_my_sql_instance_info_response import ShowGaussMySqlInstanceInfoResponse
from huaweicloudsdkgaussdb.v3.model.show_gauss_my_sql_job_info_request import ShowGaussMySqlJobInfoRequest
from huaweicloudsdkgaussdb.v3.model.show_gauss_my_sql_job_info_response import ShowGaussMySqlJobInfoResponse
from huaweicloudsdkgaussdb.v3.model.show_gauss_my_sql_project_quotas_request import ShowGaussMySqlProjectQuotasRequest
from huaweicloudsdkgaussdb.v3.model.show_gauss_my_sql_project_quotas_response import ShowGaussMySqlProjectQuotasResponse
from huaweicloudsdkgaussdb.v3.model.show_gauss_my_sql_proxy_flavors_request import ShowGaussMySqlProxyFlavorsRequest
from huaweicloudsdkgaussdb.v3.model.show_gauss_my_sql_proxy_flavors_response import ShowGaussMySqlProxyFlavorsResponse
from huaweicloudsdkgaussdb.v3.model.show_gauss_my_sql_proxy_list_request import ShowGaussMySqlProxyListRequest
from huaweicloudsdkgaussdb.v3.model.show_gauss_my_sql_proxy_list_response import ShowGaussMySqlProxyListResponse
from huaweicloudsdkgaussdb.v3.model.show_gauss_my_sql_quotas_request import ShowGaussMySqlQuotasRequest
from huaweicloudsdkgaussdb.v3.model.show_gauss_my_sql_quotas_response import ShowGaussMySqlQuotasResponse
from huaweicloudsdkgaussdb.v3.model.show_instance_monitor_extend_request import ShowInstanceMonitorExtendRequest
from huaweicloudsdkgaussdb.v3.model.show_instance_monitor_extend_response import ShowInstanceMonitorExtendResponse
from huaweicloudsdkgaussdb.v3.model.show_sql_filter_control_request import ShowSqlFilterControlRequest
from huaweicloudsdkgaussdb.v3.model.show_sql_filter_control_response import ShowSqlFilterControlResponse
from huaweicloudsdkgaussdb.v3.model.show_sql_filter_rule_request import ShowSqlFilterRuleRequest
from huaweicloudsdkgaussdb.v3.model.show_sql_filter_rule_response import ShowSqlFilterRuleResponse
from huaweicloudsdkgaussdb.v3.model.sql_filter_rule import SqlFilterRule
from huaweicloudsdkgaussdb.v3.model.sql_filter_rule_pattern import SqlFilterRulePattern
from huaweicloudsdkgaussdb.v3.model.switch_gauss_my_sql_configuration_request import SwitchGaussMySqlConfigurationRequest
from huaweicloudsdkgaussdb.v3.model.switch_gauss_my_sql_configuration_response import SwitchGaussMySqlConfigurationResponse
from huaweicloudsdkgaussdb.v3.model.switch_gauss_my_sql_instance_ssl_request import SwitchGaussMySqlInstanceSslRequest
from huaweicloudsdkgaussdb.v3.model.switch_gauss_my_sql_instance_ssl_response import SwitchGaussMySqlInstanceSslResponse
from huaweicloudsdkgaussdb.v3.model.switch_ssl_request import SwitchSSLRequest
from huaweicloudsdkgaussdb.v3.model.tag_item import TagItem
from huaweicloudsdkgaussdb.v3.model.task_detail_info import TaskDetailInfo
from huaweicloudsdkgaussdb.v3.model.taurus_modify_instance_monitor_request_body import TaurusModifyInstanceMonitorRequestBody
from huaweicloudsdkgaussdb.v3.model.taurus_modify_proxy_weight_request import TaurusModifyProxyWeightRequest
from huaweicloudsdkgaussdb.v3.model.taurus_proxy_scale_request import TaurusProxyScaleRequest
from huaweicloudsdkgaussdb.v3.model.taurus_restart_instance_request import TaurusRestartInstanceRequest
from huaweicloudsdkgaussdb.v3.model.taurus_switchover_request import TaurusSwitchoverRequest
from huaweicloudsdkgaussdb.v3.model.update_audit_log_request import UpdateAuditLogRequest
from huaweicloudsdkgaussdb.v3.model.update_audit_log_response import UpdateAuditLogResponse
from huaweicloudsdkgaussdb.v3.model.update_configuration_parameter_request_body import UpdateConfigurationParameterRequestBody
from huaweicloudsdkgaussdb.v3.model.update_database_comment import UpdateDatabaseComment
from huaweicloudsdkgaussdb.v3.model.update_database_comment_request import UpdateDatabaseCommentRequest
from huaweicloudsdkgaussdb.v3.model.update_database_user_comment import UpdateDatabaseUserComment
from huaweicloudsdkgaussdb.v3.model.update_database_user_comment_request import UpdateDatabaseUserCommentRequest
from huaweicloudsdkgaussdb.v3.model.update_gauss_my_sql_backup_policy_request import UpdateGaussMySqlBackupPolicyRequest
from huaweicloudsdkgaussdb.v3.model.update_gauss_my_sql_backup_policy_response import UpdateGaussMySqlBackupPolicyResponse
from huaweicloudsdkgaussdb.v3.model.update_gauss_my_sql_configuration_request import UpdateGaussMySqlConfigurationRequest
from huaweicloudsdkgaussdb.v3.model.update_gauss_my_sql_configuration_response import UpdateGaussMySqlConfigurationResponse
from huaweicloudsdkgaussdb.v3.model.update_gauss_my_sql_database_comment_request import UpdateGaussMySqlDatabaseCommentRequest
from huaweicloudsdkgaussdb.v3.model.update_gauss_my_sql_database_comment_response import UpdateGaussMySqlDatabaseCommentResponse
from huaweicloudsdkgaussdb.v3.model.update_gauss_my_sql_database_user_comment_request import UpdateGaussMySqlDatabaseUserCommentRequest
from huaweicloudsdkgaussdb.v3.model.update_gauss_my_sql_database_user_comment_response import UpdateGaussMySqlDatabaseUserCommentResponse
from huaweicloudsdkgaussdb.v3.model.update_gauss_my_sql_instance_alias_request import UpdateGaussMySqlInstanceAliasRequest
from huaweicloudsdkgaussdb.v3.model.update_gauss_my_sql_instance_alias_response import UpdateGaussMySqlInstanceAliasResponse
from huaweicloudsdkgaussdb.v3.model.update_gauss_my_sql_instance_eip_request import UpdateGaussMySqlInstanceEipRequest
from huaweicloudsdkgaussdb.v3.model.update_gauss_my_sql_instance_eip_response import UpdateGaussMySqlInstanceEipResponse
from huaweicloudsdkgaussdb.v3.model.update_gauss_my_sql_instance_internal_ip_request import UpdateGaussMySqlInstanceInternalIpRequest
from huaweicloudsdkgaussdb.v3.model.update_gauss_my_sql_instance_internal_ip_response import UpdateGaussMySqlInstanceInternalIpResponse
from huaweicloudsdkgaussdb.v3.model.update_gauss_my_sql_instance_name_request import UpdateGaussMySqlInstanceNameRequest
from huaweicloudsdkgaussdb.v3.model.update_gauss_my_sql_instance_name_response import UpdateGaussMySqlInstanceNameResponse
from huaweicloudsdkgaussdb.v3.model.update_gauss_my_sql_instance_ops_window_request import UpdateGaussMySqlInstanceOpsWindowRequest
from huaweicloudsdkgaussdb.v3.model.update_gauss_my_sql_instance_ops_window_response import UpdateGaussMySqlInstanceOpsWindowResponse
from huaweicloudsdkgaussdb.v3.model.update_gauss_my_sql_instance_port_request import UpdateGaussMySqlInstancePortRequest
from huaweicloudsdkgaussdb.v3.model.update_gauss_my_sql_instance_port_response import UpdateGaussMySqlInstancePortResponse
from huaweicloudsdkgaussdb.v3.model.update_gauss_my_sql_instance_security_group_request import UpdateGaussMySqlInstanceSecurityGroupRequest
from huaweicloudsdkgaussdb.v3.model.update_gauss_my_sql_instance_security_group_response import UpdateGaussMySqlInstanceSecurityGroupResponse
from huaweicloudsdkgaussdb.v3.model.update_gauss_my_sql_quotas_request import UpdateGaussMySqlQuotasRequest
from huaweicloudsdkgaussdb.v3.model.update_gauss_my_sql_quotas_response import UpdateGaussMySqlQuotasResponse
from huaweicloudsdkgaussdb.v3.model.update_instance_monitor_request import UpdateInstanceMonitorRequest
from huaweicloudsdkgaussdb.v3.model.update_instance_monitor_response import UpdateInstanceMonitorResponse
from huaweicloudsdkgaussdb.v3.model.update_proxy_connection_pool_type_request import UpdateProxyConnectionPoolTypeRequest
from huaweicloudsdkgaussdb.v3.model.update_proxy_connection_pool_type_response import UpdateProxyConnectionPoolTypeResponse
from huaweicloudsdkgaussdb.v3.model.update_proxy_session_consistence_request import UpdateProxySessionConsistenceRequest
from huaweicloudsdkgaussdb.v3.model.update_proxy_session_consistence_response import UpdateProxySessionConsistenceResponse
from huaweicloudsdkgaussdb.v3.model.update_sql_filter_control_request import UpdateSqlFilterControlRequest
from huaweicloudsdkgaussdb.v3.model.update_sql_filter_control_response import UpdateSqlFilterControlResponse
from huaweicloudsdkgaussdb.v3.model.update_transaction_split_status_request import UpdateTransactionSplitStatusRequest
from huaweicloudsdkgaussdb.v3.model.update_transaction_split_status_response import UpdateTransactionSplitStatusResponse
from huaweicloudsdkgaussdb.v3.model.upgrade_database_request import UpgradeDatabaseRequest
from huaweicloudsdkgaussdb.v3.model.upgrade_gauss_my_sql_instance_database_request import UpgradeGaussMySqlInstanceDatabaseRequest
from huaweicloudsdkgaussdb.v3.model.upgrade_gauss_my_sql_instance_database_response import UpgradeGaussMySqlInstanceDatabaseResponse

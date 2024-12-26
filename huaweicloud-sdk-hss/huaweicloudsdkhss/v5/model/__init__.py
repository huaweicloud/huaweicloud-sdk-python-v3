# coding: utf-8

from __future__ import absolute_import

# import models into model package
from huaweicloudsdkhss.v5.model.account_response_info import AccountResponseInfo
from huaweicloudsdkhss.v5.model.add_accounts_request_info import AddAccountsRequestInfo
from huaweicloudsdkhss.v5.model.add_cce_integration_protection_request import AddCceIntegrationProtectionRequest
from huaweicloudsdkhss.v5.model.add_cce_integration_protection_response import AddCceIntegrationProtectionResponse
from huaweicloudsdkhss.v5.model.add_hosts_group_request import AddHostsGroupRequest
from huaweicloudsdkhss.v5.model.add_hosts_group_request_info import AddHostsGroupRequestInfo
from huaweicloudsdkhss.v5.model.add_hosts_group_response import AddHostsGroupResponse
from huaweicloudsdkhss.v5.model.agent_id import AgentId
from huaweicloudsdkhss.v5.model.agent_install_script_response_info import AgentInstallScriptResponseInfo
from huaweicloudsdkhss.v5.model.agent_version import AgentVersion
from huaweicloudsdkhss.v5.model.alarm_white_list_response_info import AlarmWhiteListResponseInfo
from huaweicloudsdkhss.v5.model.antivirus_result_detail_info import AntivirusResultDetailInfo
from huaweicloudsdkhss.v5.model.app_change_response_info import AppChangeResponseInfo
from huaweicloudsdkhss.v5.model.app_response_info import AppResponseInfo
from huaweicloudsdkhss.v5.model.app_statistic_response_info import AppStatisticResponseInfo
from huaweicloudsdkhss.v5.model.asset_value import AssetValue
from huaweicloudsdkhss.v5.model.associate_images import AssociateImages
from huaweicloudsdkhss.v5.model.associate_policy_group_request import AssociatePolicyGroupRequest
from huaweicloudsdkhss.v5.model.associate_policy_group_request_info import AssociatePolicyGroupRequestInfo
from huaweicloudsdkhss.v5.model.associate_policy_group_response import AssociatePolicyGroupResponse
from huaweicloudsdkhss.v5.model.attack_phase import AttackPhase
from huaweicloudsdkhss.v5.model.attack_tag import AttackTag
from huaweicloudsdkhss.v5.model.auto_lauch_response_info import AutoLauchResponseInfo
from huaweicloudsdkhss.v5.model.auto_launch_change_response_info import AutoLaunchChangeResponseInfo
from huaweicloudsdkhss.v5.model.auto_launch_statistics_response_info import AutoLaunchStatisticsResponseInfo
from huaweicloudsdkhss.v5.model.available_resource_ids_info import AvailableResourceIdsInfo
from huaweicloudsdkhss.v5.model.backup_resources import BackupResources
from huaweicloudsdkhss.v5.model.backup_trigger_info import BackupTriggerInfo
from huaweicloudsdkhss.v5.model.backup_trigger_properties_info import BackupTriggerPropertiesInfo
from huaweicloudsdkhss.v5.model.backup_trigger_properties_request_info import BackupTriggerPropertiesRequestInfo
from huaweicloudsdkhss.v5.model.backup_trigger_properties_request_info1 import BackupTriggerPropertiesRequestInfo1
from huaweicloudsdkhss.v5.model.backup_trigger_request_info import BackupTriggerRequestInfo
from huaweicloudsdkhss.v5.model.backup_trigger_request_info1 import BackupTriggerRequestInfo1
from huaweicloudsdkhss.v5.model.batch_add_accounts_request import BatchAddAccountsRequest
from huaweicloudsdkhss.v5.model.batch_add_accounts_request_info import BatchAddAccountsRequestInfo
from huaweicloudsdkhss.v5.model.batch_add_accounts_response import BatchAddAccountsResponse
from huaweicloudsdkhss.v5.model.batch_create_tags_request import BatchCreateTagsRequest
from huaweicloudsdkhss.v5.model.batch_create_tags_request_info import BatchCreateTagsRequestInfo
from huaweicloudsdkhss.v5.model.batch_create_tags_response import BatchCreateTagsResponse
from huaweicloudsdkhss.v5.model.batch_scan_private_image_request_info import BatchScanPrivateImageRequestInfo
from huaweicloudsdkhss.v5.model.batch_scan_swr_image_info import BatchScanSwrImageInfo
from huaweicloudsdkhss.v5.model.batch_scan_swr_image_request import BatchScanSwrImageRequest
from huaweicloudsdkhss.v5.model.batch_scan_swr_image_response import BatchScanSwrImageResponse
from huaweicloudsdkhss.v5.model.blocked_ip_request_info import BlockedIpRequestInfo
from huaweicloudsdkhss.v5.model.blocked_ip_response_info import BlockedIpResponseInfo
from huaweicloudsdkhss.v5.model.cce_cluster_info_list_request_body import CCEClusterInfoListRequestBody
from huaweicloudsdkhss.v5.model.cce_cluster_info_list_request_body_cluster_info_list import CCEClusterInfoListRequestBodyClusterInfoList
from huaweicloudsdkhss.v5.model.cce_integration_protection_request_body import CceIntegrationProtectionRequestBody
from huaweicloudsdkhss.v5.model.change_blocked_ip_request import ChangeBlockedIpRequest
from huaweicloudsdkhss.v5.model.change_blocked_ip_request_info import ChangeBlockedIpRequestInfo
from huaweicloudsdkhss.v5.model.change_blocked_ip_response import ChangeBlockedIpResponse
from huaweicloudsdkhss.v5.model.change_check_rule_action_request import ChangeCheckRuleActionRequest
from huaweicloudsdkhss.v5.model.change_check_rule_action_response import ChangeCheckRuleActionResponse
from huaweicloudsdkhss.v5.model.change_event_request import ChangeEventRequest
from huaweicloudsdkhss.v5.model.change_event_request_info import ChangeEventRequestInfo
from huaweicloudsdkhss.v5.model.change_event_response import ChangeEventResponse
from huaweicloudsdkhss.v5.model.change_hosts_group_request import ChangeHostsGroupRequest
from huaweicloudsdkhss.v5.model.change_hosts_group_request_info import ChangeHostsGroupRequestInfo
from huaweicloudsdkhss.v5.model.change_hosts_group_response import ChangeHostsGroupResponse
from huaweicloudsdkhss.v5.model.change_isolated_file_request import ChangeIsolatedFileRequest
from huaweicloudsdkhss.v5.model.change_isolated_file_request_info import ChangeIsolatedFileRequestInfo
from huaweicloudsdkhss.v5.model.change_isolated_file_response import ChangeIsolatedFileResponse
from huaweicloudsdkhss.v5.model.change_vul_scan_policy_request import ChangeVulScanPolicyRequest
from huaweicloudsdkhss.v5.model.change_vul_scan_policy_request_info import ChangeVulScanPolicyRequestInfo
from huaweicloudsdkhss.v5.model.change_vul_scan_policy_response import ChangeVulScanPolicyResponse
from huaweicloudsdkhss.v5.model.change_vul_status_request import ChangeVulStatusRequest
from huaweicloudsdkhss.v5.model.change_vul_status_request_info import ChangeVulStatusRequestInfo
from huaweicloudsdkhss.v5.model.change_vul_status_request_info_custom_backup_hosts import ChangeVulStatusRequestInfoCustomBackupHosts
from huaweicloudsdkhss.v5.model.change_vul_status_response import ChangeVulStatusResponse
from huaweicloudsdkhss.v5.model.check_rule_check_case_response_info import CheckRuleCheckCaseResponseInfo
from huaweicloudsdkhss.v5.model.check_rule_fix_param_info import CheckRuleFixParamInfo
from huaweicloudsdkhss.v5.model.check_rule_fix_values_info import CheckRuleFixValuesInfo
from huaweicloudsdkhss.v5.model.check_rule_id_list_request_info import CheckRuleIdListRequestInfo
from huaweicloudsdkhss.v5.model.check_rule_key_info_request_info import CheckRuleKeyInfoRequestInfo
from huaweicloudsdkhss.v5.model.check_rule_risk_info_response_info import CheckRuleRiskInfoResponseInfo
from huaweicloudsdkhss.v5.model.close_protection_info_request_info import CloseProtectionInfoRequestInfo
from huaweicloudsdkhss.v5.model.cluster_config_response_info import ClusterConfigResponseInfo
from huaweicloudsdkhss.v5.model.container_base_info import ContainerBaseInfo
from huaweicloudsdkhss.v5.model.container_name import ContainerName
from huaweicloudsdkhss.v5.model.container_node_info import ContainerNodeInfo
from huaweicloudsdkhss.v5.model.create_quotas_order_request import CreateQuotasOrderRequest
from huaweicloudsdkhss.v5.model.create_quotas_order_request_info import CreateQuotasOrderRequestInfo
from huaweicloudsdkhss.v5.model.create_quotas_order_response import CreateQuotasOrderResponse
from huaweicloudsdkhss.v5.model.create_vulnerability_scan_task_request import CreateVulnerabilityScanTaskRequest
from huaweicloudsdkhss.v5.model.create_vulnerability_scan_task_response import CreateVulnerabilityScanTaskResponse
from huaweicloudsdkhss.v5.model.default_group import DefaultGroup
from huaweicloudsdkhss.v5.model.deletable import Deletable
from huaweicloudsdkhss.v5.model.delete_account_request import DeleteAccountRequest
from huaweicloudsdkhss.v5.model.delete_account_request_info import DeleteAccountRequestInfo
from huaweicloudsdkhss.v5.model.delete_account_response import DeleteAccountResponse
from huaweicloudsdkhss.v5.model.delete_agent_daemonset_request import DeleteAgentDaemonsetRequest
from huaweicloudsdkhss.v5.model.delete_agent_daemonset_response import DeleteAgentDaemonsetResponse
from huaweicloudsdkhss.v5.model.delete_hosts_group_request import DeleteHostsGroupRequest
from huaweicloudsdkhss.v5.model.delete_hosts_group_response import DeleteHostsGroupResponse
from huaweicloudsdkhss.v5.model.delete_resource_instance_tag_request import DeleteResourceInstanceTagRequest
from huaweicloudsdkhss.v5.model.delete_resource_instance_tag_response import DeleteResourceInstanceTagResponse
from huaweicloudsdkhss.v5.model.description import Description
from huaweicloudsdkhss.v5.model.enterprise_project_name import EnterpriseProjectName
from huaweicloudsdkhss.v5.model.event_class_id import EventClassId
from huaweicloudsdkhss.v5.model.event_detail_request_info import EventDetailRequestInfo
from huaweicloudsdkhss.v5.model.event_detail_response_info import EventDetailResponseInfo
from huaweicloudsdkhss.v5.model.event_file_response_info import EventFileResponseInfo
from huaweicloudsdkhss.v5.model.event_id import EventId
from huaweicloudsdkhss.v5.model.event_management_response_info import EventManagementResponseInfo
from huaweicloudsdkhss.v5.model.event_name import EventName
from huaweicloudsdkhss.v5.model.event_process_response_info import EventProcessResponseInfo
from huaweicloudsdkhss.v5.model.event_resource_response_info import EventResourceResponseInfo
from huaweicloudsdkhss.v5.model.event_type import EventType
from huaweicloudsdkhss.v5.model.event_user_response_info import EventUserResponseInfo
from huaweicloudsdkhss.v5.model.event_white_rule_list_request_info import EventWhiteRuleListRequestInfo
from huaweicloudsdkhss.v5.model.export_vul_request_body import ExportVulRequestBody
from huaweicloudsdkhss.v5.model.export_vuls_request import ExportVulsRequest
from huaweicloudsdkhss.v5.model.export_vuls_response import ExportVulsResponse
from huaweicloudsdkhss.v5.model.file_attr import FileAttr
from huaweicloudsdkhss.v5.model.file_ctime import FileCtime
from huaweicloudsdkhss.v5.model.file_hash import FileHash
from huaweicloudsdkhss.v5.model.file_mtime import FileMtime
from huaweicloudsdkhss.v5.model.file_owner import FileOwner
from huaweicloudsdkhss.v5.model.file_path import FilePath
from huaweicloudsdkhss.v5.model.file_size import FileSize
from huaweicloudsdkhss.v5.model.group_id import GroupId
from huaweicloudsdkhss.v5.model.group_name import GroupName
from huaweicloudsdkhss.v5.model.handle_method import HandleMethod
from huaweicloudsdkhss.v5.model.handle_status import HandleStatus
from huaweicloudsdkhss.v5.model.handle_time import HandleTime
from huaweicloudsdkhss.v5.model.handler import Handler
from huaweicloudsdkhss.v5.model.hash import Hash
from huaweicloudsdkhss.v5.model.host import Host
from huaweicloudsdkhss.v5.model.host_group_item import HostGroupItem
from huaweicloudsdkhss.v5.model.host_id import HostId
from huaweicloudsdkhss.v5.model.host_name import HostName
from huaweicloudsdkhss.v5.model.host_num import HostNum
from huaweicloudsdkhss.v5.model.host_protect_history_response_info import HostProtectHistoryResponseInfo
from huaweicloudsdkhss.v5.model.host_rasp_protect_history_response_info import HostRaspProtectHistoryResponseInfo
from huaweicloudsdkhss.v5.model.host_vul_info import HostVulInfo
from huaweicloudsdkhss.v5.model.host_vul_info_app_list import HostVulInfoAppList
from huaweicloudsdkhss.v5.model.host_vul_info_cve_list import HostVulInfoCveList
from huaweicloudsdkhss.v5.model.host_vul_operate_info import HostVulOperateInfo
from huaweicloudsdkhss.v5.model.image_check_rule_check_case_response_info import ImageCheckRuleCheckCaseResponseInfo
from huaweicloudsdkhss.v5.model.image_local_info import ImageLocalInfo
from huaweicloudsdkhss.v5.model.image_name import ImageName
from huaweicloudsdkhss.v5.model.image_risk_configs_check_rules_response_info import ImageRiskConfigsCheckRulesResponseInfo
from huaweicloudsdkhss.v5.model.image_risk_configs_info_response_info import ImageRiskConfigsInfoResponseInfo
from huaweicloudsdkhss.v5.model.image_vul_cve_info import ImageVulCveInfo
from huaweicloudsdkhss.v5.model.image_vul_info import ImageVulInfo
from huaweicloudsdkhss.v5.model.is_parent import IsParent
from huaweicloudsdkhss.v5.model.isolate_event_response_info import IsolateEventResponseInfo
from huaweicloudsdkhss.v5.model.isolate_source import IsolateSource
from huaweicloudsdkhss.v5.model.isolated_file_request_info import IsolatedFileRequestInfo
from huaweicloudsdkhss.v5.model.isolated_file_response_info import IsolatedFileResponseInfo
from huaweicloudsdkhss.v5.model.isolation_status import IsolationStatus
from huaweicloudsdkhss.v5.model.jar_package_host_info import JarPackageHostInfo
from huaweicloudsdkhss.v5.model.jar_package_statistics_response_info import JarPackageStatisticsResponseInfo
from huaweicloudsdkhss.v5.model.list_accounts_request import ListAccountsRequest
from huaweicloudsdkhss.v5.model.list_accounts_response import ListAccountsResponse
from huaweicloudsdkhss.v5.model.list_agent_install_script_request import ListAgentInstallScriptRequest
from huaweicloudsdkhss.v5.model.list_agent_install_script_response import ListAgentInstallScriptResponse
from huaweicloudsdkhss.v5.model.list_alarm_white_list_request import ListAlarmWhiteListRequest
from huaweicloudsdkhss.v5.model.list_alarm_white_list_response import ListAlarmWhiteListResponse
from huaweicloudsdkhss.v5.model.list_app_change_histories_request import ListAppChangeHistoriesRequest
from huaweicloudsdkhss.v5.model.list_app_change_histories_response import ListAppChangeHistoriesResponse
from huaweicloudsdkhss.v5.model.list_app_statistics_request import ListAppStatisticsRequest
from huaweicloudsdkhss.v5.model.list_app_statistics_response import ListAppStatisticsResponse
from huaweicloudsdkhss.v5.model.list_apps_request import ListAppsRequest
from huaweicloudsdkhss.v5.model.list_apps_response import ListAppsResponse
from huaweicloudsdkhss.v5.model.list_auto_launch_change_histories_request import ListAutoLaunchChangeHistoriesRequest
from huaweicloudsdkhss.v5.model.list_auto_launch_change_histories_response import ListAutoLaunchChangeHistoriesResponse
from huaweicloudsdkhss.v5.model.list_auto_launch_statistics_request import ListAutoLaunchStatisticsRequest
from huaweicloudsdkhss.v5.model.list_auto_launch_statistics_response import ListAutoLaunchStatisticsResponse
from huaweicloudsdkhss.v5.model.list_auto_launchs_request import ListAutoLaunchsRequest
from huaweicloudsdkhss.v5.model.list_auto_launchs_response import ListAutoLaunchsResponse
from huaweicloudsdkhss.v5.model.list_blocked_ip_request import ListBlockedIpRequest
from huaweicloudsdkhss.v5.model.list_blocked_ip_response import ListBlockedIpResponse
from huaweicloudsdkhss.v5.model.list_cce_cluster_config_request import ListCceClusterConfigRequest
from huaweicloudsdkhss.v5.model.list_cce_cluster_config_response import ListCceClusterConfigResponse
from huaweicloudsdkhss.v5.model.list_container_nodes_request import ListContainerNodesRequest
from huaweicloudsdkhss.v5.model.list_container_nodes_response import ListContainerNodesResponse
from huaweicloudsdkhss.v5.model.list_containers_request import ListContainersRequest
from huaweicloudsdkhss.v5.model.list_containers_response import ListContainersResponse
from huaweicloudsdkhss.v5.model.list_download_exported_file_request import ListDownloadExportedFileRequest
from huaweicloudsdkhss.v5.model.list_download_exported_file_response import ListDownloadExportedFileResponse
from huaweicloudsdkhss.v5.model.list_host_groups_request import ListHostGroupsRequest
from huaweicloudsdkhss.v5.model.list_host_groups_response import ListHostGroupsResponse
from huaweicloudsdkhss.v5.model.list_host_protect_history_info_request import ListHostProtectHistoryInfoRequest
from huaweicloudsdkhss.v5.model.list_host_protect_history_info_response import ListHostProtectHistoryInfoResponse
from huaweicloudsdkhss.v5.model.list_host_rasp_protect_history_info_request import ListHostRaspProtectHistoryInfoRequest
from huaweicloudsdkhss.v5.model.list_host_rasp_protect_history_info_response import ListHostRaspProtectHistoryInfoResponse
from huaweicloudsdkhss.v5.model.list_host_status_request import ListHostStatusRequest
from huaweicloudsdkhss.v5.model.list_host_status_response import ListHostStatusResponse
from huaweicloudsdkhss.v5.model.list_host_vuls_request import ListHostVulsRequest
from huaweicloudsdkhss.v5.model.list_host_vuls_response import ListHostVulsResponse
from huaweicloudsdkhss.v5.model.list_image_local_request import ListImageLocalRequest
from huaweicloudsdkhss.v5.model.list_image_local_response import ListImageLocalResponse
from huaweicloudsdkhss.v5.model.list_image_risk_config_rules_request import ListImageRiskConfigRulesRequest
from huaweicloudsdkhss.v5.model.list_image_risk_config_rules_response import ListImageRiskConfigRulesResponse
from huaweicloudsdkhss.v5.model.list_image_risk_configs_request import ListImageRiskConfigsRequest
from huaweicloudsdkhss.v5.model.list_image_risk_configs_response import ListImageRiskConfigsResponse
from huaweicloudsdkhss.v5.model.list_image_vulnerabilities_request import ListImageVulnerabilitiesRequest
from huaweicloudsdkhss.v5.model.list_image_vulnerabilities_response import ListImageVulnerabilitiesResponse
from huaweicloudsdkhss.v5.model.list_isolated_file_request import ListIsolatedFileRequest
from huaweicloudsdkhss.v5.model.list_isolated_file_response import ListIsolatedFileResponse
from huaweicloudsdkhss.v5.model.list_jar_package_host_info_request import ListJarPackageHostInfoRequest
from huaweicloudsdkhss.v5.model.list_jar_package_host_info_response import ListJarPackageHostInfoResponse
from huaweicloudsdkhss.v5.model.list_jar_package_statistics_request import ListJarPackageStatisticsRequest
from huaweicloudsdkhss.v5.model.list_jar_package_statistics_response import ListJarPackageStatisticsResponse
from huaweicloudsdkhss.v5.model.list_organization_tree_request import ListOrganizationTreeRequest
from huaweicloudsdkhss.v5.model.list_organization_tree_response import ListOrganizationTreeResponse
from huaweicloudsdkhss.v5.model.list_password_complexity_request import ListPasswordComplexityRequest
from huaweicloudsdkhss.v5.model.list_password_complexity_response import ListPasswordComplexityResponse
from huaweicloudsdkhss.v5.model.list_policy_group_request import ListPolicyGroupRequest
from huaweicloudsdkhss.v5.model.list_policy_group_response import ListPolicyGroupResponse
from huaweicloudsdkhss.v5.model.list_port_host_request import ListPortHostRequest
from huaweicloudsdkhss.v5.model.list_port_host_response import ListPortHostResponse
from huaweicloudsdkhss.v5.model.list_port_statistics_request import ListPortStatisticsRequest
from huaweicloudsdkhss.v5.model.list_port_statistics_response import ListPortStatisticsResponse
from huaweicloudsdkhss.v5.model.list_ports_request import ListPortsRequest
from huaweicloudsdkhss.v5.model.list_ports_response import ListPortsResponse
from huaweicloudsdkhss.v5.model.list_process_statistics_request import ListProcessStatisticsRequest
from huaweicloudsdkhss.v5.model.list_process_statistics_response import ListProcessStatisticsResponse
from huaweicloudsdkhss.v5.model.list_processes_host_request import ListProcessesHostRequest
from huaweicloudsdkhss.v5.model.list_processes_host_response import ListProcessesHostResponse
from huaweicloudsdkhss.v5.model.list_protection_policy_request import ListProtectionPolicyRequest
from huaweicloudsdkhss.v5.model.list_protection_policy_response import ListProtectionPolicyResponse
from huaweicloudsdkhss.v5.model.list_protection_server_request import ListProtectionServerRequest
from huaweicloudsdkhss.v5.model.list_protection_server_response import ListProtectionServerResponse
from huaweicloudsdkhss.v5.model.list_query_export_task_request import ListQueryExportTaskRequest
from huaweicloudsdkhss.v5.model.list_query_export_task_response import ListQueryExportTaskResponse
from huaweicloudsdkhss.v5.model.list_quotas_detail_request import ListQuotasDetailRequest
from huaweicloudsdkhss.v5.model.list_quotas_detail_response import ListQuotasDetailResponse
from huaweicloudsdkhss.v5.model.list_risk_config_check_rules_request import ListRiskConfigCheckRulesRequest
from huaweicloudsdkhss.v5.model.list_risk_config_check_rules_response import ListRiskConfigCheckRulesResponse
from huaweicloudsdkhss.v5.model.list_risk_config_hosts_request import ListRiskConfigHostsRequest
from huaweicloudsdkhss.v5.model.list_risk_config_hosts_response import ListRiskConfigHostsResponse
from huaweicloudsdkhss.v5.model.list_risk_configs_request import ListRiskConfigsRequest
from huaweicloudsdkhss.v5.model.list_risk_configs_response import ListRiskConfigsResponse
from huaweicloudsdkhss.v5.model.list_security_events_request import ListSecurityEventsRequest
from huaweicloudsdkhss.v5.model.list_security_events_response import ListSecurityEventsResponse
from huaweicloudsdkhss.v5.model.list_swr_image_repository_request import ListSwrImageRepositoryRequest
from huaweicloudsdkhss.v5.model.list_swr_image_repository_response import ListSwrImageRepositoryResponse
from huaweicloudsdkhss.v5.model.list_user_change_histories_request import ListUserChangeHistoriesRequest
from huaweicloudsdkhss.v5.model.list_user_change_histories_response import ListUserChangeHistoriesResponse
from huaweicloudsdkhss.v5.model.list_user_statistics_request import ListUserStatisticsRequest
from huaweicloudsdkhss.v5.model.list_user_statistics_response import ListUserStatisticsResponse
from huaweicloudsdkhss.v5.model.list_users_request import ListUsersRequest
from huaweicloudsdkhss.v5.model.list_users_response import ListUsersResponse
from huaweicloudsdkhss.v5.model.list_vul_hosts_request import ListVulHostsRequest
from huaweicloudsdkhss.v5.model.list_vul_hosts_response import ListVulHostsResponse
from huaweicloudsdkhss.v5.model.list_vul_scan_task_host_request import ListVulScanTaskHostRequest
from huaweicloudsdkhss.v5.model.list_vul_scan_task_host_response import ListVulScanTaskHostResponse
from huaweicloudsdkhss.v5.model.list_vul_scan_task_request import ListVulScanTaskRequest
from huaweicloudsdkhss.v5.model.list_vul_scan_task_response import ListVulScanTaskResponse
from huaweicloudsdkhss.v5.model.list_vulnerabilities_request import ListVulnerabilitiesRequest
from huaweicloudsdkhss.v5.model.list_vulnerabilities_response import ListVulnerabilitiesResponse
from huaweicloudsdkhss.v5.model.list_vulnerability_cve_request import ListVulnerabilityCveRequest
from huaweicloudsdkhss.v5.model.list_vulnerability_cve_response import ListVulnerabilityCveResponse
from huaweicloudsdkhss.v5.model.list_weak_password_users_request import ListWeakPasswordUsersRequest
from huaweicloudsdkhss.v5.model.list_weak_password_users_response import ListWeakPasswordUsersResponse
from huaweicloudsdkhss.v5.model.list_wtp_protect_host_request import ListWtpProtectHostRequest
from huaweicloudsdkhss.v5.model.list_wtp_protect_host_response import ListWtpProtectHostResponse
from huaweicloudsdkhss.v5.model.login_ip import LoginIp
from huaweicloudsdkhss.v5.model.login_type import LoginType
from huaweicloudsdkhss.v5.model.login_user_name import LoginUserName
from huaweicloudsdkhss.v5.model.malware_name import MalwareName
from huaweicloudsdkhss.v5.model.manual_vul_scan_request_info import ManualVulScanRequestInfo
from huaweicloudsdkhss.v5.model.occur_time import OccurTime
from huaweicloudsdkhss.v5.model.operate_event_request_info import OperateEventRequestInfo
from huaweicloudsdkhss.v5.model.operate_type import OperateType
from huaweicloudsdkhss.v5.model.operation_definition_info import OperationDefinitionInfo
from huaweicloudsdkhss.v5.model.operation_definition_request_info import OperationDefinitionRequestInfo
from huaweicloudsdkhss.v5.model.organization_node_response_info import OrganizationNodeResponseInfo
from huaweicloudsdkhss.v5.model.os_type import OsType
from huaweicloudsdkhss.v5.model.policy_group_id import PolicyGroupId
from huaweicloudsdkhss.v5.model.policy_group_name import PolicyGroupName
from huaweicloudsdkhss.v5.model.policy_group_response_info import PolicyGroupResponseInfo
from huaweicloudsdkhss.v5.model.port_host_response_info import PortHostResponseInfo
from huaweicloudsdkhss.v5.model.port_response_info import PortResponseInfo
from huaweicloudsdkhss.v5.model.port_statistic_response_info import PortStatisticResponseInfo
from huaweicloudsdkhss.v5.model.private_image_repository_info import PrivateImageRepositoryInfo
from huaweicloudsdkhss.v5.model.private_ip import PrivateIp
from huaweicloudsdkhss.v5.model.process_pid import ProcessPid
from huaweicloudsdkhss.v5.model.process_statistic_response_info import ProcessStatisticResponseInfo
from huaweicloudsdkhss.v5.model.processes_host_response_info import ProcessesHostResponseInfo
from huaweicloudsdkhss.v5.model.protection_info_request_info import ProtectionInfoRequestInfo
from huaweicloudsdkhss.v5.model.protection_policy_info import ProtectionPolicyInfo
from huaweicloudsdkhss.v5.model.protection_proxy_info_request_info import ProtectionProxyInfoRequestInfo
from huaweicloudsdkhss.v5.model.protection_server_info import ProtectionServerInfo
from huaweicloudsdkhss.v5.model.protection_server_info_backup_error import ProtectionServerInfoBackupError
from huaweicloudsdkhss.v5.model.public_ip import PublicIp
from huaweicloudsdkhss.v5.model.pwd_policy_info_response_info import PwdPolicyInfoResponseInfo
from huaweicloudsdkhss.v5.model.quota_resources_response_info import QuotaResourcesResponseInfo
from huaweicloudsdkhss.v5.model.quota_statistics_response_info import QuotaStatisticsResponseInfo
from huaweicloudsdkhss.v5.model.repair_priority_list_info import RepairPriorityListInfo
from huaweicloudsdkhss.v5.model.resource_info import ResourceInfo
from huaweicloudsdkhss.v5.model.resource_product_data_object_info import ResourceProductDataObjectInfo
from huaweicloudsdkhss.v5.model.resource_quotas_info import ResourceQuotasInfo
from huaweicloudsdkhss.v5.model.resource_tag_info import ResourceTagInfo
from huaweicloudsdkhss.v5.model.result_id import ResultId
from huaweicloudsdkhss.v5.model.risk_host_num import RiskHostNum
from huaweicloudsdkhss.v5.model.run_image_synchronize_request import RunImageSynchronizeRequest
from huaweicloudsdkhss.v5.model.run_image_synchronize_request_info import RunImageSynchronizeRequestInfo
from huaweicloudsdkhss.v5.model.run_image_synchronize_response import RunImageSynchronizeResponse
from huaweicloudsdkhss.v5.model.runtime_request_body import RuntimeRequestBody
from huaweicloudsdkhss.v5.model.security_check_host_info_response_info import SecurityCheckHostInfoResponseInfo
from huaweicloudsdkhss.v5.model.security_check_info_response_info import SecurityCheckInfoResponseInfo
from huaweicloudsdkhss.v5.model.set_rasp_switch_request import SetRaspSwitchRequest
from huaweicloudsdkhss.v5.model.set_rasp_switch_request_info import SetRaspSwitchRequestInfo
from huaweicloudsdkhss.v5.model.set_rasp_switch_response import SetRaspSwitchResponse
from huaweicloudsdkhss.v5.model.set_wtp_protection_status_info_request import SetWtpProtectionStatusInfoRequest
from huaweicloudsdkhss.v5.model.set_wtp_protection_status_info_response import SetWtpProtectionStatusInfoResponse
from huaweicloudsdkhss.v5.model.set_wtp_protection_status_request_info import SetWtpProtectionStatusRequestInfo
from huaweicloudsdkhss.v5.model.severity import Severity
from huaweicloudsdkhss.v5.model.show_asset_statistic_request import ShowAssetStatisticRequest
from huaweicloudsdkhss.v5.model.show_asset_statistic_response import ShowAssetStatisticResponse
from huaweicloudsdkhss.v5.model.show_backup_policy_info_request import ShowBackupPolicyInfoRequest
from huaweicloudsdkhss.v5.model.show_backup_policy_info_response import ShowBackupPolicyInfoResponse
from huaweicloudsdkhss.v5.model.show_check_rule_detail_request import ShowCheckRuleDetailRequest
from huaweicloudsdkhss.v5.model.show_check_rule_detail_response import ShowCheckRuleDetailResponse
from huaweicloudsdkhss.v5.model.show_image_check_rule_detail_request import ShowImageCheckRuleDetailRequest
from huaweicloudsdkhss.v5.model.show_image_check_rule_detail_response import ShowImageCheckRuleDetailResponse
from huaweicloudsdkhss.v5.model.show_period_response_info import ShowPeriodResponseInfo
from huaweicloudsdkhss.v5.model.show_productdata_offering_infos_request import ShowProductdataOfferingInfosRequest
from huaweicloudsdkhss.v5.model.show_productdata_offering_infos_response import ShowProductdataOfferingInfosResponse
from huaweicloudsdkhss.v5.model.show_resource_quotas_request import ShowResourceQuotasRequest
from huaweicloudsdkhss.v5.model.show_resource_quotas_response import ShowResourceQuotasResponse
from huaweicloudsdkhss.v5.model.show_risk_config_detail_request import ShowRiskConfigDetailRequest
from huaweicloudsdkhss.v5.model.show_risk_config_detail_response import ShowRiskConfigDetailResponse
from huaweicloudsdkhss.v5.model.show_vul_scan_policy_request import ShowVulScanPolicyRequest
from huaweicloudsdkhss.v5.model.show_vul_scan_policy_response import ShowVulScanPolicyResponse
from huaweicloudsdkhss.v5.model.show_vul_statics_request import ShowVulStaticsRequest
from huaweicloudsdkhss.v5.model.show_vul_statics_response import ShowVulStaticsResponse
from huaweicloudsdkhss.v5.model.src_ip import SrcIp
from huaweicloudsdkhss.v5.model.start_protection_request import StartProtectionRequest
from huaweicloudsdkhss.v5.model.start_protection_response import StartProtectionResponse
from huaweicloudsdkhss.v5.model.stop_protection_request import StopProtectionRequest
from huaweicloudsdkhss.v5.model.stop_protection_response import StopProtectionResponse
from huaweicloudsdkhss.v5.model.support_os import SupportOs
from huaweicloudsdkhss.v5.model.support_version import SupportVersion
from huaweicloudsdkhss.v5.model.switch_hosts_protect_status_request import SwitchHostsProtectStatusRequest
from huaweicloudsdkhss.v5.model.switch_hosts_protect_status_request_info import SwitchHostsProtectStatusRequestInfo
from huaweicloudsdkhss.v5.model.switch_hosts_protect_status_response import SwitchHostsProtectStatusResponse
from huaweicloudsdkhss.v5.model.tag_info import TagInfo
from huaweicloudsdkhss.v5.model.total_num import TotalNum
from huaweicloudsdkhss.v5.model.trust_process_info import TrustProcessInfo
from huaweicloudsdkhss.v5.model.unprotect_host_num import UnprotectHostNum
from huaweicloudsdkhss.v5.model.update_agent_daemonset_request import UpdateAgentDaemonsetRequest
from huaweicloudsdkhss.v5.model.update_agent_daemonset_response import UpdateAgentDaemonsetResponse
from huaweicloudsdkhss.v5.model.update_backup_policy_info_request import UpdateBackupPolicyInfoRequest
from huaweicloudsdkhss.v5.model.update_backup_policy_info_response import UpdateBackupPolicyInfoResponse
from huaweicloudsdkhss.v5.model.update_backup_policy_request_info import UpdateBackupPolicyRequestInfo
from huaweicloudsdkhss.v5.model.update_backup_policy_request_info1 import UpdateBackupPolicyRequestInfo1
from huaweicloudsdkhss.v5.model.update_daemonset_request_body import UpdateDaemonsetRequestBody
from huaweicloudsdkhss.v5.model.update_daemonset_request_body_schedule_info import UpdateDaemonsetRequestBodyScheduleInfo
from huaweicloudsdkhss.v5.model.update_protection_policy_info_request_info import UpdateProtectionPolicyInfoRequestInfo
from huaweicloudsdkhss.v5.model.update_protection_policy_request import UpdateProtectionPolicyRequest
from huaweicloudsdkhss.v5.model.update_protection_policy_response import UpdateProtectionPolicyResponse
from huaweicloudsdkhss.v5.model.update_time import UpdateTime
from huaweicloudsdkhss.v5.model.user_change_history_response_info import UserChangeHistoryResponseInfo
from huaweicloudsdkhss.v5.model.user_response_info import UserResponseInfo
from huaweicloudsdkhss.v5.model.user_statistic_info_response_info import UserStatisticInfoResponseInfo
from huaweicloudsdkhss.v5.model.vul_host_info import VulHostInfo
from huaweicloudsdkhss.v5.model.vul_host_info_disabled_operate_types import VulHostInfoDisabledOperateTypes
from huaweicloudsdkhss.v5.model.vul_info import VulInfo
from huaweicloudsdkhss.v5.model.vul_info_cve_list import VulInfoCveList
from huaweicloudsdkhss.v5.model.vul_operate_info import VulOperateInfo
from huaweicloudsdkhss.v5.model.vul_scan_task_host_info import VulScanTaskHostInfo
from huaweicloudsdkhss.v5.model.vul_scan_task_host_info_failed_reasons import VulScanTaskHostInfoFailedReasons
from huaweicloudsdkhss.v5.model.vul_scan_task_info import VulScanTaskInfo
from huaweicloudsdkhss.v5.model.vulnerability_host_number_info import VulnerabilityHostNumberInfo
from huaweicloudsdkhss.v5.model.weak_pwd_account_info_response_info import WeakPwdAccountInfoResponseInfo
from huaweicloudsdkhss.v5.model.weak_pwd_list_info_response_info import WeakPwdListInfoResponseInfo
from huaweicloudsdkhss.v5.model.wtp_protect_host_response_info import WtpProtectHostResponseInfo

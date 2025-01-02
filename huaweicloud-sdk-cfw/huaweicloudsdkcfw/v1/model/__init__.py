# coding: utf-8

from __future__ import absolute_import

# import models into model package
from huaweicloudsdkcfw.v1.model.add_acl_rule_request import AddAclRuleRequest
from huaweicloudsdkcfw.v1.model.add_acl_rule_response import AddAclRuleResponse
from huaweicloudsdkcfw.v1.model.add_address_item_request import AddAddressItemRequest
from huaweicloudsdkcfw.v1.model.add_address_item_response import AddAddressItemResponse
from huaweicloudsdkcfw.v1.model.add_address_items_info_dto import AddAddressItemsInfoDto
from huaweicloudsdkcfw.v1.model.add_address_items_info_dto_address_items import AddAddressItemsInfoDtoAddressItems
from huaweicloudsdkcfw.v1.model.add_address_set_dto import AddAddressSetDto
from huaweicloudsdkcfw.v1.model.add_address_set_request import AddAddressSetRequest
from huaweicloudsdkcfw.v1.model.add_address_set_response import AddAddressSetResponse
from huaweicloudsdkcfw.v1.model.add_black_white_list_dto import AddBlackWhiteListDto
from huaweicloudsdkcfw.v1.model.add_black_white_list_request import AddBlackWhiteListRequest
from huaweicloudsdkcfw.v1.model.add_black_white_list_response import AddBlackWhiteListResponse
from huaweicloudsdkcfw.v1.model.add_domain_list_dto import AddDomainListDto
from huaweicloudsdkcfw.v1.model.add_domain_set_info_dto import AddDomainSetInfoDto
from huaweicloudsdkcfw.v1.model.add_domain_set_request import AddDomainSetRequest
from huaweicloudsdkcfw.v1.model.add_domain_set_response import AddDomainSetResponse
from huaweicloudsdkcfw.v1.model.add_domains_request import AddDomainsRequest
from huaweicloudsdkcfw.v1.model.add_domains_response import AddDomainsResponse
from huaweicloudsdkcfw.v1.model.add_log_config_request import AddLogConfigRequest
from huaweicloudsdkcfw.v1.model.add_log_config_response import AddLogConfigResponse
from huaweicloudsdkcfw.v1.model.add_rule_acl_dto import AddRuleAclDto
from huaweicloudsdkcfw.v1.model.add_rule_acl_dto_rules import AddRuleAclDtoRules
from huaweicloudsdkcfw.v1.model.add_service_items_request import AddServiceItemsRequest
from huaweicloudsdkcfw.v1.model.add_service_items_response import AddServiceItemsResponse
from huaweicloudsdkcfw.v1.model.add_service_items_using_post_request_body import AddServiceItemsUsingPOSTRequestBody
from huaweicloudsdkcfw.v1.model.add_service_items_using_post_request_body_service_items import AddServiceItemsUsingPOSTRequestBodyServiceItems
from huaweicloudsdkcfw.v1.model.add_service_set_request import AddServiceSetRequest
from huaweicloudsdkcfw.v1.model.add_service_set_response import AddServiceSetResponse
from huaweicloudsdkcfw.v1.model.add_service_set_using_post_request_body import AddServiceSetUsingPOSTRequestBody
from huaweicloudsdkcfw.v1.model.address_group_vo import AddressGroupVO
from huaweicloudsdkcfw.v1.model.address_item_id import AddressItemId
from huaweicloudsdkcfw.v1.model.address_item_id_without_name import AddressItemIdWithoutName
from huaweicloudsdkcfw.v1.model.address_item_list_response_dto_data import AddressItemListResponseDTOData
from huaweicloudsdkcfw.v1.model.address_item_list_response_dto_data_records import AddressItemListResponseDTODataRecords
from huaweicloudsdkcfw.v1.model.address_items import AddressItems
from huaweicloudsdkcfw.v1.model.address_set_detail_response_dto_data import AddressSetDetailResponseDTOData
from huaweicloudsdkcfw.v1.model.address_set_id import AddressSetId
from huaweicloudsdkcfw.v1.model.address_set_list_response_dto_data import AddressSetListResponseDTOData
from huaweicloudsdkcfw.v1.model.address_set_list_response_dto_data_records import AddressSetListResponseDTODataRecords
from huaweicloudsdkcfw.v1.model.advanced_ips_rule_dto import AdvancedIpsRuleDto
from huaweicloudsdkcfw.v1.model.advanced_ips_rule_list_vo import AdvancedIpsRuleListVo
from huaweicloudsdkcfw.v1.model.advanced_ips_rule_vo import AdvancedIpsRuleVo
from huaweicloudsdkcfw.v1.model.alarm_config import AlarmConfig
from huaweicloudsdkcfw.v1.model.anti_virus_rule_dto import AntiVirusRuleDto
from huaweicloudsdkcfw.v1.model.anti_virus_rule_vo import AntiVirusRuleVO
from huaweicloudsdkcfw.v1.model.anti_virus_switch_dto import AntiVirusSwitchDto
from huaweicloudsdkcfw.v1.model.anti_virus_vo import AntiVirusVO
from huaweicloudsdkcfw.v1.model.batch_delete_acl_rules_request import BatchDeleteAclRulesRequest
from huaweicloudsdkcfw.v1.model.batch_delete_acl_rules_response import BatchDeleteAclRulesResponse
from huaweicloudsdkcfw.v1.model.batch_delete_acl_rules_response_data import BatchDeleteAclRulesResponseData
from huaweicloudsdkcfw.v1.model.batch_delete_address_items_request import BatchDeleteAddressItemsRequest
from huaweicloudsdkcfw.v1.model.batch_delete_address_items_response import BatchDeleteAddressItemsResponse
from huaweicloudsdkcfw.v1.model.batch_delete_domain_set_request import BatchDeleteDomainSetRequest
from huaweicloudsdkcfw.v1.model.batch_delete_domain_set_response import BatchDeleteDomainSetResponse
from huaweicloudsdkcfw.v1.model.batch_delete_domain_sets_dto import BatchDeleteDomainSetsDto
from huaweicloudsdkcfw.v1.model.batch_delete_rule_info import BatchDeleteRuleInfo
from huaweicloudsdkcfw.v1.model.batch_delete_service_items_request import BatchDeleteServiceItemsRequest
from huaweicloudsdkcfw.v1.model.batch_delete_service_items_response import BatchDeleteServiceItemsResponse
from huaweicloudsdkcfw.v1.model.batch_update_acl_rule_actions_request import BatchUpdateAclRuleActionsRequest
from huaweicloudsdkcfw.v1.model.batch_update_acl_rule_actions_response import BatchUpdateAclRuleActionsResponse
from huaweicloudsdkcfw.v1.model.black_white_list_id import BlackWhiteListId
from huaweicloudsdkcfw.v1.model.black_white_list_response_data import BlackWhiteListResponseData
from huaweicloudsdkcfw.v1.model.black_white_list_response_data_records import BlackWhiteListResponseDataRecords
from huaweicloudsdkcfw.v1.model.cancel_capture_task_dto import CancelCaptureTaskDto
from huaweicloudsdkcfw.v1.model.cancel_capture_task_request import CancelCaptureTaskRequest
from huaweicloudsdkcfw.v1.model.cancel_capture_task_response import CancelCaptureTaskResponse
from huaweicloudsdkcfw.v1.model.capture_file import CaptureFile
from huaweicloudsdkcfw.v1.model.capture_result_url_vo import CaptureResultUrlVO
from huaweicloudsdkcfw.v1.model.capture_rule_address_dto import CaptureRuleAddressDto
from huaweicloudsdkcfw.v1.model.capture_service_dto import CaptureServiceDto
from huaweicloudsdkcfw.v1.model.capture_task_dto import CaptureTaskDto
from huaweicloudsdkcfw.v1.model.capture_task_id import CaptureTaskId
from huaweicloudsdkcfw.v1.model.capture_task_vo import CaptureTaskVO
from huaweicloudsdkcfw.v1.model.change_east_west_firewall_status_request import ChangeEastWestFirewallStatusRequest
from huaweicloudsdkcfw.v1.model.change_east_west_firewall_status_response import ChangeEastWestFirewallStatusResponse
from huaweicloudsdkcfw.v1.model.change_east_west_firewall_status_response_data import ChangeEastWestFirewallStatusResponseData
from huaweicloudsdkcfw.v1.model.change_eip_status_request import ChangeEipStatusRequest
from huaweicloudsdkcfw.v1.model.change_eip_status_response import ChangeEipStatusResponse
from huaweicloudsdkcfw.v1.model.change_ips_protect_mode_request import ChangeIpsProtectModeRequest
from huaweicloudsdkcfw.v1.model.change_ips_protect_mode_response import ChangeIpsProtectModeResponse
from huaweicloudsdkcfw.v1.model.change_ips_rule_mode_request import ChangeIpsRuleModeRequest
from huaweicloudsdkcfw.v1.model.change_ips_rule_mode_response import ChangeIpsRuleModeResponse
from huaweicloudsdkcfw.v1.model.change_ips_switch_status_request import ChangeIpsSwitchStatusRequest
from huaweicloudsdkcfw.v1.model.change_ips_switch_status_response import ChangeIpsSwitchStatusResponse
from huaweicloudsdkcfw.v1.model.change_protect_status_request_body import ChangeProtectStatusRequestBody
from huaweicloudsdkcfw.v1.model.clear_access_log_rule_hit_counts_dto import ClearAccessLogRuleHitCountsDto
from huaweicloudsdkcfw.v1.model.common_response_dto_data import CommonResponseDTOData
from huaweicloudsdkcfw.v1.model.covered_ipvo import CoveredIPVO
from huaweicloudsdkcfw.v1.model.create_capture_task_request import CreateCaptureTaskRequest
from huaweicloudsdkcfw.v1.model.create_capture_task_response import CreateCaptureTaskResponse
from huaweicloudsdkcfw.v1.model.create_ew_firewall_inspect_vpc_resp import CreateEWFirewallInspectVpcResp
from huaweicloudsdkcfw.v1.model.create_ew_firewall_resp import CreateEWFirewallResp
from huaweicloudsdkcfw.v1.model.create_east_west_firewall_request import CreateEastWestFirewallRequest
from huaweicloudsdkcfw.v1.model.create_east_west_firewall_request_body import CreateEastWestFirewallRequestBody
from huaweicloudsdkcfw.v1.model.create_east_west_firewall_response import CreateEastWestFirewallResponse
from huaweicloudsdkcfw.v1.model.create_firewall_req import CreateFirewallReq
from huaweicloudsdkcfw.v1.model.create_firewall_req_charge_info import CreateFirewallReqChargeInfo
from huaweicloudsdkcfw.v1.model.create_firewall_req_flavor import CreateFirewallReqFlavor
from huaweicloudsdkcfw.v1.model.create_firewall_req_tags import CreateFirewallReqTags
from huaweicloudsdkcfw.v1.model.create_firewall_request import CreateFirewallRequest
from huaweicloudsdkcfw.v1.model.create_firewall_response import CreateFirewallResponse
from huaweicloudsdkcfw.v1.model.create_tag import CreateTag
from huaweicloudsdkcfw.v1.model.create_tag_request import CreateTagRequest
from huaweicloudsdkcfw.v1.model.create_tag_response import CreateTagResponse
from huaweicloudsdkcfw.v1.model.create_tags_dto import CreateTagsDto
from huaweicloudsdkcfw.v1.model.customer_ips_list_vo import CustomerIpsListVO
from huaweicloudsdkcfw.v1.model.delete_acl_rule_hit_count_request import DeleteAclRuleHitCountRequest
from huaweicloudsdkcfw.v1.model.delete_acl_rule_hit_count_response import DeleteAclRuleHitCountResponse
from huaweicloudsdkcfw.v1.model.delete_acl_rule_request import DeleteAclRuleRequest
from huaweicloudsdkcfw.v1.model.delete_acl_rule_response import DeleteAclRuleResponse
from huaweicloudsdkcfw.v1.model.delete_address_item_request import DeleteAddressItemRequest
from huaweicloudsdkcfw.v1.model.delete_address_item_response import DeleteAddressItemResponse
from huaweicloudsdkcfw.v1.model.delete_address_items_info_dto import DeleteAddressItemsInfoDto
from huaweicloudsdkcfw.v1.model.delete_address_set_request import DeleteAddressSetRequest
from huaweicloudsdkcfw.v1.model.delete_address_set_response import DeleteAddressSetResponse
from huaweicloudsdkcfw.v1.model.delete_black_white_list_request import DeleteBlackWhiteListRequest
from huaweicloudsdkcfw.v1.model.delete_black_white_list_response import DeleteBlackWhiteListResponse
from huaweicloudsdkcfw.v1.model.delete_capture_task_dto import DeleteCaptureTaskDto
from huaweicloudsdkcfw.v1.model.delete_capture_task_request import DeleteCaptureTaskRequest
from huaweicloudsdkcfw.v1.model.delete_capture_task_response import DeleteCaptureTaskResponse
from huaweicloudsdkcfw.v1.model.delete_domain_dto import DeleteDomainDto
from huaweicloudsdkcfw.v1.model.delete_domain_set_request import DeleteDomainSetRequest
from huaweicloudsdkcfw.v1.model.delete_domain_set_response import DeleteDomainSetResponse
from huaweicloudsdkcfw.v1.model.delete_domains_request import DeleteDomainsRequest
from huaweicloudsdkcfw.v1.model.delete_domains_response import DeleteDomainsResponse
from huaweicloudsdkcfw.v1.model.delete_firewall_request import DeleteFirewallRequest
from huaweicloudsdkcfw.v1.model.delete_firewall_response import DeleteFirewallResponse
from huaweicloudsdkcfw.v1.model.delete_rule_acl_dto import DeleteRuleAclDto
from huaweicloudsdkcfw.v1.model.delete_service_item_dto import DeleteServiceItemDto
from huaweicloudsdkcfw.v1.model.delete_service_item_request import DeleteServiceItemRequest
from huaweicloudsdkcfw.v1.model.delete_service_item_response import DeleteServiceItemResponse
from huaweicloudsdkcfw.v1.model.delete_service_item_response_body_data import DeleteServiceItemResponseBodyData
from huaweicloudsdkcfw.v1.model.delete_service_set_request import DeleteServiceSetRequest
from huaweicloudsdkcfw.v1.model.delete_service_set_response import DeleteServiceSetResponse
from huaweicloudsdkcfw.v1.model.delete_tag_request import DeleteTagRequest
from huaweicloudsdkcfw.v1.model.delete_tag_response import DeleteTagResponse
from huaweicloudsdkcfw.v1.model.delete_tags_dto import DeleteTagsDto
from huaweicloudsdkcfw.v1.model.dns_servers_response_dto import DnsServersResponseDTO
from huaweicloudsdkcfw.v1.model.domain_info import DomainInfo
from huaweicloudsdkcfw.v1.model.domain_set_info_dto import DomainSetInfoDto
from huaweicloudsdkcfw.v1.model.domain_set_response_data import DomainSetResponseData
from huaweicloudsdkcfw.v1.model.domain_set_vo import DomainSetVo
from huaweicloudsdkcfw.v1.model.eip_switch_status_vo import EIPSwitchStatusVO
from huaweicloudsdkcfw.v1.model.eip_count_resp_data import EipCountRespData
from huaweicloudsdkcfw.v1.model.eip_operate_protect_req import EipOperateProtectReq
from huaweicloudsdkcfw.v1.model.eip_operate_protect_req_ip_infos import EipOperateProtectReqIpInfos
from huaweicloudsdkcfw.v1.model.eip_resource import EipResource
from huaweicloudsdkcfw.v1.model.eip_response_data import EipResponseData
from huaweicloudsdkcfw.v1.model.er import Er
from huaweicloudsdkcfw.v1.model.er_instance import ErInstance
from huaweicloudsdkcfw.v1.model.ew_protect_resource_info import EwProtectResourceInfo
from huaweicloudsdkcfw.v1.model.failed_eip_info import FailedEipInfo
from huaweicloudsdkcfw.v1.model.firewall_instance_resource import FirewallInstanceResource
from huaweicloudsdkcfw.v1.model.firewall_instance_vo import FirewallInstanceVO
from huaweicloudsdkcfw.v1.model.firewall_status_vo import FirewallStatusVO
from huaweicloudsdkcfw.v1.model.flavor import Flavor
from huaweicloudsdkcfw.v1.model.get_create_firewall_job_response_data import GetCreateFirewallJobResponseData
from huaweicloudsdkcfw.v1.model.get_east_west_firewall_response_body import GetEastWestFirewallResponseBody
from huaweicloudsdkcfw.v1.model.get_firewall_instance_data import GetFirewallInstanceData
from huaweicloudsdkcfw.v1.model.get_firewall_instance_response_record import GetFirewallInstanceResponseRecord
from huaweicloudsdkcfw.v1.model.host_header_info import HostHeaderInfo
from huaweicloudsdkcfw.v1.model.http_firewall_instance_list_response_data import HttpFirewallInstanceListResponseData
from huaweicloudsdkcfw.v1.model.http_get_acl_tag_response_data import HttpGetAclTagResponseData
from huaweicloudsdkcfw.v1.model.http_list_customer_ips_response_data import HttpListCustomerIpsResponseData
from huaweicloudsdkcfw.v1.model.http_query_capture_task_response_data import HttpQueryCaptureTaskResponseData
from huaweicloudsdkcfw.v1.model.http_query_cfw_access_controller_logs_response_dto_data import HttpQueryCfwAccessControllerLogsResponseDTOData
from huaweicloudsdkcfw.v1.model.http_query_cfw_access_controller_logs_response_dto_data_records import HttpQueryCfwAccessControllerLogsResponseDTODataRecords
from huaweicloudsdkcfw.v1.model.http_query_cfw_attack_logs_response_dto_data import HttpQueryCfwAttackLogsResponseDTOData
from huaweicloudsdkcfw.v1.model.http_query_cfw_attack_logs_response_dto_data_records import HttpQueryCfwAttackLogsResponseDTODataRecords
from huaweicloudsdkcfw.v1.model.http_query_cfw_flow_logs_response_dto_data import HttpQueryCfwFlowLogsResponseDTOData
from huaweicloudsdkcfw.v1.model.http_query_cfw_flow_logs_response_dto_data_records import HttpQueryCfwFlowLogsResponseDTODataRecords
from huaweicloudsdkcfw.v1.model.ip_region_dto import IpRegionDto
from huaweicloudsdkcfw.v1.model.ips_protect_dto import IpsProtectDTO
from huaweicloudsdkcfw.v1.model.ips_protect_mode_object import IpsProtectModeObject
from huaweicloudsdkcfw.v1.model.ips_rule_change_dto import IpsRuleChangeDto
from huaweicloudsdkcfw.v1.model.ips_rule_change_resp_body import IpsRuleChangeRespBody
from huaweicloudsdkcfw.v1.model.ips_rule_list_vo import IpsRuleListVO
from huaweicloudsdkcfw.v1.model.ips_rule_update_time_vo import IpsRuleUpdateTimeVO
from huaweicloudsdkcfw.v1.model.ips_rule_vo import IpsRuleVO
from huaweicloudsdkcfw.v1.model.ips_switch_dto import IpsSwitchDTO
from huaweicloudsdkcfw.v1.model.ips_switch_response_dto import IpsSwitchResponseDTO
from huaweicloudsdkcfw.v1.model.list_access_control_logs_request import ListAccessControlLogsRequest
from huaweicloudsdkcfw.v1.model.list_access_control_logs_response import ListAccessControlLogsResponse
from huaweicloudsdkcfw.v1.model.list_acl_rule_hit_count_request import ListAclRuleHitCountRequest
from huaweicloudsdkcfw.v1.model.list_acl_rule_hit_count_response import ListAclRuleHitCountResponse
from huaweicloudsdkcfw.v1.model.list_acl_rules_request import ListAclRulesRequest
from huaweicloudsdkcfw.v1.model.list_acl_rules_response import ListAclRulesResponse
from huaweicloudsdkcfw.v1.model.list_address_items_request import ListAddressItemsRequest
from huaweicloudsdkcfw.v1.model.list_address_items_response import ListAddressItemsResponse
from huaweicloudsdkcfw.v1.model.list_address_set_detail_request import ListAddressSetDetailRequest
from huaweicloudsdkcfw.v1.model.list_address_set_detail_response import ListAddressSetDetailResponse
from huaweicloudsdkcfw.v1.model.list_address_sets_request import ListAddressSetsRequest
from huaweicloudsdkcfw.v1.model.list_address_sets_response import ListAddressSetsResponse
from huaweicloudsdkcfw.v1.model.list_alarm_whitelist_request import ListAlarmWhitelistRequest
from huaweicloudsdkcfw.v1.model.list_alarm_whitelist_response import ListAlarmWhitelistResponse
from huaweicloudsdkcfw.v1.model.list_attack_logs_request import ListAttackLogsRequest
from huaweicloudsdkcfw.v1.model.list_attack_logs_response import ListAttackLogsResponse
from huaweicloudsdkcfw.v1.model.list_black_white_lists_request import ListBlackWhiteListsRequest
from huaweicloudsdkcfw.v1.model.list_black_white_lists_response import ListBlackWhiteListsResponse
from huaweicloudsdkcfw.v1.model.list_capture_result_request import ListCaptureResultRequest
from huaweicloudsdkcfw.v1.model.list_capture_result_response import ListCaptureResultResponse
from huaweicloudsdkcfw.v1.model.list_capture_task_request import ListCaptureTaskRequest
from huaweicloudsdkcfw.v1.model.list_capture_task_response import ListCaptureTaskResponse
from huaweicloudsdkcfw.v1.model.list_customer_ips_request import ListCustomerIpsRequest
from huaweicloudsdkcfw.v1.model.list_customer_ips_response import ListCustomerIpsResponse
from huaweicloudsdkcfw.v1.model.list_dns_servers_request import ListDnsServersRequest
from huaweicloudsdkcfw.v1.model.list_dns_servers_response import ListDnsServersResponse
from huaweicloudsdkcfw.v1.model.list_domain_parse_detail_request import ListDomainParseDetailRequest
from huaweicloudsdkcfw.v1.model.list_domain_parse_detail_response import ListDomainParseDetailResponse
from huaweicloudsdkcfw.v1.model.list_domain_parse_ip_request import ListDomainParseIpRequest
from huaweicloudsdkcfw.v1.model.list_domain_parse_ip_response import ListDomainParseIpResponse
from huaweicloudsdkcfw.v1.model.list_domain_response_data import ListDomainResponseData
from huaweicloudsdkcfw.v1.model.list_domain_sets_request import ListDomainSetsRequest
from huaweicloudsdkcfw.v1.model.list_domain_sets_response import ListDomainSetsResponse
from huaweicloudsdkcfw.v1.model.list_domains_request import ListDomainsRequest
from huaweicloudsdkcfw.v1.model.list_domains_response import ListDomainsResponse
from huaweicloudsdkcfw.v1.model.list_domainsets_response_data import ListDomainsetsResponseData
from huaweicloudsdkcfw.v1.model.list_east_west_firewall_request import ListEastWestFirewallRequest
from huaweicloudsdkcfw.v1.model.list_east_west_firewall_response import ListEastWestFirewallResponse
from huaweicloudsdkcfw.v1.model.list_eip_count_request import ListEipCountRequest
from huaweicloudsdkcfw.v1.model.list_eip_count_response import ListEipCountResponse
from huaweicloudsdkcfw.v1.model.list_eips_request import ListEipsRequest
from huaweicloudsdkcfw.v1.model.list_eips_response import ListEipsResponse
from huaweicloudsdkcfw.v1.model.list_firewall_detail_request import ListFirewallDetailRequest
from huaweicloudsdkcfw.v1.model.list_firewall_detail_response import ListFirewallDetailResponse
from huaweicloudsdkcfw.v1.model.list_firewall_list_request import ListFirewallListRequest
from huaweicloudsdkcfw.v1.model.list_firewall_list_response import ListFirewallListResponse
from huaweicloudsdkcfw.v1.model.list_flow_logs_request import ListFlowLogsRequest
from huaweicloudsdkcfw.v1.model.list_flow_logs_response import ListFlowLogsResponse
from huaweicloudsdkcfw.v1.model.list_ips_protect_mode_request import ListIpsProtectModeRequest
from huaweicloudsdkcfw.v1.model.list_ips_protect_mode_response import ListIpsProtectModeResponse
from huaweicloudsdkcfw.v1.model.list_ips_rules1_request import ListIpsRules1Request
from huaweicloudsdkcfw.v1.model.list_ips_rules1_response import ListIpsRules1Response
from huaweicloudsdkcfw.v1.model.list_ips_rules_request import ListIpsRulesRequest
from huaweicloudsdkcfw.v1.model.list_ips_rules_response import ListIpsRulesResponse
from huaweicloudsdkcfw.v1.model.list_ips_switch_status_request import ListIpsSwitchStatusRequest
from huaweicloudsdkcfw.v1.model.list_ips_switch_status_response import ListIpsSwitchStatusResponse
from huaweicloudsdkcfw.v1.model.list_job_request import ListJobRequest
from huaweicloudsdkcfw.v1.model.list_job_response import ListJobResponse
from huaweicloudsdkcfw.v1.model.list_log_config_request import ListLogConfigRequest
from huaweicloudsdkcfw.v1.model.list_log_config_response import ListLogConfigResponse
from huaweicloudsdkcfw.v1.model.list_project_tags_request import ListProjectTagsRequest
from huaweicloudsdkcfw.v1.model.list_project_tags_response import ListProjectTagsResponse
from huaweicloudsdkcfw.v1.model.list_protected_vpcs_request import ListProtectedVpcsRequest
from huaweicloudsdkcfw.v1.model.list_protected_vpcs_response import ListProtectedVpcsResponse
from huaweicloudsdkcfw.v1.model.list_regions_request import ListRegionsRequest
from huaweicloudsdkcfw.v1.model.list_regions_response import ListRegionsResponse
from huaweicloudsdkcfw.v1.model.list_resource_tags_request import ListResourceTagsRequest
from huaweicloudsdkcfw.v1.model.list_resource_tags_response import ListResourceTagsResponse
from huaweicloudsdkcfw.v1.model.list_rule_acl_tags_request import ListRuleAclTagsRequest
from huaweicloudsdkcfw.v1.model.list_rule_acl_tags_response import ListRuleAclTagsResponse
from huaweicloudsdkcfw.v1.model.list_rule_hit_count_dto import ListRuleHitCountDto
from huaweicloudsdkcfw.v1.model.list_service_items_request import ListServiceItemsRequest
from huaweicloudsdkcfw.v1.model.list_service_items_response import ListServiceItemsResponse
from huaweicloudsdkcfw.v1.model.list_service_set_detail_request import ListServiceSetDetailRequest
from huaweicloudsdkcfw.v1.model.list_service_set_detail_response import ListServiceSetDetailResponse
from huaweicloudsdkcfw.v1.model.list_service_sets_request import ListServiceSetsRequest
from huaweicloudsdkcfw.v1.model.list_service_sets_response import ListServiceSetsResponse
from huaweicloudsdkcfw.v1.model.log_config_dto import LogConfigDto
from huaweicloudsdkcfw.v1.model.mapstringstring import Mapstringstring
from huaweicloudsdkcfw.v1.model.order_rule_acl_dto import OrderRuleAclDto
from huaweicloudsdkcfw.v1.model.order_rule_id import OrderRuleId
from huaweicloudsdkcfw.v1.model.packet_message import PacketMessage
from huaweicloudsdkcfw.v1.model.page_info import PageInfo
from huaweicloudsdkcfw.v1.model.protect_object_vo import ProtectObjectVO
from huaweicloudsdkcfw.v1.model.query_fire_wall_instance_dto import QueryFireWallInstanceDto
from huaweicloudsdkcfw.v1.model.resource_tag import ResourceTag
from huaweicloudsdkcfw.v1.model.response_data import ResponseData
from huaweicloudsdkcfw.v1.model.rule_acl_list_response_dto_data import RuleAclListResponseDTOData
from huaweicloudsdkcfw.v1.model.rule_acl_list_response_dto_data_records import RuleAclListResponseDTODataRecords
from huaweicloudsdkcfw.v1.model.rule_address_dto import RuleAddressDto
from huaweicloudsdkcfw.v1.model.rule_address_dto_for_request import RuleAddressDtoForRequest
from huaweicloudsdkcfw.v1.model.rule_address_dto_for_response import RuleAddressDtoForResponse
from huaweicloudsdkcfw.v1.model.rule_hit_count_object import RuleHitCountObject
from huaweicloudsdkcfw.v1.model.rule_hit_count_records import RuleHitCountRecords
from huaweicloudsdkcfw.v1.model.rule_id import RuleId
from huaweicloudsdkcfw.v1.model.rule_id_list import RuleIdList
from huaweicloudsdkcfw.v1.model.rule_service_dto import RuleServiceDto
from huaweicloudsdkcfw.v1.model.rule_service_dto_for_response import RuleServiceDtoForResponse
from huaweicloudsdkcfw.v1.model.save_tags_request import SaveTagsRequest
from huaweicloudsdkcfw.v1.model.save_tags_response import SaveTagsResponse
from huaweicloudsdkcfw.v1.model.scan_protocol_config import ScanProtocolConfig
from huaweicloudsdkcfw.v1.model.service_group_vo import ServiceGroupVO
from huaweicloudsdkcfw.v1.model.service_item import ServiceItem
from huaweicloudsdkcfw.v1.model.service_item_ids import ServiceItemIds
from huaweicloudsdkcfw.v1.model.service_item_ids_items import ServiceItemIdsItems
from huaweicloudsdkcfw.v1.model.service_item_list_response_dto_data import ServiceItemListResponseDtoData
from huaweicloudsdkcfw.v1.model.service_item_list_response_dto_data_records import ServiceItemListResponseDtoDataRecords
from huaweicloudsdkcfw.v1.model.service_set import ServiceSet
from huaweicloudsdkcfw.v1.model.service_set_detail_response_dto import ServiceSetDetailResponseDto
from huaweicloudsdkcfw.v1.model.service_set_id import ServiceSetId
from huaweicloudsdkcfw.v1.model.service_set_records import ServiceSetRecords
from huaweicloudsdkcfw.v1.model.show_alarm_config_request import ShowAlarmConfigRequest
from huaweicloudsdkcfw.v1.model.show_alarm_config_response import ShowAlarmConfigResponse
from huaweicloudsdkcfw.v1.model.show_anti_virus_rule_request import ShowAntiVirusRuleRequest
from huaweicloudsdkcfw.v1.model.show_anti_virus_rule_response import ShowAntiVirusRuleResponse
from huaweicloudsdkcfw.v1.model.show_anti_virus_switch_request import ShowAntiVirusSwitchRequest
from huaweicloudsdkcfw.v1.model.show_anti_virus_switch_response import ShowAntiVirusSwitchResponse
from huaweicloudsdkcfw.v1.model.show_auto_protect_status_request import ShowAutoProtectStatusRequest
from huaweicloudsdkcfw.v1.model.show_auto_protect_status_response import ShowAutoProtectStatusResponse
from huaweicloudsdkcfw.v1.model.show_domain_set_detail_request import ShowDomainSetDetailRequest
from huaweicloudsdkcfw.v1.model.show_domain_set_detail_response import ShowDomainSetDetailResponse
from huaweicloudsdkcfw.v1.model.show_import_status_request import ShowImportStatusRequest
from huaweicloudsdkcfw.v1.model.show_import_status_response import ShowImportStatusResponse
from huaweicloudsdkcfw.v1.model.show_ips_update_time_request import ShowIpsUpdateTimeRequest
from huaweicloudsdkcfw.v1.model.show_ips_update_time_response import ShowIpsUpdateTimeResponse
from huaweicloudsdkcfw.v1.model.subnet_info import SubnetInfo
from huaweicloudsdkcfw.v1.model.switch_auto_protect_status_request import SwitchAutoProtectStatusRequest
from huaweicloudsdkcfw.v1.model.switch_auto_protect_status_response import SwitchAutoProtectStatusResponse
from huaweicloudsdkcfw.v1.model.switch_eip_status_dto import SwitchEipStatusDto
from huaweicloudsdkcfw.v1.model.tag_info import TagInfo
from huaweicloudsdkcfw.v1.model.tag_value import TagValue
from huaweicloudsdkcfw.v1.model.tags_vo import TagsVO
from huaweicloudsdkcfw.v1.model.update_acl_rule_order_request import UpdateAclRuleOrderRequest
from huaweicloudsdkcfw.v1.model.update_acl_rule_order_response import UpdateAclRuleOrderResponse
from huaweicloudsdkcfw.v1.model.update_acl_rule_request import UpdateAclRuleRequest
from huaweicloudsdkcfw.v1.model.update_acl_rule_response import UpdateAclRuleResponse
from huaweicloudsdkcfw.v1.model.update_address_set_dto import UpdateAddressSetDto
from huaweicloudsdkcfw.v1.model.update_address_set_request import UpdateAddressSetRequest
from huaweicloudsdkcfw.v1.model.update_address_set_response import UpdateAddressSetResponse
from huaweicloudsdkcfw.v1.model.update_address_set_response_data import UpdateAddressSetResponseData
from huaweicloudsdkcfw.v1.model.update_advanced_ips_rule_request import UpdateAdvancedIpsRuleRequest
from huaweicloudsdkcfw.v1.model.update_advanced_ips_rule_response import UpdateAdvancedIpsRuleResponse
from huaweicloudsdkcfw.v1.model.update_alarm_config_request import UpdateAlarmConfigRequest
from huaweicloudsdkcfw.v1.model.update_alarm_config_response import UpdateAlarmConfigResponse
from huaweicloudsdkcfw.v1.model.update_anti_virus_rule_request import UpdateAntiVirusRuleRequest
from huaweicloudsdkcfw.v1.model.update_anti_virus_rule_response import UpdateAntiVirusRuleResponse
from huaweicloudsdkcfw.v1.model.update_anti_virus_switch_request import UpdateAntiVirusSwitchRequest
from huaweicloudsdkcfw.v1.model.update_anti_virus_switch_response import UpdateAntiVirusSwitchResponse
from huaweicloudsdkcfw.v1.model.update_attack_log_alarm_config_dto import UpdateAttackLogAlarmConfigDto
from huaweicloudsdkcfw.v1.model.update_black_white_list_dto import UpdateBlackWhiteListDto
from huaweicloudsdkcfw.v1.model.update_black_white_list_request import UpdateBlackWhiteListRequest
from huaweicloudsdkcfw.v1.model.update_black_white_list_response import UpdateBlackWhiteListResponse
from huaweicloudsdkcfw.v1.model.update_dns_servers_request import UpdateDnsServersRequest
from huaweicloudsdkcfw.v1.model.update_dns_servers_request_body import UpdateDnsServersRequestBody
from huaweicloudsdkcfw.v1.model.update_dns_servers_request_body_dns_server import UpdateDnsServersRequestBodyDnsServer
from huaweicloudsdkcfw.v1.model.update_dns_servers_response import UpdateDnsServersResponse
from huaweicloudsdkcfw.v1.model.update_domain_set_info_dto import UpdateDomainSetInfoDto
from huaweicloudsdkcfw.v1.model.update_domain_set_request import UpdateDomainSetRequest
from huaweicloudsdkcfw.v1.model.update_domain_set_response import UpdateDomainSetResponse
from huaweicloudsdkcfw.v1.model.update_log_config_request import UpdateLogConfigRequest
from huaweicloudsdkcfw.v1.model.update_log_config_response import UpdateLogConfigResponse
from huaweicloudsdkcfw.v1.model.update_rule_acl_dto import UpdateRuleAclDto
from huaweicloudsdkcfw.v1.model.update_security_polcies_action_dto import UpdateSecurityPolciesActionDto
from huaweicloudsdkcfw.v1.model.update_service_set_request import UpdateServiceSetRequest
from huaweicloudsdkcfw.v1.model.update_service_set_response import UpdateServiceSetResponse
from huaweicloudsdkcfw.v1.model.update_service_set_using_put_request_body import UpdateServiceSetUsingPUTRequestBody
from huaweicloudsdkcfw.v1.model.use_rule_vo import UseRuleVO
from huaweicloudsdkcfw.v1.model.vpc_protects_vo import VPCProtectsVo
from huaweicloudsdkcfw.v1.model.vpc_attachment_detail import VpcAttachmentDetail
from huaweicloudsdkcfw.v1.model.vpc_detail import VpcDetail

# coding: utf-8

from __future__ import absolute_import

from huaweicloudsdkworkspace.v2.workspace_client import WorkspaceClient
from huaweicloudsdkworkspace.v2.workspace_async_client import WorkspaceAsyncClient

from huaweicloudsdkworkspace.v2.model.access_policy_detail_info import AccessPolicyDetailInfo
from huaweicloudsdkworkspace.v2.model.access_policy_info import AccessPolicyInfo
from huaweicloudsdkworkspace.v2.model.access_policy_object import AccessPolicyObject
from huaweicloudsdkworkspace.v2.model.access_policy_object_info import AccessPolicyObjectInfo
from huaweicloudsdkworkspace.v2.model.actions_of_users_in_group_request import ActionsOfUsersInGroupRequest
from huaweicloudsdkworkspace.v2.model.ad_domain import AdDomain
from huaweicloudsdkworkspace.v2.model.ad_domain_info import AdDomainInfo
from huaweicloudsdkworkspace.v2.model.ad_info import AdInfo
from huaweicloudsdkworkspace.v2.model.add_desktop_volumes_req import AddDesktopVolumesReq
from huaweicloudsdkworkspace.v2.model.add_desktops_volumes_req import AddDesktopsVolumesReq
from huaweicloudsdkworkspace.v2.model.add_volumes_request import AddVolumesRequest
from huaweicloudsdkworkspace.v2.model.add_volumes_response import AddVolumesResponse
from huaweicloudsdkworkspace.v2.model.address_info import AddressInfo
from huaweicloudsdkworkspace.v2.model.apply_dedicated_standby_network_param import ApplyDedicatedStandbyNetworkParam
from huaweicloudsdkworkspace.v2.model.apply_desktops_internet_req import ApplyDesktopsInternetReq
from huaweicloudsdkworkspace.v2.model.apply_desktops_internet_request import ApplyDesktopsInternetRequest
from huaweicloudsdkworkspace.v2.model.apply_desktops_internet_response import ApplyDesktopsInternetResponse
from huaweicloudsdkworkspace.v2.model.apply_rule_info import ApplyRuleInfo
from huaweicloudsdkworkspace.v2.model.apply_workspace_req import ApplyWorkspaceReq
from huaweicloudsdkworkspace.v2.model.apply_workspace_request import ApplyWorkspaceRequest
from huaweicloudsdkworkspace.v2.model.apply_workspace_response import ApplyWorkspaceResponse
from huaweicloudsdkworkspace.v2.model.assist_auth_method_config_request import AssistAuthMethodConfigRequest
from huaweicloudsdkworkspace.v2.model.associate_desktops_eip_req import AssociateDesktopsEipReq
from huaweicloudsdkworkspace.v2.model.associate_desktops_eip_request import AssociateDesktopsEipRequest
from huaweicloudsdkworkspace.v2.model.associate_desktops_eip_response import AssociateDesktopsEipResponse
from huaweicloudsdkworkspace.v2.model.attach_instances_user_info import AttachInstancesUserInfo
from huaweicloudsdkworkspace.v2.model.auth_assist_enum import AuthAssistEnum
from huaweicloudsdkworkspace.v2.model.auth_server_access_mode import AuthServerAccessMode
from huaweicloudsdkworkspace.v2.model.availability_zone_info import AvailabilityZoneInfo
from huaweicloudsdkworkspace.v2.model.base_response import BaseResponse
from huaweicloudsdkworkspace.v2.model.batch_action_desktops_req import BatchActionDesktopsReq
from huaweicloudsdkworkspace.v2.model.batch_add_desktops_tags_req import BatchAddDesktopsTagsReq
from huaweicloudsdkworkspace.v2.model.batch_add_desktops_tags_request import BatchAddDesktopsTagsRequest
from huaweicloudsdkworkspace.v2.model.batch_add_desktops_tags_response import BatchAddDesktopsTagsResponse
from huaweicloudsdkworkspace.v2.model.batch_change_tags_request import BatchChangeTagsRequest
from huaweicloudsdkworkspace.v2.model.batch_change_tags_response import BatchChangeTagsResponse
from huaweicloudsdkworkspace.v2.model.batch_create_users_req import BatchCreateUsersReq
from huaweicloudsdkworkspace.v2.model.batch_create_users_request import BatchCreateUsersRequest
from huaweicloudsdkworkspace.v2.model.batch_create_users_response import BatchCreateUsersResponse
from huaweicloudsdkworkspace.v2.model.batch_delete_access_policies_req import BatchDeleteAccessPoliciesReq
from huaweicloudsdkworkspace.v2.model.batch_delete_access_policies_request import BatchDeleteAccessPoliciesRequest
from huaweicloudsdkworkspace.v2.model.batch_delete_access_policies_response import BatchDeleteAccessPoliciesResponse
from huaweicloudsdkworkspace.v2.model.batch_delete_desktop_name_policy_req import BatchDeleteDesktopNamePolicyReq
from huaweicloudsdkworkspace.v2.model.batch_delete_desktop_name_policy_request import BatchDeleteDesktopNamePolicyRequest
from huaweicloudsdkworkspace.v2.model.batch_delete_desktop_name_policy_response import BatchDeleteDesktopNamePolicyResponse
from huaweicloudsdkworkspace.v2.model.batch_delete_desktops_request import BatchDeleteDesktopsRequest
from huaweicloudsdkworkspace.v2.model.batch_delete_desktops_response import BatchDeleteDesktopsResponse
from huaweicloudsdkworkspace.v2.model.batch_delete_desktops_tags_req import BatchDeleteDesktopsTagsReq
from huaweicloudsdkworkspace.v2.model.batch_delete_desktops_tags_request import BatchDeleteDesktopsTagsRequest
from huaweicloudsdkworkspace.v2.model.batch_delete_desktops_tags_response import BatchDeleteDesktopsTagsResponse
from huaweicloudsdkworkspace.v2.model.batch_delete_otp_devices_request import BatchDeleteOtpDevicesRequest
from huaweicloudsdkworkspace.v2.model.batch_delete_otp_devices_response import BatchDeleteOtpDevicesResponse
from huaweicloudsdkworkspace.v2.model.batch_delete_user_groups_req import BatchDeleteUserGroupsReq
from huaweicloudsdkworkspace.v2.model.batch_delete_user_groups_request import BatchDeleteUserGroupsRequest
from huaweicloudsdkworkspace.v2.model.batch_delete_user_groups_response import BatchDeleteUserGroupsResponse
from huaweicloudsdkworkspace.v2.model.batch_disassociate_desktops_eip_req import BatchDisassociateDesktopsEipReq
from huaweicloudsdkworkspace.v2.model.batch_disassociate_desktops_eip_request import BatchDisassociateDesktopsEipRequest
from huaweicloudsdkworkspace.v2.model.batch_disassociate_desktops_eip_response import BatchDisassociateDesktopsEipResponse
from huaweicloudsdkworkspace.v2.model.batch_logoff_desktops_request import BatchLogoffDesktopsRequest
from huaweicloudsdkworkspace.v2.model.batch_logoff_desktops_response import BatchLogoffDesktopsResponse
from huaweicloudsdkworkspace.v2.model.batch_rebuild_desktops_system_disk_request import BatchRebuildDesktopsSystemDiskRequest
from huaweicloudsdkworkspace.v2.model.batch_rebuild_desktops_system_disk_response import BatchRebuildDesktopsSystemDiskResponse
from huaweicloudsdkworkspace.v2.model.batch_run_desktops_request import BatchRunDesktopsRequest
from huaweicloudsdkworkspace.v2.model.batch_run_desktops_response import BatchRunDesktopsResponse
from huaweicloudsdkworkspace.v2.model.cancel_workspace_request import CancelWorkspaceRequest
from huaweicloudsdkworkspace.v2.model.cancel_workspace_response import CancelWorkspaceResponse
from huaweicloudsdkworkspace.v2.model.change_desktop_network_req import ChangeDesktopNetworkReq
from huaweicloudsdkworkspace.v2.model.change_desktop_network_request import ChangeDesktopNetworkRequest
from huaweicloudsdkworkspace.v2.model.change_desktop_network_response import ChangeDesktopNetworkResponse
from huaweicloudsdkworkspace.v2.model.change_user_status_request import ChangeUserStatusRequest
from huaweicloudsdkworkspace.v2.model.change_user_status_response import ChangeUserStatusResponse
from huaweicloudsdkworkspace.v2.model.create_access_policy_req import CreateAccessPolicyReq
from huaweicloudsdkworkspace.v2.model.create_access_policy_request import CreateAccessPolicyRequest
from huaweicloudsdkworkspace.v2.model.create_access_policy_response import CreateAccessPolicyResponse
from huaweicloudsdkworkspace.v2.model.create_desktop_name_policy_req import CreateDesktopNamePolicyReq
from huaweicloudsdkworkspace.v2.model.create_desktop_name_policy_request import CreateDesktopNamePolicyRequest
from huaweicloudsdkworkspace.v2.model.create_desktop_name_policy_response import CreateDesktopNamePolicyResponse
from huaweicloudsdkworkspace.v2.model.create_desktop_req import CreateDesktopReq
from huaweicloudsdkworkspace.v2.model.create_desktop_request import CreateDesktopRequest
from huaweicloudsdkworkspace.v2.model.create_desktop_response import CreateDesktopResponse
from huaweicloudsdkworkspace.v2.model.create_desktop_user_request import CreateDesktopUserRequest
from huaweicloudsdkworkspace.v2.model.create_desktop_user_response import CreateDesktopUserResponse
from huaweicloudsdkworkspace.v2.model.create_tag_req import CreateTagReq
from huaweicloudsdkworkspace.v2.model.create_tag_request import CreateTagRequest
from huaweicloudsdkworkspace.v2.model.create_tag_response import CreateTagResponse
from huaweicloudsdkworkspace.v2.model.create_terminals_binding_desktops_info import CreateTerminalsBindingDesktopsInfo
from huaweicloudsdkworkspace.v2.model.create_terminals_binding_desktops_request import CreateTerminalsBindingDesktopsRequest
from huaweicloudsdkworkspace.v2.model.create_terminals_binding_desktops_request_body import CreateTerminalsBindingDesktopsRequestBody
from huaweicloudsdkworkspace.v2.model.create_terminals_binding_desktops_response import CreateTerminalsBindingDesktopsResponse
from huaweicloudsdkworkspace.v2.model.create_user_group_req import CreateUserGroupReq
from huaweicloudsdkworkspace.v2.model.create_user_group_request import CreateUserGroupRequest
from huaweicloudsdkworkspace.v2.model.create_user_group_response import CreateUserGroupResponse
from huaweicloudsdkworkspace.v2.model.create_user_request import CreateUserRequest
from huaweicloudsdkworkspace.v2.model.del_otp_devices_req import DelOtpDevicesReq
from huaweicloudsdkworkspace.v2.model.delete_desktop_request import DeleteDesktopRequest
from huaweicloudsdkworkspace.v2.model.delete_desktop_response import DeleteDesktopResponse
from huaweicloudsdkworkspace.v2.model.delete_desktop_volumes_request import DeleteDesktopVolumesRequest
from huaweicloudsdkworkspace.v2.model.delete_desktop_volumes_response import DeleteDesktopVolumesResponse
from huaweicloudsdkworkspace.v2.model.delete_desktops_req import DeleteDesktopsReq
from huaweicloudsdkworkspace.v2.model.delete_tag_request import DeleteTagRequest
from huaweicloudsdkworkspace.v2.model.delete_tag_response import DeleteTagResponse
from huaweicloudsdkworkspace.v2.model.delete_terminals_binding_desktops_request import DeleteTerminalsBindingDesktopsRequest
from huaweicloudsdkworkspace.v2.model.delete_terminals_binding_desktops_request_body import DeleteTerminalsBindingDesktopsRequestBody
from huaweicloudsdkworkspace.v2.model.delete_terminals_binding_desktops_response import DeleteTerminalsBindingDesktopsResponse
from huaweicloudsdkworkspace.v2.model.delete_terminals_binding_desktops_result import DeleteTerminalsBindingDesktopsResult
from huaweicloudsdkworkspace.v2.model.delete_user_group_request import DeleteUserGroupRequest
from huaweicloudsdkworkspace.v2.model.delete_user_group_response import DeleteUserGroupResponse
from huaweicloudsdkworkspace.v2.model.delete_user_request import DeleteUserRequest
from huaweicloudsdkworkspace.v2.model.delete_user_response import DeleteUserResponse
from huaweicloudsdkworkspace.v2.model.delete_volumes_req import DeleteVolumesReq
from huaweicloudsdkworkspace.v2.model.desktop import Desktop
from huaweicloudsdkworkspace.v2.model.desktop_detail_info import DesktopDetailInfo
from huaweicloudsdkworkspace.v2.model.desktop_name_policy_info import DesktopNamePolicyInfo
from huaweicloudsdkworkspace.v2.model.desktop_subnet import DesktopSubnet
from huaweicloudsdkworkspace.v2.model.desktop_tags_info import DesktopTagsInfo
from huaweicloudsdkworkspace.v2.model.desktop_used_hours_info import DesktopUsedHoursInfo
from huaweicloudsdkworkspace.v2.model.desktop_used_info import DesktopUsedInfo
from huaweicloudsdkworkspace.v2.model.edit_user_group_request import EditUserGroupRequest
from huaweicloudsdkworkspace.v2.model.edit_user_req import EditUserReq
from huaweicloudsdkworkspace.v2.model.eip import Eip
from huaweicloudsdkworkspace.v2.model.eips import Eips
from huaweicloudsdkworkspace.v2.model.expand_desktops_volumes_req import ExpandDesktopsVolumesReq
from huaweicloudsdkworkspace.v2.model.expand_volumes_req import ExpandVolumesReq
from huaweicloudsdkworkspace.v2.model.expand_volumes_request import ExpandVolumesRequest
from huaweicloudsdkworkspace.v2.model.expand_volumes_response import ExpandVolumesResponse
from huaweicloudsdkworkspace.v2.model.export_user_login_info_new_request import ExportUserLoginInfoNewRequest
from huaweicloudsdkworkspace.v2.model.export_user_login_info_new_response import ExportUserLoginInfoNewResponse
from huaweicloudsdkworkspace.v2.model.flavor_info import FlavorInfo
from huaweicloudsdkworkspace.v2.model.flavor_link_info import FlavorLinkInfo
from huaweicloudsdkworkspace.v2.model.image_info import ImageInfo
from huaweicloudsdkworkspace.v2.model.job_detail_info import JobDetailInfo
from huaweicloudsdkworkspace.v2.model.job_entities import JobEntities
from huaweicloudsdkworkspace.v2.model.list_access_policies_request import ListAccessPoliciesRequest
from huaweicloudsdkworkspace.v2.model.list_access_policies_response import ListAccessPoliciesResponse
from huaweicloudsdkworkspace.v2.model.list_access_policy_objects_request import ListAccessPolicyObjectsRequest
from huaweicloudsdkworkspace.v2.model.list_access_policy_objects_response import ListAccessPolicyObjectsResponse
from huaweicloudsdkworkspace.v2.model.list_availability_zones_request import ListAvailabilityZonesRequest
from huaweicloudsdkworkspace.v2.model.list_availability_zones_response import ListAvailabilityZonesResponse
from huaweicloudsdkworkspace.v2.model.list_desktop_by_tags_request import ListDesktopByTagsRequest
from huaweicloudsdkworkspace.v2.model.list_desktop_by_tags_response import ListDesktopByTagsResponse
from huaweicloudsdkworkspace.v2.model.list_desktop_name_policy_request import ListDesktopNamePolicyRequest
from huaweicloudsdkworkspace.v2.model.list_desktop_name_policy_response import ListDesktopNamePolicyResponse
from huaweicloudsdkworkspace.v2.model.list_desktops_detail_request import ListDesktopsDetailRequest
from huaweicloudsdkworkspace.v2.model.list_desktops_detail_response import ListDesktopsDetailResponse
from huaweicloudsdkworkspace.v2.model.list_desktops_eips_request import ListDesktopsEipsRequest
from huaweicloudsdkworkspace.v2.model.list_desktops_eips_response import ListDesktopsEipsResponse
from huaweicloudsdkworkspace.v2.model.list_desktops_request import ListDesktopsRequest
from huaweicloudsdkworkspace.v2.model.list_desktops_response import ListDesktopsResponse
from huaweicloudsdkworkspace.v2.model.list_history_online_info_new_request import ListHistoryOnlineInfoNewRequest
from huaweicloudsdkworkspace.v2.model.list_history_online_info_new_response import ListHistoryOnlineInfoNewResponse
from huaweicloudsdkworkspace.v2.model.list_images_request import ListImagesRequest
from huaweicloudsdkworkspace.v2.model.list_images_response import ListImagesResponse
from huaweicloudsdkworkspace.v2.model.list_ita_sub_jobs_request import ListItaSubJobsRequest
from huaweicloudsdkworkspace.v2.model.list_ita_sub_jobs_response import ListItaSubJobsResponse
from huaweicloudsdkworkspace.v2.model.list_login_records_new_request import ListLoginRecordsNewRequest
from huaweicloudsdkworkspace.v2.model.list_login_records_new_response import ListLoginRecordsNewResponse
from huaweicloudsdkworkspace.v2.model.list_otp_devices_by_user_id_request import ListOtpDevicesByUserIdRequest
from huaweicloudsdkworkspace.v2.model.list_otp_devices_by_user_id_response import ListOtpDevicesByUserIdResponse
from huaweicloudsdkworkspace.v2.model.list_products_request import ListProductsRequest
from huaweicloudsdkworkspace.v2.model.list_products_response import ListProductsResponse
from huaweicloudsdkworkspace.v2.model.list_project_tags_request import ListProjectTagsRequest
from huaweicloudsdkworkspace.v2.model.list_project_tags_response import ListProjectTagsResponse
from huaweicloudsdkworkspace.v2.model.list_terminals_binding_desktops_config_request import ListTerminalsBindingDesktopsConfigRequest
from huaweicloudsdkworkspace.v2.model.list_terminals_binding_desktops_config_response import ListTerminalsBindingDesktopsConfigResponse
from huaweicloudsdkworkspace.v2.model.list_terminals_binding_desktops_request import ListTerminalsBindingDesktopsRequest
from huaweicloudsdkworkspace.v2.model.list_terminals_binding_desktops_response import ListTerminalsBindingDesktopsResponse
from huaweicloudsdkworkspace.v2.model.list_unused_desktops_request import ListUnusedDesktopsRequest
from huaweicloudsdkworkspace.v2.model.list_unused_desktops_response import ListUnusedDesktopsResponse
from huaweicloudsdkworkspace.v2.model.list_used_desktop_info_req import ListUsedDesktopInfoReq
from huaweicloudsdkworkspace.v2.model.list_used_desktop_info_request import ListUsedDesktopInfoRequest
from huaweicloudsdkworkspace.v2.model.list_used_desktop_info_response import ListUsedDesktopInfoResponse
from huaweicloudsdkworkspace.v2.model.list_user_detail_request import ListUserDetailRequest
from huaweicloudsdkworkspace.v2.model.list_user_detail_response import ListUserDetailResponse
from huaweicloudsdkworkspace.v2.model.list_user_groups_request import ListUserGroupsRequest
from huaweicloudsdkworkspace.v2.model.list_user_groups_response import ListUserGroupsResponse
from huaweicloudsdkworkspace.v2.model.list_users_of_group_request import ListUsersOfGroupRequest
from huaweicloudsdkworkspace.v2.model.list_users_of_group_response import ListUsersOfGroupResponse
from huaweicloudsdkworkspace.v2.model.list_users_request import ListUsersRequest
from huaweicloudsdkworkspace.v2.model.list_users_response import ListUsersResponse
from huaweicloudsdkworkspace.v2.model.list_workspaces_request import ListWorkspacesRequest
from huaweicloudsdkworkspace.v2.model.list_workspaces_response import ListWorkspacesResponse
from huaweicloudsdkworkspace.v2.model.logoff_desktops_req import LogoffDesktopsReq
from huaweicloudsdkworkspace.v2.model.match import Match
from huaweicloudsdkworkspace.v2.model.modify_workspace_attributes_req import ModifyWorkspaceAttributesReq
from huaweicloudsdkworkspace.v2.model.network_info import NetworkInfo
from huaweicloudsdkworkspace.v2.model.nic import Nic
from huaweicloudsdkworkspace.v2.model.operate_user_req import OperateUserReq
from huaweicloudsdkworkspace.v2.model.otp_config_info import OtpConfigInfo
from huaweicloudsdkworkspace.v2.model.otp_device import OtpDevice
from huaweicloudsdkworkspace.v2.model.port import Port
from huaweicloudsdkworkspace.v2.model.product_detail_info import ProductDetailInfo
from huaweicloudsdkworkspace.v2.model.product_info import ProductInfo
from huaweicloudsdkworkspace.v2.model.public_ip import PublicIp
from huaweicloudsdkworkspace.v2.model.query_desktop_by_tag_req import QueryDesktopByTagReq
from huaweicloudsdkworkspace.v2.model.quota_no_limit import QuotaNoLimit
from huaweicloudsdkworkspace.v2.model.rebuild_desktops_req import RebuildDesktopsReq
from huaweicloudsdkworkspace.v2.model.receive_mode_enum import ReceiveModeEnum
from huaweicloudsdkworkspace.v2.model.record import Record
from huaweicloudsdkworkspace.v2.model.reset_random_password_request import ResetRandomPasswordRequest
from huaweicloudsdkworkspace.v2.model.reset_random_password_response import ResetRandomPasswordResponse
from huaweicloudsdkworkspace.v2.model.resize_desktop_data import ResizeDesktopData
from huaweicloudsdkworkspace.v2.model.resize_desktop_job_response import ResizeDesktopJobResponse
from huaweicloudsdkworkspace.v2.model.resize_desktop_req import ResizeDesktopReq
from huaweicloudsdkworkspace.v2.model.resize_desktop_request import ResizeDesktopRequest
from huaweicloudsdkworkspace.v2.model.resize_desktop_response import ResizeDesktopResponse
from huaweicloudsdkworkspace.v2.model.resource_no_limit import ResourceNoLimit
from huaweicloudsdkworkspace.v2.model.run_actions_on_group_request import RunActionsOnGroupRequest
from huaweicloudsdkworkspace.v2.model.run_actions_on_group_response import RunActionsOnGroupResponse
from huaweicloudsdkworkspace.v2.model.security_group import SecurityGroup
from huaweicloudsdkworkspace.v2.model.security_group_info import SecurityGroupInfo
from huaweicloudsdkworkspace.v2.model.show_assist_auth_config_request import ShowAssistAuthConfigRequest
from huaweicloudsdkworkspace.v2.model.show_assist_auth_config_response import ShowAssistAuthConfigResponse
from huaweicloudsdkworkspace.v2.model.show_desktop_detail_request import ShowDesktopDetailRequest
from huaweicloudsdkworkspace.v2.model.show_desktop_detail_response import ShowDesktopDetailResponse
from huaweicloudsdkworkspace.v2.model.show_desktop_network_request import ShowDesktopNetworkRequest
from huaweicloudsdkworkspace.v2.model.show_desktop_network_response import ShowDesktopNetworkResponse
from huaweicloudsdkworkspace.v2.model.show_quotas_request import ShowQuotasRequest
from huaweicloudsdkworkspace.v2.model.show_quotas_response import ShowQuotasResponse
from huaweicloudsdkworkspace.v2.model.show_tag_by_desktop_id_request import ShowTagByDesktopIdRequest
from huaweicloudsdkworkspace.v2.model.show_tag_by_desktop_id_response import ShowTagByDesktopIdResponse
from huaweicloudsdkworkspace.v2.model.show_workspace_lock_request import ShowWorkspaceLockRequest
from huaweicloudsdkworkspace.v2.model.show_workspace_lock_response import ShowWorkspaceLockResponse
from huaweicloudsdkworkspace.v2.model.simple_desktop_info import SimpleDesktopInfo
from huaweicloudsdkworkspace.v2.model.simple_product import SimpleProduct
from huaweicloudsdkworkspace.v2.model.simple_resource import SimpleResource
from huaweicloudsdkworkspace.v2.model.simple_resource_no_used import SimpleResourceNoUsed
from huaweicloudsdkworkspace.v2.model.site_quota_no_limit import SiteQuotaNoLimit
from huaweicloudsdkworkspace.v2.model.sold_out_info import SoldOutInfo
from huaweicloudsdkworkspace.v2.model.subnet import Subnet
from huaweicloudsdkworkspace.v2.model.subnet_info import SubnetInfo
from huaweicloudsdkworkspace.v2.model.tag import Tag
from huaweicloudsdkworkspace.v2.model.tag_resource import TagResource
from huaweicloudsdkworkspace.v2.model.tags import Tags
from huaweicloudsdkworkspace.v2.model.tags_req import TagsReq
from huaweicloudsdkworkspace.v2.model.terminals_binding_desktops_config import TerminalsBindingDesktopsConfig
from huaweicloudsdkworkspace.v2.model.terminals_binding_desktops_info import TerminalsBindingDesktopsInfo
from huaweicloudsdkworkspace.v2.model.tls_config import TlsConfig
from huaweicloudsdkworkspace.v2.model.unlock_workspace_request import UnlockWorkspaceRequest
from huaweicloudsdkworkspace.v2.model.unlock_workspace_request_body import UnlockWorkspaceRequestBody
from huaweicloudsdkworkspace.v2.model.unlock_workspace_response import UnlockWorkspaceResponse
from huaweicloudsdkworkspace.v2.model.unused_desktop_info import UnusedDesktopInfo
from huaweicloudsdkworkspace.v2.model.update_access_policy_objects_req import UpdateAccessPolicyObjectsReq
from huaweicloudsdkworkspace.v2.model.update_access_policy_objects_request import UpdateAccessPolicyObjectsRequest
from huaweicloudsdkworkspace.v2.model.update_access_policy_objects_response import UpdateAccessPolicyObjectsResponse
from huaweicloudsdkworkspace.v2.model.update_assist_auth_method_config_request import UpdateAssistAuthMethodConfigRequest
from huaweicloudsdkworkspace.v2.model.update_assist_auth_method_config_response import UpdateAssistAuthMethodConfigResponse
from huaweicloudsdkworkspace.v2.model.update_desktop_name_policy_req import UpdateDesktopNamePolicyReq
from huaweicloudsdkworkspace.v2.model.update_desktop_name_policy_request import UpdateDesktopNamePolicyRequest
from huaweicloudsdkworkspace.v2.model.update_desktop_name_policy_response import UpdateDesktopNamePolicyResponse
from huaweicloudsdkworkspace.v2.model.update_terminals_binding_desktops_config_request import UpdateTerminalsBindingDesktopsConfigRequest
from huaweicloudsdkworkspace.v2.model.update_terminals_binding_desktops_config_response import UpdateTerminalsBindingDesktopsConfigResponse
from huaweicloudsdkworkspace.v2.model.update_terminals_binding_desktops_request import UpdateTerminalsBindingDesktopsRequest
from huaweicloudsdkworkspace.v2.model.update_terminals_binding_desktops_request_body import UpdateTerminalsBindingDesktopsRequestBody
from huaweicloudsdkworkspace.v2.model.update_terminals_binding_desktops_response import UpdateTerminalsBindingDesktopsResponse
from huaweicloudsdkworkspace.v2.model.update_user_group_request import UpdateUserGroupRequest
from huaweicloudsdkworkspace.v2.model.update_user_group_response import UpdateUserGroupResponse
from huaweicloudsdkworkspace.v2.model.update_user_info_request import UpdateUserInfoRequest
from huaweicloudsdkworkspace.v2.model.update_user_info_response import UpdateUserInfoResponse
from huaweicloudsdkworkspace.v2.model.update_workspace_request import UpdateWorkspaceRequest
from huaweicloudsdkworkspace.v2.model.update_workspace_response import UpdateWorkspaceResponse
from huaweicloudsdkworkspace.v2.model.user import User
from huaweicloudsdkworkspace.v2.model.user_detail import UserDetail
from huaweicloudsdkworkspace.v2.model.user_group_info import UserGroupInfo
from huaweicloudsdkworkspace.v2.model.user_in_group import UserInGroup
from huaweicloudsdkworkspace.v2.model.vm_operate_result import VmOperateResult
from huaweicloudsdkworkspace.v2.model.volume import Volume
from huaweicloudsdkworkspace.v2.model.volume_detail import VolumeDetail
from huaweicloudsdkworkspace.v2.model.vpc import Vpc


# coding: utf-8

from __future__ import absolute_import

from huaweicloudsdkiam.v5.iam_client import IamClient
from huaweicloudsdkiam.v5.iam_async_client import IamAsyncClient

from huaweicloudsdkiam.v5.model.access_key import AccessKey
from huaweicloudsdkiam.v5.model.access_key_last_used import AccessKeyLastUsed
from huaweicloudsdkiam.v5.model.access_key_metadata import AccessKeyMetadata
from huaweicloudsdkiam.v5.model.access_key_status import AccessKeyStatus
from huaweicloudsdkiam.v5.model.action import Action
from huaweicloudsdkiam.v5.model.action_associated_resource import ActionAssociatedResource
from huaweicloudsdkiam.v5.model.action_name import ActionName
from huaweicloudsdkiam.v5.model.add_user_to_group_req_body import AddUserToGroupReqBody
from huaweicloudsdkiam.v5.model.add_user_to_group_v5_request import AddUserToGroupV5Request
from huaweicloudsdkiam.v5.model.add_user_to_group_v5_response import AddUserToGroupV5Response
from huaweicloudsdkiam.v5.model.agency import Agency
from huaweicloudsdkiam.v5.model.agency_ex import AgencyEx
from huaweicloudsdkiam.v5.model.agency_id import AgencyId
from huaweicloudsdkiam.v5.model.agency_name import AgencyName
from huaweicloudsdkiam.v5.model.agency_usage import AgencyUsage
from huaweicloudsdkiam.v5.model.allow_address_netmask import AllowAddressNetmask
from huaweicloudsdkiam.v5.model.allow_ip_range import AllowIpRange
from huaweicloudsdkiam.v5.model.asymmetric_signature import AsymmetricSignature
from huaweicloudsdkiam.v5.model.asymmetric_signature_with_domain_id import AsymmetricSignatureWithDomainId
from huaweicloudsdkiam.v5.model.attach_agency_policy_req_body import AttachAgencyPolicyReqBody
from huaweicloudsdkiam.v5.model.attach_agency_policy_v5_request import AttachAgencyPolicyV5Request
from huaweicloudsdkiam.v5.model.attach_agency_policy_v5_response import AttachAgencyPolicyV5Response
from huaweicloudsdkiam.v5.model.attach_group_policy_req_body import AttachGroupPolicyReqBody
from huaweicloudsdkiam.v5.model.attach_group_policy_v5_request import AttachGroupPolicyV5Request
from huaweicloudsdkiam.v5.model.attach_group_policy_v5_response import AttachGroupPolicyV5Response
from huaweicloudsdkiam.v5.model.attach_user_policy_req_body import AttachUserPolicyReqBody
from huaweicloudsdkiam.v5.model.attach_user_policy_v5_request import AttachUserPolicyV5Request
from huaweicloudsdkiam.v5.model.attach_user_policy_v5_response import AttachUserPolicyV5Response
from huaweicloudsdkiam.v5.model.attached_at import AttachedAt
from huaweicloudsdkiam.v5.model.attached_policy import AttachedPolicy
from huaweicloudsdkiam.v5.model.change_password_req_body import ChangePasswordReqBody
from huaweicloudsdkiam.v5.model.change_password_v5_request import ChangePasswordV5Request
from huaweicloudsdkiam.v5.model.change_password_v5_response import ChangePasswordV5Response
from huaweicloudsdkiam.v5.model.condition import Condition
from huaweicloudsdkiam.v5.model.condition_key import ConditionKey
from huaweicloudsdkiam.v5.model.create_access_key_v5_request import CreateAccessKeyV5Request
from huaweicloudsdkiam.v5.model.create_access_key_v5_response import CreateAccessKeyV5Response
from huaweicloudsdkiam.v5.model.create_agency_req_body import CreateAgencyReqBody
from huaweicloudsdkiam.v5.model.create_agency_v5_request import CreateAgencyV5Request
from huaweicloudsdkiam.v5.model.create_agency_v5_response import CreateAgencyV5Response
from huaweicloudsdkiam.v5.model.create_group_req_body import CreateGroupReqBody
from huaweicloudsdkiam.v5.model.create_group_v5_request import CreateGroupV5Request
from huaweicloudsdkiam.v5.model.create_group_v5_response import CreateGroupV5Response
from huaweicloudsdkiam.v5.model.create_login_profile_req_body import CreateLoginProfileReqBody
from huaweicloudsdkiam.v5.model.create_login_profile_v5_request import CreateLoginProfileV5Request
from huaweicloudsdkiam.v5.model.create_login_profile_v5_response import CreateLoginProfileV5Response
from huaweicloudsdkiam.v5.model.create_policy_req_body import CreatePolicyReqBody
from huaweicloudsdkiam.v5.model.create_policy_v5_request import CreatePolicyV5Request
from huaweicloudsdkiam.v5.model.create_policy_v5_response import CreatePolicyV5Response
from huaweicloudsdkiam.v5.model.create_policy_version_req_body import CreatePolicyVersionReqBody
from huaweicloudsdkiam.v5.model.create_policy_version_v5_request import CreatePolicyVersionV5Request
from huaweicloudsdkiam.v5.model.create_policy_version_v5_response import CreatePolicyVersionV5Response
from huaweicloudsdkiam.v5.model.create_service_linked_agency_req_body import CreateServiceLinkedAgencyReqBody
from huaweicloudsdkiam.v5.model.create_service_linked_agency_v5_request import CreateServiceLinkedAgencyV5Request
from huaweicloudsdkiam.v5.model.create_service_linked_agency_v5_response import CreateServiceLinkedAgencyV5Response
from huaweicloudsdkiam.v5.model.create_user_req_body import CreateUserReqBody
from huaweicloudsdkiam.v5.model.create_user_v5_request import CreateUserV5Request
from huaweicloudsdkiam.v5.model.create_user_v5_response import CreateUserV5Response
from huaweicloudsdkiam.v5.model.create_virtual_mfa_device_req_body import CreateVirtualMfaDeviceReqBody
from huaweicloudsdkiam.v5.model.create_virtual_mfa_device_v5_request import CreateVirtualMfaDeviceV5Request
from huaweicloudsdkiam.v5.model.create_virtual_mfa_device_v5_response import CreateVirtualMfaDeviceV5Response
from huaweicloudsdkiam.v5.model.current_count import CurrentCount
from huaweicloudsdkiam.v5.model.delete_access_key_v5_request import DeleteAccessKeyV5Request
from huaweicloudsdkiam.v5.model.delete_access_key_v5_response import DeleteAccessKeyV5Response
from huaweicloudsdkiam.v5.model.delete_agency_v5_request import DeleteAgencyV5Request
from huaweicloudsdkiam.v5.model.delete_agency_v5_response import DeleteAgencyV5Response
from huaweicloudsdkiam.v5.model.delete_group_v5_request import DeleteGroupV5Request
from huaweicloudsdkiam.v5.model.delete_group_v5_response import DeleteGroupV5Response
from huaweicloudsdkiam.v5.model.delete_login_profile_v5_request import DeleteLoginProfileV5Request
from huaweicloudsdkiam.v5.model.delete_login_profile_v5_response import DeleteLoginProfileV5Response
from huaweicloudsdkiam.v5.model.delete_policy_v5_request import DeletePolicyV5Request
from huaweicloudsdkiam.v5.model.delete_policy_v5_response import DeletePolicyV5Response
from huaweicloudsdkiam.v5.model.delete_policy_version_v5_request import DeletePolicyVersionV5Request
from huaweicloudsdkiam.v5.model.delete_policy_version_v5_response import DeletePolicyVersionV5Response
from huaweicloudsdkiam.v5.model.delete_resource_tags_v5_request import DeleteResourceTagsV5Request
from huaweicloudsdkiam.v5.model.delete_resource_tags_v5_response import DeleteResourceTagsV5Response
from huaweicloudsdkiam.v5.model.delete_service_linked_agency_v5_request import DeleteServiceLinkedAgencyV5Request
from huaweicloudsdkiam.v5.model.delete_service_linked_agency_v5_response import DeleteServiceLinkedAgencyV5Response
from huaweicloudsdkiam.v5.model.delete_user_v5_request import DeleteUserV5Request
from huaweicloudsdkiam.v5.model.delete_user_v5_response import DeleteUserV5Response
from huaweicloudsdkiam.v5.model.delete_virtual_mfa_device_v5_request import DeleteVirtualMfaDeviceV5Request
from huaweicloudsdkiam.v5.model.delete_virtual_mfa_device_v5_response import DeleteVirtualMfaDeviceV5Response
from huaweicloudsdkiam.v5.model.deletion_task_id import DeletionTaskId
from huaweicloudsdkiam.v5.model.deletion_task_status import DeletionTaskStatus
from huaweicloudsdkiam.v5.model.description import Description
from huaweicloudsdkiam.v5.model.detach_agency_policy_req_body import DetachAgencyPolicyReqBody
from huaweicloudsdkiam.v5.model.detach_agency_policy_v5_request import DetachAgencyPolicyV5Request
from huaweicloudsdkiam.v5.model.detach_agency_policy_v5_response import DetachAgencyPolicyV5Response
from huaweicloudsdkiam.v5.model.detach_group_policy_req_body import DetachGroupPolicyReqBody
from huaweicloudsdkiam.v5.model.detach_group_policy_v5_request import DetachGroupPolicyV5Request
from huaweicloudsdkiam.v5.model.detach_group_policy_v5_response import DetachGroupPolicyV5Response
from huaweicloudsdkiam.v5.model.detach_user_policy_req_body import DetachUserPolicyReqBody
from huaweicloudsdkiam.v5.model.detach_user_policy_v5_request import DetachUserPolicyV5Request
from huaweicloudsdkiam.v5.model.detach_user_policy_v5_response import DetachUserPolicyV5Response
from huaweicloudsdkiam.v5.model.disable_mfa_device_req_body import DisableMfaDeviceReqBody
from huaweicloudsdkiam.v5.model.disable_mfa_device_v5_request import DisableMfaDeviceV5Request
from huaweicloudsdkiam.v5.model.disable_mfa_device_v5_response import DisableMfaDeviceV5Response
from huaweicloudsdkiam.v5.model.enable_mfa_device_req_body import EnableMfaDeviceReqBody
from huaweicloudsdkiam.v5.model.enable_mfa_device_v5_request import EnableMfaDeviceV5Request
from huaweicloudsdkiam.v5.model.enable_mfa_device_v5_response import EnableMfaDeviceV5Response
from huaweicloudsdkiam.v5.model.get_account_summary_v5_request import GetAccountSummaryV5Request
from huaweicloudsdkiam.v5.model.get_account_summary_v5_response import GetAccountSummaryV5Response
from huaweicloudsdkiam.v5.model.get_agency_v5_request import GetAgencyV5Request
from huaweicloudsdkiam.v5.model.get_agency_v5_response import GetAgencyV5Response
from huaweicloudsdkiam.v5.model.get_asymmetric_signature_switch_v5_request import GetAsymmetricSignatureSwitchV5Request
from huaweicloudsdkiam.v5.model.get_asymmetric_signature_switch_v5_response import GetAsymmetricSignatureSwitchV5Response
from huaweicloudsdkiam.v5.model.get_authorization_schema_v5_request import GetAuthorizationSchemaV5Request
from huaweicloudsdkiam.v5.model.get_authorization_schema_v5_response import GetAuthorizationSchemaV5Response
from huaweicloudsdkiam.v5.model.get_policy_v5_request import GetPolicyV5Request
from huaweicloudsdkiam.v5.model.get_policy_v5_response import GetPolicyV5Response
from huaweicloudsdkiam.v5.model.get_policy_version_v5_request import GetPolicyVersionV5Request
from huaweicloudsdkiam.v5.model.get_policy_version_v5_response import GetPolicyVersionV5Response
from huaweicloudsdkiam.v5.model.get_service_linked_agency_deletion_status_v5_request import GetServiceLinkedAgencyDeletionStatusV5Request
from huaweicloudsdkiam.v5.model.get_service_linked_agency_deletion_status_v5_response import GetServiceLinkedAgencyDeletionStatusV5Response
from huaweicloudsdkiam.v5.model.group import Group
from huaweicloudsdkiam.v5.model.group_description import GroupDescription
from huaweicloudsdkiam.v5.model.group_id import GroupId
from huaweicloudsdkiam.v5.model.group_name import GroupName
from huaweicloudsdkiam.v5.model.key import Key
from huaweicloudsdkiam.v5.model.list_access_keys_v5_request import ListAccessKeysV5Request
from huaweicloudsdkiam.v5.model.list_access_keys_v5_response import ListAccessKeysV5Response
from huaweicloudsdkiam.v5.model.list_agencies_v5_request import ListAgenciesV5Request
from huaweicloudsdkiam.v5.model.list_agencies_v5_response import ListAgenciesV5Response
from huaweicloudsdkiam.v5.model.list_attached_agency_policies_v5_request import ListAttachedAgencyPoliciesV5Request
from huaweicloudsdkiam.v5.model.list_attached_agency_policies_v5_response import ListAttachedAgencyPoliciesV5Response
from huaweicloudsdkiam.v5.model.list_attached_group_policies_v5_request import ListAttachedGroupPoliciesV5Request
from huaweicloudsdkiam.v5.model.list_attached_group_policies_v5_response import ListAttachedGroupPoliciesV5Response
from huaweicloudsdkiam.v5.model.list_attached_user_policies_v5_request import ListAttachedUserPoliciesV5Request
from huaweicloudsdkiam.v5.model.list_attached_user_policies_v5_response import ListAttachedUserPoliciesV5Response
from huaweicloudsdkiam.v5.model.list_entities_for_policy_v5_request import ListEntitiesForPolicyV5Request
from huaweicloudsdkiam.v5.model.list_entities_for_policy_v5_response import ListEntitiesForPolicyV5Response
from huaweicloudsdkiam.v5.model.list_groups_v5_request import ListGroupsV5Request
from huaweicloudsdkiam.v5.model.list_groups_v5_response import ListGroupsV5Response
from huaweicloudsdkiam.v5.model.list_mfa_devices_v5_request import ListMfaDevicesV5Request
from huaweicloudsdkiam.v5.model.list_mfa_devices_v5_response import ListMfaDevicesV5Response
from huaweicloudsdkiam.v5.model.list_policies_v5_request import ListPoliciesV5Request
from huaweicloudsdkiam.v5.model.list_policies_v5_response import ListPoliciesV5Response
from huaweicloudsdkiam.v5.model.list_policy_versions_v5_request import ListPolicyVersionsV5Request
from huaweicloudsdkiam.v5.model.list_policy_versions_v5_response import ListPolicyVersionsV5Response
from huaweicloudsdkiam.v5.model.list_registered_services_for_auth_schema_v5_request import ListRegisteredServicesForAuthSchemaV5Request
from huaweicloudsdkiam.v5.model.list_registered_services_for_auth_schema_v5_response import ListRegisteredServicesForAuthSchemaV5Response
from huaweicloudsdkiam.v5.model.list_resource_tags_v5_request import ListResourceTagsV5Request
from huaweicloudsdkiam.v5.model.list_resource_tags_v5_response import ListResourceTagsV5Response
from huaweicloudsdkiam.v5.model.list_service_principals_v5_request import ListServicePrincipalsV5Request
from huaweicloudsdkiam.v5.model.list_service_principals_v5_response import ListServicePrincipalsV5Response
from huaweicloudsdkiam.v5.model.list_users_v5_request import ListUsersV5Request
from huaweicloudsdkiam.v5.model.list_users_v5_response import ListUsersV5Response
from huaweicloudsdkiam.v5.model.login_policy import LoginPolicy
from huaweicloudsdkiam.v5.model.login_profile import LoginProfile
from huaweicloudsdkiam.v5.model.max_session_duration import MaxSessionDuration
from huaweicloudsdkiam.v5.model.mfa_device_metadata import MfaDeviceMetadata
from huaweicloudsdkiam.v5.model.mfa_enabled import MfaEnabled
from huaweicloudsdkiam.v5.model.next_marker import NextMarker
from huaweicloudsdkiam.v5.model.operation import Operation
from huaweicloudsdkiam.v5.model.page_info import PageInfo
from huaweicloudsdkiam.v5.model.password_policy import PasswordPolicy
from huaweicloudsdkiam.v5.model.password_reset_required import PasswordResetRequired
from huaweicloudsdkiam.v5.model.path import Path
from huaweicloudsdkiam.v5.model.policy import Policy
from huaweicloudsdkiam.v5.model.policy_agency import PolicyAgency
from huaweicloudsdkiam.v5.model.policy_description import PolicyDescription
from huaweicloudsdkiam.v5.model.policy_document import PolicyDocument
from huaweicloudsdkiam.v5.model.policy_group import PolicyGroup
from huaweicloudsdkiam.v5.model.policy_id import PolicyId
from huaweicloudsdkiam.v5.model.policy_name import PolicyName
from huaweicloudsdkiam.v5.model.policy_type import PolicyType
from huaweicloudsdkiam.v5.model.policy_user import PolicyUser
from huaweicloudsdkiam.v5.model.policy_version import PolicyVersion
from huaweicloudsdkiam.v5.model.policy_version_id import PolicyVersionId
from huaweicloudsdkiam.v5.model.reason import Reason
from huaweicloudsdkiam.v5.model.region_name import RegionName
from huaweicloudsdkiam.v5.model.remove_user_from_group_req_body import RemoveUserFromGroupReqBody
from huaweicloudsdkiam.v5.model.remove_user_from_group_v5_request import RemoveUserFromGroupV5Request
from huaweicloudsdkiam.v5.model.remove_user_from_group_v5_response import RemoveUserFromGroupV5Response
from huaweicloudsdkiam.v5.model.resource import Resource
from huaweicloudsdkiam.v5.model.service_code import ServiceCode
from huaweicloudsdkiam.v5.model.service_principal import ServicePrincipal
from huaweicloudsdkiam.v5.model.service_principal_metadata import ServicePrincipalMetadata
from huaweicloudsdkiam.v5.model.set_asymmetric_signature_req import SetAsymmetricSignatureReq
from huaweicloudsdkiam.v5.model.set_asymmetric_signature_switch_v5_request import SetAsymmetricSignatureSwitchV5Request
from huaweicloudsdkiam.v5.model.set_asymmetric_signature_switch_v5_response import SetAsymmetricSignatureSwitchV5Response
from huaweicloudsdkiam.v5.model.set_default_policy_version_v5_request import SetDefaultPolicyVersionV5Request
from huaweicloudsdkiam.v5.model.set_default_policy_version_v5_response import SetDefaultPolicyVersionV5Response
from huaweicloudsdkiam.v5.model.show_access_key_last_used_v5_request import ShowAccessKeyLastUsedV5Request
from huaweicloudsdkiam.v5.model.show_access_key_last_used_v5_response import ShowAccessKeyLastUsedV5Response
from huaweicloudsdkiam.v5.model.show_group_v5_request import ShowGroupV5Request
from huaweicloudsdkiam.v5.model.show_group_v5_response import ShowGroupV5Response
from huaweicloudsdkiam.v5.model.show_login_policy_v5_request import ShowLoginPolicyV5Request
from huaweicloudsdkiam.v5.model.show_login_policy_v5_response import ShowLoginPolicyV5Response
from huaweicloudsdkiam.v5.model.show_login_profile_v5_request import ShowLoginProfileV5Request
from huaweicloudsdkiam.v5.model.show_login_profile_v5_response import ShowLoginProfileV5Response
from huaweicloudsdkiam.v5.model.show_password_policy_v5_request import ShowPasswordPolicyV5Request
from huaweicloudsdkiam.v5.model.show_password_policy_v5_response import ShowPasswordPolicyV5Response
from huaweicloudsdkiam.v5.model.show_user_last_login_v5_request import ShowUserLastLoginV5Request
from huaweicloudsdkiam.v5.model.show_user_last_login_v5_response import ShowUserLastLoginV5Response
from huaweicloudsdkiam.v5.model.show_user_v5_request import ShowUserV5Request
from huaweicloudsdkiam.v5.model.show_user_v5_response import ShowUserV5Response
from huaweicloudsdkiam.v5.model.tag import Tag
from huaweicloudsdkiam.v5.model.tag_resource_v5_request import TagResourceV5Request
from huaweicloudsdkiam.v5.model.tag_resource_v5_response import TagResourceV5Response
from huaweicloudsdkiam.v5.model.tags import Tags
from huaweicloudsdkiam.v5.model.trust_policy_document import TrustPolicyDocument
from huaweicloudsdkiam.v5.model.type_name import TypeName
from huaweicloudsdkiam.v5.model.update_access_key_req_body import UpdateAccessKeyReqBody
from huaweicloudsdkiam.v5.model.update_access_key_v5_request import UpdateAccessKeyV5Request
from huaweicloudsdkiam.v5.model.update_access_key_v5_response import UpdateAccessKeyV5Response
from huaweicloudsdkiam.v5.model.update_agency_req_body import UpdateAgencyReqBody
from huaweicloudsdkiam.v5.model.update_agency_v5_request import UpdateAgencyV5Request
from huaweicloudsdkiam.v5.model.update_agency_v5_response import UpdateAgencyV5Response
from huaweicloudsdkiam.v5.model.update_group_req_body import UpdateGroupReqBody
from huaweicloudsdkiam.v5.model.update_group_v5_request import UpdateGroupV5Request
from huaweicloudsdkiam.v5.model.update_group_v5_response import UpdateGroupV5Response
from huaweicloudsdkiam.v5.model.update_login_policy_req_body import UpdateLoginPolicyReqBody
from huaweicloudsdkiam.v5.model.update_login_policy_v5_request import UpdateLoginPolicyV5Request
from huaweicloudsdkiam.v5.model.update_login_policy_v5_response import UpdateLoginPolicyV5Response
from huaweicloudsdkiam.v5.model.update_login_profile_req_body import UpdateLoginProfileReqBody
from huaweicloudsdkiam.v5.model.update_login_profile_v5_request import UpdateLoginProfileV5Request
from huaweicloudsdkiam.v5.model.update_login_profile_v5_response import UpdateLoginProfileV5Response
from huaweicloudsdkiam.v5.model.update_password_policy_req_body import UpdatePasswordPolicyReqBody
from huaweicloudsdkiam.v5.model.update_password_policy_v5_request import UpdatePasswordPolicyV5Request
from huaweicloudsdkiam.v5.model.update_password_policy_v5_response import UpdatePasswordPolicyV5Response
from huaweicloudsdkiam.v5.model.update_trust_policy_req_body import UpdateTrustPolicyReqBody
from huaweicloudsdkiam.v5.model.update_trust_policy_v5_request import UpdateTrustPolicyV5Request
from huaweicloudsdkiam.v5.model.update_trust_policy_v5_response import UpdateTrustPolicyV5Response
from huaweicloudsdkiam.v5.model.update_user_req_body import UpdateUserReqBody
from huaweicloudsdkiam.v5.model.update_user_v5_request import UpdateUserV5Request
from huaweicloudsdkiam.v5.model.update_user_v5_response import UpdateUserV5Response
from huaweicloudsdkiam.v5.model.urn import Urn
from huaweicloudsdkiam.v5.model.urn_template import UrnTemplate
from huaweicloudsdkiam.v5.model.user import User
from huaweicloudsdkiam.v5.model.user_description import UserDescription
from huaweicloudsdkiam.v5.model.user_enabled import UserEnabled
from huaweicloudsdkiam.v5.model.user_ex import UserEx
from huaweicloudsdkiam.v5.model.user_id import UserId
from huaweicloudsdkiam.v5.model.user_last_login import UserLastLogin
from huaweicloudsdkiam.v5.model.user_name import UserName
from huaweicloudsdkiam.v5.model.user_password import UserPassword
from huaweicloudsdkiam.v5.model.user_password_new import UserPasswordNew
from huaweicloudsdkiam.v5.model.user_password_old import UserPasswordOld
from huaweicloudsdkiam.v5.model.virtual_mfa_device import VirtualMfaDevice


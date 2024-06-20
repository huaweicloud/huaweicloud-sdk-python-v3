# coding: utf-8

from __future__ import absolute_import

from huaweicloudsdkiotda.v5.iotda_client import IoTDAClient
from huaweicloudsdkiotda.v5.iotda_async_client import IoTDAAsyncClient

from huaweicloudsdkiotda.v5.model.action_device_alarm import ActionDeviceAlarm
from huaweicloudsdkiotda.v5.model.action_device_command import ActionDeviceCommand
from huaweicloudsdkiotda.v5.model.action_smn_forwarding import ActionSmnForwarding
from huaweicloudsdkiotda.v5.model.add_action_req import AddActionReq
from huaweicloudsdkiotda.v5.model.add_application import AddApplication
from huaweicloudsdkiotda.v5.model.add_application_request import AddApplicationRequest
from huaweicloudsdkiotda.v5.model.add_application_response import AddApplicationResponse
from huaweicloudsdkiotda.v5.model.add_backlog_policy import AddBacklogPolicy
from huaweicloudsdkiotda.v5.model.add_bridge import AddBridge
from huaweicloudsdkiotda.v5.model.add_bridge_request import AddBridgeRequest
from huaweicloudsdkiotda.v5.model.add_bridge_response import AddBridgeResponse
from huaweicloudsdkiotda.v5.model.add_certificate_request import AddCertificateRequest
from huaweicloudsdkiotda.v5.model.add_certificate_response import AddCertificateResponse
from huaweicloudsdkiotda.v5.model.add_device import AddDevice
from huaweicloudsdkiotda.v5.model.add_device_group_dto import AddDeviceGroupDTO
from huaweicloudsdkiotda.v5.model.add_device_group_request import AddDeviceGroupRequest
from huaweicloudsdkiotda.v5.model.add_device_group_response import AddDeviceGroupResponse
from huaweicloudsdkiotda.v5.model.add_device_proxy import AddDeviceProxy
from huaweicloudsdkiotda.v5.model.add_device_request import AddDeviceRequest
from huaweicloudsdkiotda.v5.model.add_device_response import AddDeviceResponse
from huaweicloudsdkiotda.v5.model.add_flow_control_policy import AddFlowControlPolicy
from huaweicloudsdkiotda.v5.model.add_product import AddProduct
from huaweicloudsdkiotda.v5.model.add_queue_request import AddQueueRequest
from huaweicloudsdkiotda.v5.model.add_queue_response import AddQueueResponse
from huaweicloudsdkiotda.v5.model.add_rule_req import AddRuleReq
from huaweicloudsdkiotda.v5.model.add_tunnel_dto import AddTunnelDto
from huaweicloudsdkiotda.v5.model.add_tunnel_request import AddTunnelRequest
from huaweicloudsdkiotda.v5.model.add_tunnel_response import AddTunnelResponse
from huaweicloudsdkiotda.v5.model.amqp_forwarding import AmqpForwarding
from huaweicloudsdkiotda.v5.model.application_dto import ApplicationDTO
from huaweicloudsdkiotda.v5.model.async_device_command_request import AsyncDeviceCommandRequest
from huaweicloudsdkiotda.v5.model.auth_info import AuthInfo
from huaweicloudsdkiotda.v5.model.auth_info_res import AuthInfoRes
from huaweicloudsdkiotda.v5.model.auth_info_without_secret import AuthInfoWithoutSecret
from huaweicloudsdkiotda.v5.model.backlog_policy_info import BacklogPolicyInfo
from huaweicloudsdkiotda.v5.model.batch_show_queue_request import BatchShowQueueRequest
from huaweicloudsdkiotda.v5.model.batch_show_queue_response import BatchShowQueueResponse
from huaweicloudsdkiotda.v5.model.batch_target_result import BatchTargetResult
from huaweicloudsdkiotda.v5.model.batch_targets import BatchTargets
from huaweicloudsdkiotda.v5.model.batch_task_file import BatchTaskFile
from huaweicloudsdkiotda.v5.model.bind_device_policy import BindDevicePolicy
from huaweicloudsdkiotda.v5.model.bind_device_policy_request import BindDevicePolicyRequest
from huaweicloudsdkiotda.v5.model.bind_device_policy_response import BindDevicePolicyResponse
from huaweicloudsdkiotda.v5.model.bind_tags_dto import BindTagsDTO
from huaweicloudsdkiotda.v5.model.bridge_auth_info import BridgeAuthInfo
from huaweicloudsdkiotda.v5.model.bridge_response import BridgeResponse
from huaweicloudsdkiotda.v5.model.broadcast_message_request import BroadcastMessageRequest
from huaweicloudsdkiotda.v5.model.broadcast_message_response import BroadcastMessageResponse
from huaweicloudsdkiotda.v5.model.certificates_rsp_dto import CertificatesRspDTO
from huaweicloudsdkiotda.v5.model.change_rule_status_request import ChangeRuleStatusRequest
from huaweicloudsdkiotda.v5.model.change_rule_status_response import ChangeRuleStatusResponse
from huaweicloudsdkiotda.v5.model.channel_detail import ChannelDetail
from huaweicloudsdkiotda.v5.model.check_certificate_request import CheckCertificateRequest
from huaweicloudsdkiotda.v5.model.check_certificate_response import CheckCertificateResponse
from huaweicloudsdkiotda.v5.model.close_device_tunnel_request import CloseDeviceTunnelRequest
from huaweicloudsdkiotda.v5.model.close_device_tunnel_response import CloseDeviceTunnelResponse
from huaweicloudsdkiotda.v5.model.cmd import Cmd
from huaweicloudsdkiotda.v5.model.column_mapping import ColumnMapping
from huaweicloudsdkiotda.v5.model.condition_group import ConditionGroup
from huaweicloudsdkiotda.v5.model.connect_state import ConnectState
from huaweicloudsdkiotda.v5.model.create_access_code_request import CreateAccessCodeRequest
from huaweicloudsdkiotda.v5.model.create_access_code_request_body import CreateAccessCodeRequestBody
from huaweicloudsdkiotda.v5.model.create_access_code_response import CreateAccessCodeResponse
from huaweicloudsdkiotda.v5.model.create_async_command_request import CreateAsyncCommandRequest
from huaweicloudsdkiotda.v5.model.create_async_command_response import CreateAsyncCommandResponse
from huaweicloudsdkiotda.v5.model.create_batch_task import CreateBatchTask
from huaweicloudsdkiotda.v5.model.create_batch_task_request import CreateBatchTaskRequest
from huaweicloudsdkiotda.v5.model.create_batch_task_response import CreateBatchTaskResponse
from huaweicloudsdkiotda.v5.model.create_certificate_dto import CreateCertificateDTO
from huaweicloudsdkiotda.v5.model.create_command_request import CreateCommandRequest
from huaweicloudsdkiotda.v5.model.create_command_response import CreateCommandResponse
from huaweicloudsdkiotda.v5.model.create_device_authorizer import CreateDeviceAuthorizer
from huaweicloudsdkiotda.v5.model.create_device_authorizer_request import CreateDeviceAuthorizerRequest
from huaweicloudsdkiotda.v5.model.create_device_authorizer_response import CreateDeviceAuthorizerResponse
from huaweicloudsdkiotda.v5.model.create_device_policy import CreateDevicePolicy
from huaweicloudsdkiotda.v5.model.create_device_policy_request import CreateDevicePolicyRequest
from huaweicloudsdkiotda.v5.model.create_device_policy_response import CreateDevicePolicyResponse
from huaweicloudsdkiotda.v5.model.create_device_proxy_request import CreateDeviceProxyRequest
from huaweicloudsdkiotda.v5.model.create_device_proxy_response import CreateDeviceProxyResponse
from huaweicloudsdkiotda.v5.model.create_message_request import CreateMessageRequest
from huaweicloudsdkiotda.v5.model.create_message_response import CreateMessageResponse
from huaweicloudsdkiotda.v5.model.create_or_delete_device_in_group_request import CreateOrDeleteDeviceInGroupRequest
from huaweicloudsdkiotda.v5.model.create_or_delete_device_in_group_response import CreateOrDeleteDeviceInGroupResponse
from huaweicloudsdkiotda.v5.model.create_ota_package import CreateOtaPackage
from huaweicloudsdkiotda.v5.model.create_ota_package_request import CreateOtaPackageRequest
from huaweicloudsdkiotda.v5.model.create_ota_package_response import CreateOtaPackageResponse
from huaweicloudsdkiotda.v5.model.create_product_request import CreateProductRequest
from huaweicloudsdkiotda.v5.model.create_product_response import CreateProductResponse
from huaweicloudsdkiotda.v5.model.create_provisioning_template import CreateProvisioningTemplate
from huaweicloudsdkiotda.v5.model.create_provisioning_template_request import CreateProvisioningTemplateRequest
from huaweicloudsdkiotda.v5.model.create_provisioning_template_response import CreateProvisioningTemplateResponse
from huaweicloudsdkiotda.v5.model.create_routing_backlog_policy_request import CreateRoutingBacklogPolicyRequest
from huaweicloudsdkiotda.v5.model.create_routing_backlog_policy_response import CreateRoutingBacklogPolicyResponse
from huaweicloudsdkiotda.v5.model.create_routing_flow_control_policy_request import CreateRoutingFlowControlPolicyRequest
from huaweicloudsdkiotda.v5.model.create_routing_flow_control_policy_response import CreateRoutingFlowControlPolicyResponse
from huaweicloudsdkiotda.v5.model.create_routing_rule_request import CreateRoutingRuleRequest
from huaweicloudsdkiotda.v5.model.create_routing_rule_response import CreateRoutingRuleResponse
from huaweicloudsdkiotda.v5.model.create_rule_action_request import CreateRuleActionRequest
from huaweicloudsdkiotda.v5.model.create_rule_action_response import CreateRuleActionResponse
from huaweicloudsdkiotda.v5.model.create_rule_request import CreateRuleRequest
from huaweicloudsdkiotda.v5.model.create_rule_response import CreateRuleResponse
from huaweicloudsdkiotda.v5.model.daily_timer_type import DailyTimerType
from huaweicloudsdkiotda.v5.model.delete_application_request import DeleteApplicationRequest
from huaweicloudsdkiotda.v5.model.delete_application_response import DeleteApplicationResponse
from huaweicloudsdkiotda.v5.model.delete_batch_task_file_request import DeleteBatchTaskFileRequest
from huaweicloudsdkiotda.v5.model.delete_batch_task_file_response import DeleteBatchTaskFileResponse
from huaweicloudsdkiotda.v5.model.delete_batch_task_request import DeleteBatchTaskRequest
from huaweicloudsdkiotda.v5.model.delete_batch_task_response import DeleteBatchTaskResponse
from huaweicloudsdkiotda.v5.model.delete_bridge_request import DeleteBridgeRequest
from huaweicloudsdkiotda.v5.model.delete_bridge_response import DeleteBridgeResponse
from huaweicloudsdkiotda.v5.model.delete_certificate_request import DeleteCertificateRequest
from huaweicloudsdkiotda.v5.model.delete_certificate_response import DeleteCertificateResponse
from huaweicloudsdkiotda.v5.model.delete_device_authorizer_request import DeleteDeviceAuthorizerRequest
from huaweicloudsdkiotda.v5.model.delete_device_authorizer_response import DeleteDeviceAuthorizerResponse
from huaweicloudsdkiotda.v5.model.delete_device_group_request import DeleteDeviceGroupRequest
from huaweicloudsdkiotda.v5.model.delete_device_group_response import DeleteDeviceGroupResponse
from huaweicloudsdkiotda.v5.model.delete_device_policy_request import DeleteDevicePolicyRequest
from huaweicloudsdkiotda.v5.model.delete_device_policy_response import DeleteDevicePolicyResponse
from huaweicloudsdkiotda.v5.model.delete_device_proxy_request import DeleteDeviceProxyRequest
from huaweicloudsdkiotda.v5.model.delete_device_proxy_response import DeleteDeviceProxyResponse
from huaweicloudsdkiotda.v5.model.delete_device_request import DeleteDeviceRequest
from huaweicloudsdkiotda.v5.model.delete_device_response import DeleteDeviceResponse
from huaweicloudsdkiotda.v5.model.delete_device_tunnel_request import DeleteDeviceTunnelRequest
from huaweicloudsdkiotda.v5.model.delete_device_tunnel_response import DeleteDeviceTunnelResponse
from huaweicloudsdkiotda.v5.model.delete_ota_package_request import DeleteOtaPackageRequest
from huaweicloudsdkiotda.v5.model.delete_ota_package_response import DeleteOtaPackageResponse
from huaweicloudsdkiotda.v5.model.delete_product_request import DeleteProductRequest
from huaweicloudsdkiotda.v5.model.delete_product_response import DeleteProductResponse
from huaweicloudsdkiotda.v5.model.delete_provisioning_template_request import DeleteProvisioningTemplateRequest
from huaweicloudsdkiotda.v5.model.delete_provisioning_template_response import DeleteProvisioningTemplateResponse
from huaweicloudsdkiotda.v5.model.delete_queue_request import DeleteQueueRequest
from huaweicloudsdkiotda.v5.model.delete_queue_response import DeleteQueueResponse
from huaweicloudsdkiotda.v5.model.delete_routing_backlog_policy_request import DeleteRoutingBacklogPolicyRequest
from huaweicloudsdkiotda.v5.model.delete_routing_backlog_policy_response import DeleteRoutingBacklogPolicyResponse
from huaweicloudsdkiotda.v5.model.delete_routing_flow_control_policy_request import DeleteRoutingFlowControlPolicyRequest
from huaweicloudsdkiotda.v5.model.delete_routing_flow_control_policy_response import DeleteRoutingFlowControlPolicyResponse
from huaweicloudsdkiotda.v5.model.delete_routing_rule_request import DeleteRoutingRuleRequest
from huaweicloudsdkiotda.v5.model.delete_routing_rule_response import DeleteRoutingRuleResponse
from huaweicloudsdkiotda.v5.model.delete_rule_action_request import DeleteRuleActionRequest
from huaweicloudsdkiotda.v5.model.delete_rule_action_response import DeleteRuleActionResponse
from huaweicloudsdkiotda.v5.model.delete_rule_request import DeleteRuleRequest
from huaweicloudsdkiotda.v5.model.delete_rule_response import DeleteRuleResponse
from huaweicloudsdkiotda.v5.model.device_authorizer_simple import DeviceAuthorizerSimple
from huaweicloudsdkiotda.v5.model.device_broadcast_request import DeviceBroadcastRequest
from huaweicloudsdkiotda.v5.model.device_command_request import DeviceCommandRequest
from huaweicloudsdkiotda.v5.model.device_data_condition import DeviceDataCondition
from huaweicloudsdkiotda.v5.model.device_group_response_summary import DeviceGroupResponseSummary
from huaweicloudsdkiotda.v5.model.device_linkage_status_condition import DeviceLinkageStatusCondition
from huaweicloudsdkiotda.v5.model.device_message import DeviceMessage
from huaweicloudsdkiotda.v5.model.device_message_request import DeviceMessageRequest
from huaweicloudsdkiotda.v5.model.device_policy_bind_or_unbind_failure_detail import DevicePolicyBindOrUnbindFailureDetail
from huaweicloudsdkiotda.v5.model.device_properties_request import DevicePropertiesRequest
from huaweicloudsdkiotda.v5.model.device_resource import DeviceResource
from huaweicloudsdkiotda.v5.model.device_shadow_data import DeviceShadowData
from huaweicloudsdkiotda.v5.model.device_shadow_properties import DeviceShadowProperties
from huaweicloudsdkiotda.v5.model.device_side import DeviceSide
from huaweicloudsdkiotda.v5.model.dis_forwarding import DisForwarding
from huaweicloudsdkiotda.v5.model.dms_kafka_forwarding import DmsKafkaForwarding
from huaweicloudsdkiotda.v5.model.dms_rocket_mq_forwarding import DmsRocketMQForwarding
from huaweicloudsdkiotda.v5.model.effective_time_range import EffectiveTimeRange
from huaweicloudsdkiotda.v5.model.effective_time_range_response_dto import EffectiveTimeRangeResponseDTO
from huaweicloudsdkiotda.v5.model.error_info import ErrorInfo
from huaweicloudsdkiotda.v5.model.error_info_dto import ErrorInfoDTO
from huaweicloudsdkiotda.v5.model.file_location import FileLocation
from huaweicloudsdkiotda.v5.model.flow_control_policy_info import FlowControlPolicyInfo
from huaweicloudsdkiotda.v5.model.freeze_device_request import FreezeDeviceRequest
from huaweicloudsdkiotda.v5.model.freeze_device_response import FreezeDeviceResponse
from huaweicloudsdkiotda.v5.model.function_graph_forwarding import FunctionGraphForwarding
from huaweicloudsdkiotda.v5.model.http_forwarding import HttpForwarding
from huaweicloudsdkiotda.v5.model.influx_db_forwarding import InfluxDBForwarding
from huaweicloudsdkiotda.v5.model.initial_desired import InitialDesired
from huaweicloudsdkiotda.v5.model.list_batch_task_files_request import ListBatchTaskFilesRequest
from huaweicloudsdkiotda.v5.model.list_batch_task_files_response import ListBatchTaskFilesResponse
from huaweicloudsdkiotda.v5.model.list_batch_tasks_request import ListBatchTasksRequest
from huaweicloudsdkiotda.v5.model.list_batch_tasks_response import ListBatchTasksResponse
from huaweicloudsdkiotda.v5.model.list_bridges_request import ListBridgesRequest
from huaweicloudsdkiotda.v5.model.list_bridges_response import ListBridgesResponse
from huaweicloudsdkiotda.v5.model.list_certificates_request import ListCertificatesRequest
from huaweicloudsdkiotda.v5.model.list_certificates_response import ListCertificatesResponse
from huaweicloudsdkiotda.v5.model.list_device_authorizers_request import ListDeviceAuthorizersRequest
from huaweicloudsdkiotda.v5.model.list_device_authorizers_response import ListDeviceAuthorizersResponse
from huaweicloudsdkiotda.v5.model.list_device_group_summary import ListDeviceGroupSummary
from huaweicloudsdkiotda.v5.model.list_device_groups_by_device_request import ListDeviceGroupsByDeviceRequest
from huaweicloudsdkiotda.v5.model.list_device_groups_by_device_response import ListDeviceGroupsByDeviceResponse
from huaweicloudsdkiotda.v5.model.list_device_groups_request import ListDeviceGroupsRequest
from huaweicloudsdkiotda.v5.model.list_device_groups_response import ListDeviceGroupsResponse
from huaweicloudsdkiotda.v5.model.list_device_messages_request import ListDeviceMessagesRequest
from huaweicloudsdkiotda.v5.model.list_device_messages_response import ListDeviceMessagesResponse
from huaweicloudsdkiotda.v5.model.list_device_policies_request import ListDevicePoliciesRequest
from huaweicloudsdkiotda.v5.model.list_device_policies_response import ListDevicePoliciesResponse
from huaweicloudsdkiotda.v5.model.list_device_policy_base import ListDevicePolicyBase
from huaweicloudsdkiotda.v5.model.list_device_proxies_request import ListDeviceProxiesRequest
from huaweicloudsdkiotda.v5.model.list_device_proxies_response import ListDeviceProxiesResponse
from huaweicloudsdkiotda.v5.model.list_device_tunnels_request import ListDeviceTunnelsRequest
from huaweicloudsdkiotda.v5.model.list_device_tunnels_response import ListDeviceTunnelsResponse
from huaweicloudsdkiotda.v5.model.list_devices_request import ListDevicesRequest
from huaweicloudsdkiotda.v5.model.list_devices_response import ListDevicesResponse
from huaweicloudsdkiotda.v5.model.list_ota_package_info_request import ListOtaPackageInfoRequest
from huaweicloudsdkiotda.v5.model.list_ota_package_info_response import ListOtaPackageInfoResponse
from huaweicloudsdkiotda.v5.model.list_products_request import ListProductsRequest
from huaweicloudsdkiotda.v5.model.list_products_response import ListProductsResponse
from huaweicloudsdkiotda.v5.model.list_properties_request import ListPropertiesRequest
from huaweicloudsdkiotda.v5.model.list_properties_response import ListPropertiesResponse
from huaweicloudsdkiotda.v5.model.list_provisioning_templates_request import ListProvisioningTemplatesRequest
from huaweicloudsdkiotda.v5.model.list_provisioning_templates_response import ListProvisioningTemplatesResponse
from huaweicloudsdkiotda.v5.model.list_resources_by_tags_request import ListResourcesByTagsRequest
from huaweicloudsdkiotda.v5.model.list_resources_by_tags_response import ListResourcesByTagsResponse
from huaweicloudsdkiotda.v5.model.list_routing_backlog_policy_request import ListRoutingBacklogPolicyRequest
from huaweicloudsdkiotda.v5.model.list_routing_backlog_policy_response import ListRoutingBacklogPolicyResponse
from huaweicloudsdkiotda.v5.model.list_routing_flow_control_policy_request import ListRoutingFlowControlPolicyRequest
from huaweicloudsdkiotda.v5.model.list_routing_flow_control_policy_response import ListRoutingFlowControlPolicyResponse
from huaweicloudsdkiotda.v5.model.list_routing_rules_request import ListRoutingRulesRequest
from huaweicloudsdkiotda.v5.model.list_routing_rules_response import ListRoutingRulesResponse
from huaweicloudsdkiotda.v5.model.list_rule_actions_request import ListRuleActionsRequest
from huaweicloudsdkiotda.v5.model.list_rule_actions_response import ListRuleActionsResponse
from huaweicloudsdkiotda.v5.model.list_rules_request import ListRulesRequest
from huaweicloudsdkiotda.v5.model.list_rules_response import ListRulesResponse
from huaweicloudsdkiotda.v5.model.message_result import MessageResult
from huaweicloudsdkiotda.v5.model.mrs_kafka_forwarding import MrsKafkaForwarding
from huaweicloudsdkiotda.v5.model.mysql_forwarding import MysqlForwarding
from huaweicloudsdkiotda.v5.model.net_address import NetAddress
from huaweicloudsdkiotda.v5.model.obs_forwarding import ObsForwarding
from huaweicloudsdkiotda.v5.model.obs_location import ObsLocation
from huaweicloudsdkiotda.v5.model.ota_package_info import OtaPackageInfo
from huaweicloudsdkiotda.v5.model.page import Page
from huaweicloudsdkiotda.v5.model.page_info import PageInfo
from huaweicloudsdkiotda.v5.model.parameter_ref import ParameterRef
from huaweicloudsdkiotda.v5.model.policy_resource import PolicyResource
from huaweicloudsdkiotda.v5.model.policy_target_base import PolicyTargetBase
from huaweicloudsdkiotda.v5.model.product_summary import ProductSummary
from huaweicloudsdkiotda.v5.model.properties_dto import PropertiesDTO
from huaweicloudsdkiotda.v5.model.property_filter import PropertyFilter
from huaweicloudsdkiotda.v5.model.provisioning_template_body import ProvisioningTemplateBody
from huaweicloudsdkiotda.v5.model.provisioning_template_simple import ProvisioningTemplateSimple
from huaweicloudsdkiotda.v5.model.query_device_proxy_simplify import QueryDeviceProxySimplify
from huaweicloudsdkiotda.v5.model.query_device_simplify import QueryDeviceSimplify
from huaweicloudsdkiotda.v5.model.query_queue_base import QueryQueueBase
from huaweicloudsdkiotda.v5.model.query_resource_by_tags_dto import QueryResourceByTagsDTO
from huaweicloudsdkiotda.v5.model.queue_info import QueueInfo
from huaweicloudsdkiotda.v5.model.reset_bridge_secret import ResetBridgeSecret
from huaweicloudsdkiotda.v5.model.reset_bridge_secret_request import ResetBridgeSecretRequest
from huaweicloudsdkiotda.v5.model.reset_bridge_secret_response import ResetBridgeSecretResponse
from huaweicloudsdkiotda.v5.model.reset_device_secret import ResetDeviceSecret
from huaweicloudsdkiotda.v5.model.reset_device_secret_request import ResetDeviceSecretRequest
from huaweicloudsdkiotda.v5.model.reset_device_secret_response import ResetDeviceSecretResponse
from huaweicloudsdkiotda.v5.model.reset_fingerprint import ResetFingerprint
from huaweicloudsdkiotda.v5.model.reset_fingerprint_request import ResetFingerprintRequest
from huaweicloudsdkiotda.v5.model.reset_fingerprint_response import ResetFingerprintResponse
from huaweicloudsdkiotda.v5.model.resource_dto import ResourceDTO
from huaweicloudsdkiotda.v5.model.retry_batch_task_request import RetryBatchTaskRequest
from huaweicloudsdkiotda.v5.model.retry_batch_task_response import RetryBatchTaskResponse
from huaweicloudsdkiotda.v5.model.roma_forwarding import RomaForwarding
from huaweicloudsdkiotda.v5.model.routing_rule import RoutingRule
from huaweicloudsdkiotda.v5.model.routing_rule_action import RoutingRuleAction
from huaweicloudsdkiotda.v5.model.routing_rule_subject import RoutingRuleSubject
from huaweicloudsdkiotda.v5.model.rule import Rule
from huaweicloudsdkiotda.v5.model.rule_action import RuleAction
from huaweicloudsdkiotda.v5.model.rule_condition import RuleCondition
from huaweicloudsdkiotda.v5.model.rule_response import RuleResponse
from huaweicloudsdkiotda.v5.model.rule_status import RuleStatus
from huaweicloudsdkiotda.v5.model.search_device import SearchDevice
from huaweicloudsdkiotda.v5.model.search_devices_request import SearchDevicesRequest
from huaweicloudsdkiotda.v5.model.search_devices_response import SearchDevicesResponse
from huaweicloudsdkiotda.v5.model.search_sql import SearchSql
from huaweicloudsdkiotda.v5.model.service_capability import ServiceCapability
from huaweicloudsdkiotda.v5.model.service_command import ServiceCommand
from huaweicloudsdkiotda.v5.model.service_command_para import ServiceCommandPara
from huaweicloudsdkiotda.v5.model.service_command_response import ServiceCommandResponse
from huaweicloudsdkiotda.v5.model.service_event import ServiceEvent
from huaweicloudsdkiotda.v5.model.service_property import ServiceProperty
from huaweicloudsdkiotda.v5.model.show_application_request import ShowApplicationRequest
from huaweicloudsdkiotda.v5.model.show_application_response import ShowApplicationResponse
from huaweicloudsdkiotda.v5.model.show_applications_request import ShowApplicationsRequest
from huaweicloudsdkiotda.v5.model.show_applications_response import ShowApplicationsResponse
from huaweicloudsdkiotda.v5.model.show_async_device_command_request import ShowAsyncDeviceCommandRequest
from huaweicloudsdkiotda.v5.model.show_async_device_command_response import ShowAsyncDeviceCommandResponse
from huaweicloudsdkiotda.v5.model.show_batch_task_request import ShowBatchTaskRequest
from huaweicloudsdkiotda.v5.model.show_batch_task_response import ShowBatchTaskResponse
from huaweicloudsdkiotda.v5.model.show_device_authorizer_request import ShowDeviceAuthorizerRequest
from huaweicloudsdkiotda.v5.model.show_device_authorizer_response import ShowDeviceAuthorizerResponse
from huaweicloudsdkiotda.v5.model.show_device_group_request import ShowDeviceGroupRequest
from huaweicloudsdkiotda.v5.model.show_device_group_response import ShowDeviceGroupResponse
from huaweicloudsdkiotda.v5.model.show_device_message_request import ShowDeviceMessageRequest
from huaweicloudsdkiotda.v5.model.show_device_message_response import ShowDeviceMessageResponse
from huaweicloudsdkiotda.v5.model.show_device_policy_request import ShowDevicePolicyRequest
from huaweicloudsdkiotda.v5.model.show_device_policy_response import ShowDevicePolicyResponse
from huaweicloudsdkiotda.v5.model.show_device_proxy_request import ShowDeviceProxyRequest
from huaweicloudsdkiotda.v5.model.show_device_proxy_response import ShowDeviceProxyResponse
from huaweicloudsdkiotda.v5.model.show_device_request import ShowDeviceRequest
from huaweicloudsdkiotda.v5.model.show_device_response import ShowDeviceResponse
from huaweicloudsdkiotda.v5.model.show_device_shadow_request import ShowDeviceShadowRequest
from huaweicloudsdkiotda.v5.model.show_device_shadow_response import ShowDeviceShadowResponse
from huaweicloudsdkiotda.v5.model.show_device_tunnel_request import ShowDeviceTunnelRequest
from huaweicloudsdkiotda.v5.model.show_device_tunnel_response import ShowDeviceTunnelResponse
from huaweicloudsdkiotda.v5.model.show_devices_in_group_request import ShowDevicesInGroupRequest
from huaweicloudsdkiotda.v5.model.show_devices_in_group_response import ShowDevicesInGroupResponse
from huaweicloudsdkiotda.v5.model.show_ota_package_request import ShowOtaPackageRequest
from huaweicloudsdkiotda.v5.model.show_ota_package_response import ShowOtaPackageResponse
from huaweicloudsdkiotda.v5.model.show_product_request import ShowProductRequest
from huaweicloudsdkiotda.v5.model.show_product_response import ShowProductResponse
from huaweicloudsdkiotda.v5.model.show_provisioning_template_request import ShowProvisioningTemplateRequest
from huaweicloudsdkiotda.v5.model.show_provisioning_template_response import ShowProvisioningTemplateResponse
from huaweicloudsdkiotda.v5.model.show_queue_request import ShowQueueRequest
from huaweicloudsdkiotda.v5.model.show_queue_response import ShowQueueResponse
from huaweicloudsdkiotda.v5.model.show_routing_backlog_policy_request import ShowRoutingBacklogPolicyRequest
from huaweicloudsdkiotda.v5.model.show_routing_backlog_policy_response import ShowRoutingBacklogPolicyResponse
from huaweicloudsdkiotda.v5.model.show_routing_flow_control_policy_request import ShowRoutingFlowControlPolicyRequest
from huaweicloudsdkiotda.v5.model.show_routing_flow_control_policy_response import ShowRoutingFlowControlPolicyResponse
from huaweicloudsdkiotda.v5.model.show_routing_rule_request import ShowRoutingRuleRequest
from huaweicloudsdkiotda.v5.model.show_routing_rule_response import ShowRoutingRuleResponse
from huaweicloudsdkiotda.v5.model.show_rule_action_request import ShowRuleActionRequest
from huaweicloudsdkiotda.v5.model.show_rule_action_response import ShowRuleActionResponse
from huaweicloudsdkiotda.v5.model.show_rule_request import ShowRuleRequest
from huaweicloudsdkiotda.v5.model.show_rule_response import ShowRuleResponse
from huaweicloudsdkiotda.v5.model.show_targets_in_device_policy_request import ShowTargetsInDevicePolicyRequest
from huaweicloudsdkiotda.v5.model.show_targets_in_device_policy_request_body import ShowTargetsInDevicePolicyRequestBody
from huaweicloudsdkiotda.v5.model.show_targets_in_device_policy_response import ShowTargetsInDevicePolicyResponse
from huaweicloudsdkiotda.v5.model.simple_timer_type import SimpleTimerType
from huaweicloudsdkiotda.v5.model.simplify_device import SimplifyDevice
from huaweicloudsdkiotda.v5.model.statement import Statement
from huaweicloudsdkiotda.v5.model.stop_batch_task_request import StopBatchTaskRequest
from huaweicloudsdkiotda.v5.model.stop_batch_task_response import StopBatchTaskResponse
from huaweicloudsdkiotda.v5.model.strategy import Strategy
from huaweicloudsdkiotda.v5.model.tag_device_request import TagDeviceRequest
from huaweicloudsdkiotda.v5.model.tag_device_response import TagDeviceResponse
from huaweicloudsdkiotda.v5.model.tag_ref import TagRef
from huaweicloudsdkiotda.v5.model.tag_v5_dto import TagV5DTO
from huaweicloudsdkiotda.v5.model.task import Task
from huaweicloudsdkiotda.v5.model.task_detail import TaskDetail
from huaweicloudsdkiotda.v5.model.task_policy import TaskPolicy
from huaweicloudsdkiotda.v5.model.task_progress import TaskProgress
from huaweicloudsdkiotda.v5.model.template_resource import TemplateResource
from huaweicloudsdkiotda.v5.model.time_range import TimeRange
from huaweicloudsdkiotda.v5.model.tunnel_info import TunnelInfo
from huaweicloudsdkiotda.v5.model.un_bind_device_policy import UnBindDevicePolicy
from huaweicloudsdkiotda.v5.model.unbind_device_policy_request import UnbindDevicePolicyRequest
from huaweicloudsdkiotda.v5.model.unbind_device_policy_response import UnbindDevicePolicyResponse
from huaweicloudsdkiotda.v5.model.unbind_tags_dto import UnbindTagsDTO
from huaweicloudsdkiotda.v5.model.unfreeze_device_request import UnfreezeDeviceRequest
from huaweicloudsdkiotda.v5.model.unfreeze_device_response import UnfreezeDeviceResponse
from huaweicloudsdkiotda.v5.model.untag_device_request import UntagDeviceRequest
from huaweicloudsdkiotda.v5.model.untag_device_response import UntagDeviceResponse
from huaweicloudsdkiotda.v5.model.update_action_req import UpdateActionReq
from huaweicloudsdkiotda.v5.model.update_application_dto import UpdateApplicationDTO
from huaweicloudsdkiotda.v5.model.update_application_request import UpdateApplicationRequest
from huaweicloudsdkiotda.v5.model.update_application_response import UpdateApplicationResponse
from huaweicloudsdkiotda.v5.model.update_backlog_policy import UpdateBacklogPolicy
from huaweicloudsdkiotda.v5.model.update_certificate_dto import UpdateCertificateDTO
from huaweicloudsdkiotda.v5.model.update_certificate_request import UpdateCertificateRequest
from huaweicloudsdkiotda.v5.model.update_certificate_response import UpdateCertificateResponse
from huaweicloudsdkiotda.v5.model.update_desired import UpdateDesired
from huaweicloudsdkiotda.v5.model.update_desireds import UpdateDesireds
from huaweicloudsdkiotda.v5.model.update_device import UpdateDevice
from huaweicloudsdkiotda.v5.model.update_device_authorizer import UpdateDeviceAuthorizer
from huaweicloudsdkiotda.v5.model.update_device_authorizer_request import UpdateDeviceAuthorizerRequest
from huaweicloudsdkiotda.v5.model.update_device_authorizer_response import UpdateDeviceAuthorizerResponse
from huaweicloudsdkiotda.v5.model.update_device_group_dto import UpdateDeviceGroupDTO
from huaweicloudsdkiotda.v5.model.update_device_group_request import UpdateDeviceGroupRequest
from huaweicloudsdkiotda.v5.model.update_device_group_response import UpdateDeviceGroupResponse
from huaweicloudsdkiotda.v5.model.update_device_policy import UpdateDevicePolicy
from huaweicloudsdkiotda.v5.model.update_device_policy_request import UpdateDevicePolicyRequest
from huaweicloudsdkiotda.v5.model.update_device_policy_response import UpdateDevicePolicyResponse
from huaweicloudsdkiotda.v5.model.update_device_proxy import UpdateDeviceProxy
from huaweicloudsdkiotda.v5.model.update_device_proxy_request import UpdateDeviceProxyRequest
from huaweicloudsdkiotda.v5.model.update_device_proxy_response import UpdateDeviceProxyResponse
from huaweicloudsdkiotda.v5.model.update_device_request import UpdateDeviceRequest
from huaweicloudsdkiotda.v5.model.update_device_response import UpdateDeviceResponse
from huaweicloudsdkiotda.v5.model.update_device_shadow_desired_data_request import UpdateDeviceShadowDesiredDataRequest
from huaweicloudsdkiotda.v5.model.update_device_shadow_desired_data_response import UpdateDeviceShadowDesiredDataResponse
from huaweicloudsdkiotda.v5.model.update_flow_control_policy import UpdateFlowControlPolicy
from huaweicloudsdkiotda.v5.model.update_product import UpdateProduct
from huaweicloudsdkiotda.v5.model.update_product_request import UpdateProductRequest
from huaweicloudsdkiotda.v5.model.update_product_response import UpdateProductResponse
from huaweicloudsdkiotda.v5.model.update_properties_request import UpdatePropertiesRequest
from huaweicloudsdkiotda.v5.model.update_properties_response import UpdatePropertiesResponse
from huaweicloudsdkiotda.v5.model.update_provisioning_template import UpdateProvisioningTemplate
from huaweicloudsdkiotda.v5.model.update_provisioning_template_request import UpdateProvisioningTemplateRequest
from huaweicloudsdkiotda.v5.model.update_provisioning_template_response import UpdateProvisioningTemplateResponse
from huaweicloudsdkiotda.v5.model.update_routing_backlog_policy_request import UpdateRoutingBacklogPolicyRequest
from huaweicloudsdkiotda.v5.model.update_routing_backlog_policy_response import UpdateRoutingBacklogPolicyResponse
from huaweicloudsdkiotda.v5.model.update_routing_flow_control_policy_request import UpdateRoutingFlowControlPolicyRequest
from huaweicloudsdkiotda.v5.model.update_routing_flow_control_policy_response import UpdateRoutingFlowControlPolicyResponse
from huaweicloudsdkiotda.v5.model.update_routing_rule_request import UpdateRoutingRuleRequest
from huaweicloudsdkiotda.v5.model.update_routing_rule_response import UpdateRoutingRuleResponse
from huaweicloudsdkiotda.v5.model.update_rule_action_request import UpdateRuleActionRequest
from huaweicloudsdkiotda.v5.model.update_rule_action_response import UpdateRuleActionResponse
from huaweicloudsdkiotda.v5.model.update_rule_req import UpdateRuleReq
from huaweicloudsdkiotda.v5.model.update_rule_request import UpdateRuleRequest
from huaweicloudsdkiotda.v5.model.update_rule_response import UpdateRuleResponse
from huaweicloudsdkiotda.v5.model.upload_batch_task_file_request import UploadBatchTaskFileRequest
from huaweicloudsdkiotda.v5.model.upload_batch_task_file_request_body import UploadBatchTaskFileRequestBody
from huaweicloudsdkiotda.v5.model.upload_batch_task_file_response import UploadBatchTaskFileResponse
from huaweicloudsdkiotda.v5.model.user_prop_dto import UserPropDTO
from huaweicloudsdkiotda.v5.model.verify_certificate_dto import VerifyCertificateDTO


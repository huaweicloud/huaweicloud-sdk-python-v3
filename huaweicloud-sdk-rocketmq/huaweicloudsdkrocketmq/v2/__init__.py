# coding: utf-8

from __future__ import absolute_import

from huaweicloudsdkrocketmq.v2.rocketmq_client import RocketMQClient
from huaweicloudsdkrocketmq.v2.rocketmq_async_client import RocketMQAsyncClient

from huaweicloudsdkrocketmq.v2.model.batch_create_or_delete_rocketmq_tag_request import BatchCreateOrDeleteRocketmqTagRequest
from huaweicloudsdkrocketmq.v2.model.batch_create_or_delete_rocketmq_tag_response import BatchCreateOrDeleteRocketmqTagResponse
from huaweicloudsdkrocketmq.v2.model.batch_create_or_delete_tag_req import BatchCreateOrDeleteTagReq
from huaweicloudsdkrocketmq.v2.model.batch_delete_consumer_group_req import BatchDeleteConsumerGroupReq
from huaweicloudsdkrocketmq.v2.model.batch_delete_consumer_group_resp import BatchDeleteConsumerGroupResp
from huaweicloudsdkrocketmq.v2.model.batch_delete_diagnosis_report_req import BatchDeleteDiagnosisReportReq
from huaweicloudsdkrocketmq.v2.model.batch_delete_diagnosis_report_request import BatchDeleteDiagnosisReportRequest
from huaweicloudsdkrocketmq.v2.model.batch_delete_diagnosis_report_response import BatchDeleteDiagnosisReportResponse
from huaweicloudsdkrocketmq.v2.model.batch_delete_instance_req import BatchDeleteInstanceReq
from huaweicloudsdkrocketmq.v2.model.batch_delete_instance_resp_results import BatchDeleteInstanceRespResults
from huaweicloudsdkrocketmq.v2.model.batch_delete_instances_request import BatchDeleteInstancesRequest
from huaweicloudsdkrocketmq.v2.model.batch_delete_instances_response import BatchDeleteInstancesResponse
from huaweicloudsdkrocketmq.v2.model.batch_delete_topic_req import BatchDeleteTopicReq
from huaweicloudsdkrocketmq.v2.model.batch_delete_topic_resp import BatchDeleteTopicResp
from huaweicloudsdkrocketmq.v2.model.batch_update_consumer_group import BatchUpdateConsumerGroup
from huaweicloudsdkrocketmq.v2.model.batch_update_consumer_group_req import BatchUpdateConsumerGroupReq
from huaweicloudsdkrocketmq.v2.model.batch_update_consumer_group_request import BatchUpdateConsumerGroupRequest
from huaweicloudsdkrocketmq.v2.model.batch_update_consumer_group_response import BatchUpdateConsumerGroupResponse
from huaweicloudsdkrocketmq.v2.model.brokers import Brokers
from huaweicloudsdkrocketmq.v2.model.bss_param import BssParam
from huaweicloudsdkrocketmq.v2.model.client_data import ClientData
from huaweicloudsdkrocketmq.v2.model.consumer_detail_resp import ConsumerDetailResp
from huaweicloudsdkrocketmq.v2.model.consumer_group import ConsumerGroup
from huaweicloudsdkrocketmq.v2.model.consumer_list import ConsumerList
from huaweicloudsdkrocketmq.v2.model.create_consumer_group_or_batch_delete_consumer_group_req import CreateConsumerGroupOrBatchDeleteConsumerGroupReq
from huaweicloudsdkrocketmq.v2.model.create_consumer_group_or_batch_delete_consumer_group_request import CreateConsumerGroupOrBatchDeleteConsumerGroupRequest
from huaweicloudsdkrocketmq.v2.model.create_consumer_group_or_batch_delete_consumer_group_response import CreateConsumerGroupOrBatchDeleteConsumerGroupResponse
from huaweicloudsdkrocketmq.v2.model.create_diagnosis_task_request import CreateDiagnosisTaskRequest
from huaweicloudsdkrocketmq.v2.model.create_diagnosis_task_response import CreateDiagnosisTaskResponse
from huaweicloudsdkrocketmq.v2.model.create_group_resp import CreateGroupResp
from huaweicloudsdkrocketmq.v2.model.create_instance_by_engine_req import CreateInstanceByEngineReq
from huaweicloudsdkrocketmq.v2.model.create_instance_by_engine_request import CreateInstanceByEngineRequest
from huaweicloudsdkrocketmq.v2.model.create_instance_by_engine_response import CreateInstanceByEngineResponse
from huaweicloudsdkrocketmq.v2.model.create_or_update_consumer_group import CreateOrUpdateConsumerGroup
from huaweicloudsdkrocketmq.v2.model.create_post_paid_instance_req import CreatePostPaidInstanceReq
from huaweicloudsdkrocketmq.v2.model.create_post_paid_instance_request import CreatePostPaidInstanceRequest
from huaweicloudsdkrocketmq.v2.model.create_post_paid_instance_response import CreatePostPaidInstanceResponse
from huaweicloudsdkrocketmq.v2.model.create_rocket_mq_migration_task_req import CreateRocketMqMigrationTaskReq
from huaweicloudsdkrocketmq.v2.model.create_rocket_mq_migration_task_request import CreateRocketMqMigrationTaskRequest
from huaweicloudsdkrocketmq.v2.model.create_rocket_mq_migration_task_response import CreateRocketMqMigrationTaskResponse
from huaweicloudsdkrocketmq.v2.model.create_topic_or_batch_delete_topic_req import CreateTopicOrBatchDeleteTopicReq
from huaweicloudsdkrocketmq.v2.model.create_topic_or_batch_delete_topic_request import CreateTopicOrBatchDeleteTopicRequest
from huaweicloudsdkrocketmq.v2.model.create_topic_or_batch_delete_topic_response import CreateTopicOrBatchDeleteTopicResponse
from huaweicloudsdkrocketmq.v2.model.create_topic_req import CreateTopicReq
from huaweicloudsdkrocketmq.v2.model.create_topic_req_queues import CreateTopicReqQueues
from huaweicloudsdkrocketmq.v2.model.create_topic_resp import CreateTopicResp
from huaweicloudsdkrocketmq.v2.model.create_user_request import CreateUserRequest
from huaweicloudsdkrocketmq.v2.model.create_user_response import CreateUserResponse
from huaweicloudsdkrocketmq.v2.model.deadletter_resend_req import DeadletterResendReq
from huaweicloudsdkrocketmq.v2.model.deadletter_resend_resp_resend_results import DeadletterResendRespResendResults
from huaweicloudsdkrocketmq.v2.model.delete_background_task_request import DeleteBackgroundTaskRequest
from huaweicloudsdkrocketmq.v2.model.delete_background_task_response import DeleteBackgroundTaskResponse
from huaweicloudsdkrocketmq.v2.model.delete_consumer_group_request import DeleteConsumerGroupRequest
from huaweicloudsdkrocketmq.v2.model.delete_consumer_group_response import DeleteConsumerGroupResponse
from huaweicloudsdkrocketmq.v2.model.delete_instance_request import DeleteInstanceRequest
from huaweicloudsdkrocketmq.v2.model.delete_instance_response import DeleteInstanceResponse
from huaweicloudsdkrocketmq.v2.model.delete_rocket_mq_migration_task_request import DeleteRocketMqMigrationTaskRequest
from huaweicloudsdkrocketmq.v2.model.delete_rocket_mq_migration_task_response import DeleteRocketMqMigrationTaskResponse
from huaweicloudsdkrocketmq.v2.model.delete_topic_request import DeleteTopicRequest
from huaweicloudsdkrocketmq.v2.model.delete_topic_response import DeleteTopicResponse
from huaweicloudsdkrocketmq.v2.model.delete_user_request import DeleteUserRequest
from huaweicloudsdkrocketmq.v2.model.delete_user_response import DeleteUserResponse
from huaweicloudsdkrocketmq.v2.model.diagnosis_rep import DiagnosisRep
from huaweicloudsdkrocketmq.v2.model.diagnosis_report_resp import DiagnosisReportResp
from huaweicloudsdkrocketmq.v2.model.enable_dns_request import EnableDnsRequest
from huaweicloudsdkrocketmq.v2.model.enable_dns_response import EnableDnsResponse
from huaweicloudsdkrocketmq.v2.model.export_dlq_message_req import ExportDlqMessageReq
from huaweicloudsdkrocketmq.v2.model.export_dlq_message_request import ExportDlqMessageRequest
from huaweicloudsdkrocketmq.v2.model.export_dlq_message_response import ExportDlqMessageResponse
from huaweicloudsdkrocketmq.v2.model.instance_detail import InstanceDetail
from huaweicloudsdkrocketmq.v2.model.list_access_policy_resp_policies import ListAccessPolicyRespPolicies
from huaweicloudsdkrocketmq.v2.model.list_available_zones_request import ListAvailableZonesRequest
from huaweicloudsdkrocketmq.v2.model.list_available_zones_resp_available_zones import ListAvailableZonesRespAvailableZones
from huaweicloudsdkrocketmq.v2.model.list_available_zones_response import ListAvailableZonesResponse
from huaweicloudsdkrocketmq.v2.model.list_background_tasks_request import ListBackgroundTasksRequest
from huaweicloudsdkrocketmq.v2.model.list_background_tasks_resp_tasks import ListBackgroundTasksRespTasks
from huaweicloudsdkrocketmq.v2.model.list_background_tasks_response import ListBackgroundTasksResponse
from huaweicloudsdkrocketmq.v2.model.list_brokers_request import ListBrokersRequest
from huaweicloudsdkrocketmq.v2.model.list_brokers_resp_brokers import ListBrokersRespBrokers
from huaweicloudsdkrocketmq.v2.model.list_brokers_response import ListBrokersResponse
from huaweicloudsdkrocketmq.v2.model.list_consume_group_access_policy_request import ListConsumeGroupAccessPolicyRequest
from huaweicloudsdkrocketmq.v2.model.list_consume_group_access_policy_response import ListConsumeGroupAccessPolicyResponse
from huaweicloudsdkrocketmq.v2.model.list_consumer_group_of_topic_request import ListConsumerGroupOfTopicRequest
from huaweicloudsdkrocketmq.v2.model.list_consumer_group_of_topic_response import ListConsumerGroupOfTopicResponse
from huaweicloudsdkrocketmq.v2.model.list_diagnosis_reports_request import ListDiagnosisReportsRequest
from huaweicloudsdkrocketmq.v2.model.list_diagnosis_reports_response import ListDiagnosisReportsResponse
from huaweicloudsdkrocketmq.v2.model.list_engine_products_request import ListEngineProductsRequest
from huaweicloudsdkrocketmq.v2.model.list_engine_products_response import ListEngineProductsResponse
from huaweicloudsdkrocketmq.v2.model.list_instance_consumer_groups_request import ListInstanceConsumerGroupsRequest
from huaweicloudsdkrocketmq.v2.model.list_instance_consumer_groups_response import ListInstanceConsumerGroupsResponse
from huaweicloudsdkrocketmq.v2.model.list_instances_request import ListInstancesRequest
from huaweicloudsdkrocketmq.v2.model.list_instances_response import ListInstancesResponse
from huaweicloudsdkrocketmq.v2.model.list_message_trace_request import ListMessageTraceRequest
from huaweicloudsdkrocketmq.v2.model.list_message_trace_resp_trace import ListMessageTraceRespTrace
from huaweicloudsdkrocketmq.v2.model.list_message_trace_response import ListMessageTraceResponse
from huaweicloudsdkrocketmq.v2.model.list_messages_request import ListMessagesRequest
from huaweicloudsdkrocketmq.v2.model.list_messages_response import ListMessagesResponse
from huaweicloudsdkrocketmq.v2.model.list_rocket_instance_topics_request import ListRocketInstanceTopicsRequest
from huaweicloudsdkrocketmq.v2.model.list_rocket_instance_topics_response import ListRocketInstanceTopicsResponse
from huaweicloudsdkrocketmq.v2.model.list_rocket_mq_migration_task_request import ListRocketMqMigrationTaskRequest
from huaweicloudsdkrocketmq.v2.model.list_rocket_mq_migration_task_response import ListRocketMqMigrationTaskResponse
from huaweicloudsdkrocketmq.v2.model.list_topic_access_policy_request import ListTopicAccessPolicyRequest
from huaweicloudsdkrocketmq.v2.model.list_topic_access_policy_response import ListTopicAccessPolicyResponse
from huaweicloudsdkrocketmq.v2.model.list_user_request import ListUserRequest
from huaweicloudsdkrocketmq.v2.model.list_user_response import ListUserResponse
from huaweicloudsdkrocketmq.v2.model.message import Message
from huaweicloudsdkrocketmq.v2.model.message_property_list import MessagePropertyList
from huaweicloudsdkrocketmq.v2.model.metadata_delete_req import MetadataDeleteReq
from huaweicloudsdkrocketmq.v2.model.metadata_task import MetadataTask
from huaweicloudsdkrocketmq.v2.model.migration_rabbit_binding_metadata import MigrationRabbitBindingMetadata
from huaweicloudsdkrocketmq.v2.model.migration_rabbit_exchange_metadata import MigrationRabbitExchangeMetadata
from huaweicloudsdkrocketmq.v2.model.migration_rabbit_queue_metadata import MigrationRabbitQueueMetadata
from huaweicloudsdkrocketmq.v2.model.migration_rabbit_vhost_metadata import MigrationRabbitVhostMetadata
from huaweicloudsdkrocketmq.v2.model.migration_rocket_mq_subscription_group import MigrationRocketMqSubscriptionGroup
from huaweicloudsdkrocketmq.v2.model.migration_rocket_mq_topic_config import MigrationRocketMqTopicConfig
from huaweicloudsdkrocketmq.v2.model.modify_config_req import ModifyConfigReq
from huaweicloudsdkrocketmq.v2.model.modify_instance_ssl_config_request import ModifyInstanceSslConfigRequest
from huaweicloudsdkrocketmq.v2.model.modify_instance_ssl_config_response import ModifyInstanceSslConfigResponse
from huaweicloudsdkrocketmq.v2.model.node_context_entity import NodeContextEntity
from huaweicloudsdkrocketmq.v2.model.plain_ssl_switch_rep import PlainSSLSwitchRep
from huaweicloudsdkrocketmq.v2.model.product_entity import ProductEntity
from huaweicloudsdkrocketmq.v2.model.queue import Queue
from huaweicloudsdkrocketmq.v2.model.quota_resource_entity import QuotaResourceEntity
from huaweicloudsdkrocketmq.v2.model.quotas_resp_quotas import QuotasRespQuotas
from huaweicloudsdkrocketmq.v2.model.resend_req import ResendReq
from huaweicloudsdkrocketmq.v2.model.reset_consume_offset_req import ResetConsumeOffsetReq
from huaweicloudsdkrocketmq.v2.model.reset_consume_offset_request import ResetConsumeOffsetRequest
from huaweicloudsdkrocketmq.v2.model.reset_consume_offset_resp_queues import ResetConsumeOffsetRespQueues
from huaweicloudsdkrocketmq.v2.model.reset_consume_offset_response import ResetConsumeOffsetResponse
from huaweicloudsdkrocketmq.v2.model.resize_engine_instance_req import ResizeEngineInstanceReq
from huaweicloudsdkrocketmq.v2.model.resize_instance_request import ResizeInstanceRequest
from huaweicloudsdkrocketmq.v2.model.resize_instance_response import ResizeInstanceResponse
from huaweicloudsdkrocketmq.v2.model.rocket_mq_config_req import RocketMQConfigReq
from huaweicloudsdkrocketmq.v2.model.rocket_mq_config_resp import RocketMQConfigResp
from huaweicloudsdkrocketmq.v2.model.rocket_mq_extend_product_info_entity import RocketMQExtendProductInfoEntity
from huaweicloudsdkrocketmq.v2.model.rocket_mq_extend_product_ios_entity import RocketMQExtendProductIosEntity
from huaweicloudsdkrocketmq.v2.model.rocket_mq_extend_product_properties_entity import RocketMQExtendProductPropertiesEntity
from huaweicloudsdkrocketmq.v2.model.rocket_mq_product_support_features_entity import RocketMQProductSupportFeaturesEntity
from huaweicloudsdkrocketmq.v2.model.send_dlq_message_request import SendDlqMessageRequest
from huaweicloudsdkrocketmq.v2.model.send_dlq_message_response import SendDlqMessageResponse
from huaweicloudsdkrocketmq.v2.model.send_message_properties import SendMessageProperties
from huaweicloudsdkrocketmq.v2.model.send_message_request import SendMessageRequest
from huaweicloudsdkrocketmq.v2.model.send_message_resp import SendMessageResp
from huaweicloudsdkrocketmq.v2.model.send_message_response import SendMessageResponse
from huaweicloudsdkrocketmq.v2.model.show_consumer_connections_request import ShowConsumerConnectionsRequest
from huaweicloudsdkrocketmq.v2.model.show_consumer_connections_response import ShowConsumerConnectionsResponse
from huaweicloudsdkrocketmq.v2.model.show_consumer_list_or_details_request import ShowConsumerListOrDetailsRequest
from huaweicloudsdkrocketmq.v2.model.show_consumer_list_or_details_response import ShowConsumerListOrDetailsResponse
from huaweicloudsdkrocketmq.v2.model.show_diagnosis_report_request import ShowDiagnosisReportRequest
from huaweicloudsdkrocketmq.v2.model.show_diagnosis_report_response import ShowDiagnosisReportResponse
from huaweicloudsdkrocketmq.v2.model.show_diagnosis_stack_request import ShowDiagnosisStackRequest
from huaweicloudsdkrocketmq.v2.model.show_diagnosis_stack_response import ShowDiagnosisStackResponse
from huaweicloudsdkrocketmq.v2.model.show_engine_instance_extend_product_info_request import ShowEngineInstanceExtendProductInfoRequest
from huaweicloudsdkrocketmq.v2.model.show_engine_instance_extend_product_info_response import ShowEngineInstanceExtendProductInfoResponse
from huaweicloudsdkrocketmq.v2.model.show_group_request import ShowGroupRequest
from huaweicloudsdkrocketmq.v2.model.show_group_response import ShowGroupResponse
from huaweicloudsdkrocketmq.v2.model.show_instance_nodes_request import ShowInstanceNodesRequest
from huaweicloudsdkrocketmq.v2.model.show_instance_nodes_response import ShowInstanceNodesResponse
from huaweicloudsdkrocketmq.v2.model.show_instance_request import ShowInstanceRequest
from huaweicloudsdkrocketmq.v2.model.show_instance_response import ShowInstanceResponse
from huaweicloudsdkrocketmq.v2.model.show_one_topic_request import ShowOneTopicRequest
from huaweicloudsdkrocketmq.v2.model.show_one_topic_response import ShowOneTopicResponse
from huaweicloudsdkrocketmq.v2.model.show_quotas_request import ShowQuotasRequest
from huaweicloudsdkrocketmq.v2.model.show_quotas_response import ShowQuotasResponse
from huaweicloudsdkrocketmq.v2.model.show_rocket_mq_configs_request import ShowRocketMqConfigsRequest
from huaweicloudsdkrocketmq.v2.model.show_rocket_mq_configs_response import ShowRocketMqConfigsResponse
from huaweicloudsdkrocketmq.v2.model.show_rocketmq_project_tags_request import ShowRocketmqProjectTagsRequest
from huaweicloudsdkrocketmq.v2.model.show_rocketmq_project_tags_response import ShowRocketmqProjectTagsResponse
from huaweicloudsdkrocketmq.v2.model.show_rocketmq_tags_request import ShowRocketmqTagsRequest
from huaweicloudsdkrocketmq.v2.model.show_rocketmq_tags_response import ShowRocketmqTagsResponse
from huaweicloudsdkrocketmq.v2.model.show_topic_status_request import ShowTopicStatusRequest
from huaweicloudsdkrocketmq.v2.model.show_topic_status_resp_brokers import ShowTopicStatusRespBrokers
from huaweicloudsdkrocketmq.v2.model.show_topic_status_resp_queues import ShowTopicStatusRespQueues
from huaweicloudsdkrocketmq.v2.model.show_topic_status_response import ShowTopicStatusResponse
from huaweicloudsdkrocketmq.v2.model.show_user_request import ShowUserRequest
from huaweicloudsdkrocketmq.v2.model.show_user_response import ShowUserResponse
from huaweicloudsdkrocketmq.v2.model.subscription import Subscription
from huaweicloudsdkrocketmq.v2.model.tag_entity import TagEntity
from huaweicloudsdkrocketmq.v2.model.tag_multy_value_entity import TagMultyValueEntity
from huaweicloudsdkrocketmq.v2.model.topic import Topic
from huaweicloudsdkrocketmq.v2.model.topic_brokers import TopicBrokers
from huaweicloudsdkrocketmq.v2.model.update_consumer_group import UpdateConsumerGroup
from huaweicloudsdkrocketmq.v2.model.update_consumer_group_request import UpdateConsumerGroupRequest
from huaweicloudsdkrocketmq.v2.model.update_consumer_group_response import UpdateConsumerGroupResponse
from huaweicloudsdkrocketmq.v2.model.update_instance_req import UpdateInstanceReq
from huaweicloudsdkrocketmq.v2.model.update_instance_request import UpdateInstanceRequest
from huaweicloudsdkrocketmq.v2.model.update_instance_response import UpdateInstanceResponse
from huaweicloudsdkrocketmq.v2.model.update_rocket_mq_configs_request import UpdateRocketMqConfigsRequest
from huaweicloudsdkrocketmq.v2.model.update_rocket_mq_configs_response import UpdateRocketMqConfigsResponse
from huaweicloudsdkrocketmq.v2.model.update_topic_queue_entity import UpdateTopicQueueEntity
from huaweicloudsdkrocketmq.v2.model.update_topic_req import UpdateTopicReq
from huaweicloudsdkrocketmq.v2.model.update_topic_request import UpdateTopicRequest
from huaweicloudsdkrocketmq.v2.model.update_topic_response import UpdateTopicResponse
from huaweicloudsdkrocketmq.v2.model.update_user_request import UpdateUserRequest
from huaweicloudsdkrocketmq.v2.model.update_user_response import UpdateUserResponse
from huaweicloudsdkrocketmq.v2.model.user import User
from huaweicloudsdkrocketmq.v2.model.user_group_perms import UserGroupPerms
from huaweicloudsdkrocketmq.v2.model.user_topic_perms import UserTopicPerms
from huaweicloudsdkrocketmq.v2.model.validate_consumed_message_request import ValidateConsumedMessageRequest
from huaweicloudsdkrocketmq.v2.model.validate_consumed_message_response import ValidateConsumedMessageResponse


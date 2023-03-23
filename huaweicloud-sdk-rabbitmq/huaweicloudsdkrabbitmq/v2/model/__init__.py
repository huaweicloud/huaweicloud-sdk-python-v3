# coding: utf-8

from __future__ import absolute_import

# import models into model package
from huaweicloudsdkrabbitmq.v2.model.batch_create_or_delete_rabbit_mq_tag_request import BatchCreateOrDeleteRabbitMqTagRequest
from huaweicloudsdkrabbitmq.v2.model.batch_create_or_delete_rabbit_mq_tag_response import BatchCreateOrDeleteRabbitMqTagResponse
from huaweicloudsdkrabbitmq.v2.model.batch_create_or_delete_tag_req import BatchCreateOrDeleteTagReq
from huaweicloudsdkrabbitmq.v2.model.batch_restart_or_delete_instance_req import BatchRestartOrDeleteInstanceReq
from huaweicloudsdkrabbitmq.v2.model.batch_restart_or_delete_instance_resp_results import BatchRestartOrDeleteInstanceRespResults
from huaweicloudsdkrabbitmq.v2.model.batch_restart_or_delete_instances_request import BatchRestartOrDeleteInstancesRequest
from huaweicloudsdkrabbitmq.v2.model.batch_restart_or_delete_instances_response import BatchRestartOrDeleteInstancesResponse
from huaweicloudsdkrabbitmq.v2.model.create_instance_req import CreateInstanceReq
from huaweicloudsdkrabbitmq.v2.model.create_post_paid_instance_by_engine_request import CreatePostPaidInstanceByEngineRequest
from huaweicloudsdkrabbitmq.v2.model.create_post_paid_instance_by_engine_response import CreatePostPaidInstanceByEngineResponse
from huaweicloudsdkrabbitmq.v2.model.create_post_paid_instance_request import CreatePostPaidInstanceRequest
from huaweicloudsdkrabbitmq.v2.model.create_post_paid_instance_response import CreatePostPaidInstanceResponse
from huaweicloudsdkrabbitmq.v2.model.delete_background_task_request import DeleteBackgroundTaskRequest
from huaweicloudsdkrabbitmq.v2.model.delete_background_task_response import DeleteBackgroundTaskResponse
from huaweicloudsdkrabbitmq.v2.model.delete_instance_request import DeleteInstanceRequest
from huaweicloudsdkrabbitmq.v2.model.delete_instance_response import DeleteInstanceResponse
from huaweicloudsdkrabbitmq.v2.model.list_available_zones_request import ListAvailableZonesRequest
from huaweicloudsdkrabbitmq.v2.model.list_available_zones_resp_available_zones import ListAvailableZonesRespAvailableZones
from huaweicloudsdkrabbitmq.v2.model.list_available_zones_response import ListAvailableZonesResponse
from huaweicloudsdkrabbitmq.v2.model.list_background_tasks_request import ListBackgroundTasksRequest
from huaweicloudsdkrabbitmq.v2.model.list_background_tasks_resp_tasks import ListBackgroundTasksRespTasks
from huaweicloudsdkrabbitmq.v2.model.list_background_tasks_response import ListBackgroundTasksResponse
from huaweicloudsdkrabbitmq.v2.model.list_engine_ios_entity import ListEngineIosEntity
from huaweicloudsdkrabbitmq.v2.model.list_engine_products_entity import ListEngineProductsEntity
from huaweicloudsdkrabbitmq.v2.model.list_engine_products_request import ListEngineProductsRequest
from huaweicloudsdkrabbitmq.v2.model.list_engine_products_response import ListEngineProductsResponse
from huaweicloudsdkrabbitmq.v2.model.list_engine_properties_entity import ListEnginePropertiesEntity
from huaweicloudsdkrabbitmq.v2.model.list_instances_details_request import ListInstancesDetailsRequest
from huaweicloudsdkrabbitmq.v2.model.list_instances_details_response import ListInstancesDetailsResponse
from huaweicloudsdkrabbitmq.v2.model.list_plugins_request import ListPluginsRequest
from huaweicloudsdkrabbitmq.v2.model.list_plugins_response import ListPluginsResponse
from huaweicloudsdkrabbitmq.v2.model.list_products_request import ListProductsRequest
from huaweicloudsdkrabbitmq.v2.model.list_products_resp_detail import ListProductsRespDetail
from huaweicloudsdkrabbitmq.v2.model.list_products_resp_hourly import ListProductsRespHourly
from huaweicloudsdkrabbitmq.v2.model.list_products_resp_io import ListProductsRespIo
from huaweicloudsdkrabbitmq.v2.model.list_products_resp_values import ListProductsRespValues
from huaweicloudsdkrabbitmq.v2.model.list_products_response import ListProductsResponse
from huaweicloudsdkrabbitmq.v2.model.maintain_windows_entity import MaintainWindowsEntity
from huaweicloudsdkrabbitmq.v2.model.plugin_entity import PluginEntity
from huaweicloudsdkrabbitmq.v2.model.rabbit_mq_extend_product_info_entity import RabbitMQExtendProductInfoEntity
from huaweicloudsdkrabbitmq.v2.model.rabbit_mq_extend_product_ios_entity import RabbitMQExtendProductIosEntity
from huaweicloudsdkrabbitmq.v2.model.rabbit_mq_extend_product_properties_entity import RabbitMQExtendProductPropertiesEntity
from huaweicloudsdkrabbitmq.v2.model.rabbit_mq_product_support_features_entity import RabbitMQProductSupportFeaturesEntity
from huaweicloudsdkrabbitmq.v2.model.reset_password_req import ResetPasswordReq
from huaweicloudsdkrabbitmq.v2.model.reset_password_request import ResetPasswordRequest
from huaweicloudsdkrabbitmq.v2.model.reset_password_response import ResetPasswordResponse
from huaweicloudsdkrabbitmq.v2.model.resize_engine_instance_req import ResizeEngineInstanceReq
from huaweicloudsdkrabbitmq.v2.model.resize_engine_instance_request import ResizeEngineInstanceRequest
from huaweicloudsdkrabbitmq.v2.model.resize_engine_instance_response import ResizeEngineInstanceResponse
from huaweicloudsdkrabbitmq.v2.model.resize_instance_req import ResizeInstanceReq
from huaweicloudsdkrabbitmq.v2.model.resize_instance_request import ResizeInstanceRequest
from huaweicloudsdkrabbitmq.v2.model.resize_instance_response import ResizeInstanceResponse
from huaweicloudsdkrabbitmq.v2.model.show_background_task_request import ShowBackgroundTaskRequest
from huaweicloudsdkrabbitmq.v2.model.show_background_task_response import ShowBackgroundTaskResponse
from huaweicloudsdkrabbitmq.v2.model.show_engine_instance_extend_product_info_request import ShowEngineInstanceExtendProductInfoRequest
from huaweicloudsdkrabbitmq.v2.model.show_engine_instance_extend_product_info_response import ShowEngineInstanceExtendProductInfoResponse
from huaweicloudsdkrabbitmq.v2.model.show_instance_extend_product_info_request import ShowInstanceExtendProductInfoRequest
from huaweicloudsdkrabbitmq.v2.model.show_instance_extend_product_info_response import ShowInstanceExtendProductInfoResponse
from huaweicloudsdkrabbitmq.v2.model.show_instance_request import ShowInstanceRequest
from huaweicloudsdkrabbitmq.v2.model.show_instance_resp import ShowInstanceResp
from huaweicloudsdkrabbitmq.v2.model.show_instance_response import ShowInstanceResponse
from huaweicloudsdkrabbitmq.v2.model.show_maintain_windows_request import ShowMaintainWindowsRequest
from huaweicloudsdkrabbitmq.v2.model.show_maintain_windows_response import ShowMaintainWindowsResponse
from huaweicloudsdkrabbitmq.v2.model.show_rabbit_mq_project_tags_request import ShowRabbitMqProjectTagsRequest
from huaweicloudsdkrabbitmq.v2.model.show_rabbit_mq_project_tags_response import ShowRabbitMqProjectTagsResponse
from huaweicloudsdkrabbitmq.v2.model.show_rabbit_mq_tags_request import ShowRabbitMqTagsRequest
from huaweicloudsdkrabbitmq.v2.model.show_rabbit_mq_tags_response import ShowRabbitMqTagsResponse
from huaweicloudsdkrabbitmq.v2.model.tag_entity import TagEntity
from huaweicloudsdkrabbitmq.v2.model.tag_multy_value_entity import TagMultyValueEntity
from huaweicloudsdkrabbitmq.v2.model.update_instance_req import UpdateInstanceReq
from huaweicloudsdkrabbitmq.v2.model.update_instance_request import UpdateInstanceRequest
from huaweicloudsdkrabbitmq.v2.model.update_instance_response import UpdateInstanceResponse
from huaweicloudsdkrabbitmq.v2.model.update_plugins_req import UpdatePluginsReq
from huaweicloudsdkrabbitmq.v2.model.update_plugins_request import UpdatePluginsRequest
from huaweicloudsdkrabbitmq.v2.model.update_plugins_response import UpdatePluginsResponse

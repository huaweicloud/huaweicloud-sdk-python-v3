# coding: utf-8

from __future__ import absolute_import

import importlib
import warnings

from huaweicloudsdkcore.client import Client, ClientBuilder
from huaweicloudsdkcore.utils import http_utils
from huaweicloudsdkcore.sdk_stream_request import SdkStreamRequest

try:
    from huaweicloudsdkcore.invoker.invoker import AsyncInvoker
except ImportError as e:
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkrocketmq'")


class RocketMQAsyncClient(Client):
    def __init__(self):
        super(RocketMQAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkrocketmq.v2.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "RocketMQAsyncClient":
                raise TypeError("client type error, support client type is RocketMQAsyncClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def batch_create_or_delete_rocketmq_tag_async(self, request):
        r"""批量添加或删除实例标签

        批量添加或删除实例标签。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchCreateOrDeleteRocketmqTag
        :type request: :class:`huaweicloudsdkrocketmq.v2.BatchCreateOrDeleteRocketmqTagRequest`
        :rtype: :class:`huaweicloudsdkrocketmq.v2.BatchCreateOrDeleteRocketmqTagResponse`
        """
        http_info = self._batch_create_or_delete_rocketmq_tag_http_info(request)
        return self._call_api(**http_info)

    def batch_create_or_delete_rocketmq_tag_async_invoker(self, request):
        http_info = self._batch_create_or_delete_rocketmq_tag_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_create_or_delete_rocketmq_tag_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/rocketmq/{instance_id}/tags/action",
            "request_type": request.__class__.__name__,
            "response_type": "BatchCreateOrDeleteRocketmqTagResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def batch_delete_diagnosis_report_async(self, request):
        r"""批量删除实例诊断记录

        批量删除实例诊断记录。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchDeleteDiagnosisReport
        :type request: :class:`huaweicloudsdkrocketmq.v2.BatchDeleteDiagnosisReportRequest`
        :rtype: :class:`huaweicloudsdkrocketmq.v2.BatchDeleteDiagnosisReportResponse`
        """
        http_info = self._batch_delete_diagnosis_report_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_diagnosis_report_async_invoker(self, request):
        http_info = self._batch_delete_diagnosis_report_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_delete_diagnosis_report_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{engine}/{project_id}/instances/{instance_id}/diagnosis",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeleteDiagnosisReportResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'engine' in local_var_params:
            path_params['engine'] = local_var_params['engine']
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def batch_delete_instances_async(self, request):
        r"""批量删除实例

        批量删除实例。**实例删除后，实例中原有的数据将被删除，且没有备份，请谨慎操作。**
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchDeleteInstances
        :type request: :class:`huaweicloudsdkrocketmq.v2.BatchDeleteInstancesRequest`
        :rtype: :class:`huaweicloudsdkrocketmq.v2.BatchDeleteInstancesResponse`
        """
        http_info = self._batch_delete_instances_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_instances_async_invoker(self, request):
        http_info = self._batch_delete_instances_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_delete_instances_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/instances/action",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeleteInstancesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def batch_update_consumer_group_async(self, request):
        r"""批量修改消费组

        批量修改消费组。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchUpdateConsumerGroup
        :type request: :class:`huaweicloudsdkrocketmq.v2.BatchUpdateConsumerGroupRequest`
        :rtype: :class:`huaweicloudsdkrocketmq.v2.BatchUpdateConsumerGroupResponse`
        """
        http_info = self._batch_update_consumer_group_http_info(request)
        return self._call_api(**http_info)

    def batch_update_consumer_group_async_invoker(self, request):
        http_info = self._batch_update_consumer_group_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_update_consumer_group_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/groups",
            "request_type": request.__class__.__name__,
            "response_type": "BatchUpdateConsumerGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_consumer_group_or_batch_delete_consumer_group_async(self, request):
        r"""创建消费组或批量删除消费组

        创建消费组或批量删除消费组。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateConsumerGroupOrBatchDeleteConsumerGroup
        :type request: :class:`huaweicloudsdkrocketmq.v2.CreateConsumerGroupOrBatchDeleteConsumerGroupRequest`
        :rtype: :class:`huaweicloudsdkrocketmq.v2.CreateConsumerGroupOrBatchDeleteConsumerGroupResponse`
        """
        http_info = self._create_consumer_group_or_batch_delete_consumer_group_http_info(request)
        return self._call_api(**http_info)

    def create_consumer_group_or_batch_delete_consumer_group_async_invoker(self, request):
        http_info = self._create_consumer_group_or_batch_delete_consumer_group_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_consumer_group_or_batch_delete_consumer_group_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/groups",
            "request_type": request.__class__.__name__,
            "response_type": "CreateConsumerGroupOrBatchDeleteConsumerGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'action' in local_var_params:
            query_params.append(('action', local_var_params['action']))

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_diagnosis_task_async(self, request):
        r"""创建实例诊断任务

        创建实例诊断任务。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateDiagnosisTask
        :type request: :class:`huaweicloudsdkrocketmq.v2.CreateDiagnosisTaskRequest`
        :rtype: :class:`huaweicloudsdkrocketmq.v2.CreateDiagnosisTaskResponse`
        """
        http_info = self._create_diagnosis_task_http_info(request)
        return self._call_api(**http_info)

    def create_diagnosis_task_async_invoker(self, request):
        http_info = self._create_diagnosis_task_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_diagnosis_task_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{engine}/{project_id}/instances/{instance_id}/diagnosis",
            "request_type": request.__class__.__name__,
            "response_type": "CreateDiagnosisTaskResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'engine' in local_var_params:
            path_params['engine'] = local_var_params['engine']
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_instance_by_engine_async(self, request):
        r"""创建实例

        创建实例[，该接口支持创建按需和包周期两种计费方式的实例](tag:hws,hws_eu,hws_hk,ocb,hws_ocb,ctc,g42,hk_g42,tm,hk_tm)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateInstanceByEngine
        :type request: :class:`huaweicloudsdkrocketmq.v2.CreateInstanceByEngineRequest`
        :rtype: :class:`huaweicloudsdkrocketmq.v2.CreateInstanceByEngineResponse`
        """
        http_info = self._create_instance_by_engine_http_info(request)
        return self._call_api(**http_info)

    def create_instance_by_engine_async_invoker(self, request):
        http_info = self._create_instance_by_engine_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_instance_by_engine_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{engine}/{project_id}/instances",
            "request_type": request.__class__.__name__,
            "response_type": "CreateInstanceByEngineResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'engine' in local_var_params:
            path_params['engine'] = local_var_params['engine']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_post_paid_instance_async(self, request):
        r"""创建实例（按需）

        创建实例，该接口创建的实例为按需计费的方式。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreatePostPaidInstance
        :type request: :class:`huaweicloudsdkrocketmq.v2.CreatePostPaidInstanceRequest`
        :rtype: :class:`huaweicloudsdkrocketmq.v2.CreatePostPaidInstanceResponse`
        """
        http_info = self._create_post_paid_instance_http_info(request)
        return self._call_api(**http_info)

    def create_post_paid_instance_async_invoker(self, request):
        http_info = self._create_post_paid_instance_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_post_paid_instance_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/instances",
            "request_type": request.__class__.__name__,
            "response_type": "CreatePostPaidInstanceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_rocket_mq_migration_task_async(self, request):
        r"""新建元数据迁移任务

        新建元数据迁移任务。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateRocketMqMigrationTask
        :type request: :class:`huaweicloudsdkrocketmq.v2.CreateRocketMqMigrationTaskRequest`
        :rtype: :class:`huaweicloudsdkrocketmq.v2.CreateRocketMqMigrationTaskResponse`
        """
        http_info = self._create_rocket_mq_migration_task_http_info(request)
        return self._call_api(**http_info)

    def create_rocket_mq_migration_task_async_invoker(self, request):
        http_info = self._create_rocket_mq_migration_task_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_rocket_mq_migration_task_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/metadata",
            "request_type": request.__class__.__name__,
            "response_type": "CreateRocketMqMigrationTaskResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'overwrite' in local_var_params:
            query_params.append(('overwrite', local_var_params['overwrite']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_user_async(self, request):
        r"""创建用户

        创建用户。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateUser
        :type request: :class:`huaweicloudsdkrocketmq.v2.CreateUserRequest`
        :rtype: :class:`huaweicloudsdkrocketmq.v2.CreateUserResponse`
        """
        http_info = self._create_user_http_info(request)
        return self._call_api(**http_info)

    def create_user_async_invoker(self, request):
        http_info = self._create_user_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_user_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/users",
            "request_type": request.__class__.__name__,
            "response_type": "CreateUserResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_background_task_async(self, request):
        r"""删除后台任务管理中的指定记录

        删除后台任务管理中的指定记录。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteBackgroundTask
        :type request: :class:`huaweicloudsdkrocketmq.v2.DeleteBackgroundTaskRequest`
        :rtype: :class:`huaweicloudsdkrocketmq.v2.DeleteBackgroundTaskResponse`
        """
        http_info = self._delete_background_task_http_info(request)
        return self._call_api(**http_info)

    def delete_background_task_async_invoker(self, request):
        http_info = self._delete_background_task_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_background_task_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/tasks/{task_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteBackgroundTaskResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_consumer_group_async(self, request):
        r"""删除指定消费组

        删除指定消费组。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteConsumerGroup
        :type request: :class:`huaweicloudsdkrocketmq.v2.DeleteConsumerGroupRequest`
        :rtype: :class:`huaweicloudsdkrocketmq.v2.DeleteConsumerGroupResponse`
        """
        http_info = self._delete_consumer_group_http_info(request)
        return self._call_api(**http_info)

    def delete_consumer_group_async_invoker(self, request):
        http_info = self._delete_consumer_group_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_consumer_group_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/groups/{group}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteConsumerGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'group' in local_var_params:
            path_params['group'] = local_var_params['group']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_instance_async(self, request):
        r"""删除指定的实例

        删除指定的实例，释放该实例的所有资源。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteInstance
        :type request: :class:`huaweicloudsdkrocketmq.v2.DeleteInstanceRequest`
        :rtype: :class:`huaweicloudsdkrocketmq.v2.DeleteInstanceResponse`
        """
        http_info = self._delete_instance_http_info(request)
        return self._call_api(**http_info)

    def delete_instance_async_invoker(self, request):
        http_info = self._delete_instance_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_instance_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/instances/{instance_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteInstanceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_rocket_mq_migration_task_async(self, request):
        r"""删除元数据迁移任务

        删除元数据迁移任务。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteRocketMqMigrationTask
        :type request: :class:`huaweicloudsdkrocketmq.v2.DeleteRocketMqMigrationTaskRequest`
        :rtype: :class:`huaweicloudsdkrocketmq.v2.DeleteRocketMqMigrationTaskResponse`
        """
        http_info = self._delete_rocket_mq_migration_task_http_info(request)
        return self._call_api(**http_info)

    def delete_rocket_mq_migration_task_async_invoker(self, request):
        http_info = self._delete_rocket_mq_migration_task_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_rocket_mq_migration_task_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/metadata",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteRocketMqMigrationTaskResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_user_async(self, request):
        r"""删除用户

        删除用户。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteUser
        :type request: :class:`huaweicloudsdkrocketmq.v2.DeleteUserRequest`
        :rtype: :class:`huaweicloudsdkrocketmq.v2.DeleteUserResponse`
        """
        http_info = self._delete_user_http_info(request)
        return self._call_api(**http_info)

    def delete_user_async_invoker(self, request):
        http_info = self._delete_user_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_user_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/users/{user_name}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteUserResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'user_name' in local_var_params:
            path_params['user_name'] = local_var_params['user_name']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def enable_dns_async(self, request):
        r"""开启RocketMQ实例域名访问能力

        开启RocketMQ实例域名访问能力。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for EnableDns
        :type request: :class:`huaweicloudsdkrocketmq.v2.EnableDnsRequest`
        :rtype: :class:`huaweicloudsdkrocketmq.v2.EnableDnsResponse`
        """
        http_info = self._enable_dns_http_info(request)
        return self._call_api(**http_info)

    def enable_dns_async_invoker(self, request):
        http_info = self._enable_dns_http_info(request)
        return AsyncInvoker(self, http_info)

    def _enable_dns_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/rocketmq/instances/{instance_id}/dns",
            "request_type": request.__class__.__name__,
            "response_type": "EnableDnsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def export_dlq_message_async(self, request):
        r"""导出死信消息

        导出死信消息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ExportDlqMessage
        :type request: :class:`huaweicloudsdkrocketmq.v2.ExportDlqMessageRequest`
        :rtype: :class:`huaweicloudsdkrocketmq.v2.ExportDlqMessageResponse`
        """
        http_info = self._export_dlq_message_http_info(request)
        return self._call_api(**http_info)

    def export_dlq_message_async_invoker(self, request):
        http_info = self._export_dlq_message_http_info(request)
        return AsyncInvoker(self, http_info)

    def _export_dlq_message_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/messages/export",
            "request_type": request.__class__.__name__,
            "response_type": "ExportDlqMessageResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_available_zones_async(self, request):
        r"""查询可用区信息

        在创建实例时，需要配置实例所在的可用区ID，可通过该接口查询可用区的ID。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAvailableZones
        :type request: :class:`huaweicloudsdkrocketmq.v2.ListAvailableZonesRequest`
        :rtype: :class:`huaweicloudsdkrocketmq.v2.ListAvailableZonesResponse`
        """
        http_info = self._list_available_zones_http_info(request)
        return self._call_api(**http_info)

    def list_available_zones_async_invoker(self, request):
        http_info = self._list_available_zones_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_available_zones_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/available-zones",
            "request_type": request.__class__.__name__,
            "response_type": "ListAvailableZonesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_background_tasks_async(self, request):
        r"""查询实例的后台任务列表

        查询实例的后台任务列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListBackgroundTasks
        :type request: :class:`huaweicloudsdkrocketmq.v2.ListBackgroundTasksRequest`
        :rtype: :class:`huaweicloudsdkrocketmq.v2.ListBackgroundTasksResponse`
        """
        http_info = self._list_background_tasks_http_info(request)
        return self._call_api(**http_info)

    def list_background_tasks_async_invoker(self, request):
        http_info = self._list_background_tasks_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_background_tasks_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/tasks",
            "request_type": request.__class__.__name__,
            "response_type": "ListBackgroundTasksResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'start' in local_var_params:
            query_params.append(('start', local_var_params['start']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'begin_time' in local_var_params:
            query_params.append(('begin_time', local_var_params['begin_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_brokers_async(self, request):
        r"""查询代理列表

        查询代理列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListBrokers
        :type request: :class:`huaweicloudsdkrocketmq.v2.ListBrokersRequest`
        :rtype: :class:`huaweicloudsdkrocketmq.v2.ListBrokersResponse`
        """
        http_info = self._list_brokers_http_info(request)
        return self._call_api(**http_info)

    def list_brokers_async_invoker(self, request):
        http_info = self._list_brokers_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_brokers_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/brokers",
            "request_type": request.__class__.__name__,
            "response_type": "ListBrokersResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_consume_group_access_policy_async(self, request):
        r"""查询消费组的授权用户列表

        查询消费组的授权用户列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListConsumeGroupAccessPolicy
        :type request: :class:`huaweicloudsdkrocketmq.v2.ListConsumeGroupAccessPolicyRequest`
        :rtype: :class:`huaweicloudsdkrocketmq.v2.ListConsumeGroupAccessPolicyResponse`
        """
        http_info = self._list_consume_group_access_policy_http_info(request)
        return self._call_api(**http_info)

    def list_consume_group_access_policy_async_invoker(self, request):
        http_info = self._list_consume_group_access_policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_consume_group_access_policy_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{engine}/{project_id}/instances/{instance_id}/groups/{group_id}/accesspolicy",
            "request_type": request.__class__.__name__,
            "response_type": "ListConsumeGroupAccessPolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'engine' in local_var_params:
            path_params['engine'] = local_var_params['engine']
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_diagnosis_reports_async(self, request):
        r"""查询实例诊断报告列表

        查询实例诊断报告列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListDiagnosisReports
        :type request: :class:`huaweicloudsdkrocketmq.v2.ListDiagnosisReportsRequest`
        :rtype: :class:`huaweicloudsdkrocketmq.v2.ListDiagnosisReportsResponse`
        """
        http_info = self._list_diagnosis_reports_http_info(request)
        return self._call_api(**http_info)

    def list_diagnosis_reports_async_invoker(self, request):
        http_info = self._list_diagnosis_reports_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_diagnosis_reports_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{engine}/{project_id}/instances/{instance_id}/diagnosis",
            "request_type": request.__class__.__name__,
            "response_type": "ListDiagnosisReportsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'engine' in local_var_params:
            path_params['engine'] = local_var_params['engine']
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_engine_products_async(self, request):
        r"""查询产品规格列表

        查询相应引擎的产品规格列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListEngineProducts
        :type request: :class:`huaweicloudsdkrocketmq.v2.ListEngineProductsRequest`
        :rtype: :class:`huaweicloudsdkrocketmq.v2.ListEngineProductsResponse`
        """
        http_info = self._list_engine_products_http_info(request)
        return self._call_api(**http_info)

    def list_engine_products_async_invoker(self, request):
        http_info = self._list_engine_products_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_engine_products_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{engine}/products",
            "request_type": request.__class__.__name__,
            "response_type": "ListEngineProductsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'engine' in local_var_params:
            path_params['engine'] = local_var_params['engine']

        query_params = []
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'product_id' in local_var_params:
            query_params.append(('product_id', local_var_params['product_id']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_instance_consumer_groups_async(self, request):
        r"""查询消费组列表

        查询消费组列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListInstanceConsumerGroups
        :type request: :class:`huaweicloudsdkrocketmq.v2.ListInstanceConsumerGroupsRequest`
        :rtype: :class:`huaweicloudsdkrocketmq.v2.ListInstanceConsumerGroupsResponse`
        """
        http_info = self._list_instance_consumer_groups_http_info(request)
        return self._call_api(**http_info)

    def list_instance_consumer_groups_async_invoker(self, request):
        http_info = self._list_instance_consumer_groups_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_instance_consumer_groups_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/groups",
            "request_type": request.__class__.__name__,
            "response_type": "ListInstanceConsumerGroupsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'group' in local_var_params:
            query_params.append(('group', local_var_params['group']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_instances_async(self, request):
        r"""查询所有实例列表

        查询租户的实例列表，支持按照条件查询。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListInstances
        :type request: :class:`huaweicloudsdkrocketmq.v2.ListInstancesRequest`
        :rtype: :class:`huaweicloudsdkrocketmq.v2.ListInstancesResponse`
        """
        http_info = self._list_instances_http_info(request)
        return self._call_api(**http_info)

    def list_instances_async_invoker(self, request):
        http_info = self._list_instances_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_instances_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/instances",
            "request_type": request.__class__.__name__,
            "response_type": "ListInstancesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'engine' in local_var_params:
            query_params.append(('engine', local_var_params['engine']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'instance_id' in local_var_params:
            query_params.append(('instance_id', local_var_params['instance_id']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'include_failure' in local_var_params:
            query_params.append(('include_failure', local_var_params['include_failure']))
        if 'exact_match_name' in local_var_params:
            query_params.append(('exact_match_name', local_var_params['exact_match_name']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_message_trace_async(self, request):
        r"""查询消息轨迹

        查询消息轨迹。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListMessageTrace
        :type request: :class:`huaweicloudsdkrocketmq.v2.ListMessageTraceRequest`
        :rtype: :class:`huaweicloudsdkrocketmq.v2.ListMessageTraceResponse`
        """
        http_info = self._list_message_trace_http_info(request)
        return self._call_api(**http_info)

    def list_message_trace_async_invoker(self, request):
        http_info = self._list_message_trace_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_message_trace_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{engine}/{project_id}/instances/{instance_id}/trace",
            "request_type": request.__class__.__name__,
            "response_type": "ListMessageTraceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'engine' in local_var_params:
            path_params['engine'] = local_var_params['engine']
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'msg_id' in local_var_params:
            query_params.append(('msg_id', local_var_params['msg_id']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_messages_async(self, request):
        r"""查询消息

        查询消息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListMessages
        :type request: :class:`huaweicloudsdkrocketmq.v2.ListMessagesRequest`
        :rtype: :class:`huaweicloudsdkrocketmq.v2.ListMessagesResponse`
        """
        http_info = self._list_messages_http_info(request)
        return self._call_api(**http_info)

    def list_messages_async_invoker(self, request):
        http_info = self._list_messages_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_messages_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{engine}/{project_id}/instances/{instance_id}/messages",
            "request_type": request.__class__.__name__,
            "response_type": "ListMessagesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'engine' in local_var_params:
            path_params['engine'] = local_var_params['engine']
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'topic' in local_var_params:
            query_params.append(('topic', local_var_params['topic']))
        if 'queue' in local_var_params:
            query_params.append(('queue', local_var_params['queue']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'key' in local_var_params:
            query_params.append(('key', local_var_params['key']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'msg_id' in local_var_params:
            query_params.append(('msg_id', local_var_params['msg_id']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_rocket_mq_migration_task_async(self, request):
        r"""查询实例下所有迁移任务或查询指定迁移任务信息

        1. 查询实例下所有迁移任务
        2. 查询指定迁移任务信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListRocketMqMigrationTask
        :type request: :class:`huaweicloudsdkrocketmq.v2.ListRocketMqMigrationTaskRequest`
        :rtype: :class:`huaweicloudsdkrocketmq.v2.ListRocketMqMigrationTaskResponse`
        """
        http_info = self._list_rocket_mq_migration_task_http_info(request)
        return self._call_api(**http_info)

    def list_rocket_mq_migration_task_async_invoker(self, request):
        http_info = self._list_rocket_mq_migration_task_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_rocket_mq_migration_task_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/metadata",
            "request_type": request.__class__.__name__,
            "response_type": "ListRocketMqMigrationTaskResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_topic_access_policy_async(self, request):
        r"""查询主题的授权用户列表

        查询主题的授权用户列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListTopicAccessPolicy
        :type request: :class:`huaweicloudsdkrocketmq.v2.ListTopicAccessPolicyRequest`
        :rtype: :class:`huaweicloudsdkrocketmq.v2.ListTopicAccessPolicyResponse`
        """
        http_info = self._list_topic_access_policy_http_info(request)
        return self._call_api(**http_info)

    def list_topic_access_policy_async_invoker(self, request):
        http_info = self._list_topic_access_policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_topic_access_policy_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/topics/{topic}/accesspolicy",
            "request_type": request.__class__.__name__,
            "response_type": "ListTopicAccessPolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'topic' in local_var_params:
            path_params['topic'] = local_var_params['topic']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_user_async(self, request):
        r"""查询用户列表

        查询用户列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListUser
        :type request: :class:`huaweicloudsdkrocketmq.v2.ListUserRequest`
        :rtype: :class:`huaweicloudsdkrocketmq.v2.ListUserResponse`
        """
        http_info = self._list_user_http_info(request)
        return self._call_api(**http_info)

    def list_user_async_invoker(self, request):
        http_info = self._list_user_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_user_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/users",
            "request_type": request.__class__.__name__,
            "response_type": "ListUserResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def modify_instance_ssl_config_async(self, request):
        r"""修改实例ssl相关配置

        修改实例ssl相关配置。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ModifyInstanceSslConfig
        :type request: :class:`huaweicloudsdkrocketmq.v2.ModifyInstanceSslConfigRequest`
        :rtype: :class:`huaweicloudsdkrocketmq.v2.ModifyInstanceSslConfigResponse`
        """
        http_info = self._modify_instance_ssl_config_http_info(request)
        return self._call_api(**http_info)

    def modify_instance_ssl_config_async_invoker(self, request):
        http_info = self._modify_instance_ssl_config_http_info(request)
        return AsyncInvoker(self, http_info)

    def _modify_instance_ssl_config_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/{engine}/instances/{instance_id}/plain-ssl-switch",
            "request_type": request.__class__.__name__,
            "response_type": "ModifyInstanceSslConfigResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'engine' in local_var_params:
            path_params['engine'] = local_var_params['engine']
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def reset_consume_offset_async(self, request):
        r"""重置消费进度

        重置消费进度。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ResetConsumeOffset
        :type request: :class:`huaweicloudsdkrocketmq.v2.ResetConsumeOffsetRequest`
        :rtype: :class:`huaweicloudsdkrocketmq.v2.ResetConsumeOffsetResponse`
        """
        http_info = self._reset_consume_offset_http_info(request)
        return self._call_api(**http_info)

    def reset_consume_offset_async_invoker(self, request):
        http_info = self._reset_consume_offset_http_info(request)
        return AsyncInvoker(self, http_info)

    def _reset_consume_offset_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{engine}/{project_id}/instances/{instance_id}/groups/{group_id}/reset-message-offset",
            "request_type": request.__class__.__name__,
            "response_type": "ResetConsumeOffsetResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'engine' in local_var_params:
            path_params['engine'] = local_var_params['engine']
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def resize_instance_async(self, request):
        r"""实例规格变更

        实例规格变更。
        
        [**当前通过调用API，只支持按需实例进行实例规格变更。**](tag:hws,hws_hk,ctc)
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ResizeInstance
        :type request: :class:`huaweicloudsdkrocketmq.v2.ResizeInstanceRequest`
        :rtype: :class:`huaweicloudsdkrocketmq.v2.ResizeInstanceResponse`
        """
        http_info = self._resize_instance_http_info(request)
        return self._call_api(**http_info)

    def resize_instance_async_invoker(self, request):
        http_info = self._resize_instance_http_info(request)
        return AsyncInvoker(self, http_info)

    def _resize_instance_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{engine}/{project_id}/instances/{instance_id}/extend",
            "request_type": request.__class__.__name__,
            "response_type": "ResizeInstanceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'engine' in local_var_params:
            path_params['engine'] = local_var_params['engine']
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def send_dlq_message_async(self, request):
        r"""重发死信消息

        重发死信消息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for SendDlqMessage
        :type request: :class:`huaweicloudsdkrocketmq.v2.SendDlqMessageRequest`
        :rtype: :class:`huaweicloudsdkrocketmq.v2.SendDlqMessageResponse`
        """
        http_info = self._send_dlq_message_http_info(request)
        return self._call_api(**http_info)

    def send_dlq_message_async_invoker(self, request):
        http_info = self._send_dlq_message_http_info(request)
        return AsyncInvoker(self, http_info)

    def _send_dlq_message_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{engine}/{project_id}/instances/{instance_id}/messages/deadletter-resend",
            "request_type": request.__class__.__name__,
            "response_type": "SendDlqMessageResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'engine' in local_var_params:
            path_params['engine'] = local_var_params['engine']
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def send_message_async(self, request):
        r"""发送消息

        发送消息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for SendMessage
        :type request: :class:`huaweicloudsdkrocketmq.v2.SendMessageRequest`
        :rtype: :class:`huaweicloudsdkrocketmq.v2.SendMessageResponse`
        """
        http_info = self._send_message_http_info(request)
        return self._call_api(**http_info)

    def send_message_async_invoker(self, request):
        http_info = self._send_message_http_info(request)
        return AsyncInvoker(self, http_info)

    def _send_message_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{engine}/{project_id}/instances/{instance_id}/messages",
            "request_type": request.__class__.__name__,
            "response_type": "SendMessageResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'engine' in local_var_params:
            path_params['engine'] = local_var_params['engine']
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_consumer_connections_async(self, request):
        r"""查询消费者列表

        查询消费组内消费者列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowConsumerConnections
        :type request: :class:`huaweicloudsdkrocketmq.v2.ShowConsumerConnectionsRequest`
        :rtype: :class:`huaweicloudsdkrocketmq.v2.ShowConsumerConnectionsResponse`
        """
        http_info = self._show_consumer_connections_http_info(request)
        return self._call_api(**http_info)

    def show_consumer_connections_async_invoker(self, request):
        http_info = self._show_consumer_connections_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_consumer_connections_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/rocketmq/{project_id}/instances/{instance_id}/groups/{group}/clients",
            "request_type": request.__class__.__name__,
            "response_type": "ShowConsumerConnectionsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'group' in local_var_params:
            path_params['group'] = local_var_params['group']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'is_detail' in local_var_params:
            query_params.append(('is_detail', local_var_params['is_detail']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_consumer_list_or_details_async(self, request):
        r"""查询消费列表或详情

        查询消费列表或详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowConsumerListOrDetails
        :type request: :class:`huaweicloudsdkrocketmq.v2.ShowConsumerListOrDetailsRequest`
        :rtype: :class:`huaweicloudsdkrocketmq.v2.ShowConsumerListOrDetailsResponse`
        """
        http_info = self._show_consumer_list_or_details_http_info(request)
        return self._call_api(**http_info)

    def show_consumer_list_or_details_async_invoker(self, request):
        http_info = self._show_consumer_list_or_details_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_consumer_list_or_details_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/groups/{group}/topics",
            "request_type": request.__class__.__name__,
            "response_type": "ShowConsumerListOrDetailsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'group' in local_var_params:
            path_params['group'] = local_var_params['group']

        query_params = []
        if 'topic' in local_var_params:
            query_params.append(('topic', local_var_params['topic']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_diagnosis_report_async(self, request):
        r"""查询实例诊断报告

        查询实例诊断报告。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowDiagnosisReport
        :type request: :class:`huaweicloudsdkrocketmq.v2.ShowDiagnosisReportRequest`
        :rtype: :class:`huaweicloudsdkrocketmq.v2.ShowDiagnosisReportResponse`
        """
        http_info = self._show_diagnosis_report_http_info(request)
        return self._call_api(**http_info)

    def show_diagnosis_report_async_invoker(self, request):
        http_info = self._show_diagnosis_report_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_diagnosis_report_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{engine}/{project_id}/diagnosis/{report_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDiagnosisReportResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'engine' in local_var_params:
            path_params['engine'] = local_var_params['engine']
        if 'report_id' in local_var_params:
            path_params['report_id'] = local_var_params['report_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_diagnosis_stack_async(self, request):
        r"""查询stack信息

        查询stack信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowDiagnosisStack
        :type request: :class:`huaweicloudsdkrocketmq.v2.ShowDiagnosisStackRequest`
        :rtype: :class:`huaweicloudsdkrocketmq.v2.ShowDiagnosisStackResponse`
        """
        http_info = self._show_diagnosis_stack_http_info(request)
        return self._call_api(**http_info)

    def show_diagnosis_stack_async_invoker(self, request):
        http_info = self._show_diagnosis_stack_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_diagnosis_stack_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{engine}/{project_id}/diagnosis/stack/{stack_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDiagnosisStackResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'engine' in local_var_params:
            path_params['engine'] = local_var_params['engine']
        if 'stack_id' in local_var_params:
            path_params['stack_id'] = local_var_params['stack_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_engine_instance_extend_product_info_async(self, request):
        r"""查询实例的扩容规格列表

        查询实例的扩容规格列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowEngineInstanceExtendProductInfo
        :type request: :class:`huaweicloudsdkrocketmq.v2.ShowEngineInstanceExtendProductInfoRequest`
        :rtype: :class:`huaweicloudsdkrocketmq.v2.ShowEngineInstanceExtendProductInfoResponse`
        """
        http_info = self._show_engine_instance_extend_product_info_http_info(request)
        return self._call_api(**http_info)

    def show_engine_instance_extend_product_info_async_invoker(self, request):
        http_info = self._show_engine_instance_extend_product_info_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_engine_instance_extend_product_info_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{engine}/{project_id}/instances/{instance_id}/extend",
            "request_type": request.__class__.__name__,
            "response_type": "ShowEngineInstanceExtendProductInfoResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'engine' in local_var_params:
            path_params['engine'] = local_var_params['engine']
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_group_async(self, request):
        r"""查询指定消费组

        查询指定消费组详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowGroup
        :type request: :class:`huaweicloudsdkrocketmq.v2.ShowGroupRequest`
        :rtype: :class:`huaweicloudsdkrocketmq.v2.ShowGroupResponse`
        """
        http_info = self._show_group_http_info(request)
        return self._call_api(**http_info)

    def show_group_async_invoker(self, request):
        http_info = self._show_group_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_group_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/groups/{group}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'group' in local_var_params:
            path_params['group'] = local_var_params['group']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_instance_async(self, request):
        r"""查询指定实例

        查询指定实例的详细信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowInstance
        :type request: :class:`huaweicloudsdkrocketmq.v2.ShowInstanceRequest`
        :rtype: :class:`huaweicloudsdkrocketmq.v2.ShowInstanceResponse`
        """
        http_info = self._show_instance_http_info(request)
        return self._call_api(**http_info)

    def show_instance_async_invoker(self, request):
        http_info = self._show_instance_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_instance_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/instances/{instance_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowInstanceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_instance_nodes_async(self, request):
        r"""查询实例节点

        查询实例节点信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowInstanceNodes
        :type request: :class:`huaweicloudsdkrocketmq.v2.ShowInstanceNodesRequest`
        :rtype: :class:`huaweicloudsdkrocketmq.v2.ShowInstanceNodesResponse`
        """
        http_info = self._show_instance_nodes_http_info(request)
        return self._call_api(**http_info)

    def show_instance_nodes_async_invoker(self, request):
        http_info = self._show_instance_nodes_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_instance_nodes_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/{engine}/instances/{instance_id}/nodes",
            "request_type": request.__class__.__name__,
            "response_type": "ShowInstanceNodesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'engine' in local_var_params:
            path_params['engine'] = local_var_params['engine']
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_quotas_async(self, request):
        r"""查看租户配额

        查询租户最大可以创建的实例个数和已创建的实例个数，以及每个实例最大可以创建标签的个数。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowQuotas
        :type request: :class:`huaweicloudsdkrocketmq.v2.ShowQuotasRequest`
        :rtype: :class:`huaweicloudsdkrocketmq.v2.ShowQuotasResponse`
        """
        http_info = self._show_quotas_http_info(request)
        return self._call_api(**http_info)

    def show_quotas_async_invoker(self, request):
        http_info = self._show_quotas_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_quotas_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/quotas",
            "request_type": request.__class__.__name__,
            "response_type": "ShowQuotasResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_rocket_mq_configs_async(self, request):
        r"""查询RocketMQ配置

        该接口用于查询RocketMQ配置，若成功则返回配置的相关信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowRocketMqConfigs
        :type request: :class:`huaweicloudsdkrocketmq.v2.ShowRocketMqConfigsRequest`
        :rtype: :class:`huaweicloudsdkrocketmq.v2.ShowRocketMqConfigsResponse`
        """
        http_info = self._show_rocket_mq_configs_http_info(request)
        return self._call_api(**http_info)

    def show_rocket_mq_configs_async_invoker(self, request):
        http_info = self._show_rocket_mq_configs_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_rocket_mq_configs_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/rocketmq/instances/{instance_id}/configs",
            "request_type": request.__class__.__name__,
            "response_type": "ShowRocketMqConfigsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_rocketmq_project_tags_async(self, request):
        r"""查询项目标签

        查询项目标签。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowRocketmqProjectTags
        :type request: :class:`huaweicloudsdkrocketmq.v2.ShowRocketmqProjectTagsRequest`
        :rtype: :class:`huaweicloudsdkrocketmq.v2.ShowRocketmqProjectTagsResponse`
        """
        http_info = self._show_rocketmq_project_tags_http_info(request)
        return self._call_api(**http_info)

    def show_rocketmq_project_tags_async_invoker(self, request):
        http_info = self._show_rocketmq_project_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_rocketmq_project_tags_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/rocketmq/tags",
            "request_type": request.__class__.__name__,
            "response_type": "ShowRocketmqProjectTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_rocketmq_tags_async(self, request):
        r"""查询实例标签

        查询实例标签。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowRocketmqTags
        :type request: :class:`huaweicloudsdkrocketmq.v2.ShowRocketmqTagsRequest`
        :rtype: :class:`huaweicloudsdkrocketmq.v2.ShowRocketmqTagsResponse`
        """
        http_info = self._show_rocketmq_tags_http_info(request)
        return self._call_api(**http_info)

    def show_rocketmq_tags_async_invoker(self, request):
        http_info = self._show_rocketmq_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_rocketmq_tags_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/rocketmq/{instance_id}/tags",
            "request_type": request.__class__.__name__,
            "response_type": "ShowRocketmqTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_user_async(self, request):
        r"""查询用户详情

        查询用户详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowUser
        :type request: :class:`huaweicloudsdkrocketmq.v2.ShowUserRequest`
        :rtype: :class:`huaweicloudsdkrocketmq.v2.ShowUserResponse`
        """
        http_info = self._show_user_http_info(request)
        return self._call_api(**http_info)

    def show_user_async_invoker(self, request):
        http_info = self._show_user_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_user_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/users/{user_name}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowUserResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'user_name' in local_var_params:
            path_params['user_name'] = local_var_params['user_name']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_consumer_group_async(self, request):
        r"""修改消费组

        修改指定消费组参数。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateConsumerGroup
        :type request: :class:`huaweicloudsdkrocketmq.v2.UpdateConsumerGroupRequest`
        :rtype: :class:`huaweicloudsdkrocketmq.v2.UpdateConsumerGroupResponse`
        """
        http_info = self._update_consumer_group_http_info(request)
        return self._call_api(**http_info)

    def update_consumer_group_async_invoker(self, request):
        http_info = self._update_consumer_group_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_consumer_group_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/groups/{group}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateConsumerGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'group' in local_var_params:
            path_params['group'] = local_var_params['group']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_instance_async(self, request):
        r"""修改实例信息

        修改实例的名称和描述信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateInstance
        :type request: :class:`huaweicloudsdkrocketmq.v2.UpdateInstanceRequest`
        :rtype: :class:`huaweicloudsdkrocketmq.v2.UpdateInstanceResponse`
        """
        http_info = self._update_instance_http_info(request)
        return self._call_api(**http_info)

    def update_instance_async_invoker(self, request):
        http_info = self._update_instance_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_instance_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/instances/{instance_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateInstanceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_rocket_mq_configs_async(self, request):
        r"""修改RocketMQ配置

        该接口用于修改RocketMQ配置。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateRocketMqConfigs
        :type request: :class:`huaweicloudsdkrocketmq.v2.UpdateRocketMqConfigsRequest`
        :rtype: :class:`huaweicloudsdkrocketmq.v2.UpdateRocketMqConfigsResponse`
        """
        http_info = self._update_rocket_mq_configs_http_info(request)
        return self._call_api(**http_info)

    def update_rocket_mq_configs_async_invoker(self, request):
        http_info = self._update_rocket_mq_configs_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_rocket_mq_configs_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/rocketmq/instances/{instance_id}/configs",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateRocketMqConfigsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_user_async(self, request):
        r"""修改用户参数

        修改用户参数。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateUser
        :type request: :class:`huaweicloudsdkrocketmq.v2.UpdateUserRequest`
        :rtype: :class:`huaweicloudsdkrocketmq.v2.UpdateUserResponse`
        """
        http_info = self._update_user_http_info(request)
        return self._call_api(**http_info)

    def update_user_async_invoker(self, request):
        http_info = self._update_user_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_user_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/users/{user_name}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateUserResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'user_name' in local_var_params:
            path_params['user_name'] = local_var_params['user_name']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def validate_consumed_message_async(self, request):
        r"""消费验证

        消费验证。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ValidateConsumedMessage
        :type request: :class:`huaweicloudsdkrocketmq.v2.ValidateConsumedMessageRequest`
        :rtype: :class:`huaweicloudsdkrocketmq.v2.ValidateConsumedMessageResponse`
        """
        http_info = self._validate_consumed_message_http_info(request)
        return self._call_api(**http_info)

    def validate_consumed_message_async_invoker(self, request):
        http_info = self._validate_consumed_message_http_info(request)
        return AsyncInvoker(self, http_info)

    def _validate_consumed_message_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{engine}/{project_id}/instances/{instance_id}/messages/resend",
            "request_type": request.__class__.__name__,
            "response_type": "ValidateConsumedMessageResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'engine' in local_var_params:
            path_params['engine'] = local_var_params['engine']
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_topic_or_batch_delete_topic_async(self, request):
        r"""创建主题或批量删除主题

        创建主题或批量删除主题。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateTopicOrBatchDeleteTopic
        :type request: :class:`huaweicloudsdkrocketmq.v2.CreateTopicOrBatchDeleteTopicRequest`
        :rtype: :class:`huaweicloudsdkrocketmq.v2.CreateTopicOrBatchDeleteTopicResponse`
        """
        http_info = self._create_topic_or_batch_delete_topic_http_info(request)
        return self._call_api(**http_info)

    def create_topic_or_batch_delete_topic_async_invoker(self, request):
        http_info = self._create_topic_or_batch_delete_topic_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_topic_or_batch_delete_topic_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/topics",
            "request_type": request.__class__.__name__,
            "response_type": "CreateTopicOrBatchDeleteTopicResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'action' in local_var_params:
            query_params.append(('action', local_var_params['action']))

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_topic_async(self, request):
        r"""删除指定主题

        删除指定主题。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteTopic
        :type request: :class:`huaweicloudsdkrocketmq.v2.DeleteTopicRequest`
        :rtype: :class:`huaweicloudsdkrocketmq.v2.DeleteTopicResponse`
        """
        http_info = self._delete_topic_http_info(request)
        return self._call_api(**http_info)

    def delete_topic_async_invoker(self, request):
        http_info = self._delete_topic_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_topic_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/topics/{topic}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteTopicResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'topic' in local_var_params:
            path_params['topic'] = local_var_params['topic']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_consumer_group_of_topic_async(self, request):
        r"""查询主题消费组列表

        查询主题消费组列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListConsumerGroupOfTopic
        :type request: :class:`huaweicloudsdkrocketmq.v2.ListConsumerGroupOfTopicRequest`
        :rtype: :class:`huaweicloudsdkrocketmq.v2.ListConsumerGroupOfTopicResponse`
        """
        http_info = self._list_consumer_group_of_topic_http_info(request)
        return self._call_api(**http_info)

    def list_consumer_group_of_topic_async_invoker(self, request):
        http_info = self._list_consumer_group_of_topic_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_consumer_group_of_topic_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/topics/{topic}/groups",
            "request_type": request.__class__.__name__,
            "response_type": "ListConsumerGroupOfTopicResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'topic' in local_var_params:
            path_params['topic'] = local_var_params['topic']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_rocket_instance_topics_async(self, request):
        r"""查询主题列表

        该接口用于查询指定RocketMQ实例的Topic列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListRocketInstanceTopics
        :type request: :class:`huaweicloudsdkrocketmq.v2.ListRocketInstanceTopicsRequest`
        :rtype: :class:`huaweicloudsdkrocketmq.v2.ListRocketInstanceTopicsResponse`
        """
        http_info = self._list_rocket_instance_topics_http_info(request)
        return self._call_api(**http_info)

    def list_rocket_instance_topics_async_invoker(self, request):
        http_info = self._list_rocket_instance_topics_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_rocket_instance_topics_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/topics",
            "request_type": request.__class__.__name__,
            "response_type": "ListRocketInstanceTopicsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_one_topic_async(self, request):
        r"""查询单个主题

        查询单个主题。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowOneTopic
        :type request: :class:`huaweicloudsdkrocketmq.v2.ShowOneTopicRequest`
        :rtype: :class:`huaweicloudsdkrocketmq.v2.ShowOneTopicResponse`
        """
        http_info = self._show_one_topic_http_info(request)
        return self._call_api(**http_info)

    def show_one_topic_async_invoker(self, request):
        http_info = self._show_one_topic_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_one_topic_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/topics/{topic}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowOneTopicResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'topic' in local_var_params:
            path_params['topic'] = local_var_params['topic']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_topic_status_async(self, request):
        r"""查询主题的消息数

        查询主题的消息数。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowTopicStatus
        :type request: :class:`huaweicloudsdkrocketmq.v2.ShowTopicStatusRequest`
        :rtype: :class:`huaweicloudsdkrocketmq.v2.ShowTopicStatusResponse`
        """
        http_info = self._show_topic_status_http_info(request)
        return self._call_api(**http_info)

    def show_topic_status_async_invoker(self, request):
        http_info = self._show_topic_status_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_topic_status_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/topics/{topic}/status",
            "request_type": request.__class__.__name__,
            "response_type": "ShowTopicStatusResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'topic' in local_var_params:
            path_params['topic'] = local_var_params['topic']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_topic_async(self, request):
        r"""修改主题

        修改主题。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateTopic
        :type request: :class:`huaweicloudsdkrocketmq.v2.UpdateTopicRequest`
        :rtype: :class:`huaweicloudsdkrocketmq.v2.UpdateTopicResponse`
        """
        http_info = self._update_topic_http_info(request)
        return self._call_api(**http_info)

    def update_topic_async_invoker(self, request):
        http_info = self._update_topic_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_topic_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/topics/{topic}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateTopicResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'topic' in local_var_params:
            path_params['topic'] = local_var_params['topic']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def _call_api(self, **kwargs):
        try:
            kwargs["async_request"] = True
            return self.do_http_request(**kwargs)
        except TypeError:
            import inspect
            params = inspect.signature(self.do_http_request).parameters
            http_info = {param_name: kwargs.get(param_name) for param_name in params if param_name in kwargs}
            return self.do_http_request(**http_info)

    def call_api(self, resource_path, method, path_params=None, query_params=None, header_params=None, body=None,
                 post_params=None, cname=None, response_type=None, response_headers=None, auth_settings=None,
                 collection_formats=None, request_type=None):
        """Makes the HTTP request and returns deserialized data.

        :param resource_path: Path to method endpoint.
        :param method: Method to call.
        :param path_params: Path parameters in the url.
        :param query_params: Query parameters in the url.
        :param header_params: Header parameters to be
            placed in the request header.
        :param body: Request body.
        :param post_params: Request post form parameters,
            for `application/x-www-form-urlencoded`, `multipart/form-data`.
        :param cname: Used for obs endpoint.
        :param auth_settings: Auth Settings names for the request.
        :param response_type: Response data type.
        :param response_headers: Header should be added to response data.
        :param collection_formats: dict of collection formats for path, query,
            header, and post parameters.
        :param request_type: Request data type.
        :return:
            Return the response directly.
        """
        return self.do_http_request(
            method=method,
            resource_path=resource_path,
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body,
            post_params=post_params,
            cname=cname,
            response_type=response_type,
            response_headers=response_headers,
            collection_formats=collection_formats,
            request_type=request_type,
	        async_request=True)

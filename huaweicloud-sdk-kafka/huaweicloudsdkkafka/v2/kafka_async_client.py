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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkkafka'")


class KafkaAsyncClient(Client):
    def __init__(self):
        super(KafkaAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkkafka.v2.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "KafkaAsyncClient":
                raise TypeError("client type error, support client type is KafkaAsyncClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def batch_create_or_delete_kafka_tag_async(self, request):
        r"""批量添加或删除实例标签

        批量添加或删除实例标签。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchCreateOrDeleteKafkaTag
        :type request: :class:`huaweicloudsdkkafka.v2.BatchCreateOrDeleteKafkaTagRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.BatchCreateOrDeleteKafkaTagResponse`
        """
        http_info = self._batch_create_or_delete_kafka_tag_http_info(request)
        return self._call_api(**http_info)

    def batch_create_or_delete_kafka_tag_async_invoker(self, request):
        http_info = self._batch_create_or_delete_kafka_tag_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_create_or_delete_kafka_tag_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/kafka/{instance_id}/tags/action",
            "request_type": request.__class__.__name__,
            "response_type": "BatchCreateOrDeleteKafkaTagResponse"
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

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def batch_delete_group_async(self, request):
        r"""Kafka实例批量删除消费组

        该接口用于向Kafka实例批量删除消费组。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchDeleteGroup
        :type request: :class:`huaweicloudsdkkafka.v2.BatchDeleteGroupRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.BatchDeleteGroupResponse`
        """
        http_info = self._batch_delete_group_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_group_async_invoker(self, request):
        http_info = self._batch_delete_group_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_delete_group_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/groups/batch-delete",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeleteGroupResponse"
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

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def batch_delete_instance_topic_async(self, request):
        r"""Kafka实例批量删除Topic

        该接口用于向Kafka实例批量删除Topic。批量删除多个Topic时，部分删除成功，部分失败，此时接口返回删除成功，并在返回中显示删除失败的Topic信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchDeleteInstanceTopic
        :type request: :class:`huaweicloudsdkkafka.v2.BatchDeleteInstanceTopicRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.BatchDeleteInstanceTopicResponse`
        """
        http_info = self._batch_delete_instance_topic_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_instance_topic_async_invoker(self, request):
        http_info = self._batch_delete_instance_topic_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_delete_instance_topic_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/topics/delete",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeleteInstanceTopicResponse"
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

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def batch_delete_instance_users_async(self, request):
        r"""批量删除用户

        批量删除Kafka实例的用户。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchDeleteInstanceUsers
        :type request: :class:`huaweicloudsdkkafka.v2.BatchDeleteInstanceUsersRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.BatchDeleteInstanceUsersResponse`
        """
        http_info = self._batch_delete_instance_users_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_instance_users_async_invoker(self, request):
        http_info = self._batch_delete_instance_users_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_delete_instance_users_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/users",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeleteInstanceUsersResponse"
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

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def batch_delete_message_diagnosis_reports_async(self, request):
        r"""批量删除消息积压诊断报告

        批量删除消息积压诊断报告
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchDeleteMessageDiagnosisReports
        :type request: :class:`huaweicloudsdkkafka.v2.BatchDeleteMessageDiagnosisReportsRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.BatchDeleteMessageDiagnosisReportsResponse`
        """
        http_info = self._batch_delete_message_diagnosis_reports_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_message_diagnosis_reports_async_invoker(self, request):
        http_info = self._batch_delete_message_diagnosis_reports_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_delete_message_diagnosis_reports_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/kafka/instances/{instance_id}/message-diagnosis-tasks",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeleteMessageDiagnosisReportsResponse"
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

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def batch_restart_or_delete_instances_async(self, request):
        r"""批量重启或删除实例

        批量重启或删除实例。
        
        在实例重启过程中，客户端的生产与消费消息等请求会被拒绝。
        
        实例删除后，实例中原有的数据将被删除，且没有备份，请谨慎操作。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchRestartOrDeleteInstances
        :type request: :class:`huaweicloudsdkkafka.v2.BatchRestartOrDeleteInstancesRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.BatchRestartOrDeleteInstancesResponse`
        """
        http_info = self._batch_restart_or_delete_instances_http_info(request)
        return self._call_api(**http_info)

    def batch_restart_or_delete_instances_async_invoker(self, request):
        http_info = self._batch_restart_or_delete_instances_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_restart_or_delete_instances_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/instances/action",
            "request_type": request.__class__.__name__,
            "response_type": "BatchRestartOrDeleteInstancesResponse"
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

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def close_kafka_manager_async(self, request):
        r"""关闭Kafka Manager

        关闭Kafka Manager，相应的原来开放出的management相关接口也将不可用。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CloseKafkaManager
        :type request: :class:`huaweicloudsdkkafka.v2.CloseKafkaManagerRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.CloseKafkaManagerResponse`
        """
        http_info = self._close_kafka_manager_http_info(request)
        return self._call_api(**http_info)

    def close_kafka_manager_async_invoker(self, request):
        http_info = self._close_kafka_manager_http_info(request)
        return AsyncInvoker(self, http_info)

    def _close_kafka_manager_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/kafka/instances/{instance_id}/management",
            "request_type": request.__class__.__name__,
            "response_type": "CloseKafkaManagerResponse"
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

    def create_instance_by_engine_async(self, request):
        r"""创建实例

        创建实例。
        
        [该接口支持创建按需和包周期两种计费方式的实例。](tag:hws,hws_eu,hws_hk,ctc)
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateInstanceByEngine
        :type request: :class:`huaweicloudsdkkafka.v2.CreateInstanceByEngineRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.CreateInstanceByEngineResponse`
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

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_instance_topic_async(self, request):
        r"""Kafka实例创建Topic

        该接口用于向Kafka实例创建Topic。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateInstanceTopic
        :type request: :class:`huaweicloudsdkkafka.v2.CreateInstanceTopicRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.CreateInstanceTopicResponse`
        """
        http_info = self._create_instance_topic_http_info(request)
        return self._call_api(**http_info)

    def create_instance_topic_async_invoker(self, request):
        http_info = self._create_instance_topic_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_instance_topic_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/topics",
            "request_type": request.__class__.__name__,
            "response_type": "CreateInstanceTopicResponse"
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

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_instance_user_async(self, request):
        r"""创建用户

        创建Kafka实例的用户，用户可连接开启SASL的Kafka实例。 [ 2023年7月15日前创建的Kafka实例，一个实例最多创建20个用户。2023年7月15日及以后创建的Kafka实例，一个实例最多创建500个用户。](tag:hws,hws_hk)
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateInstanceUser
        :type request: :class:`huaweicloudsdkkafka.v2.CreateInstanceUserRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.CreateInstanceUserResponse`
        """
        http_info = self._create_instance_user_http_info(request)
        return self._call_api(**http_info)

    def create_instance_user_async_invoker(self, request):
        http_info = self._create_instance_user_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_instance_user_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/users",
            "request_type": request.__class__.__name__,
            "response_type": "CreateInstanceUserResponse"
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

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_kafka_consumer_group_async(self, request):
        r"""创建消费组

        实例创建消费组
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateKafkaConsumerGroup
        :type request: :class:`huaweicloudsdkkafka.v2.CreateKafkaConsumerGroupRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.CreateKafkaConsumerGroupResponse`
        """
        http_info = self._create_kafka_consumer_group_http_info(request)
        return self._call_api(**http_info)

    def create_kafka_consumer_group_async_invoker(self, request):
        http_info = self._create_kafka_consumer_group_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_kafka_consumer_group_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/kafka/instances/{instance_id}/group",
            "request_type": request.__class__.__name__,
            "response_type": "CreateKafkaConsumerGroupResponse"
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

    def create_kafka_reassignment_task_async(self, request):
        r"""Kafka实例开始分区平衡任务

        该接口用于向Kafka实例提交分区平衡任务，若成功则返回分区平衡任务的job id。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateKafkaReassignmentTask
        :type request: :class:`huaweicloudsdkkafka.v2.CreateKafkaReassignmentTaskRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.CreateKafkaReassignmentTaskResponse`
        """
        http_info = self._create_kafka_reassignment_task_http_info(request)
        return self._call_api(**http_info)

    def create_kafka_reassignment_task_async_invoker(self, request):
        http_info = self._create_kafka_reassignment_task_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_kafka_reassignment_task_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/kafka/instances/{instance_id}/reassign",
            "request_type": request.__class__.__name__,
            "response_type": "CreateKafkaReassignmentTaskResponse"
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

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_kafka_rebalance_log_task_async(self, request):
        r"""开启Kafka实例重平衡日志功能

        开启Kafka实例重平衡日志功能。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateKafkaRebalanceLogTask
        :type request: :class:`huaweicloudsdkkafka.v2.CreateKafkaRebalanceLogTaskRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.CreateKafkaRebalanceLogTaskResponse`
        """
        http_info = self._create_kafka_rebalance_log_task_http_info(request)
        return self._call_api(**http_info)

    def create_kafka_rebalance_log_task_async_invoker(self, request):
        http_info = self._create_kafka_rebalance_log_task_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_kafka_rebalance_log_task_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/kafka/{project_id}/instances/{instance_id}/log/rebalance-log",
            "request_type": request.__class__.__name__,
            "response_type": "CreateKafkaRebalanceLogTaskResponse"
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

        auth_settings = ['IAM_AUTH_TYPE_NEW']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_kafka_topic_quota_async(self, request):
        r"""创建Topic流控配置

        该接口用于向Kafka实例提交创建Topic级别的流控任务，若成功则返回流控任务的job_id。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateKafkaTopicQuota
        :type request: :class:`huaweicloudsdkkafka.v2.CreateKafkaTopicQuotaRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.CreateKafkaTopicQuotaResponse`
        """
        http_info = self._create_kafka_topic_quota_http_info(request)
        return self._call_api(**http_info)

    def create_kafka_topic_quota_async_invoker(self, request):
        http_info = self._create_kafka_topic_quota_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_kafka_topic_quota_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/kafka/{project_id}/instances/{instance_id}/kafka-topic-quota",
            "request_type": request.__class__.__name__,
            "response_type": "CreateKafkaTopicQuotaResponse"
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

        auth_settings = ['IAM_AUTH_TYPE_NEW']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_kafka_user_client_quota_task_async(self, request):
        r"""创建用户/客户端流控配置

        该接口用于向Kafka实例提交创建用户、客户端级别的流控任务，若成功则返回流控任务的job_id。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateKafkaUserClientQuotaTask
        :type request: :class:`huaweicloudsdkkafka.v2.CreateKafkaUserClientQuotaTaskRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.CreateKafkaUserClientQuotaTaskResponse`
        """
        http_info = self._create_kafka_user_client_quota_task_http_info(request)
        return self._call_api(**http_info)

    def create_kafka_user_client_quota_task_async_invoker(self, request):
        http_info = self._create_kafka_user_client_quota_task_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_kafka_user_client_quota_task_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/kafka/{project_id}/instances/{instance_id}/kafka-user-client-quota",
            "request_type": request.__class__.__name__,
            "response_type": "CreateKafkaUserClientQuotaTaskResponse"
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

        auth_settings = ['IAM_AUTH_TYPE_NEW']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_message_diagnosis_task_async(self, request):
        r"""创建消息积压诊断任务

        创建消息积压诊断任务
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateMessageDiagnosisTask
        :type request: :class:`huaweicloudsdkkafka.v2.CreateMessageDiagnosisTaskRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.CreateMessageDiagnosisTaskResponse`
        """
        http_info = self._create_message_diagnosis_task_http_info(request)
        return self._call_api(**http_info)

    def create_message_diagnosis_task_async_invoker(self, request):
        http_info = self._create_message_diagnosis_task_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_message_diagnosis_task_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/kafka/instances/{instance_id}/message-diagnosis-tasks",
            "request_type": request.__class__.__name__,
            "response_type": "CreateMessageDiagnosisTaskResponse"
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

        auth_settings = ['apig-auth-iam']

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
        r"""创建实例

        创建按需计费类型的Kafka实例。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreatePostPaidInstance
        :type request: :class:`huaweicloudsdkkafka.v2.CreatePostPaidInstanceRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.CreatePostPaidInstanceResponse`
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

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_post_paid_kafka_instance_async(self, request):
        r"""创建Kafka实例

        创建实例。
        
        [该接口支持创建按需和包周期两种计费方式的实例。](tag:hws,hws_eu,hws_hk,ctc,cmcc)
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreatePostPaidKafkaInstance
        :type request: :class:`huaweicloudsdkkafka.v2.CreatePostPaidKafkaInstanceRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.CreatePostPaidKafkaInstanceResponse`
        """
        http_info = self._create_post_paid_kafka_instance_http_info(request)
        return self._call_api(**http_info)

    def create_post_paid_kafka_instance_async_invoker(self, request):
        http_info = self._create_post_paid_kafka_instance_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_post_paid_kafka_instance_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/kafka/instances",
            "request_type": request.__class__.__name__,
            "response_type": "CreatePostPaidKafkaInstanceResponse"
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

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_reassignment_task_async(self, request):
        r"""Kafka实例开始分区平衡任务

        该接口用于向Kafka实例提交分区平衡任务或计算分区平衡预估时间。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateReassignmentTask
        :type request: :class:`huaweicloudsdkkafka.v2.CreateReassignmentTaskRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.CreateReassignmentTaskResponse`
        """
        http_info = self._create_reassignment_task_http_info(request)
        return self._call_api(**http_info)

    def create_reassignment_task_async_invoker(self, request):
        http_info = self._create_reassignment_task_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_reassignment_task_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/kafka/{project_id}/instances/{instance_id}/reassign",
            "request_type": request.__class__.__name__,
            "response_type": "CreateReassignmentTaskResponse"
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

        auth_settings = ['apig-auth-iam']

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
        :type request: :class:`huaweicloudsdkkafka.v2.DeleteBackgroundTaskRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.DeleteBackgroundTaskResponse`
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

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_consumer_group_offsets_async(self, request):
        r"""删除消费组在指定Topic的消费位点

        删除消费组在指定Topic的消费位点。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteConsumerGroupOffsets
        :type request: :class:`huaweicloudsdkkafka.v2.DeleteConsumerGroupOffsetsRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.DeleteConsumerGroupOffsetsResponse`
        """
        http_info = self._delete_consumer_group_offsets_http_info(request)
        return self._call_api(**http_info)

    def delete_consumer_group_offsets_async_invoker(self, request):
        http_info = self._delete_consumer_group_offsets_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_consumer_group_offsets_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/kafka/{project_id}/instances/{instance_id}/groups/{group}/delete-offset",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteConsumerGroupOffsetsResponse"
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

        auth_settings = ['IAM_AUTH_TYPE_NEW']

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
        :type request: :class:`huaweicloudsdkkafka.v2.DeleteInstanceRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.DeleteInstanceResponse`
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

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_kafka_message_async(self, request):
        r"""Kafka删除消息

        Kafka删除消息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteKafkaMessage
        :type request: :class:`huaweicloudsdkkafka.v2.DeleteKafkaMessageRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.DeleteKafkaMessageResponse`
        """
        http_info = self._delete_kafka_message_http_info(request)
        return self._call_api(**http_info)

    def delete_kafka_message_async_invoker(self, request):
        http_info = self._delete_kafka_message_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_kafka_message_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/kafka/instances/{instance_id}/topics/{topic}/messages",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteKafkaMessageResponse"
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

        auth_settings = ['IAM_AUTH_TYPE_NEW']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_kafka_topic_quota_async(self, request):
        r"""删除Topic流控配置

        该接口用于向Kafka实例提交删除Topic级别的流控任务，若成功则返回流控任务的job_id。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteKafkaTopicQuota
        :type request: :class:`huaweicloudsdkkafka.v2.DeleteKafkaTopicQuotaRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.DeleteKafkaTopicQuotaResponse`
        """
        http_info = self._delete_kafka_topic_quota_http_info(request)
        return self._call_api(**http_info)

    def delete_kafka_topic_quota_async_invoker(self, request):
        http_info = self._delete_kafka_topic_quota_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_kafka_topic_quota_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/kafka/{project_id}/instances/{instance_id}/kafka-topic-quota",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteKafkaTopicQuotaResponse"
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

        auth_settings = ['IAM_AUTH_TYPE_NEW']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_kafka_user_client_quota_task_async(self, request):
        r"""删除用户/客户端流控配置

        该接口用于向Kafka实例提交删除用户、客户端级别的流控任务，若成功则返回流控任务的job_id。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteKafkaUserClientQuotaTask
        :type request: :class:`huaweicloudsdkkafka.v2.DeleteKafkaUserClientQuotaTaskRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.DeleteKafkaUserClientQuotaTaskResponse`
        """
        http_info = self._delete_kafka_user_client_quota_task_http_info(request)
        return self._call_api(**http_info)

    def delete_kafka_user_client_quota_task_async_invoker(self, request):
        http_info = self._delete_kafka_user_client_quota_task_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_kafka_user_client_quota_task_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/kafka/{project_id}/instances/{instance_id}/kafka-user-client-quota",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteKafkaUserClientQuotaTaskResponse"
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

        auth_settings = ['IAM_AUTH_TYPE_NEW']

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
        r"""开启Kafka实例域名访问能力

        开启Kafka实例域名访问后，客户端可以通过域名连接Kafka实例。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for EnableDns
        :type request: :class:`huaweicloudsdkkafka.v2.EnableDnsRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.EnableDnsResponse`
        """
        http_info = self._enable_dns_http_info(request)
        return self._call_api(**http_info)

    def enable_dns_async_invoker(self, request):
        http_info = self._enable_dns_http_info(request)
        return AsyncInvoker(self, http_info)

    def _enable_dns_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/kafka/instances/{instance_id}/dns",
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

    def list_available_zones_async(self, request):
        r"""查询可用区信息

        在创建实例时，需要配置实例所在的可用区ID，可通过该接口查询可用区的ID。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAvailableZones
        :type request: :class:`huaweicloudsdkkafka.v2.ListAvailableZonesRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.ListAvailableZonesResponse`
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

        auth_settings = ['apig-auth-iam']

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
        :type request: :class:`huaweicloudsdkkafka.v2.ListBackgroundTasksRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.ListBackgroundTasksResponse`
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

        auth_settings = ['apig-auth-iam']

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

        查询产品规格列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListEngineProducts
        :type request: :class:`huaweicloudsdkkafka.v2.ListEngineProductsRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.ListEngineProductsResponse`
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
        if 'product_id' in local_var_params:
            query_params.append(('product_id', local_var_params['product_id']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_instance_consumer_group_async(self, request):
        r"""查询指定消费组

        查询指定消费组。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListInstanceConsumerGroup
        :type request: :class:`huaweicloudsdkkafka.v2.ListInstanceConsumerGroupRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.ListInstanceConsumerGroupResponse`
        """
        http_info = self._list_instance_consumer_group_http_info(request)
        return self._call_api(**http_info)

    def list_instance_consumer_group_async_invoker(self, request):
        http_info = self._list_instance_consumer_group_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_instance_consumer_group_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{engine}/{project_id}/instances/{instance_id}/groups/{group}",
            "request_type": request.__class__.__name__,
            "response_type": "ListInstanceConsumerGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'engine' in local_var_params:
            path_params['engine'] = local_var_params['engine']
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

        auth_settings = ['IAM_AUTH_TYPE_NEW']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_instance_consumer_group_members_async(self, request):
        r"""查询指定消费组的消费成员

        查询指定消费组的消费成员。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListInstanceConsumerGroupMembers
        :type request: :class:`huaweicloudsdkkafka.v2.ListInstanceConsumerGroupMembersRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.ListInstanceConsumerGroupMembersResponse`
        """
        http_info = self._list_instance_consumer_group_members_http_info(request)
        return self._call_api(**http_info)

    def list_instance_consumer_group_members_async_invoker(self, request):
        http_info = self._list_instance_consumer_group_members_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_instance_consumer_group_members_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{engine}/{project_id}/instances/{instance_id}/groups/{group}/members",
            "request_type": request.__class__.__name__,
            "response_type": "ListInstanceConsumerGroupMembersResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'engine' in local_var_params:
            path_params['engine'] = local_var_params['engine']
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'group' in local_var_params:
            path_params['group'] = local_var_params['group']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'host' in local_var_params:
            query_params.append(('host', local_var_params['host']))
        if 'member_id' in local_var_params:
            query_params.append(('member_id', local_var_params['member_id']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['IAM_AUTH_TYPE_NEW']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_instance_consumer_group_message_offset_async(self, request):
        r"""查询消费组消息位点

        查询消费组消息位点。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListInstanceConsumerGroupMessageOffset
        :type request: :class:`huaweicloudsdkkafka.v2.ListInstanceConsumerGroupMessageOffsetRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.ListInstanceConsumerGroupMessageOffsetResponse`
        """
        http_info = self._list_instance_consumer_group_message_offset_http_info(request)
        return self._call_api(**http_info)

    def list_instance_consumer_group_message_offset_async_invoker(self, request):
        http_info = self._list_instance_consumer_group_message_offset_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_instance_consumer_group_message_offset_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{engine}/{project_id}/instances/{instance_id}/groups/{group}/message-offset",
            "request_type": request.__class__.__name__,
            "response_type": "ListInstanceConsumerGroupMessageOffsetResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'engine' in local_var_params:
            path_params['engine'] = local_var_params['engine']
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'group' in local_var_params:
            path_params['group'] = local_var_params['group']

        query_params = []
        if 'topic' in local_var_params:
            query_params.append(('topic', local_var_params['topic']))
        if 'partition' in local_var_params:
            query_params.append(('partition', local_var_params['partition']))
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

        auth_settings = ['IAM_AUTH_TYPE_NEW']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_instance_consumer_group_topics_async(self, request):
        r"""查询指定消费组的Topic

        查询指定消费组的Topic。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListInstanceConsumerGroupTopics
        :type request: :class:`huaweicloudsdkkafka.v2.ListInstanceConsumerGroupTopicsRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.ListInstanceConsumerGroupTopicsResponse`
        """
        http_info = self._list_instance_consumer_group_topics_http_info(request)
        return self._call_api(**http_info)

    def list_instance_consumer_group_topics_async_invoker(self, request):
        http_info = self._list_instance_consumer_group_topics_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_instance_consumer_group_topics_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{engine}/{project_id}/instances/{instance_id}/groups/{group}/topics",
            "request_type": request.__class__.__name__,
            "response_type": "ListInstanceConsumerGroupTopicsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'engine' in local_var_params:
            path_params['engine'] = local_var_params['engine']
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'group' in local_var_params:
            path_params['group'] = local_var_params['group']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
        if 'topic' in local_var_params:
            query_params.append(('topic', local_var_params['topic']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['IAM_AUTH_TYPE_NEW']

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
        r"""查询所有消费组

        查询所有消费组。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListInstanceConsumerGroups
        :type request: :class:`huaweicloudsdkkafka.v2.ListInstanceConsumerGroupsRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.ListInstanceConsumerGroupsResponse`
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
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'group' in local_var_params:
            query_params.append(('group', local_var_params['group']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_instance_topics_async(self, request):
        r"""Kafka实例查询Topic

        该接口用于查询指定Kafka实例的Topic详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListInstanceTopics
        :type request: :class:`huaweicloudsdkkafka.v2.ListInstanceTopicsRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.ListInstanceTopicsResponse`
        """
        http_info = self._list_instance_topics_http_info(request)
        return self._call_api(**http_info)

    def list_instance_topics_async_invoker(self, request):
        http_info = self._list_instance_topics_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_instance_topics_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/topics",
            "request_type": request.__class__.__name__,
            "response_type": "ListInstanceTopicsResponse"
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

        auth_settings = ['apig-auth-iam']

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
        :type request: :class:`huaweicloudsdkkafka.v2.ListInstancesRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.ListInstancesResponse`
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

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_message_diagnosis_reports_async(self, request):
        r"""查询消息积压诊断报告列表

        查询消息积压诊断报告列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListMessageDiagnosisReports
        :type request: :class:`huaweicloudsdkkafka.v2.ListMessageDiagnosisReportsRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.ListMessageDiagnosisReportsResponse`
        """
        http_info = self._list_message_diagnosis_reports_http_info(request)
        return self._call_api(**http_info)

    def list_message_diagnosis_reports_async_invoker(self, request):
        http_info = self._list_message_diagnosis_reports_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_message_diagnosis_reports_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/kafka/instances/{instance_id}/message-diagnosis-tasks",
            "request_type": request.__class__.__name__,
            "response_type": "ListMessageDiagnosisReportsResponse"
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

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_products_async(self, request):
        r"""查询产品规格列表

        在创建kafka实例时，需要配置订购的产品ID（即product_id），可通过该接口查询产品规格。
        
        例如，要订购按需计费、基准带宽为100MB的kafka实例，可从接口响应消息中，查找Hourly的消息体，然后找到bandwidth为100MB的记录对应的product_id，该product_id的值即是创建上述kafka实例时需要配置的产品ID。
        
        同时，unavailable_zones字段表示资源不足的可用区列表，如果为空，则表示所有可用区都有资源，如果不为空，则表示字段值的可用区没有资源。所以必须确保您购买的资源所在的可用区有资源，不在该字段列表内。
        
        [例如，响应消息中bandwidth字段为1200MB的记录，unavailable_zones字段包含cn-east-2b、cn-east-2a和cn-east-2d，表示在华东-上海2的可用区1、可用区2、可用区3都没有该资源。](tag:hws)
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListProducts
        :type request: :class:`huaweicloudsdkkafka.v2.ListProductsRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.ListProductsResponse`
        """
        http_info = self._list_products_http_info(request)
        return self._call_api(**http_info)

    def list_products_async_invoker(self, request):
        http_info = self._list_products_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_products_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/products",
            "request_type": request.__class__.__name__,
            "response_type": "ListProductsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'engine' in local_var_params:
            query_params.append(('engine', local_var_params['engine']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_topic_partitions_async(self, request):
        r"""查询Topic的分区列表

        查询Topic的分区列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListTopicPartitions
        :type request: :class:`huaweicloudsdkkafka.v2.ListTopicPartitionsRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.ListTopicPartitionsResponse`
        """
        http_info = self._list_topic_partitions_http_info(request)
        return self._call_api(**http_info)

    def list_topic_partitions_async_invoker(self, request):
        http_info = self._list_topic_partitions_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_topic_partitions_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/kafka/instances/{instance_id}/topics/{topic}/partitions",
            "request_type": request.__class__.__name__,
            "response_type": "ListTopicPartitionsResponse"
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

        auth_settings = ['IAM_AUTH_TYPE_NEW']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_topic_producers_async(self, request):
        r"""查询Topic的当前生产者列表

        查询Topic的当前生产者列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListTopicProducers
        :type request: :class:`huaweicloudsdkkafka.v2.ListTopicProducersRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.ListTopicProducersResponse`
        """
        http_info = self._list_topic_producers_http_info(request)
        return self._call_api(**http_info)

    def list_topic_producers_async_invoker(self, request):
        http_info = self._list_topic_producers_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_topic_producers_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/kafka/instances/{instance_id}/topics/{topic}/producers",
            "request_type": request.__class__.__name__,
            "response_type": "ListTopicProducersResponse"
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

        auth_settings = ['IAM_AUTH_TYPE_NEW']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def modify_instance_configs_async(self, request):
        r"""修改实例配置

        修改实例配置。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ModifyInstanceConfigs
        :type request: :class:`huaweicloudsdkkafka.v2.ModifyInstanceConfigsRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.ModifyInstanceConfigsResponse`
        """
        http_info = self._modify_instance_configs_http_info(request)
        return self._call_api(**http_info)

    def modify_instance_configs_async_invoker(self, request):
        http_info = self._modify_instance_configs_http_info(request)
        return AsyncInvoker(self, http_info)

    def _modify_instance_configs_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/configs",
            "request_type": request.__class__.__name__,
            "response_type": "ModifyInstanceConfigsResponse"
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

        auth_settings = ['IAM_AUTH_TYPE_NEW']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def modify_kafka_topic_quota_async(self, request):
        r"""修改Topic流控配置

        该接口用于向Kafka实例提交修改Topic级别的流控任务，若成功则返回流控任务的job_id。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ModifyKafkaTopicQuota
        :type request: :class:`huaweicloudsdkkafka.v2.ModifyKafkaTopicQuotaRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.ModifyKafkaTopicQuotaResponse`
        """
        http_info = self._modify_kafka_topic_quota_http_info(request)
        return self._call_api(**http_info)

    def modify_kafka_topic_quota_async_invoker(self, request):
        http_info = self._modify_kafka_topic_quota_http_info(request)
        return AsyncInvoker(self, http_info)

    def _modify_kafka_topic_quota_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/kafka/{project_id}/instances/{instance_id}/kafka-topic-quota",
            "request_type": request.__class__.__name__,
            "response_type": "ModifyKafkaTopicQuotaResponse"
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

        auth_settings = ['IAM_AUTH_TYPE_NEW']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def reset_manager_password_async(self, request):
        r"""重置Manager密码

        重置Manager密码。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ResetManagerPassword
        :type request: :class:`huaweicloudsdkkafka.v2.ResetManagerPasswordRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.ResetManagerPasswordResponse`
        """
        http_info = self._reset_manager_password_http_info(request)
        return self._call_api(**http_info)

    def reset_manager_password_async_invoker(self, request):
        http_info = self._reset_manager_password_http_info(request)
        return AsyncInvoker(self, http_info)

    def _reset_manager_password_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/kafka-manager-password",
            "request_type": request.__class__.__name__,
            "response_type": "ResetManagerPasswordResponse"
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

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def reset_message_offset_async(self, request):
        r"""重置消费组消费进度到指定位置

        Kafka实例不支持在线重置消费进度。在执行重置消费进度之前，必须停止被重置消费组客户端。
        
        停止待重置消费组客户端，然后等待一段时间（即ConsumerConfig.SESSION_TIMEOUT_MS_CONFIG配置的时间，默认为1000毫秒）后，服务端才认为此消费组客户端已下线。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ResetMessageOffset
        :type request: :class:`huaweicloudsdkkafka.v2.ResetMessageOffsetRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.ResetMessageOffsetResponse`
        """
        http_info = self._reset_message_offset_http_info(request)
        return self._call_api(**http_info)

    def reset_message_offset_async_invoker(self, request):
        http_info = self._reset_message_offset_http_info(request)
        return AsyncInvoker(self, http_info)

    def _reset_message_offset_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/management/groups/{group}/reset-message-offset",
            "request_type": request.__class__.__name__,
            "response_type": "ResetMessageOffsetResponse"
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

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def reset_message_offset_with_engine_async(self, request):
        r"""重置消费组消费进度到指定位置

        Kafka实例不支持在线重置消费进度。在执行重置消费进度之前，必须停止被重置消费组客户端。
        
        停止待重置消费组客户端，然后等待一段时间（即ConsumerConfig.SESSION_TIMEOUT_MS_CONFIG配置的时间，默认为1000毫秒）后，服务端才认为此消费组客户端已下线。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ResetMessageOffsetWithEngine
        :type request: :class:`huaweicloudsdkkafka.v2.ResetMessageOffsetWithEngineRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.ResetMessageOffsetWithEngineResponse`
        """
        http_info = self._reset_message_offset_with_engine_http_info(request)
        return self._call_api(**http_info)

    def reset_message_offset_with_engine_async_invoker(self, request):
        http_info = self._reset_message_offset_with_engine_http_info(request)
        return AsyncInvoker(self, http_info)

    def _reset_message_offset_with_engine_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/kafka/{project_id}/instances/{instance_id}/groups/{group}/reset-message-offset",
            "request_type": request.__class__.__name__,
            "response_type": "ResetMessageOffsetWithEngineResponse"
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

        auth_settings = ['IAM_AUTH_TYPE_NEW']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def reset_password_async(self, request):
        r"""重置密码

        重置密码（只针对开通SSL的实例）。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ResetPassword
        :type request: :class:`huaweicloudsdkkafka.v2.ResetPasswordRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.ResetPasswordResponse`
        """
        http_info = self._reset_password_http_info(request)
        return self._call_api(**http_info)

    def reset_password_async_invoker(self, request):
        http_info = self._reset_password_http_info(request)
        return AsyncInvoker(self, http_info)

    def _reset_password_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/password",
            "request_type": request.__class__.__name__,
            "response_type": "ResetPasswordResponse"
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

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def reset_user_passwrod_async(self, request):
        r"""重置用户密码

        重置用户密码
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ResetUserPasswrod
        :type request: :class:`huaweicloudsdkkafka.v2.ResetUserPasswrodRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.ResetUserPasswrodResponse`
        """
        http_info = self._reset_user_passwrod_http_info(request)
        return self._call_api(**http_info)

    def reset_user_passwrod_async_invoker(self, request):
        http_info = self._reset_user_passwrod_http_info(request)
        return AsyncInvoker(self, http_info)

    def _reset_user_passwrod_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/users/{user_name}",
            "request_type": request.__class__.__name__,
            "response_type": "ResetUserPasswrodResponse"
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

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def resize_engine_instance_async(self, request):
        r"""实例扩容

        实例规格变更。[当前通过调用API，只支持按需实例进行实例扩容。](tag:hws,hws_hk,ctc,cmcc,hws_eu)
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ResizeEngineInstance
        :type request: :class:`huaweicloudsdkkafka.v2.ResizeEngineInstanceRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.ResizeEngineInstanceResponse`
        """
        http_info = self._resize_engine_instance_http_info(request)
        return self._call_api(**http_info)

    def resize_engine_instance_async_invoker(self, request):
        http_info = self._resize_engine_instance_http_info(request)
        return AsyncInvoker(self, http_info)

    def _resize_engine_instance_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{engine}/{project_id}/instances/{instance_id}/extend",
            "request_type": request.__class__.__name__,
            "response_type": "ResizeEngineInstanceResponse"
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

        auth_settings = ['apig-auth-iam']

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
        r"""实例扩容

        实例扩容。[当前通过调用API，只支持按需实例进行实例扩容。](tag:hws,hws_hk,ctc,cmcc,hws_eu)
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ResizeInstance
        :type request: :class:`huaweicloudsdkkafka.v2.ResizeInstanceRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.ResizeInstanceResponse`
        """
        http_info = self._resize_instance_http_info(request)
        return self._call_api(**http_info)

    def resize_instance_async_invoker(self, request):
        http_info = self._resize_instance_http_info(request)
        return AsyncInvoker(self, http_info)

    def _resize_instance_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/extend",
            "request_type": request.__class__.__name__,
            "response_type": "ResizeInstanceResponse"
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

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def resize_kafka_instance_async(self, request):
        r"""实例扩容

        实例规格变更。[当前通过调用API，只支持按需实例进行实例扩容。](tag:hws,hws_hk,ctc,cmcc,hws_eu)
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ResizeKafkaInstance
        :type request: :class:`huaweicloudsdkkafka.v2.ResizeKafkaInstanceRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.ResizeKafkaInstanceResponse`
        """
        http_info = self._resize_kafka_instance_http_info(request)
        return self._call_api(**http_info)

    def resize_kafka_instance_async_invoker(self, request):
        http_info = self._resize_kafka_instance_http_info(request)
        return AsyncInvoker(self, http_info)

    def _resize_kafka_instance_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/kafka/instances/{instance_id}/extend",
            "request_type": request.__class__.__name__,
            "response_type": "ResizeKafkaInstanceResponse"
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

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def restart_manager_async(self, request):
        r"""重启Manager

        重启Manager。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RestartManager
        :type request: :class:`huaweicloudsdkkafka.v2.RestartManagerRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.RestartManagerResponse`
        """
        http_info = self._restart_manager_http_info(request)
        return self._call_api(**http_info)

    def restart_manager_async_invoker(self, request):
        http_info = self._restart_manager_http_info(request)
        return AsyncInvoker(self, http_info)

    def _restart_manager_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/restart-kafka-manager",
            "request_type": request.__class__.__name__,
            "response_type": "RestartManagerResponse"
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

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def send_kafka_message_async(self, request):
        r"""Kafka生产消息

        在控制台发送指定消息到Kafka实例
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for SendKafkaMessage
        :type request: :class:`huaweicloudsdkkafka.v2.SendKafkaMessageRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.SendKafkaMessageResponse`
        """
        http_info = self._send_kafka_message_http_info(request)
        return self._call_api(**http_info)

    def send_kafka_message_async_invoker(self, request):
        http_info = self._send_kafka_message_http_info(request)
        return AsyncInvoker(self, http_info)

    def _send_kafka_message_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/messages/action",
            "request_type": request.__class__.__name__,
            "response_type": "SendKafkaMessageResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'action_id' in local_var_params:
            query_params.append(('action_id', local_var_params['action_id']))

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

        auth_settings = ['IAM_AUTH_TYPE_NEW']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_background_task_async(self, request):
        r"""查询后台任务管理中的指定记录

        查询后台任务管理中的指定记录。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowBackgroundTask
        :type request: :class:`huaweicloudsdkkafka.v2.ShowBackgroundTaskRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.ShowBackgroundTaskResponse`
        """
        http_info = self._show_background_task_http_info(request)
        return self._call_api(**http_info)

    def show_background_task_async_invoker(self, request):
        http_info = self._show_background_task_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_background_task_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/tasks/{task_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowBackgroundTaskResponse"
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

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_ces_hierarchy_async(self, request):
        r"""查询实例在CES的监控层级关系

        查询实例在CES的监控层级关系。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowCesHierarchy
        :type request: :class:`huaweicloudsdkkafka.v2.ShowCesHierarchyRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.ShowCesHierarchyResponse`
        """
        http_info = self._show_ces_hierarchy_http_info(request)
        return self._call_api(**http_info)

    def show_ces_hierarchy_async_invoker(self, request):
        http_info = self._show_ces_hierarchy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_ces_hierarchy_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/ces-hierarchy",
            "request_type": request.__class__.__name__,
            "response_type": "ShowCesHierarchyResponse"
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

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_cluster_async(self, request):
        r"""查询Kafka集群元数据信息

        查询Kafka集群元数据信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowCluster
        :type request: :class:`huaweicloudsdkkafka.v2.ShowClusterRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.ShowClusterResponse`
        """
        http_info = self._show_cluster_http_info(request)
        return self._call_api(**http_info)

    def show_cluster_async_invoker(self, request):
        http_info = self._show_cluster_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_cluster_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/management/cluster",
            "request_type": request.__class__.__name__,
            "response_type": "ShowClusterResponse"
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

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_coordinators_async(self, request):
        r"""查询Kafka实例的协调器信息

        查询Kafka实例的协调器信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowCoordinators
        :type request: :class:`huaweicloudsdkkafka.v2.ShowCoordinatorsRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.ShowCoordinatorsResponse`
        """
        http_info = self._show_coordinators_http_info(request)
        return self._call_api(**http_info)

    def show_coordinators_async_invoker(self, request):
        http_info = self._show_coordinators_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_coordinators_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/management/coordinators",
            "request_type": request.__class__.__name__,
            "response_type": "ShowCoordinatorsResponse"
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

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_diagnosis_pre_check_async(self, request):
        r"""消息积压诊断预检查

        消息积压诊断预检查
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowDiagnosisPreCheck
        :type request: :class:`huaweicloudsdkkafka.v2.ShowDiagnosisPreCheckRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.ShowDiagnosisPreCheckResponse`
        """
        http_info = self._show_diagnosis_pre_check_http_info(request)
        return self._call_api(**http_info)

    def show_diagnosis_pre_check_async_invoker(self, request):
        http_info = self._show_diagnosis_pre_check_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_diagnosis_pre_check_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/kafka/instances/{instance_id}/diagnosis-check",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDiagnosisPreCheckResponse"
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
        if 'topic' in local_var_params:
            query_params.append(('topic', local_var_params['topic']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

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
        :type request: :class:`huaweicloudsdkkafka.v2.ShowEngineInstanceExtendProductInfoRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.ShowEngineInstanceExtendProductInfoResponse`
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

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_groups_async(self, request):
        r"""查询消费组信息

        查询消费组信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowGroups
        :type request: :class:`huaweicloudsdkkafka.v2.ShowGroupsRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.ShowGroupsResponse`
        """
        http_info = self._show_groups_http_info(request)
        return self._call_api(**http_info)

    def show_groups_async_invoker(self, request):
        http_info = self._show_groups_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_groups_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/management/groups/{group}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowGroupsResponse"
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

        auth_settings = ['apig-auth-iam']

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
        :type request: :class:`huaweicloudsdkkafka.v2.ShowInstanceRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.ShowInstanceResponse`
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

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_instance_configs_async(self, request):
        r"""获取实例配置

        获取实例配置。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowInstanceConfigs
        :type request: :class:`huaweicloudsdkkafka.v2.ShowInstanceConfigsRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.ShowInstanceConfigsResponse`
        """
        http_info = self._show_instance_configs_http_info(request)
        return self._call_api(**http_info)

    def show_instance_configs_async_invoker(self, request):
        http_info = self._show_instance_configs_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_instance_configs_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/configs",
            "request_type": request.__class__.__name__,
            "response_type": "ShowInstanceConfigsResponse"
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

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_instance_extend_product_info_async(self, request):
        r"""查询实例的扩容规格列表

        查询实例的扩容规格列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowInstanceExtendProductInfo
        :type request: :class:`huaweicloudsdkkafka.v2.ShowInstanceExtendProductInfoRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.ShowInstanceExtendProductInfoResponse`
        """
        http_info = self._show_instance_extend_product_info_http_info(request)
        return self._call_api(**http_info)

    def show_instance_extend_product_info_async_invoker(self, request):
        http_info = self._show_instance_extend_product_info_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_instance_extend_product_info_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/extend",
            "request_type": request.__class__.__name__,
            "response_type": "ShowInstanceExtendProductInfoResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'engine' in local_var_params:
            query_params.append(('engine', local_var_params['engine']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_instance_messages_async(self, request):
        r"""查询消息

        查询消息的偏移量和消息内容。
        先根据时间戳查询消息的偏移量，再根据偏移量查询消息内容。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowInstanceMessages
        :type request: :class:`huaweicloudsdkkafka.v2.ShowInstanceMessagesRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.ShowInstanceMessagesResponse`
        """
        http_info = self._show_instance_messages_http_info(request)
        return self._call_api(**http_info)

    def show_instance_messages_async_invoker(self, request):
        http_info = self._show_instance_messages_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_instance_messages_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/messages",
            "request_type": request.__class__.__name__,
            "response_type": "ShowInstanceMessagesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'topic' in local_var_params:
            query_params.append(('topic', local_var_params['topic']))
        if 'asc' in local_var_params:
            query_params.append(('asc', local_var_params['asc']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'download' in local_var_params:
            query_params.append(('download', local_var_params['download']))
        if 'message_offset' in local_var_params:
            query_params.append(('message_offset', local_var_params['message_offset']))
        if 'partition' in local_var_params:
            query_params.append(('partition', local_var_params['partition']))
        if 'keyword' in local_var_params:
            query_params.append(('keyword', local_var_params['keyword']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_instance_topic_detail_async(self, request):
        r"""查询Kafka实例Topic详细信息

        查询Kafka实例Topic详细信息。(单个实例调用不要超过1s一次)
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowInstanceTopicDetail
        :type request: :class:`huaweicloudsdkkafka.v2.ShowInstanceTopicDetailRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.ShowInstanceTopicDetailResponse`
        """
        http_info = self._show_instance_topic_detail_http_info(request)
        return self._call_api(**http_info)

    def show_instance_topic_detail_async_invoker(self, request):
        http_info = self._show_instance_topic_detail_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_instance_topic_detail_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/management/topics/{topic}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowInstanceTopicDetailResponse"
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

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_instance_users_async(self, request):
        r"""查询用户列表

        查询用户列表。
        
        Kafka实例开启SASL功能时，才支持多用户管理的功能。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowInstanceUsers
        :type request: :class:`huaweicloudsdkkafka.v2.ShowInstanceUsersRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.ShowInstanceUsersResponse`
        """
        http_info = self._show_instance_users_http_info(request)
        return self._call_api(**http_info)

    def show_instance_users_async_invoker(self, request):
        http_info = self._show_instance_users_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_instance_users_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/users",
            "request_type": request.__class__.__name__,
            "response_type": "ShowInstanceUsersResponse"
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

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_kafka_instance_extend_product_info_async(self, request):
        r"""查询实例的扩容规格列表

        查询实例的扩容规格列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowKafkaInstanceExtendProductInfo
        :type request: :class:`huaweicloudsdkkafka.v2.ShowKafkaInstanceExtendProductInfoRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.ShowKafkaInstanceExtendProductInfoResponse`
        """
        http_info = self._show_kafka_instance_extend_product_info_http_info(request)
        return self._call_api(**http_info)

    def show_kafka_instance_extend_product_info_async_invoker(self, request):
        http_info = self._show_kafka_instance_extend_product_info_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_kafka_instance_extend_product_info_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/kafka/instances/{instance_id}/extend",
            "request_type": request.__class__.__name__,
            "response_type": "ShowKafkaInstanceExtendProductInfoResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_kafka_project_tags_async(self, request):
        r"""查询项目标签

        查询项目标签。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowKafkaProjectTags
        :type request: :class:`huaweicloudsdkkafka.v2.ShowKafkaProjectTagsRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.ShowKafkaProjectTagsResponse`
        """
        http_info = self._show_kafka_project_tags_http_info(request)
        return self._call_api(**http_info)

    def show_kafka_project_tags_async_invoker(self, request):
        http_info = self._show_kafka_project_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_kafka_project_tags_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/kafka/tags",
            "request_type": request.__class__.__name__,
            "response_type": "ShowKafkaProjectTagsResponse"
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

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_kafka_rebalance_log_async(self, request):
        r"""查询Kafka实例重平衡日志详情

        查询Kafka实例重平衡日志详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowKafkaRebalanceLog
        :type request: :class:`huaweicloudsdkkafka.v2.ShowKafkaRebalanceLogRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.ShowKafkaRebalanceLogResponse`
        """
        http_info = self._show_kafka_rebalance_log_http_info(request)
        return self._call_api(**http_info)

    def show_kafka_rebalance_log_async_invoker(self, request):
        http_info = self._show_kafka_rebalance_log_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_kafka_rebalance_log_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/kafka/{project_id}/instances/{instance_id}/log/rebalance-log",
            "request_type": request.__class__.__name__,
            "response_type": "ShowKafkaRebalanceLogResponse"
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

        auth_settings = ['IAM_AUTH_TYPE_NEW']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_kafka_tags_async(self, request):
        r"""查询实例标签

        查询实例标签。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowKafkaTags
        :type request: :class:`huaweicloudsdkkafka.v2.ShowKafkaTagsRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.ShowKafkaTagsResponse`
        """
        http_info = self._show_kafka_tags_http_info(request)
        return self._call_api(**http_info)

    def show_kafka_tags_async_invoker(self, request):
        http_info = self._show_kafka_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_kafka_tags_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/kafka/{instance_id}/tags",
            "request_type": request.__class__.__name__,
            "response_type": "ShowKafkaTagsResponse"
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

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_kafka_topic_partition_diskusage_async(self, request):
        r"""查询topic的磁盘存储情况

        查询topic在Broker上磁盘占用情况。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowKafkaTopicPartitionDiskusage
        :type request: :class:`huaweicloudsdkkafka.v2.ShowKafkaTopicPartitionDiskusageRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.ShowKafkaTopicPartitionDiskusageResponse`
        """
        http_info = self._show_kafka_topic_partition_diskusage_http_info(request)
        return self._call_api(**http_info)

    def show_kafka_topic_partition_diskusage_async_invoker(self, request):
        http_info = self._show_kafka_topic_partition_diskusage_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_kafka_topic_partition_diskusage_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/topics/diskusage",
            "request_type": request.__class__.__name__,
            "response_type": "ShowKafkaTopicPartitionDiskusageResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'min_size' in local_var_params:
            query_params.append(('minSize', local_var_params['min_size']))
        if 'top' in local_var_params:
            query_params.append(('top', local_var_params['top']))
        if 'percentage' in local_var_params:
            query_params.append(('percentage', local_var_params['percentage']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_kafka_topic_quota_async(self, request):
        r"""查询Topic流控配置

        该接口用于查询Topic级别的流控任务。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowKafkaTopicQuota
        :type request: :class:`huaweicloudsdkkafka.v2.ShowKafkaTopicQuotaRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.ShowKafkaTopicQuotaResponse`
        """
        http_info = self._show_kafka_topic_quota_http_info(request)
        return self._call_api(**http_info)

    def show_kafka_topic_quota_async_invoker(self, request):
        http_info = self._show_kafka_topic_quota_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_kafka_topic_quota_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/kafka/{project_id}/instances/{instance_id}/kafka-topic-quota",
            "request_type": request.__class__.__name__,
            "response_type": "ShowKafkaTopicQuotaResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'keyword' in local_var_params:
            query_params.append(('keyword', local_var_params['keyword']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['IAM_AUTH_TYPE_NEW']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_kafka_user_client_quota_async(self, request):
        r"""查询用户/客户端流控配置

        该接口用于向Kafka实例查询流控的配置，若成功则返回流控配置的列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowKafkaUserClientQuota
        :type request: :class:`huaweicloudsdkkafka.v2.ShowKafkaUserClientQuotaRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.ShowKafkaUserClientQuotaResponse`
        """
        http_info = self._show_kafka_user_client_quota_http_info(request)
        return self._call_api(**http_info)

    def show_kafka_user_client_quota_async_invoker(self, request):
        http_info = self._show_kafka_user_client_quota_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_kafka_user_client_quota_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/kafka/{project_id}/instances/{instance_id}/kafka-user-client-quota",
            "request_type": request.__class__.__name__,
            "response_type": "ShowKafkaUserClientQuotaResponse"
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

        auth_settings = ['IAM_AUTH_TYPE_NEW']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_maintain_windows_async(self, request):
        r"""查询维护时间窗时间段

        查询维护时间窗开始时间和结束时间。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowMaintainWindows
        :type request: :class:`huaweicloudsdkkafka.v2.ShowMaintainWindowsRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.ShowMaintainWindowsResponse`
        """
        http_info = self._show_maintain_windows_http_info(request)
        return self._call_api(**http_info)

    def show_maintain_windows_async_invoker(self, request):
        http_info = self._show_maintain_windows_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_maintain_windows_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/instances/maintain-windows",
            "request_type": request.__class__.__name__,
            "response_type": "ShowMaintainWindowsResponse"
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

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_message_diagnosis_report_async(self, request):
        r"""查询诊断报告详情

        查询诊断报告详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowMessageDiagnosisReport
        :type request: :class:`huaweicloudsdkkafka.v2.ShowMessageDiagnosisReportRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.ShowMessageDiagnosisReportResponse`
        """
        http_info = self._show_message_diagnosis_report_http_info(request)
        return self._call_api(**http_info)

    def show_message_diagnosis_report_async_invoker(self, request):
        http_info = self._show_message_diagnosis_report_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_message_diagnosis_report_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/kafka/instances/{instance_id}/message-diagnosis/{report_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowMessageDiagnosisReportResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
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

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_messages_async(self, request):
        r"""查询分区指定时间段的消息

        查询分区指定时间段的消息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowMessages
        :type request: :class:`huaweicloudsdkkafka.v2.ShowMessagesRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.ShowMessagesResponse`
        """
        http_info = self._show_messages_http_info(request)
        return self._call_api(**http_info)

    def show_messages_async_invoker(self, request):
        http_info = self._show_messages_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_messages_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/management/topics/{topic}/messages",
            "request_type": request.__class__.__name__,
            "response_type": "ShowMessagesResponse"
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
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'partition' in local_var_params:
            query_params.append(('partition', local_var_params['partition']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_partition_beginning_message_async(self, request):
        r"""查询分区最早消息的位置

        查询分区最早消息的位置。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowPartitionBeginningMessage
        :type request: :class:`huaweicloudsdkkafka.v2.ShowPartitionBeginningMessageRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.ShowPartitionBeginningMessageResponse`
        """
        http_info = self._show_partition_beginning_message_http_info(request)
        return self._call_api(**http_info)

    def show_partition_beginning_message_async_invoker(self, request):
        http_info = self._show_partition_beginning_message_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_partition_beginning_message_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/management/topics/{topic}/partitions/{partition}/beginning-message",
            "request_type": request.__class__.__name__,
            "response_type": "ShowPartitionBeginningMessageResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'topic' in local_var_params:
            path_params['topic'] = local_var_params['topic']
        if 'partition' in local_var_params:
            path_params['partition'] = local_var_params['partition']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_partition_end_message_async(self, request):
        r"""查询分区最新消息的位置

        查询分区最新消息的位置。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowPartitionEndMessage
        :type request: :class:`huaweicloudsdkkafka.v2.ShowPartitionEndMessageRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.ShowPartitionEndMessageResponse`
        """
        http_info = self._show_partition_end_message_http_info(request)
        return self._call_api(**http_info)

    def show_partition_end_message_async_invoker(self, request):
        http_info = self._show_partition_end_message_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_partition_end_message_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/management/topics/{topic}/partitions/{partition}/end-message",
            "request_type": request.__class__.__name__,
            "response_type": "ShowPartitionEndMessageResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'topic' in local_var_params:
            path_params['topic'] = local_var_params['topic']
        if 'partition' in local_var_params:
            path_params['partition'] = local_var_params['partition']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_partition_message_async(self, request):
        r"""查询分区指定偏移量的消息

        查询分区指定偏移量的消息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowPartitionMessage
        :type request: :class:`huaweicloudsdkkafka.v2.ShowPartitionMessageRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.ShowPartitionMessageResponse`
        """
        http_info = self._show_partition_message_http_info(request)
        return self._call_api(**http_info)

    def show_partition_message_async_invoker(self, request):
        http_info = self._show_partition_message_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_partition_message_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/management/topics/{topic}/partitions/{partition}/message",
            "request_type": request.__class__.__name__,
            "response_type": "ShowPartitionMessageResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'topic' in local_var_params:
            path_params['topic'] = local_var_params['topic']
        if 'partition' in local_var_params:
            path_params['partition'] = local_var_params['partition']

        query_params = []
        if 'message_offset' in local_var_params:
            query_params.append(('message_offset', local_var_params['message_offset']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

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
        :type request: :class:`huaweicloudsdkkafka.v2.ShowQuotasRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.ShowQuotasResponse`
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
        if 'include_tags_quota' in local_var_params:
            query_params.append(('includeTagsQuota', local_var_params['include_tags_quota']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_topic_access_policy_async(self, request):
        r"""查询用户权限

        查询用户权限。
        
        Kafka实例开启SASL功能时，才支持多用户管理的功能。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowTopicAccessPolicy
        :type request: :class:`huaweicloudsdkkafka.v2.ShowTopicAccessPolicyRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.ShowTopicAccessPolicyResponse`
        """
        http_info = self._show_topic_access_policy_http_info(request)
        return self._call_api(**http_info)

    def show_topic_access_policy_async_invoker(self, request):
        http_info = self._show_topic_access_policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_topic_access_policy_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/instances/{instance_id}/topics/{topic_name}/accesspolicy",
            "request_type": request.__class__.__name__,
            "response_type": "ShowTopicAccessPolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'topic_name' in local_var_params:
            path_params['topic_name'] = local_var_params['topic_name']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def stop_kafka_rebalance_log_task_async(self, request):
        r"""关闭Kafka实例重平衡日志功能

        关闭Kafka实例重平衡日志功能。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for StopKafkaRebalanceLogTask
        :type request: :class:`huaweicloudsdkkafka.v2.StopKafkaRebalanceLogTaskRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.StopKafkaRebalanceLogTaskResponse`
        """
        http_info = self._stop_kafka_rebalance_log_task_http_info(request)
        return self._call_api(**http_info)

    def stop_kafka_rebalance_log_task_async_invoker(self, request):
        http_info = self._stop_kafka_rebalance_log_task_http_info(request)
        return AsyncInvoker(self, http_info)

    def _stop_kafka_rebalance_log_task_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/kafka/{project_id}/instances/{instance_id}/log/rebalance-log",
            "request_type": request.__class__.__name__,
            "response_type": "StopKafkaRebalanceLogTaskResponse"
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

        auth_settings = ['IAM_AUTH_TYPE_NEW']

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

        修改实例信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateInstance
        :type request: :class:`huaweicloudsdkkafka.v2.UpdateInstanceRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.UpdateInstanceResponse`
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

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_instance_auto_create_topic_async(self, request):
        r"""开启或关闭实例自动创建Topic功能

        开启或关闭实例自动创建Topic功能。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateInstanceAutoCreateTopic
        :type request: :class:`huaweicloudsdkkafka.v2.UpdateInstanceAutoCreateTopicRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.UpdateInstanceAutoCreateTopicResponse`
        """
        http_info = self._update_instance_auto_create_topic_http_info(request)
        return self._call_api(**http_info)

    def update_instance_auto_create_topic_async_invoker(self, request):
        http_info = self._update_instance_auto_create_topic_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_instance_auto_create_topic_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/autotopic",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateInstanceAutoCreateTopicResponse"
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

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_instance_consumer_group_async(self, request):
        r"""修改指定消费组

        修改指定消费组。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateInstanceConsumerGroup
        :type request: :class:`huaweicloudsdkkafka.v2.UpdateInstanceConsumerGroupRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.UpdateInstanceConsumerGroupResponse`
        """
        http_info = self._update_instance_consumer_group_http_info(request)
        return self._call_api(**http_info)

    def update_instance_consumer_group_async_invoker(self, request):
        http_info = self._update_instance_consumer_group_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_instance_consumer_group_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{engine}/{project_id}/instances/{instance_id}/groups/{group}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateInstanceConsumerGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'engine' in local_var_params:
            path_params['engine'] = local_var_params['engine']
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

        auth_settings = ['IAM_AUTH_TYPE_NEW']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_instance_cross_vpc_ip_async(self, request):
        r"""修改实例跨VPC访问的内网IP

        修改实例跨VPC访问的内网IP。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateInstanceCrossVpcIp
        :type request: :class:`huaweicloudsdkkafka.v2.UpdateInstanceCrossVpcIpRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.UpdateInstanceCrossVpcIpResponse`
        """
        http_info = self._update_instance_cross_vpc_ip_http_info(request)
        return self._call_api(**http_info)

    def update_instance_cross_vpc_ip_async_invoker(self, request):
        http_info = self._update_instance_cross_vpc_ip_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_instance_cross_vpc_ip_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/crossvpc/modify",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateInstanceCrossVpcIpResponse"
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

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_instance_group_async(self, request):
        r"""修改所有消费组

        修改所有消费组。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateInstanceGroup
        :type request: :class:`huaweicloudsdkkafka.v2.UpdateInstanceGroupRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.UpdateInstanceGroupResponse`
        """
        http_info = self._update_instance_group_http_info(request)
        return self._call_api(**http_info)

    def update_instance_group_async_invoker(self, request):
        http_info = self._update_instance_group_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_instance_group_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{engine}/{project_id}/instances/{instance_id}/groups",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateInstanceGroupResponse"
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

        auth_settings = ['IAM_AUTH_TYPE_NEW']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_instance_topic_async(self, request):
        r"""修改Kafka实例Topic

        修改Kafka实例Topic
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateInstanceTopic
        :type request: :class:`huaweicloudsdkkafka.v2.UpdateInstanceTopicRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.UpdateInstanceTopicResponse`
        """
        http_info = self._update_instance_topic_http_info(request)
        return self._call_api(**http_info)

    def update_instance_topic_async_invoker(self, request):
        http_info = self._update_instance_topic_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_instance_topic_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/topics",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateInstanceTopicResponse"
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

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_instance_user_async(self, request):
        r"""修改用户参数

        修改用户参数
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateInstanceUser
        :type request: :class:`huaweicloudsdkkafka.v2.UpdateInstanceUserRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.UpdateInstanceUserResponse`
        """
        http_info = self._update_instance_user_http_info(request)
        return self._call_api(**http_info)

    def update_instance_user_async_invoker(self, request):
        http_info = self._update_instance_user_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_instance_user_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{engine}/{project_id}/instances/{instance_id}/users/{user_name}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateInstanceUserResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'engine' in local_var_params:
            path_params['engine'] = local_var_params['engine']
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

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_kafka_port_protocol_async(self, request):
        r"""修改Kafka的接入方式

        修改Kafka的内网或者公网接入方式。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateKafkaPortProtocol
        :type request: :class:`huaweicloudsdkkafka.v2.UpdateKafkaPortProtocolRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.UpdateKafkaPortProtocolResponse`
        """
        http_info = self._update_kafka_port_protocol_http_info(request)
        return self._call_api(**http_info)

    def update_kafka_port_protocol_async_invoker(self, request):
        http_info = self._update_kafka_port_protocol_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_kafka_port_protocol_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/{engine}/instances/{instance_id}/plain-ssl-switch",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateKafkaPortProtocolResponse"
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

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_kafka_user_client_quota_task_async(self, request):
        r"""修改用户/客户端流控配置

        该接口用于向Kafka实例提交修改用户、客户端级别的流控任务，若成功则返回流控任务的job_id。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateKafkaUserClientQuotaTask
        :type request: :class:`huaweicloudsdkkafka.v2.UpdateKafkaUserClientQuotaTaskRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.UpdateKafkaUserClientQuotaTaskResponse`
        """
        http_info = self._update_kafka_user_client_quota_task_http_info(request)
        return self._call_api(**http_info)

    def update_kafka_user_client_quota_task_async_invoker(self, request):
        http_info = self._update_kafka_user_client_quota_task_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_kafka_user_client_quota_task_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/kafka/{project_id}/instances/{instance_id}/kafka-user-client-quota",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateKafkaUserClientQuotaTaskResponse"
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

        auth_settings = ['IAM_AUTH_TYPE_NEW']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_topic_access_policy_async(self, request):
        r"""设置用户权限

        设置用户权限。
        
        Kafka实例开启SASL功能时，才支持多用户管理的功能。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateTopicAccessPolicy
        :type request: :class:`huaweicloudsdkkafka.v2.UpdateTopicAccessPolicyRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.UpdateTopicAccessPolicyResponse`
        """
        http_info = self._update_topic_access_policy_http_info(request)
        return self._call_api(**http_info)

    def update_topic_access_policy_async_invoker(self, request):
        http_info = self._update_topic_access_policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_topic_access_policy_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/instances/{instance_id}/topics/accesspolicy",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateTopicAccessPolicyResponse"
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

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_topic_replica_async(self, request):
        r"""修改Kafka实例Topic分区的副本

        修改Kafka实例Topic分区的副本。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateTopicReplica
        :type request: :class:`huaweicloudsdkkafka.v2.UpdateTopicReplicaRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.UpdateTopicReplicaResponse`
        """
        http_info = self._update_topic_replica_http_info(request)
        return self._call_api(**http_info)

    def update_topic_replica_async_invoker(self, request):
        http_info = self._update_topic_replica_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_topic_replica_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/management/topics/{topic}/replicas-reassignment",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateTopicReplicaResponse"
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

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_connector_async(self, request):
        r"""开启Smart Connect（按需实例）

        开启Smart Connect，提交创建Smart Connect节点任务。
        
        [**当前通过调用API，只支持按需实例创建Smart Connect节点。**](tag:hws,hws_hk,g42,hk_g42,ctc)
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateConnector
        :type request: :class:`huaweicloudsdkkafka.v2.CreateConnectorRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.CreateConnectorResponse`
        """
        http_info = self._create_connector_http_info(request)
        return self._call_api(**http_info)

    def create_connector_async_invoker(self, request):
        http_info = self._create_connector_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_connector_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/connector",
            "request_type": request.__class__.__name__,
            "response_type": "CreateConnectorResponse"
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

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_connector_task_async(self, request):
        r"""创建Smart Connect任务

        创建Smart Connect任务。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateConnectorTask
        :type request: :class:`huaweicloudsdkkafka.v2.CreateConnectorTaskRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.CreateConnectorTaskResponse`
        """
        http_info = self._create_connector_task_http_info(request)
        return self._call_api(**http_info)

    def create_connector_task_async_invoker(self, request):
        http_info = self._create_connector_task_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_connector_task_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/connector/tasks",
            "request_type": request.__class__.__name__,
            "response_type": "CreateConnectorTaskResponse"
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

    def delete_connector_async(self, request):
        r"""关闭Smart Connect（按需实例）

        介绍按需实例如何关闭Smart Connect。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteConnector
        :type request: :class:`huaweicloudsdkkafka.v2.DeleteConnectorRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.DeleteConnectorResponse`
        """
        http_info = self._delete_connector_http_info(request)
        return self._call_api(**http_info)

    def delete_connector_async_invoker(self, request):
        http_info = self._delete_connector_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_connector_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/kafka/instances/{instance_id}/delete-connector",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteConnectorResponse"
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

    def delete_connector_task_async(self, request):
        r"""删除Smart Connect任务

        删除Smart Connect任务。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteConnectorTask
        :type request: :class:`huaweicloudsdkkafka.v2.DeleteConnectorTaskRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.DeleteConnectorTaskResponse`
        """
        http_info = self._delete_connector_task_http_info(request)
        return self._call_api(**http_info)

    def delete_connector_task_async_invoker(self, request):
        http_info = self._delete_connector_task_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_connector_task_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/connector/tasks/{task_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteConnectorTaskResponse"
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

    def list_connector_tasks_async(self, request):
        r"""查询Smart Connect任务列表

        查询Smart Connect任务列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListConnectorTasks
        :type request: :class:`huaweicloudsdkkafka.v2.ListConnectorTasksRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.ListConnectorTasksResponse`
        """
        http_info = self._list_connector_tasks_http_info(request)
        return self._call_api(**http_info)

    def list_connector_tasks_async_invoker(self, request):
        http_info = self._list_connector_tasks_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_connector_tasks_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/connector/tasks",
            "request_type": request.__class__.__name__,
            "response_type": "ListConnectorTasksResponse"
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

    def modify_connector_task_async(self, request):
        r"""修改Smart Connect任务配置。

        修改Smart Connect任务配置。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ModifyConnectorTask
        :type request: :class:`huaweicloudsdkkafka.v2.ModifyConnectorTaskRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.ModifyConnectorTaskResponse`
        """
        http_info = self._modify_connector_task_http_info(request)
        return self._call_api(**http_info)

    def modify_connector_task_async_invoker(self, request):
        http_info = self._modify_connector_task_http_info(request)
        return AsyncInvoker(self, http_info)

    def _modify_connector_task_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/connector/tasks/{task_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ModifyConnectorTaskResponse"
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

    def pause_connector_task_async(self, request):
        r"""暂停Smart Connect任务

        暂停Smart Connect任务。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for PauseConnectorTask
        :type request: :class:`huaweicloudsdkkafka.v2.PauseConnectorTaskRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.PauseConnectorTaskResponse`
        """
        http_info = self._pause_connector_task_http_info(request)
        return self._call_api(**http_info)

    def pause_connector_task_async_invoker(self, request):
        http_info = self._pause_connector_task_http_info(request)
        return AsyncInvoker(self, http_info)

    def _pause_connector_task_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/connector/tasks/{task_id}/pause",
            "request_type": request.__class__.__name__,
            "response_type": "PauseConnectorTaskResponse"
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

    def restart_connector_task_async(self, request):
        r"""启动未启动的Smart Connect任务/重启已暂停或者运行中的Smart Connect任务

        用于**启动未启动的Smart Connect任务**以及**重启已暂停或者运行中的Smart Connect任务**。注意，重启Smart Connect任务将重置同步进度，并重新开始同步任务。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RestartConnectorTask
        :type request: :class:`huaweicloudsdkkafka.v2.RestartConnectorTaskRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.RestartConnectorTaskResponse`
        """
        http_info = self._restart_connector_task_http_info(request)
        return self._call_api(**http_info)

    def restart_connector_task_async_invoker(self, request):
        http_info = self._restart_connector_task_http_info(request)
        return AsyncInvoker(self, http_info)

    def _restart_connector_task_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/kafka/instances/{instance_id}/connector/tasks/{task_id}/restart",
            "request_type": request.__class__.__name__,
            "response_type": "RestartConnectorTaskResponse"
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

    def restart_smart_connector_task_async(self, request):
        r"""启动未启动的Smart Connect任务/重启Smart Connect任务

        启动未启动的Smart Connect任务/重启Smart Connect任务。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RestartSmartConnectorTask
        :type request: :class:`huaweicloudsdkkafka.v2.RestartSmartConnectorTaskRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.RestartSmartConnectorTaskResponse`
        """
        http_info = self._restart_smart_connector_task_http_info(request)
        return self._call_api(**http_info)

    def restart_smart_connector_task_async_invoker(self, request):
        http_info = self._restart_smart_connector_task_http_info(request)
        return AsyncInvoker(self, http_info)

    def _restart_smart_connector_task_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/connector/tasks/{task_id}/restart",
            "request_type": request.__class__.__name__,
            "response_type": "RestartSmartConnectorTaskResponse"
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

    def resume_connector_task_async(self, request):
        r"""启动已暂停的Smart Connect任务

        启动已暂停的Smart Connect任务。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ResumeConnectorTask
        :type request: :class:`huaweicloudsdkkafka.v2.ResumeConnectorTaskRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.ResumeConnectorTaskResponse`
        """
        http_info = self._resume_connector_task_http_info(request)
        return self._call_api(**http_info)

    def resume_connector_task_async_invoker(self, request):
        http_info = self._resume_connector_task_http_info(request)
        return AsyncInvoker(self, http_info)

    def _resume_connector_task_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/connector/tasks/{task_id}/resume",
            "request_type": request.__class__.__name__,
            "response_type": "ResumeConnectorTaskResponse"
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

    def show_connector_task_async(self, request):
        r"""查询Smart Connect任务详情

        查询Smart Connect任务详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowConnectorTask
        :type request: :class:`huaweicloudsdkkafka.v2.ShowConnectorTaskRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.ShowConnectorTaskResponse`
        """
        http_info = self._show_connector_task_http_info(request)
        return self._call_api(**http_info)

    def show_connector_task_async_invoker(self, request):
        http_info = self._show_connector_task_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_connector_task_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/connector/tasks/{task_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowConnectorTaskResponse"
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

    def validate_connector_connectivity_async(self, request):
        r"""校验Connector连通性

        校验Connector连通性。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ValidateConnectorConnectivity
        :type request: :class:`huaweicloudsdkkafka.v2.ValidateConnectorConnectivityRequest`
        :rtype: :class:`huaweicloudsdkkafka.v2.ValidateConnectorConnectivityResponse`
        """
        http_info = self._validate_connector_connectivity_http_info(request)
        return self._call_api(**http_info)

    def validate_connector_connectivity_async_invoker(self, request):
        http_info = self._validate_connector_connectivity_http_info(request)
        return AsyncInvoker(self, http_info)

    def _validate_connector_connectivity_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/connector/validate",
            "request_type": request.__class__.__name__,
            "response_type": "ValidateConnectorConnectivityResponse"
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

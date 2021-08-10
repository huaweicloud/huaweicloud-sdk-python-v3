# coding: utf-8

from __future__ import absolute_import

import datetime
import re
import importlib

import six

from huaweicloudsdkcore.client import Client, ClientBuilder
from huaweicloudsdkcore.exceptions import exceptions
from huaweicloudsdkcore.utils import http_utils
from huaweicloudsdkcore.sdk_stream_request import SdkStreamRequest


class KafkaClient(Client):
    """
    :param configuration: .Configuration object for this client
    :param pool_threads: The number of threads to use for async requests
        to the API. More threads means more concurrent API requests.
    """

    PRIMITIVE_TYPES = (float, bool, bytes, six.text_type) + six.integer_types
    NATIVE_TYPES_MAPPING = {
        'int': int,
        'long': int if six.PY3 else long,
        'float': float,
        'str': str,
        'bool': bool,
        'date': datetime.date,
        'datetime': datetime.datetime,
        'object': object,
    }

    def __init__(self):
        super(KafkaClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkkafka.v2.model")
        self.preset_headers = {'User-Agent': 'HuaweiCloud-SDK-Python'}

    @classmethod
    def new_builder(cls, clazz=None):
        if clazz is None:
            return ClientBuilder(cls)

        if clazz.__name__ != "KafkaClient":
            raise TypeError("client type error, support client type is KafkaClient")

        return ClientBuilder(clazz)

    def batch_create_or_delete_kafka_tag(self, request):
        """批量添加或删除实例标签

        批量添加或删除实例标签。

        :param BatchCreateOrDeleteKafkaTagRequest request
        :return: BatchCreateOrDeleteKafkaTagResponse
        """
        return self.batch_create_or_delete_kafka_tag_with_http_info(request)

    def batch_create_or_delete_kafka_tag_with_http_info(self, request):
        """批量添加或删除实例标签

        批量添加或删除实例标签。

        :param BatchCreateOrDeleteKafkaTagRequest request
        :return: BatchCreateOrDeleteKafkaTagResponse
        """

        all_params = ['instance_id', 'batch_create_or_delete_kafka_tag_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v2/{project_id}/kafka/{instance_id}/tags/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='BatchCreateOrDeleteKafkaTagResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def batch_delete_instance_topic(self, request):
        """Kafka实例批量删除Topic

        该接口用于向Kafka实例批量删除Topic。

        :param BatchDeleteInstanceTopicRequest request
        :return: BatchDeleteInstanceTopicResponse
        """
        return self.batch_delete_instance_topic_with_http_info(request)

    def batch_delete_instance_topic_with_http_info(self, request):
        """Kafka实例批量删除Topic

        该接口用于向Kafka实例批量删除Topic。

        :param BatchDeleteInstanceTopicRequest request
        :return: BatchDeleteInstanceTopicResponse
        """

        all_params = ['instance_id', 'batch_delete_instance_topic_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v2/{project_id}/instances/{instance_id}/topics/delete',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='BatchDeleteInstanceTopicResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def batch_delete_instance_users(self, request):
        """批量删除用户

        批量删除Kafka实例的用户

        :param BatchDeleteInstanceUsersRequest request
        :return: BatchDeleteInstanceUsersResponse
        """
        return self.batch_delete_instance_users_with_http_info(request)

    def batch_delete_instance_users_with_http_info(self, request):
        """批量删除用户

        批量删除Kafka实例的用户

        :param BatchDeleteInstanceUsersRequest request
        :return: BatchDeleteInstanceUsersResponse
        """

        all_params = ['instance_id', 'batch_delete_instance_users_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v2/{project_id}/instances/{instance_id}/users',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='BatchDeleteInstanceUsersResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def batch_restart_or_delete_instances(self, request):
        """批量重启或删除实例

        批量重启或删除实例。  在实例重启过程中，客户端的生产与消费消息等请求会被拒绝。  实例删除后，实例中原有的数据将被删除，且没有备份，请谨慎操作。

        :param BatchRestartOrDeleteInstancesRequest request
        :return: BatchRestartOrDeleteInstancesResponse
        """
        return self.batch_restart_or_delete_instances_with_http_info(request)

    def batch_restart_or_delete_instances_with_http_info(self, request):
        """批量重启或删除实例

        批量重启或删除实例。  在实例重启过程中，客户端的生产与消费消息等请求会被拒绝。  实例删除后，实例中原有的数据将被删除，且没有备份，请谨慎操作。

        :param BatchRestartOrDeleteInstancesRequest request
        :return: BatchRestartOrDeleteInstancesResponse
        """

        all_params = ['batch_restart_or_delete_instances_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v2/{project_id}/instances/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='BatchRestartOrDeleteInstancesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_connector(self, request):
        """创建实例的转储节点

        创建实例的转储节点。

        :param CreateConnectorRequest request
        :return: CreateConnectorResponse
        """
        return self.create_connector_with_http_info(request)

    def create_connector_with_http_info(self, request):
        """创建实例的转储节点

        创建实例的转储节点。

        :param CreateConnectorRequest request
        :return: CreateConnectorResponse
        """

        all_params = ['instance_id', 'create_connector_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v2/{project_id}/instances/{instance_id}/connector',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateConnectorResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_instance_topic(self, request):
        """Kafka实例创建Topic

        该接口用于向Kafka实例创建Topic。

        :param CreateInstanceTopicRequest request
        :return: CreateInstanceTopicResponse
        """
        return self.create_instance_topic_with_http_info(request)

    def create_instance_topic_with_http_info(self, request):
        """Kafka实例创建Topic

        该接口用于向Kafka实例创建Topic。

        :param CreateInstanceTopicRequest request
        :return: CreateInstanceTopicResponse
        """

        all_params = ['instance_id', 'create_instance_topic_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v2/{project_id}/instances/{instance_id}/topics',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateInstanceTopicResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_instance_user(self, request):
        """创建用户

        创建Kafka实例的用户，用户可连接开启SASL的Kafka实例。

        :param CreateInstanceUserRequest request
        :return: CreateInstanceUserResponse
        """
        return self.create_instance_user_with_http_info(request)

    def create_instance_user_with_http_info(self, request):
        """创建用户

        创建Kafka实例的用户，用户可连接开启SASL的Kafka实例。

        :param CreateInstanceUserRequest request
        :return: CreateInstanceUserResponse
        """

        all_params = ['instance_id', 'create_instance_user_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v2/{project_id}/instances/{instance_id}/users',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateInstanceUserResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_partition(self, request):
        """新增Kafka实例指定Topic分区

        新增Kafka实例指定Topic分区。

        :param CreatePartitionRequest request
        :return: CreatePartitionResponse
        """
        return self.create_partition_with_http_info(request)

    def create_partition_with_http_info(self, request):
        """新增Kafka实例指定Topic分区

        新增Kafka实例指定Topic分区。

        :param CreatePartitionRequest request
        :return: CreatePartitionResponse
        """

        all_params = ['instance_id', 'topic', 'create_partition_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'topic' in local_var_params:
            path_params['topic'] = local_var_params['topic']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v2/{project_id}/instances/{instance_id}/management/topics/{topic}/partitions-reassignment',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreatePartitionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_post_paid_instance(self, request):
        """创建实例（按需）

        创建实例，该接口创建的实例为按需计费的方式。

        :param CreatePostPaidInstanceRequest request
        :return: CreatePostPaidInstanceResponse
        """
        return self.create_post_paid_instance_with_http_info(request)

    def create_post_paid_instance_with_http_info(self, request):
        """创建实例（按需）

        创建实例，该接口创建的实例为按需计费的方式。

        :param CreatePostPaidInstanceRequest request
        :return: CreatePostPaidInstanceResponse
        """

        all_params = ['create_post_paid_instance_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v2/{project_id}/instances',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreatePostPaidInstanceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_sink_task(self, request):
        """创建转储任务

        创建转储任务。

        :param CreateSinkTaskRequest request
        :return: CreateSinkTaskResponse
        """
        return self.create_sink_task_with_http_info(request)

    def create_sink_task_with_http_info(self, request):
        """创建转储任务

        创建转储任务。

        :param CreateSinkTaskRequest request
        :return: CreateSinkTaskResponse
        """

        all_params = ['connector_id', 'create_sink_task_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'connector_id' in local_var_params:
            path_params['connector_id'] = local_var_params['connector_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v2/{project_id}/connectors/{connector_id}/sink-tasks',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateSinkTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_background_task(self, request):
        """删除后台任务管理中的指定记录

        删除后台任务管理中的指定记录。

        :param DeleteBackgroundTaskRequest request
        :return: DeleteBackgroundTaskResponse
        """
        return self.delete_background_task_with_http_info(request)

    def delete_background_task_with_http_info(self, request):
        """删除后台任务管理中的指定记录

        删除后台任务管理中的指定记录。

        :param DeleteBackgroundTaskRequest request
        :return: DeleteBackgroundTaskResponse
        """

        all_params = ['instance_id', 'task_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v2/{project_id}/instances/{instance_id}/tasks/{task_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteBackgroundTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_instance(self, request):
        """删除指定的实例

        删除指定的实例，释放该实例的所有资源。

        :param DeleteInstanceRequest request
        :return: DeleteInstanceResponse
        """
        return self.delete_instance_with_http_info(request)

    def delete_instance_with_http_info(self, request):
        """删除指定的实例

        删除指定的实例，释放该实例的所有资源。

        :param DeleteInstanceRequest request
        :return: DeleteInstanceResponse
        """

        all_params = ['instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v2/{project_id}/instances/{instance_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteInstanceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_sink_task(self, request):
        """删除单个转储任务

        删除单个转储任务。

        :param DeleteSinkTaskRequest request
        :return: DeleteSinkTaskResponse
        """
        return self.delete_sink_task_with_http_info(request)

    def delete_sink_task_with_http_info(self, request):
        """删除单个转储任务

        删除单个转储任务。

        :param DeleteSinkTaskRequest request
        :return: DeleteSinkTaskResponse
        """

        all_params = ['connector_id', 'task_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'connector_id' in local_var_params:
            path_params['connector_id'] = local_var_params['connector_id']
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v2/{project_id}/connectors/{connector_id}/sink-tasks/{task_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteSinkTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_available_zones(self, request):
        """查询可用区信息

        在创建实例时，需要配置实例所在的可用区ID，可通过该接口查询可用区的ID。

        :param ListAvailableZonesRequest request
        :return: ListAvailableZonesResponse
        """
        return self.list_available_zones_with_http_info(request)

    def list_available_zones_with_http_info(self, request):
        """查询可用区信息

        在创建实例时，需要配置实例所在的可用区ID，可通过该接口查询可用区的ID。

        :param ListAvailableZonesRequest request
        :return: ListAvailableZonesResponse
        """

        all_params = []
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v2/available-zones',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListAvailableZonesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_background_tasks(self, request):
        """查询实例的后台任务列表

        查询实例的后台任务列表。

        :param ListBackgroundTasksRequest request
        :return: ListBackgroundTasksResponse
        """
        return self.list_background_tasks_with_http_info(request)

    def list_background_tasks_with_http_info(self, request):
        """查询实例的后台任务列表

        查询实例的后台任务列表。

        :param ListBackgroundTasksRequest request
        :return: ListBackgroundTasksResponse
        """

        all_params = ['instance_id', 'start', 'limit', 'begin_time', 'end_time']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v2/{project_id}/instances/{instance_id}/tasks',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListBackgroundTasksResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_instance_topics(self, request):
        """Kafka实例查询Topic

        该接口用于查询指定Kafka实例的Topic详情。

        :param ListInstanceTopicsRequest request
        :return: ListInstanceTopicsResponse
        """
        return self.list_instance_topics_with_http_info(request)

    def list_instance_topics_with_http_info(self, request):
        """Kafka实例查询Topic

        该接口用于查询指定Kafka实例的Topic详情。

        :param ListInstanceTopicsRequest request
        :return: ListInstanceTopicsResponse
        """

        all_params = ['instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v2/{project_id}/instances/{instance_id}/topics',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListInstanceTopicsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_instances(self, request):
        """查询所有实例列表

        查询租户的实例列表，支持按照条件查询。

        :param ListInstancesRequest request
        :return: ListInstancesResponse
        """
        return self.list_instances_with_http_info(request)

    def list_instances_with_http_info(self, request):
        """查询所有实例列表

        查询租户的实例列表，支持按照条件查询。

        :param ListInstancesRequest request
        :return: ListInstancesResponse
        """

        all_params = ['engine', 'name', 'instance_id', 'status', 'include_failure', 'exact_match_name', 'enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v2/{project_id}/instances',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListInstancesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_products(self, request):
        """查询产品规格列表

        在创建kafka实例时，需要配置订购的产品ID（即product_id），可通过该接口查询产品规格。  例如，要订购按需计费、基准带宽为100MB的kafka实例，可从接口响应消息中，查找Hourly的消息体，然后找到bandwidth为100MB的记录对应的product_id，该product_id的值即是创建上述kafka实例时需要配置的产品ID。  同时，unavailable_zones字段表示资源不足的可用区列表，如果为空，则表示所有可用区都有资源，如果不为空，则表示字段值的可用区没有资源。所以必须确保您购买的资源所在的可用区有资源，不在该字段列表内。  例如，响应消息中bandwidth字段为1200MB的记录，unavailable_zones字段包含cn-east-2b、cn-east-2a和cn-east-2d，表示在华东-上海2的可用区1、可用区2、可用区3都没有该资源。

        :param ListProductsRequest request
        :return: ListProductsResponse
        """
        return self.list_products_with_http_info(request)

    def list_products_with_http_info(self, request):
        """查询产品规格列表

        在创建kafka实例时，需要配置订购的产品ID（即product_id），可通过该接口查询产品规格。  例如，要订购按需计费、基准带宽为100MB的kafka实例，可从接口响应消息中，查找Hourly的消息体，然后找到bandwidth为100MB的记录对应的product_id，该product_id的值即是创建上述kafka实例时需要配置的产品ID。  同时，unavailable_zones字段表示资源不足的可用区列表，如果为空，则表示所有可用区都有资源，如果不为空，则表示字段值的可用区没有资源。所以必须确保您购买的资源所在的可用区有资源，不在该字段列表内。  例如，响应消息中bandwidth字段为1200MB的记录，unavailable_zones字段包含cn-east-2b、cn-east-2a和cn-east-2d，表示在华东-上海2的可用区1、可用区2、可用区3都没有该资源。

        :param ListProductsRequest request
        :return: ListProductsResponse
        """

        all_params = ['engine']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'engine' in local_var_params:
            query_params.append(('engine', local_var_params['engine']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v2/products',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListProductsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_sink_tasks(self, request):
        """查询转储任务列表

        查询转储任务列表。

        :param ListSinkTasksRequest request
        :return: ListSinkTasksResponse
        """
        return self.list_sink_tasks_with_http_info(request)

    def list_sink_tasks_with_http_info(self, request):
        """查询转储任务列表

        查询转储任务列表。

        :param ListSinkTasksRequest request
        :return: ListSinkTasksResponse
        """

        all_params = ['connector_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'connector_id' in local_var_params:
            path_params['connector_id'] = local_var_params['connector_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v2/{project_id}/connectors/{connector_id}/sink-tasks',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListSinkTasksResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def reset_manager_password(self, request):
        """重置Manager密码

        重置Manager密码。

        :param ResetManagerPasswordRequest request
        :return: ResetManagerPasswordResponse
        """
        return self.reset_manager_password_with_http_info(request)

    def reset_manager_password_with_http_info(self, request):
        """重置Manager密码

        重置Manager密码。

        :param ResetManagerPasswordRequest request
        :return: ResetManagerPasswordResponse
        """

        all_params = ['instance_id', 'reset_manager_password_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v2/{project_id}/instances/{instance_id}/kafka-manager-password',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ResetManagerPasswordResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def reset_message_offset(self, request):
        """重置消费组消费进度到指定位置

        Kafka实例不支持在线重置消费进度。在执行重置消费进度之前，必须停止被重置消费组客户端。  > 在停止被重置消费组客户端后，需要经过ConsumerConfig.SESSION_TIMEOUT_MS_CONFIG配置的时间（默认10000毫秒），服务端才认为消费组客户端真正下线。

        :param ResetMessageOffsetRequest request
        :return: ResetMessageOffsetResponse
        """
        return self.reset_message_offset_with_http_info(request)

    def reset_message_offset_with_http_info(self, request):
        """重置消费组消费进度到指定位置

        Kafka实例不支持在线重置消费进度。在执行重置消费进度之前，必须停止被重置消费组客户端。  > 在停止被重置消费组客户端后，需要经过ConsumerConfig.SESSION_TIMEOUT_MS_CONFIG配置的时间（默认10000毫秒），服务端才认为消费组客户端真正下线。

        :param ResetMessageOffsetRequest request
        :return: ResetMessageOffsetResponse
        """

        all_params = ['instance_id', 'group', 'reset_message_offset_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'group' in local_var_params:
            path_params['group'] = local_var_params['group']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v2/{project_id}/instances/{instance_id}/management/groups/{group}/reset-message-offset',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ResetMessageOffsetResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def reset_password(self, request):
        """重置密码

        重置密码。

        :param ResetPasswordRequest request
        :return: ResetPasswordResponse
        """
        return self.reset_password_with_http_info(request)

    def reset_password_with_http_info(self, request):
        """重置密码

        重置密码。

        :param ResetPasswordRequest request
        :return: ResetPasswordResponse
        """

        all_params = ['instance_id', 'reset_password_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v2/{project_id}/instances/{instance_id}/password',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ResetPasswordResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def reset_user_passwrod(self, request):
        """重置用户密码

        重置用户密码

        :param ResetUserPasswrodRequest request
        :return: ResetUserPasswrodResponse
        """
        return self.reset_user_passwrod_with_http_info(request)

    def reset_user_passwrod_with_http_info(self, request):
        """重置用户密码

        重置用户密码

        :param ResetUserPasswrodRequest request
        :return: ResetUserPasswrodResponse
        """

        all_params = ['instance_id', 'user_name', 'reset_user_passwrod_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'user_name' in local_var_params:
            path_params['user_name'] = local_var_params['user_name']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v2/{project_id}/instances/{instance_id}/users/{user_name}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ResetUserPasswrodResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def resize_instance(self, request):
        """实例规格变更

        实例规格变更。

        :param ResizeInstanceRequest request
        :return: ResizeInstanceResponse
        """
        return self.resize_instance_with_http_info(request)

    def resize_instance_with_http_info(self, request):
        """实例规格变更

        实例规格变更。

        :param ResizeInstanceRequest request
        :return: ResizeInstanceResponse
        """

        all_params = ['instance_id', 'resize_instance_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v2/{project_id}/instances/{instance_id}/extend',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ResizeInstanceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def restart_manager(self, request):
        """重启Manager

        重启Manager。

        :param RestartManagerRequest request
        :return: RestartManagerResponse
        """
        return self.restart_manager_with_http_info(request)

    def restart_manager_with_http_info(self, request):
        """重启Manager

        重启Manager。

        :param RestartManagerRequest request
        :return: RestartManagerResponse
        """

        all_params = ['instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v2/{project_id}/instances/{instance_id}/restart-kafka-manager',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='RestartManagerResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_background_task(self, request):
        """查询后台任务管理中的指定记录

        查询后台任务管理中的指定记录。

        :param ShowBackgroundTaskRequest request
        :return: ShowBackgroundTaskResponse
        """
        return self.show_background_task_with_http_info(request)

    def show_background_task_with_http_info(self, request):
        """查询后台任务管理中的指定记录

        查询后台任务管理中的指定记录。

        :param ShowBackgroundTaskRequest request
        :return: ShowBackgroundTaskResponse
        """

        all_params = ['instance_id', 'task_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v2/{project_id}/instances/{instance_id}/tasks/{task_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowBackgroundTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_ces_hierarchy(self, request):
        """查询实例在CES的监控层级关系

        查询实例在CES的监控层级关系。

        :param ShowCesHierarchyRequest request
        :return: ShowCesHierarchyResponse
        """
        return self.show_ces_hierarchy_with_http_info(request)

    def show_ces_hierarchy_with_http_info(self, request):
        """查询实例在CES的监控层级关系

        查询实例在CES的监控层级关系。

        :param ShowCesHierarchyRequest request
        :return: ShowCesHierarchyResponse
        """

        all_params = ['instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v2/{project_id}/instances/{instance_id}/ces-hierarchy',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowCesHierarchyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_cluster(self, request):
        """查询Kafka集群元数据信息

        查询Kafka集群元数据信息。

        :param ShowClusterRequest request
        :return: ShowClusterResponse
        """
        return self.show_cluster_with_http_info(request)

    def show_cluster_with_http_info(self, request):
        """查询Kafka集群元数据信息

        查询Kafka集群元数据信息。

        :param ShowClusterRequest request
        :return: ShowClusterResponse
        """

        all_params = ['instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v2/{project_id}/instances/{instance_id}/management/cluster',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowClusterResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_coordinators(self, request):
        """查询Kafka实例的协调器信息

        查询Kafka实例的协调器信息。

        :param ShowCoordinatorsRequest request
        :return: ShowCoordinatorsResponse
        """
        return self.show_coordinators_with_http_info(request)

    def show_coordinators_with_http_info(self, request):
        """查询Kafka实例的协调器信息

        查询Kafka实例的协调器信息。

        :param ShowCoordinatorsRequest request
        :return: ShowCoordinatorsResponse
        """

        all_params = ['instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v2/{project_id}/instances/{instance_id}/management/coordinators',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowCoordinatorsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_groups(self, request):
        """查询消费组信息

        查询消费组信息。

        :param ShowGroupsRequest request
        :return: ShowGroupsResponse
        """
        return self.show_groups_with_http_info(request)

    def show_groups_with_http_info(self, request):
        """查询消费组信息

        查询消费组信息。

        :param ShowGroupsRequest request
        :return: ShowGroupsResponse
        """

        all_params = ['instance_id', 'group']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'group' in local_var_params:
            path_params['group'] = local_var_params['group']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v2/{project_id}/instances/{instance_id}/management/groups/{group}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowGroupsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_instance(self, request):
        """查询指定实例

        查询指定实例的详细信息。

        :param ShowInstanceRequest request
        :return: ShowInstanceResponse
        """
        return self.show_instance_with_http_info(request)

    def show_instance_with_http_info(self, request):
        """查询指定实例

        查询指定实例的详细信息。

        :param ShowInstanceRequest request
        :return: ShowInstanceResponse
        """

        all_params = ['instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v2/{project_id}/instances/{instance_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowInstanceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_instance_extend_product_info(self, request):
        """查询实例的扩容规格列表

        查询实例的扩容规格列表。

        :param ShowInstanceExtendProductInfoRequest request
        :return: ShowInstanceExtendProductInfoResponse
        """
        return self.show_instance_extend_product_info_with_http_info(request)

    def show_instance_extend_product_info_with_http_info(self, request):
        """查询实例的扩容规格列表

        查询实例的扩容规格列表。

        :param ShowInstanceExtendProductInfoRequest request
        :return: ShowInstanceExtendProductInfoResponse
        """

        all_params = ['instance_id', 'type', 'engine']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v2/{project_id}/instances/{instance_id}/extend',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowInstanceExtendProductInfoResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_instance_messages(self, request):
        """查询消息

        查询消息的偏移量和消息内容。 先根据时间戳查询消息的偏移量，再根据偏移量查询消息内容。 **注意：调用接口时message_offset和partition查询参数二选一。**

        :param ShowInstanceMessagesRequest request
        :return: ShowInstanceMessagesResponse
        """
        return self.show_instance_messages_with_http_info(request)

    def show_instance_messages_with_http_info(self, request):
        """查询消息

        查询消息的偏移量和消息内容。 先根据时间戳查询消息的偏移量，再根据偏移量查询消息内容。 **注意：调用接口时message_offset和partition查询参数二选一。**

        :param ShowInstanceMessagesRequest request
        :return: ShowInstanceMessagesResponse
        """

        all_params = ['instance_id', 'topic', 'asc', 'start_time', 'end_time', 'limit', 'offset', 'download', 'message_offset', 'partition']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v2/{project_id}/instances/{instance_id}/messages',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowInstanceMessagesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_instance_topic_detail(self, request):
        """查询Kafka实例Topic详细信息

        查询Kafka实例Topic详细信息。

        :param ShowInstanceTopicDetailRequest request
        :return: ShowInstanceTopicDetailResponse
        """
        return self.show_instance_topic_detail_with_http_info(request)

    def show_instance_topic_detail_with_http_info(self, request):
        """查询Kafka实例Topic详细信息

        查询Kafka实例Topic详细信息。

        :param ShowInstanceTopicDetailRequest request
        :return: ShowInstanceTopicDetailResponse
        """

        all_params = ['instance_id', 'topic']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'topic' in local_var_params:
            path_params['topic'] = local_var_params['topic']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v2/{project_id}/instances/{instance_id}/management/topics/{topic}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowInstanceTopicDetailResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_instance_users(self, request):
        """查询用户列表

        查询用户列表。 Kafka实例开启SASL功能时，才支持多用户管理的功能。

        :param ShowInstanceUsersRequest request
        :return: ShowInstanceUsersResponse
        """
        return self.show_instance_users_with_http_info(request)

    def show_instance_users_with_http_info(self, request):
        """查询用户列表

        查询用户列表。 Kafka实例开启SASL功能时，才支持多用户管理的功能。

        :param ShowInstanceUsersRequest request
        :return: ShowInstanceUsersResponse
        """

        all_params = ['instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v2/{project_id}/instances/{instance_id}/users',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowInstanceUsersResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_kafka_project_tags(self, request):
        """查询项目标签

        查询项目标签。

        :param ShowKafkaProjectTagsRequest request
        :return: ShowKafkaProjectTagsResponse
        """
        return self.show_kafka_project_tags_with_http_info(request)

    def show_kafka_project_tags_with_http_info(self, request):
        """查询项目标签

        查询项目标签。

        :param ShowKafkaProjectTagsRequest request
        :return: ShowKafkaProjectTagsResponse
        """

        all_params = []
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v2/{project_id}/kafka/tags',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowKafkaProjectTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_kafka_tags(self, request):
        """查询实例标签

        查询实例标签。

        :param ShowKafkaTagsRequest request
        :return: ShowKafkaTagsResponse
        """
        return self.show_kafka_tags_with_http_info(request)

    def show_kafka_tags_with_http_info(self, request):
        """查询实例标签

        查询实例标签。

        :param ShowKafkaTagsRequest request
        :return: ShowKafkaTagsResponse
        """

        all_params = ['instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v2/{project_id}/kafka/{instance_id}/tags',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowKafkaTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_kafka_topic_partition_diskusage(self, request):
        """查询topic的磁盘存储情况

        查询topic在Broker上磁盘占用情况。

        :param ShowKafkaTopicPartitionDiskusageRequest request
        :return: ShowKafkaTopicPartitionDiskusageResponse
        """
        return self.show_kafka_topic_partition_diskusage_with_http_info(request)

    def show_kafka_topic_partition_diskusage_with_http_info(self, request):
        """查询topic的磁盘存储情况

        查询topic在Broker上磁盘占用情况。

        :param ShowKafkaTopicPartitionDiskusageRequest request
        :return: ShowKafkaTopicPartitionDiskusageResponse
        """

        all_params = ['instance_id', 'min_size', 'top', 'percentage']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v2/{project_id}/instances/{instance_id}/topics/diskusage',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowKafkaTopicPartitionDiskusageResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_maintain_windows(self, request):
        """查询维护时间窗时间段

        查询维护时间窗开始时间和结束时间。

        :param ShowMaintainWindowsRequest request
        :return: ShowMaintainWindowsResponse
        """
        return self.show_maintain_windows_with_http_info(request)

    def show_maintain_windows_with_http_info(self, request):
        """查询维护时间窗时间段

        查询维护时间窗开始时间和结束时间。

        :param ShowMaintainWindowsRequest request
        :return: ShowMaintainWindowsResponse
        """

        all_params = []
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v2/instances/maintain-windows',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowMaintainWindowsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_messages(self, request):
        """查询分区指定时间段的消息

        查询分区指定时间段的消息。

        :param ShowMessagesRequest request
        :return: ShowMessagesResponse
        """
        return self.show_messages_with_http_info(request)

    def show_messages_with_http_info(self, request):
        """查询分区指定时间段的消息

        查询分区指定时间段的消息。

        :param ShowMessagesRequest request
        :return: ShowMessagesResponse
        """

        all_params = ['instance_id', 'topic', 'start_time', 'end_time', 'limit', 'offset', 'partition']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v2/{project_id}/instances/{instance_id}/management/topics/{topic}/messages',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowMessagesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_partition_beginning_message(self, request):
        """查询分区最早消息的位置

        查询分区最早消息的位置。

        :param ShowPartitionBeginningMessageRequest request
        :return: ShowPartitionBeginningMessageResponse
        """
        return self.show_partition_beginning_message_with_http_info(request)

    def show_partition_beginning_message_with_http_info(self, request):
        """查询分区最早消息的位置

        查询分区最早消息的位置。

        :param ShowPartitionBeginningMessageRequest request
        :return: ShowPartitionBeginningMessageResponse
        """

        all_params = ['instance_id', 'topic', 'partition']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v2/{project_id}/instances/{instance_id}/management/topics/{topic}/partitions/{partition}/beginning-message',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowPartitionBeginningMessageResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_partition_end_message(self, request):
        """查询分区最新消息的位置

        查询分区最新消息的位置。

        :param ShowPartitionEndMessageRequest request
        :return: ShowPartitionEndMessageResponse
        """
        return self.show_partition_end_message_with_http_info(request)

    def show_partition_end_message_with_http_info(self, request):
        """查询分区最新消息的位置

        查询分区最新消息的位置。

        :param ShowPartitionEndMessageRequest request
        :return: ShowPartitionEndMessageResponse
        """

        all_params = ['instance_id', 'topic', 'partition']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v2/{project_id}/instances/{instance_id}/management/topics/{topic}/partitions/{partition}/end-message',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowPartitionEndMessageResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_partition_message(self, request):
        """查询分区指定偏移量的消息

        查询分区指定偏移量的消息。

        :param ShowPartitionMessageRequest request
        :return: ShowPartitionMessageResponse
        """
        return self.show_partition_message_with_http_info(request)

    def show_partition_message_with_http_info(self, request):
        """查询分区指定偏移量的消息

        查询分区指定偏移量的消息。

        :param ShowPartitionMessageRequest request
        :return: ShowPartitionMessageResponse
        """

        all_params = ['instance_id', 'topic', 'partition', 'message_offset']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v2/{project_id}/instances/{instance_id}/management/topics/{topic}/partitions/{partition}/message',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowPartitionMessageResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_sink_task_detail(self, request):
        """查询单个转储任务

        查询单个转储任务。

        :param ShowSinkTaskDetailRequest request
        :return: ShowSinkTaskDetailResponse
        """
        return self.show_sink_task_detail_with_http_info(request)

    def show_sink_task_detail_with_http_info(self, request):
        """查询单个转储任务

        查询单个转储任务。

        :param ShowSinkTaskDetailRequest request
        :return: ShowSinkTaskDetailResponse
        """

        all_params = ['connector_id', 'task_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'connector_id' in local_var_params:
            path_params['connector_id'] = local_var_params['connector_id']
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v2/{project_id}/connectors/{connector_id}/sink-tasks/{task_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowSinkTaskDetailResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_topic_access_policy(self, request):
        """查询用户权限

        查询用户权限。 Kafka实例开启SASL功能时，才支持多用户管理的功能。

        :param ShowTopicAccessPolicyRequest request
        :return: ShowTopicAccessPolicyResponse
        """
        return self.show_topic_access_policy_with_http_info(request)

    def show_topic_access_policy_with_http_info(self, request):
        """查询用户权限

        查询用户权限。 Kafka实例开启SASL功能时，才支持多用户管理的功能。

        :param ShowTopicAccessPolicyRequest request
        :return: ShowTopicAccessPolicyResponse
        """

        all_params = ['instance_id', 'topic_name']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'topic_name' in local_var_params:
            path_params['topic_name'] = local_var_params['topic_name']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v1/{project_id}/instances/{instance_id}/topics/{topic_name}/accesspolicy',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowTopicAccessPolicyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_instance(self, request):
        """修改实例信息

        修改实例的名称和描述信息。

        :param UpdateInstanceRequest request
        :return: UpdateInstanceResponse
        """
        return self.update_instance_with_http_info(request)

    def update_instance_with_http_info(self, request):
        """修改实例信息

        修改实例的名称和描述信息。

        :param UpdateInstanceRequest request
        :return: UpdateInstanceResponse
        """

        all_params = ['instance_id', 'update_instance_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v2/{project_id}/instances/{instance_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateInstanceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_instance_auto_create_topic(self, request):
        """开启或关闭实例自动创建topic功能

        开启或关闭实例自动创建topic功能。

        :param UpdateInstanceAutoCreateTopicRequest request
        :return: UpdateInstanceAutoCreateTopicResponse
        """
        return self.update_instance_auto_create_topic_with_http_info(request)

    def update_instance_auto_create_topic_with_http_info(self, request):
        """开启或关闭实例自动创建topic功能

        开启或关闭实例自动创建topic功能。

        :param UpdateInstanceAutoCreateTopicRequest request
        :return: UpdateInstanceAutoCreateTopicResponse
        """

        all_params = ['instance_id', 'update_instance_auto_create_topic_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v2/{project_id}/instances/{instance_id}/autotopic',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateInstanceAutoCreateTopicResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_instance_cross_vpc_ip(self, request):
        """修改实例跨VPC访问的内网IP

        修改实例跨VPC访问的内网IP。

        :param UpdateInstanceCrossVpcIpRequest request
        :return: UpdateInstanceCrossVpcIpResponse
        """
        return self.update_instance_cross_vpc_ip_with_http_info(request)

    def update_instance_cross_vpc_ip_with_http_info(self, request):
        """修改实例跨VPC访问的内网IP

        修改实例跨VPC访问的内网IP。

        :param UpdateInstanceCrossVpcIpRequest request
        :return: UpdateInstanceCrossVpcIpResponse
        """

        all_params = ['instance_id', 'update_instance_cross_vpc_ip_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v2/{project_id}/instances/{instance_id}/crossvpc/modify',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateInstanceCrossVpcIpResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_instance_topic(self, request):
        """修改Kafka实例Topic

        修改Kafka实例Topic

        :param UpdateInstanceTopicRequest request
        :return: UpdateInstanceTopicResponse
        """
        return self.update_instance_topic_with_http_info(request)

    def update_instance_topic_with_http_info(self, request):
        """修改Kafka实例Topic

        修改Kafka实例Topic

        :param UpdateInstanceTopicRequest request
        :return: UpdateInstanceTopicResponse
        """

        all_params = ['instance_id', 'update_instance_topic_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v2/{project_id}/instances/{instance_id}/topics',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateInstanceTopicResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_sink_task_quota(self, request):
        """修改转储任务的配额

        修改转储任务的配额。

        :param UpdateSinkTaskQuotaRequest request
        :return: UpdateSinkTaskQuotaResponse
        """
        return self.update_sink_task_quota_with_http_info(request)

    def update_sink_task_quota_with_http_info(self, request):
        """修改转储任务的配额

        修改转储任务的配额。

        :param UpdateSinkTaskQuotaRequest request
        :return: UpdateSinkTaskQuotaResponse
        """

        all_params = ['connector_id', 'update_sink_task_quota_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'connector_id' in local_var_params:
            path_params['connector_id'] = local_var_params['connector_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v2/{project_id}/connectors/{connector_id}/sink-tasks',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateSinkTaskQuotaResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_topic_access_policy(self, request):
        """设置用户权限

        设置用户权限。 Kafka实例开启SASL功能时，才支持多用户管理的功能。

        :param UpdateTopicAccessPolicyRequest request
        :return: UpdateTopicAccessPolicyResponse
        """
        return self.update_topic_access_policy_with_http_info(request)

    def update_topic_access_policy_with_http_info(self, request):
        """设置用户权限

        设置用户权限。 Kafka实例开启SASL功能时，才支持多用户管理的功能。

        :param UpdateTopicAccessPolicyRequest request
        :return: UpdateTopicAccessPolicyResponse
        """

        all_params = ['instance_id', 'update_topic_access_policy_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v1/{project_id}/instances/{instance_id}/topics/accesspolicy',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateTopicAccessPolicyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_topic_replica(self, request):
        """修改Kafka实例Topic分区的副本

        修改Kafka实例Topic分区的副本。

        :param UpdateTopicReplicaRequest request
        :return: UpdateTopicReplicaResponse
        """
        return self.update_topic_replica_with_http_info(request)

    def update_topic_replica_with_http_info(self, request):
        """修改Kafka实例Topic分区的副本

        修改Kafka实例Topic分区的副本。

        :param UpdateTopicReplicaRequest request
        :return: UpdateTopicReplicaResponse
        """

        all_params = ['instance_id', 'topic', 'update_topic_replica_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'topic' in local_var_params:
            path_params['topic'] = local_var_params['topic']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v2/{project_id}/instances/{instance_id}/management/topics/{topic}/replicas-reassignment',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateTopicReplicaResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def call_api(self, resource_path, method, path_params=None, query_params=None, header_params=None, body=None,
                 post_params=None, response_type=None, response_headers=None, auth_settings=None,
                 collection_formats=None, request_type=None):
        """Makes the HTTP request and returns deserialized data.

        :param resource_path: Path to method endpoint.
        :param method: Method to call.
        :param path_params: Path parameters in the url.
        :param query_params: Query parameters in the url.
        :param header_params: Header parameters to be placed in the request header.
        :param body: Request body.
        :param post_params dict: Request post form parameters,
            for `application/x-www-form-urlencoded`, `multipart/form-data`.
        :param auth_settings list: Auth Settings names for the request.
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
            response_type=response_type,
            response_headers=response_headers,
            collection_formats=collection_formats,
            request_type=request_type)

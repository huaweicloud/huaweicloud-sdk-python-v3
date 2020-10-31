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


class RabbitMQClient(Client):
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
        super(RabbitMQClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkrabbitmq.v2.model")
        self.preset_headers = {'User-Agent': 'HuaweiCloud-SDK-Python'}

    @staticmethod
    def new_builder(clazz):
        return ClientBuilder(clazz)

    def batch_create_or_delete_instance_tag(self, request):
        """批量添加或删除实例标签

        批量添加或删除实例标签。

        :param BatchCreateOrDeleteInstanceTagRequest request
        :return: BatchCreateOrDeleteInstanceTagResponse
        """
        return self.batch_create_or_delete_instance_tag_with_http_info(request)

    def batch_create_or_delete_instance_tag_with_http_info(self, request):
        """批量添加或删除实例标签

        批量添加或删除实例标签。

        :param BatchCreateOrDeleteInstanceTagRequest request
        :return: BatchCreateOrDeleteInstanceTagResponse
        """

        all_params = ['instance_id', 'batch_create_or_delete_instance_tag_request_body']
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

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/rabbitmq/{instance_id}/tags/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='BatchCreateOrDeleteInstanceTagResponse',
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

        auth_settings = []

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


    def create_post_paid_instance(self, request):
        """创建实例(按需)

        创建实例，该接口创建的实例为按需计费的方式。

        :param CreatePostPaidInstanceRequest request
        :return: CreatePostPaidInstanceResponse
        """
        return self.create_post_paid_instance_with_http_info(request)

    def create_post_paid_instance_with_http_info(self, request):
        """创建实例(按需)

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

        auth_settings = []

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


        auth_settings = []

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


        auth_settings = []

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


        auth_settings = []

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


        auth_settings = []

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


    def list_instances_details(self, request):
        """查询所有实例列表

        查询租户的实例列表，支持按照条件查询。

        :param ListInstancesDetailsRequest request
        :return: ListInstancesDetailsResponse
        """
        return self.list_instances_details_with_http_info(request)

    def list_instances_details_with_http_info(self, request):
        """查询所有实例列表

        查询租户的实例列表，支持按照条件查询。

        :param ListInstancesDetailsRequest request
        :return: ListInstancesDetailsResponse
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


        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/instances',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListInstancesDetailsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_plugins(self, request):
        """查询插件列表

        查询插件列表。

        :param ListPluginsRequest request
        :return: ListPluginsResponse
        """
        return self.list_plugins_with_http_info(request)

    def list_plugins_with_http_info(self, request):
        """查询插件列表

        查询插件列表。

        :param ListPluginsRequest request
        :return: ListPluginsResponse
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


        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/instances/{instance_id}/rabbitmq/plugins',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListPluginsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_products(self, request):
        """查询产品规格列表

        在创建实例时，需要配置订购的产品ID（即product_id），可通过该接口查询产品规格。

        :param ListProductsRequest request
        :return: ListProductsResponse
        """
        return self.list_products_with_http_info(request)

    def list_products_with_http_info(self, request):
        """查询产品规格列表

        在创建实例时，需要配置订购的产品ID（即product_id），可通过该接口查询产品规格。

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


        auth_settings = []

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

        auth_settings = []

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

        auth_settings = []

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


        auth_settings = []

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


    def show_instance(self, request):
        """查询指定实例成功

        查询指定实例的详细信息。

        :param ShowInstanceRequest request
        :return: ShowInstanceResponse
        """
        return self.show_instance_with_http_info(request)

    def show_instance_with_http_info(self, request):
        """查询指定实例成功

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


        auth_settings = []

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
        """查询可扩容规格列表

        查询可扩容规格列表。  RabbtiMQ只支持只增加节点数的扩容方式。

        :param ShowInstanceExtendProductInfoRequest request
        :return: ShowInstanceExtendProductInfoResponse
        """
        return self.show_instance_extend_product_info_with_http_info(request)

    def show_instance_extend_product_info_with_http_info(self, request):
        """查询可扩容规格列表

        查询可扩容规格列表。  RabbtiMQ只支持只增加节点数的扩容方式。

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


        auth_settings = []

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


    def show_instance_tags(self, request):
        """查询实例标签

        查询实例标签。

        :param ShowInstanceTagsRequest request
        :return: ShowInstanceTagsResponse
        """
        return self.show_instance_tags_with_http_info(request)

    def show_instance_tags_with_http_info(self, request):
        """查询实例标签

        查询实例标签。

        :param ShowInstanceTagsRequest request
        :return: ShowInstanceTagsResponse
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


        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/rabbitmq/{instance_id}/tags',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowInstanceTagsResponse',
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


        auth_settings = []

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


    def show_project_tags(self, request):
        """查询项目标签

        查询项目标签。

        :param ShowProjectTagsRequest request
        :return: ShowProjectTagsResponse
        """
        return self.show_project_tags_with_http_info(request)

    def show_project_tags_with_http_info(self, request):
        """查询项目标签

        查询项目标签。

        :param ShowProjectTagsRequest request
        :return: ShowProjectTagsResponse
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


        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/rabbitmq/tags',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowProjectTagsResponse',
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

        auth_settings = []

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


    def update_plugins(self, request):
        """开启或关闭插件

        开启或关闭插件。

        :param UpdatePluginsRequest request
        :return: UpdatePluginsResponse
        """
        return self.update_plugins_with_http_info(request)

    def update_plugins_with_http_info(self, request):
        """开启或关闭插件

        开启或关闭插件。

        :param UpdatePluginsRequest request
        :return: UpdatePluginsResponse
        """

        all_params = ['instance_id', 'update_plugins_request_body']
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

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/instances/{instance_id}/rabbitmq/plugins',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdatePluginsResponse',
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

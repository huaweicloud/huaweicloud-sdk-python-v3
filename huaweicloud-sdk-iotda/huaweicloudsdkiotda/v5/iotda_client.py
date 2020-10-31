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


class IoTDAClient(Client):
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
        super(IoTDAClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkiotda.v5.model")
        self.preset_headers = {'User-Agent': 'HuaweiCloud-SDK-Python'}

    @staticmethod
    def new_builder(clazz):
        return ClientBuilder(clazz)

    def create_access_code(self, request):
        """生成接入凭证

        接入凭证是用于客户端使用AMQP等协议与平台建链的一个认证凭据。只保留一条记录，如果重复调用只会重置接入凭证，使得之前的失效。

        :param CreateAccessCodeRequest request
        :return: CreateAccessCodeResponse
        """
        return self.create_access_code_with_http_info(request)

    def create_access_code_with_http_info(self, request):
        """生成接入凭证

        接入凭证是用于客户端使用AMQP等协议与平台建链的一个认证凭据。只保留一条记录，如果重复调用只会重置接入凭证，使得之前的失效。

        :param CreateAccessCodeRequest request
        :return: CreateAccessCodeResponse
        """

        all_params = ['create_access_code_request_body', 'sp_auth_token', 'stage_auth_token', 'instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'sp_auth_token' in local_var_params:
            header_params['Sp-Auth-Token'] = local_var_params['sp_auth_token']
        if 'stage_auth_token' in local_var_params:
            header_params['Stage-Auth-Token'] = local_var_params['stage_auth_token']
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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
            resource_path='/v5/iot/{project_id}/auth/accesscode',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateAccessCodeResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def add_queue(self, request):
        """创建AMQP队列

        应用服务器可调用此接口在物联网平台创建一个AMQP队列。每个租户只能创建100个队列，若超过规格，则创建失败，若队列名称与已有的队列名称相同，则创建失败。

        :param AddQueueRequest request
        :return: AddQueueResponse
        """
        return self.add_queue_with_http_info(request)

    def add_queue_with_http_info(self, request):
        """创建AMQP队列

        应用服务器可调用此接口在物联网平台创建一个AMQP队列。每个租户只能创建100个队列，若超过规格，则创建失败，若队列名称与已有的队列名称相同，则创建失败。

        :param AddQueueRequest request
        :return: AddQueueResponse
        """

        all_params = ['add_queue_re_quest_body', 'instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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
            resource_path='/v5/iot/{project_id}/amqp-queues',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='AddQueueResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def batch_show_queue(self, request):
        """查询AMQP列表

        应用服务器可调用此接口查询物联网平台中的AMQP队列信息列表。可通过队列名称作模糊查询，支持分页。

        :param BatchShowQueueRequest request
        :return: BatchShowQueueResponse
        """
        return self.batch_show_queue_with_http_info(request)

    def batch_show_queue_with_http_info(self, request):
        """查询AMQP列表

        应用服务器可调用此接口查询物联网平台中的AMQP队列信息列表。可通过队列名称作模糊查询，支持分页。

        :param BatchShowQueueRequest request
        :return: BatchShowQueueResponse
        """

        all_params = ['instance_id', 'queue_name', 'limit', 'marker', 'offset']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'queue_name' in local_var_params:
            query_params.append(('queue_name', local_var_params['queue_name']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v5/iot/{project_id}/amqp-queues',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='BatchShowQueueResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_queue(self, request):
        """删除AMQP队列

        应用服务器可调用此接口在物联网平台上删除指定AMQP队列。若当前队列正在使用，则会删除失败。

        :param DeleteQueueRequest request
        :return: DeleteQueueResponse
        """
        return self.delete_queue_with_http_info(request)

    def delete_queue_with_http_info(self, request):
        """删除AMQP队列

        应用服务器可调用此接口在物联网平台上删除指定AMQP队列。若当前队列正在使用，则会删除失败。

        :param DeleteQueueRequest request
        :return: DeleteQueueResponse
        """

        all_params = ['queue_id', 'instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'queue_id' in local_var_params:
            path_params['queue_id'] = local_var_params['queue_id']

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v5/iot/{project_id}/amqp-queues/{queue_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteQueueResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_queue(self, request):
        """查询单个AMQP队列

        应用服务器可调用此接口查询物联网平台中指定队列的详细信息。

        :param ShowQueueRequest request
        :return: ShowQueueResponse
        """
        return self.show_queue_with_http_info(request)

    def show_queue_with_http_info(self, request):
        """查询单个AMQP队列

        应用服务器可调用此接口查询物联网平台中指定队列的详细信息。

        :param ShowQueueRequest request
        :return: ShowQueueResponse
        """

        all_params = ['queue_id', 'instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'queue_id' in local_var_params:
            path_params['queue_id'] = local_var_params['queue_id']

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v5/iot/{project_id}/amqp-queues/{queue_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowQueueResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def add_application(self, request):
        """创建资源空间

        资源空间对应的是物联网平台原有的应用，在物联网平台的含义与应用一致，只是变更了名称。应用服务器可以调用此接口创建资源空间。

        :param AddApplicationRequest request
        :return: AddApplicationResponse
        """
        return self.add_application_with_http_info(request)

    def add_application_with_http_info(self, request):
        """创建资源空间

        资源空间对应的是物联网平台原有的应用，在物联网平台的含义与应用一致，只是变更了名称。应用服务器可以调用此接口创建资源空间。

        :param AddApplicationRequest request
        :return: AddApplicationResponse
        """

        all_params = ['add_application_request_body', 'instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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
            resource_path='/v5/iot/{project_id}/apps',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='AddApplicationResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_application(self, request):
        """删除资源空间

        删除指定资源空间。删除资源空间属于高危操作，删除资源空间后，该空间下的产品、设备等资源将不可用，同时影响其他引用其下设备资源的服务，请谨慎操作！

        :param DeleteApplicationRequest request
        :return: DeleteApplicationResponse
        """
        return self.delete_application_with_http_info(request)

    def delete_application_with_http_info(self, request):
        """删除资源空间

        删除指定资源空间。删除资源空间属于高危操作，删除资源空间后，该空间下的产品、设备等资源将不可用，同时影响其他引用其下设备资源的服务，请谨慎操作！

        :param DeleteApplicationRequest request
        :return: DeleteApplicationResponse
        """

        all_params = ['app_id', 'instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'app_id' in local_var_params:
            path_params['app_id'] = local_var_params['app_id']

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v5/iot/{project_id}/apps/{app_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteApplicationResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_application(self, request):
        """查询资源空间

        资源空间对应的是物联网平台原有的应用，在物联网平台的含义与应用一致，只是变更了名称。应用服务器可以调用此接口查询指定资源空间详情。

        :param ShowApplicationRequest request
        :return: ShowApplicationResponse
        """
        return self.show_application_with_http_info(request)

    def show_application_with_http_info(self, request):
        """查询资源空间

        资源空间对应的是物联网平台原有的应用，在物联网平台的含义与应用一致，只是变更了名称。应用服务器可以调用此接口查询指定资源空间详情。

        :param ShowApplicationRequest request
        :return: ShowApplicationResponse
        """

        all_params = ['app_id', 'instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'app_id' in local_var_params:
            path_params['app_id'] = local_var_params['app_id']

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v5/iot/{project_id}/apps/{app_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowApplicationResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_applications(self, request):
        """查询资源空间列表

        资源空间对应的是物联网平台原有的应用，在物联网平台的含义与应用一致，只是变更了名称。应用服务器可以调用此接口查询资源空间列表。

        :param ShowApplicationsRequest request
        :return: ShowApplicationsResponse
        """
        return self.show_applications_with_http_info(request)

    def show_applications_with_http_info(self, request):
        """查询资源空间列表

        资源空间对应的是物联网平台原有的应用，在物联网平台的含义与应用一致，只是变更了名称。应用服务器可以调用此接口查询资源空间列表。

        :param ShowApplicationsRequest request
        :return: ShowApplicationsResponse
        """

        all_params = ['instance_id', 'default_app']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'default_app' in local_var_params:
            query_params.append(('default_app', local_var_params['default_app']))

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v5/iot/{project_id}/apps',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowApplicationsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_async_command(self, request):
        """下发异步设备命令

        设备的产品模型中定义了物联网平台可向设备下发的命令，应用服务器可调用此接口向指定设备下发异步命令，以实现对设备的控制。平台负责将命令发送给设备，并将设备执行命令结果异步返回。注意：此接口适用于NB设备异步命令下发，暂不支持其他协议类型设备命令下发。 

        :param CreateAsyncCommandRequest request
        :return: CreateAsyncCommandResponse
        """
        return self.create_async_command_with_http_info(request)

    def create_async_command_with_http_info(self, request):
        """下发异步设备命令

        设备的产品模型中定义了物联网平台可向设备下发的命令，应用服务器可调用此接口向指定设备下发异步命令，以实现对设备的控制。平台负责将命令发送给设备，并将设备执行命令结果异步返回。注意：此接口适用于NB设备异步命令下发，暂不支持其他协议类型设备命令下发。 

        :param CreateAsyncCommandRequest request
        :return: CreateAsyncCommandResponse
        """

        all_params = ['device_id', 'create_async_command_request_body', 'stage_auth_token', 'instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'device_id' in local_var_params:
            path_params['device_id'] = local_var_params['device_id']

        query_params = []

        header_params = {}
        if 'stage_auth_token' in local_var_params:
            header_params['Stage-Auth-Token'] = local_var_params['stage_auth_token']
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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
            resource_path='/v5/iot/{project_id}/devices/{device_id}/async-commands',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateAsyncCommandResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_async_device_command(self, request):
        """查询指定id的命令

        物联网平台可查询指定id的命令。 

        :param ShowAsyncDeviceCommandRequest request
        :return: ShowAsyncDeviceCommandResponse
        """
        return self.show_async_device_command_with_http_info(request)

    def show_async_device_command_with_http_info(self, request):
        """查询指定id的命令

        物联网平台可查询指定id的命令。 

        :param ShowAsyncDeviceCommandRequest request
        :return: ShowAsyncDeviceCommandResponse
        """

        all_params = ['device_id', 'command_id', 'stage_auth_token', 'instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'device_id' in local_var_params:
            path_params['device_id'] = local_var_params['device_id']
        if 'command_id' in local_var_params:
            path_params['command_id'] = local_var_params['command_id']

        query_params = []

        header_params = {}
        if 'stage_auth_token' in local_var_params:
            header_params['Stage-Auth-Token'] = local_var_params['stage_auth_token']
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v5/iot/{project_id}/devices/{device_id}/async-commands/{command_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowAsyncDeviceCommandResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_batch_task(self, request):
        """创建批量任务

        应用服务器可调用此接口为创建批量处理任务，对多个设备进行批量操作。当前支持批量软固件升级、批量创建设备、批量删除设备、批量冻结设备、批量解冻设备。

        :param CreateBatchTaskRequest request
        :return: CreateBatchTaskResponse
        """
        return self.create_batch_task_with_http_info(request)

    def create_batch_task_with_http_info(self, request):
        """创建批量任务

        应用服务器可调用此接口为创建批量处理任务，对多个设备进行批量操作。当前支持批量软固件升级、批量创建设备、批量删除设备、批量冻结设备、批量解冻设备。

        :param CreateBatchTaskRequest request
        :return: CreateBatchTaskResponse
        """

        all_params = ['create_batch_task_request_body', 'instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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
            resource_path='/v5/iot/{project_id}/batchtasks',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateBatchTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_batch_tasks(self, request):
        """查询批量任务列表

        应用服务器可调用此接口查询物联网平台中批量任务列表，每一个任务又包括具体的任务内容、任务状态、任务完成情况统计等。

        :param ListBatchTasksRequest request
        :return: ListBatchTasksResponse
        """
        return self.list_batch_tasks_with_http_info(request)

    def list_batch_tasks_with_http_info(self, request):
        """查询批量任务列表

        应用服务器可调用此接口查询物联网平台中批量任务列表，每一个任务又包括具体的任务内容、任务状态、任务完成情况统计等。

        :param ListBatchTasksRequest request
        :return: ListBatchTasksResponse
        """

        all_params = ['task_type', 'instance_id', 'app_id', 'status', 'limit', 'marker', 'offset']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'app_id' in local_var_params:
            query_params.append(('app_id', local_var_params['app_id']))
        if 'task_type' in local_var_params:
            query_params.append(('task_type', local_var_params['task_type']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v5/iot/{project_id}/batchtasks',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListBatchTasksResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_batch_task(self, request):
        """查询批量任务

        应用服务器可调用此接口查询物联网平台中指定批量任务的信息，包括任务内容、任务状态、任务完成情况统计以及子任务列表等。

        :param ShowBatchTaskRequest request
        :return: ShowBatchTaskResponse
        """
        return self.show_batch_task_with_http_info(request)

    def show_batch_task_with_http_info(self, request):
        """查询批量任务

        应用服务器可调用此接口查询物联网平台中指定批量任务的信息，包括任务内容、任务状态、任务完成情况统计以及子任务列表等。

        :param ShowBatchTaskRequest request
        :return: ShowBatchTaskResponse
        """

        all_params = ['task_id', 'instance_id', 'limit', 'marker', 'offset']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v5/iot/{project_id}/batchtasks/{task_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowBatchTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_batch_task_file(self, request):
        """删除批量任务文件

        应用服务器可调用此接口删除批量任务文件。

        :param DeleteBatchTaskFileRequest request
        :return: DeleteBatchTaskFileResponse
        """
        return self.delete_batch_task_file_with_http_info(request)

    def delete_batch_task_file_with_http_info(self, request):
        """删除批量任务文件

        应用服务器可调用此接口删除批量任务文件。

        :param DeleteBatchTaskFileRequest request
        :return: DeleteBatchTaskFileResponse
        """

        all_params = ['file_id', 'instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'file_id' in local_var_params:
            path_params['file_id'] = local_var_params['file_id']

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v5/iot/{project_id}/batchtask-files/{file_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteBatchTaskFileResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_batch_task_files(self, request):
        """查询批量任务文件列表

        应用服务器可调用此接口查询批量任务文件列表。

        :param ListBatchTaskFilesRequest request
        :return: ListBatchTaskFilesResponse
        """
        return self.list_batch_task_files_with_http_info(request)

    def list_batch_task_files_with_http_info(self, request):
        """查询批量任务文件列表

        应用服务器可调用此接口查询批量任务文件列表。

        :param ListBatchTaskFilesRequest request
        :return: ListBatchTaskFilesResponse
        """

        all_params = ['instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v5/iot/{project_id}/batchtask-files',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListBatchTaskFilesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def add_certificate(self, request):
        """上传设备CA证书

        应用服务器可调用此接口在物联网平台上传设备的CA证书

        :param AddCertificateRequest request
        :return: AddCertificateResponse
        """
        return self.add_certificate_with_http_info(request)

    def add_certificate_with_http_info(self, request):
        """上传设备CA证书

        应用服务器可调用此接口在物联网平台上传设备的CA证书

        :param AddCertificateRequest request
        :return: AddCertificateResponse
        """

        all_params = ['add_certificate_request_body', 'instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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
            resource_path='/v5/iot/{project_id}/certificates',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='AddCertificateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def check_certificate(self, request):
        """验证设备CA证书

        应用服务器可调用此接口在物联网平台验证设备的CA证书，目的是为了验证用户持有设备CA证书的私钥

        :param CheckCertificateRequest request
        :return: CheckCertificateResponse
        """
        return self.check_certificate_with_http_info(request)

    def check_certificate_with_http_info(self, request):
        """验证设备CA证书

        应用服务器可调用此接口在物联网平台验证设备的CA证书，目的是为了验证用户持有设备CA证书的私钥

        :param CheckCertificateRequest request
        :return: CheckCertificateResponse
        """

        all_params = ['certificate_id', 'action_id', 'check_certificate_request_body', 'instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'certificate_id' in local_var_params:
            path_params['certificate_id'] = local_var_params['certificate_id']

        query_params = []
        if 'action_id' in local_var_params:
            query_params.append(('action_id', local_var_params['action_id']))

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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
            resource_path='/v5/iot/{project_id}/certificates/{certificate_id}/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CheckCertificateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_certificate(self, request):
        """删除设备CA证书

        应用服务器可调用此接口在物联网平台删除设备的CA证书

        :param DeleteCertificateRequest request
        :return: DeleteCertificateResponse
        """
        return self.delete_certificate_with_http_info(request)

    def delete_certificate_with_http_info(self, request):
        """删除设备CA证书

        应用服务器可调用此接口在物联网平台删除设备的CA证书

        :param DeleteCertificateRequest request
        :return: DeleteCertificateResponse
        """

        all_params = ['certificate_id', 'instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'certificate_id' in local_var_params:
            path_params['certificate_id'] = local_var_params['certificate_id']

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v5/iot/{project_id}/certificates/{certificate_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteCertificateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_certificates(self, request):
        """获取设备CA证书列表

        应用服务器可调用此接口在物联网平台获取设备的CA证书列表

        :param ListCertificatesRequest request
        :return: ListCertificatesResponse
        """
        return self.list_certificates_with_http_info(request)

    def list_certificates_with_http_info(self, request):
        """获取设备CA证书列表

        应用服务器可调用此接口在物联网平台获取设备的CA证书列表

        :param ListCertificatesRequest request
        :return: ListCertificatesResponse
        """

        all_params = ['instance_id', 'app_id', 'limit', 'marker', 'offset']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'app_id' in local_var_params:
            query_params.append(('app_id', local_var_params['app_id']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v5/iot/{project_id}/certificates',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListCertificatesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_command(self, request):
        """下发设备命令

        设备的产品模型中定义了物联网平台可向设备下发的命令，应用服务器可调用此接口向指定设备下发命令，以实现对设备的同步控制。平台负责将命令以同步方式发送给设备，并将设备执行命令结果同步返回, 如果设备没有响应，平台会返回给应用服务器超时。注意：此接口适用于MQTT设备同步命令下发，暂不支持NB-IoT设备异步命令下发。 

        :param CreateCommandRequest request
        :return: CreateCommandResponse
        """
        return self.create_command_with_http_info(request)

    def create_command_with_http_info(self, request):
        """下发设备命令

        设备的产品模型中定义了物联网平台可向设备下发的命令，应用服务器可调用此接口向指定设备下发命令，以实现对设备的同步控制。平台负责将命令以同步方式发送给设备，并将设备执行命令结果同步返回, 如果设备没有响应，平台会返回给应用服务器超时。注意：此接口适用于MQTT设备同步命令下发，暂不支持NB-IoT设备异步命令下发。 

        :param CreateCommandRequest request
        :return: CreateCommandResponse
        """

        all_params = ['device_id', 'create_command_request_body', 'instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'device_id' in local_var_params:
            path_params['device_id'] = local_var_params['device_id']

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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
            resource_path='/v5/iot/{project_id}/devices/{device_id}/commands',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateCommandResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def add_device_group(self, request):
        """添加设备组

        应用服务器可调用此接口新建设备组，一个华为云账号下最多可有1,000个分组，包括父分组和子分组。设备组的最大层级关系不超过5层，即群组形成的关系树最大深度不超过5。

        :param AddDeviceGroupRequest request
        :return: AddDeviceGroupResponse
        """
        return self.add_device_group_with_http_info(request)

    def add_device_group_with_http_info(self, request):
        """添加设备组

        应用服务器可调用此接口新建设备组，一个华为云账号下最多可有1,000个分组，包括父分组和子分组。设备组的最大层级关系不超过5层，即群组形成的关系树最大深度不超过5。

        :param AddDeviceGroupRequest request
        :return: AddDeviceGroupResponse
        """

        all_params = ['instance_id', 'add_device_group_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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
            resource_path='/v5/iot/{project_id}/device-group',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='AddDeviceGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_or_delete_device_in_group(self, request):
        """管理设备组中的设备

        应用服务器可调用此接口管理设备组中的设备。单个设备组内最多添加20,000个设备，一个设备最多可以被添加到10个设备组中。

        :param CreateOrDeleteDeviceInGroupRequest request
        :return: CreateOrDeleteDeviceInGroupResponse
        """
        return self.create_or_delete_device_in_group_with_http_info(request)

    def create_or_delete_device_in_group_with_http_info(self, request):
        """管理设备组中的设备

        应用服务器可调用此接口管理设备组中的设备。单个设备组内最多添加20,000个设备，一个设备最多可以被添加到10个设备组中。

        :param CreateOrDeleteDeviceInGroupRequest request
        :return: CreateOrDeleteDeviceInGroupResponse
        """

        all_params = ['group_id', 'action_id', 'device_id', 'instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']

        query_params = []
        if 'action_id' in local_var_params:
            query_params.append(('action_id', local_var_params['action_id']))
        if 'device_id' in local_var_params:
            query_params.append(('device_id', local_var_params['device_id']))

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v5/iot/{project_id}/device-group/{group_id}/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateOrDeleteDeviceInGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_device_group(self, request):
        """删除设备组

        应用服务器可调用此接口删除指定设备组，如果该设备组存在子设备组或者该设备组中存在设备，必须先删除子设备组并将设备从该设备组移除，才能删除该设备组。

        :param DeleteDeviceGroupRequest request
        :return: DeleteDeviceGroupResponse
        """
        return self.delete_device_group_with_http_info(request)

    def delete_device_group_with_http_info(self, request):
        """删除设备组

        应用服务器可调用此接口删除指定设备组，如果该设备组存在子设备组或者该设备组中存在设备，必须先删除子设备组并将设备从该设备组移除，才能删除该设备组。

        :param DeleteDeviceGroupRequest request
        :return: DeleteDeviceGroupResponse
        """

        all_params = ['group_id', 'instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v5/iot/{project_id}/device-group/{group_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteDeviceGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_device_groups(self, request):
        """查询设备组列表

        应用服务器可调用此接口查询物联网平台中的设备组信息列表。

        :param ListDeviceGroupsRequest request
        :return: ListDeviceGroupsResponse
        """
        return self.list_device_groups_with_http_info(request)

    def list_device_groups_with_http_info(self, request):
        """查询设备组列表

        应用服务器可调用此接口查询物联网平台中的设备组信息列表。

        :param ListDeviceGroupsRequest request
        :return: ListDeviceGroupsResponse
        """

        all_params = ['instance_id', 'limit', 'marker', 'offset', 'last_modified_time', 'app_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'last_modified_time' in local_var_params:
            query_params.append(('last_modified_time', local_var_params['last_modified_time']))
        if 'app_id' in local_var_params:
            query_params.append(('app_id', local_var_params['app_id']))

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v5/iot/{project_id}/device-group',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListDeviceGroupsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_device_group(self, request):
        """查询设备组

        应用服务器可调用此接口查询指定设备组详情。

        :param ShowDeviceGroupRequest request
        :return: ShowDeviceGroupResponse
        """
        return self.show_device_group_with_http_info(request)

    def show_device_group_with_http_info(self, request):
        """查询设备组

        应用服务器可调用此接口查询指定设备组详情。

        :param ShowDeviceGroupRequest request
        :return: ShowDeviceGroupResponse
        """

        all_params = ['group_id', 'instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v5/iot/{project_id}/device-group/{group_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowDeviceGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_devices_in_group(self, request):
        """查询设备组设备列表

        应用服务器可调用此接口查询指定设备组下的设备列表。

        :param ShowDevicesInGroupRequest request
        :return: ShowDevicesInGroupResponse
        """
        return self.show_devices_in_group_with_http_info(request)

    def show_devices_in_group_with_http_info(self, request):
        """查询设备组设备列表

        应用服务器可调用此接口查询指定设备组下的设备列表。

        :param ShowDevicesInGroupRequest request
        :return: ShowDevicesInGroupResponse
        """

        all_params = ['group_id', 'instance_id', 'limit', 'marker', 'offset']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v5/iot/{project_id}/device-group/{group_id}/devices',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowDevicesInGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_device_group(self, request):
        """修改设备组

        应用服务器可调用此接口修改物联网平台中指定设备组。

        :param UpdateDeviceGroupRequest request
        :return: UpdateDeviceGroupResponse
        """
        return self.update_device_group_with_http_info(request)

    def update_device_group_with_http_info(self, request):
        """修改设备组

        应用服务器可调用此接口修改物联网平台中指定设备组。

        :param UpdateDeviceGroupRequest request
        :return: UpdateDeviceGroupResponse
        """

        all_params = ['group_id', 'update_device_group_request_body', 'instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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
            resource_path='/v5/iot/{project_id}/device-group/{group_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateDeviceGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def add_device(self, request):
        """创建设备

        应用服务器可调用此接口在物联网平台创建一个设备，仅在创建后设备才可以接入物联网平台。  - 该接口支持使用gateway_id参数指定在父设备下创建一个子设备，并且支持多级子设备，当前最大支持二级子设备。 - 该接口同时还支持对设备进行初始配置，接口会读取创建设备请求参数product_id对应的产品详情，如果产品的属性有定义默认值，则会将该属性默认值写入该设备的设备影子中。 - 用户还可以使用创建设备请求参数shadow字段为设备指定初始配置，指定后将会根据service_id和desired设置的属性值与产品中对应属性的默认值比对，如果不同，则将以shadow字段中设置的属性值为准写入到设备影子中。

        :param AddDeviceRequest request
        :return: AddDeviceResponse
        """
        return self.add_device_with_http_info(request)

    def add_device_with_http_info(self, request):
        """创建设备

        应用服务器可调用此接口在物联网平台创建一个设备，仅在创建后设备才可以接入物联网平台。  - 该接口支持使用gateway_id参数指定在父设备下创建一个子设备，并且支持多级子设备，当前最大支持二级子设备。 - 该接口同时还支持对设备进行初始配置，接口会读取创建设备请求参数product_id对应的产品详情，如果产品的属性有定义默认值，则会将该属性默认值写入该设备的设备影子中。 - 用户还可以使用创建设备请求参数shadow字段为设备指定初始配置，指定后将会根据service_id和desired设置的属性值与产品中对应属性的默认值比对，如果不同，则将以shadow字段中设置的属性值为准写入到设备影子中。

        :param AddDeviceRequest request
        :return: AddDeviceResponse
        """

        all_params = ['add_device_request_body', 'instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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
            resource_path='/v5/iot/{project_id}/devices',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='AddDeviceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_device(self, request):
        """删除设备

        应用服务器可调用此接口在物联网平台上删除指定设备。若设备下连接了非直连设备，则必须把设备下的非直连设备都删除后，才能删除该设备。

        :param DeleteDeviceRequest request
        :return: DeleteDeviceResponse
        """
        return self.delete_device_with_http_info(request)

    def delete_device_with_http_info(self, request):
        """删除设备

        应用服务器可调用此接口在物联网平台上删除指定设备。若设备下连接了非直连设备，则必须把设备下的非直连设备都删除后，才能删除该设备。

        :param DeleteDeviceRequest request
        :return: DeleteDeviceResponse
        """

        all_params = ['device_id', 'instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'device_id' in local_var_params:
            path_params['device_id'] = local_var_params['device_id']

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v5/iot/{project_id}/devices/{device_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteDeviceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def freeze_device(self, request):
        """冻结设备

        应用服务器可调用此接口冻结设备，设备冻结后不能再连接上线，可以通过解冻设备接口解除设备冻结。注意，当前仅支持冻结与平台直连的设备。

        :param FreezeDeviceRequest request
        :return: FreezeDeviceResponse
        """
        return self.freeze_device_with_http_info(request)

    def freeze_device_with_http_info(self, request):
        """冻结设备

        应用服务器可调用此接口冻结设备，设备冻结后不能再连接上线，可以通过解冻设备接口解除设备冻结。注意，当前仅支持冻结与平台直连的设备。

        :param FreezeDeviceRequest request
        :return: FreezeDeviceResponse
        """

        all_params = ['device_id', 'instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'device_id' in local_var_params:
            path_params['device_id'] = local_var_params['device_id']

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v5/iot/{project_id}/devices/{device_id}/freeze',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='FreezeDeviceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_devices(self, request):
        """查询设备列表

        应用服务器可调用此接口查询物联网平台中的设备信息列表。

        :param ListDevicesRequest request
        :return: ListDevicesResponse
        """
        return self.list_devices_with_http_info(request)

    def list_devices_with_http_info(self, request):
        """查询设备列表

        应用服务器可调用此接口查询物联网平台中的设备信息列表。

        :param ListDevicesRequest request
        :return: ListDevicesResponse
        """

        all_params = ['instance_id', 'product_id', 'gateway_id', 'is_cascade_query', 'node_id', 'device_name', 'limit', 'marker', 'offset', 'start_time', 'end_time', 'app_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'product_id' in local_var_params:
            query_params.append(('product_id', local_var_params['product_id']))
        if 'gateway_id' in local_var_params:
            query_params.append(('gateway_id', local_var_params['gateway_id']))
        if 'is_cascade_query' in local_var_params:
            query_params.append(('is_cascade_query', local_var_params['is_cascade_query']))
        if 'node_id' in local_var_params:
            query_params.append(('node_id', local_var_params['node_id']))
        if 'device_name' in local_var_params:
            query_params.append(('device_name', local_var_params['device_name']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'app_id' in local_var_params:
            query_params.append(('app_id', local_var_params['app_id']))

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v5/iot/{project_id}/devices',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListDevicesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def reset_device_secret(self, request):
        """重置设备密钥

        应用服务器可调用此接口重置设备密钥，携带指定密钥时平台将设备密钥重置为指定的密钥，不携带密钥时平台将自动生成一个新的随机密钥返回。

        :param ResetDeviceSecretRequest request
        :return: ResetDeviceSecretResponse
        """
        return self.reset_device_secret_with_http_info(request)

    def reset_device_secret_with_http_info(self, request):
        """重置设备密钥

        应用服务器可调用此接口重置设备密钥，携带指定密钥时平台将设备密钥重置为指定的密钥，不携带密钥时平台将自动生成一个新的随机密钥返回。

        :param ResetDeviceSecretRequest request
        :return: ResetDeviceSecretResponse
        """

        all_params = ['device_id', 'action_id', 'reset_device_secret_request_body', 'instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'device_id' in local_var_params:
            path_params['device_id'] = local_var_params['device_id']

        query_params = []
        if 'action_id' in local_var_params:
            query_params.append(('action_id', local_var_params['action_id']))

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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
            resource_path='/v5/iot/{project_id}/devices/{device_id}/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ResetDeviceSecretResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_device(self, request):
        """查询设备

        应用服务器可调用此接口查询物联网平台中指定设备的详细信息。

        :param ShowDeviceRequest request
        :return: ShowDeviceResponse
        """
        return self.show_device_with_http_info(request)

    def show_device_with_http_info(self, request):
        """查询设备

        应用服务器可调用此接口查询物联网平台中指定设备的详细信息。

        :param ShowDeviceRequest request
        :return: ShowDeviceResponse
        """

        all_params = ['device_id', 'instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'device_id' in local_var_params:
            path_params['device_id'] = local_var_params['device_id']

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v5/iot/{project_id}/devices/{device_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowDeviceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def unfreeze_device(self, request):
        """解冻设备

        应用服务器可调用此接口解冻设备，解除冻结后，设备可以连接上线。

        :param UnfreezeDeviceRequest request
        :return: UnfreezeDeviceResponse
        """
        return self.unfreeze_device_with_http_info(request)

    def unfreeze_device_with_http_info(self, request):
        """解冻设备

        应用服务器可调用此接口解冻设备，解除冻结后，设备可以连接上线。

        :param UnfreezeDeviceRequest request
        :return: UnfreezeDeviceResponse
        """

        all_params = ['device_id', 'instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'device_id' in local_var_params:
            path_params['device_id'] = local_var_params['device_id']

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v5/iot/{project_id}/devices/{device_id}/unfreeze',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UnfreezeDeviceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_device(self, request):
        """修改设备

        应用服务器可调用此接口修改物联网平台中指定设备的基本信息。

        :param UpdateDeviceRequest request
        :return: UpdateDeviceResponse
        """
        return self.update_device_with_http_info(request)

    def update_device_with_http_info(self, request):
        """修改设备

        应用服务器可调用此接口修改物联网平台中指定设备的基本信息。

        :param UpdateDeviceRequest request
        :return: UpdateDeviceResponse
        """

        all_params = ['device_id', 'update_device_request_body', 'instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'device_id' in local_var_params:
            path_params['device_id'] = local_var_params['device_id']

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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
            resource_path='/v5/iot/{project_id}/devices/{device_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateDeviceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_device_shadow(self, request):
        """查询设备影子数据

        应用服务器可调用此接口查询指定设备的设备影子信息，包括对设备的期望属性信息（desired区）和设备最新上报的属性信息（reported区）。  设备影子介绍： 设备影子是一个用于存储和检索设备当前状态信息的JSON文档。 - 每个设备有且只有一个设备影子，由设备ID唯一标识 - 设备影子仅保存最近一次设备的上报数据和预期数据 - 无论该设备是否在线，都可以通过该影子获取和设置设备的属性 - 设备上线或者设备上报属性时，如果desired区和reported区存在差异，则将差异部分下发给设备，配置的预期属性需在产品模型中定义且method具有可写属性“W”才可下发 

        :param ShowDeviceShadowRequest request
        :return: ShowDeviceShadowResponse
        """
        return self.show_device_shadow_with_http_info(request)

    def show_device_shadow_with_http_info(self, request):
        """查询设备影子数据

        应用服务器可调用此接口查询指定设备的设备影子信息，包括对设备的期望属性信息（desired区）和设备最新上报的属性信息（reported区）。  设备影子介绍： 设备影子是一个用于存储和检索设备当前状态信息的JSON文档。 - 每个设备有且只有一个设备影子，由设备ID唯一标识 - 设备影子仅保存最近一次设备的上报数据和预期数据 - 无论该设备是否在线，都可以通过该影子获取和设置设备的属性 - 设备上线或者设备上报属性时，如果desired区和reported区存在差异，则将差异部分下发给设备，配置的预期属性需在产品模型中定义且method具有可写属性“W”才可下发 

        :param ShowDeviceShadowRequest request
        :return: ShowDeviceShadowResponse
        """

        all_params = ['device_id', 'instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'device_id' in local_var_params:
            path_params['device_id'] = local_var_params['device_id']

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v5/iot/{project_id}/devices/{device_id}/shadow',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowDeviceShadowResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_device_shadow_desired_data(self, request):
        """配置设备影子预期数据

        应用服务器可调用此接口配置设备影子的预期属性（desired区），当设备上线或者设备上报属性时把属性下发给设备。  设备影子介绍： 设备影子是一个用于存储和检索设备当前状态信息的JSON文档。 - 每个设备有且只有一个设备影子，由设备ID唯一标识 - 设备影子仅保存最近一次设备的上报数据和预期数据 - 无论该设备是否在线，都可以通过该影子获取和设置设备的属性 - 设备上线或者设备上报属性时，如果desired区和reported区存在差异，则将差异部分下发给设备，配置的预期属性需在产品模型中定义且method具有可写属性“W”才可下发 

        :param UpdateDeviceShadowDesiredDataRequest request
        :return: UpdateDeviceShadowDesiredDataResponse
        """
        return self.update_device_shadow_desired_data_with_http_info(request)

    def update_device_shadow_desired_data_with_http_info(self, request):
        """配置设备影子预期数据

        应用服务器可调用此接口配置设备影子的预期属性（desired区），当设备上线或者设备上报属性时把属性下发给设备。  设备影子介绍： 设备影子是一个用于存储和检索设备当前状态信息的JSON文档。 - 每个设备有且只有一个设备影子，由设备ID唯一标识 - 设备影子仅保存最近一次设备的上报数据和预期数据 - 无论该设备是否在线，都可以通过该影子获取和设置设备的属性 - 设备上线或者设备上报属性时，如果desired区和reported区存在差异，则将差异部分下发给设备，配置的预期属性需在产品模型中定义且method具有可写属性“W”才可下发 

        :param UpdateDeviceShadowDesiredDataRequest request
        :return: UpdateDeviceShadowDesiredDataResponse
        """

        all_params = ['device_id', 'update_device_shadow_desired_data_request_body', 'instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'device_id' in local_var_params:
            path_params['device_id'] = local_var_params['device_id']

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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
            resource_path='/v5/iot/{project_id}/devices/{device_id}/shadow',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateDeviceShadowDesiredDataResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_message(self, request):
        """下发设备消息

        物联网平台可向设备下发消息，应用服务器可调用此接口向指定设备下发消息，以实现对设备的控制。应用将消息下发给平台后，平台返回应用响应结果，平台再将消息发送给设备。 

        :param CreateMessageRequest request
        :return: CreateMessageResponse
        """
        return self.create_message_with_http_info(request)

    def create_message_with_http_info(self, request):
        """下发设备消息

        物联网平台可向设备下发消息，应用服务器可调用此接口向指定设备下发消息，以实现对设备的控制。应用将消息下发给平台后，平台返回应用响应结果，平台再将消息发送给设备。 

        :param CreateMessageRequest request
        :return: CreateMessageResponse
        """

        all_params = ['device_id', 'create_message_request_body', 'instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'device_id' in local_var_params:
            path_params['device_id'] = local_var_params['device_id']

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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
            resource_path='/v5/iot/{project_id}/devices/{device_id}/messages',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateMessageResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_device_messages(self, request):
        """查询设备消息

        物联网平台可查询指定设备下的消息，平台为每个设备默认最多保存20条消息，超过20条后， 后续的消息会替换下发最早的消息。 

        :param ListDeviceMessagesRequest request
        :return: ListDeviceMessagesResponse
        """
        return self.list_device_messages_with_http_info(request)

    def list_device_messages_with_http_info(self, request):
        """查询设备消息

        物联网平台可查询指定设备下的消息，平台为每个设备默认最多保存20条消息，超过20条后， 后续的消息会替换下发最早的消息。 

        :param ListDeviceMessagesRequest request
        :return: ListDeviceMessagesResponse
        """

        all_params = ['device_id', 'instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'device_id' in local_var_params:
            path_params['device_id'] = local_var_params['device_id']

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v5/iot/{project_id}/devices/{device_id}/messages',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListDeviceMessagesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_device_message(self, request):
        """查询指定消息id的消息

        物联网平台可查询指定消息id的消息。 

        :param ShowDeviceMessageRequest request
        :return: ShowDeviceMessageResponse
        """
        return self.show_device_message_with_http_info(request)

    def show_device_message_with_http_info(self, request):
        """查询指定消息id的消息

        物联网平台可查询指定消息id的消息。 

        :param ShowDeviceMessageRequest request
        :return: ShowDeviceMessageResponse
        """

        all_params = ['device_id', 'message_id', 'instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'device_id' in local_var_params:
            path_params['device_id'] = local_var_params['device_id']
        if 'message_id' in local_var_params:
            path_params['message_id'] = local_var_params['message_id']

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v5/iot/{project_id}/devices/{device_id}/messages/{message_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowDeviceMessageResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_product(self, request):
        """创建产品

        应用服务器可调用此接口创建产品。

        :param CreateProductRequest request
        :return: CreateProductResponse
        """
        return self.create_product_with_http_info(request)

    def create_product_with_http_info(self, request):
        """创建产品

        应用服务器可调用此接口创建产品。

        :param CreateProductRequest request
        :return: CreateProductResponse
        """

        all_params = ['instance_id', 'create_product_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v5/iot/{project_id}/products',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateProductResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_product(self, request):
        """删除产品

        应用服务器可调用此接口删除已导入物联网平台的指定产品模型。

        :param DeleteProductRequest request
        :return: DeleteProductResponse
        """
        return self.delete_product_with_http_info(request)

    def delete_product_with_http_info(self, request):
        """删除产品

        应用服务器可调用此接口删除已导入物联网平台的指定产品模型。

        :param DeleteProductRequest request
        :return: DeleteProductResponse
        """

        all_params = ['product_id', 'instance_id', 'app_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'product_id' in local_var_params:
            path_params['product_id'] = local_var_params['product_id']

        query_params = []
        if 'app_id' in local_var_params:
            query_params.append(('app_id', local_var_params['app_id']))

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v5/iot/{project_id}/products/{product_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteProductResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_products(self, request):
        """查询产品列表

        应用服务器可调用此接口查询已导入物联网平台的产品模型信息列表，了解产品模型的概要信息。

        :param ListProductsRequest request
        :return: ListProductsResponse
        """
        return self.list_products_with_http_info(request)

    def list_products_with_http_info(self, request):
        """查询产品列表

        应用服务器可调用此接口查询已导入物联网平台的产品模型信息列表，了解产品模型的概要信息。

        :param ListProductsRequest request
        :return: ListProductsResponse
        """

        all_params = ['instance_id', 'limit', 'marker', 'app_id', 'offset']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'app_id' in local_var_params:
            query_params.append(('app_id', local_var_params['app_id']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v5/iot/{project_id}/products',
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


    def show_product(self, request):
        """查询产品

        应用服务器可调用此接口查询已导入物联网平台的指定产品模型详细信息，包括产品模型的服务、属性、命令等。

        :param ShowProductRequest request
        :return: ShowProductResponse
        """
        return self.show_product_with_http_info(request)

    def show_product_with_http_info(self, request):
        """查询产品

        应用服务器可调用此接口查询已导入物联网平台的指定产品模型详细信息，包括产品模型的服务、属性、命令等。

        :param ShowProductRequest request
        :return: ShowProductResponse
        """

        all_params = ['product_id', 'instance_id', 'app_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'product_id' in local_var_params:
            path_params['product_id'] = local_var_params['product_id']

        query_params = []
        if 'app_id' in local_var_params:
            query_params.append(('app_id', local_var_params['app_id']))

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v5/iot/{project_id}/products/{product_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowProductResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_product(self, request):
        """修改产品

        应用服务器可调用此接口修改已导入物联网平台的指定产品模型，包括产品模型的服务、属性、命令等。

        :param UpdateProductRequest request
        :return: UpdateProductResponse
        """
        return self.update_product_with_http_info(request)

    def update_product_with_http_info(self, request):
        """修改产品

        应用服务器可调用此接口修改已导入物联网平台的指定产品模型，包括产品模型的服务、属性、命令等。

        :param UpdateProductRequest request
        :return: UpdateProductResponse
        """

        all_params = ['product_id', 'update_product_request_body', 'instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'product_id' in local_var_params:
            path_params['product_id'] = local_var_params['product_id']

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v5/iot/{project_id}/products/{product_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateProductResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_properties(self, request):
        """查询设备属性

        设备的产品模型中定义了物联网平台可向设备下发的属性，应用服务器可调用此接口查询指定设备下属性。 

        :param ListPropertiesRequest request
        :return: ListPropertiesResponse
        """
        return self.list_properties_with_http_info(request)

    def list_properties_with_http_info(self, request):
        """查询设备属性

        设备的产品模型中定义了物联网平台可向设备下发的属性，应用服务器可调用此接口查询指定设备下属性。 

        :param ListPropertiesRequest request
        :return: ListPropertiesResponse
        """

        all_params = ['device_id', 'service_id', 'instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'device_id' in local_var_params:
            path_params['device_id'] = local_var_params['device_id']

        query_params = []
        if 'service_id' in local_var_params:
            query_params.append(('service_id', local_var_params['service_id']))

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v5/iot/{project_id}/devices/{device_id}/properties',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListPropertiesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_properties(self, request):
        """修改设备属性

        设备的产品模型中定义了物联网平台可向设备下发的属性，应用服务器可调用此接口向指定设备下属性。平台负责将属性以同步方式发送给设备，并将设备执行属性结果同步返回。 

        :param UpdatePropertiesRequest request
        :return: UpdatePropertiesResponse
        """
        return self.update_properties_with_http_info(request)

    def update_properties_with_http_info(self, request):
        """修改设备属性

        设备的产品模型中定义了物联网平台可向设备下发的属性，应用服务器可调用此接口向指定设备下属性。平台负责将属性以同步方式发送给设备，并将设备执行属性结果同步返回。 

        :param UpdatePropertiesRequest request
        :return: UpdatePropertiesResponse
        """

        all_params = ['device_id', 'update_properties_request_body', 'instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'device_id' in local_var_params:
            path_params['device_id'] = local_var_params['device_id']

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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
            resource_path='/v5/iot/{project_id}/devices/{device_id}/properties',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdatePropertiesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_routing_rule(self, request):
        """创建规则触发条件

        应用服务器可调用此接口在物联网平台创建一条规则触发条件。

        :param CreateRoutingRuleRequest request
        :return: CreateRoutingRuleResponse
        """
        return self.create_routing_rule_with_http_info(request)

    def create_routing_rule_with_http_info(self, request):
        """创建规则触发条件

        应用服务器可调用此接口在物联网平台创建一条规则触发条件。

        :param CreateRoutingRuleRequest request
        :return: CreateRoutingRuleResponse
        """

        all_params = ['create_routing_rule_request_body', 'stage_auth_token', 'instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'stage_auth_token' in local_var_params:
            header_params['Stage-Auth-Token'] = local_var_params['stage_auth_token']
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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
            resource_path='/v5/iot/{project_id}/routing-rule/rules',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateRoutingRuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_rule_action(self, request):
        """创建规则动作

        应用服务器可调用此接口在物联网平台创建一条规则动作。

        :param CreateRuleActionRequest request
        :return: CreateRuleActionResponse
        """
        return self.create_rule_action_with_http_info(request)

    def create_rule_action_with_http_info(self, request):
        """创建规则动作

        应用服务器可调用此接口在物联网平台创建一条规则动作。

        :param CreateRuleActionRequest request
        :return: CreateRuleActionResponse
        """

        all_params = ['create_rule_action_request_body', 'stage_auth_token', 'instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'stage_auth_token' in local_var_params:
            header_params['Stage-Auth-Token'] = local_var_params['stage_auth_token']
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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
            resource_path='/v5/iot/{project_id}/routing-rule/actions',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateRuleActionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_routing_rule(self, request):
        """删除规则触发条件

        应用服务器可调用此接口删除物联网平台中的指定规则条件。

        :param DeleteRoutingRuleRequest request
        :return: DeleteRoutingRuleResponse
        """
        return self.delete_routing_rule_with_http_info(request)

    def delete_routing_rule_with_http_info(self, request):
        """删除规则触发条件

        应用服务器可调用此接口删除物联网平台中的指定规则条件。

        :param DeleteRoutingRuleRequest request
        :return: DeleteRoutingRuleResponse
        """

        all_params = ['rule_id', 'stage_auth_token', 'instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'rule_id' in local_var_params:
            path_params['rule_id'] = local_var_params['rule_id']

        query_params = []

        header_params = {}
        if 'stage_auth_token' in local_var_params:
            header_params['Stage-Auth-Token'] = local_var_params['stage_auth_token']
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v5/iot/{project_id}/routing-rule/rules/{rule_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteRoutingRuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_rule_action(self, request):
        """删除规则动作

        应用服务器可调用此接口删除物联网平台中的指定规则动作。

        :param DeleteRuleActionRequest request
        :return: DeleteRuleActionResponse
        """
        return self.delete_rule_action_with_http_info(request)

    def delete_rule_action_with_http_info(self, request):
        """删除规则动作

        应用服务器可调用此接口删除物联网平台中的指定规则动作。

        :param DeleteRuleActionRequest request
        :return: DeleteRuleActionResponse
        """

        all_params = ['action_id', 'stage_auth_token', 'instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'action_id' in local_var_params:
            path_params['action_id'] = local_var_params['action_id']

        query_params = []

        header_params = {}
        if 'stage_auth_token' in local_var_params:
            header_params['Stage-Auth-Token'] = local_var_params['stage_auth_token']
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v5/iot/{project_id}/routing-rule/actions/{action_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteRuleActionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_routing_rules(self, request):
        """查询规则条件列表

        应用服务器可调用此接口查询物联网平台中设置的规则条件列表。

        :param ListRoutingRulesRequest request
        :return: ListRoutingRulesResponse
        """
        return self.list_routing_rules_with_http_info(request)

    def list_routing_rules_with_http_info(self, request):
        """查询规则条件列表

        应用服务器可调用此接口查询物联网平台中设置的规则条件列表。

        :param ListRoutingRulesRequest request
        :return: ListRoutingRulesResponse
        """

        all_params = ['stage_auth_token', 'instance_id', 'resource', 'event', 'app_type', 'app_id', 'rule_name', 'limit', 'marker', 'offset']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'resource' in local_var_params:
            query_params.append(('resource', local_var_params['resource']))
        if 'event' in local_var_params:
            query_params.append(('event', local_var_params['event']))
        if 'app_type' in local_var_params:
            query_params.append(('app_type', local_var_params['app_type']))
        if 'app_id' in local_var_params:
            query_params.append(('app_id', local_var_params['app_id']))
        if 'rule_name' in local_var_params:
            query_params.append(('rule_name', local_var_params['rule_name']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

        header_params = {}
        if 'stage_auth_token' in local_var_params:
            header_params['Stage-Auth-Token'] = local_var_params['stage_auth_token']
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v5/iot/{project_id}/routing-rule/rules',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListRoutingRulesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_rule_actions(self, request):
        """查询规则动作列表

        应用服务器可调用此接口查询物联网平台中设置的规则动作列表。

        :param ListRuleActionsRequest request
        :return: ListRuleActionsResponse
        """
        return self.list_rule_actions_with_http_info(request)

    def list_rule_actions_with_http_info(self, request):
        """查询规则动作列表

        应用服务器可调用此接口查询物联网平台中设置的规则动作列表。

        :param ListRuleActionsRequest request
        :return: ListRuleActionsResponse
        """

        all_params = ['stage_auth_token', 'instance_id', 'rule_id', 'channel', 'app_type', 'app_id', 'limit', 'marker', 'offset']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'rule_id' in local_var_params:
            query_params.append(('rule_id', local_var_params['rule_id']))
        if 'channel' in local_var_params:
            query_params.append(('channel', local_var_params['channel']))
        if 'app_type' in local_var_params:
            query_params.append(('app_type', local_var_params['app_type']))
        if 'app_id' in local_var_params:
            query_params.append(('app_id', local_var_params['app_id']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

        header_params = {}
        if 'stage_auth_token' in local_var_params:
            header_params['Stage-Auth-Token'] = local_var_params['stage_auth_token']
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v5/iot/{project_id}/routing-rule/actions',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListRuleActionsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_routing_rule(self, request):
        """查询规则条件

        应用服务器可调用此接口查询物联网平台中指定规则条件的配置信息。

        :param ShowRoutingRuleRequest request
        :return: ShowRoutingRuleResponse
        """
        return self.show_routing_rule_with_http_info(request)

    def show_routing_rule_with_http_info(self, request):
        """查询规则条件

        应用服务器可调用此接口查询物联网平台中指定规则条件的配置信息。

        :param ShowRoutingRuleRequest request
        :return: ShowRoutingRuleResponse
        """

        all_params = ['rule_id', 'stage_auth_token', 'instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'rule_id' in local_var_params:
            path_params['rule_id'] = local_var_params['rule_id']

        query_params = []

        header_params = {}
        if 'stage_auth_token' in local_var_params:
            header_params['Stage-Auth-Token'] = local_var_params['stage_auth_token']
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v5/iot/{project_id}/routing-rule/rules/{rule_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowRoutingRuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_rule_action(self, request):
        """查询规则动作

        应用服务器可调用此接口查询物联网平台中指定规则动作的配置信息。

        :param ShowRuleActionRequest request
        :return: ShowRuleActionResponse
        """
        return self.show_rule_action_with_http_info(request)

    def show_rule_action_with_http_info(self, request):
        """查询规则动作

        应用服务器可调用此接口查询物联网平台中指定规则动作的配置信息。

        :param ShowRuleActionRequest request
        :return: ShowRuleActionResponse
        """

        all_params = ['action_id', 'stage_auth_token', 'instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'action_id' in local_var_params:
            path_params['action_id'] = local_var_params['action_id']

        query_params = []

        header_params = {}
        if 'stage_auth_token' in local_var_params:
            header_params['Stage-Auth-Token'] = local_var_params['stage_auth_token']
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v5/iot/{project_id}/routing-rule/actions/{action_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowRuleActionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_routing_rule(self, request):
        """修改规则触发条件

        应用服务器可调用此接口修改物联网平台中指定规则条件的配置参数。

        :param UpdateRoutingRuleRequest request
        :return: UpdateRoutingRuleResponse
        """
        return self.update_routing_rule_with_http_info(request)

    def update_routing_rule_with_http_info(self, request):
        """修改规则触发条件

        应用服务器可调用此接口修改物联网平台中指定规则条件的配置参数。

        :param UpdateRoutingRuleRequest request
        :return: UpdateRoutingRuleResponse
        """

        all_params = ['rule_id', 'update_routing_rule_request_body', 'stage_auth_token', 'instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'rule_id' in local_var_params:
            path_params['rule_id'] = local_var_params['rule_id']

        query_params = []

        header_params = {}
        if 'stage_auth_token' in local_var_params:
            header_params['Stage-Auth-Token'] = local_var_params['stage_auth_token']
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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
            resource_path='/v5/iot/{project_id}/routing-rule/rules/{rule_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateRoutingRuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_rule_action(self, request):
        """修改规则动作

        应用服务器可调用此接口修改物联网平台中指定规则动作的配置。

        :param UpdateRuleActionRequest request
        :return: UpdateRuleActionResponse
        """
        return self.update_rule_action_with_http_info(request)

    def update_rule_action_with_http_info(self, request):
        """修改规则动作

        应用服务器可调用此接口修改物联网平台中指定规则动作的配置。

        :param UpdateRuleActionRequest request
        :return: UpdateRuleActionResponse
        """

        all_params = ['action_id', 'update_rule_action_request_body', 'stage_auth_token', 'instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'action_id' in local_var_params:
            path_params['action_id'] = local_var_params['action_id']

        query_params = []

        header_params = {}
        if 'stage_auth_token' in local_var_params:
            header_params['Stage-Auth-Token'] = local_var_params['stage_auth_token']
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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
            resource_path='/v5/iot/{project_id}/routing-rule/actions/{action_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateRuleActionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def change_rule_status(self, request):
        """修改规则状态

        应用服务器可调用此接口修改物联网平台中指定规则的状态，激活或者去激活规则。

        :param ChangeRuleStatusRequest request
        :return: ChangeRuleStatusResponse
        """
        return self.change_rule_status_with_http_info(request)

    def change_rule_status_with_http_info(self, request):
        """修改规则状态

        应用服务器可调用此接口修改物联网平台中指定规则的状态，激活或者去激活规则。

        :param ChangeRuleStatusRequest request
        :return: ChangeRuleStatusResponse
        """

        all_params = ['rule_id', 'change_rule_status_request_body', 'instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'rule_id' in local_var_params:
            path_params['rule_id'] = local_var_params['rule_id']

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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
            resource_path='/v5/iot/{project_id}/rules/{rule_id}/status',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ChangeRuleStatusResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_rule(self, request):
        """创建规则

        应用服务器可调用此接口在物联网平台创建一条规则。

        :param CreateRuleRequest request
        :return: CreateRuleResponse
        """
        return self.create_rule_with_http_info(request)

    def create_rule_with_http_info(self, request):
        """创建规则

        应用服务器可调用此接口在物联网平台创建一条规则。

        :param CreateRuleRequest request
        :return: CreateRuleResponse
        """

        all_params = ['create_rule_request_body', 'instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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
            resource_path='/v5/iot/{project_id}/rules',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateRuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_rule(self, request):
        """删除规则

        应用服务器可调用此接口删除物联网平台中的指定规则。

        :param DeleteRuleRequest request
        :return: DeleteRuleResponse
        """
        return self.delete_rule_with_http_info(request)

    def delete_rule_with_http_info(self, request):
        """删除规则

        应用服务器可调用此接口删除物联网平台中的指定规则。

        :param DeleteRuleRequest request
        :return: DeleteRuleResponse
        """

        all_params = ['rule_id', 'instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'rule_id' in local_var_params:
            path_params['rule_id'] = local_var_params['rule_id']

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v5/iot/{project_id}/rules/{rule_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteRuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_rules(self, request):
        """查询规则列表

        应用服务器可调用此接口查询物联网平台中设置的规则列表。

        :param ListRulesRequest request
        :return: ListRulesResponse
        """
        return self.list_rules_with_http_info(request)

    def list_rules_with_http_info(self, request):
        """查询规则列表

        应用服务器可调用此接口查询物联网平台中设置的规则列表。

        :param ListRulesRequest request
        :return: ListRulesResponse
        """

        all_params = ['instance_id', 'app_id', 'limit', 'marker', 'offset']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'app_id' in local_var_params:
            query_params.append(('app_id', local_var_params['app_id']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v5/iot/{project_id}/rules',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListRulesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_rule(self, request):
        """查询规则

        应用服务器可调用此接口查询物联网平台中指定规则的配置信息。

        :param ShowRuleRequest request
        :return: ShowRuleResponse
        """
        return self.show_rule_with_http_info(request)

    def show_rule_with_http_info(self, request):
        """查询规则

        应用服务器可调用此接口查询物联网平台中指定规则的配置信息。

        :param ShowRuleRequest request
        :return: ShowRuleResponse
        """

        all_params = ['rule_id', 'instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'rule_id' in local_var_params:
            path_params['rule_id'] = local_var_params['rule_id']

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v5/iot/{project_id}/rules/{rule_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowRuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_rule(self, request):
        """修改规则

        应用服务器可调用此接口修改物联网平台中指定规则的配置。

        :param UpdateRuleRequest request
        :return: UpdateRuleResponse
        """
        return self.update_rule_with_http_info(request)

    def update_rule_with_http_info(self, request):
        """修改规则

        应用服务器可调用此接口修改物联网平台中指定规则的配置。

        :param UpdateRuleRequest request
        :return: UpdateRuleResponse
        """

        all_params = ['rule_id', 'update_rule_request_body', 'instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'rule_id' in local_var_params:
            path_params['rule_id'] = local_var_params['rule_id']

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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
            resource_path='/v5/iot/{project_id}/rules/{rule_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateRuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_subscription(self, request):
        """创建订阅

        应用服务器可调用此接口订阅物联网平台资源的变化事件，当资源发生变化时（如设备激活，设备数据更新等），平台会向应用服务器发送通知消息。

        :param CreateSubscriptionRequest request
        :return: CreateSubscriptionResponse
        """
        return self.create_subscription_with_http_info(request)

    def create_subscription_with_http_info(self, request):
        """创建订阅

        应用服务器可调用此接口订阅物联网平台资源的变化事件，当资源发生变化时（如设备激活，设备数据更新等），平台会向应用服务器发送通知消息。

        :param CreateSubscriptionRequest request
        :return: CreateSubscriptionResponse
        """

        all_params = ['instance_id', 'create_subscription_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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
            resource_path='/v5/iot/{project_id}/subscriptions',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateSubscriptionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_subscription(self, request):
        """删除订阅

        应用服务器可调用此接口删除物联网平台中的指定订阅配置。

        :param DeleteSubscriptionRequest request
        :return: DeleteSubscriptionResponse
        """
        return self.delete_subscription_with_http_info(request)

    def delete_subscription_with_http_info(self, request):
        """删除订阅

        应用服务器可调用此接口删除物联网平台中的指定订阅配置。

        :param DeleteSubscriptionRequest request
        :return: DeleteSubscriptionResponse
        """

        all_params = ['subscription_id', 'instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'subscription_id' in local_var_params:
            path_params['subscription_id'] = local_var_params['subscription_id']

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v5/iot/{project_id}/subscriptions/{subscription_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteSubscriptionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_subscriptions(self, request):
        """查询订阅列表

        应用服务器可调用此接口查询物联网平台中的订阅配置信息列表。

        :param ListSubscriptionsRequest request
        :return: ListSubscriptionsResponse
        """
        return self.list_subscriptions_with_http_info(request)

    def list_subscriptions_with_http_info(self, request):
        """查询订阅列表

        应用服务器可调用此接口查询物联网平台中的订阅配置信息列表。

        :param ListSubscriptionsRequest request
        :return: ListSubscriptionsResponse
        """

        all_params = ['instance_id', 'resource', 'event', 'callbackurl', 'app_id', 'channel', 'limit', 'marker', 'offset']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'resource' in local_var_params:
            query_params.append(('resource', local_var_params['resource']))
        if 'event' in local_var_params:
            query_params.append(('event', local_var_params['event']))
        if 'callbackurl' in local_var_params:
            query_params.append(('callbackurl', local_var_params['callbackurl']))
        if 'app_id' in local_var_params:
            query_params.append(('app_id', local_var_params['app_id']))
        if 'channel' in local_var_params:
            query_params.append(('channel', local_var_params['channel']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v5/iot/{project_id}/subscriptions',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListSubscriptionsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_subscription(self, request):
        """查询订阅

        应用服务器可调用此接口查询物联网平台中指定订阅的配置信息。

        :param ShowSubscriptionRequest request
        :return: ShowSubscriptionResponse
        """
        return self.show_subscription_with_http_info(request)

    def show_subscription_with_http_info(self, request):
        """查询订阅

        应用服务器可调用此接口查询物联网平台中指定订阅的配置信息。

        :param ShowSubscriptionRequest request
        :return: ShowSubscriptionResponse
        """

        all_params = ['subscription_id', 'instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'subscription_id' in local_var_params:
            path_params['subscription_id'] = local_var_params['subscription_id']

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v5/iot/{project_id}/subscriptions/{subscription_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowSubscriptionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_subscription(self, request):
        """修改订阅

        应用服务器可调用此接口修改物联网平台中的指定订阅配置，当前仅支持修改订阅回调地址（callbackurl）。

        :param UpdateSubscriptionRequest request
        :return: UpdateSubscriptionResponse
        """
        return self.update_subscription_with_http_info(request)

    def update_subscription_with_http_info(self, request):
        """修改订阅

        应用服务器可调用此接口修改物联网平台中的指定订阅配置，当前仅支持修改订阅回调地址（callbackurl）。

        :param UpdateSubscriptionRequest request
        :return: UpdateSubscriptionResponse
        """

        all_params = ['subscription_id', 'instance_id', 'update_subscription_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'subscription_id' in local_var_params:
            path_params['subscription_id'] = local_var_params['subscription_id']

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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
            resource_path='/v5/iot/{project_id}/subscriptions/{subscription_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateSubscriptionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_resources_by_tags(self, request):
        """按标签查询资源

        应用服务器可调用此接口查询绑定了指定标签的资源。当前支持标签的资源有Device(设备)。

        :param ListResourcesByTagsRequest request
        :return: ListResourcesByTagsResponse
        """
        return self.list_resources_by_tags_with_http_info(request)

    def list_resources_by_tags_with_http_info(self, request):
        """按标签查询资源

        应用服务器可调用此接口查询绑定了指定标签的资源。当前支持标签的资源有Device(设备)。

        :param ListResourcesByTagsRequest request
        :return: ListResourcesByTagsResponse
        """

        all_params = ['instance_id', 'limit', 'marker', 'offset', 'list_resources_by_tags_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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
            resource_path='/v5/iot/{project_id}/tags/query-resources',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListResourcesByTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def tag_device(self, request):
        """绑定标签

        应用服务器可调用此接口为指定资源绑定标签。当前支持标签的资源有Device(设备)。

        :param TagDeviceRequest request
        :return: TagDeviceResponse
        """
        return self.tag_device_with_http_info(request)

    def tag_device_with_http_info(self, request):
        """绑定标签

        应用服务器可调用此接口为指定资源绑定标签。当前支持标签的资源有Device(设备)。

        :param TagDeviceRequest request
        :return: TagDeviceResponse
        """

        all_params = ['instance_id', 'tag_device_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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
            resource_path='/v5/iot/{project_id}/tags/bind-resource',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='TagDeviceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def untag_device(self, request):
        """解绑标签

        应用服务器可调用此接口为指定资源解绑标签。当前支持标签的资源有Device(设备)。

        :param UntagDeviceRequest request
        :return: UntagDeviceResponse
        """
        return self.untag_device_with_http_info(request)

    def untag_device_with_http_info(self, request):
        """解绑标签

        应用服务器可调用此接口为指定资源解绑标签。当前支持标签的资源有Device(设备)。

        :param UntagDeviceRequest request
        :return: UntagDeviceResponse
        """

        all_params = ['instance_id', 'untag_device_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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
            resource_path='/v5/iot/{project_id}/tags/unbind-resource',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UntagDeviceResponse',
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

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


class SmsAsyncClient(Client):
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
        super(SmsAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdksms.v3.model")
        self.preset_headers = {'User-Agent': 'HuaweiCloud-SDK-Python'}

    @classmethod
    def new_builder(cls, clazz=None):
        if clazz is None:
            return ClientBuilder(cls)

        if clazz.__name__ != "SmsClient":
            raise TypeError("client type error, support client type is SmsClient")

        return ClientBuilder(clazz)

    def create_migproject_async(self, request):
        """新建迁移项目

        新建迁移项目

        :param CreateMigprojectRequest request
        :return: CreateMigprojectResponse
        """
        return self.create_migproject_with_http_info(request)

    def create_migproject_with_http_info(self, request):
        """新建迁移项目

        新建迁移项目

        :param CreateMigprojectRequest request
        :return: CreateMigprojectResponse
        """

        all_params = ['create_migproject_request_body']
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
            resource_path='/v3/migprojects',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateMigprojectResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_task_async(self, request):
        """创建迁移任务

        根据源端服务器创建一个迁移任务。

        :param CreateTaskRequest request
        :return: CreateTaskResponse
        """
        return self.create_task_with_http_info(request)

    def create_task_with_http_info(self, request):
        """创建迁移任务

        根据源端服务器创建一个迁移任务。

        :param CreateTaskRequest request
        :return: CreateTaskResponse
        """

        all_params = ['create_task_request_body']
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
            resource_path='/v3/tasks',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_template_async(self, request):
        """新增模板信息

        新增源端模板信息

        :param CreateTemplateRequest request
        :return: CreateTemplateResponse
        """
        return self.create_template_with_http_info(request)

    def create_template_with_http_info(self, request):
        """新增模板信息

        新增源端模板信息

        :param CreateTemplateRequest request
        :return: CreateTemplateResponse
        """

        all_params = ['create_template_request_body']
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
            resource_path='/v3/vm/templates',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateTemplateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_migproject_async(self, request):
        """删除迁移项目

        删除指定ID的迁移项目

        :param DeleteMigprojectRequest request
        :return: DeleteMigprojectResponse
        """
        return self.delete_migproject_with_http_info(request)

    def delete_migproject_with_http_info(self, request):
        """删除迁移项目

        删除指定ID的迁移项目

        :param DeleteMigprojectRequest request
        :return: DeleteMigprojectResponse
        """

        all_params = ['mig_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'mig_project_id' in local_var_params:
            path_params['mig_project_id'] = local_var_params['mig_project_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/migprojects/{mig_project_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteMigprojectResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_server_async(self, request):
        """删除指定ID的源端服务器信息

        从主机迁移服务界面上删除指定ID的源端服务器信息。一旦源端服务器信息被删除，则只能通过重启源端服务器上的迁移Agent来将源端服务器信息重新添加在主机迁移服务界面。

        :param DeleteServerRequest request
        :return: DeleteServerResponse
        """
        return self.delete_server_with_http_info(request)

    def delete_server_with_http_info(self, request):
        """删除指定ID的源端服务器信息

        从主机迁移服务界面上删除指定ID的源端服务器信息。一旦源端服务器信息被删除，则只能通过重启源端服务器上的迁移Agent来将源端服务器信息重新添加在主机迁移服务界面。

        :param DeleteServerRequest request
        :return: DeleteServerResponse
        """

        all_params = ['source_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'source_id' in local_var_params:
            path_params['source_id'] = local_var_params['source_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/sources/{source_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteServerResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_servers_async(self, request):
        """批量删除源端服务器信息

        批量删除源端服务器信息。一旦源端服务器信息被删除，则只能通过重启源端服务器上的迁移Agent来将源端服务器信息重新添加在主机迁移服务界面。

        :param DeleteServersRequest request
        :return: DeleteServersResponse
        """
        return self.delete_servers_with_http_info(request)

    def delete_servers_with_http_info(self, request):
        """批量删除源端服务器信息

        批量删除源端服务器信息。一旦源端服务器信息被删除，则只能通过重启源端服务器上的迁移Agent来将源端服务器信息重新添加在主机迁移服务界面。

        :param DeleteServersRequest request
        :return: DeleteServersResponse
        """

        all_params = ['delete_servers_request_body']
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
            resource_path='/v3/sources/delete',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteServersResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_task_async(self, request):
        """删除指定ID的迁移任务

        删除指定ID的迁移任务。

        :param DeleteTaskRequest request
        :return: DeleteTaskResponse
        """
        return self.delete_task_with_http_info(request)

    def delete_task_with_http_info(self, request):
        """删除指定ID的迁移任务

        删除指定ID的迁移任务。

        :param DeleteTaskRequest request
        :return: DeleteTaskResponse
        """

        all_params = ['task_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
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

        auth_settings = []

        return self.call_api(
            resource_path='/v3/tasks/{task_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_tasks_async(self, request):
        """批量删除迁移任务

        批量删除迁移任务。

        :param DeleteTasksRequest request
        :return: DeleteTasksResponse
        """
        return self.delete_tasks_with_http_info(request)

    def delete_tasks_with_http_info(self, request):
        """批量删除迁移任务

        批量删除迁移任务。

        :param DeleteTasksRequest request
        :return: DeleteTasksResponse
        """

        all_params = ['delete_tasks_request_body']
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
            resource_path='/v3/tasks/delete',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteTasksResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_template_async(self, request):
        """删除指定ID的模板

        删除指定ID的模板。

        :param DeleteTemplateRequest request
        :return: DeleteTemplateResponse
        """
        return self.delete_template_with_http_info(request)

    def delete_template_with_http_info(self, request):
        """删除指定ID的模板

        删除指定ID的模板。

        :param DeleteTemplateRequest request
        :return: DeleteTemplateResponse
        """

        all_params = ['id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/vm/templates/{id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteTemplateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_templates_async(self, request):
        """批量删除指定ID的模板

        批量删除指定ID的模板。

        :param DeleteTemplatesRequest request
        :return: DeleteTemplatesResponse
        """
        return self.delete_templates_with_http_info(request)

    def delete_templates_with_http_info(self, request):
        """批量删除指定ID的模板

        批量删除指定ID的模板。

        :param DeleteTemplatesRequest request
        :return: DeleteTemplatesResponse
        """

        all_params = ['deletetemplates_request_body']
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
            resource_path='/v3/vm/templates/delete',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteTemplatesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_error_servers_async(self, request):
        """查询待迁移源端的所有错误

        主机迁移过程中可能发生错误，使用该接口可以批量查询迁移过程中出现错误的源端服务器信息，以及它们的错误信息。

        :param ListErrorServersRequest request
        :return: ListErrorServersResponse
        """
        return self.list_error_servers_with_http_info(request)

    def list_error_servers_with_http_info(self, request):
        """查询待迁移源端的所有错误

        主机迁移过程中可能发生错误，使用该接口可以批量查询迁移过程中出现错误的源端服务器信息，以及它们的错误信息。

        :param ListErrorServersRequest request
        :return: ListErrorServersResponse
        """

        all_params = ['offset', 'limit', 'migproject', 'enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'migproject' in local_var_params:
            query_params.append(('migproject', local_var_params['migproject']))
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

        auth_settings = []

        return self.call_api(
            resource_path='/v3/errors',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListErrorServersResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_migprojects_async(self, request):
        """获取项目列表

        主机迁移服务中可以使用迁移项目来对源端进行项目管理，使用该接口获取当前账户下所有的迁移项目列表。

        :param ListMigprojectsRequest request
        :return: ListMigprojectsResponse
        """
        return self.list_migprojects_with_http_info(request)

    def list_migprojects_with_http_info(self, request):
        """获取项目列表

        主机迁移服务中可以使用迁移项目来对源端进行项目管理，使用该接口获取当前账户下所有的迁移项目列表。

        :param ListMigprojectsRequest request
        :return: ListMigprojectsResponse
        """

        all_params = ['limit', 'offset']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/migprojects',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListMigprojectsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_servers_async(self, request):
        """查询源端服务器列表

        用户在源端安装并成功启动Agent后，Agent会将源端服务器信息注册在主机迁移服务中，调用该接口查询已注册的源端服务器列表信息。

        :param ListServersRequest request
        :return: ListServersResponse
        """
        return self.list_servers_with_http_info(request)

    def list_servers_with_http_info(self, request):
        """查询源端服务器列表

        用户在源端安装并成功启动Agent后，Agent会将源端服务器信息注册在主机迁移服务中，调用该接口查询已注册的源端服务器列表信息。

        :param ListServersRequest request
        :return: ListServersResponse
        """

        all_params = ['state', 'name', 'id', 'ip', 'migproject', 'limit', 'offset', 'migration_cycle', 'connected', 'enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'state' in local_var_params:
            query_params.append(('state', local_var_params['state']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'ip' in local_var_params:
            query_params.append(('ip', local_var_params['ip']))
        if 'migproject' in local_var_params:
            query_params.append(('migproject', local_var_params['migproject']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'migration_cycle' in local_var_params:
            query_params.append(('migration_cycle', local_var_params['migration_cycle']))
        if 'connected' in local_var_params:
            query_params.append(('connected', local_var_params['connected']))
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

        auth_settings = []

        return self.call_api(
            resource_path='/v3/sources',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListServersResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_tasks_async(self, request):
        """查询迁移任务列表

        在设置目的端后，主机迁移服务会自动创建迁移任务，使用该接口可以查询迁移任务列表。

        :param ListTasksRequest request
        :return: ListTasksResponse
        """
        return self.list_tasks_with_http_info(request)

    def list_tasks_with_http_info(self, request):
        """查询迁移任务列表

        在设置目的端后，主机迁移服务会自动创建迁移任务，使用该接口可以查询迁移任务列表。

        :param ListTasksRequest request
        :return: ListTasksResponse
        """

        all_params = ['state', 'name', 'id', 'source_server_id', 'limit', 'offset', 'enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'state' in local_var_params:
            query_params.append(('state', local_var_params['state']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'source_server_id' in local_var_params:
            query_params.append(('source_server_id', local_var_params['source_server_id']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
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

        auth_settings = []

        return self.call_api(
            resource_path='/v3/tasks',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListTasksResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_templates_async(self, request):
        """查询模板列表

        查询弹性云服务器模板列表，迁移时选择“新建服务器”时可使用该模板创建弹性云服务器。

        :param ListTemplatesRequest request
        :return: ListTemplatesResponse
        """
        return self.list_templates_with_http_info(request)

    def list_templates_with_http_info(self, request):
        """查询模板列表

        查询弹性云服务器模板列表，迁移时选择“新建服务器”时可使用该模板创建弹性云服务器。

        :param ListTemplatesRequest request
        :return: ListTemplatesResponse
        """

        all_params = ['name', 'availability_zone', 'region', 'limit', 'offset']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'availability_zone' in local_var_params:
            query_params.append(('availability_zone', local_var_params['availability_zone']))
        if 'region' in local_var_params:
            query_params.append(('region', local_var_params['region']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/vm/templates',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListTemplatesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def register_server_async(self, request):
        """上报源端服务器基本信息

        上报源端服务器信息，上报成功后会在sms服务器列表中看到对应的源端服务器信息。

        :param RegisterServerRequest request
        :return: RegisterServerResponse
        """
        return self.register_server_with_http_info(request)

    def register_server_with_http_info(self, request):
        """上报源端服务器基本信息

        上报源端服务器信息，上报成功后会在sms服务器列表中看到对应的源端服务器信息。

        :param RegisterServerRequest request
        :return: RegisterServerResponse
        """

        all_params = ['register_server_request_body']
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
            resource_path='/v3/sources',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='RegisterServerResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_command_async(self, request):
        """获取服务端命令

        迁移Agent调用该接口从SMS服务端获取下发给指定源端迁移Agent的命令。

        :param ShowCommandRequest request
        :return: ShowCommandResponse
        """
        return self.show_command_with_http_info(request)

    def show_command_with_http_info(self, request):
        """获取服务端命令

        迁移Agent调用该接口从SMS服务端获取下发给指定源端迁移Agent的命令。

        :param ShowCommandRequest request
        :return: ShowCommandResponse
        """

        all_params = ['server_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'server_id' in local_var_params:
            path_params['server_id'] = local_var_params['server_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/sources/{server_id}/command',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowCommandResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_migproject_async(self, request):
        """查询指定ID迁移项目详情

        查询指定ID的迁移项目详情。

        :param ShowMigprojectRequest request
        :return: ShowMigprojectResponse
        """
        return self.show_migproject_with_http_info(request)

    def show_migproject_with_http_info(self, request):
        """查询指定ID迁移项目详情

        查询指定ID的迁移项目详情。

        :param ShowMigprojectRequest request
        :return: ShowMigprojectResponse
        """

        all_params = ['mig_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'mig_project_id' in local_var_params:
            path_params['mig_project_id'] = local_var_params['mig_project_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/migprojects/{mig_project_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowMigprojectResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_overview_async(self, request):
        """获取服务器总览

        获取服务器总览

        :param ShowOverviewRequest request
        :return: ShowOverviewResponse
        """
        return self.show_overview_with_http_info(request)

    def show_overview_with_http_info(self, request):
        """获取服务器总览

        获取服务器总览

        :param ShowOverviewRequest request
        :return: ShowOverviewResponse
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

        auth_settings = []

        return self.call_api(
            resource_path='/v3/sources/overview',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowOverviewResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_server_async(self, request):
        """查询指定ID的源端服务器

        迁移Agent将源端服务器信息上报到主机迁移服务后，主机迁移服务会对迁移的可行性进行检测，该接口返回源端服务器的基本信息和检查结果。

        :param ShowServerRequest request
        :return: ShowServerResponse
        """
        return self.show_server_with_http_info(request)

    def show_server_with_http_info(self, request):
        """查询指定ID的源端服务器

        迁移Agent将源端服务器信息上报到主机迁移服务后，主机迁移服务会对迁移的可行性进行检测，该接口返回源端服务器的基本信息和检查结果。

        :param ShowServerRequest request
        :return: ShowServerResponse
        """

        all_params = ['source_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'source_id' in local_var_params:
            path_params['source_id'] = local_var_params['source_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/sources/{source_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowServerResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_task_async(self, request):
        """查询指定ID的迁移任务

        查询指定ID的迁移任务。

        :param ShowTaskRequest request
        :return: ShowTaskResponse
        """
        return self.show_task_with_http_info(request)

    def show_task_with_http_info(self, request):
        """查询指定ID的迁移任务

        查询指定ID的迁移任务。

        :param ShowTaskRequest request
        :return: ShowTaskResponse
        """

        all_params = ['task_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
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

        auth_settings = []

        return self.call_api(
            resource_path='/v3/tasks/{task_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_template_async(self, request):
        """查询指定ID模板信息

        查询指定ID的弹性云服务器模板信息。

        :param ShowTemplateRequest request
        :return: ShowTemplateResponse
        """
        return self.show_template_with_http_info(request)

    def show_template_with_http_info(self, request):
        """查询指定ID模板信息

        查询指定ID的弹性云服务器模板信息。

        :param ShowTemplateRequest request
        :return: ShowTemplateResponse
        """

        all_params = ['id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/vm/templates/{id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowTemplateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def shows_speed_limits_async(self, request):
        """查询任务限速规则

        按时间段查询迁移任务的迁移速率

        :param ShowsSpeedLimitsRequest request
        :return: ShowsSpeedLimitsResponse
        """
        return self.shows_speed_limits_with_http_info(request)

    def shows_speed_limits_with_http_info(self, request):
        """查询任务限速规则

        按时间段查询迁移任务的迁移速率

        :param ShowsSpeedLimitsRequest request
        :return: ShowsSpeedLimitsResponse
        """

        all_params = ['task_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
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

        auth_settings = []

        return self.call_api(
            resource_path='/v3/tasks/{task_id}/speed-limit',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowsSpeedLimitsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_command_result_async(self, request):
        """上报服务端命令执行结果

        迁移Agent调用该接口向SMS服务端反馈指定指令的执行结果。

        :param UpdateCommandResultRequest request
        :return: UpdateCommandResultResponse
        """
        return self.update_command_result_with_http_info(request)

    def update_command_result_with_http_info(self, request):
        """上报服务端命令执行结果

        迁移Agent调用该接口向SMS服务端反馈指定指令的执行结果。

        :param UpdateCommandResultRequest request
        :return: UpdateCommandResultResponse
        """

        all_params = ['server_id', 'update_command_result_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'server_id' in local_var_params:
            path_params['server_id'] = local_var_params['server_id']

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
            resource_path='/v3/sources/{server_id}/command_result',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateCommandResultResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_copy_state_async(self, request):
        """更新任务对应源端复制状态

        更新任务对应源端复制状态

        :param UpdateCopyStateRequest request
        :return: UpdateCopyStateResponse
        """
        return self.update_copy_state_with_http_info(request)

    def update_copy_state_with_http_info(self, request):
        """更新任务对应源端复制状态

        更新任务对应源端复制状态

        :param UpdateCopyStateRequest request
        :return: UpdateCopyStateResponse
        """

        all_params = ['source_id', 'update_copy_state_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'source_id' in local_var_params:
            path_params['source_id'] = local_var_params['source_id']

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
            resource_path='/v3/sources/{source_id}/changestate',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateCopyStateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_default_migproject_async(self, request):
        """更新默认迁移项目

        更改默认迁移项目，注册源端会注册在当前的默认项目下。

        :param UpdateDefaultMigprojectRequest request
        :return: UpdateDefaultMigprojectResponse
        """
        return self.update_default_migproject_with_http_info(request)

    def update_default_migproject_with_http_info(self, request):
        """更新默认迁移项目

        更改默认迁移项目，注册源端会注册在当前的默认项目下。

        :param UpdateDefaultMigprojectRequest request
        :return: UpdateDefaultMigprojectResponse
        """

        all_params = ['mig_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'mig_project_id' in local_var_params:
            path_params['mig_project_id'] = local_var_params['mig_project_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/migprojects/{mig_project_id}/default',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateDefaultMigprojectResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_disk_info_async(self, request):
        """更新磁盘信息

        更新服务器的磁盘信息，此接口会把服务器原有磁盘信息清空，然后更新成新磁盘信息

        :param UpdateDiskInfoRequest request
        :return: UpdateDiskInfoResponse
        """
        return self.update_disk_info_with_http_info(request)

    def update_disk_info_with_http_info(self, request):
        """更新磁盘信息

        更新服务器的磁盘信息，此接口会把服务器原有磁盘信息清空，然后更新成新磁盘信息

        :param UpdateDiskInfoRequest request
        :return: UpdateDiskInfoResponse
        """

        all_params = ['source_id', 'update_disk_info_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'source_id' in local_var_params:
            path_params['source_id'] = local_var_params['source_id']

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
            resource_path='/v3/sources/{source_id}/diskinfo',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateDiskInfoResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_migproject_async(self, request):
        """更新迁移项目信息

        更新迁移项目的信息

        :param UpdateMigprojectRequest request
        :return: UpdateMigprojectResponse
        """
        return self.update_migproject_with_http_info(request)

    def update_migproject_with_http_info(self, request):
        """更新迁移项目信息

        更新迁移项目的信息

        :param UpdateMigprojectRequest request
        :return: UpdateMigprojectResponse
        """

        all_params = ['mig_project_id', 'update_migproject_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'mig_project_id' in local_var_params:
            path_params['mig_project_id'] = local_var_params['mig_project_id']

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
            resource_path='/v3/migprojects/{mig_project_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateMigprojectResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_server_name_async(self, request):
        """修改指定ID的源端服务器名称

        该功能用来修改SMS服务端的源端名称，方便用户对源端进行管理。

        :param UpdateServerNameRequest request
        :return: UpdateServerNameResponse
        """
        return self.update_server_name_with_http_info(request)

    def update_server_name_with_http_info(self, request):
        """修改指定ID的源端服务器名称

        该功能用来修改SMS服务端的源端名称，方便用户对源端进行管理。

        :param UpdateServerNameRequest request
        :return: UpdateServerNameResponse
        """

        all_params = ['source_id', 'update_server_name_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'source_id' in local_var_params:
            path_params['source_id'] = local_var_params['source_id']

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
            resource_path='/v3/sources/{source_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateServerNameResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_speed_async(self, request):
        """设置迁移限速规则

        设置迁移任务的迁移速率。

        :param UpdateSpeedRequest request
        :return: UpdateSpeedResponse
        """
        return self.update_speed_with_http_info(request)

    def update_speed_with_http_info(self, request):
        """设置迁移限速规则

        设置迁移任务的迁移速率。

        :param UpdateSpeedRequest request
        :return: UpdateSpeedResponse
        """

        all_params = ['task_id', 'update_speed_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

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
            resource_path='/v3/tasks/{task_id}/speed-limit',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateSpeedResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_task_async(self, request):
        """更新指定ID的迁移任务

        更新指定ID的迁移任务

        :param UpdateTaskRequest request
        :return: UpdateTaskResponse
        """
        return self.update_task_with_http_info(request)

    def update_task_with_http_info(self, request):
        """更新指定ID的迁移任务

        更新指定ID的迁移任务

        :param UpdateTaskRequest request
        :return: UpdateTaskResponse
        """

        all_params = ['task_id', 'update_task_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

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
            resource_path='/v3/tasks/{task_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_task_speed_async(self, request):
        """上报数据迁移进度和速率

        此接口由安装在源端服务器上的迁移Agent在数据迁移阶段调用，用来将迁移的具体进度上报给SMS服务端。   迁移Agent自动调用此接口用于上报数据迁移进度，您无需调用此接口。

        :param UpdateTaskSpeedRequest request
        :return: UpdateTaskSpeedResponse
        """
        return self.update_task_speed_with_http_info(request)

    def update_task_speed_with_http_info(self, request):
        """上报数据迁移进度和速率

        此接口由安装在源端服务器上的迁移Agent在数据迁移阶段调用，用来将迁移的具体进度上报给SMS服务端。   迁移Agent自动调用此接口用于上报数据迁移进度，您无需调用此接口。

        :param UpdateTaskSpeedRequest request
        :return: UpdateTaskSpeedResponse
        """

        all_params = ['task_id', 'update_task_speed_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

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
            resource_path='/v3/tasks/{task_id}/progress',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateTaskSpeedResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_task_status_async(self, request):
        """管理迁移任务

        管理迁移任务，包括启动任务，暂停任务，同步任务，日志上传，回滚失败迁移任务

        :param UpdateTaskStatusRequest request
        :return: UpdateTaskStatusResponse
        """
        return self.update_task_status_with_http_info(request)

    def update_task_status_with_http_info(self, request):
        """管理迁移任务

        管理迁移任务，包括启动任务，暂停任务，同步任务，日志上传，回滚失败迁移任务

        :param UpdateTaskStatusRequest request
        :return: UpdateTaskStatusResponse
        """

        all_params = ['task_id', 'update_task_status_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

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
            resource_path='/v3/tasks/{task_id}/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateTaskStatusResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_template_async(self, request):
        """修改模板信息

        修改源端模板信息。

        :param UpdateTemplateRequest request
        :return: UpdateTemplateResponse
        """
        return self.update_template_with_http_info(request)

    def update_template_with_http_info(self, request):
        """修改模板信息

        修改源端模板信息。

        :param UpdateTemplateRequest request
        :return: UpdateTemplateResponse
        """

        all_params = ['id', 'update_template_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

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
            resource_path='/v3/vm/templates/{id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateTemplateResponse',
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
        :param header_params: Header parameters to be
            placed in the request header.
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
            request_type=request_type,
	    async_request=True)

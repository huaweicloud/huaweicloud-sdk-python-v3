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


class GaussDBClient(Client):
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
        super(GaussDBClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkgaussdb.v3.model")
        self.preset_headers = {'User-Agent': 'HuaweiCloud-SDK-Python'}

    @classmethod
    def new_builder(cls, clazz=None):
        if clazz is None:
            return ClientBuilder(cls)

        if clazz.__name__ != "GaussDBClient":
            raise TypeError("client type error, support client type is GaussDBClient")

        return ClientBuilder(clazz)

    def change_gauss_my_sql_instance_specification(self, request):
        """变更实例规格

        变更数据库实例的规格。

        :param ChangeGaussMySqlInstanceSpecificationRequest request
        :return: ChangeGaussMySqlInstanceSpecificationResponse
        """
        return self.change_gauss_my_sql_instance_specification_with_http_info(request)

    def change_gauss_my_sql_instance_specification_with_http_info(self, request):
        """变更实例规格

        变更数据库实例的规格。

        :param ChangeGaussMySqlInstanceSpecificationRequest request
        :return: ChangeGaussMySqlInstanceSpecificationResponse
        """

        all_params = ['instance_id', 'mysql_change_specification_request', 'x_language']
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
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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
            resource_path='/v3/{project_id}/instances/{instance_id}/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ChangeGaussMySqlInstanceSpecificationResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_gauss_my_sql_backup(self, request):
        """创建手动备份

        创建手动备份

        :param CreateGaussMySqlBackupRequest request
        :return: CreateGaussMySqlBackupResponse
        """
        return self.create_gauss_my_sql_backup_with_http_info(request)

    def create_gauss_my_sql_backup_with_http_info(self, request):
        """创建手动备份

        创建手动备份

        :param CreateGaussMySqlBackupRequest request
        :return: CreateGaussMySqlBackupResponse
        """

        all_params = ['mysql_create_backup_request', 'x_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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
            resource_path='/v3/{project_id}/backups/create',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateGaussMySqlBackupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_gauss_my_sql_instance(self, request):
        """创建数据库实例

        创建云数据库 GaussDB(for MySQL)实例。

        :param CreateGaussMySqlInstanceRequest request
        :return: CreateGaussMySqlInstanceResponse
        """
        return self.create_gauss_my_sql_instance_with_http_info(request)

    def create_gauss_my_sql_instance_with_http_info(self, request):
        """创建数据库实例

        创建云数据库 GaussDB(for MySQL)实例。

        :param CreateGaussMySqlInstanceRequest request
        :return: CreateGaussMySqlInstanceResponse
        """

        all_params = ['create_instance_request', 'x_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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
            resource_path='/v3/{project_id}/instances',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateGaussMySqlInstanceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_gauss_my_sql_proxy(self, request):
        """开启数据库代理

        开启数据库代理，只支持ELB模式。

        :param CreateGaussMySqlProxyRequest request
        :return: CreateGaussMySqlProxyResponse
        """
        return self.create_gauss_my_sql_proxy_with_http_info(request)

    def create_gauss_my_sql_proxy_with_http_info(self, request):
        """开启数据库代理

        开启数据库代理，只支持ELB模式。

        :param CreateGaussMySqlProxyRequest request
        :return: CreateGaussMySqlProxyResponse
        """

        all_params = ['instance_id', 'x_language', 'create_mysql_proxy_request']
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
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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
            resource_path='/v3/{project_id}/instances/{instance_id}/proxy',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateGaussMySqlProxyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_gauss_my_sql_readonly_node(self, request):
        """创建只读节点

        创建只读节点。

        :param CreateGaussMySqlReadonlyNodeRequest request
        :return: CreateGaussMySqlReadonlyNodeResponse
        """
        return self.create_gauss_my_sql_readonly_node_with_http_info(request)

    def create_gauss_my_sql_readonly_node_with_http_info(self, request):
        """创建只读节点

        创建只读节点。

        :param CreateGaussMySqlReadonlyNodeRequest request
        :return: CreateGaussMySqlReadonlyNodeResponse
        """

        all_params = ['instance_id', 'mysql_create_readonly_node_request', 'x_language']
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
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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
            resource_path='/v3/{project_id}/instances/{instance_id}/nodes/enlarge',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateGaussMySqlReadonlyNodeResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_gauss_my_sql_instance(self, request):
        """删除实例

        删除数据库实例，不支持删除包周期实例。

        :param DeleteGaussMySqlInstanceRequest request
        :return: DeleteGaussMySqlInstanceResponse
        """
        return self.delete_gauss_my_sql_instance_with_http_info(request)

    def delete_gauss_my_sql_instance_with_http_info(self, request):
        """删除实例

        删除数据库实例，不支持删除包周期实例。

        :param DeleteGaussMySqlInstanceRequest request
        :return: DeleteGaussMySqlInstanceResponse
        """

        all_params = ['instance_id', 'x_language']
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
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/instances/{instance_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteGaussMySqlInstanceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_gauss_my_sql_proxy(self, request):
        """关闭数据库代理

        关闭数据库代理。

        :param DeleteGaussMySqlProxyRequest request
        :return: DeleteGaussMySqlProxyResponse
        """
        return self.delete_gauss_my_sql_proxy_with_http_info(request)

    def delete_gauss_my_sql_proxy_with_http_info(self, request):
        """关闭数据库代理

        关闭数据库代理。

        :param DeleteGaussMySqlProxyRequest request
        :return: DeleteGaussMySqlProxyResponse
        """

        all_params = ['instance_id', 'x_language']
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
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/instances/{instance_id}/proxy',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteGaussMySqlProxyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_gauss_my_sql_readonly_node(self, request):
        """删除只读节点

        删除实例的只读节点。多可用区模式删除只读节点时，要保证删除后，剩余的只读节点和主节点在不同的可用区中，否则无法删除该只读节点。

        :param DeleteGaussMySqlReadonlyNodeRequest request
        :return: DeleteGaussMySqlReadonlyNodeResponse
        """
        return self.delete_gauss_my_sql_readonly_node_with_http_info(request)

    def delete_gauss_my_sql_readonly_node_with_http_info(self, request):
        """删除只读节点

        删除实例的只读节点。多可用区模式删除只读节点时，要保证删除后，剩余的只读节点和主节点在不同的可用区中，否则无法删除该只读节点。

        :param DeleteGaussMySqlReadonlyNodeRequest request
        :return: DeleteGaussMySqlReadonlyNodeResponse
        """

        all_params = ['instance_id', 'node_id', 'x_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'node_id' in local_var_params:
            path_params['node_id'] = local_var_params['node_id']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/instances/{instance_id}/nodes/{node_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteGaussMySqlReadonlyNodeResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def expand_gauss_my_sql_instance_volume(self, request):
        """包周期存储扩容

        包周期存储扩容

        :param ExpandGaussMySqlInstanceVolumeRequest request
        :return: ExpandGaussMySqlInstanceVolumeResponse
        """
        return self.expand_gauss_my_sql_instance_volume_with_http_info(request)

    def expand_gauss_my_sql_instance_volume_with_http_info(self, request):
        """包周期存储扩容

        包周期存储扩容

        :param ExpandGaussMySqlInstanceVolumeRequest request
        :return: ExpandGaussMySqlInstanceVolumeResponse
        """

        all_params = ['instance_id', 'mysql_extend_instance_volume_request', 'x_language']
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
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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
            resource_path='/v3/{project_id}/instances/{instance_id}/volume/extend',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ExpandGaussMySqlInstanceVolumeResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def expand_gauss_my_sql_proxy(self, request):
        """扩容数据库代理节点的数量

        扩容数据库代理节点的数量。 DeC专属云账号暂不支持数据库代理。

        :param ExpandGaussMySqlProxyRequest request
        :return: ExpandGaussMySqlProxyResponse
        """
        return self.expand_gauss_my_sql_proxy_with_http_info(request)

    def expand_gauss_my_sql_proxy_with_http_info(self, request):
        """扩容数据库代理节点的数量

        扩容数据库代理节点的数量。 DeC专属云账号暂不支持数据库代理。

        :param ExpandGaussMySqlProxyRequest request
        :return: ExpandGaussMySqlProxyResponse
        """

        all_params = ['instance_id', 'enlarge_proxy_request', 'x_language']
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
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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
            resource_path='/v3/{project_id}/instances/{instance_id}/proxy/enlarge',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ExpandGaussMySqlProxyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_gauss_my_sql_configurations(self, request):
        """查询参数模板

        获取参数模板列表，包括所有数据库的默认参数模板和用户创建的参数模板。

        :param ListGaussMySqlConfigurationsRequest request
        :return: ListGaussMySqlConfigurationsResponse
        """
        return self.list_gauss_my_sql_configurations_with_http_info(request)

    def list_gauss_my_sql_configurations_with_http_info(self, request):
        """查询参数模板

        获取参数模板列表，包括所有数据库的默认参数模板和用户创建的参数模板。

        :param ListGaussMySqlConfigurationsRequest request
        :return: ListGaussMySqlConfigurationsResponse
        """

        all_params = ['x_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/configurations',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListGaussMySqlConfigurationsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_gauss_my_sql_dedicated_resources(self, request):
        """查询专属资源池列表

        获取专属资源池列表，包括用户开通的所有专属资源池信息。

        :param ListGaussMySqlDedicatedResourcesRequest request
        :return: ListGaussMySqlDedicatedResourcesResponse
        """
        return self.list_gauss_my_sql_dedicated_resources_with_http_info(request)

    def list_gauss_my_sql_dedicated_resources_with_http_info(self, request):
        """查询专属资源池列表

        获取专属资源池列表，包括用户开通的所有专属资源池信息。

        :param ListGaussMySqlDedicatedResourcesRequest request
        :return: ListGaussMySqlDedicatedResourcesResponse
        """

        all_params = ['x_language', 'offset', 'limit']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/dedicated-resources',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListGaussMySqlDedicatedResourcesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_gauss_my_sql_error_log(self, request):
        """查询数据库错误日志

        查询数据库错误日志。

        :param ListGaussMySqlErrorLogRequest request
        :return: ListGaussMySqlErrorLogResponse
        """
        return self.list_gauss_my_sql_error_log_with_http_info(request)

    def list_gauss_my_sql_error_log_with_http_info(self, request):
        """查询数据库错误日志

        查询数据库错误日志。

        :param ListGaussMySqlErrorLogRequest request
        :return: ListGaussMySqlErrorLogResponse
        """

        all_params = ['instance_id', 'start_date', 'end_date', 'x_language', 'offset', 'limit', 'level', 'node_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'start_date' in local_var_params:
            query_params.append(('start_date', local_var_params['start_date']))
        if 'end_date' in local_var_params:
            query_params.append(('end_date', local_var_params['end_date']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'level' in local_var_params:
            query_params.append(('level', local_var_params['level']))
        if 'node_id' in local_var_params:
            query_params.append(('node_id', local_var_params['node_id']))

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/instances/{instance_id}/errorlog',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListGaussMySqlErrorLogResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_gauss_my_sql_instances(self, request):
        """查询实例列表

        根据指定条件查询实例列表。

        :param ListGaussMySqlInstancesRequest request
        :return: ListGaussMySqlInstancesResponse
        """
        return self.list_gauss_my_sql_instances_with_http_info(request)

    def list_gauss_my_sql_instances_with_http_info(self, request):
        """查询实例列表

        根据指定条件查询实例列表。

        :param ListGaussMySqlInstancesRequest request
        :return: ListGaussMySqlInstancesResponse
        """

        all_params = ['x_language', 'id', 'name', 'type', 'datastore_type', 'vpc_id', 'subnet_id', 'offset', 'limit']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'datastore_type' in local_var_params:
            query_params.append(('datastore_type', local_var_params['datastore_type']))
        if 'vpc_id' in local_var_params:
            query_params.append(('vpc_id', local_var_params['vpc_id']))
        if 'subnet_id' in local_var_params:
            query_params.append(('subnet_id', local_var_params['subnet_id']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/instances',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListGaussMySqlInstancesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_gauss_my_sql_slow_log(self, request):
        """查询数据库慢日志

        查询数据库慢日志

        :param ListGaussMySqlSlowLogRequest request
        :return: ListGaussMySqlSlowLogResponse
        """
        return self.list_gauss_my_sql_slow_log_with_http_info(request)

    def list_gauss_my_sql_slow_log_with_http_info(self, request):
        """查询数据库慢日志

        查询数据库慢日志

        :param ListGaussMySqlSlowLogRequest request
        :return: ListGaussMySqlSlowLogResponse
        """

        all_params = ['instance_id', 'start_date', 'end_date', 'node_id', 'x_language', 'offset', 'limit', 'type']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'start_date' in local_var_params:
            query_params.append(('start_date', local_var_params['start_date']))
        if 'end_date' in local_var_params:
            query_params.append(('end_date', local_var_params['end_date']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'node_id' in local_var_params:
            query_params.append(('node_id', local_var_params['node_id']))

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/instances/{instance_id}/slowlog',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListGaussMySqlSlowLogResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def reset_gauss_my_sql_password(self, request):
        """重置数据库密码

        重置数据库密码

        :param ResetGaussMySqlPasswordRequest request
        :return: ResetGaussMySqlPasswordResponse
        """
        return self.reset_gauss_my_sql_password_with_http_info(request)

    def reset_gauss_my_sql_password_with_http_info(self, request):
        """重置数据库密码

        重置数据库密码

        :param ResetGaussMySqlPasswordRequest request
        :return: ResetGaussMySqlPasswordResponse
        """

        all_params = ['instance_id', 'mysql_reset_password_request', 'x_language']
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
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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
            resource_path='/v3/{project_id}/instances/{instance_id}/password',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ResetGaussMySqlPasswordResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def set_gauss_my_sql_quotas(self, request):
        """设置租户基于企业项目的资源配额

        设置指定企业项目的资源配额。

        :param SetGaussMySqlQuotasRequest request
        :return: SetGaussMySqlQuotasResponse
        """
        return self.set_gauss_my_sql_quotas_with_http_info(request)

    def set_gauss_my_sql_quotas_with_http_info(self, request):
        """设置租户基于企业项目的资源配额

        设置指定企业项目的资源配额。

        :param SetGaussMySqlQuotasRequest request
        :return: SetGaussMySqlQuotasResponse
        """

        all_params = ['x_language', 'set_quotas_request']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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
            resource_path='/v3/{project_id}/quotas',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='SetGaussMySqlQuotasResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_gauss_my_sql_backup_list(self, request):
        """查询备份列表

        查询备份列表

        :param ShowGaussMySqlBackupListRequest request
        :return: ShowGaussMySqlBackupListResponse
        """
        return self.show_gauss_my_sql_backup_list_with_http_info(request)

    def show_gauss_my_sql_backup_list_with_http_info(self, request):
        """查询备份列表

        查询备份列表

        :param ShowGaussMySqlBackupListRequest request
        :return: ShowGaussMySqlBackupListResponse
        """

        all_params = ['x_language', 'instance_id', 'backup_id', 'backup_type', 'offset', 'limit', 'begin_time', 'end_time']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'instance_id' in local_var_params:
            query_params.append(('instance_id', local_var_params['instance_id']))
        if 'backup_id' in local_var_params:
            query_params.append(('backup_id', local_var_params['backup_id']))
        if 'backup_type' in local_var_params:
            query_params.append(('backup_type', local_var_params['backup_type']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'begin_time' in local_var_params:
            query_params.append(('begin_time', local_var_params['begin_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/backups',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowGaussMySqlBackupListResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_gauss_my_sql_backup_policy(self, request):
        """查询自动备份策略

        查询自动备份策略。

        :param ShowGaussMySqlBackupPolicyRequest request
        :return: ShowGaussMySqlBackupPolicyResponse
        """
        return self.show_gauss_my_sql_backup_policy_with_http_info(request)

    def show_gauss_my_sql_backup_policy_with_http_info(self, request):
        """查询自动备份策略

        查询自动备份策略。

        :param ShowGaussMySqlBackupPolicyRequest request
        :return: ShowGaussMySqlBackupPolicyResponse
        """

        all_params = ['instance_id', 'x_language']
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
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/instances/{instance_id}/backups/policy',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowGaussMySqlBackupPolicyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_gauss_my_sql_engine_version(self, request):
        """查询数据库引擎的版本

        获取指定数据库引擎对应的数据库版本信息。

        :param ShowGaussMySqlEngineVersionRequest request
        :return: ShowGaussMySqlEngineVersionResponse
        """
        return self.show_gauss_my_sql_engine_version_with_http_info(request)

    def show_gauss_my_sql_engine_version_with_http_info(self, request):
        """查询数据库引擎的版本

        获取指定数据库引擎对应的数据库版本信息。

        :param ShowGaussMySqlEngineVersionRequest request
        :return: ShowGaussMySqlEngineVersionResponse
        """

        all_params = ['database_name', 'x_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'database_name' in local_var_params:
            path_params['database_name'] = local_var_params['database_name']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/datastores/{database_name}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowGaussMySqlEngineVersionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_gauss_my_sql_flavors(self, request):
        """查询数据库规格

        获取指定数据库引擎版本对应的规格信息。

        :param ShowGaussMySqlFlavorsRequest request
        :return: ShowGaussMySqlFlavorsResponse
        """
        return self.show_gauss_my_sql_flavors_with_http_info(request)

    def show_gauss_my_sql_flavors_with_http_info(self, request):
        """查询数据库规格

        获取指定数据库引擎版本对应的规格信息。

        :param ShowGaussMySqlFlavorsRequest request
        :return: ShowGaussMySqlFlavorsResponse
        """

        all_params = ['database_name', 'availability_zone_mode', 'x_language', 'version_name', 'spec_code']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'database_name' in local_var_params:
            path_params['database_name'] = local_var_params['database_name']

        query_params = []
        if 'version_name' in local_var_params:
            query_params.append(('version_name', local_var_params['version_name']))
        if 'availability_zone_mode' in local_var_params:
            query_params.append(('availability_zone_mode', local_var_params['availability_zone_mode']))
        if 'spec_code' in local_var_params:
            query_params.append(('spec_code', local_var_params['spec_code']))

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/flavors/{database_name}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowGaussMySqlFlavorsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_gauss_my_sql_instance_info(self, request):
        """查询实例详情信息

        查询实例详情信息

        :param ShowGaussMySqlInstanceInfoRequest request
        :return: ShowGaussMySqlInstanceInfoResponse
        """
        return self.show_gauss_my_sql_instance_info_with_http_info(request)

    def show_gauss_my_sql_instance_info_with_http_info(self, request):
        """查询实例详情信息

        查询实例详情信息

        :param ShowGaussMySqlInstanceInfoRequest request
        :return: ShowGaussMySqlInstanceInfoResponse
        """

        all_params = ['instance_id', 'x_language']
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
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/instances/{instance_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowGaussMySqlInstanceInfoResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_gauss_my_sql_job_info(self, request):
        """获取指定ID的任务信息

        获取指定ID的任务信息。

        :param ShowGaussMySqlJobInfoRequest request
        :return: ShowGaussMySqlJobInfoResponse
        """
        return self.show_gauss_my_sql_job_info_with_http_info(request)

    def show_gauss_my_sql_job_info_with_http_info(self, request):
        """获取指定ID的任务信息

        获取指定ID的任务信息。

        :param ShowGaussMySqlJobInfoRequest request
        :return: ShowGaussMySqlJobInfoResponse
        """

        all_params = ['id', 'x_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/jobs',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowGaussMySqlJobInfoResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_gauss_my_sql_project_quotas(self, request):
        """查询租户的实例配额

        获取指定租户的资源配额。

        :param ShowGaussMySqlProjectQuotasRequest request
        :return: ShowGaussMySqlProjectQuotasResponse
        """
        return self.show_gauss_my_sql_project_quotas_with_http_info(request)

    def show_gauss_my_sql_project_quotas_with_http_info(self, request):
        """查询租户的实例配额

        获取指定租户的资源配额。

        :param ShowGaussMySqlProjectQuotasRequest request
        :return: ShowGaussMySqlProjectQuotasResponse
        """

        all_params = ['x_language', 'type']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/project-quotas',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowGaussMySqlProjectQuotasResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_gauss_my_sql_proxy(self, request):
        """查询数据库代理信息

        查询数据库代理信息。

        :param ShowGaussMySqlProxyRequest request
        :return: ShowGaussMySqlProxyResponse
        """
        return self.show_gauss_my_sql_proxy_with_http_info(request)

    def show_gauss_my_sql_proxy_with_http_info(self, request):
        """查询数据库代理信息

        查询数据库代理信息。

        :param ShowGaussMySqlProxyRequest request
        :return: ShowGaussMySqlProxyResponse
        """

        all_params = ['instance_id', 'x_language']
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
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/instances/{instance_id}/proxy',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowGaussMySqlProxyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_gauss_my_sql_proxy_flavors(self, request):
        """查询数据库代理规格信息

        查询数据库代理规格信息。

        :param ShowGaussMySqlProxyFlavorsRequest request
        :return: ShowGaussMySqlProxyFlavorsResponse
        """
        return self.show_gauss_my_sql_proxy_flavors_with_http_info(request)

    def show_gauss_my_sql_proxy_flavors_with_http_info(self, request):
        """查询数据库代理规格信息

        查询数据库代理规格信息。

        :param ShowGaussMySqlProxyFlavorsRequest request
        :return: ShowGaussMySqlProxyFlavorsResponse
        """

        all_params = ['instance_id', 'x_language']
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
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/instances/{instance_id}/proxy/flavors',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowGaussMySqlProxyFlavorsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_gauss_my_sql_quotas(self, request):
        """查询租户基于企业项目的资源配额

        获取指定企业项目的资源配额。

        :param ShowGaussMySqlQuotasRequest request
        :return: ShowGaussMySqlQuotasResponse
        """
        return self.show_gauss_my_sql_quotas_with_http_info(request)

    def show_gauss_my_sql_quotas_with_http_info(self, request):
        """查询租户基于企业项目的资源配额

        获取指定企业项目的资源配额。

        :param ShowGaussMySqlQuotasRequest request
        :return: ShowGaussMySqlQuotasResponse
        """

        all_params = ['x_language', 'offset', 'limit', 'enterprise_project_name']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'enterprise_project_name' in local_var_params:
            query_params.append(('enterprise_project_name', local_var_params['enterprise_project_name']))

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/quotas',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowGaussMySqlQuotasResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_gauss_my_sql_backup_policy(self, request):
        """修改备份策略

        修改备份策略

        :param UpdateGaussMySqlBackupPolicyRequest request
        :return: UpdateGaussMySqlBackupPolicyResponse
        """
        return self.update_gauss_my_sql_backup_policy_with_http_info(request)

    def update_gauss_my_sql_backup_policy_with_http_info(self, request):
        """修改备份策略

        修改备份策略

        :param UpdateGaussMySqlBackupPolicyRequest request
        :return: UpdateGaussMySqlBackupPolicyResponse
        """

        all_params = ['instance_id', 'mysql_update_backup_policy_request', 'x_language']
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
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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
            resource_path='/v3/{project_id}/instances/{instance_id}/backups/policy/update',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateGaussMySqlBackupPolicyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_gauss_my_sql_instance_name(self, request):
        """修改实例名称

        修改实例名称

        :param UpdateGaussMySqlInstanceNameRequest request
        :return: UpdateGaussMySqlInstanceNameResponse
        """
        return self.update_gauss_my_sql_instance_name_with_http_info(request)

    def update_gauss_my_sql_instance_name_with_http_info(self, request):
        """修改实例名称

        修改实例名称

        :param UpdateGaussMySqlInstanceNameRequest request
        :return: UpdateGaussMySqlInstanceNameResponse
        """

        all_params = ['instance_id', 'mysql_update_instance_name_request', 'x_language']
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
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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
            resource_path='/v3/{project_id}/instances/{instance_id}/name',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateGaussMySqlInstanceNameResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_gauss_my_sql_quotas(self, request):
        """修改租户基于企业项目的资源配额

        修改指定企业项目的资源配额。

        :param UpdateGaussMySqlQuotasRequest request
        :return: UpdateGaussMySqlQuotasResponse
        """
        return self.update_gauss_my_sql_quotas_with_http_info(request)

    def update_gauss_my_sql_quotas_with_http_info(self, request):
        """修改租户基于企业项目的资源配额

        修改指定企业项目的资源配额。

        :param UpdateGaussMySqlQuotasRequest request
        :return: UpdateGaussMySqlQuotasResponse
        """

        all_params = ['x_language', 'set_quotas_request']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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
            resource_path='/v3/{project_id}/quotas',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateGaussMySqlQuotasResponse',
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

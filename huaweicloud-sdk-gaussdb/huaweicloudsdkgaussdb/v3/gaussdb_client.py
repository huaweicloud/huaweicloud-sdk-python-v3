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

    def change_mysql_instance_specification(self, request):
        """变更实例规格

        变更数据库实例的规格。

        :param ChangeMysqlInstanceSpecificationRequest request
        :return: ChangeMysqlInstanceSpecificationResponse
        """
        return self.change_mysql_instance_specification_with_http_info(request)

    def change_mysql_instance_specification_with_http_info(self, request):
        """变更实例规格

        变更数据库实例的规格。

        :param ChangeMysqlInstanceSpecificationRequest request
        :return: ChangeMysqlInstanceSpecificationResponse
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
            resource_path='/mysql/v3/{project_id}/instances/{instance_id}/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ChangeMysqlInstanceSpecificationResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_mysql_backup(self, request):
        """创建手动备份

        创建手动备份

        :param CreateMysqlBackupRequest request
        :return: CreateMysqlBackupResponse
        """
        return self.create_mysql_backup_with_http_info(request)

    def create_mysql_backup_with_http_info(self, request):
        """创建手动备份

        创建手动备份

        :param CreateMysqlBackupRequest request
        :return: CreateMysqlBackupResponse
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
            resource_path='/mysql/v3/{project_id}/backups/create',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateMysqlBackupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_mysql_instance(self, request):
        """创建数据库实例

        创建云数据库 GaussDB(for MySQL)实例。

        :param CreateMysqlInstanceRequest request
        :return: CreateMysqlInstanceResponse
        """
        return self.create_mysql_instance_with_http_info(request)

    def create_mysql_instance_with_http_info(self, request):
        """创建数据库实例

        创建云数据库 GaussDB(for MySQL)实例。

        :param CreateMysqlInstanceRequest request
        :return: CreateMysqlInstanceResponse
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
            resource_path='/mysql/v3/{project_id}/instances',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateMysqlInstanceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_mysql_proxy(self, request):
        """开启数据库代理

        开启数据库代理，只支持ELB模式。

        :param CreateMysqlProxyRequest request
        :return: CreateMysqlProxyResponse
        """
        return self.create_mysql_proxy_with_http_info(request)

    def create_mysql_proxy_with_http_info(self, request):
        """开启数据库代理

        开启数据库代理，只支持ELB模式。

        :param CreateMysqlProxyRequest request
        :return: CreateMysqlProxyResponse
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
            resource_path='/mysql/v3/{project_id}/instances/{instance_id}/proxy',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateMysqlProxyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_mysql_readonly_node(self, request):
        """创建只读节点

        创建只读节点。

        :param CreateMysqlReadonlyNodeRequest request
        :return: CreateMysqlReadonlyNodeResponse
        """
        return self.create_mysql_readonly_node_with_http_info(request)

    def create_mysql_readonly_node_with_http_info(self, request):
        """创建只读节点

        创建只读节点。

        :param CreateMysqlReadonlyNodeRequest request
        :return: CreateMysqlReadonlyNodeResponse
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
            resource_path='/mysql/v3/{project_id}/instances/{instance_id}/nodes/enlarge',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateMysqlReadonlyNodeResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_mysql_instance(self, request):
        """删除实例

        删除数据库实例，不支持删除包周期实例。

        :param DeleteMysqlInstanceRequest request
        :return: DeleteMysqlInstanceResponse
        """
        return self.delete_mysql_instance_with_http_info(request)

    def delete_mysql_instance_with_http_info(self, request):
        """删除实例

        删除数据库实例，不支持删除包周期实例。

        :param DeleteMysqlInstanceRequest request
        :return: DeleteMysqlInstanceResponse
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
            resource_path='/mysql/v3/{project_id}/instances/{instance_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteMysqlInstanceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_mysql_proxy(self, request):
        """关闭数据库代理

        关闭数据库代理。

        :param DeleteMysqlProxyRequest request
        :return: DeleteMysqlProxyResponse
        """
        return self.delete_mysql_proxy_with_http_info(request)

    def delete_mysql_proxy_with_http_info(self, request):
        """关闭数据库代理

        关闭数据库代理。

        :param DeleteMysqlProxyRequest request
        :return: DeleteMysqlProxyResponse
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
            resource_path='/mysql/v3/{project_id}/instances/{instance_id}/proxy',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteMysqlProxyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_mysql_readonly_node(self, request):
        """删除只读节点

        删除实例的只读节点。多可用区模式删除只读节点时，要保证删除后，剩余的只读节点和主节点在不同的可用区中，否则无法删除该只读节点。

        :param DeleteMysqlReadonlyNodeRequest request
        :return: DeleteMysqlReadonlyNodeResponse
        """
        return self.delete_mysql_readonly_node_with_http_info(request)

    def delete_mysql_readonly_node_with_http_info(self, request):
        """删除只读节点

        删除实例的只读节点。多可用区模式删除只读节点时，要保证删除后，剩余的只读节点和主节点在不同的可用区中，否则无法删除该只读节点。

        :param DeleteMysqlReadonlyNodeRequest request
        :return: DeleteMysqlReadonlyNodeResponse
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
            resource_path='/mysql/v3/{project_id}/instances/{instance_id}/nodes/{node_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteMysqlReadonlyNodeResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def expand_mysql_instance_volume(self, request):
        """包周期存储扩容

        包周期存储扩容

        :param ExpandMysqlInstanceVolumeRequest request
        :return: ExpandMysqlInstanceVolumeResponse
        """
        return self.expand_mysql_instance_volume_with_http_info(request)

    def expand_mysql_instance_volume_with_http_info(self, request):
        """包周期存储扩容

        包周期存储扩容

        :param ExpandMysqlInstanceVolumeRequest request
        :return: ExpandMysqlInstanceVolumeResponse
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
            resource_path='/mysql/v3/{project_id}/instances/{instance_id}/volume/extend',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ExpandMysqlInstanceVolumeResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def expand_mysql_proxy(self, request):
        """扩容数据库代理节点的数量

        扩容数据库代理节点的数量。 DeC专属云账号暂不支持数据库代理。

        :param ExpandMysqlProxyRequest request
        :return: ExpandMysqlProxyResponse
        """
        return self.expand_mysql_proxy_with_http_info(request)

    def expand_mysql_proxy_with_http_info(self, request):
        """扩容数据库代理节点的数量

        扩容数据库代理节点的数量。 DeC专属云账号暂不支持数据库代理。

        :param ExpandMysqlProxyRequest request
        :return: ExpandMysqlProxyResponse
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
            resource_path='/mysql/v3/{project_id}/instances/{instance_id}/proxy/enlarge',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ExpandMysqlProxyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_dedicated_resources(self, request):
        """查询专属资源池列表

        获取专属资源池列表，包括用户开通的所有专属资源池信息。

        :param ListDedicatedResourcesRequest request
        :return: ListDedicatedResourcesResponse
        """
        return self.list_dedicated_resources_with_http_info(request)

    def list_dedicated_resources_with_http_info(self, request):
        """查询专属资源池列表

        获取专属资源池列表，包括用户开通的所有专属资源池信息。

        :param ListDedicatedResourcesRequest request
        :return: ListDedicatedResourcesResponse
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
            resource_path='/mysql/v3/{project_id}/dedicated-resources',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListDedicatedResourcesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_mysql_configurations(self, request):
        """查询参数模板

        获取参数模板列表，包括所有数据库的默认参数模板和用户创建的参数模板。

        :param ListMysqlConfigurationsRequest request
        :return: ListMysqlConfigurationsResponse
        """
        return self.list_mysql_configurations_with_http_info(request)

    def list_mysql_configurations_with_http_info(self, request):
        """查询参数模板

        获取参数模板列表，包括所有数据库的默认参数模板和用户创建的参数模板。

        :param ListMysqlConfigurationsRequest request
        :return: ListMysqlConfigurationsResponse
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
            resource_path='/mysql/v3/{project_id}/configurations',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListMysqlConfigurationsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_mysql_error_log(self, request):
        """查询数据库错误日志

        查询数据库错误日志。

        :param ListMysqlErrorLogRequest request
        :return: ListMysqlErrorLogResponse
        """
        return self.list_mysql_error_log_with_http_info(request)

    def list_mysql_error_log_with_http_info(self, request):
        """查询数据库错误日志

        查询数据库错误日志。

        :param ListMysqlErrorLogRequest request
        :return: ListMysqlErrorLogResponse
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
            resource_path='/mysql/v3/{project_id}/instances/{instance_id}/errorlog',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListMysqlErrorLogResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_mysql_slow_log(self, request):
        """查询数据库慢日志

        查询数据库慢日志

        :param ListMysqlSlowLogRequest request
        :return: ListMysqlSlowLogResponse
        """
        return self.list_mysql_slow_log_with_http_info(request)

    def list_mysql_slow_log_with_http_info(self, request):
        """查询数据库慢日志

        查询数据库慢日志

        :param ListMysqlSlowLogRequest request
        :return: ListMysqlSlowLogResponse
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
            resource_path='/mysql/v3/{project_id}/instances/{instance_id}/slowlog',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListMysqlSlowLogResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def reset_mysql_password(self, request):
        """重置数据库密码

        重置数据库密码

        :param ResetMysqlPasswordRequest request
        :return: ResetMysqlPasswordResponse
        """
        return self.reset_mysql_password_with_http_info(request)

    def reset_mysql_password_with_http_info(self, request):
        """重置数据库密码

        重置数据库密码

        :param ResetMysqlPasswordRequest request
        :return: ResetMysqlPasswordResponse
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
            resource_path='/mysql/v3/{project_id}/instances/{instance_id}/password',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ResetMysqlPasswordResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def set_mysql_quotas(self, request):
        """设置租户基于企业项目的资源配额

        设置指定企业项目的资源配额。

        :param SetMysqlQuotasRequest request
        :return: SetMysqlQuotasResponse
        """
        return self.set_mysql_quotas_with_http_info(request)

    def set_mysql_quotas_with_http_info(self, request):
        """设置租户基于企业项目的资源配额

        设置指定企业项目的资源配额。

        :param SetMysqlQuotasRequest request
        :return: SetMysqlQuotasResponse
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
            resource_path='/mysql/v3/{project_id}/quotas',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='SetMysqlQuotasResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_mysql_backup_list(self, request):
        """查询备份列表

        查询备份列表

        :param ShowMysqlBackupListRequest request
        :return: ShowMysqlBackupListResponse
        """
        return self.show_mysql_backup_list_with_http_info(request)

    def show_mysql_backup_list_with_http_info(self, request):
        """查询备份列表

        查询备份列表

        :param ShowMysqlBackupListRequest request
        :return: ShowMysqlBackupListResponse
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
            resource_path='/mysql/v3/{project_id}/backups',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowMysqlBackupListResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_mysql_backup_policy(self, request):
        """查询自动备份策略

        查询自动备份策略。

        :param ShowMysqlBackupPolicyRequest request
        :return: ShowMysqlBackupPolicyResponse
        """
        return self.show_mysql_backup_policy_with_http_info(request)

    def show_mysql_backup_policy_with_http_info(self, request):
        """查询自动备份策略

        查询自动备份策略。

        :param ShowMysqlBackupPolicyRequest request
        :return: ShowMysqlBackupPolicyResponse
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
            resource_path='/mysql/v3/{project_id}/instances/{instance_id}/backups/policy',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowMysqlBackupPolicyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_mysql_engine_version(self, request):
        """查询数据库引擎的版本

        获取指定数据库引擎对应的数据库版本信息。

        :param ShowMysqlEngineVersionRequest request
        :return: ShowMysqlEngineVersionResponse
        """
        return self.show_mysql_engine_version_with_http_info(request)

    def show_mysql_engine_version_with_http_info(self, request):
        """查询数据库引擎的版本

        获取指定数据库引擎对应的数据库版本信息。

        :param ShowMysqlEngineVersionRequest request
        :return: ShowMysqlEngineVersionResponse
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
            resource_path='/mysql/v3/{project_id}/datastores/{database_name}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowMysqlEngineVersionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_mysql_flavors(self, request):
        """查询数据库规格

        获取指定数据库引擎版本对应的规格信息。

        :param ShowMysqlFlavorsRequest request
        :return: ShowMysqlFlavorsResponse
        """
        return self.show_mysql_flavors_with_http_info(request)

    def show_mysql_flavors_with_http_info(self, request):
        """查询数据库规格

        获取指定数据库引擎版本对应的规格信息。

        :param ShowMysqlFlavorsRequest request
        :return: ShowMysqlFlavorsResponse
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
            resource_path='/mysql/v3/{project_id}/flavors/{database_name}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowMysqlFlavorsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_mysql_instance_info(self, request):
        """查询实例详情信息

        查询实例详情信息

        :param ShowMysqlInstanceInfoRequest request
        :return: ShowMysqlInstanceInfoResponse
        """
        return self.show_mysql_instance_info_with_http_info(request)

    def show_mysql_instance_info_with_http_info(self, request):
        """查询实例详情信息

        查询实例详情信息

        :param ShowMysqlInstanceInfoRequest request
        :return: ShowMysqlInstanceInfoResponse
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
            resource_path='/mysql/v3/{project_id}/instances/{instance_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowMysqlInstanceInfoResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_mysql_instance_list(self, request):
        """查询实例列表

        根据指定条件查询实例列表。

        :param ShowMysqlInstanceListRequest request
        :return: ShowMysqlInstanceListResponse
        """
        return self.show_mysql_instance_list_with_http_info(request)

    def show_mysql_instance_list_with_http_info(self, request):
        """查询实例列表

        根据指定条件查询实例列表。

        :param ShowMysqlInstanceListRequest request
        :return: ShowMysqlInstanceListResponse
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
            resource_path='/mysql/v3/{project_id}/instances',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowMysqlInstanceListResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_mysql_job_info(self, request):
        """获取指定ID的任务信息

        获取指定ID的任务信息。

        :param ShowMysqlJobInfoRequest request
        :return: ShowMysqlJobInfoResponse
        """
        return self.show_mysql_job_info_with_http_info(request)

    def show_mysql_job_info_with_http_info(self, request):
        """获取指定ID的任务信息

        获取指定ID的任务信息。

        :param ShowMysqlJobInfoRequest request
        :return: ShowMysqlJobInfoResponse
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
            resource_path='/mysql/v3/{project_id}/jobs',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowMysqlJobInfoResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_mysql_project_quotas(self, request):
        """查询租户的实例配额

        获取指定租户的资源配额。

        :param ShowMysqlProjectQuotasRequest request
        :return: ShowMysqlProjectQuotasResponse
        """
        return self.show_mysql_project_quotas_with_http_info(request)

    def show_mysql_project_quotas_with_http_info(self, request):
        """查询租户的实例配额

        获取指定租户的资源配额。

        :param ShowMysqlProjectQuotasRequest request
        :return: ShowMysqlProjectQuotasResponse
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
            resource_path='/mysql/v3/{project_id}/project-quotas',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowMysqlProjectQuotasResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_mysql_proxy(self, request):
        """查询数据库代理信息

        查询数据库代理信息。

        :param ShowMysqlProxyRequest request
        :return: ShowMysqlProxyResponse
        """
        return self.show_mysql_proxy_with_http_info(request)

    def show_mysql_proxy_with_http_info(self, request):
        """查询数据库代理信息

        查询数据库代理信息。

        :param ShowMysqlProxyRequest request
        :return: ShowMysqlProxyResponse
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
            resource_path='/mysql/v3/{project_id}/instances/{instance_id}/proxy',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowMysqlProxyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_mysql_proxy_flavors(self, request):
        """查询数据库代理规格信息

        查询数据库代理规格信息。

        :param ShowMysqlProxyFlavorsRequest request
        :return: ShowMysqlProxyFlavorsResponse
        """
        return self.show_mysql_proxy_flavors_with_http_info(request)

    def show_mysql_proxy_flavors_with_http_info(self, request):
        """查询数据库代理规格信息

        查询数据库代理规格信息。

        :param ShowMysqlProxyFlavorsRequest request
        :return: ShowMysqlProxyFlavorsResponse
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
            resource_path='/mysql/v3/{project_id}/instances/{instance_id}/proxy/flavors',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowMysqlProxyFlavorsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_mysql_quotas(self, request):
        """查询租户基于企业项目的资源配额

        获取指定企业项目的资源配额。

        :param ShowMysqlQuotasRequest request
        :return: ShowMysqlQuotasResponse
        """
        return self.show_mysql_quotas_with_http_info(request)

    def show_mysql_quotas_with_http_info(self, request):
        """查询租户基于企业项目的资源配额

        获取指定企业项目的资源配额。

        :param ShowMysqlQuotasRequest request
        :return: ShowMysqlQuotasResponse
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
            resource_path='/mysql/v3/{project_id}/quotas',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowMysqlQuotasResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_mysql_backup_policy(self, request):
        """修改备份策略

        修改备份策略

        :param UpdateMysqlBackupPolicyRequest request
        :return: UpdateMysqlBackupPolicyResponse
        """
        return self.update_mysql_backup_policy_with_http_info(request)

    def update_mysql_backup_policy_with_http_info(self, request):
        """修改备份策略

        修改备份策略

        :param UpdateMysqlBackupPolicyRequest request
        :return: UpdateMysqlBackupPolicyResponse
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
            resource_path='/mysql/v3/{project_id}/instances/{instance_id}/backups/policy/update',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateMysqlBackupPolicyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_mysql_instance_name(self, request):
        """修改实例名称

        修改实例名称

        :param UpdateMysqlInstanceNameRequest request
        :return: UpdateMysqlInstanceNameResponse
        """
        return self.update_mysql_instance_name_with_http_info(request)

    def update_mysql_instance_name_with_http_info(self, request):
        """修改实例名称

        修改实例名称

        :param UpdateMysqlInstanceNameRequest request
        :return: UpdateMysqlInstanceNameResponse
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
            resource_path='/mysql/v3/{project_id}/instances/{instance_id}/name',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateMysqlInstanceNameResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_mysql_quotas(self, request):
        """修改租户基于企业项目的资源配额

        修改指定企业项目的资源配额。

        :param UpdateMysqlQuotasRequest request
        :return: UpdateMysqlQuotasResponse
        """
        return self.update_mysql_quotas_with_http_info(request)

    def update_mysql_quotas_with_http_info(self, request):
        """修改租户基于企业项目的资源配额

        修改指定企业项目的资源配额。

        :param UpdateMysqlQuotasRequest request
        :return: UpdateMysqlQuotasResponse
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
            resource_path='/mysql/v3/{project_id}/quotas',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateMysqlQuotasResponse',
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

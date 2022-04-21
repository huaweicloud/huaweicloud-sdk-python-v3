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


class CcAsyncClient(Client):
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
        super(CcAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkcc.v3.model")
        self.preset_headers = {'User-Agent': 'HuaweiCloud-SDK-Python'}

    @classmethod
    def new_builder(cls, clazz=None):
        if clazz is None:
            return ClientBuilder(cls, "GlobalCredentials")

        if clazz.__name__ != "CcClient":
            raise TypeError("client type error, support client type is CcClient")

        return ClientBuilder(clazz, "GlobalCredentials")

    def create_cloud_connection_async(self, request):
        """创建云连接实例

        创建云连接实例。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for CreateCloudConnection
        :type request: :class:`huaweicloudsdkcc.v3.CreateCloudConnectionRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.CreateCloudConnectionResponse`
        """
        return self.create_cloud_connection_with_http_info(request)

    def create_cloud_connection_with_http_info(self, request):
        all_params = ['create_cloud_connection_request_body']
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
            resource_path='/v3/{domain_id}/ccaas/cloud-connections',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateCloudConnectionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_network_instance_async(self, request):
        """创建网络实例

        创建网络实例。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for CreateNetworkInstance
        :type request: :class:`huaweicloudsdkcc.v3.CreateNetworkInstanceRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.CreateNetworkInstanceResponse`
        """
        return self.create_network_instance_with_http_info(request)

    def create_network_instance_with_http_info(self, request):
        all_params = ['create_network_instance_request_body']
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
            resource_path='/v3/{domain_id}/ccaas/network-instances',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateNetworkInstanceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_cloud_connection_async(self, request):
        """删除云连接实例

        删除云连接实例。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for DeleteCloudConnection
        :type request: :class:`huaweicloudsdkcc.v3.DeleteCloudConnectionRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.DeleteCloudConnectionResponse`
        """
        return self.delete_cloud_connection_with_http_info(request)

    def delete_cloud_connection_with_http_info(self, request):
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
            resource_path='/v3/{domain_id}/ccaas/cloud-connections/{id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteCloudConnectionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_network_instance_async(self, request):
        """删除网络实例

        删除网络实例。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for DeleteNetworkInstance
        :type request: :class:`huaweicloudsdkcc.v3.DeleteNetworkInstanceRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.DeleteNetworkInstanceResponse`
        """
        return self.delete_network_instance_with_http_info(request)

    def delete_network_instance_with_http_info(self, request):
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
            resource_path='/v3/{domain_id}/ccaas/network-instances/{id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteNetworkInstanceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_cloud_connection_routes_async(self, request):
        """查询云连接路由条目列表

        查询云连接路由条目列表。
        分页查询使用的参数为marker、limit。marker和limit一起使用时才会生效，单独使用无效。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListCloudConnectionRoutes
        :type request: :class:`huaweicloudsdkcc.v3.ListCloudConnectionRoutesRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.ListCloudConnectionRoutesResponse`
        """
        return self.list_cloud_connection_routes_with_http_info(request)

    def list_cloud_connection_routes_with_http_info(self, request):
        all_params = ['limit', 'marker', 'id', 'cloud_connection_id', 'instance_id', 'region_id']
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
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'cloud_connection_id' in local_var_params:
            query_params.append(('cloud_connection_id', local_var_params['cloud_connection_id']))
            collection_formats['cloud_connection_id'] = 'csv'
        if 'instance_id' in local_var_params:
            query_params.append(('instance_id', local_var_params['instance_id']))
            collection_formats['instance_id'] = 'csv'
        if 'region_id' in local_var_params:
            query_params.append(('region_id', local_var_params['region_id']))

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
            resource_path='/v3/{domain_id}/ccaas/cloud-connection-routes',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListCloudConnectionRoutesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_cloud_connections_async(self, request):
        """查询云连接列表

        查询云连接列表。
        分页查询使用的参数为marker、limit。marker和limit一起使用时才会生效，单独使用无效。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListCloudConnections
        :type request: :class:`huaweicloudsdkcc.v3.ListCloudConnectionsRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.ListCloudConnectionsResponse`
        """
        return self.list_cloud_connections_with_http_info(request)

    def list_cloud_connections_with_http_info(self, request):
        all_params = ['limit', 'marker', 'id', 'name', 'description', 'status', 'enterprise_project_id', 'type']
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
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
            collection_formats['id'] = 'csv'
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
            collection_formats['name'] = 'csv'
        if 'description' in local_var_params:
            query_params.append(('description', local_var_params['description']))
            collection_formats['description'] = 'csv'
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
            collection_formats['status'] = 'csv'
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
            collection_formats['enterprise_project_id'] = 'csv'
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
            collection_formats['type'] = 'csv'

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
            resource_path='/v3/{domain_id}/ccaas/cloud-connections',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListCloudConnectionsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_network_instances_async(self, request):
        """查询网络实例列表

        查询云连接列表。
        分页查询使用的参数为marker、limit。marker和limit一起使用时才会生效，单独使用无效。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListNetworkInstances
        :type request: :class:`huaweicloudsdkcc.v3.ListNetworkInstancesRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.ListNetworkInstancesResponse`
        """
        return self.list_network_instances_with_http_info(request)

    def list_network_instances_with_http_info(self, request):
        all_params = ['limit', 'marker', 'id', 'name', 'description', 'status', 'type', 'cloud_connection_id', 'instance_id', 'region_id']
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
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
            collection_formats['id'] = 'csv'
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
            collection_formats['name'] = 'csv'
        if 'description' in local_var_params:
            query_params.append(('description', local_var_params['description']))
            collection_formats['description'] = 'csv'
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
            collection_formats['status'] = 'csv'
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
            collection_formats['type'] = 'csv'
        if 'cloud_connection_id' in local_var_params:
            query_params.append(('cloud_connection_id', local_var_params['cloud_connection_id']))
            collection_formats['cloud_connection_id'] = 'csv'
        if 'instance_id' in local_var_params:
            query_params.append(('instance_id', local_var_params['instance_id']))
            collection_formats['instance_id'] = 'csv'
        if 'region_id' in local_var_params:
            query_params.append(('region_id', local_var_params['region_id']))
            collection_formats['region_id'] = 'csv'

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
            resource_path='/v3/{domain_id}/ccaas/network-instances',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListNetworkInstancesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_cloud_connection_async(self, request):
        """查询云连接实例

        查询云连接实例。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowCloudConnection
        :type request: :class:`huaweicloudsdkcc.v3.ShowCloudConnectionRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.ShowCloudConnectionResponse`
        """
        return self.show_cloud_connection_with_http_info(request)

    def show_cloud_connection_with_http_info(self, request):
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
            resource_path='/v3/{domain_id}/ccaas/cloud-connections/{id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowCloudConnectionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_cloud_connection_routes_async(self, request):
        """查询云连接路由条目详情

        查询云连接路由条目列表。
        分页查询使用的参数为marker、limit。marker和limit一起使用时才会生效，单独使用无效。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowCloudConnectionRoutes
        :type request: :class:`huaweicloudsdkcc.v3.ShowCloudConnectionRoutesRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.ShowCloudConnectionRoutesResponse`
        """
        return self.show_cloud_connection_routes_with_http_info(request)

    def show_cloud_connection_routes_with_http_info(self, request):
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
            resource_path='/v3/{domain_id}/ccaas/cloud-connection-routes/{id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowCloudConnectionRoutesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_network_instance_async(self, request):
        """查询网络实例

        查询网络实例。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowNetworkInstance
        :type request: :class:`huaweicloudsdkcc.v3.ShowNetworkInstanceRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.ShowNetworkInstanceResponse`
        """
        return self.show_network_instance_with_http_info(request)

    def show_network_instance_with_http_info(self, request):
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
            resource_path='/v3/{domain_id}/ccaas/network-instances/{id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowNetworkInstanceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_cloud_connection_async(self, request):
        """更新云连接实例

        更新云连接实例。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for UpdateCloudConnection
        :type request: :class:`huaweicloudsdkcc.v3.UpdateCloudConnectionRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.UpdateCloudConnectionResponse`
        """
        return self.update_cloud_connection_with_http_info(request)

    def update_cloud_connection_with_http_info(self, request):
        all_params = ['id', 'update_cloud_connection_request_body']
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
            resource_path='/v3/{domain_id}/ccaas/cloud-connections/{id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateCloudConnectionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_network_instance_async(self, request):
        """更新网络实例

        更新网络实例。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for UpdateNetworkInstance
        :type request: :class:`huaweicloudsdkcc.v3.UpdateNetworkInstanceRequest`
        :rtype: :class:`huaweicloudsdkcc.v3.UpdateNetworkInstanceResponse`
        """
        return self.update_network_instance_with_http_info(request)

    def update_network_instance_with_http_info(self, request):
        all_params = ['id', 'update_network_instance_request_body']
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
            resource_path='/v3/{domain_id}/ccaas/network-instances/{id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateNetworkInstanceResponse',
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

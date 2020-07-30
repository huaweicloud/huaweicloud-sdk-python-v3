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


class VpcClient(Client):
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
        super(VpcClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkvpc.v3.model")
        self.preset_headers = {'User-Agent': 'HuaweiCloud-SDK-Python'}

    @staticmethod
    def new_builder(clazz):
        return ClientBuilder(clazz)

    def batch_create_sub_network_interface_v3(self, request):
        """批量创建辅助弹性网卡

        批量创建辅助弹性网卡

        :param BatchCreateSubNetworkInterfaceV3Request request
        :return: BatchCreateSubNetworkInterfaceV3Response
        """
        return self.batch_create_sub_network_interface_v3_with_http_info(request)

    def batch_create_sub_network_interface_v3_with_http_info(self, request):
        """批量创建辅助弹性网卡

        批量创建辅助弹性网卡

        :param BatchCreateSubNetworkInterfaceV3Request request
        :return: BatchCreateSubNetworkInterfaceV3Response
        """

        all_params = ['batch_create_sub_network_interface_v3_request_body']
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

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/vpc/sub-network-interfaces/batch-create',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='BatchCreateSubNetworkInterfaceV3Response',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_sub_network_interface(self, request):
        """创建辅助弹性网卡

        创建辅助弹性网卡

        :param CreateSubNetworkInterfaceRequest request
        :return: CreateSubNetworkInterfaceResponse
        """
        return self.create_sub_network_interface_with_http_info(request)

    def create_sub_network_interface_with_http_info(self, request):
        """创建辅助弹性网卡

        创建辅助弹性网卡

        :param CreateSubNetworkInterfaceRequest request
        :return: CreateSubNetworkInterfaceResponse
        """

        all_params = ['create_sub_network_interface_request_body']
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

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/vpc/sub-network-interfaces',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateSubNetworkInterfaceResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_sub_network_interface(self, request):
        """删除辅助弹性网卡

        删除辅助弹性网卡

        :param DeleteSubNetworkInterfaceRequest request
        :return: DeleteSubNetworkInterfaceResponse
        """
        return self.delete_sub_network_interface_with_http_info(request)

    def delete_sub_network_interface_with_http_info(self, request):
        """删除辅助弹性网卡

        删除辅助弹性网卡

        :param DeleteSubNetworkInterfaceRequest request
        :return: DeleteSubNetworkInterfaceResponse
        """

        all_params = ['sub_network_interface_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'sub_network_interface_id' in local_var_params:
            path_params['sub_network_interface_id'] = local_var_params['sub_network_interface_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()


        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/vpc/sub-network-interfaces/{sub_network_interface_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteSubNetworkInterfaceResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_sub_network_interfaces(self, request):
        """查询租户下辅助弹性网卡列表

        查询辅助弹性网卡列表，单次查询最多返回2000条数据

        :param ListSubNetworkInterfacesRequest request
        :return: ListSubNetworkInterfacesResponse
        """
        return self.list_sub_network_interfaces_with_http_info(request)

    def list_sub_network_interfaces_with_http_info(self, request):
        """查询租户下辅助弹性网卡列表

        查询辅助弹性网卡列表，单次查询最多返回2000条数据

        :param ListSubNetworkInterfacesRequest request
        :return: ListSubNetworkInterfacesResponse
        """

        all_params = ['limit', 'marker', 'id', 'virsubnet_id', 'private_ip_address', 'mac_address', 'vpc_id', 'description', 'parent_id']
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
            collection_formats['id'] = 'multi'
        if 'virsubnet_id' in local_var_params:
            query_params.append(('virsubnet_id', local_var_params['virsubnet_id']))
            collection_formats['virsubnet_id'] = 'multi'
        if 'private_ip_address' in local_var_params:
            query_params.append(('private_ip_address', local_var_params['private_ip_address']))
            collection_formats['private_ip_address'] = 'multi'
        if 'mac_address' in local_var_params:
            query_params.append(('mac_address', local_var_params['mac_address']))
            collection_formats['mac_address'] = 'multi'
        if 'vpc_id' in local_var_params:
            query_params.append(('vpc_id', local_var_params['vpc_id']))
            collection_formats['vpc_id'] = 'multi'
        if 'description' in local_var_params:
            query_params.append(('description', local_var_params['description']))
            collection_formats['description'] = 'multi'
        if 'parent_id' in local_var_params:
            query_params.append(('parent_id', local_var_params['parent_id']))
            collection_formats['parent_id'] = 'multi'

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()


        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/vpc/sub-network-interfaces',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListSubNetworkInterfacesResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_sub_network_interface(self, request):
        """查询租户下辅助弹性网卡

        查询辅助弹性网卡详情

        :param ShowSubNetworkInterfaceRequest request
        :return: ShowSubNetworkInterfaceResponse
        """
        return self.show_sub_network_interface_with_http_info(request)

    def show_sub_network_interface_with_http_info(self, request):
        """查询租户下辅助弹性网卡

        查询辅助弹性网卡详情

        :param ShowSubNetworkInterfaceRequest request
        :return: ShowSubNetworkInterfaceResponse
        """

        all_params = ['sub_network_interface_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'sub_network_interface_id' in local_var_params:
            path_params['sub_network_interface_id'] = local_var_params['sub_network_interface_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()


        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/vpc/sub-network-interfaces/{sub_network_interface_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowSubNetworkInterfaceResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_sub_network_interfaces_quantity(self, request):
        """查询租户下辅助弹性网卡数目

        查询辅助弹性网卡数目

        :param ShowSubNetworkInterfacesQuantityRequest request
        :return: ShowSubNetworkInterfacesQuantityResponse
        """
        return self.show_sub_network_interfaces_quantity_with_http_info(request)

    def show_sub_network_interfaces_quantity_with_http_info(self, request):
        """查询租户下辅助弹性网卡数目

        查询辅助弹性网卡数目

        :param ShowSubNetworkInterfacesQuantityRequest request
        :return: ShowSubNetworkInterfacesQuantityResponse
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


        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/vpc/sub-network-interfaces/count',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowSubNetworkInterfacesQuantityResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_sub_network_interface(self, request):
        """更新辅助弹性网卡

        更新辅助弹性网卡

        :param UpdateSubNetworkInterfaceRequest request
        :return: UpdateSubNetworkInterfaceResponse
        """
        return self.update_sub_network_interface_with_http_info(request)

    def update_sub_network_interface_with_http_info(self, request):
        """更新辅助弹性网卡

        更新辅助弹性网卡

        :param UpdateSubNetworkInterfaceRequest request
        :return: UpdateSubNetworkInterfaceResponse
        """

        all_params = ['sub_network_interface_id', 'update_sub_network_interface_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'sub_network_interface_id' in local_var_params:
            path_params['sub_network_interface_id'] = local_var_params['sub_network_interface_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/vpc/sub-network-interfaces/{sub_network_interface_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateSubNetworkInterfaceResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def call_api(self, resource_path, method, path_params=None, query_params=None, header_params=None,
                 body=None, post_params=None, response_type=None, auth_settings=None, collection_formats=None,
                 request_type=None):
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
        :param collection_formats: dict of collection formats for path, query,
            header, and post parameters.
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
            collection_formats=collection_formats,
            request_type=request_type)

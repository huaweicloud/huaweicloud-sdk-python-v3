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


class MapDSClient(Client):
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
        super(MapDSClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkmapds.v1.model")
        self.preset_headers = {'User-Agent': 'HuaweiCloud-SDK-Python'}

    @classmethod
    def new_builder(cls, clazz=None):
        if clazz is None:
            return ClientBuilder(cls)

        if clazz.__name__ != "MapDSClient":
            raise TypeError("client type error, support client type is MapDSClient")

        return ClientBuilder(clazz)

    def create_credential(self, request):
        """创建凭证

        该接口用于创建访问地图数据服务的凭证。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateCredential
        :type request: :class:`huaweicloudsdkmapds.v1.CreateCredentialRequest`
        :rtype: :class:`huaweicloudsdkmapds.v1.CreateCredentialResponse`
        """
        return self.create_credential_with_http_info(request)

    def create_credential_with_http_info(self, request):
        all_params = ['x_auth_token', 'content_type', 'create_credential_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_auth_token' in local_var_params:
            header_params['X-Auth-Token'] = local_var_params['x_auth_token']
        if 'content_type' in local_var_params:
            header_params['Content-Type'] = local_var_params['content_type']

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
            resource_path='/v1/map/credentials',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateCredentialResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_sas_token(self, request):
        """创建SAS Token

        创建SAS token凭据，用于访问瓦片。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateSasToken
        :type request: :class:`huaweicloudsdkmapds.v1.CreateSasTokenRequest`
        :rtype: :class:`huaweicloudsdkmapds.v1.CreateSasTokenResponse`
        """
        return self.create_sas_token_with_http_info(request)

    def create_sas_token_with_http_info(self, request):
        all_params = ['x_auth_token', 'content_type', 'create_sas_token_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_auth_token' in local_var_params:
            header_params['X-Auth-Token'] = local_var_params['x_auth_token']
        if 'content_type' in local_var_params:
            header_params['Content-Type'] = local_var_params['content_type']

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
            resource_path='/v1/map/sastoken',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateSasTokenResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_cedential(self, request):
        """删除凭证

        该接口用于删除访问地图数据服务的凭证。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteCedential
        :type request: :class:`huaweicloudsdkmapds.v1.DeleteCedentialRequest`
        :rtype: :class:`huaweicloudsdkmapds.v1.DeleteCedentialResponse`
        """
        return self.delete_cedential_with_http_info(request)

    def delete_cedential_with_http_info(self, request):
        all_params = ['clientid', 'x_auth_token', 'content_type']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'clientid' in local_var_params:
            path_params['clientid'] = local_var_params['clientid']

        query_params = []

        header_params = {}
        if 'x_auth_token' in local_var_params:
            header_params['X-Auth-Token'] = local_var_params['x_auth_token']
        if 'content_type' in local_var_params:
            header_params['Content-Type'] = local_var_params['content_type']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/map/credentials/{clientid}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteCedentialResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_credential(self, request):
        """查询凭证

        该接口用于查询访问地图数据服务的凭证。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowCredential
        :type request: :class:`huaweicloudsdkmapds.v1.ShowCredentialRequest`
        :rtype: :class:`huaweicloudsdkmapds.v1.ShowCredentialResponse`
        """
        return self.show_credential_with_http_info(request)

    def show_credential_with_http_info(self, request):
        all_params = ['x_auth_token', 'content_type']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_auth_token' in local_var_params:
            header_params['X-Auth-Token'] = local_var_params['x_auth_token']
        if 'content_type' in local_var_params:
            header_params['Content-Type'] = local_var_params['content_type']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/map/credentials',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowCredentialResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_map_tile(self, request):
        """获取地图瓦片

        该接口用于获取地图瓦片。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowMapTile
        :type request: :class:`huaweicloudsdkmapds.v1.ShowMapTileRequest`
        :rtype: :class:`huaweicloudsdkmapds.v1.ShowMapTileResponse`
        """
        return self.show_map_tile_with_http_info(request)

    def show_map_tile_with_http_info(self, request):
        all_params = ['z', 'x', 'y', 'authorization']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'z' in local_var_params:
            path_params['z'] = local_var_params['z']
        if 'x' in local_var_params:
            path_params['x'] = local_var_params['x']
        if 'y' in local_var_params:
            path_params['y'] = local_var_params['y']

        query_params = []

        header_params = {}
        if 'authorization' in local_var_params:
            header_params['Authorization'] = local_var_params['authorization']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["Content-Type", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/map/tile/{z}/{x}/{y}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowMapTileResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def call_api(self, resource_path, method, path_params=None, query_params=None, header_params=None, body=None,
                 post_params=None, cname=None, response_type=None, response_headers=None, auth_settings=None,
                 collection_formats=None, request_type=None):
        """Makes the HTTP request and returns deserialized data.

        :param resource_path: Path to method endpoint.
        :param method: Method to call.
        :param path_params: Path parameters in the url.
        :param query_params: Query parameters in the url.
        :param header_params: Header parameters to be placed in the request header.
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
            request_type=request_type)

# coding: utf-8

from __future__ import absolute_import

import importlib

from huaweicloudsdkcore.client import Client, ClientBuilder
from huaweicloudsdkcore.utils import http_utils
from huaweicloudsdkcore.sdk_stream_request import SdkStreamRequest


class AsmClient(Client):
    def __init__(self):
        super(AsmClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkasm.v1.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if clazz is None:
            return ClientBuilder(cls)

        if clazz.__name__ != "AsmClient":
            raise TypeError("client type error, support client type is AsmClient")

        return ClientBuilder(clazz)

    def create_mesh(self, request):
        """新建网格

        该API用于创建一个网格。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateMesh
        :type request: :class:`huaweicloudsdkasm.v1.CreateMeshRequest`
        :rtype: :class:`huaweicloudsdkasm.v1.CreateMeshResponse`
        """
        return self._create_mesh_with_http_info(request)

    def _create_mesh_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'content_type' in local_var_params:
            header_params['Content-Type'] = local_var_params['content_type']
        if 'x_apply_project_id' in local_var_params:
            header_params['X-Apply-ProjectID'] = local_var_params['x_apply_project_id']

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
            resource_path='/v1/meshes',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateMeshResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_mesh(self, request):
        """删除网格

        该API用于删除一个指定的网格。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteMesh
        :type request: :class:`huaweicloudsdkasm.v1.DeleteMeshRequest`
        :rtype: :class:`huaweicloudsdkasm.v1.DeleteMeshResponse`
        """
        return self._delete_mesh_with_http_info(request)

    def _delete_mesh_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'mesh_id' in local_var_params:
            path_params['mesh_id'] = local_var_params['mesh_id']

        query_params = []

        header_params = {}
        if 'content_type' in local_var_params:
            header_params['Content-Type'] = local_var_params['content_type']
        if 'x_apply_project_id' in local_var_params:
            header_params['X-Apply-ProjectID'] = local_var_params['x_apply_project_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/meshes/{mesh_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteMeshResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_meshes(self, request):
        """查询网格列表

        该API用于获取用户所有网格的详细信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListMeshes
        :type request: :class:`huaweicloudsdkasm.v1.ListMeshesRequest`
        :rtype: :class:`huaweicloudsdkasm.v1.ListMeshesResponse`
        """
        return self._list_meshes_with_http_info(request)

    def _list_meshes_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'content_type' in local_var_params:
            header_params['Content-Type'] = local_var_params['content_type']
        if 'x_apply_domain_id' in local_var_params:
            header_params['X-Apply-DomainID'] = local_var_params['x_apply_domain_id']
        if 'x_apply_project_id' in local_var_params:
            header_params['X-Apply-ProjectID'] = local_var_params['x_apply_project_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/meshes',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListMeshesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_mesh(self, request):
        """查询网格

        该API用于获取指定网格的详细信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowMesh
        :type request: :class:`huaweicloudsdkasm.v1.ShowMeshRequest`
        :rtype: :class:`huaweicloudsdkasm.v1.ShowMeshResponse`
        """
        return self._show_mesh_with_http_info(request)

    def _show_mesh_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'mesh_id' in local_var_params:
            path_params['mesh_id'] = local_var_params['mesh_id']

        query_params = []

        header_params = {}
        if 'content_type' in local_var_params:
            header_params['Content-Type'] = local_var_params['content_type']
        if 'x_apply_domain_id' in local_var_params:
            header_params['X-Apply-DomainID'] = local_var_params['x_apply_domain_id']
        if 'x_apply_project_id' in local_var_params:
            header_params['X-Apply-ProjectID'] = local_var_params['x_apply_project_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/meshes/{mesh_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowMeshResponse',
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

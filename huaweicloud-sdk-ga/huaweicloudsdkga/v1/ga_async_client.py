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


class GaAsyncClient(Client):
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
        super(GaAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkga.v1.model")
        self.preset_headers = {'User-Agent': 'HuaweiCloud-SDK-Python'}

    @classmethod
    def new_builder(cls, clazz=None):
        if clazz is None:
            return ClientBuilder(cls)

        if clazz.__name__ != "GaClient":
            raise TypeError("client type error, support client type is GaClient")

        return ClientBuilder(clazz)

    def create_accelerator_async(self, request):
        """创建全球加速器

        创建全球加速器。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateAccelerator
        :type request: :class:`huaweicloudsdkga.v1.CreateAcceleratorRequest`
        :rtype: :class:`huaweicloudsdkga.v1.CreateAcceleratorResponse`
        """
        return self.create_accelerator_with_http_info(request)

    def create_accelerator_with_http_info(self, request):
        all_params = ['create_accelerator_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            resource_path='/v1/accelerators',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateAcceleratorResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_accelerator_async(self, request):
        """删除全球加速器

        删除全球加速器。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteAccelerator
        :type request: :class:`huaweicloudsdkga.v1.DeleteAcceleratorRequest`
        :rtype: :class:`huaweicloudsdkga.v1.DeleteAcceleratorResponse`
        """
        return self.delete_accelerator_with_http_info(request)

    def delete_accelerator_with_http_info(self, request):
        all_params = ['accelerator_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'accelerator_id' in local_var_params:
            path_params['accelerator_id'] = local_var_params['accelerator_id']

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
            resource_path='/v1/accelerators/{accelerator_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteAcceleratorResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_accelerators_async(self, request):
        """查询全球加速器列表

        查询全球加速器列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAccelerators
        :type request: :class:`huaweicloudsdkga.v1.ListAcceleratorsRequest`
        :rtype: :class:`huaweicloudsdkga.v1.ListAcceleratorsResponse`
        """
        return self.list_accelerators_with_http_info(request)

    def list_accelerators_with_http_info(self, request):
        all_params = ['limit', 'marker', 'page_reverse', 'id', 'name', 'status', 'enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'page_reverse' in local_var_params:
            query_params.append(('page_reverse', local_var_params['page_reverse']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
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
            resource_path='/v1/accelerators',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListAcceleratorsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_accelerator_async(self, request):
        """查询全球加速器详情

        查询全球加速器详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowAccelerator
        :type request: :class:`huaweicloudsdkga.v1.ShowAcceleratorRequest`
        :rtype: :class:`huaweicloudsdkga.v1.ShowAcceleratorResponse`
        """
        return self.show_accelerator_with_http_info(request)

    def show_accelerator_with_http_info(self, request):
        all_params = ['accelerator_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'accelerator_id' in local_var_params:
            path_params['accelerator_id'] = local_var_params['accelerator_id']

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
            resource_path='/v1/accelerators/{accelerator_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowAcceleratorResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_accelerator_async(self, request):
        """更新全球加速器

        更新全球加速器。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateAccelerator
        :type request: :class:`huaweicloudsdkga.v1.UpdateAcceleratorRequest`
        :rtype: :class:`huaweicloudsdkga.v1.UpdateAcceleratorResponse`
        """
        return self.update_accelerator_with_http_info(request)

    def update_accelerator_with_http_info(self, request):
        all_params = ['accelerator_id', 'update_accelerator_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'accelerator_id' in local_var_params:
            path_params['accelerator_id'] = local_var_params['accelerator_id']

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
            resource_path='/v1/accelerators/{accelerator_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateAcceleratorResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_endpoint_async(self, request):
        """创建终端节点

        创建终端节点。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateEndpoint
        :type request: :class:`huaweicloudsdkga.v1.CreateEndpointRequest`
        :rtype: :class:`huaweicloudsdkga.v1.CreateEndpointResponse`
        """
        return self.create_endpoint_with_http_info(request)

    def create_endpoint_with_http_info(self, request):
        all_params = ['endpoint_group_id', 'create_endpoint_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'endpoint_group_id' in local_var_params:
            path_params['endpoint_group_id'] = local_var_params['endpoint_group_id']

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
            resource_path='/v1/endpoint-groups/{endpoint_group_id}/endpoints',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateEndpointResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_endpoint_async(self, request):
        """删除终端节点

        删除终端节点。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteEndpoint
        :type request: :class:`huaweicloudsdkga.v1.DeleteEndpointRequest`
        :rtype: :class:`huaweicloudsdkga.v1.DeleteEndpointResponse`
        """
        return self.delete_endpoint_with_http_info(request)

    def delete_endpoint_with_http_info(self, request):
        all_params = ['endpoint_group_id', 'endpoint_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'endpoint_group_id' in local_var_params:
            path_params['endpoint_group_id'] = local_var_params['endpoint_group_id']
        if 'endpoint_id' in local_var_params:
            path_params['endpoint_id'] = local_var_params['endpoint_id']

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
            resource_path='/v1/endpoint-groups/{endpoint_group_id}/endpoints/{endpoint_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteEndpointResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_endpoints_async(self, request):
        """查询终端节点组下终端节点列表

        查询终端节点组下终端节点列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListEndpoints
        :type request: :class:`huaweicloudsdkga.v1.ListEndpointsRequest`
        :rtype: :class:`huaweicloudsdkga.v1.ListEndpointsResponse`
        """
        return self.list_endpoints_with_http_info(request)

    def list_endpoints_with_http_info(self, request):
        all_params = ['endpoint_group_id', 'limit', 'marker', 'page_reverse', 'id', 'status']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'endpoint_group_id' in local_var_params:
            path_params['endpoint_group_id'] = local_var_params['endpoint_group_id']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'page_reverse' in local_var_params:
            query_params.append(('page_reverse', local_var_params['page_reverse']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))

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
            resource_path='/v1/endpoint-groups/{endpoint_group_id}/endpoints',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListEndpointsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_endpoint_async(self, request):
        """查询终端节点详情

        查询终端节点详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowEndpoint
        :type request: :class:`huaweicloudsdkga.v1.ShowEndpointRequest`
        :rtype: :class:`huaweicloudsdkga.v1.ShowEndpointResponse`
        """
        return self.show_endpoint_with_http_info(request)

    def show_endpoint_with_http_info(self, request):
        all_params = ['endpoint_group_id', 'endpoint_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'endpoint_group_id' in local_var_params:
            path_params['endpoint_group_id'] = local_var_params['endpoint_group_id']
        if 'endpoint_id' in local_var_params:
            path_params['endpoint_id'] = local_var_params['endpoint_id']

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
            resource_path='/v1/endpoint-groups/{endpoint_group_id}/endpoints/{endpoint_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowEndpointResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_endpoint_async(self, request):
        """更新终端节点

        更新终端节点。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateEndpoint
        :type request: :class:`huaweicloudsdkga.v1.UpdateEndpointRequest`
        :rtype: :class:`huaweicloudsdkga.v1.UpdateEndpointResponse`
        """
        return self.update_endpoint_with_http_info(request)

    def update_endpoint_with_http_info(self, request):
        all_params = ['endpoint_group_id', 'endpoint_id', 'update_endpoint_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'endpoint_group_id' in local_var_params:
            path_params['endpoint_group_id'] = local_var_params['endpoint_group_id']
        if 'endpoint_id' in local_var_params:
            path_params['endpoint_id'] = local_var_params['endpoint_id']

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
            resource_path='/v1/endpoint-groups/{endpoint_group_id}/endpoints/{endpoint_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateEndpointResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_endpoint_group_async(self, request):
        """创建终端节点组

        创建终端节点组。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateEndpointGroup
        :type request: :class:`huaweicloudsdkga.v1.CreateEndpointGroupRequest`
        :rtype: :class:`huaweicloudsdkga.v1.CreateEndpointGroupResponse`
        """
        return self.create_endpoint_group_with_http_info(request)

    def create_endpoint_group_with_http_info(self, request):
        all_params = ['create_endpoint_group_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            resource_path='/v1/endpoint-groups',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateEndpointGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_endpoint_group_async(self, request):
        """删除终端节点组

        删除终端节点组。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteEndpointGroup
        :type request: :class:`huaweicloudsdkga.v1.DeleteEndpointGroupRequest`
        :rtype: :class:`huaweicloudsdkga.v1.DeleteEndpointGroupResponse`
        """
        return self.delete_endpoint_group_with_http_info(request)

    def delete_endpoint_group_with_http_info(self, request):
        all_params = ['endpoint_group_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'endpoint_group_id' in local_var_params:
            path_params['endpoint_group_id'] = local_var_params['endpoint_group_id']

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
            resource_path='/v1/endpoint-groups/{endpoint_group_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteEndpointGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_endpoint_groups_async(self, request):
        """查询终端节点组列表

        查询终端节点组列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListEndpointGroups
        :type request: :class:`huaweicloudsdkga.v1.ListEndpointGroupsRequest`
        :rtype: :class:`huaweicloudsdkga.v1.ListEndpointGroupsResponse`
        """
        return self.list_endpoint_groups_with_http_info(request)

    def list_endpoint_groups_with_http_info(self, request):
        all_params = ['limit', 'marker', 'page_reverse', 'id', 'name', 'status', 'listener_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'page_reverse' in local_var_params:
            query_params.append(('page_reverse', local_var_params['page_reverse']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'listener_id' in local_var_params:
            query_params.append(('listener_id', local_var_params['listener_id']))

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
            resource_path='/v1/endpoint-groups',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListEndpointGroupsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_endpoint_group_async(self, request):
        """查询终端节点组详情

        查询终端节点组详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowEndpointGroup
        :type request: :class:`huaweicloudsdkga.v1.ShowEndpointGroupRequest`
        :rtype: :class:`huaweicloudsdkga.v1.ShowEndpointGroupResponse`
        """
        return self.show_endpoint_group_with_http_info(request)

    def show_endpoint_group_with_http_info(self, request):
        all_params = ['endpoint_group_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'endpoint_group_id' in local_var_params:
            path_params['endpoint_group_id'] = local_var_params['endpoint_group_id']

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
            resource_path='/v1/endpoint-groups/{endpoint_group_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowEndpointGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_endpoint_group_async(self, request):
        """更新终端节点组

        更新终端节点组。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateEndpointGroup
        :type request: :class:`huaweicloudsdkga.v1.UpdateEndpointGroupRequest`
        :rtype: :class:`huaweicloudsdkga.v1.UpdateEndpointGroupResponse`
        """
        return self.update_endpoint_group_with_http_info(request)

    def update_endpoint_group_with_http_info(self, request):
        all_params = ['endpoint_group_id', 'update_endpoint_group_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'endpoint_group_id' in local_var_params:
            path_params['endpoint_group_id'] = local_var_params['endpoint_group_id']

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
            resource_path='/v1/endpoint-groups/{endpoint_group_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateEndpointGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_health_check_async(self, request):
        """创建健康检查

        创建健康检查。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateHealthCheck
        :type request: :class:`huaweicloudsdkga.v1.CreateHealthCheckRequest`
        :rtype: :class:`huaweicloudsdkga.v1.CreateHealthCheckResponse`
        """
        return self.create_health_check_with_http_info(request)

    def create_health_check_with_http_info(self, request):
        all_params = ['create_health_check_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            resource_path='/v1/health-checks',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateHealthCheckResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_health_check_async(self, request):
        """删除健康检查

        删除健康检查。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteHealthCheck
        :type request: :class:`huaweicloudsdkga.v1.DeleteHealthCheckRequest`
        :rtype: :class:`huaweicloudsdkga.v1.DeleteHealthCheckResponse`
        """
        return self.delete_health_check_with_http_info(request)

    def delete_health_check_with_http_info(self, request):
        all_params = ['health_check_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'health_check_id' in local_var_params:
            path_params['health_check_id'] = local_var_params['health_check_id']

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
            resource_path='/v1/health-checks/{health_check_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteHealthCheckResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_health_checks_async(self, request):
        """查询健康检查列表

        查询健康检查列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListHealthChecks
        :type request: :class:`huaweicloudsdkga.v1.ListHealthChecksRequest`
        :rtype: :class:`huaweicloudsdkga.v1.ListHealthChecksResponse`
        """
        return self.list_health_checks_with_http_info(request)

    def list_health_checks_with_http_info(self, request):
        all_params = ['limit', 'marker', 'page_reverse', 'id', 'status', 'endpoint_group_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'page_reverse' in local_var_params:
            query_params.append(('page_reverse', local_var_params['page_reverse']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'endpoint_group_id' in local_var_params:
            query_params.append(('endpoint_group_id', local_var_params['endpoint_group_id']))

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
            resource_path='/v1/health-checks',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListHealthChecksResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_health_check_async(self, request):
        """查询健康检查详情

        查询健康检查详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowHealthCheck
        :type request: :class:`huaweicloudsdkga.v1.ShowHealthCheckRequest`
        :rtype: :class:`huaweicloudsdkga.v1.ShowHealthCheckResponse`
        """
        return self.show_health_check_with_http_info(request)

    def show_health_check_with_http_info(self, request):
        all_params = ['health_check_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'health_check_id' in local_var_params:
            path_params['health_check_id'] = local_var_params['health_check_id']

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
            resource_path='/v1/health-checks/{health_check_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowHealthCheckResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_health_check_async(self, request):
        """更新健康检查

        更新健康检查。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateHealthCheck
        :type request: :class:`huaweicloudsdkga.v1.UpdateHealthCheckRequest`
        :rtype: :class:`huaweicloudsdkga.v1.UpdateHealthCheckResponse`
        """
        return self.update_health_check_with_http_info(request)

    def update_health_check_with_http_info(self, request):
        all_params = ['health_check_id', 'update_health_check_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'health_check_id' in local_var_params:
            path_params['health_check_id'] = local_var_params['health_check_id']

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
            resource_path='/v1/health-checks/{health_check_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateHealthCheckResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_listener_async(self, request):
        """创建监听器

        创建监听器。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateListener
        :type request: :class:`huaweicloudsdkga.v1.CreateListenerRequest`
        :rtype: :class:`huaweicloudsdkga.v1.CreateListenerResponse`
        """
        return self.create_listener_with_http_info(request)

    def create_listener_with_http_info(self, request):
        all_params = ['create_listener_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            resource_path='/v1/listeners',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateListenerResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_listener_async(self, request):
        """删除监听器

        删除监听器。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteListener
        :type request: :class:`huaweicloudsdkga.v1.DeleteListenerRequest`
        :rtype: :class:`huaweicloudsdkga.v1.DeleteListenerResponse`
        """
        return self.delete_listener_with_http_info(request)

    def delete_listener_with_http_info(self, request):
        all_params = ['listener_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'listener_id' in local_var_params:
            path_params['listener_id'] = local_var_params['listener_id']

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
            resource_path='/v1/listeners/{listener_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteListenerResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_listeners_async(self, request):
        """查询监听器列表

        查询监听器列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListListeners
        :type request: :class:`huaweicloudsdkga.v1.ListListenersRequest`
        :rtype: :class:`huaweicloudsdkga.v1.ListListenersResponse`
        """
        return self.list_listeners_with_http_info(request)

    def list_listeners_with_http_info(self, request):
        all_params = ['limit', 'marker', 'page_reverse', 'id', 'name', 'status', 'accelerator_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'page_reverse' in local_var_params:
            query_params.append(('page_reverse', local_var_params['page_reverse']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'accelerator_id' in local_var_params:
            query_params.append(('accelerator_id', local_var_params['accelerator_id']))

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
            resource_path='/v1/listeners',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListListenersResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_listener_async(self, request):
        """查询监听器详情

        查询监听器详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowListener
        :type request: :class:`huaweicloudsdkga.v1.ShowListenerRequest`
        :rtype: :class:`huaweicloudsdkga.v1.ShowListenerResponse`
        """
        return self.show_listener_with_http_info(request)

    def show_listener_with_http_info(self, request):
        all_params = ['listener_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'listener_id' in local_var_params:
            path_params['listener_id'] = local_var_params['listener_id']

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
            resource_path='/v1/listeners/{listener_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowListenerResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_listener_async(self, request):
        """更新监听器

        更新监听器。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateListener
        :type request: :class:`huaweicloudsdkga.v1.UpdateListenerRequest`
        :rtype: :class:`huaweicloudsdkga.v1.UpdateListenerResponse`
        """
        return self.update_listener_with_http_info(request)

    def update_listener_with_http_info(self, request):
        all_params = ['listener_id', 'update_listener_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'listener_id' in local_var_params:
            path_params['listener_id'] = local_var_params['listener_id']

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
            resource_path='/v1/listeners/{listener_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateListenerResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_regions_async(self, request):
        """查询区域列表

        查询区域列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListRegions
        :type request: :class:`huaweicloudsdkga.v1.ListRegionsRequest`
        :rtype: :class:`huaweicloudsdkga.v1.ListRegionsResponse`
        """
        return self.list_regions_with_http_info(request)

    def list_regions_with_http_info(self, request):
        all_params = []
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            resource_path='/v1/regions',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListRegionsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_tags_async(self, request):
        """批量添加标签

        批量添加标签。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateTags
        :type request: :class:`huaweicloudsdkga.v1.CreateTagsRequest`
        :rtype: :class:`huaweicloudsdkga.v1.CreateTagsResponse`
        """
        return self.create_tags_with_http_info(request)

    def create_tags_with_http_info(self, request):
        all_params = ['resource_type', 'resource_id', 'create_tags_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_type' in local_var_params:
            path_params['resource_type'] = local_var_params['resource_type']
        if 'resource_id' in local_var_params:
            path_params['resource_id'] = local_var_params['resource_id']

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
            resource_path='/v1/{resource_type}/{resource_id}/tags/create',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_tags_async(self, request):
        """批量删除标签

        批量删除标签。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteTags
        :type request: :class:`huaweicloudsdkga.v1.DeleteTagsRequest`
        :rtype: :class:`huaweicloudsdkga.v1.DeleteTagsResponse`
        """
        return self.delete_tags_with_http_info(request)

    def delete_tags_with_http_info(self, request):
        all_params = ['resource_type', 'resource_id', 'delete_tags_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_type' in local_var_params:
            path_params['resource_type'] = local_var_params['resource_type']
        if 'resource_id' in local_var_params:
            path_params['resource_id'] = local_var_params['resource_id']

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
            resource_path='/v1/{resource_type}/{resource_id}/tags/delete',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_resource_tags_async(self, request):
        """查询资源已打标签

        查询资源已打标签。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowResourceTags
        :type request: :class:`huaweicloudsdkga.v1.ShowResourceTagsRequest`
        :rtype: :class:`huaweicloudsdkga.v1.ShowResourceTagsResponse`
        """
        return self.show_resource_tags_with_http_info(request)

    def show_resource_tags_with_http_info(self, request):
        all_params = ['resource_type', 'resource_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_type' in local_var_params:
            path_params['resource_type'] = local_var_params['resource_type']
        if 'resource_id' in local_var_params:
            path_params['resource_id'] = local_var_params['resource_id']

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
            resource_path='/v1/{resource_type}/{resource_id}/tags',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowResourceTagsResponse',
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
        :param header_params: Header parameters to be
            placed in the request header.
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
            request_type=request_type,
	    async_request=True)

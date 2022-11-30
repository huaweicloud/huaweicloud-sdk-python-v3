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


class VpcepAsyncClient(Client):
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
        super(VpcepAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkvpcep.v1.model")
        self.preset_headers = {'User-Agent': 'HuaweiCloud-SDK-Python'}

    @classmethod
    def new_builder(cls, clazz=None):
        if clazz is None:
            return ClientBuilder(cls)

        if clazz.__name__ != "VpcepClient":
            raise TypeError("client type error, support client type is VpcepClient")

        return ClientBuilder(clazz)

    def accept_or_reject_endpoint_async(self, request):
        """接受或拒绝终端节点的连接

        功能介绍
        接受或者拒绝终端节点连接到当前的终端节点服务。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AcceptOrRejectEndpoint
        :type request: :class:`huaweicloudsdkvpcep.v1.AcceptOrRejectEndpointRequest`
        :rtype: :class:`huaweicloudsdkvpcep.v1.AcceptOrRejectEndpointResponse`
        """
        return self.accept_or_reject_endpoint_with_http_info(request)

    def accept_or_reject_endpoint_with_http_info(self, request):
        all_params = ['vpc_endpoint_service_id', 'accept_or_reject_endpoint_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'vpc_endpoint_service_id' in local_var_params:
            path_params['vpc_endpoint_service_id'] = local_var_params['vpc_endpoint_service_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/vpc-endpoint-services/{vpc_endpoint_service_id}/connections/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='AcceptOrRejectEndpointResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def add_or_remove_service_permissions_async(self, request):
        """批量添加或移除终端节点服务的白名单

        功能介绍
        批量添加或移除当前用户下终端节点服务的白名单。
        说明
        本帐号默认在自身用户的终端节点服务的白名单中。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AddOrRemoveServicePermissions
        :type request: :class:`huaweicloudsdkvpcep.v1.AddOrRemoveServicePermissionsRequest`
        :rtype: :class:`huaweicloudsdkvpcep.v1.AddOrRemoveServicePermissionsResponse`
        """
        return self.add_or_remove_service_permissions_with_http_info(request)

    def add_or_remove_service_permissions_with_http_info(self, request):
        all_params = ['vpc_endpoint_service_id', 'add_or_remove_service_permissions_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'vpc_endpoint_service_id' in local_var_params:
            path_params['vpc_endpoint_service_id'] = local_var_params['vpc_endpoint_service_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/vpc-endpoint-services/{vpc_endpoint_service_id}/permissions/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='AddOrRemoveServicePermissionsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_add_endpoint_service_permissions_async(self, request):
        """批量添加或移除终端节点服务的白名单

        功能介绍
        批量添加当前用户下终端节点服务的白名单，支持添加描述信息。
        说明
        本帐号默认在自身用户的终端节点服务的白名单中。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchAddEndpointServicePermissions
        :type request: :class:`huaweicloudsdkvpcep.v1.BatchAddEndpointServicePermissionsRequest`
        :rtype: :class:`huaweicloudsdkvpcep.v1.BatchAddEndpointServicePermissionsResponse`
        """
        return self.batch_add_endpoint_service_permissions_with_http_info(request)

    def batch_add_endpoint_service_permissions_with_http_info(self, request):
        all_params = ['vpc_endpoint_service_id', 'batch_add_permission']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'vpc_endpoint_service_id' in local_var_params:
            path_params['vpc_endpoint_service_id'] = local_var_params['vpc_endpoint_service_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/vpc-endpoint-services/{vpc_endpoint_service_id}/permissions/batch-create',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchAddEndpointServicePermissionsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_remove_endpoint_service_permissions_async(self, request):
        """批量添加或移除终端节点服务的白名单

        功能介绍
        批量删除当前用户下终端节点服务的白名单
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchRemoveEndpointServicePermissions
        :type request: :class:`huaweicloudsdkvpcep.v1.BatchRemoveEndpointServicePermissionsRequest`
        :rtype: :class:`huaweicloudsdkvpcep.v1.BatchRemoveEndpointServicePermissionsResponse`
        """
        return self.batch_remove_endpoint_service_permissions_with_http_info(request)

    def batch_remove_endpoint_service_permissions_with_http_info(self, request):
        all_params = ['vpc_endpoint_service_id', 'batch_remove_permission_request']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'vpc_endpoint_service_id' in local_var_params:
            path_params['vpc_endpoint_service_id'] = local_var_params['vpc_endpoint_service_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/vpc-endpoint-services/{vpc_endpoint_service_id}/permissions/batch-delete',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchRemoveEndpointServicePermissionsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_endpoint_async(self, request):
        """创建终端节点

        功能介绍
        创建终端节点，以便访问终端节点服务。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateEndpoint
        :type request: :class:`huaweicloudsdkvpcep.v1.CreateEndpointRequest`
        :rtype: :class:`huaweicloudsdkvpcep.v1.CreateEndpointResponse`
        """
        return self.create_endpoint_with_http_info(request)

    def create_endpoint_with_http_info(self, request):
        all_params = ['create_endpoint_request_body']
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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/vpc-endpoints',
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

    def create_endpoint_service_async(self, request):
        """创建终端节点服务

        功能介绍
        创建终端节点服务，允许其他用户创建终端节点连接您创建的终端节点服务，
        使用您所提供的服务。
        说明
        该接口为异步接口，调用成功会返回200状态码，说明请求已正常下发。
        通常创建终端节点服务需要1~2分钟，可以通过查询终端节点服务详情查看创建结果。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateEndpointService
        :type request: :class:`huaweicloudsdkvpcep.v1.CreateEndpointServiceRequest`
        :rtype: :class:`huaweicloudsdkvpcep.v1.CreateEndpointServiceResponse`
        """
        return self.create_endpoint_service_with_http_info(request)

    def create_endpoint_service_with_http_info(self, request):
        all_params = ['create_endpoint_service_request_body']
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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/vpc-endpoint-services',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateEndpointServiceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_endpoint_async(self, request):
        """删除终端节点

        功能介绍
        删除终端节点。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteEndpoint
        :type request: :class:`huaweicloudsdkvpcep.v1.DeleteEndpointRequest`
        :rtype: :class:`huaweicloudsdkvpcep.v1.DeleteEndpointResponse`
        """
        return self.delete_endpoint_with_http_info(request)

    def delete_endpoint_with_http_info(self, request):
        all_params = ['vpc_endpoint_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'vpc_endpoint_id' in local_var_params:
            path_params['vpc_endpoint_id'] = local_var_params['vpc_endpoint_id']

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
            resource_path='/v1/{project_id}/vpc-endpoints/{vpc_endpoint_id}',
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

    def delete_endpoint_policy_async(self, request):
        """修改终端节点路由表

        功能介绍
        删除网关型终端节点policy。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteEndpointPolicy
        :type request: :class:`huaweicloudsdkvpcep.v1.DeleteEndpointPolicyRequest`
        :rtype: :class:`huaweicloudsdkvpcep.v1.DeleteEndpointPolicyResponse`
        """
        return self.delete_endpoint_policy_with_http_info(request)

    def delete_endpoint_policy_with_http_info(self, request):
        all_params = ['vpc_endpoint_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'vpc_endpoint_id' in local_var_params:
            path_params['vpc_endpoint_id'] = local_var_params['vpc_endpoint_id']

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
            resource_path='/v1/{project_id}/vpc-endpoints/{vpc_endpoint_id}/policy',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteEndpointPolicyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_endpoint_service_async(self, request):
        """删除终端节点服务

        功能介绍
        删除终端节点服务。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteEndpointService
        :type request: :class:`huaweicloudsdkvpcep.v1.DeleteEndpointServiceRequest`
        :rtype: :class:`huaweicloudsdkvpcep.v1.DeleteEndpointServiceResponse`
        """
        return self.delete_endpoint_service_with_http_info(request)

    def delete_endpoint_service_with_http_info(self, request):
        all_params = ['vpc_endpoint_service_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'vpc_endpoint_service_id' in local_var_params:
            path_params['vpc_endpoint_service_id'] = local_var_params['vpc_endpoint_service_id']

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
            resource_path='/v1/{project_id}/vpc-endpoint-services/{vpc_endpoint_service_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteEndpointServiceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_endpoint_info_details_async(self, request):
        """查询终端节点详情

        功能介绍
        查询终端节点的详细信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListEndpointInfoDetails
        :type request: :class:`huaweicloudsdkvpcep.v1.ListEndpointInfoDetailsRequest`
        :rtype: :class:`huaweicloudsdkvpcep.v1.ListEndpointInfoDetailsResponse`
        """
        return self.list_endpoint_info_details_with_http_info(request)

    def list_endpoint_info_details_with_http_info(self, request):
        all_params = ['vpc_endpoint_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'vpc_endpoint_id' in local_var_params:
            path_params['vpc_endpoint_id'] = local_var_params['vpc_endpoint_id']

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
            resource_path='/v1/{project_id}/vpc-endpoints/{vpc_endpoint_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListEndpointInfoDetailsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_endpoint_service_async(self, request):
        """查询终端节点服务列表

        功能介绍
        查询当前用户下的终端节点服务的列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListEndpointService
        :type request: :class:`huaweicloudsdkvpcep.v1.ListEndpointServiceRequest`
        :rtype: :class:`huaweicloudsdkvpcep.v1.ListEndpointServiceResponse`
        """
        return self.list_endpoint_service_with_http_info(request)

    def list_endpoint_service_with_http_info(self, request):
        all_params = ['endpoint_service_name', 'id', 'status', 'sort_key', 'sort_dir', 'limit', 'offset', 'public_border_group']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'endpoint_service_name' in local_var_params:
            query_params.append(('endpoint_service_name', local_var_params['endpoint_service_name']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'public_border_group' in local_var_params:
            query_params.append(('public_border_group', local_var_params['public_border_group']))

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
            resource_path='/v1/{project_id}/vpc-endpoint-services',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListEndpointServiceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_endpoints_async(self, request):
        """查询终端节点列表

        功能介绍
        查询当前用户下的终端节点的列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListEndpoints
        :type request: :class:`huaweicloudsdkvpcep.v1.ListEndpointsRequest`
        :rtype: :class:`huaweicloudsdkvpcep.v1.ListEndpointsResponse`
        """
        return self.list_endpoints_with_http_info(request)

    def list_endpoints_with_http_info(self, request):
        all_params = ['endpoint_service_name', 'vpc_id', 'id', 'limit', 'offset', 'sort_key', 'sort_dir', 'public_border_group']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'endpoint_service_name' in local_var_params:
            query_params.append(('endpoint_service_name', local_var_params['endpoint_service_name']))
        if 'vpc_id' in local_var_params:
            query_params.append(('vpc_id', local_var_params['vpc_id']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
        if 'public_border_group' in local_var_params:
            query_params.append(('public_border_group', local_var_params['public_border_group']))

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
            resource_path='/v1/{project_id}/vpc-endpoints',
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

    def list_quota_details_async(self, request):
        """查询配额

        功能介绍
        查询用户的资源配额，包括终端节点服务和终端节点。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListQuotaDetails
        :type request: :class:`huaweicloudsdkvpcep.v1.ListQuotaDetailsRequest`
        :rtype: :class:`huaweicloudsdkvpcep.v1.ListQuotaDetailsResponse`
        """
        return self.list_quota_details_with_http_info(request)

    def list_quota_details_with_http_info(self, request):
        all_params = ['type']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))

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
            resource_path='/v1/{project_id}/quotas',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListQuotaDetailsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_service_connections_async(self, request):
        """查询连接终端节点服务的连接列表

        功能介绍
        查询连接当前用户下的某一个终端节点服务的连接列表。marker_id是连接的唯一标识。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListServiceConnections
        :type request: :class:`huaweicloudsdkvpcep.v1.ListServiceConnectionsRequest`
        :rtype: :class:`huaweicloudsdkvpcep.v1.ListServiceConnectionsResponse`
        """
        return self.list_service_connections_with_http_info(request)

    def list_service_connections_with_http_info(self, request):
        all_params = ['vpc_endpoint_service_id', 'id', 'marker_id', 'status', 'sort_key', 'sort_dir', 'limit', 'offset']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'vpc_endpoint_service_id' in local_var_params:
            path_params['vpc_endpoint_service_id'] = local_var_params['vpc_endpoint_service_id']

        query_params = []
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'marker_id' in local_var_params:
            query_params.append(('marker_id', local_var_params['marker_id']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
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
            resource_path='/v1/{project_id}/vpc-endpoint-services/{vpc_endpoint_service_id}/connections',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListServiceConnectionsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_service_describe_details_async(self, request):
        """查询终端节点服务概要

        功能介绍
        查询终端节点服务的概要信息， 此接口是供创建终端节点的用户来查询需要连接的终端节点服务信息。 此接口既可以方便其他用户查询到您的终端节点服务概要信息, 又可以避免您的终端节点服务的细节信息暴露给其他用户。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListServiceDescribeDetails
        :type request: :class:`huaweicloudsdkvpcep.v1.ListServiceDescribeDetailsRequest`
        :rtype: :class:`huaweicloudsdkvpcep.v1.ListServiceDescribeDetailsResponse`
        """
        return self.list_service_describe_details_with_http_info(request)

    def list_service_describe_details_with_http_info(self, request):
        all_params = ['endpoint_service_name', 'id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'endpoint_service_name' in local_var_params:
            query_params.append(('endpoint_service_name', local_var_params['endpoint_service_name']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))

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
            resource_path='/v1/{project_id}/vpc-endpoint-services/describe',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListServiceDescribeDetailsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_service_details_async(self, request):
        """查询终端节点服务详情

        功能介绍
        查询终端节点服务的详细信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListServiceDetails
        :type request: :class:`huaweicloudsdkvpcep.v1.ListServiceDetailsRequest`
        :rtype: :class:`huaweicloudsdkvpcep.v1.ListServiceDetailsResponse`
        """
        return self.list_service_details_with_http_info(request)

    def list_service_details_with_http_info(self, request):
        all_params = ['vpc_endpoint_service_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'vpc_endpoint_service_id' in local_var_params:
            path_params['vpc_endpoint_service_id'] = local_var_params['vpc_endpoint_service_id']

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
            resource_path='/v1/{project_id}/vpc-endpoint-services/{vpc_endpoint_service_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListServiceDetailsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_service_permissions_details_async(self, request):
        """查询终端节点服务的白名单列表

        功能介绍
        查询当前用户下终端节点服务的白名单列表。
        说明
        本帐号默认在当前用户下终端节点服务的白名单中。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListServicePermissionsDetails
        :type request: :class:`huaweicloudsdkvpcep.v1.ListServicePermissionsDetailsRequest`
        :rtype: :class:`huaweicloudsdkvpcep.v1.ListServicePermissionsDetailsResponse`
        """
        return self.list_service_permissions_details_with_http_info(request)

    def list_service_permissions_details_with_http_info(self, request):
        all_params = ['vpc_endpoint_service_id', 'permission', 'limit', 'offset', 'sort_key', 'sort_dir']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'vpc_endpoint_service_id' in local_var_params:
            path_params['vpc_endpoint_service_id'] = local_var_params['vpc_endpoint_service_id']

        query_params = []
        if 'permission' in local_var_params:
            query_params.append(('permission', local_var_params['permission']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))

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
            resource_path='/v1/{project_id}/vpc-endpoint-services/{vpc_endpoint_service_id}/permissions',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListServicePermissionsDetailsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_service_public_details_async(self, request):
        """查询公共终端节点服务列表

        功能介绍
        查询公共终端节点服务的列表，公共终端节点服务是所有用户可见且可连接的终端节点服务，
        由运维人员创建，用户可直接使用，但无权创建。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListServicePublicDetails
        :type request: :class:`huaweicloudsdkvpcep.v1.ListServicePublicDetailsRequest`
        :rtype: :class:`huaweicloudsdkvpcep.v1.ListServicePublicDetailsResponse`
        """
        return self.list_service_public_details_with_http_info(request)

    def list_service_public_details_with_http_info(self, request):
        all_params = ['limit', 'offset', 'endpoint_service_name', 'id', 'sort_key', 'sort_dir']
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
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'endpoint_service_name' in local_var_params:
            query_params.append(('endpoint_service_name', local_var_params['endpoint_service_name']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))

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
            resource_path='/v1/{project_id}/vpc-endpoint-services/public',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListServicePublicDetailsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_specified_version_details_async(self, request):
        """查询指定VPC终端节点接口版本信息

        功能介绍
        查询指定VPC终端节点接口版本信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListSpecifiedVersionDetails
        :type request: :class:`huaweicloudsdkvpcep.v1.ListSpecifiedVersionDetailsRequest`
        :rtype: :class:`huaweicloudsdkvpcep.v1.ListSpecifiedVersionDetailsResponse`
        """
        return self.list_specified_version_details_with_http_info(request)

    def list_specified_version_details_with_http_info(self, request):
        all_params = ['version']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'version' in local_var_params:
            path_params['version'] = local_var_params['version']

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
            resource_path='/{version}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListSpecifiedVersionDetailsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_version_details_async(self, request):
        """查询VPC终端节点接口版本列表

        功能介绍
        查询VPC终端节点接口版本列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListVersionDetails
        :type request: :class:`huaweicloudsdkvpcep.v1.ListVersionDetailsRequest`
        :rtype: :class:`huaweicloudsdkvpcep.v1.ListVersionDetailsResponse`
        """
        return self.list_version_details_with_http_info(request)

    def list_version_details_with_http_info(self, request):
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
            resource_path='/',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListVersionDetailsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_endpoint_connections_desc_async(self, request):
        """更新终端节点连接描述

        功能介绍：
             更新终端节点服务连接的终端节点的描述。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateEndpointConnectionsDesc
        :type request: :class:`huaweicloudsdkvpcep.v1.UpdateEndpointConnectionsDescRequest`
        :rtype: :class:`huaweicloudsdkvpcep.v1.UpdateEndpointConnectionsDescResponse`
        """
        return self.update_endpoint_connections_desc_with_http_info(request)

    def update_endpoint_connections_desc_with_http_info(self, request):
        all_params = ['vpc_endpoint_service_id', 'update_ep_connections']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'vpc_endpoint_service_id' in local_var_params:
            path_params['vpc_endpoint_service_id'] = local_var_params['vpc_endpoint_service_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/vpc-endpoint-services/{vpc_endpoint_service_id}/connections/description',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateEndpointConnectionsDescResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_endpoint_policy_async(self, request):
        """修改终端节点路由表

        功能介绍
        修改网关型终端节点policy。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateEndpointPolicy
        :type request: :class:`huaweicloudsdkvpcep.v1.UpdateEndpointPolicyRequest`
        :rtype: :class:`huaweicloudsdkvpcep.v1.UpdateEndpointPolicyResponse`
        """
        return self.update_endpoint_policy_with_http_info(request)

    def update_endpoint_policy_with_http_info(self, request):
        all_params = ['vpc_endpoint_id', 'update_endpoint_policy_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'vpc_endpoint_id' in local_var_params:
            path_params['vpc_endpoint_id'] = local_var_params['vpc_endpoint_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/vpc-endpoints/{vpc_endpoint_id}/policy',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateEndpointPolicyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_endpoint_routetable_async(self, request):
        """修改终端节点路由表

        功能介绍
        修改终端节点路由表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateEndpointRoutetable
        :type request: :class:`huaweicloudsdkvpcep.v1.UpdateEndpointRoutetableRequest`
        :rtype: :class:`huaweicloudsdkvpcep.v1.UpdateEndpointRoutetableResponse`
        """
        return self.update_endpoint_routetable_with_http_info(request)

    def update_endpoint_routetable_with_http_info(self, request):
        all_params = ['vpc_endpoint_id', 'update_endpoint_routetable_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'vpc_endpoint_id' in local_var_params:
            path_params['vpc_endpoint_id'] = local_var_params['vpc_endpoint_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/vpc-endpoints/{vpc_endpoint_id}/routetables',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateEndpointRoutetableResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_endpoint_service_async(self, request):
        """修改终端节点服务

        功能介绍
        修改终端节点服务。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateEndpointService
        :type request: :class:`huaweicloudsdkvpcep.v1.UpdateEndpointServiceRequest`
        :rtype: :class:`huaweicloudsdkvpcep.v1.UpdateEndpointServiceResponse`
        """
        return self.update_endpoint_service_with_http_info(request)

    def update_endpoint_service_with_http_info(self, request):
        all_params = ['vpc_endpoint_service_id', 'update_endpoint_service_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'vpc_endpoint_service_id' in local_var_params:
            path_params['vpc_endpoint_service_id'] = local_var_params['vpc_endpoint_service_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/vpc-endpoint-services/{vpc_endpoint_service_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateEndpointServiceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_endpoint_service_name_async(self, request):
        """修改终端节点服务名称

        功能介绍
        修改终端节点服务名称
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateEndpointServiceName
        :type request: :class:`huaweicloudsdkvpcep.v1.UpdateEndpointServiceNameRequest`
        :rtype: :class:`huaweicloudsdkvpcep.v1.UpdateEndpointServiceNameResponse`
        """
        return self.update_endpoint_service_name_with_http_info(request)

    def update_endpoint_service_name_with_http_info(self, request):
        all_params = ['vpc_endpoint_service_id', 'update_endpoint_service_name_mode']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'vpc_endpoint_service_id' in local_var_params:
            path_params['vpc_endpoint_service_id'] = local_var_params['vpc_endpoint_service_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/vpc-endpoint-services/{vpc_endpoint_service_id}/name',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateEndpointServiceNameResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_endpoint_service_permission_desc_async(self, request):
        """更新终端节点服务白名单描述

        功能介绍
        更新当前用户下终端节点服务白名单的描述信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateEndpointServicePermissionDesc
        :type request: :class:`huaweicloudsdkvpcep.v1.UpdateEndpointServicePermissionDescRequest`
        :rtype: :class:`huaweicloudsdkvpcep.v1.UpdateEndpointServicePermissionDescResponse`
        """
        return self.update_endpoint_service_permission_desc_with_http_info(request)

    def update_endpoint_service_permission_desc_with_http_info(self, request):
        all_params = ['vpc_endpoint_service_id', 'permission_id', 'update_permission_desc_request']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'vpc_endpoint_service_id' in local_var_params:
            path_params['vpc_endpoint_service_id'] = local_var_params['vpc_endpoint_service_id']
        if 'permission_id' in local_var_params:
            path_params['permission_id'] = local_var_params['permission_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/vpc-endpoint-services/{vpc_endpoint_service_id}/permissions/{permission_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateEndpointServicePermissionDescResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_endpoint_white_async(self, request):
        """更新终端节点的白名单

        功能介绍
        更新或删除允许访问终端节点的白名单。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateEndpointWhite
        :type request: :class:`huaweicloudsdkvpcep.v1.UpdateEndpointWhiteRequest`
        :rtype: :class:`huaweicloudsdkvpcep.v1.UpdateEndpointWhiteResponse`
        """
        return self.update_endpoint_white_with_http_info(request)

    def update_endpoint_white_with_http_info(self, request):
        all_params = ['vpc_endpoint_id', 'update_endpoint_white_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'vpc_endpoint_id' in local_var_params:
            path_params['vpc_endpoint_id'] = local_var_params['vpc_endpoint_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/vpc-endpoints/{vpc_endpoint_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateEndpointWhiteResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_add_or_remove_resource_instance_async(self, request):
        """批量添加或删除资源标签接口

        功能介绍
        为指定Endpoint Service或Endpoint批量添加或删除标签。
        ● 一个资源上最多有10个标签。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchAddOrRemoveResourceInstance
        :type request: :class:`huaweicloudsdkvpcep.v1.BatchAddOrRemoveResourceInstanceRequest`
        :rtype: :class:`huaweicloudsdkvpcep.v1.BatchAddOrRemoveResourceInstanceResponse`
        """
        return self.batch_add_or_remove_resource_instance_with_http_info(request)

    def batch_add_or_remove_resource_instance_with_http_info(self, request):
        all_params = ['resource_type', 'resource_id', 'batch_add_or_remove_resource_instance_body']
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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/{resource_type}/{resource_id}/tags/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchAddOrRemoveResourceInstanceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_query_project_resource_tags_async(self, request):
        """查询租户资源标签接口

        功能介绍
        根据租户ID和资源类型，获取租户下资源的标签。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListQueryProjectResourceTags
        :type request: :class:`huaweicloudsdkvpcep.v1.ListQueryProjectResourceTagsRequest`
        :rtype: :class:`huaweicloudsdkvpcep.v1.ListQueryProjectResourceTagsResponse`
        """
        return self.list_query_project_resource_tags_with_http_info(request)

    def list_query_project_resource_tags_with_http_info(self, request):
        all_params = ['resource_type']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_type' in local_var_params:
            path_params['resource_type'] = local_var_params['resource_type']

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
            resource_path='/v1/{project_id}/{resource_type}/tags',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListQueryProjectResourceTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_resource_instances_async(self, request):
        """查询资源实例接口

        功能介绍
        使用标签过滤查询租户下资源的实例。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListResourceInstances
        :type request: :class:`huaweicloudsdkvpcep.v1.ListResourceInstancesRequest`
        :rtype: :class:`huaweicloudsdkvpcep.v1.ListResourceInstancesResponse`
        """
        return self.list_resource_instances_with_http_info(request)

    def list_resource_instances_with_http_info(self, request):
        all_params = ['resource_type', 'query_resource_instance_tags_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_type' in local_var_params:
            path_params['resource_type'] = local_var_params['resource_type']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/{resource_type}/resource_instances/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListResourceInstancesResponse',
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

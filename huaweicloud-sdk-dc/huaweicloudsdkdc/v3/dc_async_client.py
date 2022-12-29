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


class DcAsyncClient(Client):
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
        super(DcAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkdc.v3.model")
        self.preset_headers = {'User-Agent': 'HuaweiCloud-SDK-Python'}

    @classmethod
    def new_builder(cls, clazz=None):
        if clazz is None:
            return ClientBuilder(cls)

        if clazz.__name__ != "DcClient":
            raise TypeError("client type error, support client type is DcClient")

        return ClientBuilder(clazz)

    def create_hosted_direct_connect_async(self, request):
        """创建托管专线连接

        用于合作伙伴用户最终租户创建托管专线
        创建者必须拥有合作伙伴资质，并且已经构建好运营(hosting)专线
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateHostedDirectConnect
        :type request: :class:`huaweicloudsdkdc.v3.CreateHostedDirectConnectRequest`
        :rtype: :class:`huaweicloudsdkdc.v3.CreateHostedDirectConnectResponse`
        """
        return self.create_hosted_direct_connect_with_http_info(request)

    def create_hosted_direct_connect_with_http_info(self, request):
        all_params = ['create_hosted_direct_connect_request_body']
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
            resource_path='/v3/{project_id}/dcaas/hosted-connects',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateHostedDirectConnectResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_direct_connect_async(self, request):
        """删除物理连接

        删除物理连接，本接口只适用于按需计费物理专线，对于包周期购买的专线通过订单退订的方式删除物理连接
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteDirectConnect
        :type request: :class:`huaweicloudsdkdc.v3.DeleteDirectConnectRequest`
        :rtype: :class:`huaweicloudsdkdc.v3.DeleteDirectConnectResponse`
        """
        return self.delete_direct_connect_with_http_info(request)

    def delete_direct_connect_with_http_info(self, request):
        all_params = ['direct_connect_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'direct_connect_id' in local_var_params:
            path_params['direct_connect_id'] = local_var_params['direct_connect_id']

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
            resource_path='/v3/{project_id}/dcaas/direct-connects/{direct_connect_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteDirectConnectResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_hosted_direct_connect_async(self, request):
        """删除托管专线连接

        合作伙伴删除托管专线
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteHostedDirectConnect
        :type request: :class:`huaweicloudsdkdc.v3.DeleteHostedDirectConnectRequest`
        :rtype: :class:`huaweicloudsdkdc.v3.DeleteHostedDirectConnectResponse`
        """
        return self.delete_hosted_direct_connect_with_http_info(request)

    def delete_hosted_direct_connect_with_http_info(self, request):
        all_params = ['hosted_connect_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'hosted_connect_id' in local_var_params:
            path_params['hosted_connect_id'] = local_var_params['hosted_connect_id']

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
            resource_path='/v3/{project_id}/dcaas/hosted-connects/{hosted_connect_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteHostedDirectConnectResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_direct_connects_async(self, request):
        """查询物理连接列表

        查询租户创建的所有的direct connect对象.
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListDirectConnects
        :type request: :class:`huaweicloudsdkdc.v3.ListDirectConnectsRequest`
        :rtype: :class:`huaweicloudsdkdc.v3.ListDirectConnectsResponse`
        """
        return self.list_direct_connects_with_http_info(request)

    def list_direct_connects_with_http_info(self, request):
        all_params = ['limit', 'marker', 'fields', 'sort_key', 'sort_dir', 'hosting_id', 'enterprise_project_id', 'id', 'name']
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
        if 'fields' in local_var_params:
            query_params.append(('fields', local_var_params['fields']))
            collection_formats['fields'] = 'multi'
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
            collection_formats['sort_dir'] = 'multi'
        if 'hosting_id' in local_var_params:
            query_params.append(('hosting_id', local_var_params['hosting_id']))
            collection_formats['hosting_id'] = 'multi'
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
            collection_formats['enterprise_project_id'] = 'csv'
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
            collection_formats['id'] = 'multi'
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
            collection_formats['name'] = 'csv'

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
            resource_path='/v3/{project_id}/dcaas/direct-connects',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListDirectConnectsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_hosted_direct_connects_async(self, request):
        """查询租户的托管专线列表

        查询合作伙伴创建的托管专线连接列表.
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListHostedDirectConnects
        :type request: :class:`huaweicloudsdkdc.v3.ListHostedDirectConnectsRequest`
        :rtype: :class:`huaweicloudsdkdc.v3.ListHostedDirectConnectsResponse`
        """
        return self.list_hosted_direct_connects_with_http_info(request)

    def list_hosted_direct_connects_with_http_info(self, request):
        all_params = ['limit', 'marker', 'fields', 'sort_dir', 'sort_key', 'hosting_id', 'id', 'name']
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
        if 'fields' in local_var_params:
            query_params.append(('fields', local_var_params['fields']))
            collection_formats['fields'] = 'multi'
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
            collection_formats['sort_dir'] = 'multi'
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
        if 'hosting_id' in local_var_params:
            query_params.append(('hosting_id', local_var_params['hosting_id']))
            collection_formats['hosting_id'] = 'multi'
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
            collection_formats['id'] = 'multi'
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
            collection_formats['name'] = 'csv'

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
            resource_path='/v3/{project_id}/dcaas/hosted-connects',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListHostedDirectConnectsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_direct_connect_async(self, request):
        """查询物理连接详情

        查询物理连接详细信息.
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowDirectConnect
        :type request: :class:`huaweicloudsdkdc.v3.ShowDirectConnectRequest`
        :rtype: :class:`huaweicloudsdkdc.v3.ShowDirectConnectResponse`
        """
        return self.show_direct_connect_with_http_info(request)

    def show_direct_connect_with_http_info(self, request):
        all_params = ['direct_connect_id', 'limit', 'marker', 'fields']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'direct_connect_id' in local_var_params:
            path_params['direct_connect_id'] = local_var_params['direct_connect_id']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'fields' in local_var_params:
            query_params.append(('fields', local_var_params['fields']))
            collection_formats['fields'] = 'multi'

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
            resource_path='/v3/{project_id}/dcaas/direct-connects/{direct_connect_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowDirectConnectResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_hosted_direct_connect_async(self, request):
        """查询租户的托管专线详情

        查询合法作伙伴的Hosted专线类型.
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowHostedDirectConnect
        :type request: :class:`huaweicloudsdkdc.v3.ShowHostedDirectConnectRequest`
        :rtype: :class:`huaweicloudsdkdc.v3.ShowHostedDirectConnectResponse`
        """
        return self.show_hosted_direct_connect_with_http_info(request)

    def show_hosted_direct_connect_with_http_info(self, request):
        all_params = ['hosted_connect_id', 'limit', 'marker', 'fields', 'sort_dir', 'sort_key', 'hosting_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'hosted_connect_id' in local_var_params:
            path_params['hosted_connect_id'] = local_var_params['hosted_connect_id']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'fields' in local_var_params:
            query_params.append(('fields', local_var_params['fields']))
            collection_formats['fields'] = 'multi'
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
            collection_formats['sort_dir'] = 'multi'
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
        if 'hosting_id' in local_var_params:
            query_params.append(('hosting_id', local_var_params['hosting_id']))
            collection_formats['hosting_id'] = 'multi'

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
            resource_path='/v3/{project_id}/dcaas/hosted-connects/{hosted_connect_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowHostedDirectConnectResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_direct_connect_async(self, request):
        """更新物理连接信息

        更新物理连接信息，包括名字,描述等信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateDirectConnect
        :type request: :class:`huaweicloudsdkdc.v3.UpdateDirectConnectRequest`
        :rtype: :class:`huaweicloudsdkdc.v3.UpdateDirectConnectResponse`
        """
        return self.update_direct_connect_with_http_info(request)

    def update_direct_connect_with_http_info(self, request):
        all_params = ['direct_connect_id', 'update_direct_connect_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'direct_connect_id' in local_var_params:
            path_params['direct_connect_id'] = local_var_params['direct_connect_id']

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
            resource_path='/v3/{project_id}/dcaas/direct-connects/{direct_connect_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateDirectConnectResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_hosted_direct_connect_async(self, request):
        """更新托管专线连接

        合作伙伴创建托管专线.
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateHostedDirectConnect
        :type request: :class:`huaweicloudsdkdc.v3.UpdateHostedDirectConnectRequest`
        :rtype: :class:`huaweicloudsdkdc.v3.UpdateHostedDirectConnectResponse`
        """
        return self.update_hosted_direct_connect_with_http_info(request)

    def update_hosted_direct_connect_with_http_info(self, request):
        all_params = ['hosted_connect_id', 'update_hosted_direct_connect_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'hosted_connect_id' in local_var_params:
            path_params['hosted_connect_id'] = local_var_params['hosted_connect_id']

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
            resource_path='/v3/{project_id}/dcaas/hosted-connects/{hosted_connect_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateHostedDirectConnectResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_create_resource_tags_async(self, request):
        """批量添加删除资源标签

        - 为指定实例批量添加或删除标签
        - 标签管理服务需要使用该接口批量管理实例的标签。
        - 一个资源上最多有10个标签。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchCreateResourceTags
        :type request: :class:`huaweicloudsdkdc.v3.BatchCreateResourceTagsRequest`
        :rtype: :class:`huaweicloudsdkdc.v3.BatchCreateResourceTagsResponse`
        """
        return self.batch_create_resource_tags_with_http_info(request)

    def batch_create_resource_tags_with_http_info(self, request):
        all_params = ['resource_id', 'resource_type', 'batch_create_resource_tags_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_id' in local_var_params:
            path_params['resource_id'] = local_var_params['resource_id']
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
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/{resource_type}/{resource_id}/tags/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchCreateResourceTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_resource_tag_async(self, request):
        """添加资源标签

        - 一个资源上最多有10个标签。
        - 此接口为幂等接口：
        - 创建时，如果创建的标签已经存在（key相同），则覆盖。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateResourceTag
        :type request: :class:`huaweicloudsdkdc.v3.CreateResourceTagRequest`
        :rtype: :class:`huaweicloudsdkdc.v3.CreateResourceTagResponse`
        """
        return self.create_resource_tag_with_http_info(request)

    def create_resource_tag_with_http_info(self, request):
        all_params = ['resource_id', 'resource_type', 'create_resource_tag_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_id' in local_var_params:
            path_params['resource_id'] = local_var_params['resource_id']
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
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/{resource_type}/{resource_id}/tags',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateResourceTagResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_resource_tag_async(self, request):
        """删除资源标签

        删除时,不对标签字符集做校验，调用接口前必须要做encodeURI，服务端需要对接口uri做decodeURI。删除的key不存在报404，Key不能为空或者空字符串。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteResourceTag
        :type request: :class:`huaweicloudsdkdc.v3.DeleteResourceTagRequest`
        :rtype: :class:`huaweicloudsdkdc.v3.DeleteResourceTagResponse`
        """
        return self.delete_resource_tag_with_http_info(request)

    def delete_resource_tag_with_http_info(self, request):
        all_params = ['key', 'resource_id', 'resource_type']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'key' in local_var_params:
            path_params['key'] = local_var_params['key']
        if 'resource_id' in local_var_params:
            path_params['resource_id'] = local_var_params['resource_id']
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
            resource_path='/v3/{project_id}/{resource_type}/{resource_id}/tags/{key}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteResourceTagResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_project_tags_async(self, request):
        """查询项目标签

        - 查询租户在指定Project中实例类型的所有资源标签集合。
        - 标签管理服务需要能够列出当前租户全部已使用的资源标签集合，为各服务打资源标签和过滤实例时提供标签联想功能。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListProjectTags
        :type request: :class:`huaweicloudsdkdc.v3.ListProjectTagsRequest`
        :rtype: :class:`huaweicloudsdkdc.v3.ListProjectTagsResponse`
        """
        return self.list_project_tags_with_http_info(request)

    def list_project_tags_with_http_info(self, request):
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
            resource_path='/v3/{project_id}/{resource_type}/tags',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListProjectTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_tag_resource_instances_async(self, request):
        """通过标签查询资源实例

        通过标签查询资源实例
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListTagResourceInstances
        :type request: :class:`huaweicloudsdkdc.v3.ListTagResourceInstancesRequest`
        :rtype: :class:`huaweicloudsdkdc.v3.ListTagResourceInstancesResponse`
        """
        return self.list_tag_resource_instances_with_http_info(request)

    def list_tag_resource_instances_with_http_info(self, request):
        all_params = ['resource_type', 'list_tag_resource_instances_request_body']
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
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/{resource_type}/resource-instances/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListTagResourceInstancesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_resource_tag_async(self, request):
        """查询资源标签

        查询资源标签
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowResourceTag
        :type request: :class:`huaweicloudsdkdc.v3.ShowResourceTagRequest`
        :rtype: :class:`huaweicloudsdkdc.v3.ShowResourceTagResponse`
        """
        return self.show_resource_tag_with_http_info(request)

    def show_resource_tag_with_http_info(self, request):
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
            resource_path='/v3/{project_id}/{resource_type}/{resource_id}/tags',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowResourceTagResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_virtual_gateway_async(self, request):
        """创建虚拟网关

        创建虚拟网关
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateVirtualGateway
        :type request: :class:`huaweicloudsdkdc.v3.CreateVirtualGatewayRequest`
        :rtype: :class:`huaweicloudsdkdc.v3.CreateVirtualGatewayResponse`
        """
        return self.create_virtual_gateway_with_http_info(request)

    def create_virtual_gateway_with_http_info(self, request):
        all_params = ['create_virtual_gateway_request_body']
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
            resource_path='/v3/{project_id}/dcaas/virtual-gateways',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateVirtualGatewayResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_virtual_gateway_async(self, request):
        """删除虚拟网关

        删除指定的虚拟网关
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteVirtualGateway
        :type request: :class:`huaweicloudsdkdc.v3.DeleteVirtualGatewayRequest`
        :rtype: :class:`huaweicloudsdkdc.v3.DeleteVirtualGatewayResponse`
        """
        return self.delete_virtual_gateway_with_http_info(request)

    def delete_virtual_gateway_with_http_info(self, request):
        all_params = ['virtual_gateway_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'virtual_gateway_id' in local_var_params:
            path_params['virtual_gateway_id'] = local_var_params['virtual_gateway_id']

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
            resource_path='/v3/{project_id}/dcaas/virtual-gateways/{virtual_gateway_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteVirtualGatewayResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_virtual_gateways_async(self, request):
        """查询虚拟网关列表

        查询虚拟网关列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListVirtualGateways
        :type request: :class:`huaweicloudsdkdc.v3.ListVirtualGatewaysRequest`
        :rtype: :class:`huaweicloudsdkdc.v3.ListVirtualGatewaysResponse`
        """
        return self.list_virtual_gateways_with_http_info(request)

    def list_virtual_gateways_with_http_info(self, request):
        all_params = ['limit', 'marker', 'fields', 'sort_dir', 'sort_key', 'id', 'vpc_id']
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
        if 'fields' in local_var_params:
            query_params.append(('fields', local_var_params['fields']))
            collection_formats['fields'] = 'multi'
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
            collection_formats['sort_dir'] = 'multi'
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
            collection_formats['id'] = 'multi'
        if 'vpc_id' in local_var_params:
            query_params.append(('vpc_id', local_var_params['vpc_id']))
            collection_formats['vpc_id'] = 'multi'

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
            resource_path='/v3/{project_id}/dcaas/virtual-gateways',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListVirtualGatewaysResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_virtual_gateway_async(self, request):
        """查询虚拟网关详情

        查询指定虚拟网关的详细信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowVirtualGateway
        :type request: :class:`huaweicloudsdkdc.v3.ShowVirtualGatewayRequest`
        :rtype: :class:`huaweicloudsdkdc.v3.ShowVirtualGatewayResponse`
        """
        return self.show_virtual_gateway_with_http_info(request)

    def show_virtual_gateway_with_http_info(self, request):
        all_params = ['virtual_gateway_id', 'fields']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'virtual_gateway_id' in local_var_params:
            path_params['virtual_gateway_id'] = local_var_params['virtual_gateway_id']

        query_params = []
        if 'fields' in local_var_params:
            query_params.append(('fields', local_var_params['fields']))
            collection_formats['fields'] = 'multi'

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
            resource_path='/v3/{project_id}/dcaas/virtual-gateways/{virtual_gateway_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowVirtualGatewayResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_virtual_gateway_async(self, request):
        """更新虚拟网关信息

        更新虚拟网关的信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateVirtualGateway
        :type request: :class:`huaweicloudsdkdc.v3.UpdateVirtualGatewayRequest`
        :rtype: :class:`huaweicloudsdkdc.v3.UpdateVirtualGatewayResponse`
        """
        return self.update_virtual_gateway_with_http_info(request)

    def update_virtual_gateway_with_http_info(self, request):
        all_params = ['virtual_gateway_id', 'update_virtual_gateway_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'virtual_gateway_id' in local_var_params:
            path_params['virtual_gateway_id'] = local_var_params['virtual_gateway_id']

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
            resource_path='/v3/{project_id}/dcaas/virtual-gateways/{virtual_gateway_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateVirtualGatewayResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_virtual_interface_async(self, request):
        """创建虚拟接口

        虚拟接口配置物理专线上与客户互联的IP和路由等相关信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateVirtualInterface
        :type request: :class:`huaweicloudsdkdc.v3.CreateVirtualInterfaceRequest`
        :rtype: :class:`huaweicloudsdkdc.v3.CreateVirtualInterfaceResponse`
        """
        return self.create_virtual_interface_with_http_info(request)

    def create_virtual_interface_with_http_info(self, request):
        all_params = ['create_virtual_interface_request_body']
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
            resource_path='/v3/{project_id}/dcaas/virtual-interfaces',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateVirtualInterfaceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_virtual_interface_async(self, request):
        """删除虚拟接口

        删除虚拟接口
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteVirtualInterface
        :type request: :class:`huaweicloudsdkdc.v3.DeleteVirtualInterfaceRequest`
        :rtype: :class:`huaweicloudsdkdc.v3.DeleteVirtualInterfaceResponse`
        """
        return self.delete_virtual_interface_with_http_info(request)

    def delete_virtual_interface_with_http_info(self, request):
        all_params = ['virtual_interface_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'virtual_interface_id' in local_var_params:
            path_params['virtual_interface_id'] = local_var_params['virtual_interface_id']

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
            resource_path='/v3/{project_id}/dcaas/virtual-interfaces/{virtual_interface_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteVirtualInterfaceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_virtual_interfaces_async(self, request):
        """查询虚拟接口列表

        查询租户所有的虚拟接口列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListVirtualInterfaces
        :type request: :class:`huaweicloudsdkdc.v3.ListVirtualInterfacesRequest`
        :rtype: :class:`huaweicloudsdkdc.v3.ListVirtualInterfacesResponse`
        """
        return self.list_virtual_interfaces_with_http_info(request)

    def list_virtual_interfaces_with_http_info(self, request):
        all_params = ['limit', 'marker', 'fields', 'sort_dir', 'sort_key', 'enterprise_project_id', 'id', 'status', 'direct_connect_id', 'vgw_id']
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
        if 'fields' in local_var_params:
            query_params.append(('fields', local_var_params['fields']))
            collection_formats['fields'] = 'multi'
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
            collection_formats['sort_dir'] = 'multi'
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
            collection_formats['enterprise_project_id'] = 'csv'
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
            collection_formats['id'] = 'multi'
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
            collection_formats['status'] = 'multi'
        if 'direct_connect_id' in local_var_params:
            query_params.append(('direct_connect_id', local_var_params['direct_connect_id']))
            collection_formats['direct_connect_id'] = 'multi'
        if 'vgw_id' in local_var_params:
            query_params.append(('vgw_id', local_var_params['vgw_id']))
            collection_formats['vgw_id'] = 'multi'

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
            resource_path='/v3/{project_id}/dcaas/virtual-interfaces',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListVirtualInterfacesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_virtual_interface_async(self, request):
        """查询虚拟接口详情

        查询虚拟接口详细信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowVirtualInterface
        :type request: :class:`huaweicloudsdkdc.v3.ShowVirtualInterfaceRequest`
        :rtype: :class:`huaweicloudsdkdc.v3.ShowVirtualInterfaceResponse`
        """
        return self.show_virtual_interface_with_http_info(request)

    def show_virtual_interface_with_http_info(self, request):
        all_params = ['virtual_interface_id', 'fields']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'virtual_interface_id' in local_var_params:
            path_params['virtual_interface_id'] = local_var_params['virtual_interface_id']

        query_params = []
        if 'fields' in local_var_params:
            query_params.append(('fields', local_var_params['fields']))
            collection_formats['fields'] = 'multi'

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
            resource_path='/v3/{project_id}/dcaas/virtual-interfaces/{virtual_interface_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowVirtualInterfaceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_virtual_interface_async(self, request):
        """更新虚拟接口

        更新虚拟接口的详细信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateVirtualInterface
        :type request: :class:`huaweicloudsdkdc.v3.UpdateVirtualInterfaceRequest`
        :rtype: :class:`huaweicloudsdkdc.v3.UpdateVirtualInterfaceResponse`
        """
        return self.update_virtual_interface_with_http_info(request)

    def update_virtual_interface_with_http_info(self, request):
        all_params = ['virtual_interface_id', 'update_virtual_interface_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'virtual_interface_id' in local_var_params:
            path_params['virtual_interface_id'] = local_var_params['virtual_interface_id']

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
            resource_path='/v3/{project_id}/dcaas/virtual-interfaces/{virtual_interface_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateVirtualInterfaceResponse',
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

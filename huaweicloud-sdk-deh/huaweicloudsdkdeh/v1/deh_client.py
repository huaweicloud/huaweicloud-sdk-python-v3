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


class DeHClient(Client):
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
        super(DeHClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkdeh.v1.model")
        self.preset_headers = {'User-Agent': 'HuaweiCloud-SDK-Python'}

    @classmethod
    def new_builder(cls, clazz=None):
        if clazz is None:
            return ClientBuilder(cls)

        if clazz.__name__ != "DeHClient":
            raise TypeError("client type error, support client type is DeHClient")

        return ClientBuilder(clazz)

    def batch_create_dedicated_host_tags(self, request):
        """批量添加专属主机标签

        为指定专属主机批量添加标签。
        
        标签管理服务（TMS）使用该接口批量添加专属主机的标签。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for BatchCreateDedicatedHostTags
        :type request: :class:`huaweicloudsdkdeh.v1.BatchCreateDedicatedHostTagsRequest`
        :rtype: :class:`huaweicloudsdkdeh.v1.BatchCreateDedicatedHostTagsResponse`
        """
        return self.batch_create_dedicated_host_tags_with_http_info(request)

    def batch_create_dedicated_host_tags_with_http_info(self, request):
        all_params = ['dedicated_host_id', 'req_set_or_delete_tags']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'dedicated_host_id' in local_var_params:
            path_params['dedicated_host_id'] = local_var_params['dedicated_host_id']

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
            resource_path='/v1.0/{project_id}/dedicated-host-tags/{dedicated_host_id}/tags/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='BatchCreateDedicatedHostTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_delete_dedicated_host_tags(self, request):
        """批量删除专属主机标签

        批量删除指定专属主机标签。
        
        标签管理服务（TMS）使用该接口批量删除专属主机的标签。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for BatchDeleteDedicatedHostTags
        :type request: :class:`huaweicloudsdkdeh.v1.BatchDeleteDedicatedHostTagsRequest`
        :rtype: :class:`huaweicloudsdkdeh.v1.BatchDeleteDedicatedHostTagsResponse`
        """
        return self.batch_delete_dedicated_host_tags_with_http_info(request)

    def batch_delete_dedicated_host_tags_with_http_info(self, request):
        all_params = ['dedicated_host_id', 'req_set_or_delete_tags']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'dedicated_host_id' in local_var_params:
            path_params['dedicated_host_id'] = local_var_params['dedicated_host_id']

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
            resource_path='/v1.0/{project_id}/dedicated-host-tags/{dedicated_host_id}/tags/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='BatchDeleteDedicatedHostTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_dedicated_host(self, request):
        """分配专属主机

        分配一台或多台专属主机，需要设置实例规格、所属AZ、数量等参数。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for CreateDedicatedHost
        :type request: :class:`huaweicloudsdkdeh.v1.CreateDedicatedHostRequest`
        :rtype: :class:`huaweicloudsdkdeh.v1.CreateDedicatedHostResponse`
        """
        return self.create_dedicated_host_with_http_info(request)

    def create_dedicated_host_with_http_info(self, request):
        all_params = ['req_allocate_deh']
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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1.0/{project_id}/dedicated-hosts',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateDedicatedHostResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_dedicated_host(self, request):
        """释放专属主机

        释放专属主机。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for DeleteDedicatedHost
        :type request: :class:`huaweicloudsdkdeh.v1.DeleteDedicatedHostRequest`
        :rtype: :class:`huaweicloudsdkdeh.v1.DeleteDedicatedHostResponse`
        """
        return self.delete_dedicated_host_with_http_info(request)

    def delete_dedicated_host_with_http_info(self, request):
        all_params = ['dedicated_host_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'dedicated_host_id' in local_var_params:
            path_params['dedicated_host_id'] = local_var_params['dedicated_host_id']

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
            resource_path='/v1.0/{project_id}/dedicated-hosts/{dedicated_host_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteDedicatedHostResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_dedicated_host_types(self, request):
        """查询可用的专属主机类型

        查询某一AZ内可用的专属主机类型。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListDedicatedHostTypes
        :type request: :class:`huaweicloudsdkdeh.v1.ListDedicatedHostTypesRequest`
        :rtype: :class:`huaweicloudsdkdeh.v1.ListDedicatedHostTypesResponse`
        """
        return self.list_dedicated_host_types_with_http_info(request)

    def list_dedicated_host_types_with_http_info(self, request):
        all_params = ['availability_zone']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'availability_zone' in local_var_params:
            path_params['availability_zone'] = local_var_params['availability_zone']

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
            resource_path='/v1.0/{project_id}/availability-zone/{availability_zone}/dedicated-host-types',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListDedicatedHostTypesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_dedicated_hosts(self, request):
        """查询专属主机列表

        通过该接口查询专属主机列表。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListDedicatedHosts
        :type request: :class:`huaweicloudsdkdeh.v1.ListDedicatedHostsRequest`
        :rtype: :class:`huaweicloudsdkdeh.v1.ListDedicatedHostsResponse`
        """
        return self.list_dedicated_hosts_with_http_info(request)

    def list_dedicated_hosts_with_http_info(self, request):
        all_params = ['dedicated_host_id', 'name', 'host_type', 'host_type_name', 'flavor', 'state', 'tenant', 'availability_zone', 'limit', 'marker', 'tags', 'instance_uuid', 'released_at', 'changes_since']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'dedicated_host_id' in local_var_params:
            query_params.append(('dedicated_host_id', local_var_params['dedicated_host_id']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'host_type' in local_var_params:
            query_params.append(('host_type', local_var_params['host_type']))
        if 'host_type_name' in local_var_params:
            query_params.append(('host_type_name', local_var_params['host_type_name']))
        if 'flavor' in local_var_params:
            query_params.append(('flavor', local_var_params['flavor']))
        if 'state' in local_var_params:
            query_params.append(('state', local_var_params['state']))
        if 'tenant' in local_var_params:
            query_params.append(('tenant', local_var_params['tenant']))
        if 'availability_zone' in local_var_params:
            query_params.append(('availability_zone', local_var_params['availability_zone']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'tags' in local_var_params:
            query_params.append(('tags', local_var_params['tags']))
        if 'instance_uuid' in local_var_params:
            query_params.append(('instance_uuid', local_var_params['instance_uuid']))
        if 'released_at' in local_var_params:
            query_params.append(('released_at', local_var_params['released_at']))
        if 'changes_since' in local_var_params:
            query_params.append(('changes-since', local_var_params['changes_since']))

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
            resource_path='/v1.0/{project_id}/dedicated-hosts',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListDedicatedHostsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_dedicated_hosts_by_tags(self, request):
        """按标签查询专属主机列表

        使用标签过滤专属主机列表，并返回专属主机使用的所有标签。
        
        标签管理服务（TMS）使用该接口过滤专属主机列表。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListDedicatedHostsByTags
        :type request: :class:`huaweicloudsdkdeh.v1.ListDedicatedHostsByTagsRequest`
        :rtype: :class:`huaweicloudsdkdeh.v1.ListDedicatedHostsByTagsResponse`
        """
        return self.list_dedicated_hosts_by_tags_with_http_info(request)

    def list_dedicated_hosts_by_tags_with_http_info(self, request):
        all_params = ['req_list_deh_by_tags']
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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1.0/{project_id}/dedicated-host-tags/resource_instances/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListDedicatedHostsByTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_servers_dedicated_host(self, request):
        """查询专属主机上的云服务器

        查询专属主机上已部署的云服务器信息。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListServersDedicatedHost
        :type request: :class:`huaweicloudsdkdeh.v1.ListServersDedicatedHostRequest`
        :rtype: :class:`huaweicloudsdkdeh.v1.ListServersDedicatedHostResponse`
        """
        return self.list_servers_dedicated_host_with_http_info(request)

    def list_servers_dedicated_host_with_http_info(self, request):
        all_params = ['dedicated_host_id', 'limit', 'marker']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'dedicated_host_id' in local_var_params:
            path_params['dedicated_host_id'] = local_var_params['dedicated_host_id']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))

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
            resource_path='/v1.0/{project_id}/dedicated-hosts/{dedicated_host_id}/servers',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListServersDedicatedHostResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_dedicated_host(self, request):
        """查询专属主机详情

        查询某一台专属主机的详情。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowDedicatedHost
        :type request: :class:`huaweicloudsdkdeh.v1.ShowDedicatedHostRequest`
        :rtype: :class:`huaweicloudsdkdeh.v1.ShowDedicatedHostResponse`
        """
        return self.show_dedicated_host_with_http_info(request)

    def show_dedicated_host_with_http_info(self, request):
        all_params = ['dedicated_host_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'dedicated_host_id' in local_var_params:
            path_params['dedicated_host_id'] = local_var_params['dedicated_host_id']

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
            resource_path='/v1.0/{project_id}/dedicated-hosts/{dedicated_host_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowDedicatedHostResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_dedicated_host_tags(self, request):
        """查询指定专属主机标签

        查询指定专属主机的标签信息。
        
        标签管理服务（TMS）使用该接口查询指定专属主机的全部标签数据。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowDedicatedHostTags
        :type request: :class:`huaweicloudsdkdeh.v1.ShowDedicatedHostTagsRequest`
        :rtype: :class:`huaweicloudsdkdeh.v1.ShowDedicatedHostTagsResponse`
        """
        return self.show_dedicated_host_tags_with_http_info(request)

    def show_dedicated_host_tags_with_http_info(self, request):
        all_params = ['dedicated_host_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'dedicated_host_id' in local_var_params:
            path_params['dedicated_host_id'] = local_var_params['dedicated_host_id']

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
            resource_path='/v1.0/{project_id}/dedicated-host-tags/{dedicated_host_id}/tags',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowDedicatedHostTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_quota_sets(self, request):
        """查询租户的专属主机配额

        该接口用于查询租户的专属主机配额。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowQuotaSets
        :type request: :class:`huaweicloudsdkdeh.v1.ShowQuotaSetsRequest`
        :rtype: :class:`huaweicloudsdkdeh.v1.ShowQuotaSetsResponse`
        """
        return self.show_quota_sets_with_http_info(request)

    def show_quota_sets_with_http_info(self, request):
        all_params = ['tenant_id', 'resource']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'tenant_id' in local_var_params:
            path_params['tenant_id'] = local_var_params['tenant_id']

        query_params = []
        if 'resource' in local_var_params:
            query_params.append(('resource', local_var_params['resource']))

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
            resource_path='/v1.0/{project_id}/quota-sets/{tenant_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowQuotaSetsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_dedicated_host(self, request):
        """更新专属主机属性

        该接口用于变更专属主机的“auto_placement”和“name”属性。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for UpdateDedicatedHost
        :type request: :class:`huaweicloudsdkdeh.v1.UpdateDedicatedHostRequest`
        :rtype: :class:`huaweicloudsdkdeh.v1.UpdateDedicatedHostResponse`
        """
        return self.update_dedicated_host_with_http_info(request)

    def update_dedicated_host_with_http_info(self, request):
        all_params = ['dedicated_host_id', 'req_update_deh']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'dedicated_host_id' in local_var_params:
            path_params['dedicated_host_id'] = local_var_params['dedicated_host_id']

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
            resource_path='/v1.0/{project_id}/dedicated-hosts/{dedicated_host_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateDedicatedHostResponse',
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

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


class DnsClient(Client):
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
        super(DnsClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkdns.v2.model")
        self.preset_headers = {'User-Agent': 'HuaweiCloud-SDK-Python'}

    @classmethod
    def new_builder(cls, clazz=None):
        if clazz is None:
            return ClientBuilder(cls)

        if clazz.__name__ != "DnsClient":
            raise TypeError("client type error, support client type is DnsClient")

        return ClientBuilder(clazz)

    def create_custom_line(self, request):
        """创建单个自定义线路

        创建单个自定义线路
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for CreateCustomLine
        :type request: :class:`huaweicloudsdkdns.v2.CreateCustomLineRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.CreateCustomLineResponse`
        """
        return self.create_custom_line_with_http_info(request)

    def create_custom_line_with_http_info(self, request):
        all_params = ['create_custom_lines']
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
            resource_path='/v2.1/customlines',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateCustomLineResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_custom_line(self, request):
        """删除单个自定义线路

        删除单个自定义线路
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for DeleteCustomLine
        :type request: :class:`huaweicloudsdkdns.v2.DeleteCustomLineRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.DeleteCustomLineResponse`
        """
        return self.delete_custom_line_with_http_info(request)

    def delete_custom_line_with_http_info(self, request):
        all_params = ['line_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'line_id' in local_var_params:
            path_params['line_id'] = local_var_params['line_id']

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
            resource_path='/v2.1/customlines/{line_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteCustomLineResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_api_versions(self, request):
        """查询所有的云解析服务API版本号

        查询所有的云解析服务API版本号列表
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListApiVersions
        :type request: :class:`huaweicloudsdkdns.v2.ListApiVersionsRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.ListApiVersionsResponse`
        """
        return self.list_api_versions_with_http_info(request)

    def list_api_versions_with_http_info(self, request):
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
            response_type='ListApiVersionsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_custom_line(self, request):
        """查询自定义线路

        查询自定义线路
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListCustomLine
        :type request: :class:`huaweicloudsdkdns.v2.ListCustomLineRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.ListCustomLineResponse`
        """
        return self.list_custom_line_with_http_info(request)

    def list_custom_line_with_http_info(self, request):
        all_params = ['line_id', 'name', 'limit', 'offset', 'show_detail']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'line_id' in local_var_params:
            query_params.append(('line_id', local_var_params['line_id']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'show_detail' in local_var_params:
            query_params.append(('show_detail', local_var_params['show_detail']))

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
            resource_path='/v2.1/customlines',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListCustomLineResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_name_servers(self, request):
        """查询名称服务器列表

        查询名称服务器列表
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListNameServers
        :type request: :class:`huaweicloudsdkdns.v2.ListNameServersRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.ListNameServersResponse`
        """
        return self.list_name_servers_with_http_info(request)

    def list_name_servers_with_http_info(self, request):
        all_params = ['type', 'region']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'region' in local_var_params:
            query_params.append(('region', local_var_params['region']))

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
            resource_path='/v2/nameservers',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListNameServersResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_api_info(self, request):
        """查询指定的云解析服务API版本号

        查询指定的云解析服务API版本号
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowApiInfo
        :type request: :class:`huaweicloudsdkdns.v2.ShowApiInfoRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.ShowApiInfoResponse`
        """
        return self.show_api_info_with_http_info(request)

    def show_api_info_with_http_info(self, request):
        all_params = ['version']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='ShowApiInfoResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_domain_quota(self, request):
        """查询租户配额

        查询单租户在DNS服务下的资源配额，包括公网zone配额、内网zone配额、Record Set配额、PTR Record配额、入站终端节点配额、出站终端节点配额、自定义线路配额、线路分组配额等。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowDomainQuota
        :type request: :class:`huaweicloudsdkdns.v2.ShowDomainQuotaRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.ShowDomainQuotaResponse`
        """
        return self.show_domain_quota_with_http_info(request)

    def show_domain_quota_with_http_info(self, request):
        all_params = ['domain_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'domain_id' in local_var_params:
            query_params.append(('domain_id', local_var_params['domain_id']))

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
            resource_path='/v2/quotamg/dns/quotas',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowDomainQuotaResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_custom_line(self, request):
        """更新单个自定义线路

        更新单个自定义线路
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for UpdateCustomLine
        :type request: :class:`huaweicloudsdkdns.v2.UpdateCustomLineRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.UpdateCustomLineResponse`
        """
        return self.update_custom_line_with_http_info(request)

    def update_custom_line_with_http_info(self, request):
        all_params = ['line_id', 'update_customs_line_req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'line_id' in local_var_params:
            path_params['line_id'] = local_var_params['line_id']

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
            resource_path='/v2.1/customlines/{line_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateCustomLineResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_eip_record_set(self, request):
        """设置弹性IP的PTR记录

        设置弹性IP的PTR记录
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for CreateEipRecordSet
        :type request: :class:`huaweicloudsdkdns.v2.CreateEipRecordSetRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.CreateEipRecordSetResponse`
        """
        return self.create_eip_record_set_with_http_info(request)

    def create_eip_record_set_with_http_info(self, request):
        all_params = ['region', 'floatingip_id', 'create_ptr_req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'region' in local_var_params:
            path_params['region'] = local_var_params['region']
        if 'floatingip_id' in local_var_params:
            path_params['floatingip_id'] = local_var_params['floatingip_id']

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
            resource_path='/v2/reverse/floatingips/{region}:{floatingip_id}',
            method='PATCH',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateEipRecordSetResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_ptr_records(self, request):
        """查询租户弹性IP的PTR记录列表

        查询租户弹性IP的PTR记录列表
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListPtrRecords
        :type request: :class:`huaweicloudsdkdns.v2.ListPtrRecordsRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.ListPtrRecordsResponse`
        """
        return self.list_ptr_records_with_http_info(request)

    def list_ptr_records_with_http_info(self, request):
        all_params = ['marker', 'limit', 'offset', 'enterprise_project_id', 'tags', 'status']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'tags' in local_var_params:
            query_params.append(('tags', local_var_params['tags']))
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
            resource_path='/v2/reverse/floatingips',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListPtrRecordsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def restore_ptr_record(self, request):
        """将弹性IP的PTR记录恢复为默认值

        将弹性IP的PTR记录恢复为默认值
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for RestorePtrRecord
        :type request: :class:`huaweicloudsdkdns.v2.RestorePtrRecordRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.RestorePtrRecordResponse`
        """
        return self.restore_ptr_record_with_http_info(request)

    def restore_ptr_record_with_http_info(self, request):
        all_params = ['region', 'floatingip_id', 'restore_ptr_req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'region' in local_var_params:
            path_params['region'] = local_var_params['region']
        if 'floatingip_id' in local_var_params:
            path_params['floatingip_id'] = local_var_params['floatingip_id']

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
            resource_path='/v2/reverse/floatingips/{region}:{floatingip_id}',
            method='PATCH',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='RestorePtrRecordResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_ptr_record_set(self, request):
        """查询单个弹性IP的PTR记录

        查询单个弹性IP的PTR记录
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowPtrRecordSet
        :type request: :class:`huaweicloudsdkdns.v2.ShowPtrRecordSetRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.ShowPtrRecordSetResponse`
        """
        return self.show_ptr_record_set_with_http_info(request)

    def show_ptr_record_set_with_http_info(self, request):
        all_params = ['region', 'floatingip_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'region' in local_var_params:
            path_params['region'] = local_var_params['region']
        if 'floatingip_id' in local_var_params:
            path_params['floatingip_id'] = local_var_params['floatingip_id']

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
            resource_path='/v2/reverse/floatingips/{region}:{floatingip_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowPtrRecordSetResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_ptr_record(self, request):
        """修改弹性IP的PTR记录

        修改弹性IP的PTR记录
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for UpdatePtrRecord
        :type request: :class:`huaweicloudsdkdns.v2.UpdatePtrRecordRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.UpdatePtrRecordResponse`
        """
        return self.update_ptr_record_with_http_info(request)

    def update_ptr_record_with_http_info(self, request):
        all_params = ['region', 'floatingip_id', 'update_ptr_req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'region' in local_var_params:
            path_params['region'] = local_var_params['region']
        if 'floatingip_id' in local_var_params:
            path_params['floatingip_id'] = local_var_params['floatingip_id']

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
            resource_path='/v2/reverse/floatingips/{region}:{floatingip_id}',
            method='PATCH',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdatePtrRecordResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_delete_record_set_with_line(self, request):
        """批量删除某个Zone下的Record Set资源。

        批量删除某个Zone下的Record Set资源，当删除的资源不存在时，则默认删除成功。
        响应结果中只包含本次实际删除的资源。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for BatchDeleteRecordSetWithLine
        :type request: :class:`huaweicloudsdkdns.v2.BatchDeleteRecordSetWithLineRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.BatchDeleteRecordSetWithLineResponse`
        """
        return self.batch_delete_record_set_with_line_with_http_info(request)

    def batch_delete_record_set_with_line_with_http_info(self, request):
        all_params = ['zone_id', 'batch_delete_r_set_with_line_req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'zone_id' in local_var_params:
            path_params['zone_id'] = local_var_params['zone_id']

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
            resource_path='/v2.1/zones/{zone_id}/recordsets',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='BatchDeleteRecordSetWithLineResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_update_record_set_with_line(self, request):
        """批量修改RecordSet。

        批量修改RecordSet。属于原子性操作，请求Record Set将全部完成修改，或不做任何修改。
        仅公网Zone支持。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for BatchUpdateRecordSetWithLine
        :type request: :class:`huaweicloudsdkdns.v2.BatchUpdateRecordSetWithLineRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.BatchUpdateRecordSetWithLineResponse`
        """
        return self.batch_update_record_set_with_line_with_http_info(request)

    def batch_update_record_set_with_line_with_http_info(self, request):
        all_params = ['zone_id', 'batch_update_record_set_with_line_req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'zone_id' in local_var_params:
            path_params['zone_id'] = local_var_params['zone_id']

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
            resource_path='/v2.1/zones/{zone_id}/recordsets',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='BatchUpdateRecordSetWithLineResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_record_set(self, request):
        """创建单个Record Set

        创建单个Record Set
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for CreateRecordSet
        :type request: :class:`huaweicloudsdkdns.v2.CreateRecordSetRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.CreateRecordSetResponse`
        """
        return self.create_record_set_with_http_info(request)

    def create_record_set_with_http_info(self, request):
        all_params = ['zone_id', 'create_record_set_req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'zone_id' in local_var_params:
            path_params['zone_id'] = local_var_params['zone_id']

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
            resource_path='/v2/zones/{zone_id}/recordsets',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateRecordSetResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_record_set_with_batch_lines(self, request):
        """批量线路创建RecordSet。仅公网Zone支持。

        批量线路创建RecordSet。属于原子性操作，如果存在一个参数校验不通过，则创建失败。仅公网Zone支持。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for CreateRecordSetWithBatchLines
        :type request: :class:`huaweicloudsdkdns.v2.CreateRecordSetWithBatchLinesRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.CreateRecordSetWithBatchLinesResponse`
        """
        return self.create_record_set_with_batch_lines_with_http_info(request)

    def create_record_set_with_batch_lines_with_http_info(self, request):
        all_params = ['zone_id', 'create_r_set_batch_lines_req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'zone_id' in local_var_params:
            path_params['zone_id'] = local_var_params['zone_id']

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
            resource_path='/v2.1/zones/{zone_id}/recordsets/batch/lines',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateRecordSetWithBatchLinesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_record_set_with_line(self, request):
        """创建单个Record Set，仅适用于公网DNS

        创建单个Record Set，仅适用于公网DNS
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for CreateRecordSetWithLine
        :type request: :class:`huaweicloudsdkdns.v2.CreateRecordSetWithLineRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.CreateRecordSetWithLineResponse`
        """
        return self.create_record_set_with_line_with_http_info(request)

    def create_record_set_with_line_with_http_info(self, request):
        all_params = ['zone_id', 'create_record_set_with_line_req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'zone_id' in local_var_params:
            path_params['zone_id'] = local_var_params['zone_id']

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
            resource_path='/v2.1/zones/{zone_id}/recordsets',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateRecordSetWithLineResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_record_set(self, request):
        """删除单个Record Set

        删除单个Record Set
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for DeleteRecordSet
        :type request: :class:`huaweicloudsdkdns.v2.DeleteRecordSetRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.DeleteRecordSetResponse`
        """
        return self.delete_record_set_with_http_info(request)

    def delete_record_set_with_http_info(self, request):
        all_params = ['zone_id', 'recordset_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'zone_id' in local_var_params:
            path_params['zone_id'] = local_var_params['zone_id']
        if 'recordset_id' in local_var_params:
            path_params['recordset_id'] = local_var_params['recordset_id']

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
            resource_path='/v2/zones/{zone_id}/recordsets/{recordset_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteRecordSetResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_record_sets(self, request):
        """删除单个Record Set

        删除单个Record Set
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for DeleteRecordSets
        :type request: :class:`huaweicloudsdkdns.v2.DeleteRecordSetsRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.DeleteRecordSetsResponse`
        """
        return self.delete_record_sets_with_http_info(request)

    def delete_record_sets_with_http_info(self, request):
        all_params = ['zone_id', 'recordset_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'zone_id' in local_var_params:
            path_params['zone_id'] = local_var_params['zone_id']
        if 'recordset_id' in local_var_params:
            path_params['recordset_id'] = local_var_params['recordset_id']

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
            resource_path='/v2.1/zones/{zone_id}/recordsets/{recordset_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteRecordSetsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_record_sets(self, request):
        """查询租户Record Set资源列表

        查询租户Record Set资源列表
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListRecordSets
        :type request: :class:`huaweicloudsdkdns.v2.ListRecordSetsRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.ListRecordSetsResponse`
        """
        return self.list_record_sets_with_http_info(request)

    def list_record_sets_with_http_info(self, request):
        all_params = ['zone_type', 'marker', 'limit', 'offset', 'tags', 'status', 'type', 'name', 'id', 'records', 'sort_key', 'sort_dir']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'zone_type' in local_var_params:
            query_params.append(('zone_type', local_var_params['zone_type']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'tags' in local_var_params:
            query_params.append(('tags', local_var_params['tags']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'records' in local_var_params:
            query_params.append(('records', local_var_params['records']))
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
            resource_path='/v2/recordsets',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListRecordSetsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_record_sets_by_zone(self, request):
        """查询单个Zone下Record Set列表

        查询单个Zone下Record Set列表
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListRecordSetsByZone
        :type request: :class:`huaweicloudsdkdns.v2.ListRecordSetsByZoneRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.ListRecordSetsByZoneResponse`
        """
        return self.list_record_sets_by_zone_with_http_info(request)

    def list_record_sets_by_zone_with_http_info(self, request):
        all_params = ['zone_id', 'marker', 'limit', 'offset', 'tags', 'status', 'type', 'name', 'id', 'sort_key', 'sort_dir']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'zone_id' in local_var_params:
            path_params['zone_id'] = local_var_params['zone_id']

        query_params = []
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'tags' in local_var_params:
            query_params.append(('tags', local_var_params['tags']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
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
            resource_path='/v2/zones/{zone_id}/recordsets',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListRecordSetsByZoneResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_record_sets_with_line(self, request):
        """查询租户Record Set资源列表

        查询租户Record Set资源列表
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListRecordSetsWithLine
        :type request: :class:`huaweicloudsdkdns.v2.ListRecordSetsWithLineRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.ListRecordSetsWithLineResponse`
        """
        return self.list_record_sets_with_line_with_http_info(request)

    def list_record_sets_with_line_with_http_info(self, request):
        all_params = ['zone_type', 'marker', 'limit', 'offset', 'line_id', 'tags', 'status', 'type', 'name', 'id', 'records', 'sort_key', 'sort_dir', 'health_check_id', 'search_mode']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'zone_type' in local_var_params:
            query_params.append(('zone_type', local_var_params['zone_type']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'line_id' in local_var_params:
            query_params.append(('line_id', local_var_params['line_id']))
        if 'tags' in local_var_params:
            query_params.append(('tags', local_var_params['tags']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'records' in local_var_params:
            query_params.append(('records', local_var_params['records']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
        if 'health_check_id' in local_var_params:
            query_params.append(('health_check_id', local_var_params['health_check_id']))
        if 'search_mode' in local_var_params:
            query_params.append(('search_mode', local_var_params['search_mode']))

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
            resource_path='/v2.1/recordsets',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListRecordSetsWithLineResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def set_record_sets_status(self, request):
        """设置Record Set状态

        设置Record Set状态
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for SetRecordSetsStatus
        :type request: :class:`huaweicloudsdkdns.v2.SetRecordSetsStatusRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.SetRecordSetsStatusResponse`
        """
        return self.set_record_sets_status_with_http_info(request)

    def set_record_sets_status_with_http_info(self, request):
        all_params = ['recordset_id', 'set_record_sets_status_req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'recordset_id' in local_var_params:
            path_params['recordset_id'] = local_var_params['recordset_id']

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
            resource_path='/v2.1/recordsets/{recordset_id}/statuses/set',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='SetRecordSetsStatusResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_record_set(self, request):
        """查询单个Record Set

        查询单个Record Set
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowRecordSet
        :type request: :class:`huaweicloudsdkdns.v2.ShowRecordSetRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.ShowRecordSetResponse`
        """
        return self.show_record_set_with_http_info(request)

    def show_record_set_with_http_info(self, request):
        all_params = ['zone_id', 'recordset_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'zone_id' in local_var_params:
            path_params['zone_id'] = local_var_params['zone_id']
        if 'recordset_id' in local_var_params:
            path_params['recordset_id'] = local_var_params['recordset_id']

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
            resource_path='/v2/zones/{zone_id}/recordsets/{recordset_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowRecordSetResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_record_set_by_zone(self, request):
        """查询单个Zone下Record Set列表

        查询单个Zone下Record Set列表
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowRecordSetByZone
        :type request: :class:`huaweicloudsdkdns.v2.ShowRecordSetByZoneRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.ShowRecordSetByZoneResponse`
        """
        return self.show_record_set_by_zone_with_http_info(request)

    def show_record_set_by_zone_with_http_info(self, request):
        all_params = ['zone_id', 'marker', 'limit', 'offset', 'line_id', 'tags', 'status', 'type', 'name', 'id', 'sort_key', 'sort_dir', 'search_mode']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'zone_id' in local_var_params:
            path_params['zone_id'] = local_var_params['zone_id']

        query_params = []
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'line_id' in local_var_params:
            query_params.append(('line_id', local_var_params['line_id']))
        if 'tags' in local_var_params:
            query_params.append(('tags', local_var_params['tags']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
        if 'search_mode' in local_var_params:
            query_params.append(('search_mode', local_var_params['search_mode']))

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
            resource_path='/v2.1/zones/{zone_id}/recordsets',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowRecordSetByZoneResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_record_set_with_line(self, request):
        """查询单个Record Set，仅适用于公网DNS

        查询单个Record Set，仅适用于公网DNS
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowRecordSetWithLine
        :type request: :class:`huaweicloudsdkdns.v2.ShowRecordSetWithLineRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.ShowRecordSetWithLineResponse`
        """
        return self.show_record_set_with_line_with_http_info(request)

    def show_record_set_with_line_with_http_info(self, request):
        all_params = ['zone_id', 'recordset_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'zone_id' in local_var_params:
            path_params['zone_id'] = local_var_params['zone_id']
        if 'recordset_id' in local_var_params:
            path_params['recordset_id'] = local_var_params['recordset_id']

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
            resource_path='/v2.1/zones/{zone_id}/recordsets/{recordset_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowRecordSetWithLineResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_record_set(self, request):
        """修改单个Record Set

        修改单个Record Set
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for UpdateRecordSet
        :type request: :class:`huaweicloudsdkdns.v2.UpdateRecordSetRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.UpdateRecordSetResponse`
        """
        return self.update_record_set_with_http_info(request)

    def update_record_set_with_http_info(self, request):
        all_params = ['zone_id', 'recordset_id', 'update_record_set_req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'zone_id' in local_var_params:
            path_params['zone_id'] = local_var_params['zone_id']
        if 'recordset_id' in local_var_params:
            path_params['recordset_id'] = local_var_params['recordset_id']

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
            resource_path='/v2/zones/{zone_id}/recordsets/{recordset_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateRecordSetResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_record_sets(self, request):
        """修改单个Record Set

        修改单个Record Set
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for UpdateRecordSets
        :type request: :class:`huaweicloudsdkdns.v2.UpdateRecordSetsRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.UpdateRecordSetsResponse`
        """
        return self.update_record_sets_with_http_info(request)

    def update_record_sets_with_http_info(self, request):
        all_params = ['zone_id', 'recordset_id', 'update_record_sets_req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'zone_id' in local_var_params:
            path_params['zone_id'] = local_var_params['zone_id']
        if 'recordset_id' in local_var_params:
            path_params['recordset_id'] = local_var_params['recordset_id']

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
            resource_path='/v2.1/zones/{zone_id}/recordsets/{recordset_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateRecordSetsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_create_tag(self, request):
        """为指定实例批量添加或删除标签

        为指定实例批量添加或删除标签
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for BatchCreateTag
        :type request: :class:`huaweicloudsdkdns.v2.BatchCreateTagRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.BatchCreateTagResponse`
        """
        return self.batch_create_tag_with_http_info(request)

    def batch_create_tag_with_http_info(self, request):
        all_params = ['resource_type', 'resource_id', 'batch_hand_tags']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v2/{project_id}/{resource_type}/{resource_id}/tags/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='BatchCreateTagResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_tag(self, request):
        """为指定实例添加标签

        为指定实例添加标签
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for CreateTag
        :type request: :class:`huaweicloudsdkdns.v2.CreateTagRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.CreateTagResponse`
        """
        return self.create_tag_with_http_info(request)

    def create_tag_with_http_info(self, request):
        all_params = ['resource_type', 'resource_id', 'create_tag_req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v2/{project_id}/{resource_type}/{resource_id}/tags',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateTagResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_tag(self, request):
        """删除资源标签

        删除资源标签
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for DeleteTag
        :type request: :class:`huaweicloudsdkdns.v2.DeleteTagRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.DeleteTagResponse`
        """
        return self.delete_tag_with_http_info(request)

    def delete_tag_with_http_info(self, request):
        all_params = ['resource_type', 'resource_id', 'key']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'resource_type' in local_var_params:
            path_params['resource_type'] = local_var_params['resource_type']
        if 'resource_id' in local_var_params:
            path_params['resource_id'] = local_var_params['resource_id']
        if 'key' in local_var_params:
            path_params['key'] = local_var_params['key']

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
            resource_path='/v2/{project_id}/{resource_type}/{resource_id}/tags/{key}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteTagResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_tag(self, request):
        """使用标签查询资源实例

        使用标签查询资源实例
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListTag
        :type request: :class:`huaweicloudsdkdns.v2.ListTagRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.ListTagResponse`
        """
        return self.list_tag_with_http_info(request)

    def list_tag_with_http_info(self, request):
        all_params = ['resource_type', 'list_tag_req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v2/{project_id}/{resource_type}/resource_instances/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListTagResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_tags(self, request):
        """查询指定实例类型的所有标签集合

        查询指定实例类型的所有标签集合
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListTags
        :type request: :class:`huaweicloudsdkdns.v2.ListTagsRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.ListTagsResponse`
        """
        return self.list_tags_with_http_info(request)

    def list_tags_with_http_info(self, request):
        all_params = ['resource_type']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v2/{project_id}/{resource_type}/tags',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_resource_tag(self, request):
        """查询指定实例的标签信息

        查询指定实例的标签信息
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowResourceTag
        :type request: :class:`huaweicloudsdkdns.v2.ShowResourceTagRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.ShowResourceTagResponse`
        """
        return self.show_resource_tag_with_http_info(request)

    def show_resource_tag_with_http_info(self, request):
        all_params = ['resource_type', 'resource_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v2/{project_id}/{resource_type}/{resource_id}/tags',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowResourceTagResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def associate_router(self, request):
        """在内网Zone上关联VPC

        在内网Zone上关联VPC
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for AssociateRouter
        :type request: :class:`huaweicloudsdkdns.v2.AssociateRouterRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.AssociateRouterResponse`
        """
        return self.associate_router_with_http_info(request)

    def associate_router_with_http_info(self, request):
        all_params = ['zone_id', 'associate_router_req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'zone_id' in local_var_params:
            path_params['zone_id'] = local_var_params['zone_id']

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
            resource_path='/v2/zones/{zone_id}/associaterouter',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='AssociateRouterResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_private_zone(self, request):
        """创建单个内网Zone

        创建单个内网Zone
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for CreatePrivateZone
        :type request: :class:`huaweicloudsdkdns.v2.CreatePrivateZoneRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.CreatePrivateZoneResponse`
        """
        return self.create_private_zone_with_http_info(request)

    def create_private_zone_with_http_info(self, request):
        all_params = ['create_private_zone_req']
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
            resource_path='/v2/zones',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreatePrivateZoneResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_public_zone(self, request):
        """创建单个公网Zone

        创建单个公网Zone
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for CreatePublicZone
        :type request: :class:`huaweicloudsdkdns.v2.CreatePublicZoneRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.CreatePublicZoneResponse`
        """
        return self.create_public_zone_with_http_info(request)

    def create_public_zone_with_http_info(self, request):
        all_params = ['create_public_zone']
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
            resource_path='/v2/zones',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreatePublicZoneResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_private_zone(self, request):
        """删除单个内网Zone

        删除单个内网Zone
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for DeletePrivateZone
        :type request: :class:`huaweicloudsdkdns.v2.DeletePrivateZoneRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.DeletePrivateZoneResponse`
        """
        return self.delete_private_zone_with_http_info(request)

    def delete_private_zone_with_http_info(self, request):
        all_params = ['zone_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'zone_id' in local_var_params:
            path_params['zone_id'] = local_var_params['zone_id']

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
            resource_path='/v2/zones/{zone_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeletePrivateZoneResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_public_zone(self, request):
        """删除单个公网Zone

        删除单个公网Zone
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for DeletePublicZone
        :type request: :class:`huaweicloudsdkdns.v2.DeletePublicZoneRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.DeletePublicZoneResponse`
        """
        return self.delete_public_zone_with_http_info(request)

    def delete_public_zone_with_http_info(self, request):
        all_params = ['zone_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'zone_id' in local_var_params:
            path_params['zone_id'] = local_var_params['zone_id']

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
            resource_path='/v2/zones/{zone_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeletePublicZoneResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def disassociate_router(self, request):
        """在内网Zone上解关联VPC

        在内网Zone上解关联VPC
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for DisassociateRouter
        :type request: :class:`huaweicloudsdkdns.v2.DisassociateRouterRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.DisassociateRouterResponse`
        """
        return self.disassociate_router_with_http_info(request)

    def disassociate_router_with_http_info(self, request):
        all_params = ['zone_id', 'disassociaterouter_req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'zone_id' in local_var_params:
            path_params['zone_id'] = local_var_params['zone_id']

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
            resource_path='/v2/zones/{zone_id}/disassociaterouter',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DisassociateRouterResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_private_zones(self, request):
        """查询内网Zone的列表

        查询内网Zone的列表
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListPrivateZones
        :type request: :class:`huaweicloudsdkdns.v2.ListPrivateZonesRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.ListPrivateZonesResponse`
        """
        return self.list_private_zones_with_http_info(request)

    def list_private_zones_with_http_info(self, request):
        all_params = ['type', 'limit', 'marker', 'offset', 'tags', 'name', 'status', 'enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'tags' in local_var_params:
            query_params.append(('tags', local_var_params['tags']))
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
            resource_path='/v2/zones',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListPrivateZonesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_public_zones(self, request):
        """查询公网Zone的列表

        查询公网Zone的列表
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListPublicZones
        :type request: :class:`huaweicloudsdkdns.v2.ListPublicZonesRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.ListPublicZonesResponse`
        """
        return self.list_public_zones_with_http_info(request)

    def list_public_zones_with_http_info(self, request):
        all_params = ['type', 'limit', 'marker', 'offset', 'tags', 'name', 'status', 'enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'tags' in local_var_params:
            query_params.append(('tags', local_var_params['tags']))
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
            resource_path='/v2/zones',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListPublicZonesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_private_zone(self, request):
        """查询单个内网Zone

        查询单个内网Zone
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowPrivateZone
        :type request: :class:`huaweicloudsdkdns.v2.ShowPrivateZoneRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.ShowPrivateZoneResponse`
        """
        return self.show_private_zone_with_http_info(request)

    def show_private_zone_with_http_info(self, request):
        all_params = ['zone_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'zone_id' in local_var_params:
            path_params['zone_id'] = local_var_params['zone_id']

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
            resource_path='/v2/zones/{zone_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowPrivateZoneResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_private_zone_name_server(self, request):
        """查询单个内网Zone的名称服务器

        查询单个内网Zone的名称服务器
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowPrivateZoneNameServer
        :type request: :class:`huaweicloudsdkdns.v2.ShowPrivateZoneNameServerRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.ShowPrivateZoneNameServerResponse`
        """
        return self.show_private_zone_name_server_with_http_info(request)

    def show_private_zone_name_server_with_http_info(self, request):
        all_params = ['zone_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'zone_id' in local_var_params:
            path_params['zone_id'] = local_var_params['zone_id']

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
            resource_path='/v2/zones/{zone_id}/nameservers',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowPrivateZoneNameServerResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_public_zone(self, request):
        """查询单个公网Zone

        查询单个公网Zone
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowPublicZone
        :type request: :class:`huaweicloudsdkdns.v2.ShowPublicZoneRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.ShowPublicZoneResponse`
        """
        return self.show_public_zone_with_http_info(request)

    def show_public_zone_with_http_info(self, request):
        all_params = ['zone_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'zone_id' in local_var_params:
            path_params['zone_id'] = local_var_params['zone_id']

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
            resource_path='/v2/zones/{zone_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowPublicZoneResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_public_zone_name_server(self, request):
        """查询单个公网Zone的名称服务器

        查询单个公网Zone的名称服务器
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowPublicZoneNameServer
        :type request: :class:`huaweicloudsdkdns.v2.ShowPublicZoneNameServerRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.ShowPublicZoneNameServerResponse`
        """
        return self.show_public_zone_name_server_with_http_info(request)

    def show_public_zone_name_server_with_http_info(self, request):
        all_params = ['zone_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'zone_id' in local_var_params:
            path_params['zone_id'] = local_var_params['zone_id']

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
            resource_path='/v2/zones/{zone_id}/nameservers',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowPublicZoneNameServerResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_private_zone(self, request):
        """修改单个内网Zone

        修改单个内网Zone
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for UpdatePrivateZone
        :type request: :class:`huaweicloudsdkdns.v2.UpdatePrivateZoneRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.UpdatePrivateZoneResponse`
        """
        return self.update_private_zone_with_http_info(request)

    def update_private_zone_with_http_info(self, request):
        all_params = ['zone_id', 'update_private_zone_info_req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'zone_id' in local_var_params:
            path_params['zone_id'] = local_var_params['zone_id']

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
            resource_path='/v2/zones/{zone_id}',
            method='PATCH',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdatePrivateZoneResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_public_zone(self, request):
        """修改单个公网Zone

        修改单个公网Zone
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for UpdatePublicZone
        :type request: :class:`huaweicloudsdkdns.v2.UpdatePublicZoneRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.UpdatePublicZoneResponse`
        """
        return self.update_public_zone_with_http_info(request)

    def update_public_zone_with_http_info(self, request):
        all_params = ['zone_id', 'update_public_zone_info']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'zone_id' in local_var_params:
            path_params['zone_id'] = local_var_params['zone_id']

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
            resource_path='/v2/zones/{zone_id}',
            method='PATCH',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdatePublicZoneResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_public_zone_status(self, request):
        """设置单个公网Zone状态，支持暂停、启用Zone

        设置单个公网Zone状态，支持暂停、启用Zone
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for UpdatePublicZoneStatus
        :type request: :class:`huaweicloudsdkdns.v2.UpdatePublicZoneStatusRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.UpdatePublicZoneStatusResponse`
        """
        return self.update_public_zone_status_with_http_info(request)

    def update_public_zone_status_with_http_info(self, request):
        all_params = ['zone_id', 'update_public_zone_status']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'zone_id' in local_var_params:
            path_params['zone_id'] = local_var_params['zone_id']

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
            resource_path='/v2/zones/{zone_id}/statuses',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdatePublicZoneStatusResponse',
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

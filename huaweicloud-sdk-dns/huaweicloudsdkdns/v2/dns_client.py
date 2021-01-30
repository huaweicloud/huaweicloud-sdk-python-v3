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

        :param CreateCustomLineRequest request
        :return: CreateCustomLineResponse
        """
        return self.create_custom_line_with_http_info(request)

    def create_custom_line_with_http_info(self, request):
        """创建单个自定义线路

        创建单个自定义线路

        :param CreateCustomLineRequest request
        :return: CreateCustomLineResponse
        """

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

        :param DeleteCustomLineRequest request
        :return: DeleteCustomLineResponse
        """
        return self.delete_custom_line_with_http_info(request)

    def delete_custom_line_with_http_info(self, request):
        """删除单个自定义线路

        删除单个自定义线路

        :param DeleteCustomLineRequest request
        :return: DeleteCustomLineResponse
        """

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

        :param ListApiVersionsRequest request
        :return: ListApiVersionsResponse
        """
        return self.list_api_versions_with_http_info(request)

    def list_api_versions_with_http_info(self, request):
        """查询所有的云解析服务API版本号

        查询所有的云解析服务API版本号列表

        :param ListApiVersionsRequest request
        :return: ListApiVersionsResponse
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

        :param ListCustomLineRequest request
        :return: ListCustomLineResponse
        """
        return self.list_custom_line_with_http_info(request)

    def list_custom_line_with_http_info(self, request):
        """查询自定义线路

        查询自定义线路

        :param ListCustomLineRequest request
        :return: ListCustomLineResponse
        """

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

        :param ListNameServersRequest request
        :return: ListNameServersResponse
        """
        return self.list_name_servers_with_http_info(request)

    def list_name_servers_with_http_info(self, request):
        """查询名称服务器列表

        查询名称服务器列表

        :param ListNameServersRequest request
        :return: ListNameServersResponse
        """

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

        :param ShowApiInfoRequest request
        :return: ShowApiInfoResponse
        """
        return self.show_api_info_with_http_info(request)

    def show_api_info_with_http_info(self, request):
        """查询指定的云解析服务API版本号

        查询指定的云解析服务API版本号

        :param ShowApiInfoRequest request
        :return: ShowApiInfoResponse
        """

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


    def update_custom_line(self, request):
        """更新单个自定义线路

        更新单个自定义线路

        :param UpdateCustomLineRequest request
        :return: UpdateCustomLineResponse
        """
        return self.update_custom_line_with_http_info(request)

    def update_custom_line_with_http_info(self, request):
        """更新单个自定义线路

        更新单个自定义线路

        :param UpdateCustomLineRequest request
        :return: UpdateCustomLineResponse
        """

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

        :param CreateEipRecordSetRequest request
        :return: CreateEipRecordSetResponse
        """
        return self.create_eip_record_set_with_http_info(request)

    def create_eip_record_set_with_http_info(self, request):
        """设置弹性IP的PTR记录

        设置弹性IP的PTR记录

        :param CreateEipRecordSetRequest request
        :return: CreateEipRecordSetResponse
        """

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

        :param ListPtrRecordsRequest request
        :return: ListPtrRecordsResponse
        """
        return self.list_ptr_records_with_http_info(request)

    def list_ptr_records_with_http_info(self, request):
        """查询租户弹性IP的PTR记录列表

        查询租户弹性IP的PTR记录列表

        :param ListPtrRecordsRequest request
        :return: ListPtrRecordsResponse
        """

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

        :param RestorePtrRecordRequest request
        :return: RestorePtrRecordResponse
        """
        return self.restore_ptr_record_with_http_info(request)

    def restore_ptr_record_with_http_info(self, request):
        """将弹性IP的PTR记录恢复为默认值

        将弹性IP的PTR记录恢复为默认值

        :param RestorePtrRecordRequest request
        :return: RestorePtrRecordResponse
        """

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

        :param ShowPtrRecordSetRequest request
        :return: ShowPtrRecordSetResponse
        """
        return self.show_ptr_record_set_with_http_info(request)

    def show_ptr_record_set_with_http_info(self, request):
        """查询单个弹性IP的PTR记录

        查询单个弹性IP的PTR记录

        :param ShowPtrRecordSetRequest request
        :return: ShowPtrRecordSetResponse
        """

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

        :param UpdatePtrRecordRequest request
        :return: UpdatePtrRecordResponse
        """
        return self.update_ptr_record_with_http_info(request)

    def update_ptr_record_with_http_info(self, request):
        """修改弹性IP的PTR记录

        修改弹性IP的PTR记录

        :param UpdatePtrRecordRequest request
        :return: UpdatePtrRecordResponse
        """

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


    def create_record_set(self, request):
        """创建单个Record Set

        创建单个Record Set

        :param CreateRecordSetRequest request
        :return: CreateRecordSetResponse
        """
        return self.create_record_set_with_http_info(request)

    def create_record_set_with_http_info(self, request):
        """创建单个Record Set

        创建单个Record Set

        :param CreateRecordSetRequest request
        :return: CreateRecordSetResponse
        """

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


    def create_record_set_with_line(self, request):
        """创建单个Record Set，仅适用于公网DNS

        创建单个Record Set，仅适用于公网DNS

        :param CreateRecordSetWithLineRequest request
        :return: CreateRecordSetWithLineResponse
        """
        return self.create_record_set_with_line_with_http_info(request)

    def create_record_set_with_line_with_http_info(self, request):
        """创建单个Record Set，仅适用于公网DNS

        创建单个Record Set，仅适用于公网DNS

        :param CreateRecordSetWithLineRequest request
        :return: CreateRecordSetWithLineResponse
        """

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

        :param DeleteRecordSetRequest request
        :return: DeleteRecordSetResponse
        """
        return self.delete_record_set_with_http_info(request)

    def delete_record_set_with_http_info(self, request):
        """删除单个Record Set

        删除单个Record Set

        :param DeleteRecordSetRequest request
        :return: DeleteRecordSetResponse
        """

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

        :param DeleteRecordSetsRequest request
        :return: DeleteRecordSetsResponse
        """
        return self.delete_record_sets_with_http_info(request)

    def delete_record_sets_with_http_info(self, request):
        """删除单个Record Set

        删除单个Record Set

        :param DeleteRecordSetsRequest request
        :return: DeleteRecordSetsResponse
        """

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

        :param ListRecordSetsRequest request
        :return: ListRecordSetsResponse
        """
        return self.list_record_sets_with_http_info(request)

    def list_record_sets_with_http_info(self, request):
        """查询租户Record Set资源列表

        查询租户Record Set资源列表

        :param ListRecordSetsRequest request
        :return: ListRecordSetsResponse
        """

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

        :param ListRecordSetsByZoneRequest request
        :return: ListRecordSetsByZoneResponse
        """
        return self.list_record_sets_by_zone_with_http_info(request)

    def list_record_sets_by_zone_with_http_info(self, request):
        """查询单个Zone下Record Set列表

        查询单个Zone下Record Set列表

        :param ListRecordSetsByZoneRequest request
        :return: ListRecordSetsByZoneResponse
        """

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

        :param ListRecordSetsWithLineRequest request
        :return: ListRecordSetsWithLineResponse
        """
        return self.list_record_sets_with_line_with_http_info(request)

    def list_record_sets_with_line_with_http_info(self, request):
        """查询租户Record Set资源列表

        查询租户Record Set资源列表

        :param ListRecordSetsWithLineRequest request
        :return: ListRecordSetsWithLineResponse
        """

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

        :param SetRecordSetsStatusRequest request
        :return: SetRecordSetsStatusResponse
        """
        return self.set_record_sets_status_with_http_info(request)

    def set_record_sets_status_with_http_info(self, request):
        """设置Record Set状态

        设置Record Set状态

        :param SetRecordSetsStatusRequest request
        :return: SetRecordSetsStatusResponse
        """

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

        :param ShowRecordSetRequest request
        :return: ShowRecordSetResponse
        """
        return self.show_record_set_with_http_info(request)

    def show_record_set_with_http_info(self, request):
        """查询单个Record Set

        查询单个Record Set

        :param ShowRecordSetRequest request
        :return: ShowRecordSetResponse
        """

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

        :param ShowRecordSetByZoneRequest request
        :return: ShowRecordSetByZoneResponse
        """
        return self.show_record_set_by_zone_with_http_info(request)

    def show_record_set_by_zone_with_http_info(self, request):
        """查询单个Zone下Record Set列表

        查询单个Zone下Record Set列表

        :param ShowRecordSetByZoneRequest request
        :return: ShowRecordSetByZoneResponse
        """

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

        :param ShowRecordSetWithLineRequest request
        :return: ShowRecordSetWithLineResponse
        """
        return self.show_record_set_with_line_with_http_info(request)

    def show_record_set_with_line_with_http_info(self, request):
        """查询单个Record Set，仅适用于公网DNS

        查询单个Record Set，仅适用于公网DNS

        :param ShowRecordSetWithLineRequest request
        :return: ShowRecordSetWithLineResponse
        """

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

        :param UpdateRecordSetRequest request
        :return: UpdateRecordSetResponse
        """
        return self.update_record_set_with_http_info(request)

    def update_record_set_with_http_info(self, request):
        """修改单个Record Set

        修改单个Record Set

        :param UpdateRecordSetRequest request
        :return: UpdateRecordSetResponse
        """

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

        :param UpdateRecordSetsRequest request
        :return: UpdateRecordSetsResponse
        """
        return self.update_record_sets_with_http_info(request)

    def update_record_sets_with_http_info(self, request):
        """修改单个Record Set

        修改单个Record Set

        :param UpdateRecordSetsRequest request
        :return: UpdateRecordSetsResponse
        """

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

        :param BatchCreateTagRequest request
        :return: BatchCreateTagResponse
        """
        return self.batch_create_tag_with_http_info(request)

    def batch_create_tag_with_http_info(self, request):
        """为指定实例批量添加或删除标签

        为指定实例批量添加或删除标签

        :param BatchCreateTagRequest request
        :return: BatchCreateTagResponse
        """

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

        :param CreateTagRequest request
        :return: CreateTagResponse
        """
        return self.create_tag_with_http_info(request)

    def create_tag_with_http_info(self, request):
        """为指定实例添加标签

        为指定实例添加标签

        :param CreateTagRequest request
        :return: CreateTagResponse
        """

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

        :param DeleteTagRequest request
        :return: DeleteTagResponse
        """
        return self.delete_tag_with_http_info(request)

    def delete_tag_with_http_info(self, request):
        """删除资源标签

        删除资源标签

        :param DeleteTagRequest request
        :return: DeleteTagResponse
        """

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

        :param ListTagRequest request
        :return: ListTagResponse
        """
        return self.list_tag_with_http_info(request)

    def list_tag_with_http_info(self, request):
        """使用标签查询资源实例

        使用标签查询资源实例

        :param ListTagRequest request
        :return: ListTagResponse
        """

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

        :param ListTagsRequest request
        :return: ListTagsResponse
        """
        return self.list_tags_with_http_info(request)

    def list_tags_with_http_info(self, request):
        """查询指定实例类型的所有标签集合

        查询指定实例类型的所有标签集合

        :param ListTagsRequest request
        :return: ListTagsResponse
        """

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

        :param ShowResourceTagRequest request
        :return: ShowResourceTagResponse
        """
        return self.show_resource_tag_with_http_info(request)

    def show_resource_tag_with_http_info(self, request):
        """查询指定实例的标签信息

        查询指定实例的标签信息

        :param ShowResourceTagRequest request
        :return: ShowResourceTagResponse
        """

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

        :param AssociateRouterRequest request
        :return: AssociateRouterResponse
        """
        return self.associate_router_with_http_info(request)

    def associate_router_with_http_info(self, request):
        """在内网Zone上关联VPC

        在内网Zone上关联VPC

        :param AssociateRouterRequest request
        :return: AssociateRouterResponse
        """

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

        :param CreatePrivateZoneRequest request
        :return: CreatePrivateZoneResponse
        """
        return self.create_private_zone_with_http_info(request)

    def create_private_zone_with_http_info(self, request):
        """创建单个内网Zone

        创建单个内网Zone

        :param CreatePrivateZoneRequest request
        :return: CreatePrivateZoneResponse
        """

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

        :param CreatePublicZoneRequest request
        :return: CreatePublicZoneResponse
        """
        return self.create_public_zone_with_http_info(request)

    def create_public_zone_with_http_info(self, request):
        """创建单个公网Zone

        创建单个公网Zone

        :param CreatePublicZoneRequest request
        :return: CreatePublicZoneResponse
        """

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

        :param DeletePrivateZoneRequest request
        :return: DeletePrivateZoneResponse
        """
        return self.delete_private_zone_with_http_info(request)

    def delete_private_zone_with_http_info(self, request):
        """删除单个内网Zone

        删除单个内网Zone

        :param DeletePrivateZoneRequest request
        :return: DeletePrivateZoneResponse
        """

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

        :param DeletePublicZoneRequest request
        :return: DeletePublicZoneResponse
        """
        return self.delete_public_zone_with_http_info(request)

    def delete_public_zone_with_http_info(self, request):
        """删除单个公网Zone

        删除单个公网Zone

        :param DeletePublicZoneRequest request
        :return: DeletePublicZoneResponse
        """

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
        """在Private Zone上解关联VPC

        在Private Zone上解关联VPC

        :param DisassociateRouterRequest request
        :return: DisassociateRouterResponse
        """
        return self.disassociate_router_with_http_info(request)

    def disassociate_router_with_http_info(self, request):
        """在Private Zone上解关联VPC

        在Private Zone上解关联VPC

        :param DisassociateRouterRequest request
        :return: DisassociateRouterResponse
        """

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

        :param ListPrivateZonesRequest request
        :return: ListPrivateZonesResponse
        """
        return self.list_private_zones_with_http_info(request)

    def list_private_zones_with_http_info(self, request):
        """查询内网Zone的列表

        查询内网Zone的列表

        :param ListPrivateZonesRequest request
        :return: ListPrivateZonesResponse
        """

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

        :param ListPublicZonesRequest request
        :return: ListPublicZonesResponse
        """
        return self.list_public_zones_with_http_info(request)

    def list_public_zones_with_http_info(self, request):
        """查询公网Zone的列表

        查询公网Zone的列表

        :param ListPublicZonesRequest request
        :return: ListPublicZonesResponse
        """

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

        :param ShowPrivateZoneRequest request
        :return: ShowPrivateZoneResponse
        """
        return self.show_private_zone_with_http_info(request)

    def show_private_zone_with_http_info(self, request):
        """查询单个内网Zone

        查询单个内网Zone

        :param ShowPrivateZoneRequest request
        :return: ShowPrivateZoneResponse
        """

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
        """查询内网Zone的名称服务器

        查询内网Zone的列表

        :param ShowPrivateZoneNameServerRequest request
        :return: ShowPrivateZoneNameServerResponse
        """
        return self.show_private_zone_name_server_with_http_info(request)

    def show_private_zone_name_server_with_http_info(self, request):
        """查询内网Zone的名称服务器

        查询内网Zone的列表

        :param ShowPrivateZoneNameServerRequest request
        :return: ShowPrivateZoneNameServerResponse
        """

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

        :param ShowPublicZoneRequest request
        :return: ShowPublicZoneResponse
        """
        return self.show_public_zone_with_http_info(request)

    def show_public_zone_with_http_info(self, request):
        """查询单个公网Zone

        查询单个公网Zone

        :param ShowPublicZoneRequest request
        :return: ShowPublicZoneResponse
        """

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

        :param ShowPublicZoneNameServerRequest request
        :return: ShowPublicZoneNameServerResponse
        """
        return self.show_public_zone_name_server_with_http_info(request)

    def show_public_zone_name_server_with_http_info(self, request):
        """查询单个公网Zone的名称服务器

        查询单个公网Zone的名称服务器

        :param ShowPublicZoneNameServerRequest request
        :return: ShowPublicZoneNameServerResponse
        """

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
        """修改单个Zone

        修改单个Zone

        :param UpdatePrivateZoneRequest request
        :return: UpdatePrivateZoneResponse
        """
        return self.update_private_zone_with_http_info(request)

    def update_private_zone_with_http_info(self, request):
        """修改单个Zone

        修改单个Zone

        :param UpdatePrivateZoneRequest request
        :return: UpdatePrivateZoneResponse
        """

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
        """修改单个Zone

        修改单个Zone

        :param UpdatePublicZoneRequest request
        :return: UpdatePublicZoneResponse
        """
        return self.update_public_zone_with_http_info(request)

    def update_public_zone_with_http_info(self, request):
        """修改单个Zone

        修改单个Zone

        :param UpdatePublicZoneRequest request
        :return: UpdatePublicZoneResponse
        """

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

        :param UpdatePublicZoneStatusRequest request
        :return: UpdatePublicZoneStatusResponse
        """
        return self.update_public_zone_status_with_http_info(request)

    def update_public_zone_status_with_http_info(self, request):
        """设置单个公网Zone状态，支持暂停、启用Zone

        设置单个公网Zone状态，支持暂停、启用Zone

        :param UpdatePublicZoneStatusRequest request
        :return: UpdatePublicZoneStatusResponse
        """

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

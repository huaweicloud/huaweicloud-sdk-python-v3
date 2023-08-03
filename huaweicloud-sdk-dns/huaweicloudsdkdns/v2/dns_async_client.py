# coding: utf-8

from __future__ import absolute_import

import importlib

from huaweicloudsdkcore.client import Client, ClientBuilder
from huaweicloudsdkcore.utils import http_utils
from huaweicloudsdkcore.sdk_stream_request import SdkStreamRequest


class DnsAsyncClient(Client):
    def __init__(self):
        super(DnsAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkdns.v2.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if clazz is None:
            return ClientBuilder(cls)

        if clazz.__name__ != "DnsClient":
            raise TypeError("client type error, support client type is DnsClient")

        return ClientBuilder(clazz)

    def create_custom_line_async(self, request):
        """创建单个自定义线路

        创建单个自定义线路
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateCustomLine
        :type request: :class:`huaweicloudsdkdns.v2.CreateCustomLineRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.CreateCustomLineResponse`
        """
        return self._create_custom_line_with_http_info(request)

    def _create_custom_line_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
            resource_path='/v2.1/customlines',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateCustomLineResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_line_group_async(self, request):
        """创建线路分组

        创建一个线路分组。 该接口部分区域未上线、如需使用请提交工单申请开通。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateLineGroup
        :type request: :class:`huaweicloudsdkdns.v2.CreateLineGroupRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.CreateLineGroupResponse`
        """
        return self._create_line_group_with_http_info(request)

    def _create_line_group_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
            resource_path='/v2.1/linegroups',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateLineGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_custom_line_async(self, request):
        """删除单个自定义线路

        删除单个自定义线路
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteCustomLine
        :type request: :class:`huaweicloudsdkdns.v2.DeleteCustomLineRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.DeleteCustomLineResponse`
        """
        return self._delete_custom_line_with_http_info(request)

    def _delete_custom_line_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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
            cname=cname,
            response_type='DeleteCustomLineResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_line_group_async(self, request):
        """删除线路分组

        删除单个线路分组。该接口部分区域未上线、如需使用请提交工单申请开通。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteLineGroup
        :type request: :class:`huaweicloudsdkdns.v2.DeleteLineGroupRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.DeleteLineGroupResponse`
        """
        return self._delete_line_group_with_http_info(request)

    def _delete_line_group_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'linegroup_id' in local_var_params:
            path_params['linegroup_id'] = local_var_params['linegroup_id']

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
            resource_path='/v2.1/linegroups/{linegroup_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteLineGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_api_versions_async(self, request):
        """查询所有的云解析服务API版本号

        查询所有的云解析服务API版本号列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListApiVersions
        :type request: :class:`huaweicloudsdkdns.v2.ListApiVersionsRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.ListApiVersionsResponse`
        """
        return self._list_api_versions_with_http_info(request)

    def _list_api_versions_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
            response_type='ListApiVersionsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_custom_line_async(self, request):
        """查询自定义线路

        查询自定义线路
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListCustomLine
        :type request: :class:`huaweicloudsdkdns.v2.ListCustomLineRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.ListCustomLineResponse`
        """
        return self._list_custom_line_with_http_info(request)

    def _list_custom_line_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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
            cname=cname,
            response_type='ListCustomLineResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_line_groups_async(self, request):
        """查询线路分组列表

        查询线路分组列表。该接口部分区域未上线、如需使用请提交工单申请开通。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListLineGroups
        :type request: :class:`huaweicloudsdkdns.v2.ListLineGroupsRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.ListLineGroupsResponse`
        """
        return self._list_line_groups_with_http_info(request)

    def _list_line_groups_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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
            resource_path='/v2.1/linegroups',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListLineGroupsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_name_servers_async(self, request):
        """查询名称服务器列表

        查询名称服务器列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListNameServers
        :type request: :class:`huaweicloudsdkdns.v2.ListNameServersRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.ListNameServersResponse`
        """
        return self._list_name_servers_with_http_info(request)

    def _list_name_servers_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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
            cname=cname,
            response_type='ListNameServersResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_api_info_async(self, request):
        """查询指定的云解析服务API版本号

        查询指定的云解析服务API版本号
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowApiInfo
        :type request: :class:`huaweicloudsdkdns.v2.ShowApiInfoRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.ShowApiInfoResponse`
        """
        return self._show_api_info_with_http_info(request)

    def _show_api_info_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
            response_type='ShowApiInfoResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_domain_quota_async(self, request):
        """查询租户配额

        查询单租户在DNS服务下的资源配额，包括公网zone配额、内网zone配额、Record Set配额、PTR Record配额、入站终端节点配额、出站终端节点配额、自定义线路配额、线路分组配额等。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowDomainQuota
        :type request: :class:`huaweicloudsdkdns.v2.ShowDomainQuotaRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.ShowDomainQuotaResponse`
        """
        return self._show_domain_quota_with_http_info(request)

    def _show_domain_quota_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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
            cname=cname,
            response_type='ShowDomainQuotaResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_line_group_async(self, request):
        """查询线路分组

        查询线路分组。该接口部分区域未上线、如需使用请提交工单申请开通。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowLineGroup
        :type request: :class:`huaweicloudsdkdns.v2.ShowLineGroupRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.ShowLineGroupResponse`
        """
        return self._show_line_group_with_http_info(request)

    def _show_line_group_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'linegroup_id' in local_var_params:
            path_params['linegroup_id'] = local_var_params['linegroup_id']

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
            resource_path='/v2.1/linegroups/{linegroup_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowLineGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_custom_line_async(self, request):
        """更新单个自定义线路

        更新单个自定义线路
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateCustomLine
        :type request: :class:`huaweicloudsdkdns.v2.UpdateCustomLineRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.UpdateCustomLineResponse`
        """
        return self._update_custom_line_with_http_info(request)

    def _update_custom_line_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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
            cname=cname,
            response_type='UpdateCustomLineResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_line_groups_async(self, request):
        """更新线路分组

        更新单个线路分组。该接口部分区域未上线、如需使用请提交工单申请开通。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateLineGroups
        :type request: :class:`huaweicloudsdkdns.v2.UpdateLineGroupsRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.UpdateLineGroupsResponse`
        """
        return self._update_line_groups_with_http_info(request)

    def _update_line_groups_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'linegroup_id' in local_var_params:
            path_params['linegroup_id'] = local_var_params['linegroup_id']

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
            resource_path='/v2.1/linegroups/{linegroup_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateLineGroupsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_eip_record_set_async(self, request):
        """设置弹性IP的PTR记录

        设置弹性IP的PTR记录
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateEipRecordSet
        :type request: :class:`huaweicloudsdkdns.v2.CreateEipRecordSetRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.CreateEipRecordSetResponse`
        """
        return self._create_eip_record_set_with_http_info(request)

    def _create_eip_record_set_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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
            cname=cname,
            response_type='CreateEipRecordSetResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_ptr_records_async(self, request):
        """查询租户弹性IP的PTR记录列表

        查询租户弹性IP的PTR记录列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListPtrRecords
        :type request: :class:`huaweicloudsdkdns.v2.ListPtrRecordsRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.ListPtrRecordsResponse`
        """
        return self._list_ptr_records_with_http_info(request)

    def _list_ptr_records_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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
            cname=cname,
            response_type='ListPtrRecordsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def restore_ptr_record_async(self, request):
        """将弹性IP的PTR记录恢复为默认值

        将弹性IP的PTR记录恢复为默认值
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RestorePtrRecord
        :type request: :class:`huaweicloudsdkdns.v2.RestorePtrRecordRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.RestorePtrRecordResponse`
        """
        return self._restore_ptr_record_with_http_info(request)

    def _restore_ptr_record_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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
            cname=cname,
            response_type='RestorePtrRecordResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_ptr_record_set_async(self, request):
        """查询单个弹性IP的PTR记录

        查询单个弹性IP的PTR记录
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowPtrRecordSet
        :type request: :class:`huaweicloudsdkdns.v2.ShowPtrRecordSetRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.ShowPtrRecordSetResponse`
        """
        return self._show_ptr_record_set_with_http_info(request)

    def _show_ptr_record_set_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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
            cname=cname,
            response_type='ShowPtrRecordSetResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_ptr_record_async(self, request):
        """修改弹性IP的PTR记录

        修改弹性IP的PTR记录
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdatePtrRecord
        :type request: :class:`huaweicloudsdkdns.v2.UpdatePtrRecordRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.UpdatePtrRecordResponse`
        """
        return self._update_ptr_record_with_http_info(request)

    def _update_ptr_record_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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
            cname=cname,
            response_type='UpdatePtrRecordResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def associate_health_check_async(self, request):
        """Record Set关联健康检查

        Record Set关联健康检查。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AssociateHealthCheck
        :type request: :class:`huaweicloudsdkdns.v2.AssociateHealthCheckRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.AssociateHealthCheckResponse`
        """
        return self._associate_health_check_with_http_info(request)

    def _associate_health_check_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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
            resource_path='/v2.1/recordsets/{recordset_id}/associatehealthcheck',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='AssociateHealthCheckResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_delete_record_set_with_line_async(self, request):
        """批量删除某个Zone下的Record Set资源

        批量删除某个Zone下的Record Set资源，当删除的资源不存在时，则默认删除成功。
        响应结果中只包含本次实际删除的资源。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchDeleteRecordSetWithLine
        :type request: :class:`huaweicloudsdkdns.v2.BatchDeleteRecordSetWithLineRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.BatchDeleteRecordSetWithLineResponse`
        """
        return self._batch_delete_record_set_with_line_with_http_info(request)

    def _batch_delete_record_set_with_line_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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
            cname=cname,
            response_type='BatchDeleteRecordSetWithLineResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_update_record_set_with_line_async(self, request):
        """批量修改RecordSet

        批量修改RecordSet。属于原子性操作，请求Record Set将全部完成修改，或不做任何修改。
        仅公网Zone支持。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchUpdateRecordSetWithLine
        :type request: :class:`huaweicloudsdkdns.v2.BatchUpdateRecordSetWithLineRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.BatchUpdateRecordSetWithLineResponse`
        """
        return self._batch_update_record_set_with_line_with_http_info(request)

    def _batch_update_record_set_with_line_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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
            cname=cname,
            response_type='BatchUpdateRecordSetWithLineResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_record_set_async(self, request):
        """创建单个Record Set

        创建单个Record Set
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateRecordSet
        :type request: :class:`huaweicloudsdkdns.v2.CreateRecordSetRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.CreateRecordSetResponse`
        """
        return self._create_record_set_with_http_info(request)

    def _create_record_set_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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
            cname=cname,
            response_type='CreateRecordSetResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_record_set_with_batch_lines_async(self, request):
        """批量线路创建RecordSet

        批量线路创建RecordSet。属于原子性操作，如果存在一个参数校验不通过，则创建失败。仅公网Zone支持。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateRecordSetWithBatchLines
        :type request: :class:`huaweicloudsdkdns.v2.CreateRecordSetWithBatchLinesRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.CreateRecordSetWithBatchLinesResponse`
        """
        return self._create_record_set_with_batch_lines_with_http_info(request)

    def _create_record_set_with_batch_lines_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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
            cname=cname,
            response_type='CreateRecordSetWithBatchLinesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_record_set_with_line_async(self, request):
        """创建单个Record Set

        创建单个Record Set，仅适用于公网DNS
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateRecordSetWithLine
        :type request: :class:`huaweicloudsdkdns.v2.CreateRecordSetWithLineRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.CreateRecordSetWithLineResponse`
        """
        return self._create_record_set_with_line_with_http_info(request)

    def _create_record_set_with_line_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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
            cname=cname,
            response_type='CreateRecordSetWithLineResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_record_set_async(self, request):
        """删除单个Record Set

        删除单个Record Set. 删除有添加智能解析的记录集时、需要用Record Set多线路管理模块中删除接口进行删除.
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteRecordSet
        :type request: :class:`huaweicloudsdkdns.v2.DeleteRecordSetRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.DeleteRecordSetResponse`
        """
        return self._delete_record_set_with_http_info(request)

    def _delete_record_set_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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
            cname=cname,
            response_type='DeleteRecordSetResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_record_sets_async(self, request):
        """删除单个Record Set

        删除单个Record Set
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteRecordSets
        :type request: :class:`huaweicloudsdkdns.v2.DeleteRecordSetsRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.DeleteRecordSetsResponse`
        """
        return self._delete_record_sets_with_http_info(request)

    def _delete_record_sets_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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
            cname=cname,
            response_type='DeleteRecordSetsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def disassociate_health_check_async(self, request):
        """Record Set解关联健康检查

        Record Set解关联健康检查。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DisassociateHealthCheck
        :type request: :class:`huaweicloudsdkdns.v2.DisassociateHealthCheckRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.DisassociateHealthCheckResponse`
        """
        return self._disassociate_health_check_with_http_info(request)

    def _disassociate_health_check_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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
            resource_path='/v2.1/recordsets/{recordset_id}/disassociatehealthcheck',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DisassociateHealthCheckResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_record_sets_async(self, request):
        """查询租户Record Set资源列表

        查询租户Record Set资源列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListRecordSets
        :type request: :class:`huaweicloudsdkdns.v2.ListRecordSetsRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.ListRecordSetsResponse`
        """
        return self._list_record_sets_with_http_info(request)

    def _list_record_sets_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'zone_type' in local_var_params:
            query_params.append(('zone_type', local_var_params['zone_type']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'search_mode' in local_var_params:
            query_params.append(('search_mode', local_var_params['search_mode']))
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
            cname=cname,
            response_type='ListRecordSetsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_record_sets_by_zone_async(self, request):
        """查询单个Zone下Record Set列表

        查询单个Zone下Record Set列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListRecordSetsByZone
        :type request: :class:`huaweicloudsdkdns.v2.ListRecordSetsByZoneRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.ListRecordSetsByZoneResponse`
        """
        return self._list_record_sets_by_zone_with_http_info(request)

    def _list_record_sets_by_zone_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'zone_id' in local_var_params:
            path_params['zone_id'] = local_var_params['zone_id']

        query_params = []
        if 'search_mode' in local_var_params:
            query_params.append(('search_mode', local_var_params['search_mode']))
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
            cname=cname,
            response_type='ListRecordSetsByZoneResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_record_sets_with_line_async(self, request):
        """查询租户Record Set资源列表

        查询租户Record Set资源列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListRecordSetsWithLine
        :type request: :class:`huaweicloudsdkdns.v2.ListRecordSetsWithLineRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.ListRecordSetsWithLineResponse`
        """
        return self._list_record_sets_with_line_with_http_info(request)

    def _list_record_sets_with_line_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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
            cname=cname,
            response_type='ListRecordSetsWithLineResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def set_record_sets_status_async(self, request):
        """设置Record Set状态

        设置Record Set状态
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for SetRecordSetsStatus
        :type request: :class:`huaweicloudsdkdns.v2.SetRecordSetsStatusRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.SetRecordSetsStatusResponse`
        """
        return self._set_record_sets_status_with_http_info(request)

    def _set_record_sets_status_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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
            cname=cname,
            response_type='SetRecordSetsStatusResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_record_set_async(self, request):
        """查询单个Record Set

        查询单个Record Set。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowRecordSet
        :type request: :class:`huaweicloudsdkdns.v2.ShowRecordSetRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.ShowRecordSetResponse`
        """
        return self._show_record_set_with_http_info(request)

    def _show_record_set_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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
            cname=cname,
            response_type='ShowRecordSetResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_record_set_by_zone_async(self, request):
        """查询单个Zone下Record Set列表

        查询单个Zone下Record Set列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowRecordSetByZone
        :type request: :class:`huaweicloudsdkdns.v2.ShowRecordSetByZoneRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.ShowRecordSetByZoneResponse`
        """
        return self._show_record_set_by_zone_with_http_info(request)

    def _show_record_set_by_zone_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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
            cname=cname,
            response_type='ShowRecordSetByZoneResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_record_set_with_line_async(self, request):
        """查询单个Record Set

        查询单个Record Set，仅适用于公网DNS
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowRecordSetWithLine
        :type request: :class:`huaweicloudsdkdns.v2.ShowRecordSetWithLineRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.ShowRecordSetWithLineResponse`
        """
        return self._show_record_set_with_line_with_http_info(request)

    def _show_record_set_with_line_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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
            cname=cname,
            response_type='ShowRecordSetWithLineResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_record_set_async(self, request):
        """修改单个Record Set

        修改单个Record Set
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateRecordSet
        :type request: :class:`huaweicloudsdkdns.v2.UpdateRecordSetRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.UpdateRecordSetResponse`
        """
        return self._update_record_set_with_http_info(request)

    def _update_record_set_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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
            cname=cname,
            response_type='UpdateRecordSetResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_record_sets_async(self, request):
        """修改单个Record Set

        修改单个Record Set
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateRecordSets
        :type request: :class:`huaweicloudsdkdns.v2.UpdateRecordSetsRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.UpdateRecordSetsResponse`
        """
        return self._update_record_sets_with_http_info(request)

    def _update_record_sets_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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
            cname=cname,
            response_type='UpdateRecordSetsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_create_tag_async(self, request):
        """为指定实例批量添加或删除标签

        为指定实例批量添加或删除标签
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchCreateTag
        :type request: :class:`huaweicloudsdkdns.v2.BatchCreateTagRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.BatchCreateTagResponse`
        """
        return self._batch_create_tag_with_http_info(request)

    def _batch_create_tag_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
            resource_path='/v2/{project_id}/{resource_type}/{resource_id}/tags/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchCreateTagResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_tag_async(self, request):
        """为指定实例添加标签

        为指定实例添加标签
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateTag
        :type request: :class:`huaweicloudsdkdns.v2.CreateTagRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.CreateTagResponse`
        """
        return self._create_tag_with_http_info(request)

    def _create_tag_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
            resource_path='/v2/{project_id}/{resource_type}/{resource_id}/tags',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateTagResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_tag_async(self, request):
        """删除资源标签

        删除资源标签
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteTag
        :type request: :class:`huaweicloudsdkdns.v2.DeleteTagRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.DeleteTagResponse`
        """
        return self._delete_tag_with_http_info(request)

    def _delete_tag_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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
            cname=cname,
            response_type='DeleteTagResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_tag_async(self, request):
        """使用标签查询资源实例

        使用标签查询资源实例
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListTag
        :type request: :class:`huaweicloudsdkdns.v2.ListTagRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.ListTagResponse`
        """
        return self._list_tag_with_http_info(request)

    def _list_tag_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
            resource_path='/v2/{project_id}/{resource_type}/resource_instances/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListTagResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_tags_async(self, request):
        """查询指定实例类型的所有标签集合

        查询指定实例类型的所有标签集合
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListTags
        :type request: :class:`huaweicloudsdkdns.v2.ListTagsRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.ListTagsResponse`
        """
        return self._list_tags_with_http_info(request)

    def _list_tags_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
            resource_path='/v2/{project_id}/{resource_type}/tags',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_resource_tag_async(self, request):
        """查询指定实例的标签信息

        查询指定实例的标签信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowResourceTag
        :type request: :class:`huaweicloudsdkdns.v2.ShowResourceTagRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.ShowResourceTagResponse`
        """
        return self._show_resource_tag_with_http_info(request)

    def _show_resource_tag_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
            resource_path='/v2/{project_id}/{resource_type}/{resource_id}/tags',
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

    def associate_router_async(self, request):
        """在内网Zone上关联VPC

        在内网Zone上关联VPC
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AssociateRouter
        :type request: :class:`huaweicloudsdkdns.v2.AssociateRouterRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.AssociateRouterResponse`
        """
        return self._associate_router_with_http_info(request)

    def _associate_router_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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
            cname=cname,
            response_type='AssociateRouterResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_private_zone_async(self, request):
        """创建单个内网Zone

        创建单个内网Zone
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreatePrivateZone
        :type request: :class:`huaweicloudsdkdns.v2.CreatePrivateZoneRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.CreatePrivateZoneResponse`
        """
        return self._create_private_zone_with_http_info(request)

    def _create_private_zone_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
            resource_path='/v2/zones',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreatePrivateZoneResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_public_zone_async(self, request):
        """创建单个公网Zone

        创建单个公网Zone
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreatePublicZone
        :type request: :class:`huaweicloudsdkdns.v2.CreatePublicZoneRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.CreatePublicZoneResponse`
        """
        return self._create_public_zone_with_http_info(request)

    def _create_public_zone_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
            resource_path='/v2/zones',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreatePublicZoneResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_private_zone_async(self, request):
        """删除单个内网Zone

        删除单个内网Zone
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeletePrivateZone
        :type request: :class:`huaweicloudsdkdns.v2.DeletePrivateZoneRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.DeletePrivateZoneResponse`
        """
        return self._delete_private_zone_with_http_info(request)

    def _delete_private_zone_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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
            cname=cname,
            response_type='DeletePrivateZoneResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_public_zone_async(self, request):
        """删除单个公网Zone

        删除单个公网Zone
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeletePublicZone
        :type request: :class:`huaweicloudsdkdns.v2.DeletePublicZoneRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.DeletePublicZoneResponse`
        """
        return self._delete_public_zone_with_http_info(request)

    def _delete_public_zone_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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
            cname=cname,
            response_type='DeletePublicZoneResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def disassociate_router_async(self, request):
        """在内网Zone上解关联VPC

        在内网Zone上解关联VPC
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DisassociateRouter
        :type request: :class:`huaweicloudsdkdns.v2.DisassociateRouterRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.DisassociateRouterResponse`
        """
        return self._disassociate_router_with_http_info(request)

    def _disassociate_router_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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
            cname=cname,
            response_type='DisassociateRouterResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_private_zones_async(self, request):
        """查询内网Zone列表

        查询内网Zone列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListPrivateZones
        :type request: :class:`huaweicloudsdkdns.v2.ListPrivateZonesRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.ListPrivateZonesResponse`
        """
        return self._list_private_zones_with_http_info(request)

    def _list_private_zones_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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
        if 'search_mode' in local_var_params:
            query_params.append(('search_mode', local_var_params['search_mode']))
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
            cname=cname,
            response_type='ListPrivateZonesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_public_zones_async(self, request):
        """查询公网Zone列表

        查询公网Zone列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListPublicZones
        :type request: :class:`huaweicloudsdkdns.v2.ListPublicZonesRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.ListPublicZonesResponse`
        """
        return self._list_public_zones_with_http_info(request)

    def _list_public_zones_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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
        if 'search_mode' in local_var_params:
            query_params.append(('search_mode', local_var_params['search_mode']))
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
            cname=cname,
            response_type='ListPublicZonesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_private_zone_async(self, request):
        """查询单个内网Zone

        查询单个内网Zone
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowPrivateZone
        :type request: :class:`huaweicloudsdkdns.v2.ShowPrivateZoneRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.ShowPrivateZoneResponse`
        """
        return self._show_private_zone_with_http_info(request)

    def _show_private_zone_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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
            cname=cname,
            response_type='ShowPrivateZoneResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_private_zone_name_server_async(self, request):
        """查询单个内网Zone的名称服务器

        查询单个内网Zone的名称服务器
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowPrivateZoneNameServer
        :type request: :class:`huaweicloudsdkdns.v2.ShowPrivateZoneNameServerRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.ShowPrivateZoneNameServerResponse`
        """
        return self._show_private_zone_name_server_with_http_info(request)

    def _show_private_zone_name_server_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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
            cname=cname,
            response_type='ShowPrivateZoneNameServerResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_public_zone_async(self, request):
        """查询单个公网Zone

        查询单个公网Zone
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowPublicZone
        :type request: :class:`huaweicloudsdkdns.v2.ShowPublicZoneRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.ShowPublicZoneResponse`
        """
        return self._show_public_zone_with_http_info(request)

    def _show_public_zone_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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
            cname=cname,
            response_type='ShowPublicZoneResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_public_zone_name_server_async(self, request):
        """查询单个公网Zone的名称服务器

        查询单个公网Zone的名称服务器
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowPublicZoneNameServer
        :type request: :class:`huaweicloudsdkdns.v2.ShowPublicZoneNameServerRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.ShowPublicZoneNameServerResponse`
        """
        return self._show_public_zone_name_server_with_http_info(request)

    def _show_public_zone_name_server_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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
            cname=cname,
            response_type='ShowPublicZoneNameServerResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_private_zone_async(self, request):
        """修改单个内网Zone

        修改单个内网Zone
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdatePrivateZone
        :type request: :class:`huaweicloudsdkdns.v2.UpdatePrivateZoneRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.UpdatePrivateZoneResponse`
        """
        return self._update_private_zone_with_http_info(request)

    def _update_private_zone_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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
            cname=cname,
            response_type='UpdatePrivateZoneResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_public_zone_async(self, request):
        """修改单个公网Zone

        修改单个公网Zone
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdatePublicZone
        :type request: :class:`huaweicloudsdkdns.v2.UpdatePublicZoneRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.UpdatePublicZoneResponse`
        """
        return self._update_public_zone_with_http_info(request)

    def _update_public_zone_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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
            cname=cname,
            response_type='UpdatePublicZoneResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_public_zone_status_async(self, request):
        """设置单个公网Zone状态

        设置单个公网Zone状态，支持暂停、启用Zone
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdatePublicZoneStatus
        :type request: :class:`huaweicloudsdkdns.v2.UpdatePublicZoneStatusRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.UpdatePublicZoneStatusResponse`
        """
        return self._update_public_zone_status_with_http_info(request)

    def _update_public_zone_status_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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
            cname=cname,
            response_type='UpdatePublicZoneStatusResponse',
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

# coding: utf-8

from __future__ import absolute_import

import importlib
import warnings

from huaweicloudsdkcore.client import Client, ClientBuilder
from huaweicloudsdkcore.utils import http_utils
from huaweicloudsdkcore.sdk_stream_request import SdkStreamRequest
try:
    from huaweicloudsdkcore.invoker.invoker import SyncInvoker
except ImportError as e:
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkdns'")


class DnsClient(Client):
    def __init__(self):
        super(DnsClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkdns.v2.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "DnsClient":
                raise TypeError("client type error, support client type is DnsClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def create_custom_line(self, request):
        """创建单个自定义线路

        创建单个自定义线路
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateCustomLine
        :type request: :class:`huaweicloudsdkdns.v2.CreateCustomLineRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.CreateCustomLineResponse`
        """
        http_info = self._create_custom_line_http_info(request)
        return self._call_api(**http_info)

    def create_custom_line_invoker(self, request):
        http_info = self._create_custom_line_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_custom_line_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2.1/customlines",
            "request_type": request.__class__.__name__,
            "response_type": "CreateCustomLineResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_line_group(self, request):
        """创建线路分组

        创建一个线路分组。 该接口部分区域未上线、如需使用请提交工单申请开通。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateLineGroup
        :type request: :class:`huaweicloudsdkdns.v2.CreateLineGroupRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.CreateLineGroupResponse`
        """
        http_info = self._create_line_group_http_info(request)
        return self._call_api(**http_info)

    def create_line_group_invoker(self, request):
        http_info = self._create_line_group_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_line_group_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2.1/linegroups",
            "request_type": request.__class__.__name__,
            "response_type": "CreateLineGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_custom_line(self, request):
        """删除单个自定义线路

        删除单个自定义线路
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteCustomLine
        :type request: :class:`huaweicloudsdkdns.v2.DeleteCustomLineRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.DeleteCustomLineResponse`
        """
        http_info = self._delete_custom_line_http_info(request)
        return self._call_api(**http_info)

    def delete_custom_line_invoker(self, request):
        http_info = self._delete_custom_line_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_custom_line_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2.1/customlines/{line_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteCustomLineResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'line_id' in local_var_params:
            path_params['line_id'] = local_var_params['line_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_line_group(self, request):
        """删除线路分组

        删除单个线路分组。该接口部分区域未上线、如需使用请提交工单申请开通。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteLineGroup
        :type request: :class:`huaweicloudsdkdns.v2.DeleteLineGroupRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.DeleteLineGroupResponse`
        """
        http_info = self._delete_line_group_http_info(request)
        return self._call_api(**http_info)

    def delete_line_group_invoker(self, request):
        http_info = self._delete_line_group_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_line_group_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2.1/linegroups/{linegroup_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteLineGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'linegroup_id' in local_var_params:
            path_params['linegroup_id'] = local_var_params['linegroup_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_api_versions(self, request):
        """查询所有的云解析服务API版本号

        查询所有的云解析服务API版本号列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListApiVersions
        :type request: :class:`huaweicloudsdkdns.v2.ListApiVersionsRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.ListApiVersionsResponse`
        """
        http_info = self._list_api_versions_http_info(request)
        return self._call_api(**http_info)

    def list_api_versions_invoker(self, request):
        http_info = self._list_api_versions_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_api_versions_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/",
            "request_type": request.__class__.__name__,
            "response_type": "ListApiVersionsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_custom_line(self, request):
        """查询自定义线路

        查询自定义线路
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListCustomLine
        :type request: :class:`huaweicloudsdkdns.v2.ListCustomLineRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.ListCustomLineResponse`
        """
        http_info = self._list_custom_line_http_info(request)
        return self._call_api(**http_info)

    def list_custom_line_invoker(self, request):
        http_info = self._list_custom_line_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_custom_line_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2.1/customlines",
            "request_type": request.__class__.__name__,
            "response_type": "ListCustomLineResponse"
            }

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_line_groups(self, request):
        """查询线路分组列表

        查询线路分组列表。该接口部分区域未上线、如需使用请提交工单申请开通。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListLineGroups
        :type request: :class:`huaweicloudsdkdns.v2.ListLineGroupsRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.ListLineGroupsResponse`
        """
        http_info = self._list_line_groups_http_info(request)
        return self._call_api(**http_info)

    def list_line_groups_invoker(self, request):
        http_info = self._list_line_groups_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_line_groups_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2.1/linegroups",
            "request_type": request.__class__.__name__,
            "response_type": "ListLineGroupsResponse"
            }

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_name_servers(self, request):
        """查询名称服务器列表

        查询名称服务器列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListNameServers
        :type request: :class:`huaweicloudsdkdns.v2.ListNameServersRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.ListNameServersResponse`
        """
        http_info = self._list_name_servers_http_info(request)
        return self._call_api(**http_info)

    def list_name_servers_invoker(self, request):
        http_info = self._list_name_servers_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_name_servers_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/nameservers",
            "request_type": request.__class__.__name__,
            "response_type": "ListNameServersResponse"
            }

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_api_info(self, request):
        """查询指定的云解析服务API版本号

        查询指定的云解析服务API版本号
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowApiInfo
        :type request: :class:`huaweicloudsdkdns.v2.ShowApiInfoRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.ShowApiInfoResponse`
        """
        http_info = self._show_api_info_http_info(request)
        return self._call_api(**http_info)

    def show_api_info_invoker(self, request):
        http_info = self._show_api_info_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_api_info_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/{version}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowApiInfoResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'version' in local_var_params:
            path_params['version'] = local_var_params['version']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_domain_quota(self, request):
        """查询租户配额

        查询单租户在DNS服务下的资源配额，包括公网zone配额、内网zone配额、Record Set配额、PTR Record配额、入站终端节点配额、出站终端节点配额、自定义线路配额、线路分组配额等。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDomainQuota
        :type request: :class:`huaweicloudsdkdns.v2.ShowDomainQuotaRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.ShowDomainQuotaResponse`
        """
        http_info = self._show_domain_quota_http_info(request)
        return self._call_api(**http_info)

    def show_domain_quota_invoker(self, request):
        http_info = self._show_domain_quota_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_domain_quota_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/quotamg/dns/quotas",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDomainQuotaResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'domain_id' in local_var_params:
            query_params.append(('domain_id', local_var_params['domain_id']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_line_group(self, request):
        """查询线路分组

        查询线路分组。该接口部分区域未上线、如需使用请提交工单申请开通。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowLineGroup
        :type request: :class:`huaweicloudsdkdns.v2.ShowLineGroupRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.ShowLineGroupResponse`
        """
        http_info = self._show_line_group_http_info(request)
        return self._call_api(**http_info)

    def show_line_group_invoker(self, request):
        http_info = self._show_line_group_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_line_group_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2.1/linegroups/{linegroup_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowLineGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'linegroup_id' in local_var_params:
            path_params['linegroup_id'] = local_var_params['linegroup_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_custom_line(self, request):
        """更新单个自定义线路

        更新单个自定义线路
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateCustomLine
        :type request: :class:`huaweicloudsdkdns.v2.UpdateCustomLineRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.UpdateCustomLineResponse`
        """
        http_info = self._update_custom_line_http_info(request)
        return self._call_api(**http_info)

    def update_custom_line_invoker(self, request):
        http_info = self._update_custom_line_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_custom_line_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2.1/customlines/{line_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateCustomLineResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'line_id' in local_var_params:
            path_params['line_id'] = local_var_params['line_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_line_groups(self, request):
        """更新线路分组

        更新单个线路分组。该接口部分区域未上线、如需使用请提交工单申请开通。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateLineGroups
        :type request: :class:`huaweicloudsdkdns.v2.UpdateLineGroupsRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.UpdateLineGroupsResponse`
        """
        http_info = self._update_line_groups_http_info(request)
        return self._call_api(**http_info)

    def update_line_groups_invoker(self, request):
        http_info = self._update_line_groups_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_line_groups_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2.1/linegroups/{linegroup_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateLineGroupsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'linegroup_id' in local_var_params:
            path_params['linegroup_id'] = local_var_params['linegroup_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_eip_record_set(self, request):
        """设置弹性IP的PTR记录

        设置弹性IP的PTR记录
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateEipRecordSet
        :type request: :class:`huaweicloudsdkdns.v2.CreateEipRecordSetRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.CreateEipRecordSetResponse`
        """
        http_info = self._create_eip_record_set_http_info(request)
        return self._call_api(**http_info)

    def create_eip_record_set_invoker(self, request):
        http_info = self._create_eip_record_set_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_eip_record_set_http_info(cls, request):
        http_info = {
            "method": "PATCH",
            "resource_path": "/v2/reverse/floatingips/{region}:{floatingip_id}",
            "request_type": request.__class__.__name__,
            "response_type": "CreateEipRecordSetResponse"
            }

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

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_ptr_records(self, request):
        """查询租户弹性IP的PTR记录列表

        查询租户弹性IP的PTR记录列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListPtrRecords
        :type request: :class:`huaweicloudsdkdns.v2.ListPtrRecordsRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.ListPtrRecordsResponse`
        """
        http_info = self._list_ptr_records_http_info(request)
        return self._call_api(**http_info)

    def list_ptr_records_invoker(self, request):
        http_info = self._list_ptr_records_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_ptr_records_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/reverse/floatingips",
            "request_type": request.__class__.__name__,
            "response_type": "ListPtrRecordsResponse"
            }

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def restore_ptr_record(self, request):
        """将弹性IP的PTR记录恢复为默认值

        将弹性IP的PTR记录恢复为默认值
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RestorePtrRecord
        :type request: :class:`huaweicloudsdkdns.v2.RestorePtrRecordRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.RestorePtrRecordResponse`
        """
        http_info = self._restore_ptr_record_http_info(request)
        return self._call_api(**http_info)

    def restore_ptr_record_invoker(self, request):
        http_info = self._restore_ptr_record_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _restore_ptr_record_http_info(cls, request):
        http_info = {
            "method": "PATCH",
            "resource_path": "/v2/reverse/floatingips/{region}:{floatingip_id}",
            "request_type": request.__class__.__name__,
            "response_type": "RestorePtrRecordResponse"
            }

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

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_ptr_record_set(self, request):
        """查询单个弹性IP的PTR记录

        查询单个弹性IP的PTR记录
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowPtrRecordSet
        :type request: :class:`huaweicloudsdkdns.v2.ShowPtrRecordSetRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.ShowPtrRecordSetResponse`
        """
        http_info = self._show_ptr_record_set_http_info(request)
        return self._call_api(**http_info)

    def show_ptr_record_set_invoker(self, request):
        http_info = self._show_ptr_record_set_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_ptr_record_set_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/reverse/floatingips/{region}:{floatingip_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowPtrRecordSetResponse"
            }

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_ptr_record(self, request):
        """修改弹性IP的PTR记录

        修改弹性IP的PTR记录
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdatePtrRecord
        :type request: :class:`huaweicloudsdkdns.v2.UpdatePtrRecordRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.UpdatePtrRecordResponse`
        """
        http_info = self._update_ptr_record_http_info(request)
        return self._call_api(**http_info)

    def update_ptr_record_invoker(self, request):
        http_info = self._update_ptr_record_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_ptr_record_http_info(cls, request):
        http_info = {
            "method": "PATCH",
            "resource_path": "/v2/reverse/floatingips/{region}:{floatingip_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdatePtrRecordResponse"
            }

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

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def associate_health_check(self, request):
        """Record Set关联健康检查

        Record Set关联健康检查。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AssociateHealthCheck
        :type request: :class:`huaweicloudsdkdns.v2.AssociateHealthCheckRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.AssociateHealthCheckResponse`
        """
        http_info = self._associate_health_check_http_info(request)
        return self._call_api(**http_info)

    def associate_health_check_invoker(self, request):
        http_info = self._associate_health_check_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _associate_health_check_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2.1/recordsets/{recordset_id}/associatehealthcheck",
            "request_type": request.__class__.__name__,
            "response_type": "AssociateHealthCheckResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'recordset_id' in local_var_params:
            path_params['recordset_id'] = local_var_params['recordset_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def batch_delete_record_set_with_line(self, request):
        """批量删除某个Zone下的Record Set资源

        批量删除某个Zone下的Record Set资源，当删除的资源不存在时，则默认删除成功。
        响应结果中只包含本次实际删除的资源。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchDeleteRecordSetWithLine
        :type request: :class:`huaweicloudsdkdns.v2.BatchDeleteRecordSetWithLineRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.BatchDeleteRecordSetWithLineResponse`
        """
        http_info = self._batch_delete_record_set_with_line_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_record_set_with_line_invoker(self, request):
        http_info = self._batch_delete_record_set_with_line_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_delete_record_set_with_line_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2.1/zones/{zone_id}/recordsets",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeleteRecordSetWithLineResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'zone_id' in local_var_params:
            path_params['zone_id'] = local_var_params['zone_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def batch_update_record_set_with_line(self, request):
        """批量修改RecordSet

        批量修改RecordSet。属于原子性操作，请求Record Set将全部完成修改，或不做任何修改。
        仅公网Zone支持。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchUpdateRecordSetWithLine
        :type request: :class:`huaweicloudsdkdns.v2.BatchUpdateRecordSetWithLineRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.BatchUpdateRecordSetWithLineResponse`
        """
        http_info = self._batch_update_record_set_with_line_http_info(request)
        return self._call_api(**http_info)

    def batch_update_record_set_with_line_invoker(self, request):
        http_info = self._batch_update_record_set_with_line_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_update_record_set_with_line_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2.1/zones/{zone_id}/recordsets",
            "request_type": request.__class__.__name__,
            "response_type": "BatchUpdateRecordSetWithLineResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'zone_id' in local_var_params:
            path_params['zone_id'] = local_var_params['zone_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_record_set(self, request):
        """创建单个Record Set

        创建单个Record Set
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateRecordSet
        :type request: :class:`huaweicloudsdkdns.v2.CreateRecordSetRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.CreateRecordSetResponse`
        """
        http_info = self._create_record_set_http_info(request)
        return self._call_api(**http_info)

    def create_record_set_invoker(self, request):
        http_info = self._create_record_set_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_record_set_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/zones/{zone_id}/recordsets",
            "request_type": request.__class__.__name__,
            "response_type": "CreateRecordSetResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'zone_id' in local_var_params:
            path_params['zone_id'] = local_var_params['zone_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_record_set_with_batch_lines(self, request):
        """批量线路创建RecordSet

        批量线路创建RecordSet。属于原子性操作，如果存在一个参数校验不通过，则创建失败。仅公网Zone支持。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateRecordSetWithBatchLines
        :type request: :class:`huaweicloudsdkdns.v2.CreateRecordSetWithBatchLinesRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.CreateRecordSetWithBatchLinesResponse`
        """
        http_info = self._create_record_set_with_batch_lines_http_info(request)
        return self._call_api(**http_info)

    def create_record_set_with_batch_lines_invoker(self, request):
        http_info = self._create_record_set_with_batch_lines_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_record_set_with_batch_lines_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2.1/zones/{zone_id}/recordsets/batch/lines",
            "request_type": request.__class__.__name__,
            "response_type": "CreateRecordSetWithBatchLinesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'zone_id' in local_var_params:
            path_params['zone_id'] = local_var_params['zone_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_record_set_with_line(self, request):
        """创建单个Record Set

        创建单个Record Set，仅适用于公网DNS
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateRecordSetWithLine
        :type request: :class:`huaweicloudsdkdns.v2.CreateRecordSetWithLineRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.CreateRecordSetWithLineResponse`
        """
        http_info = self._create_record_set_with_line_http_info(request)
        return self._call_api(**http_info)

    def create_record_set_with_line_invoker(self, request):
        http_info = self._create_record_set_with_line_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_record_set_with_line_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2.1/zones/{zone_id}/recordsets",
            "request_type": request.__class__.__name__,
            "response_type": "CreateRecordSetWithLineResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'zone_id' in local_var_params:
            path_params['zone_id'] = local_var_params['zone_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_record_set(self, request):
        """删除单个Record Set

        删除单个Record Set. 删除有添加智能解析的记录集时、需要用Record Set多线路管理模块中删除接口进行删除.
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteRecordSet
        :type request: :class:`huaweicloudsdkdns.v2.DeleteRecordSetRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.DeleteRecordSetResponse`
        """
        http_info = self._delete_record_set_http_info(request)
        return self._call_api(**http_info)

    def delete_record_set_invoker(self, request):
        http_info = self._delete_record_set_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_record_set_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/zones/{zone_id}/recordsets/{recordset_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteRecordSetResponse"
            }

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_record_sets(self, request):
        """删除单个Record Set

        删除单个Record Set
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteRecordSets
        :type request: :class:`huaweicloudsdkdns.v2.DeleteRecordSetsRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.DeleteRecordSetsResponse`
        """
        http_info = self._delete_record_sets_http_info(request)
        return self._call_api(**http_info)

    def delete_record_sets_invoker(self, request):
        http_info = self._delete_record_sets_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_record_sets_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2.1/zones/{zone_id}/recordsets/{recordset_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteRecordSetsResponse"
            }

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def disassociate_health_check(self, request):
        """Record Set解关联健康检查

        Record Set解关联健康检查。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DisassociateHealthCheck
        :type request: :class:`huaweicloudsdkdns.v2.DisassociateHealthCheckRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.DisassociateHealthCheckResponse`
        """
        http_info = self._disassociate_health_check_http_info(request)
        return self._call_api(**http_info)

    def disassociate_health_check_invoker(self, request):
        http_info = self._disassociate_health_check_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _disassociate_health_check_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2.1/recordsets/{recordset_id}/disassociatehealthcheck",
            "request_type": request.__class__.__name__,
            "response_type": "DisassociateHealthCheckResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'recordset_id' in local_var_params:
            path_params['recordset_id'] = local_var_params['recordset_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_record_sets(self, request):
        """查询租户Record Set资源列表

        查询租户Record Set资源列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListRecordSets
        :type request: :class:`huaweicloudsdkdns.v2.ListRecordSetsRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.ListRecordSetsResponse`
        """
        http_info = self._list_record_sets_http_info(request)
        return self._call_api(**http_info)

    def list_record_sets_invoker(self, request):
        http_info = self._list_record_sets_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_record_sets_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/recordsets",
            "request_type": request.__class__.__name__,
            "response_type": "ListRecordSetsResponse"
            }

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_record_sets_by_zone(self, request):
        """查询单个Zone下Record Set列表

        查询单个Zone下Record Set列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListRecordSetsByZone
        :type request: :class:`huaweicloudsdkdns.v2.ListRecordSetsByZoneRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.ListRecordSetsByZoneResponse`
        """
        http_info = self._list_record_sets_by_zone_http_info(request)
        return self._call_api(**http_info)

    def list_record_sets_by_zone_invoker(self, request):
        http_info = self._list_record_sets_by_zone_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_record_sets_by_zone_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/zones/{zone_id}/recordsets",
            "request_type": request.__class__.__name__,
            "response_type": "ListRecordSetsByZoneResponse"
            }

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_record_sets_with_line(self, request):
        """查询租户Record Set资源列表

        查询租户Record Set资源列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListRecordSetsWithLine
        :type request: :class:`huaweicloudsdkdns.v2.ListRecordSetsWithLineRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.ListRecordSetsWithLineResponse`
        """
        http_info = self._list_record_sets_with_line_http_info(request)
        return self._call_api(**http_info)

    def list_record_sets_with_line_invoker(self, request):
        http_info = self._list_record_sets_with_line_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_record_sets_with_line_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2.1/recordsets",
            "request_type": request.__class__.__name__,
            "response_type": "ListRecordSetsWithLineResponse"
            }

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def set_record_sets_status(self, request):
        """设置Record Set状态

        设置Record Set状态
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SetRecordSetsStatus
        :type request: :class:`huaweicloudsdkdns.v2.SetRecordSetsStatusRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.SetRecordSetsStatusResponse`
        """
        http_info = self._set_record_sets_status_http_info(request)
        return self._call_api(**http_info)

    def set_record_sets_status_invoker(self, request):
        http_info = self._set_record_sets_status_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _set_record_sets_status_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2.1/recordsets/{recordset_id}/statuses/set",
            "request_type": request.__class__.__name__,
            "response_type": "SetRecordSetsStatusResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'recordset_id' in local_var_params:
            path_params['recordset_id'] = local_var_params['recordset_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_record_set(self, request):
        """查询单个Record Set

        查询单个Record Set。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowRecordSet
        :type request: :class:`huaweicloudsdkdns.v2.ShowRecordSetRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.ShowRecordSetResponse`
        """
        http_info = self._show_record_set_http_info(request)
        return self._call_api(**http_info)

    def show_record_set_invoker(self, request):
        http_info = self._show_record_set_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_record_set_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/zones/{zone_id}/recordsets/{recordset_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowRecordSetResponse"
            }

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_record_set_by_zone(self, request):
        """查询单个Zone下Record Set列表

        查询单个Zone下Record Set列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowRecordSetByZone
        :type request: :class:`huaweicloudsdkdns.v2.ShowRecordSetByZoneRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.ShowRecordSetByZoneResponse`
        """
        http_info = self._show_record_set_by_zone_http_info(request)
        return self._call_api(**http_info)

    def show_record_set_by_zone_invoker(self, request):
        http_info = self._show_record_set_by_zone_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_record_set_by_zone_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2.1/zones/{zone_id}/recordsets",
            "request_type": request.__class__.__name__,
            "response_type": "ShowRecordSetByZoneResponse"
            }

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_record_set_with_line(self, request):
        """查询单个Record Set

        查询单个Record Set，仅适用于公网DNS
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowRecordSetWithLine
        :type request: :class:`huaweicloudsdkdns.v2.ShowRecordSetWithLineRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.ShowRecordSetWithLineResponse`
        """
        http_info = self._show_record_set_with_line_http_info(request)
        return self._call_api(**http_info)

    def show_record_set_with_line_invoker(self, request):
        http_info = self._show_record_set_with_line_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_record_set_with_line_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2.1/zones/{zone_id}/recordsets/{recordset_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowRecordSetWithLineResponse"
            }

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_record_set(self, request):
        """修改单个Record Set

        修改单个Record Set
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateRecordSet
        :type request: :class:`huaweicloudsdkdns.v2.UpdateRecordSetRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.UpdateRecordSetResponse`
        """
        http_info = self._update_record_set_http_info(request)
        return self._call_api(**http_info)

    def update_record_set_invoker(self, request):
        http_info = self._update_record_set_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_record_set_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/zones/{zone_id}/recordsets/{recordset_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateRecordSetResponse"
            }

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

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_record_sets(self, request):
        """修改单个Record Set

        修改单个Record Set
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateRecordSets
        :type request: :class:`huaweicloudsdkdns.v2.UpdateRecordSetsRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.UpdateRecordSetsResponse`
        """
        http_info = self._update_record_sets_http_info(request)
        return self._call_api(**http_info)

    def update_record_sets_invoker(self, request):
        http_info = self._update_record_sets_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_record_sets_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2.1/zones/{zone_id}/recordsets/{recordset_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateRecordSetsResponse"
            }

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

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def batch_create_tag(self, request):
        """为指定实例批量添加或删除标签

        为指定实例批量添加或删除标签
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchCreateTag
        :type request: :class:`huaweicloudsdkdns.v2.BatchCreateTagRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.BatchCreateTagResponse`
        """
        http_info = self._batch_create_tag_http_info(request)
        return self._call_api(**http_info)

    def batch_create_tag_invoker(self, request):
        http_info = self._batch_create_tag_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_create_tag_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/{resource_type}/{resource_id}/tags/action",
            "request_type": request.__class__.__name__,
            "response_type": "BatchCreateTagResponse"
            }

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

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_tag(self, request):
        """为指定实例添加标签

        为指定实例添加标签
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateTag
        :type request: :class:`huaweicloudsdkdns.v2.CreateTagRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.CreateTagResponse`
        """
        http_info = self._create_tag_http_info(request)
        return self._call_api(**http_info)

    def create_tag_invoker(self, request):
        http_info = self._create_tag_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_tag_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/{resource_type}/{resource_id}/tags",
            "request_type": request.__class__.__name__,
            "response_type": "CreateTagResponse"
            }

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

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_tag(self, request):
        """删除资源标签

        删除资源标签
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteTag
        :type request: :class:`huaweicloudsdkdns.v2.DeleteTagRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.DeleteTagResponse`
        """
        http_info = self._delete_tag_http_info(request)
        return self._call_api(**http_info)

    def delete_tag_invoker(self, request):
        http_info = self._delete_tag_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_tag_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/{resource_type}/{resource_id}/tags/{key}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteTagResponse"
            }

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_tag(self, request):
        """使用标签查询资源实例

        使用标签查询资源实例
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListTag
        :type request: :class:`huaweicloudsdkdns.v2.ListTagRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.ListTagResponse`
        """
        http_info = self._list_tag_http_info(request)
        return self._call_api(**http_info)

    def list_tag_invoker(self, request):
        http_info = self._list_tag_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_tag_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/{resource_type}/resource_instances/action",
            "request_type": request.__class__.__name__,
            "response_type": "ListTagResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_type' in local_var_params:
            path_params['resource_type'] = local_var_params['resource_type']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_tags(self, request):
        """查询指定实例类型的所有标签集合

        查询指定实例类型的所有标签集合
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListTags
        :type request: :class:`huaweicloudsdkdns.v2.ListTagsRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.ListTagsResponse`
        """
        http_info = self._list_tags_http_info(request)
        return self._call_api(**http_info)

    def list_tags_invoker(self, request):
        http_info = self._list_tags_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_tags_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/{resource_type}/tags",
            "request_type": request.__class__.__name__,
            "response_type": "ListTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_type' in local_var_params:
            path_params['resource_type'] = local_var_params['resource_type']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_resource_tag(self, request):
        """查询指定实例的标签信息

        查询指定实例的标签信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowResourceTag
        :type request: :class:`huaweicloudsdkdns.v2.ShowResourceTagRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.ShowResourceTagResponse`
        """
        http_info = self._show_resource_tag_http_info(request)
        return self._call_api(**http_info)

    def show_resource_tag_invoker(self, request):
        http_info = self._show_resource_tag_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_resource_tag_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/{resource_type}/{resource_id}/tags",
            "request_type": request.__class__.__name__,
            "response_type": "ShowResourceTagResponse"
            }

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def associate_router(self, request):
        """在内网Zone上关联VPC

        在内网Zone上关联VPC
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AssociateRouter
        :type request: :class:`huaweicloudsdkdns.v2.AssociateRouterRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.AssociateRouterResponse`
        """
        http_info = self._associate_router_http_info(request)
        return self._call_api(**http_info)

    def associate_router_invoker(self, request):
        http_info = self._associate_router_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _associate_router_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/zones/{zone_id}/associaterouter",
            "request_type": request.__class__.__name__,
            "response_type": "AssociateRouterResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'zone_id' in local_var_params:
            path_params['zone_id'] = local_var_params['zone_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_private_zone(self, request):
        """创建单个内网Zone

        创建单个内网Zone
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreatePrivateZone
        :type request: :class:`huaweicloudsdkdns.v2.CreatePrivateZoneRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.CreatePrivateZoneResponse`
        """
        http_info = self._create_private_zone_http_info(request)
        return self._call_api(**http_info)

    def create_private_zone_invoker(self, request):
        http_info = self._create_private_zone_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_private_zone_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/zones",
            "request_type": request.__class__.__name__,
            "response_type": "CreatePrivateZoneResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_public_zone(self, request):
        """创建单个公网Zone

        创建单个公网Zone
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreatePublicZone
        :type request: :class:`huaweicloudsdkdns.v2.CreatePublicZoneRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.CreatePublicZoneResponse`
        """
        http_info = self._create_public_zone_http_info(request)
        return self._call_api(**http_info)

    def create_public_zone_invoker(self, request):
        http_info = self._create_public_zone_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_public_zone_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/zones",
            "request_type": request.__class__.__name__,
            "response_type": "CreatePublicZoneResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_private_zone(self, request):
        """删除单个内网Zone

        删除单个内网Zone
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeletePrivateZone
        :type request: :class:`huaweicloudsdkdns.v2.DeletePrivateZoneRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.DeletePrivateZoneResponse`
        """
        http_info = self._delete_private_zone_http_info(request)
        return self._call_api(**http_info)

    def delete_private_zone_invoker(self, request):
        http_info = self._delete_private_zone_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_private_zone_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/zones/{zone_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeletePrivateZoneResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'zone_id' in local_var_params:
            path_params['zone_id'] = local_var_params['zone_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_public_zone(self, request):
        """删除单个公网Zone

        删除单个公网Zone
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeletePublicZone
        :type request: :class:`huaweicloudsdkdns.v2.DeletePublicZoneRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.DeletePublicZoneResponse`
        """
        http_info = self._delete_public_zone_http_info(request)
        return self._call_api(**http_info)

    def delete_public_zone_invoker(self, request):
        http_info = self._delete_public_zone_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_public_zone_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/zones/{zone_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeletePublicZoneResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'zone_id' in local_var_params:
            path_params['zone_id'] = local_var_params['zone_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def disassociate_router(self, request):
        """在内网Zone上解关联VPC

        在内网Zone上解关联VPC
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DisassociateRouter
        :type request: :class:`huaweicloudsdkdns.v2.DisassociateRouterRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.DisassociateRouterResponse`
        """
        http_info = self._disassociate_router_http_info(request)
        return self._call_api(**http_info)

    def disassociate_router_invoker(self, request):
        http_info = self._disassociate_router_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _disassociate_router_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/zones/{zone_id}/disassociaterouter",
            "request_type": request.__class__.__name__,
            "response_type": "DisassociateRouterResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'zone_id' in local_var_params:
            path_params['zone_id'] = local_var_params['zone_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_private_zones(self, request):
        """查询内网Zone列表

        查询内网Zone列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListPrivateZones
        :type request: :class:`huaweicloudsdkdns.v2.ListPrivateZonesRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.ListPrivateZonesResponse`
        """
        http_info = self._list_private_zones_http_info(request)
        return self._call_api(**http_info)

    def list_private_zones_invoker(self, request):
        http_info = self._list_private_zones_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_private_zones_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/zones",
            "request_type": request.__class__.__name__,
            "response_type": "ListPrivateZonesResponse"
            }

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_public_zones(self, request):
        """查询公网Zone列表

        查询公网Zone列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListPublicZones
        :type request: :class:`huaweicloudsdkdns.v2.ListPublicZonesRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.ListPublicZonesResponse`
        """
        http_info = self._list_public_zones_http_info(request)
        return self._call_api(**http_info)

    def list_public_zones_invoker(self, request):
        http_info = self._list_public_zones_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_public_zones_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/zones",
            "request_type": request.__class__.__name__,
            "response_type": "ListPublicZonesResponse"
            }

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_private_zone(self, request):
        """查询单个内网Zone

        查询单个内网Zone
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowPrivateZone
        :type request: :class:`huaweicloudsdkdns.v2.ShowPrivateZoneRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.ShowPrivateZoneResponse`
        """
        http_info = self._show_private_zone_http_info(request)
        return self._call_api(**http_info)

    def show_private_zone_invoker(self, request):
        http_info = self._show_private_zone_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_private_zone_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/zones/{zone_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowPrivateZoneResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'zone_id' in local_var_params:
            path_params['zone_id'] = local_var_params['zone_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_private_zone_name_server(self, request):
        """查询单个内网Zone的名称服务器

        查询单个内网Zone的名称服务器
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowPrivateZoneNameServer
        :type request: :class:`huaweicloudsdkdns.v2.ShowPrivateZoneNameServerRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.ShowPrivateZoneNameServerResponse`
        """
        http_info = self._show_private_zone_name_server_http_info(request)
        return self._call_api(**http_info)

    def show_private_zone_name_server_invoker(self, request):
        http_info = self._show_private_zone_name_server_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_private_zone_name_server_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/zones/{zone_id}/nameservers",
            "request_type": request.__class__.__name__,
            "response_type": "ShowPrivateZoneNameServerResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'zone_id' in local_var_params:
            path_params['zone_id'] = local_var_params['zone_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_public_zone(self, request):
        """查询单个公网Zone

        查询单个公网Zone
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowPublicZone
        :type request: :class:`huaweicloudsdkdns.v2.ShowPublicZoneRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.ShowPublicZoneResponse`
        """
        http_info = self._show_public_zone_http_info(request)
        return self._call_api(**http_info)

    def show_public_zone_invoker(self, request):
        http_info = self._show_public_zone_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_public_zone_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/zones/{zone_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowPublicZoneResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'zone_id' in local_var_params:
            path_params['zone_id'] = local_var_params['zone_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_public_zone_name_server(self, request):
        """查询单个公网Zone的名称服务器

        查询单个公网Zone的名称服务器
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowPublicZoneNameServer
        :type request: :class:`huaweicloudsdkdns.v2.ShowPublicZoneNameServerRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.ShowPublicZoneNameServerResponse`
        """
        http_info = self._show_public_zone_name_server_http_info(request)
        return self._call_api(**http_info)

    def show_public_zone_name_server_invoker(self, request):
        http_info = self._show_public_zone_name_server_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_public_zone_name_server_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/zones/{zone_id}/nameservers",
            "request_type": request.__class__.__name__,
            "response_type": "ShowPublicZoneNameServerResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'zone_id' in local_var_params:
            path_params['zone_id'] = local_var_params['zone_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_private_zone(self, request):
        """修改单个内网Zone

        修改单个内网Zone
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdatePrivateZone
        :type request: :class:`huaweicloudsdkdns.v2.UpdatePrivateZoneRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.UpdatePrivateZoneResponse`
        """
        http_info = self._update_private_zone_http_info(request)
        return self._call_api(**http_info)

    def update_private_zone_invoker(self, request):
        http_info = self._update_private_zone_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_private_zone_http_info(cls, request):
        http_info = {
            "method": "PATCH",
            "resource_path": "/v2/zones/{zone_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdatePrivateZoneResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'zone_id' in local_var_params:
            path_params['zone_id'] = local_var_params['zone_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_public_zone(self, request):
        """修改单个公网Zone

        修改单个公网Zone
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdatePublicZone
        :type request: :class:`huaweicloudsdkdns.v2.UpdatePublicZoneRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.UpdatePublicZoneResponse`
        """
        http_info = self._update_public_zone_http_info(request)
        return self._call_api(**http_info)

    def update_public_zone_invoker(self, request):
        http_info = self._update_public_zone_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_public_zone_http_info(cls, request):
        http_info = {
            "method": "PATCH",
            "resource_path": "/v2/zones/{zone_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdatePublicZoneResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'zone_id' in local_var_params:
            path_params['zone_id'] = local_var_params['zone_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_public_zone_status(self, request):
        """设置单个公网Zone状态

        设置单个公网Zone状态，支持暂停、启用Zone
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdatePublicZoneStatus
        :type request: :class:`huaweicloudsdkdns.v2.UpdatePublicZoneStatusRequest`
        :rtype: :class:`huaweicloudsdkdns.v2.UpdatePublicZoneStatusResponse`
        """
        http_info = self._update_public_zone_status_http_info(request)
        return self._call_api(**http_info)

    def update_public_zone_status_invoker(self, request):
        http_info = self._update_public_zone_status_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_public_zone_status_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/zones/{zone_id}/statuses",
            "request_type": request.__class__.__name__,
            "response_type": "UpdatePublicZoneStatusResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'zone_id' in local_var_params:
            path_params['zone_id'] = local_var_params['zone_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def _call_api(self, **kwargs):
        try:
            return self.do_http_request(**kwargs)
        except TypeError:
            import inspect
            params = inspect.signature(self.do_http_request).parameters
            http_info = {param_name: kwargs.get(param_name) for param_name in params if param_name in kwargs}
            return self.do_http_request(**http_info)

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

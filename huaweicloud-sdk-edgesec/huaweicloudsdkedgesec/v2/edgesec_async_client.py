# coding: utf-8

from __future__ import absolute_import

import importlib
import warnings

from huaweicloudsdkcore.client import Client, ClientBuilder
from huaweicloudsdkcore.utils import http_utils
from huaweicloudsdkcore.sdk_stream_request import SdkStreamRequest

try:
    from huaweicloudsdkcore.invoker.invoker import AsyncInvoker
except ImportError as e:
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkedgesec'")


class EdgeSecAsyncClient(Client):
    def __init__(self):
        super(EdgeSecAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkedgesec.v2.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls, "GlobalCredentials,BasicCredentials")
        else:
            if clazz.__name__ != "EdgeSecAsyncClient":
                raise TypeError("client type error, support client type is EdgeSecAsyncClient")
            client_builder = ClientBuilder(clazz, "GlobalCredentials,BasicCredentials")

        

        return client_builder

    def create_domain_async(self, request):
        r"""创建防护域名

        创建防护域名
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateDomain
        :type request: :class:`huaweicloudsdkedgesec.v2.CreateDomainRequest`
        :rtype: :class:`huaweicloudsdkedgesec.v2.CreateDomainResponse`
        """
        http_info = self._create_domain_http_info(request)
        return self._call_api(**http_info)

    def create_domain_async_invoker(self, request):
        http_info = self._create_domain_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_domain_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/edgesec/configuration/domains",
            "request_type": request.__class__.__name__,
            "response_type": "CreateDomainResponse"
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

    def create_http_reference_table_async(self, request):
        r"""创建引用表

        创建引用表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateHttpReferenceTable
        :type request: :class:`huaweicloudsdkedgesec.v2.CreateHttpReferenceTableRequest`
        :rtype: :class:`huaweicloudsdkedgesec.v2.CreateHttpReferenceTableResponse`
        """
        http_info = self._create_http_reference_table_http_info(request)
        return self._call_api(**http_info)

    def create_http_reference_table_async_invoker(self, request):
        http_info = self._create_http_reference_table_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_http_reference_table_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/edgesec/configuration/http/reference-table",
            "request_type": request.__class__.__name__,
            "response_type": "CreateHttpReferenceTableResponse"
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

    def delete_domain_async(self, request):
        r"""删除防护域名

        删除防护域名
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteDomain
        :type request: :class:`huaweicloudsdkedgesec.v2.DeleteDomainRequest`
        :rtype: :class:`huaweicloudsdkedgesec.v2.DeleteDomainResponse`
        """
        http_info = self._delete_domain_http_info(request)
        return self._call_api(**http_info)

    def delete_domain_async_invoker(self, request):
        http_info = self._delete_domain_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_domain_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/edgesec/configuration/domains/{domain_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteDomainResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']

        query_params = []
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

    def delete_http_reference_table_async(self, request):
        r"""删除引用表

        删除引用表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteHttpReferenceTable
        :type request: :class:`huaweicloudsdkedgesec.v2.DeleteHttpReferenceTableRequest`
        :rtype: :class:`huaweicloudsdkedgesec.v2.DeleteHttpReferenceTableResponse`
        """
        http_info = self._delete_http_reference_table_http_info(request)
        return self._call_api(**http_info)

    def delete_http_reference_table_async_invoker(self, request):
        http_info = self._delete_http_reference_table_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_http_reference_table_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/edgesec/configuration/http/reference-table/{table_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteHttpReferenceTableResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'table_id' in local_var_params:
            path_params['table_id'] = local_var_params['table_id']

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

    def show_domain_detail_async(self, request):
        r"""查询防护域名详情

        查询防护域名
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowDomainDetail
        :type request: :class:`huaweicloudsdkedgesec.v2.ShowDomainDetailRequest`
        :rtype: :class:`huaweicloudsdkedgesec.v2.ShowDomainDetailResponse`
        """
        http_info = self._show_domain_detail_http_info(request)
        return self._call_api(**http_info)

    def show_domain_detail_async_invoker(self, request):
        http_info = self._show_domain_detail_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_domain_detail_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/edgesec/configuration/domains/{domain_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDomainDetailResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']

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

    def show_domains_async(self, request):
        r"""查询防护域名列表

        查询防护域名列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowDomains
        :type request: :class:`huaweicloudsdkedgesec.v2.ShowDomainsRequest`
        :rtype: :class:`huaweicloudsdkedgesec.v2.ShowDomainsResponse`
        """
        http_info = self._show_domains_http_info(request)
        return self._call_api(**http_info)

    def show_domains_async_invoker(self, request):
        http_info = self._show_domains_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_domains_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/edgesec/configuration/domains",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDomainsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'domain_name' in local_var_params:
            query_params.append(('domain_name', local_var_params['domain_name']))
        if 'policy_name' in local_var_params:
            query_params.append(('policy_name', local_var_params['policy_name']))
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

    def show_http_overviews_async(self, request):
        r"""查询攻击域名

        查询安全总览top信息，包含攻击域名、攻击源ip、攻击url、攻击来源区域、防护类型
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowHttpOverviews
        :type request: :class:`huaweicloudsdkedgesec.v2.ShowHttpOverviewsRequest`
        :rtype: :class:`huaweicloudsdkedgesec.v2.ShowHttpOverviewsResponse`
        """
        http_info = self._show_http_overviews_http_info(request)
        return self._call_api(**http_info)

    def show_http_overviews_async_invoker(self, request):
        http_info = self._show_http_overviews_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_http_overviews_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/edgesec/stat/http/overviews/classification",
            "request_type": request.__class__.__name__,
            "response_type": "ShowHttpOverviewsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if '_from' in local_var_params:
            query_params.append(('from', local_var_params['_from']))
        if 'to' in local_var_params:
            query_params.append(('to', local_var_params['to']))
        if 'top' in local_var_params:
            query_params.append(('top', local_var_params['top']))
        if 'domain_name' in local_var_params:
            query_params.append(('domain_name', local_var_params['domain_name']))

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

    def show_http_reference_tables_async(self, request):
        r"""查询引用表列表

        查询引用表列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowHttpReferenceTables
        :type request: :class:`huaweicloudsdkedgesec.v2.ShowHttpReferenceTablesRequest`
        :rtype: :class:`huaweicloudsdkedgesec.v2.ShowHttpReferenceTablesResponse`
        """
        http_info = self._show_http_reference_tables_http_info(request)
        return self._call_api(**http_info)

    def show_http_reference_tables_async_invoker(self, request):
        http_info = self._show_http_reference_tables_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_http_reference_tables_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/edgesec/configuration/http/reference-table",
            "request_type": request.__class__.__name__,
            "response_type": "ShowHttpReferenceTablesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'page' in local_var_params:
            query_params.append(('page', local_var_params['page']))
        if 'pagesize' in local_var_params:
            query_params.append(('pagesize', local_var_params['pagesize']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))

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

    def show_http_statistics_async(self, request):
        r"""查询安全总览请求数据

        查询安全总览请求数据
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowHttpStatistics
        :type request: :class:`huaweicloudsdkedgesec.v2.ShowHttpStatisticsRequest`
        :rtype: :class:`huaweicloudsdkedgesec.v2.ShowHttpStatisticsResponse`
        """
        http_info = self._show_http_statistics_http_info(request)
        return self._call_api(**http_info)

    def show_http_statistics_async_invoker(self, request):
        http_info = self._show_http_statistics_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_http_statistics_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/edgesec/stat/http/overviews/statistics",
            "request_type": request.__class__.__name__,
            "response_type": "ShowHttpStatisticsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if '_from' in local_var_params:
            query_params.append(('from', local_var_params['_from']))
        if 'to' in local_var_params:
            query_params.append(('to', local_var_params['to']))
        if 'domain_name' in local_var_params:
            query_params.append(('domain_name', local_var_params['domain_name']))

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

    def update_domain_async(self, request):
        r"""更新防护域名

        更新防护域名
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateDomain
        :type request: :class:`huaweicloudsdkedgesec.v2.UpdateDomainRequest`
        :rtype: :class:`huaweicloudsdkedgesec.v2.UpdateDomainResponse`
        """
        http_info = self._update_domain_http_info(request)
        return self._call_api(**http_info)

    def update_domain_async_invoker(self, request):
        http_info = self._update_domain_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_domain_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/edgesec/configuration/domains/{domain_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateDomainResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']

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

    def update_http_reference_table_async(self, request):
        r"""更新引用表

        更新引用表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateHttpReferenceTable
        :type request: :class:`huaweicloudsdkedgesec.v2.UpdateHttpReferenceTableRequest`
        :rtype: :class:`huaweicloudsdkedgesec.v2.UpdateHttpReferenceTableResponse`
        """
        http_info = self._update_http_reference_table_http_info(request)
        return self._call_api(**http_info)

    def update_http_reference_table_async_invoker(self, request):
        http_info = self._update_http_reference_table_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_http_reference_table_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/edgesec/configuration/http/reference-table/{table_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateHttpReferenceTableResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'table_id' in local_var_params:
            path_params['table_id'] = local_var_params['table_id']

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

    def download_ddos_attack_logs_async(self, request):
        r"""Ddos攻击日志下载

        Ddos攻击日志下载
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DownloadDdosAttackLogs
        :type request: :class:`huaweicloudsdkedgesec.v2.DownloadDdosAttackLogsRequest`
        :rtype: :class:`huaweicloudsdkedgesec.v2.DownloadDdosAttackLogsResponse`
        """
        http_info = self._download_ddos_attack_logs_http_info(request)
        return self._call_api(**http_info)

    def download_ddos_attack_logs_async_invoker(self, request):
        http_info = self._download_ddos_attack_logs_http_info(request)
        return AsyncInvoker(self, http_info)

    def _download_ddos_attack_logs_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/edgesec/log/ddos-attack-logs/download",
            "request_type": request.__class__.__name__,
            "response_type": "DownloadDdosAttackLogsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

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

    def show_ddos_attack_logs_async(self, request):
        r"""查询ddos攻击日志列表

        查询ddos攻击日志列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowDdosAttackLogs
        :type request: :class:`huaweicloudsdkedgesec.v2.ShowDdosAttackLogsRequest`
        :rtype: :class:`huaweicloudsdkedgesec.v2.ShowDdosAttackLogsResponse`
        """
        http_info = self._show_ddos_attack_logs_http_info(request)
        return self._call_api(**http_info)

    def show_ddos_attack_logs_async_invoker(self, request):
        http_info = self._show_ddos_attack_logs_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_ddos_attack_logs_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/edgesec/log/ddos-attack-logs",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDdosAttackLogsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

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

    def show_ddos_attack_timeline_stats_async(self, request):
        r"""查询DDoS攻击统计时间线数据

        查询DDoS攻击统计时间线数据
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowDdosAttackTimelineStats
        :type request: :class:`huaweicloudsdkedgesec.v2.ShowDdosAttackTimelineStatsRequest`
        :rtype: :class:`huaweicloudsdkedgesec.v2.ShowDdosAttackTimelineStatsResponse`
        """
        http_info = self._show_ddos_attack_timeline_stats_http_info(request)
        return self._call_api(**http_info)

    def show_ddos_attack_timeline_stats_async_invoker(self, request):
        http_info = self._show_ddos_attack_timeline_stats_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_ddos_attack_timeline_stats_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/edgesec/stat/ddos-attack-timelines",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDdosAttackTimelineStatsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'stat_type' in local_var_params:
            query_params.append(('stat_type', local_var_params['stat_type']))
        if 'group_by' in local_var_params:
            query_params.append(('group_by', local_var_params['group_by']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))

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

    def apply_http_policy_async(self, request):
        r"""更新防护策略的域名

        更新防护策略的域名
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ApplyHttpPolicy
        :type request: :class:`huaweicloudsdkedgesec.v2.ApplyHttpPolicyRequest`
        :rtype: :class:`huaweicloudsdkedgesec.v2.ApplyHttpPolicyResponse`
        """
        http_info = self._apply_http_policy_http_info(request)
        return self._call_api(**http_info)

    def apply_http_policy_async_invoker(self, request):
        http_info = self._apply_http_policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _apply_http_policy_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/edgesec/configuration/http/policies/{policy_id}/hosts",
            "request_type": request.__class__.__name__,
            "response_type": "ApplyHttpPolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']

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

    def create_http_policy_async(self, request):
        r"""创建防护策略

        创建防护策略
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateHttpPolicy
        :type request: :class:`huaweicloudsdkedgesec.v2.CreateHttpPolicyRequest`
        :rtype: :class:`huaweicloudsdkedgesec.v2.CreateHttpPolicyResponse`
        """
        http_info = self._create_http_policy_http_info(request)
        return self._call_api(**http_info)

    def create_http_policy_async_invoker(self, request):
        http_info = self._create_http_policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_http_policy_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/edgesec/configuration/http/policies",
            "request_type": request.__class__.__name__,
            "response_type": "CreateHttpPolicyResponse"
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

    def delete_http_policy_async(self, request):
        r"""删除防护策略

        删除防护策略
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteHttpPolicy
        :type request: :class:`huaweicloudsdkedgesec.v2.DeleteHttpPolicyRequest`
        :rtype: :class:`huaweicloudsdkedgesec.v2.DeleteHttpPolicyResponse`
        """
        http_info = self._delete_http_policy_http_info(request)
        return self._call_api(**http_info)

    def delete_http_policy_async_invoker(self, request):
        http_info = self._delete_http_policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_http_policy_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/edgesec/configuration/http/policies/{policy_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteHttpPolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']

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

    def show_http_attack_distribution_stats_async(self, request):
        r"""查询HTTP攻击分布数据

        查询HTTP攻击分布数据
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowHttpAttackDistributionStats
        :type request: :class:`huaweicloudsdkedgesec.v2.ShowHttpAttackDistributionStatsRequest`
        :rtype: :class:`huaweicloudsdkedgesec.v2.ShowHttpAttackDistributionStatsResponse`
        """
        http_info = self._show_http_attack_distribution_stats_http_info(request)
        return self._call_api(**http_info)

    def show_http_attack_distribution_stats_async_invoker(self, request):
        http_info = self._show_http_attack_distribution_stats_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_http_attack_distribution_stats_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/edgesec/stat/http-attack-distribution",
            "request_type": request.__class__.__name__,
            "response_type": "ShowHttpAttackDistributionStatsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'domain_name' in local_var_params:
            query_params.append(('domain_name', local_var_params['domain_name']))
        if 'stat_type' in local_var_params:
            query_params.append(('stat_type', local_var_params['stat_type']))
        if 'group_by' in local_var_params:
            query_params.append(('group_by', local_var_params['group_by']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))

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

    def show_http_attack_timeline_stats_async(self, request):
        r"""查询HTTP攻击统计时间线数据

        查询HTTP攻击统计时间线数据
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowHttpAttackTimelineStats
        :type request: :class:`huaweicloudsdkedgesec.v2.ShowHttpAttackTimelineStatsRequest`
        :rtype: :class:`huaweicloudsdkedgesec.v2.ShowHttpAttackTimelineStatsResponse`
        """
        http_info = self._show_http_attack_timeline_stats_http_info(request)
        return self._call_api(**http_info)

    def show_http_attack_timeline_stats_async_invoker(self, request):
        http_info = self._show_http_attack_timeline_stats_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_http_attack_timeline_stats_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/edgesec/stat/http-attack-timelines",
            "request_type": request.__class__.__name__,
            "response_type": "ShowHttpAttackTimelineStatsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'domain_name' in local_var_params:
            query_params.append(('domain_name', local_var_params['domain_name']))
        if 'stat_type' in local_var_params:
            query_params.append(('stat_type', local_var_params['stat_type']))
        if 'group_by' in local_var_params:
            query_params.append(('group_by', local_var_params['group_by']))
        if 'group_by_value' in local_var_params:
            query_params.append(('group_by_value', local_var_params['group_by_value']))
        if 'interval' in local_var_params:
            query_params.append(('interval', local_var_params['interval']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))

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

    def show_http_attack_top_stats_async(self, request):
        r"""查询HTTP攻击TOP数据

        查询HTTP攻击TOP数据
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowHttpAttackTopStats
        :type request: :class:`huaweicloudsdkedgesec.v2.ShowHttpAttackTopStatsRequest`
        :rtype: :class:`huaweicloudsdkedgesec.v2.ShowHttpAttackTopStatsResponse`
        """
        http_info = self._show_http_attack_top_stats_http_info(request)
        return self._call_api(**http_info)

    def show_http_attack_top_stats_async_invoker(self, request):
        http_info = self._show_http_attack_top_stats_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_http_attack_top_stats_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/edgesec/stat/http-attack-top",
            "request_type": request.__class__.__name__,
            "response_type": "ShowHttpAttackTopStatsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'domain_name' in local_var_params:
            query_params.append(('domain_name', local_var_params['domain_name']))
        if 'stat_type' in local_var_params:
            query_params.append(('stat_type', local_var_params['stat_type']))
        if 'group_by' in local_var_params:
            query_params.append(('group_by', local_var_params['group_by']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'time_type' in local_var_params:
            query_params.append(('time_type', local_var_params['time_type']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))

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

    def show_http_policies_async(self, request):
        r"""查询防护策略列表

        查询防护策略列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowHttpPolicies
        :type request: :class:`huaweicloudsdkedgesec.v2.ShowHttpPoliciesRequest`
        :rtype: :class:`huaweicloudsdkedgesec.v2.ShowHttpPoliciesResponse`
        """
        http_info = self._show_http_policies_http_info(request)
        return self._call_api(**http_info)

    def show_http_policies_async_invoker(self, request):
        http_info = self._show_http_policies_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_http_policies_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/edgesec/configuration/http/policies",
            "request_type": request.__class__.__name__,
            "response_type": "ShowHttpPoliciesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'page' in local_var_params:
            query_params.append(('page', local_var_params['page']))
        if 'pagesize' in local_var_params:
            query_params.append(('pagesize', local_var_params['pagesize']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'hostname' in local_var_params:
            query_params.append(('hostname', local_var_params['hostname']))

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

    def show_http_policy_async(self, request):
        r"""查询防护策略

        查询防护策略
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowHttpPolicy
        :type request: :class:`huaweicloudsdkedgesec.v2.ShowHttpPolicyRequest`
        :rtype: :class:`huaweicloudsdkedgesec.v2.ShowHttpPolicyResponse`
        """
        http_info = self._show_http_policy_http_info(request)
        return self._call_api(**http_info)

    def show_http_policy_async_invoker(self, request):
        http_info = self._show_http_policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_http_policy_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/edgesec/configuration/http/policies/{policy_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowHttpPolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']

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

    def update_http_policy_async(self, request):
        r"""更新防护策略

        更新防护策略
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateHttpPolicy
        :type request: :class:`huaweicloudsdkedgesec.v2.UpdateHttpPolicyRequest`
        :rtype: :class:`huaweicloudsdkedgesec.v2.UpdateHttpPolicyResponse`
        """
        http_info = self._update_http_policy_http_info(request)
        return self._call_api(**http_info)

    def update_http_policy_async_invoker(self, request):
        http_info = self._update_http_policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_http_policy_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/edgesec/configuration/http/policies/{policy_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateHttpPolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']

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

    def update_http_policy_rule_status_async(self, request):
        r"""更新防护策略规则开关

        更新防护策略规则开关
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateHttpPolicyRuleStatus
        :type request: :class:`huaweicloudsdkedgesec.v2.UpdateHttpPolicyRuleStatusRequest`
        :rtype: :class:`huaweicloudsdkedgesec.v2.UpdateHttpPolicyRuleStatusResponse`
        """
        http_info = self._update_http_policy_rule_status_http_info(request)
        return self._call_api(**http_info)

    def update_http_policy_rule_status_async_invoker(self, request):
        http_info = self._update_http_policy_rule_status_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_http_policy_rule_status_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/edgesec/configuration/http/policies/{policy_id}/{rule_type}/{rule_id}/status",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateHttpPolicyRuleStatusResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']
        if 'rule_type' in local_var_params:
            path_params['rule_type'] = local_var_params['rule_type']
        if 'rule_id' in local_var_params:
            path_params['rule_id'] = local_var_params['rule_id']

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

    def create_http_access_control_rule_async(self, request):
        r"""创建精准防护规则

        创建精准防护规则
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateHttpAccessControlRule
        :type request: :class:`huaweicloudsdkedgesec.v2.CreateHttpAccessControlRuleRequest`
        :rtype: :class:`huaweicloudsdkedgesec.v2.CreateHttpAccessControlRuleResponse`
        """
        http_info = self._create_http_access_control_rule_http_info(request)
        return self._call_api(**http_info)

    def create_http_access_control_rule_async_invoker(self, request):
        http_info = self._create_http_access_control_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_http_access_control_rule_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/edgesec/configuration/http/policies/{policy_id}/access-control-rule",
            "request_type": request.__class__.__name__,
            "response_type": "CreateHttpAccessControlRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']

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

    def create_http_geo_ip_rule_async(self, request):
        r"""创建地理位置规则

        创建地理位置规则
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateHttpGeoIpRule
        :type request: :class:`huaweicloudsdkedgesec.v2.CreateHttpGeoIpRuleRequest`
        :rtype: :class:`huaweicloudsdkedgesec.v2.CreateHttpGeoIpRuleResponse`
        """
        http_info = self._create_http_geo_ip_rule_http_info(request)
        return self._call_api(**http_info)

    def create_http_geo_ip_rule_async_invoker(self, request):
        http_info = self._create_http_geo_ip_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_http_geo_ip_rule_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/edgesec/configuration/http/policies/{policy_id}/geoip-rule",
            "request_type": request.__class__.__name__,
            "response_type": "CreateHttpGeoIpRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']

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

    def create_http_ignore_rule_async(self, request):
        r"""创建误报屏蔽规则

        创建误报屏蔽规则
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateHttpIgnoreRule
        :type request: :class:`huaweicloudsdkedgesec.v2.CreateHttpIgnoreRuleRequest`
        :rtype: :class:`huaweicloudsdkedgesec.v2.CreateHttpIgnoreRuleResponse`
        """
        http_info = self._create_http_ignore_rule_http_info(request)
        return self._call_api(**http_info)

    def create_http_ignore_rule_async_invoker(self, request):
        http_info = self._create_http_ignore_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_http_ignore_rule_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/edgesec/configuration/http/policies/{policy_id}/ignore-rule",
            "request_type": request.__class__.__name__,
            "response_type": "CreateHttpIgnoreRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']

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

    def create_http_punishment_rule_async(self, request):
        r"""创建攻击惩罚规则

        创建攻击惩罚规则
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateHttpPunishmentRule
        :type request: :class:`huaweicloudsdkedgesec.v2.CreateHttpPunishmentRuleRequest`
        :rtype: :class:`huaweicloudsdkedgesec.v2.CreateHttpPunishmentRuleResponse`
        """
        http_info = self._create_http_punishment_rule_http_info(request)
        return self._call_api(**http_info)

    def create_http_punishment_rule_async_invoker(self, request):
        http_info = self._create_http_punishment_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_http_punishment_rule_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/edgesec/configuration/http/policies/{policy_id}/punishment-rule",
            "request_type": request.__class__.__name__,
            "response_type": "CreateHttpPunishmentRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']

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

    def delete_http_access_control_rule_async(self, request):
        r"""删除精准防护规则

        删除精准防护规则
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteHttpAccessControlRule
        :type request: :class:`huaweicloudsdkedgesec.v2.DeleteHttpAccessControlRuleRequest`
        :rtype: :class:`huaweicloudsdkedgesec.v2.DeleteHttpAccessControlRuleResponse`
        """
        http_info = self._delete_http_access_control_rule_http_info(request)
        return self._call_api(**http_info)

    def delete_http_access_control_rule_async_invoker(self, request):
        http_info = self._delete_http_access_control_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_http_access_control_rule_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/edgesec/configuration/http/policies/{policy_id}/access-control-rule/{rule_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteHttpAccessControlRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']
        if 'rule_id' in local_var_params:
            path_params['rule_id'] = local_var_params['rule_id']

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

    def delete_http_geo_ip_rule_async(self, request):
        r"""删除地理位置规则

        删除地理位置规则
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteHttpGeoIpRule
        :type request: :class:`huaweicloudsdkedgesec.v2.DeleteHttpGeoIpRuleRequest`
        :rtype: :class:`huaweicloudsdkedgesec.v2.DeleteHttpGeoIpRuleResponse`
        """
        http_info = self._delete_http_geo_ip_rule_http_info(request)
        return self._call_api(**http_info)

    def delete_http_geo_ip_rule_async_invoker(self, request):
        http_info = self._delete_http_geo_ip_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_http_geo_ip_rule_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/edgesec/configuration/http/policies/{policy_id}/geoip-rule/{rule_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteHttpGeoIpRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']
        if 'rule_id' in local_var_params:
            path_params['rule_id'] = local_var_params['rule_id']

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

    def delete_http_ignore_rule_async(self, request):
        r"""删除误报屏蔽规则

        删除误报屏蔽规则
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteHttpIgnoreRule
        :type request: :class:`huaweicloudsdkedgesec.v2.DeleteHttpIgnoreRuleRequest`
        :rtype: :class:`huaweicloudsdkedgesec.v2.DeleteHttpIgnoreRuleResponse`
        """
        http_info = self._delete_http_ignore_rule_http_info(request)
        return self._call_api(**http_info)

    def delete_http_ignore_rule_async_invoker(self, request):
        http_info = self._delete_http_ignore_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_http_ignore_rule_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/edgesec/configuration/http/policies/{policy_id}/ignore-rule/{rule_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteHttpIgnoreRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']
        if 'rule_id' in local_var_params:
            path_params['rule_id'] = local_var_params['rule_id']

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

    def delete_http_punishment_rule_async(self, request):
        r"""删除攻击惩罚规则

        删除攻击惩罚规则
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteHttpPunishmentRule
        :type request: :class:`huaweicloudsdkedgesec.v2.DeleteHttpPunishmentRuleRequest`
        :rtype: :class:`huaweicloudsdkedgesec.v2.DeleteHttpPunishmentRuleResponse`
        """
        http_info = self._delete_http_punishment_rule_http_info(request)
        return self._call_api(**http_info)

    def delete_http_punishment_rule_async_invoker(self, request):
        http_info = self._delete_http_punishment_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_http_punishment_rule_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/edgesec/configuration/http/policies/{policy_id}/punishment-rule/{rule_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteHttpPunishmentRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']
        if 'rule_id' in local_var_params:
            path_params['rule_id'] = local_var_params['rule_id']

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

    def reset_http_ignore_rule_async(self, request):
        r"""重置误报屏蔽规则

        重置误报屏蔽规则
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ResetHttpIgnoreRule
        :type request: :class:`huaweicloudsdkedgesec.v2.ResetHttpIgnoreRuleRequest`
        :rtype: :class:`huaweicloudsdkedgesec.v2.ResetHttpIgnoreRuleResponse`
        """
        http_info = self._reset_http_ignore_rule_http_info(request)
        return self._call_api(**http_info)

    def reset_http_ignore_rule_async_invoker(self, request):
        http_info = self._reset_http_ignore_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _reset_http_ignore_rule_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/edgesec/configuration/http/policies/{policy_id}/ignore-rule/{rule_id}/recount",
            "request_type": request.__class__.__name__,
            "response_type": "ResetHttpIgnoreRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']
        if 'rule_id' in local_var_params:
            path_params['rule_id'] = local_var_params['rule_id']

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

    def show_http_access_control_rule_async(self, request):
        r"""查询精准防护规则

        查询精准防护规则
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowHttpAccessControlRule
        :type request: :class:`huaweicloudsdkedgesec.v2.ShowHttpAccessControlRuleRequest`
        :rtype: :class:`huaweicloudsdkedgesec.v2.ShowHttpAccessControlRuleResponse`
        """
        http_info = self._show_http_access_control_rule_http_info(request)
        return self._call_api(**http_info)

    def show_http_access_control_rule_async_invoker(self, request):
        http_info = self._show_http_access_control_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_http_access_control_rule_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/edgesec/configuration/http/policies/{policy_id}/access-control-rule/{rule_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowHttpAccessControlRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']
        if 'rule_id' in local_var_params:
            path_params['rule_id'] = local_var_params['rule_id']

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

    def show_http_access_control_rules_async(self, request):
        r"""查询精准防护规则列表

        查询精准防护规则列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowHttpAccessControlRules
        :type request: :class:`huaweicloudsdkedgesec.v2.ShowHttpAccessControlRulesRequest`
        :rtype: :class:`huaweicloudsdkedgesec.v2.ShowHttpAccessControlRulesResponse`
        """
        http_info = self._show_http_access_control_rules_http_info(request)
        return self._call_api(**http_info)

    def show_http_access_control_rules_async_invoker(self, request):
        http_info = self._show_http_access_control_rules_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_http_access_control_rules_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/edgesec/configuration/http/policies/{policy_id}/access-control-rule",
            "request_type": request.__class__.__name__,
            "response_type": "ShowHttpAccessControlRulesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']

        query_params = []
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'page' in local_var_params:
            query_params.append(('page', local_var_params['page']))
        if 'pagesize' in local_var_params:
            query_params.append(('pagesize', local_var_params['pagesize']))

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

    def show_http_geo_ip_rule_async(self, request):
        r"""查询地理位置规则

        查询地理位置规则
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowHttpGeoIpRule
        :type request: :class:`huaweicloudsdkedgesec.v2.ShowHttpGeoIpRuleRequest`
        :rtype: :class:`huaweicloudsdkedgesec.v2.ShowHttpGeoIpRuleResponse`
        """
        http_info = self._show_http_geo_ip_rule_http_info(request)
        return self._call_api(**http_info)

    def show_http_geo_ip_rule_async_invoker(self, request):
        http_info = self._show_http_geo_ip_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_http_geo_ip_rule_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/edgesec/configuration/http/policies/{policy_id}/geoip-rule/{rule_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowHttpGeoIpRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']
        if 'rule_id' in local_var_params:
            path_params['rule_id'] = local_var_params['rule_id']

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

    def show_http_geo_ip_rules_async(self, request):
        r"""查询地理位置规则列表

        查询地理位置规则列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowHttpGeoIpRules
        :type request: :class:`huaweicloudsdkedgesec.v2.ShowHttpGeoIpRulesRequest`
        :rtype: :class:`huaweicloudsdkedgesec.v2.ShowHttpGeoIpRulesResponse`
        """
        http_info = self._show_http_geo_ip_rules_http_info(request)
        return self._call_api(**http_info)

    def show_http_geo_ip_rules_async_invoker(self, request):
        http_info = self._show_http_geo_ip_rules_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_http_geo_ip_rules_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/edgesec/configuration/http/policies/{policy_id}/geoip-rule",
            "request_type": request.__class__.__name__,
            "response_type": "ShowHttpGeoIpRulesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']

        query_params = []
        if 'page' in local_var_params:
            query_params.append(('page', local_var_params['page']))
        if 'pagesize' in local_var_params:
            query_params.append(('pagesize', local_var_params['pagesize']))

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

    def show_http_ignore_rule_async(self, request):
        r"""查询误报屏蔽规则

        查询误报屏蔽规则
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowHttpIgnoreRule
        :type request: :class:`huaweicloudsdkedgesec.v2.ShowHttpIgnoreRuleRequest`
        :rtype: :class:`huaweicloudsdkedgesec.v2.ShowHttpIgnoreRuleResponse`
        """
        http_info = self._show_http_ignore_rule_http_info(request)
        return self._call_api(**http_info)

    def show_http_ignore_rule_async_invoker(self, request):
        http_info = self._show_http_ignore_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_http_ignore_rule_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/edgesec/configuration/http/policies/{policy_id}/ignore-rule/{rule_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowHttpIgnoreRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']
        if 'rule_id' in local_var_params:
            path_params['rule_id'] = local_var_params['rule_id']

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

    def show_http_ignore_rules_async(self, request):
        r"""查询误报屏蔽规则列表

        查询误报屏蔽规则列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowHttpIgnoreRules
        :type request: :class:`huaweicloudsdkedgesec.v2.ShowHttpIgnoreRulesRequest`
        :rtype: :class:`huaweicloudsdkedgesec.v2.ShowHttpIgnoreRulesResponse`
        """
        http_info = self._show_http_ignore_rules_http_info(request)
        return self._call_api(**http_info)

    def show_http_ignore_rules_async_invoker(self, request):
        http_info = self._show_http_ignore_rules_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_http_ignore_rules_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/edgesec/configuration/http/policies/{policy_id}/ignore-rule",
            "request_type": request.__class__.__name__,
            "response_type": "ShowHttpIgnoreRulesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']

        query_params = []
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'page' in local_var_params:
            query_params.append(('page', local_var_params['page']))
        if 'pagesize' in local_var_params:
            query_params.append(('pagesize', local_var_params['pagesize']))
        if 'rule' in local_var_params:
            query_params.append(('rule', local_var_params['rule']))

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

    def show_http_punishment_rule_async(self, request):
        r"""查询攻击惩罚规则

        查询攻击惩罚规则
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowHttpPunishmentRule
        :type request: :class:`huaweicloudsdkedgesec.v2.ShowHttpPunishmentRuleRequest`
        :rtype: :class:`huaweicloudsdkedgesec.v2.ShowHttpPunishmentRuleResponse`
        """
        http_info = self._show_http_punishment_rule_http_info(request)
        return self._call_api(**http_info)

    def show_http_punishment_rule_async_invoker(self, request):
        http_info = self._show_http_punishment_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_http_punishment_rule_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/edgesec/configuration/http/policies/{policy_id}/punishment-rule/{rule_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowHttpPunishmentRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']
        if 'rule_id' in local_var_params:
            path_params['rule_id'] = local_var_params['rule_id']

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

    def show_http_punishment_rules_async(self, request):
        r"""查询攻击惩罚规则列表

        查询攻击惩罚规则列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowHttpPunishmentRules
        :type request: :class:`huaweicloudsdkedgesec.v2.ShowHttpPunishmentRulesRequest`
        :rtype: :class:`huaweicloudsdkedgesec.v2.ShowHttpPunishmentRulesResponse`
        """
        http_info = self._show_http_punishment_rules_http_info(request)
        return self._call_api(**http_info)

    def show_http_punishment_rules_async_invoker(self, request):
        http_info = self._show_http_punishment_rules_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_http_punishment_rules_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/edgesec/configuration/http/policies/{policy_id}/punishment-rule",
            "request_type": request.__class__.__name__,
            "response_type": "ShowHttpPunishmentRulesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']

        query_params = []
        if 'page' in local_var_params:
            query_params.append(('page', local_var_params['page']))
        if 'pagesize' in local_var_params:
            query_params.append(('pagesize', local_var_params['pagesize']))

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

    def update_http_access_control_rule_async(self, request):
        r"""更新精准防护规则

        更新精准防护规则
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateHttpAccessControlRule
        :type request: :class:`huaweicloudsdkedgesec.v2.UpdateHttpAccessControlRuleRequest`
        :rtype: :class:`huaweicloudsdkedgesec.v2.UpdateHttpAccessControlRuleResponse`
        """
        http_info = self._update_http_access_control_rule_http_info(request)
        return self._call_api(**http_info)

    def update_http_access_control_rule_async_invoker(self, request):
        http_info = self._update_http_access_control_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_http_access_control_rule_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/edgesec/configuration/http/policies/{policy_id}/access-control-rule/{rule_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateHttpAccessControlRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']
        if 'rule_id' in local_var_params:
            path_params['rule_id'] = local_var_params['rule_id']

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

    def update_http_geo_ip_rule_async(self, request):
        r"""更新地理位置规则

        更新地理位置规则
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateHttpGeoIpRule
        :type request: :class:`huaweicloudsdkedgesec.v2.UpdateHttpGeoIpRuleRequest`
        :rtype: :class:`huaweicloudsdkedgesec.v2.UpdateHttpGeoIpRuleResponse`
        """
        http_info = self._update_http_geo_ip_rule_http_info(request)
        return self._call_api(**http_info)

    def update_http_geo_ip_rule_async_invoker(self, request):
        http_info = self._update_http_geo_ip_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_http_geo_ip_rule_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/edgesec/configuration/http/policies/{policy_id}/geoip-rule/{rule_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateHttpGeoIpRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']
        if 'rule_id' in local_var_params:
            path_params['rule_id'] = local_var_params['rule_id']

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

    def update_http_ignore_rule_async(self, request):
        r"""更新误报屏蔽规则

        更新误报屏蔽规则
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateHttpIgnoreRule
        :type request: :class:`huaweicloudsdkedgesec.v2.UpdateHttpIgnoreRuleRequest`
        :rtype: :class:`huaweicloudsdkedgesec.v2.UpdateHttpIgnoreRuleResponse`
        """
        http_info = self._update_http_ignore_rule_http_info(request)
        return self._call_api(**http_info)

    def update_http_ignore_rule_async_invoker(self, request):
        http_info = self._update_http_ignore_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_http_ignore_rule_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/edgesec/configuration/http/policies/{policy_id}/ignore-rule/{rule_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateHttpIgnoreRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']
        if 'rule_id' in local_var_params:
            path_params['rule_id'] = local_var_params['rule_id']

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

    def update_http_punishment_rule_async(self, request):
        r"""更新攻击惩罚规则

        更新攻击惩罚规则
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateHttpPunishmentRule
        :type request: :class:`huaweicloudsdkedgesec.v2.UpdateHttpPunishmentRuleRequest`
        :rtype: :class:`huaweicloudsdkedgesec.v2.UpdateHttpPunishmentRuleResponse`
        """
        http_info = self._update_http_punishment_rule_http_info(request)
        return self._call_api(**http_info)

    def update_http_punishment_rule_async_invoker(self, request):
        http_info = self._update_http_punishment_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_http_punishment_rule_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/edgesec/configuration/http/policies/{policy_id}/punishment-rule/{rule_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateHttpPunishmentRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']
        if 'rule_id' in local_var_params:
            path_params['rule_id'] = local_var_params['rule_id']

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

    def create_http_cc_rule_async(self, request):
        r"""创建cc规则

        创建cc规则
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateHttpCcRule
        :type request: :class:`huaweicloudsdkedgesec.v2.CreateHttpCcRuleRequest`
        :rtype: :class:`huaweicloudsdkedgesec.v2.CreateHttpCcRuleResponse`
        """
        http_info = self._create_http_cc_rule_http_info(request)
        return self._call_api(**http_info)

    def create_http_cc_rule_async_invoker(self, request):
        http_info = self._create_http_cc_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_http_cc_rule_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/edgesec/configuration/http/policies/{policy_id}/cc-rule",
            "request_type": request.__class__.__name__,
            "response_type": "CreateHttpCcRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']

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

    def delete_http_cc_rule_async(self, request):
        r"""删除cc规则

        删除cc规则
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteHttpCcRule
        :type request: :class:`huaweicloudsdkedgesec.v2.DeleteHttpCcRuleRequest`
        :rtype: :class:`huaweicloudsdkedgesec.v2.DeleteHttpCcRuleResponse`
        """
        http_info = self._delete_http_cc_rule_http_info(request)
        return self._call_api(**http_info)

    def delete_http_cc_rule_async_invoker(self, request):
        http_info = self._delete_http_cc_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_http_cc_rule_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/edgesec/configuration/http/policies/{policy_id}/cc-rule/{rule_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteHttpCcRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']
        if 'rule_id' in local_var_params:
            path_params['rule_id'] = local_var_params['rule_id']

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

    def show_http_cc_rule_async(self, request):
        r"""查询cc规则

        查询cc规则
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowHttpCcRule
        :type request: :class:`huaweicloudsdkedgesec.v2.ShowHttpCcRuleRequest`
        :rtype: :class:`huaweicloudsdkedgesec.v2.ShowHttpCcRuleResponse`
        """
        http_info = self._show_http_cc_rule_http_info(request)
        return self._call_api(**http_info)

    def show_http_cc_rule_async_invoker(self, request):
        http_info = self._show_http_cc_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_http_cc_rule_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/edgesec/configuration/http/policies/{policy_id}/cc-rule/{rule_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowHttpCcRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']
        if 'rule_id' in local_var_params:
            path_params['rule_id'] = local_var_params['rule_id']

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

    def show_http_cc_rules_async(self, request):
        r"""查询cc规则列表

        查询cc规则列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowHttpCcRules
        :type request: :class:`huaweicloudsdkedgesec.v2.ShowHttpCcRulesRequest`
        :rtype: :class:`huaweicloudsdkedgesec.v2.ShowHttpCcRulesResponse`
        """
        http_info = self._show_http_cc_rules_http_info(request)
        return self._call_api(**http_info)

    def show_http_cc_rules_async_invoker(self, request):
        http_info = self._show_http_cc_rules_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_http_cc_rules_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/edgesec/configuration/http/policies/{policy_id}/cc-rule",
            "request_type": request.__class__.__name__,
            "response_type": "ShowHttpCcRulesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']

        query_params = []
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'page' in local_var_params:
            query_params.append(('page', local_var_params['page']))
        if 'pagesize' in local_var_params:
            query_params.append(('pagesize', local_var_params['pagesize']))

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

    def update_http_cc_rule_async(self, request):
        r"""更新cc规则

        更新cc规则
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateHttpCcRule
        :type request: :class:`huaweicloudsdkedgesec.v2.UpdateHttpCcRuleRequest`
        :rtype: :class:`huaweicloudsdkedgesec.v2.UpdateHttpCcRuleResponse`
        """
        http_info = self._update_http_cc_rule_http_info(request)
        return self._call_api(**http_info)

    def update_http_cc_rule_async_invoker(self, request):
        http_info = self._update_http_cc_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_http_cc_rule_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/edgesec/configuration/http/policies/{policy_id}/cc-rule/{rule_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateHttpCcRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']
        if 'rule_id' in local_var_params:
            path_params['rule_id'] = local_var_params['rule_id']

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

    def create_http_block_trust_ip_rule_async(self, request):
        r"""创建IP黑白名单规则

        创建IP黑白名单规则
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateHttpBlockTrustIpRule
        :type request: :class:`huaweicloudsdkedgesec.v2.CreateHttpBlockTrustIpRuleRequest`
        :rtype: :class:`huaweicloudsdkedgesec.v2.CreateHttpBlockTrustIpRuleResponse`
        """
        http_info = self._create_http_block_trust_ip_rule_http_info(request)
        return self._call_api(**http_info)

    def create_http_block_trust_ip_rule_async_invoker(self, request):
        http_info = self._create_http_block_trust_ip_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_http_block_trust_ip_rule_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/edgesec/configuration/http/policies/{policy_id}/blocktrustip-rule",
            "request_type": request.__class__.__name__,
            "response_type": "CreateHttpBlockTrustIpRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']

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

    def delete_http_block_trust_ip_rule_async(self, request):
        r"""删除IP黑白名单规则

        删除IP黑白名单规则
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteHttpBlockTrustIpRule
        :type request: :class:`huaweicloudsdkedgesec.v2.DeleteHttpBlockTrustIpRuleRequest`
        :rtype: :class:`huaweicloudsdkedgesec.v2.DeleteHttpBlockTrustIpRuleResponse`
        """
        http_info = self._delete_http_block_trust_ip_rule_http_info(request)
        return self._call_api(**http_info)

    def delete_http_block_trust_ip_rule_async_invoker(self, request):
        http_info = self._delete_http_block_trust_ip_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_http_block_trust_ip_rule_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/edgesec/configuration/http/policies/{policy_id}/blocktrustip-rule/{rule_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteHttpBlockTrustIpRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']
        if 'rule_id' in local_var_params:
            path_params['rule_id'] = local_var_params['rule_id']

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

    def show_http_block_trust_ip_rule_async(self, request):
        r"""查询IP黑白名单规则

        查询IP黑白名单规则
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowHttpBlockTrustIpRule
        :type request: :class:`huaweicloudsdkedgesec.v2.ShowHttpBlockTrustIpRuleRequest`
        :rtype: :class:`huaweicloudsdkedgesec.v2.ShowHttpBlockTrustIpRuleResponse`
        """
        http_info = self._show_http_block_trust_ip_rule_http_info(request)
        return self._call_api(**http_info)

    def show_http_block_trust_ip_rule_async_invoker(self, request):
        http_info = self._show_http_block_trust_ip_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_http_block_trust_ip_rule_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/edgesec/configuration/http/policies/{policy_id}/blocktrustip-rule/{rule_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowHttpBlockTrustIpRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']
        if 'rule_id' in local_var_params:
            path_params['rule_id'] = local_var_params['rule_id']

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

    def show_http_block_trust_ip_rules_async(self, request):
        r"""查询IP黑白名单规则列表

        查询IP黑白名单规则列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowHttpBlockTrustIpRules
        :type request: :class:`huaweicloudsdkedgesec.v2.ShowHttpBlockTrustIpRulesRequest`
        :rtype: :class:`huaweicloudsdkedgesec.v2.ShowHttpBlockTrustIpRulesResponse`
        """
        http_info = self._show_http_block_trust_ip_rules_http_info(request)
        return self._call_api(**http_info)

    def show_http_block_trust_ip_rules_async_invoker(self, request):
        http_info = self._show_http_block_trust_ip_rules_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_http_block_trust_ip_rules_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/edgesec/configuration/http/policies/{policy_id}/blocktrustip-rule",
            "request_type": request.__class__.__name__,
            "response_type": "ShowHttpBlockTrustIpRulesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']

        query_params = []
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'addr' in local_var_params:
            query_params.append(('addr', local_var_params['addr']))
        if 'page' in local_var_params:
            query_params.append(('page', local_var_params['page']))
        if 'pagesize' in local_var_params:
            query_params.append(('pagesize', local_var_params['pagesize']))

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

    def update_http_block_trust_ip_rule_async(self, request):
        r"""更新IP黑白名单规则

        更新IP黑白名单规则
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateHttpBlockTrustIpRule
        :type request: :class:`huaweicloudsdkedgesec.v2.UpdateHttpBlockTrustIpRuleRequest`
        :rtype: :class:`huaweicloudsdkedgesec.v2.UpdateHttpBlockTrustIpRuleResponse`
        """
        http_info = self._update_http_block_trust_ip_rule_http_info(request)
        return self._call_api(**http_info)

    def update_http_block_trust_ip_rule_async_invoker(self, request):
        http_info = self._update_http_block_trust_ip_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_http_block_trust_ip_rule_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/edgesec/configuration/http/policies/{policy_id}/blocktrustip-rule/{rule_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateHttpBlockTrustIpRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']
        if 'rule_id' in local_var_params:
            path_params['rule_id'] = local_var_params['rule_id']

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

    def create_http_ip_group_async(self, request):
        r"""创建IP地址组

        创建IP地址组
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateHttpIpGroup
        :type request: :class:`huaweicloudsdkedgesec.v2.CreateHttpIpGroupRequest`
        :rtype: :class:`huaweicloudsdkedgesec.v2.CreateHttpIpGroupResponse`
        """
        http_info = self._create_http_ip_group_http_info(request)
        return self._call_api(**http_info)

    def create_http_ip_group_async_invoker(self, request):
        http_info = self._create_http_ip_group_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_http_ip_group_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/edgesec/configuration/http/ip-groups",
            "request_type": request.__class__.__name__,
            "response_type": "CreateHttpIpGroupResponse"
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

    def delete_http_ip_group_async(self, request):
        r"""删除IP地址组

        删除IP地址组
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteHttpIpGroup
        :type request: :class:`huaweicloudsdkedgesec.v2.DeleteHttpIpGroupRequest`
        :rtype: :class:`huaweicloudsdkedgesec.v2.DeleteHttpIpGroupResponse`
        """
        http_info = self._delete_http_ip_group_http_info(request)
        return self._call_api(**http_info)

    def delete_http_ip_group_async_invoker(self, request):
        http_info = self._delete_http_ip_group_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_http_ip_group_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/edgesec/configuration/http/ip-groups/{ip_group_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteHttpIpGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ip_group_id' in local_var_params:
            path_params['ip_group_id'] = local_var_params['ip_group_id']

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

    def show_http_ip_group_async(self, request):
        r"""查询IP地址组

        查询IP地址组
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowHttpIpGroup
        :type request: :class:`huaweicloudsdkedgesec.v2.ShowHttpIpGroupRequest`
        :rtype: :class:`huaweicloudsdkedgesec.v2.ShowHttpIpGroupResponse`
        """
        http_info = self._show_http_ip_group_http_info(request)
        return self._call_api(**http_info)

    def show_http_ip_group_async_invoker(self, request):
        http_info = self._show_http_ip_group_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_http_ip_group_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/edgesec/configuration/http/ip-groups/{ip_group_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowHttpIpGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ip_group_id' in local_var_params:
            path_params['ip_group_id'] = local_var_params['ip_group_id']

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

    def show_http_ip_groups_async(self, request):
        r"""查询IP地址组列表

        查询IP地址组列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowHttpIpGroups
        :type request: :class:`huaweicloudsdkedgesec.v2.ShowHttpIpGroupsRequest`
        :rtype: :class:`huaweicloudsdkedgesec.v2.ShowHttpIpGroupsResponse`
        """
        http_info = self._show_http_ip_groups_http_info(request)
        return self._call_api(**http_info)

    def show_http_ip_groups_async_invoker(self, request):
        http_info = self._show_http_ip_groups_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_http_ip_groups_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/edgesec/configuration/http/ip-groups",
            "request_type": request.__class__.__name__,
            "response_type": "ShowHttpIpGroupsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'page' in local_var_params:
            query_params.append(('page', local_var_params['page']))
        if 'pagesize' in local_var_params:
            query_params.append(('pagesize', local_var_params['pagesize']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'ip' in local_var_params:
            query_params.append(('ip', local_var_params['ip']))

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

    def update_http_ip_group_async(self, request):
        r"""更新IP地址组

        更新IP地址组
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateHttpIpGroup
        :type request: :class:`huaweicloudsdkedgesec.v2.UpdateHttpIpGroupRequest`
        :rtype: :class:`huaweicloudsdkedgesec.v2.UpdateHttpIpGroupResponse`
        """
        http_info = self._update_http_ip_group_http_info(request)
        return self._call_api(**http_info)

    def update_http_ip_group_async_invoker(self, request):
        http_info = self._update_http_ip_group_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_http_ip_group_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/edgesec/configuration/http/ip-groups/{ip_group_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateHttpIpGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ip_group_id' in local_var_params:
            path_params['ip_group_id'] = local_var_params['ip_group_id']

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
            kwargs["async_request"] = True
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

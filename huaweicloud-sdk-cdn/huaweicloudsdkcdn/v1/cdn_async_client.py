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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkcdn'")


class CdnAsyncClient(Client):
    def __init__(self):
        super(CdnAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkcdn.v1.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls, "GlobalCredentials")
        else:
            if clazz.__name__ != "CdnAsyncClient":
                raise TypeError("client type error, support client type is CdnAsyncClient")
            client_builder = ClientBuilder(clazz, "GlobalCredentials")

        

        return client_builder

    def batch_delete_tags_async(self, request):
        r"""删除资源标签配置接口

        用于删除资源标签。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchDeleteTags
        :type request: :class:`huaweicloudsdkcdn.v1.BatchDeleteTagsRequest`
        :rtype: :class:`huaweicloudsdkcdn.v1.BatchDeleteTagsResponse`
        """
        warnings.warn("Method 'batch_delete_tags_async' of CdnAsyncClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._batch_delete_tags_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_tags_async_invoker(self, request):
        warnings.warn("Method 'batch_delete_tags_async_invoker' of CdnAsyncClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._batch_delete_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_delete_tags_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/cdn/configuration/tags/batch-delete",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeleteTagsResponse"
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

        response_headers = ["X-Request-Id", ]

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

    def create_domain_async(self, request):
        r"""创建加速域名

        创建加速域名。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateDomain
        :type request: :class:`huaweicloudsdkcdn.v1.CreateDomainRequest`
        :rtype: :class:`huaweicloudsdkcdn.v1.CreateDomainResponse`
        """
        warnings.warn("Method 'create_domain_async' of CdnAsyncClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._create_domain_http_info(request)
        return self._call_api(**http_info)

    def create_domain_async_invoker(self, request):
        warnings.warn("Method 'create_domain_async_invoker' of CdnAsyncClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._create_domain_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_domain_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/cdn/domains",
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

        response_headers = ["X-Request-Id", ]

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

    def create_preheating_tasks_async(self, request):
        r"""创建预热缓存任务

        创建预热任务。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreatePreheatingTasks
        :type request: :class:`huaweicloudsdkcdn.v1.CreatePreheatingTasksRequest`
        :rtype: :class:`huaweicloudsdkcdn.v1.CreatePreheatingTasksResponse`
        """
        warnings.warn("Method 'create_preheating_tasks_async' of CdnAsyncClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._create_preheating_tasks_http_info(request)
        return self._call_api(**http_info)

    def create_preheating_tasks_async_invoker(self, request):
        warnings.warn("Method 'create_preheating_tasks_async_invoker' of CdnAsyncClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._create_preheating_tasks_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_preheating_tasks_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/cdn/content/preheating-tasks",
            "request_type": request.__class__.__name__,
            "response_type": "CreatePreheatingTasksResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

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

    def create_refresh_tasks_async(self, request):
        r"""创建刷新缓存任务

        创建刷新缓存任务。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateRefreshTasks
        :type request: :class:`huaweicloudsdkcdn.v1.CreateRefreshTasksRequest`
        :rtype: :class:`huaweicloudsdkcdn.v1.CreateRefreshTasksResponse`
        """
        warnings.warn("Method 'create_refresh_tasks_async' of CdnAsyncClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._create_refresh_tasks_http_info(request)
        return self._call_api(**http_info)

    def create_refresh_tasks_async_invoker(self, request):
        warnings.warn("Method 'create_refresh_tasks_async_invoker' of CdnAsyncClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._create_refresh_tasks_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_refresh_tasks_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/cdn/content/refresh-tasks",
            "request_type": request.__class__.__name__,
            "response_type": "CreateRefreshTasksResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

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

    def create_tags_async(self, request):
        r"""创建资源标签配置接口

        用于创建资源标签。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateTags
        :type request: :class:`huaweicloudsdkcdn.v1.CreateTagsRequest`
        :rtype: :class:`huaweicloudsdkcdn.v1.CreateTagsResponse`
        """
        warnings.warn("Method 'create_tags_async' of CdnAsyncClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._create_tags_http_info(request)
        return self._call_api(**http_info)

    def create_tags_async_invoker(self, request):
        warnings.warn("Method 'create_tags_async_invoker' of CdnAsyncClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._create_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_tags_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/cdn/configuration/tags",
            "request_type": request.__class__.__name__,
            "response_type": "CreateTagsResponse"
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

        response_headers = ["X-Request-Id", ]

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
        r"""删除加速域名

        删除加速域名。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteDomain
        :type request: :class:`huaweicloudsdkcdn.v1.DeleteDomainRequest`
        :rtype: :class:`huaweicloudsdkcdn.v1.DeleteDomainResponse`
        """
        warnings.warn("Method 'delete_domain_async' of CdnAsyncClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._delete_domain_http_info(request)
        return self._call_api(**http_info)

    def delete_domain_async_invoker(self, request):
        warnings.warn("Method 'delete_domain_async_invoker' of CdnAsyncClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._delete_domain_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_domain_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1.0/cdn/domains/{domain_id}",
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

        response_headers = ["X-Request-Id", ]

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

    def disable_domain_async(self, request):
        r"""停用加速域名

        停用加速域名。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DisableDomain
        :type request: :class:`huaweicloudsdkcdn.v1.DisableDomainRequest`
        :rtype: :class:`huaweicloudsdkcdn.v1.DisableDomainResponse`
        """
        warnings.warn("Method 'disable_domain_async' of CdnAsyncClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._disable_domain_http_info(request)
        return self._call_api(**http_info)

    def disable_domain_async_invoker(self, request):
        warnings.warn("Method 'disable_domain_async_invoker' of CdnAsyncClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._disable_domain_http_info(request)
        return AsyncInvoker(self, http_info)

    def _disable_domain_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1.0/cdn/domains/{domain_id}/disable",
            "request_type": request.__class__.__name__,
            "response_type": "DisableDomainResponse"
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

        response_headers = ["X-Request-Id", ]

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

    def enable_domain_async(self, request):
        r"""启用加速域名

        启用加速域名。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for EnableDomain
        :type request: :class:`huaweicloudsdkcdn.v1.EnableDomainRequest`
        :rtype: :class:`huaweicloudsdkcdn.v1.EnableDomainResponse`
        """
        warnings.warn("Method 'enable_domain_async' of CdnAsyncClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._enable_domain_http_info(request)
        return self._call_api(**http_info)

    def enable_domain_async_invoker(self, request):
        warnings.warn("Method 'enable_domain_async_invoker' of CdnAsyncClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._enable_domain_http_info(request)
        return AsyncInvoker(self, http_info)

    def _enable_domain_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1.0/cdn/domains/{domain_id}/enable",
            "request_type": request.__class__.__name__,
            "response_type": "EnableDomainResponse"
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

        response_headers = ["X-Request-Id", ]

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

    def list_domains_async(self, request):
        r"""查询加速域名

        查询加速域名信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListDomains
        :type request: :class:`huaweicloudsdkcdn.v1.ListDomainsRequest`
        :rtype: :class:`huaweicloudsdkcdn.v1.ListDomainsResponse`
        """
        warnings.warn("Method 'list_domains_async' of CdnAsyncClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._list_domains_http_info(request)
        return self._call_api(**http_info)

    def list_domains_async_invoker(self, request):
        warnings.warn("Method 'list_domains_async_invoker' of CdnAsyncClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._list_domains_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_domains_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0/cdn/domains",
            "request_type": request.__class__.__name__,
            "response_type": "ListDomainsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'domain_name' in local_var_params:
            query_params.append(('domain_name', local_var_params['domain_name']))
        if 'business_type' in local_var_params:
            query_params.append(('business_type', local_var_params['business_type']))
        if 'domain_status' in local_var_params:
            query_params.append(('domain_status', local_var_params['domain_status']))
        if 'service_area' in local_var_params:
            query_params.append(('service_area', local_var_params['service_area']))
        if 'page_size' in local_var_params:
            query_params.append(('page_size', local_var_params['page_size']))
        if 'page_number' in local_var_params:
            query_params.append(('page_number', local_var_params['page_number']))
        if 'show_tags' in local_var_params:
            query_params.append(('show_tags', local_var_params['show_tags']))
        if 'exact_match' in local_var_params:
            query_params.append(('exact_match', local_var_params['exact_match']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

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

    def show_black_white_list_async(self, request):
        r"""查询IP黑白名单

        查询域名已经设置的IP黑白名单。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowBlackWhiteList
        :type request: :class:`huaweicloudsdkcdn.v1.ShowBlackWhiteListRequest`
        :rtype: :class:`huaweicloudsdkcdn.v1.ShowBlackWhiteListResponse`
        """
        warnings.warn("Method 'show_black_white_list_async' of CdnAsyncClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._show_black_white_list_http_info(request)
        return self._call_api(**http_info)

    def show_black_white_list_async_invoker(self, request):
        warnings.warn("Method 'show_black_white_list_async_invoker' of CdnAsyncClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._show_black_white_list_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_black_white_list_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0/cdn/domains/{domain_id}/ip-acl",
            "request_type": request.__class__.__name__,
            "response_type": "ShowBlackWhiteListResponse"
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

        response_headers = ["X-Request-Id", ]

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

    def show_cache_rules_async(self, request):
        r"""查询缓存规则

        查询缓存规则。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowCacheRules
        :type request: :class:`huaweicloudsdkcdn.v1.ShowCacheRulesRequest`
        :rtype: :class:`huaweicloudsdkcdn.v1.ShowCacheRulesResponse`
        """
        warnings.warn("Method 'show_cache_rules_async' of CdnAsyncClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._show_cache_rules_http_info(request)
        return self._call_api(**http_info)

    def show_cache_rules_async_invoker(self, request):
        warnings.warn("Method 'show_cache_rules_async_invoker' of CdnAsyncClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._show_cache_rules_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_cache_rules_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0/cdn/domains/{domain_id}/cache",
            "request_type": request.__class__.__name__,
            "response_type": "ShowCacheRulesResponse"
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

        response_headers = ["X-Request-Id", ]

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

    def show_certificates_https_info_async(self, request):
        r"""查询所有绑定HTTPS证书的域名信息

        查询所有绑定HTTPS证书的域名信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowCertificatesHttpsInfo
        :type request: :class:`huaweicloudsdkcdn.v1.ShowCertificatesHttpsInfoRequest`
        :rtype: :class:`huaweicloudsdkcdn.v1.ShowCertificatesHttpsInfoResponse`
        """
        warnings.warn("Method 'show_certificates_https_info_async' of CdnAsyncClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._show_certificates_https_info_http_info(request)
        return self._call_api(**http_info)

    def show_certificates_https_info_async_invoker(self, request):
        warnings.warn("Method 'show_certificates_https_info_async_invoker' of CdnAsyncClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._show_certificates_https_info_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_certificates_https_info_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0/cdn/domains/https-certificate-info",
            "request_type": request.__class__.__name__,
            "response_type": "ShowCertificatesHttpsInfoResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'page_size' in local_var_params:
            query_params.append(('page_size', local_var_params['page_size']))
        if 'page_number' in local_var_params:
            query_params.append(('page_number', local_var_params['page_number']))
        if 'domain_name' in local_var_params:
            query_params.append(('domain_name', local_var_params['domain_name']))
        if 'user_domain_id' in local_var_params:
            query_params.append(('user_domain_id', local_var_params['user_domain_id']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

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
        r"""查询加速域名详情

        查询加速域名详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowDomainDetail
        :type request: :class:`huaweicloudsdkcdn.v1.ShowDomainDetailRequest`
        :rtype: :class:`huaweicloudsdkcdn.v1.ShowDomainDetailResponse`
        """
        warnings.warn("Method 'show_domain_detail_async' of CdnAsyncClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._show_domain_detail_http_info(request)
        return self._call_api(**http_info)

    def show_domain_detail_async_invoker(self, request):
        warnings.warn("Method 'show_domain_detail_async_invoker' of CdnAsyncClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._show_domain_detail_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_domain_detail_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0/cdn/domains/{domain_id}/detail",
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
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

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

    def show_domain_full_config_async(self, request):
        r"""查询域名配置接口

        查询域名配置接口，
        支持查询回源请求头、HTTP header配置、URL鉴权、证书、源站、回源协议、强制重定向、智能压缩、IPv6开关、状态码缓存时间、Range回源、User-Agent黑白名单、改写回源URL、自定义错误页面、缓存规则、IP黑白名单、防盗链、强制跳转。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowDomainFullConfig
        :type request: :class:`huaweicloudsdkcdn.v1.ShowDomainFullConfigRequest`
        :rtype: :class:`huaweicloudsdkcdn.v1.ShowDomainFullConfigResponse`
        """
        warnings.warn("Method 'show_domain_full_config_async' of CdnAsyncClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._show_domain_full_config_http_info(request)
        return self._call_api(**http_info)

    def show_domain_full_config_async_invoker(self, request):
        warnings.warn("Method 'show_domain_full_config_async_invoker' of CdnAsyncClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._show_domain_full_config_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_domain_full_config_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.1/cdn/configuration/domains/{domain_name}/configs",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDomainFullConfigResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_name' in local_var_params:
            path_params['domain_name'] = local_var_params['domain_name']

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

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

    def show_domain_item_details_async(self, request):
        r"""批量查询域名的统计明细-按域名单独返回

        - 支持查询90天内的数据。
        - 查询跨度不能超过7天。
        - 最多同时指定100个域名。
        - 起始时间和结束时间，左闭右开，需要同时指定。
        - 开始时间、结束时间必须传毫秒级时间戳，且必须为5分钟整时刻点，如：0分、5分、10分、15分等，如果传的不是5分钟时刻点，返回数据可能与预期不一致。
        - 统一用开始时间表示一个时间段，如：2019-01-24 20:15:00 表示取 [20:15:00, 20:20:00)的统计数据，且左闭右开。
        - 流量类指标单位统一为Byte（字节）、带宽类指标单位统一为bit/s（比特/秒）、请求数类指标单位统一为次数。用于查询指定域名、指定统计指标的明细数据。
        - 如果传的是多个域名，则每个域名的数据分开返回。
        - 支持同时查询多个指标，不超过10个。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowDomainItemDetails
        :type request: :class:`huaweicloudsdkcdn.v1.ShowDomainItemDetailsRequest`
        :rtype: :class:`huaweicloudsdkcdn.v1.ShowDomainItemDetailsResponse`
        """
        warnings.warn("Method 'show_domain_item_details_async' of CdnAsyncClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._show_domain_item_details_http_info(request)
        return self._call_api(**http_info)

    def show_domain_item_details_async_invoker(self, request):
        warnings.warn("Method 'show_domain_item_details_async_invoker' of CdnAsyncClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._show_domain_item_details_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_domain_item_details_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0/cdn/statistics/domain-item-details",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDomainItemDetailsResponse"
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
        if 'domain_name' in local_var_params:
            query_params.append(('domain_name', local_var_params['domain_name']))
        if 'service_area' in local_var_params:
            query_params.append(('service_area', local_var_params['service_area']))
        if 'stat_type' in local_var_params:
            query_params.append(('stat_type', local_var_params['stat_type']))

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

    def show_domain_item_location_details_async(self, request):
        r"""批量查询域名的区域、运营商统计明细-按域名单独返回

        - 支持查询90天内的数据。
        - 查询跨度是7天。
        - 最多同时指定100个域名。
        - 起始时间和结束时间，左闭右开，需要同时指定。
        - 开始时间、结束时间必须传毫秒级时间戳，且必须为5分钟整时刻点，如：0分、5分、10分、15分等，如果传的不是5分钟时刻点，返回数据可能与预期不一致。
        - 统一用开始时间表示一个时间段，如：2019-01-24 20:15:00 表示取 [20:15:00, 20:20:00)的统计数据，且左闭右开。
        - 流量类指标单位统一为Byte（字节）、带宽类指标单位统一为bit/s（比特/秒）、请求数类指标单位统一为次数。
        - 用于查询指定域名、指定统计指标的明细数据。
        - 如果传的是多个域名，则每个域名的数据分开返回。
        - 支持按区域、运营商维度查询统计数据, 回源指标除外。
        - 支持同时查询多个指标，不超过10个。
        - 域名为海外加速场景不适用。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowDomainItemLocationDetails
        :type request: :class:`huaweicloudsdkcdn.v1.ShowDomainItemLocationDetailsRequest`
        :rtype: :class:`huaweicloudsdkcdn.v1.ShowDomainItemLocationDetailsResponse`
        """
        warnings.warn("Method 'show_domain_item_location_details_async' of CdnAsyncClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._show_domain_item_location_details_http_info(request)
        return self._call_api(**http_info)

    def show_domain_item_location_details_async_invoker(self, request):
        warnings.warn("Method 'show_domain_item_location_details_async_invoker' of CdnAsyncClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._show_domain_item_location_details_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_domain_item_location_details_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0/cdn/statistics/domain-item-location-details",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDomainItemLocationDetailsResponse"
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
        if 'domain_name' in local_var_params:
            query_params.append(('domain_name', local_var_params['domain_name']))
        if 'stat_type' in local_var_params:
            query_params.append(('stat_type', local_var_params['stat_type']))
        if 'region' in local_var_params:
            query_params.append(('region', local_var_params['region']))
        if 'isp' in local_var_params:
            query_params.append(('isp', local_var_params['isp']))

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

    def show_domain_location_stats_async(self, request):
        r"""按区域运营商查询域名统计数据

        - 支持查询90天内的数据。
        
        - 支持多指标同时查询，不超过5个。
        
        - 最多同时指定20个域名。
        
        - 起始时间和结束时间需要同时指定，左闭右开，毫秒级时间戳，且时间点必须为与查询时间间隔参数匹配的整时刻点。比如查询时间间隔为5分钟时，起始时间和结束时间必须为5分钟整时刻点，如：0分、5分、10分、15分等，如果时间点与时间间隔不匹配，返回数据可能与预期不一致。统一用开始时间表示一个时间段，如：2019-01-24 20:15:00 表示取 [20:15:00, 20:20:00)的统计数据，且左闭右开。
        
        - action取值：location_detail,location_summary
        
        - 流量类指标单位统一为Byte（字节）、带宽类指标单位统一为bit/s（比特/秒）、请求数类和状态码类指标单位统一为次数。用于查询指定域名、指定统计指标的区域运营商明细数据。
        
        - 单租户调用频率：15次/s。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowDomainLocationStats
        :type request: :class:`huaweicloudsdkcdn.v1.ShowDomainLocationStatsRequest`
        :rtype: :class:`huaweicloudsdkcdn.v1.ShowDomainLocationStatsResponse`
        """
        warnings.warn("Method 'show_domain_location_stats_async' of CdnAsyncClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._show_domain_location_stats_http_info(request)
        return self._call_api(**http_info)

    def show_domain_location_stats_async_invoker(self, request):
        warnings.warn("Method 'show_domain_location_stats_async_invoker' of CdnAsyncClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._show_domain_location_stats_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_domain_location_stats_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0/cdn/statistics/domain-location-stats",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDomainLocationStatsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'action' in local_var_params:
            query_params.append(('action', local_var_params['action']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'interval' in local_var_params:
            query_params.append(('interval', local_var_params['interval']))
        if 'domain_name' in local_var_params:
            query_params.append(('domain_name', local_var_params['domain_name']))
        if 'stat_type' in local_var_params:
            query_params.append(('stat_type', local_var_params['stat_type']))
        if 'group_by' in local_var_params:
            query_params.append(('group_by', local_var_params['group_by']))
        if 'country' in local_var_params:
            query_params.append(('country', local_var_params['country']))
        if 'province' in local_var_params:
            query_params.append(('province', local_var_params['province']))
        if 'isp' in local_var_params:
            query_params.append(('isp', local_var_params['isp']))
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

    def show_domain_stats_async(self, request):
        r"""查询域名统计数据

        - 支持查询90天内的数据。
        
        - 支持多指标同时查询，不超过5个。
        
        - 最多同时指定20个域名。
        
        - 起始时间和结束时间需要同时指定，左闭右开，毫秒级时间戳，且时间点必须为与查询时间间隔参数匹配的整时刻点。比如查询时间间隔为5分钟时，起始时间和结束时间必须为5分钟整时刻点，如：0分、5分、10分、15分等，如果时间点与时间间隔不匹配，返回数据可能与预期不一致。统一用开始时间表示一个时间段，如：2019-01-24 20:15:00 表示取 [20:15:00, 20:20:00)的统计数据，且左闭右开。
        
        - action取值：detail,summary
        
        - 流量类指标单位统一为Byte（字节）、带宽类指标单位统一为bit/s（比特/秒）、请求数类和状态码类指标单位统一为次数。用于查询指定域名、指定统计指标的明细数据。
        
        - 单租户调用频率：15次/s。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowDomainStats
        :type request: :class:`huaweicloudsdkcdn.v1.ShowDomainStatsRequest`
        :rtype: :class:`huaweicloudsdkcdn.v1.ShowDomainStatsResponse`
        """
        warnings.warn("Method 'show_domain_stats_async' of CdnAsyncClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._show_domain_stats_http_info(request)
        return self._call_api(**http_info)

    def show_domain_stats_async_invoker(self, request):
        warnings.warn("Method 'show_domain_stats_async_invoker' of CdnAsyncClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._show_domain_stats_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_domain_stats_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0/cdn/statistics/domain-stats",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDomainStatsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'action' in local_var_params:
            query_params.append(('action', local_var_params['action']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'domain_name' in local_var_params:
            query_params.append(('domain_name', local_var_params['domain_name']))
        if 'stat_type' in local_var_params:
            query_params.append(('stat_type', local_var_params['stat_type']))
        if 'interval' in local_var_params:
            query_params.append(('interval', local_var_params['interval']))
        if 'group_by' in local_var_params:
            query_params.append(('group_by', local_var_params['group_by']))
        if 'service_area' in local_var_params:
            query_params.append(('service_area', local_var_params['service_area']))
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

    def show_history_task_details_async(self, request):
        r"""查询刷新预热任务详情

        查询刷新预热任务详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowHistoryTaskDetails
        :type request: :class:`huaweicloudsdkcdn.v1.ShowHistoryTaskDetailsRequest`
        :rtype: :class:`huaweicloudsdkcdn.v1.ShowHistoryTaskDetailsResponse`
        """
        warnings.warn("Method 'show_history_task_details_async' of CdnAsyncClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._show_history_task_details_http_info(request)
        return self._call_api(**http_info)

    def show_history_task_details_async_invoker(self, request):
        warnings.warn("Method 'show_history_task_details_async_invoker' of CdnAsyncClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._show_history_task_details_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_history_task_details_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0/cdn/historytasks/{history_tasks_id}/detail",
            "request_type": request.__class__.__name__,
            "response_type": "ShowHistoryTaskDetailsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'history_tasks_id' in local_var_params:
            path_params['history_tasks_id'] = local_var_params['history_tasks_id']

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'page_size' in local_var_params:
            query_params.append(('page_size', local_var_params['page_size']))
        if 'page_number' in local_var_params:
            query_params.append(('page_number', local_var_params['page_number']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'url' in local_var_params:
            query_params.append(('url', local_var_params['url']))
        if 'create_time' in local_var_params:
            query_params.append(('create_time', local_var_params['create_time']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

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

    def show_history_tasks_async(self, request):
        r"""查询刷新预热任务

        查询刷新预热任务。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowHistoryTasks
        :type request: :class:`huaweicloudsdkcdn.v1.ShowHistoryTasksRequest`
        :rtype: :class:`huaweicloudsdkcdn.v1.ShowHistoryTasksResponse`
        """
        warnings.warn("Method 'show_history_tasks_async' of CdnAsyncClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._show_history_tasks_http_info(request)
        return self._call_api(**http_info)

    def show_history_tasks_async_invoker(self, request):
        warnings.warn("Method 'show_history_tasks_async_invoker' of CdnAsyncClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._show_history_tasks_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_history_tasks_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0/cdn/historytasks",
            "request_type": request.__class__.__name__,
            "response_type": "ShowHistoryTasksResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'page_size' in local_var_params:
            query_params.append(('page_size', local_var_params['page_size']))
        if 'page_number' in local_var_params:
            query_params.append(('page_number', local_var_params['page_number']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'start_date' in local_var_params:
            query_params.append(('start_date', local_var_params['start_date']))
        if 'end_date' in local_var_params:
            query_params.append(('end_date', local_var_params['end_date']))
        if 'order_field' in local_var_params:
            query_params.append(('order_field', local_var_params['order_field']))
        if 'order_type' in local_var_params:
            query_params.append(('order_type', local_var_params['order_type']))
        if 'file_type' in local_var_params:
            query_params.append(('file_type', local_var_params['file_type']))
        if 'task_type' in local_var_params:
            query_params.append(('task_type', local_var_params['task_type']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

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

    def show_http_info_async(self, request):
        r"""查询HTTPS配置

        获取加速域名证书。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowHttpInfo
        :type request: :class:`huaweicloudsdkcdn.v1.ShowHttpInfoRequest`
        :rtype: :class:`huaweicloudsdkcdn.v1.ShowHttpInfoResponse`
        """
        warnings.warn("Method 'show_http_info_async' of CdnAsyncClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._show_http_info_http_info(request)
        return self._call_api(**http_info)

    def show_http_info_async_invoker(self, request):
        warnings.warn("Method 'show_http_info_async_invoker' of CdnAsyncClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._show_http_info_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_http_info_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0/cdn/domains/{domain_id}/https-info",
            "request_type": request.__class__.__name__,
            "response_type": "ShowHttpInfoResponse"
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

        response_headers = ["X-Request-Id", ]

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

    def show_ip_info_async(self, request):
        r"""查询IP归属信息

        查询IP归属信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowIpInfo
        :type request: :class:`huaweicloudsdkcdn.v1.ShowIpInfoRequest`
        :rtype: :class:`huaweicloudsdkcdn.v1.ShowIpInfoResponse`
        """
        warnings.warn("Method 'show_ip_info_async' of CdnAsyncClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._show_ip_info_http_info(request)
        return self._call_api(**http_info)

    def show_ip_info_async_invoker(self, request):
        warnings.warn("Method 'show_ip_info_async_invoker' of CdnAsyncClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._show_ip_info_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_ip_info_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0/cdn/ip-info",
            "request_type": request.__class__.__name__,
            "response_type": "ShowIpInfoResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'ips' in local_var_params:
            query_params.append(('ips', local_var_params['ips']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

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

    def show_logs_async(self, request):
        r"""日志查询

        查询日志下载链接，支持查询30天内的日志信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowLogs
        :type request: :class:`huaweicloudsdkcdn.v1.ShowLogsRequest`
        :rtype: :class:`huaweicloudsdkcdn.v1.ShowLogsResponse`
        """
        http_info = self._show_logs_http_info(request)
        return self._call_api(**http_info)

    def show_logs_async_invoker(self, request):
        http_info = self._show_logs_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_logs_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0/cdn/logs",
            "request_type": request.__class__.__name__,
            "response_type": "ShowLogsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'domain_name' in local_var_params:
            query_params.append(('domain_name', local_var_params['domain_name']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'page_size' in local_var_params:
            query_params.append(('page_size', local_var_params['page_size']))
        if 'page_number' in local_var_params:
            query_params.append(('page_number', local_var_params['page_number']))
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

    def show_origin_host_async(self, request):
        r"""查询回源HOST

        查询回源HOST。回源HOST是CDN节点在回源过程中，在源站访问的站点域名，即http请求头中的host信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowOriginHost
        :type request: :class:`huaweicloudsdkcdn.v1.ShowOriginHostRequest`
        :rtype: :class:`huaweicloudsdkcdn.v1.ShowOriginHostResponse`
        """
        warnings.warn("Method 'show_origin_host_async' of CdnAsyncClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._show_origin_host_http_info(request)
        return self._call_api(**http_info)

    def show_origin_host_async_invoker(self, request):
        warnings.warn("Method 'show_origin_host_async_invoker' of CdnAsyncClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._show_origin_host_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_origin_host_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0/cdn/domains/{domain_id}/originhost",
            "request_type": request.__class__.__name__,
            "response_type": "ShowOriginHostResponse"
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

        response_headers = ["X-Request-Id", ]

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

    def show_quota_async(self, request):
        r"""查询用户配额

        查询当前用户域名、刷新文件、刷新目录和预热的配额
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowQuota
        :type request: :class:`huaweicloudsdkcdn.v1.ShowQuotaRequest`
        :rtype: :class:`huaweicloudsdkcdn.v1.ShowQuotaResponse`
        """
        warnings.warn("Method 'show_quota_async' of CdnAsyncClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._show_quota_http_info(request)
        return self._call_api(**http_info)

    def show_quota_async_invoker(self, request):
        warnings.warn("Method 'show_quota_async_invoker' of CdnAsyncClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._show_quota_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_quota_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0/cdn/quota",
            "request_type": request.__class__.__name__,
            "response_type": "ShowQuotaResponse"
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

    def show_refer_async(self, request):
        r"""查询Referer过滤规则

        查询Referer过滤规则。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowRefer
        :type request: :class:`huaweicloudsdkcdn.v1.ShowReferRequest`
        :rtype: :class:`huaweicloudsdkcdn.v1.ShowReferResponse`
        """
        warnings.warn("Method 'show_refer_async' of CdnAsyncClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._show_refer_http_info(request)
        return self._call_api(**http_info)

    def show_refer_async_invoker(self, request):
        warnings.warn("Method 'show_refer_async_invoker' of CdnAsyncClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._show_refer_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_refer_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0/cdn/domains/{domain_id}/referer",
            "request_type": request.__class__.__name__,
            "response_type": "ShowReferResponse"
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

        response_headers = ["X-Request-Id", ]

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

    def show_response_header_async(self, request):
        r"""查询响应头配置

        列举header所有配置。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowResponseHeader
        :type request: :class:`huaweicloudsdkcdn.v1.ShowResponseHeaderRequest`
        :rtype: :class:`huaweicloudsdkcdn.v1.ShowResponseHeaderResponse`
        """
        warnings.warn("Method 'show_response_header_async' of CdnAsyncClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._show_response_header_http_info(request)
        return self._call_api(**http_info)

    def show_response_header_async_invoker(self, request):
        warnings.warn("Method 'show_response_header_async_invoker' of CdnAsyncClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._show_response_header_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_response_header_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0/cdn/domains/{domain_id}/response-header",
            "request_type": request.__class__.__name__,
            "response_type": "ShowResponseHeaderResponse"
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

        response_headers = ["X-Request-Id", ]

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

    def show_tags_async(self, request):
        r"""查询资源标签列表配置接口

        用于查询资源标签列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowTags
        :type request: :class:`huaweicloudsdkcdn.v1.ShowTagsRequest`
        :rtype: :class:`huaweicloudsdkcdn.v1.ShowTagsResponse`
        """
        warnings.warn("Method 'show_tags_async' of CdnAsyncClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._show_tags_http_info(request)
        return self._call_api(**http_info)

    def show_tags_async_invoker(self, request):
        warnings.warn("Method 'show_tags_async_invoker' of CdnAsyncClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._show_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_tags_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0/cdn/configuration/tags",
            "request_type": request.__class__.__name__,
            "response_type": "ShowTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'resource_id' in local_var_params:
            query_params.append(('resource_id', local_var_params['resource_id']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

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

    def show_top_url_async(self, request):
        r"""查询TOP100 URL明细

        - 查询TOP100 URL明细。
        
        - 支持查询90天内的数据。
        
        - 查询跨度不能超过31天。
        
        - 起始时间和结束时间，左闭右开，需要同时指定。如查询2021-10-24 00:00:00 到 2021-10-25 00:00:00
        的数据，表示取 [2021-10-24 00:00:00, 2021-10-25 00:00:00)的统计数据。
        
        - 开始时间、结束时间必须传毫秒级时间戳，且必须为凌晨0点整时刻点，如果传的不是凌晨0点整时刻点，返回数据可能与预期不一致。
        
        - 流量类指标单位统一为Byte（字节）、请求数类指标单位统一为次数。用于查询指定域名、指定统计指标的明细数据。
        
        - 单租户调用频率：5次/s。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowTopUrl
        :type request: :class:`huaweicloudsdkcdn.v1.ShowTopUrlRequest`
        :rtype: :class:`huaweicloudsdkcdn.v1.ShowTopUrlResponse`
        """
        warnings.warn("Method 'show_top_url_async' of CdnAsyncClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._show_top_url_http_info(request)
        return self._call_api(**http_info)

    def show_top_url_async_invoker(self, request):
        warnings.warn("Method 'show_top_url_async_invoker' of CdnAsyncClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._show_top_url_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_top_url_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0/cdn/statistics/top-url",
            "request_type": request.__class__.__name__,
            "response_type": "ShowTopUrlResponse"
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
        if 'domain_name' in local_var_params:
            query_params.append(('domain_name', local_var_params['domain_name']))
        if 'service_area' in local_var_params:
            query_params.append(('service_area', local_var_params['service_area']))
        if 'stat_type' in local_var_params:
            query_params.append(('stat_type', local_var_params['stat_type']))

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

    def show_url_task_info_async(self, request):
        r"""查询刷新预热URL记录

        查询刷新预热URL记录。如需此接口，请提交工单开通。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowUrlTaskInfo
        :type request: :class:`huaweicloudsdkcdn.v1.ShowUrlTaskInfoRequest`
        :rtype: :class:`huaweicloudsdkcdn.v1.ShowUrlTaskInfoResponse`
        """
        warnings.warn("Method 'show_url_task_info_async' of CdnAsyncClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._show_url_task_info_http_info(request)
        return self._call_api(**http_info)

    def show_url_task_info_async_invoker(self, request):
        warnings.warn("Method 'show_url_task_info_async_invoker' of CdnAsyncClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._show_url_task_info_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_url_task_info_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0/cdn/contentgateway/url-tasks",
            "request_type": request.__class__.__name__,
            "response_type": "ShowUrlTaskInfoResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'url' in local_var_params:
            query_params.append(('url', local_var_params['url']))
        if 'task_type' in local_var_params:
            query_params.append(('task_type', local_var_params['task_type']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'file_type' in local_var_params:
            query_params.append(('file_type', local_var_params['file_type']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def update_black_white_list_async(self, request):
        r"""设置IP黑白名单

        设置域名的IP黑白名单。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateBlackWhiteList
        :type request: :class:`huaweicloudsdkcdn.v1.UpdateBlackWhiteListRequest`
        :rtype: :class:`huaweicloudsdkcdn.v1.UpdateBlackWhiteListResponse`
        """
        warnings.warn("Method 'update_black_white_list_async' of CdnAsyncClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._update_black_white_list_http_info(request)
        return self._call_api(**http_info)

    def update_black_white_list_async_invoker(self, request):
        warnings.warn("Method 'update_black_white_list_async_invoker' of CdnAsyncClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._update_black_white_list_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_black_white_list_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1.0/cdn/domains/{domain_id}/ip-acl",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateBlackWhiteListResponse"
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
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

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

    def update_cache_rules_async(self, request):
        r"""设置缓存规则

        设置CDN节点上缓存资源的缓存策略。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateCacheRules
        :type request: :class:`huaweicloudsdkcdn.v1.UpdateCacheRulesRequest`
        :rtype: :class:`huaweicloudsdkcdn.v1.UpdateCacheRulesResponse`
        """
        warnings.warn("Method 'update_cache_rules_async' of CdnAsyncClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._update_cache_rules_http_info(request)
        return self._call_api(**http_info)

    def update_cache_rules_async_invoker(self, request):
        warnings.warn("Method 'update_cache_rules_async_invoker' of CdnAsyncClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._update_cache_rules_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_cache_rules_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1.0/cdn/domains/{domain_id}/cache",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateCacheRulesResponse"
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
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

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

    def update_domain_full_config_async(self, request):
        r"""修改域名全量配置接口

        修改域名配置接口，
        支持修改回源请求头、HTTP header配置、URL鉴权、证书、源站、回源协议、强制重定向、智能压缩、IPv6开关、状态码缓存时间、Range回源、User-Agent黑白名单、改写回源URL、自定义错误页面、缓存规则、IP黑白名单、防盗链、强制跳转。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateDomainFullConfig
        :type request: :class:`huaweicloudsdkcdn.v1.UpdateDomainFullConfigRequest`
        :rtype: :class:`huaweicloudsdkcdn.v1.UpdateDomainFullConfigResponse`
        """
        warnings.warn("Method 'update_domain_full_config_async' of CdnAsyncClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._update_domain_full_config_http_info(request)
        return self._call_api(**http_info)

    def update_domain_full_config_async_invoker(self, request):
        warnings.warn("Method 'update_domain_full_config_async_invoker' of CdnAsyncClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._update_domain_full_config_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_domain_full_config_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1.1/cdn/configuration/domains/{domain_name}/configs",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateDomainFullConfigResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_name' in local_var_params:
            path_params['domain_name'] = local_var_params['domain_name']

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

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

    def update_domain_multi_certificates_async(self, request):
        r"""一个证书批量设置多个域名

        一个证书配置多个域名，设置域名强制https回源参数。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateDomainMultiCertificates
        :type request: :class:`huaweicloudsdkcdn.v1.UpdateDomainMultiCertificatesRequest`
        :rtype: :class:`huaweicloudsdkcdn.v1.UpdateDomainMultiCertificatesResponse`
        """
        warnings.warn("Method 'update_domain_multi_certificates_async' of CdnAsyncClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._update_domain_multi_certificates_http_info(request)
        return self._call_api(**http_info)

    def update_domain_multi_certificates_async_invoker(self, request):
        warnings.warn("Method 'update_domain_multi_certificates_async_invoker' of CdnAsyncClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._update_domain_multi_certificates_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_domain_multi_certificates_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1.0/cdn/domains/config-https-info",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateDomainMultiCertificatesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

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

    def update_domain_origin_async(self, request):
        r"""修改源站信息。

        修改加速域名的源站配置。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateDomainOrigin
        :type request: :class:`huaweicloudsdkcdn.v1.UpdateDomainOriginRequest`
        :rtype: :class:`huaweicloudsdkcdn.v1.UpdateDomainOriginResponse`
        """
        warnings.warn("Method 'update_domain_origin_async' of CdnAsyncClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._update_domain_origin_http_info(request)
        return self._call_api(**http_info)

    def update_domain_origin_async_invoker(self, request):
        warnings.warn("Method 'update_domain_origin_async_invoker' of CdnAsyncClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._update_domain_origin_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_domain_origin_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1.0/cdn/domains/{domain_id}/origin",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateDomainOriginResponse"
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
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

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

    def update_follow302_switch_async(self, request):
        r"""开启/关闭回源跟随

        开启此项配置后，当CDN节点回源请求源站返回301/302状态码时，CDN节点会先跳转到301/302对应地址获取资源并缓存后再返回给用户。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateFollow302Switch
        :type request: :class:`huaweicloudsdkcdn.v1.UpdateFollow302SwitchRequest`
        :rtype: :class:`huaweicloudsdkcdn.v1.UpdateFollow302SwitchResponse`
        """
        warnings.warn("Method 'update_follow302_switch_async' of CdnAsyncClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._update_follow302_switch_http_info(request)
        return self._call_api(**http_info)

    def update_follow302_switch_async_invoker(self, request):
        warnings.warn("Method 'update_follow302_switch_async_invoker' of CdnAsyncClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._update_follow302_switch_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_follow302_switch_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1.0/cdn/domains/{domain_id}/follow302-switch",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateFollow302SwitchResponse"
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
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

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

    def update_https_info_async(self, request):
        r"""配置HTTPS

        设置加速域名HTTPS。通过配置加速域名的HTTPS证书，并将其部署在全网CDN节点，实现HTTPS安全加速。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateHttpsInfo
        :type request: :class:`huaweicloudsdkcdn.v1.UpdateHttpsInfoRequest`
        :rtype: :class:`huaweicloudsdkcdn.v1.UpdateHttpsInfoResponse`
        """
        warnings.warn("Method 'update_https_info_async' of CdnAsyncClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._update_https_info_http_info(request)
        return self._call_api(**http_info)

    def update_https_info_async_invoker(self, request):
        warnings.warn("Method 'update_https_info_async_invoker' of CdnAsyncClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._update_https_info_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_https_info_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1.0/cdn/domains/{domain_id}/https-info",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateHttpsInfoResponse"
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
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

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

    def update_origin_host_async(self, request):
        r"""修改回源HOST。

        修改回源HOST。回源HOST是CDN节点在回源过程中，在源站访问的站点域名，即http请求头中的host信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateOriginHost
        :type request: :class:`huaweicloudsdkcdn.v1.UpdateOriginHostRequest`
        :rtype: :class:`huaweicloudsdkcdn.v1.UpdateOriginHostResponse`
        """
        warnings.warn("Method 'update_origin_host_async' of CdnAsyncClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._update_origin_host_http_info(request)
        return self._call_api(**http_info)

    def update_origin_host_async_invoker(self, request):
        warnings.warn("Method 'update_origin_host_async_invoker' of CdnAsyncClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._update_origin_host_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_origin_host_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1.0/cdn/domains/{domain_id}/originhost",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateOriginHostResponse"
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
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

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

    def update_private_bucket_access_async(self, request):
        r"""修改私有桶开启关闭状态

        修改私有桶开启关闭状态。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdatePrivateBucketAccess
        :type request: :class:`huaweicloudsdkcdn.v1.UpdatePrivateBucketAccessRequest`
        :rtype: :class:`huaweicloudsdkcdn.v1.UpdatePrivateBucketAccessResponse`
        """
        warnings.warn("Method 'update_private_bucket_access_async' of CdnAsyncClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._update_private_bucket_access_http_info(request)
        return self._call_api(**http_info)

    def update_private_bucket_access_async_invoker(self, request):
        warnings.warn("Method 'update_private_bucket_access_async_invoker' of CdnAsyncClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._update_private_bucket_access_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_private_bucket_access_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1.0/cdn/domains/{domain_id}/private-bucket-access",
            "request_type": request.__class__.__name__,
            "response_type": "UpdatePrivateBucketAccessResponse"
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
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

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

    def update_range_switch_async(self, request):
        r"""开启/关闭Range回源

        Range回源是指源站在收到CDN节点回源请求时，根据http请求头中的Range信息返回指定范围的数据给CDN节点。
        
        开启Range回源前需要确认源站是否支持Range请求，若源站不支持Range请求，开启Range回源将导致资源无法缓存。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateRangeSwitch
        :type request: :class:`huaweicloudsdkcdn.v1.UpdateRangeSwitchRequest`
        :rtype: :class:`huaweicloudsdkcdn.v1.UpdateRangeSwitchResponse`
        """
        warnings.warn("Method 'update_range_switch_async' of CdnAsyncClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._update_range_switch_http_info(request)
        return self._call_api(**http_info)

    def update_range_switch_async_invoker(self, request):
        warnings.warn("Method 'update_range_switch_async_invoker' of CdnAsyncClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._update_range_switch_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_range_switch_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1.0/cdn/domains/{domain_id}/range-switch",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateRangeSwitchResponse"
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
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

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

    def update_refer_async(self, request):
        r"""设置Referer过滤规则

        设置Referer过滤规则。通过设置过滤策略，对访问者身份进行识别和过滤，实现限制访问来源的目的。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateRefer
        :type request: :class:`huaweicloudsdkcdn.v1.UpdateReferRequest`
        :rtype: :class:`huaweicloudsdkcdn.v1.UpdateReferResponse`
        """
        warnings.warn("Method 'update_refer_async' of CdnAsyncClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._update_refer_http_info(request)
        return self._call_api(**http_info)

    def update_refer_async_invoker(self, request):
        warnings.warn("Method 'update_refer_async_invoker' of CdnAsyncClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._update_refer_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_refer_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1.0/cdn/domains/{domain_id}/referer",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateReferResponse"
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
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

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

    def update_response_header_async(self, request):
        r"""新增/修改响应头配置

        新增/修改域名响应头配置。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateResponseHeader
        :type request: :class:`huaweicloudsdkcdn.v1.UpdateResponseHeaderRequest`
        :rtype: :class:`huaweicloudsdkcdn.v1.UpdateResponseHeaderResponse`
        """
        warnings.warn("Method 'update_response_header_async' of CdnAsyncClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._update_response_header_http_info(request)
        return self._call_api(**http_info)

    def update_response_header_async_invoker(self, request):
        warnings.warn("Method 'update_response_header_async_invoker' of CdnAsyncClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._update_response_header_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_response_header_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1.0/cdn/domains/{domain_id}/response-header",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateResponseHeaderResponse"
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
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

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

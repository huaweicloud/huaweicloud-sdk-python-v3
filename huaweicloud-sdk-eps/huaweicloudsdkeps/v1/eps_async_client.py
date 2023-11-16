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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkeps'")


class EpsAsyncClient(Client):
    def __init__(self):
        super(EpsAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkeps.v1.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls, "GlobalCredentials")
        else:
            if clazz.__name__ != "EpsAsyncClient":
                raise TypeError("client type error, support client type is EpsAsyncClient")
            client_builder = ClientBuilder(clazz, "GlobalCredentials")

        

        return client_builder

    def create_enterprise_project_async(self, request):
        """创建企业项目

        创建企业项目。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateEnterpriseProject
        :type request: :class:`huaweicloudsdkeps.v1.CreateEnterpriseProjectRequest`
        :rtype: :class:`huaweicloudsdkeps.v1.CreateEnterpriseProjectResponse`
        """
        http_info = self._create_enterprise_project_http_info(request)
        return self._call_api(**http_info)

    def create_enterprise_project_async_invoker(self, request):
        http_info = self._create_enterprise_project_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_enterprise_project_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/enterprise-projects",
            "request_type": request.__class__.__name__,
            "response_type": "CreateEnterpriseProjectResponse"
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
            ['application/json;charset=UTF-8'])

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

    def disable_enterprise_project_async(self, request):
        """停用企业项目

        停用企业项目。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DisableEnterpriseProject
        :type request: :class:`huaweicloudsdkeps.v1.DisableEnterpriseProjectRequest`
        :rtype: :class:`huaweicloudsdkeps.v1.DisableEnterpriseProjectResponse`
        """
        http_info = self._disable_enterprise_project_http_info(request)
        return self._call_api(**http_info)

    def disable_enterprise_project_async_invoker(self, request):
        http_info = self._disable_enterprise_project_http_info(request)
        return AsyncInvoker(self, http_info)

    def _disable_enterprise_project_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/enterprise-projects/{enterprise_project_id}/action",
            "request_type": request.__class__.__name__,
            "response_type": "DisableEnterpriseProjectResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'enterprise_project_id' in local_var_params:
            path_params['enterprise_project_id'] = local_var_params['enterprise_project_id']

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
            ['application/json;charset=UTF-8'])

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

    def enable_enterprise_project_async(self, request):
        """启用企业项目

        启用企业项目。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for EnableEnterpriseProject
        :type request: :class:`huaweicloudsdkeps.v1.EnableEnterpriseProjectRequest`
        :rtype: :class:`huaweicloudsdkeps.v1.EnableEnterpriseProjectResponse`
        """
        http_info = self._enable_enterprise_project_http_info(request)
        return self._call_api(**http_info)

    def enable_enterprise_project_async_invoker(self, request):
        http_info = self._enable_enterprise_project_http_info(request)
        return AsyncInvoker(self, http_info)

    def _enable_enterprise_project_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/enterprise-projects/{enterprise_project_id}/action",
            "request_type": request.__class__.__name__,
            "response_type": "EnableEnterpriseProjectResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'enterprise_project_id' in local_var_params:
            path_params['enterprise_project_id'] = local_var_params['enterprise_project_id']

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
            ['application/json;charset=UTF-8'])

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

    def list_api_versions_async(self, request):
        """查询API版本列表

        查询企业项目的API版本列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListApiVersions
        :type request: :class:`huaweicloudsdkeps.v1.ListApiVersionsRequest`
        :rtype: :class:`huaweicloudsdkeps.v1.ListApiVersionsResponse`
        """
        http_info = self._list_api_versions_http_info(request)
        return self._call_api(**http_info)

    def list_api_versions_async_invoker(self, request):
        http_info = self._list_api_versions_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_api_versions_http_info(self, request):
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

    def list_enterprise_project_async(self, request):
        """查询企业项目列表

        查询当前用户已授权的企业项目列表，用户可以使用企业项目绑定资源。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListEnterpriseProject
        :type request: :class:`huaweicloudsdkeps.v1.ListEnterpriseProjectRequest`
        :rtype: :class:`huaweicloudsdkeps.v1.ListEnterpriseProjectResponse`
        """
        http_info = self._list_enterprise_project_http_info(request)
        return self._call_api(**http_info)

    def list_enterprise_project_async_invoker(self, request):
        http_info = self._list_enterprise_project_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_enterprise_project_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0/enterprise-projects",
            "request_type": request.__class__.__name__,
            "response_type": "ListEnterpriseProjectResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
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

    def list_providers_async(self, request):
        """查询企业项目支持的服务

        查询企业项目支持的服务
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListProviders
        :type request: :class:`huaweicloudsdkeps.v1.ListProvidersRequest`
        :rtype: :class:`huaweicloudsdkeps.v1.ListProvidersResponse`
        """
        http_info = self._list_providers_http_info(request)
        return self._call_api(**http_info)

    def list_providers_async_invoker(self, request):
        http_info = self._list_providers_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_providers_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0/enterprise-projects/providers",
            "request_type": request.__class__.__name__,
            "response_type": "ListProvidersResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'locale' in local_var_params:
            query_params.append(('locale', local_var_params['locale']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'provider' in local_var_params:
            query_params.append(('provider', local_var_params['provider']))

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

    def migrate_resource_async(self, request):
        """迁移资源

        迁移资源到目标企业项目。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for MigrateResource
        :type request: :class:`huaweicloudsdkeps.v1.MigrateResourceRequest`
        :rtype: :class:`huaweicloudsdkeps.v1.MigrateResourceResponse`
        """
        http_info = self._migrate_resource_http_info(request)
        return self._call_api(**http_info)

    def migrate_resource_async_invoker(self, request):
        http_info = self._migrate_resource_http_info(request)
        return AsyncInvoker(self, http_info)

    def _migrate_resource_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/enterprise-projects/{enterprise_project_id}/resources-migrate",
            "request_type": request.__class__.__name__,
            "response_type": "MigrateResourceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'enterprise_project_id' in local_var_params:
            path_params['enterprise_project_id'] = local_var_params['enterprise_project_id']

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
            ['application/json;charset=UTF-8'])

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

    def show_api_version_async(self, request):
        """查询API版本号详情

        查询指定的企业项目API版本号详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowApiVersion
        :type request: :class:`huaweicloudsdkeps.v1.ShowApiVersionRequest`
        :rtype: :class:`huaweicloudsdkeps.v1.ShowApiVersionResponse`
        """
        http_info = self._show_api_version_http_info(request)
        return self._call_api(**http_info)

    def show_api_version_async_invoker(self, request):
        http_info = self._show_api_version_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_api_version_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/{api_version}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowApiVersionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'api_version' in local_var_params:
            path_params['api_version'] = local_var_params['api_version']

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

    def show_enterprise_project_async(self, request):
        """查询企业项目详情

        查询企业项目详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowEnterpriseProject
        :type request: :class:`huaweicloudsdkeps.v1.ShowEnterpriseProjectRequest`
        :rtype: :class:`huaweicloudsdkeps.v1.ShowEnterpriseProjectResponse`
        """
        http_info = self._show_enterprise_project_http_info(request)
        return self._call_api(**http_info)

    def show_enterprise_project_async_invoker(self, request):
        http_info = self._show_enterprise_project_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_enterprise_project_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0/enterprise-projects/{enterprise_project_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowEnterpriseProjectResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'enterprise_project_id' in local_var_params:
            path_params['enterprise_project_id'] = local_var_params['enterprise_project_id']

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

    def show_enterprise_project_quota_async(self, request):
        """查询企业项目配额

        查询企业项目的配额信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowEnterpriseProjectQuota
        :type request: :class:`huaweicloudsdkeps.v1.ShowEnterpriseProjectQuotaRequest`
        :rtype: :class:`huaweicloudsdkeps.v1.ShowEnterpriseProjectQuotaResponse`
        """
        http_info = self._show_enterprise_project_quota_http_info(request)
        return self._call_api(**http_info)

    def show_enterprise_project_quota_async_invoker(self, request):
        http_info = self._show_enterprise_project_quota_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_enterprise_project_quota_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0/enterprise-projects/quotas",
            "request_type": request.__class__.__name__,
            "response_type": "ShowEnterpriseProjectQuotaResponse"
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

    def show_resource_bind_enterprise_project_async(self, request):
        """查询企业项目绑定的资源列表

        查询企业项目下绑定的资源详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowResourceBindEnterpriseProject
        :type request: :class:`huaweicloudsdkeps.v1.ShowResourceBindEnterpriseProjectRequest`
        :rtype: :class:`huaweicloudsdkeps.v1.ShowResourceBindEnterpriseProjectResponse`
        """
        http_info = self._show_resource_bind_enterprise_project_http_info(request)
        return self._call_api(**http_info)

    def show_resource_bind_enterprise_project_async_invoker(self, request):
        http_info = self._show_resource_bind_enterprise_project_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_resource_bind_enterprise_project_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/enterprise-projects/{enterprise_project_id}/resources/filter",
            "request_type": request.__class__.__name__,
            "response_type": "ShowResourceBindEnterpriseProjectResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'enterprise_project_id' in local_var_params:
            path_params['enterprise_project_id'] = local_var_params['enterprise_project_id']

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
            ['application/json;charset=UTF-8'])

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

    def update_enterprise_project_async(self, request):
        """修改企业项目

        修改企业项目。当前仅支持修改名称和描述。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateEnterpriseProject
        :type request: :class:`huaweicloudsdkeps.v1.UpdateEnterpriseProjectRequest`
        :rtype: :class:`huaweicloudsdkeps.v1.UpdateEnterpriseProjectResponse`
        """
        http_info = self._update_enterprise_project_http_info(request)
        return self._call_api(**http_info)

    def update_enterprise_project_async_invoker(self, request):
        http_info = self._update_enterprise_project_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_enterprise_project_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1.0/enterprise-projects/{enterprise_project_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateEnterpriseProjectResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'enterprise_project_id' in local_var_params:
            path_params['enterprise_project_id'] = local_var_params['enterprise_project_id']

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
            ['application/json;charset=UTF-8'])

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

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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdktms'")


class TmsAsyncClient(Client):
    def __init__(self):
        super(TmsAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdktms.v1.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls, "GlobalCredentials")
        else:
            if clazz.__name__ != "TmsAsyncClient":
                raise TypeError("client type error, support client type is TmsAsyncClient")
            client_builder = ClientBuilder(clazz, "GlobalCredentials")

        

        return client_builder

    def create_predefine_tags_async(self, request):
        """创建预定义标签

        用于创建预定标签。用户创建预定义标签后，可以使用预定义标签来给资源创建标签。该接口支持幂等特性和处理批量数据。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreatePredefineTags
        :type request: :class:`huaweicloudsdktms.v1.CreatePredefineTagsRequest`
        :rtype: :class:`huaweicloudsdktms.v1.CreatePredefineTagsResponse`
        """
        http_info = self._create_predefine_tags_http_info(request)
        return self._call_api(**http_info)

    def create_predefine_tags_async_invoker(self, request):
        http_info = self._create_predefine_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_predefine_tags_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/predefine_tags/action",
            "request_type": request.__class__.__name__,
            "response_type": "CreatePredefineTagsResponse"
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

    def create_resource_tag_async(self, request):
        """批量添加标签

        用于给云服务的多个资源添加标签，每个资源最多可添加10个标签，每次最多支持批量操作20个资源。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateResourceTag
        :type request: :class:`huaweicloudsdktms.v1.CreateResourceTagRequest`
        :rtype: :class:`huaweicloudsdktms.v1.CreateResourceTagResponse`
        """
        http_info = self._create_resource_tag_http_info(request)
        return self._call_api(**http_info)

    def create_resource_tag_async_invoker(self, request):
        http_info = self._create_resource_tag_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_resource_tag_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/resource-tags/batch-create",
            "request_type": request.__class__.__name__,
            "response_type": "CreateResourceTagResponse"
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

    def delete_predefine_tags_async(self, request):
        """删除预定义标签

        用于删除预定标签。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeletePredefineTags
        :type request: :class:`huaweicloudsdktms.v1.DeletePredefineTagsRequest`
        :rtype: :class:`huaweicloudsdktms.v1.DeletePredefineTagsResponse`
        """
        http_info = self._delete_predefine_tags_http_info(request)
        return self._call_api(**http_info)

    def delete_predefine_tags_async_invoker(self, request):
        http_info = self._delete_predefine_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_predefine_tags_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/predefine_tags/action",
            "request_type": request.__class__.__name__,
            "response_type": "DeletePredefineTagsResponse"
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

    def delete_resource_tag_async(self, request):
        """批量移除标签

        用于批量移除云服务多个资源的标签，每个资源最多支持移除10个标签，每次最多支持批量操作20个资源。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteResourceTag
        :type request: :class:`huaweicloudsdktms.v1.DeleteResourceTagRequest`
        :rtype: :class:`huaweicloudsdktms.v1.DeleteResourceTagResponse`
        """
        http_info = self._delete_resource_tag_http_info(request)
        return self._call_api(**http_info)

    def delete_resource_tag_async_invoker(self, request):
        http_info = self._delete_resource_tag_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_resource_tag_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/resource-tags/batch-delete",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteResourceTagResponse"
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

    def list_api_versions_async(self, request):
        """查询API版本列表

        查询标签管理服务的API版本列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListApiVersions
        :type request: :class:`huaweicloudsdktms.v1.ListApiVersionsRequest`
        :rtype: :class:`huaweicloudsdktms.v1.ListApiVersionsResponse`
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

    def list_predefine_tags_async(self, request):
        """查询预定义标签列表

        用于查询预定义标签列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListPredefineTags
        :type request: :class:`huaweicloudsdktms.v1.ListPredefineTagsRequest`
        :rtype: :class:`huaweicloudsdktms.v1.ListPredefineTagsResponse`
        """
        http_info = self._list_predefine_tags_http_info(request)
        return self._call_api(**http_info)

    def list_predefine_tags_async_invoker(self, request):
        http_info = self._list_predefine_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_predefine_tags_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0/predefine_tags",
            "request_type": request.__class__.__name__,
            "response_type": "ListPredefineTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'key' in local_var_params:
            query_params.append(('key', local_var_params['key']))
        if 'value' in local_var_params:
            query_params.append(('value', local_var_params['value']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'order_field' in local_var_params:
            query_params.append(('order_field', local_var_params['order_field']))
        if 'order_method' in local_var_params:
            query_params.append(('order_method', local_var_params['order_method']))

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
        """查询标签管理支持的服务

        查询标签管理支持的服务。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListProviders
        :type request: :class:`huaweicloudsdktms.v1.ListProvidersRequest`
        :rtype: :class:`huaweicloudsdktms.v1.ListProvidersResponse`
        """
        http_info = self._list_providers_http_info(request)
        return self._call_api(**http_info)

    def list_providers_async_invoker(self, request):
        http_info = self._list_providers_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_providers_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0/tms/providers",
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

    def list_resource_async(self, request):
        """根据标签过滤资源

        根据标签过滤资源。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListResource
        :type request: :class:`huaweicloudsdktms.v1.ListResourceRequest`
        :rtype: :class:`huaweicloudsdktms.v1.ListResourceResponse`
        """
        http_info = self._list_resource_http_info(request)
        return self._call_api(**http_info)

    def list_resource_async_invoker(self, request):
        http_info = self._list_resource_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_resource_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/resource-instances/filter",
            "request_type": request.__class__.__name__,
            "response_type": "ListResourceResponse"
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

    def list_tag_keys_async(self, request):
        """查询标签键列表

        查询指定区域的所有标签键.
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListTagKeys
        :type request: :class:`huaweicloudsdktms.v1.ListTagKeysRequest`
        :rtype: :class:`huaweicloudsdktms.v1.ListTagKeysResponse`
        """
        http_info = self._list_tag_keys_http_info(request)
        return self._call_api(**http_info)

    def list_tag_keys_async_invoker(self, request):
        http_info = self._list_tag_keys_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_tag_keys_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0/tag-keys",
            "request_type": request.__class__.__name__,
            "response_type": "ListTagKeysResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'region_id' in local_var_params:
            query_params.append(('region_id', local_var_params['region_id']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))

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

    def list_tag_values_async(self, request):
        """查询标签值列表

        查询指定区域的标签键下的所有标签值。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListTagValues
        :type request: :class:`huaweicloudsdktms.v1.ListTagValuesRequest`
        :rtype: :class:`huaweicloudsdktms.v1.ListTagValuesResponse`
        """
        http_info = self._list_tag_values_http_info(request)
        return self._call_api(**http_info)

    def list_tag_values_async_invoker(self, request):
        http_info = self._list_tag_values_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_tag_values_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0/tag-values",
            "request_type": request.__class__.__name__,
            "response_type": "ListTagValuesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'region_id' in local_var_params:
            query_params.append(('region_id', local_var_params['region_id']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'key' in local_var_params:
            query_params.append(('key', local_var_params['key']))

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

    def show_api_version_async(self, request):
        """查询API版本号详情

        查询指定的标签管理服务API版本号详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowApiVersion
        :type request: :class:`huaweicloudsdktms.v1.ShowApiVersionRequest`
        :rtype: :class:`huaweicloudsdktms.v1.ShowApiVersionResponse`
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

    def show_resource_tag_async(self, request):
        """查询资源标签

        查询单个资源上的标签。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowResourceTag
        :type request: :class:`huaweicloudsdktms.v1.ShowResourceTagRequest`
        :rtype: :class:`huaweicloudsdktms.v1.ShowResourceTagResponse`
        """
        http_info = self._show_resource_tag_http_info(request)
        return self._call_api(**http_info)

    def show_resource_tag_async_invoker(self, request):
        http_info = self._show_resource_tag_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_resource_tag_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2.0/resources/{resource_id}/tags",
            "request_type": request.__class__.__name__,
            "response_type": "ShowResourceTagResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_id' in local_var_params:
            path_params['resource_id'] = local_var_params['resource_id']

        query_params = []
        if 'project_id' in local_var_params:
            query_params.append(('project_id', local_var_params['project_id']))
        if 'resource_type' in local_var_params:
            query_params.append(('resource_type', local_var_params['resource_type']))

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

    def show_tag_quota_async(self, request):
        """查询标签配额

        查询标签的配额信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowTagQuota
        :type request: :class:`huaweicloudsdktms.v1.ShowTagQuotaRequest`
        :rtype: :class:`huaweicloudsdktms.v1.ShowTagQuotaResponse`
        """
        http_info = self._show_tag_quota_http_info(request)
        return self._call_api(**http_info)

    def show_tag_quota_async_invoker(self, request):
        http_info = self._show_tag_quota_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_tag_quota_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0/tms/quotas",
            "request_type": request.__class__.__name__,
            "response_type": "ShowTagQuotaResponse"
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

    def update_predefine_tags_async(self, request):
        """修改预定义标签

        修改预定义标签。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdatePredefineTags
        :type request: :class:`huaweicloudsdktms.v1.UpdatePredefineTagsRequest`
        :rtype: :class:`huaweicloudsdktms.v1.UpdatePredefineTagsResponse`
        """
        http_info = self._update_predefine_tags_http_info(request)
        return self._call_api(**http_info)

    def update_predefine_tags_async_invoker(self, request):
        http_info = self._update_predefine_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_predefine_tags_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1.0/predefine_tags",
            "request_type": request.__class__.__name__,
            "response_type": "UpdatePredefineTagsResponse"
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

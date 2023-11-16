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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkcloudpond'")


class CloudPondAsyncClient(Client):
    def __init__(self):
        super(CloudPondAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkcloudpond.v1.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls, "GlobalCredentials")
        else:
            if clazz.__name__ != "CloudPondAsyncClient":
                raise TypeError("client type error, support client type is CloudPondAsyncClient")
            client_builder = ClientBuilder(clazz, "GlobalCredentials")

        

        return client_builder

    def create_edge_site_async(self, request):
        """创建边缘小站

        创建边缘小站。
        - 一个边缘小站关联一个华为云指定的区域。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateEdgeSite
        :type request: :class:`huaweicloudsdkcloudpond.v1.CreateEdgeSiteRequest`
        :rtype: :class:`huaweicloudsdkcloudpond.v1.CreateEdgeSiteResponse`
        """
        http_info = self._create_edge_site_http_info(request)
        return self._call_api(**http_info)

    def create_edge_site_async_invoker(self, request):
        http_info = self._create_edge_site_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_edge_site_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{domain_id}/edge-sites",
            "request_type": request.__class__.__name__,
            "response_type": "CreateEdgeSiteResponse"
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

    def delete_edge_site_async(self, request):
        """删除边缘小站

        删除指定的边缘小站。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteEdgeSite
        :type request: :class:`huaweicloudsdkcloudpond.v1.DeleteEdgeSiteRequest`
        :rtype: :class:`huaweicloudsdkcloudpond.v1.DeleteEdgeSiteResponse`
        """
        http_info = self._delete_edge_site_http_info(request)
        return self._call_api(**http_info)

    def delete_edge_site_async_invoker(self, request):
        http_info = self._delete_edge_site_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_edge_site_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{domain_id}/edge-sites/{site_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteEdgeSiteResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'site_id' in local_var_params:
            path_params['site_id'] = local_var_params['site_id']

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

    def list_edge_sites_async(self, request):
        """查询边缘小站列表

        查询边缘小站列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListEdgeSites
        :type request: :class:`huaweicloudsdkcloudpond.v1.ListEdgeSitesRequest`
        :rtype: :class:`huaweicloudsdkcloudpond.v1.ListEdgeSitesResponse`
        """
        http_info = self._list_edge_sites_http_info(request)
        return self._call_api(**http_info)

    def list_edge_sites_async_invoker(self, request):
        http_info = self._list_edge_sites_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_edge_sites_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{domain_id}/edge-sites",
            "request_type": request.__class__.__name__,
            "response_type": "ListEdgeSitesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
            collection_formats['sort_key'] = 'multi'
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
            collection_formats['sort_dir'] = 'multi'
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
            collection_formats['id'] = 'multi'
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
            collection_formats['name'] = 'multi'
        if 'availability_zone_id' in local_var_params:
            query_params.append(('availability_zone_id', local_var_params['availability_zone_id']))
            collection_formats['availability_zone_id'] = 'multi'
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
            collection_formats['status'] = 'multi'

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

    def show_edge_site_async(self, request):
        """查询边缘小站详情

        查询边缘小站详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowEdgeSite
        :type request: :class:`huaweicloudsdkcloudpond.v1.ShowEdgeSiteRequest`
        :rtype: :class:`huaweicloudsdkcloudpond.v1.ShowEdgeSiteResponse`
        """
        http_info = self._show_edge_site_http_info(request)
        return self._call_api(**http_info)

    def show_edge_site_async_invoker(self, request):
        http_info = self._show_edge_site_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_edge_site_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{domain_id}/edge-sites/{site_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowEdgeSiteResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'site_id' in local_var_params:
            path_params['site_id'] = local_var_params['site_id']

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

    def update_edge_site_async(self, request):
        """更新边缘小站

        更新边缘小站。
        - 允许更新边缘小站描述或场地信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateEdgeSite
        :type request: :class:`huaweicloudsdkcloudpond.v1.UpdateEdgeSiteRequest`
        :rtype: :class:`huaweicloudsdkcloudpond.v1.UpdateEdgeSiteResponse`
        """
        http_info = self._update_edge_site_http_info(request)
        return self._call_api(**http_info)

    def update_edge_site_async_invoker(self, request):
        http_info = self._update_edge_site_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_edge_site_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{domain_id}/edge-sites/{site_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateEdgeSiteResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'site_id' in local_var_params:
            path_params['site_id'] = local_var_params['site_id']

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

    def list_edge_site_metrics_async(self, request):
        """查看站点容量信息

        查看站点容量信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListEdgeSiteMetrics
        :type request: :class:`huaweicloudsdkcloudpond.v1.ListEdgeSiteMetricsRequest`
        :rtype: :class:`huaweicloudsdkcloudpond.v1.ListEdgeSiteMetricsResponse`
        """
        http_info = self._list_edge_site_metrics_http_info(request)
        return self._call_api(**http_info)

    def list_edge_site_metrics_async_invoker(self, request):
        http_info = self._list_edge_site_metrics_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_edge_site_metrics_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{domain_id}/edge-sites/{site_id}/metric-data",
            "request_type": request.__class__.__name__,
            "response_type": "ListEdgeSiteMetricsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'site_id' in local_var_params:
            path_params['site_id'] = local_var_params['site_id']

        query_params = []
        if 'dim' in local_var_params:
            query_params.append(('dim', local_var_params['dim']))

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

    def list_quotas_async(self, request):
        """查询配额

        查询租户资源配额。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListQuotas
        :type request: :class:`huaweicloudsdkcloudpond.v1.ListQuotasRequest`
        :rtype: :class:`huaweicloudsdkcloudpond.v1.ListQuotasResponse`
        """
        http_info = self._list_quotas_http_info(request)
        return self._call_api(**http_info)

    def list_quotas_async_invoker(self, request):
        http_info = self._list_quotas_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_quotas_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{domain_id}/quotas",
            "request_type": request.__class__.__name__,
            "response_type": "ListQuotasResponse"
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

    def list_racks_async(self, request):
        """查询机柜列表

        查询机柜列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListRacks
        :type request: :class:`huaweicloudsdkcloudpond.v1.ListRacksRequest`
        :rtype: :class:`huaweicloudsdkcloudpond.v1.ListRacksResponse`
        """
        http_info = self._list_racks_http_info(request)
        return self._call_api(**http_info)

    def list_racks_async_invoker(self, request):
        http_info = self._list_racks_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_racks_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{domain_id}/racks",
            "request_type": request.__class__.__name__,
            "response_type": "ListRacksResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
            collection_formats['sort_key'] = 'multi'
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
            collection_formats['sort_dir'] = 'multi'
        if 'edge_site_id' in local_var_params:
            query_params.append(('edge_site_id', local_var_params['edge_site_id']))

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

    def show_rack_async(self, request):
        """查询机柜详情

        查询机柜详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowRack
        :type request: :class:`huaweicloudsdkcloudpond.v1.ShowRackRequest`
        :rtype: :class:`huaweicloudsdkcloudpond.v1.ShowRackResponse`
        """
        http_info = self._show_rack_http_info(request)
        return self._call_api(**http_info)

    def show_rack_async_invoker(self, request):
        http_info = self._show_rack_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_rack_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{domain_id}/racks/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowRackResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

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

    def list_supported_regions_async(self, request):
        """查询支持的区域列表

        查询支持智能边缘小站接入的华为云区域（region）列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListSupportedRegions
        :type request: :class:`huaweicloudsdkcloudpond.v1.ListSupportedRegionsRequest`
        :rtype: :class:`huaweicloudsdkcloudpond.v1.ListSupportedRegionsResponse`
        """
        http_info = self._list_supported_regions_http_info(request)
        return self._call_api(**http_info)

    def list_supported_regions_async_invoker(self, request):
        http_info = self._list_supported_regions_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_supported_regions_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{domain_id}/regions",
            "request_type": request.__class__.__name__,
            "response_type": "ListSupportedRegionsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
            collection_formats['sort_key'] = 'multi'
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
            collection_formats['sort_dir'] = 'multi'

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def list_storage_pools_async(self, request):
        """查询存储池列表

        查询存储池列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListStoragePools
        :type request: :class:`huaweicloudsdkcloudpond.v1.ListStoragePoolsRequest`
        :rtype: :class:`huaweicloudsdkcloudpond.v1.ListStoragePoolsResponse`
        """
        http_info = self._list_storage_pools_http_info(request)
        return self._call_api(**http_info)

    def list_storage_pools_async_invoker(self, request):
        http_info = self._list_storage_pools_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_storage_pools_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{domain_id}/storage-pools",
            "request_type": request.__class__.__name__,
            "response_type": "ListStoragePoolsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
            collection_formats['sort_key'] = 'multi'
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
            collection_formats['sort_dir'] = 'multi'
        if 'edge_site_id' in local_var_params:
            query_params.append(('edge_site_id', local_var_params['edge_site_id']))

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

    def show_storage_pool_async(self, request):
        """查询存储池详情

        查询存储池详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowStoragePool
        :type request: :class:`huaweicloudsdkcloudpond.v1.ShowStoragePoolRequest`
        :rtype: :class:`huaweicloudsdkcloudpond.v1.ShowStoragePoolResponse`
        """
        http_info = self._show_storage_pool_http_info(request)
        return self._call_api(**http_info)

    def show_storage_pool_async_invoker(self, request):
        http_info = self._show_storage_pool_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_storage_pool_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{domain_id}/storage-pools/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowStoragePoolResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

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

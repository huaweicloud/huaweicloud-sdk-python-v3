# coding: utf-8

from __future__ import absolute_import

import importlib

from huaweicloudsdkcore.client import Client, ClientBuilder
from huaweicloudsdkcore.utils import http_utils
from huaweicloudsdkcore.sdk_stream_request import SdkStreamRequest


class CloudPondClient(Client):
    def __init__(self):
        super(CloudPondClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkcloudpond.v1.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if clazz is None:
            return ClientBuilder(cls, "GlobalCredentials")

        if clazz.__name__ != "CloudPondClient":
            raise TypeError("client type error, support client type is CloudPondClient")

        return ClientBuilder(clazz, "GlobalCredentials")

    def create_edge_site(self, request):
        """创建边缘小站

        创建边缘小站。
        - 一个边缘小站关联一个华为云指定的区域。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateEdgeSite
        :type request: :class:`huaweicloudsdkcloudpond.v1.CreateEdgeSiteRequest`
        :rtype: :class:`huaweicloudsdkcloudpond.v1.CreateEdgeSiteResponse`
        """
        return self._create_edge_site_with_http_info(request)

    def _create_edge_site_with_http_info(self, request):
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
            resource_path='/v1/{domain_id}/edge-sites',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateEdgeSiteResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_edge_site(self, request):
        """删除边缘小站

        删除指定的边缘小站。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteEdgeSite
        :type request: :class:`huaweicloudsdkcloudpond.v1.DeleteEdgeSiteRequest`
        :rtype: :class:`huaweicloudsdkcloudpond.v1.DeleteEdgeSiteResponse`
        """
        return self._delete_edge_site_with_http_info(request)

    def _delete_edge_site_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'site_id' in local_var_params:
            path_params['site_id'] = local_var_params['site_id']

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
            resource_path='/v1/{domain_id}/edge-sites/{site_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteEdgeSiteResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_edge_sites(self, request):
        """查询边缘小站列表

        查询边缘小站列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListEdgeSites
        :type request: :class:`huaweicloudsdkcloudpond.v1.ListEdgeSitesRequest`
        :rtype: :class:`huaweicloudsdkcloudpond.v1.ListEdgeSitesResponse`
        """
        return self._list_edge_sites_with_http_info(request)

    def _list_edge_sites_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{domain_id}/edge-sites',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListEdgeSitesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_edge_site(self, request):
        """查询边缘小站详情

        查询边缘小站详情。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowEdgeSite
        :type request: :class:`huaweicloudsdkcloudpond.v1.ShowEdgeSiteRequest`
        :rtype: :class:`huaweicloudsdkcloudpond.v1.ShowEdgeSiteResponse`
        """
        return self._show_edge_site_with_http_info(request)

    def _show_edge_site_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'site_id' in local_var_params:
            path_params['site_id'] = local_var_params['site_id']

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
            resource_path='/v1/{domain_id}/edge-sites/{site_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowEdgeSiteResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_edge_site(self, request):
        """更新边缘小站

        更新边缘小站。
        - 允许更新边缘小站描述或场地信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateEdgeSite
        :type request: :class:`huaweicloudsdkcloudpond.v1.UpdateEdgeSiteRequest`
        :rtype: :class:`huaweicloudsdkcloudpond.v1.UpdateEdgeSiteResponse`
        """
        return self._update_edge_site_with_http_info(request)

    def _update_edge_site_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'site_id' in local_var_params:
            path_params['site_id'] = local_var_params['site_id']

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
            resource_path='/v1/{domain_id}/edge-sites/{site_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateEdgeSiteResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_edge_site_metrics(self, request):
        """查看站点容量信息

        查看站点容量信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListEdgeSiteMetrics
        :type request: :class:`huaweicloudsdkcloudpond.v1.ListEdgeSiteMetricsRequest`
        :rtype: :class:`huaweicloudsdkcloudpond.v1.ListEdgeSiteMetricsResponse`
        """
        return self._list_edge_site_metrics_with_http_info(request)

    def _list_edge_site_metrics_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{domain_id}/edge-sites/{site_id}/metric-data',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListEdgeSiteMetricsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_quotas(self, request):
        """查询配额

        查询租户资源配额。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListQuotas
        :type request: :class:`huaweicloudsdkcloudpond.v1.ListQuotasRequest`
        :rtype: :class:`huaweicloudsdkcloudpond.v1.ListQuotasResponse`
        """
        return self._list_quotas_with_http_info(request)

    def _list_quotas_with_http_info(self, request):
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
            resource_path='/v1/{domain_id}/quotas',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListQuotasResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_racks(self, request):
        """查询机柜列表

        查询机柜列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListRacks
        :type request: :class:`huaweicloudsdkcloudpond.v1.ListRacksRequest`
        :rtype: :class:`huaweicloudsdkcloudpond.v1.ListRacksResponse`
        """
        return self._list_racks_with_http_info(request)

    def _list_racks_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{domain_id}/racks',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListRacksResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_rack(self, request):
        """查询机柜详情

        查询机柜详情。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowRack
        :type request: :class:`huaweicloudsdkcloudpond.v1.ShowRackRequest`
        :rtype: :class:`huaweicloudsdkcloudpond.v1.ShowRackResponse`
        """
        return self._show_rack_with_http_info(request)

    def _show_rack_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

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
            resource_path='/v1/{domain_id}/racks/{id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowRackResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_supported_regions(self, request):
        """查询支持的区域列表

        查询支持智能边缘小站接入的华为云区域（region）列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListSupportedRegions
        :type request: :class:`huaweicloudsdkcloudpond.v1.ListSupportedRegionsRequest`
        :rtype: :class:`huaweicloudsdkcloudpond.v1.ListSupportedRegionsResponse`
        """
        return self._list_supported_regions_with_http_info(request)

    def _list_supported_regions_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{domain_id}/regions',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListSupportedRegionsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_storage_pools(self, request):
        """查询存储池列表

        查询存储池列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListStoragePools
        :type request: :class:`huaweicloudsdkcloudpond.v1.ListStoragePoolsRequest`
        :rtype: :class:`huaweicloudsdkcloudpond.v1.ListStoragePoolsResponse`
        """
        return self._list_storage_pools_with_http_info(request)

    def _list_storage_pools_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{domain_id}/storage-pools',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListStoragePoolsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_storage_pool(self, request):
        """查询存储池详情

        查询存储池详情。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowStoragePool
        :type request: :class:`huaweicloudsdkcloudpond.v1.ShowStoragePoolRequest`
        :rtype: :class:`huaweicloudsdkcloudpond.v1.ShowStoragePoolResponse`
        """
        return self._show_storage_pool_with_http_info(request)

    def _show_storage_pool_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

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
            resource_path='/v1/{domain_id}/storage-pools/{id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowStoragePoolResponse',
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

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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkgeip'")


class GeipClient(Client):
    def __init__(self):
        super(GeipClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkgeip.v3.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls, "GlobalCredentials")
        else:
            if clazz.__name__ != "GeipClient":
                raise TypeError("client type error, support client type is GeipClient")
            client_builder = ClientBuilder(clazz, "GlobalCredentials")

        

        return client_builder

    def add_internet_bandwidth_tags(self, request):
        """添加全域公网带宽标签

        添加全域公网带宽标签
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AddInternetBandwidthTags
        :type request: :class:`huaweicloudsdkgeip.v3.AddInternetBandwidthTagsRequest`
        :rtype: :class:`huaweicloudsdkgeip.v3.AddInternetBandwidthTagsResponse`
        """
        http_info = self._add_internet_bandwidth_tags_http_info(request)
        return self._call_api(**http_info)

    def add_internet_bandwidth_tags_invoker(self, request):
        http_info = self._add_internet_bandwidth_tags_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _add_internet_bandwidth_tags_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/internet-bandwidth/{resource_id}/tags",
            "request_type": request.__class__.__name__,
            "response_type": "AddInternetBandwidthTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
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

    def batch_create_internet_bandwidth(self, request):
        """批量创建全域公网带宽

        批量创建全域公网带宽
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchCreateInternetBandwidth
        :type request: :class:`huaweicloudsdkgeip.v3.BatchCreateInternetBandwidthRequest`
        :rtype: :class:`huaweicloudsdkgeip.v3.BatchCreateInternetBandwidthResponse`
        """
        http_info = self._batch_create_internet_bandwidth_http_info(request)
        return self._call_api(**http_info)

    def batch_create_internet_bandwidth_invoker(self, request):
        http_info = self._batch_create_internet_bandwidth_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_create_internet_bandwidth_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{domain_id}/geip/internet-bandwidths/batch-create",
            "request_type": request.__class__.__name__,
            "response_type": "BatchCreateInternetBandwidthResponse"
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

    def batch_create_internet_bandwidth_tags(self, request):
        """批量添加全域公网带宽标签

        批量添加全域公网带宽标签
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchCreateInternetBandwidthTags
        :type request: :class:`huaweicloudsdkgeip.v3.BatchCreateInternetBandwidthTagsRequest`
        :rtype: :class:`huaweicloudsdkgeip.v3.BatchCreateInternetBandwidthTagsResponse`
        """
        http_info = self._batch_create_internet_bandwidth_tags_http_info(request)
        return self._call_api(**http_info)

    def batch_create_internet_bandwidth_tags_invoker(self, request):
        http_info = self._batch_create_internet_bandwidth_tags_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_create_internet_bandwidth_tags_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/internet-bandwidth/{resource_id}/tags/create",
            "request_type": request.__class__.__name__,
            "response_type": "BatchCreateInternetBandwidthTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
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

    def batch_delete_internet_bandwidth_tags(self, request):
        """批量删除全域公网带宽标签

        批量删除全域公网带宽标签
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchDeleteInternetBandwidthTags
        :type request: :class:`huaweicloudsdkgeip.v3.BatchDeleteInternetBandwidthTagsRequest`
        :rtype: :class:`huaweicloudsdkgeip.v3.BatchDeleteInternetBandwidthTagsResponse`
        """
        http_info = self._batch_delete_internet_bandwidth_tags_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_internet_bandwidth_tags_invoker(self, request):
        http_info = self._batch_delete_internet_bandwidth_tags_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_delete_internet_bandwidth_tags_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/internet-bandwidth/{resource_id}/tags/delete",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeleteInternetBandwidthTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
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

    def count_internet_bandwidth(self, request):
        """查询全域公网带宽个数

        查询全域公网带宽个数
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CountInternetBandwidth
        :type request: :class:`huaweicloudsdkgeip.v3.CountInternetBandwidthRequest`
        :rtype: :class:`huaweicloudsdkgeip.v3.CountInternetBandwidthResponse`
        """
        http_info = self._count_internet_bandwidth_http_info(request)
        return self._call_api(**http_info)

    def count_internet_bandwidth_invoker(self, request):
        http_info = self._count_internet_bandwidth_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _count_internet_bandwidth_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{domain_id}/geip/internet-bandwidths/count",
            "request_type": request.__class__.__name__,
            "response_type": "CountInternetBandwidthResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
            collection_formats['id'] = 'multi'
        if 'size' in local_var_params:
            query_params.append(('size', local_var_params['size']))
            collection_formats['size'] = 'multi'
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
            collection_formats['name'] = 'multi'
        if 'name_like' in local_var_params:
            query_params.append(('name_like', local_var_params['name_like']))
        if 'access_site' in local_var_params:
            query_params.append(('access_site', local_var_params['access_site']))
            collection_formats['access_site'] = 'multi'
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
            collection_formats['status'] = 'multi'
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
            collection_formats['enterprise_project_id'] = 'multi'
        if 'tags' in local_var_params:
            query_params.append(('tags', local_var_params['tags']))
            collection_formats['tags'] = 'csv'

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

    def create_internet_bandwidth(self, request):
        """创建全域公网带宽

        创建全域公网带宽
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateInternetBandwidth
        :type request: :class:`huaweicloudsdkgeip.v3.CreateInternetBandwidthRequest`
        :rtype: :class:`huaweicloudsdkgeip.v3.CreateInternetBandwidthResponse`
        """
        http_info = self._create_internet_bandwidth_http_info(request)
        return self._call_api(**http_info)

    def create_internet_bandwidth_invoker(self, request):
        http_info = self._create_internet_bandwidth_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_internet_bandwidth_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{domain_id}/geip/internet-bandwidths",
            "request_type": request.__class__.__name__,
            "response_type": "CreateInternetBandwidthResponse"
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

    def create_user_disclaimer(self, request):
        """创建租户签署免责条款

        创建租户签署免责条款
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateUserDisclaimer
        :type request: :class:`huaweicloudsdkgeip.v3.CreateUserDisclaimerRequest`
        :rtype: :class:`huaweicloudsdkgeip.v3.CreateUserDisclaimerResponse`
        """
        http_info = self._create_user_disclaimer_http_info(request)
        return self._call_api(**http_info)

    def create_user_disclaimer_invoker(self, request):
        http_info = self._create_user_disclaimer_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_user_disclaimer_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{domain_id}/geip/user-disclaimer-records",
            "request_type": request.__class__.__name__,
            "response_type": "CreateUserDisclaimerResponse"
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

    def delete_internet_bandwidth(self, request):
        """删除全域公网带宽

        删除全域公网带宽
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteInternetBandwidth
        :type request: :class:`huaweicloudsdkgeip.v3.DeleteInternetBandwidthRequest`
        :rtype: :class:`huaweicloudsdkgeip.v3.DeleteInternetBandwidthResponse`
        """
        http_info = self._delete_internet_bandwidth_http_info(request)
        return self._call_api(**http_info)

    def delete_internet_bandwidth_invoker(self, request):
        http_info = self._delete_internet_bandwidth_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_internet_bandwidth_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{domain_id}/geip/internet-bandwidths/{internet_bandwidth_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteInternetBandwidthResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'internet_bandwidth_id' in local_var_params:
            path_params['internet_bandwidth_id'] = local_var_params['internet_bandwidth_id']

        query_params = []

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

    def delete_internet_bandwidth_tag(self, request):
        """删除全域公网带宽标签

        删除全域公网带宽标签
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteInternetBandwidthTag
        :type request: :class:`huaweicloudsdkgeip.v3.DeleteInternetBandwidthTagRequest`
        :rtype: :class:`huaweicloudsdkgeip.v3.DeleteInternetBandwidthTagResponse`
        """
        http_info = self._delete_internet_bandwidth_tag_http_info(request)
        return self._call_api(**http_info)

    def delete_internet_bandwidth_tag_invoker(self, request):
        http_info = self._delete_internet_bandwidth_tag_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_internet_bandwidth_tag_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/internet-bandwidth/{resource_id}/tags/{tag_key}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteInternetBandwidthTagResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_id' in local_var_params:
            path_params['resource_id'] = local_var_params['resource_id']
        if 'tag_key' in local_var_params:
            path_params['tag_key'] = local_var_params['tag_key']

        query_params = []

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

    def delete_user_disclaimer(self, request):
        """删除租户撤销免责条款

        删除租户撤销免责条款
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteUserDisclaimer
        :type request: :class:`huaweicloudsdkgeip.v3.DeleteUserDisclaimerRequest`
        :rtype: :class:`huaweicloudsdkgeip.v3.DeleteUserDisclaimerResponse`
        """
        http_info = self._delete_user_disclaimer_http_info(request)
        return self._call_api(**http_info)

    def delete_user_disclaimer_invoker(self, request):
        http_info = self._delete_user_disclaimer_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_user_disclaimer_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{domain_id}/geip/user-disclaimer-records",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteUserDisclaimerResponse"
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

    def list_access_sites(self, request):
        """查询接入点列表

        查询接入点列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAccessSites
        :type request: :class:`huaweicloudsdkgeip.v3.ListAccessSitesRequest`
        :rtype: :class:`huaweicloudsdkgeip.v3.ListAccessSitesResponse`
        """
        http_info = self._list_access_sites_http_info(request)
        return self._call_api(**http_info)

    def list_access_sites_invoker(self, request):
        http_info = self._list_access_sites_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_access_sites_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{domain_id}/geip/access-sites",
            "request_type": request.__class__.__name__,
            "response_type": "ListAccessSitesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'page_reverse' in local_var_params:
            query_params.append(('page_reverse', local_var_params['page_reverse']))
        if 'fields' in local_var_params:
            query_params.append(('fields', local_var_params['fields']))
            collection_formats['fields'] = 'multi'
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
        if 'proxy_region' in local_var_params:
            query_params.append(('proxy_region', local_var_params['proxy_region']))
            collection_formats['proxy_region'] = 'multi'
        if 'iec_az_code' in local_var_params:
            query_params.append(('iec_az_code', local_var_params['iec_az_code']))
            collection_formats['iec_az_code'] = 'multi'

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

    def list_geip_resource_quotas(self, request):
        """查询租户全域弹性公网IP配额

        查询租户全域弹性公网IP配额
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListGeipResourceQuotas
        :type request: :class:`huaweicloudsdkgeip.v3.ListGeipResourceQuotasRequest`
        :rtype: :class:`huaweicloudsdkgeip.v3.ListGeipResourceQuotasResponse`
        """
        http_info = self._list_geip_resource_quotas_http_info(request)
        return self._call_api(**http_info)

    def list_geip_resource_quotas_invoker(self, request):
        http_info = self._list_geip_resource_quotas_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_geip_resource_quotas_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{domain_id}/geip/quotas",
            "request_type": request.__class__.__name__,
            "response_type": "ListGeipResourceQuotasResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'page_reverse' in local_var_params:
            query_params.append(('page_reverse', local_var_params['page_reverse']))
        if 'fields' in local_var_params:
            query_params.append(('fields', local_var_params['fields']))
            collection_formats['fields'] = 'multi'
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
            collection_formats['type'] = 'multi'

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

    def list_internet_bandwidth_count_filter_tags(self, request):
        """查询资源实例列表数目

        查询资源实例列表数目
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListInternetBandwidthCountFilterTags
        :type request: :class:`huaweicloudsdkgeip.v3.ListInternetBandwidthCountFilterTagsRequest`
        :rtype: :class:`huaweicloudsdkgeip.v3.ListInternetBandwidthCountFilterTagsResponse`
        """
        http_info = self._list_internet_bandwidth_count_filter_tags_http_info(request)
        return self._call_api(**http_info)

    def list_internet_bandwidth_count_filter_tags_invoker(self, request):
        http_info = self._list_internet_bandwidth_count_filter_tags_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_internet_bandwidth_count_filter_tags_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/internet-bandwidth/resource-instances/count",
            "request_type": request.__class__.__name__,
            "response_type": "ListInternetBandwidthCountFilterTagsResponse"
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

    def list_internet_bandwidth_domain_tags(self, request):
        """查询全域公网带宽项目标签

        查询全域公网带宽项目标签
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListInternetBandwidthDomainTags
        :type request: :class:`huaweicloudsdkgeip.v3.ListInternetBandwidthDomainTagsRequest`
        :rtype: :class:`huaweicloudsdkgeip.v3.ListInternetBandwidthDomainTagsResponse`
        """
        http_info = self._list_internet_bandwidth_domain_tags_http_info(request)
        return self._call_api(**http_info)

    def list_internet_bandwidth_domain_tags_invoker(self, request):
        http_info = self._list_internet_bandwidth_domain_tags_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_internet_bandwidth_domain_tags_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/internet-bandwidth/tags",
            "request_type": request.__class__.__name__,
            "response_type": "ListInternetBandwidthDomainTagsResponse"
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

    def list_internet_bandwidth_filter_tags(self, request):
        """查询资源实例列表

        查询资源实例列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListInternetBandwidthFilterTags
        :type request: :class:`huaweicloudsdkgeip.v3.ListInternetBandwidthFilterTagsRequest`
        :rtype: :class:`huaweicloudsdkgeip.v3.ListInternetBandwidthFilterTagsResponse`
        """
        http_info = self._list_internet_bandwidth_filter_tags_http_info(request)
        return self._call_api(**http_info)

    def list_internet_bandwidth_filter_tags_invoker(self, request):
        http_info = self._list_internet_bandwidth_filter_tags_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_internet_bandwidth_filter_tags_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/internet-bandwidth/resource-instances/filter",
            "request_type": request.__class__.__name__,
            "response_type": "ListInternetBandwidthFilterTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
            collection_formats['limit'] = 'multi'
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
            collection_formats['offset'] = 'multi'

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

    def list_internet_bandwidth_limits(self, request):
        """全域公网带宽限制列表

        查询全域公网带宽限制列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListInternetBandwidthLimits
        :type request: :class:`huaweicloudsdkgeip.v3.ListInternetBandwidthLimitsRequest`
        :rtype: :class:`huaweicloudsdkgeip.v3.ListInternetBandwidthLimitsResponse`
        """
        http_info = self._list_internet_bandwidth_limits_http_info(request)
        return self._call_api(**http_info)

    def list_internet_bandwidth_limits_invoker(self, request):
        http_info = self._list_internet_bandwidth_limits_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_internet_bandwidth_limits_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{domain_id}/geip/internet-bandwidth-limits",
            "request_type": request.__class__.__name__,
            "response_type": "ListInternetBandwidthLimitsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'fields' in local_var_params:
            query_params.append(('fields', local_var_params['fields']))
            collection_formats['fields'] = 'multi'
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
            collection_formats['sort_key'] = 'multi'
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
            collection_formats['sort_dir'] = 'multi'
        if 'charge_mode' in local_var_params:
            query_params.append(('charge_mode', local_var_params['charge_mode']))
            collection_formats['charge_mode'] = 'multi'
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))

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

    def list_internet_bandwidths(self, request):
        """查询全域公网带宽列表

        查询全域公网带宽列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListInternetBandwidths
        :type request: :class:`huaweicloudsdkgeip.v3.ListInternetBandwidthsRequest`
        :rtype: :class:`huaweicloudsdkgeip.v3.ListInternetBandwidthsResponse`
        """
        http_info = self._list_internet_bandwidths_http_info(request)
        return self._call_api(**http_info)

    def list_internet_bandwidths_invoker(self, request):
        http_info = self._list_internet_bandwidths_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_internet_bandwidths_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{domain_id}/geip/internet-bandwidths",
            "request_type": request.__class__.__name__,
            "response_type": "ListInternetBandwidthsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'page_reverse' in local_var_params:
            query_params.append(('page_reverse', local_var_params['page_reverse']))
        if 'fields' in local_var_params:
            query_params.append(('fields', local_var_params['fields']))
            collection_formats['fields'] = 'multi'
        if 'ext_fields' in local_var_params:
            query_params.append(('ext-fields', local_var_params['ext_fields']))
            collection_formats['ext-fields'] = 'multi'
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
            collection_formats['sort_key'] = 'multi'
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
            collection_formats['sort_dir'] = 'multi'
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
            collection_formats['id'] = 'multi'
        if 'size' in local_var_params:
            query_params.append(('size', local_var_params['size']))
            collection_formats['size'] = 'multi'
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
            collection_formats['name'] = 'multi'
        if 'name_like' in local_var_params:
            query_params.append(('name_like', local_var_params['name_like']))
        if 'access_site' in local_var_params:
            query_params.append(('access_site', local_var_params['access_site']))
            collection_formats['access_site'] = 'multi'
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
            collection_formats['status'] = 'multi'
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
            collection_formats['enterprise_project_id'] = 'multi'
        if 'tags' in local_var_params:
            query_params.append(('tags', local_var_params['tags']))
            collection_formats['tags'] = 'csv'
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
            collection_formats['type'] = 'multi'

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

    def list_support_masks(self, request):
        """查询全域弹性公网IP段支持的掩码列表

        查询全域弹性公网IP段支持的掩码列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListSupportMasks
        :type request: :class:`huaweicloudsdkgeip.v3.ListSupportMasksRequest`
        :rtype: :class:`huaweicloudsdkgeip.v3.ListSupportMasksResponse`
        """
        http_info = self._list_support_masks_http_info(request)
        return self._call_api(**http_info)

    def list_support_masks_invoker(self, request):
        http_info = self._list_support_masks_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_support_masks_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{domain_id}/global-eip-segments/support-masks",
            "request_type": request.__class__.__name__,
            "response_type": "ListSupportMasksResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'page_reverse' in local_var_params:
            query_params.append(('page_reverse', local_var_params['page_reverse']))
        if 'fields' in local_var_params:
            query_params.append(('fields', local_var_params['fields']))
            collection_formats['fields'] = 'multi'
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
            collection_formats['sort_key'] = 'multi'
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
            collection_formats['sort_dir'] = 'multi'
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
            collection_formats['id'] = 'multi'
        if 'ip_version' in local_var_params:
            query_params.append(('ip_version', local_var_params['ip_version']))
            collection_formats['ip_version'] = 'multi'
        if 'mask' in local_var_params:
            query_params.append(('mask', local_var_params['mask']))
            collection_formats['mask'] = 'multi'

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

    def show_internet_bandwidth(self, request):
        """查询全域公网带宽详情

        查询全域公网带宽详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowInternetBandwidth
        :type request: :class:`huaweicloudsdkgeip.v3.ShowInternetBandwidthRequest`
        :rtype: :class:`huaweicloudsdkgeip.v3.ShowInternetBandwidthResponse`
        """
        http_info = self._show_internet_bandwidth_http_info(request)
        return self._call_api(**http_info)

    def show_internet_bandwidth_invoker(self, request):
        http_info = self._show_internet_bandwidth_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_internet_bandwidth_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{domain_id}/geip/internet-bandwidths/{internet_bandwidth_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowInternetBandwidthResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'internet_bandwidth_id' in local_var_params:
            path_params['internet_bandwidth_id'] = local_var_params['internet_bandwidth_id']

        query_params = []
        if 'fields' in local_var_params:
            query_params.append(('fields', local_var_params['fields']))
            collection_formats['fields'] = 'multi'

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

    def show_internet_bandwidth_tags(self, request):
        """查询全域公网带宽标签

        查询全域公网带宽标签
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowInternetBandwidthTags
        :type request: :class:`huaweicloudsdkgeip.v3.ShowInternetBandwidthTagsRequest`
        :rtype: :class:`huaweicloudsdkgeip.v3.ShowInternetBandwidthTagsResponse`
        """
        http_info = self._show_internet_bandwidth_tags_http_info(request)
        return self._call_api(**http_info)

    def show_internet_bandwidth_tags_invoker(self, request):
        http_info = self._show_internet_bandwidth_tags_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_internet_bandwidth_tags_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/internet-bandwidth/{resource_id}/tags",
            "request_type": request.__class__.__name__,
            "response_type": "ShowInternetBandwidthTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_id' in local_var_params:
            path_params['resource_id'] = local_var_params['resource_id']

        query_params = []

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

    def show_user_disclaimer(self, request):
        """查询租户签署免责条款详情

        查询租户签署免责条款详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowUserDisclaimer
        :type request: :class:`huaweicloudsdkgeip.v3.ShowUserDisclaimerRequest`
        :rtype: :class:`huaweicloudsdkgeip.v3.ShowUserDisclaimerResponse`
        """
        http_info = self._show_user_disclaimer_http_info(request)
        return self._call_api(**http_info)

    def show_user_disclaimer_invoker(self, request):
        http_info = self._show_user_disclaimer_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_user_disclaimer_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{domain_id}/geip/user-disclaimer-records",
            "request_type": request.__class__.__name__,
            "response_type": "ShowUserDisclaimerResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'fields' in local_var_params:
            query_params.append(('fields', local_var_params['fields']))
            collection_formats['fields'] = 'multi'

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

    def update_internet_bandwidth(self, request):
        """更新全域公网带宽

        更新全域公网带宽
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateInternetBandwidth
        :type request: :class:`huaweicloudsdkgeip.v3.UpdateInternetBandwidthRequest`
        :rtype: :class:`huaweicloudsdkgeip.v3.UpdateInternetBandwidthResponse`
        """
        http_info = self._update_internet_bandwidth_http_info(request)
        return self._call_api(**http_info)

    def update_internet_bandwidth_invoker(self, request):
        http_info = self._update_internet_bandwidth_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_internet_bandwidth_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{domain_id}/geip/internet-bandwidths/{internet_bandwidth_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateInternetBandwidthResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'internet_bandwidth_id' in local_var_params:
            path_params['internet_bandwidth_id'] = local_var_params['internet_bandwidth_id']

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

    def add_geip_segment_tags(self, request):
        """添加全域弹性公网IP段标签

        添加全域弹性公网IP段的标签
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AddGeipSegmentTags
        :type request: :class:`huaweicloudsdkgeip.v3.AddGeipSegmentTagsRequest`
        :rtype: :class:`huaweicloudsdkgeip.v3.AddGeipSegmentTagsResponse`
        """
        http_info = self._add_geip_segment_tags_http_info(request)
        return self._call_api(**http_info)

    def add_geip_segment_tags_invoker(self, request):
        http_info = self._add_geip_segment_tags_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _add_geip_segment_tags_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/global-eip-segment/{resource_id}/tags",
            "request_type": request.__class__.__name__,
            "response_type": "AddGeipSegmentTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
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

    def add_global_eip_tags(self, request):
        """添加全域弹性公网IP标签

        添加全域弹性公网IP的标签
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AddGlobalEipTags
        :type request: :class:`huaweicloudsdkgeip.v3.AddGlobalEipTagsRequest`
        :rtype: :class:`huaweicloudsdkgeip.v3.AddGlobalEipTagsResponse`
        """
        http_info = self._add_global_eip_tags_http_info(request)
        return self._call_api(**http_info)

    def add_global_eip_tags_invoker(self, request):
        http_info = self._add_global_eip_tags_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _add_global_eip_tags_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/global-eip/{resource_id}/tags",
            "request_type": request.__class__.__name__,
            "response_type": "AddGlobalEipTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
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

    def associate_geip_segment_instance(self, request):
        """全域弹性公网IP段绑定后端实例

        全域弹性公网IP段绑定后端实例
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AssociateGeipSegmentInstance
        :type request: :class:`huaweicloudsdkgeip.v3.AssociateGeipSegmentInstanceRequest`
        :rtype: :class:`huaweicloudsdkgeip.v3.AssociateGeipSegmentInstanceResponse`
        """
        http_info = self._associate_geip_segment_instance_http_info(request)
        return self._call_api(**http_info)

    def associate_geip_segment_instance_invoker(self, request):
        http_info = self._associate_geip_segment_instance_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _associate_geip_segment_instance_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{domain_id}/global-eip-segments/{global_eip_segment_id}/associate-instance",
            "request_type": request.__class__.__name__,
            "response_type": "AssociateGeipSegmentInstanceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'global_eip_segment_id' in local_var_params:
            path_params['global_eip_segment_id'] = local_var_params['global_eip_segment_id']

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

    def associate_instance(self, request):
        """绑定后端实例

        绑定后端实例
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AssociateInstance
        :type request: :class:`huaweicloudsdkgeip.v3.AssociateInstanceRequest`
        :rtype: :class:`huaweicloudsdkgeip.v3.AssociateInstanceResponse`
        """
        http_info = self._associate_instance_http_info(request)
        return self._call_api(**http_info)

    def associate_instance_invoker(self, request):
        http_info = self._associate_instance_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _associate_instance_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{domain_id}/global-eips/{global_eip_id}/associate-instance",
            "request_type": request.__class__.__name__,
            "response_type": "AssociateInstanceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'global_eip_id' in local_var_params:
            path_params['global_eip_id'] = local_var_params['global_eip_id']

        query_params = []

        header_params = {}
        if 'binding_instance_service' in local_var_params:
            header_params['binding-instance-service'] = local_var_params['binding_instance_service']

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

    def attach_internet_bandwidth(self, request):
        """绑定全域公网带宽

        绑定全域公网带宽
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AttachInternetBandwidth
        :type request: :class:`huaweicloudsdkgeip.v3.AttachInternetBandwidthRequest`
        :rtype: :class:`huaweicloudsdkgeip.v3.AttachInternetBandwidthResponse`
        """
        http_info = self._attach_internet_bandwidth_http_info(request)
        return self._call_api(**http_info)

    def attach_internet_bandwidth_invoker(self, request):
        http_info = self._attach_internet_bandwidth_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _attach_internet_bandwidth_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{domain_id}/global-eips/{global_eip_id}/attach-internet-bandwidth",
            "request_type": request.__class__.__name__,
            "response_type": "AttachInternetBandwidthResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'global_eip_id' in local_var_params:
            path_params['global_eip_id'] = local_var_params['global_eip_id']

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

    def batch_attach_geip_segment_internet_bandwidth(self, request):
        """全域弹性公网IP段批量绑定全域公网带宽

        全域弹性公网IP段批量绑定全域公网带宽
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchAttachGeipSegmentInternetBandwidth
        :type request: :class:`huaweicloudsdkgeip.v3.BatchAttachGeipSegmentInternetBandwidthRequest`
        :rtype: :class:`huaweicloudsdkgeip.v3.BatchAttachGeipSegmentInternetBandwidthResponse`
        """
        http_info = self._batch_attach_geip_segment_internet_bandwidth_http_info(request)
        return self._call_api(**http_info)

    def batch_attach_geip_segment_internet_bandwidth_invoker(self, request):
        http_info = self._batch_attach_geip_segment_internet_bandwidth_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_attach_geip_segment_internet_bandwidth_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{domain_id}/global-eip-segments/batch-attach-internet-bandwidths",
            "request_type": request.__class__.__name__,
            "response_type": "BatchAttachGeipSegmentInternetBandwidthResponse"
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

    def batch_attach_internet_bandwidth(self, request):
        """批量绑定全域公网带宽

        批量绑定全域公网带宽
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchAttachInternetBandwidth
        :type request: :class:`huaweicloudsdkgeip.v3.BatchAttachInternetBandwidthRequest`
        :rtype: :class:`huaweicloudsdkgeip.v3.BatchAttachInternetBandwidthResponse`
        """
        http_info = self._batch_attach_internet_bandwidth_http_info(request)
        return self._call_api(**http_info)

    def batch_attach_internet_bandwidth_invoker(self, request):
        http_info = self._batch_attach_internet_bandwidth_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_attach_internet_bandwidth_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{domain_id}/global-eips/batch-attach-internet-bandwidths",
            "request_type": request.__class__.__name__,
            "response_type": "BatchAttachInternetBandwidthResponse"
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

    def batch_create_geip_segment_tags(self, request):
        """批量添加全域弹性公网IP段标签

        批量添加全域弹性公网IP段的标签
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchCreateGeipSegmentTags
        :type request: :class:`huaweicloudsdkgeip.v3.BatchCreateGeipSegmentTagsRequest`
        :rtype: :class:`huaweicloudsdkgeip.v3.BatchCreateGeipSegmentTagsResponse`
        """
        http_info = self._batch_create_geip_segment_tags_http_info(request)
        return self._call_api(**http_info)

    def batch_create_geip_segment_tags_invoker(self, request):
        http_info = self._batch_create_geip_segment_tags_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_create_geip_segment_tags_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/global-eip-segment/{resource_id}/tags/create",
            "request_type": request.__class__.__name__,
            "response_type": "BatchCreateGeipSegmentTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
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

    def batch_create_global_eip(self, request):
        """批量创建全域弹性公网IP

        批量创建全域弹性公网IP
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchCreateGlobalEip
        :type request: :class:`huaweicloudsdkgeip.v3.BatchCreateGlobalEipRequest`
        :rtype: :class:`huaweicloudsdkgeip.v3.BatchCreateGlobalEipResponse`
        """
        http_info = self._batch_create_global_eip_http_info(request)
        return self._call_api(**http_info)

    def batch_create_global_eip_invoker(self, request):
        http_info = self._batch_create_global_eip_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_create_global_eip_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{domain_id}/global-eips/batch-create",
            "request_type": request.__class__.__name__,
            "response_type": "BatchCreateGlobalEipResponse"
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

    def batch_create_global_eip_tags(self, request):
        """批量添加全域弹性公网IP标签

        批量添加全域弹性公网IP的标签
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchCreateGlobalEipTags
        :type request: :class:`huaweicloudsdkgeip.v3.BatchCreateGlobalEipTagsRequest`
        :rtype: :class:`huaweicloudsdkgeip.v3.BatchCreateGlobalEipTagsResponse`
        """
        http_info = self._batch_create_global_eip_tags_http_info(request)
        return self._call_api(**http_info)

    def batch_create_global_eip_tags_invoker(self, request):
        http_info = self._batch_create_global_eip_tags_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_create_global_eip_tags_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/global-eip/{resource_id}/tags/create",
            "request_type": request.__class__.__name__,
            "response_type": "BatchCreateGlobalEipTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
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

    def batch_delete_geip_segment_tags(self, request):
        """批量删除全域弹性公网IP段标签

        批量删除全域弹性公网IP段的标签
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchDeleteGeipSegmentTags
        :type request: :class:`huaweicloudsdkgeip.v3.BatchDeleteGeipSegmentTagsRequest`
        :rtype: :class:`huaweicloudsdkgeip.v3.BatchDeleteGeipSegmentTagsResponse`
        """
        http_info = self._batch_delete_geip_segment_tags_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_geip_segment_tags_invoker(self, request):
        http_info = self._batch_delete_geip_segment_tags_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_delete_geip_segment_tags_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/global-eip-segment/{resource_id}/tags/delete",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeleteGeipSegmentTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
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

    def batch_delete_global_eip_tags(self, request):
        """批量删除全域弹性公网IP标签

        批量删除全域弹性公网IP的标签
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchDeleteGlobalEipTags
        :type request: :class:`huaweicloudsdkgeip.v3.BatchDeleteGlobalEipTagsRequest`
        :rtype: :class:`huaweicloudsdkgeip.v3.BatchDeleteGlobalEipTagsResponse`
        """
        http_info = self._batch_delete_global_eip_tags_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_global_eip_tags_invoker(self, request):
        http_info = self._batch_delete_global_eip_tags_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_delete_global_eip_tags_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/global-eip/{resource_id}/tags/delete",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeleteGlobalEipTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
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

    def batch_detach_geip_segment_internet_bandwidth(self, request):
        """全域弹性公网IP段批量解绑全域公网带宽

        全域弹性公网IP段批量解绑全域公网带宽
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchDetachGeipSegmentInternetBandwidth
        :type request: :class:`huaweicloudsdkgeip.v3.BatchDetachGeipSegmentInternetBandwidthRequest`
        :rtype: :class:`huaweicloudsdkgeip.v3.BatchDetachGeipSegmentInternetBandwidthResponse`
        """
        http_info = self._batch_detach_geip_segment_internet_bandwidth_http_info(request)
        return self._call_api(**http_info)

    def batch_detach_geip_segment_internet_bandwidth_invoker(self, request):
        http_info = self._batch_detach_geip_segment_internet_bandwidth_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_detach_geip_segment_internet_bandwidth_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{domain_id}/global-eip-segments/batch-detach-internet-bandwidths",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDetachGeipSegmentInternetBandwidthResponse"
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

    def batch_detach_internet_bandwidth(self, request):
        """批量解绑全域公网带宽

        批量解绑全域公网带宽
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchDetachInternetBandwidth
        :type request: :class:`huaweicloudsdkgeip.v3.BatchDetachInternetBandwidthRequest`
        :rtype: :class:`huaweicloudsdkgeip.v3.BatchDetachInternetBandwidthResponse`
        """
        http_info = self._batch_detach_internet_bandwidth_http_info(request)
        return self._call_api(**http_info)

    def batch_detach_internet_bandwidth_invoker(self, request):
        http_info = self._batch_detach_internet_bandwidth_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_detach_internet_bandwidth_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{domain_id}/global-eips/batch-detach-internet-bandwidths",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDetachInternetBandwidthResponse"
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

    def count_global_eip_segment(self, request):
        """查询全域弹性公网IP段个数

        查询全域弹性公网IP段个数
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CountGlobalEipSegment
        :type request: :class:`huaweicloudsdkgeip.v3.CountGlobalEipSegmentRequest`
        :rtype: :class:`huaweicloudsdkgeip.v3.CountGlobalEipSegmentResponse`
        """
        http_info = self._count_global_eip_segment_http_info(request)
        return self._call_api(**http_info)

    def count_global_eip_segment_invoker(self, request):
        http_info = self._count_global_eip_segment_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _count_global_eip_segment_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{domain_id}/global-eip-segments/count",
            "request_type": request.__class__.__name__,
            "response_type": "CountGlobalEipSegmentResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'page_reverse' in local_var_params:
            query_params.append(('page_reverse', local_var_params['page_reverse']))
        if 'fields' in local_var_params:
            query_params.append(('fields', local_var_params['fields']))
            collection_formats['fields'] = 'multi'
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
            collection_formats['id'] = 'multi'
        if 'internet_bandwidth_id' in local_var_params:
            query_params.append(('internet_bandwidth_id', local_var_params['internet_bandwidth_id']))
            collection_formats['internet_bandwidth_id'] = 'multi'
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
            collection_formats['name'] = 'multi'
        if 'name_like' in local_var_params:
            query_params.append(('name_like', local_var_params['name_like']))
        if 'access_site' in local_var_params:
            query_params.append(('access_site', local_var_params['access_site']))
            collection_formats['access_site'] = 'multi'
        if 'geip_pool_name' in local_var_params:
            query_params.append(('geip_pool_name', local_var_params['geip_pool_name']))
            collection_formats['geip_pool_name'] = 'multi'
        if 'isp' in local_var_params:
            query_params.append(('isp', local_var_params['isp']))
            collection_formats['isp'] = 'multi'
        if 'ip_version' in local_var_params:
            query_params.append(('ip_version', local_var_params['ip_version']))
            collection_formats['ip_version'] = 'multi'
        if 'cidr' in local_var_params:
            query_params.append(('cidr', local_var_params['cidr']))
            collection_formats['cidr'] = 'multi'
        if 'cidr_v6' in local_var_params:
            query_params.append(('cidr_v6', local_var_params['cidr_v6']))
            collection_formats['cidr_v6'] = 'multi'
        if 'freezen' in local_var_params:
            query_params.append(('freezen', local_var_params['freezen']))
            collection_formats['freezen'] = 'multi'
        if 'internet_bandwidth_is_null' in local_var_params:
            query_params.append(('internet_bandwidth_is_null', local_var_params['internet_bandwidth_is_null']))
            collection_formats['internet_bandwidth_is_null'] = 'multi'
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
            collection_formats['status'] = 'multi'
        if 'associate_instance_region' in local_var_params:
            query_params.append(('associate_instance.region', local_var_params['associate_instance_region']))
            collection_formats['associate_instance.region'] = 'multi'
        if 'associate_instance_public_border_group' in local_var_params:
            query_params.append(('associate_instance.public_border_group', local_var_params['associate_instance_public_border_group']))
            collection_formats['associate_instance.public_border_group'] = 'multi'
        if 'associate_instance_instance_site' in local_var_params:
            query_params.append(('associate_instance.instance_site', local_var_params['associate_instance_instance_site']))
            collection_formats['associate_instance.instance_site'] = 'multi'
        if 'associate_instance_instance_type' in local_var_params:
            query_params.append(('associate_instance.instance_type', local_var_params['associate_instance_instance_type']))
            collection_formats['associate_instance.instance_type'] = 'multi'
        if 'associate_instance_instance_id' in local_var_params:
            query_params.append(('associate_instance.instance_id', local_var_params['associate_instance_instance_id']))
            collection_formats['associate_instance.instance_id'] = 'multi'
        if 'associate_instance_project_id' in local_var_params:
            query_params.append(('associate_instance.project_id', local_var_params['associate_instance_project_id']))
            collection_formats['associate_instance.project_id'] = 'multi'
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
            collection_formats['enterprise_project_id'] = 'multi'
        if 'tags' in local_var_params:
            query_params.append(('tags', local_var_params['tags']))
            collection_formats['tags'] = 'csv'

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

    def count_global_eips(self, request):
        """查询全域弹性公网IP个数

        查询全域弹性公网IP个数
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CountGlobalEips
        :type request: :class:`huaweicloudsdkgeip.v3.CountGlobalEipsRequest`
        :rtype: :class:`huaweicloudsdkgeip.v3.CountGlobalEipsResponse`
        """
        http_info = self._count_global_eips_http_info(request)
        return self._call_api(**http_info)

    def count_global_eips_invoker(self, request):
        http_info = self._count_global_eips_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _count_global_eips_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{domain_id}/global-eips/count",
            "request_type": request.__class__.__name__,
            "response_type": "CountGlobalEipsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
            collection_formats['id'] = 'multi'
        if 'internet_bandwidth_id' in local_var_params:
            query_params.append(('internet_bandwidth_id', local_var_params['internet_bandwidth_id']))
            collection_formats['internet_bandwidth_id'] = 'multi'
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
            collection_formats['name'] = 'multi'
        if 'name_like' in local_var_params:
            query_params.append(('name_like', local_var_params['name_like']))
        if 'access_site' in local_var_params:
            query_params.append(('access_site', local_var_params['access_site']))
            collection_formats['access_site'] = 'multi'
        if 'geip_pool_name' in local_var_params:
            query_params.append(('geip_pool_name', local_var_params['geip_pool_name']))
            collection_formats['geip_pool_name'] = 'multi'
        if 'isp' in local_var_params:
            query_params.append(('isp', local_var_params['isp']))
            collection_formats['isp'] = 'multi'
        if 'ip_version' in local_var_params:
            query_params.append(('ip_version', local_var_params['ip_version']))
            collection_formats['ip_version'] = 'multi'
        if 'ip_address' in local_var_params:
            query_params.append(('ip_address', local_var_params['ip_address']))
            collection_formats['ip_address'] = 'multi'
        if 'ipv6_address' in local_var_params:
            query_params.append(('ipv6_address', local_var_params['ipv6_address']))
            collection_formats['ipv6_address'] = 'multi'
        if 'freezen' in local_var_params:
            query_params.append(('freezen', local_var_params['freezen']))
            collection_formats['freezen'] = 'multi'
        if 'polluted' in local_var_params:
            query_params.append(('polluted', local_var_params['polluted']))
            collection_formats['polluted'] = 'multi'
        if 'internet_bandwidth_is_null' in local_var_params:
            query_params.append(('internet_bandwidth_is_null', local_var_params['internet_bandwidth_is_null']))
            collection_formats['internet_bandwidth_is_null'] = 'multi'
        if 'gcb_bandwidth_is_null' in local_var_params:
            query_params.append(('gcb_bandwidth_is_null', local_var_params['gcb_bandwidth_is_null']))
            collection_formats['gcb_bandwidth_is_null'] = 'multi'
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
            collection_formats['status'] = 'multi'
        if 'associate_instance_info_region' in local_var_params:
            query_params.append(('associate_instance_info.region', local_var_params['associate_instance_info_region']))
            collection_formats['associate_instance_info.region'] = 'multi'
        if 'associate_instance_info_public_border_group' in local_var_params:
            query_params.append(('associate_instance_info.public_border_group', local_var_params['associate_instance_info_public_border_group']))
            collection_formats['associate_instance_info.public_border_group'] = 'multi'
        if 'associate_instance_info_instance_site' in local_var_params:
            query_params.append(('associate_instance_info.instance_site', local_var_params['associate_instance_info_instance_site']))
            collection_formats['associate_instance_info.instance_site'] = 'multi'
        if 'associate_instance_info_instance_type' in local_var_params:
            query_params.append(('associate_instance_info.instance_type', local_var_params['associate_instance_info_instance_type']))
            collection_formats['associate_instance_info.instance_type'] = 'multi'
        if 'associate_instance_info_instance_id' in local_var_params:
            query_params.append(('associate_instance_info.instance_id', local_var_params['associate_instance_info_instance_id']))
            collection_formats['associate_instance_info.instance_id'] = 'multi'
        if 'associate_instance_info_project_id' in local_var_params:
            query_params.append(('associate_instance_info.project_id', local_var_params['associate_instance_info_project_id']))
            collection_formats['associate_instance_info.project_id'] = 'multi'
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
            collection_formats['enterprise_project_id'] = 'multi'
        if 'tags' in local_var_params:
            query_params.append(('tags', local_var_params['tags']))
            collection_formats['tags'] = 'csv'

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

    def create_global_eip(self, request):
        """创建全域弹性公网IP

        创建全域弹性公网IP
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateGlobalEip
        :type request: :class:`huaweicloudsdkgeip.v3.CreateGlobalEipRequest`
        :rtype: :class:`huaweicloudsdkgeip.v3.CreateGlobalEipResponse`
        """
        http_info = self._create_global_eip_http_info(request)
        return self._call_api(**http_info)

    def create_global_eip_invoker(self, request):
        http_info = self._create_global_eip_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_global_eip_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{domain_id}/global-eips",
            "request_type": request.__class__.__name__,
            "response_type": "CreateGlobalEipResponse"
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

    def create_global_eip_segment(self, request):
        """创建全域弹性公网IP段

        创建全域弹性公网IP段
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateGlobalEipSegment
        :type request: :class:`huaweicloudsdkgeip.v3.CreateGlobalEipSegmentRequest`
        :rtype: :class:`huaweicloudsdkgeip.v3.CreateGlobalEipSegmentResponse`
        """
        http_info = self._create_global_eip_segment_http_info(request)
        return self._call_api(**http_info)

    def create_global_eip_segment_invoker(self, request):
        http_info = self._create_global_eip_segment_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_global_eip_segment_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{domain_id}/global-eip-segments",
            "request_type": request.__class__.__name__,
            "response_type": "CreateGlobalEipSegmentResponse"
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

    def delete_geip_segment_tag(self, request):
        """删除全域弹性公网IP段标签

        删除全域弹性公网IP段的标签
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteGeipSegmentTag
        :type request: :class:`huaweicloudsdkgeip.v3.DeleteGeipSegmentTagRequest`
        :rtype: :class:`huaweicloudsdkgeip.v3.DeleteGeipSegmentTagResponse`
        """
        http_info = self._delete_geip_segment_tag_http_info(request)
        return self._call_api(**http_info)

    def delete_geip_segment_tag_invoker(self, request):
        http_info = self._delete_geip_segment_tag_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_geip_segment_tag_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/global-eip-segment/{resource_id}/tags/{tag_key}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteGeipSegmentTagResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_id' in local_var_params:
            path_params['resource_id'] = local_var_params['resource_id']
        if 'tag_key' in local_var_params:
            path_params['tag_key'] = local_var_params['tag_key']

        query_params = []

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

    def delete_global_eip(self, request):
        """删除全域弹性公网IP

        删除全域弹性公网IP
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteGlobalEip
        :type request: :class:`huaweicloudsdkgeip.v3.DeleteGlobalEipRequest`
        :rtype: :class:`huaweicloudsdkgeip.v3.DeleteGlobalEipResponse`
        """
        http_info = self._delete_global_eip_http_info(request)
        return self._call_api(**http_info)

    def delete_global_eip_invoker(self, request):
        http_info = self._delete_global_eip_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_global_eip_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{domain_id}/global-eips/{global_eip_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteGlobalEipResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'global_eip_id' in local_var_params:
            path_params['global_eip_id'] = local_var_params['global_eip_id']

        query_params = []

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

    def delete_global_eip_segment(self, request):
        """删除全域弹性公网IP段

        删除全域弹性公网IP段
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteGlobalEipSegment
        :type request: :class:`huaweicloudsdkgeip.v3.DeleteGlobalEipSegmentRequest`
        :rtype: :class:`huaweicloudsdkgeip.v3.DeleteGlobalEipSegmentResponse`
        """
        http_info = self._delete_global_eip_segment_http_info(request)
        return self._call_api(**http_info)

    def delete_global_eip_segment_invoker(self, request):
        http_info = self._delete_global_eip_segment_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_global_eip_segment_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{domain_id}/global-eip-segments/{global_eip_segment_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteGlobalEipSegmentResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'global_eip_segment_id' in local_var_params:
            path_params['global_eip_segment_id'] = local_var_params['global_eip_segment_id']

        query_params = []

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

    def delete_global_eip_tag(self, request):
        """删除全域弹性公网IP标签

        删除全域弹性公网IP的标签
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteGlobalEipTag
        :type request: :class:`huaweicloudsdkgeip.v3.DeleteGlobalEipTagRequest`
        :rtype: :class:`huaweicloudsdkgeip.v3.DeleteGlobalEipTagResponse`
        """
        http_info = self._delete_global_eip_tag_http_info(request)
        return self._call_api(**http_info)

    def delete_global_eip_tag_invoker(self, request):
        http_info = self._delete_global_eip_tag_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_global_eip_tag_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/global-eip/{resource_id}/tags/{tag_key}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteGlobalEipTagResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_id' in local_var_params:
            path_params['resource_id'] = local_var_params['resource_id']
        if 'tag_key' in local_var_params:
            path_params['tag_key'] = local_var_params['tag_key']

        query_params = []

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

    def detach_internet_bandwidth(self, request):
        """解绑全域公网带宽

        解绑全域公网带宽
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DetachInternetBandwidth
        :type request: :class:`huaweicloudsdkgeip.v3.DetachInternetBandwidthRequest`
        :rtype: :class:`huaweicloudsdkgeip.v3.DetachInternetBandwidthResponse`
        """
        http_info = self._detach_internet_bandwidth_http_info(request)
        return self._call_api(**http_info)

    def detach_internet_bandwidth_invoker(self, request):
        http_info = self._detach_internet_bandwidth_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _detach_internet_bandwidth_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{domain_id}/global-eips/{global_eip_id}/detach-internet-bandwidth",
            "request_type": request.__class__.__name__,
            "response_type": "DetachInternetBandwidthResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'global_eip_id' in local_var_params:
            path_params['global_eip_id'] = local_var_params['global_eip_id']

        query_params = []
        if 'force_unbind' in local_var_params:
            query_params.append(('force_unbind', local_var_params['force_unbind']))

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

    def disassociate_geip_segment_instance(self, request):
        """全域弹性公网IP段解绑后端实例

        全域弹性公网IP段解绑后端实例
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DisassociateGeipSegmentInstance
        :type request: :class:`huaweicloudsdkgeip.v3.DisassociateGeipSegmentInstanceRequest`
        :rtype: :class:`huaweicloudsdkgeip.v3.DisassociateGeipSegmentInstanceResponse`
        """
        http_info = self._disassociate_geip_segment_instance_http_info(request)
        return self._call_api(**http_info)

    def disassociate_geip_segment_instance_invoker(self, request):
        http_info = self._disassociate_geip_segment_instance_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _disassociate_geip_segment_instance_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{domain_id}/global-eip-segments/{global_eip_segment_id}/disassociate-instance",
            "request_type": request.__class__.__name__,
            "response_type": "DisassociateGeipSegmentInstanceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'global_eip_segment_id' in local_var_params:
            path_params['global_eip_segment_id'] = local_var_params['global_eip_segment_id']

        query_params = []

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

    def disassociate_instance(self, request):
        """解绑后端实例

        解绑后端实例
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DisassociateInstance
        :type request: :class:`huaweicloudsdkgeip.v3.DisassociateInstanceRequest`
        :rtype: :class:`huaweicloudsdkgeip.v3.DisassociateInstanceResponse`
        """
        http_info = self._disassociate_instance_http_info(request)
        return self._call_api(**http_info)

    def disassociate_instance_invoker(self, request):
        http_info = self._disassociate_instance_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _disassociate_instance_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{domain_id}/global-eips/{global_eip_id}/disassociate-instance",
            "request_type": request.__class__.__name__,
            "response_type": "DisassociateInstanceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'global_eip_id' in local_var_params:
            path_params['global_eip_id'] = local_var_params['global_eip_id']

        query_params = []

        header_params = {}
        if 'is_reserve_gcb' in local_var_params:
            header_params['is_reserve_gcb'] = local_var_params['is_reserve_gcb']

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

    def list_geip_pools(self, request):
        """查询全域弹性公网IP池列表

        查询全域弹性公网IP池列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListGeipPools
        :type request: :class:`huaweicloudsdkgeip.v3.ListGeipPoolsRequest`
        :rtype: :class:`huaweicloudsdkgeip.v3.ListGeipPoolsResponse`
        """
        http_info = self._list_geip_pools_http_info(request)
        return self._call_api(**http_info)

    def list_geip_pools_invoker(self, request):
        http_info = self._list_geip_pools_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_geip_pools_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{domain_id}/geip/geip-pools",
            "request_type": request.__class__.__name__,
            "response_type": "ListGeipPoolsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'page_reverse' in local_var_params:
            query_params.append(('page_reverse', local_var_params['page_reverse']))
        if 'fields' in local_var_params:
            query_params.append(('fields', local_var_params['fields']))
            collection_formats['fields'] = 'multi'
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
        if 'access_site' in local_var_params:
            query_params.append(('access_site', local_var_params['access_site']))
            collection_formats['access_site'] = 'multi'
        if 'isp' in local_var_params:
            query_params.append(('isp', local_var_params['isp']))
            collection_formats['isp'] = 'multi'
        if 'ip_version' in local_var_params:
            query_params.append(('ip_version', local_var_params['ip_version']))
            collection_formats['ip_version'] = 'multi'
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
            collection_formats['status'] = 'multi'
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
            collection_formats['type'] = 'multi'

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

    def list_geip_segment_count_filter_tags(self, request):
        """查询资源实例列表数目

        查询资源实例列表的数目
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListGeipSegmentCountFilterTags
        :type request: :class:`huaweicloudsdkgeip.v3.ListGeipSegmentCountFilterTagsRequest`
        :rtype: :class:`huaweicloudsdkgeip.v3.ListGeipSegmentCountFilterTagsResponse`
        """
        http_info = self._list_geip_segment_count_filter_tags_http_info(request)
        return self._call_api(**http_info)

    def list_geip_segment_count_filter_tags_invoker(self, request):
        http_info = self._list_geip_segment_count_filter_tags_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_geip_segment_count_filter_tags_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/global-eip-segment/resource-instances/count",
            "request_type": request.__class__.__name__,
            "response_type": "ListGeipSegmentCountFilterTagsResponse"
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

    def list_geip_segment_domain_tags(self, request):
        """查询全域弹性公网IP段项目标签

        查询全域弹性公网IP段的项目标签
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListGeipSegmentDomainTags
        :type request: :class:`huaweicloudsdkgeip.v3.ListGeipSegmentDomainTagsRequest`
        :rtype: :class:`huaweicloudsdkgeip.v3.ListGeipSegmentDomainTagsResponse`
        """
        http_info = self._list_geip_segment_domain_tags_http_info(request)
        return self._call_api(**http_info)

    def list_geip_segment_domain_tags_invoker(self, request):
        http_info = self._list_geip_segment_domain_tags_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_geip_segment_domain_tags_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/global-eip-segment/tags",
            "request_type": request.__class__.__name__,
            "response_type": "ListGeipSegmentDomainTagsResponse"
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

    def list_geip_segment_filter_tags(self, request):
        """查询资源实例列表

        查询资源实例的列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListGeipSegmentFilterTags
        :type request: :class:`huaweicloudsdkgeip.v3.ListGeipSegmentFilterTagsRequest`
        :rtype: :class:`huaweicloudsdkgeip.v3.ListGeipSegmentFilterTagsResponse`
        """
        http_info = self._list_geip_segment_filter_tags_http_info(request)
        return self._call_api(**http_info)

    def list_geip_segment_filter_tags_invoker(self, request):
        http_info = self._list_geip_segment_filter_tags_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_geip_segment_filter_tags_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/global-eip-segment/resource-instances/filter",
            "request_type": request.__class__.__name__,
            "response_type": "ListGeipSegmentFilterTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
            collection_formats['limit'] = 'multi'
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
            collection_formats['offset'] = 'multi'

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

    def list_global_eip_count_filter_tags(self, request):
        """查询资源实例列表数目

        查询资源实例列表数目
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListGlobalEipCountFilterTags
        :type request: :class:`huaweicloudsdkgeip.v3.ListGlobalEipCountFilterTagsRequest`
        :rtype: :class:`huaweicloudsdkgeip.v3.ListGlobalEipCountFilterTagsResponse`
        """
        http_info = self._list_global_eip_count_filter_tags_http_info(request)
        return self._call_api(**http_info)

    def list_global_eip_count_filter_tags_invoker(self, request):
        http_info = self._list_global_eip_count_filter_tags_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_global_eip_count_filter_tags_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/global-eip/resource-instances/count",
            "request_type": request.__class__.__name__,
            "response_type": "ListGlobalEipCountFilterTagsResponse"
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

    def list_global_eip_domain_tags(self, request):
        """查询全域弹性公网IP项目标签

        查询全域弹性公网IP的项目标签
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListGlobalEipDomainTags
        :type request: :class:`huaweicloudsdkgeip.v3.ListGlobalEipDomainTagsRequest`
        :rtype: :class:`huaweicloudsdkgeip.v3.ListGlobalEipDomainTagsResponse`
        """
        http_info = self._list_global_eip_domain_tags_http_info(request)
        return self._call_api(**http_info)

    def list_global_eip_domain_tags_invoker(self, request):
        http_info = self._list_global_eip_domain_tags_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_global_eip_domain_tags_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/global-eip/tags",
            "request_type": request.__class__.__name__,
            "response_type": "ListGlobalEipDomainTagsResponse"
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

    def list_global_eip_filter_tags(self, request):
        """查询资源实例列表

        查询资源实例列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListGlobalEipFilterTags
        :type request: :class:`huaweicloudsdkgeip.v3.ListGlobalEipFilterTagsRequest`
        :rtype: :class:`huaweicloudsdkgeip.v3.ListGlobalEipFilterTagsResponse`
        """
        http_info = self._list_global_eip_filter_tags_http_info(request)
        return self._call_api(**http_info)

    def list_global_eip_filter_tags_invoker(self, request):
        http_info = self._list_global_eip_filter_tags_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_global_eip_filter_tags_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/global-eip/resource-instances/filter",
            "request_type": request.__class__.__name__,
            "response_type": "ListGlobalEipFilterTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
            collection_formats['limit'] = 'multi'
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
            collection_formats['offset'] = 'multi'

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

    def list_global_eip_segments(self, request):
        """查询全域弹性公网IP段列表

        查询全域弹性公网IP段列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListGlobalEipSegments
        :type request: :class:`huaweicloudsdkgeip.v3.ListGlobalEipSegmentsRequest`
        :rtype: :class:`huaweicloudsdkgeip.v3.ListGlobalEipSegmentsResponse`
        """
        http_info = self._list_global_eip_segments_http_info(request)
        return self._call_api(**http_info)

    def list_global_eip_segments_invoker(self, request):
        http_info = self._list_global_eip_segments_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_global_eip_segments_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{domain_id}/global-eip-segments",
            "request_type": request.__class__.__name__,
            "response_type": "ListGlobalEipSegmentsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'page_reverse' in local_var_params:
            query_params.append(('page_reverse', local_var_params['page_reverse']))
        if 'fields' in local_var_params:
            query_params.append(('fields', local_var_params['fields']))
            collection_formats['fields'] = 'multi'
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
            collection_formats['sort_key'] = 'multi'
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
            collection_formats['sort_dir'] = 'multi'
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
            collection_formats['id'] = 'multi'
        if 'internet_bandwidth_id' in local_var_params:
            query_params.append(('internet_bandwidth_id', local_var_params['internet_bandwidth_id']))
            collection_formats['internet_bandwidth_id'] = 'multi'
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
            collection_formats['name'] = 'multi'
        if 'name_like' in local_var_params:
            query_params.append(('name_like', local_var_params['name_like']))
        if 'access_site' in local_var_params:
            query_params.append(('access_site', local_var_params['access_site']))
            collection_formats['access_site'] = 'multi'
        if 'geip_pool_name' in local_var_params:
            query_params.append(('geip_pool_name', local_var_params['geip_pool_name']))
            collection_formats['geip_pool_name'] = 'multi'
        if 'isp' in local_var_params:
            query_params.append(('isp', local_var_params['isp']))
            collection_formats['isp'] = 'multi'
        if 'ip_version' in local_var_params:
            query_params.append(('ip_version', local_var_params['ip_version']))
            collection_formats['ip_version'] = 'multi'
        if 'cidr' in local_var_params:
            query_params.append(('cidr', local_var_params['cidr']))
            collection_formats['cidr'] = 'multi'
        if 'cidr_v6' in local_var_params:
            query_params.append(('cidr_v6', local_var_params['cidr_v6']))
            collection_formats['cidr_v6'] = 'multi'
        if 'freezen' in local_var_params:
            query_params.append(('freezen', local_var_params['freezen']))
            collection_formats['freezen'] = 'multi'
        if 'internet_bandwidth_is_null' in local_var_params:
            query_params.append(('internet_bandwidth_is_null', local_var_params['internet_bandwidth_is_null']))
            collection_formats['internet_bandwidth_is_null'] = 'multi'
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
            collection_formats['status'] = 'multi'
        if 'associate_instance_region' in local_var_params:
            query_params.append(('associate_instance.region', local_var_params['associate_instance_region']))
            collection_formats['associate_instance.region'] = 'multi'
        if 'associate_instance_instance_type' in local_var_params:
            query_params.append(('associate_instance.instance_type', local_var_params['associate_instance_instance_type']))
            collection_formats['associate_instance.instance_type'] = 'multi'
        if 'associate_instance_public_border_group' in local_var_params:
            query_params.append(('associate_instance.public_border_group', local_var_params['associate_instance_public_border_group']))
            collection_formats['associate_instance.public_border_group'] = 'multi'
        if 'associate_instance_instance_site' in local_var_params:
            query_params.append(('associate_instance.instance_site', local_var_params['associate_instance_instance_site']))
            collection_formats['associate_instance.instance_site'] = 'multi'
        if 'associate_instance_instance_id' in local_var_params:
            query_params.append(('associate_instance.instance_id', local_var_params['associate_instance_instance_id']))
            collection_formats['associate_instance.instance_id'] = 'multi'
        if 'associate_instance_project_id' in local_var_params:
            query_params.append(('associate_instance.project_id', local_var_params['associate_instance_project_id']))
            collection_formats['associate_instance.project_id'] = 'multi'
        if 'associate_instance_service_id' in local_var_params:
            query_params.append(('associate_instance.service_id', local_var_params['associate_instance_service_id']))
            collection_formats['associate_instance.service_id'] = 'multi'
        if 'associate_instance_service_type' in local_var_params:
            query_params.append(('associate_instance.service_type', local_var_params['associate_instance_service_type']))
            collection_formats['associate_instance.service_type'] = 'multi'
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
            collection_formats['enterprise_project_id'] = 'multi'
        if 'tags' in local_var_params:
            query_params.append(('tags', local_var_params['tags']))
            collection_formats['tags'] = 'csv'

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

    def list_global_eips(self, request):
        """查询全域弹性公网IP列表

        查询全域弹性公网IP列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListGlobalEips
        :type request: :class:`huaweicloudsdkgeip.v3.ListGlobalEipsRequest`
        :rtype: :class:`huaweicloudsdkgeip.v3.ListGlobalEipsResponse`
        """
        http_info = self._list_global_eips_http_info(request)
        return self._call_api(**http_info)

    def list_global_eips_invoker(self, request):
        http_info = self._list_global_eips_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_global_eips_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{domain_id}/global-eips",
            "request_type": request.__class__.__name__,
            "response_type": "ListGlobalEipsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'page_reverse' in local_var_params:
            query_params.append(('page_reverse', local_var_params['page_reverse']))
        if 'fields' in local_var_params:
            query_params.append(('fields', local_var_params['fields']))
            collection_formats['fields'] = 'multi'
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
            collection_formats['sort_key'] = 'multi'
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
            collection_formats['sort_dir'] = 'multi'
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
            collection_formats['id'] = 'multi'
        if 'internet_bandwidth_id' in local_var_params:
            query_params.append(('internet_bandwidth_id', local_var_params['internet_bandwidth_id']))
            collection_formats['internet_bandwidth_id'] = 'multi'
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
            collection_formats['name'] = 'multi'
        if 'name_like' in local_var_params:
            query_params.append(('name_like', local_var_params['name_like']))
        if 'access_site' in local_var_params:
            query_params.append(('access_site', local_var_params['access_site']))
            collection_formats['access_site'] = 'multi'
        if 'geip_pool_name' in local_var_params:
            query_params.append(('geip_pool_name', local_var_params['geip_pool_name']))
            collection_formats['geip_pool_name'] = 'multi'
        if 'isp' in local_var_params:
            query_params.append(('isp', local_var_params['isp']))
            collection_formats['isp'] = 'multi'
        if 'ip_version' in local_var_params:
            query_params.append(('ip_version', local_var_params['ip_version']))
            collection_formats['ip_version'] = 'multi'
        if 'ip_address' in local_var_params:
            query_params.append(('ip_address', local_var_params['ip_address']))
            collection_formats['ip_address'] = 'multi'
        if 'ipv6_address' in local_var_params:
            query_params.append(('ipv6_address', local_var_params['ipv6_address']))
            collection_formats['ipv6_address'] = 'multi'
        if 'freezen' in local_var_params:
            query_params.append(('freezen', local_var_params['freezen']))
            collection_formats['freezen'] = 'multi'
        if 'polluted' in local_var_params:
            query_params.append(('polluted', local_var_params['polluted']))
            collection_formats['polluted'] = 'multi'
        if 'internet_bandwidth_is_null' in local_var_params:
            query_params.append(('internet_bandwidth_is_null', local_var_params['internet_bandwidth_is_null']))
            collection_formats['internet_bandwidth_is_null'] = 'multi'
        if 'gcb_bandwidth_is_null' in local_var_params:
            query_params.append(('gcb_bandwidth_is_null', local_var_params['gcb_bandwidth_is_null']))
            collection_formats['gcb_bandwidth_is_null'] = 'multi'
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
            collection_formats['status'] = 'multi'
        if 'associate_instance_info_region' in local_var_params:
            query_params.append(('associate_instance_info.region', local_var_params['associate_instance_info_region']))
            collection_formats['associate_instance_info.region'] = 'multi'
        if 'associate_instance_info_instance_type' in local_var_params:
            query_params.append(('associate_instance_info.instance_type', local_var_params['associate_instance_info_instance_type']))
            collection_formats['associate_instance_info.instance_type'] = 'multi'
        if 'associate_instance_info_public_border_group' in local_var_params:
            query_params.append(('associate_instance_info.public_border_group', local_var_params['associate_instance_info_public_border_group']))
            collection_formats['associate_instance_info.public_border_group'] = 'multi'
        if 'associate_instance_info_instance_site' in local_var_params:
            query_params.append(('associate_instance_info.instance_site', local_var_params['associate_instance_info_instance_site']))
            collection_formats['associate_instance_info.instance_site'] = 'multi'
        if 'associate_instance_info_instance_id' in local_var_params:
            query_params.append(('associate_instance_info.instance_id', local_var_params['associate_instance_info_instance_id']))
            collection_formats['associate_instance_info.instance_id'] = 'multi'
        if 'associate_instance_info_project_id' in local_var_params:
            query_params.append(('associate_instance_info.project_id', local_var_params['associate_instance_info_project_id']))
            collection_formats['associate_instance_info.project_id'] = 'multi'
        if 'associate_instance_info_service_id' in local_var_params:
            query_params.append(('associate_instance_info.service_id', local_var_params['associate_instance_info_service_id']))
            collection_formats['associate_instance_info.service_id'] = 'multi'
        if 'associate_instance_info_service_type' in local_var_params:
            query_params.append(('associate_instance_info.service_type', local_var_params['associate_instance_info_service_type']))
            collection_formats['associate_instance_info.service_type'] = 'multi'
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
            collection_formats['enterprise_project_id'] = 'multi'
        if 'tags' in local_var_params:
            query_params.append(('tags', local_var_params['tags']))
            collection_formats['tags'] = 'csv'

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

    def show_geip_segment_tags(self, request):
        """查询全域弹性公网IP段标签

        查询全域弹性公网IP段的标签
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowGeipSegmentTags
        :type request: :class:`huaweicloudsdkgeip.v3.ShowGeipSegmentTagsRequest`
        :rtype: :class:`huaweicloudsdkgeip.v3.ShowGeipSegmentTagsResponse`
        """
        http_info = self._show_geip_segment_tags_http_info(request)
        return self._call_api(**http_info)

    def show_geip_segment_tags_invoker(self, request):
        http_info = self._show_geip_segment_tags_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_geip_segment_tags_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/global-eip-segment/{resource_id}/tags",
            "request_type": request.__class__.__name__,
            "response_type": "ShowGeipSegmentTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_id' in local_var_params:
            path_params['resource_id'] = local_var_params['resource_id']

        query_params = []

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

    def show_global_eip(self, request):
        """查询全域弹性公网IP详情

        查询全域弹性公网IP详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowGlobalEip
        :type request: :class:`huaweicloudsdkgeip.v3.ShowGlobalEipRequest`
        :rtype: :class:`huaweicloudsdkgeip.v3.ShowGlobalEipResponse`
        """
        http_info = self._show_global_eip_http_info(request)
        return self._call_api(**http_info)

    def show_global_eip_invoker(self, request):
        http_info = self._show_global_eip_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_global_eip_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{domain_id}/global-eips/{global_eip_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowGlobalEipResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'global_eip_id' in local_var_params:
            path_params['global_eip_id'] = local_var_params['global_eip_id']

        query_params = []
        if 'fields' in local_var_params:
            query_params.append(('fields', local_var_params['fields']))
            collection_formats['fields'] = 'multi'

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

    def show_global_eip_segment(self, request):
        """查询全域弹性公网IP段详情

        查询全域弹性公网IP段详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowGlobalEipSegment
        :type request: :class:`huaweicloudsdkgeip.v3.ShowGlobalEipSegmentRequest`
        :rtype: :class:`huaweicloudsdkgeip.v3.ShowGlobalEipSegmentResponse`
        """
        http_info = self._show_global_eip_segment_http_info(request)
        return self._call_api(**http_info)

    def show_global_eip_segment_invoker(self, request):
        http_info = self._show_global_eip_segment_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_global_eip_segment_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{domain_id}/global-eip-segments/{global_eip_segment_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowGlobalEipSegmentResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'global_eip_segment_id' in local_var_params:
            path_params['global_eip_segment_id'] = local_var_params['global_eip_segment_id']

        query_params = []
        if 'fields' in local_var_params:
            query_params.append(('fields', local_var_params['fields']))
            collection_formats['fields'] = 'multi'

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

    def show_global_eip_tags(self, request):
        """查询全域弹性公网IP标签

        查询全域弹性公网IP的标签
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowGlobalEipTags
        :type request: :class:`huaweicloudsdkgeip.v3.ShowGlobalEipTagsRequest`
        :rtype: :class:`huaweicloudsdkgeip.v3.ShowGlobalEipTagsResponse`
        """
        http_info = self._show_global_eip_tags_http_info(request)
        return self._call_api(**http_info)

    def show_global_eip_tags_invoker(self, request):
        http_info = self._show_global_eip_tags_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_global_eip_tags_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/global-eip/{resource_id}/tags",
            "request_type": request.__class__.__name__,
            "response_type": "ShowGlobalEipTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_id' in local_var_params:
            path_params['resource_id'] = local_var_params['resource_id']

        query_params = []

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

    def update_global_eip(self, request):
        """更新全域弹性公网IP信息

        更新全域弹性公网IP信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateGlobalEip
        :type request: :class:`huaweicloudsdkgeip.v3.UpdateGlobalEipRequest`
        :rtype: :class:`huaweicloudsdkgeip.v3.UpdateGlobalEipResponse`
        """
        http_info = self._update_global_eip_http_info(request)
        return self._call_api(**http_info)

    def update_global_eip_invoker(self, request):
        http_info = self._update_global_eip_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_global_eip_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{domain_id}/global-eips/{global_eip_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateGlobalEipResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'global_eip_id' in local_var_params:
            path_params['global_eip_id'] = local_var_params['global_eip_id']

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

    def update_global_eip_segment(self, request):
        """更新全域弹性公网IP段

        更新全域弹性公网IP段
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateGlobalEipSegment
        :type request: :class:`huaweicloudsdkgeip.v3.UpdateGlobalEipSegmentRequest`
        :rtype: :class:`huaweicloudsdkgeip.v3.UpdateGlobalEipSegmentResponse`
        """
        http_info = self._update_global_eip_segment_http_info(request)
        return self._call_api(**http_info)

    def update_global_eip_segment_invoker(self, request):
        http_info = self._update_global_eip_segment_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_global_eip_segment_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{domain_id}/global-eip-segments/{global_eip_segment_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateGlobalEipSegmentResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'global_eip_segment_id' in local_var_params:
            path_params['global_eip_segment_id'] = local_var_params['global_eip_segment_id']

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

    def list_jobs(self, request):
        """查询Job列表

        查询Job列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListJobs
        :type request: :class:`huaweicloudsdkgeip.v3.ListJobsRequest`
        :rtype: :class:`huaweicloudsdkgeip.v3.ListJobsResponse`
        """
        http_info = self._list_jobs_http_info(request)
        return self._call_api(**http_info)

    def list_jobs_invoker(self, request):
        http_info = self._list_jobs_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_jobs_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{domain_id}/geip/jobs",
            "request_type": request.__class__.__name__,
            "response_type": "ListJobsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'page_reverse' in local_var_params:
            query_params.append(('page_reverse', local_var_params['page_reverse']))
        if 'fields' in local_var_params:
            query_params.append(('fields', local_var_params['fields']))
            collection_formats['fields'] = 'multi'
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
            collection_formats['sort_key'] = 'multi'
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
            collection_formats['sort_dir'] = 'multi'
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
            collection_formats['id'] = 'multi'
        if 'action' in local_var_params:
            query_params.append(('action', local_var_params['action']))
            collection_formats['action'] = 'multi'
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
            collection_formats['status'] = 'multi'

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

    def show_jobs(self, request):
        """查询Job详情

        查询Job详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowJobs
        :type request: :class:`huaweicloudsdkgeip.v3.ShowJobsRequest`
        :rtype: :class:`huaweicloudsdkgeip.v3.ShowJobsResponse`
        """
        http_info = self._show_jobs_http_info(request)
        return self._call_api(**http_info)

    def show_jobs_invoker(self, request):
        http_info = self._show_jobs_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_jobs_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{domain_id}/geip/jobs/{job_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowJobsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []
        if 'fields' in local_var_params:
            query_params.append(('fields', local_var_params['fields']))
            collection_formats['fields'] = 'multi'

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

    def list_support_regions(self, request):
        """全域弹性公网IP支持绑定的Region限制

        全域弹性公网IP支持绑定的Region限制
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListSupportRegions
        :type request: :class:`huaweicloudsdkgeip.v3.ListSupportRegionsRequest`
        :rtype: :class:`huaweicloudsdkgeip.v3.ListSupportRegionsResponse`
        """
        http_info = self._list_support_regions_http_info(request)
        return self._call_api(**http_info)

    def list_support_regions_invoker(self, request):
        http_info = self._list_support_regions_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_support_regions_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{domain_id}/geip/support-regions",
            "request_type": request.__class__.__name__,
            "response_type": "ListSupportRegionsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'page_reverse' in local_var_params:
            query_params.append(('page_reverse', local_var_params['page_reverse']))
        if 'fields' in local_var_params:
            query_params.append(('fields', local_var_params['fields']))
            collection_formats['fields'] = 'multi'
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
            collection_formats['sort_key'] = 'multi'
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
            collection_formats['sort_dir'] = 'multi'
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
            collection_formats['id'] = 'multi'
        if 'instance_type' in local_var_params:
            query_params.append(('instance_type', local_var_params['instance_type']))
            collection_formats['instance_type'] = 'multi'
        if 'public_border_group' in local_var_params:
            query_params.append(('public_border_group', local_var_params['public_border_group']))
            collection_formats['public_border_group'] = 'multi'
        if 'access_site' in local_var_params:
            query_params.append(('access_site', local_var_params['access_site']))
            collection_formats['access_site'] = 'multi'
        if 'region_id' in local_var_params:
            query_params.append(('region_id', local_var_params['region_id']))
            collection_formats['region_id'] = 'multi'
        if 'remote_endpoint' in local_var_params:
            query_params.append(('remote_endpoint', local_var_params['remote_endpoint']))
            collection_formats['remote_endpoint'] = 'multi'
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
            collection_formats['status'] = 'multi'

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

    def list_tenant_geip_support_instances(self, request):
        """查询指定站点允许绑定的Region信息

        console通过此接口获取指定pop点的全域弹性公网IP允许绑定的region实例信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListTenantGeipSupportInstances
        :type request: :class:`huaweicloudsdkgeip.v3.ListTenantGeipSupportInstancesRequest`
        :rtype: :class:`huaweicloudsdkgeip.v3.ListTenantGeipSupportInstancesResponse`
        """
        http_info = self._list_tenant_geip_support_instances_http_info(request)
        return self._call_api(**http_info)

    def list_tenant_geip_support_instances_invoker(self, request):
        http_info = self._list_tenant_geip_support_instances_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_tenant_geip_support_instances_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{domain_id}/global-eips/support-instances/{access_site}",
            "request_type": request.__class__.__name__,
            "response_type": "ListTenantGeipSupportInstancesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'access_site' in local_var_params:
            path_params['access_site'] = local_var_params['access_site']

        query_params = []
        if 'fields' in local_var_params:
            query_params.append(('fields', local_var_params['fields']))
            collection_formats['fields'] = 'multi'

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

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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkeip'")


class EipClient(Client):
    def __init__(self):
        super(EipClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkeip.v3.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "EipClient":
                raise TypeError("client type error, support client type is EipClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def list_bandwidth(self, request):
        r"""查询带宽列表

        查询带宽列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListBandwidth
        :type request: :class:`huaweicloudsdkeip.v3.ListBandwidthRequest`
        :rtype: :class:`huaweicloudsdkeip.v3.ListBandwidthResponse`
        """
        http_info = self._list_bandwidth_http_info(request)
        return self._call_api(**http_info)

    def list_bandwidth_invoker(self, request):
        http_info = self._list_bandwidth_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_bandwidth_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/eip/bandwidths",
            "request_type": request.__class__.__name__,
            "response_type": "ListBandwidthResponse"
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
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'fields' in local_var_params:
            query_params.append(('fields', local_var_params['fields']))
            collection_formats['fields'] = 'multi'
        if 'bandwidth_type' in local_var_params:
            query_params.append(('bandwidth_type', local_var_params['bandwidth_type']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'name_like' in local_var_params:
            query_params.append(('name_like', local_var_params['name_like']))
        if 'ingress_size' in local_var_params:
            query_params.append(('ingress_size', local_var_params['ingress_size']))
        if 'admin_state' in local_var_params:
            query_params.append(('admin_state', local_var_params['admin_state']))
        if 'billing_info' in local_var_params:
            query_params.append(('billing_info', local_var_params['billing_info']))
        if 'tags' in local_var_params:
            query_params.append(('tags', local_var_params['tags']))
        if 'enable_bandwidth_rules' in local_var_params:
            query_params.append(('enable_bandwidth_rules', local_var_params['enable_bandwidth_rules']))
        if 'rule_quota' in local_var_params:
            query_params.append(('rule_quota', local_var_params['rule_quota']))
        if 'public_border_group' in local_var_params:
            query_params.append(('public_border_group', local_var_params['public_border_group']))
        if 'charge_mode' in local_var_params:
            query_params.append(('charge_mode', local_var_params['charge_mode']))
        if 'size' in local_var_params:
            query_params.append(('size', local_var_params['size']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))

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

    def list_bandwidths_limit(self, request):
        r"""查看租户带宽限制

        获取EIP带宽限制列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListBandwidthsLimit
        :type request: :class:`huaweicloudsdkeip.v3.ListBandwidthsLimitRequest`
        :rtype: :class:`huaweicloudsdkeip.v3.ListBandwidthsLimitResponse`
        """
        http_info = self._list_bandwidths_limit_http_info(request)
        return self._call_api(**http_info)

    def list_bandwidths_limit_invoker(self, request):
        http_info = self._list_bandwidths_limit_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_bandwidths_limit_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/eip/eip-bandwidth-limits",
            "request_type": request.__class__.__name__,
            "response_type": "ListBandwidthsLimitResponse"
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
            collection_formats['fields'] = 'csv'
        if 'charge_mode' in local_var_params:
            query_params.append(('charge_mode', local_var_params['charge_mode']))

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

    def list_common_pools(self, request):
        r"""查询公共池列表

        查询公共池列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListCommonPools
        :type request: :class:`huaweicloudsdkeip.v3.ListCommonPoolsRequest`
        :rtype: :class:`huaweicloudsdkeip.v3.ListCommonPoolsResponse`
        """
        http_info = self._list_common_pools_http_info(request)
        return self._call_api(**http_info)

    def list_common_pools_invoker(self, request):
        http_info = self._list_common_pools_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_common_pools_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/eip/publicip-pools/common-pools",
            "request_type": request.__class__.__name__,
            "response_type": "ListCommonPoolsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'fields' in local_var_params:
            query_params.append(('fields', local_var_params['fields']))
            collection_formats['fields'] = 'multi'
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'public_border_group' in local_var_params:
            query_params.append(('public_border_group', local_var_params['public_border_group']))

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

    def list_eip_bandwidths(self, request):
        r"""查询带宽列表

        查询带宽列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListEipBandwidths
        :type request: :class:`huaweicloudsdkeip.v3.ListEipBandwidthsRequest`
        :rtype: :class:`huaweicloudsdkeip.v3.ListEipBandwidthsResponse`
        """
        http_info = self._list_eip_bandwidths_http_info(request)
        return self._call_api(**http_info)

    def list_eip_bandwidths_invoker(self, request):
        http_info = self._list_eip_bandwidths_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_eip_bandwidths_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/eip-bandwidths",
            "request_type": request.__class__.__name__,
            "response_type": "ListEipBandwidthsResponse"
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
        if 'fields' in local_var_params:
            query_params.append(('fields', local_var_params['fields']))
            collection_formats['fields'] = 'multi'
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'bandwidth_type' in local_var_params:
            query_params.append(('bandwidth_type', local_var_params['bandwidth_type']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'name_like' in local_var_params:
            query_params.append(('name_like', local_var_params['name_like']))
        if 'tenant_id' in local_var_params:
            query_params.append(('tenant_id', local_var_params['tenant_id']))
        if 'ingress_size' in local_var_params:
            query_params.append(('ingress_size', local_var_params['ingress_size']))
        if 'admin_state' in local_var_params:
            query_params.append(('admin_state', local_var_params['admin_state']))
        if 'billing_info' in local_var_params:
            query_params.append(('billing_info', local_var_params['billing_info']))
        if 'tags' in local_var_params:
            query_params.append(('tags', local_var_params['tags']))
        if 'enable_bandwidth_rules' in local_var_params:
            query_params.append(('enable_bandwidth_rules', local_var_params['enable_bandwidth_rules']))
        if 'rule_quota' in local_var_params:
            query_params.append(('rule_quota', local_var_params['rule_quota']))
        if 'public_border_group' in local_var_params:
            query_params.append(('public_border_group', local_var_params['public_border_group']))
        if 'charge_mode' in local_var_params:
            query_params.append(('charge_mode', local_var_params['charge_mode']))
        if 'size' in local_var_params:
            query_params.append(('size', local_var_params['size']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))

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

    def list_public_border_groups(self, request):
        r"""查询公共池分组列表

        查询公共池分组列表，包含名称和位置信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListPublicBorderGroups
        :type request: :class:`huaweicloudsdkeip.v3.ListPublicBorderGroupsRequest`
        :rtype: :class:`huaweicloudsdkeip.v3.ListPublicBorderGroupsResponse`
        """
        http_info = self._list_public_border_groups_http_info(request)
        return self._call_api(**http_info)

    def list_public_border_groups_invoker(self, request):
        http_info = self._list_public_border_groups_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_public_border_groups_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/eip/public-border-groups",
            "request_type": request.__class__.__name__,
            "response_type": "ListPublicBorderGroupsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'fields' in local_var_params:
            query_params.append(('fields', local_var_params['fields']))

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

    def list_publicip_pool(self, request):
        r"""查询公网IP池列表

        全量查询公网IP池列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListPublicipPool
        :type request: :class:`huaweicloudsdkeip.v3.ListPublicipPoolRequest`
        :rtype: :class:`huaweicloudsdkeip.v3.ListPublicipPoolResponse`
        """
        http_info = self._list_publicip_pool_http_info(request)
        return self._call_api(**http_info)

    def list_publicip_pool_invoker(self, request):
        http_info = self._list_publicip_pool_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_publicip_pool_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/eip/publicip-pools",
            "request_type": request.__class__.__name__,
            "response_type": "ListPublicipPoolResponse"
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
        if 'fields' in local_var_params:
            query_params.append(('fields', local_var_params['fields']))
            collection_formats['fields'] = 'multi'
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'size' in local_var_params:
            query_params.append(('size', local_var_params['size']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'description' in local_var_params:
            query_params.append(('description', local_var_params['description']))
        if 'public_border_group' in local_var_params:
            query_params.append(('public_border_group', local_var_params['public_border_group']))

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

    def list_share_bandwidth_types(self, request):
        r"""查询指定租户下的共享带宽类型列表

        查询指定租户下的共享带宽类型列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListShareBandwidthTypes
        :type request: :class:`huaweicloudsdkeip.v3.ListShareBandwidthTypesRequest`
        :rtype: :class:`huaweicloudsdkeip.v3.ListShareBandwidthTypesResponse`
        """
        http_info = self._list_share_bandwidth_types_http_info(request)
        return self._call_api(**http_info)

    def list_share_bandwidth_types_invoker(self, request):
        http_info = self._list_share_bandwidth_types_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_share_bandwidth_types_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/eip/share-bandwidth-types",
            "request_type": request.__class__.__name__,
            "response_type": "ListShareBandwidthTypesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'fields' in local_var_params:
            query_params.append(('fields', local_var_params['fields']))
            collection_formats['fields'] = 'multi'
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'bandwidth_type' in local_var_params:
            query_params.append(('bandwidth_type', local_var_params['bandwidth_type']))
        if 'name_en' in local_var_params:
            query_params.append(('name_en', local_var_params['name_en']))
        if 'name_zh' in local_var_params:
            query_params.append(('name_zh', local_var_params['name_zh']))
        if 'public_border_group' in local_var_params:
            query_params.append(('public_border_group', local_var_params['public_border_group']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
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

    def show_publicip_pool(self, request):
        r"""查询公网IP池详情

        查询公网IP池详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowPublicipPool
        :type request: :class:`huaweicloudsdkeip.v3.ShowPublicipPoolRequest`
        :rtype: :class:`huaweicloudsdkeip.v3.ShowPublicipPoolResponse`
        """
        http_info = self._show_publicip_pool_http_info(request)
        return self._call_api(**http_info)

    def show_publicip_pool_invoker(self, request):
        http_info = self._show_publicip_pool_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_publicip_pool_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/eip/publicip-pools/{publicip_pool_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowPublicipPoolResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'publicip_pool_id' in local_var_params:
            path_params['publicip_pool_id'] = local_var_params['publicip_pool_id']

        query_params = []
        if 'fields' in local_var_params:
            query_params.append(('fields', local_var_params['fields']))
            collection_formats['fields'] = 'multi'

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

    def list_project_geip_bindings(self, request):
        r"""查询GEIP与实例绑定关系的租户列表

        查询GEIP与实例绑定关系的租户列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListProjectGeipBindings
        :type request: :class:`huaweicloudsdkeip.v3.ListProjectGeipBindingsRequest`
        :rtype: :class:`huaweicloudsdkeip.v3.ListProjectGeipBindingsResponse`
        """
        http_info = self._list_project_geip_bindings_http_info(request)
        return self._call_api(**http_info)

    def list_project_geip_bindings_invoker(self, request):
        http_info = self._list_project_geip_bindings_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_project_geip_bindings_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/geip/bindings",
            "request_type": request.__class__.__name__,
            "response_type": "ListProjectGeipBindingsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'fields' in local_var_params:
            query_params.append(('fields', local_var_params['fields']))
            collection_formats['fields'] = 'multi'
        if 'geip_id' in local_var_params:
            query_params.append(('geip_id', local_var_params['geip_id']))
        if 'geip_ip_address' in local_var_params:
            query_params.append(('geip_ip_address', local_var_params['geip_ip_address']))
        if 'public_border_group' in local_var_params:
            query_params.append(('public_border_group', local_var_params['public_border_group']))
        if 'instance_type' in local_var_params:
            query_params.append(('instance_type', local_var_params['instance_type']))
        if 'instance_id' in local_var_params:
            query_params.append(('instance_id', local_var_params['instance_id']))
        if 'instance_vpc_id' in local_var_params:
            query_params.append(('instance_vpc_id', local_var_params['instance_vpc_id']))
        if 'gcbandwidth_id' in local_var_params:
            query_params.append(('gcbandwidth.id', local_var_params['gcbandwidth_id']))
        if 'gcbandwidth_admin_status' in local_var_params:
            query_params.append(('gcbandwidth.admin_status', local_var_params['gcbandwidth_admin_status']))
        if 'gcbandwidth_size' in local_var_params:
            query_params.append(('gcbandwidth.size', local_var_params['gcbandwidth_size']))
        if 'gcbandwidth_sla_level' in local_var_params:
            query_params.append(('gcbandwidth.sla_level', local_var_params['gcbandwidth_sla_level']))
        if 'gcbandwidth_dscp' in local_var_params:
            query_params.append(('gcbandwidth.dscp', local_var_params['gcbandwidth_dscp']))
        if 'vnic_private_ip_address' in local_var_params:
            query_params.append(('vnic.private_ip_address', local_var_params['vnic_private_ip_address']))
        if 'vnic_vpc_id' in local_var_params:
            query_params.append(('vnic.vpc_id', local_var_params['vnic_vpc_id']))
        if 'vnic_port_id' in local_var_params:
            query_params.append(('vnic.port_id', local_var_params['vnic_port_id']))
        if 'vnic_device_id' in local_var_params:
            query_params.append(('vnic.device_id', local_var_params['vnic_device_id']))
        if 'vnic_device_owner' in local_var_params:
            query_params.append(('vnic.device_owner', local_var_params['vnic_device_owner']))
        if 'vnic_device_owner_prefixlike' in local_var_params:
            query_params.append(('vnic.device_owner_prefixlike', local_var_params['vnic_device_owner_prefixlike']))
        if 'vnic_instance_type' in local_var_params:
            query_params.append(('vnic.instance_type', local_var_params['vnic_instance_type']))
        if 'vnic_instance_id' in local_var_params:
            query_params.append(('vnic.instance_id', local_var_params['vnic_instance_id']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
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

    def associate_publicips(self, request):
        r"""绑定弹性公网IP

        绑定弹性公网IP
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AssociatePublicips
        :type request: :class:`huaweicloudsdkeip.v3.AssociatePublicipsRequest`
        :rtype: :class:`huaweicloudsdkeip.v3.AssociatePublicipsResponse`
        """
        http_info = self._associate_publicips_http_info(request)
        return self._call_api(**http_info)

    def associate_publicips_invoker(self, request):
        http_info = self._associate_publicips_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _associate_publicips_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/eip/publicips/{publicip_id}/associate-instance",
            "request_type": request.__class__.__name__,
            "response_type": "AssociatePublicipsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'publicip_id' in local_var_params:
            path_params['publicip_id'] = local_var_params['publicip_id']

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

    def attach_batch_public_ip(self, request):
        r"""共享带宽批量加入弹性公网IP

        共享带宽批量加入弹性公网IP
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AttachBatchPublicIp
        :type request: :class:`huaweicloudsdkeip.v3.AttachBatchPublicIpRequest`
        :rtype: :class:`huaweicloudsdkeip.v3.AttachBatchPublicIpResponse`
        """
        http_info = self._attach_batch_public_ip_http_info(request)
        return self._call_api(**http_info)

    def attach_batch_public_ip_invoker(self, request):
        http_info = self._attach_batch_public_ip_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _attach_batch_public_ip_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/eip/publicips/attach-share-bandwidth",
            "request_type": request.__class__.__name__,
            "response_type": "AttachBatchPublicIpResponse"
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

    def attach_share_bandwidth(self, request):
        r"""共享带宽加入弹性公网IP

        共享带宽加入弹性公网IP
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AttachShareBandwidth
        :type request: :class:`huaweicloudsdkeip.v3.AttachShareBandwidthRequest`
        :rtype: :class:`huaweicloudsdkeip.v3.AttachShareBandwidthResponse`
        """
        http_info = self._attach_share_bandwidth_http_info(request)
        return self._call_api(**http_info)

    def attach_share_bandwidth_invoker(self, request):
        http_info = self._attach_share_bandwidth_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _attach_share_bandwidth_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/eip/publicips/{publicip_id}/attach-share-bandwidth",
            "request_type": request.__class__.__name__,
            "response_type": "AttachShareBandwidthResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'publicip_id' in local_var_params:
            path_params['publicip_id'] = local_var_params['publicip_id']

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

    def count_eip_available_resources(self, request):
        r"""查询弹性公网IP可用数

        IP池用于查询公网可用ip个数
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CountEipAvailableResources
        :type request: :class:`huaweicloudsdkeip.v3.CountEipAvailableResourcesRequest`
        :rtype: :class:`huaweicloudsdkeip.v3.CountEipAvailableResourcesResponse`
        """
        http_info = self._count_eip_available_resources_http_info(request)
        return self._call_api(**http_info)

    def count_eip_available_resources_invoker(self, request):
        http_info = self._count_eip_available_resources_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _count_eip_available_resources_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/eip/resources/available",
            "request_type": request.__class__.__name__,
            "response_type": "CountEipAvailableResourcesResponse"
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

    def detach_batch_public_ip(self, request):
        r"""共享带宽批量移出弹性公网IP

        共享带宽批量移出弹性公网IP
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DetachBatchPublicIp
        :type request: :class:`huaweicloudsdkeip.v3.DetachBatchPublicIpRequest`
        :rtype: :class:`huaweicloudsdkeip.v3.DetachBatchPublicIpResponse`
        """
        http_info = self._detach_batch_public_ip_http_info(request)
        return self._call_api(**http_info)

    def detach_batch_public_ip_invoker(self, request):
        http_info = self._detach_batch_public_ip_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _detach_batch_public_ip_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/eip/publicips/detach-share-bandwidth",
            "request_type": request.__class__.__name__,
            "response_type": "DetachBatchPublicIpResponse"
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

    def detach_share_bandwidth(self, request):
        r"""共享带宽移出弹性公网IP

        共享带宽移出弹性公网IP
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DetachShareBandwidth
        :type request: :class:`huaweicloudsdkeip.v3.DetachShareBandwidthRequest`
        :rtype: :class:`huaweicloudsdkeip.v3.DetachShareBandwidthResponse`
        """
        http_info = self._detach_share_bandwidth_http_info(request)
        return self._call_api(**http_info)

    def detach_share_bandwidth_invoker(self, request):
        http_info = self._detach_share_bandwidth_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _detach_share_bandwidth_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/eip/publicips/{publicip_id}/detach-share-bandwidth",
            "request_type": request.__class__.__name__,
            "response_type": "DetachShareBandwidthResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'publicip_id' in local_var_params:
            path_params['publicip_id'] = local_var_params['publicip_id']

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

    def disable_nat64(self, request):
        r"""弹性公网IP关闭NAT64

        弹性公网IP关闭NAT64
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DisableNat64
        :type request: :class:`huaweicloudsdkeip.v3.DisableNat64Request`
        :rtype: :class:`huaweicloudsdkeip.v3.DisableNat64Response`
        """
        http_info = self._disable_nat64_http_info(request)
        return self._call_api(**http_info)

    def disable_nat64_invoker(self, request):
        http_info = self._disable_nat64_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _disable_nat64_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/eip/publicips/{publicip_id}/disable-nat64",
            "request_type": request.__class__.__name__,
            "response_type": "DisableNat64Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'publicip_id' in local_var_params:
            path_params['publicip_id'] = local_var_params['publicip_id']

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

    def disassociate_publicips(self, request):
        r"""解绑弹性公网IP

        解绑弹性公网IP
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DisassociatePublicips
        :type request: :class:`huaweicloudsdkeip.v3.DisassociatePublicipsRequest`
        :rtype: :class:`huaweicloudsdkeip.v3.DisassociatePublicipsResponse`
        """
        http_info = self._disassociate_publicips_http_info(request)
        return self._call_api(**http_info)

    def disassociate_publicips_invoker(self, request):
        http_info = self._disassociate_publicips_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _disassociate_publicips_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/eip/publicips/{publicip_id}/disassociate-instance",
            "request_type": request.__class__.__name__,
            "response_type": "DisassociatePublicipsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'publicip_id' in local_var_params:
            path_params['publicip_id'] = local_var_params['publicip_id']

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

    def enable_nat64(self, request):
        r"""弹性公网IP开启NAT64

        弹性公网IP开启NAT64
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for EnableNat64
        :type request: :class:`huaweicloudsdkeip.v3.EnableNat64Request`
        :rtype: :class:`huaweicloudsdkeip.v3.EnableNat64Response`
        """
        http_info = self._enable_nat64_http_info(request)
        return self._call_api(**http_info)

    def enable_nat64_invoker(self, request):
        http_info = self._enable_nat64_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _enable_nat64_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/eip/publicips/{publicip_id}/enable-nat64",
            "request_type": request.__class__.__name__,
            "response_type": "EnableNat64Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'publicip_id' in local_var_params:
            path_params['publicip_id'] = local_var_params['publicip_id']

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

    def list_publicips(self, request):
        r"""全量查询弹性公网IP列表

        查询弹性公网IP列表信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListPublicips
        :type request: :class:`huaweicloudsdkeip.v3.ListPublicipsRequest`
        :rtype: :class:`huaweicloudsdkeip.v3.ListPublicipsResponse`
        """
        http_info = self._list_publicips_http_info(request)
        return self._call_api(**http_info)

    def list_publicips_invoker(self, request):
        http_info = self._list_publicips_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_publicips_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/eip/publicips",
            "request_type": request.__class__.__name__,
            "response_type": "ListPublicipsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'fields' in local_var_params:
            query_params.append(('fields', local_var_params['fields']))
            collection_formats['fields'] = 'multi'
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
            collection_formats['id'] = 'multi'
        if 'ip_version' in local_var_params:
            query_params.append(('ip_version', local_var_params['ip_version']))
            collection_formats['ip_version'] = 'multi'
        if 'public_ip_address' in local_var_params:
            query_params.append(('public_ip_address', local_var_params['public_ip_address']))
            collection_formats['public_ip_address'] = 'multi'
        if 'public_ip_address_like' in local_var_params:
            query_params.append(('public_ip_address_like', local_var_params['public_ip_address_like']))
        if 'public_ipv6_address' in local_var_params:
            query_params.append(('public_ipv6_address', local_var_params['public_ipv6_address']))
            collection_formats['public_ipv6_address'] = 'multi'
        if 'public_ipv6_address_like' in local_var_params:
            query_params.append(('public_ipv6_address_like', local_var_params['public_ipv6_address_like']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
            collection_formats['type'] = 'multi'
        if 'network_type' in local_var_params:
            query_params.append(('network_type', local_var_params['network_type']))
            collection_formats['network_type'] = 'multi'
        if 'publicip_pool_name' in local_var_params:
            query_params.append(('publicip_pool_name', local_var_params['publicip_pool_name']))
            collection_formats['publicip_pool_name'] = 'multi'
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
            collection_formats['status'] = 'multi'
        if 'alias_like' in local_var_params:
            query_params.append(('alias_like', local_var_params['alias_like']))
        if 'alias' in local_var_params:
            query_params.append(('alias', local_var_params['alias']))
            collection_formats['alias'] = 'multi'
        if 'description' in local_var_params:
            query_params.append(('description', local_var_params['description']))
            collection_formats['description'] = 'multi'
        if 'vnic_private_ip_address' in local_var_params:
            query_params.append(('vnic.private_ip_address', local_var_params['vnic_private_ip_address']))
            collection_formats['vnic.private_ip_address'] = 'multi'
        if 'vnic_private_ip_address_like' in local_var_params:
            query_params.append(('vnic.private_ip_address_like', local_var_params['vnic_private_ip_address_like']))
        if 'vnic_device_id' in local_var_params:
            query_params.append(('vnic.device_id', local_var_params['vnic_device_id']))
            collection_formats['vnic.device_id'] = 'multi'
        if 'vnic_device_owner' in local_var_params:
            query_params.append(('vnic.device_owner', local_var_params['vnic_device_owner']))
            collection_formats['vnic.device_owner'] = 'multi'
        if 'vnic_vpc_id' in local_var_params:
            query_params.append(('vnic.vpc_id', local_var_params['vnic_vpc_id']))
            collection_formats['vnic.vpc_id'] = 'multi'
        if 'vnic_port_id' in local_var_params:
            query_params.append(('vnic.port_id', local_var_params['vnic_port_id']))
            collection_formats['vnic.port_id'] = 'multi'
        if 'vnic_device_owner_prefixlike' in local_var_params:
            query_params.append(('vnic.device_owner_prefixlike', local_var_params['vnic_device_owner_prefixlike']))
        if 'vnic_instance_type' in local_var_params:
            query_params.append(('vnic.instance_type', local_var_params['vnic_instance_type']))
            collection_formats['vnic.instance_type'] = 'multi'
        if 'vnic_instance_id' in local_var_params:
            query_params.append(('vnic.instance_id', local_var_params['vnic_instance_id']))
            collection_formats['vnic.instance_id'] = 'multi'
        if 'bandwidth_id' in local_var_params:
            query_params.append(('bandwidth.id', local_var_params['bandwidth_id']))
            collection_formats['bandwidth.id'] = 'multi'
        if 'bandwidth_name' in local_var_params:
            query_params.append(('bandwidth.name', local_var_params['bandwidth_name']))
            collection_formats['bandwidth.name'] = 'multi'
        if 'bandwidth_name_like' in local_var_params:
            query_params.append(('bandwidth.name_like', local_var_params['bandwidth_name_like']))
            collection_formats['bandwidth.name_like'] = 'multi'
        if 'bandwidth_size' in local_var_params:
            query_params.append(('bandwidth.size', local_var_params['bandwidth_size']))
            collection_formats['bandwidth.size'] = 'multi'
        if 'bandwidth_share_type' in local_var_params:
            query_params.append(('bandwidth.share_type', local_var_params['bandwidth_share_type']))
            collection_formats['bandwidth.share_type'] = 'multi'
        if 'bandwidth_charge_mode' in local_var_params:
            query_params.append(('bandwidth.charge_mode', local_var_params['bandwidth_charge_mode']))
            collection_formats['bandwidth.charge_mode'] = 'multi'
        if 'billing_info' in local_var_params:
            query_params.append(('billing_info', local_var_params['billing_info']))
            collection_formats['billing_info'] = 'multi'
        if 'billing_mode' in local_var_params:
            query_params.append(('billing_mode', local_var_params['billing_mode']))
        if 'associate_instance_type' in local_var_params:
            query_params.append(('associate_instance_type', local_var_params['associate_instance_type']))
            collection_formats['associate_instance_type'] = 'multi'
        if 'associate_instance_id' in local_var_params:
            query_params.append(('associate_instance_id', local_var_params['associate_instance_id']))
            collection_formats['associate_instance_id'] = 'multi'
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
            collection_formats['enterprise_project_id'] = 'multi'
        if 'public_border_group' in local_var_params:
            query_params.append(('public_border_group', local_var_params['public_border_group']))
            collection_formats['public_border_group'] = 'multi'
        if 'allow_share_bandwidth_type_any' in local_var_params:
            query_params.append(('allow_share_bandwidth_type_any', local_var_params['allow_share_bandwidth_type_any']))
            collection_formats['allow_share_bandwidth_type_any'] = 'multi'

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

    def show_publicip(self, request):
        r"""查询弹性公网IP详情

        查询弹性公网IP详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowPublicip
        :type request: :class:`huaweicloudsdkeip.v3.ShowPublicipRequest`
        :rtype: :class:`huaweicloudsdkeip.v3.ShowPublicipResponse`
        """
        http_info = self._show_publicip_http_info(request)
        return self._call_api(**http_info)

    def show_publicip_invoker(self, request):
        http_info = self._show_publicip_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_publicip_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/eip/publicips/{publicip_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowPublicipResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'publicip_id' in local_var_params:
            path_params['publicip_id'] = local_var_params['publicip_id']

        query_params = []
        if 'fields' in local_var_params:
            query_params.append(('fields', local_var_params['fields']))
            collection_formats['fields'] = 'csv'

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

    def update_publicip(self, request):
        r"""更新弹性公网IP

        更新弹性公网IP
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdatePublicip
        :type request: :class:`huaweicloudsdkeip.v3.UpdatePublicipRequest`
        :rtype: :class:`huaweicloudsdkeip.v3.UpdatePublicipResponse`
        """
        http_info = self._update_publicip_http_info(request)
        return self._call_api(**http_info)

    def update_publicip_invoker(self, request):
        http_info = self._update_publicip_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_publicip_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/eip/publicips/{publicip_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdatePublicipResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'publicip_id' in local_var_params:
            path_params['publicip_id'] = local_var_params['publicip_id']

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

    def create_tenant_vpc_igw(self, request):
        r"""创建虚拟igw

        创建虚拟igw
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateTenantVpcIgw
        :type request: :class:`huaweicloudsdkeip.v3.CreateTenantVpcIgwRequest`
        :rtype: :class:`huaweicloudsdkeip.v3.CreateTenantVpcIgwResponse`
        """
        http_info = self._create_tenant_vpc_igw_http_info(request)
        return self._call_api(**http_info)

    def create_tenant_vpc_igw_invoker(self, request):
        http_info = self._create_tenant_vpc_igw_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_tenant_vpc_igw_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/geip/vpc-igws",
            "request_type": request.__class__.__name__,
            "response_type": "CreateTenantVpcIgwResponse"
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

    def delete_tenant_vpc_igw(self, request):
        r"""删除虚拟igw

        删除虚拟igw
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteTenantVpcIgw
        :type request: :class:`huaweicloudsdkeip.v3.DeleteTenantVpcIgwRequest`
        :rtype: :class:`huaweicloudsdkeip.v3.DeleteTenantVpcIgwResponse`
        """
        http_info = self._delete_tenant_vpc_igw_http_info(request)
        return self._call_api(**http_info)

    def delete_tenant_vpc_igw_invoker(self, request):
        http_info = self._delete_tenant_vpc_igw_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_tenant_vpc_igw_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{project_id}/geip/vpc-igws/{vpc_igw_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteTenantVpcIgwResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'vpc_igw_id' in local_var_params:
            path_params['vpc_igw_id'] = local_var_params['vpc_igw_id']

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

    def list_tenant_vpc_igws(self, request):
        r"""查询指定租户下的虚拟igw列表

        查询指定租户下的虚拟igw列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListTenantVpcIgws
        :type request: :class:`huaweicloudsdkeip.v3.ListTenantVpcIgwsRequest`
        :rtype: :class:`huaweicloudsdkeip.v3.ListTenantVpcIgwsResponse`
        """
        http_info = self._list_tenant_vpc_igws_http_info(request)
        return self._call_api(**http_info)

    def list_tenant_vpc_igws_invoker(self, request):
        http_info = self._list_tenant_vpc_igws_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_tenant_vpc_igws_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/geip/vpc-igws",
            "request_type": request.__class__.__name__,
            "response_type": "ListTenantVpcIgwsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'fields' in local_var_params:
            query_params.append(('fields', local_var_params['fields']))
            collection_formats['fields'] = 'multi'
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'vpc_id' in local_var_params:
            query_params.append(('vpc_id', local_var_params['vpc_id']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
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

    def show_internal_vpc_igw(self, request):
        r"""查询虚拟igw详情

        查询虚拟igw详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowInternalVpcIgw
        :type request: :class:`huaweicloudsdkeip.v3.ShowInternalVpcIgwRequest`
        :rtype: :class:`huaweicloudsdkeip.v3.ShowInternalVpcIgwResponse`
        """
        http_info = self._show_internal_vpc_igw_http_info(request)
        return self._call_api(**http_info)

    def show_internal_vpc_igw_invoker(self, request):
        http_info = self._show_internal_vpc_igw_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_internal_vpc_igw_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/geip/vpc-igws/{vpc_igw_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowInternalVpcIgwResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'vpc_igw_id' in local_var_params:
            path_params['vpc_igw_id'] = local_var_params['vpc_igw_id']

        query_params = []
        if 'fields' in local_var_params:
            query_params.append(('fields', local_var_params['fields']))
            collection_formats['fields'] = 'multi'

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

    def update_tenant_vpc_igw(self, request):
        r"""修改虚拟igw

        修改虚拟igw
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateTenantVpcIgw
        :type request: :class:`huaweicloudsdkeip.v3.UpdateTenantVpcIgwRequest`
        :rtype: :class:`huaweicloudsdkeip.v3.UpdateTenantVpcIgwResponse`
        """
        http_info = self._update_tenant_vpc_igw_http_info(request)
        return self._call_api(**http_info)

    def update_tenant_vpc_igw_invoker(self, request):
        http_info = self._update_tenant_vpc_igw_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_tenant_vpc_igw_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/geip/vpc-igws/{vpc_igw_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateTenantVpcIgwResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'vpc_igw_id' in local_var_params:
            path_params['vpc_igw_id'] = local_var_params['vpc_igw_id']

        query_params = []
        if 'fields' in local_var_params:
            query_params.append(('fields', local_var_params['fields']))
            collection_formats['fields'] = 'multi'

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

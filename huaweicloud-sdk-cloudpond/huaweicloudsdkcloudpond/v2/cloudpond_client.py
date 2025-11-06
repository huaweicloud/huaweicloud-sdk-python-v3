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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkcloudpond'")


class CloudPondClient(Client):
    def __init__(self):
        super().__init__()
        self.model_package = importlib.import_module("huaweicloudsdkcloudpond.v2.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls, "GlobalCredentials")
        else:
            if clazz.__name__ != "CloudPondClient":
                raise TypeError("client type error, support client type is CloudPondClient")
            client_builder = ClientBuilder(clazz, "GlobalCredentials")

        

        return client_builder

    def list_network_devices(self, request):
        r"""查询网络设备列表

        查询网络设备列表。
        [- 该接口支持企业项目细粒度权限的校验，具体细粒度请参见 ies:edgeSite:listNetworkDevices](tag:hws)
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListNetworkDevices
        :type request: :class:`huaweicloudsdkcloudpond.v2.ListNetworkDevicesRequest`
        :rtype: :class:`huaweicloudsdkcloudpond.v2.ListNetworkDevicesResponse`
        """
        http_info = self._list_network_devices_http_info(request)
        return self._call_api(**http_info)

    def list_network_devices_invoker(self, request):
        http_info = self._list_network_devices_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_network_devices_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{domain_id}/network-devices",
            "request_type": request.__class__.__name__,
            "response_type": "ListNetworkDevicesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'edge_site_id' in local_var_params:
            query_params.append(('edge_site_id', local_var_params['edge_site_id']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
            collection_formats['status'] = 'multi'
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
            collection_formats['id'] = 'multi'

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

    def show_network_device(self, request):
        r"""查询网络设备详情

        查询网络设备详情。
        [- 该接口支持企业项目细粒度权限的校验，具体细粒度请参见 ies:edgeSite:getNetworkDevice](tag:hws)
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowNetworkDevice
        :type request: :class:`huaweicloudsdkcloudpond.v2.ShowNetworkDeviceRequest`
        :rtype: :class:`huaweicloudsdkcloudpond.v2.ShowNetworkDeviceResponse`
        """
        http_info = self._show_network_device_http_info(request)
        return self._call_api(**http_info)

    def show_network_device_invoker(self, request):
        http_info = self._show_network_device_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_network_device_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{domain_id}/network-devices/{network_device_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowNetworkDeviceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'network_device_id' in local_var_params:
            path_params['network_device_id'] = local_var_params['network_device_id']

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

    def list_network_device_offerings(self, request):
        r"""查询网络设备商品列表

        查询网络设备商品列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListNetworkDeviceOfferings
        :type request: :class:`huaweicloudsdkcloudpond.v2.ListNetworkDeviceOfferingsRequest`
        :rtype: :class:`huaweicloudsdkcloudpond.v2.ListNetworkDeviceOfferingsResponse`
        """
        http_info = self._list_network_device_offerings_http_info(request)
        return self._call_api(**http_info)

    def list_network_device_offerings_invoker(self, request):
        http_info = self._list_network_device_offerings_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_network_device_offerings_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{domain_id}/network-device-offerings",
            "request_type": request.__class__.__name__,
            "response_type": "ListNetworkDeviceOfferingsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'zone_code' in local_var_params:
            query_params.append(('zone_code', local_var_params['zone_code']))
        if 'storage_type' in local_var_params:
            query_params.append(('storage_type', local_var_params['storage_type']))
            collection_formats['storage_type'] = 'multi'
        if 'pay_mode' in local_var_params:
            query_params.append(('pay_mode', local_var_params['pay_mode']))
            collection_formats['pay_mode'] = 'multi'
        if 'period_num' in local_var_params:
            query_params.append(('period_num', local_var_params['period_num']))
            collection_formats['period_num'] = 'multi'
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

    def list_server_offerings(self, request):
        r"""查询服务器商品列表

        查询服务器销售商品列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListServerOfferings
        :type request: :class:`huaweicloudsdkcloudpond.v2.ListServerOfferingsRequest`
        :rtype: :class:`huaweicloudsdkcloudpond.v2.ListServerOfferingsResponse`
        """
        http_info = self._list_server_offerings_http_info(request)
        return self._call_api(**http_info)

    def list_server_offerings_invoker(self, request):
        http_info = self._list_server_offerings_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_server_offerings_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{domain_id}/server-offerings",
            "request_type": request.__class__.__name__,
            "response_type": "ListServerOfferingsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'zone_code' in local_var_params:
            query_params.append(('zone_code', local_var_params['zone_code']))
        if 'pay_mode' in local_var_params:
            query_params.append(('pay_mode', local_var_params['pay_mode']))
            collection_formats['pay_mode'] = 'multi'
        if 'period_num' in local_var_params:
            query_params.append(('period_num', local_var_params['period_num']))
            collection_formats['period_num'] = 'multi'
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

    def list_sale_cycles(self, request):
        r"""查询可购买的销售周期

        查询可购买的销售周期
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListSaleCycles
        :type request: :class:`huaweicloudsdkcloudpond.v2.ListSaleCyclesRequest`
        :rtype: :class:`huaweicloudsdkcloudpond.v2.ListSaleCyclesResponse`
        """
        http_info = self._list_sale_cycles_http_info(request)
        return self._call_api(**http_info)

    def list_sale_cycles_invoker(self, request):
        http_info = self._list_sale_cycles_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_sale_cycles_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{domain_id}/sale-cycles",
            "request_type": request.__class__.__name__,
            "response_type": "ListSaleCyclesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'zone_code' in local_var_params:
            query_params.append(('zone_code', local_var_params['zone_code']))

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

    def list_servers(self, request):
        r"""查询服务器列表

        查询服务器列表。
        [- 该接口支持企业项目细粒度权限的校验，具体细粒度请参见 ies:edgeSite:listServers](tag:hws)
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListServers
        :type request: :class:`huaweicloudsdkcloudpond.v2.ListServersRequest`
        :rtype: :class:`huaweicloudsdkcloudpond.v2.ListServersResponse`
        """
        http_info = self._list_servers_http_info(request)
        return self._call_api(**http_info)

    def list_servers_invoker(self, request):
        http_info = self._list_servers_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_servers_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{domain_id}/servers",
            "request_type": request.__class__.__name__,
            "response_type": "ListServersResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'edge_site_id' in local_var_params:
            query_params.append(('edge_site_id', local_var_params['edge_site_id']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
            collection_formats['status'] = 'multi'
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
            collection_formats['id'] = 'multi'

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

    def show_server(self, request):
        r"""查询服务器详情

        查询服务器详情。
        [- 该接口支持企业项目细粒度权限的校验，具体细粒度请参见 ies:edgeSite:getServer](tag:hws)
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowServer
        :type request: :class:`huaweicloudsdkcloudpond.v2.ShowServerRequest`
        :rtype: :class:`huaweicloudsdkcloudpond.v2.ShowServerResponse`
        """
        http_info = self._show_server_http_info(request)
        return self._call_api(**http_info)

    def show_server_invoker(self, request):
        http_info = self._show_server_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_server_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{domain_id}/servers/{server_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowServerResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'server_id' in local_var_params:
            path_params['server_id'] = local_var_params['server_id']

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

    def list_storage_gears(self, request):
        r"""查询存储计费档位

        该接口仅返回支持的存储计费档位，实际可购买的存储容量单独定义。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListStorageGears
        :type request: :class:`huaweicloudsdkcloudpond.v2.ListStorageGearsRequest`
        :rtype: :class:`huaweicloudsdkcloudpond.v2.ListStorageGearsResponse`
        """
        http_info = self._list_storage_gears_http_info(request)
        return self._call_api(**http_info)

    def list_storage_gears_invoker(self, request):
        http_info = self._list_storage_gears_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_storage_gears_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{domain_id}/storage-gears",
            "request_type": request.__class__.__name__,
            "response_type": "ListStorageGearsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'zone_code' in local_var_params:
            query_params.append(('zone_code', local_var_params['zone_code']))
        if 'pay_mode' in local_var_params:
            query_params.append(('pay_mode', local_var_params['pay_mode']))
            collection_formats['pay_mode'] = 'multi'
        if 'period_num' in local_var_params:
            query_params.append(('period_num', local_var_params['period_num']))
            collection_formats['period_num'] = 'multi'
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

    def list_storage_pools(self, request):
        r"""查询存储池列表

        查询存储池列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListStoragePools
        :type request: :class:`huaweicloudsdkcloudpond.v2.ListStoragePoolsRequest`
        :rtype: :class:`huaweicloudsdkcloudpond.v2.ListStoragePoolsResponse`
        """
        http_info = self._list_storage_pools_http_info(request)
        return self._call_api(**http_info)

    def list_storage_pools_invoker(self, request):
        http_info = self._list_storage_pools_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_storage_pools_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{domain_id}/storage-pools",
            "request_type": request.__class__.__name__,
            "response_type": "ListStoragePoolsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'edge_site_id' in local_var_params:
            query_params.append(('edge_site_id', local_var_params['edge_site_id']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
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

    def show_storage_pool(self, request):
        r"""查询存储池详情

        查询存储池详情。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowStoragePool
        :type request: :class:`huaweicloudsdkcloudpond.v2.ShowStoragePoolRequest`
        :rtype: :class:`huaweicloudsdkcloudpond.v2.ShowStoragePoolResponse`
        """
        http_info = self._show_storage_pool_http_info(request)
        return self._call_api(**http_info)

    def show_storage_pool_invoker(self, request):
        http_info = self._show_storage_pool_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_storage_pool_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{domain_id}/storage-pools/{id}",
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

    def list_storage_types(self, request):
        r"""查询存储类型列表

        查询支持的存储类型列表，包括步长等信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListStorageTypes
        :type request: :class:`huaweicloudsdkcloudpond.v2.ListStorageTypesRequest`
        :rtype: :class:`huaweicloudsdkcloudpond.v2.ListStorageTypesResponse`
        """
        http_info = self._list_storage_types_http_info(request)
        return self._call_api(**http_info)

    def list_storage_types_invoker(self, request):
        http_info = self._list_storage_types_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_storage_types_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{domain_id}/storage-types",
            "request_type": request.__class__.__name__,
            "response_type": "ListStorageTypesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'zone_code' in local_var_params:
            query_params.append(('zone_code', local_var_params['zone_code']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
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

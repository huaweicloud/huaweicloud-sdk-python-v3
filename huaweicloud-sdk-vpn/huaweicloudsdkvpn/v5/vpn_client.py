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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkvpn'")


class VpnClient(Client):
    def __init__(self):
        super(VpnClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkvpn.v5.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "VpnClient":
                raise TypeError("client type error, support client type is VpnClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def create_cgw(self, request):
        """创建对端网关

        创建租户用于与VPN网关相连的对端网关
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateCgw
        :type request: :class:`huaweicloudsdkvpn.v5.CreateCgwRequest`
        :rtype: :class:`huaweicloudsdkvpn.v5.CreateCgwResponse`
        """
        http_info = self._create_cgw_http_info(request)
        return self._call_api(**http_info)

    def create_cgw_invoker(self, request):
        http_info = self._create_cgw_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_cgw_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/{project_id}/customer-gateways",
            "request_type": request.__class__.__name__,
            "response_type": "CreateCgwResponse"
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

        response_headers = ["header-response-token", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_cgw(self, request):
        """删除对端网关

        根据对端网关ID，删除指定的对端网关
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteCgw
        :type request: :class:`huaweicloudsdkvpn.v5.DeleteCgwRequest`
        :rtype: :class:`huaweicloudsdkvpn.v5.DeleteCgwResponse`
        """
        http_info = self._delete_cgw_http_info(request)
        return self._call_api(**http_info)

    def delete_cgw_invoker(self, request):
        http_info = self._delete_cgw_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_cgw_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v5/{project_id}/customer-gateways/{customer_gateway_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteCgwResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'customer_gateway_id' in local_var_params:
            path_params['customer_gateway_id'] = local_var_params['customer_gateway_id']

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

    def list_cgws(self, request):
        """查询对端网关列表

        查询对端网关列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListCgws
        :type request: :class:`huaweicloudsdkvpn.v5.ListCgwsRequest`
        :rtype: :class:`huaweicloudsdkvpn.v5.ListCgwsResponse`
        """
        http_info = self._list_cgws_http_info(request)
        return self._call_api(**http_info)

    def list_cgws_invoker(self, request):
        http_info = self._list_cgws_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_cgws_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/customer-gateways",
            "request_type": request.__class__.__name__,
            "response_type": "ListCgwsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'cgw_id' in local_var_params:
            query_params.append(('cgw_id', local_var_params['cgw_id']))
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

    def show_cgw(self, request):
        """查询对端网关

        根据对端网关ID，查询指定的对端网关
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowCgw
        :type request: :class:`huaweicloudsdkvpn.v5.ShowCgwRequest`
        :rtype: :class:`huaweicloudsdkvpn.v5.ShowCgwResponse`
        """
        http_info = self._show_cgw_http_info(request)
        return self._call_api(**http_info)

    def show_cgw_invoker(self, request):
        http_info = self._show_cgw_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_cgw_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/customer-gateways/{customer_gateway_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowCgwResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'customer_gateway_id' in local_var_params:
            path_params['customer_gateway_id'] = local_var_params['customer_gateway_id']

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

    def update_cgw(self, request):
        """更新对端网关

        根据对端网关ID，更新指定的对端网关
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateCgw
        :type request: :class:`huaweicloudsdkvpn.v5.UpdateCgwRequest`
        :rtype: :class:`huaweicloudsdkvpn.v5.UpdateCgwResponse`
        """
        http_info = self._update_cgw_http_info(request)
        return self._call_api(**http_info)

    def update_cgw_invoker(self, request):
        http_info = self._update_cgw_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_cgw_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v5/{project_id}/customer-gateways/{customer_gateway_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateCgwResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'customer_gateway_id' in local_var_params:
            path_params['customer_gateway_id'] = local_var_params['customer_gateway_id']

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

    def create_vpn_connection(self, request):
        """创建VPN连接

        创建VPN连接，连接VPN网关与对端网关
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateVpnConnection
        :type request: :class:`huaweicloudsdkvpn.v5.CreateVpnConnectionRequest`
        :rtype: :class:`huaweicloudsdkvpn.v5.CreateVpnConnectionResponse`
        """
        http_info = self._create_vpn_connection_http_info(request)
        return self._call_api(**http_info)

    def create_vpn_connection_invoker(self, request):
        http_info = self._create_vpn_connection_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_vpn_connection_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/{project_id}/vpn-connection",
            "request_type": request.__class__.__name__,
            "response_type": "CreateVpnConnectionResponse"
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

        response_headers = ["header-response-token", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_vpn_connection(self, request):
        """删除VPN连接

        根据连接ID，删除指定的VPN连接
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteVpnConnection
        :type request: :class:`huaweicloudsdkvpn.v5.DeleteVpnConnectionRequest`
        :rtype: :class:`huaweicloudsdkvpn.v5.DeleteVpnConnectionResponse`
        """
        http_info = self._delete_vpn_connection_http_info(request)
        return self._call_api(**http_info)

    def delete_vpn_connection_invoker(self, request):
        http_info = self._delete_vpn_connection_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_vpn_connection_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v5/{project_id}/vpn-connection/{vpn_connection_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteVpnConnectionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'vpn_connection_id' in local_var_params:
            path_params['vpn_connection_id'] = local_var_params['vpn_connection_id']

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

    def list_vpn_connections(self, request):
        """查询VPN连接列表

        查询VPN连接列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListVpnConnections
        :type request: :class:`huaweicloudsdkvpn.v5.ListVpnConnectionsRequest`
        :rtype: :class:`huaweicloudsdkvpn.v5.ListVpnConnectionsResponse`
        """
        http_info = self._list_vpn_connections_http_info(request)
        return self._call_api(**http_info)

    def list_vpn_connections_invoker(self, request):
        http_info = self._list_vpn_connections_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_vpn_connections_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/vpn-connection",
            "request_type": request.__class__.__name__,
            "response_type": "ListVpnConnectionsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'vpn_id' in local_var_params:
            query_params.append(('vpn_id', local_var_params['vpn_id']))
        if 'eip_id' in local_var_params:
            query_params.append(('eip_id', local_var_params['eip_id']))
        if 'vgw_ip' in local_var_params:
            query_params.append(('vgw_ip', local_var_params['vgw_ip']))
        if 'vgw_id' in local_var_params:
            query_params.append(('vgw_id', local_var_params['vgw_id']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
            collection_formats['enterprise_project_id'] = 'multi'
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["header-response-token", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_vpn_connection(self, request):
        """查询VPN连接

        根据连接ID，查询指定的VPN连接的参数
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowVpnConnection
        :type request: :class:`huaweicloudsdkvpn.v5.ShowVpnConnectionRequest`
        :rtype: :class:`huaweicloudsdkvpn.v5.ShowVpnConnectionResponse`
        """
        http_info = self._show_vpn_connection_http_info(request)
        return self._call_api(**http_info)

    def show_vpn_connection_invoker(self, request):
        http_info = self._show_vpn_connection_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_vpn_connection_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/vpn-connection/{vpn_connection_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowVpnConnectionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'vpn_connection_id' in local_var_params:
            path_params['vpn_connection_id'] = local_var_params['vpn_connection_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["header-response-token", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_vpn_connection(self, request):
        """更新VPN连接

        根据连接ID，更新指定的VPN连接的参数
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateVpnConnection
        :type request: :class:`huaweicloudsdkvpn.v5.UpdateVpnConnectionRequest`
        :rtype: :class:`huaweicloudsdkvpn.v5.UpdateVpnConnectionResponse`
        """
        http_info = self._update_vpn_connection_http_info(request)
        return self._call_api(**http_info)

    def update_vpn_connection_invoker(self, request):
        http_info = self._update_vpn_connection_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_vpn_connection_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v5/{project_id}/vpn-connection/{vpn_connection_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateVpnConnectionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'vpn_connection_id' in local_var_params:
            path_params['vpn_connection_id'] = local_var_params['vpn_connection_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["header-response-token", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_vgw(self, request):
        """创建VPN网关

        创建一个VPN网关
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateVgw
        :type request: :class:`huaweicloudsdkvpn.v5.CreateVgwRequest`
        :rtype: :class:`huaweicloudsdkvpn.v5.CreateVgwResponse`
        """
        http_info = self._create_vgw_http_info(request)
        return self._call_api(**http_info)

    def create_vgw_invoker(self, request):
        http_info = self._create_vgw_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_vgw_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/{project_id}/vpn-gateways",
            "request_type": request.__class__.__name__,
            "response_type": "CreateVgwResponse"
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

        response_headers = ["header-response-token", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_vgw(self, request):
        """删除VPN网关

        根据VPN网关ID，删除指定的VPN网关
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteVgw
        :type request: :class:`huaweicloudsdkvpn.v5.DeleteVgwRequest`
        :rtype: :class:`huaweicloudsdkvpn.v5.DeleteVgwResponse`
        """
        http_info = self._delete_vgw_http_info(request)
        return self._call_api(**http_info)

    def delete_vgw_invoker(self, request):
        http_info = self._delete_vgw_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_vgw_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v5/{project_id}/vpn-gateways/{vgw_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteVgwResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'vgw_id' in local_var_params:
            path_params['vgw_id'] = local_var_params['vgw_id']

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

    def list_availability_zones(self, request):
        """查询VPN网关可用区

        查询VPN网关可用区
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAvailabilityZones
        :type request: :class:`huaweicloudsdkvpn.v5.ListAvailabilityZonesRequest`
        :rtype: :class:`huaweicloudsdkvpn.v5.ListAvailabilityZonesResponse`
        """
        http_info = self._list_availability_zones_http_info(request)
        return self._call_api(**http_info)

    def list_availability_zones_invoker(self, request):
        http_info = self._list_availability_zones_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_availability_zones_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/vpn-gateways/availability-zones",
            "request_type": request.__class__.__name__,
            "response_type": "ListAvailabilityZonesResponse"
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

    def list_vgws(self, request):
        """查询VPN网关列表

        查询VPN网关列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListVgws
        :type request: :class:`huaweicloudsdkvpn.v5.ListVgwsRequest`
        :rtype: :class:`huaweicloudsdkvpn.v5.ListVgwsResponse`
        """
        http_info = self._list_vgws_http_info(request)
        return self._call_api(**http_info)

    def list_vgws_invoker(self, request):
        http_info = self._list_vgws_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_vgws_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/vpn-gateways",
            "request_type": request.__class__.__name__,
            "response_type": "ListVgwsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'vgw_id' in local_var_params:
            query_params.append(('vgw_id', local_var_params['vgw_id']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
            collection_formats['enterprise_project_id'] = 'multi'

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

    def show_vgw(self, request):
        """查询VPN网关

        根据VPN网关ID，查询指定的VPN网关
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowVgw
        :type request: :class:`huaweicloudsdkvpn.v5.ShowVgwRequest`
        :rtype: :class:`huaweicloudsdkvpn.v5.ShowVgwResponse`
        """
        http_info = self._show_vgw_http_info(request)
        return self._call_api(**http_info)

    def show_vgw_invoker(self, request):
        http_info = self._show_vgw_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_vgw_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/vpn-gateways/{vgw_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowVgwResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'vgw_id' in local_var_params:
            path_params['vgw_id'] = local_var_params['vgw_id']

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

    def update_vgw(self, request):
        """更新VPN网关

        根据VPN网关ID，更新指定的VPN网关
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateVgw
        :type request: :class:`huaweicloudsdkvpn.v5.UpdateVgwRequest`
        :rtype: :class:`huaweicloudsdkvpn.v5.UpdateVgwResponse`
        """
        http_info = self._update_vgw_http_info(request)
        return self._call_api(**http_info)

    def update_vgw_invoker(self, request):
        http_info = self._update_vgw_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_vgw_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v5/{project_id}/vpn-gateways/{vgw_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateVgwResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'vgw_id' in local_var_params:
            path_params['vgw_id'] = local_var_params['vgw_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["header-response-token", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_vgw_certificate(self, request):
        """导入VPN网关证书

        导入租户VPN网关所使用的证书，包括签名证书、签名私钥、加密证书、加密私钥和CA证书链。当前只支持国密证书
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateVgwCertificate
        :type request: :class:`huaweicloudsdkvpn.v5.CreateVgwCertificateRequest`
        :rtype: :class:`huaweicloudsdkvpn.v5.CreateVgwCertificateResponse`
        """
        http_info = self._create_vgw_certificate_http_info(request)
        return self._call_api(**http_info)

    def create_vgw_certificate_invoker(self, request):
        http_info = self._create_vgw_certificate_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_vgw_certificate_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/{project_id}/vpn-gateways/{vgw_id}/certificate",
            "request_type": request.__class__.__name__,
            "response_type": "CreateVgwCertificateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'vgw_id' in local_var_params:
            path_params['vgw_id'] = local_var_params['vgw_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["header-response-token", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_vpn_gateway_certificate(self, request):
        """查询VPN网关证书

        根据VPN网关ID，查询所指定的VPN网关证书
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowVpnGatewayCertificate
        :type request: :class:`huaweicloudsdkvpn.v5.ShowVpnGatewayCertificateRequest`
        :rtype: :class:`huaweicloudsdkvpn.v5.ShowVpnGatewayCertificateResponse`
        """
        http_info = self._show_vpn_gateway_certificate_http_info(request)
        return self._call_api(**http_info)

    def show_vpn_gateway_certificate_invoker(self, request):
        http_info = self._show_vpn_gateway_certificate_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_vpn_gateway_certificate_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/vpn-gateways/{vgw_id}/certificate",
            "request_type": request.__class__.__name__,
            "response_type": "ShowVpnGatewayCertificateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'vgw_id' in local_var_params:
            path_params['vgw_id'] = local_var_params['vgw_id']

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

    def update_vgw_certificate(self, request):
        """更新VPN网关证书

        更新租户VPN网关所使用的证书，包括签名证书、签名私钥、加密证书、加密私钥和CA证书链。当前只支持国密证书
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateVgwCertificate
        :type request: :class:`huaweicloudsdkvpn.v5.UpdateVgwCertificateRequest`
        :rtype: :class:`huaweicloudsdkvpn.v5.UpdateVgwCertificateResponse`
        """
        http_info = self._update_vgw_certificate_http_info(request)
        return self._call_api(**http_info)

    def update_vgw_certificate_invoker(self, request):
        http_info = self._update_vgw_certificate_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_vgw_certificate_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v5/{project_id}/vpn-gateways/{vgw_id}/certificate/{certificate_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateVgwCertificateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'vgw_id' in local_var_params:
            path_params['vgw_id'] = local_var_params['vgw_id']
        if 'certificate_id' in local_var_params:
            path_params['certificate_id'] = local_var_params['certificate_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["header-response-token", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_quotas_info(self, request):
        """查询指定租户配额

        查询指定租户的配额
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowQuotasInfo
        :type request: :class:`huaweicloudsdkvpn.v5.ShowQuotasInfoRequest`
        :rtype: :class:`huaweicloudsdkvpn.v5.ShowQuotasInfoResponse`
        """
        http_info = self._show_quotas_info_http_info(request)
        return self._call_api(**http_info)

    def show_quotas_info_invoker(self, request):
        http_info = self._show_quotas_info_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_quotas_info_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/vpn/quotas",
            "request_type": request.__class__.__name__,
            "response_type": "ShowQuotasInfoResponse"
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

    def create_connection_monitor(self, request):
        """创建VPN连接监控

        创建VPN连接监控
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateConnectionMonitor
        :type request: :class:`huaweicloudsdkvpn.v5.CreateConnectionMonitorRequest`
        :rtype: :class:`huaweicloudsdkvpn.v5.CreateConnectionMonitorResponse`
        """
        http_info = self._create_connection_monitor_http_info(request)
        return self._call_api(**http_info)

    def create_connection_monitor_invoker(self, request):
        http_info = self._create_connection_monitor_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_connection_monitor_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/{project_id}/connection-monitors",
            "request_type": request.__class__.__name__,
            "response_type": "CreateConnectionMonitorResponse"
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

        response_headers = ["header-response-token", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_connection_monitor(self, request):
        """删除VPN连接监控

        根据VPN连接监控的ID，删除指定的VPN连接监控
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteConnectionMonitor
        :type request: :class:`huaweicloudsdkvpn.v5.DeleteConnectionMonitorRequest`
        :rtype: :class:`huaweicloudsdkvpn.v5.DeleteConnectionMonitorResponse`
        """
        http_info = self._delete_connection_monitor_http_info(request)
        return self._call_api(**http_info)

    def delete_connection_monitor_invoker(self, request):
        http_info = self._delete_connection_monitor_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_connection_monitor_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v5/{project_id}/connection-monitors/{connection_monitor_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteConnectionMonitorResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'connection_monitor_id' in local_var_params:
            path_params['connection_monitor_id'] = local_var_params['connection_monitor_id']

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

    def list_connection_monitors(self, request):
        """查询VPN连接监控列表

        查询VPN连接监控列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListConnectionMonitors
        :type request: :class:`huaweicloudsdkvpn.v5.ListConnectionMonitorsRequest`
        :rtype: :class:`huaweicloudsdkvpn.v5.ListConnectionMonitorsResponse`
        """
        http_info = self._list_connection_monitors_http_info(request)
        return self._call_api(**http_info)

    def list_connection_monitors_invoker(self, request):
        http_info = self._list_connection_monitors_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_connection_monitors_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/connection-monitors",
            "request_type": request.__class__.__name__,
            "response_type": "ListConnectionMonitorsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'vpn_connection_id' in local_var_params:
            query_params.append(('vpn_connection_id', local_var_params['vpn_connection_id']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
            collection_formats['enterprise_project_id'] = 'multi'

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

    def show_connection_monitor(self, request):
        """查询VPN连接监控

        根据VPN连接监控的ID,查询指定的VPN连接监控
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowConnectionMonitor
        :type request: :class:`huaweicloudsdkvpn.v5.ShowConnectionMonitorRequest`
        :rtype: :class:`huaweicloudsdkvpn.v5.ShowConnectionMonitorResponse`
        """
        http_info = self._show_connection_monitor_http_info(request)
        return self._call_api(**http_info)

    def show_connection_monitor_invoker(self, request):
        http_info = self._show_connection_monitor_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_connection_monitor_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/connection-monitors/{connection_monitor_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowConnectionMonitorResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'connection_monitor_id' in local_var_params:
            path_params['connection_monitor_id'] = local_var_params['connection_monitor_id']

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

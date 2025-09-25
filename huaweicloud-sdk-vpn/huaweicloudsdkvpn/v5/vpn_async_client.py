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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkvpn'")


class VpnAsyncClient(Client):
    def __init__(self):
        super(VpnAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkvpn.v5.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "VpnAsyncClient":
                raise TypeError("client type error, support client type is VpnAsyncClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def check_client_ca_certificate_async(self, request):
        r"""校验客户端CA

        创建服务端时，可以先调用客户端CA的预校验API，检查CA的合法性
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CheckClientCaCertificate
        :type request: :class:`huaweicloudsdkvpn.v5.CheckClientCaCertificateRequest`
        :rtype: :class:`huaweicloudsdkvpn.v5.CheckClientCaCertificateResponse`
        """
        http_info = self._check_client_ca_certificate_http_info(request)
        return self._call_api(**http_info)

    def check_client_ca_certificate_async_invoker(self, request):
        http_info = self._check_client_ca_certificate_http_info(request)
        return AsyncInvoker(self, http_info)

    def _check_client_ca_certificate_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/{project_id}/p2c-vpn-gateways/vpn-servers/client-ca-certificates/check",
            "request_type": request.__class__.__name__,
            "response_type": "CheckClientCaCertificateResponse"
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

    def delete_client_ca_async(self, request):
        r"""删除客户端的CA证书

        删除客户端CA证书
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteClientCa
        :type request: :class:`huaweicloudsdkvpn.v5.DeleteClientCaRequest`
        :rtype: :class:`huaweicloudsdkvpn.v5.DeleteClientCaResponse`
        """
        http_info = self._delete_client_ca_http_info(request)
        return self._call_api(**http_info)

    def delete_client_ca_async_invoker(self, request):
        http_info = self._delete_client_ca_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_client_ca_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v5/{project_id}/p2c-vpn-gateways/vpn-servers/{vpn_server_id}/client-ca-certificates/{client_ca_certificate_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteClientCaResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'vpn_server_id' in local_var_params:
            path_params['vpn_server_id'] = local_var_params['vpn_server_id']
        if 'client_ca_certificate_id' in local_var_params:
            path_params['client_ca_certificate_id'] = local_var_params['client_ca_certificate_id']

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

    def import_client_ca_async(self, request):
        r"""导入客户端 CA 证书

        导入客户端 CA 证书
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ImportClientCa
        :type request: :class:`huaweicloudsdkvpn.v5.ImportClientCaRequest`
        :rtype: :class:`huaweicloudsdkvpn.v5.ImportClientCaResponse`
        """
        http_info = self._import_client_ca_http_info(request)
        return self._call_api(**http_info)

    def import_client_ca_async_invoker(self, request):
        http_info = self._import_client_ca_http_info(request)
        return AsyncInvoker(self, http_info)

    def _import_client_ca_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/{project_id}/p2c-vpn-gateways/vpn-servers/{vpn_server_id}/client-ca-certificates",
            "request_type": request.__class__.__name__,
            "response_type": "ImportClientCaResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'vpn_server_id' in local_var_params:
            path_params['vpn_server_id'] = local_var_params['vpn_server_id']

        query_params = []

        header_params = {}
        if 'x_client_token' in local_var_params:
            header_params['X-Client-Token'] = local_var_params['x_client_token']

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

    def show_client_ca_async(self, request):
        r"""查询客户端的CA证书

        查询客户端CA证书
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowClientCa
        :type request: :class:`huaweicloudsdkvpn.v5.ShowClientCaRequest`
        :rtype: :class:`huaweicloudsdkvpn.v5.ShowClientCaResponse`
        """
        http_info = self._show_client_ca_http_info(request)
        return self._call_api(**http_info)

    def show_client_ca_async_invoker(self, request):
        http_info = self._show_client_ca_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_client_ca_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/p2c-vpn-gateways/vpn-servers/{vpn_server_id}/client-ca-certificates/{client_ca_certificate_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowClientCaResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'vpn_server_id' in local_var_params:
            path_params['vpn_server_id'] = local_var_params['vpn_server_id']
        if 'client_ca_certificate_id' in local_var_params:
            path_params['client_ca_certificate_id'] = local_var_params['client_ca_certificate_id']

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

    def update_client_ca_async(self, request):
        r"""修改客户端的CA证书

        修改客户端CA证书
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateClientCa
        :type request: :class:`huaweicloudsdkvpn.v5.UpdateClientCaRequest`
        :rtype: :class:`huaweicloudsdkvpn.v5.UpdateClientCaResponse`
        """
        http_info = self._update_client_ca_http_info(request)
        return self._call_api(**http_info)

    def update_client_ca_async_invoker(self, request):
        http_info = self._update_client_ca_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_client_ca_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v5/{project_id}/p2c-vpn-gateways/vpn-servers/{vpn_server_id}/client-ca-certificates/{client_ca_certificate_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateClientCaResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'vpn_server_id' in local_var_params:
            path_params['vpn_server_id'] = local_var_params['vpn_server_id']
        if 'client_ca_certificate_id' in local_var_params:
            path_params['client_ca_certificate_id'] = local_var_params['client_ca_certificate_id']

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

    def create_connection_monitor_async(self, request):
        r"""创建VPN连接监控

        创建VPN连接监控
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateConnectionMonitor
        :type request: :class:`huaweicloudsdkvpn.v5.CreateConnectionMonitorRequest`
        :rtype: :class:`huaweicloudsdkvpn.v5.CreateConnectionMonitorResponse`
        """
        http_info = self._create_connection_monitor_http_info(request)
        return self._call_api(**http_info)

    def create_connection_monitor_async_invoker(self, request):
        http_info = self._create_connection_monitor_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_connection_monitor_http_info(self, request):
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

    def delete_connection_monitor_async(self, request):
        r"""删除VPN连接监控

        根据VPN连接监控的ID，删除指定的VPN连接监控
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteConnectionMonitor
        :type request: :class:`huaweicloudsdkvpn.v5.DeleteConnectionMonitorRequest`
        :rtype: :class:`huaweicloudsdkvpn.v5.DeleteConnectionMonitorResponse`
        """
        http_info = self._delete_connection_monitor_http_info(request)
        return self._call_api(**http_info)

    def delete_connection_monitor_async_invoker(self, request):
        http_info = self._delete_connection_monitor_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_connection_monitor_http_info(self, request):
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

    def list_connection_monitors_async(self, request):
        r"""查询VPN连接监控列表

        查询VPN连接监控列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListConnectionMonitors
        :type request: :class:`huaweicloudsdkvpn.v5.ListConnectionMonitorsRequest`
        :rtype: :class:`huaweicloudsdkvpn.v5.ListConnectionMonitorsResponse`
        """
        http_info = self._list_connection_monitors_http_info(request)
        return self._call_api(**http_info)

    def list_connection_monitors_async_invoker(self, request):
        http_info = self._list_connection_monitors_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_connection_monitors_http_info(self, request):
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

    def show_connection_monitor_async(self, request):
        r"""查询VPN连接监控

        根据VPN连接监控的ID,查询指定的VPN连接监控
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowConnectionMonitor
        :type request: :class:`huaweicloudsdkvpn.v5.ShowConnectionMonitorRequest`
        :rtype: :class:`huaweicloudsdkvpn.v5.ShowConnectionMonitorResponse`
        """
        http_info = self._show_connection_monitor_http_info(request)
        return self._call_api(**http_info)

    def show_connection_monitor_async_invoker(self, request):
        http_info = self._show_connection_monitor_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_connection_monitor_http_info(self, request):
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

    def create_cgw_async(self, request):
        r"""创建对端网关

        创建租户用于与VPN网关相连的对端网关
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateCgw
        :type request: :class:`huaweicloudsdkvpn.v5.CreateCgwRequest`
        :rtype: :class:`huaweicloudsdkvpn.v5.CreateCgwResponse`
        """
        http_info = self._create_cgw_http_info(request)
        return self._call_api(**http_info)

    def create_cgw_async_invoker(self, request):
        http_info = self._create_cgw_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_cgw_http_info(self, request):
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

    def delete_cgw_async(self, request):
        r"""删除对端网关

        根据对端网关ID，删除指定的对端网关
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteCgw
        :type request: :class:`huaweicloudsdkvpn.v5.DeleteCgwRequest`
        :rtype: :class:`huaweicloudsdkvpn.v5.DeleteCgwResponse`
        """
        http_info = self._delete_cgw_http_info(request)
        return self._call_api(**http_info)

    def delete_cgw_async_invoker(self, request):
        http_info = self._delete_cgw_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_cgw_http_info(self, request):
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

    def list_cgws_async(self, request):
        r"""查询对端网关列表

        查询对端网关列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListCgws
        :type request: :class:`huaweicloudsdkvpn.v5.ListCgwsRequest`
        :rtype: :class:`huaweicloudsdkvpn.v5.ListCgwsResponse`
        """
        http_info = self._list_cgws_http_info(request)
        return self._call_api(**http_info)

    def list_cgws_async_invoker(self, request):
        http_info = self._list_cgws_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_cgws_http_info(self, request):
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

    def show_cgw_async(self, request):
        r"""查询对端网关

        根据对端网关ID，查询指定的对端网关
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowCgw
        :type request: :class:`huaweicloudsdkvpn.v5.ShowCgwRequest`
        :rtype: :class:`huaweicloudsdkvpn.v5.ShowCgwResponse`
        """
        http_info = self._show_cgw_http_info(request)
        return self._call_api(**http_info)

    def show_cgw_async_invoker(self, request):
        http_info = self._show_cgw_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_cgw_http_info(self, request):
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

    def update_cgw_async(self, request):
        r"""更新对端网关

        根据对端网关ID，更新指定的对端网关
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateCgw
        :type request: :class:`huaweicloudsdkvpn.v5.UpdateCgwRequest`
        :rtype: :class:`huaweicloudsdkvpn.v5.UpdateCgwResponse`
        """
        http_info = self._update_cgw_http_info(request)
        return self._call_api(**http_info)

    def update_cgw_async_invoker(self, request):
        http_info = self._update_cgw_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_cgw_http_info(self, request):
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

    def create_p2c_vgw_async(self, request):
        r"""创建P2C VPN网关

        创建终端入云VPN网关
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateP2cVgw
        :type request: :class:`huaweicloudsdkvpn.v5.CreateP2cVgwRequest`
        :rtype: :class:`huaweicloudsdkvpn.v5.CreateP2cVgwResponse`
        """
        http_info = self._create_p2c_vgw_http_info(request)
        return self._call_api(**http_info)

    def create_p2c_vgw_async_invoker(self, request):
        http_info = self._create_p2c_vgw_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_p2c_vgw_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/{project_id}/p2c-vpn-gateways",
            "request_type": request.__class__.__name__,
            "response_type": "CreateP2cVgwResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_client_token' in local_var_params:
            header_params['X-Client-Token'] = local_var_params['x_client_token']

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

    def delete_p2c_vgw_async(self, request):
        r"""删除P2C VPN网关

        根据P2C VPN网关ID，删除指定的VPN网关
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteP2cVgw
        :type request: :class:`huaweicloudsdkvpn.v5.DeleteP2cVgwRequest`
        :rtype: :class:`huaweicloudsdkvpn.v5.DeleteP2cVgwResponse`
        """
        http_info = self._delete_p2c_vgw_http_info(request)
        return self._call_api(**http_info)

    def delete_p2c_vgw_async_invoker(self, request):
        http_info = self._delete_p2c_vgw_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_p2c_vgw_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v5/{project_id}/p2c-vpn-gateways/{p2c_vgw_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteP2cVgwResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'p2c_vgw_id' in local_var_params:
            path_params['p2c_vgw_id'] = local_var_params['p2c_vgw_id']

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

    def delete_p2c_vgw_connection_async(self, request):
        r"""断开P2C VPN网关连接

        断开P2C VPN网关连接
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteP2cVgwConnection
        :type request: :class:`huaweicloudsdkvpn.v5.DeleteP2cVgwConnectionRequest`
        :rtype: :class:`huaweicloudsdkvpn.v5.DeleteP2cVgwConnectionResponse`
        """
        http_info = self._delete_p2c_vgw_connection_http_info(request)
        return self._call_api(**http_info)

    def delete_p2c_vgw_connection_async_invoker(self, request):
        http_info = self._delete_p2c_vgw_connection_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_p2c_vgw_connection_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/{project_id}/p2c-vpn-gateways/{p2c_vgw_id}/connections/{connection_id}/disconnect",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteP2cVgwConnectionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'p2c_vgw_id' in local_var_params:
            path_params['p2c_vgw_id'] = local_var_params['p2c_vgw_id']
        if 'connection_id' in local_var_params:
            path_params['connection_id'] = local_var_params['connection_id']

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

    def list_p2c_vgw_availability_zones_async(self, request):
        r"""查询P2C VPN网关可用区

        查询P2C VPN网关可用区
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListP2cVgwAvailabilityZones
        :type request: :class:`huaweicloudsdkvpn.v5.ListP2cVgwAvailabilityZonesRequest`
        :rtype: :class:`huaweicloudsdkvpn.v5.ListP2cVgwAvailabilityZonesResponse`
        """
        http_info = self._list_p2c_vgw_availability_zones_http_info(request)
        return self._call_api(**http_info)

    def list_p2c_vgw_availability_zones_async_invoker(self, request):
        http_info = self._list_p2c_vgw_availability_zones_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_p2c_vgw_availability_zones_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/p2c-vpn-gateways/availability-zones",
            "request_type": request.__class__.__name__,
            "response_type": "ListP2cVgwAvailabilityZonesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'flavor' in local_var_params:
            query_params.append(('flavor', local_var_params['flavor']))

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

    def list_p2c_vgw_connections_async(self, request):
        r"""查询P2C VPN网关连接信息列表

        List p2c vpn gateway connections
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListP2cVgwConnections
        :type request: :class:`huaweicloudsdkvpn.v5.ListP2cVgwConnectionsRequest`
        :rtype: :class:`huaweicloudsdkvpn.v5.ListP2cVgwConnectionsResponse`
        """
        http_info = self._list_p2c_vgw_connections_http_info(request)
        return self._call_api(**http_info)

    def list_p2c_vgw_connections_async_invoker(self, request):
        http_info = self._list_p2c_vgw_connections_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_p2c_vgw_connections_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/p2c-vpn-gateways/{p2c_vgw_id}/connections",
            "request_type": request.__class__.__name__,
            "response_type": "ListP2cVgwConnectionsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'p2c_vgw_id' in local_var_params:
            path_params['p2c_vgw_id'] = local_var_params['p2c_vgw_id']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
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

    def list_p2c_vgws_async(self, request):
        r"""查询P2C VPN网关列表

        查询P2C VPN网关列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListP2cVgws
        :type request: :class:`huaweicloudsdkvpn.v5.ListP2cVgwsRequest`
        :rtype: :class:`huaweicloudsdkvpn.v5.ListP2cVgwsResponse`
        """
        http_info = self._list_p2c_vgws_http_info(request)
        return self._call_api(**http_info)

    def list_p2c_vgws_async_invoker(self, request):
        http_info = self._list_p2c_vgws_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_p2c_vgws_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/p2c-vpn-gateways",
            "request_type": request.__class__.__name__,
            "response_type": "ListP2cVgwsResponse"
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

    def show_p2c_vgw_async(self, request):
        r"""查询P2C VPN网关

        根据P2C VPN网关ID，查询指定的VPN网关
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowP2cVgw
        :type request: :class:`huaweicloudsdkvpn.v5.ShowP2cVgwRequest`
        :rtype: :class:`huaweicloudsdkvpn.v5.ShowP2cVgwResponse`
        """
        http_info = self._show_p2c_vgw_http_info(request)
        return self._call_api(**http_info)

    def show_p2c_vgw_async_invoker(self, request):
        http_info = self._show_p2c_vgw_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_p2c_vgw_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/p2c-vpn-gateways/{p2c_vgw_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowP2cVgwResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'p2c_vgw_id' in local_var_params:
            path_params['p2c_vgw_id'] = local_var_params['p2c_vgw_id']

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

    def update_p2c_vgw_async(self, request):
        r"""更新P2C VPN网关

        根据P2C VPN网关ID，更新指定的P2C VPN网关
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateP2cVgw
        :type request: :class:`huaweicloudsdkvpn.v5.UpdateP2cVgwRequest`
        :rtype: :class:`huaweicloudsdkvpn.v5.UpdateP2cVgwResponse`
        """
        http_info = self._update_p2c_vgw_http_info(request)
        return self._call_api(**http_info)

    def update_p2c_vgw_async_invoker(self, request):
        http_info = self._update_p2c_vgw_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_p2c_vgw_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v5/{project_id}/p2c-vpn-gateways/{p2c_vgw_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateP2cVgwResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'p2c_vgw_id' in local_var_params:
            path_params['p2c_vgw_id'] = local_var_params['p2c_vgw_id']

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

    def batch_create_resource_tags_async(self, request):
        r"""批量添加资源标签

        为指定实例批量添加标签
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchCreateResourceTags
        :type request: :class:`huaweicloudsdkvpn.v5.BatchCreateResourceTagsRequest`
        :rtype: :class:`huaweicloudsdkvpn.v5.BatchCreateResourceTagsResponse`
        """
        http_info = self._batch_create_resource_tags_http_info(request)
        return self._call_api(**http_info)

    def batch_create_resource_tags_async_invoker(self, request):
        http_info = self._batch_create_resource_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_create_resource_tags_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/{project_id}/{resource_type}/{resource_id}/tags/create",
            "request_type": request.__class__.__name__,
            "response_type": "BatchCreateResourceTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_type' in local_var_params:
            path_params['resource_type'] = local_var_params['resource_type']
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

    def batch_delete_resource_tags_async(self, request):
        r"""批量删除资源标签

        为指定实例批量删除标签
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchDeleteResourceTags
        :type request: :class:`huaweicloudsdkvpn.v5.BatchDeleteResourceTagsRequest`
        :rtype: :class:`huaweicloudsdkvpn.v5.BatchDeleteResourceTagsResponse`
        """
        http_info = self._batch_delete_resource_tags_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_resource_tags_async_invoker(self, request):
        http_info = self._batch_delete_resource_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_delete_resource_tags_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/{project_id}/{resource_type}/{resource_id}/tags/delete",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeleteResourceTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_type' in local_var_params:
            path_params['resource_type'] = local_var_params['resource_type']
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

    def count_resources_by_tags_async(self, request):
        r"""查询资源实例数量

        根据标签查询资源实例数量
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CountResourcesByTags
        :type request: :class:`huaweicloudsdkvpn.v5.CountResourcesByTagsRequest`
        :rtype: :class:`huaweicloudsdkvpn.v5.CountResourcesByTagsResponse`
        """
        http_info = self._count_resources_by_tags_http_info(request)
        return self._call_api(**http_info)

    def count_resources_by_tags_async_invoker(self, request):
        http_info = self._count_resources_by_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _count_resources_by_tags_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/{project_id}/{resource_type}/resource-instances/count",
            "request_type": request.__class__.__name__,
            "response_type": "CountResourcesByTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_type' in local_var_params:
            path_params['resource_type'] = local_var_params['resource_type']

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

    def list_project_tags_async(self, request):
        r"""查询项目标签

        查询租户在指定项目中指定资源类型下的所有标签
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListProjectTags
        :type request: :class:`huaweicloudsdkvpn.v5.ListProjectTagsRequest`
        :rtype: :class:`huaweicloudsdkvpn.v5.ListProjectTagsResponse`
        """
        http_info = self._list_project_tags_http_info(request)
        return self._call_api(**http_info)

    def list_project_tags_async_invoker(self, request):
        http_info = self._list_project_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_project_tags_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/{resource_type}/tags",
            "request_type": request.__class__.__name__,
            "response_type": "ListProjectTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_type' in local_var_params:
            path_params['resource_type'] = local_var_params['resource_type']

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

    def list_resources_by_tags_async(self, request):
        r"""查询资源实例列表

        根据标签查询资源实例列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListResourcesByTags
        :type request: :class:`huaweicloudsdkvpn.v5.ListResourcesByTagsRequest`
        :rtype: :class:`huaweicloudsdkvpn.v5.ListResourcesByTagsResponse`
        """
        http_info = self._list_resources_by_tags_http_info(request)
        return self._call_api(**http_info)

    def list_resources_by_tags_async_invoker(self, request):
        http_info = self._list_resources_by_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_resources_by_tags_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/{project_id}/{resource_type}/resource-instances/filter",
            "request_type": request.__class__.__name__,
            "response_type": "ListResourcesByTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_type' in local_var_params:
            path_params['resource_type'] = local_var_params['resource_type']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

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

    def show_resource_tags_async(self, request):
        r"""查询资源标签

        查询指定实例的标签信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowResourceTags
        :type request: :class:`huaweicloudsdkvpn.v5.ShowResourceTagsRequest`
        :rtype: :class:`huaweicloudsdkvpn.v5.ShowResourceTagsResponse`
        """
        http_info = self._show_resource_tags_http_info(request)
        return self._call_api(**http_info)

    def show_resource_tags_async_invoker(self, request):
        http_info = self._show_resource_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_resource_tags_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/{resource_type}/{resource_id}/tags",
            "request_type": request.__class__.__name__,
            "response_type": "ShowResourceTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_type' in local_var_params:
            path_params['resource_type'] = local_var_params['resource_type']
        if 'resource_id' in local_var_params:
            path_params['resource_id'] = local_var_params['resource_id']

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

    def create_vpn_access_policy_async(self, request):
        r"""创建VPN访问策略

        创建VPN访问策略
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateVpnAccessPolicy
        :type request: :class:`huaweicloudsdkvpn.v5.CreateVpnAccessPolicyRequest`
        :rtype: :class:`huaweicloudsdkvpn.v5.CreateVpnAccessPolicyResponse`
        """
        http_info = self._create_vpn_access_policy_http_info(request)
        return self._call_api(**http_info)

    def create_vpn_access_policy_async_invoker(self, request):
        http_info = self._create_vpn_access_policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_vpn_access_policy_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/{project_id}/p2c-vpn-gateways/vpn-servers/{vpn_server_id}/access-policies",
            "request_type": request.__class__.__name__,
            "response_type": "CreateVpnAccessPolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'vpn_server_id' in local_var_params:
            path_params['vpn_server_id'] = local_var_params['vpn_server_id']

        query_params = []

        header_params = {}
        if 'x_client_token' in local_var_params:
            header_params['X-Client-Token'] = local_var_params['x_client_token']

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

    def delete_vpn_access_policy_async(self, request):
        r"""删除VPN访问策略

        删除VPN访问策略
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteVpnAccessPolicy
        :type request: :class:`huaweicloudsdkvpn.v5.DeleteVpnAccessPolicyRequest`
        :rtype: :class:`huaweicloudsdkvpn.v5.DeleteVpnAccessPolicyResponse`
        """
        http_info = self._delete_vpn_access_policy_http_info(request)
        return self._call_api(**http_info)

    def delete_vpn_access_policy_async_invoker(self, request):
        http_info = self._delete_vpn_access_policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_vpn_access_policy_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v5/{project_id}/p2c-vpn-gateways/vpn-servers/{vpn_server_id}/access-policies/{policy_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteVpnAccessPolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'vpn_server_id' in local_var_params:
            path_params['vpn_server_id'] = local_var_params['vpn_server_id']
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

    def list_vpn_access_policies_async(self, request):
        r"""查询VPN访问策略列表

        查询VPN访问策略列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListVpnAccessPolicies
        :type request: :class:`huaweicloudsdkvpn.v5.ListVpnAccessPoliciesRequest`
        :rtype: :class:`huaweicloudsdkvpn.v5.ListVpnAccessPoliciesResponse`
        """
        http_info = self._list_vpn_access_policies_http_info(request)
        return self._call_api(**http_info)

    def list_vpn_access_policies_async_invoker(self, request):
        http_info = self._list_vpn_access_policies_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_vpn_access_policies_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/p2c-vpn-gateways/vpn-servers/{vpn_server_id}/access-policies",
            "request_type": request.__class__.__name__,
            "response_type": "ListVpnAccessPoliciesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'vpn_server_id' in local_var_params:
            path_params['vpn_server_id'] = local_var_params['vpn_server_id']

        query_params = []
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

    def show_vpn_access_policy_async(self, request):
        r"""查询VPN访问策略

        查询VPN访问策略
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowVpnAccessPolicy
        :type request: :class:`huaweicloudsdkvpn.v5.ShowVpnAccessPolicyRequest`
        :rtype: :class:`huaweicloudsdkvpn.v5.ShowVpnAccessPolicyResponse`
        """
        http_info = self._show_vpn_access_policy_http_info(request)
        return self._call_api(**http_info)

    def show_vpn_access_policy_async_invoker(self, request):
        http_info = self._show_vpn_access_policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_vpn_access_policy_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/p2c-vpn-gateways/vpn-servers/{vpn_server_id}/access-policies/{policy_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowVpnAccessPolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'vpn_server_id' in local_var_params:
            path_params['vpn_server_id'] = local_var_params['vpn_server_id']
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']

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

    def update_vpn_access_policy_async(self, request):
        r"""修改VPN访问策略

        修改VPN访问策略
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateVpnAccessPolicy
        :type request: :class:`huaweicloudsdkvpn.v5.UpdateVpnAccessPolicyRequest`
        :rtype: :class:`huaweicloudsdkvpn.v5.UpdateVpnAccessPolicyResponse`
        """
        http_info = self._update_vpn_access_policy_http_info(request)
        return self._call_api(**http_info)

    def update_vpn_access_policy_async_invoker(self, request):
        http_info = self._update_vpn_access_policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_vpn_access_policy_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v5/{project_id}/p2c-vpn-gateways/vpn-servers/{vpn_server_id}/access-policies/{policy_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateVpnAccessPolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'vpn_server_id' in local_var_params:
            path_params['vpn_server_id'] = local_var_params['vpn_server_id']
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

    def batch_create_vpn_connection_async(self, request):
        r"""批量创建VPN连接

        同时创建1-2条VPN连接
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchCreateVpnConnection
        :type request: :class:`huaweicloudsdkvpn.v5.BatchCreateVpnConnectionRequest`
        :rtype: :class:`huaweicloudsdkvpn.v5.BatchCreateVpnConnectionResponse`
        """
        http_info = self._batch_create_vpn_connection_http_info(request)
        return self._call_api(**http_info)

    def batch_create_vpn_connection_async_invoker(self, request):
        http_info = self._batch_create_vpn_connection_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_create_vpn_connection_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/{project_id}/vpn-connections/batch-create",
            "request_type": request.__class__.__name__,
            "response_type": "BatchCreateVpnConnectionResponse"
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

    def create_vpn_connection_async(self, request):
        r"""创建VPN连接

        创建VPN连接，连接VPN网关与对端网关
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateVpnConnection
        :type request: :class:`huaweicloudsdkvpn.v5.CreateVpnConnectionRequest`
        :rtype: :class:`huaweicloudsdkvpn.v5.CreateVpnConnectionResponse`
        """
        http_info = self._create_vpn_connection_http_info(request)
        return self._call_api(**http_info)

    def create_vpn_connection_async_invoker(self, request):
        http_info = self._create_vpn_connection_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_vpn_connection_http_info(self, request):
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

    def delete_vpn_connection_async(self, request):
        r"""删除VPN连接

        根据连接ID，删除指定的VPN连接
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteVpnConnection
        :type request: :class:`huaweicloudsdkvpn.v5.DeleteVpnConnectionRequest`
        :rtype: :class:`huaweicloudsdkvpn.v5.DeleteVpnConnectionResponse`
        """
        http_info = self._delete_vpn_connection_http_info(request)
        return self._call_api(**http_info)

    def delete_vpn_connection_async_invoker(self, request):
        http_info = self._delete_vpn_connection_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_vpn_connection_http_info(self, request):
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

    def list_vpn_connections_async(self, request):
        r"""查询VPN连接列表

        查询VPN连接列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListVpnConnections
        :type request: :class:`huaweicloudsdkvpn.v5.ListVpnConnectionsRequest`
        :rtype: :class:`huaweicloudsdkvpn.v5.ListVpnConnectionsResponse`
        """
        http_info = self._list_vpn_connections_http_info(request)
        return self._call_api(**http_info)

    def list_vpn_connections_async_invoker(self, request):
        http_info = self._list_vpn_connections_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_vpn_connections_http_info(self, request):
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

    def reset_vpn_connection_async(self, request):
        r"""重置VPN连接

        根据连接ID，重置指定VPN连接
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ResetVpnConnection
        :type request: :class:`huaweicloudsdkvpn.v5.ResetVpnConnectionRequest`
        :rtype: :class:`huaweicloudsdkvpn.v5.ResetVpnConnectionResponse`
        """
        http_info = self._reset_vpn_connection_http_info(request)
        return self._call_api(**http_info)

    def reset_vpn_connection_async_invoker(self, request):
        http_info = self._reset_vpn_connection_http_info(request)
        return AsyncInvoker(self, http_info)

    def _reset_vpn_connection_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/{project_id}/vpn-connection/{vpn_connection_id}/reset",
            "request_type": request.__class__.__name__,
            "response_type": "ResetVpnConnectionResponse"
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

    def show_vpn_connection_async(self, request):
        r"""查询VPN连接

        根据连接ID，查询指定的VPN连接的参数
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowVpnConnection
        :type request: :class:`huaweicloudsdkvpn.v5.ShowVpnConnectionRequest`
        :rtype: :class:`huaweicloudsdkvpn.v5.ShowVpnConnectionResponse`
        """
        http_info = self._show_vpn_connection_http_info(request)
        return self._call_api(**http_info)

    def show_vpn_connection_async_invoker(self, request):
        http_info = self._show_vpn_connection_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_vpn_connection_http_info(self, request):
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

    def show_vpn_connection_log_async(self, request):
        r"""查询VPN连接日志

        根据连接ID，查询指定的VPN连接日志
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowVpnConnectionLog
        :type request: :class:`huaweicloudsdkvpn.v5.ShowVpnConnectionLogRequest`
        :rtype: :class:`huaweicloudsdkvpn.v5.ShowVpnConnectionLogResponse`
        """
        http_info = self._show_vpn_connection_log_http_info(request)
        return self._call_api(**http_info)

    def show_vpn_connection_log_async_invoker(self, request):
        http_info = self._show_vpn_connection_log_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_vpn_connection_log_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/vpn-connection/{vpn_connection_id}/log",
            "request_type": request.__class__.__name__,
            "response_type": "ShowVpnConnectionLogResponse"
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

    def update_vpn_connection_async(self, request):
        r"""更新VPN连接

        根据连接ID，更新指定的VPN连接的参数
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateVpnConnection
        :type request: :class:`huaweicloudsdkvpn.v5.UpdateVpnConnectionRequest`
        :rtype: :class:`huaweicloudsdkvpn.v5.UpdateVpnConnectionResponse`
        """
        http_info = self._update_vpn_connection_http_info(request)
        return self._call_api(**http_info)

    def update_vpn_connection_async_invoker(self, request):
        http_info = self._update_vpn_connection_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_vpn_connection_http_info(self, request):
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

    def delete_vpn_connections_log_config_async(self, request):
        r"""删除VPN连接日志配置

        删除VPN连接日志配置
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteVpnConnectionsLogConfig
        :type request: :class:`huaweicloudsdkvpn.v5.DeleteVpnConnectionsLogConfigRequest`
        :rtype: :class:`huaweicloudsdkvpn.v5.DeleteVpnConnectionsLogConfigResponse`
        """
        http_info = self._delete_vpn_connections_log_config_http_info(request)
        return self._call_api(**http_info)

    def delete_vpn_connections_log_config_async_invoker(self, request):
        http_info = self._delete_vpn_connections_log_config_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_vpn_connections_log_config_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v5/{project_id}/p2c-vpn-gateways/{p2c_vgw_id}/log-config",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteVpnConnectionsLogConfigResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'p2c_vgw_id' in local_var_params:
            path_params['p2c_vgw_id'] = local_var_params['p2c_vgw_id']

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

    def show_vpn_connections_log_config_async(self, request):
        r"""查询VPN连接日志配置

        查询VPN连接日志配置
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowVpnConnectionsLogConfig
        :type request: :class:`huaweicloudsdkvpn.v5.ShowVpnConnectionsLogConfigRequest`
        :rtype: :class:`huaweicloudsdkvpn.v5.ShowVpnConnectionsLogConfigResponse`
        """
        http_info = self._show_vpn_connections_log_config_http_info(request)
        return self._call_api(**http_info)

    def show_vpn_connections_log_config_async_invoker(self, request):
        http_info = self._show_vpn_connections_log_config_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_vpn_connections_log_config_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/p2c-vpn-gateways/{p2c_vgw_id}/log-config",
            "request_type": request.__class__.__name__,
            "response_type": "ShowVpnConnectionsLogConfigResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'p2c_vgw_id' in local_var_params:
            path_params['p2c_vgw_id'] = local_var_params['p2c_vgw_id']

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

    def update_vpn_connections_log_config_async(self, request):
        r"""更新VPN连接日志配置

        更新VPN连接日志配置
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateVpnConnectionsLogConfig
        :type request: :class:`huaweicloudsdkvpn.v5.UpdateVpnConnectionsLogConfigRequest`
        :rtype: :class:`huaweicloudsdkvpn.v5.UpdateVpnConnectionsLogConfigResponse`
        """
        http_info = self._update_vpn_connections_log_config_http_info(request)
        return self._call_api(**http_info)

    def update_vpn_connections_log_config_async_invoker(self, request):
        http_info = self._update_vpn_connections_log_config_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_vpn_connections_log_config_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v5/{project_id}/p2c-vpn-gateways/{p2c_vgw_id}/log-config",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateVpnConnectionsLogConfigResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'p2c_vgw_id' in local_var_params:
            path_params['p2c_vgw_id'] = local_var_params['p2c_vgw_id']

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

    def create_vgw_async(self, request):
        r"""创建VPN网关

        创建一个VPN网关
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateVgw
        :type request: :class:`huaweicloudsdkvpn.v5.CreateVgwRequest`
        :rtype: :class:`huaweicloudsdkvpn.v5.CreateVgwResponse`
        """
        http_info = self._create_vgw_http_info(request)
        return self._call_api(**http_info)

    def create_vgw_async_invoker(self, request):
        http_info = self._create_vgw_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_vgw_http_info(self, request):
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

    def delete_vgw_async(self, request):
        r"""删除VPN网关

        根据VPN网关ID，删除指定的VPN网关
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteVgw
        :type request: :class:`huaweicloudsdkvpn.v5.DeleteVgwRequest`
        :rtype: :class:`huaweicloudsdkvpn.v5.DeleteVgwResponse`
        """
        http_info = self._delete_vgw_http_info(request)
        return self._call_api(**http_info)

    def delete_vgw_async_invoker(self, request):
        http_info = self._delete_vgw_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_vgw_http_info(self, request):
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

    def list_availability_zones_async(self, request):
        r"""查询VPN网关可用区

        查询VPN网关可用区
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAvailabilityZones
        :type request: :class:`huaweicloudsdkvpn.v5.ListAvailabilityZonesRequest`
        :rtype: :class:`huaweicloudsdkvpn.v5.ListAvailabilityZonesResponse`
        """
        http_info = self._list_availability_zones_http_info(request)
        return self._call_api(**http_info)

    def list_availability_zones_async_invoker(self, request):
        http_info = self._list_availability_zones_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_availability_zones_http_info(self, request):
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

    def list_extended_availability_zones_async(self, request):
        r"""查询VPN网关可用区

        查询VPN网关可用区
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListExtendedAvailabilityZones
        :type request: :class:`huaweicloudsdkvpn.v5.ListExtendedAvailabilityZonesRequest`
        :rtype: :class:`huaweicloudsdkvpn.v5.ListExtendedAvailabilityZonesResponse`
        """
        http_info = self._list_extended_availability_zones_http_info(request)
        return self._call_api(**http_info)

    def list_extended_availability_zones_async_invoker(self, request):
        http_info = self._list_extended_availability_zones_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_extended_availability_zones_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5.1/{project_id}/vpn-gateways/availability-zones",
            "request_type": request.__class__.__name__,
            "response_type": "ListExtendedAvailabilityZonesResponse"
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

    def list_vgws_async(self, request):
        r"""查询VPN网关列表

        查询VPN网关列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListVgws
        :type request: :class:`huaweicloudsdkvpn.v5.ListVgwsRequest`
        :rtype: :class:`huaweicloudsdkvpn.v5.ListVgwsResponse`
        """
        http_info = self._list_vgws_http_info(request)
        return self._call_api(**http_info)

    def list_vgws_async_invoker(self, request):
        http_info = self._list_vgws_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_vgws_http_info(self, request):
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

    def show_vgw_async(self, request):
        r"""查询VPN网关

        根据VPN网关ID，查询指定的VPN网关
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowVgw
        :type request: :class:`huaweicloudsdkvpn.v5.ShowVgwRequest`
        :rtype: :class:`huaweicloudsdkvpn.v5.ShowVgwResponse`
        """
        http_info = self._show_vgw_http_info(request)
        return self._call_api(**http_info)

    def show_vgw_async_invoker(self, request):
        http_info = self._show_vgw_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_vgw_http_info(self, request):
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

    def show_vpn_gateway_routing_table_async(self, request):
        r"""查询VPN网关路由表

        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowVpnGatewayRoutingTable
        :type request: :class:`huaweicloudsdkvpn.v5.ShowVpnGatewayRoutingTableRequest`
        :rtype: :class:`huaweicloudsdkvpn.v5.ShowVpnGatewayRoutingTableResponse`
        """
        http_info = self._show_vpn_gateway_routing_table_http_info(request)
        return self._call_api(**http_info)

    def show_vpn_gateway_routing_table_async_invoker(self, request):
        http_info = self._show_vpn_gateway_routing_table_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_vpn_gateway_routing_table_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/vpn-gateways/{vgw_id}/routing-table",
            "request_type": request.__class__.__name__,
            "response_type": "ShowVpnGatewayRoutingTableResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'vgw_id' in local_var_params:
            path_params['vgw_id'] = local_var_params['vgw_id']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'is_include_nexthop_resource' in local_var_params:
            query_params.append(('is_include_nexthop_resource', local_var_params['is_include_nexthop_resource']))

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

    def update_postpaid_vgw_specification_async(self, request):
        r"""修改网关规格

        对单个网关规格进行修改，可以升配或降配
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdatePostpaidVgwSpecification
        :type request: :class:`huaweicloudsdkvpn.v5.UpdatePostpaidVgwSpecificationRequest`
        :rtype: :class:`huaweicloudsdkvpn.v5.UpdatePostpaidVgwSpecificationResponse`
        """
        http_info = self._update_postpaid_vgw_specification_http_info(request)
        return self._call_api(**http_info)

    def update_postpaid_vgw_specification_async_invoker(self, request):
        http_info = self._update_postpaid_vgw_specification_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_postpaid_vgw_specification_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/{project_id}/vpn-gateways/{vgw_id}/update-specification",
            "request_type": request.__class__.__name__,
            "response_type": "UpdatePostpaidVgwSpecificationResponse"
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

    def update_vgw_async(self, request):
        r"""更新VPN网关

        根据VPN网关ID，更新指定的VPN网关
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateVgw
        :type request: :class:`huaweicloudsdkvpn.v5.UpdateVgwRequest`
        :rtype: :class:`huaweicloudsdkvpn.v5.UpdateVgwResponse`
        """
        http_info = self._update_vgw_http_info(request)
        return self._call_api(**http_info)

    def update_vgw_async_invoker(self, request):
        http_info = self._update_vgw_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_vgw_http_info(self, request):
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

    def create_vgw_certificate_async(self, request):
        r"""导入VPN网关证书

        导入租户VPN网关所使用的证书，包括签名证书、签名私钥、加密证书、加密私钥和CA证书链。当前只支持国密证书
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateVgwCertificate
        :type request: :class:`huaweicloudsdkvpn.v5.CreateVgwCertificateRequest`
        :rtype: :class:`huaweicloudsdkvpn.v5.CreateVgwCertificateResponse`
        """
        http_info = self._create_vgw_certificate_http_info(request)
        return self._call_api(**http_info)

    def create_vgw_certificate_async_invoker(self, request):
        http_info = self._create_vgw_certificate_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_vgw_certificate_http_info(self, request):
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

    def show_vpn_gateway_certificate_async(self, request):
        r"""查询VPN网关证书

        根据VPN网关ID，查询所指定的VPN网关证书
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowVpnGatewayCertificate
        :type request: :class:`huaweicloudsdkvpn.v5.ShowVpnGatewayCertificateRequest`
        :rtype: :class:`huaweicloudsdkvpn.v5.ShowVpnGatewayCertificateResponse`
        """
        http_info = self._show_vpn_gateway_certificate_http_info(request)
        return self._call_api(**http_info)

    def show_vpn_gateway_certificate_async_invoker(self, request):
        http_info = self._show_vpn_gateway_certificate_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_vpn_gateway_certificate_http_info(self, request):
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

    def update_vgw_certificate_async(self, request):
        r"""更新VPN网关证书

        更新租户VPN网关所使用的证书，包括签名证书、签名私钥、加密证书、加密私钥和CA证书链。当前只支持国密证书
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateVgwCertificate
        :type request: :class:`huaweicloudsdkvpn.v5.UpdateVgwCertificateRequest`
        :rtype: :class:`huaweicloudsdkvpn.v5.UpdateVgwCertificateResponse`
        """
        http_info = self._update_vgw_certificate_http_info(request)
        return self._call_api(**http_info)

    def update_vgw_certificate_async_invoker(self, request):
        http_info = self._update_vgw_certificate_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_vgw_certificate_http_info(self, request):
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

    def show_quotas_info_async(self, request):
        r"""查询指定租户配额

        查询指定租户的配额
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowQuotasInfo
        :type request: :class:`huaweicloudsdkvpn.v5.ShowQuotasInfoRequest`
        :rtype: :class:`huaweicloudsdkvpn.v5.ShowQuotasInfoResponse`
        """
        http_info = self._show_quotas_info_http_info(request)
        return self._call_api(**http_info)

    def show_quotas_info_async_invoker(self, request):
        http_info = self._show_quotas_info_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_quotas_info_http_info(self, request):
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

    def create_vpn_server_async(self, request):
        r"""创建一个VPN 服务端

        创建一个VPN 服务端
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateVpnServer
        :type request: :class:`huaweicloudsdkvpn.v5.CreateVpnServerRequest`
        :rtype: :class:`huaweicloudsdkvpn.v5.CreateVpnServerResponse`
        """
        http_info = self._create_vpn_server_http_info(request)
        return self._call_api(**http_info)

    def create_vpn_server_async_invoker(self, request):
        http_info = self._create_vpn_server_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_vpn_server_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/{project_id}/p2c-vpn-gateways/{p2c_vgw_id}/vpn-servers",
            "request_type": request.__class__.__name__,
            "response_type": "CreateVpnServerResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'p2c_vgw_id' in local_var_params:
            path_params['p2c_vgw_id'] = local_var_params['p2c_vgw_id']

        query_params = []

        header_params = {}
        if 'x_client_token' in local_var_params:
            header_params['X-Client-Token'] = local_var_params['x_client_token']

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

    def export_client_config_async(self, request):
        r"""导出服务端对应的客户端配置信息

        导出客户端配置信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ExportClientConfig
        :type request: :class:`huaweicloudsdkvpn.v5.ExportClientConfigRequest`
        :rtype: :class:`huaweicloudsdkvpn.v5.ExportClientConfigResponse`
        """
        http_info = self._export_client_config_http_info(request)
        return self._call_api(**http_info)

    def export_client_config_async_invoker(self, request):
        http_info = self._export_client_config_http_info(request)
        return AsyncInvoker(self, http_info)

    def _export_client_config_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/{project_id}/p2c-vpn-gateways/vpn-servers/{vpn_server_id}/client-config/export",
            "request_type": request.__class__.__name__,
            "response_type": "ExportClientConfigResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'vpn_server_id' in local_var_params:
            path_params['vpn_server_id'] = local_var_params['vpn_server_id']

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

    def list_vpn_servers_by_project_async(self, request):
        r"""查询租户下的所有服务端信息

        查询租户下的所有服务端信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListVpnServersByProject
        :type request: :class:`huaweicloudsdkvpn.v5.ListVpnServersByProjectRequest`
        :rtype: :class:`huaweicloudsdkvpn.v5.ListVpnServersByProjectResponse`
        """
        http_info = self._list_vpn_servers_by_project_http_info(request)
        return self._call_api(**http_info)

    def list_vpn_servers_by_project_async_invoker(self, request):
        http_info = self._list_vpn_servers_by_project_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_vpn_servers_by_project_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/vpn-servers",
            "request_type": request.__class__.__name__,
            "response_type": "ListVpnServersByProjectResponse"
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

    def list_vpn_servers_by_vgw_async(self, request):
        r"""查询一个网关下的服务端信息

        查询一个网关下的服务端信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListVpnServersByVgw
        :type request: :class:`huaweicloudsdkvpn.v5.ListVpnServersByVgwRequest`
        :rtype: :class:`huaweicloudsdkvpn.v5.ListVpnServersByVgwResponse`
        """
        http_info = self._list_vpn_servers_by_vgw_http_info(request)
        return self._call_api(**http_info)

    def list_vpn_servers_by_vgw_async_invoker(self, request):
        http_info = self._list_vpn_servers_by_vgw_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_vpn_servers_by_vgw_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/p2c-vpn-gateways/{p2c_vgw_id}/vpn-servers",
            "request_type": request.__class__.__name__,
            "response_type": "ListVpnServersByVgwResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'p2c_vgw_id' in local_var_params:
            path_params['p2c_vgw_id'] = local_var_params['p2c_vgw_id']

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

    def update_vpn_server_async(self, request):
        r"""更新指定VPN 服务端

        更新指定VPN 服务端
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateVpnServer
        :type request: :class:`huaweicloudsdkvpn.v5.UpdateVpnServerRequest`
        :rtype: :class:`huaweicloudsdkvpn.v5.UpdateVpnServerResponse`
        """
        http_info = self._update_vpn_server_http_info(request)
        return self._call_api(**http_info)

    def update_vpn_server_async_invoker(self, request):
        http_info = self._update_vpn_server_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_vpn_server_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v5/{project_id}/p2c-vpn-gateways/vpn-servers/{vpn_server_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateVpnServerResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'vpn_server_id' in local_var_params:
            path_params['vpn_server_id'] = local_var_params['vpn_server_id']

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

    def batch_create_vpn_users_async(self, request):
        r"""批量创建VPN用户

        批量创建P2C VPN用户
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchCreateVpnUsers
        :type request: :class:`huaweicloudsdkvpn.v5.BatchCreateVpnUsersRequest`
        :rtype: :class:`huaweicloudsdkvpn.v5.BatchCreateVpnUsersResponse`
        """
        http_info = self._batch_create_vpn_users_http_info(request)
        return self._call_api(**http_info)

    def batch_create_vpn_users_async_invoker(self, request):
        http_info = self._batch_create_vpn_users_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_create_vpn_users_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/{project_id}/p2c-vpn-gateways/vpn-servers/{vpn_server_id}/users/batch-create",
            "request_type": request.__class__.__name__,
            "response_type": "BatchCreateVpnUsersResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'vpn_server_id' in local_var_params:
            path_params['vpn_server_id'] = local_var_params['vpn_server_id']

        query_params = []

        header_params = {}
        if 'x_client_token' in local_var_params:
            header_params['X-Client-Token'] = local_var_params['x_client_token']

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

    def batch_delete_vpn_users_async(self, request):
        r"""批量删除VPN用户

        批量删除P2C VPN用户
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchDeleteVpnUsers
        :type request: :class:`huaweicloudsdkvpn.v5.BatchDeleteVpnUsersRequest`
        :rtype: :class:`huaweicloudsdkvpn.v5.BatchDeleteVpnUsersResponse`
        """
        http_info = self._batch_delete_vpn_users_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_vpn_users_async_invoker(self, request):
        http_info = self._batch_delete_vpn_users_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_delete_vpn_users_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/{project_id}/p2c-vpn-gateways/vpn-servers/{vpn_server_id}/users/batch-delete",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeleteVpnUsersResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'vpn_server_id' in local_var_params:
            path_params['vpn_server_id'] = local_var_params['vpn_server_id']

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

    def create_vpn_user_async(self, request):
        r"""创建VPN用户

        创建VPN用户
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateVpnUser
        :type request: :class:`huaweicloudsdkvpn.v5.CreateVpnUserRequest`
        :rtype: :class:`huaweicloudsdkvpn.v5.CreateVpnUserResponse`
        """
        http_info = self._create_vpn_user_http_info(request)
        return self._call_api(**http_info)

    def create_vpn_user_async_invoker(self, request):
        http_info = self._create_vpn_user_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_vpn_user_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/{project_id}/p2c-vpn-gateways/vpn-servers/{vpn_server_id}/users",
            "request_type": request.__class__.__name__,
            "response_type": "CreateVpnUserResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'vpn_server_id' in local_var_params:
            path_params['vpn_server_id'] = local_var_params['vpn_server_id']

        query_params = []

        header_params = {}
        if 'x_client_token' in local_var_params:
            header_params['X-Client-Token'] = local_var_params['x_client_token']

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

    def delete_vpn_user_async(self, request):
        r"""删除VPN用户

        删除VPN用户
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteVpnUser
        :type request: :class:`huaweicloudsdkvpn.v5.DeleteVpnUserRequest`
        :rtype: :class:`huaweicloudsdkvpn.v5.DeleteVpnUserResponse`
        """
        http_info = self._delete_vpn_user_http_info(request)
        return self._call_api(**http_info)

    def delete_vpn_user_async_invoker(self, request):
        http_info = self._delete_vpn_user_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_vpn_user_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v5/{project_id}/p2c-vpn-gateways/vpn-servers/{vpn_server_id}/users/{user_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteVpnUserResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'vpn_server_id' in local_var_params:
            path_params['vpn_server_id'] = local_var_params['vpn_server_id']
        if 'user_id' in local_var_params:
            path_params['user_id'] = local_var_params['user_id']

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

    def list_vpn_users_async(self, request):
        r"""查询VPN用户列表

        查询VPN用户列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListVpnUsers
        :type request: :class:`huaweicloudsdkvpn.v5.ListVpnUsersRequest`
        :rtype: :class:`huaweicloudsdkvpn.v5.ListVpnUsersResponse`
        """
        http_info = self._list_vpn_users_http_info(request)
        return self._call_api(**http_info)

    def list_vpn_users_async_invoker(self, request):
        http_info = self._list_vpn_users_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_vpn_users_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/p2c-vpn-gateways/vpn-servers/{vpn_server_id}/users",
            "request_type": request.__class__.__name__,
            "response_type": "ListVpnUsersResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'vpn_server_id' in local_var_params:
            path_params['vpn_server_id'] = local_var_params['vpn_server_id']

        query_params = []
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

    def reset_vpn_user_password_async(self, request):
        r"""重置VPN用户密码

        重置VPN用户密码
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ResetVpnUserPassword
        :type request: :class:`huaweicloudsdkvpn.v5.ResetVpnUserPasswordRequest`
        :rtype: :class:`huaweicloudsdkvpn.v5.ResetVpnUserPasswordResponse`
        """
        http_info = self._reset_vpn_user_password_http_info(request)
        return self._call_api(**http_info)

    def reset_vpn_user_password_async_invoker(self, request):
        http_info = self._reset_vpn_user_password_http_info(request)
        return AsyncInvoker(self, http_info)

    def _reset_vpn_user_password_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/{project_id}/p2c-vpn-gateways/vpn-servers/{vpn_server_id}/users/{user_id}/reset-password",
            "request_type": request.__class__.__name__,
            "response_type": "ResetVpnUserPasswordResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'vpn_server_id' in local_var_params:
            path_params['vpn_server_id'] = local_var_params['vpn_server_id']
        if 'user_id' in local_var_params:
            path_params['user_id'] = local_var_params['user_id']

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

    def show_vpn_user_async(self, request):
        r"""查询VPN用户

        查询VPN用户
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowVpnUser
        :type request: :class:`huaweicloudsdkvpn.v5.ShowVpnUserRequest`
        :rtype: :class:`huaweicloudsdkvpn.v5.ShowVpnUserResponse`
        """
        http_info = self._show_vpn_user_http_info(request)
        return self._call_api(**http_info)

    def show_vpn_user_async_invoker(self, request):
        http_info = self._show_vpn_user_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_vpn_user_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/p2c-vpn-gateways/vpn-servers/{vpn_server_id}/users/{user_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowVpnUserResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'vpn_server_id' in local_var_params:
            path_params['vpn_server_id'] = local_var_params['vpn_server_id']
        if 'user_id' in local_var_params:
            path_params['user_id'] = local_var_params['user_id']

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

    def update_vpn_user_async(self, request):
        r"""修改VPN用户

        修改VPN用户
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateVpnUser
        :type request: :class:`huaweicloudsdkvpn.v5.UpdateVpnUserRequest`
        :rtype: :class:`huaweicloudsdkvpn.v5.UpdateVpnUserResponse`
        """
        http_info = self._update_vpn_user_http_info(request)
        return self._call_api(**http_info)

    def update_vpn_user_async_invoker(self, request):
        http_info = self._update_vpn_user_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_vpn_user_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v5/{project_id}/p2c-vpn-gateways/vpn-servers/{vpn_server_id}/users/{user_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateVpnUserResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'vpn_server_id' in local_var_params:
            path_params['vpn_server_id'] = local_var_params['vpn_server_id']
        if 'user_id' in local_var_params:
            path_params['user_id'] = local_var_params['user_id']

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

    def update_vpn_user_password_async(self, request):
        r"""修改VPN用户密码

        修改VPN用户密码
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateVpnUserPassword
        :type request: :class:`huaweicloudsdkvpn.v5.UpdateVpnUserPasswordRequest`
        :rtype: :class:`huaweicloudsdkvpn.v5.UpdateVpnUserPasswordResponse`
        """
        http_info = self._update_vpn_user_password_http_info(request)
        return self._call_api(**http_info)

    def update_vpn_user_password_async_invoker(self, request):
        http_info = self._update_vpn_user_password_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_vpn_user_password_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v5/{project_id}/p2c-vpn-gateways/vpn-servers/{vpn_server_id}/users/{user_id}/password",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateVpnUserPasswordResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'vpn_server_id' in local_var_params:
            path_params['vpn_server_id'] = local_var_params['vpn_server_id']
        if 'user_id' in local_var_params:
            path_params['user_id'] = local_var_params['user_id']

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

    def add_vpn_users_to_group_async(self, request):
        r"""添加VPN用户到组

        添加VPN用户到组
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AddVpnUsersToGroup
        :type request: :class:`huaweicloudsdkvpn.v5.AddVpnUsersToGroupRequest`
        :rtype: :class:`huaweicloudsdkvpn.v5.AddVpnUsersToGroupResponse`
        """
        http_info = self._add_vpn_users_to_group_http_info(request)
        return self._call_api(**http_info)

    def add_vpn_users_to_group_async_invoker(self, request):
        http_info = self._add_vpn_users_to_group_http_info(request)
        return AsyncInvoker(self, http_info)

    def _add_vpn_users_to_group_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/{project_id}/p2c-vpn-gateways/vpn-servers/{vpn_server_id}/groups/{group_id}/add-users",
            "request_type": request.__class__.__name__,
            "response_type": "AddVpnUsersToGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'vpn_server_id' in local_var_params:
            path_params['vpn_server_id'] = local_var_params['vpn_server_id']
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']

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

    def create_vpn_user_group_async(self, request):
        r"""创建VPN用户组

        创建VPN用户组
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateVpnUserGroup
        :type request: :class:`huaweicloudsdkvpn.v5.CreateVpnUserGroupRequest`
        :rtype: :class:`huaweicloudsdkvpn.v5.CreateVpnUserGroupResponse`
        """
        http_info = self._create_vpn_user_group_http_info(request)
        return self._call_api(**http_info)

    def create_vpn_user_group_async_invoker(self, request):
        http_info = self._create_vpn_user_group_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_vpn_user_group_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/{project_id}/p2c-vpn-gateways/vpn-servers/{vpn_server_id}/groups",
            "request_type": request.__class__.__name__,
            "response_type": "CreateVpnUserGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'vpn_server_id' in local_var_params:
            path_params['vpn_server_id'] = local_var_params['vpn_server_id']

        query_params = []

        header_params = {}
        if 'x_client_token' in local_var_params:
            header_params['X-Client-Token'] = local_var_params['x_client_token']

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

    def delete_vpn_user_group_async(self, request):
        r"""删除VPN用户组

        删除VPN用户组
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteVpnUserGroup
        :type request: :class:`huaweicloudsdkvpn.v5.DeleteVpnUserGroupRequest`
        :rtype: :class:`huaweicloudsdkvpn.v5.DeleteVpnUserGroupResponse`
        """
        http_info = self._delete_vpn_user_group_http_info(request)
        return self._call_api(**http_info)

    def delete_vpn_user_group_async_invoker(self, request):
        http_info = self._delete_vpn_user_group_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_vpn_user_group_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v5/{project_id}/p2c-vpn-gateways/vpn-servers/{vpn_server_id}/groups/{group_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteVpnUserGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'vpn_server_id' in local_var_params:
            path_params['vpn_server_id'] = local_var_params['vpn_server_id']
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']

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

    def list_vpn_user_groups_async(self, request):
        r"""查询VPN用户组列表

        查询VPN用户组列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListVpnUserGroups
        :type request: :class:`huaweicloudsdkvpn.v5.ListVpnUserGroupsRequest`
        :rtype: :class:`huaweicloudsdkvpn.v5.ListVpnUserGroupsResponse`
        """
        http_info = self._list_vpn_user_groups_http_info(request)
        return self._call_api(**http_info)

    def list_vpn_user_groups_async_invoker(self, request):
        http_info = self._list_vpn_user_groups_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_vpn_user_groups_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/p2c-vpn-gateways/vpn-servers/{vpn_server_id}/groups",
            "request_type": request.__class__.__name__,
            "response_type": "ListVpnUserGroupsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'vpn_server_id' in local_var_params:
            path_params['vpn_server_id'] = local_var_params['vpn_server_id']

        query_params = []
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

    def list_vpn_users_in_group_async(self, request):
        r"""查询组内VPN用户

        查询组内VPN用户
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListVpnUsersInGroup
        :type request: :class:`huaweicloudsdkvpn.v5.ListVpnUsersInGroupRequest`
        :rtype: :class:`huaweicloudsdkvpn.v5.ListVpnUsersInGroupResponse`
        """
        http_info = self._list_vpn_users_in_group_http_info(request)
        return self._call_api(**http_info)

    def list_vpn_users_in_group_async_invoker(self, request):
        http_info = self._list_vpn_users_in_group_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_vpn_users_in_group_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/p2c-vpn-gateways/vpn-servers/{vpn_server_id}/groups/{group_id}/users",
            "request_type": request.__class__.__name__,
            "response_type": "ListVpnUsersInGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'vpn_server_id' in local_var_params:
            path_params['vpn_server_id'] = local_var_params['vpn_server_id']
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']

        query_params = []
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

    def remove_vpn_users_from_group_async(self, request):
        r"""删除组内VPN用户

        删除组内VPN用户
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RemoveVpnUsersFromGroup
        :type request: :class:`huaweicloudsdkvpn.v5.RemoveVpnUsersFromGroupRequest`
        :rtype: :class:`huaweicloudsdkvpn.v5.RemoveVpnUsersFromGroupResponse`
        """
        http_info = self._remove_vpn_users_from_group_http_info(request)
        return self._call_api(**http_info)

    def remove_vpn_users_from_group_async_invoker(self, request):
        http_info = self._remove_vpn_users_from_group_http_info(request)
        return AsyncInvoker(self, http_info)

    def _remove_vpn_users_from_group_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/{project_id}/p2c-vpn-gateways/vpn-servers/{vpn_server_id}/groups/{group_id}/remove-users",
            "request_type": request.__class__.__name__,
            "response_type": "RemoveVpnUsersFromGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'vpn_server_id' in local_var_params:
            path_params['vpn_server_id'] = local_var_params['vpn_server_id']
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']

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

    def show_vpn_user_group_async(self, request):
        r"""查询VPN用户组

        查询VPN用户组
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowVpnUserGroup
        :type request: :class:`huaweicloudsdkvpn.v5.ShowVpnUserGroupRequest`
        :rtype: :class:`huaweicloudsdkvpn.v5.ShowVpnUserGroupResponse`
        """
        http_info = self._show_vpn_user_group_http_info(request)
        return self._call_api(**http_info)

    def show_vpn_user_group_async_invoker(self, request):
        http_info = self._show_vpn_user_group_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_vpn_user_group_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/p2c-vpn-gateways/vpn-servers/{vpn_server_id}/groups/{group_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowVpnUserGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'vpn_server_id' in local_var_params:
            path_params['vpn_server_id'] = local_var_params['vpn_server_id']
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']

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

    def update_vpn_user_group_async(self, request):
        r"""修改VPN用户组

        修改VPN用户组
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateVpnUserGroup
        :type request: :class:`huaweicloudsdkvpn.v5.UpdateVpnUserGroupRequest`
        :rtype: :class:`huaweicloudsdkvpn.v5.UpdateVpnUserGroupResponse`
        """
        http_info = self._update_vpn_user_group_http_info(request)
        return self._call_api(**http_info)

    def update_vpn_user_group_async_invoker(self, request):
        http_info = self._update_vpn_user_group_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_vpn_user_group_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v5/{project_id}/p2c-vpn-gateways/vpn-servers/{vpn_server_id}/groups/{group_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateVpnUserGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'vpn_server_id' in local_var_params:
            path_params['vpn_server_id'] = local_var_params['vpn_server_id']
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']

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

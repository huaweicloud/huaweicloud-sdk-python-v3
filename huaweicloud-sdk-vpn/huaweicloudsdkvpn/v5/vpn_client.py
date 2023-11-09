# coding: utf-8

from __future__ import absolute_import

import importlib

from huaweicloudsdkcore.client import Client, ClientBuilder
from huaweicloudsdkcore.utils import http_utils
from huaweicloudsdkcore.sdk_stream_request import SdkStreamRequest


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
        return self._create_cgw_with_http_info(request)

    def _create_cgw_with_http_info(self, request):
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

        response_headers = ["header-response-token", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v5/{project_id}/customer-gateways',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateCgwResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_cgw(self, request):
        """删除对端网关

        根据对端网关ID，删除指定的对端网关
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteCgw
        :type request: :class:`huaweicloudsdkvpn.v5.DeleteCgwRequest`
        :rtype: :class:`huaweicloudsdkvpn.v5.DeleteCgwResponse`
        """
        return self._delete_cgw_with_http_info(request)

    def _delete_cgw_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'customer_gateway_id' in local_var_params:
            path_params['customer_gateway_id'] = local_var_params['customer_gateway_id']

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
            resource_path='/v5/{project_id}/customer-gateways/{customer_gateway_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteCgwResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_cgws(self, request):
        """查询对端网关列表

        查询对端网关列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListCgws
        :type request: :class:`huaweicloudsdkvpn.v5.ListCgwsRequest`
        :rtype: :class:`huaweicloudsdkvpn.v5.ListCgwsResponse`
        """
        return self._list_cgws_with_http_info(request)

    def _list_cgws_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v5/{project_id}/customer-gateways',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListCgwsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_cgw(self, request):
        """查询对端网关

        根据对端网关ID，查询指定的对端网关
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowCgw
        :type request: :class:`huaweicloudsdkvpn.v5.ShowCgwRequest`
        :rtype: :class:`huaweicloudsdkvpn.v5.ShowCgwResponse`
        """
        return self._show_cgw_with_http_info(request)

    def _show_cgw_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'customer_gateway_id' in local_var_params:
            path_params['customer_gateway_id'] = local_var_params['customer_gateway_id']

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
            resource_path='/v5/{project_id}/customer-gateways/{customer_gateway_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowCgwResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_cgw(self, request):
        """更新对端网关

        根据对端网关ID，更新指定的对端网关
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateCgw
        :type request: :class:`huaweicloudsdkvpn.v5.UpdateCgwRequest`
        :rtype: :class:`huaweicloudsdkvpn.v5.UpdateCgwResponse`
        """
        return self._update_cgw_with_http_info(request)

    def _update_cgw_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'customer_gateway_id' in local_var_params:
            path_params['customer_gateway_id'] = local_var_params['customer_gateway_id']

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
            resource_path='/v5/{project_id}/customer-gateways/{customer_gateway_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateCgwResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_vpn_connection(self, request):
        """创建VPN连接

        创建VPN连接，连接VPN网关与对端网关
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateVpnConnection
        :type request: :class:`huaweicloudsdkvpn.v5.CreateVpnConnectionRequest`
        :rtype: :class:`huaweicloudsdkvpn.v5.CreateVpnConnectionResponse`
        """
        return self._create_vpn_connection_with_http_info(request)

    def _create_vpn_connection_with_http_info(self, request):
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

        response_headers = ["header-response-token", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v5/{project_id}/vpn-connection',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateVpnConnectionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_vpn_connection(self, request):
        """删除VPN连接

        根据连接ID，删除指定的VPN连接
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteVpnConnection
        :type request: :class:`huaweicloudsdkvpn.v5.DeleteVpnConnectionRequest`
        :rtype: :class:`huaweicloudsdkvpn.v5.DeleteVpnConnectionResponse`
        """
        return self._delete_vpn_connection_with_http_info(request)

    def _delete_vpn_connection_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'vpn_connection_id' in local_var_params:
            path_params['vpn_connection_id'] = local_var_params['vpn_connection_id']

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
            resource_path='/v5/{project_id}/vpn-connection/{vpn_connection_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteVpnConnectionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_vpn_connections(self, request):
        """查询VPN连接列表

        查询VPN连接列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListVpnConnections
        :type request: :class:`huaweicloudsdkvpn.v5.ListVpnConnectionsRequest`
        :rtype: :class:`huaweicloudsdkvpn.v5.ListVpnConnectionsResponse`
        """
        return self._list_vpn_connections_with_http_info(request)

    def _list_vpn_connections_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["header-response-token", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v5/{project_id}/vpn-connection',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListVpnConnectionsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_vpn_connection(self, request):
        """查询VPN连接

        根据连接ID，查询指定的VPN连接的参数
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowVpnConnection
        :type request: :class:`huaweicloudsdkvpn.v5.ShowVpnConnectionRequest`
        :rtype: :class:`huaweicloudsdkvpn.v5.ShowVpnConnectionResponse`
        """
        return self._show_vpn_connection_with_http_info(request)

    def _show_vpn_connection_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'vpn_connection_id' in local_var_params:
            path_params['vpn_connection_id'] = local_var_params['vpn_connection_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["header-response-token", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v5/{project_id}/vpn-connection/{vpn_connection_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowVpnConnectionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_vpn_connection(self, request):
        """更新VPN连接

        根据连接ID，更新指定的VPN连接的参数
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateVpnConnection
        :type request: :class:`huaweicloudsdkvpn.v5.UpdateVpnConnectionRequest`
        :rtype: :class:`huaweicloudsdkvpn.v5.UpdateVpnConnectionResponse`
        """
        return self._update_vpn_connection_with_http_info(request)

    def _update_vpn_connection_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'vpn_connection_id' in local_var_params:
            path_params['vpn_connection_id'] = local_var_params['vpn_connection_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["header-response-token", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v5/{project_id}/vpn-connection/{vpn_connection_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateVpnConnectionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_vgw(self, request):
        """创建VPN网关

        创建一个VPN网关
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateVgw
        :type request: :class:`huaweicloudsdkvpn.v5.CreateVgwRequest`
        :rtype: :class:`huaweicloudsdkvpn.v5.CreateVgwResponse`
        """
        return self._create_vgw_with_http_info(request)

    def _create_vgw_with_http_info(self, request):
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

        response_headers = ["header-response-token", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v5/{project_id}/vpn-gateways',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateVgwResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_vgw(self, request):
        """删除VPN网关

        根据VPN网关ID，删除指定的VPN网关
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteVgw
        :type request: :class:`huaweicloudsdkvpn.v5.DeleteVgwRequest`
        :rtype: :class:`huaweicloudsdkvpn.v5.DeleteVgwResponse`
        """
        return self._delete_vgw_with_http_info(request)

    def _delete_vgw_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'vgw_id' in local_var_params:
            path_params['vgw_id'] = local_var_params['vgw_id']

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
            resource_path='/v5/{project_id}/vpn-gateways/{vgw_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteVgwResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_availability_zones(self, request):
        """查询VPN网关可用区

        查询VPN网关可用区
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAvailabilityZones
        :type request: :class:`huaweicloudsdkvpn.v5.ListAvailabilityZonesRequest`
        :rtype: :class:`huaweicloudsdkvpn.v5.ListAvailabilityZonesResponse`
        """
        return self._list_availability_zones_with_http_info(request)

    def _list_availability_zones_with_http_info(self, request):
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
            resource_path='/v5/{project_id}/vpn-gateways/availability-zones',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListAvailabilityZonesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_vgws(self, request):
        """查询VPN网关列表

        查询VPN网关列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListVgws
        :type request: :class:`huaweicloudsdkvpn.v5.ListVgwsRequest`
        :rtype: :class:`huaweicloudsdkvpn.v5.ListVgwsResponse`
        """
        return self._list_vgws_with_http_info(request)

    def _list_vgws_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v5/{project_id}/vpn-gateways',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListVgwsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_vgw(self, request):
        """查询VPN网关

        根据VPN网关ID，查询指定的VPN网关
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowVgw
        :type request: :class:`huaweicloudsdkvpn.v5.ShowVgwRequest`
        :rtype: :class:`huaweicloudsdkvpn.v5.ShowVgwResponse`
        """
        return self._show_vgw_with_http_info(request)

    def _show_vgw_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'vgw_id' in local_var_params:
            path_params['vgw_id'] = local_var_params['vgw_id']

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
            resource_path='/v5/{project_id}/vpn-gateways/{vgw_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowVgwResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_vgw(self, request):
        """更新VPN网关

        根据VPN网关ID，更新指定的VPN网关
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateVgw
        :type request: :class:`huaweicloudsdkvpn.v5.UpdateVgwRequest`
        :rtype: :class:`huaweicloudsdkvpn.v5.UpdateVgwResponse`
        """
        return self._update_vgw_with_http_info(request)

    def _update_vgw_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'vgw_id' in local_var_params:
            path_params['vgw_id'] = local_var_params['vgw_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["header-response-token", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v5/{project_id}/vpn-gateways/{vgw_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateVgwResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_vgw_certificate(self, request):
        """导入VPN网关证书

        导入租户VPN网关所使用的证书，包括签名证书、签名私钥、加密证书、加密私钥和CA证书链。当前只支持国密证书
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateVgwCertificate
        :type request: :class:`huaweicloudsdkvpn.v5.CreateVgwCertificateRequest`
        :rtype: :class:`huaweicloudsdkvpn.v5.CreateVgwCertificateResponse`
        """
        return self._create_vgw_certificate_with_http_info(request)

    def _create_vgw_certificate_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'vgw_id' in local_var_params:
            path_params['vgw_id'] = local_var_params['vgw_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["header-response-token", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v5/{project_id}/vpn-gateways/{vgw_id}/certificate',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateVgwCertificateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_vpn_gateway_certificate(self, request):
        """查询VPN网关证书

        根据VPN网关ID，查询所指定的VPN网关证书
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowVpnGatewayCertificate
        :type request: :class:`huaweicloudsdkvpn.v5.ShowVpnGatewayCertificateRequest`
        :rtype: :class:`huaweicloudsdkvpn.v5.ShowVpnGatewayCertificateResponse`
        """
        return self._show_vpn_gateway_certificate_with_http_info(request)

    def _show_vpn_gateway_certificate_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'vgw_id' in local_var_params:
            path_params['vgw_id'] = local_var_params['vgw_id']

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
            resource_path='/v5/{project_id}/vpn-gateways/{vgw_id}/certificate',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowVpnGatewayCertificateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_vgw_certificate(self, request):
        """更新VPN网关证书

        更新租户VPN网关所使用的证书，包括签名证书、签名私钥、加密证书、加密私钥和CA证书链。当前只支持国密证书
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateVgwCertificate
        :type request: :class:`huaweicloudsdkvpn.v5.UpdateVgwCertificateRequest`
        :rtype: :class:`huaweicloudsdkvpn.v5.UpdateVgwCertificateResponse`
        """
        return self._update_vgw_certificate_with_http_info(request)

    def _update_vgw_certificate_with_http_info(self, request):
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

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["header-response-token", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v5/{project_id}/vpn-gateways/{vgw_id}/certificate/{certificate_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateVgwCertificateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_quotas_info(self, request):
        """查询指定租户配额

        查询指定租户的配额
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowQuotasInfo
        :type request: :class:`huaweicloudsdkvpn.v5.ShowQuotasInfoRequest`
        :rtype: :class:`huaweicloudsdkvpn.v5.ShowQuotasInfoResponse`
        """
        return self._show_quotas_info_with_http_info(request)

    def _show_quotas_info_with_http_info(self, request):
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
            resource_path='/v5/{project_id}/vpn/quotas',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowQuotasInfoResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_connection_monitor(self, request):
        """创建VPN连接监控

        创建VPN连接监控
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateConnectionMonitor
        :type request: :class:`huaweicloudsdkvpn.v5.CreateConnectionMonitorRequest`
        :rtype: :class:`huaweicloudsdkvpn.v5.CreateConnectionMonitorResponse`
        """
        return self._create_connection_monitor_with_http_info(request)

    def _create_connection_monitor_with_http_info(self, request):
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

        response_headers = ["header-response-token", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v5/{project_id}/connection-monitors',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateConnectionMonitorResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_connection_monitor(self, request):
        """删除VPN连接监控

        根据VPN连接监控的ID，删除指定的VPN连接监控
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteConnectionMonitor
        :type request: :class:`huaweicloudsdkvpn.v5.DeleteConnectionMonitorRequest`
        :rtype: :class:`huaweicloudsdkvpn.v5.DeleteConnectionMonitorResponse`
        """
        return self._delete_connection_monitor_with_http_info(request)

    def _delete_connection_monitor_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'connection_monitor_id' in local_var_params:
            path_params['connection_monitor_id'] = local_var_params['connection_monitor_id']

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
            resource_path='/v5/{project_id}/connection-monitors/{connection_monitor_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteConnectionMonitorResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_connection_monitors(self, request):
        """查询VPN连接监控列表

        查询VPN连接监控列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListConnectionMonitors
        :type request: :class:`huaweicloudsdkvpn.v5.ListConnectionMonitorsRequest`
        :rtype: :class:`huaweicloudsdkvpn.v5.ListConnectionMonitorsResponse`
        """
        return self._list_connection_monitors_with_http_info(request)

    def _list_connection_monitors_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v5/{project_id}/connection-monitors',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListConnectionMonitorsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_connection_monitor(self, request):
        """查询VPN连接监控

        根据VPN连接监控的ID,查询指定的VPN连接监控
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowConnectionMonitor
        :type request: :class:`huaweicloudsdkvpn.v5.ShowConnectionMonitorRequest`
        :rtype: :class:`huaweicloudsdkvpn.v5.ShowConnectionMonitorResponse`
        """
        return self._show_connection_monitor_with_http_info(request)

    def _show_connection_monitor_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'connection_monitor_id' in local_var_params:
            path_params['connection_monitor_id'] = local_var_params['connection_monitor_id']

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
            resource_path='/v5/{project_id}/connection-monitors/{connection_monitor_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowConnectionMonitorResponse',
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

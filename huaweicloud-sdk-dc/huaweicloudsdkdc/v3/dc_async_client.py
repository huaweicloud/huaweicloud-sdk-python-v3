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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkdc'")


class DcAsyncClient(Client):
    def __init__(self):
        super(DcAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkdc.v3.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "DcAsyncClient":
                raise TypeError("client type error, support client type is DcAsyncClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def bind_global_eips_async(self, request):
        r"""绑定GEIP操作

        绑定GEIP操作
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BindGlobalEips
        :type request: :class:`huaweicloudsdkdc.v3.BindGlobalEipsRequest`
        :rtype: :class:`huaweicloudsdkdc.v3.BindGlobalEipsResponse`
        """
        http_info = self._bind_global_eips_http_info(request)
        return self._call_api(**http_info)

    def bind_global_eips_async_invoker(self, request):
        http_info = self._bind_global_eips_http_info(request)
        return AsyncInvoker(self, http_info)

    def _bind_global_eips_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/dcaas/connect-gateways/{connect_gateway_id}/binding-global-eips",
            "request_type": request.__class__.__name__,
            "response_type": "BindGlobalEipsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'connect_gateway_id' in local_var_params:
            path_params['connect_gateway_id'] = local_var_params['connect_gateway_id']

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

    def list_global_eips_async(self, request):
        r"""查询已经绑定的GEIP列表

        查询已经绑定的GEIP列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListGlobalEips
        :type request: :class:`huaweicloudsdkdc.v3.ListGlobalEipsRequest`
        :rtype: :class:`huaweicloudsdkdc.v3.ListGlobalEipsResponse`
        """
        http_info = self._list_global_eips_http_info(request)
        return self._call_api(**http_info)

    def list_global_eips_async_invoker(self, request):
        http_info = self._list_global_eips_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_global_eips_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/dcaas/connect-gateways/{connect_gateway_id}/binding-global-eips",
            "request_type": request.__class__.__name__,
            "response_type": "ListGlobalEipsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'connect_gateway_id' in local_var_params:
            path_params['connect_gateway_id'] = local_var_params['connect_gateway_id']

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
            query_params.append(('ext_fields', local_var_params['ext_fields']))
            collection_formats['ext_fields'] = 'multi'
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
            collection_formats['sort_dir'] = 'multi'
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
            collection_formats['status'] = 'multi'
        if 'global_eip_id' in local_var_params:
            query_params.append(('global_eip_id', local_var_params['global_eip_id']))
            collection_formats['global_eip_id'] = 'multi'
        if 'global_eip_segment_id' in local_var_params:
            query_params.append(('global_eip_segment_id', local_var_params['global_eip_segment_id']))
            collection_formats['global_eip_segment_id'] = 'multi'

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

    def unbind_global_eips_async(self, request):
        r"""解绑GEIP

        解绑GEIP
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UnbindGlobalEips
        :type request: :class:`huaweicloudsdkdc.v3.UnbindGlobalEipsRequest`
        :rtype: :class:`huaweicloudsdkdc.v3.UnbindGlobalEipsResponse`
        """
        http_info = self._unbind_global_eips_http_info(request)
        return self._call_api(**http_info)

    def unbind_global_eips_async_invoker(self, request):
        http_info = self._unbind_global_eips_http_info(request)
        return AsyncInvoker(self, http_info)

    def _unbind_global_eips_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/dcaas/connect-gateways/{connect_gateway_id}/unbinding-global-eips",
            "request_type": request.__class__.__name__,
            "response_type": "UnbindGlobalEipsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'connect_gateway_id' in local_var_params:
            path_params['connect_gateway_id'] = local_var_params['connect_gateway_id']

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

    def create_connect_gateway_async(self, request):
        r"""创建互联网关

        创建互联网关
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateConnectGateway
        :type request: :class:`huaweicloudsdkdc.v3.CreateConnectGatewayRequest`
        :rtype: :class:`huaweicloudsdkdc.v3.CreateConnectGatewayResponse`
        """
        http_info = self._create_connect_gateway_http_info(request)
        return self._call_api(**http_info)

    def create_connect_gateway_async_invoker(self, request):
        http_info = self._create_connect_gateway_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_connect_gateway_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/dcaas/connect-gateways",
            "request_type": request.__class__.__name__,
            "response_type": "CreateConnectGatewayResponse"
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

    def delete_connect_gateway_async(self, request):
        r"""删除互联网关

        删除互联网关
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteConnectGateway
        :type request: :class:`huaweicloudsdkdc.v3.DeleteConnectGatewayRequest`
        :rtype: :class:`huaweicloudsdkdc.v3.DeleteConnectGatewayResponse`
        """
        http_info = self._delete_connect_gateway_http_info(request)
        return self._call_api(**http_info)

    def delete_connect_gateway_async_invoker(self, request):
        http_info = self._delete_connect_gateway_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_connect_gateway_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{project_id}/dcaas/connect-gateways/{connect_gateway_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteConnectGatewayResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'connect_gateway_id' in local_var_params:
            path_params['connect_gateway_id'] = local_var_params['connect_gateway_id']

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

    def list_connect_gateways_async(self, request):
        r"""查询互联网关列表信息

        查询互联网关列表信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListConnectGateways
        :type request: :class:`huaweicloudsdkdc.v3.ListConnectGatewaysRequest`
        :rtype: :class:`huaweicloudsdkdc.v3.ListConnectGatewaysResponse`
        """
        http_info = self._list_connect_gateways_http_info(request)
        return self._call_api(**http_info)

    def list_connect_gateways_async_invoker(self, request):
        http_info = self._list_connect_gateways_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_connect_gateways_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/dcaas/connect-gateways",
            "request_type": request.__class__.__name__,
            "response_type": "ListConnectGatewaysResponse"
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
            query_params.append(('ext_fields', local_var_params['ext_fields']))
            collection_formats['ext_fields'] = 'multi'
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
            collection_formats['sort_dir'] = 'multi'
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
            collection_formats['id'] = 'multi'
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
            collection_formats['name'] = 'csv'
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

    def show_connect_gateway_async(self, request):
        r"""查询互联网关详细信息

        查询互联网关详细信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowConnectGateway
        :type request: :class:`huaweicloudsdkdc.v3.ShowConnectGatewayRequest`
        :rtype: :class:`huaweicloudsdkdc.v3.ShowConnectGatewayResponse`
        """
        http_info = self._show_connect_gateway_http_info(request)
        return self._call_api(**http_info)

    def show_connect_gateway_async_invoker(self, request):
        http_info = self._show_connect_gateway_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_connect_gateway_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/dcaas/connect-gateways/{connect_gateway_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowConnectGatewayResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'connect_gateway_id' in local_var_params:
            path_params['connect_gateway_id'] = local_var_params['connect_gateway_id']

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

    def update_connect_gateway_async(self, request):
        r"""更新互联网关

        更新互联网关
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateConnectGateway
        :type request: :class:`huaweicloudsdkdc.v3.UpdateConnectGatewayRequest`
        :rtype: :class:`huaweicloudsdkdc.v3.UpdateConnectGatewayResponse`
        """
        http_info = self._update_connect_gateway_http_info(request)
        return self._call_api(**http_info)

    def update_connect_gateway_async_invoker(self, request):
        http_info = self._update_connect_gateway_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_connect_gateway_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/dcaas/connect-gateways/{connect_gateway_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateConnectGatewayResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'connect_gateway_id' in local_var_params:
            path_params['connect_gateway_id'] = local_var_params['connect_gateway_id']

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

    def create_hosted_direct_connect_async(self, request):
        r"""创建托管专线连接

        用于合作伙伴用户最终租户创建托管专线
        创建者必须拥有合作伙伴资质，并且已经构建好运营(hosting)专线
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateHostedDirectConnect
        :type request: :class:`huaweicloudsdkdc.v3.CreateHostedDirectConnectRequest`
        :rtype: :class:`huaweicloudsdkdc.v3.CreateHostedDirectConnectResponse`
        """
        http_info = self._create_hosted_direct_connect_http_info(request)
        return self._call_api(**http_info)

    def create_hosted_direct_connect_async_invoker(self, request):
        http_info = self._create_hosted_direct_connect_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_hosted_direct_connect_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/dcaas/hosted-connects",
            "request_type": request.__class__.__name__,
            "response_type": "CreateHostedDirectConnectResponse"
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

    def delete_direct_connect_async(self, request):
        r"""删除物理连接

        删除物理连接，本接口只适用于按需计费物理专线，对于包周期购买的专线通过订单退订的方式删除物理连接
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteDirectConnect
        :type request: :class:`huaweicloudsdkdc.v3.DeleteDirectConnectRequest`
        :rtype: :class:`huaweicloudsdkdc.v3.DeleteDirectConnectResponse`
        """
        http_info = self._delete_direct_connect_http_info(request)
        return self._call_api(**http_info)

    def delete_direct_connect_async_invoker(self, request):
        http_info = self._delete_direct_connect_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_direct_connect_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{project_id}/dcaas/direct-connects/{direct_connect_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteDirectConnectResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'direct_connect_id' in local_var_params:
            path_params['direct_connect_id'] = local_var_params['direct_connect_id']

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

    def delete_hosted_direct_connect_async(self, request):
        r"""删除托管专线连接

        合作伙伴删除托管专线
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteHostedDirectConnect
        :type request: :class:`huaweicloudsdkdc.v3.DeleteHostedDirectConnectRequest`
        :rtype: :class:`huaweicloudsdkdc.v3.DeleteHostedDirectConnectResponse`
        """
        http_info = self._delete_hosted_direct_connect_http_info(request)
        return self._call_api(**http_info)

    def delete_hosted_direct_connect_async_invoker(self, request):
        http_info = self._delete_hosted_direct_connect_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_hosted_direct_connect_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{project_id}/dcaas/hosted-connects/{hosted_connect_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteHostedDirectConnectResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'hosted_connect_id' in local_var_params:
            path_params['hosted_connect_id'] = local_var_params['hosted_connect_id']

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

    def list_direct_connects_async(self, request):
        r"""查询物理连接列表

        查询租户创建的所有的direct connect对象.
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListDirectConnects
        :type request: :class:`huaweicloudsdkdc.v3.ListDirectConnectsRequest`
        :rtype: :class:`huaweicloudsdkdc.v3.ListDirectConnectsResponse`
        """
        http_info = self._list_direct_connects_http_info(request)
        return self._call_api(**http_info)

    def list_direct_connects_async_invoker(self, request):
        http_info = self._list_direct_connects_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_direct_connects_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/dcaas/direct-connects",
            "request_type": request.__class__.__name__,
            "response_type": "ListDirectConnectsResponse"
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
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
            collection_formats['sort_dir'] = 'multi'
        if 'hosting_id' in local_var_params:
            query_params.append(('hosting_id', local_var_params['hosting_id']))
            collection_formats['hosting_id'] = 'multi'
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
            collection_formats['enterprise_project_id'] = 'csv'
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
            collection_formats['id'] = 'multi'
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
            collection_formats['name'] = 'csv'

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

    def list_hosted_direct_connects_async(self, request):
        r"""查询租户的托管专线列表

        查询合作伙伴创建的托管专线连接列表.
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListHostedDirectConnects
        :type request: :class:`huaweicloudsdkdc.v3.ListHostedDirectConnectsRequest`
        :rtype: :class:`huaweicloudsdkdc.v3.ListHostedDirectConnectsResponse`
        """
        http_info = self._list_hosted_direct_connects_http_info(request)
        return self._call_api(**http_info)

    def list_hosted_direct_connects_async_invoker(self, request):
        http_info = self._list_hosted_direct_connects_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_hosted_direct_connects_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/dcaas/hosted-connects",
            "request_type": request.__class__.__name__,
            "response_type": "ListHostedDirectConnectsResponse"
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
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
            collection_formats['sort_dir'] = 'multi'
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
        if 'hosting_id' in local_var_params:
            query_params.append(('hosting_id', local_var_params['hosting_id']))
            collection_formats['hosting_id'] = 'multi'
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
            collection_formats['id'] = 'multi'
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
            collection_formats['name'] = 'csv'

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

    def show_direct_connect_async(self, request):
        r"""查询物理连接详情

        查询物理连接详细信息.
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowDirectConnect
        :type request: :class:`huaweicloudsdkdc.v3.ShowDirectConnectRequest`
        :rtype: :class:`huaweicloudsdkdc.v3.ShowDirectConnectResponse`
        """
        http_info = self._show_direct_connect_http_info(request)
        return self._call_api(**http_info)

    def show_direct_connect_async_invoker(self, request):
        http_info = self._show_direct_connect_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_direct_connect_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/dcaas/direct-connects/{direct_connect_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDirectConnectResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'direct_connect_id' in local_var_params:
            path_params['direct_connect_id'] = local_var_params['direct_connect_id']

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

    def show_hosted_direct_connect_async(self, request):
        r"""查询租户的托管专线详情

        查询合法作伙伴的Hosted专线类型.
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowHostedDirectConnect
        :type request: :class:`huaweicloudsdkdc.v3.ShowHostedDirectConnectRequest`
        :rtype: :class:`huaweicloudsdkdc.v3.ShowHostedDirectConnectResponse`
        """
        http_info = self._show_hosted_direct_connect_http_info(request)
        return self._call_api(**http_info)

    def show_hosted_direct_connect_async_invoker(self, request):
        http_info = self._show_hosted_direct_connect_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_hosted_direct_connect_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/dcaas/hosted-connects/{hosted_connect_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowHostedDirectConnectResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'hosted_connect_id' in local_var_params:
            path_params['hosted_connect_id'] = local_var_params['hosted_connect_id']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'fields' in local_var_params:
            query_params.append(('fields', local_var_params['fields']))
            collection_formats['fields'] = 'multi'
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
            collection_formats['sort_dir'] = 'multi'
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
        if 'hosting_id' in local_var_params:
            query_params.append(('hosting_id', local_var_params['hosting_id']))
            collection_formats['hosting_id'] = 'multi'

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

    def update_direct_connect_async(self, request):
        r"""更新物理连接信息

        更新物理连接信息，包括名字,描述等信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateDirectConnect
        :type request: :class:`huaweicloudsdkdc.v3.UpdateDirectConnectRequest`
        :rtype: :class:`huaweicloudsdkdc.v3.UpdateDirectConnectResponse`
        """
        http_info = self._update_direct_connect_http_info(request)
        return self._call_api(**http_info)

    def update_direct_connect_async_invoker(self, request):
        http_info = self._update_direct_connect_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_direct_connect_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/dcaas/direct-connects/{direct_connect_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateDirectConnectResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'direct_connect_id' in local_var_params:
            path_params['direct_connect_id'] = local_var_params['direct_connect_id']

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

    def update_hosted_direct_connect_async(self, request):
        r"""更新托管专线连接

        合作伙伴更新托管专线.
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateHostedDirectConnect
        :type request: :class:`huaweicloudsdkdc.v3.UpdateHostedDirectConnectRequest`
        :rtype: :class:`huaweicloudsdkdc.v3.UpdateHostedDirectConnectResponse`
        """
        http_info = self._update_hosted_direct_connect_http_info(request)
        return self._call_api(**http_info)

    def update_hosted_direct_connect_async_invoker(self, request):
        http_info = self._update_hosted_direct_connect_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_hosted_direct_connect_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/dcaas/hosted-connects/{hosted_connect_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateHostedDirectConnectResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'hosted_connect_id' in local_var_params:
            path_params['hosted_connect_id'] = local_var_params['hosted_connect_id']

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

    def list_direct_connect_locations_async(self, request):
        r"""查询专线接入点位置列表

        查询本区域下所有专线的接入点的信息，分页查询使用的参数为marker、limit。marker和limit一起使用时才会生效，单独使用无效
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListDirectConnectLocations
        :type request: :class:`huaweicloudsdkdc.v3.ListDirectConnectLocationsRequest`
        :rtype: :class:`huaweicloudsdkdc.v3.ListDirectConnectLocationsResponse`
        """
        http_info = self._list_direct_connect_locations_http_info(request)
        return self._call_api(**http_info)

    def list_direct_connect_locations_async_invoker(self, request):
        http_info = self._list_direct_connect_locations_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_direct_connect_locations_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/dcaas/direct-connect-locations",
            "request_type": request.__class__.__name__,
            "response_type": "ListDirectConnectLocationsResponse"
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
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
            collection_formats['sort_dir'] = 'multi'
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
            collection_formats['id'] = 'multi'
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
            collection_formats['name'] = 'csv'
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

    def show_direct_connect_location_async(self, request):
        r"""查询指定专线接入点详情

        查询指定的专线接入点详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowDirectConnectLocation
        :type request: :class:`huaweicloudsdkdc.v3.ShowDirectConnectLocationRequest`
        :rtype: :class:`huaweicloudsdkdc.v3.ShowDirectConnectLocationResponse`
        """
        http_info = self._show_direct_connect_location_http_info(request)
        return self._call_api(**http_info)

    def show_direct_connect_location_async_invoker(self, request):
        http_info = self._show_direct_connect_location_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_direct_connect_location_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/dcaas/direct-connect-locations/{direct_connect_location_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDirectConnectLocationResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'direct_connect_location_id' in local_var_params:
            path_params['direct_connect_location_id'] = local_var_params['direct_connect_location_id']

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

    def list_gdgw_route_tables_async(self, request):
        r"""查询全域接入网关路由表

        查询全域接入网关路由表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListGdgwRouteTables
        :type request: :class:`huaweicloudsdkdc.v3.ListGdgwRouteTablesRequest`
        :rtype: :class:`huaweicloudsdkdc.v3.ListGdgwRouteTablesResponse`
        """
        http_info = self._list_gdgw_route_tables_http_info(request)
        return self._call_api(**http_info)

    def list_gdgw_route_tables_async_invoker(self, request):
        http_info = self._list_gdgw_route_tables_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_gdgw_route_tables_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/dcaas/gdgw/{gdgw_id}/routetables",
            "request_type": request.__class__.__name__,
            "response_type": "ListGdgwRouteTablesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'gdgw_id' in local_var_params:
            path_params['gdgw_id'] = local_var_params['gdgw_id']

        query_params = []
        if 'fields' in local_var_params:
            query_params.append(('fields', local_var_params['fields']))
            collection_formats['fields'] = 'multi'
        if 'ext_fields' in local_var_params:
            query_params.append(('ext_fields', local_var_params['ext_fields']))
            collection_formats['ext_fields'] = 'multi'
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'nexthop' in local_var_params:
            query_params.append(('nexthop', local_var_params['nexthop']))
            collection_formats['nexthop'] = 'multi'
        if 'destination' in local_var_params:
            query_params.append(('destination', local_var_params['destination']))
            collection_formats['destination'] = 'multi'
        if 'address_family' in local_var_params:
            query_params.append(('address_family', local_var_params['address_family']))
            collection_formats['address_family'] = 'multi'

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

    def update_gdgw_route_table_async(self, request):
        r"""修改全域接入网关路由表

        支持的修改操作：新增、删除、修改
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateGdgwRouteTable
        :type request: :class:`huaweicloudsdkdc.v3.UpdateGdgwRouteTableRequest`
        :rtype: :class:`huaweicloudsdkdc.v3.UpdateGdgwRouteTableResponse`
        """
        http_info = self._update_gdgw_route_table_http_info(request)
        return self._call_api(**http_info)

    def update_gdgw_route_table_async_invoker(self, request):
        http_info = self._update_gdgw_route_table_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_gdgw_route_table_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/dcaas/gdgw/{gdgw_id}/routetables",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateGdgwRouteTableResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'gdgw_id' in local_var_params:
            path_params['gdgw_id'] = local_var_params['gdgw_id']

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

    def create_global_dc_gateway_async(self, request):
        r"""创建专线全域接入网关

        创建专线全域接入网关实例(global-dc-gateway)，用于接入全球的ER实例
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateGlobalDcGateway
        :type request: :class:`huaweicloudsdkdc.v3.CreateGlobalDcGatewayRequest`
        :rtype: :class:`huaweicloudsdkdc.v3.CreateGlobalDcGatewayResponse`
        """
        http_info = self._create_global_dc_gateway_http_info(request)
        return self._call_api(**http_info)

    def create_global_dc_gateway_async_invoker(self, request):
        http_info = self._create_global_dc_gateway_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_global_dc_gateway_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/dcaas/global-dc-gateways",
            "request_type": request.__class__.__name__,
            "response_type": "CreateGlobalDcGatewayResponse"
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

    def delete_global_dc_gateway_async(self, request):
        r"""删除专线全域接入网关

        删除专线全域接入网关global-dc-gateway实例
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteGlobalDcGateway
        :type request: :class:`huaweicloudsdkdc.v3.DeleteGlobalDcGatewayRequest`
        :rtype: :class:`huaweicloudsdkdc.v3.DeleteGlobalDcGatewayResponse`
        """
        http_info = self._delete_global_dc_gateway_http_info(request)
        return self._call_api(**http_info)

    def delete_global_dc_gateway_async_invoker(self, request):
        http_info = self._delete_global_dc_gateway_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_global_dc_gateway_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{project_id}/dcaas/global-dc-gateways/{global_dc_gateway_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteGlobalDcGatewayResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'global_dc_gateway_id' in local_var_params:
            path_params['global_dc_gateway_id'] = local_var_params['global_dc_gateway_id']

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

    def list_global_dc_gateways_async(self, request):
        r"""查询专线全域接入网关列表

        查询专线全域接入网关列表，建议使用分页查询 分页查询使用的参数为marker、limit。marker和limit一起使用时才会生效，单独使用无效
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListGlobalDcGateways
        :type request: :class:`huaweicloudsdkdc.v3.ListGlobalDcGatewaysRequest`
        :rtype: :class:`huaweicloudsdkdc.v3.ListGlobalDcGatewaysResponse`
        """
        http_info = self._list_global_dc_gateways_http_info(request)
        return self._call_api(**http_info)

    def list_global_dc_gateways_async_invoker(self, request):
        http_info = self._list_global_dc_gateways_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_global_dc_gateways_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/dcaas/global-dc-gateways",
            "request_type": request.__class__.__name__,
            "response_type": "ListGlobalDcGatewaysResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'fields' in local_var_params:
            query_params.append(('fields', local_var_params['fields']))
            collection_formats['fields'] = 'multi'
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
            collection_formats['sort_dir'] = 'multi'
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
            collection_formats['id'] = 'multi'
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
            collection_formats['name'] = 'csv'
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
            collection_formats['enterprise_project_id'] = 'csv'
        if 'site_network_id' in local_var_params:
            query_params.append(('site_network_id', local_var_params['site_network_id']))
            collection_formats['site_network_id'] = 'multi'
        if 'cloud_connection_id' in local_var_params:
            query_params.append(('cloud_connection_id', local_var_params['cloud_connection_id']))
            collection_formats['cloud_connection_id'] = 'multi'
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
            collection_formats['status'] = 'multi'
        if 'global_center_network_id' in local_var_params:
            query_params.append(('global_center_network_id', local_var_params['global_center_network_id']))
            collection_formats['global_center_network_id'] = 'multi'

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

    def show_global_dc_gateway_async(self, request):
        r"""查询专线全域接入网关详情

        查询专线全域接入网关实例详情信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowGlobalDcGateway
        :type request: :class:`huaweicloudsdkdc.v3.ShowGlobalDcGatewayRequest`
        :rtype: :class:`huaweicloudsdkdc.v3.ShowGlobalDcGatewayResponse`
        """
        http_info = self._show_global_dc_gateway_http_info(request)
        return self._call_api(**http_info)

    def show_global_dc_gateway_async_invoker(self, request):
        http_info = self._show_global_dc_gateway_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_global_dc_gateway_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/dcaas/global-dc-gateways/{global_dc_gateway_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowGlobalDcGatewayResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'global_dc_gateway_id' in local_var_params:
            path_params['global_dc_gateway_id'] = local_var_params['global_dc_gateway_id']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'fields' in local_var_params:
            query_params.append(('fields', local_var_params['fields']))
            collection_formats['fields'] = 'multi'
        if 'ext_fields' in local_var_params:
            query_params.append(('ext_fields', local_var_params['ext_fields']))
            collection_formats['ext_fields'] = 'multi'
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
            collection_formats['enterprise_project_id'] = 'csv'

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

    def update_global_dc_gateway_async(self, request):
        r"""更新专线全域接入网关

        更新专线全域接入网关global-dc-gateway的名字，描述等信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateGlobalDcGateway
        :type request: :class:`huaweicloudsdkdc.v3.UpdateGlobalDcGatewayRequest`
        :rtype: :class:`huaweicloudsdkdc.v3.UpdateGlobalDcGatewayResponse`
        """
        http_info = self._update_global_dc_gateway_http_info(request)
        return self._call_api(**http_info)

    def update_global_dc_gateway_async_invoker(self, request):
        http_info = self._update_global_dc_gateway_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_global_dc_gateway_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/dcaas/global-dc-gateways/{global_dc_gateway_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateGlobalDcGatewayResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'global_dc_gateway_id' in local_var_params:
            path_params['global_dc_gateway_id'] = local_var_params['global_dc_gateway_id']

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

    def create_peer_link_async(self, request):
        r"""创建专线关联连接

        创建专线全域接入网关的关联连接peer-link对象，用于连接企业路由器或者其他接入网关
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreatePeerLink
        :type request: :class:`huaweicloudsdkdc.v3.CreatePeerLinkRequest`
        :rtype: :class:`huaweicloudsdkdc.v3.CreatePeerLinkResponse`
        """
        http_info = self._create_peer_link_http_info(request)
        return self._call_api(**http_info)

    def create_peer_link_async_invoker(self, request):
        http_info = self._create_peer_link_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_peer_link_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/dcaas/global-dc-gateways/{global_dc_gateway_id}/peer-links",
            "request_type": request.__class__.__name__,
            "response_type": "CreatePeerLinkResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'global_dc_gateway_id' in local_var_params:
            path_params['global_dc_gateway_id'] = local_var_params['global_dc_gateway_id']

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

    def delete_peer_link_async(self, request):
        r"""删除专线关联连接

        删除全域接入网关与ER的关联连接peer-link
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeletePeerLink
        :type request: :class:`huaweicloudsdkdc.v3.DeletePeerLinkRequest`
        :rtype: :class:`huaweicloudsdkdc.v3.DeletePeerLinkResponse`
        """
        http_info = self._delete_peer_link_http_info(request)
        return self._call_api(**http_info)

    def delete_peer_link_async_invoker(self, request):
        http_info = self._delete_peer_link_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_peer_link_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{project_id}/dcaas/global-dc-gateways/{global_dc_gateway_id}/peer-links/{peer_link_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeletePeerLinkResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'global_dc_gateway_id' in local_var_params:
            path_params['global_dc_gateway_id'] = local_var_params['global_dc_gateway_id']
        if 'peer_link_id' in local_var_params:
            path_params['peer_link_id'] = local_var_params['peer_link_id']

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

    def list_peer_links_async(self, request):
        r"""查询专线关联连接列表

        查询全域接入网关与ER等对象的关联连接列表，分页查询使用的参数为marker、limit。marker和limit一起使用时才会生效，单独使用无效
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListPeerLinks
        :type request: :class:`huaweicloudsdkdc.v3.ListPeerLinksRequest`
        :rtype: :class:`huaweicloudsdkdc.v3.ListPeerLinksResponse`
        """
        http_info = self._list_peer_links_http_info(request)
        return self._call_api(**http_info)

    def list_peer_links_async_invoker(self, request):
        http_info = self._list_peer_links_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_peer_links_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/dcaas/global-dc-gateways/{global_dc_gateway_id}/peer-links",
            "request_type": request.__class__.__name__,
            "response_type": "ListPeerLinksResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'global_dc_gateway_id' in local_var_params:
            path_params['global_dc_gateway_id'] = local_var_params['global_dc_gateway_id']

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
            query_params.append(('ext_fields', local_var_params['ext_fields']))
            collection_formats['ext_fields'] = 'multi'
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
            collection_formats['sort_dir'] = 'multi'
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
            collection_formats['id'] = 'multi'
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
            collection_formats['name'] = 'csv'

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

    def show_peer_link_async(self, request):
        r"""查询专线关联连接详情

        查询指定接入网关的指定的关联连接(peer link)详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowPeerLink
        :type request: :class:`huaweicloudsdkdc.v3.ShowPeerLinkRequest`
        :rtype: :class:`huaweicloudsdkdc.v3.ShowPeerLinkResponse`
        """
        http_info = self._show_peer_link_http_info(request)
        return self._call_api(**http_info)

    def show_peer_link_async_invoker(self, request):
        http_info = self._show_peer_link_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_peer_link_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/dcaas/global-dc-gateways/{global_dc_gateway_id}/peer-links/{peer_link_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowPeerLinkResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'global_dc_gateway_id' in local_var_params:
            path_params['global_dc_gateway_id'] = local_var_params['global_dc_gateway_id']
        if 'peer_link_id' in local_var_params:
            path_params['peer_link_id'] = local_var_params['peer_link_id']

        query_params = []
        if 'fields' in local_var_params:
            query_params.append(('fields', local_var_params['fields']))
            collection_formats['fields'] = 'multi'
        if 'ext_fields' in local_var_params:
            query_params.append(('ext_fields', local_var_params['ext_fields']))
            collection_formats['ext_fields'] = 'multi'

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

    def update_peer_link_async(self, request):
        r"""更新专线关联连接

        更新接入网关与ER对接的关联连接peer-link
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdatePeerLink
        :type request: :class:`huaweicloudsdkdc.v3.UpdatePeerLinkRequest`
        :rtype: :class:`huaweicloudsdkdc.v3.UpdatePeerLinkResponse`
        """
        http_info = self._update_peer_link_http_info(request)
        return self._call_api(**http_info)

    def update_peer_link_async_invoker(self, request):
        http_info = self._update_peer_link_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_peer_link_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/dcaas/global-dc-gateways/{global_dc_gateway_id}/peer-links/{peer_link_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdatePeerLinkResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'global_dc_gateway_id' in local_var_params:
            path_params['global_dc_gateway_id'] = local_var_params['global_dc_gateway_id']
        if 'peer_link_id' in local_var_params:
            path_params['peer_link_id'] = local_var_params['peer_link_id']

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

    def show_quotas_async(self, request):
        r"""查询配额

        查询租户各类资源的使用情况，如Directconnect的使用量，虚拟接口的使用量等。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowQuotas
        :type request: :class:`huaweicloudsdkdc.v3.ShowQuotasRequest`
        :rtype: :class:`huaweicloudsdkdc.v3.ShowQuotasResponse`
        """
        http_info = self._show_quotas_http_info(request)
        return self._call_api(**http_info)

    def show_quotas_async_invoker(self, request):
        http_info = self._show_quotas_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_quotas_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/dcaas/quotas",
            "request_type": request.__class__.__name__,
            "response_type": "ShowQuotasResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
            collection_formats['type'] = 'multi'

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

    def batch_create_resource_tags_async(self, request):
        r"""批量添加删除资源标签

        - 为指定实例批量添加或删除标签
        - 标签管理服务需要使用该接口批量管理实例的标签。
        - 一个资源上最多有10个标签。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchCreateResourceTags
        :type request: :class:`huaweicloudsdkdc.v3.BatchCreateResourceTagsRequest`
        :rtype: :class:`huaweicloudsdkdc.v3.BatchCreateResourceTagsResponse`
        """
        http_info = self._batch_create_resource_tags_http_info(request)
        return self._call_api(**http_info)

    def batch_create_resource_tags_async_invoker(self, request):
        http_info = self._batch_create_resource_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_create_resource_tags_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/{resource_type}/{resource_id}/tags/action",
            "request_type": request.__class__.__name__,
            "response_type": "BatchCreateResourceTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_id' in local_var_params:
            path_params['resource_id'] = local_var_params['resource_id']
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

    def create_resource_tag_async(self, request):
        r"""添加资源标签

        - 一个资源上最多有10个标签。
        - 此接口为幂等接口：
        - 创建时，如果创建的标签已经存在（key相同），则覆盖。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateResourceTag
        :type request: :class:`huaweicloudsdkdc.v3.CreateResourceTagRequest`
        :rtype: :class:`huaweicloudsdkdc.v3.CreateResourceTagResponse`
        """
        http_info = self._create_resource_tag_http_info(request)
        return self._call_api(**http_info)

    def create_resource_tag_async_invoker(self, request):
        http_info = self._create_resource_tag_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_resource_tag_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/{resource_type}/{resource_id}/tags",
            "request_type": request.__class__.__name__,
            "response_type": "CreateResourceTagResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_id' in local_var_params:
            path_params['resource_id'] = local_var_params['resource_id']
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

    def delete_resource_tag_async(self, request):
        r"""删除资源标签

        删除时,不对标签字符集做校验，调用接口前必须要做encodeURI，服务端需要对接口uri做decodeURI。删除的key不存在报404，Key不能为空或者空字符串。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteResourceTag
        :type request: :class:`huaweicloudsdkdc.v3.DeleteResourceTagRequest`
        :rtype: :class:`huaweicloudsdkdc.v3.DeleteResourceTagResponse`
        """
        http_info = self._delete_resource_tag_http_info(request)
        return self._call_api(**http_info)

    def delete_resource_tag_async_invoker(self, request):
        http_info = self._delete_resource_tag_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_resource_tag_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{project_id}/{resource_type}/{resource_id}/tags/{key}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteResourceTagResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'key' in local_var_params:
            path_params['key'] = local_var_params['key']
        if 'resource_id' in local_var_params:
            path_params['resource_id'] = local_var_params['resource_id']
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

    def list_project_tags_async(self, request):
        r"""查询项目标签

        - 查询租户在指定Project中实例类型的所有资源标签集合。
        - 标签管理服务需要能够列出当前租户全部已使用的资源标签集合，为各服务打资源标签和过滤实例时提供标签联想功能。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListProjectTags
        :type request: :class:`huaweicloudsdkdc.v3.ListProjectTagsRequest`
        :rtype: :class:`huaweicloudsdkdc.v3.ListProjectTagsResponse`
        """
        http_info = self._list_project_tags_http_info(request)
        return self._call_api(**http_info)

    def list_project_tags_async_invoker(self, request):
        http_info = self._list_project_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_project_tags_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/{resource_type}/tags",
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

    def list_tag_resource_instances_async(self, request):
        r"""通过标签查询资源实例

        通过标签查询资源实例
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListTagResourceInstances
        :type request: :class:`huaweicloudsdkdc.v3.ListTagResourceInstancesRequest`
        :rtype: :class:`huaweicloudsdkdc.v3.ListTagResourceInstancesResponse`
        """
        http_info = self._list_tag_resource_instances_http_info(request)
        return self._call_api(**http_info)

    def list_tag_resource_instances_async_invoker(self, request):
        http_info = self._list_tag_resource_instances_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_tag_resource_instances_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/{resource_type}/resource-instances/action",
            "request_type": request.__class__.__name__,
            "response_type": "ListTagResourceInstancesResponse"
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

    def show_resource_tag_async(self, request):
        r"""查询资源标签

        查询资源标签
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowResourceTag
        :type request: :class:`huaweicloudsdkdc.v3.ShowResourceTagRequest`
        :rtype: :class:`huaweicloudsdkdc.v3.ShowResourceTagResponse`
        """
        http_info = self._show_resource_tag_http_info(request)
        return self._call_api(**http_info)

    def show_resource_tag_async_invoker(self, request):
        http_info = self._show_resource_tag_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_resource_tag_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/{resource_type}/{resource_id}/tags",
            "request_type": request.__class__.__name__,
            "response_type": "ShowResourceTagResponse"
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

    def create_virtual_gateway_async(self, request):
        r"""创建虚拟网关

        创建虚拟网关
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateVirtualGateway
        :type request: :class:`huaweicloudsdkdc.v3.CreateVirtualGatewayRequest`
        :rtype: :class:`huaweicloudsdkdc.v3.CreateVirtualGatewayResponse`
        """
        http_info = self._create_virtual_gateway_http_info(request)
        return self._call_api(**http_info)

    def create_virtual_gateway_async_invoker(self, request):
        http_info = self._create_virtual_gateway_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_virtual_gateway_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/dcaas/virtual-gateways",
            "request_type": request.__class__.__name__,
            "response_type": "CreateVirtualGatewayResponse"
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

    def delete_virtual_gateway_async(self, request):
        r"""删除虚拟网关

        删除指定的虚拟网关
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteVirtualGateway
        :type request: :class:`huaweicloudsdkdc.v3.DeleteVirtualGatewayRequest`
        :rtype: :class:`huaweicloudsdkdc.v3.DeleteVirtualGatewayResponse`
        """
        http_info = self._delete_virtual_gateway_http_info(request)
        return self._call_api(**http_info)

    def delete_virtual_gateway_async_invoker(self, request):
        http_info = self._delete_virtual_gateway_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_virtual_gateway_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{project_id}/dcaas/virtual-gateways/{virtual_gateway_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteVirtualGatewayResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'virtual_gateway_id' in local_var_params:
            path_params['virtual_gateway_id'] = local_var_params['virtual_gateway_id']

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

    def list_virtual_gateways_async(self, request):
        r"""查询虚拟网关列表

        查询虚拟网关列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListVirtualGateways
        :type request: :class:`huaweicloudsdkdc.v3.ListVirtualGatewaysRequest`
        :rtype: :class:`huaweicloudsdkdc.v3.ListVirtualGatewaysResponse`
        """
        http_info = self._list_virtual_gateways_http_info(request)
        return self._call_api(**http_info)

    def list_virtual_gateways_async_invoker(self, request):
        http_info = self._list_virtual_gateways_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_virtual_gateways_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/dcaas/virtual-gateways",
            "request_type": request.__class__.__name__,
            "response_type": "ListVirtualGatewaysResponse"
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
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
            collection_formats['sort_dir'] = 'multi'
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
            collection_formats['id'] = 'multi'
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
            collection_formats['enterprise_project_id'] = 'csv'
        if 'vpc_id' in local_var_params:
            query_params.append(('vpc_id', local_var_params['vpc_id']))
            collection_formats['vpc_id'] = 'multi'

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

    def show_virtual_gateway_async(self, request):
        r"""查询虚拟网关详情

        查询指定虚拟网关的详细信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowVirtualGateway
        :type request: :class:`huaweicloudsdkdc.v3.ShowVirtualGatewayRequest`
        :rtype: :class:`huaweicloudsdkdc.v3.ShowVirtualGatewayResponse`
        """
        http_info = self._show_virtual_gateway_http_info(request)
        return self._call_api(**http_info)

    def show_virtual_gateway_async_invoker(self, request):
        http_info = self._show_virtual_gateway_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_virtual_gateway_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/dcaas/virtual-gateways/{virtual_gateway_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowVirtualGatewayResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'virtual_gateway_id' in local_var_params:
            path_params['virtual_gateway_id'] = local_var_params['virtual_gateway_id']

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

    def update_virtual_gateway_async(self, request):
        r"""更新虚拟网关信息

        更新虚拟网关的信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateVirtualGateway
        :type request: :class:`huaweicloudsdkdc.v3.UpdateVirtualGatewayRequest`
        :rtype: :class:`huaweicloudsdkdc.v3.UpdateVirtualGatewayResponse`
        """
        http_info = self._update_virtual_gateway_http_info(request)
        return self._call_api(**http_info)

    def update_virtual_gateway_async_invoker(self, request):
        http_info = self._update_virtual_gateway_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_virtual_gateway_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/dcaas/virtual-gateways/{virtual_gateway_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateVirtualGatewayResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'virtual_gateway_id' in local_var_params:
            path_params['virtual_gateway_id'] = local_var_params['virtual_gateway_id']

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

    def create_vif_peer_async(self, request):
        r"""创建虚拟接口对等体

        每个虚拟接口可支持两个对等体，IPv4和IPv6对等体，在创建虚拟接口时默认创建IPv4对等体， 本接口一般用于增加ipv6对等体。创建虚拟接口对接体之后，可以通过虚拟接口查询配置结果 本接口只在支持Ipv6的区域开放，如需要使用请联系客服
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateVifPeer
        :type request: :class:`huaweicloudsdkdc.v3.CreateVifPeerRequest`
        :rtype: :class:`huaweicloudsdkdc.v3.CreateVifPeerResponse`
        """
        http_info = self._create_vif_peer_http_info(request)
        return self._call_api(**http_info)

    def create_vif_peer_async_invoker(self, request):
        http_info = self._create_vif_peer_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_vif_peer_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/dcaas/vif-peers",
            "request_type": request.__class__.__name__,
            "response_type": "CreateVifPeerResponse"
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

    def create_virtual_interface_async(self, request):
        r"""创建虚拟接口

        虚拟接口配置物理专线上与客户互联的IP和路由等相关信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateVirtualInterface
        :type request: :class:`huaweicloudsdkdc.v3.CreateVirtualInterfaceRequest`
        :rtype: :class:`huaweicloudsdkdc.v3.CreateVirtualInterfaceResponse`
        """
        http_info = self._create_virtual_interface_http_info(request)
        return self._call_api(**http_info)

    def create_virtual_interface_async_invoker(self, request):
        http_info = self._create_virtual_interface_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_virtual_interface_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/dcaas/virtual-interfaces",
            "request_type": request.__class__.__name__,
            "response_type": "CreateVirtualInterfaceResponse"
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

    def delete_vif_peer_async(self, request):
        r"""删除虚拟接口对应的对等体

        删除虚拟接口对等体信息,虚拟接口至少要含一个对等体，最后一个对等体不能删除 本接口只在支持Ipv6的区域开放，如需要使用请联系客服
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteVifPeer
        :type request: :class:`huaweicloudsdkdc.v3.DeleteVifPeerRequest`
        :rtype: :class:`huaweicloudsdkdc.v3.DeleteVifPeerResponse`
        """
        http_info = self._delete_vif_peer_http_info(request)
        return self._call_api(**http_info)

    def delete_vif_peer_async_invoker(self, request):
        http_info = self._delete_vif_peer_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_vif_peer_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{project_id}/dcaas/vif-peers/{vif_peer_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteVifPeerResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'vif_peer_id' in local_var_params:
            path_params['vif_peer_id'] = local_var_params['vif_peer_id']

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

    def delete_virtual_interface_async(self, request):
        r"""删除虚拟接口

        删除虚拟接口
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteVirtualInterface
        :type request: :class:`huaweicloudsdkdc.v3.DeleteVirtualInterfaceRequest`
        :rtype: :class:`huaweicloudsdkdc.v3.DeleteVirtualInterfaceResponse`
        """
        http_info = self._delete_virtual_interface_http_info(request)
        return self._call_api(**http_info)

    def delete_virtual_interface_async_invoker(self, request):
        http_info = self._delete_virtual_interface_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_virtual_interface_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{project_id}/dcaas/virtual-interfaces/{virtual_interface_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteVirtualInterfaceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'virtual_interface_id' in local_var_params:
            path_params['virtual_interface_id'] = local_var_params['virtual_interface_id']

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

    def list_switchover_test_records_async(self, request):
        r"""查询虚拟接口倒换测试记录列表

        查询倒换测试记录列表，只展示operate_status为COMPELTE的记录。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListSwitchoverTestRecords
        :type request: :class:`huaweicloudsdkdc.v3.ListSwitchoverTestRecordsRequest`
        :rtype: :class:`huaweicloudsdkdc.v3.ListSwitchoverTestRecordsResponse`
        """
        http_info = self._list_switchover_test_records_http_info(request)
        return self._call_api(**http_info)

    def list_switchover_test_records_async_invoker(self, request):
        http_info = self._list_switchover_test_records_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_switchover_test_records_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/dcaas/switchover-test",
            "request_type": request.__class__.__name__,
            "response_type": "ListSwitchoverTestRecordsResponse"
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
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
            collection_formats['sort_dir'] = 'multi'
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
        if 'resource_id' in local_var_params:
            query_params.append(('resource_id', local_var_params['resource_id']))
            collection_formats['resource_id'] = 'multi'

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

    def list_virtual_interfaces_async(self, request):
        r"""查询虚拟接口列表

        查询租户所有的虚拟接口列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListVirtualInterfaces
        :type request: :class:`huaweicloudsdkdc.v3.ListVirtualInterfacesRequest`
        :rtype: :class:`huaweicloudsdkdc.v3.ListVirtualInterfacesResponse`
        """
        http_info = self._list_virtual_interfaces_http_info(request)
        return self._call_api(**http_info)

    def list_virtual_interfaces_async_invoker(self, request):
        http_info = self._list_virtual_interfaces_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_virtual_interfaces_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/dcaas/virtual-interfaces",
            "request_type": request.__class__.__name__,
            "response_type": "ListVirtualInterfacesResponse"
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
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
            collection_formats['sort_dir'] = 'multi'
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
            collection_formats['enterprise_project_id'] = 'csv'
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
            collection_formats['id'] = 'multi'
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
            collection_formats['status'] = 'multi'
        if 'direct_connect_id' in local_var_params:
            query_params.append(('direct_connect_id', local_var_params['direct_connect_id']))
            collection_formats['direct_connect_id'] = 'multi'
        if 'vgw_id' in local_var_params:
            query_params.append(('vgw_id', local_var_params['vgw_id']))
            collection_formats['vgw_id'] = 'multi'

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

    def show_virtual_interface_async(self, request):
        r"""查询虚拟接口详情

        查询虚拟接口详细信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowVirtualInterface
        :type request: :class:`huaweicloudsdkdc.v3.ShowVirtualInterfaceRequest`
        :rtype: :class:`huaweicloudsdkdc.v3.ShowVirtualInterfaceResponse`
        """
        http_info = self._show_virtual_interface_http_info(request)
        return self._call_api(**http_info)

    def show_virtual_interface_async_invoker(self, request):
        http_info = self._show_virtual_interface_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_virtual_interface_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/dcaas/virtual-interfaces/{virtual_interface_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowVirtualInterfaceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'virtual_interface_id' in local_var_params:
            path_params['virtual_interface_id'] = local_var_params['virtual_interface_id']

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

    def switchover_test_async(self, request):
        r"""执行虚拟接口倒换测试

        客户双专线接入，需要支持双线自动倒换，方便进行功能测试。 虚拟接口进行倒换测试会导致接口关闭，业务流量中断。 对于虚拟接口，支持“关闭接口”和“开放接口”两种操作。 1、关闭接口：下发shutdown命令，关闭接口； 2、开放接口：下发undo_shutdown命令，使能接口。 倒换测试选择shutdown时，虚拟接口的状态为ADMIN_SHUTDOWN，此状态不允许虚拟接口的其他操作。 倒换测试选择undo_shutdown时，虚拟接口的状态为ACTIVE。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for SwitchoverTest
        :type request: :class:`huaweicloudsdkdc.v3.SwitchoverTestRequest`
        :rtype: :class:`huaweicloudsdkdc.v3.SwitchoverTestResponse`
        """
        http_info = self._switchover_test_http_info(request)
        return self._call_api(**http_info)

    def switchover_test_async_invoker(self, request):
        http_info = self._switchover_test_http_info(request)
        return AsyncInvoker(self, http_info)

    def _switchover_test_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/dcaas/switchover-test",
            "request_type": request.__class__.__name__,
            "response_type": "SwitchoverTestResponse"
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

    def update_vif_peer_async(self, request):
        r"""更新虚拟接口对等体

        更新虚拟接口对等体信息,包括远端子网，名字和描述等。 本接口只在支持Ipv6的区域开放，如需要使用请联系客服
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateVifPeer
        :type request: :class:`huaweicloudsdkdc.v3.UpdateVifPeerRequest`
        :rtype: :class:`huaweicloudsdkdc.v3.UpdateVifPeerResponse`
        """
        http_info = self._update_vif_peer_http_info(request)
        return self._call_api(**http_info)

    def update_vif_peer_async_invoker(self, request):
        http_info = self._update_vif_peer_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_vif_peer_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/dcaas/vif-peers/{vif_peer_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateVifPeerResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'vif_peer_id' in local_var_params:
            path_params['vif_peer_id'] = local_var_params['vif_peer_id']

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

    def update_virtual_interface_async(self, request):
        r"""更新虚拟接口

        更新虚拟接口的详细信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateVirtualInterface
        :type request: :class:`huaweicloudsdkdc.v3.UpdateVirtualInterfaceRequest`
        :rtype: :class:`huaweicloudsdkdc.v3.UpdateVirtualInterfaceResponse`
        """
        http_info = self._update_virtual_interface_http_info(request)
        return self._call_api(**http_info)

    def update_virtual_interface_async_invoker(self, request):
        http_info = self._update_virtual_interface_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_virtual_interface_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/dcaas/virtual-interfaces/{virtual_interface_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateVirtualInterfaceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'virtual_interface_id' in local_var_params:
            path_params['virtual_interface_id'] = local_var_params['virtual_interface_id']

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

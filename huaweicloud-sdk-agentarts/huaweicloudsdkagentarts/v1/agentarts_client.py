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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkagentarts'")


class AgentArtsClient(Client):
    def __init__(self):
        super().__init__()
        self.model_package = importlib.import_module("huaweicloudsdkagentarts.v1.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "AgentArtsClient":
                raise TypeError("client type error, support client type is AgentArtsClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def create_core_gateway(self, request):
        r"""创建网关

        使用指定配置创建一个新的网关。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateCoreGateway
        :type request: :class:`huaweicloudsdkagentarts.v1.CreateCoreGatewayRequest`
        :rtype: :class:`huaweicloudsdkagentarts.v1.CreateCoreGatewayResponse`
        """
        http_info = self._create_core_gateway_http_info(request)
        return self._call_api(**http_info)

    def create_core_gateway_invoker(self, request):
        http_info = self._create_core_gateway_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_core_gateway_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/core/gateways",
            "request_type": request.__class__.__name__,
            "response_type": "CreateCoreGatewayResponse"
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

        auth_settings = ['api_key']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_core_gateway(self, request):
        r"""删除网关

        永久删除指定 ID 的网关。此操作无法撤销。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteCoreGateway
        :type request: :class:`huaweicloudsdkagentarts.v1.DeleteCoreGatewayRequest`
        :rtype: :class:`huaweicloudsdkagentarts.v1.DeleteCoreGatewayResponse`
        """
        http_info = self._delete_core_gateway_http_info(request)
        return self._call_api(**http_info)

    def delete_core_gateway_invoker(self, request):
        http_info = self._delete_core_gateway_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_core_gateway_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/core/gateways/{gateway_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteCoreGatewayResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'gateway_id' in local_var_params:
            path_params['gateway_id'] = local_var_params['gateway_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['api_key']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_core_gateways(self, request):
        r"""列出所有网关

        检索所有网关的列表，支持可选的过滤和分页功能。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListCoreGateways
        :type request: :class:`huaweicloudsdkagentarts.v1.ListCoreGatewaysRequest`
        :rtype: :class:`huaweicloudsdkagentarts.v1.ListCoreGatewaysResponse`
        """
        http_info = self._list_core_gateways_http_info(request)
        return self._call_api(**http_info)

    def list_core_gateways_invoker(self, request):
        http_info = self._list_core_gateways_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_core_gateways_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/core/gateways",
            "request_type": request.__class__.__name__,
            "response_type": "ListCoreGatewaysResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'gateway_id' in local_var_params:
            query_params.append(('gateway_id', local_var_params['gateway_id']))
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

        auth_settings = ['api_key']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_core_gateway(self, request):
        r"""获取网关详情

        通过 ID 获取指定网关的详细信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowCoreGateway
        :type request: :class:`huaweicloudsdkagentarts.v1.ShowCoreGatewayRequest`
        :rtype: :class:`huaweicloudsdkagentarts.v1.ShowCoreGatewayResponse`
        """
        http_info = self._show_core_gateway_http_info(request)
        return self._call_api(**http_info)

    def show_core_gateway_invoker(self, request):
        http_info = self._show_core_gateway_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_core_gateway_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/core/gateways/{gateway_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowCoreGatewayResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'gateway_id' in local_var_params:
            path_params['gateway_id'] = local_var_params['gateway_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['api_key']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_core_gateway(self, request):
        r"""更新网关

        使用新配置更新现有网关。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateCoreGateway
        :type request: :class:`huaweicloudsdkagentarts.v1.UpdateCoreGatewayRequest`
        :rtype: :class:`huaweicloudsdkagentarts.v1.UpdateCoreGatewayResponse`
        """
        http_info = self._update_core_gateway_http_info(request)
        return self._call_api(**http_info)

    def update_core_gateway_invoker(self, request):
        http_info = self._update_core_gateway_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_core_gateway_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/core/gateways/{gateway_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateCoreGatewayResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'gateway_id' in local_var_params:
            path_params['gateway_id'] = local_var_params['gateway_id']

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

        auth_settings = ['api_key']

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

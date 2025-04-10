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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkidentitycenteroidc'")


class IdentityCenterOIDCClient(Client):
    def __init__(self):
        super(IdentityCenterOIDCClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkidentitycenteroidc.v1.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls, "IdentityCenterOIDCCredentials")
        else:
            if clazz.__name__ != "IdentityCenterOIDCClient":
                raise TypeError("client type error, support client type is IdentityCenterOIDCClient")
            client_builder = ClientBuilder(clazz, "IdentityCenterOIDCCredentials")

        

        return client_builder

    def register_client(self, request):
        r"""注册客户端

        向IAM身份中心注册客户端，这允许客户端启动设备授权，输出应该持久化以便于身份验证请求重用
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RegisterClient
        :type request: :class:`huaweicloudsdkidentitycenteroidc.v1.RegisterClientRequest`
        :rtype: :class:`huaweicloudsdkidentitycenteroidc.v1.RegisterClientResponse`
        """
        http_info = self._register_client_http_info(request)
        return self._call_api(**http_info)

    def register_client_invoker(self, request):
        http_info = self._register_client_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _register_client_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/clients",
            "request_type": request.__class__.__name__,
            "response_type": "RegisterClientResponse"
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

    def start_device_authorization(self, request):
        r"""请求设备授权

        发起设备授权请求
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for StartDeviceAuthorization
        :type request: :class:`huaweicloudsdkidentitycenteroidc.v1.StartDeviceAuthorizationRequest`
        :rtype: :class:`huaweicloudsdkidentitycenteroidc.v1.StartDeviceAuthorizationResponse`
        """
        http_info = self._start_device_authorization_http_info(request)
        return self._call_api(**http_info)

    def start_device_authorization_invoker(self, request):
        http_info = self._start_device_authorization_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _start_device_authorization_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/device/authorize",
            "request_type": request.__class__.__name__,
            "response_type": "StartDeviceAuthorizationResponse"
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

    def create_token(self, request):
        r"""创建令牌

        获取访问令牌
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateToken
        :type request: :class:`huaweicloudsdkidentitycenteroidc.v1.CreateTokenRequest`
        :rtype: :class:`huaweicloudsdkidentitycenteroidc.v1.CreateTokenResponse`
        """
        http_info = self._create_token_http_info(request)
        return self._call_api(**http_info)

    def create_token_invoker(self, request):
        http_info = self._create_token_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_token_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/tokens",
            "request_type": request.__class__.__name__,
            "response_type": "CreateTokenResponse"
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

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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkorgid'")


class OrgIDClient(Client):
    def __init__(self):
        super(OrgIDClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkorgid.v1.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls, "GlobalCredentials")
        else:
            if clazz.__name__ != "OrgIDClient":
                raise TypeError("client type error, support client type is OrgIDClient")
            client_builder = ClientBuilder(clazz, "GlobalCredentials")

        

        return client_builder

    def validate_service(self, request):
        r"""验证票据接口

        CAS 3.0验证票据接口
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ValidateService
        :type request: :class:`huaweicloudsdkorgid.v1.ValidateServiceRequest`
        :rtype: :class:`huaweicloudsdkorgid.v1.ValidateServiceResponse`
        """
        http_info = self._validate_service_http_info(request)
        return self._call_api(**http_info)

    def validate_service_invoker(self, request):
        http_info = self._validate_service_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _validate_service_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/orgid/openapi/v1/cas/p3/serviceValidate",
            "request_type": request.__class__.__name__,
            "response_type": "ValidateServiceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'service' in local_var_params:
            query_params.append(('service', local_var_params['service']))
        if 'ticket' in local_var_params:
            query_params.append(('ticket', local_var_params['ticket']))

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

    def show_oauth2_token(self, request):
        r"""用户级Token获取

        用户级Token获取
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowOauth2Token
        :type request: :class:`huaweicloudsdkorgid.v1.ShowOauth2TokenRequest`
        :rtype: :class:`huaweicloudsdkorgid.v1.ShowOauth2TokenResponse`
        """
        http_info = self._show_oauth2_token_http_info(request)
        return self._call_api(**http_info)

    def show_oauth2_token_invoker(self, request):
        http_info = self._show_oauth2_token_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_oauth2_token_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/orgid/openapi/v1/oauth2/token",
            "request_type": request.__class__.__name__,
            "response_type": "ShowOauth2TokenResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}
        if 'grant_type' in local_var_params:
            form_params['grant_type'] = local_var_params['grant_type']
        if 'code' in local_var_params:
            form_params['code'] = local_var_params['code']
        if 'client_id' in local_var_params:
            form_params['client_id'] = local_var_params['client_id']
        if 'client_secret' in local_var_params:
            form_params['client_secret'] = local_var_params['client_secret']
        if 'redirect_uri' in local_var_params:
            form_params['redirect_uri'] = local_var_params['redirect_uri']
        if 'access_type' in local_var_params:
            form_params['access_type'] = local_var_params['access_type']

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['multipart/form-data'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_oauth2_user_info(self, request):
        r"""用户信息获取

        用户级Token获取
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowOauth2UserInfo
        :type request: :class:`huaweicloudsdkorgid.v1.ShowOauth2UserInfoRequest`
        :rtype: :class:`huaweicloudsdkorgid.v1.ShowOauth2UserInfoResponse`
        """
        http_info = self._show_oauth2_user_info_http_info(request)
        return self._call_api(**http_info)

    def show_oauth2_user_info_invoker(self, request):
        http_info = self._show_oauth2_user_info_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_oauth2_user_info_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/orgid/openapi/v1/oauth2/userinfo",
            "request_type": request.__class__.__name__,
            "response_type": "ShowOauth2UserInfoResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_org_id_authorization' in local_var_params:
            header_params['X-OrgID-Authorization'] = local_var_params['x_org_id_authorization']

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

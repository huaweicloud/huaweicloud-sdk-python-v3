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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdksts'")


class StsAsyncClient(Client):
    def __init__(self):
        super().__init__()
        self.model_package = importlib.import_module("huaweicloudsdksts.v1.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "StsAsyncClient":
                raise TypeError("client type error, support client type is StsAsyncClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def assume_agency_async(self, request):
        r"""通过委托或者信任委托获取临时安全凭证

        通过委托或者信任委托获取临时安全凭证，临时安全凭证可用于对云资源发起访问。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AssumeAgency
        :type request: :class:`huaweicloudsdksts.v1.AssumeAgencyRequest`
        :rtype: :class:`huaweicloudsdksts.v1.AssumeAgencyResponse`
        """
        http_info = self._assume_agency_http_info(request)
        return self._call_api(**http_info)

    def assume_agency_async_invoker(self, request):
        http_info = self._assume_agency_http_info(request)
        return AsyncInvoker(self, http_info)

    def _assume_agency_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/agencies/assume",
            "request_type": request.__class__.__name__,
            "response_type": "AssumeAgencyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_security_token' in local_var_params:
            header_params['X-Security-Token'] = local_var_params['x_security_token']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['AccessKeySignature']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def assume_agency_with_oidc_async(self, request):
        r"""通过使用OIDC协议SSO的信任委托获取临时安全凭证

        为通过 OIDC 身份提供商令牌验证的用户返回一组临时安全凭证。此操作提供了一种机制，可以让外部的任何兼容 OIDC 身份提供商使用信任委托的临时安全凭证华为云访问，而无需使用 IAM 用户的凭证。
        
        **会话持续时间：**
        默认情况下，通过 AssumeAgencyWithOIDC 创建的临时安全凭证有效期为一小时。您可以使用可选的 duration_seconds 参数来指定会话的持续时间，duration_seconds 取值范围是从 900 秒（15 分钟）到该信任委托设置的最大会话持续时长，最大会话持续时长的取值范围可以从 1 小时到 12 小时。注意：委托链会将您的会话持续时间限制为最多一小时，当您使用 AssumeAgency API 操作来进行委托链的切换时，如果您提供了大于一小时的 duration_seconds 参数值，该操作将会失败。
        
        **权限：**
        调用 AssumeAgencyWithOIDC 不需要使用华为云凭证。调用者的身份是通过使用您 JWKS 端点中的公钥进行验证的。
        您可以使用 policy 和 policy_ids 参数传递自定义策略和已有的身份策略来限制本次会话获得的临时安全凭证的权限范围，最终获得临时安全凭证的权限是 policy 和 policy_ids 与信任委托身上附加的身份策略的交集。
        
        **标签：**
        在信任委托的信任策略中添加了 sts::tagSession 授权项时，您可以配置您的身份提供商，将属性作为会话标签传递到您的 ID Token 中。每个会话标签由一个键（Key）和一个值（Value）组成。您最多可以传递 20 个会话标签。纯文本形式的会话标签键不得超过 128 个字符，值不得超过 255 个字符。您也可以传递与信任委托身上标签同名的会话标签，此时会话标签会覆盖具有相同键的信任委托标签。您可以将会话标签设置为可传递的 (Transitive)，可传递的会话标签在角色链期间会持续保留。
        
        **身份：**
        在您的应用程序可以调用 AssumeAgencyWithOIDC 之前，您必须使用您的账号在 IAM 中创建 OIDC 提供商和信任委托，并在信任委托的信任策略中指定该 OIDC 提供商，然后还需要配置您的 OIDC 身份提供商以颁发 IAM 所需的 ID Token。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AssumeAgencyWithOIDC
        :type request: :class:`huaweicloudsdksts.v1.AssumeAgencyWithOIDCRequest`
        :rtype: :class:`huaweicloudsdksts.v1.AssumeAgencyWithOIDCResponse`
        """
        http_info = self._assume_agency_with_oidc_http_info(request)
        return self._call_api(**http_info)

    def assume_agency_with_oidc_async_invoker(self, request):
        http_info = self._assume_agency_with_oidc_http_info(request)
        return AsyncInvoker(self, http_info)

    def _assume_agency_with_oidc_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/agencies/assume-with-oidc",
            "request_type": request.__class__.__name__,
            "response_type": "AssumeAgencyWithOIDCResponse"
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

    def assume_agency_with_saml_async(self, request):
        r"""通过使用SAML协议SSO的信任委托获取临时安全凭证

        为通过 SAML 身份验证响应（SAML Authentication Response）验证的用户返回一组临时安全凭证。此操作提供了一种机制，可以让外部的 SAML 身份提供商使用信任委托的临时安全凭证华为云访问，而无需使用 IAM 用户的凭证。
        
        **会话持续时间：**
        默认情况下，通过 AssumeAgencyWithSAML 创建的临时安全凭证有效期为一小时。您可以使用可选的 duration_seconds 参数或者 SAML 身份验证响应中 SessionNotOnOrAfter 值和 SessionDuration 值来指定会话的持续时间，最终的会话持续时间以三者中较短的一个为准，且会话的持续时间不能超过委托设置的最大会话时长限制。duration_seconds 取值范围是从 900 秒（15 分钟）到该信任委托设置的最大会话持续时长，最大会话持续时长的取值范围可以从 1 小时到 12 小时。注意：委托链会将您的会话持续时间限制为最多一小时，当您使用 AssumeAgency API 操作来进行委托链的切换时，如果您提供了大于一小时的 duration_seconds 参数值，该操作将会失败。
        
        **权限：**
        调用 AssumeAgencyWithSAML 不需要使用华为云凭证。调用者的身份是通过使用您上传的 SAML 提供商元数据文档中的密钥进行验证的。
        您可以使用 policy 和 policy_ids 参数传递自定义策略和已有的身份策略来限制本次会话获得的临时安全凭证的权限范围，最终获得临时安全凭证的权限是 policy 和 policy_ids 与信任委托身上附加的身份策略的交集。
        
        **标签：**
        在信任委托的信任策略中添加了 sts::tagSession 授权项时，您可以配置您的身份提供商，将属性作为会话标签 (Session Tags) 传递到 SAML 断言中。每个会话标签由一个键（Key）和一个值（Value）组成。您最多可以传递 20 个会话标签。纯文本形式的会话标签键不得超过 128 个字符，值不得超过 255 个字符。您也可以传递与信任委托身上标签同名的会话标签，此时会话标签会覆盖具有相同键的信任委托标签。您可以将会话标签设置为可传递的 (Transitive)，可传递的会话标签在角色链期间会持续保留。
        
        **SAML 配置：**
        在您的应用程序调用 AssumeAgencyWithSAML 之前，您必须使用您的账号在 IAM 中创建 SAML 提供商和信任委托，并在信任委托的信任策略中指定该 SAML 提供商，然后还需要配置您的 SAML 身份提供商以发布 IAM 所需的声明 (Claims)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AssumeAgencyWithSAML
        :type request: :class:`huaweicloudsdksts.v1.AssumeAgencyWithSAMLRequest`
        :rtype: :class:`huaweicloudsdksts.v1.AssumeAgencyWithSAMLResponse`
        """
        http_info = self._assume_agency_with_saml_http_info(request)
        return self._call_api(**http_info)

    def assume_agency_with_saml_async_invoker(self, request):
        http_info = self._assume_agency_with_saml_http_info(request)
        return AsyncInvoker(self, http_info)

    def _assume_agency_with_saml_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/agencies/assume-with-saml",
            "request_type": request.__class__.__name__,
            "response_type": "AssumeAgencyWithSAMLResponse"
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

    def decode_authorization_message_async(self, request):
        r"""解密鉴权失败的原因

        解密鉴权失败的原因。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DecodeAuthorizationMessage
        :type request: :class:`huaweicloudsdksts.v1.DecodeAuthorizationMessageRequest`
        :rtype: :class:`huaweicloudsdksts.v1.DecodeAuthorizationMessageResponse`
        """
        http_info = self._decode_authorization_message_http_info(request)
        return self._call_api(**http_info)

    def decode_authorization_message_async_invoker(self, request):
        http_info = self._decode_authorization_message_http_info(request)
        return AsyncInvoker(self, http_info)

    def _decode_authorization_message_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/decode-authorization-message",
            "request_type": request.__class__.__name__,
            "response_type": "DecodeAuthorizationMessageResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_security_token' in local_var_params:
            header_params['X-Security-Token'] = local_var_params['x_security_token']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['AccessKeySignature']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def get_caller_identity_async(self, request):
        r"""获取调用者身份信息

        获取调用者（用户，委托等）身份信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for GetCallerIdentity
        :type request: :class:`huaweicloudsdksts.v1.GetCallerIdentityRequest`
        :rtype: :class:`huaweicloudsdksts.v1.GetCallerIdentityResponse`
        """
        http_info = self._get_caller_identity_http_info(request)
        return self._call_api(**http_info)

    def get_caller_identity_async_invoker(self, request):
        http_info = self._get_caller_identity_http_info(request)
        return AsyncInvoker(self, http_info)

    def _get_caller_identity_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/caller-identity",
            "request_type": request.__class__.__name__,
            "response_type": "GetCallerIdentityResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_security_token' in local_var_params:
            header_params['X-Security-Token'] = local_var_params['x_security_token']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['AccessKeySignature']

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

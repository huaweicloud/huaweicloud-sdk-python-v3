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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkagentidentity'")


class AgentIdentityAsyncClient(Client):
    def __init__(self):
        super().__init__()
        self.model_package = importlib.import_module("huaweicloudsdkagentidentity.v1.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "AgentIdentityAsyncClient":
                raise TypeError("client type error, support client type is AgentIdentityAsyncClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def create_api_key_credential_provider_async(self, request):
        r"""创建API密钥凭证提供者

        Creates a new API key credential provider.
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateApiKeyCredentialProvider
        :type request: :class:`huaweicloudsdkagentidentity.v1.CreateApiKeyCredentialProviderRequest`
        :rtype: :class:`huaweicloudsdkagentidentity.v1.CreateApiKeyCredentialProviderResponse`
        """
        http_info = self._create_api_key_credential_provider_http_info(request)
        return self._call_api(**http_info)

    def create_api_key_credential_provider_async_invoker(self, request):
        http_info = self._create_api_key_credential_provider_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_api_key_credential_provider_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/api-key-credential-providers",
            "request_type": request.__class__.__name__,
            "response_type": "CreateApiKeyCredentialProviderResponse"
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

        auth_settings = ['AccessKeyAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_api_key_credential_provider_async(self, request):
        r"""删除API密钥凭证提供者

        Deletes an API key credential provider.
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteApiKeyCredentialProvider
        :type request: :class:`huaweicloudsdkagentidentity.v1.DeleteApiKeyCredentialProviderRequest`
        :rtype: :class:`huaweicloudsdkagentidentity.v1.DeleteApiKeyCredentialProviderResponse`
        """
        http_info = self._delete_api_key_credential_provider_http_info(request)
        return self._call_api(**http_info)

    def delete_api_key_credential_provider_async_invoker(self, request):
        http_info = self._delete_api_key_credential_provider_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_api_key_credential_provider_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/api-key-credential-providers/{credential_provider_name}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteApiKeyCredentialProviderResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'credential_provider_name' in local_var_params:
            path_params['credential_provider_name'] = local_var_params['credential_provider_name']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['AccessKeyAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def get_api_key_credential_provider_async(self, request):
        r"""查询API密钥凭证提供者详情

        Gets details of an API key credential provider.
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for GetApiKeyCredentialProvider
        :type request: :class:`huaweicloudsdkagentidentity.v1.GetApiKeyCredentialProviderRequest`
        :rtype: :class:`huaweicloudsdkagentidentity.v1.GetApiKeyCredentialProviderResponse`
        """
        http_info = self._get_api_key_credential_provider_http_info(request)
        return self._call_api(**http_info)

    def get_api_key_credential_provider_async_invoker(self, request):
        http_info = self._get_api_key_credential_provider_http_info(request)
        return AsyncInvoker(self, http_info)

    def _get_api_key_credential_provider_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/api-key-credential-providers/{credential_provider_name}",
            "request_type": request.__class__.__name__,
            "response_type": "GetApiKeyCredentialProviderResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'credential_provider_name' in local_var_params:
            path_params['credential_provider_name'] = local_var_params['credential_provider_name']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['AccessKeyAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_api_key_credential_providers_async(self, request):
        r"""查询API密钥凭证提供者列表

        Lists API key credential providers.
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListApiKeyCredentialProviders
        :type request: :class:`huaweicloudsdkagentidentity.v1.ListApiKeyCredentialProvidersRequest`
        :rtype: :class:`huaweicloudsdkagentidentity.v1.ListApiKeyCredentialProvidersResponse`
        """
        http_info = self._list_api_key_credential_providers_http_info(request)
        return self._call_api(**http_info)

    def list_api_key_credential_providers_async_invoker(self, request):
        http_info = self._list_api_key_credential_providers_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_api_key_credential_providers_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/api-key-credential-providers",
            "request_type": request.__class__.__name__,
            "response_type": "ListApiKeyCredentialProvidersResponse"
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

        auth_settings = ['AccessKeyAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_api_key_credential_provider_async(self, request):
        r"""更新API密钥凭证提供者

        Updates the API key of an existing API key credential provider.
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateApiKeyCredentialProvider
        :type request: :class:`huaweicloudsdkagentidentity.v1.UpdateApiKeyCredentialProviderRequest`
        :rtype: :class:`huaweicloudsdkagentidentity.v1.UpdateApiKeyCredentialProviderResponse`
        """
        http_info = self._update_api_key_credential_provider_http_info(request)
        return self._call_api(**http_info)

    def update_api_key_credential_provider_async_invoker(self, request):
        http_info = self._update_api_key_credential_provider_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_api_key_credential_provider_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/api-key-credential-providers/{credential_provider_name}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateApiKeyCredentialProviderResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'credential_provider_name' in local_var_params:
            path_params['credential_provider_name'] = local_var_params['credential_provider_name']

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

        auth_settings = ['AccessKeyAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def complete_resource_token_auth_async(self, request):
        r"""Confirm user authentication session for OAuth2.0 tokens

        Confirms the user authentication session to obtain OAuth2.0 tokens for a resource
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CompleteResourceTokenAuth
        :type request: :class:`huaweicloudsdkagentidentity.v1.CompleteResourceTokenAuthRequest`
        :rtype: :class:`huaweicloudsdkagentidentity.v1.CompleteResourceTokenAuthResponse`
        """
        http_info = self._complete_resource_token_auth_http_info(request)
        return self._call_api(**http_info)

    def complete_resource_token_auth_async_invoker(self, request):
        http_info = self._complete_resource_token_auth_http_info(request)
        return AsyncInvoker(self, http_info)

    def _complete_resource_token_auth_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/resource-token-auth/complete",
            "request_type": request.__class__.__name__,
            "response_type": "CompleteResourceTokenAuthResponse"
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

        auth_settings = ['AccessKeyAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def get_resource_api_key_async(self, request):
        r"""Retrieve API key from resource credential provider

        Retrieves the API key associated with a specified resource credential provider
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for GetResourceApiKey
        :type request: :class:`huaweicloudsdkagentidentity.v1.GetResourceApiKeyRequest`
        :rtype: :class:`huaweicloudsdkagentidentity.v1.GetResourceApiKeyResponse`
        """
        http_info = self._get_resource_api_key_http_info(request)
        return self._call_api(**http_info)

    def get_resource_api_key_async_invoker(self, request):
        http_info = self._get_resource_api_key_http_info(request)
        return AsyncInvoker(self, http_info)

    def _get_resource_api_key_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/api-key",
            "request_type": request.__class__.__name__,
            "response_type": "GetResourceApiKeyResponse"
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

        auth_settings = ['AccessKeyAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def get_resource_oauth2_token_async(self, request):
        r"""Retrieve OAuth2.0 token from resource credential provider

        Returns the OAuth2.0 token for the specified resource using the configured flow
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for GetResourceOauth2Token
        :type request: :class:`huaweicloudsdkagentidentity.v1.GetResourceOauth2TokenRequest`
        :rtype: :class:`huaweicloudsdkagentidentity.v1.GetResourceOauth2TokenResponse`
        """
        http_info = self._get_resource_oauth2_token_http_info(request)
        return self._call_api(**http_info)

    def get_resource_oauth2_token_async_invoker(self, request):
        http_info = self._get_resource_oauth2_token_http_info(request)
        return AsyncInvoker(self, http_info)

    def _get_resource_oauth2_token_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/oauth2/token",
            "request_type": request.__class__.__name__,
            "response_type": "GetResourceOauth2TokenResponse"
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

        auth_settings = ['AccessKeyAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def get_resource_sts_token_async(self, request):
        r"""Retrieve STS credentials from STS credential provider

        Retrieves temporary STS credentials from a specified STS credential provider
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for GetResourceStsToken
        :type request: :class:`huaweicloudsdkagentidentity.v1.GetResourceStsTokenRequest`
        :rtype: :class:`huaweicloudsdkagentidentity.v1.GetResourceStsTokenResponse`
        """
        http_info = self._get_resource_sts_token_http_info(request)
        return self._call_api(**http_info)

    def get_resource_sts_token_async_invoker(self, request):
        http_info = self._get_resource_sts_token_http_info(request)
        return AsyncInvoker(self, http_info)

    def _get_resource_sts_token_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/sts/token",
            "request_type": request.__class__.__name__,
            "response_type": "GetResourceStsTokenResponse"
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

        auth_settings = ['AccessKeyAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def oauth2_authorize_async(self, request):
        r"""OAuth2.0 Pushed Authorization Request (PAR) standard authorize API

        Core OAuth2 authorization endpoint following RFC 9126 PAR spec, only accepts authorization request via request_uri parameter to trigger user authorization flow
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for Oauth2Authorize
        :type request: :class:`huaweicloudsdkagentidentity.v1.Oauth2AuthorizeRequest`
        :rtype: :class:`huaweicloudsdkagentidentity.v1.Oauth2AuthorizeResponse`
        """
        http_info = self._oauth2_authorize_http_info(request)
        return self._call_api(**http_info)

    def oauth2_authorize_async_invoker(self, request):
        http_info = self._oauth2_authorize_http_info(request)
        return AsyncInvoker(self, http_info)

    def _oauth2_authorize_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/oauth2/authorize",
            "request_type": request.__class__.__name__,
            "response_type": "Oauth2AuthorizeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'request_uri' in local_var_params:
            query_params.append(('request_uri', local_var_params['request_uri']))

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

    def oauth2_callback_async(self, request):
        r"""OAuth2.0 Standard Authorization Callback API

        OAuth2 redirect callback endpoint to receive authorization result after user consent/denial
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for Oauth2Callback
        :type request: :class:`huaweicloudsdkagentidentity.v1.Oauth2CallbackRequest`
        :rtype: :class:`huaweicloudsdkagentidentity.v1.Oauth2CallbackResponse`
        """
        http_info = self._oauth2_callback_http_info(request)
        return self._call_api(**http_info)

    def oauth2_callback_async_invoker(self, request):
        http_info = self._oauth2_callback_http_info(request)
        return AsyncInvoker(self, http_info)

    def _oauth2_callback_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/oauth2/callback/{credential_provider_id}",
            "request_type": request.__class__.__name__,
            "response_type": "Oauth2CallbackResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'credential_provider_id' in local_var_params:
            path_params['credential_provider_id'] = local_var_params['credential_provider_id']

        query_params = []
        if 'code' in local_var_params:
            query_params.append(('code', local_var_params['code']))
        if 'state' in local_var_params:
            query_params.append(('state', local_var_params['state']))
        if 'error' in local_var_params:
            query_params.append(('error', local_var_params['error']))
        if 'error_description' in local_var_params:
            query_params.append(('error_description', local_var_params['error_description']))

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

    def create_oauth2_credential_provider_async(self, request):
        r"""创建OAuth2凭证提供者

        Creates a new OAuth2 credential provider.
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateOauth2CredentialProvider
        :type request: :class:`huaweicloudsdkagentidentity.v1.CreateOauth2CredentialProviderRequest`
        :rtype: :class:`huaweicloudsdkagentidentity.v1.CreateOauth2CredentialProviderResponse`
        """
        http_info = self._create_oauth2_credential_provider_http_info(request)
        return self._call_api(**http_info)

    def create_oauth2_credential_provider_async_invoker(self, request):
        http_info = self._create_oauth2_credential_provider_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_oauth2_credential_provider_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/oauth2-credential-providers",
            "request_type": request.__class__.__name__,
            "response_type": "CreateOauth2CredentialProviderResponse"
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

        auth_settings = ['AccessKeyAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_oauth2_credential_provider_async(self, request):
        r"""删除OAuth2凭证提供者

        Deletes an OAuth2 credential provider.
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteOauth2CredentialProvider
        :type request: :class:`huaweicloudsdkagentidentity.v1.DeleteOauth2CredentialProviderRequest`
        :rtype: :class:`huaweicloudsdkagentidentity.v1.DeleteOauth2CredentialProviderResponse`
        """
        http_info = self._delete_oauth2_credential_provider_http_info(request)
        return self._call_api(**http_info)

    def delete_oauth2_credential_provider_async_invoker(self, request):
        http_info = self._delete_oauth2_credential_provider_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_oauth2_credential_provider_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/oauth2-credential-providers/{credential_provider_name}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteOauth2CredentialProviderResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'credential_provider_name' in local_var_params:
            path_params['credential_provider_name'] = local_var_params['credential_provider_name']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['AccessKeyAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def get_oauth2_credential_provider_async(self, request):
        r"""查询OAuth2凭证提供者详情

        Gets details of an OAuth2 credential provider.
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for GetOauth2CredentialProvider
        :type request: :class:`huaweicloudsdkagentidentity.v1.GetOauth2CredentialProviderRequest`
        :rtype: :class:`huaweicloudsdkagentidentity.v1.GetOauth2CredentialProviderResponse`
        """
        http_info = self._get_oauth2_credential_provider_http_info(request)
        return self._call_api(**http_info)

    def get_oauth2_credential_provider_async_invoker(self, request):
        http_info = self._get_oauth2_credential_provider_http_info(request)
        return AsyncInvoker(self, http_info)

    def _get_oauth2_credential_provider_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/oauth2-credential-providers/{credential_provider_name}",
            "request_type": request.__class__.__name__,
            "response_type": "GetOauth2CredentialProviderResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'credential_provider_name' in local_var_params:
            path_params['credential_provider_name'] = local_var_params['credential_provider_name']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['AccessKeyAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_oauth2_credential_providers_async(self, request):
        r"""查询OAuth2凭证提供者列表

        Lists OAuth2 credential providers.
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListOauth2CredentialProviders
        :type request: :class:`huaweicloudsdkagentidentity.v1.ListOauth2CredentialProvidersRequest`
        :rtype: :class:`huaweicloudsdkagentidentity.v1.ListOauth2CredentialProvidersResponse`
        """
        http_info = self._list_oauth2_credential_providers_http_info(request)
        return self._call_api(**http_info)

    def list_oauth2_credential_providers_async_invoker(self, request):
        http_info = self._list_oauth2_credential_providers_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_oauth2_credential_providers_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/oauth2-credential-providers",
            "request_type": request.__class__.__name__,
            "response_type": "ListOauth2CredentialProvidersResponse"
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

        auth_settings = ['AccessKeyAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_oauth2_credential_provider_async(self, request):
        r"""更新OAuth2凭证提供者

        Updates an existing OAuth2 credential provider.
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateOauth2CredentialProvider
        :type request: :class:`huaweicloudsdkagentidentity.v1.UpdateOauth2CredentialProviderRequest`
        :rtype: :class:`huaweicloudsdkagentidentity.v1.UpdateOauth2CredentialProviderResponse`
        """
        http_info = self._update_oauth2_credential_provider_http_info(request)
        return self._call_api(**http_info)

    def update_oauth2_credential_provider_async_invoker(self, request):
        http_info = self._update_oauth2_credential_provider_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_oauth2_credential_provider_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/oauth2-credential-providers/{credential_provider_name}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateOauth2CredentialProviderResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'credential_provider_name' in local_var_params:
            path_params['credential_provider_name'] = local_var_params['credential_provider_name']

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

        auth_settings = ['AccessKeyAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_sts_credential_provider_async(self, request):
        r"""创建STS凭证提供者

        Creates a new STS credential provider.
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateStsCredentialProvider
        :type request: :class:`huaweicloudsdkagentidentity.v1.CreateStsCredentialProviderRequest`
        :rtype: :class:`huaweicloudsdkagentidentity.v1.CreateStsCredentialProviderResponse`
        """
        http_info = self._create_sts_credential_provider_http_info(request)
        return self._call_api(**http_info)

    def create_sts_credential_provider_async_invoker(self, request):
        http_info = self._create_sts_credential_provider_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_sts_credential_provider_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/sts-credential-providers",
            "request_type": request.__class__.__name__,
            "response_type": "CreateStsCredentialProviderResponse"
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

        auth_settings = ['AccessKeyAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_sts_credential_provider_async(self, request):
        r"""删除STS凭证提供者

        Deletes an STS credential provider.
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteStsCredentialProvider
        :type request: :class:`huaweicloudsdkagentidentity.v1.DeleteStsCredentialProviderRequest`
        :rtype: :class:`huaweicloudsdkagentidentity.v1.DeleteStsCredentialProviderResponse`
        """
        http_info = self._delete_sts_credential_provider_http_info(request)
        return self._call_api(**http_info)

    def delete_sts_credential_provider_async_invoker(self, request):
        http_info = self._delete_sts_credential_provider_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_sts_credential_provider_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/sts-credential-providers/{credential_provider_name}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteStsCredentialProviderResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'credential_provider_name' in local_var_params:
            path_params['credential_provider_name'] = local_var_params['credential_provider_name']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['AccessKeyAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def get_sts_credential_provider_async(self, request):
        r"""查询STS凭证提供者详情

        Gets details of an STS credential provider.
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for GetStsCredentialProvider
        :type request: :class:`huaweicloudsdkagentidentity.v1.GetStsCredentialProviderRequest`
        :rtype: :class:`huaweicloudsdkagentidentity.v1.GetStsCredentialProviderResponse`
        """
        http_info = self._get_sts_credential_provider_http_info(request)
        return self._call_api(**http_info)

    def get_sts_credential_provider_async_invoker(self, request):
        http_info = self._get_sts_credential_provider_http_info(request)
        return AsyncInvoker(self, http_info)

    def _get_sts_credential_provider_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/sts-credential-providers/{credential_provider_name}",
            "request_type": request.__class__.__name__,
            "response_type": "GetStsCredentialProviderResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'credential_provider_name' in local_var_params:
            path_params['credential_provider_name'] = local_var_params['credential_provider_name']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['AccessKeyAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_sts_credential_providers_async(self, request):
        r"""查询STS凭证提供者列表

        Lists STS credential providers.
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListStsCredentialProviders
        :type request: :class:`huaweicloudsdkagentidentity.v1.ListStsCredentialProvidersRequest`
        :rtype: :class:`huaweicloudsdkagentidentity.v1.ListStsCredentialProvidersResponse`
        """
        http_info = self._list_sts_credential_providers_http_info(request)
        return self._call_api(**http_info)

    def list_sts_credential_providers_async_invoker(self, request):
        http_info = self._list_sts_credential_providers_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_sts_credential_providers_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/sts-credential-providers",
            "request_type": request.__class__.__name__,
            "response_type": "ListStsCredentialProvidersResponse"
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

        auth_settings = ['AccessKeyAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_sts_credential_provider_async(self, request):
        r"""更新STS凭证提供者

        Updates an existing STS credential provider.
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateStsCredentialProvider
        :type request: :class:`huaweicloudsdkagentidentity.v1.UpdateStsCredentialProviderRequest`
        :rtype: :class:`huaweicloudsdkagentidentity.v1.UpdateStsCredentialProviderResponse`
        """
        http_info = self._update_sts_credential_provider_http_info(request)
        return self._call_api(**http_info)

    def update_sts_credential_provider_async_invoker(self, request):
        http_info = self._update_sts_credential_provider_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_sts_credential_provider_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/sts-credential-providers/{credential_provider_name}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateStsCredentialProviderResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'credential_provider_name' in local_var_params:
            path_params['credential_provider_name'] = local_var_params['credential_provider_name']

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

        auth_settings = ['AccessKeyAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def get_token_vault_async(self, request):
        r"""查询令牌保管库详情

        Gets details of a token vault.
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for GetTokenVault
        :type request: :class:`huaweicloudsdkagentidentity.v1.GetTokenVaultRequest`
        :rtype: :class:`huaweicloudsdkagentidentity.v1.GetTokenVaultResponse`
        """
        http_info = self._get_token_vault_http_info(request)
        return self._call_api(**http_info)

    def get_token_vault_async_invoker(self, request):
        http_info = self._get_token_vault_http_info(request)
        return AsyncInvoker(self, http_info)

    def _get_token_vault_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/token-vaults/{token_vault_id}",
            "request_type": request.__class__.__name__,
            "response_type": "GetTokenVaultResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'token_vault_id' in local_var_params:
            path_params['token_vault_id'] = local_var_params['token_vault_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['AccessKeyAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_workload_access_token_async(self, request):
        r"""Create workload access token (not acting on behalf of a user)

        Retrieves a workload access token for agentic workloads that do not act on behalf of a user
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateWorkloadAccessToken
        :type request: :class:`huaweicloudsdkagentidentity.v1.CreateWorkloadAccessTokenRequest`
        :rtype: :class:`huaweicloudsdkagentidentity.v1.CreateWorkloadAccessTokenResponse`
        """
        http_info = self._create_workload_access_token_http_info(request)
        return self._call_api(**http_info)

    def create_workload_access_token_async_invoker(self, request):
        http_info = self._create_workload_access_token_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_workload_access_token_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/workload-access-token",
            "request_type": request.__class__.__name__,
            "response_type": "CreateWorkloadAccessTokenResponse"
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

        auth_settings = ['AccessKeyAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_workload_access_token_for_jwt_async(self, request):
        r"""Create workload access token using JWT (acting on behalf of a user)

        Retrieves a workload access token for agentic workloads acting on behalf of a user, using a JWT token
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateWorkloadAccessTokenForJwt
        :type request: :class:`huaweicloudsdkagentidentity.v1.CreateWorkloadAccessTokenForJwtRequest`
        :rtype: :class:`huaweicloudsdkagentidentity.v1.CreateWorkloadAccessTokenForJwtResponse`
        """
        http_info = self._create_workload_access_token_for_jwt_http_info(request)
        return self._call_api(**http_info)

    def create_workload_access_token_for_jwt_async_invoker(self, request):
        http_info = self._create_workload_access_token_for_jwt_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_workload_access_token_for_jwt_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/workload-access-token-for-jwt",
            "request_type": request.__class__.__name__,
            "response_type": "CreateWorkloadAccessTokenForJwtResponse"
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

        auth_settings = ['AccessKeyAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_workload_access_token_for_user_id_async(self, request):
        r"""Create workload access token using user ID (acting on behalf of a user)

        Retrieves a workload access token for agentic workloads acting on behalf of a user, using the user&#39;s ID
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateWorkloadAccessTokenForUserId
        :type request: :class:`huaweicloudsdkagentidentity.v1.CreateWorkloadAccessTokenForUserIdRequest`
        :rtype: :class:`huaweicloudsdkagentidentity.v1.CreateWorkloadAccessTokenForUserIdResponse`
        """
        http_info = self._create_workload_access_token_for_user_id_http_info(request)
        return self._call_api(**http_info)

    def create_workload_access_token_for_user_id_async_invoker(self, request):
        http_info = self._create_workload_access_token_for_user_id_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_workload_access_token_for_user_id_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/workload-access-token-for-user-id",
            "request_type": request.__class__.__name__,
            "response_type": "CreateWorkloadAccessTokenForUserIdResponse"
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

        auth_settings = ['AccessKeyAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_workload_identity_async(self, request):
        r"""创建工作负载身份

        Creates a new workload identity.
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateWorkloadIdentity
        :type request: :class:`huaweicloudsdkagentidentity.v1.CreateWorkloadIdentityRequest`
        :rtype: :class:`huaweicloudsdkagentidentity.v1.CreateWorkloadIdentityResponse`
        """
        http_info = self._create_workload_identity_http_info(request)
        return self._call_api(**http_info)

    def create_workload_identity_async_invoker(self, request):
        http_info = self._create_workload_identity_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_workload_identity_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/workload-identities",
            "request_type": request.__class__.__name__,
            "response_type": "CreateWorkloadIdentityResponse"
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

        auth_settings = ['AccessKeyAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_workload_identity_async(self, request):
        r"""删除工作负载身份

        Deletes a workload identity.
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteWorkloadIdentity
        :type request: :class:`huaweicloudsdkagentidentity.v1.DeleteWorkloadIdentityRequest`
        :rtype: :class:`huaweicloudsdkagentidentity.v1.DeleteWorkloadIdentityResponse`
        """
        http_info = self._delete_workload_identity_http_info(request)
        return self._call_api(**http_info)

    def delete_workload_identity_async_invoker(self, request):
        http_info = self._delete_workload_identity_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_workload_identity_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/workload-identities/{workload_identity_name}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteWorkloadIdentityResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workload_identity_name' in local_var_params:
            path_params['workload_identity_name'] = local_var_params['workload_identity_name']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['AccessKeyAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def get_workload_identity_async(self, request):
        r"""查询工作负载身份详情

        Gets details of a workload identity.
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for GetWorkloadIdentity
        :type request: :class:`huaweicloudsdkagentidentity.v1.GetWorkloadIdentityRequest`
        :rtype: :class:`huaweicloudsdkagentidentity.v1.GetWorkloadIdentityResponse`
        """
        http_info = self._get_workload_identity_http_info(request)
        return self._call_api(**http_info)

    def get_workload_identity_async_invoker(self, request):
        http_info = self._get_workload_identity_http_info(request)
        return AsyncInvoker(self, http_info)

    def _get_workload_identity_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/workload-identities/{workload_identity_name}",
            "request_type": request.__class__.__name__,
            "response_type": "GetWorkloadIdentityResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workload_identity_name' in local_var_params:
            path_params['workload_identity_name'] = local_var_params['workload_identity_name']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['AccessKeyAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def get_workload_identity_authorizer_configuration_async(self, request):
        r"""查询工作负载身份的授权配置

        Gets the authorizer configuration of a workload identity.
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for GetWorkloadIdentityAuthorizerConfiguration
        :type request: :class:`huaweicloudsdkagentidentity.v1.GetWorkloadIdentityAuthorizerConfigurationRequest`
        :rtype: :class:`huaweicloudsdkagentidentity.v1.GetWorkloadIdentityAuthorizerConfigurationResponse`
        """
        http_info = self._get_workload_identity_authorizer_configuration_http_info(request)
        return self._call_api(**http_info)

    def get_workload_identity_authorizer_configuration_async_invoker(self, request):
        http_info = self._get_workload_identity_authorizer_configuration_http_info(request)
        return AsyncInvoker(self, http_info)

    def _get_workload_identity_authorizer_configuration_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/workload-identities/{workload_identity_name}/authorizer-configuration",
            "request_type": request.__class__.__name__,
            "response_type": "GetWorkloadIdentityAuthorizerConfigurationResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workload_identity_name' in local_var_params:
            path_params['workload_identity_name'] = local_var_params['workload_identity_name']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['AccessKeyAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_workload_identities_async(self, request):
        r"""查询工作负载身份列表

        Lists workload identities.
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListWorkloadIdentities
        :type request: :class:`huaweicloudsdkagentidentity.v1.ListWorkloadIdentitiesRequest`
        :rtype: :class:`huaweicloudsdkagentidentity.v1.ListWorkloadIdentitiesResponse`
        """
        http_info = self._list_workload_identities_http_info(request)
        return self._call_api(**http_info)

    def list_workload_identities_async_invoker(self, request):
        http_info = self._list_workload_identities_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_workload_identities_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/workload-identities",
            "request_type": request.__class__.__name__,
            "response_type": "ListWorkloadIdentitiesResponse"
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

        auth_settings = ['AccessKeyAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_workload_identity_async(self, request):
        r"""更新工作负载身份

        Updates an existing workload identity.
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateWorkloadIdentity
        :type request: :class:`huaweicloudsdkagentidentity.v1.UpdateWorkloadIdentityRequest`
        :rtype: :class:`huaweicloudsdkagentidentity.v1.UpdateWorkloadIdentityResponse`
        """
        http_info = self._update_workload_identity_http_info(request)
        return self._call_api(**http_info)

    def update_workload_identity_async_invoker(self, request):
        http_info = self._update_workload_identity_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_workload_identity_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/workload-identities/{workload_identity_name}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateWorkloadIdentityResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workload_identity_name' in local_var_params:
            path_params['workload_identity_name'] = local_var_params['workload_identity_name']

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

        auth_settings = ['AccessKeyAuth']

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

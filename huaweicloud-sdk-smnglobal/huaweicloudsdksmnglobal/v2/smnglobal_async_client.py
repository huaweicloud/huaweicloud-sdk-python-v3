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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdksmnglobal'")


class SmnglobalAsyncClient(Client):
    def __init__(self):
        super(SmnglobalAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdksmnglobal.v2.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls, "GlobalCredentials")
        else:
            if clazz.__name__ != "SmnglobalAsyncClient":
                raise TypeError("client type error, support client type is SmnglobalAsyncClient")
            client_builder = ClientBuilder(clazz, "GlobalCredentials")

        

        return client_builder

    def create_subscription_user_async(self, request):
        r"""添加订阅用户

        添加订阅用户。如果订阅用户的状态为未确认，则会向订阅用户发送一条确认订阅消息。订阅用户点击订阅链接确认订阅后，则订阅用户的状态变更为已确认，同时会向订阅用户发送一条取消订阅消息，便于订阅用户随时可以取消订阅。订阅用户点击取消订阅链接后，则订阅用户的状态变更为已取消，同时会向订阅用户发送一条重新订阅消息，便于订阅用户可以重新订阅。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateSubscriptionUser
        :type request: :class:`huaweicloudsdksmnglobal.v2.CreateSubscriptionUserRequest`
        :rtype: :class:`huaweicloudsdksmnglobal.v2.CreateSubscriptionUserResponse`
        """
        http_info = self._create_subscription_user_http_info(request)
        return self._call_api(**http_info)

    def create_subscription_user_async_invoker(self, request):
        http_info = self._create_subscription_user_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_subscription_user_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{domain_id}/subscription-users",
            "request_type": request.__class__.__name__,
            "response_type": "CreateSubscriptionUserResponse"
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
            ['application/json;charset=UTF-8'])

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

    def delete_subscription_user_async(self, request):
        r"""删除订阅用户

        删除订阅用户。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteSubscriptionUser
        :type request: :class:`huaweicloudsdksmnglobal.v2.DeleteSubscriptionUserRequest`
        :rtype: :class:`huaweicloudsdksmnglobal.v2.DeleteSubscriptionUserResponse`
        """
        http_info = self._delete_subscription_user_http_info(request)
        return self._call_api(**http_info)

    def delete_subscription_user_async_invoker(self, request):
        http_info = self._delete_subscription_user_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_subscription_user_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{domain_id}/subscription-users/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteSubscriptionUserResponse"
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

    def list_subscription_user_async(self, request):
        r"""查询订阅用户列表

        查询订阅用户列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListSubscriptionUser
        :type request: :class:`huaweicloudsdksmnglobal.v2.ListSubscriptionUserRequest`
        :rtype: :class:`huaweicloudsdksmnglobal.v2.ListSubscriptionUserResponse`
        """
        http_info = self._list_subscription_user_http_info(request)
        return self._call_api(**http_info)

    def list_subscription_user_async_invoker(self, request):
        http_info = self._list_subscription_user_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_subscription_user_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{domain_id}/subscription-users",
            "request_type": request.__class__.__name__,
            "response_type": "ListSubscriptionUserResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'protocol' in local_var_params:
            query_params.append(('protocol', local_var_params['protocol']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'group' in local_var_params:
            query_params.append(('group', local_var_params['group']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

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

    def update_subscription_user_async(self, request):
        r"""更新订阅用户

        更新订阅用户。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateSubscriptionUser
        :type request: :class:`huaweicloudsdksmnglobal.v2.UpdateSubscriptionUserRequest`
        :rtype: :class:`huaweicloudsdksmnglobal.v2.UpdateSubscriptionUserResponse`
        """
        http_info = self._update_subscription_user_http_info(request)
        return self._call_api(**http_info)

    def update_subscription_user_async_invoker(self, request):
        http_info = self._update_subscription_user_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_subscription_user_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{domain_id}/subscription-users/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateSubscriptionUserResponse"
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
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

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

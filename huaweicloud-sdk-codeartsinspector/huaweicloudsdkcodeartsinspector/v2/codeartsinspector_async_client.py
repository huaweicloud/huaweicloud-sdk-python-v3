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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkcodeartsinspector'")


class CodeArtsInspectorAsyncClient(Client):
    def __init__(self):
        super(CodeArtsInspectorAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkcodeartsinspector.v2.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "CodeArtsInspectorAsyncClient":
                raise TypeError("client type error, support client type is CodeArtsInspectorAsyncClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def create_purchase_order_async(self, request):
        """订购下单接口

        订购下单接口
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreatePurchaseOrder
        :type request: :class:`huaweicloudsdkcodeartsinspector.v2.CreatePurchaseOrderRequest`
        :rtype: :class:`huaweicloudsdkcodeartsinspector.v2.CreatePurchaseOrderResponse`
        """
        http_info = self._create_purchase_order_http_info(request)
        return self._call_api(**http_info)

    def create_purchase_order_async_invoker(self, request):
        http_info = self._create_purchase_order_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_purchase_order_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/{service}/subscription/purchase",
            "request_type": request.__class__.__name__,
            "response_type": "CreatePurchaseOrderResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'service' in local_var_params:
            path_params['service'] = local_var_params['service']

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
            ['application/json;charset=utf8'])

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

    def update_purchase_order_async(self, request):
        """变更下单接口

        变更下单接口
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdatePurchaseOrder
        :type request: :class:`huaweicloudsdkcodeartsinspector.v2.UpdatePurchaseOrderRequest`
        :rtype: :class:`huaweicloudsdkcodeartsinspector.v2.UpdatePurchaseOrderResponse`
        """
        http_info = self._update_purchase_order_http_info(request)
        return self._call_api(**http_info)

    def update_purchase_order_async_invoker(self, request):
        http_info = self._update_purchase_order_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_purchase_order_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/{service}/subscription/alter",
            "request_type": request.__class__.__name__,
            "response_type": "UpdatePurchaseOrderResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'service' in local_var_params:
            path_params['service'] = local_var_params['service']

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
            ['application/json;charset=utf8'])

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

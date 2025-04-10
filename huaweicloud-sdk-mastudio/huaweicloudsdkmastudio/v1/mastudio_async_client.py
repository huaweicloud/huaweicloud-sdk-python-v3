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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkmastudio'")


class MaStudioAsyncClient(Client):
    def __init__(self):
        super(MaStudioAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkmastudio.v1.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "MaStudioAsyncClient":
                raise TypeError("client type error, support client type is MaStudioAsyncClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def execute_chat_completion_async(self, request):
        r"""对话问答

        基于对话问答功能，用户可以与模型进行自然而流畅的对话和交流。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ExecuteChatCompletion
        :type request: :class:`huaweicloudsdkmastudio.v1.ExecuteChatCompletionRequest`
        :rtype: :class:`huaweicloudsdkmastudio.v1.ExecuteChatCompletionResponse`
        """
        http_info = self._execute_chat_completion_http_info(request)
        return self._call_api(**http_info)

    def execute_chat_completion_async_invoker(self, request):
        http_info = self._execute_chat_completion_http_info(request)
        return AsyncInvoker(self, http_info)

    def _execute_chat_completion_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/deployments/{deployment_id}/chat/completions",
            "request_type": request.__class__.__name__,
            "response_type": "ExecuteChatCompletionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'deployment_id' in local_var_params:
            path_params['deployment_id'] = local_var_params['deployment_id']

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

    def execute_text_completion_async(self, request):
        r"""通用文本

        给定一个提示和一些参数，模型会根据这些信息生成一个或多个预测的补全，还可以返回每个位置上不同词语的概率。它可以用来做文本生成、自动写作、代码补全等任务。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ExecuteTextCompletion
        :type request: :class:`huaweicloudsdkmastudio.v1.ExecuteTextCompletionRequest`
        :rtype: :class:`huaweicloudsdkmastudio.v1.ExecuteTextCompletionResponse`
        """
        http_info = self._execute_text_completion_http_info(request)
        return self._call_api(**http_info)

    def execute_text_completion_async_invoker(self, request):
        http_info = self._execute_text_completion_http_info(request)
        return AsyncInvoker(self, http_info)

    def _execute_text_completion_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/deployments/{deployment_id}/text/completions",
            "request_type": request.__class__.__name__,
            "response_type": "ExecuteTextCompletionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'deployment_id' in local_var_params:
            path_params['deployment_id'] = local_var_params['deployment_id']

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

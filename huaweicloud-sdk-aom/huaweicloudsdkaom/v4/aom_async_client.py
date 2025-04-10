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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkaom'")


class AomAsyncClient(Client):
    def __init__(self):
        super(AomAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkaom.v4.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "AomAsyncClient":
                raise TypeError("client type error, support client type is AomAsyncClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def batch_import_agent_async(self, request):
        r"""下发批量安装UniAgent任务

        该接口用于下发批量安装UniAgent任务。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchImportAgent
        :type request: :class:`huaweicloudsdkaom.v4.BatchImportAgentRequest`
        :rtype: :class:`huaweicloudsdkaom.v4.BatchImportAgentResponse`
        """
        http_info = self._batch_import_agent_http_info(request)
        return self._call_api(**http_info)

    def batch_import_agent_async_invoker(self, request):
        http_info = self._batch_import_agent_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_import_agent_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/uniagent-console/mainview/batch-import",
            "request_type": request.__class__.__name__,
            "response_type": "BatchImportAgentResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'region' in local_var_params:
            header_params['region'] = local_var_params['region']

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

    def batch_update_agent_async(self, request):
        r"""下发批量升级UniAgent任务

        该接口用于下发批量升级UniAgent任务。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchUpdateAgent
        :type request: :class:`huaweicloudsdkaom.v4.BatchUpdateAgentRequest`
        :rtype: :class:`huaweicloudsdkaom.v4.BatchUpdateAgentResponse`
        """
        http_info = self._batch_update_agent_http_info(request)
        return self._call_api(**http_info)

    def batch_update_agent_async_invoker(self, request):
        http_info = self._batch_update_agent_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_update_agent_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/uniagent-console/upgrade/batch-upgrade",
            "request_type": request.__class__.__name__,
            "response_type": "BatchUpdateAgentResponse"
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

    def show_agent_infos_async(self, request):
        r"""查询UniAgent主机列表信息

        该接口用于查询执行过安装UniAgent任务的主机列表信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowAgentInfos
        :type request: :class:`huaweicloudsdkaom.v4.ShowAgentInfosRequest`
        :rtype: :class:`huaweicloudsdkaom.v4.ShowAgentInfosResponse`
        """
        http_info = self._show_agent_infos_http_info(request)
        return self._call_api(**http_info)

    def show_agent_infos_async_invoker(self, request):
        http_info = self._show_agent_infos_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_agent_infos_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/uniagent-console/agent-list/all",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAgentInfosResponse"
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

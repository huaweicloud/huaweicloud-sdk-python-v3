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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkces'")


class CesClient(Client):
    def __init__(self):
        super(CesClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkces.v3.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "CesClient":
                raise TypeError("client type error, support client type is CesClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def list_agent_status(self, request):
        """插件状态查询

        插件状态查询，包括uniagent状态以及插件状态
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAgentStatus
        :type request: :class:`huaweicloudsdkces.v3.ListAgentStatusRequest`
        :rtype: :class:`huaweicloudsdkces.v3.ListAgentStatusResponse`
        """
        http_info = self._list_agent_status_http_info(request)
        return self._call_api(**http_info)

    def list_agent_status_invoker(self, request):
        http_info = self._list_agent_status_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_agent_status_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/agent-status/batch-query",
            "request_type": request.__class__.__name__,
            "response_type": "ListAgentStatusResponse"
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

    def batch_create_agent_invocations(self, request):
        """批量创建Agent任务

        批量创建Agent任务
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchCreateAgentInvocations
        :type request: :class:`huaweicloudsdkces.v3.BatchCreateAgentInvocationsRequest`
        :rtype: :class:`huaweicloudsdkces.v3.BatchCreateAgentInvocationsResponse`
        """
        http_info = self._batch_create_agent_invocations_http_info(request)
        return self._call_api(**http_info)

    def batch_create_agent_invocations_invoker(self, request):
        http_info = self._batch_create_agent_invocations_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_create_agent_invocations_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/agent-invocations/batch-create",
            "request_type": request.__class__.__name__,
            "response_type": "BatchCreateAgentInvocationsResponse"
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

    def list_agent_invocations(self, request):
        """查询Agent任务列表

        查询Agent任务列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAgentInvocations
        :type request: :class:`huaweicloudsdkces.v3.ListAgentInvocationsRequest`
        :rtype: :class:`huaweicloudsdkces.v3.ListAgentInvocationsResponse`
        """
        http_info = self._list_agent_invocations_http_info(request)
        return self._call_api(**http_info)

    def list_agent_invocations_invoker(self, request):
        http_info = self._list_agent_invocations_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_agent_invocations_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/agent-invocations",
            "request_type": request.__class__.__name__,
            "response_type": "ListAgentInvocationsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'instance_id' in local_var_params:
            query_params.append(('instance_id', local_var_params['instance_id']))
        if 'instance_type' in local_var_params:
            query_params.append(('instance_type', local_var_params['instance_type']))
        if 'invocation_id' in local_var_params:
            query_params.append(('invocation_id', local_var_params['invocation_id']))
        if 'invocation_type' in local_var_params:
            query_params.append(('invocation_type', local_var_params['invocation_type']))
        if 'invocation_target' in local_var_params:
            query_params.append(('invocation_target', local_var_params['invocation_target']))
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

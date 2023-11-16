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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkhss'")


class HssAsyncClient(Client):
    def __init__(self):
        super(HssAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkhss.v1.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "HssAsyncClient":
                raise TypeError("client type error, support client type is HssAsyncClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def list_events_async(self, request):
        """查入侵事件列表

        查入侵事件列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListEvents
        :type request: :class:`huaweicloudsdkhss.v1.ListEventsRequest`
        :rtype: :class:`huaweicloudsdkhss.v1.ListEventsResponse`
        """
        http_info = self._list_events_http_info(request)
        return self._call_api(**http_info)

    def list_events_async_invoker(self, request):
        http_info = self._list_events_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_events_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/api/event-management/events",
            "request_type": request.__class__.__name__,
            "response_type": "ListEventsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'begin_time' in local_var_params:
            query_params.append(('begin_time', local_var_params['begin_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'host_name' in local_var_params:
            query_params.append(('host_name', local_var_params['host_name']))
        if 'event_types' in local_var_params:
            query_params.append(('event_types', local_var_params['event_types']))
            collection_formats['event_types'] = 'csv'
        if 'handle_status' in local_var_params:
            query_params.append(('handle_status', local_var_params['handle_status']))
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

    def list_hosts_async(self, request):
        """查询弹性云服务器状态列表

        查询弹性云服务器状态列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListHosts
        :type request: :class:`huaweicloudsdkhss.v1.ListHostsRequest`
        :rtype: :class:`huaweicloudsdkhss.v1.ListHostsResponse`
        """
        http_info = self._list_hosts_http_info(request)
        return self._call_api(**http_info)

    def list_hosts_async_invoker(self, request):
        http_info = self._list_hosts_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_hosts_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/api/host-management/hosts",
            "request_type": request.__class__.__name__,
            "response_type": "ListHostsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'version' in local_var_params:
            query_params.append(('version', local_var_params['version']))
        if 'agent_status' in local_var_params:
            query_params.append(('agent_status', local_var_params['agent_status']))
        if 'host_status' in local_var_params:
            query_params.append(('host_status', local_var_params['host_status']))
        if 'protect_status' in local_var_params:
            query_params.append(('protect_status', local_var_params['protect_status']))
        if 'detect_result' in local_var_params:
            query_params.append(('detect_result', local_var_params['detect_result']))
        if 'host_name' in local_var_params:
            query_params.append(('host_name', local_var_params['host_name']))
        if 'host_ip' in local_var_params:
            query_params.append(('host_ip', local_var_params['host_ip']))
        if 'public_ip' in local_var_params:
            query_params.append(('public_ip', local_var_params['public_ip']))
        if 'os_type' in local_var_params:
            query_params.append(('os_type', local_var_params['os_type']))
        if 'charging_mode' in local_var_params:
            query_params.append(('charging_mode', local_var_params['charging_mode']))
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

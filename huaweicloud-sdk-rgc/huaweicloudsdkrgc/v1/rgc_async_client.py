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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkrgc'")


class RgcAsyncClient(Client):
    def __init__(self):
        super(RgcAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkrgc.v1.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "RgcAsyncClient":
                raise TypeError("client type error, support client type is RgcAsyncClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def disable_control_async(self, request):
        """关闭控制策略

        关闭组织下的某个单元的某个控制策略。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DisableControl
        :type request: :class:`huaweicloudsdkrgc.v1.DisableControlRequest`
        :rtype: :class:`huaweicloudsdkrgc.v1.DisableControlResponse`
        """
        http_info = self._disable_control_http_info(request)
        return self._call_api(**http_info)

    def disable_control_async_invoker(self, request):
        http_info = self._disable_control_http_info(request)
        return AsyncInvoker(self, http_info)

    def _disable_control_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/governance/controls/disable",
            "request_type": request.__class__.__name__,
            "response_type": "DisableControlResponse"
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

    def enable_control_async(self, request):
        """开启控制策略

        给组织下的某个单元开启某个控制策略。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for EnableControl
        :type request: :class:`huaweicloudsdkrgc.v1.EnableControlRequest`
        :rtype: :class:`huaweicloudsdkrgc.v1.EnableControlResponse`
        """
        http_info = self._enable_control_http_info(request)
        return self._call_api(**http_info)

    def enable_control_async_invoker(self, request):
        http_info = self._enable_control_http_info(request)
        return AsyncInvoker(self, http_info)

    def _enable_control_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/governance/controls/enable",
            "request_type": request.__class__.__name__,
            "response_type": "EnableControlResponse"
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

    def list_controls_for_organizational_unit_async(self, request):
        """列出注册OU下开启的控制策略

        列出组织里某个注册OU开启的所有控制策略信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListControlsForOrganizationalUnit
        :type request: :class:`huaweicloudsdkrgc.v1.ListControlsForOrganizationalUnitRequest`
        :rtype: :class:`huaweicloudsdkrgc.v1.ListControlsForOrganizationalUnitResponse`
        """
        http_info = self._list_controls_for_organizational_unit_http_info(request)
        return self._call_api(**http_info)

    def list_controls_for_organizational_unit_async_invoker(self, request):
        http_info = self._list_controls_for_organizational_unit_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_controls_for_organizational_unit_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/governance/managed-organizational-units/{managed_organizational_unit_id}/controls",
            "request_type": request.__class__.__name__,
            "response_type": "ListControlsForOrganizationalUnitResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'managed_organizational_unit_id' in local_var_params:
            path_params['managed_organizational_unit_id'] = local_var_params['managed_organizational_unit_id']

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

    def show_control_operate_async(self, request):
        """查询控制策略操作状态

        根据操作ID查询返回指定ID的操作状态。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowControlOperate
        :type request: :class:`huaweicloudsdkrgc.v1.ShowControlOperateRequest`
        :rtype: :class:`huaweicloudsdkrgc.v1.ShowControlOperateResponse`
        """
        http_info = self._show_control_operate_http_info(request)
        return self._call_api(**http_info)

    def show_control_operate_async_invoker(self, request):
        http_info = self._show_control_operate_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_control_operate_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/governance/operation-control-status/{operation_control_status_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowControlOperateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'operation_control_status_id' in local_var_params:
            path_params['operation_control_status_id'] = local_var_params['operation_control_status_id']

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

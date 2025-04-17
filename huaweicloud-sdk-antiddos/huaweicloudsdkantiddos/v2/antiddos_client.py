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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkantiddos'")


class AntiDDoSClient(Client):
    def __init__(self):
        super(AntiDDoSClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkantiddos.v2.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "AntiDDoSClient":
                raise TypeError("client type error, support client type is AntiDDoSClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def show_alert_config(self, request):
        r"""查询告警配置信息

        查询用户配置信息，用户可以通过此接口查询是否接收某类告警，同时可以配置是手机短信还是电子邮件接收告警信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAlertConfig
        :type request: :class:`huaweicloudsdkantiddos.v2.ShowAlertConfigRequest`
        :rtype: :class:`huaweicloudsdkantiddos.v2.ShowAlertConfigResponse`
        """
        http_info = self._show_alert_config_http_info(request)
        return self._call_api(**http_info)

    def show_alert_config_invoker(self, request):
        http_info = self._show_alert_config_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_alert_config_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/warnalert/alertconfig/query",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAlertConfigResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

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

    def update_alert_config(self, request):
        r"""更新告警配置信息

        更新用户配置信息，用户可以通过此接口更新是否接收某类告警，同时可以配置是手机短信还是电子邮件接收告警信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateAlertConfig
        :type request: :class:`huaweicloudsdkantiddos.v2.UpdateAlertConfigRequest`
        :rtype: :class:`huaweicloudsdkantiddos.v2.UpdateAlertConfigResponse`
        """
        http_info = self._update_alert_config_http_info(request)
        return self._call_api(**http_info)

    def update_alert_config_invoker(self, request):
        http_info = self._update_alert_config_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_alert_config_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/warnalert/alertconfig/update",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateAlertConfigResponse"
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

    def list_d_dos_status(self, request):
        r"""查询EIP防护状态列表

        查询用户所有EIP的Anti-DDoS防护状态信息，用户的EIP无论是否绑定到云服务器，都可以进行查询。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListDDosStatus
        :type request: :class:`huaweicloudsdkantiddos.v2.ListDDosStatusRequest`
        :rtype: :class:`huaweicloudsdkantiddos.v2.ListDDosStatusResponse`
        """
        http_info = self._list_d_dos_status_http_info(request)
        return self._call_api(**http_info)

    def list_d_dos_status_invoker(self, request):
        http_info = self._list_d_dos_status_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_d_dos_status_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/antiddos",
            "request_type": request.__class__.__name__,
            "response_type": "ListDDosStatusResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'ips' in local_var_params:
            query_params.append(('ips', local_var_params['ips']))

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

    def list_new_configs(self, request):
        r"""查询Anti-DDoS配置可选范围

        查询系统支持的Anti-DDoS防护策略配置的可选范围，用户根据范围列表选择适合自已业务的防护策略进行Anti-DDoS流量清洗。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListNewConfigs
        :type request: :class:`huaweicloudsdkantiddos.v2.ListNewConfigsRequest`
        :rtype: :class:`huaweicloudsdkantiddos.v2.ListNewConfigsResponse`
        """
        http_info = self._list_new_configs_http_info(request)
        return self._call_api(**http_info)

    def list_new_configs_invoker(self, request):
        http_info = self._list_new_configs_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_new_configs_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/antiddos/query-config-list",
            "request_type": request.__class__.__name__,
            "response_type": "ListNewConfigsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

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

    def show_new_task_status(self, request):
        r"""查询Anti-DDoS任务

        用户查询指定的Anti-DDoS防护配置任务，得到任务当前执行的状态。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowNewTaskStatus
        :type request: :class:`huaweicloudsdkantiddos.v2.ShowNewTaskStatusRequest`
        :rtype: :class:`huaweicloudsdkantiddos.v2.ShowNewTaskStatusResponse`
        """
        http_info = self._show_new_task_status_http_info(request)
        return self._call_api(**http_info)

    def show_new_task_status_invoker(self, request):
        http_info = self._show_new_task_status_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_new_task_status_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/query-task-status",
            "request_type": request.__class__.__name__,
            "response_type": "ShowNewTaskStatusResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'task_id' in local_var_params:
            query_params.append(('task_id', local_var_params['task_id']))

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

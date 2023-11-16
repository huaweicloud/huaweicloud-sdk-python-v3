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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkantiddos'")


class AntiDDoSAsyncClient(Client):
    def __init__(self):
        super(AntiDDoSAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkantiddos.v1.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "AntiDDoSAsyncClient":
                raise TypeError("client type error, support client type is AntiDDoSAsyncClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def create_default_config_async(self, request):
        """配置Anti-DDoS默认防护策略

        配置用户的默认防护策略。配置防护策略后，新购买的资源在自动开启防护时，会按照该默认防护策略进行配置。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateDefaultConfig
        :type request: :class:`huaweicloudsdkantiddos.v1.CreateDefaultConfigRequest`
        :rtype: :class:`huaweicloudsdkantiddos.v1.CreateDefaultConfigResponse`
        """
        http_info = self._create_default_config_http_info(request)
        return self._call_api(**http_info)

    def create_default_config_async_invoker(self, request):
        http_info = self._create_default_config_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_default_config_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/antiddos/default-config",
            "request_type": request.__class__.__name__,
            "response_type": "CreateDefaultConfigResponse"
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

    def delete_default_config_async(self, request):
        """删除Ani-DDoS默认防护策略

        删除用户配置的默认防护策略。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteDefaultConfig
        :type request: :class:`huaweicloudsdkantiddos.v1.DeleteDefaultConfigRequest`
        :rtype: :class:`huaweicloudsdkantiddos.v1.DeleteDefaultConfigResponse`
        """
        http_info = self._delete_default_config_http_info(request)
        return self._call_api(**http_info)

    def delete_default_config_async_invoker(self, request):
        http_info = self._delete_default_config_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_default_config_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/antiddos/default-config",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteDefaultConfigResponse"
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

    def show_alert_config_async(self, request):
        """查询告警配置信息

        查询用户配置信息，用户可以通过此接口查询是否接收某类告警，同时可以配置是手机短信还是电子邮件接收告警信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowAlertConfig
        :type request: :class:`huaweicloudsdkantiddos.v1.ShowAlertConfigRequest`
        :rtype: :class:`huaweicloudsdkantiddos.v1.ShowAlertConfigResponse`
        """
        http_info = self._show_alert_config_http_info(request)
        return self._call_api(**http_info)

    def show_alert_config_async_invoker(self, request):
        http_info = self._show_alert_config_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_alert_config_http_info(self, request):
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

    def show_default_config_async(self, request):
        """查询Ani-DDoS默认防护策略

        查询用户配置的默认防护策略。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowDefaultConfig
        :type request: :class:`huaweicloudsdkantiddos.v1.ShowDefaultConfigRequest`
        :rtype: :class:`huaweicloudsdkantiddos.v1.ShowDefaultConfigResponse`
        """
        http_info = self._show_default_config_http_info(request)
        return self._call_api(**http_info)

    def show_default_config_async_invoker(self, request):
        http_info = self._show_default_config_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_default_config_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/antiddos/default-config",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDefaultConfigResponse"
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

    def update_alert_config_async(self, request):
        """更新告警配置信息

        更新用户配置信息，用户可以通过此接口更新是否接收某类告警，同时可以配置是手机短信还是电子邮件接收告警信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateAlertConfig
        :type request: :class:`huaweicloudsdkantiddos.v1.UpdateAlertConfigRequest`
        :rtype: :class:`huaweicloudsdkantiddos.v1.UpdateAlertConfigResponse`
        """
        http_info = self._update_alert_config_http_info(request)
        return self._call_api(**http_info)

    def update_alert_config_async_invoker(self, request):
        http_info = self._update_alert_config_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_alert_config_http_info(self, request):
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

    def list_d_dos_status_async(self, request):
        """查询EIP防护状态列表

        查询用户所有EIP的Anti-DDoS防护状态信息，用户的EIP无论是否绑定到云服务器，都可以进行查询。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListDDosStatus
        :type request: :class:`huaweicloudsdkantiddos.v1.ListDDosStatusRequest`
        :rtype: :class:`huaweicloudsdkantiddos.v1.ListDDosStatusResponse`
        """
        http_info = self._list_d_dos_status_http_info(request)
        return self._call_api(**http_info)

    def list_d_dos_status_async_invoker(self, request):
        http_info = self._list_d_dos_status_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_d_dos_status_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/antiddos",
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
        if 'ip' in local_var_params:
            query_params.append(('ip', local_var_params['ip']))

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

    def list_daily_log_async(self, request):
        """查询指定EIP异常事件

        查询指定EIP在过去24小时之内的异常事件信息，异常事件包括清洗事件和黑洞事件，查询延迟在5分钟之内。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListDailyLog
        :type request: :class:`huaweicloudsdkantiddos.v1.ListDailyLogRequest`
        :rtype: :class:`huaweicloudsdkantiddos.v1.ListDailyLogResponse`
        """
        http_info = self._list_daily_log_http_info(request)
        return self._call_api(**http_info)

    def list_daily_log_async_invoker(self, request):
        http_info = self._list_daily_log_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_daily_log_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/antiddos/{floating_ip_id}/logs",
            "request_type": request.__class__.__name__,
            "response_type": "ListDailyLogResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'floating_ip_id' in local_var_params:
            path_params['floating_ip_id'] = local_var_params['floating_ip_id']

        query_params = []
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'ip' in local_var_params:
            query_params.append(('ip', local_var_params['ip']))

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

    def list_daily_report_async(self, request):
        """查询指定EIP防护流量

        查询指定EIP在过去24小时之内的防护流量信息，流量的间隔时间单位为5分钟。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListDailyReport
        :type request: :class:`huaweicloudsdkantiddos.v1.ListDailyReportRequest`
        :rtype: :class:`huaweicloudsdkantiddos.v1.ListDailyReportResponse`
        """
        http_info = self._list_daily_report_http_info(request)
        return self._call_api(**http_info)

    def list_daily_report_async_invoker(self, request):
        http_info = self._list_daily_report_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_daily_report_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/antiddos/{floating_ip_id}/daily",
            "request_type": request.__class__.__name__,
            "response_type": "ListDailyReportResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'floating_ip_id' in local_var_params:
            path_params['floating_ip_id'] = local_var_params['floating_ip_id']

        query_params = []
        if 'ip' in local_var_params:
            query_params.append(('ip', local_var_params['ip']))

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

    def list_new_configs_async(self, request):
        """查询Anti-DDoS配置可选范围

        查询系统支持的Anti-DDoS防护策略配置的可选范围，用户根据范围列表选择适合自已业务的防护策略进行Anti-DDoS流量清洗。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListNewConfigs
        :type request: :class:`huaweicloudsdkantiddos.v1.ListNewConfigsRequest`
        :rtype: :class:`huaweicloudsdkantiddos.v1.ListNewConfigsResponse`
        """
        http_info = self._list_new_configs_http_info(request)
        return self._call_api(**http_info)

    def list_new_configs_async_invoker(self, request):
        http_info = self._list_new_configs_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_new_configs_http_info(self, request):
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

    def list_weekly_reports_async(self, request):
        """查询周防护统计情况

        查询用户所有Anti-DDoS防护周统计情况，包括一周内DDoS拦截次数和攻击次数、以及按照被攻击次数进行的排名信息等统计数据。系统支持当前时间之前四周的周统计数据查询，超过这个时间的请求是查询不到统计数据的。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListWeeklyReports
        :type request: :class:`huaweicloudsdkantiddos.v1.ListWeeklyReportsRequest`
        :rtype: :class:`huaweicloudsdkantiddos.v1.ListWeeklyReportsResponse`
        """
        http_info = self._list_weekly_reports_http_info(request)
        return self._call_api(**http_info)

    def list_weekly_reports_async_invoker(self, request):
        http_info = self._list_weekly_reports_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_weekly_reports_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/antiddos/weekly",
            "request_type": request.__class__.__name__,
            "response_type": "ListWeeklyReportsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'period_start_date' in local_var_params:
            query_params.append(('period_start_date', local_var_params['period_start_date']))

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

    def show_d_dos_async(self, request):
        """查询Anti-DDoS服务

        查询配置的Anti-DDoS防护策略，用户可以查询指定EIP的Anti-DDoS防护策略。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowDDos
        :type request: :class:`huaweicloudsdkantiddos.v1.ShowDDosRequest`
        :rtype: :class:`huaweicloudsdkantiddos.v1.ShowDDosResponse`
        """
        http_info = self._show_d_dos_http_info(request)
        return self._call_api(**http_info)

    def show_d_dos_async_invoker(self, request):
        http_info = self._show_d_dos_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_d_dos_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/antiddos/{floating_ip_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDDosResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'floating_ip_id' in local_var_params:
            path_params['floating_ip_id'] = local_var_params['floating_ip_id']

        query_params = []
        if 'ip' in local_var_params:
            query_params.append(('ip', local_var_params['ip']))

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

    def show_d_dos_status_async(self, request):
        """查询指定EIP防护状态

        查询指定EIP的Anti-DDoS防护状态。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowDDosStatus
        :type request: :class:`huaweicloudsdkantiddos.v1.ShowDDosStatusRequest`
        :rtype: :class:`huaweicloudsdkantiddos.v1.ShowDDosStatusResponse`
        """
        http_info = self._show_d_dos_status_http_info(request)
        return self._call_api(**http_info)

    def show_d_dos_status_async_invoker(self, request):
        http_info = self._show_d_dos_status_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_d_dos_status_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/antiddos/{floating_ip_id}/status",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDDosStatusResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'floating_ip_id' in local_var_params:
            path_params['floating_ip_id'] = local_var_params['floating_ip_id']

        query_params = []
        if 'ip' in local_var_params:
            query_params.append(('ip', local_var_params['ip']))

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

    def show_new_task_status_async(self, request):
        """查询Anti-DDoS任务

        用户查询指定的Anti-DDoS防护配置任务，得到任务当前执行的状态。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowNewTaskStatus
        :type request: :class:`huaweicloudsdkantiddos.v1.ShowNewTaskStatusRequest`
        :rtype: :class:`huaweicloudsdkantiddos.v1.ShowNewTaskStatusResponse`
        """
        http_info = self._show_new_task_status_http_info(request)
        return self._call_api(**http_info)

    def show_new_task_status_async_invoker(self, request):
        http_info = self._show_new_task_status_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_new_task_status_http_info(self, request):
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

    def update_d_dos_async(self, request):
        """更新Anti-DDoS服务

        更新指定EIP的Anti-DDoS防护策略配置。调用成功，只是说明服务节点收到了关闭更新配置请求，操作是否成功需要通过任务查询接口查询该任务的执行状态，具体请参考查询Anti-DDoS任务。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateDDos
        :type request: :class:`huaweicloudsdkantiddos.v1.UpdateDDosRequest`
        :rtype: :class:`huaweicloudsdkantiddos.v1.UpdateDDosResponse`
        """
        http_info = self._update_d_dos_http_info(request)
        return self._call_api(**http_info)

    def update_d_dos_async_invoker(self, request):
        http_info = self._update_d_dos_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_d_dos_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/antiddos/{floating_ip_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateDDosResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'floating_ip_id' in local_var_params:
            path_params['floating_ip_id'] = local_var_params['floating_ip_id']

        query_params = []
        if 'ip' in local_var_params:
            query_params.append(('ip', local_var_params['ip']))

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

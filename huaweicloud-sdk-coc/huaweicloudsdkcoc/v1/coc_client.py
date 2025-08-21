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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkcoc'")


class CocClient(Client):
    def __init__(self):
        super(CocClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkcoc.v1.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls, "GlobalCredentials,BasicCredentials")
        else:
            if clazz.__name__ != "CocClient":
                raise TypeError("client type error, support client type is CocClient")
            client_builder = ClientBuilder(clazz, "GlobalCredentials,BasicCredentials")

        

        return client_builder

    def create_password_change_plan(self, request):
        r"""创建改密计划

        创建改密计划
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreatePasswordChangePlan
        :type request: :class:`huaweicloudsdkcoc.v1.CreatePasswordChangePlanRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.CreatePasswordChangePlanResponse`
        """
        http_info = self._create_password_change_plan_http_info(request)
        return self._call_api(**http_info)

    def create_password_change_plan_invoker(self, request):
        http_info = self._create_password_change_plan_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_password_change_plan_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/account-mgmt/accounts/password-change-plan",
            "request_type": request.__class__.__name__,
            "response_type": "CreatePasswordChangePlanResponse"
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

    def reset_account_password(self, request):
        r"""主机密码重置

        主机密码重置
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ResetAccountPassword
        :type request: :class:`huaweicloudsdkcoc.v1.ResetAccountPasswordRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.ResetAccountPasswordResponse`
        """
        http_info = self._reset_account_password_http_info(request)
        return self._call_api(**http_info)

    def reset_account_password_invoker(self, request):
        http_info = self._reset_account_password_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _reset_account_password_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/account-mgmt/accounts/password/reset",
            "request_type": request.__class__.__name__,
            "response_type": "ResetAccountPasswordResponse"
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

    def update_account_password(self, request):
        r"""回写改密结果

        回写改密结果
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateAccountPassword
        :type request: :class:`huaweicloudsdkcoc.v1.UpdateAccountPasswordRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.UpdateAccountPasswordResponse`
        """
        http_info = self._update_account_password_http_info(request)
        return self._call_api(**http_info)

    def update_account_password_invoker(self, request):
        http_info = self._update_account_password_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_account_password_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/account-mgmt/accounts/password/update",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateAccountPasswordResponse"
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

    def clear_alarm(self, request):
        r"""批量清除告警

        清除告警
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ClearAlarm
        :type request: :class:`huaweicloudsdkcoc.v1.ClearAlarmRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.ClearAlarmResponse`
        """
        http_info = self._clear_alarm_http_info(request)
        return self._call_api(**http_info)

    def clear_alarm_invoker(self, request):
        http_info = self._clear_alarm_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _clear_alarm_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/alarm-mgmt/alarms/cancel",
            "request_type": request.__class__.__name__,
            "response_type": "ClearAlarmResponse"
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

    def handle_alarm(self, request):
        r"""自动处理告警

        自动处理告警
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for HandleAlarm
        :type request: :class:`huaweicloudsdkcoc.v1.HandleAlarmRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.HandleAlarmResponse`
        """
        http_info = self._handle_alarm_http_info(request)
        return self._call_api(**http_info)

    def handle_alarm_invoker(self, request):
        http_info = self._handle_alarm_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _handle_alarm_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/alarm-mgmt/alarm/{alarm_id}/auto-process",
            "request_type": request.__class__.__name__,
            "response_type": "HandleAlarmResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'alarm_id' in local_var_params:
            path_params['alarm_id'] = local_var_params['alarm_id']

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

    def list_alarm_handle_histories(self, request):
        r"""查询告警工单历史

        查询告警工单历史
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAlarmHandleHistories
        :type request: :class:`huaweicloudsdkcoc.v1.ListAlarmHandleHistoriesRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.ListAlarmHandleHistoriesResponse`
        """
        http_info = self._list_alarm_handle_histories_http_info(request)
        return self._call_api(**http_info)

    def list_alarm_handle_histories_invoker(self, request):
        http_info = self._list_alarm_handle_histories_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_alarm_handle_histories_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/alarm-mgmt/alarm/{alarm_id}/handle-histories",
            "request_type": request.__class__.__name__,
            "response_type": "ListAlarmHandleHistoriesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'alarm_id' in local_var_params:
            path_params['alarm_id'] = local_var_params['alarm_id']

        query_params = []
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

    def show_alarm(self, request):
        r"""查询Alarm

        Get alarm info by id
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAlarm
        :type request: :class:`huaweicloudsdkcoc.v1.ShowAlarmRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.ShowAlarmResponse`
        """
        http_info = self._show_alarm_http_info(request)
        return self._call_api(**http_info)

    def show_alarm_invoker(self, request):
        http_info = self._show_alarm_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_alarm_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/alarm-mgmt/alarm/{alarm_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAlarmResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'alarm_id' in local_var_params:
            path_params['alarm_id'] = local_var_params['alarm_id']

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

    def transfer_alarm_to_incident(self, request):
        r"""批量告警转事件

        批量告警转事件
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for TransferAlarmToIncident
        :type request: :class:`huaweicloudsdkcoc.v1.TransferAlarmToIncidentRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.TransferAlarmToIncidentResponse`
        """
        http_info = self._transfer_alarm_to_incident_http_info(request)
        return self._call_api(**http_info)

    def transfer_alarm_to_incident_invoker(self, request):
        http_info = self._transfer_alarm_to_incident_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _transfer_alarm_to_incident_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/alarm-mgmt/alarms-linked-incident",
            "request_type": request.__class__.__name__,
            "response_type": "TransferAlarmToIncidentResponse"
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

    def create_assess_task(self, request):
        r"""创建应用评估任务

        创建应用评估任务
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateAssessTask
        :type request: :class:`huaweicloudsdkcoc.v1.CreateAssessTaskRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.CreateAssessTaskResponse`
        """
        http_info = self._create_assess_task_http_info(request)
        return self._call_api(**http_info)

    def create_assess_task_invoker(self, request):
        http_info = self._create_assess_task_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_assess_task_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/assess-tasks",
            "request_type": request.__class__.__name__,
            "response_type": "CreateAssessTaskResponse"
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

    def list_assess_task(self, request):
        r"""分页查询评估任务列表

        分页查询评估任务列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAssessTask
        :type request: :class:`huaweicloudsdkcoc.v1.ListAssessTaskRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.ListAssessTaskResponse`
        """
        http_info = self._list_assess_task_http_info(request)
        return self._call_api(**http_info)

    def list_assess_task_invoker(self, request):
        http_info = self._list_assess_task_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_assess_task_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/assess-tasks",
            "request_type": request.__class__.__name__,
            "response_type": "ListAssessTaskResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'application_id' in local_var_params:
            query_params.append(('application_id', local_var_params['application_id']))
        if 'assess_status_list' in local_var_params:
            query_params.append(('assess_status_list', local_var_params['assess_status_list']))
            collection_formats['assess_status_list'] = 'csv'

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

    def update_change(self, request):
        r"""UpdateChange 更新变更单

        UpdateChange 更新变更单
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateChange
        :type request: :class:`huaweicloudsdkcoc.v1.UpdateChangeRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.UpdateChangeResponse`
        """
        http_info = self._update_change_http_info(request)
        return self._call_api(**http_info)

    def update_change_invoker(self, request):
        http_info = self._update_change_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_change_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/changes/{change_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateChangeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'change_id' in local_var_params:
            path_params['change_id'] = local_var_params['change_id']

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

    def handle_incident(self, request):
        r"""HandleIncident 处理事件单

        HandleIncident 处理事件单
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for HandleIncident
        :type request: :class:`huaweicloudsdkcoc.v1.HandleIncidentRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.HandleIncidentResponse`
        """
        http_info = self._handle_incident_http_info(request)
        return self._call_api(**http_info)

    def handle_incident_invoker(self, request):
        http_info = self._handle_incident_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _handle_incident_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/incidents/{incident_id}/actions",
            "request_type": request.__class__.__name__,
            "response_type": "HandleIncidentResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'incident_id' in local_var_params:
            path_params['incident_id'] = local_var_params['incident_id']

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

    def list_incidents(self, request):
        r"""ListIncidents 查询事件单列表

        ListIncidents 查询事件单列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListIncidents
        :type request: :class:`huaweicloudsdkcoc.v1.ListIncidentsRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.ListIncidentsResponse`
        """
        http_info = self._list_incidents_http_info(request)
        return self._call_api(**http_info)

    def list_incidents_invoker(self, request):
        http_info = self._list_incidents_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_incidents_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/incidents/list",
            "request_type": request.__class__.__name__,
            "response_type": "ListIncidentsResponse"
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

    def list_incidents_histories(self, request):
        r"""ListIncidentsHistories 获取事件单历史

        ListIncidentsHistories  获取事件单历史
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListIncidentsHistories
        :type request: :class:`huaweicloudsdkcoc.v1.ListIncidentsHistoriesRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.ListIncidentsHistoriesResponse`
        """
        http_info = self._list_incidents_histories_http_info(request)
        return self._call_api(**http_info)

    def list_incidents_histories_invoker(self, request):
        http_info = self._list_incidents_histories_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_incidents_histories_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/incidents/{incident_id}/histories",
            "request_type": request.__class__.__name__,
            "response_type": "ListIncidentsHistoriesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'incident_id' in local_var_params:
            path_params['incident_id'] = local_var_params['incident_id']

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

    def show_incident_task(self, request):
        r"""ShowIncidentTask 获取事件任务

        ShowIncidentTask 获取事件任务
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowIncidentTask
        :type request: :class:`huaweicloudsdkcoc.v1.ShowIncidentTaskRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.ShowIncidentTaskResponse`
        """
        http_info = self._show_incident_task_http_info(request)
        return self._call_api(**http_info)

    def show_incident_task_invoker(self, request):
        http_info = self._show_incident_task_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_incident_task_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/incidents/{incident_id}/tasks",
            "request_type": request.__class__.__name__,
            "response_type": "ShowIncidentTaskResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'incident_id' in local_var_params:
            path_params['incident_id'] = local_var_params['incident_id']

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

    def create_report_custom_event(self, request):
        r"""支持用户自主接入告警数据

        支持租户将自开发的监控系统按照标准化集成至COC，集成后告警会按照标准格式上报至COC告警中心
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateReportCustomEvent
        :type request: :class:`huaweicloudsdkcoc.v1.CreateReportCustomEventRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.CreateReportCustomEventResponse`
        """
        http_info = self._create_report_custom_event_http_info(request)
        return self._call_api(**http_info)

    def create_report_custom_event_invoker(self, request):
        http_info = self._create_report_custom_event_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_report_custom_event_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/event/huawei/custom/{integration_key}",
            "request_type": request.__class__.__name__,
            "response_type": "CreateReportCustomEventResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'integration_key' in local_var_params:
            path_params['integration_key'] = local_var_params['integration_key']

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
            ['application/json; charset=utf-8'])

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

    def cancel_diagnosis_task(self, request):
        r"""取消诊断任务

        取消诊断任务
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CancelDiagnosisTask
        :type request: :class:`huaweicloudsdkcoc.v1.CancelDiagnosisTaskRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.CancelDiagnosisTaskResponse`
        """
        http_info = self._cancel_diagnosis_task_http_info(request)
        return self._call_api(**http_info)

    def cancel_diagnosis_task_invoker(self, request):
        http_info = self._cancel_diagnosis_task_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _cancel_diagnosis_task_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/diagnosis/tasks/{task_id}/cancel",
            "request_type": request.__class__.__name__,
            "response_type": "CancelDiagnosisTaskResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

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

    def create_diagnosis_task(self, request):
        r"""提交诊断任务

        提交诊断任务
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateDiagnosisTask
        :type request: :class:`huaweicloudsdkcoc.v1.CreateDiagnosisTaskRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.CreateDiagnosisTaskResponse`
        """
        http_info = self._create_diagnosis_task_http_info(request)
        return self._call_api(**http_info)

    def create_diagnosis_task_invoker(self, request):
        http_info = self._create_diagnosis_task_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_diagnosis_task_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/diagnosis/tasks",
            "request_type": request.__class__.__name__,
            "response_type": "CreateDiagnosisTaskResponse"
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

    def list_diagnosis_tasks(self, request):
        r"""查询诊断记录

        查询诊断记录
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListDiagnosisTasks
        :type request: :class:`huaweicloudsdkcoc.v1.ListDiagnosisTasksRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.ListDiagnosisTasksResponse`
        """
        http_info = self._list_diagnosis_tasks_http_info(request)
        return self._call_api(**http_info)

    def list_diagnosis_tasks_invoker(self, request):
        http_info = self._list_diagnosis_tasks_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_diagnosis_tasks_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/diagnosis/tasks",
            "request_type": request.__class__.__name__,
            "response_type": "ListDiagnosisTasksResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'task_id' in local_var_params:
            query_params.append(('task_id', local_var_params['task_id']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'region' in local_var_params:
            query_params.append(('region', local_var_params['region']))
        if 'creator' in local_var_params:
            query_params.append(('creator', local_var_params['creator']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'page_index' in local_var_params:
            query_params.append(('page_index', local_var_params['page_index']))
        if 'page_size' in local_var_params:
            query_params.append(('page_size', local_var_params['page_size']))

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

    def retry_diagnosis_task(self, request):
        r"""重试诊断任务

        重试诊断任务
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RetryDiagnosisTask
        :type request: :class:`huaweicloudsdkcoc.v1.RetryDiagnosisTaskRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.RetryDiagnosisTaskResponse`
        """
        http_info = self._retry_diagnosis_task_http_info(request)
        return self._call_api(**http_info)

    def retry_diagnosis_task_invoker(self, request):
        http_info = self._retry_diagnosis_task_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _retry_diagnosis_task_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/diagnosis/tasks/{task_id}/retry",
            "request_type": request.__class__.__name__,
            "response_type": "RetryDiagnosisTaskResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

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

    def show_diagnosis_node(self, request):
        r"""查询指定诊断记录下的指定诊断步骤的详情

        查询指定诊断记录下的指定诊断步骤的详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDiagnosisNode
        :type request: :class:`huaweicloudsdkcoc.v1.ShowDiagnosisNodeRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.ShowDiagnosisNodeResponse`
        """
        http_info = self._show_diagnosis_node_http_info(request)
        return self._call_api(**http_info)

    def show_diagnosis_node_invoker(self, request):
        http_info = self._show_diagnosis_node_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_diagnosis_node_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/diagnosis/tasks/{task_id}/node/{code}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDiagnosisNodeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']
        if 'code' in local_var_params:
            path_params['code'] = local_var_params['code']

        query_params = []
        if 'instance_id' in local_var_params:
            query_params.append(('instance_id', local_var_params['instance_id']))

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

    def show_diagnosis_summary(self, request):
        r"""查询批量诊断任务的结果概要

        查询诊断任务的结果概要
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDiagnosisSummary
        :type request: :class:`huaweicloudsdkcoc.v1.ShowDiagnosisSummaryRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.ShowDiagnosisSummaryResponse`
        """
        http_info = self._show_diagnosis_summary_http_info(request)
        return self._call_api(**http_info)

    def show_diagnosis_summary_invoker(self, request):
        http_info = self._show_diagnosis_summary_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_diagnosis_summary_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/diagnosis/tasks/{task_id}/summary",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDiagnosisSummaryResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

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

    def show_diagnosis_task(self, request):
        r"""查询单个诊断任务详情

        查询单个诊断任务详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDiagnosisTask
        :type request: :class:`huaweicloudsdkcoc.v1.ShowDiagnosisTaskRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.ShowDiagnosisTaskResponse`
        """
        http_info = self._show_diagnosis_task_http_info(request)
        return self._call_api(**http_info)

    def show_diagnosis_task_invoker(self, request):
        http_info = self._show_diagnosis_task_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_diagnosis_task_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/diagnosis/tasks/{task_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDiagnosisTaskResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

        query_params = []
        if 'instance_id' in local_var_params:
            query_params.append(('instance_id', local_var_params['instance_id']))

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

    def create_document(self, request):
        r"""创建自定义作业

        创建自定义作业
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateDocument
        :type request: :class:`huaweicloudsdkcoc.v1.CreateDocumentRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.CreateDocumentResponse`
        """
        http_info = self._create_document_http_info(request)
        return self._call_api(**http_info)

    def create_document_invoker(self, request):
        http_info = self._create_document_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_document_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/documents",
            "request_type": request.__class__.__name__,
            "response_type": "CreateDocumentResponse"
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

        response_headers = ["X-request-id", ]

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

    def delete_document(self, request):
        r"""删除自定义作业

        删除自定义作业
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteDocument
        :type request: :class:`huaweicloudsdkcoc.v1.DeleteDocumentRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.DeleteDocumentResponse`
        """
        http_info = self._delete_document_http_info(request)
        return self._call_api(**http_info)

    def delete_document_invoker(self, request):
        http_info = self._delete_document_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_document_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/documents/{document_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteDocumentResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'document_id' in local_var_params:
            path_params['document_id'] = local_var_params['document_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def execute_document(self, request):
        r"""执行自定义作业

        执行自定义作业
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ExecuteDocument
        :type request: :class:`huaweicloudsdkcoc.v1.ExecuteDocumentRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.ExecuteDocumentResponse`
        """
        http_info = self._execute_document_http_info(request)
        return self._call_api(**http_info)

    def execute_document_invoker(self, request):
        http_info = self._execute_document_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _execute_document_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/documents/{document_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ExecuteDocumentResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'document_id' in local_var_params:
            path_params['document_id'] = local_var_params['document_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def get_document(self, request):
        r"""查询自定义作业详情

        查询自定义作业详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for GetDocument
        :type request: :class:`huaweicloudsdkcoc.v1.GetDocumentRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.GetDocumentResponse`
        """
        http_info = self._get_document_http_info(request)
        return self._call_api(**http_info)

    def get_document_invoker(self, request):
        http_info = self._get_document_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _get_document_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/documents/{document_id}",
            "request_type": request.__class__.__name__,
            "response_type": "GetDocumentResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'document_id' in local_var_params:
            path_params['document_id'] = local_var_params['document_id']

        query_params = []
        if 'version' in local_var_params:
            query_params.append(('version', local_var_params['version']))
        if 'document_type' in local_var_params:
            query_params.append(('document_type', local_var_params['document_type']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def get_document_atomic_info(self, request):
        r"""获取原子能力详细

        获取原子能力详细
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for GetDocumentAtomicInfo
        :type request: :class:`huaweicloudsdkcoc.v1.GetDocumentAtomicInfoRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.GetDocumentAtomicInfoResponse`
        """
        http_info = self._get_document_atomic_info_http_info(request)
        return self._call_api(**http_info)

    def get_document_atomic_info_invoker(self, request):
        http_info = self._get_document_atomic_info_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _get_document_atomic_info_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/atomics/{atomic_unique_key}",
            "request_type": request.__class__.__name__,
            "response_type": "GetDocumentAtomicInfoResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'atomic_unique_key' in local_var_params:
            path_params['atomic_unique_key'] = local_var_params['atomic_unique_key']

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

    def list_document_atomics(self, request):
        r"""获取原子能力列表

        获取原子能力列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListDocumentAtomics
        :type request: :class:`huaweicloudsdkcoc.v1.ListDocumentAtomicsRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.ListDocumentAtomicsResponse`
        """
        http_info = self._list_document_atomics_http_info(request)
        return self._call_api(**http_info)

    def list_document_atomics_invoker(self, request):
        http_info = self._list_document_atomics_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_document_atomics_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/atomics",
            "request_type": request.__class__.__name__,
            "response_type": "ListDocumentAtomicsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
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

    def list_documents(self, request):
        r"""查询自定义作业列表

        查询自定义作业列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListDocuments
        :type request: :class:`huaweicloudsdkcoc.v1.ListDocumentsRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.ListDocumentsResponse`
        """
        http_info = self._list_documents_http_info(request)
        return self._call_api(**http_info)

    def list_documents_invoker(self, request):
        http_info = self._list_documents_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_documents_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/documents",
            "request_type": request.__class__.__name__,
            "response_type": "ListDocumentsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'name_like' in local_var_params:
            query_params.append(('name_like', local_var_params['name_like']))
        if 'creator' in local_var_params:
            query_params.append(('creator', local_var_params['creator']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'document_type' in local_var_params:
            query_params.append(('document_type', local_var_params['document_type']))

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

    def update_document(self, request):
        r"""修改自定义作业

        修改自定义作业
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateDocument
        :type request: :class:`huaweicloudsdkcoc.v1.UpdateDocumentRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.UpdateDocumentResponse`
        """
        http_info = self._update_document_http_info(request)
        return self._call_api(**http_info)

    def update_document_invoker(self, request):
        http_info = self._update_document_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_document_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/documents/{document_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateDocumentResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'document_id' in local_var_params:
            path_params['document_id'] = local_var_params['document_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def create_report_prometheus_event(self, request):
        r"""Prometheus事件接入

        Prometheus事件接入
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateReportPrometheusEvent
        :type request: :class:`huaweicloudsdkcoc.v1.CreateReportPrometheusEventRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.CreateReportPrometheusEventResponse`
        """
        http_info = self._create_report_prometheus_event_http_info(request)
        return self._call_api(**http_info)

    def create_report_prometheus_event_invoker(self, request):
        http_info = self._create_report_prometheus_event_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_report_prometheus_event_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/event/prometheus/{integration_key}",
            "request_type": request.__class__.__name__,
            "response_type": "CreateReportPrometheusEventResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'integration_key' in local_var_params:
            path_params['integration_key'] = local_var_params['integration_key']

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
            ['application/json; charset=utf-8'])

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

    def get_execution(self, request):
        r"""查询作业工单详情

        查询作业工单详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for GetExecution
        :type request: :class:`huaweicloudsdkcoc.v1.GetExecutionRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.GetExecutionResponse`
        """
        http_info = self._get_execution_http_info(request)
        return self._call_api(**http_info)

    def get_execution_invoker(self, request):
        http_info = self._get_execution_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _get_execution_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/executions/{execution_id}",
            "request_type": request.__class__.__name__,
            "response_type": "GetExecutionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'execution_id' in local_var_params:
            path_params['execution_id'] = local_var_params['execution_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def list_execution_instances(self, request):
        r"""查询工单步骤批次实例

        查询工单步骤批次实例，如脚本分批操作里的ECS实例
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListExecutionInstances
        :type request: :class:`huaweicloudsdkcoc.v1.ListExecutionInstancesRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.ListExecutionInstancesResponse`
        """
        http_info = self._list_execution_instances_http_info(request)
        return self._call_api(**http_info)

    def list_execution_instances_invoker(self, request):
        http_info = self._list_execution_instances_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_execution_instances_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/executions/instances",
            "request_type": request.__class__.__name__,
            "response_type": "ListExecutionInstancesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'execution_step_id' in local_var_params:
            query_params.append(('execution_step_id', local_var_params['execution_step_id']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def list_execution_steps(self, request):
        r"""查询工单步骤详情

        查询工单步骤详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListExecutionSteps
        :type request: :class:`huaweicloudsdkcoc.v1.ListExecutionStepsRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.ListExecutionStepsResponse`
        """
        http_info = self._list_execution_steps_http_info(request)
        return self._call_api(**http_info)

    def list_execution_steps_invoker(self, request):
        http_info = self._list_execution_steps_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_execution_steps_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/executions/{execution_id}/steps",
            "request_type": request.__class__.__name__,
            "response_type": "ListExecutionStepsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'execution_id' in local_var_params:
            path_params['execution_id'] = local_var_params['execution_id']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'execution_step_id_list' in local_var_params:
            query_params.append(('execution_step_id_list', local_var_params['execution_step_id_list']))
            collection_formats['execution_step_id_list'] = 'csv'

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def list_executions(self, request):
        r"""查询作业工单列表

        查询作业工单列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListExecutions
        :type request: :class:`huaweicloudsdkcoc.v1.ListExecutionsRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.ListExecutionsResponse`
        """
        http_info = self._list_executions_http_info(request)
        return self._call_api(**http_info)

    def list_executions_invoker(self, request):
        http_info = self._list_executions_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_executions_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/executions",
            "request_type": request.__class__.__name__,
            "response_type": "ListExecutionsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'creator' in local_var_params:
            query_params.append(('creator', local_var_params['creator']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'document_name' in local_var_params:
            query_params.append(('document_name', local_var_params['document_name']))
        if 'document_id' in local_var_params:
            query_params.append(('document_id', local_var_params['document_id']))
        if 'tags' in local_var_params:
            query_params.append(('tags', local_var_params['tags']))
        if 'exclude_child_executions' in local_var_params:
            query_params.append(('exclude_child_executions', local_var_params['exclude_child_executions']))

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

    def operate_execution(self, request):
        r"""操作工单

        操作工单
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for OperateExecution
        :type request: :class:`huaweicloudsdkcoc.v1.OperateExecutionRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.OperateExecutionResponse`
        """
        http_info = self._operate_execution_http_info(request)
        return self._call_api(**http_info)

    def operate_execution_invoker(self, request):
        http_info = self._operate_execution_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _operate_execution_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/executions",
            "request_type": request.__class__.__name__,
            "response_type": "OperateExecutionResponse"
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

    def list_sub_tickets(self, request):
        r"""搜索变更工单子单

        搜索变更工单子单。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListSubTickets
        :type request: :class:`huaweicloudsdkcoc.v1.ListSubTicketsRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.ListSubTicketsResponse`
        """
        http_info = self._list_sub_tickets_http_info(request)
        return self._call_api(**http_info)

    def list_sub_tickets_invoker(self, request):
        http_info = self._list_sub_tickets_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_sub_tickets_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{ticket_type}/tickets/{ticket_id}/list-sub-tickets",
            "request_type": request.__class__.__name__,
            "response_type": "ListSubTicketsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ticket_type' in local_var_params:
            path_params['ticket_type'] = local_var_params['ticket_type']
        if 'ticket_id' in local_var_params:
            path_params['ticket_id'] = local_var_params['ticket_id']

        query_params = []
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
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

    def execute_ticket_action(self, request):
        r"""工单操作

        变更单审批、撤销以及问题单的所有操作均通过此接口完成。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ExecuteTicketAction
        :type request: :class:`huaweicloudsdkcoc.v1.ExecuteTicketActionRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.ExecuteTicketActionResponse`
        """
        http_info = self._execute_ticket_action_http_info(request)
        return self._call_api(**http_info)

    def execute_ticket_action_invoker(self, request):
        http_info = self._execute_ticket_action_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _execute_ticket_action_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{ticket_type}/actions",
            "request_type": request.__class__.__name__,
            "response_type": "ExecuteTicketActionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ticket_type' in local_var_params:
            path_params['ticket_type'] = local_var_params['ticket_type']

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

    def list_ticket_operation_histories(self, request):
        r"""搜索工单历史

        List Histories
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListTicketOperationHistories
        :type request: :class:`huaweicloudsdkcoc.v1.ListTicketOperationHistoriesRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.ListTicketOperationHistoriesResponse`
        """
        http_info = self._list_ticket_operation_histories_http_info(request)
        return self._call_api(**http_info)

    def list_ticket_operation_histories_invoker(self, request):
        http_info = self._list_ticket_operation_histories_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_ticket_operation_histories_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{ticket_type}/list-histories",
            "request_type": request.__class__.__name__,
            "response_type": "ListTicketOperationHistoriesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ticket_type' in local_var_params:
            path_params['ticket_type'] = local_var_params['ticket_type']

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

    def list_tickets(self, request):
        r"""搜索工单

        List ticket
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListTickets
        :type request: :class:`huaweicloudsdkcoc.v1.ListTicketsRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.ListTicketsResponse`
        """
        http_info = self._list_tickets_http_info(request)
        return self._call_api(**http_info)

    def list_tickets_invoker(self, request):
        http_info = self._list_tickets_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_tickets_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{ticket_type}/list-tickets",
            "request_type": request.__class__.__name__,
            "response_type": "ListTicketsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ticket_type' in local_var_params:
            path_params['ticket_type'] = local_var_params['ticket_type']

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

    def show_ticket_info(self, request):
        r"""查询Ticket

        Get Ticket info by id
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowTicketInfo
        :type request: :class:`huaweicloudsdkcoc.v1.ShowTicketInfoRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.ShowTicketInfoResponse`
        """
        http_info = self._show_ticket_info_http_info(request)
        return self._call_api(**http_info)

    def show_ticket_info_invoker(self, request):
        http_info = self._show_ticket_info_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_ticket_info_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{ticket_type}/tickets/{ticket_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowTicketInfoResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ticket_type' in local_var_params:
            path_params['ticket_type'] = local_var_params['ticket_type']
        if 'ticket_id' in local_var_params:
            path_params['ticket_id'] = local_var_params['ticket_id']

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

    def delete_ticket_info(self, request):
        r"""删除变更单

        删除变更单，当变更单为撤销状态下，变更单可进行删除操作。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteTicketInfo
        :type request: :class:`huaweicloudsdkcoc.v1.DeleteTicketInfoRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.DeleteTicketInfoResponse`
        """
        http_info = self._delete_ticket_info_http_info(request)
        return self._call_api(**http_info)

    def delete_ticket_info_invoker(self, request):
        http_info = self._delete_ticket_info_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_ticket_info_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{ticket_type}/tickets/{ticket_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteTicketInfoResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ticket_type' in local_var_params:
            path_params['ticket_type'] = local_var_params['ticket_type']
        if 'ticket_id' in local_var_params:
            path_params['ticket_id'] = local_var_params['ticket_id']

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

    def update_ticket(self, request):
        r"""变更单状态修改

        变更单状态修改，请求路径中的ticket_type为固定值change，且ticket_id传递变更单单号。此接口可操作变更开始、变更结束、变更取消和添加变更结果操作。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateTicket
        :type request: :class:`huaweicloudsdkcoc.v1.UpdateTicketRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.UpdateTicketResponse`
        """
        http_info = self._update_ticket_http_info(request)
        return self._call_api(**http_info)

    def update_ticket_invoker(self, request):
        http_info = self._update_ticket_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_ticket_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{ticket_type}/tickets/{ticket_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateTicketResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ticket_type' in local_var_params:
            path_params['ticket_type'] = local_var_params['ticket_type']
        if 'ticket_id' in local_var_params:
            path_params['ticket_id'] = local_var_params['ticket_id']

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

    def create_coc_incident(self, request):
        r"""CreateExternalIncident 创建事件单

        CreateExternalIncident 创建事件单
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateCocIncident
        :type request: :class:`huaweicloudsdkcoc.v1.CreateCocIncidentRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.CreateCocIncidentResponse`
        """
        http_info = self._create_coc_incident_http_info(request)
        return self._call_api(**http_info)

    def create_coc_incident_invoker(self, request):
        http_info = self._create_coc_incident_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_coc_incident_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/external/incident/create",
            "request_type": request.__class__.__name__,
            "response_type": "CreateCocIncidentResponse"
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

    def create_external_coc_attachment(self, request):
        r"""上传附件

        上传附件，创建事件单的场景下，如需上传附件，需要先调用该接口将文件上传到obs。上传成功时，该接口将返回文档唯一id。支持文件类型：.jpg,.png,.docx,.txt,.pdf，且文本大小不超10M
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateExternalCocAttachment
        :type request: :class:`huaweicloudsdkcoc.v1.CreateExternalCocAttachmentRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.CreateExternalCocAttachmentResponse`
        """
        http_info = self._create_external_coc_attachment_http_info(request)
        return self._call_api(**http_info)

    def create_external_coc_attachment_invoker(self, request):
        http_info = self._create_external_coc_attachment_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_external_coc_attachment_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/external/incident/attachments",
            "request_type": request.__class__.__name__,
            "response_type": "CreateExternalCocAttachmentResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}
        if 'file' in local_var_params:
            form_params['file'] = local_var_params['file']

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['multipart/form-data'])

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

    def handle_coc_incident(self, request):
        r"""HandleCocIncident处理事件单

        HandleCocIncident 处理事件单
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for HandleCocIncident
        :type request: :class:`huaweicloudsdkcoc.v1.HandleCocIncidentRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.HandleCocIncidentResponse`
        """
        http_info = self._handle_coc_incident_http_info(request)
        return self._call_api(**http_info)

    def handle_coc_incident_invoker(self, request):
        http_info = self._handle_coc_incident_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _handle_coc_incident_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/external/incident/handle",
            "request_type": request.__class__.__name__,
            "response_type": "HandleCocIncidentResponse"
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

    def list_coc_ticket_operation_histories(self, request):
        r"""GetCocTicketOperationHistories 获取事件单历史

        ListCocTicketOperationHistories  获取事件单历史
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListCocTicketOperationHistories
        :type request: :class:`huaweicloudsdkcoc.v1.ListCocTicketOperationHistoriesRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.ListCocTicketOperationHistoriesResponse`
        """
        http_info = self._list_coc_ticket_operation_histories_http_info(request)
        return self._call_api(**http_info)

    def list_coc_ticket_operation_histories_invoker(self, request):
        http_info = self._list_coc_ticket_operation_histories_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_coc_ticket_operation_histories_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/external/{ticket_type}/list-histories",
            "request_type": request.__class__.__name__,
            "response_type": "ListCocTicketOperationHistoriesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ticket_type' in local_var_params:
            path_params['ticket_type'] = local_var_params['ticket_type']

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

    def list_incident_simple_tickets(self, request):
        r"""查询简易版事件单列表

        该接口可分页查询到事件单列表信息，分页参数为limit与offset。该接口不支持对事件单进行除分页参数外的条件过滤，且返回的列表字段相对简单，只有事件单标题、事件单单号、描述信息、工单状态、事件级别、企业项目ID、事件单来源、创建人及责任人。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListIncidentSimpleTickets
        :type request: :class:`huaweicloudsdkcoc.v1.ListIncidentSimpleTicketsRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.ListIncidentSimpleTicketsResponse`
        """
        http_info = self._list_incident_simple_tickets_http_info(request)
        return self._call_api(**http_info)

    def list_incident_simple_tickets_invoker(self, request):
        http_info = self._list_incident_simple_tickets_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_incident_simple_tickets_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/incident-tickets",
            "request_type": request.__class__.__name__,
            "response_type": "ListIncidentSimpleTicketsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
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

    def show_coc_incident_detail(self, request):
        r"""GetCocIncidentDetail 获取事件单详细

        ShowCocIncidentDetail  获取事件单详细
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowCocIncidentDetail
        :type request: :class:`huaweicloudsdkcoc.v1.ShowCocIncidentDetailRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.ShowCocIncidentDetailResponse`
        """
        http_info = self._show_coc_incident_detail_http_info(request)
        return self._call_api(**http_info)

    def show_coc_incident_detail_invoker(self, request):
        http_info = self._show_coc_incident_detail_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_coc_incident_detail_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/external/incident/{incident_num}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowCocIncidentDetailResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'incident_num' in local_var_params:
            path_params['incident_num'] = local_var_params['incident_num']

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

    def create_coc_issues(self, request):
        r"""CreateExternalIssues 创建问题单

        CreateExternalIssues 创建问题单
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateCocIssues
        :type request: :class:`huaweicloudsdkcoc.v1.CreateCocIssuesRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.CreateCocIssuesResponse`
        """
        http_info = self._create_coc_issues_http_info(request)
        return self._call_api(**http_info)

    def create_coc_issues_invoker(self, request):
        http_info = self._create_coc_issues_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_coc_issues_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/external/issues/create",
            "request_type": request.__class__.__name__,
            "response_type": "CreateCocIssuesResponse"
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

    def show_coc_issues_detail(self, request):
        r"""GetCocIssuesDetail 获取事件单详细

        ShowCocIssuesDetail  获取事件单详细
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowCocIssuesDetail
        :type request: :class:`huaweicloudsdkcoc.v1.ShowCocIssuesDetailRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.ShowCocIssuesDetailResponse`
        """
        http_info = self._show_coc_issues_detail_http_info(request)
        return self._call_api(**http_info)

    def show_coc_issues_detail_invoker(self, request):
        http_info = self._show_coc_issues_detail_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_coc_issues_detail_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/external/issues/{ticket_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowCocIssuesDetailResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ticket_id' in local_var_params:
            path_params['ticket_id'] = local_var_params['ticket_id']

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

    def create_attachment(self, request):
        r"""上传附件

        上传附件，创建工单（事件单、变更单、问题单）的场景下，如需上传附件，需要先调用该接口将文件上传到obs。上传成功时，该接口将返回文档唯一id。支持文件类型：.jpg,.png,.docx,.txt,.pdf，且文本大小不超10M。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateAttachment
        :type request: :class:`huaweicloudsdkcoc.v1.CreateAttachmentRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.CreateAttachmentResponse`
        """
        http_info = self._create_attachment_http_info(request)
        return self._call_api(**http_info)

    def create_attachment_invoker(self, request):
        http_info = self._create_attachment_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_attachment_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{ticket_type}/attachments",
            "request_type": request.__class__.__name__,
            "response_type": "CreateAttachmentResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ticket_type' in local_var_params:
            path_params['ticket_type'] = local_var_params['ticket_type']

        query_params = []

        header_params = {}

        form_params = {}
        if 'file' in local_var_params:
            form_params['file'] = local_var_params['file']

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['multipart/form-data'])

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

    def create_ticket(self, request):
        r"""新建工单

        创建变更单或问题单的接口，通过路径参数ticket_type区分需要创建的工单类型。ticket_type为change表示要创建变更单，ticket_type为issues_mgmt为创建问题单。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateTicket
        :type request: :class:`huaweicloudsdkcoc.v1.CreateTicketRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.CreateTicketResponse`
        """
        http_info = self._create_ticket_http_info(request)
        return self._call_api(**http_info)

    def create_ticket_invoker(self, request):
        http_info = self._create_ticket_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_ticket_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{ticket_type}/tickets",
            "request_type": request.__class__.__name__,
            "response_type": "CreateTicketResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ticket_type' in local_var_params:
            path_params['ticket_type'] = local_var_params['ticket_type']

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

    def download_attachment(self, request):
        r"""下载附件

        附件下载操作需基于已上传的附件资源。上传附件时，需调用/v1/{ticket_type}/attachments接口完成上传；成功上传后，可从接口响应中获取doc_id参数。下载附件时，凭借此doc_id再次调用/v1/{ticket_type}/attachments接口，即可获取已上传的对应附件资源，实现附件全生命周期管理。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DownloadAttachment
        :type request: :class:`huaweicloudsdkcoc.v1.DownloadAttachmentRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.DownloadAttachmentResponse`
        """
        http_info = self._download_attachment_http_info(request)
        return self._call_api(**http_info)

    def download_attachment_invoker(self, request):
        http_info = self._download_attachment_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _download_attachment_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{ticket_type}/attachments/{doc_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DownloadAttachmentResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ticket_type' in local_var_params:
            path_params['ticket_type'] = local_var_params['ticket_type']
        if 'doc_id' in local_var_params:
            path_params['doc_id'] = local_var_params['doc_id']

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

    def list_authorizable_tickets_external(self, request):
        r"""查询COC可授权单列表

        查询COC可授权单列表（变更单号、事件单号、warroom和告警）
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAuthorizableTicketsExternal
        :type request: :class:`huaweicloudsdkcoc.v1.ListAuthorizableTicketsExternalRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.ListAuthorizableTicketsExternalResponse`
        """
        http_info = self._list_authorizable_tickets_external_http_info(request)
        return self._call_api(**http_info)

    def list_authorizable_tickets_external_invoker(self, request):
        http_info = self._list_authorizable_tickets_external_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_authorizable_tickets_external_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/external/list/authorizable-tickets",
            "request_type": request.__class__.__name__,
            "response_type": "ListAuthorizableTicketsExternalResponse"
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

    def list_script_resource_tags(self, request):
        r"""查询资源标签列表

        查询资源标签列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListScriptResourceTags
        :type request: :class:`huaweicloudsdkcoc.v1.ListScriptResourceTagsRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.ListScriptResourceTagsResponse`
        """
        http_info = self._list_script_resource_tags_http_info(request)
        return self._call_api(**http_info)

    def list_script_resource_tags_invoker(self, request):
        http_info = self._list_script_resource_tags_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_script_resource_tags_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/script/{resource_type}/tags",
            "request_type": request.__class__.__name__,
            "response_type": "ListScriptResourceTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_type' in local_var_params:
            path_params['resource_type'] = local_var_params['resource_type']

        query_params = []
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

    def update_resource_tags(self, request):
        r"""更新资源标签

        更新资源标签
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateResourceTags
        :type request: :class:`huaweicloudsdkcoc.v1.UpdateResourceTagsRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.UpdateResourceTagsResponse`
        """
        http_info = self._update_resource_tags_http_info(request)
        return self._call_api(**http_info)

    def update_resource_tags_invoker(self, request):
        http_info = self._update_resource_tags_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_resource_tags_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/script/{resource_type}/{resource_id}/tags/update",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateResourceTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_id' in local_var_params:
            path_params['resource_id'] = local_var_params['resource_id']
        if 'resource_type' in local_var_params:
            path_params['resource_type'] = local_var_params['resource_type']

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

    def create_scheduled_task(self, request):
        r"""新建定时运维

        Create Scheduled Task
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateScheduledTask
        :type request: :class:`huaweicloudsdkcoc.v1.CreateScheduledTaskRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.CreateScheduledTaskResponse`
        """
        http_info = self._create_scheduled_task_http_info(request)
        return self._call_api(**http_info)

    def create_scheduled_task_invoker(self, request):
        http_info = self._create_scheduled_task_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_scheduled_task_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/schedule/task",
            "request_type": request.__class__.__name__,
            "response_type": "CreateScheduledTaskResponse"
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

    def delete_scheduled_task(self, request):
        r"""删除ScheduledTask

        Delete scheduled task by id
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteScheduledTask
        :type request: :class:`huaweicloudsdkcoc.v1.DeleteScheduledTaskRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.DeleteScheduledTaskResponse`
        """
        http_info = self._delete_scheduled_task_http_info(request)
        return self._call_api(**http_info)

    def delete_scheduled_task_invoker(self, request):
        http_info = self._delete_scheduled_task_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_scheduled_task_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/schedule/task/{task_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteScheduledTaskResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

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

    def disable_scheduled_task(self, request):
        r"""禁用ScheduledTask

        Disable scheduled task by id
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DisableScheduledTask
        :type request: :class:`huaweicloudsdkcoc.v1.DisableScheduledTaskRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.DisableScheduledTaskResponse`
        """
        http_info = self._disable_scheduled_task_http_info(request)
        return self._call_api(**http_info)

    def disable_scheduled_task_invoker(self, request):
        http_info = self._disable_scheduled_task_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _disable_scheduled_task_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/schedule/task/{task_id}/disable",
            "request_type": request.__class__.__name__,
            "response_type": "DisableScheduledTaskResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

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

    def enable_scheduled_task(self, request):
        r"""启用ScheduledTask

        Enable scheduled task by id
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for EnableScheduledTask
        :type request: :class:`huaweicloudsdkcoc.v1.EnableScheduledTaskRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.EnableScheduledTaskResponse`
        """
        http_info = self._enable_scheduled_task_http_info(request)
        return self._call_api(**http_info)

    def enable_scheduled_task_invoker(self, request):
        http_info = self._enable_scheduled_task_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _enable_scheduled_task_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/schedule/task/{task_id}/enable",
            "request_type": request.__class__.__name__,
            "response_type": "EnableScheduledTaskResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

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

    def list_scheduled_task(self, request):
        r"""查询ScheduledTask列表

        Get ScheduledTask infos
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListScheduledTask
        :type request: :class:`huaweicloudsdkcoc.v1.ListScheduledTaskRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.ListScheduledTaskResponse`
        """
        http_info = self._list_scheduled_task_http_info(request)
        return self._call_api(**http_info)

    def list_scheduled_task_invoker(self, request):
        http_info = self._list_scheduled_task_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_scheduled_task_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/schedule/task",
            "request_type": request.__class__.__name__,
            "response_type": "ListScheduledTaskResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'task_id' in local_var_params:
            query_params.append(('task_id', local_var_params['task_id']))
        if 'task_name' in local_var_params:
            query_params.append(('task_name', local_var_params['task_name']))
        if 'scheduled_type' in local_var_params:
            query_params.append(('scheduled_type', local_var_params['scheduled_type']))
        if 'task_type' in local_var_params:
            query_params.append(('task_type', local_var_params['task_type']))
        if 'associated_task_type' in local_var_params:
            query_params.append(('associated_task_type', local_var_params['associated_task_type']))
        if 'risk_level' in local_var_params:
            query_params.append(('risk_level', local_var_params['risk_level']))
        if 'created_by' in local_var_params:
            query_params.append(('created_by', local_var_params['created_by']))
        if 'reviewer' in local_var_params:
            query_params.append(('reviewer', local_var_params['reviewer']))
        if 'reviewer_user_name' in local_var_params:
            query_params.append(('reviewer_user_name', local_var_params['reviewer_user_name']))
        if 'approve_status' in local_var_params:
            query_params.append(('approve_status', local_var_params['approve_status']))
        if 'last_execution_status' in local_var_params:
            query_params.append(('last_execution_status', local_var_params['last_execution_status']))
        if 'last_execution_start_time' in local_var_params:
            query_params.append(('last_execution_start_time', local_var_params['last_execution_start_time']))
        if 'last_execution_end_time' in local_var_params:
            query_params.append(('last_execution_end_time', local_var_params['last_execution_end_time']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'region_id' in local_var_params:
            query_params.append(('region_id', local_var_params['region_id']))
        if 'resource_id' in local_var_params:
            query_params.append(('resource_id', local_var_params['resource_id']))
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

    def list_scheduled_task_history(self, request):
        r"""查询定时运维历史记录

        get scheduled task history list
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListScheduledTaskHistory
        :type request: :class:`huaweicloudsdkcoc.v1.ListScheduledTaskHistoryRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.ListScheduledTaskHistoryResponse`
        """
        http_info = self._list_scheduled_task_history_http_info(request)
        return self._call_api(**http_info)

    def list_scheduled_task_history_invoker(self, request):
        http_info = self._list_scheduled_task_history_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_scheduled_task_history_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/schedule/task/history",
            "request_type": request.__class__.__name__,
            "response_type": "ListScheduledTaskHistoryResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'task_id' in local_var_params:
            query_params.append(('task_id', local_var_params['task_id']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'region' in local_var_params:
            query_params.append(('region', local_var_params['region']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'started_start_time' in local_var_params:
            query_params.append(('started_start_time', local_var_params['started_start_time']))
        if 'started_end_time' in local_var_params:
            query_params.append(('started_end_time', local_var_params['started_end_time']))
        if 'finished_start_time' in local_var_params:
            query_params.append(('finished_start_time', local_var_params['finished_start_time']))
        if 'finished_end_time' in local_var_params:
            query_params.append(('finished_end_time', local_var_params['finished_end_time']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))

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

    def show_scheduled_task(self, request):
        r"""查询ScheduledTask

        Get ScheduledTask info by id
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowScheduledTask
        :type request: :class:`huaweicloudsdkcoc.v1.ShowScheduledTaskRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.ShowScheduledTaskResponse`
        """
        http_info = self._show_scheduled_task_http_info(request)
        return self._call_api(**http_info)

    def show_scheduled_task_invoker(self, request):
        http_info = self._show_scheduled_task_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_scheduled_task_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/schedule/task/{task_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowScheduledTaskResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

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

    def update_scheduled_task(self, request):
        r"""修改ScheduledTask

        Update ScheduledTask
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateScheduledTask
        :type request: :class:`huaweicloudsdkcoc.v1.UpdateScheduledTaskRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.UpdateScheduledTaskResponse`
        """
        http_info = self._update_scheduled_task_http_info(request)
        return self._call_api(**http_info)

    def update_scheduled_task_invoker(self, request):
        http_info = self._update_scheduled_task_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_scheduled_task_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/schedule/task/{task_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateScheduledTaskResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

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

    def get_script_job_batch(self, request):
        r"""展示批次详情

        查询：批次详情，分页获取批次中的实例列表。
        过滤条件：分页参数
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for GetScriptJobBatch
        :type request: :class:`huaweicloudsdkcoc.v1.GetScriptJobBatchRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.GetScriptJobBatchResponse`
        """
        http_info = self._get_script_job_batch_http_info(request)
        return self._call_api(**http_info)

    def get_script_job_batch_invoker(self, request):
        http_info = self._get_script_job_batch_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _get_script_job_batch_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/job/script/orders/{execute_uuid}/batches/{batch_index}",
            "request_type": request.__class__.__name__,
            "response_type": "GetScriptJobBatchResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'batch_index' in local_var_params:
            path_params['batch_index'] = local_var_params['batch_index']
        if 'execute_uuid' in local_var_params:
            path_params['execute_uuid'] = local_var_params['execute_uuid']

        query_params = []
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']
        if 'x_project_id' in local_var_params:
            header_params['x-project-id'] = local_var_params['x_project_id']
        if 'x_user_profile' in local_var_params:
            header_params['x-user-profile'] = local_var_params['x_user_profile']

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

    def get_script_job_info(self, request):
        r"""展示脚本工单基本信息

        查询执行：基本信息
        执行类型、执行名称、创建人、创建时间、结束时间、执行状态、标签（脚本id，脚本名，执行脚本参数，执行用户，超时时长、成功率阈值）
        
        不同的任务类型消费标签中的不同key
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for GetScriptJobInfo
        :type request: :class:`huaweicloudsdkcoc.v1.GetScriptJobInfoRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.GetScriptJobInfoResponse`
        """
        http_info = self._get_script_job_info_http_info(request)
        return self._call_api(**http_info)

    def get_script_job_info_invoker(self, request):
        http_info = self._get_script_job_info_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _get_script_job_info_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/job/script/orders/{execute_uuid}",
            "request_type": request.__class__.__name__,
            "response_type": "GetScriptJobInfoResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'execute_uuid' in local_var_params:
            path_params['execute_uuid'] = local_var_params['execute_uuid']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']
        if 'x_project_id' in local_var_params:
            header_params['x-project-id'] = local_var_params['x_project_id']
        if 'x_user_profile' in local_var_params:
            header_params['x-user-profile'] = local_var_params['x_user_profile']

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

    def get_script_job_statistics(self, request):
        r"""展示实例状态统计信息

        查询：实例状态统计信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for GetScriptJobStatistics
        :type request: :class:`huaweicloudsdkcoc.v1.GetScriptJobStatisticsRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.GetScriptJobStatisticsResponse`
        """
        http_info = self._get_script_job_statistics_http_info(request)
        return self._call_api(**http_info)

    def get_script_job_statistics_invoker(self, request):
        http_info = self._get_script_job_statistics_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _get_script_job_statistics_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/job/script/orders/{execute_uuid}/statistics",
            "request_type": request.__class__.__name__,
            "response_type": "GetScriptJobStatisticsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'execute_uuid' in local_var_params:
            path_params['execute_uuid'] = local_var_params['execute_uuid']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']
        if 'x_project_id' in local_var_params:
            header_params['x-project-id'] = local_var_params['x_project_id']
        if 'x_user_profile' in local_var_params:
            header_params['x-user-profile'] = local_var_params['x_user_profile']

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

    def list_script_job_batches(self, request):
        r"""展示批次列表

        查询：批次列表
        返回：批次index、批次标签
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListScriptJobBatches
        :type request: :class:`huaweicloudsdkcoc.v1.ListScriptJobBatchesRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.ListScriptJobBatchesResponse`
        """
        http_info = self._list_script_job_batches_http_info(request)
        return self._call_api(**http_info)

    def list_script_job_batches_invoker(self, request):
        http_info = self._list_script_job_batches_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_script_job_batches_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/job/script/orders/{execute_uuid}/batches",
            "request_type": request.__class__.__name__,
            "response_type": "ListScriptJobBatchesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'execute_uuid' in local_var_params:
            path_params['execute_uuid'] = local_var_params['execute_uuid']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']
        if 'x_project_id' in local_var_params:
            header_params['x-project-id'] = local_var_params['x_project_id']
        if 'x_user_profile' in local_var_params:
            header_params['x-user-profile'] = local_var_params['x_user_profile']

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

    def list_script_jobs(self, request):
        r"""展示工单列表

        查询作业工单列表，分页查询
        过滤：创建时间开始，创建时间结束、创建人
        返回：id、脚本名称、区域、创建人、创建时间、结束时间、总耗时、状态
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListScriptJobs
        :type request: :class:`huaweicloudsdkcoc.v1.ListScriptJobsRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.ListScriptJobsResponse`
        """
        http_info = self._list_script_jobs_http_info(request)
        return self._call_api(**http_info)

    def list_script_jobs_invoker(self, request):
        http_info = self._list_script_jobs_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_script_jobs_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/job/script/orders",
            "request_type": request.__class__.__name__,
            "response_type": "ListScriptJobsResponse"
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
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'creator' in local_var_params:
            query_params.append(('creator', local_var_params['creator']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']
        if 'x_project_id' in local_var_params:
            header_params['x-project-id'] = local_var_params['x_project_id']
        if 'x_user_profile' in local_var_params:
            header_params['x-user-profile'] = local_var_params['x_user_profile']

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

    def operate_script_job(self, request):
        r"""操作脚本工单

        操作类型：取消实例、跳过批次、取消整个工单、暂停整个工单、继续整个工单
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for OperateScriptJob
        :type request: :class:`huaweicloudsdkcoc.v1.OperateScriptJobRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.OperateScriptJobResponse`
        """
        http_info = self._operate_script_job_http_info(request)
        return self._call_api(**http_info)

    def operate_script_job_invoker(self, request):
        http_info = self._operate_script_job_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _operate_script_job_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/job/script/orders/{execute_uuid}/operation",
            "request_type": request.__class__.__name__,
            "response_type": "OperateScriptJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'execute_uuid' in local_var_params:
            path_params['execute_uuid'] = local_var_params['execute_uuid']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']
        if 'x_project_id' in local_var_params:
            header_params['x-project-id'] = local_var_params['x_project_id']
        if 'x_user_profile' in local_var_params:
            header_params['x-user-profile'] = local_var_params['x_user_profile']

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

    def accept_script(self, request):
        r"""审批待审批的脚本

        功能：审批脚本。
        约束条件：只有创建脚本填写了审批人，脚本为待审批状态才能审批。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AcceptScript
        :type request: :class:`huaweicloudsdkcoc.v1.AcceptScriptRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.AcceptScriptResponse`
        """
        http_info = self._accept_script_http_info(request)
        return self._call_api(**http_info)

    def accept_script_invoker(self, request):
        http_info = self._accept_script_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _accept_script_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/job/scripts/{script_uuid}/action",
            "request_type": request.__class__.__name__,
            "response_type": "AcceptScriptResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'script_uuid' in local_var_params:
            path_params['script_uuid'] = local_var_params['script_uuid']

        query_params = []

        header_params = {}
        if 'x_project_id' in local_var_params:
            header_params['x-project-id'] = local_var_params['x_project_id']
        if 'x_user_profile' in local_var_params:
            header_params['x-user-profile'] = local_var_params['x_user_profile']
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def check_script_risk(self, request):
        r"""评估脚本风险等级

        根据作业内容，对作业评估风险，返回相关分析的结果和信息，结果仅供参考。
        高危命令指影响系统或服务的正常运行，或造成系统特殊文件被恶意删除或修改命令。 高危命令检测通过校验规则正则匹配脚本内容中是否包含高危命令。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CheckScriptRisk
        :type request: :class:`huaweicloudsdkcoc.v1.CheckScriptRiskRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.CheckScriptRiskResponse`
        """
        http_info = self._check_script_risk_http_info(request)
        return self._call_api(**http_info)

    def check_script_risk_invoker(self, request):
        http_info = self._check_script_risk_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _check_script_risk_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/job/analyze-job",
            "request_type": request.__class__.__name__,
            "response_type": "CheckScriptRiskResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']
        if 'x_project_id' in local_var_params:
            header_params['x-project-id'] = local_var_params['x_project_id']
        if 'x_user_profile' in local_var_params:
            header_params['x-user-profile'] = local_var_params['x_user_profile']

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

    def create_script(self, request):
        r"""创建脚本

        创建作业脚本：自定义脚本
        - 脚本有标签属性，表示是高危脚本。创建时候不需要对脚本进行是否是高危的二次校验。
        - 进行租户隔离；北向接口创建的脚本，审批人字段不填写，默认不需要审批
        - 约束条件：
        - 脚本名称：同一租户下，脚本名称不能重复，最大字符64个字符，支持中文+字母+数字+下划线。
        - 脚本内容最大100kb。
        - 脚本参数个数最多20个。
        - 脚本描述：最大256个字符。
        - 单个参数的参数名称 64个字符，只支持字母+数字+下划线。
        - 单个参数的值最大1024个字符，正则表达式如下：^((?!\\.{2,})[a-zA-Z0-9_\\-/\\.\\*\\x20\\?:\&quot;,&#x3D;+@\\\\\\[\\{\\]\\}])*$。
        - 审批人最多支持5人。
        - 脚本输出的日志总量只支持1MB。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateScript
        :type request: :class:`huaweicloudsdkcoc.v1.CreateScriptRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.CreateScriptResponse`
        """
        http_info = self._create_script_http_info(request)
        return self._call_api(**http_info)

    def create_script_invoker(self, request):
        http_info = self._create_script_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_script_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/job/scripts",
            "request_type": request.__class__.__name__,
            "response_type": "CreateScriptResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_project_id' in local_var_params:
            header_params['x-project-id'] = local_var_params['x_project_id']
        if 'x_user_profile' in local_var_params:
            header_params['x-user-profile'] = local_var_params['x_user_profile']
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def delete_script(self, request):
        r"""删除自定义脚本

        删除作业脚本：自定义脚本。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteScript
        :type request: :class:`huaweicloudsdkcoc.v1.DeleteScriptRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.DeleteScriptResponse`
        """
        http_info = self._delete_script_http_info(request)
        return self._call_api(**http_info)

    def delete_script_invoker(self, request):
        http_info = self._delete_script_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_script_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/job/scripts/{script_uuid}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteScriptResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'script_uuid' in local_var_params:
            path_params['script_uuid'] = local_var_params['script_uuid']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']
        if 'x_project_id' in local_var_params:
            header_params['x-project-id'] = local_var_params['x_project_id']
        if 'x_user_profile' in local_var_params:
            header_params['x-user-profile'] = local_var_params['x_user_profile']

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

    def execute_script(self, request):
        r"""执行自定义脚本

        执行脚本
        
        脚本入参、超时时间、执行用户、资源受限
        脚本入参支持20个。
        单次下发的机器支持200个。
        单次批次内机器数量最大10个。
        最大批次数量为20批。
        脚本输出的日志总量只支持1MB。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ExecuteScript
        :type request: :class:`huaweicloudsdkcoc.v1.ExecuteScriptRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.ExecuteScriptResponse`
        """
        http_info = self._execute_script_http_info(request)
        return self._call_api(**http_info)

    def execute_script_invoker(self, request):
        http_info = self._execute_script_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _execute_script_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/job/scripts/{script_uuid}",
            "request_type": request.__class__.__name__,
            "response_type": "ExecuteScriptResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'script_uuid' in local_var_params:
            path_params['script_uuid'] = local_var_params['script_uuid']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']
        if 'x_project_id' in local_var_params:
            header_params['x-project-id'] = local_var_params['x_project_id']
        if 'x_user_profile' in local_var_params:
            header_params['x-user-profile'] = local_var_params['x_user_profile']

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

    def get_script(self, request):
        r"""获取自定义脚本详情

        获取脚本详情
        约束条件：
        只能查询自定义脚本详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for GetScript
        :type request: :class:`huaweicloudsdkcoc.v1.GetScriptRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.GetScriptResponse`
        """
        http_info = self._get_script_http_info(request)
        return self._call_api(**http_info)

    def get_script_invoker(self, request):
        http_info = self._get_script_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _get_script_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/job/scripts/{script_uuid}",
            "request_type": request.__class__.__name__,
            "response_type": "GetScriptResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'script_uuid' in local_var_params:
            path_params['script_uuid'] = local_var_params['script_uuid']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']
        if 'x_project_id' in local_var_params:
            header_params['x-project-id'] = local_var_params['x_project_id']
        if 'x_user_profile' in local_var_params:
            header_params['x-user-profile'] = local_var_params['x_user_profile']

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

    def list_instances_batch(self, request):
        r"""获取自动分批结果

        根据分批策略获取分批结果，只支持自动分批：
        规则如下：
        1.单个批次的所有实例必须属于同一个区域；
             * 2.单个批次的所有实例必须属于同一个可用区；
             * 3.单个批次的所有实例必须属于同一个应用；
             * 4.单个批次内同一分组下的实例不超过50%（除分组下仅以一个实例的情况外）；
             * 5.前三批每批节点数量不超过10。
             * 6.每批次实例数量不超过10。
        
           总机器数量为200。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListInstancesBatch
        :type request: :class:`huaweicloudsdkcoc.v1.ListInstancesBatchRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.ListInstancesBatchResponse`
        """
        http_info = self._list_instances_batch_http_info(request)
        return self._call_api(**http_info)

    def list_instances_batch_invoker(self, request):
        http_info = self._list_instances_batch_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_instances_batch_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/instances/batches",
            "request_type": request.__class__.__name__,
            "response_type": "ListInstancesBatchResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']
        if 'x_project_id' in local_var_params:
            header_params['x-project-id'] = local_var_params['x_project_id']
        if 'x_user_profile' in local_var_params:
            header_params['x-user-profile'] = local_var_params['x_user_profile']

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

    def list_scripts(self, request):
        r"""查询脚本列表

        作业脚本列表：自定义脚本
        
        limit最大为100
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListScripts
        :type request: :class:`huaweicloudsdkcoc.v1.ListScriptsRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.ListScriptsResponse`
        """
        http_info = self._list_scripts_http_info(request)
        return self._call_api(**http_info)

    def list_scripts_invoker(self, request):
        http_info = self._list_scripts_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_scripts_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/job/scripts",
            "request_type": request.__class__.__name__,
            "response_type": "ListScriptsResponse"
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
        if 'name_like' in local_var_params:
            query_params.append(('name_like', local_var_params['name_like']))
        if 'creator' in local_var_params:
            query_params.append(('creator', local_var_params['creator']))
        if 'risk_level' in local_var_params:
            query_params.append(('risk_level', local_var_params['risk_level']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']
        if 'x_project_id' in local_var_params:
            header_params['x-project-id'] = local_var_params['x_project_id']
        if 'x_user_profile' in local_var_params:
            header_params['x-user-profile'] = local_var_params['x_user_profile']

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

    def update_script(self, request):
        r"""修改脚本

        修改作业脚本：自定义脚本
        约束条件：
        脚本名称：同一租户下，脚本名称不能重复，最大字符64个字符，支持中文+字母+数字+下划线。
        脚本内容最大4096个字符。
        脚本参数个数最多20个。
        脚本描述：最大256个字符。
        单个参数的参数名称 64个字符，只支持字母+数字+下划线。
        单个参数的值最大1024个字符，正则表达式如下：^((?!.{2,})[a-zA-Z0-9_-/.*\\x20?:\&quot;,&#x3D;+@\\[{]}])*$。
        修改的脚本如果有审批人，在修改之后，需要再次选择审批人，查询审批
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateScript
        :type request: :class:`huaweicloudsdkcoc.v1.UpdateScriptRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.UpdateScriptResponse`
        """
        http_info = self._update_script_http_info(request)
        return self._call_api(**http_info)

    def update_script_invoker(self, request):
        http_info = self._update_script_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_script_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/job/scripts/{script_uuid}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateScriptResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'script_uuid' in local_var_params:
            path_params['script_uuid'] = local_var_params['script_uuid']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']
        if 'x_project_id' in local_var_params:
            header_params['x-project-id'] = local_var_params['x_project_id']
        if 'x_user_profile' in local_var_params:
            header_params['x-user-profile'] = local_var_params['x_user_profile']

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

    def execute_public_script(self, request):
        r"""执行公共脚本

        执行公共脚本
        脚本入参、超时时间、执行用户、资源受限
        脚本入参支持20个。
        单次下发的机器支持200个。
        单次批次内机器数量最大10个。
        最大批次数量为20批。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ExecutePublicScript
        :type request: :class:`huaweicloudsdkcoc.v1.ExecutePublicScriptRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.ExecutePublicScriptResponse`
        """
        http_info = self._execute_public_script_http_info(request)
        return self._call_api(**http_info)

    def execute_public_script_invoker(self, request):
        http_info = self._execute_public_script_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _execute_public_script_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/job/public-scripts/{script_uuid}",
            "request_type": request.__class__.__name__,
            "response_type": "ExecutePublicScriptResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'script_uuid' in local_var_params:
            path_params['script_uuid'] = local_var_params['script_uuid']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']
        if 'x_project_id' in local_var_params:
            header_params['x-project-id'] = local_var_params['x_project_id']
        if 'x_user_profile' in local_var_params:
            header_params['x-user-profile'] = local_var_params['x_user_profile']

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

    def get_public_script(self, request):
        r"""展示公共脚本详情

        展示公共脚本详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for GetPublicScript
        :type request: :class:`huaweicloudsdkcoc.v1.GetPublicScriptRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.GetPublicScriptResponse`
        """
        http_info = self._get_public_script_http_info(request)
        return self._call_api(**http_info)

    def get_public_script_invoker(self, request):
        http_info = self._get_public_script_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _get_public_script_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/job/public-scripts/{script_uuid}",
            "request_type": request.__class__.__name__,
            "response_type": "GetPublicScriptResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'script_uuid' in local_var_params:
            path_params['script_uuid'] = local_var_params['script_uuid']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']
        if 'x_project_id' in local_var_params:
            header_params['x-project-id'] = local_var_params['x_project_id']
        if 'x_user_profile' in local_var_params:
            header_params['x-user-profile'] = local_var_params['x_user_profile']

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

    def list_public_scripts(self, request):
        r"""获取公共脚本列表

        获取公共脚本列表，分页逻辑：采用limit+marker方式，提高分页效率。用自增id作为marker参数
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListPublicScripts
        :type request: :class:`huaweicloudsdkcoc.v1.ListPublicScriptsRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.ListPublicScriptsResponse`
        """
        http_info = self._list_public_scripts_http_info(request)
        return self._call_api(**http_info)

    def list_public_scripts_invoker(self, request):
        http_info = self._list_public_scripts_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_public_scripts_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/job/public-scripts",
            "request_type": request.__class__.__name__,
            "response_type": "ListPublicScriptsResponse"
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
        if 'name_like' in local_var_params:
            query_params.append(('name_like', local_var_params['name_like']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'risk_level' in local_var_params:
            query_params.append(('risk_level', local_var_params['risk_level']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']
        if 'x_project_id' in local_var_params:
            header_params['x-project-id'] = local_var_params['x_project_id']
        if 'x_user_profile' in local_var_params:
            header_params['x-user-profile'] = local_var_params['x_user_profile']

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

    def create_war_room(self, request):
        r"""创建租户区WarRoom

        创建租户区WarRoom
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateWarRoom
        :type request: :class:`huaweicloudsdkcoc.v1.CreateWarRoomRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.CreateWarRoomResponse`
        """
        http_info = self._create_war_room_http_info(request)
        return self._call_api(**http_info)

    def create_war_room_invoker(self, request):
        http_info = self._create_war_room_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_war_room_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/external/warrooms",
            "request_type": request.__class__.__name__,
            "response_type": "CreateWarRoomResponse"
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

    def list_war_rooms(self, request):
        r"""查询租户区WarRoom信息列表

        查询租户区WarRoom信息列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListWarRooms
        :type request: :class:`huaweicloudsdkcoc.v1.ListWarRoomsRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.ListWarRoomsResponse`
        """
        http_info = self._list_war_rooms_http_info(request)
        return self._call_api(**http_info)

    def list_war_rooms_invoker(self, request):
        http_info = self._list_war_rooms_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_war_rooms_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/external/warrooms/list",
            "request_type": request.__class__.__name__,
            "response_type": "ListWarRoomsResponse"
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

    def batch_create_application_view(self, request):
        r"""批量创建应用，分组，组件

        批量创建应用，分组，组件。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchCreateApplicationView
        :type request: :class:`huaweicloudsdkcoc.v1.BatchCreateApplicationViewRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.BatchCreateApplicationViewResponse`
        """
        http_info = self._batch_create_application_view_http_info(request)
        return self._call_api(**http_info)

    def batch_create_application_view_invoker(self, request):
        http_info = self._batch_create_application_view_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_create_application_view_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/application-view/batch-create",
            "request_type": request.__class__.__name__,
            "response_type": "BatchCreateApplicationViewResponse"
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

    def list_instance_compliant(self, request):
        r"""获取节点合规性报告

        分页获取节点合规性报告
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListInstanceCompliant
        :type request: :class:`huaweicloudsdkcoc.v1.ListInstanceCompliantRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.ListInstanceCompliantResponse`
        """
        http_info = self._list_instance_compliant_http_info(request)
        return self._call_api(**http_info)

    def list_instance_compliant_invoker(self, request):
        http_info = self._list_instance_compliant_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_instance_compliant_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/patch/instance/compliant",
            "request_type": request.__class__.__name__,
            "response_type": "ListInstanceCompliantResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'instance_id' in local_var_params:
            query_params.append(('instance_id', local_var_params['instance_id']))
        if 'ip' in local_var_params:
            query_params.append(('ip', local_var_params['ip']))
        if 'eip' in local_var_params:
            query_params.append(('eip', local_var_params['eip']))
        if 'operating_system' in local_var_params:
            query_params.append(('operating_system', local_var_params['operating_system']))
        if 'region' in local_var_params:
            query_params.append(('region', local_var_params['region']))
        if 'group' in local_var_params:
            query_params.append(('group', local_var_params['group']))
        if 'compliant_status' in local_var_params:
            query_params.append(('compliant_status', local_var_params['compliant_status']))
        if 'order_id' in local_var_params:
            query_params.append(('order_id', local_var_params['order_id']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
        if 'report_scene' in local_var_params:
            query_params.append(('report_scene', local_var_params['report_scene']))
        if 'cce_info_id' in local_var_params:
            query_params.append(('cce_info_id', local_var_params['cce_info_id']))

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

    def show_instance_patch_items(self, request):
        r"""分页获取节点补丁详情

        分页获取节点补丁详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowInstancePatchItems
        :type request: :class:`huaweicloudsdkcoc.v1.ShowInstancePatchItemsRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.ShowInstancePatchItemsResponse`
        """
        http_info = self._show_instance_patch_items_http_info(request)
        return self._call_api(**http_info)

    def show_instance_patch_items_invoker(self, request):
        http_info = self._show_instance_patch_items_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_instance_patch_items_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/patch/instance/compliant/{instance_compliant_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowInstancePatchItemsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_compliant_id' in local_var_params:
            path_params['instance_compliant_id'] = local_var_params['instance_compliant_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'title' in local_var_params:
            query_params.append(('title', local_var_params['title']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
        if 'patch_status' in local_var_params:
            query_params.append(('patch_status', local_var_params['patch_status']))
        if 'classification' in local_var_params:
            query_params.append(('classification', local_var_params['classification']))
        if 'severity_level' in local_var_params:
            query_params.append(('severity_level', local_var_params['severity_level']))
        if 'compliance_level' in local_var_params:
            query_params.append(('compliance_level', local_var_params['compliance_level']))

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

    def count_multi_cloud_resources(self, request):
        r"""查询用户在云厂商的资源总数

        查询用户在云厂商（阿里云、AWS、Azure和HCS）的资源总数。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CountMultiCloudResources
        :type request: :class:`huaweicloudsdkcoc.v1.CountMultiCloudResourcesRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.CountMultiCloudResourcesResponse`
        """
        http_info = self._count_multi_cloud_resources_http_info(request)
        return self._call_api(**http_info)

    def count_multi_cloud_resources_invoker(self, request):
        http_info = self._count_multi_cloud_resources_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _count_multi_cloud_resources_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/multicloud-resources/count",
            "request_type": request.__class__.__name__,
            "response_type": "CountMultiCloudResourcesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'vendor' in local_var_params:
            query_params.append(('vendor', local_var_params['vendor']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'resource_id_list' in local_var_params:
            query_params.append(('resource_id_list', local_var_params['resource_id_list']))
            collection_formats['resource_id_list'] = 'csv'
        if 'name_list' in local_var_params:
            query_params.append(('name_list', local_var_params['name_list']))
            collection_formats['name_list'] = 'csv'
        if 'region_id_list' in local_var_params:
            query_params.append(('region_id_list', local_var_params['region_id_list']))
            collection_formats['region_id_list'] = 'csv'

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

    def sync_multi_cloud_resource(self, request):
        r"""手动从云厂商同步用户资源

        手动从云厂商同步用户资源。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SyncMultiCloudResource
        :type request: :class:`huaweicloudsdkcoc.v1.SyncMultiCloudResourceRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.SyncMultiCloudResourceResponse`
        """
        http_info = self._sync_multi_cloud_resource_http_info(request)
        return self._call_api(**http_info)

    def sync_multi_cloud_resource_invoker(self, request):
        http_info = self._sync_multi_cloud_resource_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _sync_multi_cloud_resource_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/multicloud-resources/sync",
            "request_type": request.__class__.__name__,
            "response_type": "SyncMultiCloudResourceResponse"
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

    def count_multi_resources(self, request):
        r"""查询用户各种资源总数

        查询用户各种资源总数
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CountMultiResources
        :type request: :class:`huaweicloudsdkcoc.v1.CountMultiResourcesRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.CountMultiResourcesResponse`
        """
        http_info = self._count_multi_resources_http_info(request)
        return self._call_api(**http_info)

    def count_multi_resources_invoker(self, request):
        http_info = self._count_multi_resources_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _count_multi_resources_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/resources/multi-count",
            "request_type": request.__class__.__name__,
            "response_type": "CountMultiResourcesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'vendor' in local_var_params:
            query_params.append(('vendor', local_var_params['vendor']))
        if 'view_id' in local_var_params:
            query_params.append(('view_id', local_var_params['view_id']))
        if 'is_resource' in local_var_params:
            query_params.append(('is_resource', local_var_params['is_resource']))
        if 'region_id' in local_var_params:
            query_params.append(('region_id', local_var_params['region_id']))

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

    def list_resources(self, request):
        r"""查询用户所有资源

        查询租户所有资源：
         - 查询租户所有资源等相关信息，便于租户详细了解资源总体情况。
         - 请求参数provider（云服务名称），type（云资源类型），limit（查询条数）必填，单次最大查询条数：500。
         - 返回信息包括：资源ID，资源名称，云服务名称，资源类型，项目ID，租户ID，区域ID，企业项目ID，资源标签，资源详细属性，资源ingest属性，uniagentID，uniagent状态，是否托管，是否可运维。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListResources
        :type request: :class:`huaweicloudsdkcoc.v1.ListResourcesRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.ListResourcesResponse`
        """
        http_info = self._list_resources_http_info(request)
        return self._call_api(**http_info)

    def list_resources_invoker(self, request):
        http_info = self._list_resources_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_resources_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/resources",
            "request_type": request.__class__.__name__,
            "response_type": "ListResourcesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'provider' in local_var_params:
            query_params.append(('provider', local_var_params['provider']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'resource_id_list' in local_var_params:
            query_params.append(('resource_id_list', local_var_params['resource_id_list']))
            collection_formats['resource_id_list'] = 'csv'
        if 'ip_list' in local_var_params:
            query_params.append(('ip_list', local_var_params['ip_list']))
            collection_formats['ip_list'] = 'csv'
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'region_id' in local_var_params:
            query_params.append(('region_id', local_var_params['region_id']))
        if 'az_id' in local_var_params:
            query_params.append(('az_id', local_var_params['az_id']))
        if 'ip_type' in local_var_params:
            query_params.append(('ip_type', local_var_params['ip_type']))
        if 'ip' in local_var_params:
            query_params.append(('ip', local_var_params['ip']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'agent_state' in local_var_params:
            query_params.append(('agent_state', local_var_params['agent_state']))
        if 'image_name' in local_var_params:
            query_params.append(('image_name', local_var_params['image_name']))
        if 'os_type' in local_var_params:
            query_params.append(('os_type', local_var_params['os_type']))
        if 'tag' in local_var_params:
            query_params.append(('tag', local_var_params['tag']))
        if 'tag_key' in local_var_params:
            query_params.append(('tag_key', local_var_params['tag_key']))
        if 'group_id' in local_var_params:
            query_params.append(('group_id', local_var_params['group_id']))
        if 'component_id' in local_var_params:
            query_params.append(('component_id', local_var_params['component_id']))
        if 'application_id' in local_var_params:
            query_params.append(('application_id', local_var_params['application_id']))
        if 'cce_cluster_id' in local_var_params:
            query_params.append(('cce_cluster_id', local_var_params['cce_cluster_id']))
        if 'vpc_id' in local_var_params:
            query_params.append(('vpc_id', local_var_params['vpc_id']))
        if 'ep_id' in local_var_params:
            query_params.append(('ep_id', local_var_params['ep_id']))
        if 'is_delegated' in local_var_params:
            query_params.append(('is_delegated', local_var_params['is_delegated']))
        if 'is_collected' in local_var_params:
            query_params.append(('is_collected', local_var_params['is_collected']))
        if 'flavor_name' in local_var_params:
            query_params.append(('flavor_name', local_var_params['flavor_name']))
        if 'charging_mode' in local_var_params:
            query_params.append(('charging_mode', local_var_params['charging_mode']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'order_field' in local_var_params:
            query_params.append(('order_field', local_var_params['order_field']))
        if 'direction' in local_var_params:
            query_params.append(('direction', local_var_params['direction']))
        if 'show_associated_groups' in local_var_params:
            query_params.append(('show_associated_groups', local_var_params['show_associated_groups']))
        if 'operable' in local_var_params:
            query_params.append(('operable', local_var_params['operable']))
        if 'create_since' in local_var_params:
            query_params.append(('create_since', local_var_params['create_since']))
        if 'create_until' in local_var_params:
            query_params.append(('create_until', local_var_params['create_until']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def sync_resource(self, request):
        r"""从RMS同步用户所有资源

        从RMS同步用户所有资源
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SyncResource
        :type request: :class:`huaweicloudsdkcoc.v1.SyncResourceRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.SyncResourceResponse`
        """
        http_info = self._sync_resource_http_info(request)
        return self._call_api(**http_info)

    def sync_resource_invoker(self, request):
        http_info = self._sync_resource_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _sync_resource_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/resources/sync",
            "request_type": request.__class__.__name__,
            "response_type": "SyncResourceResponse"
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

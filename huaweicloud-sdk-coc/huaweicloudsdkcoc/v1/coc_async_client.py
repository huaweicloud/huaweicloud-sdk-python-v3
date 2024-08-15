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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkcoc'")


class CocAsyncClient(Client):
    def __init__(self):
        super(CocAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkcoc.v1.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "CocAsyncClient":
                raise TypeError("client type error, support client type is CocAsyncClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def create_report_custom_event_async(self, request):
        """支持用户自主接入告警数据

        支持租户将自开发的监控系统按照标准化集成至COC，集成后告警会按照标准格式上报至COC告警中心
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateReportCustomEvent
        :type request: :class:`huaweicloudsdkcoc.v1.CreateReportCustomEventRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.CreateReportCustomEventResponse`
        """
        http_info = self._create_report_custom_event_http_info(request)
        return self._call_api(**http_info)

    def create_report_custom_event_async_invoker(self, request):
        http_info = self._create_report_custom_event_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_report_custom_event_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/event/huawei/custom/{integration_key}",
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

    def create_report_prometheus_event_async(self, request):
        """Prometheus事件接入

        Prometheus事件接入
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateReportPrometheusEvent
        :type request: :class:`huaweicloudsdkcoc.v1.CreateReportPrometheusEventRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.CreateReportPrometheusEventResponse`
        """
        http_info = self._create_report_prometheus_event_http_info(request)
        return self._call_api(**http_info)

    def create_report_prometheus_event_async_invoker(self, request):
        http_info = self._create_report_prometheus_event_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_report_prometheus_event_http_info(self, request):
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

    def create_coc_incident_async(self, request):
        """CreateExternalIncident 创建事件单

        CreateExternalIncident 创建事件单
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateCocIncident
        :type request: :class:`huaweicloudsdkcoc.v1.CreateCocIncidentRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.CreateCocIncidentResponse`
        """
        http_info = self._create_coc_incident_http_info(request)
        return self._call_api(**http_info)

    def create_coc_incident_async_invoker(self, request):
        http_info = self._create_coc_incident_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_coc_incident_http_info(self, request):
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

    def handle_coc_incident_async(self, request):
        """HandleCocIncident处理事件单

        HandleCocIncident 处理事件单
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for HandleCocIncident
        :type request: :class:`huaweicloudsdkcoc.v1.HandleCocIncidentRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.HandleCocIncidentResponse`
        """
        http_info = self._handle_coc_incident_http_info(request)
        return self._call_api(**http_info)

    def handle_coc_incident_async_invoker(self, request):
        http_info = self._handle_coc_incident_http_info(request)
        return AsyncInvoker(self, http_info)

    def _handle_coc_incident_http_info(self, request):
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

    def list_coc_ticket_operation_histories_async(self, request):
        """GetCocTicketOperationHistories 获取事件单历史

        ListCocTicketOperationHistories  获取事件单历史
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListCocTicketOperationHistories
        :type request: :class:`huaweicloudsdkcoc.v1.ListCocTicketOperationHistoriesRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.ListCocTicketOperationHistoriesResponse`
        """
        http_info = self._list_coc_ticket_operation_histories_http_info(request)
        return self._call_api(**http_info)

    def list_coc_ticket_operation_histories_async_invoker(self, request):
        http_info = self._list_coc_ticket_operation_histories_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_coc_ticket_operation_histories_http_info(self, request):
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

    def show_coc_incident_detail_async(self, request):
        """GetCocIncidentDetail 获取事件单详细

        ShowCocIncidentDetail  获取事件单详细
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowCocIncidentDetail
        :type request: :class:`huaweicloudsdkcoc.v1.ShowCocIncidentDetailRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.ShowCocIncidentDetailResponse`
        """
        http_info = self._show_coc_incident_detail_http_info(request)
        return self._call_api(**http_info)

    def show_coc_incident_detail_async_invoker(self, request):
        http_info = self._show_coc_incident_detail_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_coc_incident_detail_http_info(self, request):
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

    def create_coc_issues_async(self, request):
        """CreateExternalIssues 创建问题单

        CreateExternalIssues 创建问题单
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateCocIssues
        :type request: :class:`huaweicloudsdkcoc.v1.CreateCocIssuesRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.CreateCocIssuesResponse`
        """
        http_info = self._create_coc_issues_http_info(request)
        return self._call_api(**http_info)

    def create_coc_issues_async_invoker(self, request):
        http_info = self._create_coc_issues_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_coc_issues_http_info(self, request):
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

    def show_coc_issues_detail_async(self, request):
        """GetCocIssuesDetail 获取事件单详细

        ShowCocIssuesDetail  获取事件单详细
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowCocIssuesDetail
        :type request: :class:`huaweicloudsdkcoc.v1.ShowCocIssuesDetailRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.ShowCocIssuesDetailResponse`
        """
        http_info = self._show_coc_issues_detail_http_info(request)
        return self._call_api(**http_info)

    def show_coc_issues_detail_async_invoker(self, request):
        http_info = self._show_coc_issues_detail_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_coc_issues_detail_http_info(self, request):
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

    def list_authorizable_tickets_external_async(self, request):
        """查询COC可授权单列表

        查询COC可授权单列表（变更单号、事件单号、warroom和告警）
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAuthorizableTicketsExternal
        :type request: :class:`huaweicloudsdkcoc.v1.ListAuthorizableTicketsExternalRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.ListAuthorizableTicketsExternalResponse`
        """
        http_info = self._list_authorizable_tickets_external_http_info(request)
        return self._call_api(**http_info)

    def list_authorizable_tickets_external_async_invoker(self, request):
        http_info = self._list_authorizable_tickets_external_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_authorizable_tickets_external_http_info(self, request):
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

    def get_script_job_batch_async(self, request):
        """展示批次详情

        查询：批次详情，分页获取批次中的实例列表。
        过滤条件：分页参数
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for GetScriptJobBatch
        :type request: :class:`huaweicloudsdkcoc.v1.GetScriptJobBatchRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.GetScriptJobBatchResponse`
        """
        http_info = self._get_script_job_batch_http_info(request)
        return self._call_api(**http_info)

    def get_script_job_batch_async_invoker(self, request):
        http_info = self._get_script_job_batch_http_info(request)
        return AsyncInvoker(self, http_info)

    def _get_script_job_batch_http_info(self, request):
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

    def get_script_job_info_async(self, request):
        """展示脚本工单基本信息

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

    def get_script_job_info_async_invoker(self, request):
        http_info = self._get_script_job_info_http_info(request)
        return AsyncInvoker(self, http_info)

    def _get_script_job_info_http_info(self, request):
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

    def get_script_job_statistics_async(self, request):
        """展示实例状态统计信息

        查询：实例状态统计信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for GetScriptJobStatistics
        :type request: :class:`huaweicloudsdkcoc.v1.GetScriptJobStatisticsRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.GetScriptJobStatisticsResponse`
        """
        http_info = self._get_script_job_statistics_http_info(request)
        return self._call_api(**http_info)

    def get_script_job_statistics_async_invoker(self, request):
        http_info = self._get_script_job_statistics_http_info(request)
        return AsyncInvoker(self, http_info)

    def _get_script_job_statistics_http_info(self, request):
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

    def list_script_job_batches_async(self, request):
        """展示批次列表

        查询：批次列表
        返回：批次index、批次标签
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListScriptJobBatches
        :type request: :class:`huaweicloudsdkcoc.v1.ListScriptJobBatchesRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.ListScriptJobBatchesResponse`
        """
        http_info = self._list_script_job_batches_http_info(request)
        return self._call_api(**http_info)

    def list_script_job_batches_async_invoker(self, request):
        http_info = self._list_script_job_batches_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_script_job_batches_http_info(self, request):
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

    def list_script_jobs_async(self, request):
        """展示工单列表

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

    def list_script_jobs_async_invoker(self, request):
        http_info = self._list_script_jobs_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_script_jobs_http_info(self, request):
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

    def operate_script_job_async(self, request):
        """操作脚本工单

        操作类型：取消实例、跳过批次、取消整个工单、暂停整个工单、继续整个工单
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for OperateScriptJob
        :type request: :class:`huaweicloudsdkcoc.v1.OperateScriptJobRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.OperateScriptJobResponse`
        """
        http_info = self._operate_script_job_http_info(request)
        return self._call_api(**http_info)

    def operate_script_job_async_invoker(self, request):
        http_info = self._operate_script_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _operate_script_job_http_info(self, request):
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

    def create_script_async(self, request):
        """创建脚本

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

    def create_script_async_invoker(self, request):
        http_info = self._create_script_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_script_http_info(self, request):
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

    def delete_script_async(self, request):
        """删除自定义脚本

        删除作业脚本：自定义脚本。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteScript
        :type request: :class:`huaweicloudsdkcoc.v1.DeleteScriptRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.DeleteScriptResponse`
        """
        http_info = self._delete_script_http_info(request)
        return self._call_api(**http_info)

    def delete_script_async_invoker(self, request):
        http_info = self._delete_script_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_script_http_info(self, request):
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

    def execute_script_async(self, request):
        """执行自定义脚本

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

    def execute_script_async_invoker(self, request):
        http_info = self._execute_script_http_info(request)
        return AsyncInvoker(self, http_info)

    def _execute_script_http_info(self, request):
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

    def get_script_async(self, request):
        """获取自定义脚本详情

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

    def get_script_async_invoker(self, request):
        http_info = self._get_script_http_info(request)
        return AsyncInvoker(self, http_info)

    def _get_script_http_info(self, request):
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

    def list_scripts_async(self, request):
        """查询脚本列表

        作业脚本列表：自定义脚本
        
        limit最大为100
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListScripts
        :type request: :class:`huaweicloudsdkcoc.v1.ListScriptsRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.ListScriptsResponse`
        """
        http_info = self._list_scripts_http_info(request)
        return self._call_api(**http_info)

    def list_scripts_async_invoker(self, request):
        http_info = self._list_scripts_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_scripts_http_info(self, request):
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

    def update_script_async(self, request):
        """修改脚本

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

    def update_script_async_invoker(self, request):
        http_info = self._update_script_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_script_http_info(self, request):
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

    def execute_public_script_async(self, request):
        """执行公共脚本

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

    def execute_public_script_async_invoker(self, request):
        http_info = self._execute_public_script_http_info(request)
        return AsyncInvoker(self, http_info)

    def _execute_public_script_http_info(self, request):
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

    def get_public_script_async(self, request):
        """展示公共脚本详情

        展示公共脚本详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for GetPublicScript
        :type request: :class:`huaweicloudsdkcoc.v1.GetPublicScriptRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.GetPublicScriptResponse`
        """
        http_info = self._get_public_script_http_info(request)
        return self._call_api(**http_info)

    def get_public_script_async_invoker(self, request):
        http_info = self._get_public_script_http_info(request)
        return AsyncInvoker(self, http_info)

    def _get_public_script_http_info(self, request):
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

    def list_public_scripts_async(self, request):
        """获取公共脚本列表

        获取公共脚本列表，分页逻辑：采用limit+marker方式，提高分页效率。用自增id作为marker参数
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListPublicScripts
        :type request: :class:`huaweicloudsdkcoc.v1.ListPublicScriptsRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.ListPublicScriptsResponse`
        """
        http_info = self._list_public_scripts_http_info(request)
        return self._call_api(**http_info)

    def list_public_scripts_async_invoker(self, request):
        http_info = self._list_public_scripts_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_public_scripts_http_info(self, request):
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

    def create_war_room_async(self, request):
        """创建租户区WarRoom

        创建租户区WarRoom
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateWarRoom
        :type request: :class:`huaweicloudsdkcoc.v1.CreateWarRoomRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.CreateWarRoomResponse`
        """
        http_info = self._create_war_room_http_info(request)
        return self._call_api(**http_info)

    def create_war_room_async_invoker(self, request):
        http_info = self._create_war_room_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_war_room_http_info(self, request):
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

    def list_war_rooms_async(self, request):
        """查询租户区WarRoom信息列表

        查询租户区WarRoom信息列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListWarRooms
        :type request: :class:`huaweicloudsdkcoc.v1.ListWarRoomsRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.ListWarRoomsResponse`
        """
        http_info = self._list_war_rooms_http_info(request)
        return self._call_api(**http_info)

    def list_war_rooms_async_invoker(self, request):
        http_info = self._list_war_rooms_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_war_rooms_http_info(self, request):
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

    def list_applications_async(self, request):
        """查询应用

        查询应用
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListApplications
        :type request: :class:`huaweicloudsdkcoc.v1.ListApplicationsRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.ListApplicationsResponse`
        """
        http_info = self._list_applications_http_info(request)
        return self._call_api(**http_info)

    def list_applications_async_invoker(self, request):
        http_info = self._list_applications_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_applications_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/applications",
            "request_type": request.__class__.__name__,
            "response_type": "ListApplicationsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'id_list' in local_var_params:
            query_params.append(('id_list', local_var_params['id_list']))
            collection_formats['id_list'] = 'csv'
        if 'parent_id' in local_var_params:
            query_params.append(('parent_id', local_var_params['parent_id']))
        if 'name_like' in local_var_params:
            query_params.append(('name_like', local_var_params['name_like']))
        if 'code' in local_var_params:
            query_params.append(('code', local_var_params['code']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
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

    def list_instance_compliant_async(self, request):
        """获取节点合规性报告

        分页获取节点合规性报告
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListInstanceCompliant
        :type request: :class:`huaweicloudsdkcoc.v1.ListInstanceCompliantRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.ListInstanceCompliantResponse`
        """
        http_info = self._list_instance_compliant_http_info(request)
        return self._call_api(**http_info)

    def list_instance_compliant_async_invoker(self, request):
        http_info = self._list_instance_compliant_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_instance_compliant_http_info(self, request):
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

    def show_instance_patch_items_async(self, request):
        """分页获取节点补丁详情

        分页获取节点补丁详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowInstancePatchItems
        :type request: :class:`huaweicloudsdkcoc.v1.ShowInstancePatchItemsRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.ShowInstancePatchItemsResponse`
        """
        http_info = self._show_instance_patch_items_http_info(request)
        return self._call_api(**http_info)

    def show_instance_patch_items_async_invoker(self, request):
        http_info = self._show_instance_patch_items_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_instance_patch_items_http_info(self, request):
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

    def list_resource_async(self, request):
        """查询用户所有资源

        查询用户所有资源
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListResource
        :type request: :class:`huaweicloudsdkcoc.v1.ListResourceRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.ListResourceResponse`
        """
        http_info = self._list_resource_http_info(request)
        return self._call_api(**http_info)

    def list_resource_async_invoker(self, request):
        http_info = self._list_resource_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_resource_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/resources",
            "request_type": request.__class__.__name__,
            "response_type": "ListResourceResponse"
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

    def sync_resource_async(self, request):
        """从RMS同步用户所有资源

        从RMS同步用户所有资源
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for SyncResource
        :type request: :class:`huaweicloudsdkcoc.v1.SyncResourceRequest`
        :rtype: :class:`huaweicloudsdkcoc.v1.SyncResourceResponse`
        """
        http_info = self._sync_resource_http_info(request)
        return self._call_api(**http_info)

    def sync_resource_async_invoker(self, request):
        http_info = self._sync_resource_http_info(request)
        return AsyncInvoker(self, http_info)

    def _sync_resource_http_info(self, request):
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

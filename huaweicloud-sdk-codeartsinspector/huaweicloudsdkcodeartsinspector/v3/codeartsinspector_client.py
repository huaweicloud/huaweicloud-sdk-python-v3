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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkcodeartsinspector'")


class CodeArtsInspectorClient(Client):
    def __init__(self):
        super(CodeArtsInspectorClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkcodeartsinspector.v3.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "CodeArtsInspectorClient":
                raise TypeError("client type error, support client type is CodeArtsInspectorClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def download_task_report(self, request):
        """下载网站扫描报告

        下载网站扫描任务PDF报告
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DownloadTaskReport
        :type request: :class:`huaweicloudsdkcodeartsinspector.v3.DownloadTaskReportRequest`
        :rtype: :class:`huaweicloudsdkcodeartsinspector.v3.DownloadTaskReportResponse`
        """
        http_info = self._download_task_report_http_info(request)
        return self._call_api(**http_info)

    def download_task_report_invoker(self, request):
        http_info = self._download_task_report_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _download_task_report_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/webscan/report",
            "request_type": request.__class__.__name__,
            "response_type": "DownloadTaskReportResponse"
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

    def execute_generate_report(self, request):
        """生成网站扫描报告

        生成网站扫描PDF报告
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ExecuteGenerateReport
        :type request: :class:`huaweicloudsdkcodeartsinspector.v3.ExecuteGenerateReportRequest`
        :rtype: :class:`huaweicloudsdkcodeartsinspector.v3.ExecuteGenerateReportResponse`
        """
        http_info = self._execute_generate_report_http_info(request)
        return self._call_api(**http_info)

    def execute_generate_report_invoker(self, request):
        http_info = self._execute_generate_report_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _execute_generate_report_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/webscan/report",
            "request_type": request.__class__.__name__,
            "response_type": "ExecuteGenerateReportResponse"
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
            ['application/json; charset=UTF-8'])

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

    def list_business_risks(self, request):
        """获取网站业务风险扫描结果

        获取网站业务风险扫描结果
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListBusinessRisks
        :type request: :class:`huaweicloudsdkcodeartsinspector.v3.ListBusinessRisksRequest`
        :rtype: :class:`huaweicloudsdkcodeartsinspector.v3.ListBusinessRisksResponse`
        """
        http_info = self._list_business_risks_http_info(request)
        return self._call_api(**http_info)

    def list_business_risks_invoker(self, request):
        http_info = self._list_business_risks_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_business_risks_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/webscan/results/business-risk",
            "request_type": request.__class__.__name__,
            "response_type": "ListBusinessRisksResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'task_id' in local_var_params:
            query_params.append(('task_id', local_var_params['task_id']))
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

    def list_port_results(self, request):
        """获取网站端口扫描结果

        获取网站端口扫描结果
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListPortResults
        :type request: :class:`huaweicloudsdkcodeartsinspector.v3.ListPortResultsRequest`
        :rtype: :class:`huaweicloudsdkcodeartsinspector.v3.ListPortResultsResponse`
        """
        http_info = self._list_port_results_http_info(request)
        return self._call_api(**http_info)

    def list_port_results_invoker(self, request):
        http_info = self._list_port_results_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_port_results_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/webscan/results/ports",
            "request_type": request.__class__.__name__,
            "response_type": "ListPortResultsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'task_id' in local_var_params:
            query_params.append(('task_id', local_var_params['task_id']))
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

    def show_report_status(self, request):
        """获取网站扫描报告状态

        获取网站扫描PDF报告生成状态
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowReportStatus
        :type request: :class:`huaweicloudsdkcodeartsinspector.v3.ShowReportStatusRequest`
        :rtype: :class:`huaweicloudsdkcodeartsinspector.v3.ShowReportStatusResponse`
        """
        http_info = self._show_report_status_http_info(request)
        return self._call_api(**http_info)

    def show_report_status_invoker(self, request):
        http_info = self._show_report_status_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_report_status_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/webscan/report/status",
            "request_type": request.__class__.__name__,
            "response_type": "ShowReportStatusResponse"
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

    def show_results(self, request):
        """获取网站扫描结果

        获取网站漏洞扫描结果
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowResults
        :type request: :class:`huaweicloudsdkcodeartsinspector.v3.ShowResultsRequest`
        :rtype: :class:`huaweicloudsdkcodeartsinspector.v3.ShowResultsResponse`
        """
        http_info = self._show_results_http_info(request)
        return self._call_api(**http_info)

    def show_results_invoker(self, request):
        http_info = self._show_results_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_results_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/webscan/results",
            "request_type": request.__class__.__name__,
            "response_type": "ShowResultsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'task_id' in local_var_params:
            query_params.append(('task_id', local_var_params['task_id']))
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

    def update_false_positive(self, request):
        """更新网站漏洞的误报状态

        更新网站扫描漏洞的误报状态
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateFalsePositive
        :type request: :class:`huaweicloudsdkcodeartsinspector.v3.UpdateFalsePositiveRequest`
        :rtype: :class:`huaweicloudsdkcodeartsinspector.v3.UpdateFalsePositiveResponse`
        """
        http_info = self._update_false_positive_http_info(request)
        return self._call_api(**http_info)

    def update_false_positive_invoker(self, request):
        http_info = self._update_false_positive_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_false_positive_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/webscan/vulnerability/false-positive",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateFalsePositiveResponse"
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
            ['application/json; charset=UTF-8'])

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

    def cancel_tasks(self, request):
        """取消或重启网站扫描任务

        取消或重启网站漏洞扫描任务
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CancelTasks
        :type request: :class:`huaweicloudsdkcodeartsinspector.v3.CancelTasksRequest`
        :rtype: :class:`huaweicloudsdkcodeartsinspector.v3.CancelTasksResponse`
        """
        http_info = self._cancel_tasks_http_info(request)
        return self._call_api(**http_info)

    def cancel_tasks_invoker(self, request):
        http_info = self._cancel_tasks_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _cancel_tasks_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/webscan/tasks",
            "request_type": request.__class__.__name__,
            "response_type": "CancelTasksResponse"
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
            ['application/json; charset=UTF-8'])

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

    def create_tasks(self, request):
        """创建网站扫描任务并启动

        创建网站漏洞扫描任务并启动
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateTasks
        :type request: :class:`huaweicloudsdkcodeartsinspector.v3.CreateTasksRequest`
        :rtype: :class:`huaweicloudsdkcodeartsinspector.v3.CreateTasksResponse`
        """
        http_info = self._create_tasks_http_info(request)
        return self._call_api(**http_info)

    def create_tasks_invoker(self, request):
        http_info = self._create_tasks_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_tasks_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/webscan/tasks",
            "request_type": request.__class__.__name__,
            "response_type": "CreateTasksResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'upgrade' in local_var_params:
            query_params.append(('upgrade', local_var_params['upgrade']))

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json; charset=UTF-8'])

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

    def list_task_histories(self, request):
        """获取网站的历史扫描任务

        获取网站漏洞扫描的历史扫描任务
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListTaskHistories
        :type request: :class:`huaweicloudsdkcodeartsinspector.v3.ListTaskHistoriesRequest`
        :rtype: :class:`huaweicloudsdkcodeartsinspector.v3.ListTaskHistoriesResponse`
        """
        http_info = self._list_task_histories_http_info(request)
        return self._call_api(**http_info)

    def list_task_histories_invoker(self, request):
        http_info = self._list_task_histories_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_task_histories_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/webscan/tasks/histories",
            "request_type": request.__class__.__name__,
            "response_type": "ListTaskHistoriesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'domain_id' in local_var_params:
            query_params.append(('domain_id', local_var_params['domain_id']))
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

    def show_tasks(self, request):
        """获取网站扫描任务详情

        获取网站漏洞扫描任务详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowTasks
        :type request: :class:`huaweicloudsdkcodeartsinspector.v3.ShowTasksRequest`
        :rtype: :class:`huaweicloudsdkcodeartsinspector.v3.ShowTasksResponse`
        """
        http_info = self._show_tasks_http_info(request)
        return self._call_api(**http_info)

    def show_tasks_invoker(self, request):
        http_info = self._show_tasks_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_tasks_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/webscan/tasks",
            "request_type": request.__class__.__name__,
            "response_type": "ShowTasksResponse"
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

    def authorize_domains(self, request):
        """认证网站资产

        认证租户的网站资产
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AuthorizeDomains
        :type request: :class:`huaweicloudsdkcodeartsinspector.v3.AuthorizeDomainsRequest`
        :rtype: :class:`huaweicloudsdkcodeartsinspector.v3.AuthorizeDomainsResponse`
        """
        http_info = self._authorize_domains_http_info(request)
        return self._call_api(**http_info)

    def authorize_domains_invoker(self, request):
        http_info = self._authorize_domains_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _authorize_domains_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/webscan/domains/authenticate",
            "request_type": request.__class__.__name__,
            "response_type": "AuthorizeDomainsResponse"
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
            ['application/json; charset=UTF-8'])

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

    def create_domains(self, request):
        """创建网站资产

        创建租户的网站资产
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateDomains
        :type request: :class:`huaweicloudsdkcodeartsinspector.v3.CreateDomainsRequest`
        :rtype: :class:`huaweicloudsdkcodeartsinspector.v3.CreateDomainsResponse`
        """
        http_info = self._create_domains_http_info(request)
        return self._call_api(**http_info)

    def create_domains_invoker(self, request):
        http_info = self._create_domains_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_domains_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/webscan/domains",
            "request_type": request.__class__.__name__,
            "response_type": "CreateDomainsResponse"
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
            ['application/json; charset=UTF-8'])

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

    def delete_domains(self, request):
        """删除网站资产

        删除租户的网站资产
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteDomains
        :type request: :class:`huaweicloudsdkcodeartsinspector.v3.DeleteDomainsRequest`
        :rtype: :class:`huaweicloudsdkcodeartsinspector.v3.DeleteDomainsResponse`
        """
        http_info = self._delete_domains_http_info(request)
        return self._call_api(**http_info)

    def delete_domains_invoker(self, request):
        http_info = self._delete_domains_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_domains_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{project_id}/webscan/domains",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteDomainsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'domain_name' in local_var_params:
            query_params.append(('domain_name', local_var_params['domain_name']))

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

    def list_domains(self, request):
        """获取网站资产

        获取租户的所有网站资产
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListDomains
        :type request: :class:`huaweicloudsdkcodeartsinspector.v3.ListDomainsRequest`
        :rtype: :class:`huaweicloudsdkcodeartsinspector.v3.ListDomainsResponse`
        """
        http_info = self._list_domains_http_info(request)
        return self._call_api(**http_info)

    def list_domains_invoker(self, request):
        http_info = self._list_domains_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_domains_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/webscan/domains",
            "request_type": request.__class__.__name__,
            "response_type": "ListDomainsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'domain_id' in local_var_params:
            query_params.append(('domain_id', local_var_params['domain_id']))
        if 'auth_status' in local_var_params:
            query_params.append(('auth_status', local_var_params['auth_status']))
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

    def show_domain_settings(self, request):
        """获取网站配置

        获取网站登录配置
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDomainSettings
        :type request: :class:`huaweicloudsdkcodeartsinspector.v3.ShowDomainSettingsRequest`
        :rtype: :class:`huaweicloudsdkcodeartsinspector.v3.ShowDomainSettingsResponse`
        """
        http_info = self._show_domain_settings_http_info(request)
        return self._call_api(**http_info)

    def show_domain_settings_invoker(self, request):
        http_info = self._show_domain_settings_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_domain_settings_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/webscan/domains/settings",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDomainSettingsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'domain_id' in local_var_params:
            query_params.append(('domain_id', local_var_params['domain_id']))

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

    def update_domain_settings(self, request):
        """更新网站配置

        更新网站登录配置
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateDomainSettings
        :type request: :class:`huaweicloudsdkcodeartsinspector.v3.UpdateDomainSettingsRequest`
        :rtype: :class:`huaweicloudsdkcodeartsinspector.v3.UpdateDomainSettingsResponse`
        """
        http_info = self._update_domain_settings_http_info(request)
        return self._call_api(**http_info)

    def update_domain_settings_invoker(self, request):
        http_info = self._update_domain_settings_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_domain_settings_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/webscan/domains/settings",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateDomainSettingsResponse"
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
            ['application/json; charset=UTF-8'])

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

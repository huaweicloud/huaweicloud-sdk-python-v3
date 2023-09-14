# coding: utf-8

from __future__ import absolute_import

import importlib

from huaweicloudsdkcore.client import Client, ClientBuilder
from huaweicloudsdkcore.utils import http_utils
from huaweicloudsdkcore.sdk_stream_request import SdkStreamRequest


class CodeArtsInspectorClient(Client):
    def __init__(self):
        super(CodeArtsInspectorClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkcodeartsinspector.v3.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if clazz is None:
            return ClientBuilder(cls)

        if clazz.__name__ != "CodeArtsInspectorClient":
            raise TypeError("client type error, support client type is CodeArtsInspectorClient")

        return ClientBuilder(clazz)

    def download_task_report(self, request):
        """下载网站扫描报告

        下载网站扫描任务PDF报告
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DownloadTaskReport
        :type request: :class:`huaweicloudsdkcodeartsinspector.v3.DownloadTaskReportRequest`
        :rtype: :class:`huaweicloudsdkcodeartsinspector.v3.DownloadTaskReportResponse`
        """
        return self._download_task_report_with_http_info(request)

    def _download_task_report_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'task_id' in local_var_params:
            query_params.append(('task_id', local_var_params['task_id']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/webscan/report',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DownloadTaskReportResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def execute_generate_report(self, request):
        """生成网站扫描报告

        生成网站扫描PDF报告
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ExecuteGenerateReport
        :type request: :class:`huaweicloudsdkcodeartsinspector.v3.ExecuteGenerateReportRequest`
        :rtype: :class:`huaweicloudsdkcodeartsinspector.v3.ExecuteGenerateReportResponse`
        """
        return self._execute_generate_report_with_http_info(request)

    def _execute_generate_report_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json; charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/webscan/report',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ExecuteGenerateReportResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_business_risks(self, request):
        """获取网站业务风险扫描结果

        获取网站业务风险扫描结果
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListBusinessRisks
        :type request: :class:`huaweicloudsdkcodeartsinspector.v3.ListBusinessRisksRequest`
        :rtype: :class:`huaweicloudsdkcodeartsinspector.v3.ListBusinessRisksResponse`
        """
        return self._list_business_risks_with_http_info(request)

    def _list_business_risks_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/webscan/results/business-risk',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListBusinessRisksResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_port_results(self, request):
        """获取网站端口扫描结果

        获取网站端口扫描结果
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListPortResults
        :type request: :class:`huaweicloudsdkcodeartsinspector.v3.ListPortResultsRequest`
        :rtype: :class:`huaweicloudsdkcodeartsinspector.v3.ListPortResultsResponse`
        """
        return self._list_port_results_with_http_info(request)

    def _list_port_results_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/webscan/results/ports',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListPortResultsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_report_status(self, request):
        """获取网站扫描报告状态

        获取网站扫描PDF报告生成状态
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowReportStatus
        :type request: :class:`huaweicloudsdkcodeartsinspector.v3.ShowReportStatusRequest`
        :rtype: :class:`huaweicloudsdkcodeartsinspector.v3.ShowReportStatusResponse`
        """
        return self._show_report_status_with_http_info(request)

    def _show_report_status_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'task_id' in local_var_params:
            query_params.append(('task_id', local_var_params['task_id']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/webscan/report/status',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowReportStatusResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_results(self, request):
        """获取网站扫描结果

        获取网站漏洞扫描结果
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowResults
        :type request: :class:`huaweicloudsdkcodeartsinspector.v3.ShowResultsRequest`
        :rtype: :class:`huaweicloudsdkcodeartsinspector.v3.ShowResultsResponse`
        """
        return self._show_results_with_http_info(request)

    def _show_results_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/webscan/results',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowResultsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_false_positive(self, request):
        """更新网站漏洞的误报状态

        更新网站扫描漏洞的误报状态
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateFalsePositive
        :type request: :class:`huaweicloudsdkcodeartsinspector.v3.UpdateFalsePositiveRequest`
        :rtype: :class:`huaweicloudsdkcodeartsinspector.v3.UpdateFalsePositiveResponse`
        """
        return self._update_false_positive_with_http_info(request)

    def _update_false_positive_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json; charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/webscan/vulnerability/false-positive',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateFalsePositiveResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def cancel_tasks(self, request):
        """取消或重启网站扫描任务

        取消或重启网站漏洞扫描任务
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CancelTasks
        :type request: :class:`huaweicloudsdkcodeartsinspector.v3.CancelTasksRequest`
        :rtype: :class:`huaweicloudsdkcodeartsinspector.v3.CancelTasksResponse`
        """
        return self._cancel_tasks_with_http_info(request)

    def _cancel_tasks_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json; charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/webscan/tasks',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CancelTasksResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_tasks(self, request):
        """创建网站扫描任务并启动

        创建网站漏洞扫描任务并启动
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateTasks
        :type request: :class:`huaweicloudsdkcodeartsinspector.v3.CreateTasksRequest`
        :rtype: :class:`huaweicloudsdkcodeartsinspector.v3.CreateTasksResponse`
        """
        return self._create_tasks_with_http_info(request)

    def _create_tasks_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'upgrade' in local_var_params:
            query_params.append(('upgrade', local_var_params['upgrade']))

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json; charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/webscan/tasks',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateTasksResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_task_histories(self, request):
        """获取网站的历史扫描任务

        获取网站漏洞扫描的历史扫描任务
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListTaskHistories
        :type request: :class:`huaweicloudsdkcodeartsinspector.v3.ListTaskHistoriesRequest`
        :rtype: :class:`huaweicloudsdkcodeartsinspector.v3.ListTaskHistoriesResponse`
        """
        return self._list_task_histories_with_http_info(request)

    def _list_task_histories_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/webscan/tasks/histories',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListTaskHistoriesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_tasks(self, request):
        """获取网站扫描任务详情

        获取网站漏洞扫描任务详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowTasks
        :type request: :class:`huaweicloudsdkcodeartsinspector.v3.ShowTasksRequest`
        :rtype: :class:`huaweicloudsdkcodeartsinspector.v3.ShowTasksResponse`
        """
        return self._show_tasks_with_http_info(request)

    def _show_tasks_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'task_id' in local_var_params:
            query_params.append(('task_id', local_var_params['task_id']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/webscan/tasks',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowTasksResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def authorize_domains(self, request):
        """认证网站资产

        认证租户的网站资产
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AuthorizeDomains
        :type request: :class:`huaweicloudsdkcodeartsinspector.v3.AuthorizeDomainsRequest`
        :rtype: :class:`huaweicloudsdkcodeartsinspector.v3.AuthorizeDomainsResponse`
        """
        return self._authorize_domains_with_http_info(request)

    def _authorize_domains_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json; charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/webscan/domains/authenticate',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='AuthorizeDomainsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_domains(self, request):
        """创建网站资产

        创建租户的网站资产
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateDomains
        :type request: :class:`huaweicloudsdkcodeartsinspector.v3.CreateDomainsRequest`
        :rtype: :class:`huaweicloudsdkcodeartsinspector.v3.CreateDomainsResponse`
        """
        return self._create_domains_with_http_info(request)

    def _create_domains_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json; charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/webscan/domains',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateDomainsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_domains(self, request):
        """删除网站资产

        删除租户的网站资产
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteDomains
        :type request: :class:`huaweicloudsdkcodeartsinspector.v3.DeleteDomainsRequest`
        :rtype: :class:`huaweicloudsdkcodeartsinspector.v3.DeleteDomainsResponse`
        """
        return self._delete_domains_with_http_info(request)

    def _delete_domains_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'domain_name' in local_var_params:
            query_params.append(('domain_name', local_var_params['domain_name']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/webscan/domains',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteDomainsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_domains(self, request):
        """获取网站资产

        获取租户的所有网站资产
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListDomains
        :type request: :class:`huaweicloudsdkcodeartsinspector.v3.ListDomainsRequest`
        :rtype: :class:`huaweicloudsdkcodeartsinspector.v3.ListDomainsResponse`
        """
        return self._list_domains_with_http_info(request)

    def _list_domains_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/webscan/domains',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListDomainsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_domain_settings(self, request):
        """获取网站配置

        获取网站登录配置
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDomainSettings
        :type request: :class:`huaweicloudsdkcodeartsinspector.v3.ShowDomainSettingsRequest`
        :rtype: :class:`huaweicloudsdkcodeartsinspector.v3.ShowDomainSettingsResponse`
        """
        return self._show_domain_settings_with_http_info(request)

    def _show_domain_settings_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'domain_id' in local_var_params:
            query_params.append(('domain_id', local_var_params['domain_id']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/webscan/domains/settings',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowDomainSettingsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_domain_settings(self, request):
        """更新网站配置

        更新网站登录配置
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateDomainSettings
        :type request: :class:`huaweicloudsdkcodeartsinspector.v3.UpdateDomainSettingsRequest`
        :rtype: :class:`huaweicloudsdkcodeartsinspector.v3.UpdateDomainSettingsResponse`
        """
        return self._update_domain_settings_with_http_info(request)

    def _update_domain_settings_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json; charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/webscan/domains/settings',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateDomainSettingsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

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

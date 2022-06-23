# coding: utf-8

from __future__ import absolute_import

import datetime
import re
import importlib

import six

from huaweicloudsdkcore.client import Client, ClientBuilder
from huaweicloudsdkcore.exceptions import exceptions
from huaweicloudsdkcore.utils import http_utils
from huaweicloudsdkcore.sdk_stream_request import SdkStreamRequest


class VssClient(Client):
    """
    :param configuration: .Configuration object for this client
    :param pool_threads: The number of threads to use for async requests
        to the API. More threads means more concurrent API requests.
    """

    PRIMITIVE_TYPES = (float, bool, bytes, six.text_type) + six.integer_types
    NATIVE_TYPES_MAPPING = {
        'int': int,
        'long': int if six.PY3 else long,
        'float': float,
        'str': str,
        'bool': bool,
        'date': datetime.date,
        'datetime': datetime.datetime,
        'object': object,
    }

    def __init__(self):
        super(VssClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkvss.v3.model")
        self.preset_headers = {'User-Agent': 'HuaweiCloud-SDK-Python'}

    @classmethod
    def new_builder(cls, clazz=None):
        if clazz is None:
            return ClientBuilder(cls)

        if clazz.__name__ != "VssClient":
            raise TypeError("client type error, support client type is VssClient")

        return ClientBuilder(clazz)

    def authorize_domains(self, request):
        """认证域名资产

        认证租户的域名资产
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for AuthorizeDomains
        :type request: :class:`huaweicloudsdkvss.v3.AuthorizeDomainsRequest`
        :rtype: :class:`huaweicloudsdkvss.v3.AuthorizeDomainsResponse`
        """
        return self.authorize_domains_with_http_info(request)

    def authorize_domains_with_http_info(self, request):
        all_params = ['authorize_domains_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='AuthorizeDomainsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_domains(self, request):
        """创建域名资产

        创建租户的域名资产
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for CreateDomains
        :type request: :class:`huaweicloudsdkvss.v3.CreateDomainsRequest`
        :rtype: :class:`huaweicloudsdkvss.v3.CreateDomainsResponse`
        """
        return self.create_domains_with_http_info(request)

    def create_domains_with_http_info(self, request):
        all_params = ['create_domains_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='CreateDomainsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_domains(self, request):
        """删除域名资产

        删除租户的域名资产
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for DeleteDomains
        :type request: :class:`huaweicloudsdkvss.v3.DeleteDomainsRequest`
        :rtype: :class:`huaweicloudsdkvss.v3.DeleteDomainsResponse`
        """
        return self.delete_domains_with_http_info(request)

    def delete_domains_with_http_info(self, request):
        all_params = ['domain_name']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='DeleteDomainsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_domains(self, request):
        """获取域名资产

        获取租户的所有域名资产
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListDomains
        :type request: :class:`huaweicloudsdkvss.v3.ListDomainsRequest`
        :rtype: :class:`huaweicloudsdkvss.v3.ListDomainsResponse`
        """
        return self.list_domains_with_http_info(request)

    def list_domains_with_http_info(self, request):
        all_params = ['domain_id', 'auth_status', 'offset', 'limit']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='ListDomainsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_domain_settings(self, request):
        """获取域名配置

        获取域名登录配置
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowDomainSettings
        :type request: :class:`huaweicloudsdkvss.v3.ShowDomainSettingsRequest`
        :rtype: :class:`huaweicloudsdkvss.v3.ShowDomainSettingsResponse`
        """
        return self.show_domain_settings_with_http_info(request)

    def show_domain_settings_with_http_info(self, request):
        all_params = ['domain_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='ShowDomainSettingsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_domain_settings(self, request):
        """更新域名配置

        更新域名登录配置
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for UpdateDomainSettings
        :type request: :class:`huaweicloudsdkvss.v3.UpdateDomainSettingsRequest`
        :rtype: :class:`huaweicloudsdkvss.v3.UpdateDomainSettingsResponse`
        """
        return self.update_domain_settings_with_http_info(request)

    def update_domain_settings_with_http_info(self, request):
        all_params = ['update_domain_settings_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='UpdateDomainSettingsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def download_task_report(self, request):
        """下载域名扫描报告

        下载域名扫描任务PDF报告
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for DownloadTaskReport
        :type request: :class:`huaweicloudsdkvss.v3.DownloadTaskReportRequest`
        :rtype: :class:`huaweicloudsdkvss.v3.DownloadTaskReportResponse`
        """
        return self.download_task_report_with_http_info(request)

    def download_task_report_with_http_info(self, request):
        all_params = ['task_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='DownloadTaskReportResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def execute_generate_report(self, request):
        """生成域名扫描报告

        生成域名扫描PDF报告
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ExecuteGenerateReport
        :type request: :class:`huaweicloudsdkvss.v3.ExecuteGenerateReportRequest`
        :rtype: :class:`huaweicloudsdkvss.v3.ExecuteGenerateReportResponse`
        """
        return self.execute_generate_report_with_http_info(request)

    def execute_generate_report_with_http_info(self, request):
        all_params = ['execute_generate_report_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='ExecuteGenerateReportResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_business_risks(self, request):
        """获取业务风险扫描结果

        获取域名业务风险扫描结果
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListBusinessRisks
        :type request: :class:`huaweicloudsdkvss.v3.ListBusinessRisksRequest`
        :rtype: :class:`huaweicloudsdkvss.v3.ListBusinessRisksResponse`
        """
        return self.list_business_risks_with_http_info(request)

    def list_business_risks_with_http_info(self, request):
        all_params = ['task_id', 'offset', 'limit']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='ListBusinessRisksResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_port_results(self, request):
        """获取端口扫描结果

        获取域名端口扫描结果
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListPortResults
        :type request: :class:`huaweicloudsdkvss.v3.ListPortResultsRequest`
        :rtype: :class:`huaweicloudsdkvss.v3.ListPortResultsResponse`
        """
        return self.list_port_results_with_http_info(request)

    def list_port_results_with_http_info(self, request):
        all_params = ['task_id', 'offset', 'limit']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='ListPortResultsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_report_status(self, request):
        """获取域名扫描报告状态

        获取域名扫描PDF报告生成状态
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowReportStatus
        :type request: :class:`huaweicloudsdkvss.v3.ShowReportStatusRequest`
        :rtype: :class:`huaweicloudsdkvss.v3.ShowReportStatusResponse`
        """
        return self.show_report_status_with_http_info(request)

    def show_report_status_with_http_info(self, request):
        all_params = ['task_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='ShowReportStatusResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_results(self, request):
        """获取扫描结果

        获取域名漏洞扫描结果
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowResults
        :type request: :class:`huaweicloudsdkvss.v3.ShowResultsRequest`
        :rtype: :class:`huaweicloudsdkvss.v3.ShowResultsResponse`
        """
        return self.show_results_with_http_info(request)

    def show_results_with_http_info(self, request):
        all_params = ['task_id', 'offset', 'limit']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='ShowResultsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_false_positive(self, request):
        """更新漏洞的误报状态

        更新域名扫描漏洞的误报状态
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for UpdateFalsePositive
        :type request: :class:`huaweicloudsdkvss.v3.UpdateFalsePositiveRequest`
        :rtype: :class:`huaweicloudsdkvss.v3.UpdateFalsePositiveResponse`
        """
        return self.update_false_positive_with_http_info(request)

    def update_false_positive_with_http_info(self, request):
        all_params = ['update_false_positive_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='UpdateFalsePositiveResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def cancel_tasks(self, request):
        """取消或重启扫描任务

        取消或重启域名漏洞扫描任务
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for CancelTasks
        :type request: :class:`huaweicloudsdkvss.v3.CancelTasksRequest`
        :rtype: :class:`huaweicloudsdkvss.v3.CancelTasksResponse`
        """
        return self.cancel_tasks_with_http_info(request)

    def cancel_tasks_with_http_info(self, request):
        all_params = ['cancel_tasks_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='CancelTasksResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_tasks(self, request):
        """创建扫描任务并启动

        创建域名漏洞扫描任务并启动
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for CreateTasks
        :type request: :class:`huaweicloudsdkvss.v3.CreateTasksRequest`
        :rtype: :class:`huaweicloudsdkvss.v3.CreateTasksResponse`
        """
        return self.create_tasks_with_http_info(request)

    def create_tasks_with_http_info(self, request):
        all_params = ['create_tasks_request_body', 'upgrade']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='CreateTasksResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_task_histories(self, request):
        """获取域名的历史扫描任务

        获取域名漏洞扫描的历史扫描任务
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListTaskHistories
        :type request: :class:`huaweicloudsdkvss.v3.ListTaskHistoriesRequest`
        :rtype: :class:`huaweicloudsdkvss.v3.ListTaskHistoriesResponse`
        """
        return self.list_task_histories_with_http_info(request)

    def list_task_histories_with_http_info(self, request):
        all_params = ['domain_id', 'offset', 'limit']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='ListTaskHistoriesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_tasks(self, request):
        """获取扫描任务详情

        获取域名漏洞扫描任务详情
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowTasks
        :type request: :class:`huaweicloudsdkvss.v3.ShowTasksRequest`
        :rtype: :class:`huaweicloudsdkvss.v3.ShowTasksResponse`
        """
        return self.show_tasks_with_http_info(request)

    def show_tasks_with_http_info(self, request):
        all_params = ['task_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='ShowTasksResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def call_api(self, resource_path, method, path_params=None, query_params=None, header_params=None, body=None,
                 post_params=None, response_type=None, response_headers=None, auth_settings=None,
                 collection_formats=None, request_type=None):
        """Makes the HTTP request and returns deserialized data.

        :param resource_path: Path to method endpoint.
        :param method: Method to call.
        :param path_params: Path parameters in the url.
        :param query_params: Query parameters in the url.
        :param header_params: Header parameters to be placed in the request header.
        :param body: Request body.
        :param post_params dict: Request post form parameters,
            for `application/x-www-form-urlencoded`, `multipart/form-data`.
        :param auth_settings list: Auth Settings names for the request.
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
            response_type=response_type,
            response_headers=response_headers,
            collection_formats=collection_formats,
            request_type=request_type)

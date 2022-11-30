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


class AomAsyncClient(Client):
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
        super(AomAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkaom.v1.model")
        self.preset_headers = {'User-Agent': 'HuaweiCloud-SDK-Python'}

    @classmethod
    def new_builder(cls, clazz=None):
        if clazz is None:
            return ClientBuilder(cls)

        if clazz.__name__ != "AomClient":
            raise TypeError("client type error, support client type is AomClient")

        return ClientBuilder(clazz)

    def create_fast_execute_script_async(self, request):
        """快速创建并执行脚本

        该接口用于创建快速执行脚本的任务，可以指定脚本类型，执行用户，脚本参数，执行机器，脚本内容，在用户指定的机器上执行脚本。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateFastExecuteScript
        :type request: :class:`huaweicloudsdkaom.v1.CreateFastExecuteScriptRequest`
        :rtype: :class:`huaweicloudsdkaom.v1.CreateFastExecuteScriptResponse`
        """
        return self.create_fast_execute_script_with_http_info(request)

    def create_fast_execute_script_with_http_info(self, request):
        all_params = ['create_fast_execute_script_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/cms/fast-execute-script',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateFastExecuteScriptResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_workflow_async(self, request):
        """创建任务

        该接口用于创建工作流（任务），返回工作流详情。任务类型取决于模板名称和&#39;input&#39;参数。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateWorkflow
        :type request: :class:`huaweicloudsdkaom.v1.CreateWorkflowRequest`
        :rtype: :class:`huaweicloudsdkaom.v1.CreateWorkflowResponse`
        """
        return self.create_workflow_with_http_info(request)

    def create_workflow_with_http_info(self, request):
        all_params = ['create_workflow_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/cms/workflow',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateWorkflowResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def execute_workflow_async(self, request):
        """执行工作流

        该接口可下发执行指定的任务
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ExecuteWorkflow
        :type request: :class:`huaweicloudsdkaom.v1.ExecuteWorkflowRequest`
        :rtype: :class:`huaweicloudsdkaom.v1.ExecuteWorkflowResponse`
        """
        return self.execute_workflow_with_http_info(request)

    def execute_workflow_with_http_info(self, request):
        all_params = ['workflow_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workflow_id' in local_var_params:
            path_params['workflow_id'] = local_var_params['workflow_id']

        query_params = []

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
            resource_path='/v1/{project_id}/cms/workflow/{workflow_id}/executions',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ExecuteWorkflowResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_all_job_by_name_async(self, request):
        """作业管理主页模糊查询

        该接口可查询已创建的作业，可指定作业名称和作业创建人去精确查询，返回作业列表信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAllJobByName
        :type request: :class:`huaweicloudsdkaom.v1.ListAllJobByNameRequest`
        :rtype: :class:`huaweicloudsdkaom.v1.ListAllJobByNameResponse`
        """
        return self.list_all_job_by_name_with_http_info(request)

    def list_all_job_by_name_with_http_info(self, request):
        all_params = ['list_all_job_by_name_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/cms/job/list',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListAllJobByNameResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_all_script_by_name_async(self, request):
        """脚本主页查询

        该接口是脚本主页查询，可指定脚本名称和脚本创建人进行精确查询，返回包含脚本基本信息的列表数据。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAllScriptByName
        :type request: :class:`huaweicloudsdkaom.v1.ListAllScriptByNameRequest`
        :rtype: :class:`huaweicloudsdkaom.v1.ListAllScriptByNameResponse`
        """
        return self.list_all_script_by_name_with_http_info(request)

    def list_all_script_by_name_with_http_info(self, request):
        all_params = ['list_all_script_by_name_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/cms/script/list',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListAllScriptByNameResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_all_version_by_version_id_async(self, request):
        """脚本管理主页查询，版本管理查询

        该接口可查询指定脚本ID下的所有版本，返回该名称的脚本版本列表信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAllVersionByVersionId
        :type request: :class:`huaweicloudsdkaom.v1.ListAllVersionByVersionIdRequest`
        :rtype: :class:`huaweicloudsdkaom.v1.ListAllVersionByVersionIdResponse`
        """
        return self.list_all_version_by_version_id_with_http_info(request)

    def list_all_version_by_version_id_with_http_info(self, request):
        all_params = ['list_all_version_by_version_id_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/cms/script-version-list',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListAllVersionByVersionIdResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_template_by_job_id_async(self, request):
        """根据作业id查询方案(自定义模板)列表

        该接口可根据作业ID查询执行方案，分页返回执行方案列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListTemplateByJobId
        :type request: :class:`huaweicloudsdkaom.v1.ListTemplateByJobIdRequest`
        :rtype: :class:`huaweicloudsdkaom.v1.ListTemplateByJobIdResponse`
        """
        return self.list_template_by_job_id_with_http_info(request)

    def list_template_by_job_id_with_http_info(self, request):
        all_params = ['job_id', 'list_template_by_job_id_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

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
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/cms/template-list/{job_id}',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListTemplateByJobIdResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_workflow_async(self, request):
        """查询任务列表

        该接口可返回已经创建的任务列表，可按任务名称，任务状态，任务类型，执行人，更新时间为查询条件分页查询任务。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListWorkflow
        :type request: :class:`huaweicloudsdkaom.v1.ListWorkflowRequest`
        :rtype: :class:`huaweicloudsdkaom.v1.ListWorkflowResponse`
        """
        return self.list_workflow_with_http_info(request)

    def list_workflow_with_http_info(self, request):
        all_params = ['list_workflow_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/cms/workflow-list',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListWorkflowResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_workflow_executions_async(self, request):
        """获取任务执行历史

        该接口可获取执行任务的执行历史。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListWorkflowExecutions
        :type request: :class:`huaweicloudsdkaom.v1.ListWorkflowExecutionsRequest`
        :rtype: :class:`huaweicloudsdkaom.v1.ListWorkflowExecutionsResponse`
        """
        return self.list_workflow_executions_with_http_info(request)

    def list_workflow_executions_with_http_info(self, request):
        all_params = ['workflow_id', 'x_enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workflow_id' in local_var_params:
            path_params['workflow_id'] = local_var_params['workflow_id']

        query_params = []
        if 'x_enterprise_project_id' in local_var_params:
            query_params.append(('x_enterprise_project_id', local_var_params['x_enterprise_project_id']))

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
            resource_path='/v1/{project_id}/cms/workflow/{workflow_id}/executions',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListWorkflowExecutionsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def search_template_by_id_async(self, request):
        """获取方案信息

        该接口可根据执行方案id查询执行方案详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for SearchTemplateById
        :type request: :class:`huaweicloudsdkaom.v1.SearchTemplateByIdRequest`
        :rtype: :class:`huaweicloudsdkaom.v1.SearchTemplateByIdResponse`
        """
        return self.search_template_by_id_with_http_info(request)

    def search_template_by_id_with_http_info(self, request):
        all_params = ['template_id', 'share_type']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'template_id' in local_var_params:
            path_params['template_id'] = local_var_params['template_id']

        query_params = []
        if 'share_type' in local_var_params:
            query_params.append(('share_type', local_var_params['share_type']))

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
            resource_path='/v1/{project_id}/cms/template/{template_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='SearchTemplateByIdResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def search_workflow_execution_detail_async(self, request):
        """获取工作流执行中的执行详情

        该接口可获取任务的执行详情，可指定工作流ID和执行ID去查询对应的任务，返回任务执行详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for SearchWorkflowExecutionDetail
        :type request: :class:`huaweicloudsdkaom.v1.SearchWorkflowExecutionDetailRequest`
        :rtype: :class:`huaweicloudsdkaom.v1.SearchWorkflowExecutionDetailResponse`
        """
        return self.search_workflow_execution_detail_with_http_info(request)

    def search_workflow_execution_detail_with_http_info(self, request):
        all_params = ['workflow_id', 'execution_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workflow_id' in local_var_params:
            path_params['workflow_id'] = local_var_params['workflow_id']
        if 'execution_id' in local_var_params:
            path_params['execution_id'] = local_var_params['execution_id']

        query_params = []

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
            resource_path='/v1/{project_id}/cms/workflow/{workflow_id}/executions/{execution_id}/status',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='SearchWorkflowExecutionDetailResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def start_pausing_workflow_executions_async(self, request):
        """对暂停中的任务进行操作

        该接口可对任务进行失败重试、失败跳过、暂停继续操作，返回操作结果。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for StartPausingWorkflowExecutions
        :type request: :class:`huaweicloudsdkaom.v1.StartPausingWorkflowExecutionsRequest`
        :rtype: :class:`huaweicloudsdkaom.v1.StartPausingWorkflowExecutionsResponse`
        """
        return self.start_pausing_workflow_executions_with_http_info(request)

    def start_pausing_workflow_executions_with_http_info(self, request):
        all_params = ['workflow_id', 'execution_id', 'action', 'node_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workflow_id' in local_var_params:
            path_params['workflow_id'] = local_var_params['workflow_id']
        if 'execution_id' in local_var_params:
            path_params['execution_id'] = local_var_params['execution_id']

        query_params = []
        if 'action' in local_var_params:
            query_params.append(('action', local_var_params['action']))
        if 'node_id' in local_var_params:
            query_params.append(('node_id', local_var_params['node_id']))

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
            resource_path='/v1/{project_id}/cms/workflow/{workflow_id}/executions/{execution_id}/operation',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='StartPausingWorkflowExecutionsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def stop_execution_async(self, request):
        """终止任务执行

        该接口可终止正在执行的任务，指定工作流ID和执行ID去终止对应的任务，返回终止操作状态。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for StopExecution
        :type request: :class:`huaweicloudsdkaom.v1.StopExecutionRequest`
        :rtype: :class:`huaweicloudsdkaom.v1.StopExecutionResponse`
        """
        return self.stop_execution_with_http_info(request)

    def stop_execution_with_http_info(self, request):
        all_params = ['workflow_id', 'execution_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workflow_id' in local_var_params:
            path_params['workflow_id'] = local_var_params['workflow_id']
        if 'execution_id' in local_var_params:
            path_params['execution_id'] = local_var_params['execution_id']

        query_params = []

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
            resource_path='/v1/{project_id}/cms/workflow/{workflow_id}/executions/{execution_id}/terminate',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='StopExecutionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_workflow_trigger_status_async(self, request):
        """更新任务

        更新定时任务的启停状态，可启动定时任务或停止定时任务，返回操作任务结果。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateWorkflowTriggerStatus
        :type request: :class:`huaweicloudsdkaom.v1.UpdateWorkflowTriggerStatusRequest`
        :rtype: :class:`huaweicloudsdkaom.v1.UpdateWorkflowTriggerStatusResponse`
        """
        return self.update_workflow_trigger_status_with_http_info(request)

    def update_workflow_trigger_status_with_http_info(self, request):
        all_params = ['workflow_id', 'action']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workflow_id' in local_var_params:
            path_params['workflow_id'] = local_var_params['workflow_id']

        query_params = []
        if 'action' in local_var_params:
            query_params.append(('action', local_var_params['action']))

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
            resource_path='/v1/{project_id}/cms/workflow/{workflow_id}/trigger/action',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateWorkflowTriggerStatusResponse',
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

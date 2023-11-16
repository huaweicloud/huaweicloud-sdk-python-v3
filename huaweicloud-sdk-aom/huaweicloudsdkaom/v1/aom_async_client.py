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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkaom'")


class AomAsyncClient(Client):
    def __init__(self):
        super(AomAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkaom.v1.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "AomAsyncClient":
                raise TypeError("client type error, support client type is AomAsyncClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def create_fast_execute_script_async(self, request):
        """快速创建并执行脚本

        该接口用于创建快速执行脚本的任务，可以指定脚本类型，执行用户，脚本参数，执行机器，脚本内容，在用户指定的机器上执行脚本。（注：接口目前开放的region为：华东-苏州二零一）。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateFastExecuteScript
        :type request: :class:`huaweicloudsdkaom.v1.CreateFastExecuteScriptRequest`
        :rtype: :class:`huaweicloudsdkaom.v1.CreateFastExecuteScriptResponse`
        """
        http_info = self._create_fast_execute_script_http_info(request)
        return self._call_api(**http_info)

    def create_fast_execute_script_async_invoker(self, request):
        http_info = self._create_fast_execute_script_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_fast_execute_script_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/cms/fast-execute-script",
            "request_type": request.__class__.__name__,
            "response_type": "CreateFastExecuteScriptResponse"
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

    def create_workflow_async(self, request):
        """创建任务

        该接口用于创建工作流（任务），返回工作流详情。任务类型取决于模板名称和&#39;input&#39;参数。（注：接口目前开放的region为：华北-北京四,华东-上海一,华东-上海二,华南-广州）。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateWorkflow
        :type request: :class:`huaweicloudsdkaom.v1.CreateWorkflowRequest`
        :rtype: :class:`huaweicloudsdkaom.v1.CreateWorkflowResponse`
        """
        http_info = self._create_workflow_http_info(request)
        return self._call_api(**http_info)

    def create_workflow_async_invoker(self, request):
        http_info = self._create_workflow_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_workflow_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/cms/workflow",
            "request_type": request.__class__.__name__,
            "response_type": "CreateWorkflowResponse"
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

    def execute_workflow_async(self, request):
        """执行工作流

        该接口可下发执行指定的任务。（注：接口目前开放的region为：华北-北京四,华东-上海一,华东-上海二,华南-广州）。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ExecuteWorkflow
        :type request: :class:`huaweicloudsdkaom.v1.ExecuteWorkflowRequest`
        :rtype: :class:`huaweicloudsdkaom.v1.ExecuteWorkflowResponse`
        """
        http_info = self._execute_workflow_http_info(request)
        return self._call_api(**http_info)

    def execute_workflow_async_invoker(self, request):
        http_info = self._execute_workflow_http_info(request)
        return AsyncInvoker(self, http_info)

    def _execute_workflow_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/cms/workflow/{workflow_id}/executions",
            "request_type": request.__class__.__name__,
            "response_type": "ExecuteWorkflowResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workflow_id' in local_var_params:
            path_params['workflow_id'] = local_var_params['workflow_id']

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

    def list_all_job_by_name_async(self, request):
        """作业管理主页模糊查询

        该接口可查询已创建的作业，可指定作业名称和作业创建人去精确查询，返回作业列表信息。（注：接口目前开放的region为：华北-北京四,华东-上海一,华东-上海二,华南-广州）。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAllJobByName
        :type request: :class:`huaweicloudsdkaom.v1.ListAllJobByNameRequest`
        :rtype: :class:`huaweicloudsdkaom.v1.ListAllJobByNameResponse`
        """
        http_info = self._list_all_job_by_name_http_info(request)
        return self._call_api(**http_info)

    def list_all_job_by_name_async_invoker(self, request):
        http_info = self._list_all_job_by_name_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_all_job_by_name_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/cms/job/list",
            "request_type": request.__class__.__name__,
            "response_type": "ListAllJobByNameResponse"
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

    def list_all_script_by_name_async(self, request):
        """脚本查询

        该接口是脚本主页查询，可指定脚本名称和脚本创建人进行精确查询，返回包含脚本基本信息的列表数据。（注：接口目前开放的region为：华北-北京四,华东-上海一,华东-上海二,华南-广州）。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAllScriptByName
        :type request: :class:`huaweicloudsdkaom.v1.ListAllScriptByNameRequest`
        :rtype: :class:`huaweicloudsdkaom.v1.ListAllScriptByNameResponse`
        """
        http_info = self._list_all_script_by_name_http_info(request)
        return self._call_api(**http_info)

    def list_all_script_by_name_async_invoker(self, request):
        http_info = self._list_all_script_by_name_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_all_script_by_name_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/cms/script/list",
            "request_type": request.__class__.__name__,
            "response_type": "ListAllScriptByNameResponse"
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

    def list_all_version_by_version_id_async(self, request):
        """脚本版本查询

        该接口可查询指定脚本ID下的所有版本，返回该名称的脚本版本列表信息。（注：接口目前开放的region为：华北-北京四,华东-上海一,华东-上海二,华南-广州）。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAllVersionByVersionId
        :type request: :class:`huaweicloudsdkaom.v1.ListAllVersionByVersionIdRequest`
        :rtype: :class:`huaweicloudsdkaom.v1.ListAllVersionByVersionIdResponse`
        """
        http_info = self._list_all_version_by_version_id_http_info(request)
        return self._call_api(**http_info)

    def list_all_version_by_version_id_async_invoker(self, request):
        http_info = self._list_all_version_by_version_id_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_all_version_by_version_id_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/cms/script-version-list",
            "request_type": request.__class__.__name__,
            "response_type": "ListAllVersionByVersionIdResponse"
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

    def list_template_by_job_id_async(self, request):
        """根据作业id查询方案(自定义模板)列表

        该接口可根据作业ID查询执行方案，分页返回执行方案列表。（注：接口目前开放的region为：华北-北京四,华东-上海一,华东-上海二,华南-广州）。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListTemplateByJobId
        :type request: :class:`huaweicloudsdkaom.v1.ListTemplateByJobIdRequest`
        :rtype: :class:`huaweicloudsdkaom.v1.ListTemplateByJobIdResponse`
        """
        http_info = self._list_template_by_job_id_http_info(request)
        return self._call_api(**http_info)

    def list_template_by_job_id_async_invoker(self, request):
        http_info = self._list_template_by_job_id_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_template_by_job_id_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/cms/template-list/{job_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ListTemplateByJobIdResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

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

    def list_workflow_async(self, request):
        """查询任务列表

        该接口可返回已经创建的任务列表，可按任务名称，任务状态，任务类型，执行人，更新时间为查询条件分页查询任务。（注：接口目前开放的region为：华北-北京四,华东-上海一,华东-上海二,华南-广州）。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListWorkflow
        :type request: :class:`huaweicloudsdkaom.v1.ListWorkflowRequest`
        :rtype: :class:`huaweicloudsdkaom.v1.ListWorkflowResponse`
        """
        http_info = self._list_workflow_http_info(request)
        return self._call_api(**http_info)

    def list_workflow_async_invoker(self, request):
        http_info = self._list_workflow_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_workflow_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/cms/workflow-list",
            "request_type": request.__class__.__name__,
            "response_type": "ListWorkflowResponse"
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

    def list_workflow_executions_async(self, request):
        """获取任务执行历史

        该接口可获取执行任务的执行历史。（注：接口目前开放的region为：华北-北京四,华东-上海一,华东-上海二,华南-广州）。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListWorkflowExecutions
        :type request: :class:`huaweicloudsdkaom.v1.ListWorkflowExecutionsRequest`
        :rtype: :class:`huaweicloudsdkaom.v1.ListWorkflowExecutionsResponse`
        """
        http_info = self._list_workflow_executions_http_info(request)
        return self._call_api(**http_info)

    def list_workflow_executions_async_invoker(self, request):
        http_info = self._list_workflow_executions_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_workflow_executions_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/cms/workflow/{workflow_id}/executions",
            "request_type": request.__class__.__name__,
            "response_type": "ListWorkflowExecutionsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def search_template_by_id_async(self, request):
        """获取方案信息

        该接口可根据执行方案id查询执行方案详情。（注：接口目前开放的region为：华北-北京四,华东-上海一,华东-上海二,华南-广州）。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for SearchTemplateById
        :type request: :class:`huaweicloudsdkaom.v1.SearchTemplateByIdRequest`
        :rtype: :class:`huaweicloudsdkaom.v1.SearchTemplateByIdResponse`
        """
        http_info = self._search_template_by_id_http_info(request)
        return self._call_api(**http_info)

    def search_template_by_id_async_invoker(self, request):
        http_info = self._search_template_by_id_http_info(request)
        return AsyncInvoker(self, http_info)

    def _search_template_by_id_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/cms/template/{template_id}",
            "request_type": request.__class__.__name__,
            "response_type": "SearchTemplateByIdResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def search_workflow_execution_detail_async(self, request):
        """获取工作流执行中的执行详情

        该接口可获取任务的执行详情，可指定工作流ID和执行ID去查询对应的任务，返回任务执行详情。（注：接口目前开放的region为：华北-北京四,华东-上海一,华东-上海二,华南-广州）。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for SearchWorkflowExecutionDetail
        :type request: :class:`huaweicloudsdkaom.v1.SearchWorkflowExecutionDetailRequest`
        :rtype: :class:`huaweicloudsdkaom.v1.SearchWorkflowExecutionDetailResponse`
        """
        http_info = self._search_workflow_execution_detail_http_info(request)
        return self._call_api(**http_info)

    def search_workflow_execution_detail_async_invoker(self, request):
        http_info = self._search_workflow_execution_detail_http_info(request)
        return AsyncInvoker(self, http_info)

    def _search_workflow_execution_detail_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/cms/workflow/{workflow_id}/executions/{execution_id}/status",
            "request_type": request.__class__.__name__,
            "response_type": "SearchWorkflowExecutionDetailResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def start_pausing_workflow_executions_async(self, request):
        """对暂停中的任务进行操作

        该接口可对任务进行失败重试、失败跳过、暂停继续操作，返回操作结果。（注：接口目前开放的region为：华北-北京四,华东-上海一,华东-上海二,华南-广州）。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for StartPausingWorkflowExecutions
        :type request: :class:`huaweicloudsdkaom.v1.StartPausingWorkflowExecutionsRequest`
        :rtype: :class:`huaweicloudsdkaom.v1.StartPausingWorkflowExecutionsResponse`
        """
        http_info = self._start_pausing_workflow_executions_http_info(request)
        return self._call_api(**http_info)

    def start_pausing_workflow_executions_async_invoker(self, request):
        http_info = self._start_pausing_workflow_executions_http_info(request)
        return AsyncInvoker(self, http_info)

    def _start_pausing_workflow_executions_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/cms/workflow/{workflow_id}/executions/{execution_id}/operation",
            "request_type": request.__class__.__name__,
            "response_type": "StartPausingWorkflowExecutionsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def stop_execution_async(self, request):
        """终止任务执行

        该接口可终止正在执行的任务，指定工作流ID和执行ID去终止对应的任务，返回终止操作状态。（注：接口目前开放的region为：华北-北京四,华东-上海一,华东-上海二,华南-广州）。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for StopExecution
        :type request: :class:`huaweicloudsdkaom.v1.StopExecutionRequest`
        :rtype: :class:`huaweicloudsdkaom.v1.StopExecutionResponse`
        """
        http_info = self._stop_execution_http_info(request)
        return self._call_api(**http_info)

    def stop_execution_async_invoker(self, request):
        http_info = self._stop_execution_http_info(request)
        return AsyncInvoker(self, http_info)

    def _stop_execution_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/cms/workflow/{workflow_id}/executions/{execution_id}/terminate",
            "request_type": request.__class__.__name__,
            "response_type": "StopExecutionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def update_workflow_trigger_status_async(self, request):
        """更新任务

        更新定时任务的启停状态，可启动定时任务或停止定时任务，返回操作任务结果。（注：接口目前开放的region为：华北-北京四,华东-上海一,华东-上海二,华南-广州）。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateWorkflowTriggerStatus
        :type request: :class:`huaweicloudsdkaom.v1.UpdateWorkflowTriggerStatusRequest`
        :rtype: :class:`huaweicloudsdkaom.v1.UpdateWorkflowTriggerStatusResponse`
        """
        http_info = self._update_workflow_trigger_status_http_info(request)
        return self._call_api(**http_info)

    def update_workflow_trigger_status_async_invoker(self, request):
        http_info = self._update_workflow_trigger_status_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_workflow_trigger_status_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/cms/workflow/{workflow_id}/trigger/action",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateWorkflowTriggerStatusResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

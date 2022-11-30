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


class DwrAsyncClient(Client):
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
        super(DwrAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkdwr.v3.model")
        self.preset_headers = {'User-Agent': 'HuaweiCloud-SDK-Python'}

    @classmethod
    def new_builder(cls, clazz=None):
        if clazz is None:
            return ClientBuilder(cls)

        if clazz.__name__ != "DwrClient":
            raise TypeError("client type error, support client type is DwrClient")

        return ClientBuilder(clazz)

    def accept_service_contract_async(self, request):
        """同意服务协议

        本接口用于使用工作流时需要同意服务使用协议。该函数具有幂等性。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AcceptServiceContract
        :type request: :class:`huaweicloudsdkdwr.v3.AcceptServiceContractRequest`
        :rtype: :class:`huaweicloudsdkdwr.v3.AcceptServiceContractResponse`
        """
        return self.accept_service_contract_with_http_info(request)

    def accept_service_contract_with_http_info(self, request):
        all_params = ['type']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["x-request-id", "Content-Length", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/workflow-agreements',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='AcceptServiceContractResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def async_invoke_api_start_workflow_async(self, request):
        """API异步启动工作流

        本接口用于API方式异步启动已有工作流，产生工作流实例
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AsyncInvokeApiStartWorkflow
        :type request: :class:`huaweicloudsdkdwr.v3.AsyncInvokeApiStartWorkflowRequest`
        :rtype: :class:`huaweicloudsdkdwr.v3.AsyncInvokeApiStartWorkflowResponse`
        """
        return self.async_invoke_api_start_workflow_with_http_info(request)

    def async_invoke_api_start_workflow_with_http_info(self, request):
        all_params = ['graph_name', 'async_invoke_api_start_workflow_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'graph_name' in local_var_params:
            path_params['graph_name'] = local_var_params['graph_name']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["x-request-id", "Connection", "Content-Length", "Date", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/workflows/{graph_name}/execute',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='AsyncInvokeApiStartWorkflowResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def check_workflow_authentication_async(self, request):
        """查询授权

        本接口用于查询授权，查询由DWR服务自动帮助用户创建工作流运行时需要的函数服务权限，以及函数服务运行时的权限。该函数具有幂等性。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CheckWorkflowAuthentication
        :type request: :class:`huaweicloudsdkdwr.v3.CheckWorkflowAuthenticationRequest`
        :rtype: :class:`huaweicloudsdkdwr.v3.CheckWorkflowAuthenticationResponse`
        """
        return self.check_workflow_authentication_with_http_info(request)

    def check_workflow_authentication_with_http_info(self, request):
        all_params = []
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
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["x-request-id", "Connection", "Content-Length", "Date", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/workflow-authorization',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CheckWorkflowAuthenticationResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_my_action_template_async(self, request):
        """创建第三方算子模板

        创建第三方算子模板
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateMyActionTemplate
        :type request: :class:`huaweicloudsdkdwr.v3.CreateMyActionTemplateRequest`
        :rtype: :class:`huaweicloudsdkdwr.v3.CreateMyActionTemplateResponse`
        """
        return self.create_my_action_template_with_http_info(request)

    def create_my_action_template_with_http_info(self, request):
        all_params = ['template_name', 'create_my_action_template_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'template_name' in local_var_params:
            path_params['template_name'] = local_var_params['template_name']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-request-id", "Connection", "Content-Length", "Date", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/myactiontemplates/{template_name}',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateMyActionTemplateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_workflow_authentication_async(self, request):
        """开通授权

        本接口用于开通授权，由DWR服务自动帮助用户创建工作流运行时需要的函数服务权限，以及函数服务运行时的权限。该函数具有幂等性。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateWorkflowAuthentication
        :type request: :class:`huaweicloudsdkdwr.v3.CreateWorkflowAuthenticationRequest`
        :rtype: :class:`huaweicloudsdkdwr.v3.CreateWorkflowAuthenticationResponse`
        """
        return self.create_workflow_authentication_with_http_info(request)

    def create_workflow_authentication_with_http_info(self, request):
        all_params = []
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
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["x-request-id", "Content-Length", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/workflow-authorization',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateWorkflowAuthenticationResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_my_action_template_async(self, request):
        """删除第三方算子模板

        本接口用于标记删除提交的第三方算子模板。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteMyActionTemplate
        :type request: :class:`huaweicloudsdkdwr.v3.DeleteMyActionTemplateRequest`
        :rtype: :class:`huaweicloudsdkdwr.v3.DeleteMyActionTemplateResponse`
        """
        return self.delete_my_action_template_with_http_info(request)

    def delete_my_action_template_with_http_info(self, request):
        all_params = ['template_name']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'template_name' in local_var_params:
            path_params['template_name'] = local_var_params['template_name']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["x-request-id", "Content-Length", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/myactiontemplates/{template_name}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteMyActionTemplateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_my_action_template_async(self, request):
        """查询第三方算子列表

        本接口用于查询提交注册过的三方算子列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListMyActionTemplate
        :type request: :class:`huaweicloudsdkdwr.v3.ListMyActionTemplateRequest`
        :rtype: :class:`huaweicloudsdkdwr.v3.ListMyActionTemplateResponse`
        """
        return self.list_my_action_template_with_http_info(request)

    def list_my_action_template_with_http_info(self, request):
        all_params = ['prefix', 'status', 'category', 'offset', 'limit']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'prefix' in local_var_params:
            query_params.append(('prefix', local_var_params['prefix']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'category' in local_var_params:
            query_params.append(('category', local_var_params['category']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["x-request-id", "Connection", "Content-Length", "Date", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/myactiontemplates',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListMyActionTemplateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_system_templates_async(self, request):
        """查询华为云内置算子列表

        本接口用于按名称查询系统内置算子列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListSystemTemplates
        :type request: :class:`huaweicloudsdkdwr.v3.ListSystemTemplatesRequest`
        :rtype: :class:`huaweicloudsdkdwr.v3.ListSystemTemplatesResponse`
        """
        return self.list_system_templates_with_http_info(request)

    def list_system_templates_with_http_info(self, request):
        all_params = ['prefix', 'category', 'offset', 'limit']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'prefix' in local_var_params:
            query_params.append(('prefix', local_var_params['prefix']))
        if 'category' in local_var_params:
            query_params.append(('category', local_var_params['category']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["x-request-id", "Connection", "Content-Length", "Date", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/actiontemplates',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListSystemTemplatesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_workflow_instance_async(self, request):
        """本接口用于查询用户工作流的实例列表

        本接口用于查询用户工作流的实例列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListWorkflowInstance
        :type request: :class:`huaweicloudsdkdwr.v3.ListWorkflowInstanceRequest`
        :rtype: :class:`huaweicloudsdkdwr.v3.ListWorkflowInstanceResponse`
        """
        return self.list_workflow_instance_with_http_info(request)

    def list_workflow_instance_with_http_info(self, request):
        all_params = ['graph_name', 'limit', 'start_time', 'end_time', 'status', 'offset']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'graph_name' in local_var_params:
            query_params.append(('graph_name', local_var_params['graph_name']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-Request-Id", "Content-Length", "Date", "Content-Type", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/workflowexecutions',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListWorkflowInstanceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def restore_workflow_execution_async(self, request):
        """恢复一个执行失败状态的工作流实例

        本接口用于恢复一个执行失败状态的工作流实例。恢复后，工作流实例将从上次失败的状态处继续执行，而工作流步骤中已经执行成功的状态不会再执行。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RestoreWorkflowExecution
        :type request: :class:`huaweicloudsdkdwr.v3.RestoreWorkflowExecutionRequest`
        :rtype: :class:`huaweicloudsdkdwr.v3.RestoreWorkflowExecutionResponse`
        """
        return self.restore_workflow_execution_with_http_info(request)

    def restore_workflow_execution_with_http_info(self, request):
        all_params = ['execution_name', 'graph_name']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'execution_name' in local_var_params:
            path_params['execution_name'] = local_var_params['execution_name']
        if 'graph_name' in local_var_params:
            path_params['graph_name'] = local_var_params['graph_name']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["x-request-id", "Connection", "Content-Length", "Date", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/workflows/{graph_name}/workflowexecution/{execution_name}/retry',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RestoreWorkflowExecutionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_public_action_list_async(self, request):
        """查询已发布算子列表

        本接口用于查询开放的算子列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowPublicActionList
        :type request: :class:`huaweicloudsdkdwr.v3.ShowPublicActionListRequest`
        :rtype: :class:`huaweicloudsdkdwr.v3.ShowPublicActionListResponse`
        """
        return self.show_public_action_list_with_http_info(request)

    def show_public_action_list_with_http_info(self, request):
        all_params = ['prefix', 'category', 'offset', 'limit']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'prefix' in local_var_params:
            query_params.append(('prefix', local_var_params['prefix']))
        if 'category' in local_var_params:
            query_params.append(('category', local_var_params['category']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-request-id", "Connection", "Content-Length", "Date", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/publicactiontemplates',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowPublicActionListResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_public_template_info_async(self, request):
        """查询已发布算子模板详情

        本接口用于按名称查询开放的算子详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowPublicTemplateInfo
        :type request: :class:`huaweicloudsdkdwr.v3.ShowPublicTemplateInfoRequest`
        :rtype: :class:`huaweicloudsdkdwr.v3.ShowPublicTemplateInfoResponse`
        """
        return self.show_public_template_info_with_http_info(request)

    def show_public_template_info_with_http_info(self, request):
        all_params = ['template_name']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'template_name' in local_var_params:
            path_params['template_name'] = local_var_params['template_name']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-request-id", "Connection", "Content-Length", "Date", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/publicactiontemplate/{template_name}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowPublicTemplateInfoResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_service_contract_async(self, request):
        """查询服务协议

        本接口用于查询使用工作流时同意的服务协议。该函数具有幂等性。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowServiceContract
        :type request: :class:`huaweicloudsdkdwr.v3.ShowServiceContractRequest`
        :rtype: :class:`huaweicloudsdkdwr.v3.ShowServiceContractResponse`
        """
        return self.show_service_contract_with_http_info(request)

    def show_service_contract_with_http_info(self, request):
        all_params = ['type']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["x-request-id", "Connection", "Content-Length", "Date", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/workflow-agreements',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowServiceContractResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_system_template_detail_async(self, request):
        """查询华为云内置算子模板信息

        本接口用于按名称查询系统内置算子详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowSystemTemplateDetail
        :type request: :class:`huaweicloudsdkdwr.v3.ShowSystemTemplateDetailRequest`
        :rtype: :class:`huaweicloudsdkdwr.v3.ShowSystemTemplateDetailResponse`
        """
        return self.show_system_template_detail_with_http_info(request)

    def show_system_template_detail_with_http_info(self, request):
        all_params = ['template_name']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'template_name' in local_var_params:
            path_params['template_name'] = local_var_params['template_name']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["x-request-id", "Connection", "Content-Length", "Date", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/actiontemplate/{template_name}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowSystemTemplateDetailResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_third_template_info_async(self, request):
        """查询公共Action模板详情

        本接口用于按名称查询第三方模板详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowThirdTemplateInfo
        :type request: :class:`huaweicloudsdkdwr.v3.ShowThirdTemplateInfoRequest`
        :rtype: :class:`huaweicloudsdkdwr.v3.ShowThirdTemplateInfoResponse`
        """
        return self.show_third_template_info_with_http_info(request)

    def show_third_template_info_with_http_info(self, request):
        all_params = ['template_name']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'template_name' in local_var_params:
            path_params['template_name'] = local_var_params['template_name']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["x-request-id", "Connection", "Content-Length", "Date", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/myactiontemplate/{template_name}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowThirdTemplateInfoResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_workflow_instance_async(self, request):
        """本接口用于查询指定工作流实例详细

        本接口用于查询指定工作流实例详细。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowWorkflowInstance
        :type request: :class:`huaweicloudsdkdwr.v3.ShowWorkflowInstanceRequest`
        :rtype: :class:`huaweicloudsdkdwr.v3.ShowWorkflowInstanceResponse`
        """
        return self.show_workflow_instance_with_http_info(request)

    def show_workflow_instance_with_http_info(self, request):
        all_params = ['execution_name', 'graph_name']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'execution_name' in local_var_params:
            path_params['execution_name'] = local_var_params['execution_name']
        if 'graph_name' in local_var_params:
            path_params['graph_name'] = local_var_params['graph_name']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["x-request-id", "Connection", "Content-Length", "Date", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/workflows/{graph_name}/workflowexecution/{execution_name}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowWorkflowInstanceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_my_action_template_async(self, request):
        """更新第三方算子模板

        本接口用于修改第三方算子和将三方算子提交审核
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateMyActionTemplate
        :type request: :class:`huaweicloudsdkdwr.v3.UpdateMyActionTemplateRequest`
        :rtype: :class:`huaweicloudsdkdwr.v3.UpdateMyActionTemplateResponse`
        """
        return self.update_my_action_template_with_http_info(request)

    def update_my_action_template_with_http_info(self, request):
        all_params = ['template_name', 'update_my_action_template_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'template_name' in local_var_params:
            path_params['template_name'] = local_var_params['template_name']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["x-request-id", "Connection", "Content-Length", "Date", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/myactiontemplates/{template_name}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateMyActionTemplateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_my_action_template_to_deprecated_async(self, request):
        """禁用第三方算子模板

        本接口用于申请禁用第三方算子。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateMyActionTemplateToDeprecated
        :type request: :class:`huaweicloudsdkdwr.v3.UpdateMyActionTemplateToDeprecatedRequest`
        :rtype: :class:`huaweicloudsdkdwr.v3.UpdateMyActionTemplateToDeprecatedResponse`
        """
        return self.update_my_action_template_to_deprecated_with_http_info(request)

    def update_my_action_template_to_deprecated_with_http_info(self, request):
        all_params = ['template_name']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'template_name' in local_var_params:
            path_params['template_name'] = local_var_params['template_name']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["x-request-id", "Content-Length", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/myactiontemplates/{template_name}/forbid',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateMyActionTemplateToDeprecatedResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_workflow_async(self, request):
        """创建工作流

        本接口用于通过Body体直接创建工作流
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateWorkflow
        :type request: :class:`huaweicloudsdkdwr.v3.CreateWorkflowRequest`
        :rtype: :class:`huaweicloudsdkdwr.v3.CreateWorkflowResponse`
        """
        return self.create_workflow_with_http_info(request)

    def create_workflow_with_http_info(self, request):
        all_params = ['graph_name', 'create_workflow_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'graph_name' in local_var_params:
            path_params['graph_name'] = local_var_params['graph_name']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["x-request-id", "Connection", "Content-Length", "Date", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/workflows/{graph_name}',
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

    def delete_workflow_async(self, request):
        """删除工作流

        本接口用于删除工作流。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteWorkflow
        :type request: :class:`huaweicloudsdkdwr.v3.DeleteWorkflowRequest`
        :rtype: :class:`huaweicloudsdkdwr.v3.DeleteWorkflowResponse`
        """
        return self.delete_workflow_with_http_info(request)

    def delete_workflow_with_http_info(self, request):
        all_params = ['graph_name']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'graph_name' in local_var_params:
            path_params['graph_name'] = local_var_params['graph_name']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["x-request-id", "Content-Length", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/workflows/{graph_name}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteWorkflowResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_workflows_async(self, request):
        """查询工作流列表

        本接口用于查询工作流列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListWorkflows
        :type request: :class:`huaweicloudsdkdwr.v3.ListWorkflowsRequest`
        :rtype: :class:`huaweicloudsdkdwr.v3.ListWorkflowsResponse`
        """
        return self.list_workflows_with_http_info(request)

    def list_workflows_with_http_info(self, request):
        all_params = ['prefix', 'offset', 'limit']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'prefix' in local_var_params:
            query_params.append(('prefix', local_var_params['prefix']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["x-request-id", "Connection", "Content-Length", "Date", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/workflows',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListWorkflowsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_workflow_info_async(self, request):
        """查询工作流信息

        本接口用于根据工作流名称查询工作流详细信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowWorkflowInfo
        :type request: :class:`huaweicloudsdkdwr.v3.ShowWorkflowInfoRequest`
        :rtype: :class:`huaweicloudsdkdwr.v3.ShowWorkflowInfoResponse`
        """
        return self.show_workflow_info_with_http_info(request)

    def show_workflow_info_with_http_info(self, request):
        all_params = ['graph_name']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'graph_name' in local_var_params:
            path_params['graph_name'] = local_var_params['graph_name']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["x-request-id", "Connection", "Content-Length", "Date", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/workflows/{graph_name}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowWorkflowInfoResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_workflow_async(self, request):
        """更新工作流

        Update Workflow
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateWorkflow
        :type request: :class:`huaweicloudsdkdwr.v3.UpdateWorkflowRequest`
        :rtype: :class:`huaweicloudsdkdwr.v3.UpdateWorkflowResponse`
        """
        return self.update_workflow_with_http_info(request)

    def update_workflow_with_http_info(self, request):
        all_params = ['graph_name', 'update_workflow_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'graph_name' in local_var_params:
            path_params['graph_name'] = local_var_params['graph_name']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["x-request-id", "Connection", "Content-Length", "Date", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/workflows/{graph_name}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateWorkflowResponse',
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

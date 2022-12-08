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


class AosClient(Client):
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
        super(AosClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkaos.v1.model")
        self.preset_headers = {'User-Agent': 'HuaweiCloud-SDK-Python'}

    @classmethod
    def new_builder(cls, clazz=None):
        if clazz is None:
            return ClientBuilder(cls)

        if clazz.__name__ != "AosClient":
            raise TypeError("client type error, support client type is AosClient")

        return ClientBuilder(clazz)

    def apply_execution_plan(self, request):
        """此命令用于执行已有的执行计划(execution plan)

        此命令用于执行已有的执行计划(execution plan)
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ApplyExecutionPlan
        :type request: :class:`huaweicloudsdkaos.v1.ApplyExecutionPlanRequest`
        :rtype: :class:`huaweicloudsdkaos.v1.ApplyExecutionPlanResponse`
        """
        return self.apply_execution_plan_with_http_info(request)

    def apply_execution_plan_with_http_info(self, request):
        all_params = ['client_request_id', 'stack_name', 'execution_plan_name', 'apply_execution_plan_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'stack_name' in local_var_params:
            path_params['stack_name'] = local_var_params['stack_name']
        if 'execution_plan_name' in local_var_params:
            path_params['execution_plan_name'] = local_var_params['execution_plan_name']

        query_params = []

        header_params = {}
        if 'client_request_id' in local_var_params:
            header_params['Client-Request-Id'] = local_var_params['client_request_id']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['token']

        return self.call_api(
            resource_path='/v1/{project_id}/stacks/{stack_name}/execution-plans/{execution_plan_name}',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ApplyExecutionPlanResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_execution_plan(self, request):
        """此命令用于生成一个执行计划(execution plan)

        此命令用于生成一个执行计划(execution plan)
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateExecutionPlan
        :type request: :class:`huaweicloudsdkaos.v1.CreateExecutionPlanRequest`
        :rtype: :class:`huaweicloudsdkaos.v1.CreateExecutionPlanResponse`
        """
        return self.create_execution_plan_with_http_info(request)

    def create_execution_plan_with_http_info(self, request):
        all_params = ['client_request_id', 'stack_name', 'create_execution_plan_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'stack_name' in local_var_params:
            path_params['stack_name'] = local_var_params['stack_name']

        query_params = []

        header_params = {}
        if 'client_request_id' in local_var_params:
            header_params['Client-Request-Id'] = local_var_params['client_request_id']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['token']

        return self.call_api(
            resource_path='/v1/{project_id}/stacks/{stack_name}/execution-plans',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateExecutionPlanResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_execution_plan(self, request):
        """此命令用于删除已有的执行计划(execution plan)

        此命令用于删除已有的执行计划(execution plan)
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteExecutionPlan
        :type request: :class:`huaweicloudsdkaos.v1.DeleteExecutionPlanRequest`
        :rtype: :class:`huaweicloudsdkaos.v1.DeleteExecutionPlanResponse`
        """
        return self.delete_execution_plan_with_http_info(request)

    def delete_execution_plan_with_http_info(self, request):
        all_params = ['client_request_id', 'stack_name', 'execution_plan_name', 'stack_id', 'execution_plan_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'stack_name' in local_var_params:
            path_params['stack_name'] = local_var_params['stack_name']
        if 'execution_plan_name' in local_var_params:
            path_params['execution_plan_name'] = local_var_params['execution_plan_name']

        query_params = []
        if 'stack_id' in local_var_params:
            query_params.append(('stack_id', local_var_params['stack_id']))
        if 'execution_plan_id' in local_var_params:
            query_params.append(('execution_plan_id', local_var_params['execution_plan_id']))

        header_params = {}
        if 'client_request_id' in local_var_params:
            header_params['Client-Request-Id'] = local_var_params['client_request_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['token']

        return self.call_api(
            resource_path='/v1/{project_id}/stacks/{stack_name}/execution-plans/{execution_plan_name}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteExecutionPlanResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_stack(self, request):
        """删除资源栈

        删除资源栈
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteStack
        :type request: :class:`huaweicloudsdkaos.v1.DeleteStackRequest`
        :rtype: :class:`huaweicloudsdkaos.v1.DeleteStackResponse`
        """
        return self.delete_stack_with_http_info(request)

    def delete_stack_with_http_info(self, request):
        all_params = ['client_request_id', 'stack_name', 'stack_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'stack_name' in local_var_params:
            path_params['stack_name'] = local_var_params['stack_name']

        query_params = []
        if 'stack_id' in local_var_params:
            query_params.append(('stack_id', local_var_params['stack_id']))

        header_params = {}
        if 'client_request_id' in local_var_params:
            header_params['Client-Request-Id'] = local_var_params['client_request_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['token']

        return self.call_api(
            resource_path='/v1/{project_id}/stacks/{stack_name}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteStackResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def describe_execution_plan(self, request):
        """描述执行计划当前的状态，返回执行计划的元数据

        描述执行计划当前的状态，返回执行计划的元数据
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DescribeExecutionPlan
        :type request: :class:`huaweicloudsdkaos.v1.DescribeExecutionPlanRequest`
        :rtype: :class:`huaweicloudsdkaos.v1.DescribeExecutionPlanResponse`
        """
        return self.describe_execution_plan_with_http_info(request)

    def describe_execution_plan_with_http_info(self, request):
        all_params = ['client_request_id', 'stack_name', 'execution_plan_name', 'stack_id', 'execution_plan_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'stack_name' in local_var_params:
            path_params['stack_name'] = local_var_params['stack_name']
        if 'execution_plan_name' in local_var_params:
            path_params['execution_plan_name'] = local_var_params['execution_plan_name']

        query_params = []
        if 'stack_id' in local_var_params:
            query_params.append(('stack_id', local_var_params['stack_id']))
        if 'execution_plan_id' in local_var_params:
            query_params.append(('execution_plan_id', local_var_params['execution_plan_id']))

        header_params = {}
        if 'client_request_id' in local_var_params:
            header_params['Client-Request-Id'] = local_var_params['client_request_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['token']

        return self.call_api(
            resource_path='/v1/{project_id}/stacks/{stack_name}/execution-plans/{execution_plan_name}/metadata',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DescribeExecutionPlanResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def estimate_execution_plan_price(self, request):
        """预估执行计划的价格

        预估执行计划的价格
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for EstimateExecutionPlanPrice
        :type request: :class:`huaweicloudsdkaos.v1.EstimateExecutionPlanPriceRequest`
        :rtype: :class:`huaweicloudsdkaos.v1.EstimateExecutionPlanPriceResponse`
        """
        return self.estimate_execution_plan_price_with_http_info(request)

    def estimate_execution_plan_price_with_http_info(self, request):
        all_params = ['client_request_id', 'stack_name', 'execution_plan_name', 'stack_id', 'execution_plan_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'stack_name' in local_var_params:
            path_params['stack_name'] = local_var_params['stack_name']
        if 'execution_plan_name' in local_var_params:
            path_params['execution_plan_name'] = local_var_params['execution_plan_name']

        query_params = []
        if 'stack_id' in local_var_params:
            query_params.append(('stack_id', local_var_params['stack_id']))
        if 'execution_plan_id' in local_var_params:
            query_params.append(('execution_plan_id', local_var_params['execution_plan_id']))

        header_params = {}
        if 'client_request_id' in local_var_params:
            header_params['Client-Request-Id'] = local_var_params['client_request_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['token']

        return self.call_api(
            resource_path='/v1/{project_id}/stacks/{stack_name}/execution-plans/{execution_plan_name}/prices',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='EstimateExecutionPlanPriceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def get_execution_plan(self, request):
        """此接口用于获取执行计划的详细内容

        此接口用于获取执行计划的详细内容
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for GetExecutionPlan
        :type request: :class:`huaweicloudsdkaos.v1.GetExecutionPlanRequest`
        :rtype: :class:`huaweicloudsdkaos.v1.GetExecutionPlanResponse`
        """
        return self.get_execution_plan_with_http_info(request)

    def get_execution_plan_with_http_info(self, request):
        all_params = ['client_request_id', 'stack_name', 'execution_plan_name', 'stack_id', 'execution_plan_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'stack_name' in local_var_params:
            path_params['stack_name'] = local_var_params['stack_name']
        if 'execution_plan_name' in local_var_params:
            path_params['execution_plan_name'] = local_var_params['execution_plan_name']

        query_params = []
        if 'stack_id' in local_var_params:
            query_params.append(('stack_id', local_var_params['stack_id']))
        if 'execution_plan_id' in local_var_params:
            query_params.append(('execution_plan_id', local_var_params['execution_plan_id']))

        header_params = {}
        if 'client_request_id' in local_var_params:
            header_params['Client-Request-Id'] = local_var_params['client_request_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['token']

        return self.call_api(
            resource_path='/v1/{project_id}/stacks/{stack_name}/execution-plans/{execution_plan_name}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='GetExecutionPlanResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def get_stack_metadata(self, request):
        """描述栈的状态，返回栈的元数据

        描述栈的状态，返回栈的元数据
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for GetStackMetadata
        :type request: :class:`huaweicloudsdkaos.v1.GetStackMetadataRequest`
        :rtype: :class:`huaweicloudsdkaos.v1.GetStackMetadataResponse`
        """
        return self.get_stack_metadata_with_http_info(request)

    def get_stack_metadata_with_http_info(self, request):
        all_params = ['client_request_id', 'stack_name', 'stack_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'stack_name' in local_var_params:
            path_params['stack_name'] = local_var_params['stack_name']

        query_params = []
        if 'stack_id' in local_var_params:
            query_params.append(('stack_id', local_var_params['stack_id']))

        header_params = {}
        if 'client_request_id' in local_var_params:
            header_params['Client-Request-Id'] = local_var_params['client_request_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['token']

        return self.call_api(
            resource_path='/v1/{project_id}/stacks/{stack_name}/metadata',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='GetStackMetadataResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def get_stack_template(self, request):
        """获取资源栈模板

        获取资源栈当前使用的模板
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for GetStackTemplate
        :type request: :class:`huaweicloudsdkaos.v1.GetStackTemplateRequest`
        :rtype: :class:`huaweicloudsdkaos.v1.GetStackTemplateResponse`
        """
        return self.get_stack_template_with_http_info(request)

    def get_stack_template_with_http_info(self, request):
        all_params = ['client_request_id', 'stack_name', 'stack_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'stack_name' in local_var_params:
            path_params['stack_name'] = local_var_params['stack_name']

        query_params = []
        if 'stack_id' in local_var_params:
            query_params.append(('stack_id', local_var_params['stack_id']))

        header_params = {}
        if 'client_request_id' in local_var_params:
            header_params['Client-Request-Id'] = local_var_params['client_request_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['token']

        return self.call_api(
            resource_path='/v1/{project_id}/stacks/{stack_name}/templates',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='GetStackTemplateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_execution_plans(self, request):
        """列举执行计划

        列举执行计划
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListExecutionPlans
        :type request: :class:`huaweicloudsdkaos.v1.ListExecutionPlansRequest`
        :rtype: :class:`huaweicloudsdkaos.v1.ListExecutionPlansResponse`
        """
        return self.list_execution_plans_with_http_info(request)

    def list_execution_plans_with_http_info(self, request):
        all_params = ['client_request_id', 'stack_name', 'stack_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'stack_name' in local_var_params:
            path_params['stack_name'] = local_var_params['stack_name']

        query_params = []
        if 'stack_id' in local_var_params:
            query_params.append(('stack_id', local_var_params['stack_id']))

        header_params = {}
        if 'client_request_id' in local_var_params:
            header_params['Client-Request-Id'] = local_var_params['client_request_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['token']

        return self.call_api(
            resource_path='/v1/{project_id}/stacks/{stack_name}/execution-plans',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListExecutionPlansResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_stack_events(self, request):
        """获取栈的细节更新状态

        获取栈的细节更新状态，可以获取整个栈从生成到当前时间点的所有状态
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListStackEvents
        :type request: :class:`huaweicloudsdkaos.v1.ListStackEventsRequest`
        :rtype: :class:`huaweicloudsdkaos.v1.ListStackEventsResponse`
        """
        return self.list_stack_events_with_http_info(request)

    def list_stack_events_with_http_info(self, request):
        all_params = ['client_request_id', 'stack_name', 'stack_id', 'deployment_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'stack_name' in local_var_params:
            path_params['stack_name'] = local_var_params['stack_name']

        query_params = []
        if 'stack_id' in local_var_params:
            query_params.append(('stack_id', local_var_params['stack_id']))
        if 'deployment_id' in local_var_params:
            query_params.append(('deployment_id', local_var_params['deployment_id']))

        header_params = {}
        if 'client_request_id' in local_var_params:
            header_params['Client-Request-Id'] = local_var_params['client_request_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['token']

        return self.call_api(
            resource_path='/v1/{project_id}/stacks/{stack_name}/events',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListStackEventsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_stack_outputs(self, request):
        """列举资源栈的输出

        列举资源栈的输出
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListStackOutputs
        :type request: :class:`huaweicloudsdkaos.v1.ListStackOutputsRequest`
        :rtype: :class:`huaweicloudsdkaos.v1.ListStackOutputsResponse`
        """
        return self.list_stack_outputs_with_http_info(request)

    def list_stack_outputs_with_http_info(self, request):
        all_params = ['client_request_id', 'stack_name', 'stack_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'stack_name' in local_var_params:
            path_params['stack_name'] = local_var_params['stack_name']

        query_params = []
        if 'stack_id' in local_var_params:
            query_params.append(('stack_id', local_var_params['stack_id']))

        header_params = {}
        if 'client_request_id' in local_var_params:
            header_params['Client-Request-Id'] = local_var_params['client_request_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['token']

        return self.call_api(
            resource_path='/v1/{project_id}/stacks/{stack_name}/outputs',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListStackOutputsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_stack_resources(self, request):
        """获取资源栈的资源列表

        获取资源栈的资源列表，可以获取整个栈从生成到当前时间点的所有状态
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListStackResources
        :type request: :class:`huaweicloudsdkaos.v1.ListStackResourcesRequest`
        :rtype: :class:`huaweicloudsdkaos.v1.ListStackResourcesResponse`
        """
        return self.list_stack_resources_with_http_info(request)

    def list_stack_resources_with_http_info(self, request):
        all_params = ['client_request_id', 'stack_name', 'stack_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'stack_name' in local_var_params:
            path_params['stack_name'] = local_var_params['stack_name']

        query_params = []
        if 'stack_id' in local_var_params:
            query_params.append(('stack_id', local_var_params['stack_id']))

        header_params = {}
        if 'client_request_id' in local_var_params:
            header_params['Client-Request-Id'] = local_var_params['client_request_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['token']

        return self.call_api(
            resource_path='/v1/{project_id}/stacks/{stack_name}/resources',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListStackResourcesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def parse_template_variables(self, request):
        """此命令用于解析模板参数

        此命令用于解析模板参数
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ParseTemplateVariables
        :type request: :class:`huaweicloudsdkaos.v1.ParseTemplateVariablesRequest`
        :rtype: :class:`huaweicloudsdkaos.v1.ParseTemplateVariablesResponse`
        """
        return self.parse_template_variables_with_http_info(request)

    def parse_template_variables_with_http_info(self, request):
        all_params = ['client_request_id', 'parse_template_variables_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'client_request_id' in local_var_params:
            header_params['Client-Request-Id'] = local_var_params['client_request_id']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['token']

        return self.call_api(
            resource_path='/v1/{project_id}/template-analyses/variables',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ParseTemplateVariablesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def continue_rollback_stack(self, request):
        """继续回滚资源栈

        如果资源栈开启了自动回滚，在部署失败的时候则会自动回滚。但是自动回滚依然有可能失败，用户可以根据错误信息修复后，调用ContinueRollbackStack触发继续回滚，即重试回滚
        
        * 如果资源栈当前可以回滚，即处于&#x60;ROLLBACK_FAILED&#x60;，则返回202与对应生成的deploymentId，否则将不允许回滚并返回响应的错误码
        * 继续回滚也有可能会回滚失败。如果失败，用户可以从ListStackEvents获取对应的log，解决后可再次调用ContinueRollbackStack去继续触发回滚
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ContinueRollbackStack
        :type request: :class:`huaweicloudsdkaos.v1.ContinueRollbackStackRequest`
        :rtype: :class:`huaweicloudsdkaos.v1.ContinueRollbackStackResponse`
        """
        return self.continue_rollback_stack_with_http_info(request)

    def continue_rollback_stack_with_http_info(self, request):
        all_params = ['client_request_id', 'stack_name', 'continue_rollback_stack_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'stack_name' in local_var_params:
            path_params['stack_name'] = local_var_params['stack_name']

        query_params = []

        header_params = {}
        if 'client_request_id' in local_var_params:
            header_params['Client-Request-Id'] = local_var_params['client_request_id']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['token']

        return self.call_api(
            resource_path='/v1/{project_id}/stacks/{stack_name}/rollbacks',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ContinueRollbackStackResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_stack(self, request):
        """创建资源栈

        CreateStack用于生成一个资源栈
        
        * 当请求中不含有模板（template）、参数（vars）等信息，将生成一个无任何资源的空资源栈，返回资源栈ID（stack_id）
        * 当请求中携带了模板（template）、参数（vars）等信息，则会同时创建并部署资源栈，返回资源栈ID（stack_id）和部署ID（deployment_id）
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateStack
        :type request: :class:`huaweicloudsdkaos.v1.CreateStackRequest`
        :rtype: :class:`huaweicloudsdkaos.v1.CreateStackResponse`
        """
        return self.create_stack_with_http_info(request)

    def create_stack_with_http_info(self, request):
        all_params = ['client_request_id', 'create_stack_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'client_request_id' in local_var_params:
            header_params['Client-Request-Id'] = local_var_params['client_request_id']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['token']

        return self.call_api(
            resource_path='/v1/{project_id}/stacks',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateStackResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def deploy_stack(self, request):
        """部署一个已有的资源栈

        部署一个已有的资源栈
        
        * 用户可以使用此API更新模板、参数等并触发一个新的部署
        
        * 此API会直接触发部署，如果用户希望先确认部署会发生的时间，请使用执行计划，即使用CreateExecutionPlan以创建执行计划、使用GetExecutionPlan以获取执行计划
        
        * 此API为全量API，即用户每次部署都需要给予所想要使用的template、vars的全量
        
        * 当触发的部署失败时，如果资源栈开启了自动回滚，会触发自动回滚的流程，否则就会停留在部署失败时的状态
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeployStack
        :type request: :class:`huaweicloudsdkaos.v1.DeployStackRequest`
        :rtype: :class:`huaweicloudsdkaos.v1.DeployStackResponse`
        """
        return self.deploy_stack_with_http_info(request)

    def deploy_stack_with_http_info(self, request):
        all_params = ['client_request_id', 'stack_name', 'deploy_stack_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'stack_name' in local_var_params:
            path_params['stack_name'] = local_var_params['stack_name']

        query_params = []

        header_params = {}
        if 'client_request_id' in local_var_params:
            header_params['Client-Request-Id'] = local_var_params['client_request_id']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['token']

        return self.call_api(
            resource_path='/v1/{project_id}/stacks/{stack_name}/deployments',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeployStackResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_stacks(self, request):
        """列举资源栈

        ListStacks 列举当前局点下用户所有的资源栈
        
          * 默认按照生成时间排序，最早生成的在最前
          * 注意：目前暂时返回全量资源栈信息，即不支持分页
          * 如果没有任何资源栈，则返回空list
        
        ListStacks返回的只有摘要信息（具体摘要信息见ListStacksResponseBody），如果用户需要详细的资源栈元数据请调用GetStackMetadata
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListStacks
        :type request: :class:`huaweicloudsdkaos.v1.ListStacksRequest`
        :rtype: :class:`huaweicloudsdkaos.v1.ListStacksResponse`
        """
        return self.list_stacks_with_http_info(request)

    def list_stacks_with_http_info(self, request):
        all_params = ['client_request_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'client_request_id' in local_var_params:
            header_params['Client-Request-Id'] = local_var_params['client_request_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['token']

        return self.call_api(
            resource_path='/v1/{project_id}/stacks',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListStacksResponse',
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

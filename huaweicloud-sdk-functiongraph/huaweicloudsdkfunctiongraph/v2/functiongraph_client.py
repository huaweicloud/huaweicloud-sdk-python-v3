# coding: utf-8

from __future__ import absolute_import

import importlib

from huaweicloudsdkcore.client import Client, ClientBuilder
from huaweicloudsdkcore.utils import http_utils
from huaweicloudsdkcore.sdk_stream_request import SdkStreamRequest


class FunctionGraphClient(Client):
    def __init__(self):
        super(FunctionGraphClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkfunctiongraph.v2.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if clazz is None:
            return ClientBuilder(cls)

        if clazz.__name__ != "FunctionGraphClient":
            raise TypeError("client type error, support client type is FunctionGraphClient")

        return ClientBuilder(clazz)

    def async_invoke_function(self, request):
        """异步执行函数

        异步执行函数。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AsyncInvokeFunction
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.AsyncInvokeFunctionRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.AsyncInvokeFunctionResponse`
        """
        return self._async_invoke_function_with_http_info(request)

    def _async_invoke_function_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'function_urn' in local_var_params:
            path_params['function_urn'] = local_var_params['function_urn']

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
            resource_path='/v2/{project_id}/fgs/functions/{function_urn}/invocations-async',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='AsyncInvokeFunctionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def async_invoke_reserved_function(self, request):
        """函数异步执行并返回预留实例ID

        函数异步执行并返回预留实例ID用于场景指客户端请求执行比较费时任务，不需要同步等待执行完成返回结果，该方法提前返回任务执行对应的预留实例ID, 如果预留实例有异常，可以通过该实例ID把对应实例删除（该接口主要针对白名单用户）。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AsyncInvokeReservedFunction
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.AsyncInvokeReservedFunctionRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.AsyncInvokeReservedFunctionResponse`
        """
        return self._async_invoke_reserved_function_with_http_info(request)

    def _async_invoke_reserved_function_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'function_urn' in local_var_params:
            path_params['function_urn'] = local_var_params['function_urn']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["Content-Type", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/fgs/functions/{function_urn}/reserved-invocations',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='AsyncInvokeReservedFunctionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_delete_function_triggers(self, request):
        """删除指定函数的所有触发器

        删除指定函数所有触发器设置。
        
        在提供函数版本且非latest的情况下，删除对应函数版本的触发器。
        在提供函数别名的情况下，删除对应函数别名的触发器。
        在不提供函数版本（也不提供别名）或版本为latest的情况下，删除该函数所有的触发器（包括所有版本和别名）。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchDeleteFunctionTriggers
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.BatchDeleteFunctionTriggersRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.BatchDeleteFunctionTriggersResponse`
        """
        return self._batch_delete_function_triggers_with_http_info(request)

    def _batch_delete_function_triggers_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'function_urn' in local_var_params:
            path_params['function_urn'] = local_var_params['function_urn']

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
            resource_path='/v2/{project_id}/fgs/triggers/{function_urn}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchDeleteFunctionTriggersResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_delete_workflows(self, request):
        """删除函数流

        删除函数流
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchDeleteWorkflows
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.BatchDeleteWorkflowsRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.BatchDeleteWorkflowsResponse`
        """
        return self._batch_delete_workflows_with_http_info(request)

    def _batch_delete_workflows_with_http_info(self, request):
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
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/fgs/workflows',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchDeleteWorkflowsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def cancel_async_invocation(self, request):
        """停止函数异步调用请求

        -| 停止函数异步调用请求 当前仅支持recursive为false且force为true的参数。针对1：N的函数做并发异步调用 停止异步请求时实例同时在执行的其他请求也会被一并停止并返回4208 function invocation canceled 目前仅支持广州和贵阳一
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CancelAsyncInvocation
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.CancelAsyncInvocationRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.CancelAsyncInvocationResponse`
        """
        return self._cancel_async_invocation_with_http_info(request)

    def _cancel_async_invocation_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'function_urn' in local_var_params:
            path_params['function_urn'] = local_var_params['function_urn']

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
            resource_path='/v2/{project_id}/fgs/functions/{function_urn}/cancel',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CancelAsyncInvocationResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_dependency(self, request):
        """创建依赖包

        创建依赖包
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateDependency
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.CreateDependencyRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.CreateDependencyResponse`
        """
        return self._create_dependency_with_http_info(request)

    def _create_dependency_with_http_info(self, request):
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
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/fgs/dependencies',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateDependencyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_dependency_version(self, request):
        """创建依赖包版本

        创建依赖包版本
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateDependencyVersion
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.CreateDependencyVersionRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.CreateDependencyVersionResponse`
        """
        return self._create_dependency_version_with_http_info(request)

    def _create_dependency_version_with_http_info(self, request):
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
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/fgs/dependencies/version',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateDependencyVersionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_event(self, request):
        """创建测试事件

        创建测试事件
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateEvent
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.CreateEventRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.CreateEventResponse`
        """
        return self._create_event_with_http_info(request)

    def _create_event_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'function_urn' in local_var_params:
            path_params['function_urn'] = local_var_params['function_urn']

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
            resource_path='/v2/{project_id}/fgs/functions/{function_urn}/events',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateEventResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_function(self, request):
        """创建函数

        创建指定的函数。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateFunction
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.CreateFunctionRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.CreateFunctionResponse`
        """
        return self._create_function_with_http_info(request)

    def _create_function_with_http_info(self, request):
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
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/fgs/functions',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateFunctionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_function_trigger(self, request):
        """创建触发器

        创建触发器。
        
        - 可以创建的触发器类型包括TIMER、APIG、CTS、DDS、DMS、DIS、LTS、OBS、SMN、KAFKA。
        - DDS和KAFKA触发器创建时默认为DISABLED状态，其他触发器默认为ACTIVE状态。
        - TIMER、DDS、DMS、KAFKA、LTS触发器支持禁用，其他触发器不支持。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateFunctionTrigger
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.CreateFunctionTriggerRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.CreateFunctionTriggerResponse`
        """
        return self._create_function_trigger_with_http_info(request)

    def _create_function_trigger_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'function_urn' in local_var_params:
            path_params['function_urn'] = local_var_params['function_urn']

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
            resource_path='/v2/{project_id}/fgs/triggers/{function_urn}',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateFunctionTriggerResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_function_version(self, request):
        """发布函数版本

        发布函数版本。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateFunctionVersion
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.CreateFunctionVersionRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.CreateFunctionVersionResponse`
        """
        return self._create_function_version_with_http_info(request)

    def _create_function_version_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'function_urn' in local_var_params:
            path_params['function_urn'] = local_var_params['function_urn']

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
            resource_path='/v2/{project_id}/fgs/functions/{function_urn}/versions',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateFunctionVersionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_tags(self, request):
        """创建资源标签

        创建资源标签。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateTags
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.CreateTagsRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.CreateTagsResponse`
        """
        return self._create_tags_with_http_info(request)

    def _create_tags_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_type' in local_var_params:
            path_params['resource_type'] = local_var_params['resource_type']
        if 'resource_id' in local_var_params:
            path_params['resource_id'] = local_var_params['resource_id']

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
            resource_path='/v2/{project_id}/{resource_type}/{resource_id}/tags/create',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_version_alias(self, request):
        """创建函数版本别名

        创建函数灰度版本别名。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateVersionAlias
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.CreateVersionAliasRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.CreateVersionAliasResponse`
        """
        return self._create_version_alias_with_http_info(request)

    def _create_version_alias_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'function_urn' in local_var_params:
            path_params['function_urn'] = local_var_params['function_urn']

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
            resource_path='/v2/{project_id}/fgs/functions/{function_urn}/aliases',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateVersionAliasResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_vpc_endpoint(self, request):
        """创建下沉入口

        创建下沉入口。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateVpcEndpoint
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.CreateVpcEndpointRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.CreateVpcEndpointResponse`
        """
        return self._create_vpc_endpoint_with_http_info(request)

    def _create_vpc_endpoint_with_http_info(self, request):
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
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/fgs/vpc-endpoint',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateVpcEndpointResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_workflow(self, request):
        """创建函数流

        创建函数流
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateWorkflow
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.CreateWorkflowRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.CreateWorkflowResponse`
        """
        return self._create_workflow_with_http_info(request)

    def _create_workflow_with_http_info(self, request):
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
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/fgs/workflows',
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

    def delete_dependency(self, request):
        """删除指定的依赖包

        删除指定的依赖包
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteDependency
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.DeleteDependencyRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.DeleteDependencyResponse`
        """
        return self._delete_dependency_with_http_info(request)

    def _delete_dependency_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'depend_id' in local_var_params:
            path_params['depend_id'] = local_var_params['depend_id']

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
            resource_path='/v2/{project_id}/fgs/dependencies/{depend_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteDependencyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_dependency_version(self, request):
        """删除依赖包版本

        删除依赖包版本
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteDependencyVersion
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.DeleteDependencyVersionRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.DeleteDependencyVersionResponse`
        """
        return self._delete_dependency_version_with_http_info(request)

    def _delete_dependency_version_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'depend_id' in local_var_params:
            path_params['depend_id'] = local_var_params['depend_id']
        if 'version' in local_var_params:
            path_params['version'] = local_var_params['version']

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
            resource_path='/v2/{project_id}/fgs/dependencies/{depend_id}/version/{version}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteDependencyVersionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_event(self, request):
        """删除指定测试事件

        删除指定测试事件
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteEvent
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.DeleteEventRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.DeleteEventResponse`
        """
        return self._delete_event_with_http_info(request)

    def _delete_event_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'function_urn' in local_var_params:
            path_params['function_urn'] = local_var_params['function_urn']
        if 'event_id' in local_var_params:
            path_params['event_id'] = local_var_params['event_id']

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
            resource_path='/v2/{project_id}/fgs/functions/{function_urn}/events/{event_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteEventResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_function(self, request):
        """删除函数/版本

        删除指定的函数或者特定的版本（不允许删除latest版本）。
        
        如果URN中包含函数版本或者别名，则删除特定的函数版本或者别名指向的版本以及该版本关联的trigger。
        如果URN中不包含版本或者别名，则删除整个函数，包含所有版本以及别名，触发器。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteFunction
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.DeleteFunctionRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.DeleteFunctionResponse`
        """
        return self._delete_function_with_http_info(request)

    def _delete_function_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'function_urn' in local_var_params:
            path_params['function_urn'] = local_var_params['function_urn']

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
            resource_path='/v2/{project_id}/fgs/functions/{function_urn}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteFunctionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_function_async_invoke_config(self, request):
        """删除函数异步配置信息

        删除函数异步配置信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteFunctionAsyncInvokeConfig
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.DeleteFunctionAsyncInvokeConfigRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.DeleteFunctionAsyncInvokeConfigResponse`
        """
        return self._delete_function_async_invoke_config_with_http_info(request)

    def _delete_function_async_invoke_config_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'function_urn' in local_var_params:
            path_params['function_urn'] = local_var_params['function_urn']

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
            resource_path='/v2/{project_id}/fgs/functions/{function_urn}/async-invoke-config',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteFunctionAsyncInvokeConfigResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_function_trigger(self, request):
        """删除触发器

        删除触发器。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteFunctionTrigger
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.DeleteFunctionTriggerRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.DeleteFunctionTriggerResponse`
        """
        return self._delete_function_trigger_with_http_info(request)

    def _delete_function_trigger_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'function_urn' in local_var_params:
            path_params['function_urn'] = local_var_params['function_urn']
        if 'trigger_type_code' in local_var_params:
            path_params['trigger_type_code'] = local_var_params['trigger_type_code']
        if 'trigger_id' in local_var_params:
            path_params['trigger_id'] = local_var_params['trigger_id']

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
            resource_path='/v2/{project_id}/fgs/triggers/{function_urn}/{trigger_type_code}/{trigger_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteFunctionTriggerResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_tags(self, request):
        """删除资源标签

        删除资源标签。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteTags
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.DeleteTagsRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.DeleteTagsResponse`
        """
        return self._delete_tags_with_http_info(request)

    def _delete_tags_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_type' in local_var_params:
            path_params['resource_type'] = local_var_params['resource_type']
        if 'resource_id' in local_var_params:
            path_params['resource_id'] = local_var_params['resource_id']

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
            resource_path='/v2/{project_id}/{resource_type}/{resource_id}/tags/delete',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_version_alias(self, request):
        """删除函数版本别名

        删除函数版本别名。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteVersionAlias
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.DeleteVersionAliasRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.DeleteVersionAliasResponse`
        """
        return self._delete_version_alias_with_http_info(request)

    def _delete_version_alias_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'function_urn' in local_var_params:
            path_params['function_urn'] = local_var_params['function_urn']
        if 'alias_name' in local_var_params:
            path_params['alias_name'] = local_var_params['alias_name']

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
            resource_path='/v2/{project_id}/fgs/functions/{function_urn}/aliases/{alias_name}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteVersionAliasResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_vpc_endpoint(self, request):
        """删除下沉入口

        删除下沉入口。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteVpcEndpoint
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.DeleteVpcEndpointRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.DeleteVpcEndpointResponse`
        """
        return self._delete_vpc_endpoint_with_http_info(request)

    def _delete_vpc_endpoint_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'vpc_id' in local_var_params:
            path_params['vpc_id'] = local_var_params['vpc_id']
        if 'subnet_id' in local_var_params:
            path_params['subnet_id'] = local_var_params['subnet_id']

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
            resource_path='/v2/{project_id}/fgs/vpc-endpoint/{vpc_id}/{subnet_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteVpcEndpointResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def enable_lts_logs(self, request):
        """开通lts日志上报功能

        开通lts日志上报功能。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for EnableLtsLogs
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.EnableLtsLogsRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.EnableLtsLogsResponse`
        """
        return self._enable_lts_logs_with_http_info(request)

    def _enable_lts_logs_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

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
            resource_path='/v2/{project_id}/fgs/functions/enable-lts-logs',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='EnableLtsLogsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def export_function(self, request):
        """导出函数

        导出函数
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ExportFunction
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.ExportFunctionRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.ExportFunctionResponse`
        """
        return self._export_function_with_http_info(request)

    def _export_function_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'function_urn' in local_var_params:
            path_params['function_urn'] = local_var_params['function_urn']

        query_params = []
        if 'config' in local_var_params:
            query_params.append(('config', local_var_params['config']))
        if 'code' in local_var_params:
            query_params.append(('code', local_var_params['code']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))

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
            resource_path='/v2/{project_id}/fgs/functions/{function_urn}/export',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ExportFunctionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def import_function(self, request):
        """导入函数

        导入函数
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ImportFunction
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.ImportFunctionRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.ImportFunctionResponse`
        """
        return self._import_function_with_http_info(request)

    def _import_function_with_http_info(self, request):
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
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/fgs/functions/import',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ImportFunctionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def invoke_function(self, request):
        """同步执行函数

        同步调用指的是客户端请求需要明确等到响应结果，也就是说这样的请求必须得调用到用户的函数，并且等到调用完成才返回。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for InvokeFunction
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.InvokeFunctionRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.InvokeFunctionResponse`
        """
        return self._invoke_function_with_http_info(request)

    def _invoke_function_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'function_urn' in local_var_params:
            path_params['function_urn'] = local_var_params['function_urn']

        query_params = []

        header_params = {}
        if 'x_cff_log_type' in local_var_params:
            header_params['X-Cff-Log-Type'] = local_var_params['x_cff_log_type']
        if 'x_cff_request_version' in local_var_params:
            header_params['X-CFF-Request-Version'] = local_var_params['x_cff_request_version']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-Cff-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/fgs/functions/{function_urn}/invocations',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='InvokeFunctionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_active_async_invocations(self, request):
        """获取函数活跃异步调用请求列表

        获取函数异步调用活跃请求列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListActiveAsyncInvocations
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.ListActiveAsyncInvocationsRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.ListActiveAsyncInvocationsResponse`
        """
        return self._list_active_async_invocations_with_http_info(request)

    def _list_active_async_invocations_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'function_urn' in local_var_params:
            path_params['function_urn'] = local_var_params['function_urn']

        query_params = []
        if 'requests' in local_var_params:
            query_params.append(('requests', local_var_params['requests']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'query_begin_time' in local_var_params:
            query_params.append(('query_begin_time', local_var_params['query_begin_time']))
        if 'query_end_time' in local_var_params:
            query_params.append(('query_end_time', local_var_params['query_end_time']))

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
            resource_path='/v2/{project_id}/fgs/functions/{function_urn}/active-async-invocations',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListActiveAsyncInvocationsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_async_invocations(self, request):
        """获取函数异步调用请求列表

        获取函数异步调用请求列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAsyncInvocations
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.ListAsyncInvocationsRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.ListAsyncInvocationsResponse`
        """
        return self._list_async_invocations_with_http_info(request)

    def _list_async_invocations_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'function_urn' in local_var_params:
            path_params['function_urn'] = local_var_params['function_urn']

        query_params = []
        if 'request_id' in local_var_params:
            query_params.append(('request_id', local_var_params['request_id']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'query_begin_time' in local_var_params:
            query_params.append(('query_begin_time', local_var_params['query_begin_time']))
        if 'query_end_time' in local_var_params:
            query_params.append(('query_end_time', local_var_params['query_end_time']))

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
            resource_path='/v2/{project_id}/fgs/functions/{function_urn}/async-invocations',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListAsyncInvocationsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_dependencies(self, request):
        """获取依赖包列表

        获取依赖包列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListDependencies
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.ListDependenciesRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.ListDependenciesResponse`
        """
        return self._list_dependencies_with_http_info(request)

    def _list_dependencies_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'maxitems' in local_var_params:
            query_params.append(('maxitems', local_var_params['maxitems']))
        if 'ispublic' in local_var_params:
            query_params.append(('ispublic', local_var_params['ispublic']))
        if 'dependency_type' in local_var_params:
            query_params.append(('dependency_type', local_var_params['dependency_type']))
        if 'runtime' in local_var_params:
            query_params.append(('runtime', local_var_params['runtime']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
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
            resource_path='/v2/{project_id}/fgs/dependencies',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListDependenciesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_dependency_version(self, request):
        """获取依赖包版本列表

        获取依赖包版本列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListDependencyVersion
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.ListDependencyVersionRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.ListDependencyVersionResponse`
        """
        return self._list_dependency_version_with_http_info(request)

    def _list_dependency_version_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'depend_id' in local_var_params:
            path_params['depend_id'] = local_var_params['depend_id']

        query_params = []
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'maxitems' in local_var_params:
            query_params.append(('maxitems', local_var_params['maxitems']))

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
            resource_path='/v2/{project_id}/fgs/dependencies/{depend_id}/version',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListDependencyVersionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_events(self, request):
        """获取指定函数的测试事件列表

        获取指定函数的测试事件列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListEvents
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.ListEventsRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.ListEventsResponse`
        """
        return self._list_events_with_http_info(request)

    def _list_events_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'function_urn' in local_var_params:
            path_params['function_urn'] = local_var_params['function_urn']

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
            resource_path='/v2/{project_id}/fgs/functions/{function_urn}/events',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListEventsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_function_as_metric(self, request):
        """获取按指定指标排序的函数列表

        按指定指标排序的函数列表。
        
        默认统计按错误次数指标统计最近一天失败次数最多的前10个函数
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListFunctionAsMetric
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.ListFunctionAsMetricRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.ListFunctionAsMetricResponse`
        """
        return self._list_function_as_metric_with_http_info(request)

    def _list_function_as_metric_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
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
            resource_path='/v2/{project_id}/fgs/function/report',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListFunctionAsMetricResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_function_async_invoke_config(self, request):
        """获取函数异步配置列表

        获取指定函数所有版本的异步配置列表。。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListFunctionAsyncInvokeConfig
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.ListFunctionAsyncInvokeConfigRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.ListFunctionAsyncInvokeConfigResponse`
        """
        return self._list_function_async_invoke_config_with_http_info(request)

    def _list_function_async_invoke_config_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'function_urn' in local_var_params:
            path_params['function_urn'] = local_var_params['function_urn']

        query_params = []
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
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
            resource_path='/v2/{project_id}/fgs/functions/{function_urn}/async-invoke-configs',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListFunctionAsyncInvokeConfigResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_function_reserved_instances(self, request):
        """获取函数预留实例数量

        获取函数预留实例数量。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListFunctionReservedInstances
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.ListFunctionReservedInstancesRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.ListFunctionReservedInstancesResponse`
        """
        return self._list_function_reserved_instances_with_http_info(request)

    def _list_function_reserved_instances_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'urn' in local_var_params:
            query_params.append(('urn', local_var_params['urn']))

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
            resource_path='/v2/{project_id}/fgs/functions/reservedinstances',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListFunctionReservedInstancesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_function_statistics(self, request):
        """获取指定时间段的函数运行指标

        获取指定时间段的函数运行指标。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListFunctionStatistics
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.ListFunctionStatisticsRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.ListFunctionStatisticsResponse`
        """
        return self._list_function_statistics_with_http_info(request)

    def _list_function_statistics_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'func_urn' in local_var_params:
            path_params['func_urn'] = local_var_params['func_urn']
        if 'period' in local_var_params:
            path_params['period'] = local_var_params['period']

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
            resource_path='/v2/{project_id}/fgs/functions/{func_urn}/statistics/{period}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListFunctionStatisticsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_function_triggers(self, request):
        """获取指定函数的所有触发器

        获取指定函数的所有触发器设置。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListFunctionTriggers
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.ListFunctionTriggersRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.ListFunctionTriggersResponse`
        """
        return self._list_function_triggers_with_http_info(request)

    def _list_function_triggers_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'function_urn' in local_var_params:
            path_params['function_urn'] = local_var_params['function_urn']

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
            resource_path='/v2/{project_id}/fgs/triggers/{function_urn}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListFunctionTriggersResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_function_versions(self, request):
        """获取指定函数的版本列表

        获取指定函数的版本列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListFunctionVersions
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.ListFunctionVersionsRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.ListFunctionVersionsResponse`
        """
        return self._list_function_versions_with_http_info(request)

    def _list_function_versions_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'function_urn' in local_var_params:
            path_params['function_urn'] = local_var_params['function_urn']

        query_params = []
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'maxitems' in local_var_params:
            query_params.append(('maxitems', local_var_params['maxitems']))

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
            resource_path='/v2/{project_id}/fgs/functions/{function_urn}/versions',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListFunctionVersionsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_functions(self, request):
        """获取函数列表

        获取函数列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListFunctions
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.ListFunctionsRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.ListFunctionsResponse`
        """
        return self._list_functions_with_http_info(request)

    def _list_functions_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'maxitems' in local_var_params:
            query_params.append(('maxitems', local_var_params['maxitems']))
        if 'package_name' in local_var_params:
            query_params.append(('package_name', local_var_params['package_name']))

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
            resource_path='/v2/{project_id}/fgs/functions',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListFunctionsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_quotas(self, request):
        """查询租户配额

        查询租户配额
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListQuotas
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.ListQuotasRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.ListQuotasResponse`
        """
        return self._list_quotas_with_http_info(request)

    def _list_quotas_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

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
            resource_path='/v2/{project_id}/fgs/quotas',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListQuotasResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_reserved_instance_configs(self, request):
        """获取函数预留实例配置列表

        获取函数预留实例配置列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListReservedInstanceConfigs
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.ListReservedInstanceConfigsRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.ListReservedInstanceConfigsResponse`
        """
        return self._list_reserved_instance_configs_with_http_info(request)

    def _list_reserved_instance_configs_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'function_urn' in local_var_params:
            query_params.append(('function_urn', local_var_params['function_urn']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
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
            resource_path='/v2/{project_id}/fgs/functions/reservedinstanceconfigs',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListReservedInstanceConfigsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_statistics(self, request):
        """租户函数统计信息

        租户函数统计信息。
        
        返回三类的统计信息，函数格式和大小使用情况包括配额和使用量，流量报告。
        通过查询参数filter可以进行过滤，查询参数period可以指定返回的时间段。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListStatistics
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.ListStatisticsRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.ListStatisticsResponse`
        """
        return self._list_statistics_with_http_info(request)

    def _list_statistics_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'filter' in local_var_params:
            query_params.append(('filter', local_var_params['filter']))
        if 'period' in local_var_params:
            query_params.append(('period', local_var_params['period']))
        if 'option' in local_var_params:
            query_params.append(('option', local_var_params['option']))

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
            resource_path='/v2/{project_id}/fgs/functions/statistics',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListStatisticsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_version_aliases(self, request):
        """获取指定函数所有版本别名列表

        获取函数版本别名列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListVersionAliases
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.ListVersionAliasesRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.ListVersionAliasesResponse`
        """
        return self._list_version_aliases_with_http_info(request)

    def _list_version_aliases_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'function_urn' in local_var_params:
            path_params['function_urn'] = local_var_params['function_urn']

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
            resource_path='/v2/{project_id}/fgs/functions/{function_urn}/aliases',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListVersionAliasesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_workflow(self, request):
        """查询函数流

        查询函数流
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListWorkflow
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.ListWorkflowRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.ListWorkflowResponse`
        """
        return self._list_workflow_with_http_info(request)

    def _list_workflow_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'workflow_name' in local_var_params:
            query_params.append(('workflow_name', local_var_params['workflow_name']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'enterprise_project' in local_var_params:
            query_params.append(('enterprise_project', local_var_params['enterprise_project']))
        if 'mode' in local_var_params:
            query_params.append(('mode', local_var_params['mode']))

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
            resource_path='/v2/{project_id}/fgs/workflows',
            method='GET',
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

    def list_workflow_executions(self, request):
        """获取指定函数流执行实例列表

        获取指定函数流执行实例列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListWorkflowExecutions
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.ListWorkflowExecutionsRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.ListWorkflowExecutionsResponse`
        """
        return self._list_workflow_executions_with_http_info(request)

    def _list_workflow_executions_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workflow_id' in local_var_params:
            path_params['workflow_id'] = local_var_params['workflow_id']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))

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
            resource_path='/v2/{project_id}/fgs/workflows/{workflow_id}/executions',
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

    def retry_work_flow(self, request):
        """重试函数流

        重试函数流
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RetryWorkFlow
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.RetryWorkFlowRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.RetryWorkFlowResponse`
        """
        return self._retry_work_flow_with_http_info(request)

    def _retry_work_flow_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/fgs/workflows/{workflow_id}/executions/{execution_id}/retry',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RetryWorkFlowResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_dependcy(self, request):
        """获取指定依赖包

        获取指定依赖包
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDependcy
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.ShowDependcyRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.ShowDependcyResponse`
        """
        return self._show_dependcy_with_http_info(request)

    def _show_dependcy_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'depend_id' in local_var_params:
            path_params['depend_id'] = local_var_params['depend_id']

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
            resource_path='/v2/{project_id}/fgs/dependencies/{depend_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowDependcyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_dependency_version(self, request):
        """获取依赖包版本详情

        获取依赖包版本详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDependencyVersion
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.ShowDependencyVersionRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.ShowDependencyVersionResponse`
        """
        return self._show_dependency_version_with_http_info(request)

    def _show_dependency_version_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'depend_id' in local_var_params:
            path_params['depend_id'] = local_var_params['depend_id']
        if 'version' in local_var_params:
            path_params['version'] = local_var_params['version']

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
            resource_path='/v2/{project_id}/fgs/dependencies/{depend_id}/version/{version}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowDependencyVersionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_event(self, request):
        """获取测试事件详细信息

        获取测试事件详细信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowEvent
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.ShowEventRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.ShowEventResponse`
        """
        return self._show_event_with_http_info(request)

    def _show_event_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'function_urn' in local_var_params:
            path_params['function_urn'] = local_var_params['function_urn']
        if 'event_id' in local_var_params:
            path_params['event_id'] = local_var_params['event_id']

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
            resource_path='/v2/{project_id}/fgs/functions/{function_urn}/events/{event_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowEventResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_func_snapshot_state(self, request):
        """查询函数快照制作状态

        查询函数快照制作状态。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowFuncSnapshotState
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.ShowFuncSnapshotStateRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.ShowFuncSnapshotStateResponse`
        """
        return self._show_func_snapshot_state_with_http_info(request)

    def _show_func_snapshot_state_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'function_urn' in local_var_params:
            path_params['function_urn'] = local_var_params['function_urn']
        if 'action' in local_var_params:
            path_params['action'] = local_var_params['action']

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
            resource_path='/v2/{project_id}/fgs/functions/{function_urn}/snapshots/{action}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowFuncSnapshotStateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_function_async_invoke_config(self, request):
        """获取函数异步配置信息

        获取指定函数某一版本的异步配置信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowFunctionAsyncInvokeConfig
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.ShowFunctionAsyncInvokeConfigRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.ShowFunctionAsyncInvokeConfigResponse`
        """
        return self._show_function_async_invoke_config_with_http_info(request)

    def _show_function_async_invoke_config_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'function_urn' in local_var_params:
            path_params['function_urn'] = local_var_params['function_urn']

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
            resource_path='/v2/{project_id}/fgs/functions/{function_urn}/async-invoke-config',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowFunctionAsyncInvokeConfigResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_function_code(self, request):
        """获取指定函数代码

        获取指定函数的代码。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowFunctionCode
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.ShowFunctionCodeRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.ShowFunctionCodeResponse`
        """
        return self._show_function_code_with_http_info(request)

    def _show_function_code_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'function_urn' in local_var_params:
            path_params['function_urn'] = local_var_params['function_urn']

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
            resource_path='/v2/{project_id}/fgs/functions/{function_urn}/code',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowFunctionCodeResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_function_config(self, request):
        """获取函数的metadata

        获取指定函数的metadata。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowFunctionConfig
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.ShowFunctionConfigRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.ShowFunctionConfigResponse`
        """
        return self._show_function_config_with_http_info(request)

    def _show_function_config_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'function_urn' in local_var_params:
            path_params['function_urn'] = local_var_params['function_urn']

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
            resource_path='/v2/{project_id}/fgs/functions/{function_urn}/config',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowFunctionConfigResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_function_trigger(self, request):
        """获取指定触发器的信息

        获取特定触发器的信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowFunctionTrigger
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.ShowFunctionTriggerRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.ShowFunctionTriggerResponse`
        """
        return self._show_function_trigger_with_http_info(request)

    def _show_function_trigger_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'function_urn' in local_var_params:
            path_params['function_urn'] = local_var_params['function_urn']
        if 'trigger_type_code' in local_var_params:
            path_params['trigger_type_code'] = local_var_params['trigger_type_code']
        if 'trigger_id' in local_var_params:
            path_params['trigger_id'] = local_var_params['trigger_id']

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
            resource_path='/v2/{project_id}/fgs/triggers/{function_urn}/{trigger_type_code}/{trigger_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowFunctionTriggerResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_lts_log_details(self, request):
        """获取指定函数的lts日志组日志流配置

        获取指定函数的lts日志组日志流配置。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowLtsLogDetails
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.ShowLtsLogDetailsRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.ShowLtsLogDetailsResponse`
        """
        return self._show_lts_log_details_with_http_info(request)

    def _show_lts_log_details_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'function_urn' in local_var_params:
            path_params['function_urn'] = local_var_params['function_urn']

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
            resource_path='/v2/{project_id}/fgs/functions/{function_urn}/lts-log-detail',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowLtsLogDetailsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_project_tags_list(self, request):
        """查询资源标签

        查询资源标签。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowProjectTagsList
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.ShowProjectTagsListRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.ShowProjectTagsListResponse`
        """
        return self._show_project_tags_list_with_http_info(request)

    def _show_project_tags_list_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_type' in local_var_params:
            path_params['resource_type'] = local_var_params['resource_type']

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
            resource_path='/v2/{project_id}/{resource_type}/tags',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowProjectTagsListResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_res_instance_info(self, request):
        """查询资源实例

        查询资源实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowResInstanceInfo
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.ShowResInstanceInfoRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.ShowResInstanceInfoResponse`
        """
        return self._show_res_instance_info_with_http_info(request)

    def _show_res_instance_info_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_type' in local_var_params:
            path_params['resource_type'] = local_var_params['resource_type']
        if 'action' in local_var_params:
            path_params['action'] = local_var_params['action']

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
            resource_path='/v2/{project_id}/{resource_type}/resource-instances/{action}',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowResInstanceInfoResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_tenant_metric(self, request):
        """获取函数流指标

        获取函数流指标
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowTenantMetric
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.ShowTenantMetricRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.ShowTenantMetricResponse`
        """
        return self._show_tenant_metric_with_http_info(request)

    def _show_tenant_metric_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'period' in local_var_params:
            query_params.append(('period', local_var_params['period']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'metric_type' in local_var_params:
            query_params.append(('metric_type', local_var_params['metric_type']))

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
            resource_path='/v2/{project_id}/fgs/workflow-statistic',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowTenantMetricResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_tracing(self, request):
        """获取函数调用链配置

        获取函数调用链配置
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowTracing
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.ShowTracingRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.ShowTracingResponse`
        """
        return self._show_tracing_with_http_info(request)

    def _show_tracing_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'function_urn' in local_var_params:
            path_params['function_urn'] = local_var_params['function_urn']

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
            resource_path='/v2/{project_id}/fgs/functions/{function_urn}/tracing',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowTracingResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_version_alias(self, request):
        """获取函数版本的指定别名信息

        获取函数指定的版本别名信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowVersionAlias
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.ShowVersionAliasRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.ShowVersionAliasResponse`
        """
        return self._show_version_alias_with_http_info(request)

    def _show_version_alias_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'function_urn' in local_var_params:
            path_params['function_urn'] = local_var_params['function_urn']
        if 'alias_name' in local_var_params:
            path_params['alias_name'] = local_var_params['alias_name']

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
            resource_path='/v2/{project_id}/fgs/functions/{function_urn}/aliases/{alias_name}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowVersionAliasResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_work_flow(self, request):
        """获取指定函数流实例的元数据

        获取指定函数流实例的元数据
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowWorkFlow
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.ShowWorkFlowRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.ShowWorkFlowResponse`
        """
        return self._show_work_flow_with_http_info(request)

    def _show_work_flow_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
            resource_path='/v2/{project_id}/fgs/workflows/{workflow_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowWorkFlowResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_work_flow_metric(self, request):
        """获取指定函数流指标

        获取指定函数流指标
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowWorkFlowMetric
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.ShowWorkFlowMetricRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.ShowWorkFlowMetricResponse`
        """
        return self._show_work_flow_metric_with_http_info(request)

    def _show_work_flow_metric_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workflow_urn' in local_var_params:
            path_params['workflow_urn'] = local_var_params['workflow_urn']

        query_params = []
        if 'period' in local_var_params:
            query_params.append(('period', local_var_params['period']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))

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
            resource_path='/v2/{project_id}/fgs/workflow-statistic/{workflow_urn}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowWorkFlowMetricResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_workflow_execution(self, request):
        """获取指定函数流执行实例

        获取指定函数流执行实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowWorkflowExecution
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.ShowWorkflowExecutionRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.ShowWorkflowExecutionResponse`
        """
        return self._show_workflow_execution_with_http_info(request)

    def _show_workflow_execution_with_http_info(self, request):
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
        if 'x_get_workflow_full_history_data' in local_var_params:
            header_params['X-Get-Workflow-Full-History-Data'] = local_var_params['x_get_workflow_full_history_data']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/fgs/workflows/{workflow_id}/executions/{execution_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowWorkflowExecutionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_workflow_execution_for_page(self, request):
        """分页获取指定函数流执行实例列表

        分页获取指定函数流执行实例列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowWorkflowExecutionForPage
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.ShowWorkflowExecutionForPageRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.ShowWorkflowExecutionForPageResponse`
        """
        return self._show_workflow_execution_for_page_with_http_info(request)

    def _show_workflow_execution_for_page_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workflow_id' in local_var_params:
            path_params['workflow_id'] = local_var_params['workflow_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))

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
            resource_path='/v2/{project_id}/fgs/workflows/{workflow_id}/executions-history',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowWorkflowExecutionForPageResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def start_sync_workflow_execution(self, request):
        """同步执行函数流

        以同步执行方式启动函数流（仅快速模式函数流支持）
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for StartSyncWorkflowExecution
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.StartSyncWorkflowExecutionRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.StartSyncWorkflowExecutionResponse`
        """
        return self._start_sync_workflow_execution_with_http_info(request)

    def _start_sync_workflow_execution_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workflow_id' in local_var_params:
            path_params['workflow_id'] = local_var_params['workflow_id']

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
            resource_path='/v2/{project_id}/fgs/workflows/{workflow_id}/sync-executions',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='StartSyncWorkflowExecutionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def start_workflow_execution(self, request):
        """开始执行函数流

        以异步执行方式启动函数流
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for StartWorkflowExecution
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.StartWorkflowExecutionRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.StartWorkflowExecutionResponse`
        """
        return self._start_workflow_execution_with_http_info(request)

    def _start_workflow_execution_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workflow_id' in local_var_params:
            path_params['workflow_id'] = local_var_params['workflow_id']

        query_params = []

        header_params = {}
        if 'x_create_time' in local_var_params:
            header_params['X-Create-Time'] = local_var_params['x_create_time']
        if 'x_workflow_run_id' in local_var_params:
            header_params['X-WorkflowRun-ID'] = local_var_params['x_workflow_run_id']
        if 'x_workflow_run_merge_fn_parameters' in local_var_params:
            header_params['X-WorkflowRun-MergeFnParameters'] = local_var_params['x_workflow_run_merge_fn_parameters']

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
            resource_path='/v2/{project_id}/fgs/workflows/{workflow_id}/executions',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='StartWorkflowExecutionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def stop_work_flow(self, request):
        """停止函数流

        停止函数流
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for StopWorkFlow
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.StopWorkFlowRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.StopWorkFlowResponse`
        """
        return self._stop_work_flow_with_http_info(request)

    def _stop_work_flow_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/fgs/workflows/{workflow_id}/executions/{execution_id}/terminate',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='StopWorkFlowResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_dependcy(self, request):
        """更新指定依赖包

        更新指定依赖包
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateDependcy
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.UpdateDependcyRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.UpdateDependcyResponse`
        """
        return self._update_dependcy_with_http_info(request)

    def _update_dependcy_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'depend_id' in local_var_params:
            path_params['depend_id'] = local_var_params['depend_id']

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
            resource_path='/v2/{project_id}/fgs/dependencies/{depend_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateDependcyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_event(self, request):
        """更新测试事件详细信息

        更新测试事件详细信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateEvent
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.UpdateEventRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.UpdateEventResponse`
        """
        return self._update_event_with_http_info(request)

    def _update_event_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'function_urn' in local_var_params:
            path_params['function_urn'] = local_var_params['function_urn']
        if 'event_id' in local_var_params:
            path_params['event_id'] = local_var_params['event_id']

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
            resource_path='/v2/{project_id}/fgs/functions/{function_urn}/events/{event_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateEventResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_func_snapshot(self, request):
        """禁用/启动函数快照

        禁用/启动函数快照
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateFuncSnapshot
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.UpdateFuncSnapshotRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.UpdateFuncSnapshotResponse`
        """
        return self._update_func_snapshot_with_http_info(request)

    def _update_func_snapshot_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'action' in local_var_params:
            path_params['action'] = local_var_params['action']
        if 'function_urn' in local_var_params:
            path_params['function_urn'] = local_var_params['function_urn']

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
            resource_path='/v2/{project_id}/fgs/functions/{function_urn}/snapshots/{action}',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateFuncSnapshotResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_function_async_invoke_config(self, request):
        """设置函数异步配置信息

        设置函数异步配置信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateFunctionAsyncInvokeConfig
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.UpdateFunctionAsyncInvokeConfigRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.UpdateFunctionAsyncInvokeConfigResponse`
        """
        return self._update_function_async_invoke_config_with_http_info(request)

    def _update_function_async_invoke_config_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'function_urn' in local_var_params:
            path_params['function_urn'] = local_var_params['function_urn']

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
            resource_path='/v2/{project_id}/fgs/functions/{function_urn}/async-invoke-config',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateFunctionAsyncInvokeConfigResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_function_code(self, request):
        """修改函数代码

        修改指定的函数的代码。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateFunctionCode
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.UpdateFunctionCodeRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.UpdateFunctionCodeResponse`
        """
        return self._update_function_code_with_http_info(request)

    def _update_function_code_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'function_urn' in local_var_params:
            path_params['function_urn'] = local_var_params['function_urn']

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
            resource_path='/v2/{project_id}/fgs/functions/{function_urn}/code',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateFunctionCodeResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_function_config(self, request):
        """修改函数的metadata信息

        修改指定的函数的metadata信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateFunctionConfig
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.UpdateFunctionConfigRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.UpdateFunctionConfigResponse`
        """
        return self._update_function_config_with_http_info(request)

    def _update_function_config_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'function_urn' in local_var_params:
            path_params['function_urn'] = local_var_params['function_urn']

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
            resource_path='/v2/{project_id}/fgs/functions/{function_urn}/config',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateFunctionConfigResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_function_max_instance_config(self, request):
        """更新函数最大实例数

        更新函数最大实例数
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateFunctionMaxInstanceConfig
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.UpdateFunctionMaxInstanceConfigRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.UpdateFunctionMaxInstanceConfigResponse`
        """
        return self._update_function_max_instance_config_with_http_info(request)

    def _update_function_max_instance_config_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'function_urn' in local_var_params:
            path_params['function_urn'] = local_var_params['function_urn']

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
            resource_path='/v2/{project_id}/fgs/functions/{function_urn}/config-max-instance',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateFunctionMaxInstanceConfigResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_function_reserved_instances_count(self, request):
        """修改函数预留实例数量

        修改函数预留实例数量。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateFunctionReservedInstancesCount
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.UpdateFunctionReservedInstancesCountRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.UpdateFunctionReservedInstancesCountResponse`
        """
        return self._update_function_reserved_instances_count_with_http_info(request)

    def _update_function_reserved_instances_count_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'function_urn' in local_var_params:
            path_params['function_urn'] = local_var_params['function_urn']

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
            resource_path='/v2/{project_id}/fgs/functions/{function_urn}/reservedinstances',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateFunctionReservedInstancesCountResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_tracing(self, request):
        """修改函数调用链配置

        修改函数调用链配置,开通/修改传入aksk，关闭aksk传空
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateTracing
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.UpdateTracingRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.UpdateTracingResponse`
        """
        return self._update_tracing_with_http_info(request)

    def _update_tracing_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'function_urn' in local_var_params:
            path_params['function_urn'] = local_var_params['function_urn']

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
            resource_path='/v2/{project_id}/fgs/functions/{function_urn}/tracing',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateTracingResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_trigger(self, request):
        """更新触发器

        更新触发器
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateTrigger
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.UpdateTriggerRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.UpdateTriggerResponse`
        """
        return self._update_trigger_with_http_info(request)

    def _update_trigger_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'function_urn' in local_var_params:
            path_params['function_urn'] = local_var_params['function_urn']
        if 'trigger_type_code' in local_var_params:
            path_params['trigger_type_code'] = local_var_params['trigger_type_code']
        if 'trigger_id' in local_var_params:
            path_params['trigger_id'] = local_var_params['trigger_id']

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
            resource_path='/v2/{project_id}/fgs/triggers/{function_urn}/{trigger_type_code}/{trigger_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateTriggerResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_version_alias(self, request):
        """修改函数版本别名信息

        修改函数版本别名信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateVersionAlias
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.UpdateVersionAliasRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.UpdateVersionAliasResponse`
        """
        return self._update_version_alias_with_http_info(request)

    def _update_version_alias_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'function_urn' in local_var_params:
            path_params['function_urn'] = local_var_params['function_urn']
        if 'alias_name' in local_var_params:
            path_params['alias_name'] = local_var_params['alias_name']

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
            resource_path='/v2/{project_id}/fgs/functions/{function_urn}/aliases/{alias_name}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateVersionAliasResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_work_flow(self, request):
        """修改指定函数流实例的元数据

        修改指定函数流实例的元数据
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateWorkFlow
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.UpdateWorkFlowRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.UpdateWorkFlowResponse`
        """
        return self._update_work_flow_with_http_info(request)

    def _update_work_flow_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workflow_id' in local_var_params:
            path_params['workflow_id'] = local_var_params['workflow_id']

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
            resource_path='/v2/{project_id}/fgs/workflows/{workflow_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateWorkFlowResponse',
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

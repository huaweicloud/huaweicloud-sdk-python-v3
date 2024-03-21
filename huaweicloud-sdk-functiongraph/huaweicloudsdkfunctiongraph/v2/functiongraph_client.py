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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkfunctiongraph'")


class FunctionGraphClient(Client):
    def __init__(self):
        super(FunctionGraphClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkfunctiongraph.v2.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "FunctionGraphClient":
                raise TypeError("client type error, support client type is FunctionGraphClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def async_invoke_function(self, request):
        """异步执行函数

        异步执行函数。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AsyncInvokeFunction
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.AsyncInvokeFunctionRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.AsyncInvokeFunctionResponse`
        """
        http_info = self._async_invoke_function_http_info(request)
        return self._call_api(**http_info)

    def async_invoke_function_invoker(self, request):
        http_info = self._async_invoke_function_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _async_invoke_function_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/fgs/functions/{function_urn}/invocations-async",
            "request_type": request.__class__.__name__,
            "response_type": "AsyncInvokeFunctionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'function_urn' in local_var_params:
            path_params['function_urn'] = local_var_params['function_urn']

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
        http_info = self._batch_delete_function_triggers_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_function_triggers_invoker(self, request):
        http_info = self._batch_delete_function_triggers_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_delete_function_triggers_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/fgs/triggers/{function_urn}",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeleteFunctionTriggersResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'function_urn' in local_var_params:
            path_params['function_urn'] = local_var_params['function_urn']

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

    def batch_delete_workflows(self, request):
        """删除函数流

        删除函数流
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchDeleteWorkflows
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.BatchDeleteWorkflowsRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.BatchDeleteWorkflowsResponse`
        """
        http_info = self._batch_delete_workflows_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_workflows_invoker(self, request):
        http_info = self._batch_delete_workflows_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_delete_workflows_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/fgs/workflows",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeleteWorkflowsResponse"
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

    def cancel_async_invocation(self, request):
        """停止函数异步调用请求

        -| 当前仅支持参数recursive为false且force为true的函数。 在1：N的函数做并发异步调用的场景下调用停止异步请求接口时，同一函数实例同时在执行的其他请求也会被一并停止并返回4208 function invocation canceled
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CancelAsyncInvocation
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.CancelAsyncInvocationRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.CancelAsyncInvocationResponse`
        """
        http_info = self._cancel_async_invocation_http_info(request)
        return self._call_api(**http_info)

    def cancel_async_invocation_invoker(self, request):
        http_info = self._cancel_async_invocation_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _cancel_async_invocation_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/fgs/functions/{function_urn}/cancel",
            "request_type": request.__class__.__name__,
            "response_type": "CancelAsyncInvocationResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'function_urn' in local_var_params:
            path_params['function_urn'] = local_var_params['function_urn']

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

    def create_callback_workflow(self, request):
        """回调工作流

        回调工作流
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateCallbackWorkflow
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.CreateCallbackWorkflowRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.CreateCallbackWorkflowResponse`
        """
        http_info = self._create_callback_workflow_http_info(request)
        return self._call_api(**http_info)

    def create_callback_workflow_invoker(self, request):
        http_info = self._create_callback_workflow_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_callback_workflow_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/fgs/workflows/{workflow_id}/callback",
            "request_type": request.__class__.__name__,
            "response_type": "CreateCallbackWorkflowResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workflow_id' in local_var_params:
            path_params['workflow_id'] = local_var_params['workflow_id']

        query_params = []

        header_params = {}
        if 'x_workflow_run_id' in local_var_params:
            header_params['X-Workflow-Run-Id'] = local_var_params['x_workflow_run_id']
        if 'x_workflow_state_id' in local_var_params:
            header_params['X-Workflow-State-Id'] = local_var_params['x_workflow_state_id']

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

    def create_dependency_version(self, request):
        """创建依赖包版本

        创建依赖包版本
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateDependencyVersion
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.CreateDependencyVersionRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.CreateDependencyVersionResponse`
        """
        http_info = self._create_dependency_version_http_info(request)
        return self._call_api(**http_info)

    def create_dependency_version_invoker(self, request):
        http_info = self._create_dependency_version_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_dependency_version_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/fgs/dependencies/version",
            "request_type": request.__class__.__name__,
            "response_type": "CreateDependencyVersionResponse"
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

    def create_event(self, request):
        """创建测试事件

        创建测试事件
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateEvent
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.CreateEventRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.CreateEventResponse`
        """
        http_info = self._create_event_http_info(request)
        return self._call_api(**http_info)

    def create_event_invoker(self, request):
        http_info = self._create_event_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_event_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/fgs/functions/{function_urn}/events",
            "request_type": request.__class__.__name__,
            "response_type": "CreateEventResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'function_urn' in local_var_params:
            path_params['function_urn'] = local_var_params['function_urn']

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

    def create_function(self, request):
        """创建函数

        创建指定的函数。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateFunction
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.CreateFunctionRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.CreateFunctionResponse`
        """
        http_info = self._create_function_http_info(request)
        return self._call_api(**http_info)

    def create_function_invoker(self, request):
        http_info = self._create_function_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_function_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/fgs/functions",
            "request_type": request.__class__.__name__,
            "response_type": "CreateFunctionResponse"
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

    def create_function_app(self, request):
        """创建应用程序

        创建应用程序（该功能目前仅支持华北-北京四、华东-上海一）
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateFunctionApp
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.CreateFunctionAppRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.CreateFunctionAppResponse`
        """
        http_info = self._create_function_app_http_info(request)
        return self._call_api(**http_info)

    def create_function_app_invoker(self, request):
        http_info = self._create_function_app_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_function_app_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/fgs/applications",
            "request_type": request.__class__.__name__,
            "response_type": "CreateFunctionAppResponse"
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
        http_info = self._create_function_trigger_http_info(request)
        return self._call_api(**http_info)

    def create_function_trigger_invoker(self, request):
        http_info = self._create_function_trigger_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_function_trigger_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/fgs/triggers/{function_urn}",
            "request_type": request.__class__.__name__,
            "response_type": "CreateFunctionTriggerResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'function_urn' in local_var_params:
            path_params['function_urn'] = local_var_params['function_urn']

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

    def create_function_version(self, request):
        """发布函数版本

        发布函数版本。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateFunctionVersion
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.CreateFunctionVersionRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.CreateFunctionVersionResponse`
        """
        http_info = self._create_function_version_http_info(request)
        return self._call_api(**http_info)

    def create_function_version_invoker(self, request):
        http_info = self._create_function_version_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_function_version_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/fgs/functions/{function_urn}/versions",
            "request_type": request.__class__.__name__,
            "response_type": "CreateFunctionVersionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'function_urn' in local_var_params:
            path_params['function_urn'] = local_var_params['function_urn']

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

    def create_tags(self, request):
        """创建资源标签

        创建资源标签。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateTags
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.CreateTagsRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.CreateTagsResponse`
        """
        http_info = self._create_tags_http_info(request)
        return self._call_api(**http_info)

    def create_tags_invoker(self, request):
        http_info = self._create_tags_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_tags_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/{resource_type}/{resource_id}/tags/create",
            "request_type": request.__class__.__name__,
            "response_type": "CreateTagsResponse"
            }

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

    def create_version_alias(self, request):
        """创建函数版本别名

        创建函数灰度版本别名。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateVersionAlias
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.CreateVersionAliasRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.CreateVersionAliasResponse`
        """
        http_info = self._create_version_alias_http_info(request)
        return self._call_api(**http_info)

    def create_version_alias_invoker(self, request):
        http_info = self._create_version_alias_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_version_alias_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/fgs/functions/{function_urn}/aliases",
            "request_type": request.__class__.__name__,
            "response_type": "CreateVersionAliasResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'function_urn' in local_var_params:
            path_params['function_urn'] = local_var_params['function_urn']

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

    def create_vpc_endpoint(self, request):
        """创建下沉入口

        创建下沉入口。（该功能目前仅支持华北-北京四、华东-上海一、华东-上海二、西南-贵阳一）
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateVpcEndpoint
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.CreateVpcEndpointRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.CreateVpcEndpointResponse`
        """
        http_info = self._create_vpc_endpoint_http_info(request)
        return self._call_api(**http_info)

    def create_vpc_endpoint_invoker(self, request):
        http_info = self._create_vpc_endpoint_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_vpc_endpoint_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/fgs/vpc-endpoint",
            "request_type": request.__class__.__name__,
            "response_type": "CreateVpcEndpointResponse"
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

    def create_workflow(self, request):
        """创建函数流

        创建函数流
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateWorkflow
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.CreateWorkflowRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.CreateWorkflowResponse`
        """
        http_info = self._create_workflow_http_info(request)
        return self._call_api(**http_info)

    def create_workflow_invoker(self, request):
        http_info = self._create_workflow_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_workflow_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/fgs/workflows",
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

    def delete_dependency_version(self, request):
        """删除依赖包版本

        删除依赖包版本
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteDependencyVersion
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.DeleteDependencyVersionRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.DeleteDependencyVersionResponse`
        """
        http_info = self._delete_dependency_version_http_info(request)
        return self._call_api(**http_info)

    def delete_dependency_version_invoker(self, request):
        http_info = self._delete_dependency_version_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_dependency_version_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/fgs/dependencies/{depend_id}/version/{version}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteDependencyVersionResponse"
            }

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

    def delete_event(self, request):
        """删除指定测试事件

        删除指定测试事件
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteEvent
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.DeleteEventRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.DeleteEventResponse`
        """
        http_info = self._delete_event_http_info(request)
        return self._call_api(**http_info)

    def delete_event_invoker(self, request):
        http_info = self._delete_event_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_event_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/fgs/functions/{function_urn}/events/{event_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteEventResponse"
            }

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
        http_info = self._delete_function_http_info(request)
        return self._call_api(**http_info)

    def delete_function_invoker(self, request):
        http_info = self._delete_function_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_function_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/fgs/functions/{function_urn}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteFunctionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'function_urn' in local_var_params:
            path_params['function_urn'] = local_var_params['function_urn']

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

    def delete_function_app(self, request):
        """删除应用程序

        删除应用程序（该功能目前仅支持华北-北京四、华东-上海一）
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteFunctionApp
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.DeleteFunctionAppRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.DeleteFunctionAppResponse`
        """
        http_info = self._delete_function_app_http_info(request)
        return self._call_api(**http_info)

    def delete_function_app_invoker(self, request):
        http_info = self._delete_function_app_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_function_app_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/fgs/applications/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteFunctionAppResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

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

    def delete_function_async_invoke_config(self, request):
        """删除函数异步配置信息

        删除函数异步配置信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteFunctionAsyncInvokeConfig
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.DeleteFunctionAsyncInvokeConfigRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.DeleteFunctionAsyncInvokeConfigResponse`
        """
        http_info = self._delete_function_async_invoke_config_http_info(request)
        return self._call_api(**http_info)

    def delete_function_async_invoke_config_invoker(self, request):
        http_info = self._delete_function_async_invoke_config_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_function_async_invoke_config_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/fgs/functions/{function_urn}/async-invoke-config",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteFunctionAsyncInvokeConfigResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'function_urn' in local_var_params:
            path_params['function_urn'] = local_var_params['function_urn']

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

    def delete_function_trigger(self, request):
        """删除触发器

        删除触发器。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteFunctionTrigger
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.DeleteFunctionTriggerRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.DeleteFunctionTriggerResponse`
        """
        http_info = self._delete_function_trigger_http_info(request)
        return self._call_api(**http_info)

    def delete_function_trigger_invoker(self, request):
        http_info = self._delete_function_trigger_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_function_trigger_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/fgs/triggers/{function_urn}/{trigger_type_code}/{trigger_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteFunctionTriggerResponse"
            }

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

    def delete_tags(self, request):
        """删除资源标签

        删除资源标签。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteTags
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.DeleteTagsRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.DeleteTagsResponse`
        """
        http_info = self._delete_tags_http_info(request)
        return self._call_api(**http_info)

    def delete_tags_invoker(self, request):
        http_info = self._delete_tags_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_tags_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/{resource_type}/{resource_id}/tags/delete",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteTagsResponse"
            }

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

    def delete_version_alias(self, request):
        """删除函数版本别名

        删除函数版本别名。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteVersionAlias
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.DeleteVersionAliasRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.DeleteVersionAliasResponse`
        """
        http_info = self._delete_version_alias_http_info(request)
        return self._call_api(**http_info)

    def delete_version_alias_invoker(self, request):
        http_info = self._delete_version_alias_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_version_alias_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/fgs/functions/{function_urn}/aliases/{alias_name}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteVersionAliasResponse"
            }

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

    def delete_vpc_endpoint(self, request):
        """删除下沉入口

        删除下沉入口。（该功能目前仅支持华北-北京四、华东-上海一、华东-上海二、西南-贵阳一）
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteVpcEndpoint
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.DeleteVpcEndpointRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.DeleteVpcEndpointResponse`
        """
        http_info = self._delete_vpc_endpoint_http_info(request)
        return self._call_api(**http_info)

    def delete_vpc_endpoint_invoker(self, request):
        http_info = self._delete_vpc_endpoint_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_vpc_endpoint_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/fgs/vpc-endpoint/{vpc_id}/{subnet_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteVpcEndpointResponse"
            }

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

    def enable_async_status_log(self, request):
        """允许异步状态通知

        允许异步状态通知。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for EnableAsyncStatusLog
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.EnableAsyncStatusLogRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.EnableAsyncStatusLogResponse`
        """
        http_info = self._enable_async_status_log_http_info(request)
        return self._call_api(**http_info)

    def enable_async_status_log_invoker(self, request):
        http_info = self._enable_async_status_log_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _enable_async_status_log_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/fgs/functions/enable-async-status-logs",
            "request_type": request.__class__.__name__,
            "response_type": "EnableAsyncStatusLogResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

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

    def enable_lts_logs(self, request):
        """开通lts日志上报功能

        开通lts日志上报功能。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for EnableLtsLogs
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.EnableLtsLogsRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.EnableLtsLogsResponse`
        """
        http_info = self._enable_lts_logs_http_info(request)
        return self._call_api(**http_info)

    def enable_lts_logs_invoker(self, request):
        http_info = self._enable_lts_logs_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _enable_lts_logs_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/fgs/functions/enable-lts-logs",
            "request_type": request.__class__.__name__,
            "response_type": "EnableLtsLogsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

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

    def export_function(self, request):
        """导出函数

        导出函数
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ExportFunction
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.ExportFunctionRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.ExportFunctionResponse`
        """
        http_info = self._export_function_http_info(request)
        return self._call_api(**http_info)

    def export_function_invoker(self, request):
        http_info = self._export_function_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _export_function_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/fgs/functions/{function_urn}/export",
            "request_type": request.__class__.__name__,
            "response_type": "ExportFunctionResponse"
            }

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

    def import_function(self, request):
        """导入函数

        导入函数
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ImportFunction
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.ImportFunctionRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.ImportFunctionResponse`
        """
        http_info = self._import_function_http_info(request)
        return self._call_api(**http_info)

    def import_function_invoker(self, request):
        http_info = self._import_function_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _import_function_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/fgs/functions/import",
            "request_type": request.__class__.__name__,
            "response_type": "ImportFunctionResponse"
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

    def invoke_function(self, request):
        """同步执行函数

        同步调用指的是客户端请求需要明确等到响应结果，也就是说这样的请求必须得调用到用户的函数，并且等到调用完成才返回。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for InvokeFunction
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.InvokeFunctionRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.InvokeFunctionResponse`
        """
        http_info = self._invoke_function_http_info(request)
        return self._call_api(**http_info)

    def invoke_function_invoker(self, request):
        http_info = self._invoke_function_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _invoke_function_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/fgs/functions/{function_urn}/invocations",
            "request_type": request.__class__.__name__,
            "response_type": "InvokeFunctionResponse"
            }

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

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Cff-Request-Id", ]

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

    def list_active_async_invocations(self, request):
        """获取函数活跃异步调用请求列表

        获取函数异步调用活跃请求列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListActiveAsyncInvocations
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.ListActiveAsyncInvocationsRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.ListActiveAsyncInvocationsResponse`
        """
        http_info = self._list_active_async_invocations_http_info(request)
        return self._call_api(**http_info)

    def list_active_async_invocations_invoker(self, request):
        http_info = self._list_active_async_invocations_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_active_async_invocations_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/fgs/functions/{function_urn}/active-async-invocations",
            "request_type": request.__class__.__name__,
            "response_type": "ListActiveAsyncInvocationsResponse"
            }

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

    def list_app_templates(self, request):
        """查询应用程序模板列表

        查询应用程序模板列表（该功能目前仅支持华北-北京四、华东-上海一）
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAppTemplates
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.ListAppTemplatesRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.ListAppTemplatesResponse`
        """
        http_info = self._list_app_templates_http_info(request)
        return self._call_api(**http_info)

    def list_app_templates_invoker(self, request):
        http_info = self._list_app_templates_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_app_templates_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/fgs/application/templates",
            "request_type": request.__class__.__name__,
            "response_type": "ListAppTemplatesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'maxitems' in local_var_params:
            query_params.append(('maxitems', local_var_params['maxitems']))
        if 'runtime' in local_var_params:
            query_params.append(('runtime', local_var_params['runtime']))
        if 'category' in local_var_params:
            query_params.append(('category', local_var_params['category']))

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def list_async_invocations(self, request):
        """获取函数异步调用请求列表

        获取函数异步调用请求列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAsyncInvocations
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.ListAsyncInvocationsRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.ListAsyncInvocationsResponse`
        """
        http_info = self._list_async_invocations_http_info(request)
        return self._call_api(**http_info)

    def list_async_invocations_invoker(self, request):
        http_info = self._list_async_invocations_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_async_invocations_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/fgs/functions/{function_urn}/async-invocations",
            "request_type": request.__class__.__name__,
            "response_type": "ListAsyncInvocationsResponse"
            }

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

    def list_bridge_functions(self, request):
        """获取指定函数绑定的servicebridge函数列表

        获取指定函数绑定的servicebridge函数列表信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListBridgeFunctions
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.ListBridgeFunctionsRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.ListBridgeFunctionsResponse`
        """
        http_info = self._list_bridge_functions_http_info(request)
        return self._call_api(**http_info)

    def list_bridge_functions_invoker(self, request):
        http_info = self._list_bridge_functions_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_bridge_functions_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/fgs/functions/{function_urn}/servicebridge/relation",
            "request_type": request.__class__.__name__,
            "response_type": "ListBridgeFunctionsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'function_urn' in local_var_params:
            path_params['function_urn'] = local_var_params['function_urn']

        query_params = []
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))

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

    def list_bridge_versions(self, request):
        """获取servicebridge可用的版本

        获取servicebridge可用的版本
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListBridgeVersions
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.ListBridgeVersionsRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.ListBridgeVersionsResponse`
        """
        http_info = self._list_bridge_versions_http_info(request)
        return self._call_api(**http_info)

    def list_bridge_versions_invoker(self, request):
        http_info = self._list_bridge_versions_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_bridge_versions_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/fgs/servicebridge/version",
            "request_type": request.__class__.__name__,
            "response_type": "ListBridgeVersionsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))

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

    def list_dependencies(self, request):
        """获取依赖包列表

        获取依赖包列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListDependencies
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.ListDependenciesRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.ListDependenciesResponse`
        """
        http_info = self._list_dependencies_http_info(request)
        return self._call_api(**http_info)

    def list_dependencies_invoker(self, request):
        http_info = self._list_dependencies_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_dependencies_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/fgs/dependencies",
            "request_type": request.__class__.__name__,
            "response_type": "ListDependenciesResponse"
            }

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

    def list_dependency_version(self, request):
        """获取依赖包版本列表

        获取依赖包版本列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListDependencyVersion
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.ListDependencyVersionRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.ListDependencyVersionResponse`
        """
        http_info = self._list_dependency_version_http_info(request)
        return self._call_api(**http_info)

    def list_dependency_version_invoker(self, request):
        http_info = self._list_dependency_version_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_dependency_version_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/fgs/dependencies/{depend_id}/version",
            "request_type": request.__class__.__name__,
            "response_type": "ListDependencyVersionResponse"
            }

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

    def list_events(self, request):
        """获取指定函数的测试事件列表

        获取指定函数的测试事件列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListEvents
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.ListEventsRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.ListEventsResponse`
        """
        http_info = self._list_events_http_info(request)
        return self._call_api(**http_info)

    def list_events_invoker(self, request):
        http_info = self._list_events_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_events_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/fgs/functions/{function_urn}/events",
            "request_type": request.__class__.__name__,
            "response_type": "ListEventsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'function_urn' in local_var_params:
            path_params['function_urn'] = local_var_params['function_urn']

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

    def list_function_applications(self, request):
        """查询应用程序列表

        查询应用程序列表（该功能目前仅支持华北-北京四、华东-上海一）
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListFunctionApplications
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.ListFunctionApplicationsRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.ListFunctionApplicationsResponse`
        """
        http_info = self._list_function_applications_http_info(request)
        return self._call_api(**http_info)

    def list_function_applications_invoker(self, request):
        http_info = self._list_function_applications_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_function_applications_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/fgs/applications",
            "request_type": request.__class__.__name__,
            "response_type": "ListFunctionApplicationsResponse"
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

    def list_function_as_metric(self, request):
        """获取按指定指标排序的函数列表

        按指定指标排序的函数列表。
        
        默认统计按错误次数指标统计最近一天失败次数最多的前10个函数
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListFunctionAsMetric
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.ListFunctionAsMetricRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.ListFunctionAsMetricResponse`
        """
        http_info = self._list_function_as_metric_http_info(request)
        return self._call_api(**http_info)

    def list_function_as_metric_invoker(self, request):
        http_info = self._list_function_as_metric_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_function_as_metric_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/fgs/function/report",
            "request_type": request.__class__.__name__,
            "response_type": "ListFunctionAsMetricResponse"
            }

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

    def list_function_async_invoke_config(self, request):
        """获取函数异步配置列表

        获取指定函数所有版本的异步配置列表。。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListFunctionAsyncInvokeConfig
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.ListFunctionAsyncInvokeConfigRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.ListFunctionAsyncInvokeConfigResponse`
        """
        http_info = self._list_function_async_invoke_config_http_info(request)
        return self._call_api(**http_info)

    def list_function_async_invoke_config_invoker(self, request):
        http_info = self._list_function_async_invoke_config_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_function_async_invoke_config_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/fgs/functions/{function_urn}/async-invoke-configs",
            "request_type": request.__class__.__name__,
            "response_type": "ListFunctionAsyncInvokeConfigResponse"
            }

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

    def list_function_reserved_instances(self, request):
        """获取函数预留实例数量

        获取函数预留实例数量。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListFunctionReservedInstances
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.ListFunctionReservedInstancesRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.ListFunctionReservedInstancesResponse`
        """
        http_info = self._list_function_reserved_instances_http_info(request)
        return self._call_api(**http_info)

    def list_function_reserved_instances_invoker(self, request):
        http_info = self._list_function_reserved_instances_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_function_reserved_instances_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/fgs/functions/reservedinstances",
            "request_type": request.__class__.__name__,
            "response_type": "ListFunctionReservedInstancesResponse"
            }

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

    def list_function_statistics(self, request):
        """获取指定时间段的函数运行指标

        获取指定时间段的函数运行指标。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListFunctionStatistics
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.ListFunctionStatisticsRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.ListFunctionStatisticsResponse`
        """
        http_info = self._list_function_statistics_http_info(request)
        return self._call_api(**http_info)

    def list_function_statistics_invoker(self, request):
        http_info = self._list_function_statistics_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_function_statistics_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/fgs/functions/{func_urn}/statistics/{period}",
            "request_type": request.__class__.__name__,
            "response_type": "ListFunctionStatisticsResponse"
            }

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

    def list_function_tags(self, request):
        """查询函数标签列表

        查询函数标签列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListFunctionTags
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.ListFunctionTagsRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.ListFunctionTagsResponse`
        """
        http_info = self._list_function_tags_http_info(request)
        return self._call_api(**http_info)

    def list_function_tags_invoker(self, request):
        http_info = self._list_function_tags_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_function_tags_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/{resource_type}/{resource_id}/tags",
            "request_type": request.__class__.__name__,
            "response_type": "ListFunctionTagsResponse"
            }

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

    def list_function_template(self, request):
        """获取函数模板列表

        获取函数模板列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListFunctionTemplate
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.ListFunctionTemplateRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.ListFunctionTemplateResponse`
        """
        http_info = self._list_function_template_http_info(request)
        return self._call_api(**http_info)

    def list_function_template_invoker(self, request):
        http_info = self._list_function_template_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_function_template_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/fgs/templates",
            "request_type": request.__class__.__name__,
            "response_type": "ListFunctionTemplateResponse"
            }

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
        if 'runtime' in local_var_params:
            query_params.append(('runtime', local_var_params['runtime']))
        if 'scene' in local_var_params:
            query_params.append(('scene', local_var_params['scene']))
        if 'service' in local_var_params:
            query_params.append(('service', local_var_params['service']))

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

    def list_function_triggers(self, request):
        """获取指定函数的所有触发器

        获取指定函数的所有触发器设置。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListFunctionTriggers
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.ListFunctionTriggersRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.ListFunctionTriggersResponse`
        """
        http_info = self._list_function_triggers_http_info(request)
        return self._call_api(**http_info)

    def list_function_triggers_invoker(self, request):
        http_info = self._list_function_triggers_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_function_triggers_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/fgs/triggers/{function_urn}",
            "request_type": request.__class__.__name__,
            "response_type": "ListFunctionTriggersResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'function_urn' in local_var_params:
            path_params['function_urn'] = local_var_params['function_urn']

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

    def list_function_versions(self, request):
        """获取指定函数的版本列表

        获取指定函数的版本列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListFunctionVersions
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.ListFunctionVersionsRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.ListFunctionVersionsResponse`
        """
        http_info = self._list_function_versions_http_info(request)
        return self._call_api(**http_info)

    def list_function_versions_invoker(self, request):
        http_info = self._list_function_versions_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_function_versions_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/fgs/functions/{function_urn}/versions",
            "request_type": request.__class__.__name__,
            "response_type": "ListFunctionVersionsResponse"
            }

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

    def list_functions(self, request):
        """获取函数列表

        获取函数列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListFunctions
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.ListFunctionsRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.ListFunctionsResponse`
        """
        http_info = self._list_functions_http_info(request)
        return self._call_api(**http_info)

    def list_functions_invoker(self, request):
        http_info = self._list_functions_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_functions_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/fgs/functions",
            "request_type": request.__class__.__name__,
            "response_type": "ListFunctionsResponse"
            }

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

    def list_quotas(self, request):
        """查询租户配额

        查询租户配额
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListQuotas
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.ListQuotasRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.ListQuotasResponse`
        """
        http_info = self._list_quotas_http_info(request)
        return self._call_api(**http_info)

    def list_quotas_invoker(self, request):
        http_info = self._list_quotas_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_quotas_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/fgs/quotas",
            "request_type": request.__class__.__name__,
            "response_type": "ListQuotasResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

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

    def list_reserved_instance_configs(self, request):
        """获取函数预留实例配置列表

        获取函数预留实例配置列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListReservedInstanceConfigs
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.ListReservedInstanceConfigsRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.ListReservedInstanceConfigsResponse`
        """
        http_info = self._list_reserved_instance_configs_http_info(request)
        return self._call_api(**http_info)

    def list_reserved_instance_configs_invoker(self, request):
        http_info = self._list_reserved_instance_configs_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_reserved_instance_configs_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/fgs/functions/reservedinstanceconfigs",
            "request_type": request.__class__.__name__,
            "response_type": "ListReservedInstanceConfigsResponse"
            }

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
        http_info = self._list_statistics_http_info(request)
        return self._call_api(**http_info)

    def list_statistics_invoker(self, request):
        http_info = self._list_statistics_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_statistics_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/fgs/functions/statistics",
            "request_type": request.__class__.__name__,
            "response_type": "ListStatisticsResponse"
            }

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

    def list_version_aliases(self, request):
        """获取指定函数所有版本别名列表

        获取函数版本别名列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListVersionAliases
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.ListVersionAliasesRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.ListVersionAliasesResponse`
        """
        http_info = self._list_version_aliases_http_info(request)
        return self._call_api(**http_info)

    def list_version_aliases_invoker(self, request):
        http_info = self._list_version_aliases_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_version_aliases_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/fgs/functions/{function_urn}/aliases",
            "request_type": request.__class__.__name__,
            "response_type": "ListVersionAliasesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'function_urn' in local_var_params:
            path_params['function_urn'] = local_var_params['function_urn']

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

    def list_workflow(self, request):
        """查询函数流

        查询函数流
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListWorkflow
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.ListWorkflowRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.ListWorkflowResponse`
        """
        http_info = self._list_workflow_http_info(request)
        return self._call_api(**http_info)

    def list_workflow_invoker(self, request):
        http_info = self._list_workflow_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_workflow_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/fgs/workflows",
            "request_type": request.__class__.__name__,
            "response_type": "ListWorkflowResponse"
            }

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

    def list_workflow_executions(self, request):
        """获取指定函数流执行实例列表

        获取指定函数流执行实例列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListWorkflowExecutions
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.ListWorkflowExecutionsRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.ListWorkflowExecutionsResponse`
        """
        http_info = self._list_workflow_executions_http_info(request)
        return self._call_api(**http_info)

    def list_workflow_executions_invoker(self, request):
        http_info = self._list_workflow_executions_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_workflow_executions_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/fgs/workflows/{workflow_id}/executions",
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

    def retry_work_flow(self, request):
        """重试函数流

        重试函数流
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RetryWorkFlow
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.RetryWorkFlowRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.RetryWorkFlowResponse`
        """
        http_info = self._retry_work_flow_http_info(request)
        return self._call_api(**http_info)

    def retry_work_flow_invoker(self, request):
        http_info = self._retry_work_flow_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _retry_work_flow_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/fgs/workflows/{workflow_id}/executions/{execution_id}/retry",
            "request_type": request.__class__.__name__,
            "response_type": "RetryWorkFlowResponse"
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

    def show_app_template(self, request):
        """查询应用程序模板详情

        查询应用程序模板详情（该功能目前仅支持华北-北京四、华东-上海一）
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAppTemplate
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.ShowAppTemplateRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.ShowAppTemplateResponse`
        """
        http_info = self._show_app_template_http_info(request)
        return self._call_api(**http_info)

    def show_app_template_invoker(self, request):
        http_info = self._show_app_template_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_app_template_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/fgs/application/templates/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAppTemplateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

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

    def show_dependency_version(self, request):
        """获取依赖包版本详情

        获取依赖包版本详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDependencyVersion
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.ShowDependencyVersionRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.ShowDependencyVersionResponse`
        """
        http_info = self._show_dependency_version_http_info(request)
        return self._call_api(**http_info)

    def show_dependency_version_invoker(self, request):
        http_info = self._show_dependency_version_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_dependency_version_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/fgs/dependencies/{depend_id}/version/{version}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDependencyVersionResponse"
            }

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

    def show_event(self, request):
        """获取测试事件详细信息

        获取测试事件详细信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowEvent
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.ShowEventRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.ShowEventResponse`
        """
        http_info = self._show_event_http_info(request)
        return self._call_api(**http_info)

    def show_event_invoker(self, request):
        http_info = self._show_event_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_event_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/fgs/functions/{function_urn}/events/{event_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowEventResponse"
            }

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

    def show_func_reserved_instance_metrics(self, request):
        """查询函数实例使用情况指标

        查询函数实例使用情况指标。
        
        - 指标单位为分钟：
            当查询时间范围小于1小时,指标周期为1分钟
            当查询时间范围小于1天,指标周期为30分钟
            当查询时间范围大于1天,指标周期为180分钟
        - 指标分为如下几类：reservedinstancenum（预留实例使用）、concurrency（实例使用/并发）
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowFuncReservedInstanceMetrics
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.ShowFuncReservedInstanceMetricsRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.ShowFuncReservedInstanceMetricsResponse`
        """
        http_info = self._show_func_reserved_instance_metrics_http_info(request)
        return self._call_api(**http_info)

    def show_func_reserved_instance_metrics_invoker(self, request):
        http_info = self._show_func_reserved_instance_metrics_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_func_reserved_instance_metrics_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/fgs/functions/{func_urn}/instancereports",
            "request_type": request.__class__.__name__,
            "response_type": "ShowFuncReservedInstanceMetricsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'func_urn' in local_var_params:
            path_params['func_urn'] = local_var_params['func_urn']

        query_params = []
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

    def show_func_snapshot_state(self, request):
        """查询函数快照制作状态

        查询函数快照制作状态。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowFuncSnapshotState
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.ShowFuncSnapshotStateRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.ShowFuncSnapshotStateResponse`
        """
        http_info = self._show_func_snapshot_state_http_info(request)
        return self._call_api(**http_info)

    def show_func_snapshot_state_invoker(self, request):
        http_info = self._show_func_snapshot_state_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_func_snapshot_state_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/fgs/functions/{function_urn}/snapshots/{action}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowFuncSnapshotStateResponse"
            }

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

    def show_function_app(self, request):
        """查询应用程序详情

        查询应用程序详情（该功能目前仅支持华北-北京四、华东-上海一）
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowFunctionApp
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.ShowFunctionAppRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.ShowFunctionAppResponse`
        """
        http_info = self._show_function_app_http_info(request)
        return self._call_api(**http_info)

    def show_function_app_invoker(self, request):
        http_info = self._show_function_app_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_function_app_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/fgs/applications/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowFunctionAppResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

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

    def show_function_async_invoke_config(self, request):
        """获取函数异步配置信息

        获取指定函数某一版本的异步配置信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowFunctionAsyncInvokeConfig
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.ShowFunctionAsyncInvokeConfigRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.ShowFunctionAsyncInvokeConfigResponse`
        """
        http_info = self._show_function_async_invoke_config_http_info(request)
        return self._call_api(**http_info)

    def show_function_async_invoke_config_invoker(self, request):
        http_info = self._show_function_async_invoke_config_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_function_async_invoke_config_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/fgs/functions/{function_urn}/async-invoke-config",
            "request_type": request.__class__.__name__,
            "response_type": "ShowFunctionAsyncInvokeConfigResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'function_urn' in local_var_params:
            path_params['function_urn'] = local_var_params['function_urn']

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

    def show_function_code(self, request):
        """获取指定函数代码

        获取指定函数的代码。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowFunctionCode
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.ShowFunctionCodeRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.ShowFunctionCodeResponse`
        """
        http_info = self._show_function_code_http_info(request)
        return self._call_api(**http_info)

    def show_function_code_invoker(self, request):
        http_info = self._show_function_code_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_function_code_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/fgs/functions/{function_urn}/code",
            "request_type": request.__class__.__name__,
            "response_type": "ShowFunctionCodeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'function_urn' in local_var_params:
            path_params['function_urn'] = local_var_params['function_urn']

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

    def show_function_config(self, request):
        """获取函数的metadata

        获取指定函数的metadata。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowFunctionConfig
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.ShowFunctionConfigRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.ShowFunctionConfigResponse`
        """
        http_info = self._show_function_config_http_info(request)
        return self._call_api(**http_info)

    def show_function_config_invoker(self, request):
        http_info = self._show_function_config_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_function_config_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/fgs/functions/{function_urn}/config",
            "request_type": request.__class__.__name__,
            "response_type": "ShowFunctionConfigResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'function_urn' in local_var_params:
            path_params['function_urn'] = local_var_params['function_urn']

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

    def show_function_metrics(self, request):
        """查询函数实例流量指标

        查询函数流量指标。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowFunctionMetrics
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.ShowFunctionMetricsRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.ShowFunctionMetricsResponse`
        """
        http_info = self._show_function_metrics_http_info(request)
        return self._call_api(**http_info)

    def show_function_metrics_invoker(self, request):
        http_info = self._show_function_metrics_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_function_metrics_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/fgs/functions/{func_urn}/slareports/{period}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowFunctionMetricsResponse"
            }

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

    def show_function_template(self, request):
        """获取指定函数模板

        获取指定函数模板
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowFunctionTemplate
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.ShowFunctionTemplateRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.ShowFunctionTemplateResponse`
        """
        http_info = self._show_function_template_http_info(request)
        return self._call_api(**http_info)

    def show_function_template_invoker(self, request):
        http_info = self._show_function_template_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_function_template_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/fgs/templates/{template_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowFunctionTemplateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'template_id' in local_var_params:
            path_params['template_id'] = local_var_params['template_id']

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

    def show_function_trigger(self, request):
        """获取指定触发器的信息

        获取特定触发器的信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowFunctionTrigger
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.ShowFunctionTriggerRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.ShowFunctionTriggerResponse`
        """
        http_info = self._show_function_trigger_http_info(request)
        return self._call_api(**http_info)

    def show_function_trigger_invoker(self, request):
        http_info = self._show_function_trigger_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_function_trigger_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/fgs/triggers/{function_urn}/{trigger_type_code}/{trigger_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowFunctionTriggerResponse"
            }

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

    def show_lts_log_details(self, request):
        """获取指定函数的lts日志组日志流配置

        获取指定函数的lts日志组日志流配置。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowLtsLogDetails
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.ShowLtsLogDetailsRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.ShowLtsLogDetailsResponse`
        """
        http_info = self._show_lts_log_details_http_info(request)
        return self._call_api(**http_info)

    def show_lts_log_details_invoker(self, request):
        http_info = self._show_lts_log_details_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_lts_log_details_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/fgs/functions/{function_urn}/lts-log-detail",
            "request_type": request.__class__.__name__,
            "response_type": "ShowLtsLogDetailsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'function_urn' in local_var_params:
            path_params['function_urn'] = local_var_params['function_urn']

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

    def show_project_async_status_log_info(self, request):
        """查询异步日志详情

        查询异步日志详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowProjectAsyncStatusLogInfo
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.ShowProjectAsyncStatusLogInfoRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.ShowProjectAsyncStatusLogInfoResponse`
        """
        http_info = self._show_project_async_status_log_info_http_info(request)
        return self._call_api(**http_info)

    def show_project_async_status_log_info_invoker(self, request):
        http_info = self._show_project_async_status_log_info_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_project_async_status_log_info_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/fgs/functions/async-status-log-detail",
            "request_type": request.__class__.__name__,
            "response_type": "ShowProjectAsyncStatusLogInfoResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

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

    def show_project_tags_list(self, request):
        """查询资源标签

        查询资源标签。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowProjectTagsList
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.ShowProjectTagsListRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.ShowProjectTagsListResponse`
        """
        http_info = self._show_project_tags_list_http_info(request)
        return self._call_api(**http_info)

    def show_project_tags_list_invoker(self, request):
        http_info = self._show_project_tags_list_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_project_tags_list_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/{resource_type}/tags",
            "request_type": request.__class__.__name__,
            "response_type": "ShowProjectTagsListResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_type' in local_var_params:
            path_params['resource_type'] = local_var_params['resource_type']

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

    def show_res_instance_info(self, request):
        """查询资源实例

        查询资源实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowResInstanceInfo
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.ShowResInstanceInfoRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.ShowResInstanceInfoResponse`
        """
        http_info = self._show_res_instance_info_http_info(request)
        return self._call_api(**http_info)

    def show_res_instance_info_invoker(self, request):
        http_info = self._show_res_instance_info_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_res_instance_info_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/{resource_type}/resource-instances/{action}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowResInstanceInfoResponse"
            }

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

    def show_tenant_metric(self, request):
        """获取函数流指标

        获取函数流指标
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowTenantMetric
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.ShowTenantMetricRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.ShowTenantMetricResponse`
        """
        http_info = self._show_tenant_metric_http_info(request)
        return self._call_api(**http_info)

    def show_tenant_metric_invoker(self, request):
        http_info = self._show_tenant_metric_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_tenant_metric_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/fgs/workflow-statistic",
            "request_type": request.__class__.__name__,
            "response_type": "ShowTenantMetricResponse"
            }

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

    def show_tracing(self, request):
        """获取函数调用链配置

        获取函数调用链配置
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowTracing
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.ShowTracingRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.ShowTracingResponse`
        """
        http_info = self._show_tracing_http_info(request)
        return self._call_api(**http_info)

    def show_tracing_invoker(self, request):
        http_info = self._show_tracing_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_tracing_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/fgs/functions/{function_urn}/tracing",
            "request_type": request.__class__.__name__,
            "response_type": "ShowTracingResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'function_urn' in local_var_params:
            path_params['function_urn'] = local_var_params['function_urn']

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

    def show_version_alias(self, request):
        """获取函数版本的指定别名信息

        获取函数指定的版本别名信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowVersionAlias
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.ShowVersionAliasRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.ShowVersionAliasResponse`
        """
        http_info = self._show_version_alias_http_info(request)
        return self._call_api(**http_info)

    def show_version_alias_invoker(self, request):
        http_info = self._show_version_alias_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_version_alias_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/fgs/functions/{function_urn}/aliases/{alias_name}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowVersionAliasResponse"
            }

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

    def show_work_flow(self, request):
        """获取指定函数流实例的元数据

        获取指定函数流实例的元数据
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowWorkFlow
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.ShowWorkFlowRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.ShowWorkFlowResponse`
        """
        http_info = self._show_work_flow_http_info(request)
        return self._call_api(**http_info)

    def show_work_flow_invoker(self, request):
        http_info = self._show_work_flow_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_work_flow_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/fgs/workflows/{workflow_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowWorkFlowResponse"
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

    def show_work_flow_metric(self, request):
        """获取指定函数流指标

        获取指定函数流指标
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowWorkFlowMetric
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.ShowWorkFlowMetricRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.ShowWorkFlowMetricResponse`
        """
        http_info = self._show_work_flow_metric_http_info(request)
        return self._call_api(**http_info)

    def show_work_flow_metric_invoker(self, request):
        http_info = self._show_work_flow_metric_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_work_flow_metric_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/fgs/workflow-statistic/{workflow_urn}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowWorkFlowMetricResponse"
            }

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

    def show_workflow_execution(self, request):
        """获取指定函数流执行实例

        获取指定函数流执行实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowWorkflowExecution
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.ShowWorkflowExecutionRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.ShowWorkflowExecutionResponse`
        """
        http_info = self._show_workflow_execution_http_info(request)
        return self._call_api(**http_info)

    def show_workflow_execution_invoker(self, request):
        http_info = self._show_workflow_execution_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_workflow_execution_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/fgs/workflows/{workflow_id}/executions/{execution_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowWorkflowExecutionResponse"
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
        if 'x_get_workflow_full_history_data' in local_var_params:
            header_params['X-Get-Workflow-Full-History-Data'] = local_var_params['x_get_workflow_full_history_data']

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

    def show_workflow_execution_for_page(self, request):
        """分页获取指定函数流执行实例列表

        分页获取指定函数流执行实例列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowWorkflowExecutionForPage
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.ShowWorkflowExecutionForPageRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.ShowWorkflowExecutionForPageResponse`
        """
        http_info = self._show_workflow_execution_for_page_http_info(request)
        return self._call_api(**http_info)

    def show_workflow_execution_for_page_invoker(self, request):
        http_info = self._show_workflow_execution_for_page_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_workflow_execution_for_page_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/fgs/workflows/{workflow_id}/executions-history",
            "request_type": request.__class__.__name__,
            "response_type": "ShowWorkflowExecutionForPageResponse"
            }

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

    def start_sync_workflow_execution(self, request):
        """同步执行函数流

        以同步执行方式启动函数流（仅快速模式函数流支持）
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for StartSyncWorkflowExecution
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.StartSyncWorkflowExecutionRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.StartSyncWorkflowExecutionResponse`
        """
        http_info = self._start_sync_workflow_execution_http_info(request)
        return self._call_api(**http_info)

    def start_sync_workflow_execution_invoker(self, request):
        http_info = self._start_sync_workflow_execution_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _start_sync_workflow_execution_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/fgs/workflows/{workflow_id}/sync-executions",
            "request_type": request.__class__.__name__,
            "response_type": "StartSyncWorkflowExecutionResponse"
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

    def start_workflow_execution(self, request):
        """开始执行函数流

        以异步执行方式启动函数流
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for StartWorkflowExecution
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.StartWorkflowExecutionRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.StartWorkflowExecutionResponse`
        """
        http_info = self._start_workflow_execution_http_info(request)
        return self._call_api(**http_info)

    def start_workflow_execution_invoker(self, request):
        http_info = self._start_workflow_execution_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _start_workflow_execution_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/fgs/workflows/{workflow_id}/executions",
            "request_type": request.__class__.__name__,
            "response_type": "StartWorkflowExecutionResponse"
            }

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

    def stop_work_flow(self, request):
        """停止函数流

        停止函数流
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for StopWorkFlow
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.StopWorkFlowRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.StopWorkFlowResponse`
        """
        http_info = self._stop_work_flow_http_info(request)
        return self._call_api(**http_info)

    def stop_work_flow_invoker(self, request):
        http_info = self._stop_work_flow_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _stop_work_flow_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/fgs/workflows/{workflow_id}/executions/{execution_id}/terminate",
            "request_type": request.__class__.__name__,
            "response_type": "StopWorkFlowResponse"
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

    def update_event(self, request):
        """更新测试事件详细信息

        更新测试事件详细信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateEvent
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.UpdateEventRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.UpdateEventResponse`
        """
        http_info = self._update_event_http_info(request)
        return self._call_api(**http_info)

    def update_event_invoker(self, request):
        http_info = self._update_event_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_event_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/fgs/functions/{function_urn}/events/{event_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateEventResponse"
            }

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

    def update_func_snapshot(self, request):
        """禁用/启动函数快照

        禁用/启动函数快照，仅支持java运行时函数，且为非latest版本才能开启函数快照功能。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateFuncSnapshot
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.UpdateFuncSnapshotRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.UpdateFuncSnapshotResponse`
        """
        http_info = self._update_func_snapshot_http_info(request)
        return self._call_api(**http_info)

    def update_func_snapshot_invoker(self, request):
        http_info = self._update_func_snapshot_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_func_snapshot_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/fgs/functions/{function_urn}/snapshots/{action}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateFuncSnapshotResponse"
            }

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

    def update_function_async_invoke_config(self, request):
        """设置函数异步配置信息

        设置函数异步配置信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateFunctionAsyncInvokeConfig
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.UpdateFunctionAsyncInvokeConfigRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.UpdateFunctionAsyncInvokeConfigResponse`
        """
        http_info = self._update_function_async_invoke_config_http_info(request)
        return self._call_api(**http_info)

    def update_function_async_invoke_config_invoker(self, request):
        http_info = self._update_function_async_invoke_config_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_function_async_invoke_config_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/fgs/functions/{function_urn}/async-invoke-config",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateFunctionAsyncInvokeConfigResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'function_urn' in local_var_params:
            path_params['function_urn'] = local_var_params['function_urn']

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

    def update_function_code(self, request):
        """修改函数代码

        修改指定的函数的代码。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateFunctionCode
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.UpdateFunctionCodeRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.UpdateFunctionCodeResponse`
        """
        http_info = self._update_function_code_http_info(request)
        return self._call_api(**http_info)

    def update_function_code_invoker(self, request):
        http_info = self._update_function_code_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_function_code_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/fgs/functions/{function_urn}/code",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateFunctionCodeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'function_urn' in local_var_params:
            path_params['function_urn'] = local_var_params['function_urn']

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

    def update_function_collect_state(self, request):
        """更新函数置顶状态

        更新函数置顶状态
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateFunctionCollectState
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.UpdateFunctionCollectStateRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.UpdateFunctionCollectStateResponse`
        """
        http_info = self._update_function_collect_state_http_info(request)
        return self._call_api(**http_info)

    def update_function_collect_state_invoker(self, request):
        http_info = self._update_function_collect_state_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_function_collect_state_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/fgs/functions/{func_urn}/collect/{state}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateFunctionCollectStateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'func_urn' in local_var_params:
            path_params['func_urn'] = local_var_params['func_urn']
        if 'state' in local_var_params:
            path_params['state'] = local_var_params['state']

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

    def update_function_config(self, request):
        """修改函数的metadata信息

        修改指定的函数的metadata信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateFunctionConfig
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.UpdateFunctionConfigRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.UpdateFunctionConfigResponse`
        """
        http_info = self._update_function_config_http_info(request)
        return self._call_api(**http_info)

    def update_function_config_invoker(self, request):
        http_info = self._update_function_config_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_function_config_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/fgs/functions/{function_urn}/config",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateFunctionConfigResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'function_urn' in local_var_params:
            path_params['function_urn'] = local_var_params['function_urn']

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

    def update_function_max_instance_config(self, request):
        """更新函数最大实例数

        更新函数最大实例数
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateFunctionMaxInstanceConfig
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.UpdateFunctionMaxInstanceConfigRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.UpdateFunctionMaxInstanceConfigResponse`
        """
        http_info = self._update_function_max_instance_config_http_info(request)
        return self._call_api(**http_info)

    def update_function_max_instance_config_invoker(self, request):
        http_info = self._update_function_max_instance_config_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_function_max_instance_config_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/fgs/functions/{function_urn}/config-max-instance",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateFunctionMaxInstanceConfigResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'function_urn' in local_var_params:
            path_params['function_urn'] = local_var_params['function_urn']

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

    def update_function_reserved_instances_count(self, request):
        """修改函数预留实例数量

        修改函数预留实例数量。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateFunctionReservedInstancesCount
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.UpdateFunctionReservedInstancesCountRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.UpdateFunctionReservedInstancesCountResponse`
        """
        http_info = self._update_function_reserved_instances_count_http_info(request)
        return self._call_api(**http_info)

    def update_function_reserved_instances_count_invoker(self, request):
        http_info = self._update_function_reserved_instances_count_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_function_reserved_instances_count_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/fgs/functions/{function_urn}/reservedinstances",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateFunctionReservedInstancesCountResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'function_urn' in local_var_params:
            path_params['function_urn'] = local_var_params['function_urn']

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

    def update_tracing(self, request):
        """修改函数调用链配置

        修改函数调用链配置,开通/修改传入aksk，关闭aksk传空
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateTracing
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.UpdateTracingRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.UpdateTracingResponse`
        """
        http_info = self._update_tracing_http_info(request)
        return self._call_api(**http_info)

    def update_tracing_invoker(self, request):
        http_info = self._update_tracing_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_tracing_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/fgs/functions/{function_urn}/tracing",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateTracingResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'function_urn' in local_var_params:
            path_params['function_urn'] = local_var_params['function_urn']

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

    def update_trigger(self, request):
        """更新触发器

        更新触发器
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateTrigger
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.UpdateTriggerRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.UpdateTriggerResponse`
        """
        http_info = self._update_trigger_http_info(request)
        return self._call_api(**http_info)

    def update_trigger_invoker(self, request):
        http_info = self._update_trigger_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_trigger_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/fgs/triggers/{function_urn}/{trigger_type_code}/{trigger_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateTriggerResponse"
            }

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

    def update_version_alias(self, request):
        """修改函数版本别名信息

        修改函数版本别名信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateVersionAlias
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.UpdateVersionAliasRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.UpdateVersionAliasResponse`
        """
        http_info = self._update_version_alias_http_info(request)
        return self._call_api(**http_info)

    def update_version_alias_invoker(self, request):
        http_info = self._update_version_alias_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_version_alias_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/fgs/functions/{function_urn}/aliases/{alias_name}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateVersionAliasResponse"
            }

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

    def update_work_flow(self, request):
        """修改指定函数流实例的元数据

        修改指定函数流实例的元数据
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateWorkFlow
        :type request: :class:`huaweicloudsdkfunctiongraph.v2.UpdateWorkFlowRequest`
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.UpdateWorkFlowResponse`
        """
        http_info = self._update_work_flow_http_info(request)
        return self._call_api(**http_info)

    def update_work_flow_invoker(self, request):
        http_info = self._update_work_flow_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_work_flow_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/fgs/workflows/{workflow_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateWorkFlowResponse"
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

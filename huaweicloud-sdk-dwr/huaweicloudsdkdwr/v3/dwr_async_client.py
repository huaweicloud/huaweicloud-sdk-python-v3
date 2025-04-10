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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkdwr'")


class DwrAsyncClient(Client):
    def __init__(self):
        super(DwrAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkdwr.v3.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "DwrAsyncClient":
                raise TypeError("client type error, support client type is DwrAsyncClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def accept_service_contract_async(self, request):
        r"""同意服务协议

        本接口用于使用工作流时需要同意服务使用协议。该函数具有幂等性。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AcceptServiceContract
        :type request: :class:`huaweicloudsdkdwr.v3.AcceptServiceContractRequest`
        :rtype: :class:`huaweicloudsdkdwr.v3.AcceptServiceContractResponse`
        """
        http_info = self._accept_service_contract_http_info(request)
        return self._call_api(**http_info)

    def accept_service_contract_async_invoker(self, request):
        http_info = self._accept_service_contract_http_info(request)
        return AsyncInvoker(self, http_info)

    def _accept_service_contract_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/workflow-agreements",
            "request_type": request.__class__.__name__,
            "response_type": "AcceptServiceContractResponse"
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

        response_headers = ["x-request-id", "Content-Length", ]

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

    def async_invoke_api_start_workflow_async(self, request):
        r"""API异步启动工作流

        本接口用于API方式异步启动已有工作流，产生工作流实例
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AsyncInvokeApiStartWorkflow
        :type request: :class:`huaweicloudsdkdwr.v3.AsyncInvokeApiStartWorkflowRequest`
        :rtype: :class:`huaweicloudsdkdwr.v3.AsyncInvokeApiStartWorkflowResponse`
        """
        http_info = self._async_invoke_api_start_workflow_http_info(request)
        return self._call_api(**http_info)

    def async_invoke_api_start_workflow_async_invoker(self, request):
        http_info = self._async_invoke_api_start_workflow_http_info(request)
        return AsyncInvoker(self, http_info)

    def _async_invoke_api_start_workflow_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/workflows/{graph_name}/execute",
            "request_type": request.__class__.__name__,
            "response_type": "AsyncInvokeApiStartWorkflowResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'graph_name' in local_var_params:
            path_params['graph_name'] = local_var_params['graph_name']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["x-request-id", "Connection", "Content-Length", "Date", ]

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

    def check_workflow_authentication_async(self, request):
        r"""查询授权

        本接口用于查询授权，查询由DWR服务自动帮助用户创建工作流运行时需要的函数服务权限，以及函数服务运行时的权限。该函数具有幂等性。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CheckWorkflowAuthentication
        :type request: :class:`huaweicloudsdkdwr.v3.CheckWorkflowAuthenticationRequest`
        :rtype: :class:`huaweicloudsdkdwr.v3.CheckWorkflowAuthenticationResponse`
        """
        http_info = self._check_workflow_authentication_http_info(request)
        return self._call_api(**http_info)

    def check_workflow_authentication_async_invoker(self, request):
        http_info = self._check_workflow_authentication_http_info(request)
        return AsyncInvoker(self, http_info)

    def _check_workflow_authentication_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/workflow-authorization",
            "request_type": request.__class__.__name__,
            "response_type": "CheckWorkflowAuthenticationResponse"
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

        response_headers = ["x-request-id", "Connection", "Content-Length", "Date", ]

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

    def create_my_action_template_async(self, request):
        r"""创建第三方算子模板

        创建第三方算子模板
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateMyActionTemplate
        :type request: :class:`huaweicloudsdkdwr.v3.CreateMyActionTemplateRequest`
        :rtype: :class:`huaweicloudsdkdwr.v3.CreateMyActionTemplateResponse`
        """
        http_info = self._create_my_action_template_http_info(request)
        return self._call_api(**http_info)

    def create_my_action_template_async_invoker(self, request):
        http_info = self._create_my_action_template_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_my_action_template_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/myactiontemplates/{template_name}",
            "request_type": request.__class__.__name__,
            "response_type": "CreateMyActionTemplateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'template_name' in local_var_params:
            path_params['template_name'] = local_var_params['template_name']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", "Connection", "Content-Length", "Date", ]

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

    def create_workflow_authentication_async(self, request):
        r"""开通授权

        本接口用于开通授权，由DWR服务自动帮助用户创建工作流运行时需要的函数服务权限，以及函数服务运行时的权限。该函数具有幂等性。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateWorkflowAuthentication
        :type request: :class:`huaweicloudsdkdwr.v3.CreateWorkflowAuthenticationRequest`
        :rtype: :class:`huaweicloudsdkdwr.v3.CreateWorkflowAuthenticationResponse`
        """
        http_info = self._create_workflow_authentication_http_info(request)
        return self._call_api(**http_info)

    def create_workflow_authentication_async_invoker(self, request):
        http_info = self._create_workflow_authentication_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_workflow_authentication_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/workflow-authorization",
            "request_type": request.__class__.__name__,
            "response_type": "CreateWorkflowAuthenticationResponse"
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

        response_headers = ["x-request-id", "Content-Length", ]

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

    def delete_my_action_template_async(self, request):
        r"""删除第三方算子模板

        本接口用于标记删除提交的第三方算子模板。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteMyActionTemplate
        :type request: :class:`huaweicloudsdkdwr.v3.DeleteMyActionTemplateRequest`
        :rtype: :class:`huaweicloudsdkdwr.v3.DeleteMyActionTemplateResponse`
        """
        http_info = self._delete_my_action_template_http_info(request)
        return self._call_api(**http_info)

    def delete_my_action_template_async_invoker(self, request):
        http_info = self._delete_my_action_template_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_my_action_template_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{project_id}/myactiontemplates/{template_name}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteMyActionTemplateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'template_name' in local_var_params:
            path_params['template_name'] = local_var_params['template_name']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["x-request-id", "Content-Length", ]

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

    def list_my_action_template_async(self, request):
        r"""查询第三方算子列表

        本接口用于查询提交注册过的三方算子列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListMyActionTemplate
        :type request: :class:`huaweicloudsdkdwr.v3.ListMyActionTemplateRequest`
        :rtype: :class:`huaweicloudsdkdwr.v3.ListMyActionTemplateResponse`
        """
        http_info = self._list_my_action_template_http_info(request)
        return self._call_api(**http_info)

    def list_my_action_template_async_invoker(self, request):
        http_info = self._list_my_action_template_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_my_action_template_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/myactiontemplates",
            "request_type": request.__class__.__name__,
            "response_type": "ListMyActionTemplateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["x-request-id", "Connection", "Content-Length", "Date", ]

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

    def list_system_templates_async(self, request):
        r"""查询华为云内置算子列表

        本接口用于按名称查询系统内置算子列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListSystemTemplates
        :type request: :class:`huaweicloudsdkdwr.v3.ListSystemTemplatesRequest`
        :rtype: :class:`huaweicloudsdkdwr.v3.ListSystemTemplatesResponse`
        """
        http_info = self._list_system_templates_http_info(request)
        return self._call_api(**http_info)

    def list_system_templates_async_invoker(self, request):
        http_info = self._list_system_templates_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_system_templates_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/actiontemplates",
            "request_type": request.__class__.__name__,
            "response_type": "ListSystemTemplatesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["x-request-id", "Connection", "Content-Length", "Date", ]

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

    def list_workflow_instance_async(self, request):
        r"""本接口用于查询用户工作流的实例列表

        本接口用于查询用户工作流的实例列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListWorkflowInstance
        :type request: :class:`huaweicloudsdkdwr.v3.ListWorkflowInstanceRequest`
        :rtype: :class:`huaweicloudsdkdwr.v3.ListWorkflowInstanceResponse`
        """
        http_info = self._list_workflow_instance_http_info(request)
        return self._call_api(**http_info)

    def list_workflow_instance_async_invoker(self, request):
        http_info = self._list_workflow_instance_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_workflow_instance_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/workflowexecutions",
            "request_type": request.__class__.__name__,
            "response_type": "ListWorkflowInstanceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", "Content-Length", "Date", "Content-Type", ]

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

    def restore_workflow_execution_async(self, request):
        r"""恢复一个执行失败状态的工作流实例

        本接口用于恢复一个执行失败状态的工作流实例。恢复后，工作流实例将从上次失败的状态处继续执行，而工作流步骤中已经执行成功的状态不会再执行。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RestoreWorkflowExecution
        :type request: :class:`huaweicloudsdkdwr.v3.RestoreWorkflowExecutionRequest`
        :rtype: :class:`huaweicloudsdkdwr.v3.RestoreWorkflowExecutionResponse`
        """
        http_info = self._restore_workflow_execution_http_info(request)
        return self._call_api(**http_info)

    def restore_workflow_execution_async_invoker(self, request):
        http_info = self._restore_workflow_execution_http_info(request)
        return AsyncInvoker(self, http_info)

    def _restore_workflow_execution_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/workflows/{graph_name}/workflowexecution/{execution_name}/retry",
            "request_type": request.__class__.__name__,
            "response_type": "RestoreWorkflowExecutionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["x-request-id", "Connection", "Content-Length", "Date", ]

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

    def show_public_action_list_async(self, request):
        r"""查询已发布算子列表

        本接口用于查询开放的算子列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowPublicActionList
        :type request: :class:`huaweicloudsdkdwr.v3.ShowPublicActionListRequest`
        :rtype: :class:`huaweicloudsdkdwr.v3.ShowPublicActionListResponse`
        """
        http_info = self._show_public_action_list_http_info(request)
        return self._call_api(**http_info)

    def show_public_action_list_async_invoker(self, request):
        http_info = self._show_public_action_list_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_public_action_list_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/publicactiontemplates",
            "request_type": request.__class__.__name__,
            "response_type": "ShowPublicActionListResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", "Connection", "Content-Length", "Date", ]

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

    def show_public_template_info_async(self, request):
        r"""查询已发布算子模板详情

        本接口用于按名称查询开放的算子详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowPublicTemplateInfo
        :type request: :class:`huaweicloudsdkdwr.v3.ShowPublicTemplateInfoRequest`
        :rtype: :class:`huaweicloudsdkdwr.v3.ShowPublicTemplateInfoResponse`
        """
        http_info = self._show_public_template_info_http_info(request)
        return self._call_api(**http_info)

    def show_public_template_info_async_invoker(self, request):
        http_info = self._show_public_template_info_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_public_template_info_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/publicactiontemplate/{template_name}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowPublicTemplateInfoResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'template_name' in local_var_params:
            path_params['template_name'] = local_var_params['template_name']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", "Connection", "Content-Length", "Date", ]

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

    def show_service_contract_async(self, request):
        r"""查询服务协议

        本接口用于查询使用工作流时同意的服务协议。该函数具有幂等性。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowServiceContract
        :type request: :class:`huaweicloudsdkdwr.v3.ShowServiceContractRequest`
        :rtype: :class:`huaweicloudsdkdwr.v3.ShowServiceContractResponse`
        """
        http_info = self._show_service_contract_http_info(request)
        return self._call_api(**http_info)

    def show_service_contract_async_invoker(self, request):
        http_info = self._show_service_contract_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_service_contract_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/workflow-agreements",
            "request_type": request.__class__.__name__,
            "response_type": "ShowServiceContractResponse"
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

        response_headers = ["x-request-id", "Connection", "Content-Length", "Date", ]

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

    def show_system_template_detail_async(self, request):
        r"""查询华为云内置算子模板信息

        本接口用于按名称查询系统内置算子详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowSystemTemplateDetail
        :type request: :class:`huaweicloudsdkdwr.v3.ShowSystemTemplateDetailRequest`
        :rtype: :class:`huaweicloudsdkdwr.v3.ShowSystemTemplateDetailResponse`
        """
        http_info = self._show_system_template_detail_http_info(request)
        return self._call_api(**http_info)

    def show_system_template_detail_async_invoker(self, request):
        http_info = self._show_system_template_detail_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_system_template_detail_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/actiontemplate/{template_name}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowSystemTemplateDetailResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'template_name' in local_var_params:
            path_params['template_name'] = local_var_params['template_name']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["x-request-id", "Connection", "Content-Length", "Date", ]

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

    def show_third_template_info_async(self, request):
        r"""查询公共Action模板详情

        本接口用于按名称查询第三方模板详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowThirdTemplateInfo
        :type request: :class:`huaweicloudsdkdwr.v3.ShowThirdTemplateInfoRequest`
        :rtype: :class:`huaweicloudsdkdwr.v3.ShowThirdTemplateInfoResponse`
        """
        http_info = self._show_third_template_info_http_info(request)
        return self._call_api(**http_info)

    def show_third_template_info_async_invoker(self, request):
        http_info = self._show_third_template_info_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_third_template_info_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/myactiontemplate/{template_name}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowThirdTemplateInfoResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'template_name' in local_var_params:
            path_params['template_name'] = local_var_params['template_name']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["x-request-id", "Connection", "Content-Length", "Date", ]

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

    def show_workflow_instance_async(self, request):
        r"""本接口用于查询指定工作流实例详细

        本接口用于查询指定工作流实例详细。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowWorkflowInstance
        :type request: :class:`huaweicloudsdkdwr.v3.ShowWorkflowInstanceRequest`
        :rtype: :class:`huaweicloudsdkdwr.v3.ShowWorkflowInstanceResponse`
        """
        http_info = self._show_workflow_instance_http_info(request)
        return self._call_api(**http_info)

    def show_workflow_instance_async_invoker(self, request):
        http_info = self._show_workflow_instance_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_workflow_instance_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/workflows/{graph_name}/workflowexecution/{execution_name}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowWorkflowInstanceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["x-request-id", "Connection", "Content-Length", "Date", ]

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

    def update_my_action_template_async(self, request):
        r"""更新第三方算子模板

        本接口用于修改第三方算子和将三方算子提交审核
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateMyActionTemplate
        :type request: :class:`huaweicloudsdkdwr.v3.UpdateMyActionTemplateRequest`
        :rtype: :class:`huaweicloudsdkdwr.v3.UpdateMyActionTemplateResponse`
        """
        http_info = self._update_my_action_template_http_info(request)
        return self._call_api(**http_info)

    def update_my_action_template_async_invoker(self, request):
        http_info = self._update_my_action_template_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_my_action_template_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/myactiontemplates/{template_name}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateMyActionTemplateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'template_name' in local_var_params:
            path_params['template_name'] = local_var_params['template_name']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["x-request-id", "Connection", "Content-Length", "Date", ]

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

    def update_my_action_template_to_deprecated_async(self, request):
        r"""禁用第三方算子模板

        本接口用于申请禁用第三方算子。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateMyActionTemplateToDeprecated
        :type request: :class:`huaweicloudsdkdwr.v3.UpdateMyActionTemplateToDeprecatedRequest`
        :rtype: :class:`huaweicloudsdkdwr.v3.UpdateMyActionTemplateToDeprecatedResponse`
        """
        http_info = self._update_my_action_template_to_deprecated_http_info(request)
        return self._call_api(**http_info)

    def update_my_action_template_to_deprecated_async_invoker(self, request):
        http_info = self._update_my_action_template_to_deprecated_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_my_action_template_to_deprecated_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/myactiontemplates/{template_name}/forbid",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateMyActionTemplateToDeprecatedResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'template_name' in local_var_params:
            path_params['template_name'] = local_var_params['template_name']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["x-request-id", "Content-Length", ]

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
        r"""创建工作流

        本接口用于通过Body体直接创建工作流
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateWorkflow
        :type request: :class:`huaweicloudsdkdwr.v3.CreateWorkflowRequest`
        :rtype: :class:`huaweicloudsdkdwr.v3.CreateWorkflowResponse`
        """
        http_info = self._create_workflow_http_info(request)
        return self._call_api(**http_info)

    def create_workflow_async_invoker(self, request):
        http_info = self._create_workflow_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_workflow_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/workflows/{graph_name}",
            "request_type": request.__class__.__name__,
            "response_type": "CreateWorkflowResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'graph_name' in local_var_params:
            path_params['graph_name'] = local_var_params['graph_name']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["x-request-id", "Connection", "Content-Length", "Date", ]

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

    def delete_workflow_async(self, request):
        r"""删除工作流

        本接口用于删除工作流。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteWorkflow
        :type request: :class:`huaweicloudsdkdwr.v3.DeleteWorkflowRequest`
        :rtype: :class:`huaweicloudsdkdwr.v3.DeleteWorkflowResponse`
        """
        http_info = self._delete_workflow_http_info(request)
        return self._call_api(**http_info)

    def delete_workflow_async_invoker(self, request):
        http_info = self._delete_workflow_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_workflow_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{project_id}/workflows/{graph_name}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteWorkflowResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'graph_name' in local_var_params:
            path_params['graph_name'] = local_var_params['graph_name']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["x-request-id", "Content-Length", ]

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

    def list_workflows_async(self, request):
        r"""查询工作流列表

        本接口用于查询工作流列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListWorkflows
        :type request: :class:`huaweicloudsdkdwr.v3.ListWorkflowsRequest`
        :rtype: :class:`huaweicloudsdkdwr.v3.ListWorkflowsResponse`
        """
        http_info = self._list_workflows_http_info(request)
        return self._call_api(**http_info)

    def list_workflows_async_invoker(self, request):
        http_info = self._list_workflows_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_workflows_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/workflows",
            "request_type": request.__class__.__name__,
            "response_type": "ListWorkflowsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["x-request-id", "Connection", "Content-Length", "Date", ]

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

    def show_workflow_info_async(self, request):
        r"""查询工作流信息

        本接口用于根据工作流名称查询工作流详细信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowWorkflowInfo
        :type request: :class:`huaweicloudsdkdwr.v3.ShowWorkflowInfoRequest`
        :rtype: :class:`huaweicloudsdkdwr.v3.ShowWorkflowInfoResponse`
        """
        http_info = self._show_workflow_info_http_info(request)
        return self._call_api(**http_info)

    def show_workflow_info_async_invoker(self, request):
        http_info = self._show_workflow_info_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_workflow_info_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/workflows/{graph_name}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowWorkflowInfoResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'graph_name' in local_var_params:
            path_params['graph_name'] = local_var_params['graph_name']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["x-request-id", "Connection", "Content-Length", "Date", ]

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

    def update_workflow_async(self, request):
        r"""更新工作流

        Update Workflow
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateWorkflow
        :type request: :class:`huaweicloudsdkdwr.v3.UpdateWorkflowRequest`
        :rtype: :class:`huaweicloudsdkdwr.v3.UpdateWorkflowResponse`
        """
        http_info = self._update_workflow_http_info(request)
        return self._call_api(**http_info)

    def update_workflow_async_invoker(self, request):
        http_info = self._update_workflow_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_workflow_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/workflows/{graph_name}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateWorkflowResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'graph_name' in local_var_params:
            path_params['graph_name'] = local_var_params['graph_name']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["x-request-id", "Connection", "Content-Length", "Date", ]

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

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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdksa'")


class SaAsyncClient(Client):
    def __init__(self):
        super(SaAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdksa.v2.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "SaAsyncClient":
                raise TypeError("client type error, support client type is SaAsyncClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def create_alert_rule_async(self, request):
        r"""创建告警规则（仅支持华东-上海一使用）

        Create alert rule
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateAlertRule
        :type request: :class:`huaweicloudsdksa.v2.CreateAlertRuleRequest`
        :rtype: :class:`huaweicloudsdksa.v2.CreateAlertRuleResponse`
        """
        http_info = self._create_alert_rule_http_info(request)
        return self._call_api(**http_info)

    def create_alert_rule_async_invoker(self, request):
        http_info = self._create_alert_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_alert_rule_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/siem/alert-rules",
            "request_type": request.__class__.__name__,
            "response_type": "CreateAlertRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def create_alert_rule_simulation_async(self, request):
        r"""模拟告警规则（仅支持华东-上海一使用）

        Simulate alert rule
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateAlertRuleSimulation
        :type request: :class:`huaweicloudsdksa.v2.CreateAlertRuleSimulationRequest`
        :rtype: :class:`huaweicloudsdksa.v2.CreateAlertRuleSimulationResponse`
        """
        http_info = self._create_alert_rule_simulation_http_info(request)
        return self._call_api(**http_info)

    def create_alert_rule_simulation_async_invoker(self, request):
        http_info = self._create_alert_rule_simulation_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_alert_rule_simulation_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/siem/alert-rules/simulation",
            "request_type": request.__class__.__name__,
            "response_type": "CreateAlertRuleSimulationResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def delete_alert_rule_async(self, request):
        r"""删除告警规则（仅支持华东-上海一使用）

        Delete alert rule
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteAlertRule
        :type request: :class:`huaweicloudsdksa.v2.DeleteAlertRuleRequest`
        :rtype: :class:`huaweicloudsdksa.v2.DeleteAlertRuleResponse`
        """
        http_info = self._delete_alert_rule_http_info(request)
        return self._call_api(**http_info)

    def delete_alert_rule_async_invoker(self, request):
        http_info = self._delete_alert_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_alert_rule_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/siem/alert-rules",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteAlertRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def disable_alert_rule_async(self, request):
        r"""停用告警规则（仅支持华东-上海一使用）

        Disable alert rule
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DisableAlertRule
        :type request: :class:`huaweicloudsdksa.v2.DisableAlertRuleRequest`
        :rtype: :class:`huaweicloudsdksa.v2.DisableAlertRuleResponse`
        """
        http_info = self._disable_alert_rule_http_info(request)
        return self._call_api(**http_info)

    def disable_alert_rule_async_invoker(self, request):
        http_info = self._disable_alert_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _disable_alert_rule_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/siem/alert-rules/disable",
            "request_type": request.__class__.__name__,
            "response_type": "DisableAlertRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def enable_alert_rule_async(self, request):
        r"""启用告警规则（仅支持华东-上海一使用）

        Enable alert rule
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for EnableAlertRule
        :type request: :class:`huaweicloudsdksa.v2.EnableAlertRuleRequest`
        :rtype: :class:`huaweicloudsdksa.v2.EnableAlertRuleResponse`
        """
        http_info = self._enable_alert_rule_http_info(request)
        return self._call_api(**http_info)

    def enable_alert_rule_async_invoker(self, request):
        http_info = self._enable_alert_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _enable_alert_rule_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/siem/alert-rules/enable",
            "request_type": request.__class__.__name__,
            "response_type": "EnableAlertRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def list_alert_rule_metrics_async(self, request):
        r"""告警规则总览（仅支持华东-上海一使用）

        List alert rule metrics
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAlertRuleMetrics
        :type request: :class:`huaweicloudsdksa.v2.ListAlertRuleMetricsRequest`
        :rtype: :class:`huaweicloudsdksa.v2.ListAlertRuleMetricsResponse`
        """
        http_info = self._list_alert_rule_metrics_http_info(request)
        return self._call_api(**http_info)

    def list_alert_rule_metrics_async_invoker(self, request):
        http_info = self._list_alert_rule_metrics_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_alert_rule_metrics_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/siem/alert-rules/metrics",
            "request_type": request.__class__.__name__,
            "response_type": "ListAlertRuleMetricsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def list_alert_rule_templates_async(self, request):
        r"""列出告警规则模板（仅支持华东-上海一使用）

        List alert rule templates
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAlertRuleTemplates
        :type request: :class:`huaweicloudsdksa.v2.ListAlertRuleTemplatesRequest`
        :rtype: :class:`huaweicloudsdksa.v2.ListAlertRuleTemplatesResponse`
        """
        http_info = self._list_alert_rule_templates_http_info(request)
        return self._call_api(**http_info)

    def list_alert_rule_templates_async_invoker(self, request):
        http_info = self._list_alert_rule_templates_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_alert_rule_templates_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/siem/alert-rules/templates",
            "request_type": request.__class__.__name__,
            "response_type": "ListAlertRuleTemplatesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
        if 'severity' in local_var_params:
            query_params.append(('severity', local_var_params['severity']))
            collection_formats['severity'] = 'csv'

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def list_alert_rules_async(self, request):
        r"""列出告警规则（仅支持华东-上海一使用）

        List alert rules
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAlertRules
        :type request: :class:`huaweicloudsdksa.v2.ListAlertRulesRequest`
        :rtype: :class:`huaweicloudsdksa.v2.ListAlertRulesResponse`
        """
        http_info = self._list_alert_rules_http_info(request)
        return self._call_api(**http_info)

    def list_alert_rules_async_invoker(self, request):
        http_info = self._list_alert_rules_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_alert_rules_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/siem/alert-rules",
            "request_type": request.__class__.__name__,
            "response_type": "ListAlertRulesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
        if 'pipe_id' in local_var_params:
            query_params.append(('pipe_id', local_var_params['pipe_id']))
        if 'rule_name' in local_var_params:
            query_params.append(('rule_name', local_var_params['rule_name']))
        if 'rule_id' in local_var_params:
            query_params.append(('rule_id', local_var_params['rule_id']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
            collection_formats['status'] = 'csv'
        if 'severity' in local_var_params:
            query_params.append(('severity', local_var_params['severity']))
            collection_formats['severity'] = 'csv'

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def show_alert_rule_async(self, request):
        r"""查看告警规则（仅支持华东-上海一使用）

        Get alert rule
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowAlertRule
        :type request: :class:`huaweicloudsdksa.v2.ShowAlertRuleRequest`
        :rtype: :class:`huaweicloudsdksa.v2.ShowAlertRuleResponse`
        """
        http_info = self._show_alert_rule_http_info(request)
        return self._call_api(**http_info)

    def show_alert_rule_async_invoker(self, request):
        http_info = self._show_alert_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_alert_rule_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/siem/alert-rules/{rule_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAlertRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'rule_id' in local_var_params:
            path_params['rule_id'] = local_var_params['rule_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def show_alert_rule_template_async(self, request):
        r"""查看告警规则模板（仅支持华东-上海一使用）

        List alert rule templates
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowAlertRuleTemplate
        :type request: :class:`huaweicloudsdksa.v2.ShowAlertRuleTemplateRequest`
        :rtype: :class:`huaweicloudsdksa.v2.ShowAlertRuleTemplateResponse`
        """
        http_info = self._show_alert_rule_template_http_info(request)
        return self._call_api(**http_info)

    def show_alert_rule_template_async_invoker(self, request):
        http_info = self._show_alert_rule_template_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_alert_rule_template_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/siem/alert-rules/templates/{template_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAlertRuleTemplateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'template_id' in local_var_params:
            path_params['template_id'] = local_var_params['template_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def update_alert_rule_async(self, request):
        r"""更新告警规则（仅支持华东-上海一使用）

        Update alert rule
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateAlertRule
        :type request: :class:`huaweicloudsdksa.v2.UpdateAlertRuleRequest`
        :rtype: :class:`huaweicloudsdksa.v2.UpdateAlertRuleResponse`
        """
        http_info = self._update_alert_rule_http_info(request)
        return self._call_api(**http_info)

    def update_alert_rule_async_invoker(self, request):
        http_info = self._update_alert_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_alert_rule_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/siem/alert-rules/{rule_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateAlertRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'rule_id' in local_var_params:
            path_params['rule_id'] = local_var_params['rule_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def change_alert_async(self, request):
        r"""更新告警（仅支持华东-上海一使用）

        编辑告警，根据实际修改的属性更新，未修改的列不更新
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ChangeAlert
        :type request: :class:`huaweicloudsdksa.v2.ChangeAlertRequest`
        :rtype: :class:`huaweicloudsdksa.v2.ChangeAlertResponse`
        """
        http_info = self._change_alert_http_info(request)
        return self._call_api(**http_info)

    def change_alert_async_invoker(self, request):
        http_info = self._change_alert_http_info(request)
        return AsyncInvoker(self, http_info)

    def _change_alert_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/alerts/{alert_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ChangeAlertResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'alert_id' in local_var_params:
            path_params['alert_id'] = local_var_params['alert_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def create_alert_async(self, request):
        r"""创建告警（仅支持华东-上海一使用）

        创建告警
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateAlert
        :type request: :class:`huaweicloudsdksa.v2.CreateAlertRequest`
        :rtype: :class:`huaweicloudsdksa.v2.CreateAlertResponse`
        """
        http_info = self._create_alert_http_info(request)
        return self._call_api(**http_info)

    def create_alert_async_invoker(self, request):
        http_info = self._create_alert_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_alert_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/alerts",
            "request_type": request.__class__.__name__,
            "response_type": "CreateAlertResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def create_batch_order_alerts_async(self, request):
        r"""告警转事件（仅支持华东-上海一使用）

        告警转事件
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateBatchOrderAlerts
        :type request: :class:`huaweicloudsdksa.v2.CreateBatchOrderAlertsRequest`
        :rtype: :class:`huaweicloudsdksa.v2.CreateBatchOrderAlertsResponse`
        """
        http_info = self._create_batch_order_alerts_http_info(request)
        return self._call_api(**http_info)

    def create_batch_order_alerts_async_invoker(self, request):
        http_info = self._create_batch_order_alerts_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_batch_order_alerts_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/alerts/batch-order",
            "request_type": request.__class__.__name__,
            "response_type": "CreateBatchOrderAlertsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def delete_alert_async(self, request):
        r"""删除告警（仅支持华东-上海一使用）

        删除告警
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteAlert
        :type request: :class:`huaweicloudsdksa.v2.DeleteAlertRequest`
        :rtype: :class:`huaweicloudsdksa.v2.DeleteAlertResponse`
        """
        http_info = self._delete_alert_http_info(request)
        return self._call_api(**http_info)

    def delete_alert_async_invoker(self, request):
        http_info = self._delete_alert_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_alert_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/alerts",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteAlertResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def list_alerts_async(self, request):
        r"""搜索告警列表（仅支持华东-上海一使用）

        搜索告警列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAlerts
        :type request: :class:`huaweicloudsdksa.v2.ListAlertsRequest`
        :rtype: :class:`huaweicloudsdksa.v2.ListAlertsResponse`
        """
        http_info = self._list_alerts_http_info(request)
        return self._call_api(**http_info)

    def list_alerts_async_invoker(self, request):
        http_info = self._list_alerts_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_alerts_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/alerts/search",
            "request_type": request.__class__.__name__,
            "response_type": "ListAlertsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def show_alert_async(self, request):
        r"""获取告警详情（仅支持华东-上海一使用）

        获取告警详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowAlert
        :type request: :class:`huaweicloudsdksa.v2.ShowAlertRequest`
        :rtype: :class:`huaweicloudsdksa.v2.ShowAlertResponse`
        """
        http_info = self._show_alert_http_info(request)
        return self._call_api(**http_info)

    def show_alert_async_invoker(self, request):
        http_info = self._show_alert_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_alert_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/alerts/{alert_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAlertResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'alert_id' in local_var_params:
            path_params['alert_id'] = local_var_params['alert_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def change_incident_async(self, request):
        r"""更新事件（仅支持华东-上海一使用）

        编辑事件，根据实际修改的属性更新，未修改的列不更新
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ChangeIncident
        :type request: :class:`huaweicloudsdksa.v2.ChangeIncidentRequest`
        :rtype: :class:`huaweicloudsdksa.v2.ChangeIncidentResponse`
        """
        http_info = self._change_incident_http_info(request)
        return self._call_api(**http_info)

    def change_incident_async_invoker(self, request):
        http_info = self._change_incident_http_info(request)
        return AsyncInvoker(self, http_info)

    def _change_incident_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/incidents/{incident_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ChangeIncidentResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'incident_id' in local_var_params:
            path_params['incident_id'] = local_var_params['incident_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def create_incident_async(self, request):
        r"""创建事件（仅支持华东-上海一使用）

        创建事件
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateIncident
        :type request: :class:`huaweicloudsdksa.v2.CreateIncidentRequest`
        :rtype: :class:`huaweicloudsdksa.v2.CreateIncidentResponse`
        """
        http_info = self._create_incident_http_info(request)
        return self._call_api(**http_info)

    def create_incident_async_invoker(self, request):
        http_info = self._create_incident_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_incident_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/incidents",
            "request_type": request.__class__.__name__,
            "response_type": "CreateIncidentResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def delete_incident_async(self, request):
        r"""创建事件（仅支持华东-上海一使用）

        创建事件
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteIncident
        :type request: :class:`huaweicloudsdksa.v2.DeleteIncidentRequest`
        :rtype: :class:`huaweicloudsdksa.v2.DeleteIncidentResponse`
        """
        http_info = self._delete_incident_http_info(request)
        return self._call_api(**http_info)

    def delete_incident_async_invoker(self, request):
        http_info = self._delete_incident_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_incident_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/incidents",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteIncidentResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def list_incident_types_async(self, request):
        r"""获取事件的类型列表（仅支持华东-上海一使用）

        获取事件的类型列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListIncidentTypes
        :type request: :class:`huaweicloudsdksa.v2.ListIncidentTypesRequest`
        :rtype: :class:`huaweicloudsdksa.v2.ListIncidentTypesResponse`
        """
        http_info = self._list_incident_types_http_info(request)
        return self._call_api(**http_info)

    def list_incident_types_async_invoker(self, request):
        http_info = self._list_incident_types_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_incident_types_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/incidents/types",
            "request_type": request.__class__.__name__,
            "response_type": "ListIncidentTypesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

        query_params = []
        if 'parent_business_code' in local_var_params:
            query_params.append(('parent_business_code', local_var_params['parent_business_code']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'order' in local_var_params:
            query_params.append(('order', local_var_params['order']))
        if 'sortby' in local_var_params:
            query_params.append(('sortby', local_var_params['sortby']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'enabled' in local_var_params:
            query_params.append(('enabled', local_var_params['enabled']))
        if 'layout_name' in local_var_params:
            query_params.append(('layout_name', local_var_params['layout_name']))
        if 'is_built_in' in local_var_params:
            query_params.append(('is_built_in', local_var_params['is_built_in']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def list_incidents_async(self, request):
        r"""搜索事件列表（仅支持华东-上海一使用）

        搜索事件列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListIncidents
        :type request: :class:`huaweicloudsdksa.v2.ListIncidentsRequest`
        :rtype: :class:`huaweicloudsdksa.v2.ListIncidentsResponse`
        """
        http_info = self._list_incidents_http_info(request)
        return self._call_api(**http_info)

    def list_incidents_async_invoker(self, request):
        http_info = self._list_incidents_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_incidents_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/incidents/search",
            "request_type": request.__class__.__name__,
            "response_type": "ListIncidentsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def show_incident_async(self, request):
        r"""获取事件详情（仅支持华东-上海一使用）

        获取事件详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowIncident
        :type request: :class:`huaweicloudsdksa.v2.ShowIncidentRequest`
        :rtype: :class:`huaweicloudsdksa.v2.ShowIncidentResponse`
        """
        http_info = self._show_incident_http_info(request)
        return self._call_api(**http_info)

    def show_incident_async_invoker(self, request):
        http_info = self._show_incident_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_incident_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/incidents/{incident_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowIncidentResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'incident_id' in local_var_params:
            path_params['incident_id'] = local_var_params['incident_id']

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

    def create_indicator_async(self, request):
        r"""创建指标

        创建指标（仅支持华东-上海一使用）
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateIndicator
        :type request: :class:`huaweicloudsdksa.v2.CreateIndicatorRequest`
        :rtype: :class:`huaweicloudsdksa.v2.CreateIndicatorResponse`
        """
        http_info = self._create_indicator_http_info(request)
        return self._call_api(**http_info)

    def create_indicator_async_invoker(self, request):
        http_info = self._create_indicator_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_indicator_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/indicators",
            "request_type": request.__class__.__name__,
            "response_type": "CreateIndicatorResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def delete_indicator_async(self, request):
        r"""删除指标

        删除指标（仅支持华东-上海一使用）
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteIndicator
        :type request: :class:`huaweicloudsdksa.v2.DeleteIndicatorRequest`
        :rtype: :class:`huaweicloudsdksa.v2.DeleteIndicatorResponse`
        """
        http_info = self._delete_indicator_http_info(request)
        return self._call_api(**http_info)

    def delete_indicator_async_invoker(self, request):
        http_info = self._delete_indicator_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_indicator_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/indicators",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteIndicatorResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def list_indicators_async(self, request):
        r"""查询指标列表（仅支持华东-上海一使用）

        List all indicators
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListIndicators
        :type request: :class:`huaweicloudsdksa.v2.ListIndicatorsRequest`
        :rtype: :class:`huaweicloudsdksa.v2.ListIndicatorsResponse`
        """
        http_info = self._list_indicators_http_info(request)
        return self._call_api(**http_info)

    def list_indicators_async_invoker(self, request):
        http_info = self._list_indicators_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_indicators_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/indicators/search",
            "request_type": request.__class__.__name__,
            "response_type": "ListIndicatorsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

        query_params = []
        if 'order' in local_var_params:
            query_params.append(('order', local_var_params['order']))
        if 'from_date' in local_var_params:
            query_params.append(('from_date', local_var_params['from_date']))
        if 'to_date' in local_var_params:
            query_params.append(('to_date', local_var_params['to_date']))

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def show_indicator_detail_async(self, request):
        r"""查询指标详情

        查询指标详情（仅支持华东-上海一使用）
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowIndicatorDetail
        :type request: :class:`huaweicloudsdksa.v2.ShowIndicatorDetailRequest`
        :rtype: :class:`huaweicloudsdksa.v2.ShowIndicatorDetailResponse`
        """
        http_info = self._show_indicator_detail_http_info(request)
        return self._call_api(**http_info)

    def show_indicator_detail_async_invoker(self, request):
        http_info = self._show_indicator_detail_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_indicator_detail_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/indicators/{indicator_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowIndicatorDetailResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'indicator_id' in local_var_params:
            path_params['indicator_id'] = local_var_params['indicator_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def update_indicator_async(self, request):
        r"""更新指标

        更新指标（仅支持华东-上海一使用）
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateIndicator
        :type request: :class:`huaweicloudsdksa.v2.UpdateIndicatorRequest`
        :rtype: :class:`huaweicloudsdksa.v2.UpdateIndicatorResponse`
        """
        http_info = self._update_indicator_http_info(request)
        return self._call_api(**http_info)

    def update_indicator_async_invoker(self, request):
        http_info = self._update_indicator_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_indicator_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/indicators/{indicator_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateIndicatorResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'indicator_id' in local_var_params:
            path_params['indicator_id'] = local_var_params['indicator_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def create_playbook_async(self, request):
        r"""创建剧本（仅支持华东-上海一使用）

        Create playbook.
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreatePlaybook
        :type request: :class:`huaweicloudsdksa.v2.CreatePlaybookRequest`
        :rtype: :class:`huaweicloudsdksa.v2.CreatePlaybookResponse`
        """
        http_info = self._create_playbook_http_info(request)
        return self._call_api(**http_info)

    def create_playbook_async_invoker(self, request):
        http_info = self._create_playbook_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_playbook_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/playbooks",
            "request_type": request.__class__.__name__,
            "response_type": "CreatePlaybookResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def delete_playbook_async(self, request):
        r"""删除剧本（仅支持华东-上海一使用）

        Delete playbook.
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeletePlaybook
        :type request: :class:`huaweicloudsdksa.v2.DeletePlaybookRequest`
        :rtype: :class:`huaweicloudsdksa.v2.DeletePlaybookResponse`
        """
        http_info = self._delete_playbook_http_info(request)
        return self._call_api(**http_info)

    def delete_playbook_async_invoker(self, request):
        http_info = self._delete_playbook_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_playbook_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/playbooks/{playbook_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeletePlaybookResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'playbook_id' in local_var_params:
            path_params['playbook_id'] = local_var_params['playbook_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def list_playbooks_async(self, request):
        r"""查询剧本列表（仅支持华东-上海一使用）

        List all playbooks.
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListPlaybooks
        :type request: :class:`huaweicloudsdksa.v2.ListPlaybooksRequest`
        :rtype: :class:`huaweicloudsdksa.v2.ListPlaybooksResponse`
        """
        http_info = self._list_playbooks_http_info(request)
        return self._call_api(**http_info)

    def list_playbooks_async_invoker(self, request):
        http_info = self._list_playbooks_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_playbooks_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/playbooks",
            "request_type": request.__class__.__name__,
            "response_type": "ListPlaybooksResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

        query_params = []
        if 'search_txt' in local_var_params:
            query_params.append(('search_txt', local_var_params['search_txt']))
        if 'component_id' in local_var_params:
            query_params.append(('component_id', local_var_params['component_id']))
        if 'enabled' in local_var_params:
            query_params.append(('enabled', local_var_params['enabled']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'description' in local_var_params:
            query_params.append(('description', local_var_params['description']))
        if 'dataclass_name' in local_var_params:
            query_params.append(('dataclass_name', local_var_params['dataclass_name']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def show_playbook_async(self, request):
        r"""查询剧本详情（仅支持华东-上海一使用）

        Show playbook
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowPlaybook
        :type request: :class:`huaweicloudsdksa.v2.ShowPlaybookRequest`
        :rtype: :class:`huaweicloudsdksa.v2.ShowPlaybookResponse`
        """
        http_info = self._show_playbook_http_info(request)
        return self._call_api(**http_info)

    def show_playbook_async_invoker(self, request):
        http_info = self._show_playbook_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_playbook_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/playbooks/{playbook_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowPlaybookResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'playbook_id' in local_var_params:
            path_params['playbook_id'] = local_var_params['playbook_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def show_playbook_monitors_async(self, request):
        r"""剧本运行监控（仅支持华东-上海一使用）

        剧本运行监控
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowPlaybookMonitors
        :type request: :class:`huaweicloudsdksa.v2.ShowPlaybookMonitorsRequest`
        :rtype: :class:`huaweicloudsdksa.v2.ShowPlaybookMonitorsResponse`
        """
        http_info = self._show_playbook_monitors_http_info(request)
        return self._call_api(**http_info)

    def show_playbook_monitors_async_invoker(self, request):
        http_info = self._show_playbook_monitors_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_playbook_monitors_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/playbooks/{playbook_id}/monitor",
            "request_type": request.__class__.__name__,
            "response_type": "ShowPlaybookMonitorsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'playbook_id' in local_var_params:
            path_params['playbook_id'] = local_var_params['playbook_id']

        query_params = []
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'version_query_type' in local_var_params:
            query_params.append(('version_query_type', local_var_params['version_query_type']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def show_playbook_statistics_async(self, request):
        r"""剧本数据统计（仅支持华东-上海一使用）

        剧本统计数据
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowPlaybookStatistics
        :type request: :class:`huaweicloudsdksa.v2.ShowPlaybookStatisticsRequest`
        :rtype: :class:`huaweicloudsdksa.v2.ShowPlaybookStatisticsResponse`
        """
        http_info = self._show_playbook_statistics_http_info(request)
        return self._call_api(**http_info)

    def show_playbook_statistics_async_invoker(self, request):
        http_info = self._show_playbook_statistics_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_playbook_statistics_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/playbooks/statistics",
            "request_type": request.__class__.__name__,
            "response_type": "ShowPlaybookStatisticsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def update_playbook_async(self, request):
        r"""修改剧本（仅支持华东-上海一使用）

        Update playbook.
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdatePlaybook
        :type request: :class:`huaweicloudsdksa.v2.UpdatePlaybookRequest`
        :rtype: :class:`huaweicloudsdksa.v2.UpdatePlaybookResponse`
        """
        http_info = self._update_playbook_http_info(request)
        return self._call_api(**http_info)

    def update_playbook_async_invoker(self, request):
        http_info = self._update_playbook_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_playbook_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/playbooks/{playbook_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdatePlaybookResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'playbook_id' in local_var_params:
            path_params['playbook_id'] = local_var_params['playbook_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def create_playbook_action_async(self, request):
        r"""创建剧本动作（仅支持华东-上海一使用）

        Create action.
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreatePlaybookAction
        :type request: :class:`huaweicloudsdksa.v2.CreatePlaybookActionRequest`
        :rtype: :class:`huaweicloudsdksa.v2.CreatePlaybookActionResponse`
        """
        http_info = self._create_playbook_action_http_info(request)
        return self._call_api(**http_info)

    def create_playbook_action_async_invoker(self, request):
        http_info = self._create_playbook_action_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_playbook_action_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/playbooks/versions/{version_id}/actions",
            "request_type": request.__class__.__name__,
            "response_type": "CreatePlaybookActionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'version_id' in local_var_params:
            path_params['version_id'] = local_var_params['version_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def delete_playbook_action_async(self, request):
        r"""删除剧本动作（仅支持华东-上海一使用）

        Delete action.
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeletePlaybookAction
        :type request: :class:`huaweicloudsdksa.v2.DeletePlaybookActionRequest`
        :rtype: :class:`huaweicloudsdksa.v2.DeletePlaybookActionResponse`
        """
        http_info = self._delete_playbook_action_http_info(request)
        return self._call_api(**http_info)

    def delete_playbook_action_async_invoker(self, request):
        http_info = self._delete_playbook_action_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_playbook_action_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/playbooks/versions/{version_id}/actions/{action_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeletePlaybookActionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'version_id' in local_var_params:
            path_params['version_id'] = local_var_params['version_id']
        if 'action_id' in local_var_params:
            path_params['action_id'] = local_var_params['action_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def list_playbook_actions_async(self, request):
        r"""查询剧本动作（仅支持华东-上海一使用）

        List all actions.
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListPlaybookActions
        :type request: :class:`huaweicloudsdksa.v2.ListPlaybookActionsRequest`
        :rtype: :class:`huaweicloudsdksa.v2.ListPlaybookActionsResponse`
        """
        http_info = self._list_playbook_actions_http_info(request)
        return self._call_api(**http_info)

    def list_playbook_actions_async_invoker(self, request):
        http_info = self._list_playbook_actions_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_playbook_actions_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/playbooks/versions/{version_id}/actions",
            "request_type": request.__class__.__name__,
            "response_type": "ListPlaybookActionsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'version_id' in local_var_params:
            path_params['version_id'] = local_var_params['version_id']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def update_playbook_action_async(self, request):
        r"""更新剧本动作（仅支持华东-上海一使用）

        Update action.
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdatePlaybookAction
        :type request: :class:`huaweicloudsdksa.v2.UpdatePlaybookActionRequest`
        :rtype: :class:`huaweicloudsdksa.v2.UpdatePlaybookActionResponse`
        """
        http_info = self._update_playbook_action_http_info(request)
        return self._call_api(**http_info)

    def update_playbook_action_async_invoker(self, request):
        http_info = self._update_playbook_action_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_playbook_action_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/playbooks/versions/{version_id}/actions/{action_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdatePlaybookActionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'version_id' in local_var_params:
            path_params['version_id'] = local_var_params['version_id']
        if 'action_id' in local_var_params:
            path_params['action_id'] = local_var_params['action_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def create_playbook_approve_async(self, request):
        r"""审核剧本（仅支持华东-上海一使用）

        Create playbook approve.
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreatePlaybookApprove
        :type request: :class:`huaweicloudsdksa.v2.CreatePlaybookApproveRequest`
        :rtype: :class:`huaweicloudsdksa.v2.CreatePlaybookApproveResponse`
        """
        http_info = self._create_playbook_approve_http_info(request)
        return self._call_api(**http_info)

    def create_playbook_approve_async_invoker(self, request):
        http_info = self._create_playbook_approve_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_playbook_approve_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/playbooks/versions/{version_id}/approval",
            "request_type": request.__class__.__name__,
            "response_type": "CreatePlaybookApproveResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'version_id' in local_var_params:
            path_params['version_id'] = local_var_params['version_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def list_playbook_approves_async(self, request):
        r"""查询剧本审核结果（仅支持华东-上海一使用）

        List approves.
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListPlaybookApproves
        :type request: :class:`huaweicloudsdksa.v2.ListPlaybookApprovesRequest`
        :rtype: :class:`huaweicloudsdksa.v2.ListPlaybookApprovesResponse`
        """
        http_info = self._list_playbook_approves_http_info(request)
        return self._call_api(**http_info)

    def list_playbook_approves_async_invoker(self, request):
        http_info = self._list_playbook_approves_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_playbook_approves_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/playbooks/versions/approval",
            "request_type": request.__class__.__name__,
            "response_type": "ListPlaybookApprovesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

        query_params = []
        if 'resource_id' in local_var_params:
            query_params.append(('resource_id', local_var_params['resource_id']))
        if 'approve_type' in local_var_params:
            query_params.append(('approve_type', local_var_params['approve_type']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def change_playbook_instance_async(self, request):
        r"""操作剧本实例（仅支持华东-上海一使用）

        Operation Playbook Instance.
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ChangePlaybookInstance
        :type request: :class:`huaweicloudsdksa.v2.ChangePlaybookInstanceRequest`
        :rtype: :class:`huaweicloudsdksa.v2.ChangePlaybookInstanceResponse`
        """
        http_info = self._change_playbook_instance_http_info(request)
        return self._call_api(**http_info)

    def change_playbook_instance_async_invoker(self, request):
        http_info = self._change_playbook_instance_http_info(request)
        return AsyncInvoker(self, http_info)

    def _change_playbook_instance_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/playbooks/instances/{instance_id}/operation",
            "request_type": request.__class__.__name__,
            "response_type": "ChangePlaybookInstanceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def list_playbook_audit_logs_async(self, request):
        r"""查询剧本实例审计日志（仅支持华东-上海一使用）

        List audit logs.
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListPlaybookAuditLogs
        :type request: :class:`huaweicloudsdksa.v2.ListPlaybookAuditLogsRequest`
        :rtype: :class:`huaweicloudsdksa.v2.ListPlaybookAuditLogsResponse`
        """
        http_info = self._list_playbook_audit_logs_http_info(request)
        return self._call_api(**http_info)

    def list_playbook_audit_logs_async_invoker(self, request):
        http_info = self._list_playbook_audit_logs_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_playbook_audit_logs_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/playbooks/instances/auditlogs",
            "request_type": request.__class__.__name__,
            "response_type": "ListPlaybookAuditLogsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def list_playbook_instances_async(self, request):
        r"""查询剧本实例列表（仅支持华东-上海一使用）

        List playbook instances
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListPlaybookInstances
        :type request: :class:`huaweicloudsdksa.v2.ListPlaybookInstancesRequest`
        :rtype: :class:`huaweicloudsdksa.v2.ListPlaybookInstancesResponse`
        """
        http_info = self._list_playbook_instances_http_info(request)
        return self._call_api(**http_info)

    def list_playbook_instances_async_invoker(self, request):
        http_info = self._list_playbook_instances_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_playbook_instances_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/playbooks/instances",
            "request_type": request.__class__.__name__,
            "response_type": "ListPlaybookInstancesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

        query_params = []
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'date_type' in local_var_params:
            query_params.append(('date_type', local_var_params['date_type']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'playbook_name' in local_var_params:
            query_params.append(('playbook_name', local_var_params['playbook_name']))
        if 'dataclass_name' in local_var_params:
            query_params.append(('dataclass_name', local_var_params['dataclass_name']))
        if 'dataobject_name' in local_var_params:
            query_params.append(('dataobject_name', local_var_params['dataobject_name']))
        if 'trigger_type' in local_var_params:
            query_params.append(('trigger_type', local_var_params['trigger_type']))
        if 'from_date' in local_var_params:
            query_params.append(('from_date', local_var_params['from_date']))
        if 'to_date' in local_var_params:
            query_params.append(('to_date', local_var_params['to_date']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def show_playbook_instance_async(self, request):
        r"""查询剧本实例详情（仅支持华东-上海一使用）

        Show playbook instance
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowPlaybookInstance
        :type request: :class:`huaweicloudsdksa.v2.ShowPlaybookInstanceRequest`
        :rtype: :class:`huaweicloudsdksa.v2.ShowPlaybookInstanceResponse`
        """
        http_info = self._show_playbook_instance_http_info(request)
        return self._call_api(**http_info)

    def show_playbook_instance_async_invoker(self, request):
        http_info = self._show_playbook_instance_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_playbook_instance_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/playbooks/instances/{instance_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowPlaybookInstanceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def show_playbook_topology_async(self, request):
        r"""查询剧本拓扑关系（仅支持华东-上海一使用）

        Show playbook Topology
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowPlaybookTopology
        :type request: :class:`huaweicloudsdksa.v2.ShowPlaybookTopologyRequest`
        :rtype: :class:`huaweicloudsdksa.v2.ShowPlaybookTopologyResponse`
        """
        http_info = self._show_playbook_topology_http_info(request)
        return self._call_api(**http_info)

    def show_playbook_topology_async_invoker(self, request):
        http_info = self._show_playbook_topology_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_playbook_topology_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/playbooks/instances/{instance_id}/topology",
            "request_type": request.__class__.__name__,
            "response_type": "ShowPlaybookTopologyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def create_playbook_rule_async(self, request):
        r"""创建剧本规则（仅支持华东-上海一使用）

        Create rule.
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreatePlaybookRule
        :type request: :class:`huaweicloudsdksa.v2.CreatePlaybookRuleRequest`
        :rtype: :class:`huaweicloudsdksa.v2.CreatePlaybookRuleResponse`
        """
        http_info = self._create_playbook_rule_http_info(request)
        return self._call_api(**http_info)

    def create_playbook_rule_async_invoker(self, request):
        http_info = self._create_playbook_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_playbook_rule_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/playbooks/versions/{version_id}/rules",
            "request_type": request.__class__.__name__,
            "response_type": "CreatePlaybookRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'version_id' in local_var_params:
            path_params['version_id'] = local_var_params['version_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def delete_playbook_rule_async(self, request):
        r"""删除剧本规则（仅支持华东-上海一使用）

        Delete rule.
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeletePlaybookRule
        :type request: :class:`huaweicloudsdksa.v2.DeletePlaybookRuleRequest`
        :rtype: :class:`huaweicloudsdksa.v2.DeletePlaybookRuleResponse`
        """
        http_info = self._delete_playbook_rule_http_info(request)
        return self._call_api(**http_info)

    def delete_playbook_rule_async_invoker(self, request):
        http_info = self._delete_playbook_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_playbook_rule_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/playbooks/versions/{version_id}/rules/{rule_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeletePlaybookRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'version_id' in local_var_params:
            path_params['version_id'] = local_var_params['version_id']
        if 'rule_id' in local_var_params:
            path_params['rule_id'] = local_var_params['rule_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def show_playbook_rule_async(self, request):
        r"""查询剧本规则详情（仅支持华东-上海一使用）

        Show rule formation.
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowPlaybookRule
        :type request: :class:`huaweicloudsdksa.v2.ShowPlaybookRuleRequest`
        :rtype: :class:`huaweicloudsdksa.v2.ShowPlaybookRuleResponse`
        """
        http_info = self._show_playbook_rule_http_info(request)
        return self._call_api(**http_info)

    def show_playbook_rule_async_invoker(self, request):
        http_info = self._show_playbook_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_playbook_rule_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/playbooks/versions/{version_id}/rules/{rule_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowPlaybookRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'version_id' in local_var_params:
            path_params['version_id'] = local_var_params['version_id']
        if 'rule_id' in local_var_params:
            path_params['rule_id'] = local_var_params['rule_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def update_playbook_rule_async(self, request):
        r"""更新剧本规则（仅支持华东-上海一使用）

        Update rule.
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdatePlaybookRule
        :type request: :class:`huaweicloudsdksa.v2.UpdatePlaybookRuleRequest`
        :rtype: :class:`huaweicloudsdksa.v2.UpdatePlaybookRuleResponse`
        """
        http_info = self._update_playbook_rule_http_info(request)
        return self._call_api(**http_info)

    def update_playbook_rule_async_invoker(self, request):
        http_info = self._update_playbook_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_playbook_rule_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/playbooks/versions/{version_id}/rules/{rule_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdatePlaybookRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'version_id' in local_var_params:
            path_params['version_id'] = local_var_params['version_id']
        if 'rule_id' in local_var_params:
            path_params['rule_id'] = local_var_params['rule_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def copy_playbook_version_async(self, request):
        r"""克隆剧本及版本（仅支持华东-上海一使用）

        Copy Playbook and version to a new one
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CopyPlaybookVersion
        :type request: :class:`huaweicloudsdksa.v2.CopyPlaybookVersionRequest`
        :rtype: :class:`huaweicloudsdksa.v2.CopyPlaybookVersionResponse`
        """
        http_info = self._copy_playbook_version_http_info(request)
        return self._call_api(**http_info)

    def copy_playbook_version_async_invoker(self, request):
        http_info = self._copy_playbook_version_http_info(request)
        return AsyncInvoker(self, http_info)

    def _copy_playbook_version_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/playbooks/versions/{version_id}/clone",
            "request_type": request.__class__.__name__,
            "response_type": "CopyPlaybookVersionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'version_id' in local_var_params:
            path_params['version_id'] = local_var_params['version_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def create_playbook_version_async(self, request):
        r"""创建剧本版本（仅支持华东-上海一使用）

        Create playbook version.
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreatePlaybookVersion
        :type request: :class:`huaweicloudsdksa.v2.CreatePlaybookVersionRequest`
        :rtype: :class:`huaweicloudsdksa.v2.CreatePlaybookVersionResponse`
        """
        http_info = self._create_playbook_version_http_info(request)
        return self._call_api(**http_info)

    def create_playbook_version_async_invoker(self, request):
        http_info = self._create_playbook_version_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_playbook_version_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/playbooks/{playbook_id}/versions",
            "request_type": request.__class__.__name__,
            "response_type": "CreatePlaybookVersionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'playbook_id' in local_var_params:
            path_params['playbook_id'] = local_var_params['playbook_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def delete_playbook_version_async(self, request):
        r"""删除剧本版本（仅支持华东-上海一使用）

        Delete playbook version.
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeletePlaybookVersion
        :type request: :class:`huaweicloudsdksa.v2.DeletePlaybookVersionRequest`
        :rtype: :class:`huaweicloudsdksa.v2.DeletePlaybookVersionResponse`
        """
        http_info = self._delete_playbook_version_http_info(request)
        return self._call_api(**http_info)

    def delete_playbook_version_async_invoker(self, request):
        http_info = self._delete_playbook_version_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_playbook_version_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/playbooks/versions/{version_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeletePlaybookVersionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'version_id' in local_var_params:
            path_params['version_id'] = local_var_params['version_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def list_playbook_versions_async(self, request):
        r"""查询剧本版本列表（仅支持华东-上海一使用）

        List all versions of playbook.
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListPlaybookVersions
        :type request: :class:`huaweicloudsdksa.v2.ListPlaybookVersionsRequest`
        :rtype: :class:`huaweicloudsdksa.v2.ListPlaybookVersionsResponse`
        """
        http_info = self._list_playbook_versions_http_info(request)
        return self._call_api(**http_info)

    def list_playbook_versions_async_invoker(self, request):
        http_info = self._list_playbook_versions_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_playbook_versions_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/playbooks/{playbook_id}/versions",
            "request_type": request.__class__.__name__,
            "response_type": "ListPlaybookVersionsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'playbook_id' in local_var_params:
            path_params['playbook_id'] = local_var_params['playbook_id']

        query_params = []
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'enabled' in local_var_params:
            query_params.append(('enabled', local_var_params['enabled']))
        if 'version_type' in local_var_params:
            query_params.append(('version_type', local_var_params['version_type']))
        if 'approve_role' in local_var_params:
            query_params.append(('approve_role', local_var_params['approve_role']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def show_playbook_version_async(self, request):
        r"""查询剧本版本详情（仅支持华东-上海一使用）

        Show playbook version version
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowPlaybookVersion
        :type request: :class:`huaweicloudsdksa.v2.ShowPlaybookVersionRequest`
        :rtype: :class:`huaweicloudsdksa.v2.ShowPlaybookVersionResponse`
        """
        http_info = self._show_playbook_version_http_info(request)
        return self._call_api(**http_info)

    def show_playbook_version_async_invoker(self, request):
        http_info = self._show_playbook_version_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_playbook_version_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/playbooks/versions/{version_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowPlaybookVersionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'version_id' in local_var_params:
            path_params['version_id'] = local_var_params['version_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def update_playbook_version_async(self, request):
        r"""更新剧本版本（仅支持华东-上海一使用）

        Update playbook version.
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdatePlaybookVersion
        :type request: :class:`huaweicloudsdksa.v2.UpdatePlaybookVersionRequest`
        :rtype: :class:`huaweicloudsdksa.v2.UpdatePlaybookVersionResponse`
        """
        http_info = self._update_playbook_version_http_info(request)
        return self._call_api(**http_info)

    def update_playbook_version_async_invoker(self, request):
        http_info = self._update_playbook_version_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_playbook_version_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/playbooks/versions/{version_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdatePlaybookVersionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'version_id' in local_var_params:
            path_params['version_id'] = local_var_params['version_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def create_dataobject_relation_async(self, request):
        r"""创建Dataobject关系

        Create Dataobject Relation
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateDataobjectRelation
        :type request: :class:`huaweicloudsdksa.v2.CreateDataobjectRelationRequest`
        :rtype: :class:`huaweicloudsdksa.v2.CreateDataobjectRelationResponse`
        """
        http_info = self._create_dataobject_relation_http_info(request)
        return self._call_api(**http_info)

    def create_dataobject_relation_async_invoker(self, request):
        http_info = self._create_dataobject_relation_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_dataobject_relation_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/{dataclass_type}/{data_object_id}/{related_dataclass_type}",
            "request_type": request.__class__.__name__,
            "response_type": "CreateDataobjectRelationResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'dataclass_type' in local_var_params:
            path_params['dataclass_type'] = local_var_params['dataclass_type']
        if 'data_object_id' in local_var_params:
            path_params['data_object_id'] = local_var_params['data_object_id']
        if 'related_dataclass_type' in local_var_params:
            path_params['related_dataclass_type'] = local_var_params['related_dataclass_type']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def delete_dataobject_relation_async(self, request):
        r"""删除Dataobject关系

        Delete Dataobject Relation
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteDataobjectRelation
        :type request: :class:`huaweicloudsdksa.v2.DeleteDataobjectRelationRequest`
        :rtype: :class:`huaweicloudsdksa.v2.DeleteDataobjectRelationResponse`
        """
        http_info = self._delete_dataobject_relation_http_info(request)
        return self._call_api(**http_info)

    def delete_dataobject_relation_async_invoker(self, request):
        http_info = self._delete_dataobject_relation_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_dataobject_relation_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/{dataclass_type}/{data_object_id}/{related_dataclass_type}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteDataobjectRelationResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'dataclass_type' in local_var_params:
            path_params['dataclass_type'] = local_var_params['dataclass_type']
        if 'data_object_id' in local_var_params:
            path_params['data_object_id'] = local_var_params['data_object_id']
        if 'related_dataclass_type' in local_var_params:
            path_params['related_dataclass_type'] = local_var_params['related_dataclass_type']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def list_dataobject_relation_async(self, request):
        r"""查询Dataobject关系列表

        List Dataobject Relation
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListDataobjectRelation
        :type request: :class:`huaweicloudsdksa.v2.ListDataobjectRelationRequest`
        :rtype: :class:`huaweicloudsdksa.v2.ListDataobjectRelationResponse`
        """
        http_info = self._list_dataobject_relation_http_info(request)
        return self._call_api(**http_info)

    def list_dataobject_relation_async_invoker(self, request):
        http_info = self._list_dataobject_relation_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_dataobject_relation_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/workspaces/{workspace_id}/soc/{dataclass_type}/{data_object_id}/{related_dataclass_type}/search",
            "request_type": request.__class__.__name__,
            "response_type": "ListDataobjectRelationResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'dataclass_type' in local_var_params:
            path_params['dataclass_type'] = local_var_params['dataclass_type']
        if 'data_object_id' in local_var_params:
            path_params['data_object_id'] = local_var_params['data_object_id']
        if 'related_dataclass_type' in local_var_params:
            path_params['related_dataclass_type'] = local_var_params['related_dataclass_type']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

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


class SaAsyncClient(Client):
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
        super(SaAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdksa.v2.model")
        self.preset_headers = {'User-Agent': 'HuaweiCloud-SDK-Python'}

    @classmethod
    def new_builder(cls, clazz=None):
        if clazz is None:
            return ClientBuilder(cls)

        if clazz.__name__ != "SaClient":
            raise TypeError("client type error, support client type is SaClient")

        return ClientBuilder(clazz)

    def create_alert_rule_async(self, request):
        """创建告警规则（仅支持华东-上海一使用）

        Create alert rule
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateAlertRule
        :type request: :class:`huaweicloudsdksa.v2.CreateAlertRuleRequest`
        :rtype: :class:`huaweicloudsdksa.v2.CreateAlertRuleResponse`
        """
        return self.create_alert_rule_with_http_info(request)

    def create_alert_rule_with_http_info(self, request):
        all_params = ['project_id', 'workspace_id', 'create_alert_rule_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/workspaces/{workspace_id}/siem/alert-rules',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateAlertRuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_alert_rule_simulation_async(self, request):
        """模拟告警规则（仅支持华东-上海一使用）

        Simulate alert rule
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateAlertRuleSimulation
        :type request: :class:`huaweicloudsdksa.v2.CreateAlertRuleSimulationRequest`
        :rtype: :class:`huaweicloudsdksa.v2.CreateAlertRuleSimulationResponse`
        """
        return self.create_alert_rule_simulation_with_http_info(request)

    def create_alert_rule_simulation_with_http_info(self, request):
        all_params = ['project_id', 'workspace_id', 'create_alert_rule_simulation_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/workspaces/{workspace_id}/siem/alert-rules/simulation',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateAlertRuleSimulationResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_alert_rule_async(self, request):
        """删除告警规则（仅支持华东-上海一使用）

        Delete alert rule
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteAlertRule
        :type request: :class:`huaweicloudsdksa.v2.DeleteAlertRuleRequest`
        :rtype: :class:`huaweicloudsdksa.v2.DeleteAlertRuleResponse`
        """
        return self.delete_alert_rule_with_http_info(request)

    def delete_alert_rule_with_http_info(self, request):
        all_params = ['project_id', 'workspace_id', 'delete_alert_rule_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/workspaces/{workspace_id}/siem/alert-rules',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteAlertRuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def disable_alert_rule_async(self, request):
        """停用告警规则（仅支持华东-上海一使用）

        Disable alert rule
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DisableAlertRule
        :type request: :class:`huaweicloudsdksa.v2.DisableAlertRuleRequest`
        :rtype: :class:`huaweicloudsdksa.v2.DisableAlertRuleResponse`
        """
        return self.disable_alert_rule_with_http_info(request)

    def disable_alert_rule_with_http_info(self, request):
        all_params = ['project_id', 'workspace_id', 'disable_alert_rule_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/workspaces/{workspace_id}/siem/alert-rules/disable',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DisableAlertRuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def enable_alert_rule_async(self, request):
        """启用告警规则（仅支持华东-上海一使用）

        Enable alert rule
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for EnableAlertRule
        :type request: :class:`huaweicloudsdksa.v2.EnableAlertRuleRequest`
        :rtype: :class:`huaweicloudsdksa.v2.EnableAlertRuleResponse`
        """
        return self.enable_alert_rule_with_http_info(request)

    def enable_alert_rule_with_http_info(self, request):
        all_params = ['project_id', 'workspace_id', 'enable_alert_rule_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/workspaces/{workspace_id}/siem/alert-rules/enable',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='EnableAlertRuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_alert_rule_metrics_async(self, request):
        """告警规则总览（仅支持华东-上海一使用）

        List alert rule metrics
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAlertRuleMetrics
        :type request: :class:`huaweicloudsdksa.v2.ListAlertRuleMetricsRequest`
        :rtype: :class:`huaweicloudsdksa.v2.ListAlertRuleMetricsResponse`
        """
        return self.list_alert_rule_metrics_with_http_info(request)

    def list_alert_rule_metrics_with_http_info(self, request):
        all_params = ['project_id', 'workspace_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/workspaces/{workspace_id}/siem/alert-rules/metrics',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListAlertRuleMetricsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_alert_rule_templates_async(self, request):
        """列出告警规则模板（仅支持华东-上海一使用）

        List alert rule templates
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAlertRuleTemplates
        :type request: :class:`huaweicloudsdksa.v2.ListAlertRuleTemplatesRequest`
        :rtype: :class:`huaweicloudsdksa.v2.ListAlertRuleTemplatesResponse`
        """
        return self.list_alert_rule_templates_with_http_info(request)

    def list_alert_rule_templates_with_http_info(self, request):
        all_params = ['project_id', 'workspace_id', 'offset', 'limit', 'sort_key', 'sort_dir', 'severity']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/workspaces/{workspace_id}/siem/alert-rules/templates',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListAlertRuleTemplatesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_alert_rules_async(self, request):
        """列出告警规则（仅支持华东-上海一使用）

        List alert rules
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAlertRules
        :type request: :class:`huaweicloudsdksa.v2.ListAlertRulesRequest`
        :rtype: :class:`huaweicloudsdksa.v2.ListAlertRulesResponse`
        """
        return self.list_alert_rules_with_http_info(request)

    def list_alert_rules_with_http_info(self, request):
        all_params = ['project_id', 'workspace_id', 'offset', 'limit', 'sort_key', 'sort_dir', 'pipe_id', 'rule_name', 'rule_id', 'status', 'severity']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/workspaces/{workspace_id}/siem/alert-rules',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListAlertRulesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_alert_rule_async(self, request):
        """查看告警规则（仅支持华东-上海一使用）

        Get alert rule
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowAlertRule
        :type request: :class:`huaweicloudsdksa.v2.ShowAlertRuleRequest`
        :rtype: :class:`huaweicloudsdksa.v2.ShowAlertRuleResponse`
        """
        return self.show_alert_rule_with_http_info(request)

    def show_alert_rule_with_http_info(self, request):
        all_params = ['project_id', 'workspace_id', 'rule_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/workspaces/{workspace_id}/siem/alert-rules/{rule_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowAlertRuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_alert_rule_template_async(self, request):
        """查看告警规则模板（仅支持华东-上海一使用）

        List alert rule templates
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowAlertRuleTemplate
        :type request: :class:`huaweicloudsdksa.v2.ShowAlertRuleTemplateRequest`
        :rtype: :class:`huaweicloudsdksa.v2.ShowAlertRuleTemplateResponse`
        """
        return self.show_alert_rule_template_with_http_info(request)

    def show_alert_rule_template_with_http_info(self, request):
        all_params = ['project_id', 'workspace_id', 'template_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/workspaces/{workspace_id}/siem/alert-rules/templates/{template_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowAlertRuleTemplateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_alert_rule_async(self, request):
        """更新告警规则（仅支持华东-上海一使用）

        Update alert rule
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateAlertRule
        :type request: :class:`huaweicloudsdksa.v2.UpdateAlertRuleRequest`
        :rtype: :class:`huaweicloudsdksa.v2.UpdateAlertRuleResponse`
        """
        return self.update_alert_rule_with_http_info(request)

    def update_alert_rule_with_http_info(self, request):
        all_params = ['project_id', 'workspace_id', 'rule_id', 'update_alert_rule_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/workspaces/{workspace_id}/siem/alert-rules/{rule_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateAlertRuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def change_alert_async(self, request):
        """更新告警（仅支持华东-上海一使用）

        编辑告警，根据实际修改的属性更新，未修改的列不更新
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ChangeAlert
        :type request: :class:`huaweicloudsdksa.v2.ChangeAlertRequest`
        :rtype: :class:`huaweicloudsdksa.v2.ChangeAlertResponse`
        """
        return self.change_alert_with_http_info(request)

    def change_alert_with_http_info(self, request):
        all_params = ['project_id', 'workspace_id', 'alert_id', 'change_alert_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/workspaces/{workspace_id}/soc/alerts/{alert_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ChangeAlertResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_alert_async(self, request):
        """创建告警（仅支持华东-上海一使用）

        创建告警
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateAlert
        :type request: :class:`huaweicloudsdksa.v2.CreateAlertRequest`
        :rtype: :class:`huaweicloudsdksa.v2.CreateAlertResponse`
        """
        return self.create_alert_with_http_info(request)

    def create_alert_with_http_info(self, request):
        all_params = ['project_id', 'workspace_id', 'create_alert_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/workspaces/{workspace_id}/soc/alerts',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateAlertResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_batch_order_alerts_async(self, request):
        """告警转事件（仅支持华东-上海一使用）

        告警转事件
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateBatchOrderAlerts
        :type request: :class:`huaweicloudsdksa.v2.CreateBatchOrderAlertsRequest`
        :rtype: :class:`huaweicloudsdksa.v2.CreateBatchOrderAlertsResponse`
        """
        return self.create_batch_order_alerts_with_http_info(request)

    def create_batch_order_alerts_with_http_info(self, request):
        all_params = ['project_id', 'workspace_id', 'create_batch_order_alerts_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/workspaces/{workspace_id}/soc/alerts/batch-order',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateBatchOrderAlertsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_alert_async(self, request):
        """删除告警（仅支持华东-上海一使用）

        删除告警
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteAlert
        :type request: :class:`huaweicloudsdksa.v2.DeleteAlertRequest`
        :rtype: :class:`huaweicloudsdksa.v2.DeleteAlertResponse`
        """
        return self.delete_alert_with_http_info(request)

    def delete_alert_with_http_info(self, request):
        all_params = ['project_id', 'workspace_id', 'delete_alert_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/workspaces/{workspace_id}/soc/alerts',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteAlertResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_alerts_async(self, request):
        """搜索告警列表（仅支持华东-上海一使用）

        搜索告警列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAlerts
        :type request: :class:`huaweicloudsdksa.v2.ListAlertsRequest`
        :rtype: :class:`huaweicloudsdksa.v2.ListAlertsResponse`
        """
        return self.list_alerts_with_http_info(request)

    def list_alerts_with_http_info(self, request):
        all_params = ['project_id', 'workspace_id', 'list_alerts_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/workspaces/{workspace_id}/soc/alerts/search',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListAlertsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_alert_async(self, request):
        """获取告警详情（仅支持华东-上海一使用）

        获取告警详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowAlert
        :type request: :class:`huaweicloudsdksa.v2.ShowAlertRequest`
        :rtype: :class:`huaweicloudsdksa.v2.ShowAlertResponse`
        """
        return self.show_alert_with_http_info(request)

    def show_alert_with_http_info(self, request):
        all_params = ['project_id', 'workspace_id', 'alert_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/workspaces/{workspace_id}/soc/alerts/{alert_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowAlertResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def change_incident_async(self, request):
        """更新事件（仅支持华东-上海一使用）

        编辑事件，根据实际修改的属性更新，未修改的列不更新
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ChangeIncident
        :type request: :class:`huaweicloudsdksa.v2.ChangeIncidentRequest`
        :rtype: :class:`huaweicloudsdksa.v2.ChangeIncidentResponse`
        """
        return self.change_incident_with_http_info(request)

    def change_incident_with_http_info(self, request):
        all_params = ['project_id', 'workspace_id', 'incident_id', 'change_incident_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/workspaces/{workspace_id}/soc/incidents/{incident_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ChangeIncidentResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_incident_async(self, request):
        """创建事件（仅支持华东-上海一使用）

        创建事件
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateIncident
        :type request: :class:`huaweicloudsdksa.v2.CreateIncidentRequest`
        :rtype: :class:`huaweicloudsdksa.v2.CreateIncidentResponse`
        """
        return self.create_incident_with_http_info(request)

    def create_incident_with_http_info(self, request):
        all_params = ['project_id', 'workspace_id', 'create_incident_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/workspaces/{workspace_id}/soc/incidents',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateIncidentResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_incident_async(self, request):
        """创建事件（仅支持华东-上海一使用）

        创建事件
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteIncident
        :type request: :class:`huaweicloudsdksa.v2.DeleteIncidentRequest`
        :rtype: :class:`huaweicloudsdksa.v2.DeleteIncidentResponse`
        """
        return self.delete_incident_with_http_info(request)

    def delete_incident_with_http_info(self, request):
        all_params = ['project_id', 'workspace_id', 'delete_incident_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/workspaces/{workspace_id}/soc/incidents',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteIncidentResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_incident_types_async(self, request):
        """获取事件的类型列表（仅支持华东-上海一使用）

        获取事件的类型列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListIncidentTypes
        :type request: :class:`huaweicloudsdksa.v2.ListIncidentTypesRequest`
        :rtype: :class:`huaweicloudsdksa.v2.ListIncidentTypesResponse`
        """
        return self.list_incident_types_with_http_info(request)

    def list_incident_types_with_http_info(self, request):
        all_params = ['project_id', 'workspace_id', 'parent_business_code', 'offset', 'limit', 'order', 'sortby', 'name', 'enabled', 'layout_name', 'is_built_in']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/workspaces/{workspace_id}/soc/incidents/types',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListIncidentTypesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_incidents_async(self, request):
        """搜索事件列表（仅支持华东-上海一使用）

        搜索事件列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListIncidents
        :type request: :class:`huaweicloudsdksa.v2.ListIncidentsRequest`
        :rtype: :class:`huaweicloudsdksa.v2.ListIncidentsResponse`
        """
        return self.list_incidents_with_http_info(request)

    def list_incidents_with_http_info(self, request):
        all_params = ['project_id', 'workspace_id', 'listincidents_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/workspaces/{workspace_id}/soc/incidents/search',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListIncidentsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_incident_async(self, request):
        """获取事件详情（仅支持华东-上海一使用）

        获取事件详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowIncident
        :type request: :class:`huaweicloudsdksa.v2.ShowIncidentRequest`
        :rtype: :class:`huaweicloudsdksa.v2.ShowIncidentResponse`
        """
        return self.show_incident_with_http_info(request)

    def show_incident_with_http_info(self, request):
        all_params = ['project_id', 'workspace_id', 'incident_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/workspaces/{workspace_id}/soc/incidents/{incident_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowIncidentResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_indicator_async(self, request):
        """创建指标

        创建指标（仅支持华东-上海一使用）
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateIndicator
        :type request: :class:`huaweicloudsdksa.v2.CreateIndicatorRequest`
        :rtype: :class:`huaweicloudsdksa.v2.CreateIndicatorResponse`
        """
        return self.create_indicator_with_http_info(request)

    def create_indicator_with_http_info(self, request):
        all_params = ['project_id', 'workspace_id', 'create_indicator_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/workspaces/{workspace_id}/soc/indicators',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateIndicatorResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_indicator_async(self, request):
        """删除指标

        删除指标（仅支持华东-上海一使用）
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteIndicator
        :type request: :class:`huaweicloudsdksa.v2.DeleteIndicatorRequest`
        :rtype: :class:`huaweicloudsdksa.v2.DeleteIndicatorResponse`
        """
        return self.delete_indicator_with_http_info(request)

    def delete_indicator_with_http_info(self, request):
        all_params = ['project_id', 'workspace_id', 'delete_indicator_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/workspaces/{workspace_id}/soc/indicators',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteIndicatorResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_indicators_async(self, request):
        """查询指标列表（仅支持华东-上海一使用）

        List all indicators
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListIndicators
        :type request: :class:`huaweicloudsdksa.v2.ListIndicatorsRequest`
        :rtype: :class:`huaweicloudsdksa.v2.ListIndicatorsResponse`
        """
        return self.list_indicators_with_http_info(request)

    def list_indicators_with_http_info(self, request):
        all_params = ['project_id', 'workspace_id', 'list_indicators_request_body', 'order', 'from_date', 'to_date']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/workspaces/{workspace_id}/soc/indicators/search',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListIndicatorsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_indicator_detail_async(self, request):
        """查询指标详情

        查询指标详情（仅支持华东-上海一使用）
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowIndicatorDetail
        :type request: :class:`huaweicloudsdksa.v2.ShowIndicatorDetailRequest`
        :rtype: :class:`huaweicloudsdksa.v2.ShowIndicatorDetailResponse`
        """
        return self.show_indicator_detail_with_http_info(request)

    def show_indicator_detail_with_http_info(self, request):
        all_params = ['project_id', 'workspace_id', 'indicator_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/workspaces/{workspace_id}/soc/indicators/{indicator_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowIndicatorDetailResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_indicator_async(self, request):
        """更新指标

        更新指标（仅支持华东-上海一使用）
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateIndicator
        :type request: :class:`huaweicloudsdksa.v2.UpdateIndicatorRequest`
        :rtype: :class:`huaweicloudsdksa.v2.UpdateIndicatorResponse`
        """
        return self.update_indicator_with_http_info(request)

    def update_indicator_with_http_info(self, request):
        all_params = ['project_id', 'workspace_id', 'indicator_id', 'update_indicator_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/workspaces/{workspace_id}/soc/indicators/{indicator_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateIndicatorResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_playbook_async(self, request):
        """创建剧本（仅支持华东-上海一使用）

        Create playbook.
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreatePlaybook
        :type request: :class:`huaweicloudsdksa.v2.CreatePlaybookRequest`
        :rtype: :class:`huaweicloudsdksa.v2.CreatePlaybookResponse`
        """
        return self.create_playbook_with_http_info(request)

    def create_playbook_with_http_info(self, request):
        all_params = ['project_id', 'workspace_id', 'create_playbook_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/workspaces/{workspace_id}/soc/playbooks',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreatePlaybookResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_playbook_async(self, request):
        """删除剧本（仅支持华东-上海一使用）

        Delete playbook.
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeletePlaybook
        :type request: :class:`huaweicloudsdksa.v2.DeletePlaybookRequest`
        :rtype: :class:`huaweicloudsdksa.v2.DeletePlaybookResponse`
        """
        return self.delete_playbook_with_http_info(request)

    def delete_playbook_with_http_info(self, request):
        all_params = ['project_id', 'workspace_id', 'playbook_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/workspaces/{workspace_id}/soc/playbooks/{playbook_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeletePlaybookResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_playbooks_async(self, request):
        """查询剧本列表（仅支持华东-上海一使用）

        List all playbooks.
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListPlaybooks
        :type request: :class:`huaweicloudsdksa.v2.ListPlaybooksRequest`
        :rtype: :class:`huaweicloudsdksa.v2.ListPlaybooksResponse`
        """
        return self.list_playbooks_with_http_info(request)

    def list_playbooks_with_http_info(self, request):
        all_params = ['project_id', 'workspace_id', 'search_txt', 'component_id', 'enabled', 'offset', 'limit', 'description', 'dataclass_name', 'name']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/workspaces/{workspace_id}/soc/playbooks',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListPlaybooksResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_playbook_async(self, request):
        """查询剧本详情（仅支持华东-上海一使用）

        Show playbook
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowPlaybook
        :type request: :class:`huaweicloudsdksa.v2.ShowPlaybookRequest`
        :rtype: :class:`huaweicloudsdksa.v2.ShowPlaybookResponse`
        """
        return self.show_playbook_with_http_info(request)

    def show_playbook_with_http_info(self, request):
        all_params = ['project_id', 'workspace_id', 'playbook_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/workspaces/{workspace_id}/soc/playbooks/{playbook_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowPlaybookResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_playbook_monitors_async(self, request):
        """剧本运行监控（仅支持华东-上海一使用）

        剧本运行监控
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowPlaybookMonitors
        :type request: :class:`huaweicloudsdksa.v2.ShowPlaybookMonitorsRequest`
        :rtype: :class:`huaweicloudsdksa.v2.ShowPlaybookMonitorsResponse`
        """
        return self.show_playbook_monitors_with_http_info(request)

    def show_playbook_monitors_with_http_info(self, request):
        all_params = ['project_id', 'workspace_id', 'playbook_id', 'start_time', 'version_query_type', 'end_time']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/workspaces/{workspace_id}/soc/playbooks/{playbook_id}/monitor',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowPlaybookMonitorsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_playbook_statistics_async(self, request):
        """剧本数据统计（仅支持华东-上海一使用）

        剧本统计数据
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowPlaybookStatistics
        :type request: :class:`huaweicloudsdksa.v2.ShowPlaybookStatisticsRequest`
        :rtype: :class:`huaweicloudsdksa.v2.ShowPlaybookStatisticsResponse`
        """
        return self.show_playbook_statistics_with_http_info(request)

    def show_playbook_statistics_with_http_info(self, request):
        all_params = ['project_id', 'workspace_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/workspaces/{workspace_id}/soc/playbooks/statistics',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowPlaybookStatisticsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_playbook_async(self, request):
        """修改剧本（仅支持华东-上海一使用）

        Update playbook.
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdatePlaybook
        :type request: :class:`huaweicloudsdksa.v2.UpdatePlaybookRequest`
        :rtype: :class:`huaweicloudsdksa.v2.UpdatePlaybookResponse`
        """
        return self.update_playbook_with_http_info(request)

    def update_playbook_with_http_info(self, request):
        all_params = ['project_id', 'workspace_id', 'playbook_id', 'update_playbook_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/workspaces/{workspace_id}/soc/playbooks/{playbook_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdatePlaybookResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_playbook_action_async(self, request):
        """创建剧本动作（仅支持华东-上海一使用）

        Create action.
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreatePlaybookAction
        :type request: :class:`huaweicloudsdksa.v2.CreatePlaybookActionRequest`
        :rtype: :class:`huaweicloudsdksa.v2.CreatePlaybookActionResponse`
        """
        return self.create_playbook_action_with_http_info(request)

    def create_playbook_action_with_http_info(self, request):
        all_params = ['project_id', 'workspace_id', 'version_id', 'create_playbook_action_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/workspaces/{workspace_id}/soc/playbooks/versions/{version_id}/actions',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreatePlaybookActionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_playbook_action_async(self, request):
        """删除剧本动作（仅支持华东-上海一使用）

        Delete action.
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeletePlaybookAction
        :type request: :class:`huaweicloudsdksa.v2.DeletePlaybookActionRequest`
        :rtype: :class:`huaweicloudsdksa.v2.DeletePlaybookActionResponse`
        """
        return self.delete_playbook_action_with_http_info(request)

    def delete_playbook_action_with_http_info(self, request):
        all_params = ['project_id', 'workspace_id', 'version_id', 'action_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/workspaces/{workspace_id}/soc/playbooks/versions/{version_id}/actions/{action_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeletePlaybookActionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_playbook_actions_async(self, request):
        """查询剧本动作（仅支持华东-上海一使用）

        List all actions.
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListPlaybookActions
        :type request: :class:`huaweicloudsdksa.v2.ListPlaybookActionsRequest`
        :rtype: :class:`huaweicloudsdksa.v2.ListPlaybookActionsResponse`
        """
        return self.list_playbook_actions_with_http_info(request)

    def list_playbook_actions_with_http_info(self, request):
        all_params = ['project_id', 'workspace_id', 'version_id', 'limit', 'offset']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/workspaces/{workspace_id}/soc/playbooks/versions/{version_id}/actions',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListPlaybookActionsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_playbook_action_async(self, request):
        """更新剧本动作（仅支持华东-上海一使用）

        Update action.
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdatePlaybookAction
        :type request: :class:`huaweicloudsdksa.v2.UpdatePlaybookActionRequest`
        :rtype: :class:`huaweicloudsdksa.v2.UpdatePlaybookActionResponse`
        """
        return self.update_playbook_action_with_http_info(request)

    def update_playbook_action_with_http_info(self, request):
        all_params = ['project_id', 'workspace_id', 'version_id', 'action_id', 'update_playbook_action_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/workspaces/{workspace_id}/soc/playbooks/versions/{version_id}/actions/{action_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdatePlaybookActionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_playbook_approve_async(self, request):
        """审核剧本（仅支持华东-上海一使用）

        Create playbook approve.
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreatePlaybookApprove
        :type request: :class:`huaweicloudsdksa.v2.CreatePlaybookApproveRequest`
        :rtype: :class:`huaweicloudsdksa.v2.CreatePlaybookApproveResponse`
        """
        return self.create_playbook_approve_with_http_info(request)

    def create_playbook_approve_with_http_info(self, request):
        all_params = ['project_id', 'workspace_id', 'version_id', 'create_playbook_approve_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/workspaces/{workspace_id}/soc/playbooks/versions/{version_id}/approval',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreatePlaybookApproveResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_playbook_approves_async(self, request):
        """查询剧本审核结果（仅支持华东-上海一使用）

        List approves.
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListPlaybookApproves
        :type request: :class:`huaweicloudsdksa.v2.ListPlaybookApprovesRequest`
        :rtype: :class:`huaweicloudsdksa.v2.ListPlaybookApprovesResponse`
        """
        return self.list_playbook_approves_with_http_info(request)

    def list_playbook_approves_with_http_info(self, request):
        all_params = ['project_id', 'workspace_id', 'resource_id', 'approve_type']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/workspaces/{workspace_id}/soc/playbooks/versions/approval',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListPlaybookApprovesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def change_playbook_instance_async(self, request):
        """操作剧本实例（仅支持华东-上海一使用）

        Operation Playbook Instance.
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ChangePlaybookInstance
        :type request: :class:`huaweicloudsdksa.v2.ChangePlaybookInstanceRequest`
        :rtype: :class:`huaweicloudsdksa.v2.ChangePlaybookInstanceResponse`
        """
        return self.change_playbook_instance_with_http_info(request)

    def change_playbook_instance_with_http_info(self, request):
        all_params = ['project_id', 'workspace_id', 'instance_id', 'change_playbook_instance_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/workspaces/{workspace_id}/soc/playbooks/instances/{instance_id}/operation',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ChangePlaybookInstanceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_playbook_audit_logs_async(self, request):
        """查询剧本实例审计日志（仅支持华东-上海一使用）

        List audit logs.
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListPlaybookAuditLogs
        :type request: :class:`huaweicloudsdksa.v2.ListPlaybookAuditLogsRequest`
        :rtype: :class:`huaweicloudsdksa.v2.ListPlaybookAuditLogsResponse`
        """
        return self.list_playbook_audit_logs_with_http_info(request)

    def list_playbook_audit_logs_with_http_info(self, request):
        all_params = ['project_id', 'workspace_id', 'offset', 'limit', 'sort_key', 'sort_dir', 'list_playbook_audit_logs_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/workspaces/{workspace_id}/soc/playbooks/instances/auditlogs',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListPlaybookAuditLogsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_playbook_instances_async(self, request):
        """查询剧本实例列表（仅支持华东-上海一使用）

        List playbook instances
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListPlaybookInstances
        :type request: :class:`huaweicloudsdksa.v2.ListPlaybookInstancesRequest`
        :rtype: :class:`huaweicloudsdksa.v2.ListPlaybookInstancesResponse`
        """
        return self.list_playbook_instances_with_http_info(request)

    def list_playbook_instances_with_http_info(self, request):
        all_params = ['project_id', 'workspace_id', 'status', 'date_type', 'name', 'playbook_name', 'dataclass_name', 'dataobject_name', 'trigger_type', 'from_date', 'to_date', 'limit', 'offset']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/workspaces/{workspace_id}/soc/playbooks/instances',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListPlaybookInstancesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_playbook_instance_async(self, request):
        """查询剧本实例详情（仅支持华东-上海一使用）

        Show playbook instance
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowPlaybookInstance
        :type request: :class:`huaweicloudsdksa.v2.ShowPlaybookInstanceRequest`
        :rtype: :class:`huaweicloudsdksa.v2.ShowPlaybookInstanceResponse`
        """
        return self.show_playbook_instance_with_http_info(request)

    def show_playbook_instance_with_http_info(self, request):
        all_params = ['project_id', 'workspace_id', 'instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/workspaces/{workspace_id}/soc/playbooks/instances/{instance_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowPlaybookInstanceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_playbook_topology_async(self, request):
        """查询剧本拓扑关系（仅支持华东-上海一使用）

        Show playbook Topology
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowPlaybookTopology
        :type request: :class:`huaweicloudsdksa.v2.ShowPlaybookTopologyRequest`
        :rtype: :class:`huaweicloudsdksa.v2.ShowPlaybookTopologyResponse`
        """
        return self.show_playbook_topology_with_http_info(request)

    def show_playbook_topology_with_http_info(self, request):
        all_params = ['project_id', 'workspace_id', 'instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/workspaces/{workspace_id}/soc/playbooks/instances/{instance_id}/topology',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowPlaybookTopologyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_playbook_rule_async(self, request):
        """创建剧本规则（仅支持华东-上海一使用）

        Create rule.
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreatePlaybookRule
        :type request: :class:`huaweicloudsdksa.v2.CreatePlaybookRuleRequest`
        :rtype: :class:`huaweicloudsdksa.v2.CreatePlaybookRuleResponse`
        """
        return self.create_playbook_rule_with_http_info(request)

    def create_playbook_rule_with_http_info(self, request):
        all_params = ['project_id', 'workspace_id', 'version_id', 'create_playbook_rule_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/workspaces/{workspace_id}/soc/playbooks/versions/{version_id}/rules',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreatePlaybookRuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_playbook_rule_async(self, request):
        """删除剧本规则（仅支持华东-上海一使用）

        Delete rule.
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeletePlaybookRule
        :type request: :class:`huaweicloudsdksa.v2.DeletePlaybookRuleRequest`
        :rtype: :class:`huaweicloudsdksa.v2.DeletePlaybookRuleResponse`
        """
        return self.delete_playbook_rule_with_http_info(request)

    def delete_playbook_rule_with_http_info(self, request):
        all_params = ['project_id', 'workspace_id', 'version_id', 'rule_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/workspaces/{workspace_id}/soc/playbooks/versions/{version_id}/rules/{rule_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeletePlaybookRuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_playbook_rule_async(self, request):
        """查询剧本规则详情（仅支持华东-上海一使用）

        Show rule formation.
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowPlaybookRule
        :type request: :class:`huaweicloudsdksa.v2.ShowPlaybookRuleRequest`
        :rtype: :class:`huaweicloudsdksa.v2.ShowPlaybookRuleResponse`
        """
        return self.show_playbook_rule_with_http_info(request)

    def show_playbook_rule_with_http_info(self, request):
        all_params = ['project_id', 'workspace_id', 'version_id', 'rule_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/workspaces/{workspace_id}/soc/playbooks/versions/{version_id}/rules/{rule_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowPlaybookRuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_playbook_rule_async(self, request):
        """更新剧本规则（仅支持华东-上海一使用）

        Update rule.
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdatePlaybookRule
        :type request: :class:`huaweicloudsdksa.v2.UpdatePlaybookRuleRequest`
        :rtype: :class:`huaweicloudsdksa.v2.UpdatePlaybookRuleResponse`
        """
        return self.update_playbook_rule_with_http_info(request)

    def update_playbook_rule_with_http_info(self, request):
        all_params = ['project_id', 'workspace_id', 'version_id', 'rule_id', 'update_playbook_rule_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/workspaces/{workspace_id}/soc/playbooks/versions/{version_id}/rules/{rule_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdatePlaybookRuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def copy_playbook_version_async(self, request):
        """克隆剧本及版本（仅支持华东-上海一使用）

        Copy Playbook and version to a new one
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CopyPlaybookVersion
        :type request: :class:`huaweicloudsdksa.v2.CopyPlaybookVersionRequest`
        :rtype: :class:`huaweicloudsdksa.v2.CopyPlaybookVersionResponse`
        """
        return self.copy_playbook_version_with_http_info(request)

    def copy_playbook_version_with_http_info(self, request):
        all_params = ['project_id', 'workspace_id', 'version_id', 'copy_playbook_version_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/workspaces/{workspace_id}/soc/playbooks/versions/{version_id}/clone',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CopyPlaybookVersionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_playbook_version_async(self, request):
        """创建剧本版本（仅支持华东-上海一使用）

        Create playbook version.
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreatePlaybookVersion
        :type request: :class:`huaweicloudsdksa.v2.CreatePlaybookVersionRequest`
        :rtype: :class:`huaweicloudsdksa.v2.CreatePlaybookVersionResponse`
        """
        return self.create_playbook_version_with_http_info(request)

    def create_playbook_version_with_http_info(self, request):
        all_params = ['project_id', 'workspace_id', 'playbook_id', 'create_playbook_version_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/workspaces/{workspace_id}/soc/playbooks/{playbook_id}/versions',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreatePlaybookVersionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_playbook_version_async(self, request):
        """删除剧本版本（仅支持华东-上海一使用）

        Delete playbook version.
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeletePlaybookVersion
        :type request: :class:`huaweicloudsdksa.v2.DeletePlaybookVersionRequest`
        :rtype: :class:`huaweicloudsdksa.v2.DeletePlaybookVersionResponse`
        """
        return self.delete_playbook_version_with_http_info(request)

    def delete_playbook_version_with_http_info(self, request):
        all_params = ['project_id', 'workspace_id', 'version_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/workspaces/{workspace_id}/soc/playbooks/versions/{version_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeletePlaybookVersionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_playbook_versions_async(self, request):
        """查询剧本版本列表（仅支持华东-上海一使用）

        List all versions of playbook.
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListPlaybookVersions
        :type request: :class:`huaweicloudsdksa.v2.ListPlaybookVersionsRequest`
        :rtype: :class:`huaweicloudsdksa.v2.ListPlaybookVersionsResponse`
        """
        return self.list_playbook_versions_with_http_info(request)

    def list_playbook_versions_with_http_info(self, request):
        all_params = ['project_id', 'workspace_id', 'playbook_id', 'status', 'enabled', 'version_type', 'approve_role', 'offset', 'limit']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/workspaces/{workspace_id}/soc/playbooks/{playbook_id}/versions',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListPlaybookVersionsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_playbook_version_async(self, request):
        """查询剧本版本详情（仅支持华东-上海一使用）

        Show playbook version version
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowPlaybookVersion
        :type request: :class:`huaweicloudsdksa.v2.ShowPlaybookVersionRequest`
        :rtype: :class:`huaweicloudsdksa.v2.ShowPlaybookVersionResponse`
        """
        return self.show_playbook_version_with_http_info(request)

    def show_playbook_version_with_http_info(self, request):
        all_params = ['project_id', 'workspace_id', 'version_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/workspaces/{workspace_id}/soc/playbooks/versions/{version_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowPlaybookVersionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_playbook_version_async(self, request):
        """更新剧本版本（仅支持华东-上海一使用）

        Update playbook version.
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdatePlaybookVersion
        :type request: :class:`huaweicloudsdksa.v2.UpdatePlaybookVersionRequest`
        :rtype: :class:`huaweicloudsdksa.v2.UpdatePlaybookVersionResponse`
        """
        return self.update_playbook_version_with_http_info(request)

    def update_playbook_version_with_http_info(self, request):
        all_params = ['project_id', 'workspace_id', 'version_id', 'update_playbook_version_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/workspaces/{workspace_id}/soc/playbooks/versions/{version_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdatePlaybookVersionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_dataobject_relation_async(self, request):
        """创建Dataobject关系

        Create Dataobject Relation
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateDataobjectRelation
        :type request: :class:`huaweicloudsdksa.v2.CreateDataobjectRelationRequest`
        :rtype: :class:`huaweicloudsdksa.v2.CreateDataobjectRelationResponse`
        """
        return self.create_dataobject_relation_with_http_info(request)

    def create_dataobject_relation_with_http_info(self, request):
        all_params = ['project_id', 'workspace_id', 'dataclass_type', 'data_object_id', 'related_dataclass_type', 'create_dataobject_relation_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/workspaces/{workspace_id}/soc/{dataclass_type}/{data_object_id}/{related_dataclass_type}',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateDataobjectRelationResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_dataobject_relation_async(self, request):
        """删除Dataobject关系

        Delete Dataobject Relation
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteDataobjectRelation
        :type request: :class:`huaweicloudsdksa.v2.DeleteDataobjectRelationRequest`
        :rtype: :class:`huaweicloudsdksa.v2.DeleteDataobjectRelationResponse`
        """
        return self.delete_dataobject_relation_with_http_info(request)

    def delete_dataobject_relation_with_http_info(self, request):
        all_params = ['project_id', 'workspace_id', 'dataclass_type', 'data_object_id', 'related_dataclass_type', 'delete_dataobject_relation_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/workspaces/{workspace_id}/soc/{dataclass_type}/{data_object_id}/{related_dataclass_type}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteDataobjectRelationResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_dataobject_relation_async(self, request):
        """查询Dataobject关系列表

        List Dataobject Relation
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListDataobjectRelation
        :type request: :class:`huaweicloudsdksa.v2.ListDataobjectRelationRequest`
        :rtype: :class:`huaweicloudsdksa.v2.ListDataobjectRelationResponse`
        """
        return self.list_dataobject_relation_with_http_info(request)

    def list_dataobject_relation_with_http_info(self, request):
        all_params = ['project_id', 'workspace_id', 'dataclass_type', 'data_object_id', 'related_dataclass_type', 'list_dataobject_relation_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/workspaces/{workspace_id}/soc/{dataclass_type}/{data_object_id}/{related_dataclass_type}/search',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListDataobjectRelationResponse',
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

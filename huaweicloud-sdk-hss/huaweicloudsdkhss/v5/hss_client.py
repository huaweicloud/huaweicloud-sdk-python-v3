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


class HssClient(Client):
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
        super(HssClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkhss.v5.model")
        self.preset_headers = {'User-Agent': 'HuaweiCloud-SDK-Python'}

    @classmethod
    def new_builder(cls, clazz=None):
        if clazz is None:
            return ClientBuilder(cls)

        if clazz.__name__ != "HssClient":
            raise TypeError("client type error, support client type is HssClient")

        return ClientBuilder(clazz)

    def batch_create_tags(self, request):
        """批量创建标签

        批量创建标签
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for BatchCreateTags
        :type request: :class:`huaweicloudsdkhss.v5.BatchCreateTagsRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.BatchCreateTagsResponse`
        """
        return self.batch_create_tags_with_http_info(request)

    def batch_create_tags_with_http_info(self, request):
        all_params = ['resource_type', 'resource_id', 'batch_create_tags_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v5/{project_id}/{resource_type}/{resource_id}/tags/create',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='BatchCreateTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_resource_instance_tag(self, request):
        """删除资源标签

        删除单个资源下的标签
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for DeleteResourceInstanceTag
        :type request: :class:`huaweicloudsdkhss.v5.DeleteResourceInstanceTagRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.DeleteResourceInstanceTagResponse`
        """
        return self.delete_resource_instance_tag_with_http_info(request)

    def delete_resource_instance_tag_with_http_info(self, request):
        all_params = ['resource_type', 'resource_id', 'key']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'resource_type' in local_var_params:
            path_params['resource_type'] = local_var_params['resource_type']
        if 'resource_id' in local_var_params:
            path_params['resource_id'] = local_var_params['resource_id']
        if 'key' in local_var_params:
            path_params['key'] = local_var_params['key']

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
            resource_path='/v5/{project_id}/{resource_type}/{resource_id}/tags/{key}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteResourceInstanceTagResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_host_status(self, request):
        """查询云服务器列表

        查询云服务器列表
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListHostStatus
        :type request: :class:`huaweicloudsdkhss.v5.ListHostStatusRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListHostStatusResponse`
        """
        return self.list_host_status_with_http_info(request)

    def list_host_status_with_http_info(self, request):
        all_params = ['region', 'enterprise_project_id', 'version', 'agent_status', 'detect_result', 'host_name', 'host_id', 'host_status', 'os_type', 'private_ip', 'public_ip', 'ip_addr', 'protect_status', 'group_id', 'group_name', 'policy_group_id', 'policy_group_name', 'charging_mode', 'refresh', 'above_version', 'outside_host', 'asset_value', 'label', 'server_group', 'limit', 'offset']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'version' in local_var_params:
            query_params.append(('version', local_var_params['version']))
        if 'agent_status' in local_var_params:
            query_params.append(('agent_status', local_var_params['agent_status']))
        if 'detect_result' in local_var_params:
            query_params.append(('detect_result', local_var_params['detect_result']))
        if 'host_name' in local_var_params:
            query_params.append(('host_name', local_var_params['host_name']))
        if 'host_id' in local_var_params:
            query_params.append(('host_id', local_var_params['host_id']))
        if 'host_status' in local_var_params:
            query_params.append(('host_status', local_var_params['host_status']))
        if 'os_type' in local_var_params:
            query_params.append(('os_type', local_var_params['os_type']))
        if 'private_ip' in local_var_params:
            query_params.append(('private_ip', local_var_params['private_ip']))
        if 'public_ip' in local_var_params:
            query_params.append(('public_ip', local_var_params['public_ip']))
        if 'ip_addr' in local_var_params:
            query_params.append(('ip_addr', local_var_params['ip_addr']))
        if 'protect_status' in local_var_params:
            query_params.append(('protect_status', local_var_params['protect_status']))
        if 'group_id' in local_var_params:
            query_params.append(('group_id', local_var_params['group_id']))
        if 'group_name' in local_var_params:
            query_params.append(('group_name', local_var_params['group_name']))
        if 'policy_group_id' in local_var_params:
            query_params.append(('policy_group_id', local_var_params['policy_group_id']))
        if 'policy_group_name' in local_var_params:
            query_params.append(('policy_group_name', local_var_params['policy_group_name']))
        if 'charging_mode' in local_var_params:
            query_params.append(('charging_mode', local_var_params['charging_mode']))
        if 'refresh' in local_var_params:
            query_params.append(('refresh', local_var_params['refresh']))
        if 'above_version' in local_var_params:
            query_params.append(('above_version', local_var_params['above_version']))
        if 'outside_host' in local_var_params:
            query_params.append(('outside_host', local_var_params['outside_host']))
        if 'asset_value' in local_var_params:
            query_params.append(('asset_value', local_var_params['asset_value']))
        if 'label' in local_var_params:
            query_params.append(('label', local_var_params['label']))
        if 'server_group' in local_var_params:
            query_params.append(('server_group', local_var_params['server_group']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

        header_params = {}
        if 'region' in local_var_params:
            header_params['region'] = local_var_params['region']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v5/{project_id}/host-management/hosts',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListHostStatusResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_password_complexity(self, request):
        """查询口令复杂度策略检测报告

        查询口令复杂度策略检测报告
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListPasswordComplexity
        :type request: :class:`huaweicloudsdkhss.v5.ListPasswordComplexityRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListPasswordComplexityResponse`
        """
        return self.list_password_complexity_with_http_info(request)

    def list_password_complexity_with_http_info(self, request):
        all_params = ['enterprise_project_id', 'host_name', 'host_ip', 'host_id', 'limit', 'offset']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'host_name' in local_var_params:
            query_params.append(('host_name', local_var_params['host_name']))
        if 'host_ip' in local_var_params:
            query_params.append(('host_ip', local_var_params['host_ip']))
        if 'host_id' in local_var_params:
            query_params.append(('host_id', local_var_params['host_id']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

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
            resource_path='/v5/{project_id}/baseline/password-complexity',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListPasswordComplexityResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_quotas_detail(self, request):
        """查询配额详情

        查询配额详情
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListQuotasDetail
        :type request: :class:`huaweicloudsdkhss.v5.ListQuotasDetailRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListQuotasDetailResponse`
        """
        return self.list_quotas_detail_with_http_info(request)

    def list_quotas_detail_with_http_info(self, request):
        all_params = ['region', 'enterprise_project_id', 'version', 'category', 'quota_status', 'used_status', 'host_name', 'resource_id', 'charging_mode', 'limit', 'offset']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'version' in local_var_params:
            query_params.append(('version', local_var_params['version']))
        if 'category' in local_var_params:
            query_params.append(('category', local_var_params['category']))
        if 'quota_status' in local_var_params:
            query_params.append(('quota_status', local_var_params['quota_status']))
        if 'used_status' in local_var_params:
            query_params.append(('used_status', local_var_params['used_status']))
        if 'host_name' in local_var_params:
            query_params.append(('host_name', local_var_params['host_name']))
        if 'resource_id' in local_var_params:
            query_params.append(('resource_id', local_var_params['resource_id']))
        if 'charging_mode' in local_var_params:
            query_params.append(('charging_mode', local_var_params['charging_mode']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

        header_params = {}
        if 'region' in local_var_params:
            header_params['region'] = local_var_params['region']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v5/{project_id}/billing/quotas-detail',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListQuotasDetailResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_risk_config_check_rules(self, request):
        """查询指定安全配置项的检查项列表

        查询指定安全配置项的检查项列表
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListRiskConfigCheckRules
        :type request: :class:`huaweicloudsdkhss.v5.ListRiskConfigCheckRulesRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListRiskConfigCheckRulesResponse`
        """
        return self.list_risk_config_check_rules_with_http_info(request)

    def list_risk_config_check_rules_with_http_info(self, request):
        all_params = ['check_name', 'standard', 'enterprise_project_id', 'result_type', 'check_rule_name', 'severity', 'host_id', 'limit', 'offset']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'check_name' in local_var_params:
            path_params['check_name'] = local_var_params['check_name']

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'standard' in local_var_params:
            query_params.append(('standard', local_var_params['standard']))
        if 'result_type' in local_var_params:
            query_params.append(('result_type', local_var_params['result_type']))
        if 'check_rule_name' in local_var_params:
            query_params.append(('check_rule_name', local_var_params['check_rule_name']))
        if 'severity' in local_var_params:
            query_params.append(('severity', local_var_params['severity']))
        if 'host_id' in local_var_params:
            query_params.append(('host_id', local_var_params['host_id']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

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
            resource_path='/v5/{project_id}/baseline/risk-config/{check_name}/check-rules',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListRiskConfigCheckRulesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_risk_config_hosts(self, request):
        """查询指定安全配置项的受影响服务器列表

        查询指定安全配置项的受影响服务器列表
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListRiskConfigHosts
        :type request: :class:`huaweicloudsdkhss.v5.ListRiskConfigHostsRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListRiskConfigHostsResponse`
        """
        return self.list_risk_config_hosts_with_http_info(request)

    def list_risk_config_hosts_with_http_info(self, request):
        all_params = ['check_name', 'standard', 'enterprise_project_id', 'host_name', 'host_ip', 'limit', 'offset']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'check_name' in local_var_params:
            path_params['check_name'] = local_var_params['check_name']

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'standard' in local_var_params:
            query_params.append(('standard', local_var_params['standard']))
        if 'host_name' in local_var_params:
            query_params.append(('host_name', local_var_params['host_name']))
        if 'host_ip' in local_var_params:
            query_params.append(('host_ip', local_var_params['host_ip']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

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
            resource_path='/v5/{project_id}/baseline/risk-config/{check_name}/hosts',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListRiskConfigHostsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_risk_configs(self, request):
        """查询租户的服务器安全配置检测结果列表

        查询租户的服务器安全配置检测结果列表
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListRiskConfigs
        :type request: :class:`huaweicloudsdkhss.v5.ListRiskConfigsRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListRiskConfigsResponse`
        """
        return self.list_risk_configs_with_http_info(request)

    def list_risk_configs_with_http_info(self, request):
        all_params = ['enterprise_project_id', 'check_name', 'severity', 'standard', 'host_id', 'limit', 'offset']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'check_name' in local_var_params:
            query_params.append(('check_name', local_var_params['check_name']))
        if 'severity' in local_var_params:
            query_params.append(('severity', local_var_params['severity']))
        if 'standard' in local_var_params:
            query_params.append(('standard', local_var_params['standard']))
        if 'host_id' in local_var_params:
            query_params.append(('host_id', local_var_params['host_id']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

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
            resource_path='/v5/{project_id}/baseline/risk-configs',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListRiskConfigsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_security_events(self, request):
        """查入侵事件列表

        查入侵事件列表
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListSecurityEvents
        :type request: :class:`huaweicloudsdkhss.v5.ListSecurityEventsRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListSecurityEventsResponse`
        """
        return self.list_security_events_with_http_info(request)

    def list_security_events_with_http_info(self, request):
        all_params = ['region', 'category', 'enterprise_project_id', 'last_days', 'host_name', 'host_id', 'private_ip', 'container_name', 'offset', 'limit', 'event_types', 'handle_status', 'severity', 'begin_time', 'end_time']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'last_days' in local_var_params:
            query_params.append(('last_days', local_var_params['last_days']))
        if 'host_name' in local_var_params:
            query_params.append(('host_name', local_var_params['host_name']))
        if 'host_id' in local_var_params:
            query_params.append(('host_id', local_var_params['host_id']))
        if 'private_ip' in local_var_params:
            query_params.append(('private_ip', local_var_params['private_ip']))
        if 'container_name' in local_var_params:
            query_params.append(('container_name', local_var_params['container_name']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'event_types' in local_var_params:
            query_params.append(('event_types', local_var_params['event_types']))
            collection_formats['event_types'] = 'csv'
        if 'handle_status' in local_var_params:
            query_params.append(('handle_status', local_var_params['handle_status']))
        if 'severity' in local_var_params:
            query_params.append(('severity', local_var_params['severity']))
        if 'category' in local_var_params:
            query_params.append(('category', local_var_params['category']))
        if 'begin_time' in local_var_params:
            query_params.append(('begin_time', local_var_params['begin_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))

        header_params = {}
        if 'region' in local_var_params:
            header_params['region'] = local_var_params['region']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v5/{project_id}/event/events',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListSecurityEventsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_user_change_histories(self, request):
        """获取账户变动历史信息

        获取账户变动历史记录信息
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListUserChangeHistories
        :type request: :class:`huaweicloudsdkhss.v5.ListUserChangeHistoriesRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListUserChangeHistoriesResponse`
        """
        return self.list_user_change_histories_with_http_info(request)

    def list_user_change_histories_with_http_info(self, request):
        all_params = ['user_name', 'host_id', 'root_permission', 'host_name', 'private_ip', 'change_type', 'limit', 'offset', 'enterprise_project_id', 'start_time', 'end_time']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'user_name' in local_var_params:
            query_params.append(('user_name', local_var_params['user_name']))
        if 'host_id' in local_var_params:
            query_params.append(('host_id', local_var_params['host_id']))
        if 'root_permission' in local_var_params:
            query_params.append(('root_permission', local_var_params['root_permission']))
        if 'host_name' in local_var_params:
            query_params.append(('host_name', local_var_params['host_name']))
        if 'private_ip' in local_var_params:
            query_params.append(('private_ip', local_var_params['private_ip']))
        if 'change_type' in local_var_params:
            query_params.append(('change_type', local_var_params['change_type']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
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
            resource_path='/v5/{project_id}/asset/user/change-history',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListUserChangeHistoriesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_users(self, request):
        """获取资产的账号列表

        获取资产的账号列表
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListUsers
        :type request: :class:`huaweicloudsdkhss.v5.ListUsersRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListUsersResponse`
        """
        return self.list_users_with_http_info(request)

    def list_users_with_http_info(self, request):
        all_params = ['host_id', 'user_name', 'host_name', 'private_ip', 'login_permission', 'root_permission', 'user_group', 'enterprise_project_id', 'limit', 'offset']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'host_id' in local_var_params:
            query_params.append(('host_id', local_var_params['host_id']))
        if 'user_name' in local_var_params:
            query_params.append(('user_name', local_var_params['user_name']))
        if 'host_name' in local_var_params:
            query_params.append(('host_name', local_var_params['host_name']))
        if 'private_ip' in local_var_params:
            query_params.append(('private_ip', local_var_params['private_ip']))
        if 'login_permission' in local_var_params:
            query_params.append(('login_permission', local_var_params['login_permission']))
        if 'root_permission' in local_var_params:
            query_params.append(('root_permission', local_var_params['root_permission']))
        if 'user_group' in local_var_params:
            query_params.append(('user_group', local_var_params['user_group']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

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
            resource_path='/v5/{project_id}/asset/users',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListUsersResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_vulnerabilities(self, request):
        """查询漏洞列表

        查询漏洞列表
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListVulnerabilities
        :type request: :class:`huaweicloudsdkhss.v5.ListVulnerabilitiesRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListVulnerabilitiesResponse`
        """
        return self.list_vulnerabilities_with_http_info(request)

    def list_vulnerabilities_with_http_info(self, request):
        all_params = ['vul_id', 'enterprise_project_id', 'type', 'vul_name', 'limit', 'offset']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'vul_id' in local_var_params:
            query_params.append(('vul_id', local_var_params['vul_id']))
        if 'vul_name' in local_var_params:
            query_params.append(('vul_name', local_var_params['vul_name']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

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
            resource_path='/v5/{project_id}/vulnerability/vulnerabilities',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListVulnerabilitiesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_weak_password_users(self, request):
        """查询弱口令检测结果列表

        查询弱口令检测结果列表
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListWeakPasswordUsers
        :type request: :class:`huaweicloudsdkhss.v5.ListWeakPasswordUsersRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ListWeakPasswordUsersResponse`
        """
        return self.list_weak_password_users_with_http_info(request)

    def list_weak_password_users_with_http_info(self, request):
        all_params = ['enterprise_project_id', 'host_name', 'host_ip', 'user_name', 'host_id', 'limit', 'offset']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'host_name' in local_var_params:
            query_params.append(('host_name', local_var_params['host_name']))
        if 'host_ip' in local_var_params:
            query_params.append(('host_ip', local_var_params['host_ip']))
        if 'user_name' in local_var_params:
            query_params.append(('user_name', local_var_params['user_name']))
        if 'host_id' in local_var_params:
            query_params.append(('host_id', local_var_params['host_id']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

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
            resource_path='/v5/{project_id}/baseline/weak-password-users',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListWeakPasswordUsersResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_check_rule_detail(self, request):
        """查询配置检查项检测报告

        查询配置检查项检测报告
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowCheckRuleDetail
        :type request: :class:`huaweicloudsdkhss.v5.ShowCheckRuleDetailRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ShowCheckRuleDetailResponse`
        """
        return self.show_check_rule_detail_with_http_info(request)

    def show_check_rule_detail_with_http_info(self, request):
        all_params = ['check_name', 'check_rule_id', 'standard', 'enterprise_project_id', 'host_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'check_name' in local_var_params:
            query_params.append(('check_name', local_var_params['check_name']))
        if 'check_rule_id' in local_var_params:
            query_params.append(('check_rule_id', local_var_params['check_rule_id']))
        if 'standard' in local_var_params:
            query_params.append(('standard', local_var_params['standard']))
        if 'host_id' in local_var_params:
            query_params.append(('host_id', local_var_params['host_id']))

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
            resource_path='/v5/{project_id}/baseline/check-rule/detail',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowCheckRuleDetailResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_resource_quotas(self, request):
        """查询配额信息

        查询配额信息
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowResourceQuotas
        :type request: :class:`huaweicloudsdkhss.v5.ShowResourceQuotasRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ShowResourceQuotasResponse`
        """
        return self.show_resource_quotas_with_http_info(request)

    def show_resource_quotas_with_http_info(self, request):
        all_params = ['region', 'enterprise_project_id', 'version', 'charging_mode']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'version' in local_var_params:
            query_params.append(('version', local_var_params['version']))
        if 'charging_mode' in local_var_params:
            query_params.append(('charging_mode', local_var_params['charging_mode']))

        header_params = {}
        if 'region' in local_var_params:
            header_params['region'] = local_var_params['region']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v5/{project_id}/billing/quotas',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowResourceQuotasResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_risk_config_detail(self, request):
        """查询指定安全配置项的检查结果

        查询指定安全配置项的检查结果
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowRiskConfigDetail
        :type request: :class:`huaweicloudsdkhss.v5.ShowRiskConfigDetailRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.ShowRiskConfigDetailResponse`
        """
        return self.show_risk_config_detail_with_http_info(request)

    def show_risk_config_detail_with_http_info(self, request):
        all_params = ['check_name', 'standard', 'enterprise_project_id', 'host_id', 'limit', 'offset']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'check_name' in local_var_params:
            path_params['check_name'] = local_var_params['check_name']

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'standard' in local_var_params:
            query_params.append(('standard', local_var_params['standard']))
        if 'host_id' in local_var_params:
            query_params.append(('host_id', local_var_params['host_id']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

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
            resource_path='/v5/{project_id}/baseline/risk-config/{check_name}/detail',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowRiskConfigDetailResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def switch_hosts_protect_status(self, request):
        """切换防护状态

        切换防护状态
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for SwitchHostsProtectStatus
        :type request: :class:`huaweicloudsdkhss.v5.SwitchHostsProtectStatusRequest`
        :rtype: :class:`huaweicloudsdkhss.v5.SwitchHostsProtectStatusResponse`
        """
        return self.switch_hosts_protect_status_with_http_info(request)

    def switch_hosts_protect_status_with_http_info(self, request):
        all_params = ['region', 'switch_hosts_protect_status_request_body', 'enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

        header_params = {}
        if 'region' in local_var_params:
            header_params['region'] = local_var_params['region']

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
            resource_path='/v5/{project_id}/host-management/protection',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='SwitchHostsProtectStatusResponse',
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

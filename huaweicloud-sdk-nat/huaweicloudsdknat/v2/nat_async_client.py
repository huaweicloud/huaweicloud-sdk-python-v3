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


class NatAsyncClient(Client):
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
        super(NatAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdknat.v2.model")
        self.preset_headers = {'User-Agent': 'HuaweiCloud-SDK-Python'}

    @classmethod
    def new_builder(cls, clazz=None):
        if clazz is None:
            return ClientBuilder(cls)

        if clazz.__name__ != "NatClient":
            raise TypeError("client type error, support client type is NatClient")

        return ClientBuilder(clazz)

    def batch_create_nat_gateway_dnat_rules_async(self, request):
        """批量创建DNAT规则

        批量创建DNAT规则。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for BatchCreateNatGatewayDnatRules
        :type request: :class:`huaweicloudsdknat.v2.BatchCreateNatGatewayDnatRulesRequest`
        :rtype: :class:`huaweicloudsdknat.v2.BatchCreateNatGatewayDnatRulesResponse`
        """
        return self.batch_create_nat_gateway_dnat_rules_with_http_info(request)

    def batch_create_nat_gateway_dnat_rules_with_http_info(self, request):
        all_params = ['batch_create_nat_gateway_dnat_rules_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v2/{project_id}/dnat_rules/batch',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='BatchCreateNatGatewayDnatRulesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_nat_gateway_dnat_rule_async(self, request):
        """创建DNAT规则

        创建DNAT规则。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for CreateNatGatewayDnatRule
        :type request: :class:`huaweicloudsdknat.v2.CreateNatGatewayDnatRuleRequest`
        :rtype: :class:`huaweicloudsdknat.v2.CreateNatGatewayDnatRuleResponse`
        """
        return self.create_nat_gateway_dnat_rule_with_http_info(request)

    def create_nat_gateway_dnat_rule_with_http_info(self, request):
        all_params = ['create_nat_gateway_dnat_rule_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v2/{project_id}/dnat_rules',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateNatGatewayDnatRuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_nat_gateway_dnat_rule_async(self, request):
        """删除DNAT规则

        删除指定的DNAT规则。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for DeleteNatGatewayDnatRule
        :type request: :class:`huaweicloudsdknat.v2.DeleteNatGatewayDnatRuleRequest`
        :rtype: :class:`huaweicloudsdknat.v2.DeleteNatGatewayDnatRuleResponse`
        """
        return self.delete_nat_gateway_dnat_rule_with_http_info(request)

    def delete_nat_gateway_dnat_rule_with_http_info(self, request):
        all_params = ['nat_gateway_id', 'dnat_rule_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'nat_gateway_id' in local_var_params:
            path_params['nat_gateway_id'] = local_var_params['nat_gateway_id']
        if 'dnat_rule_id' in local_var_params:
            path_params['dnat_rule_id'] = local_var_params['dnat_rule_id']

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
            resource_path='/v2/{project_id}/nat_gateways/{nat_gateway_id}/dnat_rules/{dnat_rule_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteNatGatewayDnatRuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_nat_gateway_dnat_rules_async(self, request):
        """查询DNAT规则列表

        查询DNAT规则列表。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListNatGatewayDnatRules
        :type request: :class:`huaweicloudsdknat.v2.ListNatGatewayDnatRulesRequest`
        :rtype: :class:`huaweicloudsdknat.v2.ListNatGatewayDnatRulesResponse`
        """
        return self.list_nat_gateway_dnat_rules_with_http_info(request)

    def list_nat_gateway_dnat_rules_with_http_info(self, request):
        all_params = ['admin_state_up', 'external_service_port', 'floating_ip_address', 'status', 'floating_ip_id', 'internal_service_port', 'limit', 'id', 'description', 'created_at', 'nat_gateway_id', 'port_id', 'private_ip', 'protocol']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'admin_state_up' in local_var_params:
            query_params.append(('admin_state_up', local_var_params['admin_state_up']))
        if 'external_service_port' in local_var_params:
            query_params.append(('external_service_port', local_var_params['external_service_port']))
        if 'floating_ip_address' in local_var_params:
            query_params.append(('floating_ip_address', local_var_params['floating_ip_address']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
            collection_formats['status'] = 'csv'
        if 'floating_ip_id' in local_var_params:
            query_params.append(('floating_ip_id', local_var_params['floating_ip_id']))
        if 'internal_service_port' in local_var_params:
            query_params.append(('internal_service_port', local_var_params['internal_service_port']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'description' in local_var_params:
            query_params.append(('description', local_var_params['description']))
        if 'created_at' in local_var_params:
            query_params.append(('created_at', local_var_params['created_at']))
        if 'nat_gateway_id' in local_var_params:
            query_params.append(('nat_gateway_id', local_var_params['nat_gateway_id']))
            collection_formats['nat_gateway_id'] = 'csv'
        if 'port_id' in local_var_params:
            query_params.append(('port_id', local_var_params['port_id']))
        if 'private_ip' in local_var_params:
            query_params.append(('private_ip', local_var_params['private_ip']))
        if 'protocol' in local_var_params:
            query_params.append(('protocol', local_var_params['protocol']))
            collection_formats['protocol'] = 'csv'

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
            resource_path='/v2/{project_id}/dnat_rules',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListNatGatewayDnatRulesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_nat_gateway_dnat_rule_async(self, request):
        """查询指定的DNAT规则详情

        查询指定的DNAT规则详情。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowNatGatewayDnatRule
        :type request: :class:`huaweicloudsdknat.v2.ShowNatGatewayDnatRuleRequest`
        :rtype: :class:`huaweicloudsdknat.v2.ShowNatGatewayDnatRuleResponse`
        """
        return self.show_nat_gateway_dnat_rule_with_http_info(request)

    def show_nat_gateway_dnat_rule_with_http_info(self, request):
        all_params = ['dnat_rule_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'dnat_rule_id' in local_var_params:
            path_params['dnat_rule_id'] = local_var_params['dnat_rule_id']

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
            resource_path='/v2/{project_id}/dnat_rules/{dnat_rule_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowNatGatewayDnatRuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_nat_gateway_dnat_rule_async(self, request):
        """更新DNAT规则

        更新指定的DNAT规则。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for UpdateNatGatewayDnatRule
        :type request: :class:`huaweicloudsdknat.v2.UpdateNatGatewayDnatRuleRequest`
        :rtype: :class:`huaweicloudsdknat.v2.UpdateNatGatewayDnatRuleResponse`
        """
        return self.update_nat_gateway_dnat_rule_with_http_info(request)

    def update_nat_gateway_dnat_rule_with_http_info(self, request):
        all_params = ['dnat_rule_id', 'update_nat_gateway_dnat_rule_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'dnat_rule_id' in local_var_params:
            path_params['dnat_rule_id'] = local_var_params['dnat_rule_id']

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
            resource_path='/v2/{project_id}/dnat_rules/{dnat_rule_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateNatGatewayDnatRuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_nat_gateway_async(self, request):
        """创建公网NAT网关

        创建公网NAT网关实例。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for CreateNatGateway
        :type request: :class:`huaweicloudsdknat.v2.CreateNatGatewayRequest`
        :rtype: :class:`huaweicloudsdknat.v2.CreateNatGatewayResponse`
        """
        return self.create_nat_gateway_with_http_info(request)

    def create_nat_gateway_with_http_info(self, request):
        all_params = ['create_nat_gateway_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v2/{project_id}/nat_gateways',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateNatGatewayResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_nat_gateway_async(self, request):
        """删除公网NAT网关

        删除公网NAT网关实例。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for DeleteNatGateway
        :type request: :class:`huaweicloudsdknat.v2.DeleteNatGatewayRequest`
        :rtype: :class:`huaweicloudsdknat.v2.DeleteNatGatewayResponse`
        """
        return self.delete_nat_gateway_with_http_info(request)

    def delete_nat_gateway_with_http_info(self, request):
        all_params = ['nat_gateway_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'nat_gateway_id' in local_var_params:
            path_params['nat_gateway_id'] = local_var_params['nat_gateway_id']

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
            resource_path='/v2/{project_id}/nat_gateways/{nat_gateway_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteNatGatewayResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_nat_gateways_async(self, request):
        """查询公网NAT网关列表

        查询公网NAT网关实例列表。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListNatGateways
        :type request: :class:`huaweicloudsdknat.v2.ListNatGatewaysRequest`
        :rtype: :class:`huaweicloudsdknat.v2.ListNatGatewaysResponse`
        """
        return self.list_nat_gateways_with_http_info(request)

    def list_nat_gateways_with_http_info(self, request):
        all_params = ['id', 'enterprise_project_id', 'description', 'created_at', 'name', 'status', 'spec', 'admin_state_up', 'internal_network_id', 'router_id', 'limit']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'description' in local_var_params:
            query_params.append(('description', local_var_params['description']))
        if 'created_at' in local_var_params:
            query_params.append(('created_at', local_var_params['created_at']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
            collection_formats['status'] = 'csv'
        if 'spec' in local_var_params:
            query_params.append(('spec', local_var_params['spec']))
            collection_formats['spec'] = 'csv'
        if 'admin_state_up' in local_var_params:
            query_params.append(('admin_state_up', local_var_params['admin_state_up']))
        if 'internal_network_id' in local_var_params:
            query_params.append(('internal_network_id', local_var_params['internal_network_id']))
        if 'router_id' in local_var_params:
            query_params.append(('router_id', local_var_params['router_id']))
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
            resource_path='/v2/{project_id}/nat_gateways',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListNatGatewaysResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_nat_gateway_async(self, request):
        """查询指定的公网NAT网关详情

        查询指定的公网NAT网关实例详情。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowNatGateway
        :type request: :class:`huaweicloudsdknat.v2.ShowNatGatewayRequest`
        :rtype: :class:`huaweicloudsdknat.v2.ShowNatGatewayResponse`
        """
        return self.show_nat_gateway_with_http_info(request)

    def show_nat_gateway_with_http_info(self, request):
        all_params = ['nat_gateway_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'nat_gateway_id' in local_var_params:
            path_params['nat_gateway_id'] = local_var_params['nat_gateway_id']

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
            resource_path='/v2/{project_id}/nat_gateways/{nat_gateway_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowNatGatewayResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_nat_gateway_async(self, request):
        """更新公网NAT网关

        更新公网NAT网关实例。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for UpdateNatGateway
        :type request: :class:`huaweicloudsdknat.v2.UpdateNatGatewayRequest`
        :rtype: :class:`huaweicloudsdknat.v2.UpdateNatGatewayResponse`
        """
        return self.update_nat_gateway_with_http_info(request)

    def update_nat_gateway_with_http_info(self, request):
        all_params = ['nat_gateway_id', 'update_nat_gateway_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'nat_gateway_id' in local_var_params:
            path_params['nat_gateway_id'] = local_var_params['nat_gateway_id']

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
            resource_path='/v2/{project_id}/nat_gateways/{nat_gateway_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateNatGatewayResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_nat_gateway_snat_rule_async(self, request):
        """创建SNAT规则

        创建SNAT规则。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for CreateNatGatewaySnatRule
        :type request: :class:`huaweicloudsdknat.v2.CreateNatGatewaySnatRuleRequest`
        :rtype: :class:`huaweicloudsdknat.v2.CreateNatGatewaySnatRuleResponse`
        """
        return self.create_nat_gateway_snat_rule_with_http_info(request)

    def create_nat_gateway_snat_rule_with_http_info(self, request):
        all_params = ['create_nat_gateway_snat_rule_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v2/{project_id}/snat_rules',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateNatGatewaySnatRuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_nat_gateway_snat_rule_async(self, request):
        """删除SNAT规则

        删除指定的SNAT规则。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for DeleteNatGatewaySnatRule
        :type request: :class:`huaweicloudsdknat.v2.DeleteNatGatewaySnatRuleRequest`
        :rtype: :class:`huaweicloudsdknat.v2.DeleteNatGatewaySnatRuleResponse`
        """
        return self.delete_nat_gateway_snat_rule_with_http_info(request)

    def delete_nat_gateway_snat_rule_with_http_info(self, request):
        all_params = ['nat_gateway_id', 'snat_rule_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'nat_gateway_id' in local_var_params:
            path_params['nat_gateway_id'] = local_var_params['nat_gateway_id']
        if 'snat_rule_id' in local_var_params:
            path_params['snat_rule_id'] = local_var_params['snat_rule_id']

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
            resource_path='/v2/{project_id}/nat_gateways/{nat_gateway_id}/snat_rules/{snat_rule_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteNatGatewaySnatRuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_nat_gateway_snat_rules_async(self, request):
        """查询SNAT规则列表

        查询SNAT规则列表。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListNatGatewaySnatRules
        :type request: :class:`huaweicloudsdknat.v2.ListNatGatewaySnatRulesRequest`
        :rtype: :class:`huaweicloudsdknat.v2.ListNatGatewaySnatRulesResponse`
        """
        return self.list_nat_gateway_snat_rules_with_http_info(request)

    def list_nat_gateway_snat_rules_with_http_info(self, request):
        all_params = ['admin_state_up', 'cidr', 'limit', 'floating_ip_address', 'floating_ip_id', 'id', 'description', 'created_at', 'nat_gateway_id', 'network_id', 'source_type', 'status']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'admin_state_up' in local_var_params:
            query_params.append(('admin_state_up', local_var_params['admin_state_up']))
        if 'cidr' in local_var_params:
            query_params.append(('cidr', local_var_params['cidr']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'floating_ip_address' in local_var_params:
            query_params.append(('floating_ip_address', local_var_params['floating_ip_address']))
        if 'floating_ip_id' in local_var_params:
            query_params.append(('floating_ip_id', local_var_params['floating_ip_id']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'description' in local_var_params:
            query_params.append(('description', local_var_params['description']))
        if 'created_at' in local_var_params:
            query_params.append(('created_at', local_var_params['created_at']))
        if 'nat_gateway_id' in local_var_params:
            query_params.append(('nat_gateway_id', local_var_params['nat_gateway_id']))
            collection_formats['nat_gateway_id'] = 'csv'
        if 'network_id' in local_var_params:
            query_params.append(('network_id', local_var_params['network_id']))
        if 'source_type' in local_var_params:
            query_params.append(('source_type', local_var_params['source_type']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))

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
            resource_path='/v2/{project_id}/snat_rules',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListNatGatewaySnatRulesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_nat_gateway_snat_rule_async(self, request):
        """查询指定的SNAT规则详情

        查询指定的SNAT规则详情。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowNatGatewaySnatRule
        :type request: :class:`huaweicloudsdknat.v2.ShowNatGatewaySnatRuleRequest`
        :rtype: :class:`huaweicloudsdknat.v2.ShowNatGatewaySnatRuleResponse`
        """
        return self.show_nat_gateway_snat_rule_with_http_info(request)

    def show_nat_gateway_snat_rule_with_http_info(self, request):
        all_params = ['snat_rule_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'snat_rule_id' in local_var_params:
            path_params['snat_rule_id'] = local_var_params['snat_rule_id']

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
            resource_path='/v2/{project_id}/snat_rules/{snat_rule_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowNatGatewaySnatRuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_nat_gateway_snat_rule_async(self, request):
        """更新SNAT规则

        更新指定的SNAT规则。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for UpdateNatGatewaySnatRule
        :type request: :class:`huaweicloudsdknat.v2.UpdateNatGatewaySnatRuleRequest`
        :rtype: :class:`huaweicloudsdknat.v2.UpdateNatGatewaySnatRuleResponse`
        """
        return self.update_nat_gateway_snat_rule_with_http_info(request)

    def update_nat_gateway_snat_rule_with_http_info(self, request):
        all_params = ['snat_rule_id', 'update_nat_gateway_snat_rule_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'snat_rule_id' in local_var_params:
            path_params['snat_rule_id'] = local_var_params['snat_rule_id']

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
            resource_path='/v2/{project_id}/snat_rules/{snat_rule_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateNatGatewaySnatRuleResponse',
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
        :param header_params: Header parameters to be
            placed in the request header.
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
            request_type=request_type,
	    async_request=True)

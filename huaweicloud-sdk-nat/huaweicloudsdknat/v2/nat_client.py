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


class NatClient(Client):
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
        super(NatClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdknat.v2.model")
        self.preset_headers = {'User-Agent': 'HuaweiCloud-SDK-Python'}

    @classmethod
    def new_builder(cls, clazz=None):
        if clazz is None:
            return ClientBuilder(cls)

        if clazz.__name__ != "NatClient":
            raise TypeError("client type error, support client type is NatClient")

        return ClientBuilder(clazz)

    def batch_create_nat_gateway_dnat_rules(self, request):
        """批量创建DNAT规则

        批量创建DNAT规则。
        
        Please refer to HUAWEI cloud API Explorer for details.

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
            resource_path='/v2/{project_id}/dnat_rules/batch',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchCreateNatGatewayDnatRulesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_nat_gateway_dnat_rule(self, request):
        """创建DNAT规则

        创建DNAT规则。
        
        Please refer to HUAWEI cloud API Explorer for details.

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
            resource_path='/v2/{project_id}/dnat_rules',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateNatGatewayDnatRuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_private_dnat(self, request):
        """创建DNAT规则

        创建DNAT规则。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreatePrivateDnat
        :type request: :class:`huaweicloudsdknat.v2.CreatePrivateDnatRequest`
        :rtype: :class:`huaweicloudsdknat.v2.CreatePrivateDnatResponse`
        """
        return self.create_private_dnat_with_http_info(request)

    def create_private_dnat_with_http_info(self, request):
        all_params = ['create_private_dnat_request_body']
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
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/private-nat/dnat-rules',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreatePrivateDnatResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_nat_gateway_dnat_rule(self, request):
        """删除DNAT规则

        删除指定的DNAT规则。
        
        Please refer to HUAWEI cloud API Explorer for details.

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

        cname = None

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
            cname=cname,
            response_type='DeleteNatGatewayDnatRuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_private_dnat(self, request):
        """删除DNAT规则

        删除指定的DNAT规则。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeletePrivateDnat
        :type request: :class:`huaweicloudsdknat.v2.DeletePrivateDnatRequest`
        :rtype: :class:`huaweicloudsdknat.v2.DeletePrivateDnatResponse`
        """
        return self.delete_private_dnat_with_http_info(request)

    def delete_private_dnat_with_http_info(self, request):
        all_params = ['dnat_rule_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            resource_path='/v3/{project_id}/private-nat/dnat-rules/{dnat_rule_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeletePrivateDnatResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_nat_gateway_dnat_rules(self, request):
        """查询DNAT规则列表

        查询DNAT规则列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

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

        cname = None

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
            cname=cname,
            response_type='ListNatGatewayDnatRulesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_private_dnats(self, request):
        """查询DNAT规则列表

        查询DNAT规则列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListPrivateDnats
        :type request: :class:`huaweicloudsdknat.v2.ListPrivateDnatsRequest`
        :rtype: :class:`huaweicloudsdknat.v2.ListPrivateDnatsResponse`
        """
        return self.list_private_dnats_with_http_info(request)

    def list_private_dnats_with_http_info(self, request):
        all_params = ['limit', 'marker', 'page_reverse', 'id', 'enterprise_project_id', 'description', 'gateway_id', 'transit_ip_id', 'external_ip_address', 'network_interface_id', 'type', 'private_ip_address']
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
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'page_reverse' in local_var_params:
            query_params.append(('page_reverse', local_var_params['page_reverse']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
            collection_formats['id'] = 'csv'
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
            collection_formats['enterprise_project_id'] = 'csv'
        if 'description' in local_var_params:
            query_params.append(('description', local_var_params['description']))
            collection_formats['description'] = 'csv'
        if 'gateway_id' in local_var_params:
            query_params.append(('gateway_id', local_var_params['gateway_id']))
            collection_formats['gateway_id'] = 'csv'
        if 'transit_ip_id' in local_var_params:
            query_params.append(('transit_ip_id', local_var_params['transit_ip_id']))
            collection_formats['transit_ip_id'] = 'csv'
        if 'external_ip_address' in local_var_params:
            query_params.append(('external_ip_address', local_var_params['external_ip_address']))
            collection_formats['external_ip_address'] = 'csv'
        if 'network_interface_id' in local_var_params:
            query_params.append(('network_interface_id', local_var_params['network_interface_id']))
            collection_formats['network_interface_id'] = 'csv'
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
            collection_formats['type'] = 'csv'
        if 'private_ip_address' in local_var_params:
            query_params.append(('private_ip_address', local_var_params['private_ip_address']))
            collection_formats['private_ip_address'] = 'csv'

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
            resource_path='/v3/{project_id}/private-nat/dnat-rules',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListPrivateDnatsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_nat_gateway_dnat_rule(self, request):
        """查询指定的DNAT规则详情

        查询指定的DNAT规则详情。
        
        Please refer to HUAWEI cloud API Explorer for details.

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

        cname = None

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
            cname=cname,
            response_type='ShowNatGatewayDnatRuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_private_dnat(self, request):
        """查询指定的DNAT规则详情

        查询指定的DNAT规则详情。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowPrivateDnat
        :type request: :class:`huaweicloudsdknat.v2.ShowPrivateDnatRequest`
        :rtype: :class:`huaweicloudsdknat.v2.ShowPrivateDnatResponse`
        """
        return self.show_private_dnat_with_http_info(request)

    def show_private_dnat_with_http_info(self, request):
        all_params = ['dnat_rule_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            resource_path='/v3/{project_id}/private-nat/dnat-rules/{dnat_rule_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowPrivateDnatResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_nat_gateway_dnat_rule(self, request):
        """更新DNAT规则

        更新指定的DNAT规则。
        
        Please refer to HUAWEI cloud API Explorer for details.

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

        cname = None

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
            cname=cname,
            response_type='UpdateNatGatewayDnatRuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_private_dnat(self, request):
        """更新DNAT规则

        更新指定的DNAT规则。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdatePrivateDnat
        :type request: :class:`huaweicloudsdknat.v2.UpdatePrivateDnatRequest`
        :rtype: :class:`huaweicloudsdknat.v2.UpdatePrivateDnatResponse`
        """
        return self.update_private_dnat_with_http_info(request)

    def update_private_dnat_with_http_info(self, request):
        all_params = ['dnat_rule_id', 'update_private_dnat_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            resource_path='/v3/{project_id}/private-nat/dnat-rules/{dnat_rule_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdatePrivateDnatResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_create_delete_transit_ip_tags(self, request):
        """批量添加删除中转IP标签

        - 为指定中转IP实例批量添加或删除标签
        - 标签管理服务需要使用该接口批量管理中转IP实例的标签。
        - 一个中转IP上最多有10个标签。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchCreateDeleteTransitIpTags
        :type request: :class:`huaweicloudsdknat.v2.BatchCreateDeleteTransitIpTagsRequest`
        :rtype: :class:`huaweicloudsdknat.v2.BatchCreateDeleteTransitIpTagsResponse`
        """
        return self.batch_create_delete_transit_ip_tags_with_http_info(request)

    def batch_create_delete_transit_ip_tags_with_http_info(self, request):
        all_params = ['resource_id', 'batch_create_delete_transit_ip_tags_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
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
            resource_path='/v3/{project_id}/transit-ips/{resource_id}/tags/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchCreateDeleteTransitIpTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_transit_ip_tag(self, request):
        """添加中转IP标签

        - 一个中转IP上最多有10个标签。
        - 此接口为幂等接口：
        - 创建时，如果创建的标签已经存在（key相同），则覆盖。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateTransitIpTag
        :type request: :class:`huaweicloudsdknat.v2.CreateTransitIpTagRequest`
        :rtype: :class:`huaweicloudsdknat.v2.CreateTransitIpTagResponse`
        """
        return self.create_transit_ip_tag_with_http_info(request)

    def create_transit_ip_tag_with_http_info(self, request):
        all_params = ['resource_id', 'create_transit_ip_tag_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
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
            resource_path='/v3/{project_id}/transit-ips/{resource_id}/tags',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateTransitIpTagResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_transit_ip_tag(self, request):
        """删除中转IP标签

        - 幂等接口：
        - 删除时，不对标签字符集做校验，调用接口前必须要做encodeURI，服务端需要对接口uri做decodeURI。删除的key不存在报404，key不能为空或者空字符串。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteTransitIpTag
        :type request: :class:`huaweicloudsdknat.v2.DeleteTransitIpTagRequest`
        :rtype: :class:`huaweicloudsdknat.v2.DeleteTransitIpTagResponse`
        """
        return self.delete_transit_ip_tag_with_http_info(request)

    def delete_transit_ip_tag_with_http_info(self, request):
        all_params = ['key', 'resource_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'key' in local_var_params:
            path_params['key'] = local_var_params['key']
        if 'resource_id' in local_var_params:
            path_params['resource_id'] = local_var_params['resource_id']

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
            resource_path='/v3/{project_id}/transit-ips/{resource_id}/tags/{key}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteTransitIpTagResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_transit_ip_tags(self, request):
        """查询中转IP项目标签

        - 查询租户在指定Project和实例类型的所有中转IP标签集合。
        - 标签管理服务需要能够列出当前租户全部已使用的中转IP标签集合，为打中转IP标签和过滤中转IP实例时提供标签联想功能。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListTransitIpTags
        :type request: :class:`huaweicloudsdknat.v2.ListTransitIpTagsRequest`
        :rtype: :class:`huaweicloudsdknat.v2.ListTransitIpTagsResponse`
        """
        return self.list_transit_ip_tags_with_http_info(request)

    def list_transit_ip_tags_with_http_info(self, request):
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

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/transit-ips/tags',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListTransitIpTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_transit_ips_by_tags(self, request):
        """查询中转IP实例

        - 使用标签过滤中转IP实例。
        - 标签管理服务需要提供按标签过滤中转IP服务实例并汇总显示在列表中，需要中转IP服务提供查询能力。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListTransitIpsByTags
        :type request: :class:`huaweicloudsdknat.v2.ListTransitIpsByTagsRequest`
        :rtype: :class:`huaweicloudsdknat.v2.ListTransitIpsByTagsResponse`
        """
        return self.list_transit_ips_by_tags_with_http_info(request)

    def list_transit_ips_by_tags_with_http_info(self, request):
        all_params = ['list_transit_ips_by_tags_request_body']
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
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/transit-ips/resource_instances/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListTransitIpsByTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_transit_ip_tags(self, request):
        """查询中转IP标签

        - 查询指定中转IP实例的标签信息。
        - 标签管理服务需要使用该接口查询指定中转IP实例的全部标签数据。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowTransitIpTags
        :type request: :class:`huaweicloudsdknat.v2.ShowTransitIpTagsRequest`
        :rtype: :class:`huaweicloudsdknat.v2.ShowTransitIpTagsResponse`
        """
        return self.show_transit_ip_tags_with_http_info(request)

    def show_transit_ip_tags_with_http_info(self, request):
        all_params = ['resource_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_id' in local_var_params:
            path_params['resource_id'] = local_var_params['resource_id']

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
            resource_path='/v3/{project_id}/transit-ips/{resource_id}/tags',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowTransitIpTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_create_delete_private_nat_tags(self, request):
        """批量添加删除私网NAT网关标签

        - 为指定私网NAT网关实例批量添加或删除标签
        - 标签管理服务需要使用该接口批量管理私网NAT网关实例的标签。
        - 一个私网NAT网关上最多有10个标签。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchCreateDeletePrivateNatTags
        :type request: :class:`huaweicloudsdknat.v2.BatchCreateDeletePrivateNatTagsRequest`
        :rtype: :class:`huaweicloudsdknat.v2.BatchCreateDeletePrivateNatTagsResponse`
        """
        return self.batch_create_delete_private_nat_tags_with_http_info(request)

    def batch_create_delete_private_nat_tags_with_http_info(self, request):
        all_params = ['resource_id', 'batch_create_delete_private_nat_tags_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
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
            resource_path='/v3/{project_id}/private-nat-gateways/{resource_id}/tags/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchCreateDeletePrivateNatTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_nat_gateway(self, request):
        """创建公网NAT网关

        创建公网NAT网关实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

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
            resource_path='/v2/{project_id}/nat_gateways',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateNatGatewayResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_private_nat(self, request):
        """创建私网NAT网关

        创建私网NAT网关实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreatePrivateNat
        :type request: :class:`huaweicloudsdknat.v2.CreatePrivateNatRequest`
        :rtype: :class:`huaweicloudsdknat.v2.CreatePrivateNatResponse`
        """
        return self.create_private_nat_with_http_info(request)

    def create_private_nat_with_http_info(self, request):
        all_params = ['create_private_nat_request_body']
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
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/private-nat/gateways',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreatePrivateNatResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_private_nat_tag(self, request):
        """添加私网NAT网关标签

        - 一个私网NAT网关上最多有10个标签。
        - 此接口为幂等接口：
        - 创建时，如果创建的标签已经存在（key相同），则覆盖。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreatePrivateNatTag
        :type request: :class:`huaweicloudsdknat.v2.CreatePrivateNatTagRequest`
        :rtype: :class:`huaweicloudsdknat.v2.CreatePrivateNatTagResponse`
        """
        return self.create_private_nat_tag_with_http_info(request)

    def create_private_nat_tag_with_http_info(self, request):
        all_params = ['resource_id', 'create_private_nat_tag_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
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
            resource_path='/v3/{project_id}/private-nat-gateways/{resource_id}/tags',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreatePrivateNatTagResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_nat_gateway(self, request):
        """删除公网NAT网关

        删除公网NAT网关实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

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

        cname = None

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
            cname=cname,
            response_type='DeleteNatGatewayResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_private_nat(self, request):
        """删除私网NAT网关

        删除私网NAT网关实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeletePrivateNat
        :type request: :class:`huaweicloudsdknat.v2.DeletePrivateNatRequest`
        :rtype: :class:`huaweicloudsdknat.v2.DeletePrivateNatResponse`
        """
        return self.delete_private_nat_with_http_info(request)

    def delete_private_nat_with_http_info(self, request):
        all_params = ['gateway_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'gateway_id' in local_var_params:
            path_params['gateway_id'] = local_var_params['gateway_id']

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
            resource_path='/v3/{project_id}/private-nat/gateways/{gateway_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeletePrivateNatResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_private_nat_tag(self, request):
        """删除私网NAT网关标签

        - 幂等接口：
        - 删除时，不对标签字符集做校验，调用接口前必须要做encodeURI，服务端需要对接口uri做decodeURI。删除的key不存在报404，key不能为空或者空字符串。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeletePrivateNatTag
        :type request: :class:`huaweicloudsdknat.v2.DeletePrivateNatTagRequest`
        :rtype: :class:`huaweicloudsdknat.v2.DeletePrivateNatTagResponse`
        """
        return self.delete_private_nat_tag_with_http_info(request)

    def delete_private_nat_tag_with_http_info(self, request):
        all_params = ['key', 'resource_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'key' in local_var_params:
            path_params['key'] = local_var_params['key']
        if 'resource_id' in local_var_params:
            path_params['resource_id'] = local_var_params['resource_id']

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
            resource_path='/v3/{project_id}/private-nat-gateways/{resource_id}/tags/{key}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeletePrivateNatTagResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_nat_gateways(self, request):
        """查询公网NAT网关列表

        查询公网NAT网关实例列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

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

        cname = None

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
            cname=cname,
            response_type='ListNatGatewaysResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_private_nat_tags(self, request):
        """查询私网NAT网关项目标签

        - 查询租户在指定Project和实例类型的所有私网NAT网关标签集合。
        - 标签管理服务需要能够列出当前租户全部已使用的私网NAT网关标签集合，为打私网NAT网关标签和过滤私网NAT网关实例时提供标签联想功能。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListPrivateNatTags
        :type request: :class:`huaweicloudsdknat.v2.ListPrivateNatTagsRequest`
        :rtype: :class:`huaweicloudsdknat.v2.ListPrivateNatTagsResponse`
        """
        return self.list_private_nat_tags_with_http_info(request)

    def list_private_nat_tags_with_http_info(self, request):
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

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/private-nat-gateways/tags',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListPrivateNatTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_private_nats(self, request):
        """查询私网NAT网关列表

        查询私网NAT网关实例列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListPrivateNats
        :type request: :class:`huaweicloudsdknat.v2.ListPrivateNatsRequest`
        :rtype: :class:`huaweicloudsdknat.v2.ListPrivateNatsResponse`
        """
        return self.list_private_nats_with_http_info(request)

    def list_private_nats_with_http_info(self, request):
        all_params = ['limit', 'marker', 'page_reverse', 'id', 'name', 'description', 'spec', 'status', 'vpc_id', 'virsubnet_id', 'enterprise_project_id']
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
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'page_reverse' in local_var_params:
            query_params.append(('page_reverse', local_var_params['page_reverse']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
            collection_formats['id'] = 'csv'
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
            collection_formats['name'] = 'csv'
        if 'description' in local_var_params:
            query_params.append(('description', local_var_params['description']))
            collection_formats['description'] = 'csv'
        if 'spec' in local_var_params:
            query_params.append(('spec', local_var_params['spec']))
            collection_formats['spec'] = 'csv'
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
            collection_formats['status'] = 'csv'
        if 'vpc_id' in local_var_params:
            query_params.append(('vpc_id', local_var_params['vpc_id']))
            collection_formats['vpc_id'] = 'csv'
        if 'virsubnet_id' in local_var_params:
            query_params.append(('virsubnet_id', local_var_params['virsubnet_id']))
            collection_formats['virsubnet_id'] = 'csv'
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
            collection_formats['enterprise_project_id'] = 'csv'

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
            resource_path='/v3/{project_id}/private-nat/gateways',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListPrivateNatsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_private_nats_by_tags(self, request):
        """查询私网NAT网关实例

        - 使用标签过滤私网NAT网关实例。
        - 标签管理服务需要提供按标签过滤私网NAT网关服务实例并汇总显示在列表中，需要私网NAT网关服务提供查询能力。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListPrivateNatsByTags
        :type request: :class:`huaweicloudsdknat.v2.ListPrivateNatsByTagsRequest`
        :rtype: :class:`huaweicloudsdknat.v2.ListPrivateNatsByTagsResponse`
        """
        return self.list_private_nats_by_tags_with_http_info(request)

    def list_private_nats_by_tags_with_http_info(self, request):
        all_params = ['list_private_nats_by_tags_request_body']
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
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/private-nat-gateways/resource_instances/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListPrivateNatsByTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_nat_gateway(self, request):
        """查询指定的公网NAT网关详情

        查询指定的公网NAT网关实例详情。
        
        Please refer to HUAWEI cloud API Explorer for details.

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

        cname = None

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
            cname=cname,
            response_type='ShowNatGatewayResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_private_nat(self, request):
        """查询指定的私网NAT网关详情

        查询指定的私网NAT网关实例详情。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowPrivateNat
        :type request: :class:`huaweicloudsdknat.v2.ShowPrivateNatRequest`
        :rtype: :class:`huaweicloudsdknat.v2.ShowPrivateNatResponse`
        """
        return self.show_private_nat_with_http_info(request)

    def show_private_nat_with_http_info(self, request):
        all_params = ['gateway_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'gateway_id' in local_var_params:
            path_params['gateway_id'] = local_var_params['gateway_id']

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
            resource_path='/v3/{project_id}/private-nat/gateways/{gateway_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowPrivateNatResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_private_nat_tags(self, request):
        """查询私网NAT网关标签

        - 查询指定私网NAT网关实例的标签信息。
        - 标签管理服务需要使用该接口查询指定私网NAT网关实例的全部标签数据。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowPrivateNatTags
        :type request: :class:`huaweicloudsdknat.v2.ShowPrivateNatTagsRequest`
        :rtype: :class:`huaweicloudsdknat.v2.ShowPrivateNatTagsResponse`
        """
        return self.show_private_nat_tags_with_http_info(request)

    def show_private_nat_tags_with_http_info(self, request):
        all_params = ['resource_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_id' in local_var_params:
            path_params['resource_id'] = local_var_params['resource_id']

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
            resource_path='/v3/{project_id}/private-nat-gateways/{resource_id}/tags',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowPrivateNatTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_nat_gateway(self, request):
        """更新公网NAT网关

        更新公网NAT网关实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

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

        cname = None

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
            cname=cname,
            response_type='UpdateNatGatewayResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_private_nat(self, request):
        """更新私网NAT网关

        更新私网NAT网关实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdatePrivateNat
        :type request: :class:`huaweicloudsdknat.v2.UpdatePrivateNatRequest`
        :rtype: :class:`huaweicloudsdknat.v2.UpdatePrivateNatResponse`
        """
        return self.update_private_nat_with_http_info(request)

    def update_private_nat_with_http_info(self, request):
        all_params = ['gateway_id', 'update_private_nat_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'gateway_id' in local_var_params:
            path_params['gateway_id'] = local_var_params['gateway_id']

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
            resource_path='/v3/{project_id}/private-nat/gateways/{gateway_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdatePrivateNatResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_transit_ip(self, request):
        """创建中转IP

        创建中转IP。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateTransitIp
        :type request: :class:`huaweicloudsdknat.v2.CreateTransitIpRequest`
        :rtype: :class:`huaweicloudsdknat.v2.CreateTransitIpResponse`
        """
        return self.create_transit_ip_with_http_info(request)

    def create_transit_ip_with_http_info(self, request):
        all_params = ['create_transit_ip_request_body']
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
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/private-nat/transit-ips',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateTransitIpResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_transit_ip(self, request):
        """删除中转IP

        删除中转IP。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteTransitIp
        :type request: :class:`huaweicloudsdknat.v2.DeleteTransitIpRequest`
        :rtype: :class:`huaweicloudsdknat.v2.DeleteTransitIpResponse`
        """
        return self.delete_transit_ip_with_http_info(request)

    def delete_transit_ip_with_http_info(self, request):
        all_params = ['transit_ip_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'transit_ip_id' in local_var_params:
            path_params['transit_ip_id'] = local_var_params['transit_ip_id']

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
            resource_path='/v3/{project_id}/private-nat/transit-ips/{transit_ip_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteTransitIpResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_transit_ips(self, request):
        """查询中转IP列表

        查询中转IP列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListTransitIps
        :type request: :class:`huaweicloudsdknat.v2.ListTransitIpsRequest`
        :rtype: :class:`huaweicloudsdknat.v2.ListTransitIpsResponse`
        """
        return self.list_transit_ips_with_http_info(request)

    def list_transit_ips_with_http_info(self, request):
        all_params = ['limit', 'marker', 'page_reverse', 'id', 'network_interface_id', 'ip_address', 'gateway_id', 'enterprise_project_id', 'virsubnet_id']
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
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'page_reverse' in local_var_params:
            query_params.append(('page_reverse', local_var_params['page_reverse']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
            collection_formats['id'] = 'csv'
        if 'network_interface_id' in local_var_params:
            query_params.append(('network_interface_id', local_var_params['network_interface_id']))
            collection_formats['network_interface_id'] = 'csv'
        if 'ip_address' in local_var_params:
            query_params.append(('ip_address', local_var_params['ip_address']))
            collection_formats['ip_address'] = 'csv'
        if 'gateway_id' in local_var_params:
            query_params.append(('gateway_id', local_var_params['gateway_id']))
            collection_formats['gateway_id'] = 'csv'
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
            collection_formats['enterprise_project_id'] = 'csv'
        if 'virsubnet_id' in local_var_params:
            query_params.append(('virsubnet_id', local_var_params['virsubnet_id']))
            collection_formats['virsubnet_id'] = 'csv'

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
            resource_path='/v3/{project_id}/private-nat/transit-ips',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListTransitIpsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_transit_ip(self, request):
        """查询指定的中转IP详情

        查询中转IP详情。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowTransitIp
        :type request: :class:`huaweicloudsdknat.v2.ShowTransitIpRequest`
        :rtype: :class:`huaweicloudsdknat.v2.ShowTransitIpResponse`
        """
        return self.show_transit_ip_with_http_info(request)

    def show_transit_ip_with_http_info(self, request):
        all_params = ['transit_ip_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'transit_ip_id' in local_var_params:
            path_params['transit_ip_id'] = local_var_params['transit_ip_id']

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
            resource_path='/v3/{project_id}/private-nat/transit-ips/{transit_ip_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowTransitIpResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_nat_gateway_snat_rule(self, request):
        """创建SNAT规则

        创建SNAT规则。
        
        Please refer to HUAWEI cloud API Explorer for details.

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
            resource_path='/v2/{project_id}/snat_rules',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateNatGatewaySnatRuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_private_snat(self, request):
        """创建SNAT规则

        创建SNAT规则。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreatePrivateSnat
        :type request: :class:`huaweicloudsdknat.v2.CreatePrivateSnatRequest`
        :rtype: :class:`huaweicloudsdknat.v2.CreatePrivateSnatResponse`
        """
        return self.create_private_snat_with_http_info(request)

    def create_private_snat_with_http_info(self, request):
        all_params = ['create_private_snat_request_body']
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
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/private-nat/snat-rules',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreatePrivateSnatResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_nat_gateway_snat_rule(self, request):
        """删除SNAT规则

        删除指定的SNAT规则。
        
        Please refer to HUAWEI cloud API Explorer for details.

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

        cname = None

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
            cname=cname,
            response_type='DeleteNatGatewaySnatRuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_private_snat(self, request):
        """删除SNAT规则

        删除指定的SNAT规则。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeletePrivateSnat
        :type request: :class:`huaweicloudsdknat.v2.DeletePrivateSnatRequest`
        :rtype: :class:`huaweicloudsdknat.v2.DeletePrivateSnatResponse`
        """
        return self.delete_private_snat_with_http_info(request)

    def delete_private_snat_with_http_info(self, request):
        all_params = ['snat_rule_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            resource_path='/v3/{project_id}/private-nat/snat-rules/{snat_rule_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeletePrivateSnatResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_nat_gateway_snat_rules(self, request):
        """查询SNAT规则列表

        查询SNAT规则列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

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

        cname = None

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
            cname=cname,
            response_type='ListNatGatewaySnatRulesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_private_snats(self, request):
        """查询SNAT规则列表

        查询SNAT规则列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListPrivateSnats
        :type request: :class:`huaweicloudsdknat.v2.ListPrivateSnatsRequest`
        :rtype: :class:`huaweicloudsdknat.v2.ListPrivateSnatsResponse`
        """
        return self.list_private_snats_with_http_info(request)

    def list_private_snats_with_http_info(self, request):
        all_params = ['limit', 'marker', 'page_reverse', 'id', 'description', 'gateway_id', 'cidr', 'virsubnet_id', 'transit_ip_id', 'transit_ip_address', 'enterprise_project_id']
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
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'page_reverse' in local_var_params:
            query_params.append(('page_reverse', local_var_params['page_reverse']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
            collection_formats['id'] = 'csv'
        if 'description' in local_var_params:
            query_params.append(('description', local_var_params['description']))
            collection_formats['description'] = 'csv'
        if 'gateway_id' in local_var_params:
            query_params.append(('gateway_id', local_var_params['gateway_id']))
            collection_formats['gateway_id'] = 'csv'
        if 'cidr' in local_var_params:
            query_params.append(('cidr', local_var_params['cidr']))
            collection_formats['cidr'] = 'csv'
        if 'virsubnet_id' in local_var_params:
            query_params.append(('virsubnet_id', local_var_params['virsubnet_id']))
            collection_formats['virsubnet_id'] = 'csv'
        if 'transit_ip_id' in local_var_params:
            query_params.append(('transit_ip_id', local_var_params['transit_ip_id']))
            collection_formats['transit_ip_id'] = 'csv'
        if 'transit_ip_address' in local_var_params:
            query_params.append(('transit_ip_address', local_var_params['transit_ip_address']))
            collection_formats['transit_ip_address'] = 'csv'
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
            collection_formats['enterprise_project_id'] = 'csv'

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
            resource_path='/v3/{project_id}/private-nat/snat-rules',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListPrivateSnatsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_nat_gateway_snat_rule(self, request):
        """查询指定的SNAT规则详情

        查询指定的SNAT规则详情。
        
        Please refer to HUAWEI cloud API Explorer for details.

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

        cname = None

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
            cname=cname,
            response_type='ShowNatGatewaySnatRuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_private_snat(self, request):
        """查询指定的SNAT规则详情

        查询指定的SNAT规则详情。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowPrivateSnat
        :type request: :class:`huaweicloudsdknat.v2.ShowPrivateSnatRequest`
        :rtype: :class:`huaweicloudsdknat.v2.ShowPrivateSnatResponse`
        """
        return self.show_private_snat_with_http_info(request)

    def show_private_snat_with_http_info(self, request):
        all_params = ['snat_rule_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            resource_path='/v3/{project_id}/private-nat/snat-rules/{snat_rule_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowPrivateSnatResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_nat_gateway_snat_rule(self, request):
        """更新SNAT规则

        更新指定的SNAT规则。
        
        Please refer to HUAWEI cloud API Explorer for details.

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

        cname = None

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
            cname=cname,
            response_type='UpdateNatGatewaySnatRuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_private_snat(self, request):
        """更新SNAT规则

        更新指定的SNAT规则。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdatePrivateSnat
        :type request: :class:`huaweicloudsdknat.v2.UpdatePrivateSnatRequest`
        :rtype: :class:`huaweicloudsdknat.v2.UpdatePrivateSnatResponse`
        """
        return self.update_private_snat_with_http_info(request)

    def update_private_snat_with_http_info(self, request):
        all_params = ['snat_rule_id', 'update_private_snat_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            resource_path='/v3/{project_id}/private-nat/snat-rules/{snat_rule_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdatePrivateSnatResponse',
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

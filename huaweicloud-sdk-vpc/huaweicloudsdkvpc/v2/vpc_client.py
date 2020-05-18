# coding: utf-8

from __future__ import absolute_import

import datetime
import re
import importlib

# python 2 and python 3 compatibility library
import six

from huaweicloudsdkcore.client import Client
from huaweicloudsdkcore.exceptions import exceptions
from huaweicloudsdkcore.utils import http_utils


class VpcClient(Client):
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
        super(VpcClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkvpc.v2.model")
        self.preset_headers = {'User-Agent': 'HuaweiCloud-SDK-Python'}



    def accept_vpc_peering(self, request):
        """接受对等连接请求

        租户A名下的VPC申请和租户B的VPC建立对等连接，需要等待租户B接受该请求。此接口用于租户接受其他租户发起的对等连接请求。

        :param AcceptVpcPeeringRequest request
        :return: AcceptVpcPeeringResponse
        """
        return self.accept_vpc_peering_with_http_info(request)

    def accept_vpc_peering_with_http_info(self, request):
        """接受对等连接请求

        租户A名下的VPC申请和租户B的VPC建立对等连接，需要等待租户B接受该请求。此接口用于租户接受其他租户发起的对等连接请求。

        :param AcceptVpcPeeringRequest request
        :return: tuple(AcceptVpcPeeringResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['peering_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'peering_id' in local_var_params:
            path_params['peering_id'] = local_var_params['peering_id']

        query_params = []

        header_params = {}

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/v2.0/vpc/peerings/{peering_id}/accept', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='AcceptVpcPeeringResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def associate_route_table(self, request):
        """子网关联路由表

        路由表关联子网。子网关联路由表A后，再关联B，不需要先跟路由表A解关联再关联路由表B

        :param AssociateRouteTableRequest request
        :return: AssociateRouteTableResponse
        """
        return self.associate_route_table_with_http_info(request)

    def associate_route_table_with_http_info(self, request):
        """子网关联路由表

        路由表关联子网。子网关联路由表A后，再关联B，不需要先跟路由表A解关联再关联路由表B

        :param AssociateRouteTableRequest request
        :return: tuple(AssociateRouteTableResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['routetable_id', 'routetable_associate']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'routetable_id' in local_var_params:
            path_params['routetable_id'] = local_var_params['routetable_id']

        query_params = []

        header_params = {}

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])
        auth_settings = []

        return self.call_api(
            '/v1/{project_id}/routetables/{routetable_id}/action', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='AssociateRouteTableResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def associate_vip(self, request):
        """VIP绑定接口

        只开放消费者云

        :param AssociateVipRequest request
        :return: None
        """
        return self.associate_vip_with_http_info(request)

    def associate_vip_with_http_info(self, request):
        """VIP绑定接口

        只开放消费者云

        :param AssociateVipRequest request
        :return: None
        """

        all_params = ['port_id', 'associate_vip_request_body']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'port_id' in local_var_params:
            path_params['port_id'] = local_var_params['port_id']

        query_params = []

        header_params = {}

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']


        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])
        auth_settings = []

        return self.call_api(
            '/v1/{project_id}/vport/{port_id}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type=None,
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def create_port(self, request):
        """创建端口

        创建端口。

        :param CreatePortRequest request
        :return: CreatePortResponse
        """
        return self.create_port_with_http_info(request)

    def create_port_with_http_info(self, request):
        """创建端口

        创建端口。

        :param CreatePortRequest request
        :return: tuple(CreatePortResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['port']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])
        auth_settings = []

        return self.call_api(
            '/v1/{project_id}/ports', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreatePortResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def create_route_table(self, request):
        """创建路由表

        创建路由表

        :param CreateRouteTableRequest request
        :return: CreateRouteTableResponse
        """
        return self.create_route_table_with_http_info(request)

    def create_route_table_with_http_info(self, request):
        """创建路由表

        创建路由表

        :param CreateRouteTableRequest request
        :return: tuple(CreateRouteTableResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['routetable']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])
        auth_settings = []

        return self.call_api(
            '/v1/{project_id}/routetables', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateRouteTableResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def create_security_group(self, request):
        """创建安全组

        创建安全组。

        :param CreateSecurityGroupRequest request
        :return: CreateSecurityGroupResponse
        """
        return self.create_security_group_with_http_info(request)

    def create_security_group_with_http_info(self, request):
        """创建安全组

        创建安全组。

        :param CreateSecurityGroupRequest request
        :return: tuple(CreateSecurityGroupResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['security_group']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])
        auth_settings = []

        return self.call_api(
            '/v1/{project_id}/security-groups', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateSecurityGroupResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def create_security_group_rule(self, request):
        """创建安全组规则

        创建安全组规则。

        :param CreateSecurityGroupRuleRequest request
        :return: CreateSecurityGroupRuleResponse
        """
        return self.create_security_group_rule_with_http_info(request)

    def create_security_group_rule_with_http_info(self, request):
        """创建安全组规则

        创建安全组规则。

        :param CreateSecurityGroupRuleRequest request
        :return: tuple(CreateSecurityGroupRuleResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['security_group_rule']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])
        auth_settings = []

        return self.call_api(
            '/v1/{project_id}/security-group-rules', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateSecurityGroupRuleResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def create_subnet(self, request):
        """创建子网

        创建子网。

        :param CreateSubnetRequest request
        :return: CreateSubnetResponse
        """
        return self.create_subnet_with_http_info(request)

    def create_subnet_with_http_info(self, request):
        """创建子网

        创建子网。

        :param CreateSubnetRequest request
        :return: tuple(CreateSubnetResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['subnet']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])
        auth_settings = []

        return self.call_api(
            '/v1/{project_id}/subnets', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateSubnetResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def create_vpc_peering(self, request):
        """创建对等连接

        创建对等连接。

        :param CreateVpcPeeringRequest request
        :return: CreateVpcPeeringResponse
        """
        return self.create_vpc_peering_with_http_info(request)

    def create_vpc_peering_with_http_info(self, request):
        """创建对等连接

        创建对等连接。

        :param CreateVpcPeeringRequest request
        :return: tuple(CreateVpcPeeringResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['peering']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])
        auth_settings = []

        return self.call_api(
            '/v2.0/vpc/peerings', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateVpcPeeringResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def delete_port(self, request):
        """删除端口

        删除端口。

        :param DeletePortRequest request
        :return: None
        """
        return self.delete_port_with_http_info(request)

    def delete_port_with_http_info(self, request):
        """删除端口

        删除端口。

        :param DeletePortRequest request
        :return: None
        """

        all_params = ['port_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'port_id' in local_var_params:
            path_params['port_id'] = local_var_params['port_id']

        query_params = []

        header_params = {}

        form_params = []

        body_params = None


        auth_settings = []

        return self.call_api(
            '/v1/{project_id}/ports/{port_id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type=None,
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def delete_route_table(self, request):
        """删除路由表

        删除路由表

        :param DeleteRouteTableRequest request
        :return: None
        """
        return self.delete_route_table_with_http_info(request)

    def delete_route_table_with_http_info(self, request):
        """删除路由表

        删除路由表

        :param DeleteRouteTableRequest request
        :return: None
        """

        all_params = ['routetable_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'routetable_id' in local_var_params:
            path_params['routetable_id'] = local_var_params['routetable_id']

        query_params = []

        header_params = {}

        form_params = []

        body_params = None


        auth_settings = []

        return self.call_api(
            '/v1/{project_id}/routetables/{routetable_id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type=None,
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def delete_security_group(self, request):
        """删除安全组

        删除安全组。

        :param DeleteSecurityGroupRequest request
        :return: None
        """
        return self.delete_security_group_with_http_info(request)

    def delete_security_group_with_http_info(self, request):
        """删除安全组

        删除安全组。

        :param DeleteSecurityGroupRequest request
        :return: None
        """

        all_params = ['security_group_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'security_group_id' in local_var_params:
            path_params['security_group_id'] = local_var_params['security_group_id']

        query_params = []

        header_params = {}

        form_params = []

        body_params = None


        auth_settings = []

        return self.call_api(
            '/v1/{project_id}/security-groups/{security_group_id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type=None,
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def delete_security_group_rule(self, request):
        """删除安全组规则

        删除安全组规则。

        :param DeleteSecurityGroupRuleRequest request
        :return: None
        """
        return self.delete_security_group_rule_with_http_info(request)

    def delete_security_group_rule_with_http_info(self, request):
        """删除安全组规则

        删除安全组规则。

        :param DeleteSecurityGroupRuleRequest request
        :return: None
        """

        all_params = ['security_group_rule_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'security_group_rule_id' in local_var_params:
            path_params['security_group_rule_id'] = local_var_params['security_group_rule_id']

        query_params = []

        header_params = {}

        form_params = []

        body_params = None


        auth_settings = []

        return self.call_api(
            '/v1/{project_id}/security-group-rules/{security_group_rule_id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type=None,
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def delete_subnet(self, request):
        """删除子网

        删除子网

        :param DeleteSubnetRequest request
        :return: None
        """
        return self.delete_subnet_with_http_info(request)

    def delete_subnet_with_http_info(self, request):
        """删除子网

        删除子网

        :param DeleteSubnetRequest request
        :return: None
        """

        all_params = ['vpc_id', 'subnet_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'vpc_id' in local_var_params:
            path_params['vpc_id'] = local_var_params['vpc_id']
        if 'subnet_id' in local_var_params:
            path_params['subnet_id'] = local_var_params['subnet_id']

        query_params = []

        header_params = {}

        form_params = []

        body_params = None


        auth_settings = []

        return self.call_api(
            '/v1/{project_id}/vpcs/{vpc_id}/subnets/{subnet_id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type=None,
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def delete_vpc_peering(self, request):
        """删除对等连接

        删除对等连接。 可以在在本端或对端任何一端删除对等连接。

        :param DeleteVpcPeeringRequest request
        :return: None
        """
        return self.delete_vpc_peering_with_http_info(request)

    def delete_vpc_peering_with_http_info(self, request):
        """删除对等连接

        删除对等连接。 可以在在本端或对端任何一端删除对等连接。

        :param DeleteVpcPeeringRequest request
        :return: None
        """

        all_params = ['peering_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'peering_id' in local_var_params:
            path_params['peering_id'] = local_var_params['peering_id']

        query_params = []

        header_params = {}

        form_params = []

        body_params = None


        auth_settings = []

        return self.call_api(
            '/v2.0/vpc/peerings/{peering_id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type=None,
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def disassociate_route_table(self, request):
        """子网解关联路由表

        子网解关联路由表

        :param DisassociateRouteTableRequest request
        :return: DisassociateRouteTableResponse
        """
        return self.disassociate_route_table_with_http_info(request)

    def disassociate_route_table_with_http_info(self, request):
        """子网解关联路由表

        子网解关联路由表

        :param DisassociateRouteTableRequest request
        :return: tuple(DisassociateRouteTableResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['routetable_id', 'routetable_associate']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'routetable_id' in local_var_params:
            path_params['routetable_id'] = local_var_params['routetable_id']

        query_params = []

        header_params = {}

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])
        auth_settings = []

        return self.call_api(
            '/v1/{project_id}/routetables/{routetable_id}/action', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='DisassociateRouteTableResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def disassociate_vip(self, request):
        """VIP解绑接口

        只开放消费者云

        :param DisassociateVipRequest request
        :return: None
        """
        return self.disassociate_vip_with_http_info(request)

    def disassociate_vip_with_http_info(self, request):
        """VIP解绑接口

        只开放消费者云

        :param DisassociateVipRequest request
        :return: None
        """

        all_params = ['port_id', 'disassociate_vip_request_body']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'port_id' in local_var_params:
            path_params['port_id'] = local_var_params['port_id']

        query_params = []

        header_params = {}

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']


        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])
        auth_settings = []

        return self.call_api(
            '/v1/{project_id}/vport/{port_id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type=None,
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def list_ports(self, request):
        """查询端口列表

        查询提交请求的租户的所有端口，单次查询最多返回2000条数据。

        :param ListPortsRequest request
        :return: ListPortsResponse
        """
        return self.list_ports_with_http_info(request)

    def list_ports_with_http_info(self, request):
        """查询端口列表

        查询提交请求的租户的所有端口，单次查询最多返回2000条数据。

        :param ListPortsRequest request
        :return: tuple(ListPortsResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['name', 'id', 'limit', 'admin_state_up', 'network_id', 'mac_address', 'device_id', 'device_owner', 'status', 'marker', 'fixed_ips', 'enterprise_project_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'admin_state_up' in local_var_params:
            query_params.append(('admin_state_up', local_var_params['admin_state_up']))
        if 'network_id' in local_var_params:
            query_params.append(('network_id', local_var_params['network_id']))
        if 'mac_address' in local_var_params:
            query_params.append(('mac_address', local_var_params['mac_address']))
        if 'device_id' in local_var_params:
            query_params.append(('device_id', local_var_params['device_id']))
        if 'device_owner' in local_var_params:
            query_params.append(('device_owner', local_var_params['device_owner']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'fixed_ips' in local_var_params:
            query_params.append(('fixed_ips', local_var_params['fixed_ips']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

        header_params = {}

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/v1/{project_id}/ports', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListPortsResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def list_route_tables(self, request):
        """查询路由表列表

        查询提交请求的帐户的所有路由表列表，并根据过滤条件进行过滤

        :param ListRouteTablesRequest request
        :return: ListRouteTablesResponse
        """
        return self.list_route_tables_with_http_info(request)

    def list_route_tables_with_http_info(self, request):
        """查询路由表列表

        查询提交请求的帐户的所有路由表列表，并根据过滤条件进行过滤

        :param ListRouteTablesRequest request
        :return: tuple(ListRouteTablesResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['limit', 'marker', 'id', 'vpc_id', 'subnet_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'vpc_id' in local_var_params:
            query_params.append(('vpc_id', local_var_params['vpc_id']))
        if 'subnet_id' in local_var_params:
            query_params.append(('subnet_id', local_var_params['subnet_id']))

        header_params = {}

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/v1/{project_id}/routetables', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListRouteTablesResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def list_security_group_rules(self, request):
        """查询安全组规则列表

        查询安全组规则列表。

        :param ListSecurityGroupRulesRequest request
        :return: ListSecurityGroupRulesResponse
        """
        return self.list_security_group_rules_with_http_info(request)

    def list_security_group_rules_with_http_info(self, request):
        """查询安全组规则列表

        查询安全组规则列表。

        :param ListSecurityGroupRulesRequest request
        :return: tuple(ListSecurityGroupRulesResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['marker', 'limit', 'security_group_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'security_group_id' in local_var_params:
            query_params.append(('security_group_id', local_var_params['security_group_id']))

        header_params = {}

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/v1/{project_id}/security-group-rules', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListSecurityGroupRulesResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def list_security_groups(self, request):
        """查询安全组列表

        查询安全组列表

        :param ListSecurityGroupsRequest request
        :return: ListSecurityGroupsResponse
        """
        return self.list_security_groups_with_http_info(request)

    def list_security_groups_with_http_info(self, request):
        """查询安全组列表

        查询安全组列表

        :param ListSecurityGroupsRequest request
        :return: tuple(ListSecurityGroupsResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['limit', 'marker', 'vpc_id', 'enterprise_project_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'vpc_id' in local_var_params:
            query_params.append(('vpc_id', local_var_params['vpc_id']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

        header_params = {}

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/v1/{project_id}/security-groups', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListSecurityGroupsResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def list_subnets(self, request):
        """查询子网列表

        查询子网列表

        :param ListSubnetsRequest request
        :return: ListSubnetsResponse
        """
        return self.list_subnets_with_http_info(request)

    def list_subnets_with_http_info(self, request):
        """查询子网列表

        查询子网列表

        :param ListSubnetsRequest request
        :return: tuple(ListSubnetsResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['limit', 'marker', 'vpc_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'vpc_id' in local_var_params:
            query_params.append(('vpc_id', local_var_params['vpc_id']))

        header_params = {}

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/v1/{project_id}/subnets', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListSubnetsResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def list_vpc_peerings(self, request):
        """查询对等连接列表

        查询提交请求的租户的所有对等连接。根据过滤条件进行过滤。

        :param ListVpcPeeringsRequest request
        :return: ListVpcPeeringsResponse
        """
        return self.list_vpc_peerings_with_http_info(request)

    def list_vpc_peerings_with_http_info(self, request):
        """查询对等连接列表

        查询提交请求的租户的所有对等连接。根据过滤条件进行过滤。

        :param ListVpcPeeringsRequest request
        :return: tuple(ListVpcPeeringsResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['limit', 'marker', 'id', 'name', 'status', 'tenant_id', 'vpc_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'tenant_id' in local_var_params:
            query_params.append(('tenant_id', local_var_params['tenant_id']))
        if 'vpc_id' in local_var_params:
            query_params.append(('vpc_id', local_var_params['vpc_id']))

        header_params = {}

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/v2.0/vpc/peerings', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListVpcPeeringsResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def reject_vpc_peering(self, request):
        """拒绝对等连接请求

        租户A名下的VPC申请和租户B的VPC建立对等连接，需要等待租户B接受该请求。此接口用于租户拒绝其他租户发起的对等连接请求。

        :param RejectVpcPeeringRequest request
        :return: RejectVpcPeeringResponse
        """
        return self.reject_vpc_peering_with_http_info(request)

    def reject_vpc_peering_with_http_info(self, request):
        """拒绝对等连接请求

        租户A名下的VPC申请和租户B的VPC建立对等连接，需要等待租户B接受该请求。此接口用于租户拒绝其他租户发起的对等连接请求。

        :param RejectVpcPeeringRequest request
        :return: tuple(RejectVpcPeeringResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['peering_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'peering_id' in local_var_params:
            path_params['peering_id'] = local_var_params['peering_id']

        query_params = []

        header_params = {}

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/v2.0/vpc/peerings/{peering_id}/reject', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='RejectVpcPeeringResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def show_port(self, request):
        """查询端口

        查询单个端口详情。

        :param ShowPortRequest request
        :return: ShowPortResponse
        """
        return self.show_port_with_http_info(request)

    def show_port_with_http_info(self, request):
        """查询端口

        查询单个端口详情。

        :param ShowPortRequest request
        :return: tuple(ShowPortResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['port_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'port_id' in local_var_params:
            path_params['port_id'] = local_var_params['port_id']

        query_params = []

        header_params = {}

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/v1/{project_id}/ports/{port_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowPortResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def show_quota(self, request):
        """查询配额

        查询单租户在VPC服务下的网络资源配额，包括vpc配额、子网配额、安全组配额、安全组规则配额、弹性公网IP配额，vpn配额等。

        :param ShowQuotaRequest request
        :return: ShowQuotaResponse
        """
        return self.show_quota_with_http_info(request)

    def show_quota_with_http_info(self, request):
        """查询配额

        查询单租户在VPC服务下的网络资源配额，包括vpc配额、子网配额、安全组配额、安全组规则配额、弹性公网IP配额，vpn配额等。

        :param ShowQuotaRequest request
        :return: tuple(ShowQuotaResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['type']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))

        header_params = {}

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/v1/{project_id}/quotas', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowQuotaResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def show_route_table(self, request):
        """查询路由表

        查询路由表详情

        :param ShowRouteTableRequest request
        :return: ShowRouteTableResponse
        """
        return self.show_route_table_with_http_info(request)

    def show_route_table_with_http_info(self, request):
        """查询路由表

        查询路由表详情

        :param ShowRouteTableRequest request
        :return: tuple(ShowRouteTableResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['routetable_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'routetable_id' in local_var_params:
            path_params['routetable_id'] = local_var_params['routetable_id']

        query_params = []

        header_params = {}

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/v1/{project_id}/routetables/{routetable_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowRouteTableResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def show_security_group(self, request):
        """查询安全组

        查询单个安全组详情。

        :param ShowSecurityGroupRequest request
        :return: ShowSecurityGroupResponse
        """
        return self.show_security_group_with_http_info(request)

    def show_security_group_with_http_info(self, request):
        """查询安全组

        查询单个安全组详情。

        :param ShowSecurityGroupRequest request
        :return: tuple(ShowSecurityGroupResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['security_group_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'security_group_id' in local_var_params:
            path_params['security_group_id'] = local_var_params['security_group_id']

        query_params = []

        header_params = {}

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/v1/{project_id}/security-groups/{security_group_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowSecurityGroupResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def show_security_group_rule(self, request):
        """查询安全组规则

        查询单个安全组规则详情

        :param ShowSecurityGroupRuleRequest request
        :return: ShowSecurityGroupRuleResponse
        """
        return self.show_security_group_rule_with_http_info(request)

    def show_security_group_rule_with_http_info(self, request):
        """查询安全组规则

        查询单个安全组规则详情

        :param ShowSecurityGroupRuleRequest request
        :return: tuple(ShowSecurityGroupRuleResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['security_group_rule_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'security_group_rule_id' in local_var_params:
            path_params['security_group_rule_id'] = local_var_params['security_group_rule_id']

        query_params = []

        header_params = {}

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/v1/{project_id}/security-group-rules/{security_group_rule_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowSecurityGroupRuleResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def show_subnet(self, request):
        """查询子网

        查询子网详情。

        :param ShowSubnetRequest request
        :return: ShowSubnetResponse
        """
        return self.show_subnet_with_http_info(request)

    def show_subnet_with_http_info(self, request):
        """查询子网

        查询子网详情。

        :param ShowSubnetRequest request
        :return: tuple(ShowSubnetResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['subnet_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'subnet_id' in local_var_params:
            path_params['subnet_id'] = local_var_params['subnet_id']

        query_params = []

        header_params = {}

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/v1/{project_id}/subnets/{subnet_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowSubnetResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def show_vpc_peering(self, request):
        """查询对等连接

        查询对等连接详情。

        :param ShowVpcPeeringRequest request
        :return: ShowVpcPeeringResponse
        """
        return self.show_vpc_peering_with_http_info(request)

    def show_vpc_peering_with_http_info(self, request):
        """查询对等连接

        查询对等连接详情。

        :param ShowVpcPeeringRequest request
        :return: tuple(ShowVpcPeeringResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['peering_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'peering_id' in local_var_params:
            path_params['peering_id'] = local_var_params['peering_id']

        query_params = []

        header_params = {}

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/v2.0/vpc/peerings/{peering_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowVpcPeeringResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def update_port(self, request):
        """更新端口

        更新端口。

        :param UpdatePortRequest request
        :return: UpdatePortResponse
        """
        return self.update_port_with_http_info(request)

    def update_port_with_http_info(self, request):
        """更新端口

        更新端口。

        :param UpdatePortRequest request
        :return: tuple(UpdatePortResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['port_id', 'port']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'port_id' in local_var_params:
            path_params['port_id'] = local_var_params['port_id']

        query_params = []

        header_params = {}

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])
        auth_settings = []

        return self.call_api(
            '/v1/{project_id}/ports/{port_id}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdatePortResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def update_route_table(self, request):
        """更新路由表

        更新路由表，包括可以更新路由表的名称，描述，以及新增、更新、删除路由条目

        :param UpdateRouteTableRequest request
        :return: UpdateRouteTableResponse
        """
        return self.update_route_table_with_http_info(request)

    def update_route_table_with_http_info(self, request):
        """更新路由表

        更新路由表，包括可以更新路由表的名称，描述，以及新增、更新、删除路由条目

        :param UpdateRouteTableRequest request
        :return: tuple(UpdateRouteTableResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['routetable_id', 'routetable']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'routetable_id' in local_var_params:
            path_params['routetable_id'] = local_var_params['routetable_id']

        query_params = []

        header_params = {}

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])
        auth_settings = []

        return self.call_api(
            '/v1/{project_id}/routetables/{routetable_id}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateRouteTableResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def update_subnet(self, request):
        """更新子网

        更新子网。

        :param UpdateSubnetRequest request
        :return: UpdateSubnetResponse
        """
        return self.update_subnet_with_http_info(request)

    def update_subnet_with_http_info(self, request):
        """更新子网

        更新子网。

        :param UpdateSubnetRequest request
        :return: tuple(UpdateSubnetResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['vpc_id', 'subnet_id', 'subnet']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'vpc_id' in local_var_params:
            path_params['vpc_id'] = local_var_params['vpc_id']
        if 'subnet_id' in local_var_params:
            path_params['subnet_id'] = local_var_params['subnet_id']

        query_params = []

        header_params = {}

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])
        auth_settings = []

        return self.call_api(
            '/v1/{project_id}/vpcs/{vpc_id}/subnets/{subnet_id}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateSubnetResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def update_vpc_peering(self, request):
        """更新对等连接

        更新对等连接。

        :param UpdateVpcPeeringRequest request
        :return: UpdateVpcPeeringResponse
        """
        return self.update_vpc_peering_with_http_info(request)

    def update_vpc_peering_with_http_info(self, request):
        """更新对等连接

        更新对等连接。

        :param UpdateVpcPeeringRequest request
        :return: tuple(UpdateVpcPeeringResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['peering_id', 'peering']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'peering_id' in local_var_params:
            path_params['peering_id'] = local_var_params['peering_id']

        query_params = []

        header_params = {}

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])
        auth_settings = []

        return self.call_api(
            '/v2.0/vpc/peerings/{peering_id}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateVpcPeeringResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)


    def create_ip_address_group(self, request):
        """创建IP地址组

        创建IP地址组

        :param CreateIpAddressGroupRequest request
        :return: CreateIpAddressGroupResponse
        """
        return self.create_ip_address_group_with_http_info(request)

    def create_ip_address_group_with_http_info(self, request):
        """创建IP地址组

        创建IP地址组

        :param CreateIpAddressGroupRequest request
        :return: tuple(CreateIpAddressGroupResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['address_group']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])
        auth_settings = []

        return self.call_api(
            '/v3/{project_id}/vpc/address_groups', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateIpAddressGroupResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def create_privateip(self, request):
        """申请私有IP

        申请私有IP。

        :param CreatePrivateipRequest request
        :return: CreatePrivateipResponse
        """
        return self.create_privateip_with_http_info(request)

    def create_privateip_with_http_info(self, request):
        """申请私有IP

        申请私有IP。

        :param CreatePrivateipRequest request
        :return: tuple(CreatePrivateipResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['privateips']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])
        auth_settings = []

        return self.call_api(
            '/v1/{project_id}/privateips', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreatePrivateipResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def delete_ip_address_group(self, request):
        """删除未关联安全组规则的ip地址组

        删除IP地址组，非强制删除，删除的IP地址组有关联的安全组规则时无法删除，报错提示操作冲突；没有关联的安全组规则时，删除成功。

        :param DeleteIpAddressGroupRequest request
        :return: None
        """
        return self.delete_ip_address_group_with_http_info(request)

    def delete_ip_address_group_with_http_info(self, request):
        """删除未关联安全组规则的ip地址组

        删除IP地址组，非强制删除，删除的IP地址组有关联的安全组规则时无法删除，报错提示操作冲突；没有关联的安全组规则时，删除成功。

        :param DeleteIpAddressGroupRequest request
        :return: None
        """

        all_params = ['address_group_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'address_group_id' in local_var_params:
            path_params['address_group_id'] = local_var_params['address_group_id']

        query_params = []

        header_params = {}

        form_params = []

        body_params = None


        auth_settings = []

        return self.call_api(
            '/v3/{project_id}/vpc/address_groups/{address_group_id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type=None,
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def delete_ip_address_group_force(self, request):
        """强制删除IP地址组

        强制删除IP地址组，删除的IP地址组与安全组规则关联时，会删除IP地址组与关联的安全组规则。

        :param DeleteIpAddressGroupForceRequest request
        :return: None
        """
        return self.delete_ip_address_group_force_with_http_info(request)

    def delete_ip_address_group_force_with_http_info(self, request):
        """强制删除IP地址组

        强制删除IP地址组，删除的IP地址组与安全组规则关联时，会删除IP地址组与关联的安全组规则。

        :param DeleteIpAddressGroupForceRequest request
        :return: None
        """

        all_params = ['address_group_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'address_group_id' in local_var_params:
            path_params['address_group_id'] = local_var_params['address_group_id']

        query_params = []

        header_params = {}

        form_params = []

        body_params = None


        auth_settings = []

        return self.call_api(
            '/v3/{project_id}/vpc/address_groups/{address_group_id}/force', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type=None,
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def delete_privateip(self, request):
        """删除私有IP

        删除私有IP。

        :param DeletePrivateipRequest request
        :return: None
        """
        return self.delete_privateip_with_http_info(request)

    def delete_privateip_with_http_info(self, request):
        """删除私有IP

        删除私有IP。

        :param DeletePrivateipRequest request
        :return: None
        """

        all_params = ['privateip_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'privateip_id' in local_var_params:
            path_params['privateip_id'] = local_var_params['privateip_id']

        query_params = []

        header_params = {}

        form_params = []

        body_params = None


        auth_settings = []

        return self.call_api(
            '/v1/{project_id}/privateips/{privateip_id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type=None,
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def list_ip_address_group(self, request):
        """查询IP地址组列表

        查询IP地址组列表，根据过滤条件进行过滤。

        :param ListIpAddressGroupRequest request
        :return: ListIpAddressGroupResponse
        """
        return self.list_ip_address_group_with_http_info(request)

    def list_ip_address_group_with_http_info(self, request):
        """查询IP地址组列表

        查询IP地址组列表，根据过滤条件进行过滤。

        :param ListIpAddressGroupRequest request
        :return: tuple(ListIpAddressGroupResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['id', 'name', 'ip_version', 'description', 'limit', 'marker']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'ip_version' in local_var_params:
            query_params.append(('ip_version', local_var_params['ip_version']))
        if 'description' in local_var_params:
            query_params.append(('description', local_var_params['description']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))

        header_params = {}

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/v3/{project_id}/vpc/address_groups', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListIpAddressGroupResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def list_privateips(self, request):
        """查询私有IP列表

        查询指定子网下的私有IP列表。

        :param ListPrivateipsRequest request
        :return: ListPrivateipsResponse
        """
        return self.list_privateips_with_http_info(request)

    def list_privateips_with_http_info(self, request):
        """查询私有IP列表

        查询指定子网下的私有IP列表。

        :param ListPrivateipsRequest request
        :return: tuple(ListPrivateipsResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['subnet_id', 'limit', 'marker']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'subnet_id' in local_var_params:
            path_params['subnet_id'] = local_var_params['subnet_id']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))

        header_params = {}

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/v1/{project_id}/subnets/{subnet_id}/privateips', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListPrivateipsResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def show_ip_address_group(self, request):
        """查询IP地址组

        查询IP地址组详情。

        :param ShowIpAddressGroupRequest request
        :return: ShowIpAddressGroupResponse
        """
        return self.show_ip_address_group_with_http_info(request)

    def show_ip_address_group_with_http_info(self, request):
        """查询IP地址组

        查询IP地址组详情。

        :param ShowIpAddressGroupRequest request
        :return: tuple(ShowIpAddressGroupResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['address_group_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'address_group_id' in local_var_params:
            path_params['address_group_id'] = local_var_params['address_group_id']

        query_params = []

        header_params = {}

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/v3/{project_id}/vpc/address_groups/{address_group_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowIpAddressGroupResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def show_network_ip_availabilities(self, request):
        """查询网络IP使用情况

        显示一个指定网络中的IP地址使用情况。 包括此网络中的IP总数以及已用IP总数，以及网络下每一个子网的IP地址总数和可用IP地址总数。  > 须知  - 系统预留地址指的是子网的第1个以及最后4个地址，一般用于网关、DHCP等服务。 - 这里以及下文描述的IP地址总数、已用IP地址总数不包含系统预留地址。 - 在分配IP时，用户可以指定系统预留的IP地址。但是不论IP是如何分配的，只要是处于系统预留IP地址段的IP均不会被统计到已用IP地址数目和IP地址总数中。

        :param ShowNetworkIpAvailabilitiesRequest request
        :return: ShowNetworkIpAvailabilitiesResponse
        """
        return self.show_network_ip_availabilities_with_http_info(request)

    def show_network_ip_availabilities_with_http_info(self, request):
        """查询网络IP使用情况

        显示一个指定网络中的IP地址使用情况。 包括此网络中的IP总数以及已用IP总数，以及网络下每一个子网的IP地址总数和可用IP地址总数。  > 须知  - 系统预留地址指的是子网的第1个以及最后4个地址，一般用于网关、DHCP等服务。 - 这里以及下文描述的IP地址总数、已用IP地址总数不包含系统预留地址。 - 在分配IP时，用户可以指定系统预留的IP地址。但是不论IP是如何分配的，只要是处于系统预留IP地址段的IP均不会被统计到已用IP地址数目和IP地址总数中。

        :param ShowNetworkIpAvailabilitiesRequest request
        :return: tuple(ShowNetworkIpAvailabilitiesResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['network_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'network_id' in local_var_params:
            path_params['network_id'] = local_var_params['network_id']

        query_params = []

        header_params = {}

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/v2.0/network-ip-availabilities/{network_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowNetworkIpAvailabilitiesResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def show_privateip(self, request):
        """查询私有IP

        指定ID查询私有IP。

        :param ShowPrivateipRequest request
        :return: ShowPrivateipResponse
        """
        return self.show_privateip_with_http_info(request)

    def show_privateip_with_http_info(self, request):
        """查询私有IP

        指定ID查询私有IP。

        :param ShowPrivateipRequest request
        :return: tuple(ShowPrivateipResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['privateip_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'privateip_id' in local_var_params:
            path_params['privateip_id'] = local_var_params['privateip_id']

        query_params = []

        header_params = {}

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/v1/{project_id}/privateips/{privateip_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowPrivateipResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)


    def neutron_add_router_interface(self, request):
        """路由器添加接口

        添加路由器接口。

        :param NeutronAddRouterInterfaceRequest request
        :return: NeutronAddRouterInterfaceResponse
        """
        return self.neutron_add_router_interface_with_http_info(request)

    def neutron_add_router_interface_with_http_info(self, request):
        """路由器添加接口

        添加路由器接口。

        :param NeutronAddRouterInterfaceRequest request
        :return: tuple(NeutronAddRouterInterfaceResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['router_id', 'add_router_interface']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'router_id' in local_var_params:
            path_params['router_id'] = local_var_params['router_id']

        query_params = []

        header_params = {}

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])
        auth_settings = []

        return self.call_api(
            '/v2.0/routers/{router_id}/add_router_interface', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='NeutronAddRouterInterfaceResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def neutron_create_network(self, request):
        """创建网络

        创建网络

        :param NeutronCreateNetworkRequest request
        :return: NeutronCreateNetworkResponse
        """
        return self.neutron_create_network_with_http_info(request)

    def neutron_create_network_with_http_info(self, request):
        """创建网络

        创建网络

        :param NeutronCreateNetworkRequest request
        :return: tuple(NeutronCreateNetworkResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['network']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])
        auth_settings = []

        return self.call_api(
            '/v2.0/networks', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='NeutronCreateNetworkResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def neutron_create_port(self, request):
        """创建端口

        创建端口。

        :param NeutronCreatePortRequest request
        :return: NeutronCreatePortResponse
        """
        return self.neutron_create_port_with_http_info(request)

    def neutron_create_port_with_http_info(self, request):
        """创建端口

        创建端口。

        :param NeutronCreatePortRequest request
        :return: tuple(NeutronCreatePortResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['port']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])
        auth_settings = []

        return self.call_api(
            '/v2.0/ports', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='NeutronCreatePortResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def neutron_create_router(self, request):
        """创建路由器

        创建路由器。

        :param NeutronCreateRouterRequest request
        :return: NeutronCreateRouterResponse
        """
        return self.neutron_create_router_with_http_info(request)

    def neutron_create_router_with_http_info(self, request):
        """创建路由器

        创建路由器。

        :param NeutronCreateRouterRequest request
        :return: tuple(NeutronCreateRouterResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['router']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])
        auth_settings = []

        return self.call_api(
            '/v2.0/routers', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='NeutronCreateRouterResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def neutron_create_security_group(self, request):
        """创建安全组

        创建安全组

        :param NeutronCreateSecurityGroupRequest request
        :return: NeutronCreateSecurityGroupResponse
        """
        return self.neutron_create_security_group_with_http_info(request)

    def neutron_create_security_group_with_http_info(self, request):
        """创建安全组

        创建安全组

        :param NeutronCreateSecurityGroupRequest request
        :return: tuple(NeutronCreateSecurityGroupResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['security_group']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])
        auth_settings = []

        return self.call_api(
            '/v2.0/security-groups', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='NeutronCreateSecurityGroupResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def neutron_create_security_group_rule(self, request):
        """创建安全组规则

        创建安全组规则

        :param NeutronCreateSecurityGroupRuleRequest request
        :return: NeutronCreateSecurityGroupRuleResponse
        """
        return self.neutron_create_security_group_rule_with_http_info(request)

    def neutron_create_security_group_rule_with_http_info(self, request):
        """创建安全组规则

        创建安全组规则

        :param NeutronCreateSecurityGroupRuleRequest request
        :return: tuple(NeutronCreateSecurityGroupRuleResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['security_group_rule']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])
        auth_settings = []

        return self.call_api(
            '/v2.0/security-group-rules', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='NeutronCreateSecurityGroupRuleResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def neutron_create_subnet(self, request):
        """创建子网

        创建子网。

        :param NeutronCreateSubnetRequest request
        :return: NeutronCreateSubnetResponse
        """
        return self.neutron_create_subnet_with_http_info(request)

    def neutron_create_subnet_with_http_info(self, request):
        """创建子网

        创建子网。

        :param NeutronCreateSubnetRequest request
        :return: tuple(NeutronCreateSubnetResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['subnet']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])
        auth_settings = []

        return self.call_api(
            '/v2.0/subnets', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='NeutronCreateSubnetResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def neutron_delete_network(self, request):
        """删除网络

        删除网络

        :param NeutronDeleteNetworkRequest request
        :return: None
        """
        return self.neutron_delete_network_with_http_info(request)

    def neutron_delete_network_with_http_info(self, request):
        """删除网络

        删除网络

        :param NeutronDeleteNetworkRequest request
        :return: None
        """

        all_params = ['network_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'network_id' in local_var_params:
            path_params['network_id'] = local_var_params['network_id']

        query_params = []

        header_params = {}

        form_params = []

        body_params = None


        auth_settings = []

        return self.call_api(
            '/v2.0/networks/{network_id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type=None,
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def neutron_delete_port(self, request):
        """删除端口

        删除端口。

        :param NeutronDeletePortRequest request
        :return: None
        """
        return self.neutron_delete_port_with_http_info(request)

    def neutron_delete_port_with_http_info(self, request):
        """删除端口

        删除端口。

        :param NeutronDeletePortRequest request
        :return: None
        """

        all_params = ['port_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'port_id' in local_var_params:
            path_params['port_id'] = local_var_params['port_id']

        query_params = []

        header_params = {}

        form_params = []

        body_params = None


        auth_settings = []

        return self.call_api(
            '/v2.0/ports/{port_id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type=None,
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def neutron_delete_router(self, request):
        """删除路由器

        删除路由器

        :param NeutronDeleteRouterRequest request
        :return: None
        """
        return self.neutron_delete_router_with_http_info(request)

    def neutron_delete_router_with_http_info(self, request):
        """删除路由器

        删除路由器

        :param NeutronDeleteRouterRequest request
        :return: None
        """

        all_params = ['router_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'router_id' in local_var_params:
            path_params['router_id'] = local_var_params['router_id']

        query_params = []

        header_params = {}

        form_params = []

        body_params = None


        auth_settings = []

        return self.call_api(
            '/v2.0/routers/{router_id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type=None,
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def neutron_delete_security_group(self, request):
        """删除安全组

        删除安全组

        :param NeutronDeleteSecurityGroupRequest request
        :return: None
        """
        return self.neutron_delete_security_group_with_http_info(request)

    def neutron_delete_security_group_with_http_info(self, request):
        """删除安全组

        删除安全组

        :param NeutronDeleteSecurityGroupRequest request
        :return: None
        """

        all_params = ['security_group_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'security_group_id' in local_var_params:
            path_params['security_group_id'] = local_var_params['security_group_id']

        query_params = []

        header_params = {}

        form_params = []

        body_params = None


        auth_settings = []

        return self.call_api(
            '/v2.0/security-groups/{security_group_id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type=None,
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def neutron_delete_security_group_rule(self, request):
        """删除安全组规则

        删除安全组规则

        :param NeutronDeleteSecurityGroupRuleRequest request
        :return: None
        """
        return self.neutron_delete_security_group_rule_with_http_info(request)

    def neutron_delete_security_group_rule_with_http_info(self, request):
        """删除安全组规则

        删除安全组规则

        :param NeutronDeleteSecurityGroupRuleRequest request
        :return: None
        """

        all_params = ['security_group_rule_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'security_group_rule_id' in local_var_params:
            path_params['security_group_rule_id'] = local_var_params['security_group_rule_id']

        query_params = []

        header_params = {}

        form_params = []

        body_params = None


        auth_settings = []

        return self.call_api(
            '/v2.0/security-group-rules/{security_group_rule_id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type=None,
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def neutron_delete_subnet(self, request):
        """删除子网

        删除子网

        :param NeutronDeleteSubnetRequest request
        :return: None
        """
        return self.neutron_delete_subnet_with_http_info(request)

    def neutron_delete_subnet_with_http_info(self, request):
        """删除子网

        删除子网

        :param NeutronDeleteSubnetRequest request
        :return: None
        """

        all_params = ['subnet_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'subnet_id' in local_var_params:
            path_params['subnet_id'] = local_var_params['subnet_id']

        query_params = []

        header_params = {}

        form_params = []

        body_params = None


        auth_settings = []

        return self.call_api(
            '/v2.0/subnets/{subnet_id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type=None,
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def neutron_list_networks(self, request):
        """查询网络列表

        查询提交请求的租户的所有网络，单次查询最多返回2000条数据，超过2000后会返回分页标记。分页查询请参考分页查询。

        :param NeutronListNetworksRequest request
        :return: NeutronListNetworksResponse
        """
        return self.neutron_list_networks_with_http_info(request)

    def neutron_list_networks_with_http_info(self, request):
        """查询网络列表

        查询提交请求的租户的所有网络，单次查询最多返回2000条数据，超过2000后会返回分页标记。分页查询请参考分页查询。

        :param NeutronListNetworksRequest request
        :return: tuple(NeutronListNetworksResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['limit', 'marker', 'id', 'name', 'status', 'shared', 'routerexternal', 'admin_state_up', 'providernetwork_type', 'tenant_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'shared' in local_var_params:
            query_params.append(('shared', local_var_params['shared']))
        if 'routerexternal' in local_var_params:
            query_params.append(('router:external', local_var_params['routerexternal']))
        if 'admin_state_up' in local_var_params:
            query_params.append(('admin_state_up', local_var_params['admin_state_up']))
        if 'providernetwork_type' in local_var_params:
            query_params.append(('provider:network_type', local_var_params['providernetwork_type']))
        if 'tenant_id' in local_var_params:
            query_params.append(('tenant_id', local_var_params['tenant_id']))

        header_params = {}

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/v2.0/networks', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='NeutronListNetworksResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def neutron_list_ports(self, request):
        """查询端口列表

        查询提交请求的租户的所有端口，单次查询最多返回2000条数据，超过2000后会返回分页标记。分页查询请参考分页查询。

        :param NeutronListPortsRequest request
        :return: NeutronListPortsResponse
        """
        return self.neutron_list_ports_with_http_info(request)

    def neutron_list_ports_with_http_info(self, request):
        """查询端口列表

        查询提交请求的租户的所有端口，单次查询最多返回2000条数据，超过2000后会返回分页标记。分页查询请参考分页查询。

        :param NeutronListPortsRequest request
        :return: tuple(NeutronListPortsResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['limit', 'marker', 'id', 'name', 'admin_state_up', 'network_id', 'mac_address', 'device_id', 'device_owner', 'status', 'fixed_ips', 'tenant_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'admin_state_up' in local_var_params:
            query_params.append(('admin_state_up', local_var_params['admin_state_up']))
        if 'network_id' in local_var_params:
            query_params.append(('network_id', local_var_params['network_id']))
        if 'mac_address' in local_var_params:
            query_params.append(('mac_address', local_var_params['mac_address']))
        if 'device_id' in local_var_params:
            query_params.append(('device_id', local_var_params['device_id']))
        if 'device_owner' in local_var_params:
            query_params.append(('device_owner', local_var_params['device_owner']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'fixed_ips' in local_var_params:
            query_params.append(('fixed_ips', local_var_params['fixed_ips']))
            collection_formats['fixed_ips'] = 'multi'
        if 'tenant_id' in local_var_params:
            query_params.append(('tenant_id', local_var_params['tenant_id']))

        header_params = {}

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/v2.0/ports', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='NeutronListPortsResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def neutron_list_routers(self, request):
        """查询路由器列表

        查询提交请求的租户有权限操作的所有路由器信息，单次查询最多返回2000条数据，超过2000后会返回分页标记。

        :param NeutronListRoutersRequest request
        :return: NeutronListRoutersResponse
        """
        return self.neutron_list_routers_with_http_info(request)

    def neutron_list_routers_with_http_info(self, request):
        """查询路由器列表

        查询提交请求的租户有权限操作的所有路由器信息，单次查询最多返回2000条数据，超过2000后会返回分页标记。

        :param NeutronListRoutersRequest request
        :return: tuple(NeutronListRoutersResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['limit', 'marker', 'id', 'status', 'tenant_id', 'admin_state_up']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'tenant_id' in local_var_params:
            query_params.append(('tenant_id', local_var_params['tenant_id']))
        if 'admin_state_up' in local_var_params:
            query_params.append(('admin_state_up', local_var_params['admin_state_up']))

        header_params = {}

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/v2.0/routers', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='NeutronListRoutersResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def neutron_list_security_group_rules(self, request):
        """查询安全组规则列表

        查询提交请求的租户有权限查看的所有安全组规则。单次查询最多返回2000条数据，超过2000后会返回分页标记。分页查询请参考分页查询

        :param NeutronListSecurityGroupRulesRequest request
        :return: NeutronListSecurityGroupRulesResponse
        """
        return self.neutron_list_security_group_rules_with_http_info(request)

    def neutron_list_security_group_rules_with_http_info(self, request):
        """查询安全组规则列表

        查询提交请求的租户有权限查看的所有安全组规则。单次查询最多返回2000条数据，超过2000后会返回分页标记。分页查询请参考分页查询

        :param NeutronListSecurityGroupRulesRequest request
        :return: tuple(NeutronListSecurityGroupRulesResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['limit', 'marker', 'id', 'direction', 'protocol', 'ethertype', 'description', 'remote_ip_prefix', 'remote_group_id', 'security_group_id', 'port_range_max', 'port_range_min', 'tenant_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'direction' in local_var_params:
            query_params.append(('direction', local_var_params['direction']))
        if 'protocol' in local_var_params:
            query_params.append(('protocol', local_var_params['protocol']))
        if 'ethertype' in local_var_params:
            query_params.append(('ethertype', local_var_params['ethertype']))
        if 'description' in local_var_params:
            query_params.append(('description', local_var_params['description']))
        if 'remote_ip_prefix' in local_var_params:
            query_params.append(('remote_ip_prefix', local_var_params['remote_ip_prefix']))
        if 'remote_group_id' in local_var_params:
            query_params.append(('remote_group_id', local_var_params['remote_group_id']))
        if 'security_group_id' in local_var_params:
            query_params.append(('security_group_id', local_var_params['security_group_id']))
        if 'port_range_max' in local_var_params:
            query_params.append(('port_range_max', local_var_params['port_range_max']))
        if 'port_range_min' in local_var_params:
            query_params.append(('port_range_min', local_var_params['port_range_min']))
        if 'tenant_id' in local_var_params:
            query_params.append(('tenant_id', local_var_params['tenant_id']))

        header_params = {}

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/v2.0/security-group-rules', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='NeutronListSecurityGroupRulesResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def neutron_list_security_groups(self, request):
        """查询安全组列表

        查询提交请求租户的所有安全组，单次查询最多返回2000条数据，超过2000后会返回分页标记。分页查询请参考分页查询 。

        :param NeutronListSecurityGroupsRequest request
        :return: NeutronListSecurityGroupsResponse
        """
        return self.neutron_list_security_groups_with_http_info(request)

    def neutron_list_security_groups_with_http_info(self, request):
        """查询安全组列表

        查询提交请求租户的所有安全组，单次查询最多返回2000条数据，超过2000后会返回分页标记。分页查询请参考分页查询 。

        :param NeutronListSecurityGroupsRequest request
        :return: tuple(NeutronListSecurityGroupsResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['limit', 'marker', 'id', 'name', 'description', 'tenant_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'description' in local_var_params:
            query_params.append(('description', local_var_params['description']))
        if 'tenant_id' in local_var_params:
            query_params.append(('tenant_id', local_var_params['tenant_id']))

        header_params = {}

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/v2.0/security-groups', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='NeutronListSecurityGroupsResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def neutron_list_subnets(self, request):
        """查询子网列表

        查询提交请求租户的所有子网，单次查询最多返回2000条数据，超过2000后会返回分页标记。分页查询请参考分页查询 。

        :param NeutronListSubnetsRequest request
        :return: NeutronListSubnetsResponse
        """
        return self.neutron_list_subnets_with_http_info(request)

    def neutron_list_subnets_with_http_info(self, request):
        """查询子网列表

        查询提交请求租户的所有子网，单次查询最多返回2000条数据，超过2000后会返回分页标记。分页查询请参考分页查询 。

        :param NeutronListSubnetsRequest request
        :return: tuple(NeutronListSubnetsResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['limit', 'marker', 'id', 'cidr', 'name', 'enable_dhcp', 'network_id', 'ip_version', 'gateway_ip', 'tenant_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'cidr' in local_var_params:
            query_params.append(('cidr', local_var_params['cidr']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'enable_dhcp' in local_var_params:
            query_params.append(('enable_dhcp', local_var_params['enable_dhcp']))
        if 'network_id' in local_var_params:
            query_params.append(('network_id', local_var_params['network_id']))
        if 'ip_version' in local_var_params:
            query_params.append(('ip_version', local_var_params['ip_version']))
        if 'gateway_ip' in local_var_params:
            query_params.append(('gateway_ip', local_var_params['gateway_ip']))
        if 'tenant_id' in local_var_params:
            query_params.append(('tenant_id', local_var_params['tenant_id']))

        header_params = {}

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/v2.0/subnets', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='NeutronListSubnetsResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def neutron_remove_router_interface(self, request):
        """路由器删除接口

        删除路由器接口。

        :param NeutronRemoveRouterInterfaceRequest request
        :return: NeutronRemoveRouterInterfaceResponse
        """
        return self.neutron_remove_router_interface_with_http_info(request)

    def neutron_remove_router_interface_with_http_info(self, request):
        """路由器删除接口

        删除路由器接口。

        :param NeutronRemoveRouterInterfaceRequest request
        :return: tuple(NeutronRemoveRouterInterfaceResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['router_id', 'remove_router_interface']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'router_id' in local_var_params:
            path_params['router_id'] = local_var_params['router_id']

        query_params = []

        header_params = {}

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])
        auth_settings = []

        return self.call_api(
            '/v2.0/routers/{router_id}/remove_router_interface', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='NeutronRemoveRouterInterfaceResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def neutron_show_network(self, request):
        """查询网络

        查询指定的网络详情

        :param NeutronShowNetworkRequest request
        :return: NeutronShowNetworkResponse
        """
        return self.neutron_show_network_with_http_info(request)

    def neutron_show_network_with_http_info(self, request):
        """查询网络

        查询指定的网络详情

        :param NeutronShowNetworkRequest request
        :return: tuple(NeutronShowNetworkResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['network_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'network_id' in local_var_params:
            path_params['network_id'] = local_var_params['network_id']

        query_params = []

        header_params = {}

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/v2.0/networks/{network_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='NeutronShowNetworkResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def neutron_show_port(self, request):
        """查询端口

        查询端口详情。

        :param NeutronShowPortRequest request
        :return: NeutronShowPortResponse
        """
        return self.neutron_show_port_with_http_info(request)

    def neutron_show_port_with_http_info(self, request):
        """查询端口

        查询端口详情。

        :param NeutronShowPortRequest request
        :return: tuple(NeutronShowPortResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['port_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'port_id' in local_var_params:
            path_params['port_id'] = local_var_params['port_id']

        query_params = []

        header_params = {}

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/v2.0/ports/{port_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='NeutronShowPortResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def neutron_show_router(self, request):
        """查询路由器

        查询路由器详情。

        :param NeutronShowRouterRequest request
        :return: NeutronShowRouterResponse
        """
        return self.neutron_show_router_with_http_info(request)

    def neutron_show_router_with_http_info(self, request):
        """查询路由器

        查询路由器详情。

        :param NeutronShowRouterRequest request
        :return: tuple(NeutronShowRouterResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['router_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'router_id' in local_var_params:
            path_params['router_id'] = local_var_params['router_id']

        query_params = []

        header_params = {}

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/v2.0/routers/{router_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='NeutronShowRouterResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def neutron_show_security_group(self, request):
        """查询安全组

        查询安全组详情

        :param NeutronShowSecurityGroupRequest request
        :return: NeutronShowSecurityGroupResponse
        """
        return self.neutron_show_security_group_with_http_info(request)

    def neutron_show_security_group_with_http_info(self, request):
        """查询安全组

        查询安全组详情

        :param NeutronShowSecurityGroupRequest request
        :return: tuple(NeutronShowSecurityGroupResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['security_group_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'security_group_id' in local_var_params:
            path_params['security_group_id'] = local_var_params['security_group_id']

        query_params = []

        header_params = {}

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/v2.0/security-groups/{security_group_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='NeutronShowSecurityGroupResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def neutron_show_security_group_rule(self, request):
        """查询安全组规则

        查询安全组规则详情。

        :param NeutronShowSecurityGroupRuleRequest request
        :return: NeutronShowSecurityGroupRuleResponse
        """
        return self.neutron_show_security_group_rule_with_http_info(request)

    def neutron_show_security_group_rule_with_http_info(self, request):
        """查询安全组规则

        查询安全组规则详情。

        :param NeutronShowSecurityGroupRuleRequest request
        :return: tuple(NeutronShowSecurityGroupRuleResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['security_group_rule_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'security_group_rule_id' in local_var_params:
            path_params['security_group_rule_id'] = local_var_params['security_group_rule_id']

        query_params = []

        header_params = {}

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/v2.0/security-group-rules/{security_group_rule_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='NeutronShowSecurityGroupRuleResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def neutron_show_subnet(self, request):
        """查询子网

        查询子网详情

        :param NeutronShowSubnetRequest request
        :return: NeutronShowSubnetResponse
        """
        return self.neutron_show_subnet_with_http_info(request)

    def neutron_show_subnet_with_http_info(self, request):
        """查询子网

        查询子网详情

        :param NeutronShowSubnetRequest request
        :return: tuple(NeutronShowSubnetResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['subnet_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'subnet_id' in local_var_params:
            path_params['subnet_id'] = local_var_params['subnet_id']

        query_params = []

        header_params = {}

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/v2.0/subnets/{subnet_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='NeutronShowSubnetResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def neutron_update_network(self, request):
        """更新网络

        更新网络

        :param NeutronUpdateNetworkRequest request
        :return: NeutronUpdateNetworkResponse
        """
        return self.neutron_update_network_with_http_info(request)

    def neutron_update_network_with_http_info(self, request):
        """更新网络

        更新网络

        :param NeutronUpdateNetworkRequest request
        :return: tuple(NeutronUpdateNetworkResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['network_id', 'network']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'network_id' in local_var_params:
            path_params['network_id'] = local_var_params['network_id']

        query_params = []

        header_params = {}

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])
        auth_settings = []

        return self.call_api(
            '/v2.0/networks/{network_id}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='NeutronUpdateNetworkResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def neutron_update_port(self, request):
        """更新端口

        更新端口

        :param NeutronUpdatePortRequest request
        :return: NeutronUpdatePortResponse
        """
        return self.neutron_update_port_with_http_info(request)

    def neutron_update_port_with_http_info(self, request):
        """更新端口

        更新端口

        :param NeutronUpdatePortRequest request
        :return: tuple(NeutronUpdatePortResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['port_id', 'port']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'port_id' in local_var_params:
            path_params['port_id'] = local_var_params['port_id']

        query_params = []

        header_params = {}

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])
        auth_settings = []

        return self.call_api(
            '/v2.0/ports/{port_id}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='NeutronUpdatePortResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def neutron_update_router(self, request):
        """更新路由器

        更新路由器。

        :param NeutronUpdateRouterRequest request
        :return: NeutronUpdateRouterResponse
        """
        return self.neutron_update_router_with_http_info(request)

    def neutron_update_router_with_http_info(self, request):
        """更新路由器

        更新路由器。

        :param NeutronUpdateRouterRequest request
        :return: tuple(NeutronUpdateRouterResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['router_id', 'router']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'router_id' in local_var_params:
            path_params['router_id'] = local_var_params['router_id']

        query_params = []

        header_params = {}

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])
        auth_settings = []

        return self.call_api(
            '/v2.0/routers/{router_id}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='NeutronUpdateRouterResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def neutron_update_security_group(self, request):
        """更新安全组

        更新安全组

        :param NeutronUpdateSecurityGroupRequest request
        :return: NeutronUpdateSecurityGroupResponse
        """
        return self.neutron_update_security_group_with_http_info(request)

    def neutron_update_security_group_with_http_info(self, request):
        """更新安全组

        更新安全组

        :param NeutronUpdateSecurityGroupRequest request
        :return: tuple(NeutronUpdateSecurityGroupResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['security_group_id', 'security_group']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'security_group_id' in local_var_params:
            path_params['security_group_id'] = local_var_params['security_group_id']

        query_params = []

        header_params = {}

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])
        auth_settings = []

        return self.call_api(
            '/v2.0/security-groups/{security_group_id}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='NeutronUpdateSecurityGroupResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def neutron_update_subnet(self, request):
        """更新子网

        更新子网

        :param NeutronUpdateSubnetRequest request
        :return: NeutronUpdateSubnetResponse
        """
        return self.neutron_update_subnet_with_http_info(request)

    def neutron_update_subnet_with_http_info(self, request):
        """更新子网

        更新子网

        :param NeutronUpdateSubnetRequest request
        :return: tuple(NeutronUpdateSubnetResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['subnet_id', 'subnet']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'subnet_id' in local_var_params:
            path_params['subnet_id'] = local_var_params['subnet_id']

        query_params = []

        header_params = {}

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])
        auth_settings = []

        return self.call_api(
            '/v2.0/subnets/{subnet_id}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='NeutronUpdateSubnetResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)


    def neutron_add_firewall_rule(self, request):
        """插入网络ACL规则

        插入一条网络ACL规则到某一网络ACL策略中。

        :param NeutronAddFirewallRuleRequest request
        :return: NeutronAddFirewallRuleResponse
        """
        return self.neutron_add_firewall_rule_with_http_info(request)

    def neutron_add_firewall_rule_with_http_info(self, request):
        """插入网络ACL规则

        插入一条网络ACL规则到某一网络ACL策略中。

        :param NeutronAddFirewallRuleRequest request
        :return: tuple(NeutronAddFirewallRuleResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['firewall_policy_id', 'insert_firewall_rule']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'firewall_policy_id' in local_var_params:
            path_params['firewall_policy_id'] = local_var_params['firewall_policy_id']

        query_params = []

        header_params = {}

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])
        auth_settings = []

        return self.call_api(
            '/v2.0/fwaas/firewall_policies/{firewall_policy_id}/insert_rule', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='NeutronAddFirewallRuleResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def neutron_create_firewall_group(self, request):
        """创建网络ACL组

        创建网络ACL组。

        :param NeutronCreateFirewallGroupRequest request
        :return: NeutronCreateFirewallGroupResponse
        """
        return self.neutron_create_firewall_group_with_http_info(request)

    def neutron_create_firewall_group_with_http_info(self, request):
        """创建网络ACL组

        创建网络ACL组。

        :param NeutronCreateFirewallGroupRequest request
        :return: tuple(NeutronCreateFirewallGroupResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['firewall_group']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])
        auth_settings = []

        return self.call_api(
            '/v2.0/fwaas/firewall_groups', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='NeutronCreateFirewallGroupResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def neutron_create_firewall_policy(self, request):
        """创建网络ACL策略

        创建网络ACL策略。

        :param NeutronCreateFirewallPolicyRequest request
        :return: NeutronCreateFirewallPolicyResponse
        """
        return self.neutron_create_firewall_policy_with_http_info(request)

    def neutron_create_firewall_policy_with_http_info(self, request):
        """创建网络ACL策略

        创建网络ACL策略。

        :param NeutronCreateFirewallPolicyRequest request
        :return: tuple(NeutronCreateFirewallPolicyResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['firewall_policy']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])
        auth_settings = []

        return self.call_api(
            '/v2.0/fwaas/firewall_policies', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='NeutronCreateFirewallPolicyResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def neutron_create_firewall_rule(self, request):
        """创建网络ACL规则

        创建网络ACL规则。

        :param NeutronCreateFirewallRuleRequest request
        :return: NeutronCreateFirewallRuleResponse
        """
        return self.neutron_create_firewall_rule_with_http_info(request)

    def neutron_create_firewall_rule_with_http_info(self, request):
        """创建网络ACL规则

        创建网络ACL规则。

        :param NeutronCreateFirewallRuleRequest request
        :return: tuple(NeutronCreateFirewallRuleResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['firewall_rule']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])
        auth_settings = []

        return self.call_api(
            '/v2.0/fwaas/firewall_rules', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='NeutronCreateFirewallRuleResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def neutron_delete_firewall_group(self, request):
        """删除网络ACL组

        删除网络ACL组。

        :param NeutronDeleteFirewallGroupRequest request
        :return: None
        """
        return self.neutron_delete_firewall_group_with_http_info(request)

    def neutron_delete_firewall_group_with_http_info(self, request):
        """删除网络ACL组

        删除网络ACL组。

        :param NeutronDeleteFirewallGroupRequest request
        :return: None
        """

        all_params = ['firewall_group_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'firewall_group_id' in local_var_params:
            path_params['firewall_group_id'] = local_var_params['firewall_group_id']

        query_params = []

        header_params = {}

        form_params = []

        body_params = None


        auth_settings = []

        return self.call_api(
            '/v2.0/fwaas/firewall_groups/{firewall_group_id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type=None,
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def neutron_delete_firewall_policy(self, request):
        """删除网络ACL策略

        删除网络ACL策略。

        :param NeutronDeleteFirewallPolicyRequest request
        :return: None
        """
        return self.neutron_delete_firewall_policy_with_http_info(request)

    def neutron_delete_firewall_policy_with_http_info(self, request):
        """删除网络ACL策略

        删除网络ACL策略。

        :param NeutronDeleteFirewallPolicyRequest request
        :return: None
        """

        all_params = ['firewall_policy_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'firewall_policy_id' in local_var_params:
            path_params['firewall_policy_id'] = local_var_params['firewall_policy_id']

        query_params = []

        header_params = {}

        form_params = []

        body_params = None


        auth_settings = []

        return self.call_api(
            '/v2.0/fwaas/firewall_policies/{firewall_policy_id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type=None,
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def neutron_delete_firewall_rule(self, request):
        """删除网络ACL规则

        删除网络ACL规则。

        :param NeutronDeleteFirewallRuleRequest request
        :return: None
        """
        return self.neutron_delete_firewall_rule_with_http_info(request)

    def neutron_delete_firewall_rule_with_http_info(self, request):
        """删除网络ACL规则

        删除网络ACL规则。

        :param NeutronDeleteFirewallRuleRequest request
        :return: None
        """

        all_params = ['firewall_rule_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'firewall_rule_id' in local_var_params:
            path_params['firewall_rule_id'] = local_var_params['firewall_rule_id']

        query_params = []

        header_params = {}

        form_params = []

        body_params = None


        auth_settings = []

        return self.call_api(
            '/v2.0/fwaas/firewall_rules/{firewall_rule_id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type=None,
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def neutron_list_firewall_groups(self, request):
        """查询所有网络ACL组

        查询提交请求的租户有权限操作的所有网络ACL组信息。单次查询最多返回2000条数据，超过2000后会返回分页标记。

        :param NeutronListFirewallGroupsRequest request
        :return: NeutronListFirewallGroupsResponse
        """
        return self.neutron_list_firewall_groups_with_http_info(request)

    def neutron_list_firewall_groups_with_http_info(self, request):
        """查询所有网络ACL组

        查询提交请求的租户有权限操作的所有网络ACL组信息。单次查询最多返回2000条数据，超过2000后会返回分页标记。

        :param NeutronListFirewallGroupsRequest request
        :return: tuple(NeutronListFirewallGroupsResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['marker', 'limit']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

        header_params = {}

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/v2.0/fwaas/firewall_groups', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='NeutronListFirewallGroupsResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def neutron_list_firewall_policies(self, request):
        """查询所有网络ACL策略

        查询提交请求的租户有权限操作的所有网络ACL策略信息。单次查询最多返回2000条数据，超过2000后会返回分页标记。

        :param NeutronListFirewallPoliciesRequest request
        :return: NeutronListFirewallPoliciesResponse
        """
        return self.neutron_list_firewall_policies_with_http_info(request)

    def neutron_list_firewall_policies_with_http_info(self, request):
        """查询所有网络ACL策略

        查询提交请求的租户有权限操作的所有网络ACL策略信息。单次查询最多返回2000条数据，超过2000后会返回分页标记。

        :param NeutronListFirewallPoliciesRequest request
        :return: tuple(NeutronListFirewallPoliciesResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['limit', 'marker']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))

        header_params = {}

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/v2.0/fwaas/firewall_policies', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='NeutronListFirewallPoliciesResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def neutron_list_firewall_rules(self, request):
        """查询所有网络ACL规则

        查询提交请求的租户有权限操作的所有网络ACL规则信息。单次查询最多返回2000条数据，超过2000后会返回分页标记。

        :param NeutronListFirewallRulesRequest request
        :return: NeutronListFirewallRulesResponse
        """
        return self.neutron_list_firewall_rules_with_http_info(request)

    def neutron_list_firewall_rules_with_http_info(self, request):
        """查询所有网络ACL规则

        查询提交请求的租户有权限操作的所有网络ACL规则信息。单次查询最多返回2000条数据，超过2000后会返回分页标记。

        :param NeutronListFirewallRulesRequest request
        :return: tuple(NeutronListFirewallRulesResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['marker', 'limit']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

        header_params = {}

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/v2.0/fwaas/firewall_rules', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='NeutronListFirewallRulesResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def neutron_remove_firewall_rule(self, request):
        """移除网络ACL规则

        从某一网络ACL策略中移除一条网络ACL规则。

        :param NeutronRemoveFirewallRuleRequest request
        :return: NeutronRemoveFirewallRuleResponse
        """
        return self.neutron_remove_firewall_rule_with_http_info(request)

    def neutron_remove_firewall_rule_with_http_info(self, request):
        """移除网络ACL规则

        从某一网络ACL策略中移除一条网络ACL规则。

        :param NeutronRemoveFirewallRuleRequest request
        :return: tuple(NeutronRemoveFirewallRuleResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['firewall_policy_id', 'remove_firewall_rule']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'firewall_policy_id' in local_var_params:
            path_params['firewall_policy_id'] = local_var_params['firewall_policy_id']

        query_params = []

        header_params = {}

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])
        auth_settings = []

        return self.call_api(
            '/v2.0/fwaas/firewall_policies/{firewall_policy_id}/remove_rule', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='NeutronRemoveFirewallRuleResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def neutron_show_firewall_group(self, request):
        """查询特定网络ACL组详情

        查询特定网络ACL组详情。

        :param NeutronShowFirewallGroupRequest request
        :return: NeutronShowFirewallGroupResponse
        """
        return self.neutron_show_firewall_group_with_http_info(request)

    def neutron_show_firewall_group_with_http_info(self, request):
        """查询特定网络ACL组详情

        查询特定网络ACL组详情。

        :param NeutronShowFirewallGroupRequest request
        :return: tuple(NeutronShowFirewallGroupResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['firewall_group_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'firewall_group_id' in local_var_params:
            path_params['firewall_group_id'] = local_var_params['firewall_group_id']

        query_params = []

        header_params = {}

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/v2.0/fwaas/firewall_groups/{firewall_group_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='NeutronShowFirewallGroupResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def neutron_show_firewall_policy(self, request):
        """查询特定网络ACL策略详情

        查询特定网络ACL策略详情。

        :param NeutronShowFirewallPolicyRequest request
        :return: NeutronShowFirewallPolicyResponse
        """
        return self.neutron_show_firewall_policy_with_http_info(request)

    def neutron_show_firewall_policy_with_http_info(self, request):
        """查询特定网络ACL策略详情

        查询特定网络ACL策略详情。

        :param NeutronShowFirewallPolicyRequest request
        :return: tuple(NeutronShowFirewallPolicyResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['firewall_policy_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'firewall_policy_id' in local_var_params:
            path_params['firewall_policy_id'] = local_var_params['firewall_policy_id']

        query_params = []

        header_params = {}

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/v2.0/fwaas/firewall_policies/{firewall_policy_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='NeutronShowFirewallPolicyResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def neutron_show_firewall_rule(self, request):
        """查询特定网络ACL规则

        查询特定网络ACL规则。

        :param NeutronShowFirewallRuleRequest request
        :return: NeutronShowFirewallRuleResponse
        """
        return self.neutron_show_firewall_rule_with_http_info(request)

    def neutron_show_firewall_rule_with_http_info(self, request):
        """查询特定网络ACL规则

        查询特定网络ACL规则。

        :param NeutronShowFirewallRuleRequest request
        :return: tuple(NeutronShowFirewallRuleResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['firewall_rule_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'firewall_rule_id' in local_var_params:
            path_params['firewall_rule_id'] = local_var_params['firewall_rule_id']

        query_params = []

        header_params = {}

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/v2.0/fwaas/firewall_rules/{firewall_rule_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='NeutronShowFirewallRuleResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def neutron_update_firewall_group(self, request):
        """更新网络ACL组

        更新网络ACL组。

        :param NeutronUpdateFirewallGroupRequest request
        :return: NeutronUpdateFirewallGroupResponse
        """
        return self.neutron_update_firewall_group_with_http_info(request)

    def neutron_update_firewall_group_with_http_info(self, request):
        """更新网络ACL组

        更新网络ACL组。

        :param NeutronUpdateFirewallGroupRequest request
        :return: tuple(NeutronUpdateFirewallGroupResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['firewall_group_id', 'firewall_group']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'firewall_group_id' in local_var_params:
            path_params['firewall_group_id'] = local_var_params['firewall_group_id']

        query_params = []

        header_params = {}

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])
        auth_settings = []

        return self.call_api(
            '/v2.0/fwaas/firewall_groups/{firewall_group_id}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='NeutronUpdateFirewallGroupResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def neutron_update_firewall_policy(self, request):
        """更新网络ACL策略

        更新网络ACL策略。

        :param NeutronUpdateFirewallPolicyRequest request
        :return: NeutronUpdateFirewallPolicyResponse
        """
        return self.neutron_update_firewall_policy_with_http_info(request)

    def neutron_update_firewall_policy_with_http_info(self, request):
        """更新网络ACL策略

        更新网络ACL策略。

        :param NeutronUpdateFirewallPolicyRequest request
        :return: tuple(NeutronUpdateFirewallPolicyResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['firewall_policy_id', 'firewall_policy']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'firewall_policy_id' in local_var_params:
            path_params['firewall_policy_id'] = local_var_params['firewall_policy_id']

        query_params = []

        header_params = {}

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])
        auth_settings = []

        return self.call_api(
            '/v2.0/fwaas/firewall_policies/{firewall_policy_id}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='NeutronUpdateFirewallPolicyResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def neutron_update_firewall_rule(self, request):
        """更新网络ACL规则

        更新网络ACL规则。

        :param NeutronUpdateFirewallRuleRequest request
        :return: NeutronUpdateFirewallRuleResponse
        """
        return self.neutron_update_firewall_rule_with_http_info(request)

    def neutron_update_firewall_rule_with_http_info(self, request):
        """更新网络ACL规则

        更新网络ACL规则。

        :param NeutronUpdateFirewallRuleRequest request
        :return: tuple(NeutronUpdateFirewallRuleResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['firewall_rule_id', 'firewall_rule']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'firewall_rule_id' in local_var_params:
            path_params['firewall_rule_id'] = local_var_params['firewall_rule_id']

        query_params = []

        header_params = {}

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])
        auth_settings = []

        return self.call_api(
            '/v2.0/fwaas/firewall_rules/{firewall_rule_id}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='NeutronUpdateFirewallRuleResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)


    def list_api_version(self, request):
        """查询API版本信息列表

        返回当前API所有可用的版本（仅针对OpenStack原生接口）。

        :param ListApiVersionRequest request
        :return: ListApiVersionResponse
        """
        return self.list_api_version_with_http_info(request)

    def list_api_version_with_http_info(self, request):
        """查询API版本信息列表

        返回当前API所有可用的版本（仅针对OpenStack原生接口）。

        :param ListApiVersionRequest request
        :return: tuple(ListApiVersionResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = []
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListApiVersionResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)


    def create_vpc(self, request):
        """创建VPC

        创建虚拟私有云。

        :param CreateVpcRequest request
        :return: CreateVpcResponse
        """
        return self.create_vpc_with_http_info(request)

    def create_vpc_with_http_info(self, request):
        """创建VPC

        创建虚拟私有云。

        :param CreateVpcRequest request
        :return: tuple(CreateVpcResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['vpc']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])
        auth_settings = []

        return self.call_api(
            '/v1/{project_id}/vpcs', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateVpcResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def create_vpc_route(self, request):
        """创建VPC路由

        创建路由

        :param CreateVpcRouteRequest request
        :return: CreateVpcRouteResponse
        """
        return self.create_vpc_route_with_http_info(request)

    def create_vpc_route_with_http_info(self, request):
        """创建VPC路由

        创建路由

        :param CreateVpcRouteRequest request
        :return: tuple(CreateVpcRouteResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['route']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])
        auth_settings = []

        return self.call_api(
            '/v2.0/vpc/routes', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateVpcRouteResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def delete_vpc(self, request):
        """删除VPC

        删除虚拟私有云。

        :param DeleteVpcRequest request
        :return: None
        """
        return self.delete_vpc_with_http_info(request)

    def delete_vpc_with_http_info(self, request):
        """删除VPC

        删除虚拟私有云。

        :param DeleteVpcRequest request
        :return: None
        """

        all_params = ['vpc_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'vpc_id' in local_var_params:
            path_params['vpc_id'] = local_var_params['vpc_id']

        query_params = []

        header_params = {}

        form_params = []

        body_params = None


        auth_settings = []

        return self.call_api(
            '/v1/{project_id}/vpcs/{vpc_id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type=None,
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def delete_vpc_route(self, request):
        """删除VPC路由

        删除路由

        :param DeleteVpcRouteRequest request
        :return: None
        """
        return self.delete_vpc_route_with_http_info(request)

    def delete_vpc_route_with_http_info(self, request):
        """删除VPC路由

        删除路由

        :param DeleteVpcRouteRequest request
        :return: None
        """

        all_params = ['route_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'route_id' in local_var_params:
            path_params['route_id'] = local_var_params['route_id']

        query_params = []

        header_params = {}

        form_params = []

        body_params = None


        auth_settings = []

        return self.call_api(
            '/v2.0/vpc/routes/{route_id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type=None,
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def list_vpc_routes(self, request):
        """查询VPC路由列表

        查询提交请求的租户的所有路由列表，并根据过滤条件进行过滤。

        :param ListVpcRoutesRequest request
        :return: ListVpcRoutesResponse
        """
        return self.list_vpc_routes_with_http_info(request)

    def list_vpc_routes_with_http_info(self, request):
        """查询VPC路由列表

        查询提交请求的租户的所有路由列表，并根据过滤条件进行过滤。

        :param ListVpcRoutesRequest request
        :return: tuple(ListVpcRoutesResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['limit', 'marker', 'id', 'type', 'vpc_id', 'destination', 'tenant_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'vpc_id' in local_var_params:
            query_params.append(('vpc_id', local_var_params['vpc_id']))
        if 'destination' in local_var_params:
            query_params.append(('destination', local_var_params['destination']))
        if 'tenant_id' in local_var_params:
            query_params.append(('tenant_id', local_var_params['tenant_id']))

        header_params = {}

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/v2.0/vpc/routes', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListVpcRoutesResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def list_vpcs(self, request):
        """查询VPC列表

        查询虚拟私有云列表。

        :param ListVpcsRequest request
        :return: ListVpcsResponse
        """
        return self.list_vpcs_with_http_info(request)

    def list_vpcs_with_http_info(self, request):
        """查询VPC列表

        查询虚拟私有云列表。

        :param ListVpcsRequest request
        :return: tuple(ListVpcsResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['limit', 'marker', 'id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))

        header_params = {}

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/v1/{project_id}/vpcs', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListVpcsResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def show_vpc(self, request):
        """查询VPC

        查询虚拟私有云。

        :param ShowVpcRequest request
        :return: ShowVpcResponse
        """
        return self.show_vpc_with_http_info(request)

    def show_vpc_with_http_info(self, request):
        """查询VPC

        查询虚拟私有云。

        :param ShowVpcRequest request
        :return: tuple(ShowVpcResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['vpc_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'vpc_id' in local_var_params:
            path_params['vpc_id'] = local_var_params['vpc_id']

        query_params = []

        header_params = {}

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/v1/{project_id}/vpcs/{vpc_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowVpcResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def show_vpc_route(self, request):
        """查询VPC路由

        查询路由详情

        :param ShowVpcRouteRequest request
        :return: ShowVpcRouteResponse
        """
        return self.show_vpc_route_with_http_info(request)

    def show_vpc_route_with_http_info(self, request):
        """查询VPC路由

        查询路由详情

        :param ShowVpcRouteRequest request
        :return: tuple(ShowVpcRouteResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['route_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'route_id' in local_var_params:
            path_params['route_id'] = local_var_params['route_id']

        query_params = []

        header_params = {}

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/v2.0/vpc/routes/{route_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowVpcRouteResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)

    def update_vpc(self, request):
        """更新VPC

        更新虚拟私有云。

        :param UpdateVpcRequest request
        :return: UpdateVpcResponse
        """
        return self.update_vpc_with_http_info(request)

    def update_vpc_with_http_info(self, request):
        """更新VPC

        更新虚拟私有云。

        :param UpdateVpcRequest request
        :return: tuple(UpdateVpcResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['vpc_id', 'vpc']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'vpc_id' in local_var_params:
            path_params['vpc_id'] = local_var_params['vpc_id']

        query_params = []

        header_params = {}

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])
        auth_settings = []

        return self.call_api(
            '/v1/{project_id}/vpcs/{vpc_id}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateVpcResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats)


    def call_api(self, resource_path, method,
                 path_params=None, query_params=None, header_params=None,
                 body=None, post_params=None,
                 response_type=None, auth_settings=None,  collection_formats=None):
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
        :param collection_formats: dict of collection formats for path, query,
            header, and post parameters.
        :return:
            Return the response directly.
        """
        return self.do_http_request(method, resource_path, path_params,
                                    query_params, header_params, body, post_params,
                                    response_type, collection_formats)

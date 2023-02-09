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


class VpcAsyncClient(Client):
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
        super(VpcAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkvpc.v2.model")
        self.preset_headers = {'User-Agent': 'HuaweiCloud-SDK-Python'}

    @classmethod
    def new_builder(cls, clazz=None):
        if clazz is None:
            return ClientBuilder(cls)

        if clazz.__name__ != "VpcClient":
            raise TypeError("client type error, support client type is VpcClient")

        return ClientBuilder(clazz)

    def accept_vpc_peering_async(self, request):
        """接受对等连接请求

        租户A名下的VPC申请和租户B的VPC建立对等连接，需要等待租户B接受该请求。此接口用于租户接受其他租户发起的对等连接请求。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AcceptVpcPeering
        :type request: :class:`huaweicloudsdkvpc.v2.AcceptVpcPeeringRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.AcceptVpcPeeringResponse`
        """
        return self.accept_vpc_peering_with_http_info(request)

    def accept_vpc_peering_with_http_info(self, request):
        all_params = ['peering_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'peering_id' in local_var_params:
            path_params['peering_id'] = local_var_params['peering_id']

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
            resource_path='/v2.0/vpc/peerings/{peering_id}/accept',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='AcceptVpcPeeringResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def associate_route_table_async(self, request):
        """子网关联路由表

        路由表关联子网。子网关联路由表A后，再关联B，不需要先跟路由表A解关联再关联路由表B
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AssociateRouteTable
        :type request: :class:`huaweicloudsdkvpc.v2.AssociateRouteTableRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.AssociateRouteTableResponse`
        """
        return self.associate_route_table_with_http_info(request)

    def associate_route_table_with_http_info(self, request):
        all_params = ['routetable_id', 'routetable_associate']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'routetable_id' in local_var_params:
            path_params['routetable_id'] = local_var_params['routetable_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/routetables/{routetable_id}/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='AssociateRouteTableResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_create_subnet_tags_async(self, request):
        """批量创建子网资源标签

        为指定的子网资源实例批量添加标签。
        此接口为幂等接口：创建时如果请求体中存在重复key则报错。创建时，不允许设置重复key数据，如果数据库已存在该key，就覆盖value的值。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchCreateSubnetTags
        :type request: :class:`huaweicloudsdkvpc.v2.BatchCreateSubnetTagsRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.BatchCreateSubnetTagsResponse`
        """
        return self.batch_create_subnet_tags_with_http_info(request)

    def batch_create_subnet_tags_with_http_info(self, request):
        all_params = ['subnet_id', 'batch_create_subnet_tags_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'subnet_id' in local_var_params:
            path_params['subnet_id'] = local_var_params['subnet_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2.0/{project_id}/subnets/{subnet_id}/tags/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchCreateSubnetTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_delete_subnet_tags_async(self, request):
        """批量删除子网资源标签

        为指定的子网资源实例批量删除标签
        此接口为幂等接口：删除时，如果删除的标签不存在，默认处理成功；删除时不对标签字符集范围做校验。删除时tags结构体不能缺失，key不能为空，或者空字符串。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchDeleteSubnetTags
        :type request: :class:`huaweicloudsdkvpc.v2.BatchDeleteSubnetTagsRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.BatchDeleteSubnetTagsResponse`
        """
        return self.batch_delete_subnet_tags_with_http_info(request)

    def batch_delete_subnet_tags_with_http_info(self, request):
        all_params = ['subnet_id', 'batch_delete_subnet_tags_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'subnet_id' in local_var_params:
            path_params['subnet_id'] = local_var_params['subnet_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2.0/{project_id}/subnets/{subnet_id}/tags/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchDeleteSubnetTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_flow_log_async(self, request):
        """创建流日志

        创建流日志。
        流日志功能可以记录虚拟私有云中的流量信息，帮助您检查和优化安全组和网络ACL防火墙控制规则、监控网络流量、进行网络攻击分析等。
        VPC流日志功能需要与云日志服务LTS结合使用，请先在云日志服务中创建日志组和日志主题，然后再创建VPC流日志。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateFlowLog
        :type request: :class:`huaweicloudsdkvpc.v2.CreateFlowLogRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.CreateFlowLogResponse`
        """
        return self.create_flow_log_with_http_info(request)

    def create_flow_log_with_http_info(self, request):
        all_params = ['flow_log']
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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/fl/flow_logs',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateFlowLogResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_port_async(self, request):
        """创建端口

        创建端口。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreatePort
        :type request: :class:`huaweicloudsdkvpc.v2.CreatePortRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.CreatePortResponse`
        """
        return self.create_port_with_http_info(request)

    def create_port_with_http_info(self, request):
        all_params = ['port']
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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/ports',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreatePortResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_route_table_async(self, request):
        """创建路由表

        创建路由表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateRouteTable
        :type request: :class:`huaweicloudsdkvpc.v2.CreateRouteTableRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.CreateRouteTableResponse`
        """
        return self.create_route_table_with_http_info(request)

    def create_route_table_with_http_info(self, request):
        all_params = ['routetable']
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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/routetables',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateRouteTableResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_security_group_async(self, request):
        """创建安全组

        创建安全组。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateSecurityGroup
        :type request: :class:`huaweicloudsdkvpc.v2.CreateSecurityGroupRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.CreateSecurityGroupResponse`
        """
        return self.create_security_group_with_http_info(request)

    def create_security_group_with_http_info(self, request):
        all_params = ['security_group']
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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/security-groups',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateSecurityGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_security_group_rule_async(self, request):
        """创建安全组规则

        创建安全组规则。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateSecurityGroupRule
        :type request: :class:`huaweicloudsdkvpc.v2.CreateSecurityGroupRuleRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.CreateSecurityGroupRuleResponse`
        """
        return self.create_security_group_rule_with_http_info(request)

    def create_security_group_rule_with_http_info(self, request):
        all_params = ['security_group_rule']
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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/security-group-rules',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateSecurityGroupRuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_subnet_async(self, request):
        """创建子网

        创建子网。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateSubnet
        :type request: :class:`huaweicloudsdkvpc.v2.CreateSubnetRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.CreateSubnetResponse`
        """
        return self.create_subnet_with_http_info(request)

    def create_subnet_with_http_info(self, request):
        all_params = ['subnet']
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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/subnets',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateSubnetResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_subnet_tag_async(self, request):
        """创建子网资源标签

        给指定子网资源实例增加标签信息。
        此接口为幂等接口：创建时，如果创建的标签已经存在（key相同），则覆盖。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateSubnetTag
        :type request: :class:`huaweicloudsdkvpc.v2.CreateSubnetTagRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.CreateSubnetTagResponse`
        """
        return self.create_subnet_tag_with_http_info(request)

    def create_subnet_tag_with_http_info(self, request):
        all_params = ['subnet_id', 'create_subnet_tag_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'subnet_id' in local_var_params:
            path_params['subnet_id'] = local_var_params['subnet_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2.0/{project_id}/subnets/{subnet_id}/tags',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateSubnetTagResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_vpc_peering_async(self, request):
        """创建对等连接

        创建对等连接。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateVpcPeering
        :type request: :class:`huaweicloudsdkvpc.v2.CreateVpcPeeringRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.CreateVpcPeeringResponse`
        """
        return self.create_vpc_peering_with_http_info(request)

    def create_vpc_peering_with_http_info(self, request):
        all_params = ['peering']
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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2.0/vpc/peerings',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateVpcPeeringResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_flow_log_async(self, request):
        """删除流日志

        删除流日志
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteFlowLog
        :type request: :class:`huaweicloudsdkvpc.v2.DeleteFlowLogRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.DeleteFlowLogResponse`
        """
        return self.delete_flow_log_with_http_info(request)

    def delete_flow_log_with_http_info(self, request):
        all_params = ['flowlog_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'flowlog_id' in local_var_params:
            path_params['flowlog_id'] = local_var_params['flowlog_id']

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
            resource_path='/v1/{project_id}/fl/flow_logs/{flowlog_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteFlowLogResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_port_async(self, request):
        """删除端口

        删除端口。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeletePort
        :type request: :class:`huaweicloudsdkvpc.v2.DeletePortRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.DeletePortResponse`
        """
        return self.delete_port_with_http_info(request)

    def delete_port_with_http_info(self, request):
        all_params = ['port_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'port_id' in local_var_params:
            path_params['port_id'] = local_var_params['port_id']

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
            resource_path='/v1/{project_id}/ports/{port_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeletePortResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_route_table_async(self, request):
        """删除路由表

        删除路由表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteRouteTable
        :type request: :class:`huaweicloudsdkvpc.v2.DeleteRouteTableRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.DeleteRouteTableResponse`
        """
        return self.delete_route_table_with_http_info(request)

    def delete_route_table_with_http_info(self, request):
        all_params = ['routetable_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'routetable_id' in local_var_params:
            path_params['routetable_id'] = local_var_params['routetable_id']

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
            resource_path='/v1/{project_id}/routetables/{routetable_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteRouteTableResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_security_group_async(self, request):
        """删除安全组

        删除安全组。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteSecurityGroup
        :type request: :class:`huaweicloudsdkvpc.v2.DeleteSecurityGroupRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.DeleteSecurityGroupResponse`
        """
        return self.delete_security_group_with_http_info(request)

    def delete_security_group_with_http_info(self, request):
        all_params = ['security_group_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'security_group_id' in local_var_params:
            path_params['security_group_id'] = local_var_params['security_group_id']

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
            resource_path='/v1/{project_id}/security-groups/{security_group_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteSecurityGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_security_group_rule_async(self, request):
        """删除安全组规则

        删除安全组规则。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteSecurityGroupRule
        :type request: :class:`huaweicloudsdkvpc.v2.DeleteSecurityGroupRuleRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.DeleteSecurityGroupRuleResponse`
        """
        return self.delete_security_group_rule_with_http_info(request)

    def delete_security_group_rule_with_http_info(self, request):
        all_params = ['security_group_rule_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'security_group_rule_id' in local_var_params:
            path_params['security_group_rule_id'] = local_var_params['security_group_rule_id']

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
            resource_path='/v1/{project_id}/security-group-rules/{security_group_rule_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteSecurityGroupRuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_subnet_async(self, request):
        """删除子网

        删除子网
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteSubnet
        :type request: :class:`huaweicloudsdkvpc.v2.DeleteSubnetRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.DeleteSubnetResponse`
        """
        return self.delete_subnet_with_http_info(request)

    def delete_subnet_with_http_info(self, request):
        all_params = ['vpc_id', 'subnet_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v1/{project_id}/vpcs/{vpc_id}/subnets/{subnet_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteSubnetResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_subnet_tag_async(self, request):
        """删除子网资源标签

        删除指定子网资源实例的标签信息。
        该接口为幂等接口：删除的key不存在报404，Key不能为空或者空字符串
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteSubnetTag
        :type request: :class:`huaweicloudsdkvpc.v2.DeleteSubnetTagRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.DeleteSubnetTagResponse`
        """
        return self.delete_subnet_tag_with_http_info(request)

    def delete_subnet_tag_with_http_info(self, request):
        all_params = ['subnet_id', 'key']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'subnet_id' in local_var_params:
            path_params['subnet_id'] = local_var_params['subnet_id']
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
            resource_path='/v2.0/{project_id}/subnets/{subnet_id}/tags/{key}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteSubnetTagResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_vpc_peering_async(self, request):
        """删除对等连接

        删除对等连接。
        可以在在本端或对端任何一端删除对等连接。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteVpcPeering
        :type request: :class:`huaweicloudsdkvpc.v2.DeleteVpcPeeringRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.DeleteVpcPeeringResponse`
        """
        return self.delete_vpc_peering_with_http_info(request)

    def delete_vpc_peering_with_http_info(self, request):
        all_params = ['peering_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'peering_id' in local_var_params:
            path_params['peering_id'] = local_var_params['peering_id']

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
            resource_path='/v2.0/vpc/peerings/{peering_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteVpcPeeringResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def disassociate_route_table_async(self, request):
        """子网解关联路由表

        子网解关联路由表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DisassociateRouteTable
        :type request: :class:`huaweicloudsdkvpc.v2.DisassociateRouteTableRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.DisassociateRouteTableResponse`
        """
        return self.disassociate_route_table_with_http_info(request)

    def disassociate_route_table_with_http_info(self, request):
        all_params = ['routetable_id', 'routetable_associate']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'routetable_id' in local_var_params:
            path_params['routetable_id'] = local_var_params['routetable_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/routetables/{routetable_id}/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DisassociateRouteTableResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_flow_logs_async(self, request):
        """查询流日志列表

        查询提交请求的租户的所有流日志列表，并根据过滤条件进行过滤
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListFlowLogs
        :type request: :class:`huaweicloudsdkvpc.v2.ListFlowLogsRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.ListFlowLogsResponse`
        """
        return self.list_flow_logs_with_http_info(request)

    def list_flow_logs_with_http_info(self, request):
        all_params = ['id', 'name', 'tenant_id', 'description', 'resource_type', 'resource_id', 'traffic_type', 'log_group_id', 'log_topic_id', 'log_store_type', 'status', 'limit', 'marker']
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
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'tenant_id' in local_var_params:
            query_params.append(('tenant_id', local_var_params['tenant_id']))
        if 'description' in local_var_params:
            query_params.append(('description', local_var_params['description']))
        if 'resource_type' in local_var_params:
            query_params.append(('resource_type', local_var_params['resource_type']))
        if 'resource_id' in local_var_params:
            query_params.append(('resource_id', local_var_params['resource_id']))
        if 'traffic_type' in local_var_params:
            query_params.append(('traffic_type', local_var_params['traffic_type']))
        if 'log_group_id' in local_var_params:
            query_params.append(('log_group_id', local_var_params['log_group_id']))
        if 'log_topic_id' in local_var_params:
            query_params.append(('log_topic_id', local_var_params['log_topic_id']))
        if 'log_store_type' in local_var_params:
            query_params.append(('log_store_type', local_var_params['log_store_type']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))

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
            resource_path='/v1/{project_id}/fl/flow_logs',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListFlowLogsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_ports_async(self, request):
        """查询端口列表

        查询提交请求的租户的所有端口，单次查询最多返回2000条数据。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListPorts
        :type request: :class:`huaweicloudsdkvpc.v2.ListPortsRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.ListPortsResponse`
        """
        return self.list_ports_with_http_info(request)

    def list_ports_with_http_info(self, request):
        all_params = ['name', 'id', 'limit', 'admin_state_up', 'network_id', 'mac_address', 'device_id', 'device_owner', 'status', 'security_groups', 'marker', 'fixed_ips', 'enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
        if 'security_groups' in local_var_params:
            query_params.append(('security_groups', local_var_params['security_groups']))
            collection_formats['security_groups'] = 'multi'
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'fixed_ips' in local_var_params:
            query_params.append(('fixed_ips', local_var_params['fixed_ips']))
            collection_formats['fixed_ips'] = 'multi'
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

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
            resource_path='/v1/{project_id}/ports',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListPortsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_route_tables_async(self, request):
        """查询路由表列表

        查询提交请求的帐户的所有路由表列表，并根据过滤条件进行过滤
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListRouteTables
        :type request: :class:`huaweicloudsdkvpc.v2.ListRouteTablesRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.ListRouteTablesResponse`
        """
        return self.list_route_tables_with_http_info(request)

    def list_route_tables_with_http_info(self, request):
        all_params = ['limit', 'marker', 'id', 'vpc_id', 'subnet_id']
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
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'vpc_id' in local_var_params:
            query_params.append(('vpc_id', local_var_params['vpc_id']))
        if 'subnet_id' in local_var_params:
            query_params.append(('subnet_id', local_var_params['subnet_id']))

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
            resource_path='/v1/{project_id}/routetables',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListRouteTablesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_security_group_rules_async(self, request):
        """查询安全组规则列表

        查询安全组规则列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListSecurityGroupRules
        :type request: :class:`huaweicloudsdkvpc.v2.ListSecurityGroupRulesRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.ListSecurityGroupRulesResponse`
        """
        return self.list_security_group_rules_with_http_info(request)

    def list_security_group_rules_with_http_info(self, request):
        all_params = ['marker', 'limit', 'security_group_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/security-group-rules',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListSecurityGroupRulesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_security_groups_async(self, request):
        """查询安全组列表

        查询安全组列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListSecurityGroups
        :type request: :class:`huaweicloudsdkvpc.v2.ListSecurityGroupsRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.ListSecurityGroupsResponse`
        """
        return self.list_security_groups_with_http_info(request)

    def list_security_groups_with_http_info(self, request):
        all_params = ['limit', 'marker', 'vpc_id', 'enterprise_project_id']
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
        if 'vpc_id' in local_var_params:
            query_params.append(('vpc_id', local_var_params['vpc_id']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

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
            resource_path='/v1/{project_id}/security-groups',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListSecurityGroupsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_subnet_tags_async(self, request):
        """查询子网项目标签

        查询租户在指定区域和实例类型的所有标签集合
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListSubnetTags
        :type request: :class:`huaweicloudsdkvpc.v2.ListSubnetTagsRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.ListSubnetTagsResponse`
        """
        return self.list_subnet_tags_with_http_info(request)

    def list_subnet_tags_with_http_info(self, request):
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
            resource_path='/v2.0/{project_id}/subnets/tags',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListSubnetTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_subnets_async(self, request):
        """查询子网列表

        查询子网列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListSubnets
        :type request: :class:`huaweicloudsdkvpc.v2.ListSubnetsRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.ListSubnetsResponse`
        """
        return self.list_subnets_with_http_info(request)

    def list_subnets_with_http_info(self, request):
        all_params = ['limit', 'marker', 'vpc_id']
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
        if 'vpc_id' in local_var_params:
            query_params.append(('vpc_id', local_var_params['vpc_id']))

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
            resource_path='/v1/{project_id}/subnets',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListSubnetsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_subnets_by_tags_async(self, request):
        """查询子网资源实例

        使用标签过滤实例
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListSubnetsByTags
        :type request: :class:`huaweicloudsdkvpc.v2.ListSubnetsByTagsRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.ListSubnetsByTagsResponse`
        """
        return self.list_subnets_by_tags_with_http_info(request)

    def list_subnets_by_tags_with_http_info(self, request):
        all_params = ['list_subnets_by_tags_request_body']
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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2.0/{project_id}/subnets/resource_instances/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListSubnetsByTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_vpc_peerings_async(self, request):
        """查询对等连接列表

        查询提交请求的租户的所有对等连接。根据过滤条件进行过滤。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListVpcPeerings
        :type request: :class:`huaweicloudsdkvpc.v2.ListVpcPeeringsRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.ListVpcPeeringsResponse`
        """
        return self.list_vpc_peerings_with_http_info(request)

    def list_vpc_peerings_with_http_info(self, request):
        all_params = ['limit', 'marker', 'id', 'name', 'status', 'tenant_id', 'vpc_id']
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

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2.0/vpc/peerings',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListVpcPeeringsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def reject_vpc_peering_async(self, request):
        """拒绝对等连接请求

        租户A名下的VPC申请和租户B的VPC建立对等连接，需要等待租户B接受该请求。此接口用于租户拒绝其他租户发起的对等连接请求。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RejectVpcPeering
        :type request: :class:`huaweicloudsdkvpc.v2.RejectVpcPeeringRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.RejectVpcPeeringResponse`
        """
        return self.reject_vpc_peering_with_http_info(request)

    def reject_vpc_peering_with_http_info(self, request):
        all_params = ['peering_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'peering_id' in local_var_params:
            path_params['peering_id'] = local_var_params['peering_id']

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
            resource_path='/v2.0/vpc/peerings/{peering_id}/reject',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RejectVpcPeeringResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_flow_log_async(self, request):
        """查询流日志

        查询流日志详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowFlowLog
        :type request: :class:`huaweicloudsdkvpc.v2.ShowFlowLogRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.ShowFlowLogResponse`
        """
        return self.show_flow_log_with_http_info(request)

    def show_flow_log_with_http_info(self, request):
        all_params = ['flowlog_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'flowlog_id' in local_var_params:
            path_params['flowlog_id'] = local_var_params['flowlog_id']

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
            resource_path='/v1/{project_id}/fl/flow_logs/{flowlog_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowFlowLogResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_port_async(self, request):
        """查询端口

        查询单个端口详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowPort
        :type request: :class:`huaweicloudsdkvpc.v2.ShowPortRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.ShowPortResponse`
        """
        return self.show_port_with_http_info(request)

    def show_port_with_http_info(self, request):
        all_params = ['port_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'port_id' in local_var_params:
            path_params['port_id'] = local_var_params['port_id']

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
            resource_path='/v1/{project_id}/ports/{port_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowPortResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_quota_async(self, request):
        """查询配额

        查询单租户在VPC服务下的网络资源配额，包括vpc配额、子网配额、安全组配额、安全组规则配额、弹性公网IP配额，vpn配额等。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowQuota
        :type request: :class:`huaweicloudsdkvpc.v2.ShowQuotaRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.ShowQuotaResponse`
        """
        return self.show_quota_with_http_info(request)

    def show_quota_with_http_info(self, request):
        all_params = ['type']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
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
            resource_path='/v1/{project_id}/quotas',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowQuotaResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_route_table_async(self, request):
        """查询路由表

        查询路由表详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowRouteTable
        :type request: :class:`huaweicloudsdkvpc.v2.ShowRouteTableRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.ShowRouteTableResponse`
        """
        return self.show_route_table_with_http_info(request)

    def show_route_table_with_http_info(self, request):
        all_params = ['routetable_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'routetable_id' in local_var_params:
            path_params['routetable_id'] = local_var_params['routetable_id']

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
            resource_path='/v1/{project_id}/routetables/{routetable_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowRouteTableResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_security_group_async(self, request):
        """查询安全组

        查询单个安全组详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowSecurityGroup
        :type request: :class:`huaweicloudsdkvpc.v2.ShowSecurityGroupRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.ShowSecurityGroupResponse`
        """
        return self.show_security_group_with_http_info(request)

    def show_security_group_with_http_info(self, request):
        all_params = ['security_group_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'security_group_id' in local_var_params:
            path_params['security_group_id'] = local_var_params['security_group_id']

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
            resource_path='/v1/{project_id}/security-groups/{security_group_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowSecurityGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_security_group_rule_async(self, request):
        """查询安全组规则

        查询单个安全组规则详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowSecurityGroupRule
        :type request: :class:`huaweicloudsdkvpc.v2.ShowSecurityGroupRuleRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.ShowSecurityGroupRuleResponse`
        """
        return self.show_security_group_rule_with_http_info(request)

    def show_security_group_rule_with_http_info(self, request):
        all_params = ['security_group_rule_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'security_group_rule_id' in local_var_params:
            path_params['security_group_rule_id'] = local_var_params['security_group_rule_id']

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
            resource_path='/v1/{project_id}/security-group-rules/{security_group_rule_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowSecurityGroupRuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_subnet_async(self, request):
        """查询子网

        查询子网详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowSubnet
        :type request: :class:`huaweicloudsdkvpc.v2.ShowSubnetRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.ShowSubnetResponse`
        """
        return self.show_subnet_with_http_info(request)

    def show_subnet_with_http_info(self, request):
        all_params = ['subnet_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
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
            resource_path='/v1/{project_id}/subnets/{subnet_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowSubnetResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_subnet_tags_async(self, request):
        """查询子网资源标签

        查询指定子网实例的标签信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowSubnetTags
        :type request: :class:`huaweicloudsdkvpc.v2.ShowSubnetTagsRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.ShowSubnetTagsResponse`
        """
        return self.show_subnet_tags_with_http_info(request)

    def show_subnet_tags_with_http_info(self, request):
        all_params = ['subnet_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
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
            resource_path='/v2.0/{project_id}/subnets/{subnet_id}/tags',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowSubnetTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_vpc_peering_async(self, request):
        """查询对等连接

        查询对等连接详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowVpcPeering
        :type request: :class:`huaweicloudsdkvpc.v2.ShowVpcPeeringRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.ShowVpcPeeringResponse`
        """
        return self.show_vpc_peering_with_http_info(request)

    def show_vpc_peering_with_http_info(self, request):
        all_params = ['peering_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'peering_id' in local_var_params:
            path_params['peering_id'] = local_var_params['peering_id']

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
            resource_path='/v2.0/vpc/peerings/{peering_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowVpcPeeringResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_flow_log_async(self, request):
        """更新流日志

        更新流日志
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateFlowLog
        :type request: :class:`huaweicloudsdkvpc.v2.UpdateFlowLogRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.UpdateFlowLogResponse`
        """
        return self.update_flow_log_with_http_info(request)

    def update_flow_log_with_http_info(self, request):
        all_params = ['flowlog_id', 'flow_log']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'flowlog_id' in local_var_params:
            path_params['flowlog_id'] = local_var_params['flowlog_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/fl/flow_logs/{flowlog_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateFlowLogResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_port_async(self, request):
        """更新端口

        更新端口。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdatePort
        :type request: :class:`huaweicloudsdkvpc.v2.UpdatePortRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.UpdatePortResponse`
        """
        return self.update_port_with_http_info(request)

    def update_port_with_http_info(self, request):
        all_params = ['port_id', 'port']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'port_id' in local_var_params:
            path_params['port_id'] = local_var_params['port_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/ports/{port_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdatePortResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_route_table_async(self, request):
        """更新路由表

        更新路由表，包括可以更新路由表的名称，描述，以及新增、更新、删除路由条目
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateRouteTable
        :type request: :class:`huaweicloudsdkvpc.v2.UpdateRouteTableRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.UpdateRouteTableResponse`
        """
        return self.update_route_table_with_http_info(request)

    def update_route_table_with_http_info(self, request):
        all_params = ['routetable_id', 'routetable']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'routetable_id' in local_var_params:
            path_params['routetable_id'] = local_var_params['routetable_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/routetables/{routetable_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateRouteTableResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_subnet_async(self, request):
        """更新子网

        更新子网。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateSubnet
        :type request: :class:`huaweicloudsdkvpc.v2.UpdateSubnetRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.UpdateSubnetResponse`
        """
        return self.update_subnet_with_http_info(request)

    def update_subnet_with_http_info(self, request):
        all_params = ['vpc_id', 'subnet_id', 'subnet']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/vpcs/{vpc_id}/subnets/{subnet_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateSubnetResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_vpc_peering_async(self, request):
        """更新对等连接

        更新对等连接。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateVpcPeering
        :type request: :class:`huaweicloudsdkvpc.v2.UpdateVpcPeeringRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.UpdateVpcPeeringResponse`
        """
        return self.update_vpc_peering_with_http_info(request)

    def update_vpc_peering_with_http_info(self, request):
        all_params = ['peering_id', 'peering']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'peering_id' in local_var_params:
            path_params['peering_id'] = local_var_params['peering_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2.0/vpc/peerings/{peering_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateVpcPeeringResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_privateip_async(self, request):
        """申请私有IP

        申请私有IP。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreatePrivateip
        :type request: :class:`huaweicloudsdkvpc.v2.CreatePrivateipRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.CreatePrivateipResponse`
        """
        return self.create_privateip_with_http_info(request)

    def create_privateip_with_http_info(self, request):
        all_params = ['privateips']
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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/privateips',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreatePrivateipResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_privateip_async(self, request):
        """删除私有IP

        删除私有IP。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeletePrivateip
        :type request: :class:`huaweicloudsdkvpc.v2.DeletePrivateipRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.DeletePrivateipResponse`
        """
        return self.delete_privateip_with_http_info(request)

    def delete_privateip_with_http_info(self, request):
        all_params = ['privateip_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'privateip_id' in local_var_params:
            path_params['privateip_id'] = local_var_params['privateip_id']

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
            resource_path='/v1/{project_id}/privateips/{privateip_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeletePrivateipResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_privateips_async(self, request):
        """查询私有IP列表

        查询指定子网下的私有IP列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListPrivateips
        :type request: :class:`huaweicloudsdkvpc.v2.ListPrivateipsRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.ListPrivateipsResponse`
        """
        return self.list_privateips_with_http_info(request)

    def list_privateips_with_http_info(self, request):
        all_params = ['subnet_id', 'limit', 'marker']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/subnets/{subnet_id}/privateips',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListPrivateipsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_network_ip_availabilities_async(self, request):
        """查询网络IP使用情况

        显示一个指定网络中的IPv4地址使用情况。
        包括此网络中的IP总数以及已用IP总数，以及网络下每一个子网的IP地址总数和可用IP地址总数。
        
        &gt; 须知
        
        - 系统预留地址指的是子网的第1个以及最后4个地址，一般用于网关、DHCP等服务。
        - 这里以及下文描述的IP地址总数、已用IP地址总数不包含系统预留地址。
        - 在分配IP时，用户可以指定系统预留的IP地址。但是不论IP是如何分配的，只要是处于系统预留IP地址段的IP均不会被统计到已用IP地址数目和IP地址总数中。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowNetworkIpAvailabilities
        :type request: :class:`huaweicloudsdkvpc.v2.ShowNetworkIpAvailabilitiesRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.ShowNetworkIpAvailabilitiesResponse`
        """
        return self.show_network_ip_availabilities_with_http_info(request)

    def show_network_ip_availabilities_with_http_info(self, request):
        all_params = ['network_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'network_id' in local_var_params:
            path_params['network_id'] = local_var_params['network_id']

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
            resource_path='/v2.0/network-ip-availabilities/{network_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowNetworkIpAvailabilitiesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_privateip_async(self, request):
        """查询私有IP

        指定ID查询私有IP。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowPrivateip
        :type request: :class:`huaweicloudsdkvpc.v2.ShowPrivateipRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.ShowPrivateipResponse`
        """
        return self.show_privateip_with_http_info(request)

    def show_privateip_with_http_info(self, request):
        all_params = ['privateip_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'privateip_id' in local_var_params:
            path_params['privateip_id'] = local_var_params['privateip_id']

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
            resource_path='/v1/{project_id}/privateips/{privateip_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowPrivateipResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def neutron_create_security_group_async(self, request):
        """创建安全组

        创建安全组
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for NeutronCreateSecurityGroup
        :type request: :class:`huaweicloudsdkvpc.v2.NeutronCreateSecurityGroupRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.NeutronCreateSecurityGroupResponse`
        """
        return self.neutron_create_security_group_with_http_info(request)

    def neutron_create_security_group_with_http_info(self, request):
        all_params = ['security_group']
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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2.0/security-groups',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='NeutronCreateSecurityGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def neutron_create_security_group_rule_async(self, request):
        """创建安全组规则

        创建安全组规则
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for NeutronCreateSecurityGroupRule
        :type request: :class:`huaweicloudsdkvpc.v2.NeutronCreateSecurityGroupRuleRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.NeutronCreateSecurityGroupRuleResponse`
        """
        return self.neutron_create_security_group_rule_with_http_info(request)

    def neutron_create_security_group_rule_with_http_info(self, request):
        all_params = ['security_group_rule']
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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2.0/security-group-rules',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='NeutronCreateSecurityGroupRuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def neutron_delete_security_group_async(self, request):
        """删除安全组

        删除安全组
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for NeutronDeleteSecurityGroup
        :type request: :class:`huaweicloudsdkvpc.v2.NeutronDeleteSecurityGroupRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.NeutronDeleteSecurityGroupResponse`
        """
        return self.neutron_delete_security_group_with_http_info(request)

    def neutron_delete_security_group_with_http_info(self, request):
        all_params = ['security_group_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'security_group_id' in local_var_params:
            path_params['security_group_id'] = local_var_params['security_group_id']

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
            resource_path='/v2.0/security-groups/{security_group_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='NeutronDeleteSecurityGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def neutron_delete_security_group_rule_async(self, request):
        """删除安全组规则

        删除安全组规则
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for NeutronDeleteSecurityGroupRule
        :type request: :class:`huaweicloudsdkvpc.v2.NeutronDeleteSecurityGroupRuleRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.NeutronDeleteSecurityGroupRuleResponse`
        """
        return self.neutron_delete_security_group_rule_with_http_info(request)

    def neutron_delete_security_group_rule_with_http_info(self, request):
        all_params = ['security_group_rule_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'security_group_rule_id' in local_var_params:
            path_params['security_group_rule_id'] = local_var_params['security_group_rule_id']

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
            resource_path='/v2.0/security-group-rules/{security_group_rule_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='NeutronDeleteSecurityGroupRuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def neutron_list_security_group_rules_async(self, request):
        """查询安全组规则列表

        查询提交请求的租户有权限查看的所有安全组规则。单次查询最多返回2000条数据，超过2000后会返回分页标记。分页查询请参考分页查询
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for NeutronListSecurityGroupRules
        :type request: :class:`huaweicloudsdkvpc.v2.NeutronListSecurityGroupRulesRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.NeutronListSecurityGroupRulesResponse`
        """
        return self.neutron_list_security_group_rules_with_http_info(request)

    def neutron_list_security_group_rules_with_http_info(self, request):
        all_params = ['limit', 'marker', 'id', 'direction', 'protocol', 'ethertype', 'description', 'remote_ip_prefix', 'remote_group_id', 'security_group_id', 'port_range_max', 'port_range_min', 'tenant_id']
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

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2.0/security-group-rules',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='NeutronListSecurityGroupRulesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def neutron_list_security_groups_async(self, request):
        """查询安全组列表

        查询提交请求租户的所有安全组，单次查询最多返回2000条数据，超过2000后会返回分页标记。分页查询请参考分页查询 。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for NeutronListSecurityGroups
        :type request: :class:`huaweicloudsdkvpc.v2.NeutronListSecurityGroupsRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.NeutronListSecurityGroupsResponse`
        """
        return self.neutron_list_security_groups_with_http_info(request)

    def neutron_list_security_groups_with_http_info(self, request):
        all_params = ['limit', 'marker', 'id', 'name', 'description', 'tenant_id']
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
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'description' in local_var_params:
            query_params.append(('description', local_var_params['description']))
        if 'tenant_id' in local_var_params:
            query_params.append(('tenant_id', local_var_params['tenant_id']))

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
            resource_path='/v2.0/security-groups',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='NeutronListSecurityGroupsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def neutron_show_security_group_async(self, request):
        """查询安全组

        查询安全组详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for NeutronShowSecurityGroup
        :type request: :class:`huaweicloudsdkvpc.v2.NeutronShowSecurityGroupRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.NeutronShowSecurityGroupResponse`
        """
        return self.neutron_show_security_group_with_http_info(request)

    def neutron_show_security_group_with_http_info(self, request):
        all_params = ['security_group_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'security_group_id' in local_var_params:
            path_params['security_group_id'] = local_var_params['security_group_id']

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
            resource_path='/v2.0/security-groups/{security_group_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='NeutronShowSecurityGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def neutron_show_security_group_rule_async(self, request):
        """查询安全组规则

        查询安全组规则详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for NeutronShowSecurityGroupRule
        :type request: :class:`huaweicloudsdkvpc.v2.NeutronShowSecurityGroupRuleRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.NeutronShowSecurityGroupRuleResponse`
        """
        return self.neutron_show_security_group_rule_with_http_info(request)

    def neutron_show_security_group_rule_with_http_info(self, request):
        all_params = ['security_group_rule_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'security_group_rule_id' in local_var_params:
            path_params['security_group_rule_id'] = local_var_params['security_group_rule_id']

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
            resource_path='/v2.0/security-group-rules/{security_group_rule_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='NeutronShowSecurityGroupRuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def neutron_update_security_group_async(self, request):
        """更新安全组

        更新安全组
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for NeutronUpdateSecurityGroup
        :type request: :class:`huaweicloudsdkvpc.v2.NeutronUpdateSecurityGroupRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.NeutronUpdateSecurityGroupResponse`
        """
        return self.neutron_update_security_group_with_http_info(request)

    def neutron_update_security_group_with_http_info(self, request):
        all_params = ['security_group_id', 'security_group']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'security_group_id' in local_var_params:
            path_params['security_group_id'] = local_var_params['security_group_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2.0/security-groups/{security_group_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='NeutronUpdateSecurityGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def neutron_add_firewall_rule_async(self, request):
        """插入网络ACL规则

        插入一条网络ACL规则到某一网络ACL策略中。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for NeutronAddFirewallRule
        :type request: :class:`huaweicloudsdkvpc.v2.NeutronAddFirewallRuleRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.NeutronAddFirewallRuleResponse`
        """
        return self.neutron_add_firewall_rule_with_http_info(request)

    def neutron_add_firewall_rule_with_http_info(self, request):
        all_params = ['firewall_policy_id', 'insert_firewall_rule']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'firewall_policy_id' in local_var_params:
            path_params['firewall_policy_id'] = local_var_params['firewall_policy_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2.0/fwaas/firewall_policies/{firewall_policy_id}/insert_rule',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='NeutronAddFirewallRuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def neutron_create_firewall_group_async(self, request):
        """创建网络ACL组

        创建网络ACL组
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for NeutronCreateFirewallGroup
        :type request: :class:`huaweicloudsdkvpc.v2.NeutronCreateFirewallGroupRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.NeutronCreateFirewallGroupResponse`
        """
        return self.neutron_create_firewall_group_with_http_info(request)

    def neutron_create_firewall_group_with_http_info(self, request):
        all_params = ['firewall_group']
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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2.0/fwaas/firewall_groups',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='NeutronCreateFirewallGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def neutron_create_firewall_policy_async(self, request):
        """创建网络ACL策略

        创建网络ACL策略。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for NeutronCreateFirewallPolicy
        :type request: :class:`huaweicloudsdkvpc.v2.NeutronCreateFirewallPolicyRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.NeutronCreateFirewallPolicyResponse`
        """
        return self.neutron_create_firewall_policy_with_http_info(request)

    def neutron_create_firewall_policy_with_http_info(self, request):
        all_params = ['firewall_policy']
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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2.0/fwaas/firewall_policies',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='NeutronCreateFirewallPolicyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def neutron_create_firewall_rule_async(self, request):
        """创建网络ACL规则

        创建网络ACL规则。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for NeutronCreateFirewallRule
        :type request: :class:`huaweicloudsdkvpc.v2.NeutronCreateFirewallRuleRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.NeutronCreateFirewallRuleResponse`
        """
        return self.neutron_create_firewall_rule_with_http_info(request)

    def neutron_create_firewall_rule_with_http_info(self, request):
        all_params = ['firewall_rule']
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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2.0/fwaas/firewall_rules',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='NeutronCreateFirewallRuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def neutron_delete_firewall_group_async(self, request):
        """删除网络ACL组

        删除网络ACL组
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for NeutronDeleteFirewallGroup
        :type request: :class:`huaweicloudsdkvpc.v2.NeutronDeleteFirewallGroupRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.NeutronDeleteFirewallGroupResponse`
        """
        return self.neutron_delete_firewall_group_with_http_info(request)

    def neutron_delete_firewall_group_with_http_info(self, request):
        all_params = ['firewall_group_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'firewall_group_id' in local_var_params:
            path_params['firewall_group_id'] = local_var_params['firewall_group_id']

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
            resource_path='/v2.0/fwaas/firewall_groups/{firewall_group_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='NeutronDeleteFirewallGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def neutron_delete_firewall_policy_async(self, request):
        """删除网络ACL策略

        删除网络ACL策略。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for NeutronDeleteFirewallPolicy
        :type request: :class:`huaweicloudsdkvpc.v2.NeutronDeleteFirewallPolicyRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.NeutronDeleteFirewallPolicyResponse`
        """
        return self.neutron_delete_firewall_policy_with_http_info(request)

    def neutron_delete_firewall_policy_with_http_info(self, request):
        all_params = ['firewall_policy_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'firewall_policy_id' in local_var_params:
            path_params['firewall_policy_id'] = local_var_params['firewall_policy_id']

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
            resource_path='/v2.0/fwaas/firewall_policies/{firewall_policy_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='NeutronDeleteFirewallPolicyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def neutron_delete_firewall_rule_async(self, request):
        """删除网络ACL规则

        删除网络ACL规则。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for NeutronDeleteFirewallRule
        :type request: :class:`huaweicloudsdkvpc.v2.NeutronDeleteFirewallRuleRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.NeutronDeleteFirewallRuleResponse`
        """
        return self.neutron_delete_firewall_rule_with_http_info(request)

    def neutron_delete_firewall_rule_with_http_info(self, request):
        all_params = ['firewall_rule_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'firewall_rule_id' in local_var_params:
            path_params['firewall_rule_id'] = local_var_params['firewall_rule_id']

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
            resource_path='/v2.0/fwaas/firewall_rules/{firewall_rule_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='NeutronDeleteFirewallRuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def neutron_list_firewall_groups_async(self, request):
        """查询所有网络ACL组

        查询提交请求的租户有权限操作的所有网络ACL组信息。单次查询最多返回2000条数据，超过2000后会返回分页标记。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for NeutronListFirewallGroups
        :type request: :class:`huaweicloudsdkvpc.v2.NeutronListFirewallGroupsRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.NeutronListFirewallGroupsResponse`
        """
        return self.neutron_list_firewall_groups_with_http_info(request)

    def neutron_list_firewall_groups_with_http_info(self, request):
        all_params = ['marker', 'limit', 'id', 'name', 'description', 'ingress_firewall_policy_id', 'egress_firewall_policy_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
            collection_formats['id'] = 'multi'
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
            collection_formats['name'] = 'multi'
        if 'description' in local_var_params:
            query_params.append(('description', local_var_params['description']))
            collection_formats['description'] = 'multi'
        if 'ingress_firewall_policy_id' in local_var_params:
            query_params.append(('ingress_firewall_policy_id', local_var_params['ingress_firewall_policy_id']))
        if 'egress_firewall_policy_id' in local_var_params:
            query_params.append(('egress_firewall_policy_id', local_var_params['egress_firewall_policy_id']))

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
            resource_path='/v2.0/fwaas/firewall_groups',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='NeutronListFirewallGroupsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def neutron_list_firewall_policies_async(self, request):
        """查询所有网络ACL策略

        查询提交请求的租户有权限操作的所有网络ACL策略信息。单次查询最多返回2000条数据，超过2000后会返回分页标记。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for NeutronListFirewallPolicies
        :type request: :class:`huaweicloudsdkvpc.v2.NeutronListFirewallPoliciesRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.NeutronListFirewallPoliciesResponse`
        """
        return self.neutron_list_firewall_policies_with_http_info(request)

    def neutron_list_firewall_policies_with_http_info(self, request):
        all_params = ['limit', 'marker', 'id', 'name', 'description', 'tenant_id']
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
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
            collection_formats['id'] = 'multi'
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
            collection_formats['name'] = 'multi'
        if 'description' in local_var_params:
            query_params.append(('description', local_var_params['description']))
            collection_formats['description'] = 'multi'
        if 'tenant_id' in local_var_params:
            query_params.append(('tenant_id', local_var_params['tenant_id']))

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
            resource_path='/v2.0/fwaas/firewall_policies',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='NeutronListFirewallPoliciesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def neutron_list_firewall_rules_async(self, request):
        """查询所有网络ACL规则

        查询提交请求的租户有权限操作的所有网络ACL规则信息。单次查询最多返回2000条数据，超过2000后会返回分页标记。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for NeutronListFirewallRules
        :type request: :class:`huaweicloudsdkvpc.v2.NeutronListFirewallRulesRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.NeutronListFirewallRulesResponse`
        """
        return self.neutron_list_firewall_rules_with_http_info(request)

    def neutron_list_firewall_rules_with_http_info(self, request):
        all_params = ['marker', 'limit', 'id', 'name', 'description', 'action', 'tenant_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
            collection_formats['id'] = 'multi'
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
            collection_formats['name'] = 'multi'
        if 'description' in local_var_params:
            query_params.append(('description', local_var_params['description']))
            collection_formats['description'] = 'multi'
        if 'action' in local_var_params:
            query_params.append(('action', local_var_params['action']))
        if 'tenant_id' in local_var_params:
            query_params.append(('tenant_id', local_var_params['tenant_id']))

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
            resource_path='/v2.0/fwaas/firewall_rules',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='NeutronListFirewallRulesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def neutron_remove_firewall_rule_async(self, request):
        """移除网络ACL规则

        从某一网络ACL策略中移除一条网络ACL规则。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for NeutronRemoveFirewallRule
        :type request: :class:`huaweicloudsdkvpc.v2.NeutronRemoveFirewallRuleRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.NeutronRemoveFirewallRuleResponse`
        """
        return self.neutron_remove_firewall_rule_with_http_info(request)

    def neutron_remove_firewall_rule_with_http_info(self, request):
        all_params = ['firewall_policy_id', 'remove_firewall_rule']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'firewall_policy_id' in local_var_params:
            path_params['firewall_policy_id'] = local_var_params['firewall_policy_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2.0/fwaas/firewall_policies/{firewall_policy_id}/remove_rule',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='NeutronRemoveFirewallRuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def neutron_show_firewall_group_async(self, request):
        """查询特定网络ACL组详情

        查询特定网络ACL组详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for NeutronShowFirewallGroup
        :type request: :class:`huaweicloudsdkvpc.v2.NeutronShowFirewallGroupRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.NeutronShowFirewallGroupResponse`
        """
        return self.neutron_show_firewall_group_with_http_info(request)

    def neutron_show_firewall_group_with_http_info(self, request):
        all_params = ['firewall_group_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'firewall_group_id' in local_var_params:
            path_params['firewall_group_id'] = local_var_params['firewall_group_id']

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
            resource_path='/v2.0/fwaas/firewall_groups/{firewall_group_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='NeutronShowFirewallGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def neutron_show_firewall_policy_async(self, request):
        """查询特定网络ACL策略详情

        查询特定网络ACL策略详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for NeutronShowFirewallPolicy
        :type request: :class:`huaweicloudsdkvpc.v2.NeutronShowFirewallPolicyRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.NeutronShowFirewallPolicyResponse`
        """
        return self.neutron_show_firewall_policy_with_http_info(request)

    def neutron_show_firewall_policy_with_http_info(self, request):
        all_params = ['firewall_policy_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'firewall_policy_id' in local_var_params:
            path_params['firewall_policy_id'] = local_var_params['firewall_policy_id']

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
            resource_path='/v2.0/fwaas/firewall_policies/{firewall_policy_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='NeutronShowFirewallPolicyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def neutron_show_firewall_rule_async(self, request):
        """查询特定网络ACL规则

        查询特定网络ACL规则。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for NeutronShowFirewallRule
        :type request: :class:`huaweicloudsdkvpc.v2.NeutronShowFirewallRuleRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.NeutronShowFirewallRuleResponse`
        """
        return self.neutron_show_firewall_rule_with_http_info(request)

    def neutron_show_firewall_rule_with_http_info(self, request):
        all_params = ['firewall_rule_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'firewall_rule_id' in local_var_params:
            path_params['firewall_rule_id'] = local_var_params['firewall_rule_id']

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
            resource_path='/v2.0/fwaas/firewall_rules/{firewall_rule_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='NeutronShowFirewallRuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def neutron_update_firewall_group_async(self, request):
        """更新网络ACL组

        更新网络ACL组。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for NeutronUpdateFirewallGroup
        :type request: :class:`huaweicloudsdkvpc.v2.NeutronUpdateFirewallGroupRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.NeutronUpdateFirewallGroupResponse`
        """
        return self.neutron_update_firewall_group_with_http_info(request)

    def neutron_update_firewall_group_with_http_info(self, request):
        all_params = ['firewall_group_id', 'firewall_group']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'firewall_group_id' in local_var_params:
            path_params['firewall_group_id'] = local_var_params['firewall_group_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2.0/fwaas/firewall_groups/{firewall_group_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='NeutronUpdateFirewallGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def neutron_update_firewall_policy_async(self, request):
        """更新网络ACL策略

        更新网络ACL策略。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for NeutronUpdateFirewallPolicy
        :type request: :class:`huaweicloudsdkvpc.v2.NeutronUpdateFirewallPolicyRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.NeutronUpdateFirewallPolicyResponse`
        """
        return self.neutron_update_firewall_policy_with_http_info(request)

    def neutron_update_firewall_policy_with_http_info(self, request):
        all_params = ['firewall_policy_id', 'firewall_policy']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'firewall_policy_id' in local_var_params:
            path_params['firewall_policy_id'] = local_var_params['firewall_policy_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2.0/fwaas/firewall_policies/{firewall_policy_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='NeutronUpdateFirewallPolicyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def neutron_update_firewall_rule_async(self, request):
        """更新网络ACL规则

        更新网络ACL规则。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for NeutronUpdateFirewallRule
        :type request: :class:`huaweicloudsdkvpc.v2.NeutronUpdateFirewallRuleRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.NeutronUpdateFirewallRuleResponse`
        """
        return self.neutron_update_firewall_rule_with_http_info(request)

    def neutron_update_firewall_rule_with_http_info(self, request):
        all_params = ['firewall_rule_id', 'firewall_rule']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'firewall_rule_id' in local_var_params:
            path_params['firewall_rule_id'] = local_var_params['firewall_rule_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2.0/fwaas/firewall_rules/{firewall_rule_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='NeutronUpdateFirewallRuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_create_vpc_tags_async(self, request):
        """批量创建VPC资源标签

        为指定的VPC资源实例批量添加标签。
        此接口为幂等接口：创建时如果请求体中存在重复key则报错。创建时，不允许设置重复key数据，如果数据库已存在该key，就覆盖value的值。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchCreateVpcTags
        :type request: :class:`huaweicloudsdkvpc.v2.BatchCreateVpcTagsRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.BatchCreateVpcTagsResponse`
        """
        return self.batch_create_vpc_tags_with_http_info(request)

    def batch_create_vpc_tags_with_http_info(self, request):
        all_params = ['vpc_id', 'batch_create_vpc_tags_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'vpc_id' in local_var_params:
            path_params['vpc_id'] = local_var_params['vpc_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2.0/{project_id}/vpcs/{vpc_id}/tags/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchCreateVpcTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_delete_vpc_tags_async(self, request):
        """批量删除VPC资源标签

        为指定的VPC资源实例批量删除标签。
        此接口为幂等接口：删除时，如果删除的标签不存在，默认处理成功；删除时不对标签字符集范围做校验。删除时tags结构体不能缺失，key不能为空，或者空字符串。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchDeleteVpcTags
        :type request: :class:`huaweicloudsdkvpc.v2.BatchDeleteVpcTagsRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.BatchDeleteVpcTagsResponse`
        """
        return self.batch_delete_vpc_tags_with_http_info(request)

    def batch_delete_vpc_tags_with_http_info(self, request):
        all_params = ['vpc_id', 'batch_delete_vpc_tags_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'vpc_id' in local_var_params:
            path_params['vpc_id'] = local_var_params['vpc_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2.0/{project_id}/vpcs/{vpc_id}/tags/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchDeleteVpcTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_vpc_async(self, request):
        """创建VPC

        创建虚拟私有云。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateVpc
        :type request: :class:`huaweicloudsdkvpc.v2.CreateVpcRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.CreateVpcResponse`
        """
        return self.create_vpc_with_http_info(request)

    def create_vpc_with_http_info(self, request):
        all_params = ['vpc']
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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/vpcs',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateVpcResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_vpc_resource_tag_async(self, request):
        """创建VPC资源标签

        给指定VPC资源实例增加标签信息
        此接口为幂等接口：创建时，如果创建的标签已经存在（key相同），则覆盖。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateVpcResourceTag
        :type request: :class:`huaweicloudsdkvpc.v2.CreateVpcResourceTagRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.CreateVpcResourceTagResponse`
        """
        return self.create_vpc_resource_tag_with_http_info(request)

    def create_vpc_resource_tag_with_http_info(self, request):
        all_params = ['vpc_id', 'create_vpc_resource_tag_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'vpc_id' in local_var_params:
            path_params['vpc_id'] = local_var_params['vpc_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2.0/{project_id}/vpcs/{vpc_id}/tags',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateVpcResourceTagResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_vpc_route_async(self, request):
        """创建VPC路由

        创建路由
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateVpcRoute
        :type request: :class:`huaweicloudsdkvpc.v2.CreateVpcRouteRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.CreateVpcRouteResponse`
        """
        return self.create_vpc_route_with_http_info(request)

    def create_vpc_route_with_http_info(self, request):
        all_params = ['route']
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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2.0/vpc/routes',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateVpcRouteResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_vpc_async(self, request):
        """删除VPC

        删除虚拟私有云。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteVpc
        :type request: :class:`huaweicloudsdkvpc.v2.DeleteVpcRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.DeleteVpcResponse`
        """
        return self.delete_vpc_with_http_info(request)

    def delete_vpc_with_http_info(self, request):
        all_params = ['vpc_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'vpc_id' in local_var_params:
            path_params['vpc_id'] = local_var_params['vpc_id']

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
            resource_path='/v1/{project_id}/vpcs/{vpc_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteVpcResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_vpc_route_async(self, request):
        """删除VPC路由

        删除路由
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteVpcRoute
        :type request: :class:`huaweicloudsdkvpc.v2.DeleteVpcRouteRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.DeleteVpcRouteResponse`
        """
        return self.delete_vpc_route_with_http_info(request)

    def delete_vpc_route_with_http_info(self, request):
        all_params = ['route_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'route_id' in local_var_params:
            path_params['route_id'] = local_var_params['route_id']

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
            resource_path='/v2.0/vpc/routes/{route_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteVpcRouteResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_vpc_tag_async(self, request):
        """删除VPC资源标签

        删除指定VPC资源实例的标签信息
        该接口为幂等接口：删除的key不存在报404，Key不能为空或者空字符串
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteVpcTag
        :type request: :class:`huaweicloudsdkvpc.v2.DeleteVpcTagRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.DeleteVpcTagResponse`
        """
        return self.delete_vpc_tag_with_http_info(request)

    def delete_vpc_tag_with_http_info(self, request):
        all_params = ['vpc_id', 'key']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'vpc_id' in local_var_params:
            path_params['vpc_id'] = local_var_params['vpc_id']
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
            resource_path='/v2.0/{project_id}/vpcs/{vpc_id}/tags/{key}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteVpcTagResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_vpc_routes_async(self, request):
        """查询VPC路由列表

        查询提交请求的租户的所有路由列表，并根据过滤条件进行过滤。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListVpcRoutes
        :type request: :class:`huaweicloudsdkvpc.v2.ListVpcRoutesRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.ListVpcRoutesResponse`
        """
        return self.list_vpc_routes_with_http_info(request)

    def list_vpc_routes_with_http_info(self, request):
        all_params = ['limit', 'marker', 'id', 'type', 'vpc_id', 'destination', 'tenant_id']
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

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2.0/vpc/routes',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListVpcRoutesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_vpc_tags_async(self, request):
        """查询VPC项目标签

        查询租户在指定区域和实例类型的所有标签集合
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListVpcTags
        :type request: :class:`huaweicloudsdkvpc.v2.ListVpcTagsRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.ListVpcTagsResponse`
        """
        return self.list_vpc_tags_with_http_info(request)

    def list_vpc_tags_with_http_info(self, request):
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
            resource_path='/v2.0/{project_id}/vpcs/tags',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListVpcTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_vpcs_async(self, request):
        """查询VPC列表

        查询虚拟私有云列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListVpcs
        :type request: :class:`huaweicloudsdkvpc.v2.ListVpcsRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.ListVpcsResponse`
        """
        return self.list_vpcs_with_http_info(request)

    def list_vpcs_with_http_info(self, request):
        all_params = ['limit', 'marker', 'id', 'enterprise_project_id']
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
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

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
            resource_path='/v1/{project_id}/vpcs',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListVpcsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_vpcs_by_tags_async(self, request):
        """查询VPC资源实例

        使用标签过滤实例。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListVpcsByTags
        :type request: :class:`huaweicloudsdkvpc.v2.ListVpcsByTagsRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.ListVpcsByTagsResponse`
        """
        return self.list_vpcs_by_tags_with_http_info(request)

    def list_vpcs_by_tags_with_http_info(self, request):
        all_params = ['list_vpcs_by_tags_request_body']
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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2.0/{project_id}/vpcs/resource_instances/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListVpcsByTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_vpc_async(self, request):
        """查询VPC

        查询虚拟私有云。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowVpc
        :type request: :class:`huaweicloudsdkvpc.v2.ShowVpcRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.ShowVpcResponse`
        """
        return self.show_vpc_with_http_info(request)

    def show_vpc_with_http_info(self, request):
        all_params = ['vpc_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'vpc_id' in local_var_params:
            path_params['vpc_id'] = local_var_params['vpc_id']

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
            resource_path='/v1/{project_id}/vpcs/{vpc_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowVpcResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_vpc_route_async(self, request):
        """查询VPC路由

        查询路由详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowVpcRoute
        :type request: :class:`huaweicloudsdkvpc.v2.ShowVpcRouteRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.ShowVpcRouteResponse`
        """
        return self.show_vpc_route_with_http_info(request)

    def show_vpc_route_with_http_info(self, request):
        all_params = ['route_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'route_id' in local_var_params:
            path_params['route_id'] = local_var_params['route_id']

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
            resource_path='/v2.0/vpc/routes/{route_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowVpcRouteResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_vpc_tags_async(self, request):
        """查询VPC资源标签

        查询指定VPC实例的标签信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowVpcTags
        :type request: :class:`huaweicloudsdkvpc.v2.ShowVpcTagsRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.ShowVpcTagsResponse`
        """
        return self.show_vpc_tags_with_http_info(request)

    def show_vpc_tags_with_http_info(self, request):
        all_params = ['vpc_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'vpc_id' in local_var_params:
            path_params['vpc_id'] = local_var_params['vpc_id']

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
            resource_path='/v2.0/{project_id}/vpcs/{vpc_id}/tags',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowVpcTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_vpc_async(self, request):
        """更新VPC

        更新虚拟私有云。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateVpc
        :type request: :class:`huaweicloudsdkvpc.v2.UpdateVpcRequest`
        :rtype: :class:`huaweicloudsdkvpc.v2.UpdateVpcResponse`
        """
        return self.update_vpc_with_http_info(request)

    def update_vpc_with_http_info(self, request):
        all_params = ['vpc_id', 'vpc']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'vpc_id' in local_var_params:
            path_params['vpc_id'] = local_var_params['vpc_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/vpcs/{vpc_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateVpcResponse',
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

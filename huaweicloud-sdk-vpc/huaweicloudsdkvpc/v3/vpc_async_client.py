# coding: utf-8

from __future__ import absolute_import

import importlib

from huaweicloudsdkcore.client import Client, ClientBuilder
from huaweicloudsdkcore.utils import http_utils
from huaweicloudsdkcore.sdk_stream_request import SdkStreamRequest


class VpcAsyncClient(Client):
    def __init__(self):
        super(VpcAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkvpc.v3.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if clazz is None:
            return ClientBuilder(cls)

        if clazz.__name__ != "VpcClient":
            raise TypeError("client type error, support client type is VpcClient")

        return ClientBuilder(clazz)

    def batch_create_sub_network_interface_async(self, request):
        """批量创建辅助弹性网卡

        批量创建辅助弹性网卡
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchCreateSubNetworkInterface
        :type request: :class:`huaweicloudsdkvpc.v3.BatchCreateSubNetworkInterfaceRequest`
        :rtype: :class:`huaweicloudsdkvpc.v3.BatchCreateSubNetworkInterfaceResponse`
        """
        return self._batch_create_sub_network_interface_with_http_info(request)

    def _batch_create_sub_network_interface_with_http_info(self, request):
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
            resource_path='/v3/{project_id}/vpc/sub-network-interfaces/batch-create',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchCreateSubNetworkInterfaceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_security_group_async(self, request):
        """创建安全组

        创建安全组
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateSecurityGroup
        :type request: :class:`huaweicloudsdkvpc.v3.CreateSecurityGroupRequest`
        :rtype: :class:`huaweicloudsdkvpc.v3.CreateSecurityGroupResponse`
        """
        return self._create_security_group_with_http_info(request)

    def _create_security_group_with_http_info(self, request):
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
            resource_path='/v3/{project_id}/vpc/security-groups',
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

        创建安全组规则
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateSecurityGroupRule
        :type request: :class:`huaweicloudsdkvpc.v3.CreateSecurityGroupRuleRequest`
        :rtype: :class:`huaweicloudsdkvpc.v3.CreateSecurityGroupRuleResponse`
        """
        return self._create_security_group_rule_with_http_info(request)

    def _create_security_group_rule_with_http_info(self, request):
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
            resource_path='/v3/{project_id}/vpc/security-group-rules',
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

    def create_sub_network_interface_async(self, request):
        """创建辅助弹性网卡

        创建辅助弹性网卡
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateSubNetworkInterface
        :type request: :class:`huaweicloudsdkvpc.v3.CreateSubNetworkInterfaceRequest`
        :rtype: :class:`huaweicloudsdkvpc.v3.CreateSubNetworkInterfaceResponse`
        """
        return self._create_sub_network_interface_with_http_info(request)

    def _create_sub_network_interface_with_http_info(self, request):
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
            resource_path='/v3/{project_id}/vpc/sub-network-interfaces',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateSubNetworkInterfaceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_security_group_async(self, request):
        """删除安全组

        删除安全组
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteSecurityGroup
        :type request: :class:`huaweicloudsdkvpc.v3.DeleteSecurityGroupRequest`
        :rtype: :class:`huaweicloudsdkvpc.v3.DeleteSecurityGroupResponse`
        """
        return self._delete_security_group_with_http_info(request)

    def _delete_security_group_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
            resource_path='/v3/{project_id}/vpc/security-groups/{security_group_id}',
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

        删除安全组规则
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteSecurityGroupRule
        :type request: :class:`huaweicloudsdkvpc.v3.DeleteSecurityGroupRuleRequest`
        :rtype: :class:`huaweicloudsdkvpc.v3.DeleteSecurityGroupRuleResponse`
        """
        return self._delete_security_group_rule_with_http_info(request)

    def _delete_security_group_rule_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
            resource_path='/v3/{project_id}/vpc/security-group-rules/{security_group_rule_id}',
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

    def delete_sub_network_interface_async(self, request):
        """删除辅助弹性网卡

        删除辅助弹性网卡
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteSubNetworkInterface
        :type request: :class:`huaweicloudsdkvpc.v3.DeleteSubNetworkInterfaceRequest`
        :rtype: :class:`huaweicloudsdkvpc.v3.DeleteSubNetworkInterfaceResponse`
        """
        return self._delete_sub_network_interface_with_http_info(request)

    def _delete_sub_network_interface_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'sub_network_interface_id' in local_var_params:
            path_params['sub_network_interface_id'] = local_var_params['sub_network_interface_id']

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
            resource_path='/v3/{project_id}/vpc/sub-network-interfaces/{sub_network_interface_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteSubNetworkInterfaceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_security_group_rules_async(self, request):
        """查询安全组规则列表

        查询安全组规则列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListSecurityGroupRules
        :type request: :class:`huaweicloudsdkvpc.v3.ListSecurityGroupRulesRequest`
        :rtype: :class:`huaweicloudsdkvpc.v3.ListSecurityGroupRulesResponse`
        """
        return self._list_security_group_rules_with_http_info(request)

    def _list_security_group_rules_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
        if 'security_group_id' in local_var_params:
            query_params.append(('security_group_id', local_var_params['security_group_id']))
            collection_formats['security_group_id'] = 'multi'
        if 'protocol' in local_var_params:
            query_params.append(('protocol', local_var_params['protocol']))
            collection_formats['protocol'] = 'multi'
        if 'description' in local_var_params:
            query_params.append(('description', local_var_params['description']))
            collection_formats['description'] = 'multi'
        if 'remote_group_id' in local_var_params:
            query_params.append(('remote_group_id', local_var_params['remote_group_id']))
            collection_formats['remote_group_id'] = 'multi'
        if 'direction' in local_var_params:
            query_params.append(('direction', local_var_params['direction']))
        if 'action' in local_var_params:
            query_params.append(('action', local_var_params['action']))
        if 'remote_ip_prefix' in local_var_params:
            query_params.append(('remote_ip_prefix', local_var_params['remote_ip_prefix']))

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
            resource_path='/v3/{project_id}/vpc/security-group-rules',
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

        查询某租户下的安全组列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListSecurityGroups
        :type request: :class:`huaweicloudsdkvpc.v3.ListSecurityGroupsRequest`
        :rtype: :class:`huaweicloudsdkvpc.v3.ListSecurityGroupsResponse`
        """
        return self._list_security_groups_with_http_info(request)

    def _list_security_groups_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
            resource_path='/v3/{project_id}/vpc/security-groups',
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

    def list_sub_network_interfaces_async(self, request):
        """查询租户下辅助弹性网卡列表

        查询辅助弹性网卡列表，单次查询最多返回2000条数据
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListSubNetworkInterfaces
        :type request: :class:`huaweicloudsdkvpc.v3.ListSubNetworkInterfacesRequest`
        :rtype: :class:`huaweicloudsdkvpc.v3.ListSubNetworkInterfacesResponse`
        """
        return self._list_sub_network_interfaces_with_http_info(request)

    def _list_sub_network_interfaces_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
        if 'virsubnet_id' in local_var_params:
            query_params.append(('virsubnet_id', local_var_params['virsubnet_id']))
            collection_formats['virsubnet_id'] = 'multi'
        if 'private_ip_address' in local_var_params:
            query_params.append(('private_ip_address', local_var_params['private_ip_address']))
            collection_formats['private_ip_address'] = 'multi'
        if 'mac_address' in local_var_params:
            query_params.append(('mac_address', local_var_params['mac_address']))
            collection_formats['mac_address'] = 'multi'
        if 'vpc_id' in local_var_params:
            query_params.append(('vpc_id', local_var_params['vpc_id']))
            collection_formats['vpc_id'] = 'multi'
        if 'description' in local_var_params:
            query_params.append(('description', local_var_params['description']))
            collection_formats['description'] = 'multi'
        if 'parent_id' in local_var_params:
            query_params.append(('parent_id', local_var_params['parent_id']))
            collection_formats['parent_id'] = 'multi'

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
            resource_path='/v3/{project_id}/vpc/sub-network-interfaces',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListSubNetworkInterfacesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def migrate_sub_network_interface_async(self, request):
        """迁移辅助弹性网卡

        批量迁移辅助弹性网卡
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for MigrateSubNetworkInterface
        :type request: :class:`huaweicloudsdkvpc.v3.MigrateSubNetworkInterfaceRequest`
        :rtype: :class:`huaweicloudsdkvpc.v3.MigrateSubNetworkInterfaceResponse`
        """
        return self._migrate_sub_network_interface_with_http_info(request)

    def _migrate_sub_network_interface_with_http_info(self, request):
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
            resource_path='/v3/{project_id}/vpc/sub-network-interfaces/migrate',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='MigrateSubNetworkInterfaceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_security_group_async(self, request):
        """查询安全组

        查询单个安全组详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowSecurityGroup
        :type request: :class:`huaweicloudsdkvpc.v3.ShowSecurityGroupRequest`
        :rtype: :class:`huaweicloudsdkvpc.v3.ShowSecurityGroupResponse`
        """
        return self._show_security_group_with_http_info(request)

    def _show_security_group_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
            resource_path='/v3/{project_id}/vpc/security-groups/{security_group_id}',
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

        查询单个安全组规则
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowSecurityGroupRule
        :type request: :class:`huaweicloudsdkvpc.v3.ShowSecurityGroupRuleRequest`
        :rtype: :class:`huaweicloudsdkvpc.v3.ShowSecurityGroupRuleResponse`
        """
        return self._show_security_group_rule_with_http_info(request)

    def _show_security_group_rule_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
            resource_path='/v3/{project_id}/vpc/security-group-rules/{security_group_rule_id}',
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

    def show_sub_network_interface_async(self, request):
        """查询租户下辅助弹性网卡

        查询辅助弹性网卡详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowSubNetworkInterface
        :type request: :class:`huaweicloudsdkvpc.v3.ShowSubNetworkInterfaceRequest`
        :rtype: :class:`huaweicloudsdkvpc.v3.ShowSubNetworkInterfaceResponse`
        """
        return self._show_sub_network_interface_with_http_info(request)

    def _show_sub_network_interface_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'sub_network_interface_id' in local_var_params:
            path_params['sub_network_interface_id'] = local_var_params['sub_network_interface_id']

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
            resource_path='/v3/{project_id}/vpc/sub-network-interfaces/{sub_network_interface_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowSubNetworkInterfaceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_sub_network_interfaces_quantity_async(self, request):
        """查询租户下辅助弹性网卡数目

        查询辅助弹性网卡数目
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowSubNetworkInterfacesQuantity
        :type request: :class:`huaweicloudsdkvpc.v3.ShowSubNetworkInterfacesQuantityRequest`
        :rtype: :class:`huaweicloudsdkvpc.v3.ShowSubNetworkInterfacesQuantityResponse`
        """
        return self._show_sub_network_interfaces_quantity_with_http_info(request)

    def _show_sub_network_interfaces_quantity_with_http_info(self, request):
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
            resource_path='/v3/{project_id}/vpc/sub-network-interfaces/count',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowSubNetworkInterfacesQuantityResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_security_group_async(self, request):
        """更新安全组

        更新安全组
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateSecurityGroup
        :type request: :class:`huaweicloudsdkvpc.v3.UpdateSecurityGroupRequest`
        :rtype: :class:`huaweicloudsdkvpc.v3.UpdateSecurityGroupResponse`
        """
        return self._update_security_group_with_http_info(request)

    def _update_security_group_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/vpc/security-groups/{security_group_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateSecurityGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_sub_network_interface_async(self, request):
        """更新辅助弹性网卡

        更新辅助弹性网卡
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateSubNetworkInterface
        :type request: :class:`huaweicloudsdkvpc.v3.UpdateSubNetworkInterfaceRequest`
        :rtype: :class:`huaweicloudsdkvpc.v3.UpdateSubNetworkInterfaceResponse`
        """
        return self._update_sub_network_interface_with_http_info(request)

    def _update_sub_network_interface_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'sub_network_interface_id' in local_var_params:
            path_params['sub_network_interface_id'] = local_var_params['sub_network_interface_id']

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
            resource_path='/v3/{project_id}/vpc/sub-network-interfaces/{sub_network_interface_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateSubNetworkInterfaceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_address_group_async(self, request):
        """创建地址组

        创建地址组
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateAddressGroup
        :type request: :class:`huaweicloudsdkvpc.v3.CreateAddressGroupRequest`
        :rtype: :class:`huaweicloudsdkvpc.v3.CreateAddressGroupResponse`
        """
        return self._create_address_group_with_http_info(request)

    def _create_address_group_with_http_info(self, request):
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
            resource_path='/v3/{project_id}/vpc/address-groups',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateAddressGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_address_group_async(self, request):
        """删除地址组

        删除地址组，非强制删除，删除前请确保未被其他资源引用
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteAddressGroup
        :type request: :class:`huaweicloudsdkvpc.v3.DeleteAddressGroupRequest`
        :rtype: :class:`huaweicloudsdkvpc.v3.DeleteAddressGroupResponse`
        """
        return self._delete_address_group_with_http_info(request)

    def _delete_address_group_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'address_group_id' in local_var_params:
            path_params['address_group_id'] = local_var_params['address_group_id']

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
            resource_path='/v3/{project_id}/vpc/address-groups/{address_group_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteAddressGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_ip_address_group_force_async(self, request):
        """强制删除地址组

        强制删除地址组，删除的地址组与安全组规则关联时，会删除地址组与关联的安全组规则。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteIpAddressGroupForce
        :type request: :class:`huaweicloudsdkvpc.v3.DeleteIpAddressGroupForceRequest`
        :rtype: :class:`huaweicloudsdkvpc.v3.DeleteIpAddressGroupForceResponse`
        """
        return self._delete_ip_address_group_force_with_http_info(request)

    def _delete_ip_address_group_force_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'address_group_id' in local_var_params:
            path_params['address_group_id'] = local_var_params['address_group_id']

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
            resource_path='/v3/{project_id}/vpc/address-groups/{address_group_id}/force',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteIpAddressGroupForceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_address_group_async(self, request):
        """查询地址组列表

        查询地址组列表，根据过滤条件进行过滤。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAddressGroup
        :type request: :class:`huaweicloudsdkvpc.v3.ListAddressGroupRequest`
        :rtype: :class:`huaweicloudsdkvpc.v3.ListAddressGroupResponse`
        """
        return self._list_address_group_with_http_info(request)

    def _list_address_group_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
        if 'ip_version' in local_var_params:
            query_params.append(('ip_version', local_var_params['ip_version']))
        if 'description' in local_var_params:
            query_params.append(('description', local_var_params['description']))
            collection_formats['description'] = 'multi'
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
            resource_path='/v3/{project_id}/vpc/address-groups',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListAddressGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_address_group_async(self, request):
        """查询地址组

        查询地址组详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowAddressGroup
        :type request: :class:`huaweicloudsdkvpc.v3.ShowAddressGroupRequest`
        :rtype: :class:`huaweicloudsdkvpc.v3.ShowAddressGroupResponse`
        """
        return self._show_address_group_with_http_info(request)

    def _show_address_group_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'address_group_id' in local_var_params:
            path_params['address_group_id'] = local_var_params['address_group_id']

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
            resource_path='/v3/{project_id}/vpc/address-groups/{address_group_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowAddressGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_address_group_async(self, request):
        """更新地址组

        更新地址组。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateAddressGroup
        :type request: :class:`huaweicloudsdkvpc.v3.UpdateAddressGroupRequest`
        :rtype: :class:`huaweicloudsdkvpc.v3.UpdateAddressGroupResponse`
        """
        return self._update_address_group_with_http_info(request)

    def _update_address_group_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'address_group_id' in local_var_params:
            path_params['address_group_id'] = local_var_params['address_group_id']

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
            resource_path='/v3/{project_id}/vpc/address-groups/{address_group_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateAddressGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def add_vpc_extend_cidr_async(self, request):
        """添加VPC扩展网段

        添加VPC的扩展网段
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AddVpcExtendCidr
        :type request: :class:`huaweicloudsdkvpc.v3.AddVpcExtendCidrRequest`
        :rtype: :class:`huaweicloudsdkvpc.v3.AddVpcExtendCidrResponse`
        """
        return self._add_vpc_extend_cidr_with_http_info(request)

    def _add_vpc_extend_cidr_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/vpc/vpcs/{vpc_id}/add-extend-cidr',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='AddVpcExtendCidrResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_vpc_async(self, request):
        """创建VPC

        创建虚拟私有云
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateVpc
        :type request: :class:`huaweicloudsdkvpc.v3.CreateVpcRequest`
        :rtype: :class:`huaweicloudsdkvpc.v3.CreateVpcResponse`
        """
        return self._create_vpc_with_http_info(request)

    def _create_vpc_with_http_info(self, request):
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
            resource_path='/v3/{project_id}/vpc/vpcs',
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

    def delete_vpc_async(self, request):
        """删除VPC

        删除VPC
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteVpc
        :type request: :class:`huaweicloudsdkvpc.v3.DeleteVpcRequest`
        :rtype: :class:`huaweicloudsdkvpc.v3.DeleteVpcResponse`
        """
        return self._delete_vpc_with_http_info(request)

    def _delete_vpc_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
            resource_path='/v3/{project_id}/vpc/vpcs/{vpc_id}',
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

    def list_vpcs_async(self, request):
        """查询VPC列表

        查询vpc列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListVpcs
        :type request: :class:`huaweicloudsdkvpc.v3.ListVpcsRequest`
        :rtype: :class:`huaweicloudsdkvpc.v3.ListVpcsResponse`
        """
        return self._list_vpcs_with_http_info(request)

    def _list_vpcs_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
        if 'cidr' in local_var_params:
            query_params.append(('cidr', local_var_params['cidr']))
            collection_formats['cidr'] = 'multi'

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
            resource_path='/v3/{project_id}/vpc/vpcs',
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

    def remove_vpc_extend_cidr_async(self, request):
        """移除VPC扩展网段

        移除VPC扩展网段
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RemoveVpcExtendCidr
        :type request: :class:`huaweicloudsdkvpc.v3.RemoveVpcExtendCidrRequest`
        :rtype: :class:`huaweicloudsdkvpc.v3.RemoveVpcExtendCidrResponse`
        """
        return self._remove_vpc_extend_cidr_with_http_info(request)

    def _remove_vpc_extend_cidr_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/vpc/vpcs/{vpc_id}/remove-extend-cidr',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RemoveVpcExtendCidrResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_vpc_async(self, request):
        """查询VPC详情

        查询vpc详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowVpc
        :type request: :class:`huaweicloudsdkvpc.v3.ShowVpcRequest`
        :rtype: :class:`huaweicloudsdkvpc.v3.ShowVpcResponse`
        """
        return self._show_vpc_with_http_info(request)

    def _show_vpc_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
            resource_path='/v3/{project_id}/vpc/vpcs/{vpc_id}',
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

    def update_vpc_async(self, request):
        """更新VPC

        更新vpc
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateVpc
        :type request: :class:`huaweicloudsdkvpc.v3.UpdateVpcRequest`
        :rtype: :class:`huaweicloudsdkvpc.v3.UpdateVpcResponse`
        """
        return self._update_vpc_with_http_info(request)

    def _update_vpc_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/vpc/vpcs/{vpc_id}',
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

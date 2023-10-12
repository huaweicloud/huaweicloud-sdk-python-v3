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

    def add_sources_to_traffic_mirror_session_async(self, request):
        """流量镜像会话添加镜像源

        流量镜像会话添加镜像源
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AddSourcesToTrafficMirrorSession
        :type request: :class:`huaweicloudsdkvpc.v3.AddSourcesToTrafficMirrorSessionRequest`
        :rtype: :class:`huaweicloudsdkvpc.v3.AddSourcesToTrafficMirrorSessionResponse`
        """
        return self._add_sources_to_traffic_mirror_session_with_http_info(request)

    def _add_sources_to_traffic_mirror_session_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'traffic_mirror_session_id' in local_var_params:
            path_params['traffic_mirror_session_id'] = local_var_params['traffic_mirror_session_id']

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
            resource_path='/v3/{project_id}/vpc/traffic-mirror-sessions/{traffic_mirror_session_id}/add-sources',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='AddSourcesToTrafficMirrorSessionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

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

    def create_traffic_mirror_filter_async(self, request):
        """创建流量镜像筛选条件

        创建流量镜像筛选条件
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateTrafficMirrorFilter
        :type request: :class:`huaweicloudsdkvpc.v3.CreateTrafficMirrorFilterRequest`
        :rtype: :class:`huaweicloudsdkvpc.v3.CreateTrafficMirrorFilterResponse`
        """
        return self._create_traffic_mirror_filter_with_http_info(request)

    def _create_traffic_mirror_filter_with_http_info(self, request):
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
            resource_path='/v3/{project_id}/vpc/traffic-mirror-filters',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateTrafficMirrorFilterResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_traffic_mirror_filter_rule_async(self, request):
        """创建流量镜像筛选规则

        创建流量镜像筛选规则
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateTrafficMirrorFilterRule
        :type request: :class:`huaweicloudsdkvpc.v3.CreateTrafficMirrorFilterRuleRequest`
        :rtype: :class:`huaweicloudsdkvpc.v3.CreateTrafficMirrorFilterRuleResponse`
        """
        return self._create_traffic_mirror_filter_rule_with_http_info(request)

    def _create_traffic_mirror_filter_rule_with_http_info(self, request):
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
            resource_path='/v3/{project_id}/vpc/traffic-mirror-filter-rules',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateTrafficMirrorFilterRuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_traffic_mirror_session_async(self, request):
        """创建流量镜像会话

        创建流量镜像会话
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateTrafficMirrorSession
        :type request: :class:`huaweicloudsdkvpc.v3.CreateTrafficMirrorSessionRequest`
        :rtype: :class:`huaweicloudsdkvpc.v3.CreateTrafficMirrorSessionResponse`
        """
        return self._create_traffic_mirror_session_with_http_info(request)

    def _create_traffic_mirror_session_with_http_info(self, request):
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
            resource_path='/v3/{project_id}/vpc/traffic-mirror-sessions',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateTrafficMirrorSessionResponse',
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

    def delete_traffic_mirror_filter_async(self, request):
        """删除流量镜像筛选条件

        删除流量镜像筛选条件
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteTrafficMirrorFilter
        :type request: :class:`huaweicloudsdkvpc.v3.DeleteTrafficMirrorFilterRequest`
        :rtype: :class:`huaweicloudsdkvpc.v3.DeleteTrafficMirrorFilterResponse`
        """
        return self._delete_traffic_mirror_filter_with_http_info(request)

    def _delete_traffic_mirror_filter_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'traffic_mirror_filter_id' in local_var_params:
            path_params['traffic_mirror_filter_id'] = local_var_params['traffic_mirror_filter_id']

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
            resource_path='/v3/{project_id}/vpc/traffic-mirror-filters/{traffic_mirror_filter_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteTrafficMirrorFilterResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_traffic_mirror_filter_rule_async(self, request):
        """删除流量镜像筛选规则

        删除流量镜像筛选规则
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteTrafficMirrorFilterRule
        :type request: :class:`huaweicloudsdkvpc.v3.DeleteTrafficMirrorFilterRuleRequest`
        :rtype: :class:`huaweicloudsdkvpc.v3.DeleteTrafficMirrorFilterRuleResponse`
        """
        return self._delete_traffic_mirror_filter_rule_with_http_info(request)

    def _delete_traffic_mirror_filter_rule_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'traffic_mirror_filter_rule_id' in local_var_params:
            path_params['traffic_mirror_filter_rule_id'] = local_var_params['traffic_mirror_filter_rule_id']

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
            resource_path='/v3/{project_id}/vpc/traffic-mirror-filter-rules/{traffic_mirror_filter_rule_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteTrafficMirrorFilterRuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_traffic_mirror_session_async(self, request):
        """删除流量镜像会话

        删除流量镜像会话
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteTrafficMirrorSession
        :type request: :class:`huaweicloudsdkvpc.v3.DeleteTrafficMirrorSessionRequest`
        :rtype: :class:`huaweicloudsdkvpc.v3.DeleteTrafficMirrorSessionResponse`
        """
        return self._delete_traffic_mirror_session_with_http_info(request)

    def _delete_traffic_mirror_session_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'traffic_mirror_session_id' in local_var_params:
            path_params['traffic_mirror_session_id'] = local_var_params['traffic_mirror_session_id']

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
            resource_path='/v3/{project_id}/vpc/traffic-mirror-sessions/{traffic_mirror_session_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteTrafficMirrorSessionResponse',
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

    def list_traffic_mirror_filter_rules_async(self, request):
        """查询流量镜像筛选规则列表

        查询流量镜像筛选规则列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListTrafficMirrorFilterRules
        :type request: :class:`huaweicloudsdkvpc.v3.ListTrafficMirrorFilterRulesRequest`
        :rtype: :class:`huaweicloudsdkvpc.v3.ListTrafficMirrorFilterRulesResponse`
        """
        return self._list_traffic_mirror_filter_rules_with_http_info(request)

    def _list_traffic_mirror_filter_rules_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'description' in local_var_params:
            query_params.append(('description', local_var_params['description']))
        if 'traffic_mirror_filter_id' in local_var_params:
            query_params.append(('traffic_mirror_filter_id', local_var_params['traffic_mirror_filter_id']))
        if 'direction' in local_var_params:
            query_params.append(('direction', local_var_params['direction']))
        if 'protocol' in local_var_params:
            query_params.append(('protocol', local_var_params['protocol']))
        if 'source_cidr_block' in local_var_params:
            query_params.append(('source_cidr_block', local_var_params['source_cidr_block']))
        if 'destination_cidr_block' in local_var_params:
            query_params.append(('destination_cidr_block', local_var_params['destination_cidr_block']))
        if 'source_port_range' in local_var_params:
            query_params.append(('source_port_range', local_var_params['source_port_range']))
        if 'destination_port_range' in local_var_params:
            query_params.append(('destination_port_range', local_var_params['destination_port_range']))
        if 'action' in local_var_params:
            query_params.append(('action', local_var_params['action']))
        if 'priority' in local_var_params:
            query_params.append(('priority', local_var_params['priority']))

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
            resource_path='/v3/{project_id}/vpc/traffic-mirror-filter-rules',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListTrafficMirrorFilterRulesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_traffic_mirror_filters_async(self, request):
        """查询流量镜像筛选条件列表

        查询流量镜像筛选条件列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListTrafficMirrorFilters
        :type request: :class:`huaweicloudsdkvpc.v3.ListTrafficMirrorFiltersRequest`
        :rtype: :class:`huaweicloudsdkvpc.v3.ListTrafficMirrorFiltersResponse`
        """
        return self._list_traffic_mirror_filters_with_http_info(request)

    def _list_traffic_mirror_filters_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'description' in local_var_params:
            query_params.append(('description', local_var_params['description']))
        if 'created_at' in local_var_params:
            query_params.append(('created_at', local_var_params['created_at']))
        if 'updated_at' in local_var_params:
            query_params.append(('updated_at', local_var_params['updated_at']))

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
            resource_path='/v3/{project_id}/vpc/traffic-mirror-filters',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListTrafficMirrorFiltersResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_traffic_mirror_sessions_async(self, request):
        """查询流量镜像会话列表

        查询流量镜像会话列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListTrafficMirrorSessions
        :type request: :class:`huaweicloudsdkvpc.v3.ListTrafficMirrorSessionsRequest`
        :rtype: :class:`huaweicloudsdkvpc.v3.ListTrafficMirrorSessionsResponse`
        """
        return self._list_traffic_mirror_sessions_with_http_info(request)

    def _list_traffic_mirror_sessions_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'description' in local_var_params:
            query_params.append(('description', local_var_params['description']))
        if 'traffic_mirror_filter_id' in local_var_params:
            query_params.append(('traffic_mirror_filter_id', local_var_params['traffic_mirror_filter_id']))
        if 'traffic_mirror_target_id' in local_var_params:
            query_params.append(('traffic_mirror_target_id', local_var_params['traffic_mirror_target_id']))
        if 'traffic_mirror_target_type' in local_var_params:
            query_params.append(('traffic_mirror_target_type', local_var_params['traffic_mirror_target_type']))
        if 'virtual_network_id' in local_var_params:
            query_params.append(('virtual_network_id', local_var_params['virtual_network_id']))
        if 'packet_length' in local_var_params:
            query_params.append(('packet_length', local_var_params['packet_length']))
        if 'priority' in local_var_params:
            query_params.append(('priority', local_var_params['priority']))
        if 'enabled' in local_var_params:
            query_params.append(('enabled', local_var_params['enabled']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'created_at' in local_var_params:
            query_params.append(('created_at', local_var_params['created_at']))
        if 'updated_at' in local_var_params:
            query_params.append(('updated_at', local_var_params['updated_at']))

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
            resource_path='/v3/{project_id}/vpc/traffic-mirror-sessions',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListTrafficMirrorSessionsResponse',
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

    def remove_sources_from_traffic_mirror_session_async(self, request):
        """流量镜像会话移除镜像源

        流量镜像会话移除镜像源
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RemoveSourcesFromTrafficMirrorSession
        :type request: :class:`huaweicloudsdkvpc.v3.RemoveSourcesFromTrafficMirrorSessionRequest`
        :rtype: :class:`huaweicloudsdkvpc.v3.RemoveSourcesFromTrafficMirrorSessionResponse`
        """
        return self._remove_sources_from_traffic_mirror_session_with_http_info(request)

    def _remove_sources_from_traffic_mirror_session_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'traffic_mirror_session_id' in local_var_params:
            path_params['traffic_mirror_session_id'] = local_var_params['traffic_mirror_session_id']

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
            resource_path='/v3/{project_id}/vpc/traffic-mirror-sessions/{traffic_mirror_session_id}/remove-sources',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RemoveSourcesFromTrafficMirrorSessionResponse',
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

    def show_traffic_mirror_filter_async(self, request):
        """查询流量镜像筛选条件详情

        查询流量镜像筛选条件详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowTrafficMirrorFilter
        :type request: :class:`huaweicloudsdkvpc.v3.ShowTrafficMirrorFilterRequest`
        :rtype: :class:`huaweicloudsdkvpc.v3.ShowTrafficMirrorFilterResponse`
        """
        return self._show_traffic_mirror_filter_with_http_info(request)

    def _show_traffic_mirror_filter_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'traffic_mirror_filter_id' in local_var_params:
            path_params['traffic_mirror_filter_id'] = local_var_params['traffic_mirror_filter_id']

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
            resource_path='/v3/{project_id}/vpc/traffic-mirror-filters/{traffic_mirror_filter_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowTrafficMirrorFilterResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_traffic_mirror_filter_rule_async(self, request):
        """查询流量镜像筛选规则详情

        查询流量镜像筛选规则详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowTrafficMirrorFilterRule
        :type request: :class:`huaweicloudsdkvpc.v3.ShowTrafficMirrorFilterRuleRequest`
        :rtype: :class:`huaweicloudsdkvpc.v3.ShowTrafficMirrorFilterRuleResponse`
        """
        return self._show_traffic_mirror_filter_rule_with_http_info(request)

    def _show_traffic_mirror_filter_rule_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'traffic_mirror_filter_rule_id' in local_var_params:
            path_params['traffic_mirror_filter_rule_id'] = local_var_params['traffic_mirror_filter_rule_id']

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
            resource_path='/v3/{project_id}/vpc/traffic-mirror-filter-rules/{traffic_mirror_filter_rule_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowTrafficMirrorFilterRuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_traffic_mirror_session_async(self, request):
        """查询流量镜像会话详情

        查询流量镜像会话详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowTrafficMirrorSession
        :type request: :class:`huaweicloudsdkvpc.v3.ShowTrafficMirrorSessionRequest`
        :rtype: :class:`huaweicloudsdkvpc.v3.ShowTrafficMirrorSessionResponse`
        """
        return self._show_traffic_mirror_session_with_http_info(request)

    def _show_traffic_mirror_session_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'traffic_mirror_session_id' in local_var_params:
            path_params['traffic_mirror_session_id'] = local_var_params['traffic_mirror_session_id']

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
            resource_path='/v3/{project_id}/vpc/traffic-mirror-sessions/{traffic_mirror_session_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowTrafficMirrorSessionResponse',
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

    def update_traffic_mirror_filter_async(self, request):
        """更新流量镜像筛选条件

        更新流量镜像筛选条件
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateTrafficMirrorFilter
        :type request: :class:`huaweicloudsdkvpc.v3.UpdateTrafficMirrorFilterRequest`
        :rtype: :class:`huaweicloudsdkvpc.v3.UpdateTrafficMirrorFilterResponse`
        """
        return self._update_traffic_mirror_filter_with_http_info(request)

    def _update_traffic_mirror_filter_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'traffic_mirror_filter_id' in local_var_params:
            path_params['traffic_mirror_filter_id'] = local_var_params['traffic_mirror_filter_id']

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
            resource_path='/v3/{project_id}/vpc/traffic-mirror-filters/{traffic_mirror_filter_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateTrafficMirrorFilterResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_traffic_mirror_filter_rule_async(self, request):
        """更新流量镜像筛选规则

        更新流量镜像筛选规则
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateTrafficMirrorFilterRule
        :type request: :class:`huaweicloudsdkvpc.v3.UpdateTrafficMirrorFilterRuleRequest`
        :rtype: :class:`huaweicloudsdkvpc.v3.UpdateTrafficMirrorFilterRuleResponse`
        """
        return self._update_traffic_mirror_filter_rule_with_http_info(request)

    def _update_traffic_mirror_filter_rule_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'traffic_mirror_filter_rule_id' in local_var_params:
            path_params['traffic_mirror_filter_rule_id'] = local_var_params['traffic_mirror_filter_rule_id']

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
            resource_path='/v3/{project_id}/vpc/traffic-mirror-filter-rules/{traffic_mirror_filter_rule_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateTrafficMirrorFilterRuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_traffic_mirror_session_async(self, request):
        """更新流量镜像会话

        更新流量镜像会话
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateTrafficMirrorSession
        :type request: :class:`huaweicloudsdkvpc.v3.UpdateTrafficMirrorSessionRequest`
        :rtype: :class:`huaweicloudsdkvpc.v3.UpdateTrafficMirrorSessionResponse`
        """
        return self._update_traffic_mirror_session_with_http_info(request)

    def _update_traffic_mirror_session_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'traffic_mirror_session_id' in local_var_params:
            path_params['traffic_mirror_session_id'] = local_var_params['traffic_mirror_session_id']

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
            resource_path='/v3/{project_id}/vpc/traffic-mirror-sessions/{traffic_mirror_session_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateTrafficMirrorSessionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def add_firewall_rules_async(self, request):
        """网络ACL插入规则

        网络ACL插入规则
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AddFirewallRules
        :type request: :class:`huaweicloudsdkvpc.v3.AddFirewallRulesRequest`
        :rtype: :class:`huaweicloudsdkvpc.v3.AddFirewallRulesResponse`
        """
        return self._add_firewall_rules_with_http_info(request)

    def _add_firewall_rules_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'firewall_id' in local_var_params:
            path_params['firewall_id'] = local_var_params['firewall_id']

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
            resource_path='/v3/{project_id}/vpc/firewalls/{firewall_id}/insert-rules',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='AddFirewallRulesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def associate_subnet_firewall_async(self, request):
        """网络ACL绑定子网

        网络ACL绑定子网
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AssociateSubnetFirewall
        :type request: :class:`huaweicloudsdkvpc.v3.AssociateSubnetFirewallRequest`
        :rtype: :class:`huaweicloudsdkvpc.v3.AssociateSubnetFirewallResponse`
        """
        return self._associate_subnet_firewall_with_http_info(request)

    def _associate_subnet_firewall_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'firewall_id' in local_var_params:
            path_params['firewall_id'] = local_var_params['firewall_id']

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
            resource_path='/v3/{project_id}/vpc/firewalls/{firewall_id}/associate-subnets',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='AssociateSubnetFirewallResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_firewall_async(self, request):
        """创建网络ACL

        创建网络ACL
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateFirewall
        :type request: :class:`huaweicloudsdkvpc.v3.CreateFirewallRequest`
        :rtype: :class:`huaweicloudsdkvpc.v3.CreateFirewallResponse`
        """
        return self._create_firewall_with_http_info(request)

    def _create_firewall_with_http_info(self, request):
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
            resource_path='/v3/{project_id}/vpc/firewalls',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateFirewallResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_firewall_async(self, request):
        """删除网络ACL

        删除网络ACL
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteFirewall
        :type request: :class:`huaweicloudsdkvpc.v3.DeleteFirewallRequest`
        :rtype: :class:`huaweicloudsdkvpc.v3.DeleteFirewallResponse`
        """
        return self._delete_firewall_with_http_info(request)

    def _delete_firewall_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'firewall_id' in local_var_params:
            path_params['firewall_id'] = local_var_params['firewall_id']

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
            resource_path='/v3/{project_id}/vpc/firewalls/{firewall_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteFirewallResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def disassociate_subnet_firewall_async(self, request):
        """网络ACL解绑子网

        网络ACL解绑子网
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DisassociateSubnetFirewall
        :type request: :class:`huaweicloudsdkvpc.v3.DisassociateSubnetFirewallRequest`
        :rtype: :class:`huaweicloudsdkvpc.v3.DisassociateSubnetFirewallResponse`
        """
        return self._disassociate_subnet_firewall_with_http_info(request)

    def _disassociate_subnet_firewall_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'firewall_id' in local_var_params:
            path_params['firewall_id'] = local_var_params['firewall_id']

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
            resource_path='/v3/{project_id}/vpc/firewalls/{firewall_id}/disassociate-subnets',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DisassociateSubnetFirewallResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_firewall_async(self, request):
        """查询网络ACL列表

        查询网络ACL列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListFirewall
        :type request: :class:`huaweicloudsdkvpc.v3.ListFirewallRequest`
        :rtype: :class:`huaweicloudsdkvpc.v3.ListFirewallResponse`
        """
        return self._list_firewall_with_http_info(request)

    def _list_firewall_with_http_info(self, request):
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
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'admin_state_up' in local_var_params:
            query_params.append(('admin_state_up', local_var_params['admin_state_up']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
            collection_formats['enterprise_project_id'] = 'multi'

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
            resource_path='/v3/{project_id}/vpc/firewalls',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListFirewallResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def remove_firewall_rules_async(self, request):
        """网络ACL移除规则

        网络ACL移除规则
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RemoveFirewallRules
        :type request: :class:`huaweicloudsdkvpc.v3.RemoveFirewallRulesRequest`
        :rtype: :class:`huaweicloudsdkvpc.v3.RemoveFirewallRulesResponse`
        """
        return self._remove_firewall_rules_with_http_info(request)

    def _remove_firewall_rules_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'firewall_id' in local_var_params:
            path_params['firewall_id'] = local_var_params['firewall_id']

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
            resource_path='/v3/{project_id}/vpc/firewalls/{firewall_id}/remove-rules',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RemoveFirewallRulesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_firewall_async(self, request):
        """查询网络ACL详情

        查询网络ACL详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowFirewall
        :type request: :class:`huaweicloudsdkvpc.v3.ShowFirewallRequest`
        :rtype: :class:`huaweicloudsdkvpc.v3.ShowFirewallResponse`
        """
        return self._show_firewall_with_http_info(request)

    def _show_firewall_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'firewall_id' in local_var_params:
            path_params['firewall_id'] = local_var_params['firewall_id']

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
            resource_path='/v3/{project_id}/vpc/firewalls/{firewall_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowFirewallResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_firewall_async(self, request):
        """更新网络ACL

        更新网络ACL
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateFirewall
        :type request: :class:`huaweicloudsdkvpc.v3.UpdateFirewallRequest`
        :rtype: :class:`huaweicloudsdkvpc.v3.UpdateFirewallResponse`
        """
        return self._update_firewall_with_http_info(request)

    def _update_firewall_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'firewall_id' in local_var_params:
            path_params['firewall_id'] = local_var_params['firewall_id']

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
            resource_path='/v3/{project_id}/vpc/firewalls/{firewall_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateFirewallResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_firewall_rules_async(self, request):
        """网络ACL更新规则

        网络ACL更新规则
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateFirewallRules
        :type request: :class:`huaweicloudsdkvpc.v3.UpdateFirewallRulesRequest`
        :rtype: :class:`huaweicloudsdkvpc.v3.UpdateFirewallRulesResponse`
        """
        return self._update_firewall_rules_with_http_info(request)

    def _update_firewall_rules_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'firewall_id' in local_var_params:
            path_params['firewall_id'] = local_var_params['firewall_id']

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
            resource_path='/v3/{project_id}/vpc/firewalls/{firewall_id}/update-rules',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateFirewallRulesResponse',
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

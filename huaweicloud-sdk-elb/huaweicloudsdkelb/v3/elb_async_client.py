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


class ElbAsyncClient(Client):
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
        super(ElbAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkelb.v3.model")
        self.preset_headers = {'User-Agent': 'HuaweiCloud-SDK-Python'}

    @classmethod
    def new_builder(cls, clazz=None):
        if clazz is None:
            return ClientBuilder(cls)

        if clazz.__name__ != "ElbClient":
            raise TypeError("client type error, support client type is ElbClient")

        return ClientBuilder(clazz)

    def batch_create_members_async(self, request):
        """批量创建后端服务器

        在指定pool下批量创建后端服务器。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchCreateMembers
        :type request: :class:`huaweicloudsdkelb.v3.BatchCreateMembersRequest`
        :rtype: :class:`huaweicloudsdkelb.v3.BatchCreateMembersResponse`
        """
        return self.batch_create_members_with_http_info(request)

    def batch_create_members_with_http_info(self, request):
        all_params = ['pool_id', 'batch_create_members_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'pool_id' in local_var_params:
            path_params['pool_id'] = local_var_params['pool_id']

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
            resource_path='/v3/{project_id}/elb/pools/{pool_id}/members/batch-add',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchCreateMembersResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_delete_members_async(self, request):
        """批量删除后端服务器

        在指定pool下批量删除后端服务器。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchDeleteMembers
        :type request: :class:`huaweicloudsdkelb.v3.BatchDeleteMembersRequest`
        :rtype: :class:`huaweicloudsdkelb.v3.BatchDeleteMembersResponse`
        """
        return self.batch_delete_members_with_http_info(request)

    def batch_delete_members_with_http_info(self, request):
        all_params = ['pool_id', 'batch_delete_members_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'pool_id' in local_var_params:
            path_params['pool_id'] = local_var_params['pool_id']

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
            resource_path='/v3/{project_id}/elb/pools/{pool_id}/members/batch-delete',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchDeleteMembersResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_update_policies_priority_async(self, request):
        """批量更新转发策略优先级

        批量更新转发策略的优先级。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchUpdatePoliciesPriority
        :type request: :class:`huaweicloudsdkelb.v3.BatchUpdatePoliciesPriorityRequest`
        :rtype: :class:`huaweicloudsdkelb.v3.BatchUpdatePoliciesPriorityResponse`
        """
        return self.batch_update_policies_priority_with_http_info(request)

    def batch_update_policies_priority_with_http_info(self, request):
        all_params = ['batch_update_policies_priority_request_body']
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
            resource_path='/v3/{project_id}/elb/l7policies/batch-update-priority',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchUpdatePoliciesPriorityResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def change_loadbalancer_charge_mode_async(self, request):
        """变更负载均衡器计费模式

        负载均衡器计费模式变更，当前只支持按需计费转包周期计费。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ChangeLoadbalancerChargeMode
        :type request: :class:`huaweicloudsdkelb.v3.ChangeLoadbalancerChargeModeRequest`
        :rtype: :class:`huaweicloudsdkelb.v3.ChangeLoadbalancerChargeModeResponse`
        """
        return self.change_loadbalancer_charge_mode_with_http_info(request)

    def change_loadbalancer_charge_mode_with_http_info(self, request):
        all_params = ['change_loadbalancer_charge_mode_request_body']
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
            resource_path='/v3/{project_id}/elb/loadbalancers/change-charge-mode',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ChangeLoadbalancerChargeModeResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_certificate_async(self, request):
        """创建证书

        创建证书。用于HTTPS协议监听器。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateCertificate
        :type request: :class:`huaweicloudsdkelb.v3.CreateCertificateRequest`
        :rtype: :class:`huaweicloudsdkelb.v3.CreateCertificateResponse`
        """
        return self.create_certificate_with_http_info(request)

    def create_certificate_with_http_info(self, request):
        all_params = ['create_certificate_request_body']
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
            resource_path='/v3/{project_id}/elb/certificates',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateCertificateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_health_monitor_async(self, request):
        """创建健康检查

        创建健康检查。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateHealthMonitor
        :type request: :class:`huaweicloudsdkelb.v3.CreateHealthMonitorRequest`
        :rtype: :class:`huaweicloudsdkelb.v3.CreateHealthMonitorResponse`
        """
        return self.create_health_monitor_with_http_info(request)

    def create_health_monitor_with_http_info(self, request):
        all_params = ['create_health_monitor_request_body']
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
            resource_path='/v3/{project_id}/elb/healthmonitors',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateHealthMonitorResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_l7_policy_async(self, request):
        """创建转发策略

        创建七层转发策略。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateL7Policy
        :type request: :class:`huaweicloudsdkelb.v3.CreateL7PolicyRequest`
        :rtype: :class:`huaweicloudsdkelb.v3.CreateL7PolicyResponse`
        """
        return self.create_l7_policy_with_http_info(request)

    def create_l7_policy_with_http_info(self, request):
        all_params = ['create_l7_policy_request_body']
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
            resource_path='/v3/{project_id}/elb/l7policies',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateL7PolicyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_l7_rule_async(self, request):
        """创建转发规则

        创建七层转发规则。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateL7Rule
        :type request: :class:`huaweicloudsdkelb.v3.CreateL7RuleRequest`
        :rtype: :class:`huaweicloudsdkelb.v3.CreateL7RuleResponse`
        """
        return self.create_l7_rule_with_http_info(request)

    def create_l7_rule_with_http_info(self, request):
        all_params = ['l7policy_id', 'create_l7_rule_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'l7policy_id' in local_var_params:
            path_params['l7policy_id'] = local_var_params['l7policy_id']

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
            resource_path='/v3/{project_id}/elb/l7policies/{l7policy_id}/rules',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateL7RuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_listener_async(self, request):
        """创建监听器

        创建监听器。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateListener
        :type request: :class:`huaweicloudsdkelb.v3.CreateListenerRequest`
        :rtype: :class:`huaweicloudsdkelb.v3.CreateListenerResponse`
        """
        return self.create_listener_with_http_info(request)

    def create_listener_with_http_info(self, request):
        all_params = ['create_listener_request_body']
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
            resource_path='/v3/{project_id}/elb/listeners',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateListenerResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_load_balancer_async(self, request):
        """创建负载均衡器

        创建负载均衡器。
        1. 若要创建内网IPv4负载均衡器，则需要设置vip_subnet_cidr_id。
        2. 若要创建公网IPv4负载均衡器，则需要设置publicip，以及设置vpc_id和vip_subnet_cidr_id这两个参数中的一个。
        3. 若要绑定有已有公网IPv4地址，
        则需要设置publicip_ids，以及设置vpc_id和vip_subnet_cidr_id这两个参数中的一个。
        4. 若要创建内网双栈负载均衡器，则需要设置ipv6_vip_virsubnet_id。
        5. 若要创建公网双栈负载均衡器，则需要设置ipv6_vip_virsubnet_id和ipv6_bandwidth。
        6. 不支持绑定已有未使用的内网IPv4、内网IPv6或公网IPv6地址。
        
        [&gt; 不支持创建IPv6地址负载均衡器](tag:dt,dt_test)
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateLoadBalancer
        :type request: :class:`huaweicloudsdkelb.v3.CreateLoadBalancerRequest`
        :rtype: :class:`huaweicloudsdkelb.v3.CreateLoadBalancerResponse`
        """
        return self.create_load_balancer_with_http_info(request)

    def create_load_balancer_with_http_info(self, request):
        all_params = ['create_load_balancer_request_body']
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
            resource_path='/v3/{project_id}/elb/loadbalancers',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateLoadBalancerResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_logtank_async(self, request):
        """创建云日志

        创建云日志。[荷兰region不支持云日志功能，请勿使用。](tag:dt)
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateLogtank
        :type request: :class:`huaweicloudsdkelb.v3.CreateLogtankRequest`
        :rtype: :class:`huaweicloudsdkelb.v3.CreateLogtankResponse`
        """
        return self.create_logtank_with_http_info(request)

    def create_logtank_with_http_info(self, request):
        all_params = ['create_logtank_request_body']
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
            resource_path='/v3/{project_id}/elb/logtanks',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateLogtankResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_member_async(self, request):
        """创建后端服务器

        创建后端服务器。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateMember
        :type request: :class:`huaweicloudsdkelb.v3.CreateMemberRequest`
        :rtype: :class:`huaweicloudsdkelb.v3.CreateMemberResponse`
        """
        return self.create_member_with_http_info(request)

    def create_member_with_http_info(self, request):
        all_params = ['pool_id', 'create_member_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'pool_id' in local_var_params:
            path_params['pool_id'] = local_var_params['pool_id']

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
            resource_path='/v3/{project_id}/elb/pools/{pool_id}/members',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateMemberResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_pool_async(self, request):
        """创建后端服务器组

        创建后端服务器组。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreatePool
        :type request: :class:`huaweicloudsdkelb.v3.CreatePoolRequest`
        :rtype: :class:`huaweicloudsdkelb.v3.CreatePoolResponse`
        """
        return self.create_pool_with_http_info(request)

    def create_pool_with_http_info(self, request):
        all_params = ['create_pool_request_body']
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
            resource_path='/v3/{project_id}/elb/pools',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreatePoolResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_security_policy_async(self, request):
        """创建自定义安全策略

        创建自定义安全策略。用于在创建HTTPS监听器时，请求参数中指定security_policy_id来设置监听器的自定义安全策略。
        
        [荷兰region不支持自定义安全策略功能，请勿使用。](tag:dt)
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateSecurityPolicy
        :type request: :class:`huaweicloudsdkelb.v3.CreateSecurityPolicyRequest`
        :rtype: :class:`huaweicloudsdkelb.v3.CreateSecurityPolicyResponse`
        """
        return self.create_security_policy_with_http_info(request)

    def create_security_policy_with_http_info(self, request):
        all_params = ['create_security_policy_request_body']
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
            resource_path='/v3/{project_id}/elb/security-policies',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateSecurityPolicyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_certificate_async(self, request):
        """删除证书

        删除证书。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteCertificate
        :type request: :class:`huaweicloudsdkelb.v3.DeleteCertificateRequest`
        :rtype: :class:`huaweicloudsdkelb.v3.DeleteCertificateResponse`
        """
        return self.delete_certificate_with_http_info(request)

    def delete_certificate_with_http_info(self, request):
        all_params = ['certificate_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'certificate_id' in local_var_params:
            path_params['certificate_id'] = local_var_params['certificate_id']

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
            resource_path='/v3/{project_id}/elb/certificates/{certificate_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteCertificateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_health_monitor_async(self, request):
        """删除健康检查

        删除健康检查。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteHealthMonitor
        :type request: :class:`huaweicloudsdkelb.v3.DeleteHealthMonitorRequest`
        :rtype: :class:`huaweicloudsdkelb.v3.DeleteHealthMonitorResponse`
        """
        return self.delete_health_monitor_with_http_info(request)

    def delete_health_monitor_with_http_info(self, request):
        all_params = ['healthmonitor_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'healthmonitor_id' in local_var_params:
            path_params['healthmonitor_id'] = local_var_params['healthmonitor_id']

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
            resource_path='/v3/{project_id}/elb/healthmonitors/{healthmonitor_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteHealthMonitorResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_l7_policy_async(self, request):
        """删除转发策略

        删除七层转发策略。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteL7Policy
        :type request: :class:`huaweicloudsdkelb.v3.DeleteL7PolicyRequest`
        :rtype: :class:`huaweicloudsdkelb.v3.DeleteL7PolicyResponse`
        """
        return self.delete_l7_policy_with_http_info(request)

    def delete_l7_policy_with_http_info(self, request):
        all_params = ['l7policy_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'l7policy_id' in local_var_params:
            path_params['l7policy_id'] = local_var_params['l7policy_id']

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
            resource_path='/v3/{project_id}/elb/l7policies/{l7policy_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteL7PolicyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_l7_rule_async(self, request):
        """删除转发规则

        删除七层转发规则。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteL7Rule
        :type request: :class:`huaweicloudsdkelb.v3.DeleteL7RuleRequest`
        :rtype: :class:`huaweicloudsdkelb.v3.DeleteL7RuleResponse`
        """
        return self.delete_l7_rule_with_http_info(request)

    def delete_l7_rule_with_http_info(self, request):
        all_params = ['l7policy_id', 'l7rule_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'l7policy_id' in local_var_params:
            path_params['l7policy_id'] = local_var_params['l7policy_id']
        if 'l7rule_id' in local_var_params:
            path_params['l7rule_id'] = local_var_params['l7rule_id']

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
            resource_path='/v3/{project_id}/elb/l7policies/{l7policy_id}/rules/{l7rule_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteL7RuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_listener_async(self, request):
        """删除监听器

        删除监听器。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteListener
        :type request: :class:`huaweicloudsdkelb.v3.DeleteListenerRequest`
        :rtype: :class:`huaweicloudsdkelb.v3.DeleteListenerResponse`
        """
        return self.delete_listener_with_http_info(request)

    def delete_listener_with_http_info(self, request):
        all_params = ['listener_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'listener_id' in local_var_params:
            path_params['listener_id'] = local_var_params['listener_id']

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
            resource_path='/v3/{project_id}/elb/listeners/{listener_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteListenerResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_load_balancer_async(self, request):
        """删除负载均衡器

        删除负载均衡器。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteLoadBalancer
        :type request: :class:`huaweicloudsdkelb.v3.DeleteLoadBalancerRequest`
        :rtype: :class:`huaweicloudsdkelb.v3.DeleteLoadBalancerResponse`
        """
        return self.delete_load_balancer_with_http_info(request)

    def delete_load_balancer_with_http_info(self, request):
        all_params = ['loadbalancer_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'loadbalancer_id' in local_var_params:
            path_params['loadbalancer_id'] = local_var_params['loadbalancer_id']

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
            resource_path='/v3/{project_id}/elb/loadbalancers/{loadbalancer_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteLoadBalancerResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_logtank_async(self, request):
        """删除云日志

        删除云日志。[荷兰region不支持云日志功能，请勿使用。](tag:dt)
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteLogtank
        :type request: :class:`huaweicloudsdkelb.v3.DeleteLogtankRequest`
        :rtype: :class:`huaweicloudsdkelb.v3.DeleteLogtankResponse`
        """
        return self.delete_logtank_with_http_info(request)

    def delete_logtank_with_http_info(self, request):
        all_params = ['logtank_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'logtank_id' in local_var_params:
            path_params['logtank_id'] = local_var_params['logtank_id']

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
            resource_path='/v3/{project_id}/elb/logtanks/{logtank_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteLogtankResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_member_async(self, request):
        """删除后端服务器

        删除后端服务器。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteMember
        :type request: :class:`huaweicloudsdkelb.v3.DeleteMemberRequest`
        :rtype: :class:`huaweicloudsdkelb.v3.DeleteMemberResponse`
        """
        return self.delete_member_with_http_info(request)

    def delete_member_with_http_info(self, request):
        all_params = ['pool_id', 'member_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'pool_id' in local_var_params:
            path_params['pool_id'] = local_var_params['pool_id']
        if 'member_id' in local_var_params:
            path_params['member_id'] = local_var_params['member_id']

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
            resource_path='/v3/{project_id}/elb/pools/{pool_id}/members/{member_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteMemberResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_pool_async(self, request):
        """删除后端服务器组

        删除后端服务器组。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeletePool
        :type request: :class:`huaweicloudsdkelb.v3.DeletePoolRequest`
        :rtype: :class:`huaweicloudsdkelb.v3.DeletePoolResponse`
        """
        return self.delete_pool_with_http_info(request)

    def delete_pool_with_http_info(self, request):
        all_params = ['pool_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'pool_id' in local_var_params:
            path_params['pool_id'] = local_var_params['pool_id']

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
            resource_path='/v3/{project_id}/elb/pools/{pool_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeletePoolResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_security_policy_async(self, request):
        """删除自定义安全策略

        删除自定义安全策略。[荷兰region不支持自定义安全策略功能，请勿使用。](tag:dt)
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteSecurityPolicy
        :type request: :class:`huaweicloudsdkelb.v3.DeleteSecurityPolicyRequest`
        :rtype: :class:`huaweicloudsdkelb.v3.DeleteSecurityPolicyResponse`
        """
        return self.delete_security_policy_with_http_info(request)

    def delete_security_policy_with_http_info(self, request):
        all_params = ['security_policy_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'security_policy_id' in local_var_params:
            path_params['security_policy_id'] = local_var_params['security_policy_id']

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
            resource_path='/v3/{project_id}/elb/security-policies/{security_policy_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteSecurityPolicyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_all_members_async(self, request):
        """后端服务器全局列表

        查询当前租户下的后端服务器列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAllMembers
        :type request: :class:`huaweicloudsdkelb.v3.ListAllMembersRequest`
        :rtype: :class:`huaweicloudsdkelb.v3.ListAllMembersResponse`
        """
        return self.list_all_members_with_http_info(request)

    def list_all_members_with_http_info(self, request):
        all_params = ['marker', 'limit', 'page_reverse', 'name', 'weight', 'admin_state_up', 'subnet_cidr_id', 'address', 'protocol_port', 'id', 'operating_status', 'enterprise_project_id', 'ip_version', 'pool_id', 'loadbalancer_id']
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
        if 'page_reverse' in local_var_params:
            query_params.append(('page_reverse', local_var_params['page_reverse']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
            collection_formats['name'] = 'multi'
        if 'weight' in local_var_params:
            query_params.append(('weight', local_var_params['weight']))
            collection_formats['weight'] = 'multi'
        if 'admin_state_up' in local_var_params:
            query_params.append(('admin_state_up', local_var_params['admin_state_up']))
        if 'subnet_cidr_id' in local_var_params:
            query_params.append(('subnet_cidr_id', local_var_params['subnet_cidr_id']))
            collection_formats['subnet_cidr_id'] = 'multi'
        if 'address' in local_var_params:
            query_params.append(('address', local_var_params['address']))
            collection_formats['address'] = 'multi'
        if 'protocol_port' in local_var_params:
            query_params.append(('protocol_port', local_var_params['protocol_port']))
            collection_formats['protocol_port'] = 'multi'
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
            collection_formats['id'] = 'multi'
        if 'operating_status' in local_var_params:
            query_params.append(('operating_status', local_var_params['operating_status']))
            collection_formats['operating_status'] = 'multi'
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
            collection_formats['enterprise_project_id'] = 'multi'
        if 'ip_version' in local_var_params:
            query_params.append(('ip_version', local_var_params['ip_version']))
            collection_formats['ip_version'] = 'multi'
        if 'pool_id' in local_var_params:
            query_params.append(('pool_id', local_var_params['pool_id']))
            collection_formats['pool_id'] = 'multi'
        if 'loadbalancer_id' in local_var_params:
            query_params.append(('loadbalancer_id', local_var_params['loadbalancer_id']))
            collection_formats['loadbalancer_id'] = 'multi'

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
            resource_path='/v3/{project_id}/elb/members',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListAllMembersResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_availability_zones_async(self, request):
        """查询可用区列表

        返回租户创建LB时可使用的可用区集合列表情况。
        
        - 默认情况下，会返回一个可用区集合。
        在（如创建LB）设置可用区时，填写的可用区必须包含在可用区集合中、为这个可用区集合的子集。
        
        - 特殊场景下，部分客户要求负载均衡只能创建在指定可用区集合中，此时会返回客户定制的可用区集合。
        返回可用区集合可能为一个也可能为多个，比如列表有两个可用区集合\\[az1,az2\\],\\[az2,az3\\]。
        在创建负载均衡器时，可以选择创建在多个可用区，但所选的多个可用区必须同属于其中一个可用区集合，
        如可以选az2和az3，但不能选择az1和az3。你可以选择多个可用区，只要这些可用区在一个子集中
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAvailabilityZones
        :type request: :class:`huaweicloudsdkelb.v3.ListAvailabilityZonesRequest`
        :rtype: :class:`huaweicloudsdkelb.v3.ListAvailabilityZonesResponse`
        """
        return self.list_availability_zones_with_http_info(request)

    def list_availability_zones_with_http_info(self, request):
        all_params = ['public_border_group']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'public_border_group' in local_var_params:
            query_params.append(('public_border_group', local_var_params['public_border_group']))

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
            resource_path='/v3/{project_id}/elb/availability-zones',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListAvailabilityZonesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_certificates_async(self, request):
        """查询证书列表

        查询证书列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListCertificates
        :type request: :class:`huaweicloudsdkelb.v3.ListCertificatesRequest`
        :rtype: :class:`huaweicloudsdkelb.v3.ListCertificatesResponse`
        """
        return self.list_certificates_with_http_info(request)

    def list_certificates_with_http_info(self, request):
        all_params = ['marker', 'limit', 'page_reverse', 'id', 'name', 'description', 'admin_state_up', 'domain', 'type']
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
        if 'page_reverse' in local_var_params:
            query_params.append(('page_reverse', local_var_params['page_reverse']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
            collection_formats['id'] = 'multi'
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
            collection_formats['name'] = 'multi'
        if 'description' in local_var_params:
            query_params.append(('description', local_var_params['description']))
            collection_formats['description'] = 'multi'
        if 'admin_state_up' in local_var_params:
            query_params.append(('admin_state_up', local_var_params['admin_state_up']))
        if 'domain' in local_var_params:
            query_params.append(('domain', local_var_params['domain']))
            collection_formats['domain'] = 'multi'
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
            collection_formats['type'] = 'multi'

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
            resource_path='/v3/{project_id}/elb/certificates',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListCertificatesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_flavors_async(self, request):
        """查询规格列表

        查询租户在当前region下可用的负载均衡规格列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListFlavors
        :type request: :class:`huaweicloudsdkelb.v3.ListFlavorsRequest`
        :rtype: :class:`huaweicloudsdkelb.v3.ListFlavorsResponse`
        """
        return self.list_flavors_with_http_info(request)

    def list_flavors_with_http_info(self, request):
        all_params = ['marker', 'limit', 'page_reverse', 'id', 'name', 'type', 'shared']
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
        if 'page_reverse' in local_var_params:
            query_params.append(('page_reverse', local_var_params['page_reverse']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
            collection_formats['id'] = 'multi'
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
            collection_formats['name'] = 'multi'
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
            collection_formats['type'] = 'multi'
        if 'shared' in local_var_params:
            query_params.append(('shared', local_var_params['shared']))

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
            resource_path='/v3/{project_id}/elb/flavors',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListFlavorsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_health_monitors_async(self, request):
        """查询健康检查列表

        健康检查列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListHealthMonitors
        :type request: :class:`huaweicloudsdkelb.v3.ListHealthMonitorsRequest`
        :rtype: :class:`huaweicloudsdkelb.v3.ListHealthMonitorsResponse`
        """
        return self.list_health_monitors_with_http_info(request)

    def list_health_monitors_with_http_info(self, request):
        all_params = ['marker', 'limit', 'page_reverse', 'id', 'monitor_port', 'domain_name', 'name', 'delay', 'max_retries', 'admin_state_up', 'max_retries_down', 'timeout', 'type', 'expected_codes', 'url_path', 'http_method', 'enterprise_project_id']
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
        if 'page_reverse' in local_var_params:
            query_params.append(('page_reverse', local_var_params['page_reverse']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
            collection_formats['id'] = 'multi'
        if 'monitor_port' in local_var_params:
            query_params.append(('monitor_port', local_var_params['monitor_port']))
            collection_formats['monitor_port'] = 'multi'
        if 'domain_name' in local_var_params:
            query_params.append(('domain_name', local_var_params['domain_name']))
            collection_formats['domain_name'] = 'multi'
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
            collection_formats['name'] = 'multi'
        if 'delay' in local_var_params:
            query_params.append(('delay', local_var_params['delay']))
            collection_formats['delay'] = 'multi'
        if 'max_retries' in local_var_params:
            query_params.append(('max_retries', local_var_params['max_retries']))
            collection_formats['max_retries'] = 'multi'
        if 'admin_state_up' in local_var_params:
            query_params.append(('admin_state_up', local_var_params['admin_state_up']))
        if 'max_retries_down' in local_var_params:
            query_params.append(('max_retries_down', local_var_params['max_retries_down']))
            collection_formats['max_retries_down'] = 'multi'
        if 'timeout' in local_var_params:
            query_params.append(('timeout', local_var_params['timeout']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
            collection_formats['type'] = 'multi'
        if 'expected_codes' in local_var_params:
            query_params.append(('expected_codes', local_var_params['expected_codes']))
            collection_formats['expected_codes'] = 'multi'
        if 'url_path' in local_var_params:
            query_params.append(('url_path', local_var_params['url_path']))
            collection_formats['url_path'] = 'multi'
        if 'http_method' in local_var_params:
            query_params.append(('http_method', local_var_params['http_method']))
            collection_formats['http_method'] = 'multi'
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
            resource_path='/v3/{project_id}/elb/healthmonitors',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListHealthMonitorsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_l7_policies_async(self, request):
        """查询转发策略列表

        查询七层转发策略列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListL7Policies
        :type request: :class:`huaweicloudsdkelb.v3.ListL7PoliciesRequest`
        :rtype: :class:`huaweicloudsdkelb.v3.ListL7PoliciesResponse`
        """
        return self.list_l7_policies_with_http_info(request)

    def list_l7_policies_with_http_info(self, request):
        all_params = ['marker', 'limit', 'page_reverse', 'enterprise_project_id', 'id', 'name', 'description', 'admin_state_up', 'listener_id', 'position', 'action', 'redirect_url', 'redirect_pool_id', 'redirect_listener_id', 'provisioning_status', 'display_all_rules', 'priority']
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
        if 'page_reverse' in local_var_params:
            query_params.append(('page_reverse', local_var_params['page_reverse']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
            collection_formats['enterprise_project_id'] = 'multi'
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
            collection_formats['id'] = 'multi'
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
            collection_formats['name'] = 'multi'
        if 'description' in local_var_params:
            query_params.append(('description', local_var_params['description']))
            collection_formats['description'] = 'multi'
        if 'admin_state_up' in local_var_params:
            query_params.append(('admin_state_up', local_var_params['admin_state_up']))
        if 'listener_id' in local_var_params:
            query_params.append(('listener_id', local_var_params['listener_id']))
            collection_formats['listener_id'] = 'multi'
        if 'position' in local_var_params:
            query_params.append(('position', local_var_params['position']))
            collection_formats['position'] = 'multi'
        if 'action' in local_var_params:
            query_params.append(('action', local_var_params['action']))
            collection_formats['action'] = 'multi'
        if 'redirect_url' in local_var_params:
            query_params.append(('redirect_url', local_var_params['redirect_url']))
            collection_formats['redirect_url'] = 'multi'
        if 'redirect_pool_id' in local_var_params:
            query_params.append(('redirect_pool_id', local_var_params['redirect_pool_id']))
            collection_formats['redirect_pool_id'] = 'multi'
        if 'redirect_listener_id' in local_var_params:
            query_params.append(('redirect_listener_id', local_var_params['redirect_listener_id']))
            collection_formats['redirect_listener_id'] = 'multi'
        if 'provisioning_status' in local_var_params:
            query_params.append(('provisioning_status', local_var_params['provisioning_status']))
            collection_formats['provisioning_status'] = 'multi'
        if 'display_all_rules' in local_var_params:
            query_params.append(('display_all_rules', local_var_params['display_all_rules']))
        if 'priority' in local_var_params:
            query_params.append(('priority', local_var_params['priority']))
            collection_formats['priority'] = 'csv'

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
            resource_path='/v3/{project_id}/elb/l7policies',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListL7PoliciesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_l7_rules_async(self, request):
        """查询转发规则列表

        查询转发规则列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListL7Rules
        :type request: :class:`huaweicloudsdkelb.v3.ListL7RulesRequest`
        :rtype: :class:`huaweicloudsdkelb.v3.ListL7RulesResponse`
        """
        return self.list_l7_rules_with_http_info(request)

    def list_l7_rules_with_http_info(self, request):
        all_params = ['l7policy_id', 'limit', 'marker', 'page_reverse', 'id', 'compare_type', 'provisioning_status', 'invert', 'admin_state_up', 'value', 'key', 'type', 'enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'l7policy_id' in local_var_params:
            path_params['l7policy_id'] = local_var_params['l7policy_id']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'page_reverse' in local_var_params:
            query_params.append(('page_reverse', local_var_params['page_reverse']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
            collection_formats['id'] = 'multi'
        if 'compare_type' in local_var_params:
            query_params.append(('compare_type', local_var_params['compare_type']))
            collection_formats['compare_type'] = 'multi'
        if 'provisioning_status' in local_var_params:
            query_params.append(('provisioning_status', local_var_params['provisioning_status']))
            collection_formats['provisioning_status'] = 'multi'
        if 'invert' in local_var_params:
            query_params.append(('invert', local_var_params['invert']))
        if 'admin_state_up' in local_var_params:
            query_params.append(('admin_state_up', local_var_params['admin_state_up']))
        if 'value' in local_var_params:
            query_params.append(('value', local_var_params['value']))
            collection_formats['value'] = 'multi'
        if 'key' in local_var_params:
            query_params.append(('key', local_var_params['key']))
            collection_formats['key'] = 'multi'
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
            collection_formats['type'] = 'multi'
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
            resource_path='/v3/{project_id}/elb/l7policies/{l7policy_id}/rules',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListL7RulesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_listeners_async(self, request):
        """查询监听器列表

        查询监听器列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListListeners
        :type request: :class:`huaweicloudsdkelb.v3.ListListenersRequest`
        :rtype: :class:`huaweicloudsdkelb.v3.ListListenersResponse`
        """
        return self.list_listeners_with_http_info(request)

    def list_listeners_with_http_info(self, request):
        all_params = ['limit', 'marker', 'page_reverse', 'protocol_port', 'protocol', 'description', 'default_tls_container_ref', 'client_ca_tls_container_ref', 'admin_state_up', 'connection_limit', 'default_pool_id', 'id', 'name', 'http2_enable', 'loadbalancer_id', 'tls_ciphers_policy', 'member_address', 'member_device_id', 'enterprise_project_id', 'enable_member_retry', 'member_timeout', 'client_timeout', 'keepalive_timeout', 'transparent_client_ip_enable', 'enhance_l7policy_enable', 'member_instance_id']
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
        if 'protocol_port' in local_var_params:
            query_params.append(('protocol_port', local_var_params['protocol_port']))
            collection_formats['protocol_port'] = 'multi'
        if 'protocol' in local_var_params:
            query_params.append(('protocol', local_var_params['protocol']))
            collection_formats['protocol'] = 'multi'
        if 'description' in local_var_params:
            query_params.append(('description', local_var_params['description']))
            collection_formats['description'] = 'multi'
        if 'default_tls_container_ref' in local_var_params:
            query_params.append(('default_tls_container_ref', local_var_params['default_tls_container_ref']))
            collection_formats['default_tls_container_ref'] = 'multi'
        if 'client_ca_tls_container_ref' in local_var_params:
            query_params.append(('client_ca_tls_container_ref', local_var_params['client_ca_tls_container_ref']))
            collection_formats['client_ca_tls_container_ref'] = 'multi'
        if 'admin_state_up' in local_var_params:
            query_params.append(('admin_state_up', local_var_params['admin_state_up']))
        if 'connection_limit' in local_var_params:
            query_params.append(('connection_limit', local_var_params['connection_limit']))
            collection_formats['connection_limit'] = 'multi'
        if 'default_pool_id' in local_var_params:
            query_params.append(('default_pool_id', local_var_params['default_pool_id']))
            collection_formats['default_pool_id'] = 'multi'
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
            collection_formats['id'] = 'multi'
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
            collection_formats['name'] = 'multi'
        if 'http2_enable' in local_var_params:
            query_params.append(('http2_enable', local_var_params['http2_enable']))
        if 'loadbalancer_id' in local_var_params:
            query_params.append(('loadbalancer_id', local_var_params['loadbalancer_id']))
            collection_formats['loadbalancer_id'] = 'multi'
        if 'tls_ciphers_policy' in local_var_params:
            query_params.append(('tls_ciphers_policy', local_var_params['tls_ciphers_policy']))
            collection_formats['tls_ciphers_policy'] = 'multi'
        if 'member_address' in local_var_params:
            query_params.append(('member_address', local_var_params['member_address']))
            collection_formats['member_address'] = 'multi'
        if 'member_device_id' in local_var_params:
            query_params.append(('member_device_id', local_var_params['member_device_id']))
            collection_formats['member_device_id'] = 'multi'
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
            collection_formats['enterprise_project_id'] = 'multi'
        if 'enable_member_retry' in local_var_params:
            query_params.append(('enable_member_retry', local_var_params['enable_member_retry']))
        if 'member_timeout' in local_var_params:
            query_params.append(('member_timeout', local_var_params['member_timeout']))
            collection_formats['member_timeout'] = 'multi'
        if 'client_timeout' in local_var_params:
            query_params.append(('client_timeout', local_var_params['client_timeout']))
            collection_formats['client_timeout'] = 'multi'
        if 'keepalive_timeout' in local_var_params:
            query_params.append(('keepalive_timeout', local_var_params['keepalive_timeout']))
            collection_formats['keepalive_timeout'] = 'multi'
        if 'transparent_client_ip_enable' in local_var_params:
            query_params.append(('transparent_client_ip_enable', local_var_params['transparent_client_ip_enable']))
        if 'enhance_l7policy_enable' in local_var_params:
            query_params.append(('enhance_l7policy_enable', local_var_params['enhance_l7policy_enable']))
        if 'member_instance_id' in local_var_params:
            query_params.append(('member_instance_id', local_var_params['member_instance_id']))
            collection_formats['member_instance_id'] = 'csv'

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
            resource_path='/v3/{project_id}/elb/listeners',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListListenersResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_load_balancers_async(self, request):
        """查询负载均衡器列表

        查询负载均衡器列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListLoadBalancers
        :type request: :class:`huaweicloudsdkelb.v3.ListLoadBalancersRequest`
        :rtype: :class:`huaweicloudsdkelb.v3.ListLoadBalancersResponse`
        """
        return self.list_load_balancers_with_http_info(request)

    def list_load_balancers_with_http_info(self, request):
        all_params = ['marker', 'limit', 'page_reverse', 'id', 'name', 'description', 'admin_state_up', 'provisioning_status', 'operating_status', 'guaranteed', 'vpc_id', 'vip_port_id', 'vip_address', 'vip_subnet_cidr_id', 'ipv6_vip_port_id', 'ipv6_vip_address', 'ipv6_vip_virsubnet_id', 'eips', 'publicips', 'availability_zone_list', 'l4_flavor_id', 'l4_scale_flavor_id', 'l7_flavor_id', 'l7_scale_flavor_id', 'billing_info', 'member_device_id', 'member_address', 'enterprise_project_id', 'ip_version', 'deletion_protection_enable', 'elb_virsubnet_type', 'autoscaling']
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
        if 'page_reverse' in local_var_params:
            query_params.append(('page_reverse', local_var_params['page_reverse']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
            collection_formats['id'] = 'multi'
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
            collection_formats['name'] = 'multi'
        if 'description' in local_var_params:
            query_params.append(('description', local_var_params['description']))
            collection_formats['description'] = 'multi'
        if 'admin_state_up' in local_var_params:
            query_params.append(('admin_state_up', local_var_params['admin_state_up']))
        if 'provisioning_status' in local_var_params:
            query_params.append(('provisioning_status', local_var_params['provisioning_status']))
            collection_formats['provisioning_status'] = 'multi'
        if 'operating_status' in local_var_params:
            query_params.append(('operating_status', local_var_params['operating_status']))
            collection_formats['operating_status'] = 'multi'
        if 'guaranteed' in local_var_params:
            query_params.append(('guaranteed', local_var_params['guaranteed']))
        if 'vpc_id' in local_var_params:
            query_params.append(('vpc_id', local_var_params['vpc_id']))
            collection_formats['vpc_id'] = 'multi'
        if 'vip_port_id' in local_var_params:
            query_params.append(('vip_port_id', local_var_params['vip_port_id']))
            collection_formats['vip_port_id'] = 'multi'
        if 'vip_address' in local_var_params:
            query_params.append(('vip_address', local_var_params['vip_address']))
            collection_formats['vip_address'] = 'multi'
        if 'vip_subnet_cidr_id' in local_var_params:
            query_params.append(('vip_subnet_cidr_id', local_var_params['vip_subnet_cidr_id']))
            collection_formats['vip_subnet_cidr_id'] = 'multi'
        if 'ipv6_vip_port_id' in local_var_params:
            query_params.append(('ipv6_vip_port_id', local_var_params['ipv6_vip_port_id']))
            collection_formats['ipv6_vip_port_id'] = 'multi'
        if 'ipv6_vip_address' in local_var_params:
            query_params.append(('ipv6_vip_address', local_var_params['ipv6_vip_address']))
            collection_formats['ipv6_vip_address'] = 'multi'
        if 'ipv6_vip_virsubnet_id' in local_var_params:
            query_params.append(('ipv6_vip_virsubnet_id', local_var_params['ipv6_vip_virsubnet_id']))
            collection_formats['ipv6_vip_virsubnet_id'] = 'multi'
        if 'eips' in local_var_params:
            query_params.append(('eips', local_var_params['eips']))
            collection_formats['eips'] = 'multi'
        if 'publicips' in local_var_params:
            query_params.append(('publicips', local_var_params['publicips']))
            collection_formats['publicips'] = 'multi'
        if 'availability_zone_list' in local_var_params:
            query_params.append(('availability_zone_list', local_var_params['availability_zone_list']))
            collection_formats['availability_zone_list'] = 'multi'
        if 'l4_flavor_id' in local_var_params:
            query_params.append(('l4_flavor_id', local_var_params['l4_flavor_id']))
            collection_formats['l4_flavor_id'] = 'multi'
        if 'l4_scale_flavor_id' in local_var_params:
            query_params.append(('l4_scale_flavor_id', local_var_params['l4_scale_flavor_id']))
            collection_formats['l4_scale_flavor_id'] = 'multi'
        if 'l7_flavor_id' in local_var_params:
            query_params.append(('l7_flavor_id', local_var_params['l7_flavor_id']))
            collection_formats['l7_flavor_id'] = 'multi'
        if 'l7_scale_flavor_id' in local_var_params:
            query_params.append(('l7_scale_flavor_id', local_var_params['l7_scale_flavor_id']))
            collection_formats['l7_scale_flavor_id'] = 'multi'
        if 'billing_info' in local_var_params:
            query_params.append(('billing_info', local_var_params['billing_info']))
            collection_formats['billing_info'] = 'multi'
        if 'member_device_id' in local_var_params:
            query_params.append(('member_device_id', local_var_params['member_device_id']))
            collection_formats['member_device_id'] = 'multi'
        if 'member_address' in local_var_params:
            query_params.append(('member_address', local_var_params['member_address']))
            collection_formats['member_address'] = 'multi'
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
            collection_formats['enterprise_project_id'] = 'multi'
        if 'ip_version' in local_var_params:
            query_params.append(('ip_version', local_var_params['ip_version']))
            collection_formats['ip_version'] = 'multi'
        if 'deletion_protection_enable' in local_var_params:
            query_params.append(('deletion_protection_enable', local_var_params['deletion_protection_enable']))
        if 'elb_virsubnet_type' in local_var_params:
            query_params.append(('elb_virsubnet_type', local_var_params['elb_virsubnet_type']))
            collection_formats['elb_virsubnet_type'] = 'csv'
        if 'autoscaling' in local_var_params:
            query_params.append(('autoscaling', local_var_params['autoscaling']))
            collection_formats['autoscaling'] = 'csv'

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
            resource_path='/v3/{project_id}/elb/loadbalancers',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListLoadBalancersResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_logtanks_async(self, request):
        """查询云日志列表

        查询云日志列表。[荷兰region不支持云日志功能，请勿使用。](tag:dt)
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListLogtanks
        :type request: :class:`huaweicloudsdkelb.v3.ListLogtanksRequest`
        :rtype: :class:`huaweicloudsdkelb.v3.ListLogtanksResponse`
        """
        return self.list_logtanks_with_http_info(request)

    def list_logtanks_with_http_info(self, request):
        all_params = ['limit', 'marker', 'page_reverse', 'enterprise_project_id', 'id', 'loadbalancer_id', 'log_group_id', 'log_topic_id']
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
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
            collection_formats['enterprise_project_id'] = 'csv'
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
            collection_formats['id'] = 'csv'
        if 'loadbalancer_id' in local_var_params:
            query_params.append(('loadbalancer_id', local_var_params['loadbalancer_id']))
            collection_formats['loadbalancer_id'] = 'csv'
        if 'log_group_id' in local_var_params:
            query_params.append(('log_group_id', local_var_params['log_group_id']))
            collection_formats['log_group_id'] = 'csv'
        if 'log_topic_id' in local_var_params:
            query_params.append(('log_topic_id', local_var_params['log_topic_id']))
            collection_formats['log_topic_id'] = 'csv'

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
            resource_path='/v3/{project_id}/elb/logtanks',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListLogtanksResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_members_async(self, request):
        """查询后端服务器列表

        Pool下的后端服务器列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListMembers
        :type request: :class:`huaweicloudsdkelb.v3.ListMembersRequest`
        :rtype: :class:`huaweicloudsdkelb.v3.ListMembersResponse`
        """
        return self.list_members_with_http_info(request)

    def list_members_with_http_info(self, request):
        all_params = ['pool_id', 'marker', 'limit', 'page_reverse', 'name', 'weight', 'admin_state_up', 'subnet_cidr_id', 'address', 'protocol_port', 'id', 'operating_status', 'enterprise_project_id', 'ip_version', 'member_type', 'instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'pool_id' in local_var_params:
            path_params['pool_id'] = local_var_params['pool_id']

        query_params = []
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'page_reverse' in local_var_params:
            query_params.append(('page_reverse', local_var_params['page_reverse']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
            collection_formats['name'] = 'multi'
        if 'weight' in local_var_params:
            query_params.append(('weight', local_var_params['weight']))
            collection_formats['weight'] = 'multi'
        if 'admin_state_up' in local_var_params:
            query_params.append(('admin_state_up', local_var_params['admin_state_up']))
        if 'subnet_cidr_id' in local_var_params:
            query_params.append(('subnet_cidr_id', local_var_params['subnet_cidr_id']))
            collection_formats['subnet_cidr_id'] = 'multi'
        if 'address' in local_var_params:
            query_params.append(('address', local_var_params['address']))
            collection_formats['address'] = 'multi'
        if 'protocol_port' in local_var_params:
            query_params.append(('protocol_port', local_var_params['protocol_port']))
            collection_formats['protocol_port'] = 'multi'
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
            collection_formats['id'] = 'multi'
        if 'operating_status' in local_var_params:
            query_params.append(('operating_status', local_var_params['operating_status']))
            collection_formats['operating_status'] = 'multi'
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
            collection_formats['enterprise_project_id'] = 'multi'
        if 'ip_version' in local_var_params:
            query_params.append(('ip_version', local_var_params['ip_version']))
            collection_formats['ip_version'] = 'multi'
        if 'member_type' in local_var_params:
            query_params.append(('member_type', local_var_params['member_type']))
            collection_formats['member_type'] = 'csv'
        if 'instance_id' in local_var_params:
            query_params.append(('instance_id', local_var_params['instance_id']))
            collection_formats['instance_id'] = 'csv'

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
            resource_path='/v3/{project_id}/elb/pools/{pool_id}/members',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListMembersResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_pools_async(self, request):
        """查询后端服务器组列表

        后端服务器组列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListPools
        :type request: :class:`huaweicloudsdkelb.v3.ListPoolsRequest`
        :rtype: :class:`huaweicloudsdkelb.v3.ListPoolsResponse`
        """
        return self.list_pools_with_http_info(request)

    def list_pools_with_http_info(self, request):
        all_params = ['marker', 'limit', 'page_reverse', 'description', 'admin_state_up', 'healthmonitor_id', 'id', 'name', 'loadbalancer_id', 'protocol', 'lb_algorithm', 'enterprise_project_id', 'ip_version', 'member_address', 'member_device_id', 'member_deletion_protection_enable', 'listener_id', 'member_instance_id', 'vpc_id', 'type']
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
        if 'page_reverse' in local_var_params:
            query_params.append(('page_reverse', local_var_params['page_reverse']))
        if 'description' in local_var_params:
            query_params.append(('description', local_var_params['description']))
            collection_formats['description'] = 'multi'
        if 'admin_state_up' in local_var_params:
            query_params.append(('admin_state_up', local_var_params['admin_state_up']))
        if 'healthmonitor_id' in local_var_params:
            query_params.append(('healthmonitor_id', local_var_params['healthmonitor_id']))
            collection_formats['healthmonitor_id'] = 'multi'
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
            collection_formats['id'] = 'multi'
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
            collection_formats['name'] = 'multi'
        if 'loadbalancer_id' in local_var_params:
            query_params.append(('loadbalancer_id', local_var_params['loadbalancer_id']))
            collection_formats['loadbalancer_id'] = 'multi'
        if 'protocol' in local_var_params:
            query_params.append(('protocol', local_var_params['protocol']))
            collection_formats['protocol'] = 'multi'
        if 'lb_algorithm' in local_var_params:
            query_params.append(('lb_algorithm', local_var_params['lb_algorithm']))
            collection_formats['lb_algorithm'] = 'multi'
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
            collection_formats['enterprise_project_id'] = 'multi'
        if 'ip_version' in local_var_params:
            query_params.append(('ip_version', local_var_params['ip_version']))
            collection_formats['ip_version'] = 'multi'
        if 'member_address' in local_var_params:
            query_params.append(('member_address', local_var_params['member_address']))
            collection_formats['member_address'] = 'multi'
        if 'member_device_id' in local_var_params:
            query_params.append(('member_device_id', local_var_params['member_device_id']))
            collection_formats['member_device_id'] = 'multi'
        if 'member_deletion_protection_enable' in local_var_params:
            query_params.append(('member_deletion_protection_enable', local_var_params['member_deletion_protection_enable']))
        if 'listener_id' in local_var_params:
            query_params.append(('listener_id', local_var_params['listener_id']))
            collection_formats['listener_id'] = 'csv'
        if 'member_instance_id' in local_var_params:
            query_params.append(('member_instance_id', local_var_params['member_instance_id']))
            collection_formats['member_instance_id'] = 'csv'
        if 'vpc_id' in local_var_params:
            query_params.append(('vpc_id', local_var_params['vpc_id']))
            collection_formats['vpc_id'] = 'csv'
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
            collection_formats['type'] = 'csv'

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
            resource_path='/v3/{project_id}/elb/pools',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListPoolsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_quota_details_async(self, request):
        """查询配额使用详情

        查询指定项目中负载均衡相关的各类资源的当前配额和已使用配额信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListQuotaDetails
        :type request: :class:`huaweicloudsdkelb.v3.ListQuotaDetailsRequest`
        :rtype: :class:`huaweicloudsdkelb.v3.ListQuotaDetailsResponse`
        """
        return self.list_quota_details_with_http_info(request)

    def list_quota_details_with_http_info(self, request):
        all_params = ['quota_key']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'quota_key' in local_var_params:
            query_params.append(('quota_key', local_var_params['quota_key']))
            collection_formats['quota_key'] = 'csv'

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
            resource_path='/v3/{project_id}/elb/quotas/details',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListQuotaDetailsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_security_policies_async(self, request):
        """查询自定义安全策略列表

        查询自定义安全策略列表。[荷兰region不支持自定义安全策略功能，请勿使用。](tag:dt)
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListSecurityPolicies
        :type request: :class:`huaweicloudsdkelb.v3.ListSecurityPoliciesRequest`
        :rtype: :class:`huaweicloudsdkelb.v3.ListSecurityPoliciesResponse`
        """
        return self.list_security_policies_with_http_info(request)

    def list_security_policies_with_http_info(self, request):
        all_params = ['marker', 'limit', 'page_reverse', 'id', 'name', 'description', 'protocols', 'ciphers']
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
        if 'page_reverse' in local_var_params:
            query_params.append(('page_reverse', local_var_params['page_reverse']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
            collection_formats['id'] = 'multi'
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
            collection_formats['name'] = 'multi'
        if 'description' in local_var_params:
            query_params.append(('description', local_var_params['description']))
            collection_formats['description'] = 'multi'
        if 'protocols' in local_var_params:
            query_params.append(('protocols', local_var_params['protocols']))
            collection_formats['protocols'] = 'csv'
        if 'ciphers' in local_var_params:
            query_params.append(('ciphers', local_var_params['ciphers']))
            collection_formats['ciphers'] = 'csv'

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
            resource_path='/v3/{project_id}/elb/security-policies',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListSecurityPoliciesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_system_security_policies_async(self, request):
        """查询系统安全策略列表

        查询系统安全策略列表。
        
        系统安全策略为预置的所有租户通用的安全策略，租户不可新增或修改。
        
        [荷兰region不支持自定义安全策略功能，请勿使用。](tag:dt)
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListSystemSecurityPolicies
        :type request: :class:`huaweicloudsdkelb.v3.ListSystemSecurityPoliciesRequest`
        :rtype: :class:`huaweicloudsdkelb.v3.ListSystemSecurityPoliciesResponse`
        """
        return self.list_system_security_policies_with_http_info(request)

    def list_system_security_policies_with_http_info(self, request):
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
            resource_path='/v3/{project_id}/elb/system-security-policies',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListSystemSecurityPoliciesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_certificate_async(self, request):
        """查询证书详情

        查询证书详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowCertificate
        :type request: :class:`huaweicloudsdkelb.v3.ShowCertificateRequest`
        :rtype: :class:`huaweicloudsdkelb.v3.ShowCertificateResponse`
        """
        return self.show_certificate_with_http_info(request)

    def show_certificate_with_http_info(self, request):
        all_params = ['certificate_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'certificate_id' in local_var_params:
            path_params['certificate_id'] = local_var_params['certificate_id']

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
            resource_path='/v3/{project_id}/elb/certificates/{certificate_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowCertificateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_flavor_async(self, request):
        """查询规格详情

        查询规格的详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowFlavor
        :type request: :class:`huaweicloudsdkelb.v3.ShowFlavorRequest`
        :rtype: :class:`huaweicloudsdkelb.v3.ShowFlavorResponse`
        """
        return self.show_flavor_with_http_info(request)

    def show_flavor_with_http_info(self, request):
        all_params = ['flavor_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'flavor_id' in local_var_params:
            path_params['flavor_id'] = local_var_params['flavor_id']

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
            resource_path='/v3/{project_id}/elb/flavors/{flavor_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowFlavorResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_health_monitor_async(self, request):
        """查询健康检查详情

        查询健康检查详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowHealthMonitor
        :type request: :class:`huaweicloudsdkelb.v3.ShowHealthMonitorRequest`
        :rtype: :class:`huaweicloudsdkelb.v3.ShowHealthMonitorResponse`
        """
        return self.show_health_monitor_with_http_info(request)

    def show_health_monitor_with_http_info(self, request):
        all_params = ['healthmonitor_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'healthmonitor_id' in local_var_params:
            path_params['healthmonitor_id'] = local_var_params['healthmonitor_id']

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
            resource_path='/v3/{project_id}/elb/healthmonitors/{healthmonitor_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowHealthMonitorResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_l7_policy_async(self, request):
        """查询转发策略详情

        查询七层转发策略详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowL7Policy
        :type request: :class:`huaweicloudsdkelb.v3.ShowL7PolicyRequest`
        :rtype: :class:`huaweicloudsdkelb.v3.ShowL7PolicyResponse`
        """
        return self.show_l7_policy_with_http_info(request)

    def show_l7_policy_with_http_info(self, request):
        all_params = ['l7policy_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'l7policy_id' in local_var_params:
            path_params['l7policy_id'] = local_var_params['l7policy_id']

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
            resource_path='/v3/{project_id}/elb/l7policies/{l7policy_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowL7PolicyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_l7_rule_async(self, request):
        """查询转发规则详情

        查询七层转发规则详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowL7Rule
        :type request: :class:`huaweicloudsdkelb.v3.ShowL7RuleRequest`
        :rtype: :class:`huaweicloudsdkelb.v3.ShowL7RuleResponse`
        """
        return self.show_l7_rule_with_http_info(request)

    def show_l7_rule_with_http_info(self, request):
        all_params = ['l7policy_id', 'l7rule_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'l7policy_id' in local_var_params:
            path_params['l7policy_id'] = local_var_params['l7policy_id']
        if 'l7rule_id' in local_var_params:
            path_params['l7rule_id'] = local_var_params['l7rule_id']

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
            resource_path='/v3/{project_id}/elb/l7policies/{l7policy_id}/rules/{l7rule_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowL7RuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_listener_async(self, request):
        """查询监听器详情

        监听器详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowListener
        :type request: :class:`huaweicloudsdkelb.v3.ShowListenerRequest`
        :rtype: :class:`huaweicloudsdkelb.v3.ShowListenerResponse`
        """
        return self.show_listener_with_http_info(request)

    def show_listener_with_http_info(self, request):
        all_params = ['listener_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'listener_id' in local_var_params:
            path_params['listener_id'] = local_var_params['listener_id']

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
            resource_path='/v3/{project_id}/elb/listeners/{listener_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowListenerResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_load_balancer_async(self, request):
        """查询负载均衡器详情

        查询负载均衡器详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowLoadBalancer
        :type request: :class:`huaweicloudsdkelb.v3.ShowLoadBalancerRequest`
        :rtype: :class:`huaweicloudsdkelb.v3.ShowLoadBalancerResponse`
        """
        return self.show_load_balancer_with_http_info(request)

    def show_load_balancer_with_http_info(self, request):
        all_params = ['loadbalancer_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'loadbalancer_id' in local_var_params:
            path_params['loadbalancer_id'] = local_var_params['loadbalancer_id']

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
            resource_path='/v3/{project_id}/elb/loadbalancers/{loadbalancer_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowLoadBalancerResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_load_balancer_status_async(self, request):
        """查询负载均衡器状态树

        查询负载均衡器状态树，包括负载均衡器及其关联的子资源的状态信息。
        注意：该接口中的operating_status不一定与对应资源的operating_status相同。
        如：当Member的admin_state_up&#x3D;false且operating_status&#x3D;OFFLINE时，
        该接口返回member的operating_status&#x3D;DISABLE。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowLoadBalancerStatus
        :type request: :class:`huaweicloudsdkelb.v3.ShowLoadBalancerStatusRequest`
        :rtype: :class:`huaweicloudsdkelb.v3.ShowLoadBalancerStatusResponse`
        """
        return self.show_load_balancer_status_with_http_info(request)

    def show_load_balancer_status_with_http_info(self, request):
        all_params = ['loadbalancer_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'loadbalancer_id' in local_var_params:
            path_params['loadbalancer_id'] = local_var_params['loadbalancer_id']

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
            resource_path='/v3/{project_id}/elb/loadbalancers/{loadbalancer_id}/statuses',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowLoadBalancerStatusResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_logtank_async(self, request):
        """查询云日志详情

        云日志详情。[荷兰region不支持云日志功能，请勿使用。](tag:dt)
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowLogtank
        :type request: :class:`huaweicloudsdkelb.v3.ShowLogtankRequest`
        :rtype: :class:`huaweicloudsdkelb.v3.ShowLogtankResponse`
        """
        return self.show_logtank_with_http_info(request)

    def show_logtank_with_http_info(self, request):
        all_params = ['logtank_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'logtank_id' in local_var_params:
            path_params['logtank_id'] = local_var_params['logtank_id']

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
            resource_path='/v3/{project_id}/elb/logtanks/{logtank_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowLogtankResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_member_async(self, request):
        """查询后端服务器详情

        后端服务器详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowMember
        :type request: :class:`huaweicloudsdkelb.v3.ShowMemberRequest`
        :rtype: :class:`huaweicloudsdkelb.v3.ShowMemberResponse`
        """
        return self.show_member_with_http_info(request)

    def show_member_with_http_info(self, request):
        all_params = ['pool_id', 'member_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'pool_id' in local_var_params:
            path_params['pool_id'] = local_var_params['pool_id']
        if 'member_id' in local_var_params:
            path_params['member_id'] = local_var_params['member_id']

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
            resource_path='/v3/{project_id}/elb/pools/{pool_id}/members/{member_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowMemberResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_pool_async(self, request):
        """查询后端服务器组详情

        后端服务器组详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowPool
        :type request: :class:`huaweicloudsdkelb.v3.ShowPoolRequest`
        :rtype: :class:`huaweicloudsdkelb.v3.ShowPoolResponse`
        """
        return self.show_pool_with_http_info(request)

    def show_pool_with_http_info(self, request):
        all_params = ['pool_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'pool_id' in local_var_params:
            path_params['pool_id'] = local_var_params['pool_id']

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
            resource_path='/v3/{project_id}/elb/pools/{pool_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowPoolResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_quota_async(self, request):
        """查询配额详情

        查询指定项目中负载均衡相关的各类资源的当前配额。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowQuota
        :type request: :class:`huaweicloudsdkelb.v3.ShowQuotaRequest`
        :rtype: :class:`huaweicloudsdkelb.v3.ShowQuotaResponse`
        """
        return self.show_quota_with_http_info(request)

    def show_quota_with_http_info(self, request):
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
            resource_path='/v3/{project_id}/elb/quotas',
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

    def show_security_policy_async(self, request):
        """查询自定义安全策略详情

        查询自定义安全策略详情。[荷兰region不支持自定义安全策略功能，请勿使用。](tag:dt)
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowSecurityPolicy
        :type request: :class:`huaweicloudsdkelb.v3.ShowSecurityPolicyRequest`
        :rtype: :class:`huaweicloudsdkelb.v3.ShowSecurityPolicyResponse`
        """
        return self.show_security_policy_with_http_info(request)

    def show_security_policy_with_http_info(self, request):
        all_params = ['security_policy_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'security_policy_id' in local_var_params:
            path_params['security_policy_id'] = local_var_params['security_policy_id']

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
            resource_path='/v3/{project_id}/elb/security-policies/{security_policy_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowSecurityPolicyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_certificate_async(self, request):
        """更新证书

        更新证书。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateCertificate
        :type request: :class:`huaweicloudsdkelb.v3.UpdateCertificateRequest`
        :rtype: :class:`huaweicloudsdkelb.v3.UpdateCertificateResponse`
        """
        return self.update_certificate_with_http_info(request)

    def update_certificate_with_http_info(self, request):
        all_params = ['certificate_id', 'update_certificate_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'certificate_id' in local_var_params:
            path_params['certificate_id'] = local_var_params['certificate_id']

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
            resource_path='/v3/{project_id}/elb/certificates/{certificate_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateCertificateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_health_monitor_async(self, request):
        """更新健康检查

        更新健康检查。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateHealthMonitor
        :type request: :class:`huaweicloudsdkelb.v3.UpdateHealthMonitorRequest`
        :rtype: :class:`huaweicloudsdkelb.v3.UpdateHealthMonitorResponse`
        """
        return self.update_health_monitor_with_http_info(request)

    def update_health_monitor_with_http_info(self, request):
        all_params = ['healthmonitor_id', 'update_health_monitor_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'healthmonitor_id' in local_var_params:
            path_params['healthmonitor_id'] = local_var_params['healthmonitor_id']

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
            resource_path='/v3/{project_id}/elb/healthmonitors/{healthmonitor_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateHealthMonitorResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_l7_policy_async(self, request):
        """更新转发策略

        更新七层转发策略。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateL7Policy
        :type request: :class:`huaweicloudsdkelb.v3.UpdateL7PolicyRequest`
        :rtype: :class:`huaweicloudsdkelb.v3.UpdateL7PolicyResponse`
        """
        return self.update_l7_policy_with_http_info(request)

    def update_l7_policy_with_http_info(self, request):
        all_params = ['l7policy_id', 'update_l7_policy_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'l7policy_id' in local_var_params:
            path_params['l7policy_id'] = local_var_params['l7policy_id']

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
            resource_path='/v3/{project_id}/elb/l7policies/{l7policy_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateL7PolicyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_l7_rule_async(self, request):
        """更新转发规则

        更新七层转发规则。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateL7Rule
        :type request: :class:`huaweicloudsdkelb.v3.UpdateL7RuleRequest`
        :rtype: :class:`huaweicloudsdkelb.v3.UpdateL7RuleResponse`
        """
        return self.update_l7_rule_with_http_info(request)

    def update_l7_rule_with_http_info(self, request):
        all_params = ['l7policy_id', 'l7rule_id', 'update_l7_rule_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'l7policy_id' in local_var_params:
            path_params['l7policy_id'] = local_var_params['l7policy_id']
        if 'l7rule_id' in local_var_params:
            path_params['l7rule_id'] = local_var_params['l7rule_id']

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
            resource_path='/v3/{project_id}/elb/l7policies/{l7policy_id}/rules/{l7rule_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateL7RuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_listener_async(self, request):
        """更新监听器

        更新监听器。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateListener
        :type request: :class:`huaweicloudsdkelb.v3.UpdateListenerRequest`
        :rtype: :class:`huaweicloudsdkelb.v3.UpdateListenerResponse`
        """
        return self.update_listener_with_http_info(request)

    def update_listener_with_http_info(self, request):
        all_params = ['listener_id', 'update_listener_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'listener_id' in local_var_params:
            path_params['listener_id'] = local_var_params['listener_id']

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
            resource_path='/v3/{project_id}/elb/listeners/{listener_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateListenerResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_load_balancer_async(self, request):
        """更新负载均衡器

        更新负载均衡器。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateLoadBalancer
        :type request: :class:`huaweicloudsdkelb.v3.UpdateLoadBalancerRequest`
        :rtype: :class:`huaweicloudsdkelb.v3.UpdateLoadBalancerResponse`
        """
        return self.update_load_balancer_with_http_info(request)

    def update_load_balancer_with_http_info(self, request):
        all_params = ['loadbalancer_id', 'update_load_balancer_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'loadbalancer_id' in local_var_params:
            path_params['loadbalancer_id'] = local_var_params['loadbalancer_id']

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
            resource_path='/v3/{project_id}/elb/loadbalancers/{loadbalancer_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateLoadBalancerResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_logtank_async(self, request):
        """更新云日志

        更新云日志。[荷兰region不支持云日志功能，请勿使用。](tag:dt)
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateLogtank
        :type request: :class:`huaweicloudsdkelb.v3.UpdateLogtankRequest`
        :rtype: :class:`huaweicloudsdkelb.v3.UpdateLogtankResponse`
        """
        return self.update_logtank_with_http_info(request)

    def update_logtank_with_http_info(self, request):
        all_params = ['logtank_id', 'update_logtank_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'logtank_id' in local_var_params:
            path_params['logtank_id'] = local_var_params['logtank_id']

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
            resource_path='/v3/{project_id}/elb/logtanks/{logtank_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateLogtankResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_member_async(self, request):
        """更新后端服务器

        更新后端服务器。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateMember
        :type request: :class:`huaweicloudsdkelb.v3.UpdateMemberRequest`
        :rtype: :class:`huaweicloudsdkelb.v3.UpdateMemberResponse`
        """
        return self.update_member_with_http_info(request)

    def update_member_with_http_info(self, request):
        all_params = ['member_id', 'pool_id', 'update_member_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'member_id' in local_var_params:
            path_params['member_id'] = local_var_params['member_id']
        if 'pool_id' in local_var_params:
            path_params['pool_id'] = local_var_params['pool_id']

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
            resource_path='/v3/{project_id}/elb/pools/{pool_id}/members/{member_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateMemberResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_pool_async(self, request):
        """更新后端服务器组

        更新后端服务器组。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdatePool
        :type request: :class:`huaweicloudsdkelb.v3.UpdatePoolRequest`
        :rtype: :class:`huaweicloudsdkelb.v3.UpdatePoolResponse`
        """
        return self.update_pool_with_http_info(request)

    def update_pool_with_http_info(self, request):
        all_params = ['pool_id', 'update_pool_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'pool_id' in local_var_params:
            path_params['pool_id'] = local_var_params['pool_id']

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
            resource_path='/v3/{project_id}/elb/pools/{pool_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdatePoolResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_security_policy_async(self, request):
        """更新自定义安全策略

        更新自定义安全策略。[荷兰region不支持自定义安全策略功能，请勿使用。](tag:dt)
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateSecurityPolicy
        :type request: :class:`huaweicloudsdkelb.v3.UpdateSecurityPolicyRequest`
        :rtype: :class:`huaweicloudsdkelb.v3.UpdateSecurityPolicyResponse`
        """
        return self.update_security_policy_with_http_info(request)

    def update_security_policy_with_http_info(self, request):
        all_params = ['security_policy_id', 'update_security_policy_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'security_policy_id' in local_var_params:
            path_params['security_policy_id'] = local_var_params['security_policy_id']

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
            resource_path='/v3/{project_id}/elb/security-policies/{security_policy_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateSecurityPolicyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_api_versions_async(self, request):
        """查询API版本列表信息

        返回ELB当前所有可用的API版本。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListApiVersions
        :type request: :class:`huaweicloudsdkelb.v3.ListApiVersionsRequest`
        :rtype: :class:`huaweicloudsdkelb.v3.ListApiVersionsResponse`
        """
        return self.list_api_versions_with_http_info(request)

    def list_api_versions_with_http_info(self, request):
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
            resource_path='/versions',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListApiVersionsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_delete_ip_list_async(self, request):
        """删除IP地址组的IP列表项

        批量删除IP地址组的IP列表信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchDeleteIpList
        :type request: :class:`huaweicloudsdkelb.v3.BatchDeleteIpListRequest`
        :rtype: :class:`huaweicloudsdkelb.v3.BatchDeleteIpListResponse`
        """
        return self.batch_delete_ip_list_with_http_info(request)

    def batch_delete_ip_list_with_http_info(self, request):
        all_params = ['ipgroup_id', 'batch_delete_ip_list_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ipgroup_id' in local_var_params:
            path_params['ipgroup_id'] = local_var_params['ipgroup_id']

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
            resource_path='/v3/{project_id}/elb/ipgroups/{ipgroup_id}/iplist/batch-delete',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchDeleteIpListResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def count_preoccupy_ip_num_async(self, request):
        """计算预占IP数

        计算以下几种场景的预占用IP数量：
        
        - 计算创建LB的第一个七层监听器后总占用IP数量：
        传入loadbalancer_id、l7_flavor_id为空、ip_target_enable不传或为false。
        
        - 计算LB规格变更或开启跨VPC后总占用IP数量：
        传入参数loadbalancer_id，及l7_flavor_id不为空或ip_target_enable为true。
        
        - 计算创建LB所需IP数量：传入参数availability_zone_id，
        及可选参数l7_flavor_id、ip_target_enable、ip_version，不能传loadbalancer_id。
        
        说明：
        - 计算出来的预占IP数大于等于最终实际占用的IP数。
        - 总占用IP数量，即整个LB所占用的IP数量。
        
        [不支持传入l7_flavor_id](tag:fcs)
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CountPreoccupyIpNum
        :type request: :class:`huaweicloudsdkelb.v3.CountPreoccupyIpNumRequest`
        :rtype: :class:`huaweicloudsdkelb.v3.CountPreoccupyIpNumResponse`
        """
        return self.count_preoccupy_ip_num_with_http_info(request)

    def count_preoccupy_ip_num_with_http_info(self, request):
        all_params = ['l7_flavor_id', 'ip_target_enable', 'ip_version', 'loadbalancer_id', 'availability_zone_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'l7_flavor_id' in local_var_params:
            query_params.append(('l7_flavor_id', local_var_params['l7_flavor_id']))
        if 'ip_target_enable' in local_var_params:
            query_params.append(('ip_target_enable', local_var_params['ip_target_enable']))
        if 'ip_version' in local_var_params:
            query_params.append(('ip_version', local_var_params['ip_version']))
        if 'loadbalancer_id' in local_var_params:
            query_params.append(('loadbalancer_id', local_var_params['loadbalancer_id']))
        if 'availability_zone_id' in local_var_params:
            query_params.append(('availability_zone_id', local_var_params['availability_zone_id']))
            collection_formats['availability_zone_id'] = 'multi'

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
            resource_path='/v3/{project_id}/elb/preoccupy-ip-num',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CountPreoccupyIpNumResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_ip_group_async(self, request):
        """创建IP地址组

        创建IP地址组。输入的ip可为ip地址或者CIDR子网，支持IPV4和IPV6。
        
        需要注意0.0.0.0与0.0.0.0/32视为重复，0:0:0:0:0:0:0:1与::1与::1/128视为重复，只会保存其中一个。
        
        [荷兰region不支持IP地址组功能，请勿使用。](tag:dt)
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateIpGroup
        :type request: :class:`huaweicloudsdkelb.v3.CreateIpGroupRequest`
        :rtype: :class:`huaweicloudsdkelb.v3.CreateIpGroupResponse`
        """
        return self.create_ip_group_with_http_info(request)

    def create_ip_group_with_http_info(self, request):
        all_params = ['create_ip_group_request_body']
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
            resource_path='/v3/{project_id}/elb/ipgroups',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateIpGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_ip_group_async(self, request):
        """删除IP地址组

        删除ip地址组。[荷兰region不支持IP地址组功能，请勿使用。](tag:dt)
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteIpGroup
        :type request: :class:`huaweicloudsdkelb.v3.DeleteIpGroupRequest`
        :rtype: :class:`huaweicloudsdkelb.v3.DeleteIpGroupResponse`
        """
        return self.delete_ip_group_with_http_info(request)

    def delete_ip_group_with_http_info(self, request):
        all_params = ['ipgroup_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ipgroup_id' in local_var_params:
            path_params['ipgroup_id'] = local_var_params['ipgroup_id']

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
            resource_path='/v3/{project_id}/elb/ipgroups/{ipgroup_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteIpGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_ip_groups_async(self, request):
        """查询IP地址组列表

        查询IP地址组列表。[荷兰region不支持IP地址组功能，请勿使用。](tag:dt)
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListIpGroups
        :type request: :class:`huaweicloudsdkelb.v3.ListIpGroupsRequest`
        :rtype: :class:`huaweicloudsdkelb.v3.ListIpGroupsResponse`
        """
        return self.list_ip_groups_with_http_info(request)

    def list_ip_groups_with_http_info(self, request):
        all_params = ['marker', 'limit', 'page_reverse', 'id', 'name', 'description', 'ip_list']
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
        if 'page_reverse' in local_var_params:
            query_params.append(('page_reverse', local_var_params['page_reverse']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
            collection_formats['id'] = 'multi'
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
            collection_formats['name'] = 'multi'
        if 'description' in local_var_params:
            query_params.append(('description', local_var_params['description']))
            collection_formats['description'] = 'multi'
        if 'ip_list' in local_var_params:
            query_params.append(('ip_list', local_var_params['ip_list']))
            collection_formats['ip_list'] = 'multi'

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
            resource_path='/v3/{project_id}/elb/ipgroups',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListIpGroupsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_ip_group_async(self, request):
        """查询IP地址组详情

        获取IP地址组详情。[荷兰region不支持IP地址组功能，请勿使用。](tag:dt)
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowIpGroup
        :type request: :class:`huaweicloudsdkelb.v3.ShowIpGroupRequest`
        :rtype: :class:`huaweicloudsdkelb.v3.ShowIpGroupResponse`
        """
        return self.show_ip_group_with_http_info(request)

    def show_ip_group_with_http_info(self, request):
        all_params = ['ipgroup_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ipgroup_id' in local_var_params:
            path_params['ipgroup_id'] = local_var_params['ipgroup_id']

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
            resource_path='/v3/{project_id}/elb/ipgroups/{ipgroup_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowIpGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_ip_group_async(self, request):
        """更新IP地址组

        更新IP地址组，只支持全量更新IP。即IP地址组中的ip_list将被全量覆盖，不在请求参数中的IP地址将被移除。
        输入的ip可为ip地址或者CIDR子网，支持IPV4和IPV6。
        
        需要注意0.0.0.0与0.0.0.0/32视为重复，0:0:0:0:0:0:0:1与::1与::1/128视为重复，只会保存其中一个。
        
        [荷兰region不支持IP地址组功能，请勿使用。](tag:dt)
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateIpGroup
        :type request: :class:`huaweicloudsdkelb.v3.UpdateIpGroupRequest`
        :rtype: :class:`huaweicloudsdkelb.v3.UpdateIpGroupResponse`
        """
        return self.update_ip_group_with_http_info(request)

    def update_ip_group_with_http_info(self, request):
        all_params = ['ipgroup_id', 'update_ip_group_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ipgroup_id' in local_var_params:
            path_params['ipgroup_id'] = local_var_params['ipgroup_id']

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
            resource_path='/v3/{project_id}/elb/ipgroups/{ipgroup_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateIpGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_ip_list_async(self, request):
        """更新IP地址组的IP列表项

        更新IP地址组的IP列表信息。[荷兰region不支持该API](tag:dt,dt_test)
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateIpList
        :type request: :class:`huaweicloudsdkelb.v3.UpdateIpListRequest`
        :rtype: :class:`huaweicloudsdkelb.v3.UpdateIpListResponse`
        """
        return self.update_ip_list_with_http_info(request)

    def update_ip_list_with_http_info(self, request):
        all_params = ['ipgroup_id', 'update_ip_list_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ipgroup_id' in local_var_params:
            path_params['ipgroup_id'] = local_var_params['ipgroup_id']

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
            resource_path='/v3/{project_id}/elb/ipgroups/{ipgroup_id}/iplist/create-or-update',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateIpListResponse',
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

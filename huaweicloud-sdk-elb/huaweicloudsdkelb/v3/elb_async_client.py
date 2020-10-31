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
        super(ElbAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkelb.v3.model")
        self.preset_headers = {'User-Agent': 'HuaweiCloud-SDK-Python'}

    @staticmethod
    def new_builder(clazz):
        return ClientBuilder(clazz)

    def create_certificate_async(self, request):
        """创建证书

        创建证书。

        :param CreateCertificateRequest request
        :return: CreateCertificateResponse
        """
        return self.create_certificate_with_http_info(request)

    def create_certificate_with_http_info(self, request):
        """创建证书

        创建证书。

        :param CreateCertificateRequest request
        :return: CreateCertificateResponse
        """

        all_params = ['create_certificate_request_body']
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
            response_type='CreateCertificateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_health_monitor_async(self, request):
        """创建健康检查

        创建健康检查。

        :param CreateHealthMonitorRequest request
        :return: CreateHealthMonitorResponse
        """
        return self.create_health_monitor_with_http_info(request)

    def create_health_monitor_with_http_info(self, request):
        """创建健康检查

        创建健康检查。

        :param CreateHealthMonitorRequest request
        :return: CreateHealthMonitorResponse
        """

        all_params = ['create_health_monitor_request_body']
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
            response_type='CreateHealthMonitorResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_l7_policy_async(self, request):
        """创建转发策略

        创建转发策略.

        :param CreateL7PolicyRequest request
        :return: CreateL7PolicyResponse
        """
        return self.create_l7_policy_with_http_info(request)

    def create_l7_policy_with_http_info(self, request):
        """创建转发策略

        创建转发策略.

        :param CreateL7PolicyRequest request
        :return: CreateL7PolicyResponse
        """

        all_params = ['create_l7_policy_request_body']
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
            response_type='CreateL7PolicyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_l7_rule_async(self, request):
        """创建转发规则

        创建转发规则。

        :param CreateL7RuleRequest request
        :return: CreateL7RuleResponse
        """
        return self.create_l7_rule_with_http_info(request)

    def create_l7_rule_with_http_info(self, request):
        """创建转发规则

        创建转发规则。

        :param CreateL7RuleRequest request
        :return: CreateL7RuleResponse
        """

        all_params = ['l7policy_id', 'create_l7_rule_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='CreateL7RuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_listener_async(self, request):
        """创建监听器

        ElbV3 创建监听器。

        :param CreateListenerRequest request
        :return: CreateListenerResponse
        """
        return self.create_listener_with_http_info(request)

    def create_listener_with_http_info(self, request):
        """创建监听器

        ElbV3 创建监听器。

        :param CreateListenerRequest request
        :return: CreateListenerResponse
        """

        all_params = ['create_listener_request_body']
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
            response_type='CreateListenerResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_load_balancer_async(self, request):
        """创建负载均衡器

        创建负载均衡器。 1.创建公网负载均衡器的场合，需要传入vpc_id。 2.创建内网负载均衡器的场合，需要传入vip_subnet_cidr_id。 3.创建内网双栈负载均衡器的场合，需要传入ipv6_vip_virsubnet_id。  关联有已有公网ip地址，需要传入publicip_ids 新建公网ip地址，需要传入publicip 包括IPV4私网类型，IPV4公网类型，IPV6私网，IPV6公网

        :param CreateLoadBalancerRequest request
        :return: CreateLoadBalancerResponse
        """
        return self.create_load_balancer_with_http_info(request)

    def create_load_balancer_with_http_info(self, request):
        """创建负载均衡器

        创建负载均衡器。 1.创建公网负载均衡器的场合，需要传入vpc_id。 2.创建内网负载均衡器的场合，需要传入vip_subnet_cidr_id。 3.创建内网双栈负载均衡器的场合，需要传入ipv6_vip_virsubnet_id。  关联有已有公网ip地址，需要传入publicip_ids 新建公网ip地址，需要传入publicip 包括IPV4私网类型，IPV4公网类型，IPV6私网，IPV6公网

        :param CreateLoadBalancerRequest request
        :return: CreateLoadBalancerResponse
        """

        all_params = ['create_load_balancer_request_body']
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
            response_type='CreateLoadBalancerResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_member_async(self, request):
        """创建后端服务器

        创建后端服务器。

        :param CreateMemberRequest request
        :return: CreateMemberResponse
        """
        return self.create_member_with_http_info(request)

    def create_member_with_http_info(self, request):
        """创建后端服务器

        创建后端服务器。

        :param CreateMemberRequest request
        :return: CreateMemberResponse
        """

        all_params = ['pool_id', 'create_member_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='CreateMemberResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_pool_async(self, request):
        """创建后端服务器组

        创建后端服务器组。

        :param CreatePoolRequest request
        :return: CreatePoolResponse
        """
        return self.create_pool_with_http_info(request)

    def create_pool_with_http_info(self, request):
        """创建后端服务器组

        创建后端服务器组。

        :param CreatePoolRequest request
        :return: CreatePoolResponse
        """

        all_params = ['create_pool_request_body']
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
            response_type='CreatePoolResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_certificate_async(self, request):
        """删除证书

        删除SSL证书。

        :param DeleteCertificateRequest request
        :return: DeleteCertificateResponse
        """
        return self.delete_certificate_with_http_info(request)

    def delete_certificate_with_http_info(self, request):
        """删除证书

        删除SSL证书。

        :param DeleteCertificateRequest request
        :return: DeleteCertificateResponse
        """

        all_params = ['certificate_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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


        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/elb/certificates/{certificate_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteCertificateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_health_monitor_async(self, request):
        """删除健康检查

        删除健康检查。

        :param DeleteHealthMonitorRequest request
        :return: DeleteHealthMonitorResponse
        """
        return self.delete_health_monitor_with_http_info(request)

    def delete_health_monitor_with_http_info(self, request):
        """删除健康检查

        删除健康检查。

        :param DeleteHealthMonitorRequest request
        :return: DeleteHealthMonitorResponse
        """

        all_params = ['healthmonitor_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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


        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/elb/healthmonitors/{healthmonitor_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteHealthMonitorResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_l7_policy_async(self, request):
        """删除转发策略

        删除转发策略。

        :param DeleteL7PolicyRequest request
        :return: DeleteL7PolicyResponse
        """
        return self.delete_l7_policy_with_http_info(request)

    def delete_l7_policy_with_http_info(self, request):
        """删除转发策略

        删除转发策略。

        :param DeleteL7PolicyRequest request
        :return: DeleteL7PolicyResponse
        """

        all_params = ['l7policy_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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


        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/elb/l7policies/{l7policy_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteL7PolicyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_l7_rule_async(self, request):
        """删除转发规则

        删除转发规则。

        :param DeleteL7RuleRequest request
        :return: DeleteL7RuleResponse
        """
        return self.delete_l7_rule_with_http_info(request)

    def delete_l7_rule_with_http_info(self, request):
        """删除转发规则

        删除转发规则。

        :param DeleteL7RuleRequest request
        :return: DeleteL7RuleResponse
        """

        all_params = ['l7policy_id', 'l7rule_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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


        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/elb/l7policies/{l7policy_id}/rules/{l7rule_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteL7RuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_listener_async(self, request):
        """删除监听器

        删除监听器。

        :param DeleteListenerRequest request
        :return: DeleteListenerResponse
        """
        return self.delete_listener_with_http_info(request)

    def delete_listener_with_http_info(self, request):
        """删除监听器

        删除监听器。

        :param DeleteListenerRequest request
        :return: DeleteListenerResponse
        """

        all_params = ['listener_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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


        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/elb/listeners/{listener_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteListenerResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_load_balancer_async(self, request):
        """删除负载均衡器

        删除负载均衡器。

        :param DeleteLoadBalancerRequest request
        :return: DeleteLoadBalancerResponse
        """
        return self.delete_load_balancer_with_http_info(request)

    def delete_load_balancer_with_http_info(self, request):
        """删除负载均衡器

        删除负载均衡器。

        :param DeleteLoadBalancerRequest request
        :return: DeleteLoadBalancerResponse
        """

        all_params = ['loadbalancer_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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


        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/elb/loadbalancers/{loadbalancer_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteLoadBalancerResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_member_async(self, request):
        """删除后端服务器

        删除后端服务器。

        :param DeleteMemberRequest request
        :return: DeleteMemberResponse
        """
        return self.delete_member_with_http_info(request)

    def delete_member_with_http_info(self, request):
        """删除后端服务器

        删除后端服务器。

        :param DeleteMemberRequest request
        :return: DeleteMemberResponse
        """

        all_params = ['member_id', 'pool_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/elb/pools/{pool_id}/members/{member_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteMemberResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_pool_async(self, request):
        """删除后端服务器组

        删除后端服务器组。

        :param DeletePoolRequest request
        :return: DeletePoolResponse
        """
        return self.delete_pool_with_http_info(request)

    def delete_pool_with_http_info(self, request):
        """删除后端服务器组

        删除后端服务器组。

        :param DeletePoolRequest request
        :return: DeletePoolResponse
        """

        all_params = ['pool_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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


        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/elb/pools/{pool_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeletePoolResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_availability_zones_async(self, request):
        """查询可用区列表

        返回租户创建LB时可使用的可用区列表情况。  返回的数据类型是可用区集合的列表，比如列表 [ [az1,az2],  [az2, az3] ] ，有两个可用区集合。在创建负载均衡器时，可以选择创建在多个可用区，但所选的多个可用区必须同属于其中一个可用区集合，如可以选择 az2和az3，但不能选择 az1和az3。

        :param ListAvailabilityZonesRequest request
        :return: ListAvailabilityZonesResponse
        """
        return self.list_availability_zones_with_http_info(request)

    def list_availability_zones_with_http_info(self, request):
        """查询可用区列表

        返回租户创建LB时可使用的可用区列表情况。  返回的数据类型是可用区集合的列表，比如列表 [ [az1,az2],  [az2, az3] ] ，有两个可用区集合。在创建负载均衡器时，可以选择创建在多个可用区，但所选的多个可用区必须同属于其中一个可用区集合，如可以选择 az2和az3，但不能选择 az1和az3。

        :param ListAvailabilityZonesRequest request
        :return: ListAvailabilityZonesResponse
        """

        all_params = []
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
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/elb/availability-zones',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListAvailabilityZonesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_certificates_async(self, request):
        """证书列表

        查询SSL证书列表。

        :param ListCertificatesRequest request
        :return: ListCertificatesResponse
        """
        return self.list_certificates_with_http_info(request)

    def list_certificates_with_http_info(self, request):
        """证书列表

        查询SSL证书列表。

        :param ListCertificatesRequest request
        :return: ListCertificatesResponse
        """

        all_params = ['admin_state_up', 'description', 'domain', 'id', 'limit', 'marker', 'name', 'page_reverse', 'type']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'admin_state_up' in local_var_params:
            query_params.append(('admin_state_up', local_var_params['admin_state_up']))
        if 'description' in local_var_params:
            query_params.append(('description', local_var_params['description']))
            collection_formats['description'] = 'multi'
        if 'domain' in local_var_params:
            query_params.append(('domain', local_var_params['domain']))
            collection_formats['domain'] = 'multi'
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
            collection_formats['id'] = 'multi'
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
            collection_formats['name'] = 'multi'
        if 'page_reverse' in local_var_params:
            query_params.append(('page_reverse', local_var_params['page_reverse']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
            collection_formats['type'] = 'multi'

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/elb/certificates',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListCertificatesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_flavors_async(self, request):
        """查询规格列表

        查询所有的规格。

        :param ListFlavorsRequest request
        :return: ListFlavorsResponse
        """
        return self.list_flavors_with_http_info(request)

    def list_flavors_with_http_info(self, request):
        """查询规格列表

        查询所有的规格。

        :param ListFlavorsRequest request
        :return: ListFlavorsResponse
        """

        all_params = ['id', 'limit', 'marker', 'name', 'page_reverse', 'shared', 'type']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
            collection_formats['id'] = 'multi'
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
            collection_formats['name'] = 'multi'
        if 'page_reverse' in local_var_params:
            query_params.append(('page_reverse', local_var_params['page_reverse']))
        if 'shared' in local_var_params:
            query_params.append(('shared', local_var_params['shared']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
            collection_formats['type'] = 'multi'

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/elb/flavors',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListFlavorsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_health_monitors_async(self, request):
        """查询健康检查列表

        健康检查列表。

        :param ListHealthMonitorsRequest request
        :return: ListHealthMonitorsResponse
        """
        return self.list_health_monitors_with_http_info(request)

    def list_health_monitors_with_http_info(self, request):
        """查询健康检查列表

        健康检查列表。

        :param ListHealthMonitorsRequest request
        :return: ListHealthMonitorsResponse
        """

        all_params = ['admin_state_up', 'delay', 'domain_name', 'enterprise_project_id', 'expected_codes', 'http_method', 'id', 'limit', 'marker', 'max_retries', 'max_retries_down', 'monitor_port', 'name', 'page_reverse', 'timeout', 'type', 'url_path']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'admin_state_up' in local_var_params:
            query_params.append(('admin_state_up', local_var_params['admin_state_up']))
        if 'delay' in local_var_params:
            query_params.append(('delay', local_var_params['delay']))
            collection_formats['delay'] = 'multi'
        if 'domain_name' in local_var_params:
            query_params.append(('domain_name', local_var_params['domain_name']))
            collection_formats['domain_name'] = 'multi'
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
            collection_formats['enterprise_project_id'] = 'multi'
        if 'expected_codes' in local_var_params:
            query_params.append(('expected_codes', local_var_params['expected_codes']))
            collection_formats['expected_codes'] = 'multi'
        if 'http_method' in local_var_params:
            query_params.append(('http_method', local_var_params['http_method']))
            collection_formats['http_method'] = 'multi'
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
            collection_formats['id'] = 'multi'
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'max_retries' in local_var_params:
            query_params.append(('max_retries', local_var_params['max_retries']))
            collection_formats['max_retries'] = 'multi'
        if 'max_retries_down' in local_var_params:
            query_params.append(('max_retries_down', local_var_params['max_retries_down']))
            collection_formats['max_retries_down'] = 'multi'
        if 'monitor_port' in local_var_params:
            query_params.append(('monitor_port', local_var_params['monitor_port']))
            collection_formats['monitor_port'] = 'multi'
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
            collection_formats['name'] = 'multi'
        if 'page_reverse' in local_var_params:
            query_params.append(('page_reverse', local_var_params['page_reverse']))
        if 'timeout' in local_var_params:
            query_params.append(('timeout', local_var_params['timeout']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
            collection_formats['type'] = 'multi'
        if 'url_path' in local_var_params:
            query_params.append(('url_path', local_var_params['url_path']))
            collection_formats['url_path'] = 'multi'

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/elb/healthmonitors',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListHealthMonitorsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_l7_policies_async(self, request):
        """查询转发策略列表

        查询转发策略列表。

        :param ListL7PoliciesRequest request
        :return: ListL7PoliciesResponse
        """
        return self.list_l7_policies_with_http_info(request)

    def list_l7_policies_with_http_info(self, request):
        """查询转发策略列表

        查询转发策略列表。

        :param ListL7PoliciesRequest request
        :return: ListL7PoliciesResponse
        """

        all_params = ['action', 'admin_state_up', 'description', 'display_all_rules', 'enterprise_project_id', 'id', 'limit', 'listener_id', 'marker', 'name', 'page_reverse', 'position', 'provisioning_status', 'redirect_listener_id', 'redirect_pool_id', 'redirect_url']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'action' in local_var_params:
            query_params.append(('action', local_var_params['action']))
            collection_formats['action'] = 'multi'
        if 'admin_state_up' in local_var_params:
            query_params.append(('admin_state_up', local_var_params['admin_state_up']))
        if 'description' in local_var_params:
            query_params.append(('description', local_var_params['description']))
            collection_formats['description'] = 'multi'
        if 'display_all_rules' in local_var_params:
            query_params.append(('display_all_rules', local_var_params['display_all_rules']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
            collection_formats['enterprise_project_id'] = 'multi'
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
            collection_formats['id'] = 'multi'
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'listener_id' in local_var_params:
            query_params.append(('listener_id', local_var_params['listener_id']))
            collection_formats['listener_id'] = 'multi'
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
            collection_formats['name'] = 'multi'
        if 'page_reverse' in local_var_params:
            query_params.append(('page_reverse', local_var_params['page_reverse']))
        if 'position' in local_var_params:
            query_params.append(('position', local_var_params['position']))
            collection_formats['position'] = 'multi'
        if 'provisioning_status' in local_var_params:
            query_params.append(('provisioning_status', local_var_params['provisioning_status']))
            collection_formats['provisioning_status'] = 'multi'
        if 'redirect_listener_id' in local_var_params:
            query_params.append(('redirect_listener_id', local_var_params['redirect_listener_id']))
            collection_formats['redirect_listener_id'] = 'multi'
        if 'redirect_pool_id' in local_var_params:
            query_params.append(('redirect_pool_id', local_var_params['redirect_pool_id']))
            collection_formats['redirect_pool_id'] = 'multi'
        if 'redirect_url' in local_var_params:
            query_params.append(('redirect_url', local_var_params['redirect_url']))
            collection_formats['redirect_url'] = 'multi'

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/elb/l7policies',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListL7PoliciesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_l7_rules_async(self, request):
        """查询转发规则列表

        查询转发规则列表。

        :param ListL7RulesRequest request
        :return: ListL7RulesResponse
        """
        return self.list_l7_rules_with_http_info(request)

    def list_l7_rules_with_http_info(self, request):
        """查询转发规则列表

        查询转发规则列表。

        :param ListL7RulesRequest request
        :return: ListL7RulesResponse
        """

        all_params = ['l7policy_id', 'admin_state_up', 'compare_type', 'enterprise_project_id', 'id', 'invert', 'key', 'limit', 'marker', 'page_reverse', 'provisioning_status', 'type', 'value']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'l7policy_id' in local_var_params:
            path_params['l7policy_id'] = local_var_params['l7policy_id']

        query_params = []
        if 'admin_state_up' in local_var_params:
            query_params.append(('admin_state_up', local_var_params['admin_state_up']))
        if 'compare_type' in local_var_params:
            query_params.append(('compare_type', local_var_params['compare_type']))
            collection_formats['compare_type'] = 'multi'
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
            collection_formats['enterprise_project_id'] = 'multi'
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
            collection_formats['id'] = 'multi'
        if 'invert' in local_var_params:
            query_params.append(('invert', local_var_params['invert']))
        if 'key' in local_var_params:
            query_params.append(('key', local_var_params['key']))
            collection_formats['key'] = 'multi'
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'page_reverse' in local_var_params:
            query_params.append(('page_reverse', local_var_params['page_reverse']))
        if 'provisioning_status' in local_var_params:
            query_params.append(('provisioning_status', local_var_params['provisioning_status']))
            collection_formats['provisioning_status'] = 'multi'
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
            collection_formats['type'] = 'multi'
        if 'value' in local_var_params:
            query_params.append(('value', local_var_params['value']))
            collection_formats['value'] = 'multi'

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/elb/l7policies/{l7policy_id}/rules',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListL7RulesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_listeners_async(self, request):
        """查询监听器列表

        查询监听器列表。

        :param ListListenersRequest request
        :return: ListListenersResponse
        """
        return self.list_listeners_with_http_info(request)

    def list_listeners_with_http_info(self, request):
        """查询监听器列表

        查询监听器列表。

        :param ListListenersRequest request
        :return: ListListenersResponse
        """

        all_params = ['admin_state_up', 'client_ca_tls_container_ref', 'client_timeout', 'connection_limit', 'default_pool_id', 'default_tls_container_ref', 'description', 'enable_member_retry', 'enterprise_project_id', 'http2_enable', 'id', 'keepalive_timeout', 'limit', 'loadbalancer_id', 'marker', 'member_address', 'member_device_id', 'member_timeout', 'name', 'page_reverse', 'protocol', 'protocol_port', 'tls_ciphers_policy', 'transparent_client_ip_enable']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'admin_state_up' in local_var_params:
            query_params.append(('admin_state_up', local_var_params['admin_state_up']))
        if 'client_ca_tls_container_ref' in local_var_params:
            query_params.append(('client_ca_tls_container_ref', local_var_params['client_ca_tls_container_ref']))
            collection_formats['client_ca_tls_container_ref'] = 'multi'
        if 'client_timeout' in local_var_params:
            query_params.append(('client_timeout', local_var_params['client_timeout']))
            collection_formats['client_timeout'] = 'multi'
        if 'connection_limit' in local_var_params:
            query_params.append(('connection_limit', local_var_params['connection_limit']))
            collection_formats['connection_limit'] = 'multi'
        if 'default_pool_id' in local_var_params:
            query_params.append(('default_pool_id', local_var_params['default_pool_id']))
            collection_formats['default_pool_id'] = 'multi'
        if 'default_tls_container_ref' in local_var_params:
            query_params.append(('default_tls_container_ref', local_var_params['default_tls_container_ref']))
            collection_formats['default_tls_container_ref'] = 'multi'
        if 'description' in local_var_params:
            query_params.append(('description', local_var_params['description']))
            collection_formats['description'] = 'multi'
        if 'enable_member_retry' in local_var_params:
            query_params.append(('enable_member_retry', local_var_params['enable_member_retry']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
            collection_formats['enterprise_project_id'] = 'multi'
        if 'http2_enable' in local_var_params:
            query_params.append(('http2_enable', local_var_params['http2_enable']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
            collection_formats['id'] = 'multi'
        if 'keepalive_timeout' in local_var_params:
            query_params.append(('keepalive_timeout', local_var_params['keepalive_timeout']))
            collection_formats['keepalive_timeout'] = 'multi'
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'loadbalancer_id' in local_var_params:
            query_params.append(('loadbalancer_id', local_var_params['loadbalancer_id']))
            collection_formats['loadbalancer_id'] = 'multi'
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'member_address' in local_var_params:
            query_params.append(('member_address', local_var_params['member_address']))
            collection_formats['member_address'] = 'multi'
        if 'member_device_id' in local_var_params:
            query_params.append(('member_device_id', local_var_params['member_device_id']))
            collection_formats['member_device_id'] = 'multi'
        if 'member_timeout' in local_var_params:
            query_params.append(('member_timeout', local_var_params['member_timeout']))
            collection_formats['member_timeout'] = 'multi'
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
            collection_formats['name'] = 'multi'
        if 'page_reverse' in local_var_params:
            query_params.append(('page_reverse', local_var_params['page_reverse']))
        if 'protocol' in local_var_params:
            query_params.append(('protocol', local_var_params['protocol']))
            collection_formats['protocol'] = 'multi'
        if 'protocol_port' in local_var_params:
            query_params.append(('protocol_port', local_var_params['protocol_port']))
            collection_formats['protocol_port'] = 'multi'
        if 'tls_ciphers_policy' in local_var_params:
            query_params.append(('tls_ciphers_policy', local_var_params['tls_ciphers_policy']))
            collection_formats['tls_ciphers_policy'] = 'multi'
        if 'transparent_client_ip_enable' in local_var_params:
            query_params.append(('transparent_client_ip_enable', local_var_params['transparent_client_ip_enable']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/elb/listeners',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListListenersResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_load_balancers_async(self, request):
        """查询负载均衡器列表

        查询负载均衡器列表，支持过滤查询和分页查询

        :param ListLoadBalancersRequest request
        :return: ListLoadBalancersResponse
        """
        return self.list_load_balancers_with_http_info(request)

    def list_load_balancers_with_http_info(self, request):
        """查询负载均衡器列表

        查询负载均衡器列表，支持过滤查询和分页查询

        :param ListLoadBalancersRequest request
        :return: ListLoadBalancersResponse
        """

        all_params = ['admin_state_up', 'availability_zone_list', 'billing_info', 'deletion_protection_enable', 'description', 'eips', 'enterprise_project_id', 'guaranteed', 'id', 'ip_version', 'ipv6_vip_address', 'ipv6_vip_port_id', 'ipv6_vip_virsubnet_id', 'l4_flavor_id', 'l4_scale_flavor_id', 'l7_flavor_id', 'l7_scale_flavor_id', 'limit', 'marker', 'member_address', 'member_device_id', 'name', 'operating_status', 'page_reverse', 'provisioning_status', 'publicips', 'vip_address', 'vip_port_id', 'vip_subnet_cidr_id', 'vpc_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'admin_state_up' in local_var_params:
            query_params.append(('admin_state_up', local_var_params['admin_state_up']))
        if 'availability_zone_list' in local_var_params:
            query_params.append(('availability_zone_list', local_var_params['availability_zone_list']))
            collection_formats['availability_zone_list'] = 'multi'
        if 'billing_info' in local_var_params:
            query_params.append(('billing_info', local_var_params['billing_info']))
            collection_formats['billing_info'] = 'multi'
        if 'deletion_protection_enable' in local_var_params:
            query_params.append(('deletion_protection_enable', local_var_params['deletion_protection_enable']))
        if 'description' in local_var_params:
            query_params.append(('description', local_var_params['description']))
            collection_formats['description'] = 'multi'
        if 'eips' in local_var_params:
            query_params.append(('eips', local_var_params['eips']))
            collection_formats['eips'] = 'multi'
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
            collection_formats['enterprise_project_id'] = 'multi'
        if 'guaranteed' in local_var_params:
            query_params.append(('guaranteed', local_var_params['guaranteed']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
            collection_formats['id'] = 'multi'
        if 'ip_version' in local_var_params:
            query_params.append(('ip_version', local_var_params['ip_version']))
            collection_formats['ip_version'] = 'multi'
        if 'ipv6_vip_address' in local_var_params:
            query_params.append(('ipv6_vip_address', local_var_params['ipv6_vip_address']))
            collection_formats['ipv6_vip_address'] = 'multi'
        if 'ipv6_vip_port_id' in local_var_params:
            query_params.append(('ipv6_vip_port_id', local_var_params['ipv6_vip_port_id']))
            collection_formats['ipv6_vip_port_id'] = 'multi'
        if 'ipv6_vip_virsubnet_id' in local_var_params:
            query_params.append(('ipv6_vip_virsubnet_id', local_var_params['ipv6_vip_virsubnet_id']))
            collection_formats['ipv6_vip_virsubnet_id'] = 'multi'
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
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'member_address' in local_var_params:
            query_params.append(('member_address', local_var_params['member_address']))
            collection_formats['member_address'] = 'multi'
        if 'member_device_id' in local_var_params:
            query_params.append(('member_device_id', local_var_params['member_device_id']))
            collection_formats['member_device_id'] = 'multi'
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
            collection_formats['name'] = 'multi'
        if 'operating_status' in local_var_params:
            query_params.append(('operating_status', local_var_params['operating_status']))
            collection_formats['operating_status'] = 'multi'
        if 'page_reverse' in local_var_params:
            query_params.append(('page_reverse', local_var_params['page_reverse']))
        if 'provisioning_status' in local_var_params:
            query_params.append(('provisioning_status', local_var_params['provisioning_status']))
            collection_formats['provisioning_status'] = 'multi'
        if 'publicips' in local_var_params:
            query_params.append(('publicips', local_var_params['publicips']))
            collection_formats['publicips'] = 'multi'
        if 'vip_address' in local_var_params:
            query_params.append(('vip_address', local_var_params['vip_address']))
            collection_formats['vip_address'] = 'multi'
        if 'vip_port_id' in local_var_params:
            query_params.append(('vip_port_id', local_var_params['vip_port_id']))
            collection_formats['vip_port_id'] = 'multi'
        if 'vip_subnet_cidr_id' in local_var_params:
            query_params.append(('vip_subnet_cidr_id', local_var_params['vip_subnet_cidr_id']))
            collection_formats['vip_subnet_cidr_id'] = 'multi'
        if 'vpc_id' in local_var_params:
            query_params.append(('vpc_id', local_var_params['vpc_id']))
            collection_formats['vpc_id'] = 'multi'

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/elb/loadbalancers',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListLoadBalancersResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_members_async(self, request):
        """后端服务器列表

        Pool下的后端服务器列表。

        :param ListMembersRequest request
        :return: ListMembersResponse
        """
        return self.list_members_with_http_info(request)

    def list_members_with_http_info(self, request):
        """后端服务器列表

        Pool下的后端服务器列表。

        :param ListMembersRequest request
        :return: ListMembersResponse
        """

        all_params = ['pool_id', 'address', 'admin_state_up', 'enterprise_project_id', 'id', 'limit', 'marker', 'name', 'operating_status', 'page_reverse', 'protocol_port', 'subnet_cidr_id', 'weight']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'pool_id' in local_var_params:
            path_params['pool_id'] = local_var_params['pool_id']

        query_params = []
        if 'address' in local_var_params:
            query_params.append(('address', local_var_params['address']))
            collection_formats['address'] = 'multi'
        if 'admin_state_up' in local_var_params:
            query_params.append(('admin_state_up', local_var_params['admin_state_up']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
            collection_formats['enterprise_project_id'] = 'multi'
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
            collection_formats['id'] = 'multi'
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
            collection_formats['name'] = 'multi'
        if 'operating_status' in local_var_params:
            query_params.append(('operating_status', local_var_params['operating_status']))
            collection_formats['operating_status'] = 'multi'
        if 'page_reverse' in local_var_params:
            query_params.append(('page_reverse', local_var_params['page_reverse']))
        if 'protocol_port' in local_var_params:
            query_params.append(('protocol_port', local_var_params['protocol_port']))
            collection_formats['protocol_port'] = 'multi'
        if 'subnet_cidr_id' in local_var_params:
            query_params.append(('subnet_cidr_id', local_var_params['subnet_cidr_id']))
            collection_formats['subnet_cidr_id'] = 'multi'
        if 'weight' in local_var_params:
            query_params.append(('weight', local_var_params['weight']))
            collection_formats['weight'] = 'multi'

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/elb/pools/{pool_id}/members',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListMembersResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_pools_async(self, request):
        """查询后端服务器组列表

        后端服务器组列表。

        :param ListPoolsRequest request
        :return: ListPoolsResponse
        """
        return self.list_pools_with_http_info(request)

    def list_pools_with_http_info(self, request):
        """查询后端服务器组列表

        后端服务器组列表。

        :param ListPoolsRequest request
        :return: ListPoolsResponse
        """

        all_params = ['admin_state_up', 'description', 'enterprise_project_id', 'healthmonitor_id', 'id', 'ip_version', 'lb_algorithm', 'limit', 'loadbalancer_id', 'marker', 'member_address', 'member_deletion_protection_enable', 'member_device_id', 'name', 'page_reverse', 'protocol']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'admin_state_up' in local_var_params:
            query_params.append(('admin_state_up', local_var_params['admin_state_up']))
        if 'description' in local_var_params:
            query_params.append(('description', local_var_params['description']))
            collection_formats['description'] = 'multi'
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
            collection_formats['enterprise_project_id'] = 'multi'
        if 'healthmonitor_id' in local_var_params:
            query_params.append(('healthmonitor_id', local_var_params['healthmonitor_id']))
            collection_formats['healthmonitor_id'] = 'multi'
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
            collection_formats['id'] = 'multi'
        if 'ip_version' in local_var_params:
            query_params.append(('ip_version', local_var_params['ip_version']))
            collection_formats['ip_version'] = 'multi'
        if 'lb_algorithm' in local_var_params:
            query_params.append(('lb_algorithm', local_var_params['lb_algorithm']))
            collection_formats['lb_algorithm'] = 'multi'
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'loadbalancer_id' in local_var_params:
            query_params.append(('loadbalancer_id', local_var_params['loadbalancer_id']))
            collection_formats['loadbalancer_id'] = 'multi'
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'member_address' in local_var_params:
            query_params.append(('member_address', local_var_params['member_address']))
            collection_formats['member_address'] = 'multi'
        if 'member_deletion_protection_enable' in local_var_params:
            query_params.append(('member_deletion_protection_enable', local_var_params['member_deletion_protection_enable']))
        if 'member_device_id' in local_var_params:
            query_params.append(('member_device_id', local_var_params['member_device_id']))
            collection_formats['member_device_id'] = 'multi'
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
            collection_formats['name'] = 'multi'
        if 'page_reverse' in local_var_params:
            query_params.append(('page_reverse', local_var_params['page_reverse']))
        if 'protocol' in local_var_params:
            query_params.append(('protocol', local_var_params['protocol']))
            collection_formats['protocol'] = 'multi'

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/elb/pools',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListPoolsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_certificate_async(self, request):
        """证书详情

        查询SSL证书详情。

        :param ShowCertificateRequest request
        :return: ShowCertificateResponse
        """
        return self.show_certificate_with_http_info(request)

    def show_certificate_with_http_info(self, request):
        """证书详情

        查询SSL证书详情。

        :param ShowCertificateRequest request
        :return: ShowCertificateResponse
        """

        all_params = ['certificate_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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


        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/elb/certificates/{certificate_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowCertificateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_flavor_async(self, request):
        """查询规格详情

        查询规格的详情。

        :param ShowFlavorRequest request
        :return: ShowFlavorResponse
        """
        return self.show_flavor_with_http_info(request)

    def show_flavor_with_http_info(self, request):
        """查询规格详情

        查询规格的详情。

        :param ShowFlavorRequest request
        :return: ShowFlavorResponse
        """

        all_params = ['flavor_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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


        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/elb/flavors/{flavor_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowFlavorResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_health_monitor_async(self, request):
        """查询健康检查详情

        查询健康检查详情。

        :param ShowHealthMonitorRequest request
        :return: ShowHealthMonitorResponse
        """
        return self.show_health_monitor_with_http_info(request)

    def show_health_monitor_with_http_info(self, request):
        """查询健康检查详情

        查询健康检查详情。

        :param ShowHealthMonitorRequest request
        :return: ShowHealthMonitorResponse
        """

        all_params = ['healthmonitor_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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


        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/elb/healthmonitors/{healthmonitor_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowHealthMonitorResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_l7_policy_async(self, request):
        """查询转发策略详情

        查询转发策略详情。

        :param ShowL7PolicyRequest request
        :return: ShowL7PolicyResponse
        """
        return self.show_l7_policy_with_http_info(request)

    def show_l7_policy_with_http_info(self, request):
        """查询转发策略详情

        查询转发策略详情。

        :param ShowL7PolicyRequest request
        :return: ShowL7PolicyResponse
        """

        all_params = ['l7policy_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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


        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/elb/l7policies/{l7policy_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowL7PolicyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_l7_rule_async(self, request):
        """查询转发规则详情

        查询转发规则详情

        :param ShowL7RuleRequest request
        :return: ShowL7RuleResponse
        """
        return self.show_l7_rule_with_http_info(request)

    def show_l7_rule_with_http_info(self, request):
        """查询转发规则详情

        查询转发规则详情

        :param ShowL7RuleRequest request
        :return: ShowL7RuleResponse
        """

        all_params = ['l7policy_id', 'l7rule_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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


        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/elb/l7policies/{l7policy_id}/rules/{l7rule_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowL7RuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_listener_async(self, request):
        """查询监听器详情

        监听器详情。

        :param ShowListenerRequest request
        :return: ShowListenerResponse
        """
        return self.show_listener_with_http_info(request)

    def show_listener_with_http_info(self, request):
        """查询监听器详情

        监听器详情。

        :param ShowListenerRequest request
        :return: ShowListenerResponse
        """

        all_params = ['listener_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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


        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/elb/listeners/{listener_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowListenerResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_load_balancer_async(self, request):
        """查询负载均衡器详情

        查询负载均衡器详情

        :param ShowLoadBalancerRequest request
        :return: ShowLoadBalancerResponse
        """
        return self.show_load_balancer_with_http_info(request)

    def show_load_balancer_with_http_info(self, request):
        """查询负载均衡器详情

        查询负载均衡器详情

        :param ShowLoadBalancerRequest request
        :return: ShowLoadBalancerResponse
        """

        all_params = ['loadbalancer_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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


        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/elb/loadbalancers/{loadbalancer_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowLoadBalancerResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_load_balancer_status_async(self, request):
        """查询负载均衡器状态树

        查询负载均衡器状态树，列出负载均衡器关联的子资源的信息

        :param ShowLoadBalancerStatusRequest request
        :return: ShowLoadBalancerStatusResponse
        """
        return self.show_load_balancer_status_with_http_info(request)

    def show_load_balancer_status_with_http_info(self, request):
        """查询负载均衡器状态树

        查询负载均衡器状态树，列出负载均衡器关联的子资源的信息

        :param ShowLoadBalancerStatusRequest request
        :return: ShowLoadBalancerStatusResponse
        """

        all_params = ['loadbalancer_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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


        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/elb/loadbalancers/{loadbalancer_id}/statuses',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowLoadBalancerStatusResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_member_async(self, request):
        """后端服务器详情

        后端服务器详情

        :param ShowMemberRequest request
        :return: ShowMemberResponse
        """
        return self.show_member_with_http_info(request)

    def show_member_with_http_info(self, request):
        """后端服务器详情

        后端服务器详情

        :param ShowMemberRequest request
        :return: ShowMemberResponse
        """

        all_params = ['member_id', 'pool_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/elb/pools/{pool_id}/members/{member_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowMemberResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_pool_async(self, request):
        """查询后端服务器组详情

        后端服务器组详情。

        :param ShowPoolRequest request
        :return: ShowPoolResponse
        """
        return self.show_pool_with_http_info(request)

    def show_pool_with_http_info(self, request):
        """查询后端服务器组详情

        后端服务器组详情。

        :param ShowPoolRequest request
        :return: ShowPoolResponse
        """

        all_params = ['pool_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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


        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/elb/pools/{pool_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowPoolResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_quota_async(self, request):
        """查询配额详情

        【不开放】查询特定项目的配额数。

        :param ShowQuotaRequest request
        :return: ShowQuotaResponse
        """
        return self.show_quota_with_http_info(request)

    def show_quota_with_http_info(self, request):
        """查询配额详情

        【不开放】查询特定项目的配额数。

        :param ShowQuotaRequest request
        :return: ShowQuotaResponse
        """

        all_params = []
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
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/elb/quotas',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowQuotaResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_quota_defaults_async(self, request):
        """查询默认配额

        【不开放】查询默认配额数。

        :param ShowQuotaDefaultsRequest request
        :return: ShowQuotaDefaultsResponse
        """
        return self.show_quota_defaults_with_http_info(request)

    def show_quota_defaults_with_http_info(self, request):
        """查询默认配额

        【不开放】查询默认配额数。

        :param ShowQuotaDefaultsRequest request
        :return: ShowQuotaDefaultsResponse
        """

        all_params = []
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
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/elb/quotas/defaults',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowQuotaDefaultsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_certificate_async(self, request):
        """更新证书

        更新SSL证书。

        :param UpdateCertificateRequest request
        :return: UpdateCertificateResponse
        """
        return self.update_certificate_with_http_info(request)

    def update_certificate_with_http_info(self, request):
        """更新证书

        更新SSL证书。

        :param UpdateCertificateRequest request
        :return: UpdateCertificateResponse
        """

        all_params = ['certificate_id', 'update_certificate_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='UpdateCertificateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_health_monitor_async(self, request):
        """更新健康检查

        更新健康检查。

        :param UpdateHealthMonitorRequest request
        :return: UpdateHealthMonitorResponse
        """
        return self.update_health_monitor_with_http_info(request)

    def update_health_monitor_with_http_info(self, request):
        """更新健康检查

        更新健康检查。

        :param UpdateHealthMonitorRequest request
        :return: UpdateHealthMonitorResponse
        """

        all_params = ['healthmonitor_id', 'update_health_monitor_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='UpdateHealthMonitorResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_l7_policy_async(self, request):
        """更新转发策略

        更新转发策略。

        :param UpdateL7PolicyRequest request
        :return: UpdateL7PolicyResponse
        """
        return self.update_l7_policy_with_http_info(request)

    def update_l7_policy_with_http_info(self, request):
        """更新转发策略

        更新转发策略。

        :param UpdateL7PolicyRequest request
        :return: UpdateL7PolicyResponse
        """

        all_params = ['l7policy_id', 'update_l7_policy_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='UpdateL7PolicyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_l7_rule_async(self, request):
        """更新转发规则

        更新转发规则。

        :param UpdateL7RuleRequest request
        :return: UpdateL7RuleResponse
        """
        return self.update_l7_rule_with_http_info(request)

    def update_l7_rule_with_http_info(self, request):
        """更新转发规则

        更新转发规则。

        :param UpdateL7RuleRequest request
        :return: UpdateL7RuleResponse
        """

        all_params = ['l7policy_id', 'l7rule_id', 'update_l7_rule_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='UpdateL7RuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_listener_async(self, request):
        """更新监听器

        更新监听器。

        :param UpdateListenerRequest request
        :return: UpdateListenerResponse
        """
        return self.update_listener_with_http_info(request)

    def update_listener_with_http_info(self, request):
        """更新监听器

        更新监听器。

        :param UpdateListenerRequest request
        :return: UpdateListenerResponse
        """

        all_params = ['listener_id', 'update_listener_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='UpdateListenerResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_load_balancer_async(self, request):
        """更新负载均衡器

        更新负载均衡器。

        :param UpdateLoadBalancerRequest request
        :return: UpdateLoadBalancerResponse
        """
        return self.update_load_balancer_with_http_info(request)

    def update_load_balancer_with_http_info(self, request):
        """更新负载均衡器

        更新负载均衡器。

        :param UpdateLoadBalancerRequest request
        :return: UpdateLoadBalancerResponse
        """

        all_params = ['loadbalancer_id', 'update_load_balancer_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='UpdateLoadBalancerResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_member_async(self, request):
        """更新后端服务器

        如果member绑定的负载均衡器的provisioning status不是ACTIVE，则不能更新该member。

        :param UpdateMemberRequest request
        :return: UpdateMemberResponse
        """
        return self.update_member_with_http_info(request)

    def update_member_with_http_info(self, request):
        """更新后端服务器

        如果member绑定的负载均衡器的provisioning status不是ACTIVE，则不能更新该member。

        :param UpdateMemberRequest request
        :return: UpdateMemberResponse
        """

        all_params = ['member_id', 'pool_id', 'update_member_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='UpdateMemberResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_pool_async(self, request):
        """更新后端服务器组

        更新后端服务器组。

        :param UpdatePoolRequest request
        :return: UpdatePoolResponse
        """
        return self.update_pool_with_http_info(request)

    def update_pool_with_http_info(self, request):
        """更新后端服务器组

        更新后端服务器组。

        :param UpdatePoolRequest request
        :return: UpdatePoolResponse
        """

        all_params = ['pool_id', 'update_pool_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='UpdatePoolResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def count_preoccupy_ip_num_async(self, request):
        """计算预占IP数

        计算创建一个负载均衡实例和第一个七层监听器需预占用的IP数

        :param CountPreoccupyIpNumRequest request
        :return: CountPreoccupyIpNumResponse
        """
        return self.count_preoccupy_ip_num_with_http_info(request)

    def count_preoccupy_ip_num_with_http_info(self, request):
        """计算预占IP数

        计算创建一个负载均衡实例和第一个七层监听器需预占用的IP数

        :param CountPreoccupyIpNumRequest request
        :return: CountPreoccupyIpNumResponse
        """

        all_params = ['availability_zone_id', 'ip_target_enable', 'ip_version', 'l7_flavor_id', 'loadbalancer_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'availability_zone_id' in local_var_params:
            query_params.append(('availability_zone_id', local_var_params['availability_zone_id']))
            collection_formats['availability_zone_id'] = 'multi'
        if 'ip_target_enable' in local_var_params:
            query_params.append(('ip_target_enable', local_var_params['ip_target_enable']))
        if 'ip_version' in local_var_params:
            query_params.append(('ip_version', local_var_params['ip_version']))
        if 'l7_flavor_id' in local_var_params:
            query_params.append(('l7_flavor_id', local_var_params['l7_flavor_id']))
        if 'loadbalancer_id' in local_var_params:
            query_params.append(('loadbalancer_id', local_var_params['loadbalancer_id']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/elb/preoccupy-ip-num',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CountPreoccupyIpNumResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_ip_group_async(self, request):
        """创建IP地址组

        创建ip地址组

        :param CreateIpGroupRequest request
        :return: CreateIpGroupResponse
        """
        return self.create_ip_group_with_http_info(request)

    def create_ip_group_with_http_info(self, request):
        """创建IP地址组

        创建ip地址组

        :param CreateIpGroupRequest request
        :return: CreateIpGroupResponse
        """

        all_params = ['create_ip_group_request_body']
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
            response_type='CreateIpGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_ip_group_async(self, request):
        """删除IP地址组

        删除ip地址组。

        :param DeleteIpGroupRequest request
        :return: DeleteIpGroupResponse
        """
        return self.delete_ip_group_with_http_info(request)

    def delete_ip_group_with_http_info(self, request):
        """删除IP地址组

        删除ip地址组。

        :param DeleteIpGroupRequest request
        :return: DeleteIpGroupResponse
        """

        all_params = ['ipgroup_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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


        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/elb/ipgroups/{ipgroup_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteIpGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_ip_groups_async(self, request):
        """查询IP地址组列表

        查询IP地址组列表

        :param ListIpGroupsRequest request
        :return: ListIpGroupsResponse
        """
        return self.list_ip_groups_with_http_info(request)

    def list_ip_groups_with_http_info(self, request):
        """查询IP地址组列表

        查询IP地址组列表

        :param ListIpGroupsRequest request
        :return: ListIpGroupsResponse
        """

        all_params = ['description', 'id', 'ip_list', 'limit', 'marker', 'name', 'page_reverse']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'description' in local_var_params:
            query_params.append(('description', local_var_params['description']))
            collection_formats['description'] = 'multi'
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
            collection_formats['id'] = 'multi'
        if 'ip_list' in local_var_params:
            query_params.append(('ip_list', local_var_params['ip_list']))
            collection_formats['ip_list'] = 'multi'
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
            collection_formats['name'] = 'multi'
        if 'page_reverse' in local_var_params:
            query_params.append(('page_reverse', local_var_params['page_reverse']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/elb/ipgroups',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListIpGroupsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_ip_group_async(self, request):
        """查询IP地址组详情

        获取ip地址组详情

        :param ShowIpGroupRequest request
        :return: ShowIpGroupResponse
        """
        return self.show_ip_group_with_http_info(request)

    def show_ip_group_with_http_info(self, request):
        """查询IP地址组详情

        获取ip地址组详情

        :param ShowIpGroupRequest request
        :return: ShowIpGroupResponse
        """

        all_params = ['ipgroup_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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


        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/elb/ipgroups/{ipgroup_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowIpGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_ip_group_async(self, request):
        """更新IP地址组

        更新ip地址组，只支持全量更新ip。

        :param UpdateIpGroupRequest request
        :return: UpdateIpGroupResponse
        """
        return self.update_ip_group_with_http_info(request)

    def update_ip_group_with_http_info(self, request):
        """更新IP地址组

        更新ip地址组，只支持全量更新ip。

        :param UpdateIpGroupRequest request
        :return: UpdateIpGroupResponse
        """

        all_params = ['ipgroup_id', 'update_ip_group_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='UpdateIpGroupResponse',
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

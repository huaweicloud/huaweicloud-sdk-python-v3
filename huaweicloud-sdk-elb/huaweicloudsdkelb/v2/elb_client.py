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


class ElbClient(Client):
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
        super(ElbClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkelb.v2.model")
        self.preset_headers = {'User-Agent': 'HuaweiCloud-SDK-Python'}

    @classmethod
    def new_builder(cls, clazz=None):
        if clazz is None:
            return ClientBuilder(cls)

        if clazz.__name__ != "ElbClient":
            raise TypeError("client type error, support client type is ElbClient")

        return ClientBuilder(clazz)

    def create_healthmonitor(self, request):
        """创建健康检查

        给后端云服务器组添加健康检查

        :param CreateHealthmonitorRequest request
        :return: CreateHealthmonitorResponse
        """
        return self.create_healthmonitor_with_http_info(request)

    def create_healthmonitor_with_http_info(self, request):
        """创建健康检查

        给后端云服务器组添加健康检查

        :param CreateHealthmonitorRequest request
        :return: CreateHealthmonitorResponse
        """

        all_params = ['create_healthmonitor_request_body']
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
            resource_path='/v2/{project_id}/elb/healthmonitors',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateHealthmonitorResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_l7policy(self, request):
        """创建转发策略

        创建listener关联的转发策略

        :param CreateL7policyRequest request
        :return: CreateL7policyResponse
        """
        return self.create_l7policy_with_http_info(request)

    def create_l7policy_with_http_info(self, request):
        """创建转发策略

        创建listener关联的转发策略

        :param CreateL7policyRequest request
        :return: CreateL7policyResponse
        """

        all_params = ['create_l7policy_request_body']
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
            resource_path='/v2/{project_id}/elb/l7policies',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateL7policyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_l7rule(self, request):
        """创建转发规则

        创建转发规则

        :param CreateL7ruleRequest request
        :return: CreateL7ruleResponse
        """
        return self.create_l7rule_with_http_info(request)

    def create_l7rule_with_http_info(self, request):
        """创建转发规则

        创建转发规则

        :param CreateL7ruleRequest request
        :return: CreateL7ruleResponse
        """

        all_params = ['l7policy_id', 'create_l7rule_request_body']
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
            resource_path='/v2/{project_id}/elb/l7policies/{l7policy_id}/rules',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateL7ruleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_listener(self, request):
        """创建监听器

        创建与负载均衡器绑定的监听器。

        :param CreateListenerRequest request
        :return: CreateListenerResponse
        """
        return self.create_listener_with_http_info(request)

    def create_listener_with_http_info(self, request):
        """创建监听器

        创建与负载均衡器绑定的监听器。

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
            resource_path='/v2/{project_id}/elb/listeners',
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


    def create_loadbalancer(self, request):
        """创建负载均衡器

        创建私网类型的增强型负载均衡器。创建成功后，该接口会返回创建的增强型负载均衡器的ID、所属子网ID、负载均衡器IP等详细信息。若要创建公网类型的增强型负载均衡器，还需调用创建浮动IP的接口，将浮动IP与私网负载均衡器的vip_port_id绑定。

        :param CreateLoadbalancerRequest request
        :return: CreateLoadbalancerResponse
        """
        return self.create_loadbalancer_with_http_info(request)

    def create_loadbalancer_with_http_info(self, request):
        """创建负载均衡器

        创建私网类型的增强型负载均衡器。创建成功后，该接口会返回创建的增强型负载均衡器的ID、所属子网ID、负载均衡器IP等详细信息。若要创建公网类型的增强型负载均衡器，还需调用创建浮动IP的接口，将浮动IP与私网负载均衡器的vip_port_id绑定。

        :param CreateLoadbalancerRequest request
        :return: CreateLoadbalancerResponse
        """

        all_params = ['create_loadbalancer_request_body']
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
            resource_path='/v2/{project_id}/elb/loadbalancers',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateLoadbalancerResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_member(self, request):
        """创建后端云服务器

        添加属于某个后端云服务器组的后端云服务器。

        :param CreateMemberRequest request
        :return: CreateMemberResponse
        """
        return self.create_member_with_http_info(request)

    def create_member_with_http_info(self, request):
        """创建后端云服务器

        添加属于某个后端云服务器组的后端云服务器。

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
            resource_path='/v2/{project_id}/elb/pools/{pool_id}/members',
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


    def create_pool(self, request):
        """创建后端云服务器组

        创建后端云服务器组。将多个后端云服务器添加到后端云服务器组中后，请求会在后端云服务器间按后端云服务器组的负载均衡算法和后端云服务器的权重来做请求分发。

        :param CreatePoolRequest request
        :return: CreatePoolResponse
        """
        return self.create_pool_with_http_info(request)

    def create_pool_with_http_info(self, request):
        """创建后端云服务器组

        创建后端云服务器组。将多个后端云服务器添加到后端云服务器组中后，请求会在后端云服务器间按后端云服务器组的负载均衡算法和后端云服务器的权重来做请求分发。

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
            resource_path='/v2/{project_id}/elb/pools',
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


    def create_whitelist(self, request):
        """创建白名单

        创建白名单，控制监听器的访问权限。若开启了白名单功能，只有白名单中放通的IP可以访问该监听器的后端服务。

        :param CreateWhitelistRequest request
        :return: CreateWhitelistResponse
        """
        return self.create_whitelist_with_http_info(request)

    def create_whitelist_with_http_info(self, request):
        """创建白名单

        创建白名单，控制监听器的访问权限。若开启了白名单功能，只有白名单中放通的IP可以访问该监听器的后端服务。

        :param CreateWhitelistRequest request
        :return: CreateWhitelistResponse
        """

        all_params = ['create_whitelist_request_body']
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
            resource_path='/v2/{project_id}/elb/whitelists',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateWhitelistResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_healthmonitor(self, request):
        """删除健康检查

        删除健康检查

        :param DeleteHealthmonitorRequest request
        :return: DeleteHealthmonitorResponse
        """
        return self.delete_healthmonitor_with_http_info(request)

    def delete_healthmonitor_with_http_info(self, request):
        """删除健康检查

        删除健康检查

        :param DeleteHealthmonitorRequest request
        :return: DeleteHealthmonitorResponse
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

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/elb/healthmonitors/{healthmonitor_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteHealthmonitorResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_l7policy(self, request):
        """删除转发策略

        删除转发策略

        :param DeleteL7policyRequest request
        :return: DeleteL7policyResponse
        """
        return self.delete_l7policy_with_http_info(request)

    def delete_l7policy_with_http_info(self, request):
        """删除转发策略

        删除转发策略

        :param DeleteL7policyRequest request
        :return: DeleteL7policyResponse
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

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/elb/l7policies/{l7policy_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteL7policyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_l7rule(self, request):
        """删除转发规则

        删除转发规则

        :param DeleteL7ruleRequest request
        :return: DeleteL7ruleResponse
        """
        return self.delete_l7rule_with_http_info(request)

    def delete_l7rule_with_http_info(self, request):
        """删除转发规则

        删除转发规则

        :param DeleteL7ruleRequest request
        :return: DeleteL7ruleResponse
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

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/elb/l7policies/{l7policy_id}/rules/{l7rule_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteL7ruleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_listener(self, request):
        """删除监听器

        根据指定ID删除监听器。提供级联删除选项，当选择级联删除时，删除和负载均衡器关联的转发规则、转发策略、白名单、标签等。

        :param DeleteListenerRequest request
        :return: DeleteListenerResponse
        """
        return self.delete_listener_with_http_info(request)

    def delete_listener_with_http_info(self, request):
        """删除监听器

        根据指定ID删除监听器。提供级联删除选项，当选择级联删除时，删除和负载均衡器关联的转发规则、转发策略、白名单、标签等。

        :param DeleteListenerRequest request
        :return: DeleteListenerResponse
        """

        all_params = ['listener_id', 'cascade']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'listener_id' in local_var_params:
            path_params['listener_id'] = local_var_params['listener_id']

        query_params = []
        if 'cascade' in local_var_params:
            query_params.append(('cascade', local_var_params['cascade']))

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
            resource_path='/v2/{project_id}/elb/listeners/{listener_id}',
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


    def delete_loadbalancer(self, request):
        """删除负载均衡

        根据指定ID删除负载均衡器。提供级联删除选项，当选择级联删除时，删除和负载均衡器关联的监听器、后端云服务器组、后端云服务器、健康检查、转发策略、转发规则、白名单、标签等

        :param DeleteLoadbalancerRequest request
        :return: DeleteLoadbalancerResponse
        """
        return self.delete_loadbalancer_with_http_info(request)

    def delete_loadbalancer_with_http_info(self, request):
        """删除负载均衡

        根据指定ID删除负载均衡器。提供级联删除选项，当选择级联删除时，删除和负载均衡器关联的监听器、后端云服务器组、后端云服务器、健康检查、转发策略、转发规则、白名单、标签等

        :param DeleteLoadbalancerRequest request
        :return: DeleteLoadbalancerResponse
        """

        all_params = ['loadbalancer_id', 'cascade']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'loadbalancer_id' in local_var_params:
            path_params['loadbalancer_id'] = local_var_params['loadbalancer_id']

        query_params = []
        if 'cascade' in local_var_params:
            query_params.append(('cascade', local_var_params['cascade']))

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
            resource_path='/v2/{project_id}/elb/loadbalancers/{loadbalancer_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteLoadbalancerResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_member(self, request):
        """删除后端云服务器

        删除后端云服务器

        :param DeleteMemberRequest request
        :return: DeleteMemberResponse
        """
        return self.delete_member_with_http_info(request)

    def delete_member_with_http_info(self, request):
        """删除后端云服务器

        删除后端云服务器

        :param DeleteMemberRequest request
        :return: DeleteMemberResponse
        """

        all_params = ['pool_id', 'member_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v2/{project_id}/elb/pools/{pool_id}/members/{member_id}',
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


    def delete_pool(self, request):
        """删除后端云服务器组

        删除后端云服务器组。

        :param DeletePoolRequest request
        :return: DeletePoolResponse
        """
        return self.delete_pool_with_http_info(request)

    def delete_pool_with_http_info(self, request):
        """删除后端云服务器组

        删除后端云服务器组。

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

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/elb/pools/{pool_id}',
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


    def delete_whitelist(self, request):
        """删除白名单

        删除白名单

        :param DeleteWhitelistRequest request
        :return: DeleteWhitelistResponse
        """
        return self.delete_whitelist_with_http_info(request)

    def delete_whitelist_with_http_info(self, request):
        """删除白名单

        删除白名单

        :param DeleteWhitelistRequest request
        :return: DeleteWhitelistResponse
        """

        all_params = ['whitelist_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'whitelist_id' in local_var_params:
            path_params['whitelist_id'] = local_var_params['whitelist_id']

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
            resource_path='/v2/{project_id}/elb/whitelists/{whitelist_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteWhitelistResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_healthmonitors(self, request):
        """查询健康检查列表

        查询健康检查列表

        :param ListHealthmonitorsRequest request
        :return: ListHealthmonitorsResponse
        """
        return self.list_healthmonitors_with_http_info(request)

    def list_healthmonitors_with_http_info(self, request):
        """查询健康检查列表

        查询健康检查列表

        :param ListHealthmonitorsRequest request
        :return: ListHealthmonitorsResponse
        """

        all_params = ['limit', 'marker', 'page_reverse', 'id', 'name', 'delay', 'max_retries', 'admin_state_up', 'timeout', 'type', 'monitor_port', 'expected_codes', 'domain_name', 'url_path', 'http_method']
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
        if 'page_reverse' in local_var_params:
            query_params.append(('page_reverse', local_var_params['page_reverse']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'delay' in local_var_params:
            query_params.append(('delay', local_var_params['delay']))
        if 'max_retries' in local_var_params:
            query_params.append(('max_retries', local_var_params['max_retries']))
        if 'admin_state_up' in local_var_params:
            query_params.append(('admin_state_up', local_var_params['admin_state_up']))
        if 'timeout' in local_var_params:
            query_params.append(('timeout', local_var_params['timeout']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'monitor_port' in local_var_params:
            query_params.append(('monitor_port', local_var_params['monitor_port']))
        if 'expected_codes' in local_var_params:
            query_params.append(('expected_codes', local_var_params['expected_codes']))
        if 'domain_name' in local_var_params:
            query_params.append(('domain_name', local_var_params['domain_name']))
        if 'url_path' in local_var_params:
            query_params.append(('url_path', local_var_params['url_path']))
        if 'http_method' in local_var_params:
            query_params.append(('http_method', local_var_params['http_method']))

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
            resource_path='/v2/{project_id}/elb/healthmonitors',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListHealthmonitorsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_l7policies(self, request):
        """查询转发策略列表

        查询转发策略。支持过滤查询和分页查询。

        :param ListL7policiesRequest request
        :return: ListL7policiesResponse
        """
        return self.list_l7policies_with_http_info(request)

    def list_l7policies_with_http_info(self, request):
        """查询转发策略列表

        查询转发策略。支持过滤查询和分页查询。

        :param ListL7policiesRequest request
        :return: ListL7policiesResponse
        """

        all_params = ['limit', 'marker', 'page_reverse', 'id', 'name', 'description', 'admin_state_up', 'listener_id', 'action', 'redirect_pool_id', 'redirect_listener_id', 'redirect_url', 'position', 'provisioning_status', 'enterprise_project_id', 'display_all_rules']
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
        if 'page_reverse' in local_var_params:
            query_params.append(('page_reverse', local_var_params['page_reverse']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'description' in local_var_params:
            query_params.append(('description', local_var_params['description']))
        if 'admin_state_up' in local_var_params:
            query_params.append(('admin_state_up', local_var_params['admin_state_up']))
        if 'listener_id' in local_var_params:
            query_params.append(('listener_id', local_var_params['listener_id']))
        if 'action' in local_var_params:
            query_params.append(('action', local_var_params['action']))
        if 'redirect_pool_id' in local_var_params:
            query_params.append(('redirect_pool_id', local_var_params['redirect_pool_id']))
        if 'redirect_listener_id' in local_var_params:
            query_params.append(('redirect_listener_id', local_var_params['redirect_listener_id']))
        if 'redirect_url' in local_var_params:
            query_params.append(('redirect_url', local_var_params['redirect_url']))
        if 'position' in local_var_params:
            query_params.append(('position', local_var_params['position']))
        if 'provisioning_status' in local_var_params:
            query_params.append(('provisioning_status', local_var_params['provisioning_status']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'display_all_rules' in local_var_params:
            query_params.append(('display_all_rules', local_var_params['display_all_rules']))

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
            resource_path='/v2/{project_id}/elb/l7policies',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListL7policiesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_l7rules(self, request):
        """查询转发规则列表

        查询指定转发策略下关联的转发规则列表

        :param ListL7rulesRequest request
        :return: ListL7rulesResponse
        """
        return self.list_l7rules_with_http_info(request)

    def list_l7rules_with_http_info(self, request):
        """查询转发规则列表

        查询指定转发策略下关联的转发规则列表

        :param ListL7rulesRequest request
        :return: ListL7rulesResponse
        """

        all_params = ['l7policy_id', 'limit', 'marker', 'page_reverse', 'id', 'admin_state_up', 'type', 'compare_type', 'invert', 'key', 'value', 'provisioning_status']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
        if 'admin_state_up' in local_var_params:
            query_params.append(('admin_state_up', local_var_params['admin_state_up']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'compare_type' in local_var_params:
            query_params.append(('compare_type', local_var_params['compare_type']))
        if 'invert' in local_var_params:
            query_params.append(('invert', local_var_params['invert']))
        if 'key' in local_var_params:
            query_params.append(('key', local_var_params['key']))
        if 'value' in local_var_params:
            query_params.append(('value', local_var_params['value']))
        if 'provisioning_status' in local_var_params:
            query_params.append(('provisioning_status', local_var_params['provisioning_status']))

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
            resource_path='/v2/{project_id}/elb/l7policies/{l7policy_id}/rules',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListL7rulesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_listeners(self, request):
        """查询监听器列表

        查询监听器列表。支持过滤查询和分页查询。可以通过监听器ID、协议类型、监听端口号、关联的后端云服务器的IP等查询监听器。

        :param ListListenersRequest request
        :return: ListListenersResponse
        """
        return self.list_listeners_with_http_info(request)

    def list_listeners_with_http_info(self, request):
        """查询监听器列表

        查询监听器列表。支持过滤查询和分页查询。可以通过监听器ID、协议类型、监听端口号、关联的后端云服务器的IP等查询监听器。

        :param ListListenersRequest request
        :return: ListListenersResponse
        """

        all_params = ['limit', 'marker', 'page_reverse', 'id', 'name', 'description', 'default_pool_id', 'default_tls_container_ref', 'client_ca_tls_container_ref', 'protocol', 'protocol_port', 'tls_ciphers_policy', 'member_timeout', 'client_timeout', 'keepalive_timeout', 'tls_container_id']
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
        if 'page_reverse' in local_var_params:
            query_params.append(('page_reverse', local_var_params['page_reverse']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'description' in local_var_params:
            query_params.append(('description', local_var_params['description']))
        if 'default_pool_id' in local_var_params:
            query_params.append(('default_pool_id', local_var_params['default_pool_id']))
        if 'default_tls_container_ref' in local_var_params:
            query_params.append(('default_tls_container_ref', local_var_params['default_tls_container_ref']))
        if 'client_ca_tls_container_ref' in local_var_params:
            query_params.append(('client_ca_tls_container_ref', local_var_params['client_ca_tls_container_ref']))
        if 'protocol' in local_var_params:
            query_params.append(('protocol', local_var_params['protocol']))
        if 'protocol_port' in local_var_params:
            query_params.append(('protocol_port', local_var_params['protocol_port']))
        if 'tls_ciphers_policy' in local_var_params:
            query_params.append(('tls_ciphers_policy', local_var_params['tls_ciphers_policy']))
        if 'member_timeout' in local_var_params:
            query_params.append(('member_timeout', local_var_params['member_timeout']))
        if 'client_timeout' in local_var_params:
            query_params.append(('client_timeout', local_var_params['client_timeout']))
        if 'keepalive_timeout' in local_var_params:
            query_params.append(('keepalive_timeout', local_var_params['keepalive_timeout']))
        if 'tls_container_id' in local_var_params:
            query_params.append(('tls_container_id', local_var_params['tls_container_id']))

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
            resource_path='/v2/{project_id}/elb/listeners',
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


    def list_loadbalancers(self, request):
        """查询负载均衡列表

        查询负载均衡器列表。

        :param ListLoadbalancersRequest request
        :return: ListLoadbalancersResponse
        """
        return self.list_loadbalancers_with_http_info(request)

    def list_loadbalancers_with_http_info(self, request):
        """查询负载均衡列表

        查询负载均衡器列表。

        :param ListLoadbalancersRequest request
        :return: ListLoadbalancersResponse
        """

        all_params = ['limit', 'marker', 'page_reverse', 'id', 'description', 'name', 'operating_status', 'provisioning_status', 'vip_address', 'vip_port_id', 'vip_subnet_id', 'vpc_id', 'enterprise_project_id', 'admin_state_up', 'member_address', 'member_device_id']
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
        if 'page_reverse' in local_var_params:
            query_params.append(('page_reverse', local_var_params['page_reverse']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'description' in local_var_params:
            query_params.append(('description', local_var_params['description']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'operating_status' in local_var_params:
            query_params.append(('operating_status', local_var_params['operating_status']))
        if 'provisioning_status' in local_var_params:
            query_params.append(('provisioning_status', local_var_params['provisioning_status']))
        if 'vip_address' in local_var_params:
            query_params.append(('vip_address', local_var_params['vip_address']))
        if 'vip_port_id' in local_var_params:
            query_params.append(('vip_port_id', local_var_params['vip_port_id']))
        if 'vip_subnet_id' in local_var_params:
            query_params.append(('vip_subnet_id', local_var_params['vip_subnet_id']))
        if 'vpc_id' in local_var_params:
            query_params.append(('vpc_id', local_var_params['vpc_id']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'admin_state_up' in local_var_params:
            query_params.append(('admin_state_up', local_var_params['admin_state_up']))
        if 'member_address' in local_var_params:
            query_params.append(('member_address', local_var_params['member_address']))
        if 'member_device_id' in local_var_params:
            query_params.append(('member_device_id', local_var_params['member_device_id']))

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
            resource_path='/v2/{project_id}/elb/loadbalancers',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListLoadbalancersResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_menbers(self, request):
        """查询后端云服务器列表

        添加属于某个后端云服务器组的后端云服务器。

        :param ListMenbersRequest request
        :return: ListMenbersResponse
        """
        return self.list_menbers_with_http_info(request)

    def list_menbers_with_http_info(self, request):
        """查询后端云服务器列表

        添加属于某个后端云服务器组的后端云服务器。

        :param ListMenbersRequest request
        :return: ListMenbersResponse
        """

        all_params = ['pool_id', 'limit', 'marker', 'page_reverse', 'id', 'name', 'address', 'protocol_port', 'subnet_id', 'admin_state_up', 'weight']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'pool_id' in local_var_params:
            path_params['pool_id'] = local_var_params['pool_id']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'page_reverse' in local_var_params:
            query_params.append(('page_reverse', local_var_params['page_reverse']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'address' in local_var_params:
            query_params.append(('address', local_var_params['address']))
        if 'protocol_port' in local_var_params:
            query_params.append(('protocol_port', local_var_params['protocol_port']))
        if 'subnet_id' in local_var_params:
            query_params.append(('subnet_id', local_var_params['subnet_id']))
        if 'admin_state_up' in local_var_params:
            query_params.append(('admin_state_up', local_var_params['admin_state_up']))
        if 'weight' in local_var_params:
            query_params.append(('weight', local_var_params['weight']))

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
            resource_path='/v2/{project_id}/elb/pools/{pool_id}/members',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListMenbersResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_pools(self, request):
        """查询后端云服务器组列表

        查询后端云服务器组列表。

        :param ListPoolsRequest request
        :return: ListPoolsResponse
        """
        return self.list_pools_with_http_info(request)

    def list_pools_with_http_info(self, request):
        """查询后端云服务器组列表

        查询后端云服务器组列表。

        :param ListPoolsRequest request
        :return: ListPoolsResponse
        """

        all_params = ['limit', 'marker', 'page_reverse', 'id', 'name', 'description', 'healthmonitor_id', 'loadbalancer_id', 'protocol', 'lb_algorithm', 'member_address', 'member_device_id', 'enterprise_project_id']
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
        if 'page_reverse' in local_var_params:
            query_params.append(('page_reverse', local_var_params['page_reverse']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'description' in local_var_params:
            query_params.append(('description', local_var_params['description']))
        if 'healthmonitor_id' in local_var_params:
            query_params.append(('healthmonitor_id', local_var_params['healthmonitor_id']))
        if 'loadbalancer_id' in local_var_params:
            query_params.append(('loadbalancer_id', local_var_params['loadbalancer_id']))
        if 'protocol' in local_var_params:
            query_params.append(('protocol', local_var_params['protocol']))
        if 'lb_algorithm' in local_var_params:
            query_params.append(('lb_algorithm', local_var_params['lb_algorithm']))
        if 'member_address' in local_var_params:
            query_params.append(('member_address', local_var_params['member_address']))
        if 'member_device_id' in local_var_params:
            query_params.append(('member_device_id', local_var_params['member_device_id']))
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
            resource_path='/v2/{project_id}/elb/pools',
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


    def list_whitelists(self, request):
        """查询白名单列表

        查询白名单，支持过滤查询和分页查询。

        :param ListWhitelistsRequest request
        :return: ListWhitelistsResponse
        """
        return self.list_whitelists_with_http_info(request)

    def list_whitelists_with_http_info(self, request):
        """查询白名单列表

        查询白名单，支持过滤查询和分页查询。

        :param ListWhitelistsRequest request
        :return: ListWhitelistsResponse
        """

        all_params = ['limit', 'marker', 'page_reverse', 'id', 'enable_whitelist', 'listener_id', 'whitelist']
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
        if 'page_reverse' in local_var_params:
            query_params.append(('page_reverse', local_var_params['page_reverse']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'enable_whitelist' in local_var_params:
            query_params.append(('enable_whitelist', local_var_params['enable_whitelist']))
        if 'listener_id' in local_var_params:
            query_params.append(('listener_id', local_var_params['listener_id']))
        if 'whitelist' in local_var_params:
            query_params.append(('whitelist', local_var_params['whitelist']))

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
            resource_path='/v2/{project_id}/elb/whitelists',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListWhitelistsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_healthmonitors(self, request):
        """查询健康检查详情

        根据指定ID查询健康检查详情。

        :param ShowHealthmonitorsRequest request
        :return: ShowHealthmonitorsResponse
        """
        return self.show_healthmonitors_with_http_info(request)

    def show_healthmonitors_with_http_info(self, request):
        """查询健康检查详情

        根据指定ID查询健康检查详情。

        :param ShowHealthmonitorsRequest request
        :return: ShowHealthmonitorsResponse
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

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/elb/healthmonitors/{healthmonitor_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowHealthmonitorsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_l7policy(self, request):
        """查询转发策略详情

        根据指定ID查询转发策略详情。

        :param ShowL7policyRequest request
        :return: ShowL7policyResponse
        """
        return self.show_l7policy_with_http_info(request)

    def show_l7policy_with_http_info(self, request):
        """查询转发策略详情

        根据指定ID查询转发策略详情。

        :param ShowL7policyRequest request
        :return: ShowL7policyResponse
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

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/elb/l7policies/{l7policy_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowL7policyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_l7rule(self, request):
        """查询转发规则详情

        根据指定ID查询某转发策略下关联的转发规则详情。

        :param ShowL7ruleRequest request
        :return: ShowL7ruleResponse
        """
        return self.show_l7rule_with_http_info(request)

    def show_l7rule_with_http_info(self, request):
        """查询转发规则详情

        根据指定ID查询某转发策略下关联的转发规则详情。

        :param ShowL7ruleRequest request
        :return: ShowL7ruleResponse
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

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/elb/l7policies/{l7policy_id}/rules/{l7rule_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowL7ruleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_listener(self, request):
        """查询监听器详情

        根据指定ID查询监听器详情。

        :param ShowListenerRequest request
        :return: ShowListenerResponse
        """
        return self.show_listener_with_http_info(request)

    def show_listener_with_http_info(self, request):
        """查询监听器详情

        根据指定ID查询监听器详情。

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

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/elb/listeners/{listener_id}',
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


    def show_loadbalancer(self, request):
        """查询负载均衡详情

        根据指定负载均衡器ID查询负载均衡器详情

        :param ShowLoadbalancerRequest request
        :return: ShowLoadbalancerResponse
        """
        return self.show_loadbalancer_with_http_info(request)

    def show_loadbalancer_with_http_info(self, request):
        """查询负载均衡详情

        根据指定负载均衡器ID查询负载均衡器详情

        :param ShowLoadbalancerRequest request
        :return: ShowLoadbalancerResponse
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

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/elb/loadbalancers/{loadbalancer_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowLoadbalancerResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_loadbalancers_status(self, request):
        """查询负载均衡状态树

        查询负载均衡器状态树。可通过该接口查询负载均衡器关联的监听器、后端云服务器组、后端云服务器、健康检查、转发策略、转发规则的主要信息，了解负载均衡器下资源的拓扑情况。

        :param ShowLoadbalancersStatusRequest request
        :return: ShowLoadbalancersStatusResponse
        """
        return self.show_loadbalancers_status_with_http_info(request)

    def show_loadbalancers_status_with_http_info(self, request):
        """查询负载均衡状态树

        查询负载均衡器状态树。可通过该接口查询负载均衡器关联的监听器、后端云服务器组、后端云服务器、健康检查、转发策略、转发规则的主要信息，了解负载均衡器下资源的拓扑情况。

        :param ShowLoadbalancersStatusRequest request
        :return: ShowLoadbalancersStatusResponse
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

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/elb/loadbalancers/{loadbalancer_id}/statuses',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowLoadbalancersStatusResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_member(self, request):
        """查询后端云服务器详情

        根据指定ID查询后端云服务器详情。

        :param ShowMemberRequest request
        :return: ShowMemberResponse
        """
        return self.show_member_with_http_info(request)

    def show_member_with_http_info(self, request):
        """查询后端云服务器详情

        根据指定ID查询后端云服务器详情。

        :param ShowMemberRequest request
        :return: ShowMemberResponse
        """

        all_params = ['pool_id', 'member_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v2/{project_id}/elb/pools/{pool_id}/members/{member_id}',
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


    def show_pool(self, request):
        """查询后端云服务器组详情

        根据指定ID查询后端云服务器组详情。

        :param ShowPoolRequest request
        :return: ShowPoolResponse
        """
        return self.show_pool_with_http_info(request)

    def show_pool_with_http_info(self, request):
        """查询后端云服务器组详情

        根据指定ID查询后端云服务器组详情。

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

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/elb/pools/{pool_id}',
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


    def show_whitelist(self, request):
        """查询白名单详情

        根据指定ID查询白名单详情。

        :param ShowWhitelistRequest request
        :return: ShowWhitelistResponse
        """
        return self.show_whitelist_with_http_info(request)

    def show_whitelist_with_http_info(self, request):
        """查询白名单详情

        根据指定ID查询白名单详情。

        :param ShowWhitelistRequest request
        :return: ShowWhitelistResponse
        """

        all_params = ['whitelist_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'whitelist_id' in local_var_params:
            path_params['whitelist_id'] = local_var_params['whitelist_id']

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
            resource_path='/v2/{project_id}/elb/whitelists/{whitelist_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowWhitelistResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_healthmonitor(self, request):
        """更新健康检查

        更新健康检查

        :param UpdateHealthmonitorRequest request
        :return: UpdateHealthmonitorResponse
        """
        return self.update_healthmonitor_with_http_info(request)

    def update_healthmonitor_with_http_info(self, request):
        """更新健康检查

        更新健康检查

        :param UpdateHealthmonitorRequest request
        :return: UpdateHealthmonitorResponse
        """

        all_params = ['healthmonitor_id', 'update_healthmonitor_request_body']
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
            resource_path='/v2/{project_id}/elb/healthmonitors/{healthmonitor_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateHealthmonitorResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_l7policies(self, request):
        """更新转发策略

        更新转发策略

        :param UpdateL7policiesRequest request
        :return: UpdateL7policiesResponse
        """
        return self.update_l7policies_with_http_info(request)

    def update_l7policies_with_http_info(self, request):
        """更新转发策略

        更新转发策略

        :param UpdateL7policiesRequest request
        :return: UpdateL7policiesResponse
        """

        all_params = ['l7policy_id', 'update_l7policies_request_body']
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
            resource_path='/v2/{project_id}/elb/l7policies/{l7policy_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateL7policiesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_l7rule(self, request):
        """更新转发规则

        更新指定的转发规则

        :param UpdateL7ruleRequest request
        :return: UpdateL7ruleResponse
        """
        return self.update_l7rule_with_http_info(request)

    def update_l7rule_with_http_info(self, request):
        """更新转发规则

        更新指定的转发规则

        :param UpdateL7ruleRequest request
        :return: UpdateL7ruleResponse
        """

        all_params = ['l7policy_id', 'l7rule_id', 'update_l7rule_request_body']
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
            resource_path='/v2/{project_id}/elb/l7policies/{l7policy_id}/rules/{l7rule_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateL7ruleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_listener(self, request):
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
            resource_path='/v2/{project_id}/elb/listeners/{listener_id}',
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


    def update_loadbalancer(self, request):
        """更新负载均衡器

        更新负载均衡器。

        :param UpdateLoadbalancerRequest request
        :return: UpdateLoadbalancerResponse
        """
        return self.update_loadbalancer_with_http_info(request)

    def update_loadbalancer_with_http_info(self, request):
        """更新负载均衡器

        更新负载均衡器。

        :param UpdateLoadbalancerRequest request
        :return: UpdateLoadbalancerResponse
        """

        all_params = ['loadbalancer_id', 'update_loadbalancer_request_body']
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
            resource_path='/v2/{project_id}/elb/loadbalancers/{loadbalancer_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateLoadbalancerResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_member(self, request):
        """更新后端云服务器

        更新后端云服务器

        :param UpdateMemberRequest request
        :return: UpdateMemberResponse
        """
        return self.update_member_with_http_info(request)

    def update_member_with_http_info(self, request):
        """更新后端云服务器

        更新后端云服务器

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
            resource_path='/v2/{project_id}/elb/pools/{pool_id}/members/{member_id}',
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


    def update_pool(self, request):
        """更新后端云服务器组

        更新后端云服务器组。

        :param UpdatePoolRequest request
        :return: UpdatePoolResponse
        """
        return self.update_pool_with_http_info(request)

    def update_pool_with_http_info(self, request):
        """更新后端云服务器组

        更新后端云服务器组。

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
            resource_path='/v2/{project_id}/elb/pools/{pool_id}',
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


    def update_whitelist(self, request):
        """更新白名单

        更新白名单。可以打开或关闭白名单，或更新访问控制的IP。

        :param UpdateWhitelistRequest request
        :return: UpdateWhitelistResponse
        """
        return self.update_whitelist_with_http_info(request)

    def update_whitelist_with_http_info(self, request):
        """更新白名单

        更新白名单。可以打开或关闭白名单，或更新访问控制的IP。

        :param UpdateWhitelistRequest request
        :return: UpdateWhitelistResponse
        """

        all_params = ['whitelist_id', 'update_whitelist_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'whitelist_id' in local_var_params:
            path_params['whitelist_id'] = local_var_params['whitelist_id']

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
            resource_path='/v2/{project_id}/elb/whitelists/{whitelist_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateWhitelistResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_certificate(self, request):
        """创建SSL证书

        创建SSL证书。将监听器和SSL证书绑定后，可以通过负载均衡器实现服务端认证，后端服务器只要提供HTTP服务就能实现安全可靠的连接。

        :param CreateCertificateRequest request
        :return: CreateCertificateResponse
        """
        return self.create_certificate_with_http_info(request)

    def create_certificate_with_http_info(self, request):
        """创建SSL证书

        创建SSL证书。将监听器和SSL证书绑定后，可以通过负载均衡器实现服务端认证，后端服务器只要提供HTTP服务就能实现安全可靠的连接。

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
            resource_path='/v2/{project_id}/elb/certificates',
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


    def delete_certificate(self, request):
        """删除SSL证书

        删除指定的SSL证书

        :param DeleteCertificateRequest request
        :return: DeleteCertificateResponse
        """
        return self.delete_certificate_with_http_info(request)

    def delete_certificate_with_http_info(self, request):
        """删除SSL证书

        删除指定的SSL证书

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

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/elb/certificates/{certificate_id}',
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


    def list_certificates(self, request):
        """查询SSL证书列表

        查询SSL证书。支持过滤查询和分页查询。

        :param ListCertificatesRequest request
        :return: ListCertificatesResponse
        """
        return self.list_certificates_with_http_info(request)

    def list_certificates_with_http_info(self, request):
        """查询SSL证书列表

        查询SSL证书。支持过滤查询和分页查询。

        :param ListCertificatesRequest request
        :return: ListCertificatesResponse
        """

        all_params = ['limit', 'marker', 'page_reverse', 'id', 'name', 'description', 'type', 'domain', 'private_key', 'certificate']
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
        if 'page_reverse' in local_var_params:
            query_params.append(('page_reverse', local_var_params['page_reverse']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'description' in local_var_params:
            query_params.append(('description', local_var_params['description']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'domain' in local_var_params:
            query_params.append(('domain', local_var_params['domain']))
        if 'private_key' in local_var_params:
            query_params.append(('private_key', local_var_params['private_key']))
        if 'certificate' in local_var_params:
            query_params.append(('certificate', local_var_params['certificate']))

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
            resource_path='/v2/{project_id}/elb/certificates',
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


    def show_certificate(self, request):
        """查询SSL证书详情

        查询指定SSL证书的详情信息。

        :param ShowCertificateRequest request
        :return: ShowCertificateResponse
        """
        return self.show_certificate_with_http_info(request)

    def show_certificate_with_http_info(self, request):
        """查询SSL证书详情

        查询指定SSL证书的详情信息。

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

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/elb/certificates/{certificate_id}',
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


    def update_certificate(self, request):
        """更新SSL证书

        更新指定的SSL证书

        :param UpdateCertificateRequest request
        :return: UpdateCertificateResponse
        """
        return self.update_certificate_with_http_info(request)

    def update_certificate_with_http_info(self, request):
        """更新SSL证书

        更新指定的SSL证书

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
            resource_path='/v2/{project_id}/elb/certificates/{certificate_id}',
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

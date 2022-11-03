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


class WafAsyncClient(Client):
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
        super(WafAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkwaf.v1.model")
        self.preset_headers = {'User-Agent': 'HuaweiCloud-SDK-Python'}

    @classmethod
    def new_builder(cls, clazz=None):
        if clazz is None:
            return ClientBuilder(cls)

        if clazz.__name__ != "WafClient":
            raise TypeError("client type error, support client type is WafClient")

        return ClientBuilder(clazz)

    def apply_certificate_to_host_async(self, request):
        """绑定证书到域名

        绑定证书到域名
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ApplyCertificateToHost
        :type request: :class:`huaweicloudsdkwaf.v1.ApplyCertificateToHostRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.ApplyCertificateToHostResponse`
        """
        return self.apply_certificate_to_host_with_http_info(request)

    def apply_certificate_to_host_with_http_info(self, request):
        all_params = ['certificate_id', 'enterprise_project_id', 'apply_certificate_to_host_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'certificate_id' in local_var_params:
            path_params['certificate_id'] = local_var_params['certificate_id']

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

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
            resource_path='/v1/{project_id}/waf/certificate/{certificate_id}/apply-to-hosts',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ApplyCertificateToHostResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_anti_tamper_rule_async(self, request):
        """创建防篡改规则

        创建防篡改规则
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for CreateAntiTamperRule
        :type request: :class:`huaweicloudsdkwaf.v1.CreateAntiTamperRuleRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.CreateAntiTamperRuleResponse`
        """
        return self.create_anti_tamper_rule_with_http_info(request)

    def create_anti_tamper_rule_with_http_info(self, request):
        all_params = ['policy_id', 'create_anti_tamper_rule_request_body', 'enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

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
            resource_path='/v1/{project_id}/waf/policy/{policy_id}/antitamper',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateAntiTamperRuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_certificate_async(self, request):
        """创建证书

        创建证书
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for CreateCertificate
        :type request: :class:`huaweicloudsdkwaf.v1.CreateCertificateRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.CreateCertificateResponse`
        """
        return self.create_certificate_with_http_info(request)

    def create_certificate_with_http_info(self, request):
        all_params = ['create_certificate_request_body', 'enterprise_project_id']
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
            resource_path='/v1/{project_id}/waf/certificate',
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

    def create_geoip_rule_async(self, request):
        """创建地理位置控制规则

        创建地理位置控制规则
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for CreateGeoipRule
        :type request: :class:`huaweicloudsdkwaf.v1.CreateGeoipRuleRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.CreateGeoipRuleResponse`
        """
        return self.create_geoip_rule_with_http_info(request)

    def create_geoip_rule_with_http_info(self, request):
        all_params = ['policy_id', 'create_geo_ip_rule_request_body', 'enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

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
            resource_path='/v1/{project_id}/waf/policy/{policy_id}/geoip',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateGeoipRuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_host_async(self, request):
        """创建云模式防护域名

        创建云模式防护域名
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for CreateHost
        :type request: :class:`huaweicloudsdkwaf.v1.CreateHostRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.CreateHostResponse`
        """
        return self.create_host_with_http_info(request)

    def create_host_with_http_info(self, request):
        all_params = ['create_host_request_body', 'enterprise_project_id']
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
            resource_path='/v1/{project_id}/waf/instance',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateHostResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_ignore_rule_async(self, request):
        """创建全局白名单(原误报屏蔽)规则

        创建全局白名单(原误报屏蔽)规则
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for CreateIgnoreRule
        :type request: :class:`huaweicloudsdkwaf.v1.CreateIgnoreRuleRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.CreateIgnoreRuleResponse`
        """
        return self.create_ignore_rule_with_http_info(request)

    def create_ignore_rule_with_http_info(self, request):
        all_params = ['policy_id', 'create_ignore_rule_request_body', 'enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

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
            resource_path='/v1/{project_id}/waf/policy/{policy_id}/ignore',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateIgnoreRuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_instance_async(self, request):
        """创建WAF独享引擎实例

        创建WAF独享引擎实例
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for CreateInstance
        :type request: :class:`huaweicloudsdkwaf.v1.CreateInstanceRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.CreateInstanceResponse`
        """
        return self.create_instance_with_http_info(request)

    def create_instance_with_http_info(self, request):
        all_params = ['create_instance_request_body', 'enterprise_project_id']
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
            resource_path='/v1/{project_id}/premium-waf/instance',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateInstanceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_ip_group_async(self, request):
        """创建ip地址组

        创建ip地址组
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for CreateIpGroup
        :type request: :class:`huaweicloudsdkwaf.v1.CreateIpGroupRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.CreateIpGroupResponse`
        """
        return self.create_ip_group_with_http_info(request)

    def create_ip_group_with_http_info(self, request):
        all_params = ['create_ip_group_request_body', 'enterprise_project_id']
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
            resource_path='/v1/{project_id}/waf/ip-groups',
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

    def create_policy_async(self, request):
        """创建防护策略

        创建防护策略，系统会在生成策略时配置一些默认的配置项，如果需要修改策略的默认配置项需要通过调用更新防护策略接口实现
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for CreatePolicy
        :type request: :class:`huaweicloudsdkwaf.v1.CreatePolicyRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.CreatePolicyResponse`
        """
        return self.create_policy_with_http_info(request)

    def create_policy_with_http_info(self, request):
        all_params = ['create_policy_request_body', 'enterprise_project_id']
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
            resource_path='/v1/{project_id}/waf/policy',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreatePolicyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_premium_host_async(self, request):
        """创建独享模式域名

        创建独享模式域名
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for CreatePremiumHost
        :type request: :class:`huaweicloudsdkwaf.v1.CreatePremiumHostRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.CreatePremiumHostResponse`
        """
        return self.create_premium_host_with_http_info(request)

    def create_premium_host_with_http_info(self, request):
        all_params = ['enterprise_project_id', 'create_premium_host_request_body']
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
            resource_path='/v1/{project_id}/premium-waf/host',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreatePremiumHostResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_privacy_rule_async(self, request):
        """创建隐私屏蔽防护规则

        创建隐私屏蔽防护规则
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for CreatePrivacyRule
        :type request: :class:`huaweicloudsdkwaf.v1.CreatePrivacyRuleRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.CreatePrivacyRuleResponse`
        """
        return self.create_privacy_rule_with_http_info(request)

    def create_privacy_rule_with_http_info(self, request):
        all_params = ['policy_id', 'create_privacy_rule_request_body', 'enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

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
            resource_path='/v1/{project_id}/waf/policy/{policy_id}/privacy',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreatePrivacyRuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_value_list_async(self, request):
        """创建引用表

        创建引用表，引用表能够被CC攻击防护规则和精准访问防护中的规则所引用。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for CreateValueList
        :type request: :class:`huaweicloudsdkwaf.v1.CreateValueListRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.CreateValueListResponse`
        """
        return self.create_value_list_with_http_info(request)

    def create_value_list_with_http_info(self, request):
        all_params = ['create_value_list_request_body', 'enterprise_project_id']
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
            resource_path='/v1/{project_id}/waf/valuelist',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateValueListResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_whiteblackip_rule_async(self, request):
        """创建黑白名单规则

        创建黑白名单规则
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for CreateWhiteblackipRule
        :type request: :class:`huaweicloudsdkwaf.v1.CreateWhiteblackipRuleRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.CreateWhiteblackipRuleResponse`
        """
        return self.create_whiteblackip_rule_with_http_info(request)

    def create_whiteblackip_rule_with_http_info(self, request):
        all_params = ['policy_id', 'create_whiteblackip_rule_request_body', 'enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

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
            resource_path='/v1/{project_id}/waf/policy/{policy_id}/whiteblackip',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateWhiteblackipRuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_antitamper_rule_async(self, request):
        """删除防篡改防护规则

        删除防篡改防护规则
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for DeleteAntitamperRule
        :type request: :class:`huaweicloudsdkwaf.v1.DeleteAntitamperRuleRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.DeleteAntitamperRuleResponse`
        """
        return self.delete_antitamper_rule_with_http_info(request)

    def delete_antitamper_rule_with_http_info(self, request):
        all_params = ['policy_id', 'rule_id', 'enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']
        if 'rule_id' in local_var_params:
            path_params['rule_id'] = local_var_params['rule_id']

        query_params = []
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
            resource_path='/v1/{project_id}/waf/policy/{policy_id}/antitamper/{rule_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteAntitamperRuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_certificate_async(self, request):
        """删除证书

        删除证书
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for DeleteCertificate
        :type request: :class:`huaweicloudsdkwaf.v1.DeleteCertificateRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.DeleteCertificateResponse`
        """
        return self.delete_certificate_with_http_info(request)

    def delete_certificate_with_http_info(self, request):
        all_params = ['certificate_id', 'enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'certificate_id' in local_var_params:
            path_params['certificate_id'] = local_var_params['certificate_id']

        query_params = []
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
            resource_path='/v1/{project_id}/waf/certificate/{certificate_id}',
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

    def delete_geoip_rule_async(self, request):
        """删除地理位置控制防护规则

        删除地理位置控制防护规则
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for DeleteGeoipRule
        :type request: :class:`huaweicloudsdkwaf.v1.DeleteGeoipRuleRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.DeleteGeoipRuleResponse`
        """
        return self.delete_geoip_rule_with_http_info(request)

    def delete_geoip_rule_with_http_info(self, request):
        all_params = ['policy_id', 'rule_id', 'enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']
        if 'rule_id' in local_var_params:
            path_params['rule_id'] = local_var_params['rule_id']

        query_params = []
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
            resource_path='/v1/{project_id}/waf/policy/{policy_id}/geoip/{rule_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteGeoipRuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_host_async(self, request):
        """删除云模式防护域名

        删除云模式防护域名
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for DeleteHost
        :type request: :class:`huaweicloudsdkwaf.v1.DeleteHostRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.DeleteHostResponse`
        """
        return self.delete_host_with_http_info(request)

    def delete_host_with_http_info(self, request):
        all_params = ['instance_id', 'enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
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
            resource_path='/v1/{project_id}/waf/instance/{instance_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteHostResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_ignore_rule_async(self, request):
        """删除全局白名单(原误报屏蔽)防护规则

        删除全局白名单(原误报屏蔽)防护规则
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for DeleteIgnoreRule
        :type request: :class:`huaweicloudsdkwaf.v1.DeleteIgnoreRuleRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.DeleteIgnoreRuleResponse`
        """
        return self.delete_ignore_rule_with_http_info(request)

    def delete_ignore_rule_with_http_info(self, request):
        all_params = ['policy_id', 'rule_id', 'enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']
        if 'rule_id' in local_var_params:
            path_params['rule_id'] = local_var_params['rule_id']

        query_params = []
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
            resource_path='/v1/{project_id}/waf/policy/{policy_id}/ignore/{rule_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteIgnoreRuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_instance_async(self, request):
        """删除WAF独享引擎信息

        删除WAF独享引擎信息
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for DeleteInstance
        :type request: :class:`huaweicloudsdkwaf.v1.DeleteInstanceRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.DeleteInstanceResponse`
        """
        return self.delete_instance_with_http_info(request)

    def delete_instance_with_http_info(self, request):
        all_params = ['instance_id', 'enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
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
            resource_path='/v1/{project_id}/premium-waf/instance/{instance_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteInstanceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_ip_group_async(self, request):
        """删除ip地址组

        删除ip地址组
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for DeleteIpGroup
        :type request: :class:`huaweicloudsdkwaf.v1.DeleteIpGroupRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.DeleteIpGroupResponse`
        """
        return self.delete_ip_group_with_http_info(request)

    def delete_ip_group_with_http_info(self, request):
        all_params = ['id', 'enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

        query_params = []
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
            resource_path='/v1/{project_id}/waf/ip-group/{id}',
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

    def delete_policy_async(self, request):
        """删除防护策略

        删除防护策略，若策略正在使用，则需要先接解除域名与策略的绑定关系才能删除策略。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for DeletePolicy
        :type request: :class:`huaweicloudsdkwaf.v1.DeletePolicyRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.DeletePolicyResponse`
        """
        return self.delete_policy_with_http_info(request)

    def delete_policy_with_http_info(self, request):
        all_params = ['policy_id', 'enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']

        query_params = []
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
            resource_path='/v1/{project_id}/waf/policy/{policy_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeletePolicyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_premium_host_async(self, request):
        """删除独享模式域名

        删除独享模式域名
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for DeletePremiumHost
        :type request: :class:`huaweicloudsdkwaf.v1.DeletePremiumHostRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.DeletePremiumHostResponse`
        """
        return self.delete_premium_host_with_http_info(request)

    def delete_premium_host_with_http_info(self, request):
        all_params = ['host_id', 'enterprise_project_id', 'keep_policy']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'host_id' in local_var_params:
            path_params['host_id'] = local_var_params['host_id']

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'keep_policy' in local_var_params:
            query_params.append(('keepPolicy', local_var_params['keep_policy']))

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
            resource_path='/v1/{project_id}/premium-waf/host/{host_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeletePremiumHostResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_privacy_rule_async(self, request):
        """删除隐私屏蔽防护规则

        删除隐私屏蔽防护规则
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for DeletePrivacyRule
        :type request: :class:`huaweicloudsdkwaf.v1.DeletePrivacyRuleRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.DeletePrivacyRuleResponse`
        """
        return self.delete_privacy_rule_with_http_info(request)

    def delete_privacy_rule_with_http_info(self, request):
        all_params = ['policy_id', 'rule_id', 'enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']
        if 'rule_id' in local_var_params:
            path_params['rule_id'] = local_var_params['rule_id']

        query_params = []
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
            resource_path='/v1/{project_id}/waf/policy/{policy_id}/privacy/{rule_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeletePrivacyRuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_value_list_async(self, request):
        """删除引用表

        删除引用表
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for DeleteValueList
        :type request: :class:`huaweicloudsdkwaf.v1.DeleteValueListRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.DeleteValueListResponse`
        """
        return self.delete_value_list_with_http_info(request)

    def delete_value_list_with_http_info(self, request):
        all_params = ['valuelistid', 'enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'valuelistid' in local_var_params:
            path_params['valuelistid'] = local_var_params['valuelistid']

        query_params = []
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
            resource_path='/v1/{project_id}/waf/valuelist/{valuelistid}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteValueListResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_white_black_ip_rule_async(self, request):
        """删除黑白名单防护规则

        删除黑白名单防护规则
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for DeleteWhiteBlackIpRule
        :type request: :class:`huaweicloudsdkwaf.v1.DeleteWhiteBlackIpRuleRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.DeleteWhiteBlackIpRuleResponse`
        """
        return self.delete_white_black_ip_rule_with_http_info(request)

    def delete_white_black_ip_rule_with_http_info(self, request):
        all_params = ['policy_id', 'rule_id', 'enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']
        if 'rule_id' in local_var_params:
            path_params['rule_id'] = local_var_params['rule_id']

        query_params = []
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
            resource_path='/v1/{project_id}/waf/policy/{policy_id}/whiteblackip/{rule_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteWhiteBlackIpRuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_antitamper_rule_async(self, request):
        """查询防篡改规则列表

        查询防篡改规则列表
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListAntitamperRule
        :type request: :class:`huaweicloudsdkwaf.v1.ListAntitamperRuleRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.ListAntitamperRuleResponse`
        """
        return self.list_antitamper_rule_with_http_info(request)

    def list_antitamper_rule_with_http_info(self, request):
        all_params = ['policy_id', 'enterprise_project_id', 'page', 'pagesize']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'page' in local_var_params:
            query_params.append(('page', local_var_params['page']))
        if 'pagesize' in local_var_params:
            query_params.append(('pagesize', local_var_params['pagesize']))

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
            resource_path='/v1/{project_id}/waf/policy/{policy_id}/antitamper',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListAntitamperRuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_bandwidth_timeline_async(self, request):
        """查询安全统计带宽数据

        查询安全统计带宽数据。需要注意的是，安全统计相关的接口，暂时不能支持任意时间的查询。只能支持 console上显示的 昨天，今天，3天，7天和30天 数据查询。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListBandwidthTimeline
        :type request: :class:`huaweicloudsdkwaf.v1.ListBandwidthTimelineRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.ListBandwidthTimelineResponse`
        """
        return self.list_bandwidth_timeline_with_http_info(request)

    def list_bandwidth_timeline_with_http_info(self, request):
        all_params = ['_from', 'to', 'enterprise_project_id', 'hosts', 'instances', 'group_by']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if '_from' in local_var_params:
            query_params.append(('from', local_var_params['_from']))
        if 'to' in local_var_params:
            query_params.append(('to', local_var_params['to']))
        if 'hosts' in local_var_params:
            query_params.append(('hosts', local_var_params['hosts']))
        if 'instances' in local_var_params:
            query_params.append(('instances', local_var_params['instances']))
        if 'group_by' in local_var_params:
            query_params.append(('group_by', local_var_params['group_by']))

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
            resource_path='/v1/{project_id}/waf/overviews/bandwidth/timeline',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListBandwidthTimelineResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_certificates_async(self, request):
        """查询证书列表

        查询证书列表
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListCertificates
        :type request: :class:`huaweicloudsdkwaf.v1.ListCertificatesRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.ListCertificatesResponse`
        """
        return self.list_certificates_with_http_info(request)

    def list_certificates_with_http_info(self, request):
        all_params = ['enterprise_project_id', 'page', 'pagesize', 'name', 'host', 'exp_status']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'page' in local_var_params:
            query_params.append(('page', local_var_params['page']))
        if 'pagesize' in local_var_params:
            query_params.append(('pagesize', local_var_params['pagesize']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'host' in local_var_params:
            query_params.append(('host', local_var_params['host']))
        if 'exp_status' in local_var_params:
            query_params.append(('exp_status', local_var_params['exp_status']))

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
            resource_path='/v1/{project_id}/waf/certificate',
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

    def list_composite_hosts_async(self, request):
        """查询全部防护域名列表

        查询全部防护域名列表，包括云模式和独享模式
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListCompositeHosts
        :type request: :class:`huaweicloudsdkwaf.v1.ListCompositeHostsRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.ListCompositeHostsResponse`
        """
        return self.list_composite_hosts_with_http_info(request)

    def list_composite_hosts_with_http_info(self, request):
        all_params = ['enterprise_project_id', 'page', 'pagesize', 'hostname', 'policyname', 'protect_status', 'waf_type', 'is_https']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'page' in local_var_params:
            query_params.append(('page', local_var_params['page']))
        if 'pagesize' in local_var_params:
            query_params.append(('pagesize', local_var_params['pagesize']))
        if 'hostname' in local_var_params:
            query_params.append(('hostname', local_var_params['hostname']))
        if 'policyname' in local_var_params:
            query_params.append(('policyname', local_var_params['policyname']))
        if 'protect_status' in local_var_params:
            query_params.append(('protect_status', local_var_params['protect_status']))
        if 'waf_type' in local_var_params:
            query_params.append(('waf_type', local_var_params['waf_type']))
        if 'is_https' in local_var_params:
            query_params.append(('is_https', local_var_params['is_https']))

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
            resource_path='/v1/{project_id}/composite-waf/host',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListCompositeHostsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_event_async(self, request):
        """查询攻击事件列表

        查询攻击事件列表，该API暂时不支持查询全部防护事件，pagesize参数不可设为-1，由于性能原因，数据量越大消耗的内存越大，后端最多限制查询10000条数据，例如：自定义时间段内的数据超过了10000条，就无法查出page为101，pagesize为100之后的数据，需要调整时间区间，再进行查询
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListEvent
        :type request: :class:`huaweicloudsdkwaf.v1.ListEventRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.ListEventResponse`
        """
        return self.list_event_with_http_info(request)

    def list_event_with_http_info(self, request):
        all_params = ['enterprise_project_id', 'recent', '_from', 'to', 'attacks', 'hosts', 'page', 'pagesize']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'recent' in local_var_params:
            query_params.append(('recent', local_var_params['recent']))
        if '_from' in local_var_params:
            query_params.append(('from', local_var_params['_from']))
        if 'to' in local_var_params:
            query_params.append(('to', local_var_params['to']))
        if 'attacks' in local_var_params:
            query_params.append(('attacks', local_var_params['attacks']))
            collection_formats['attacks'] = 'csv'
        if 'hosts' in local_var_params:
            query_params.append(('hosts', local_var_params['hosts']))
            collection_formats['hosts'] = 'csv'
        if 'page' in local_var_params:
            query_params.append(('page', local_var_params['page']))
        if 'pagesize' in local_var_params:
            query_params.append(('pagesize', local_var_params['pagesize']))

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
            resource_path='/v1/{project_id}/waf/event',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListEventResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_geoip_rule_async(self, request):
        """查询地理位置访问控制规则列表

        查询地理位置访问控制规则列表
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListGeoipRule
        :type request: :class:`huaweicloudsdkwaf.v1.ListGeoipRuleRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.ListGeoipRuleResponse`
        """
        return self.list_geoip_rule_with_http_info(request)

    def list_geoip_rule_with_http_info(self, request):
        all_params = ['policy_id', 'enterprise_project_id', 'page', 'pagesize']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'page' in local_var_params:
            query_params.append(('page', local_var_params['page']))
        if 'pagesize' in local_var_params:
            query_params.append(('pagesize', local_var_params['pagesize']))

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
            resource_path='/v1/{project_id}/waf/policy/{policy_id}/geoip',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListGeoipRuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_host_async(self, request):
        """查询云模式防护域名列表

        查询云模式防护域名列表
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListHost
        :type request: :class:`huaweicloudsdkwaf.v1.ListHostRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.ListHostResponse`
        """
        return self.list_host_with_http_info(request)

    def list_host_with_http_info(self, request):
        all_params = ['enterprise_project_id', 'page', 'pagesize', 'hostname', 'policyname']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'page' in local_var_params:
            query_params.append(('page', local_var_params['page']))
        if 'pagesize' in local_var_params:
            query_params.append(('pagesize', local_var_params['pagesize']))
        if 'hostname' in local_var_params:
            query_params.append(('hostname', local_var_params['hostname']))
        if 'policyname' in local_var_params:
            query_params.append(('policyname', local_var_params['policyname']))

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
            resource_path='/v1/{project_id}/waf/instance',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListHostResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_host_route_async(self, request):
        """获取云模式域名路由信息

        返回路由信息
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListHostRoute
        :type request: :class:`huaweicloudsdkwaf.v1.ListHostRouteRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.ListHostRouteResponse`
        """
        return self.list_host_route_with_http_info(request)

    def list_host_route_with_http_info(self, request):
        all_params = ['instance_id', 'enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
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
            resource_path='/v1/{project_id}/waf/instance/{instance_id}/route',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListHostRouteResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_ignore_rule_async(self, request):
        """查询全局白名单(原误报屏蔽)规则列表

        查询全局白名单(原误报屏蔽)规则列表
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListIgnoreRule
        :type request: :class:`huaweicloudsdkwaf.v1.ListIgnoreRuleRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.ListIgnoreRuleResponse`
        """
        return self.list_ignore_rule_with_http_info(request)

    def list_ignore_rule_with_http_info(self, request):
        all_params = ['policy_id', 'enterprise_project_id', 'page', 'pagesize']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'page' in local_var_params:
            query_params.append(('page', local_var_params['page']))
        if 'pagesize' in local_var_params:
            query_params.append(('pagesize', local_var_params['pagesize']))

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
            resource_path='/v1/{project_id}/waf/policy/{policy_id}/ignore',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListIgnoreRuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_instance_async(self, request):
        """查询WAF独享引擎列表

        查询WAF独享引擎列表
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListInstance
        :type request: :class:`huaweicloudsdkwaf.v1.ListInstanceRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.ListInstanceResponse`
        """
        return self.list_instance_with_http_info(request)

    def list_instance_with_http_info(self, request):
        all_params = ['enterprise_project_id', 'page', 'pagesize', 'instancename']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'page' in local_var_params:
            query_params.append(('page', local_var_params['page']))
        if 'pagesize' in local_var_params:
            query_params.append(('pagesize', local_var_params['pagesize']))
        if 'instancename' in local_var_params:
            query_params.append(('instancename', local_var_params['instancename']))

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
            resource_path='/v1/{project_id}/premium-waf/instance',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListInstanceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_ip_group_async(self, request):
        """查询地址组列表

        查询地址组列表
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListIpGroup
        :type request: :class:`huaweicloudsdkwaf.v1.ListIpGroupRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.ListIpGroupResponse`
        """
        return self.list_ip_group_with_http_info(request)

    def list_ip_group_with_http_info(self, request):
        all_params = ['enterprise_project_id', 'page', 'pagesize', 'name', 'ip']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'page' in local_var_params:
            query_params.append(('page', local_var_params['page']))
        if 'pagesize' in local_var_params:
            query_params.append(('pagesize', local_var_params['pagesize']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'ip' in local_var_params:
            query_params.append(('ip', local_var_params['ip']))

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
            resource_path='/v1/{project_id}/waf/ip-groups',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListIpGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_overviews_classification_async(self, request):
        """查询安全总览分类统计top信息

        查询安全总览分类统计TOP信息，包含受攻击域名 、攻击源ip、受攻击URL、攻击来源区域、攻击事件分布。需要注意的是，安全总览相关的接口，暂时不能支持任意时间的查询。只能支持 console上显示的 昨天，今天，3天，7天和30天 数据查询。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListOverviewsClassification
        :type request: :class:`huaweicloudsdkwaf.v1.ListOverviewsClassificationRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.ListOverviewsClassificationResponse`
        """
        return self.list_overviews_classification_with_http_info(request)

    def list_overviews_classification_with_http_info(self, request):
        all_params = ['_from', 'to', 'enterprise_project_id', 'top', 'hosts', 'instances']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if '_from' in local_var_params:
            query_params.append(('from', local_var_params['_from']))
        if 'to' in local_var_params:
            query_params.append(('to', local_var_params['to']))
        if 'top' in local_var_params:
            query_params.append(('top', local_var_params['top']))
        if 'hosts' in local_var_params:
            query_params.append(('hosts', local_var_params['hosts']))
        if 'instances' in local_var_params:
            query_params.append(('instances', local_var_params['instances']))

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
            resource_path='/v1/{project_id}/waf/overviews/classification',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListOverviewsClassificationResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_policy_async(self, request):
        """查询防护策略列表

        查询防护策略列表
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListPolicy
        :type request: :class:`huaweicloudsdkwaf.v1.ListPolicyRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.ListPolicyResponse`
        """
        return self.list_policy_with_http_info(request)

    def list_policy_with_http_info(self, request):
        all_params = ['enterprise_project_id', 'page', 'pagesize', 'name']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'page' in local_var_params:
            query_params.append(('page', local_var_params['page']))
        if 'pagesize' in local_var_params:
            query_params.append(('pagesize', local_var_params['pagesize']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))

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
            resource_path='/v1/{project_id}/waf/policy',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListPolicyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_premium_host_async(self, request):
        """独享模式域名列表

        独享模式域名列表
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListPremiumHost
        :type request: :class:`huaweicloudsdkwaf.v1.ListPremiumHostRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.ListPremiumHostResponse`
        """
        return self.list_premium_host_with_http_info(request)

    def list_premium_host_with_http_info(self, request):
        all_params = ['enterprise_project_id', 'page', 'pagesize', 'hostname', 'policyname', 'protect_status']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'page' in local_var_params:
            query_params.append(('page', local_var_params['page']))
        if 'pagesize' in local_var_params:
            query_params.append(('pagesize', local_var_params['pagesize']))
        if 'hostname' in local_var_params:
            query_params.append(('hostname', local_var_params['hostname']))
        if 'policyname' in local_var_params:
            query_params.append(('policyname', local_var_params['policyname']))
        if 'protect_status' in local_var_params:
            query_params.append(('protect_status', local_var_params['protect_status']))

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
            resource_path='/v1/{project_id}/premium-waf/host',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListPremiumHostResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_privacy_rule_async(self, request):
        """查询隐私屏蔽防护规则

        查询隐私屏蔽防护规则
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListPrivacyRule
        :type request: :class:`huaweicloudsdkwaf.v1.ListPrivacyRuleRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.ListPrivacyRuleResponse`
        """
        return self.list_privacy_rule_with_http_info(request)

    def list_privacy_rule_with_http_info(self, request):
        all_params = ['policy_id', 'enterprise_project_id', 'page', 'pagesize']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'page' in local_var_params:
            query_params.append(('page', local_var_params['page']))
        if 'pagesize' in local_var_params:
            query_params.append(('pagesize', local_var_params['pagesize']))

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
            resource_path='/v1/{project_id}/waf/policy/{policy_id}/privacy',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListPrivacyRuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_qps_timeline_async(self, request):
        """查询安全统计qps次数

        查询安全统计qps次数。需要注意的是，安全统计相关的接口，暂时不能支持任意时间的查询。只能支持 console上显示的 昨天，今天，3天，7天和30天 数据查询。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListQpsTimeline
        :type request: :class:`huaweicloudsdkwaf.v1.ListQpsTimelineRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.ListQpsTimelineResponse`
        """
        return self.list_qps_timeline_with_http_info(request)

    def list_qps_timeline_with_http_info(self, request):
        all_params = ['_from', 'to', 'enterprise_project_id', 'hosts', 'instances', 'group_by']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if '_from' in local_var_params:
            query_params.append(('from', local_var_params['_from']))
        if 'to' in local_var_params:
            query_params.append(('to', local_var_params['to']))
        if 'hosts' in local_var_params:
            query_params.append(('hosts', local_var_params['hosts']))
        if 'instances' in local_var_params:
            query_params.append(('instances', local_var_params['instances']))
        if 'group_by' in local_var_params:
            query_params.append(('group_by', local_var_params['group_by']))

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
            resource_path='/v1/{project_id}/waf/overviews/qps/timeline',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListQpsTimelineResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_request_timeline_async(self, request):
        """查询安全总览中请求次数时间线统计数据

        查询安全总览中请求次数时间线统计数据。需要注意的是，安全总览相关的接口，暂时不能支持任意时间的查询。只能支持 console上显示的 昨天，今天，3天，7天和30天 数据查询。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListRequestTimeline
        :type request: :class:`huaweicloudsdkwaf.v1.ListRequestTimelineRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.ListRequestTimelineResponse`
        """
        return self.list_request_timeline_with_http_info(request)

    def list_request_timeline_with_http_info(self, request):
        all_params = ['_from', 'to', 'enterprise_project_id', 'hosts', 'instances', 'group_by']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if '_from' in local_var_params:
            query_params.append(('from', local_var_params['_from']))
        if 'to' in local_var_params:
            query_params.append(('to', local_var_params['to']))
        if 'hosts' in local_var_params:
            query_params.append(('hosts', local_var_params['hosts']))
            collection_formats['hosts'] = 'csv'
        if 'instances' in local_var_params:
            query_params.append(('instances', local_var_params['instances']))
            collection_formats['instances'] = 'csv'
        if 'group_by' in local_var_params:
            query_params.append(('group_by', local_var_params['group_by']))

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
            resource_path='/v1/{project_id}/waf/overviews/request/timeline',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListRequestTimelineResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_statistics_async(self, request):
        """查询安全总览请求与攻击数量

        查询安全总览请求与攻击数量。需要注意的是，安全总览相关的接口，暂时不能支持任意时间的查询。只能支持 console上显示的 昨天，今天，3天，7天和30天 数据查询。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListStatistics
        :type request: :class:`huaweicloudsdkwaf.v1.ListStatisticsRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.ListStatisticsResponse`
        """
        return self.list_statistics_with_http_info(request)

    def list_statistics_with_http_info(self, request):
        all_params = ['_from', 'to', 'enterprise_project_id', 'hosts', 'instances']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if '_from' in local_var_params:
            query_params.append(('from', local_var_params['_from']))
        if 'to' in local_var_params:
            query_params.append(('to', local_var_params['to']))
        if 'hosts' in local_var_params:
            query_params.append(('hosts', local_var_params['hosts']))
        if 'instances' in local_var_params:
            query_params.append(('instances', local_var_params['instances']))

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
            resource_path='/v1/{project_id}/waf/overviews/statistics',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListStatisticsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_top_abnormal_async(self, request):
        """查询业务异常数量

        查询业务异常TOP统计信息。需要注意的是，安全总览相关的接口，暂时不能支持任意时间的查询。只能支持 console上显示的 昨天，今天，3天，7天和30天 数据查询。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListTopAbnormal
        :type request: :class:`huaweicloudsdkwaf.v1.ListTopAbnormalRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.ListTopAbnormalResponse`
        """
        return self.list_top_abnormal_with_http_info(request)

    def list_top_abnormal_with_http_info(self, request):
        all_params = ['_from', 'to', 'enterprise_project_id', 'top', 'code', 'hosts', 'instances']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if '_from' in local_var_params:
            query_params.append(('from', local_var_params['_from']))
        if 'to' in local_var_params:
            query_params.append(('to', local_var_params['to']))
        if 'top' in local_var_params:
            query_params.append(('top', local_var_params['top']))
        if 'code' in local_var_params:
            query_params.append(('code', local_var_params['code']))
        if 'hosts' in local_var_params:
            query_params.append(('hosts', local_var_params['hosts']))
        if 'instances' in local_var_params:
            query_params.append(('instances', local_var_params['instances']))

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
            resource_path='/v1/{project_id}/waf/overviews/abnormal',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListTopAbnormalResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_value_list_async(self, request):
        """查询引用表列表

        查询引用表列表
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListValueList
        :type request: :class:`huaweicloudsdkwaf.v1.ListValueListRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.ListValueListResponse`
        """
        return self.list_value_list_with_http_info(request)

    def list_value_list_with_http_info(self, request):
        all_params = ['page', 'pagesize', 'name']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'page' in local_var_params:
            query_params.append(('page', local_var_params['page']))
        if 'pagesize' in local_var_params:
            query_params.append(('pagesize', local_var_params['pagesize']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))

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
            resource_path='/v1/{project_id}/waf/valuelist',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListValueListResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_whiteblackip_rule_async(self, request):
        """查询黑白名单规则列表

        查询黑白名单规则列表
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListWhiteblackipRule
        :type request: :class:`huaweicloudsdkwaf.v1.ListWhiteblackipRuleRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.ListWhiteblackipRuleResponse`
        """
        return self.list_whiteblackip_rule_with_http_info(request)

    def list_whiteblackip_rule_with_http_info(self, request):
        all_params = ['policy_id', 'enterprise_project_id', 'page', 'pagesize', 'name']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'page' in local_var_params:
            query_params.append(('page', local_var_params['page']))
        if 'pagesize' in local_var_params:
            query_params.append(('pagesize', local_var_params['pagesize']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))

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
            resource_path='/v1/{project_id}/waf/policy/{policy_id}/whiteblackip',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListWhiteblackipRuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def rename_instance_async(self, request):
        """重命名WAF独享引擎

        重命名WAF独享引擎
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for RenameInstance
        :type request: :class:`huaweicloudsdkwaf.v1.RenameInstanceRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.RenameInstanceResponse`
        """
        return self.rename_instance_with_http_info(request)

    def rename_instance_with_http_info(self, request):
        all_params = ['instance_id', 'enterprise_project_id', 'rename_instance_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

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
            resource_path='/v1/{project_id}/premium-waf/instance/{instance_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='RenameInstanceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_certificate_async(self, request):
        """查询证书

        查询证书
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowCertificate
        :type request: :class:`huaweicloudsdkwaf.v1.ShowCertificateRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.ShowCertificateResponse`
        """
        return self.show_certificate_with_http_info(request)

    def show_certificate_with_http_info(self, request):
        all_params = ['certificate_id', 'enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'certificate_id' in local_var_params:
            path_params['certificate_id'] = local_var_params['certificate_id']

        query_params = []
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
            resource_path='/v1/{project_id}/waf/certificate/{certificate_id}',
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

    def show_composite_host_async(self, request):
        """根据Id查询防护域名

        根据Id查询防护域名
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowCompositeHost
        :type request: :class:`huaweicloudsdkwaf.v1.ShowCompositeHostRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.ShowCompositeHostResponse`
        """
        return self.show_composite_host_with_http_info(request)

    def show_composite_host_with_http_info(self, request):
        all_params = ['host_id', 'enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'host_id' in local_var_params:
            path_params['host_id'] = local_var_params['host_id']

        query_params = []
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
            resource_path='/v1/{project_id}/composite-waf/host/{host_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowCompositeHostResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_console_config_async(self, request):
        """局点支持特性查询

        局点支持特性查询
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowConsoleConfig
        :type request: :class:`huaweicloudsdkwaf.v1.ShowConsoleConfigRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.ShowConsoleConfigResponse`
        """
        return self.show_console_config_with_http_info(request)

    def show_console_config_with_http_info(self, request):
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

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/waf/config/console',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowConsoleConfigResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_event_async(self, request):
        """查询指定事件id的防护事件详情

        查询指定事件id的防护事件详情
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowEvent
        :type request: :class:`huaweicloudsdkwaf.v1.ShowEventRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.ShowEventResponse`
        """
        return self.show_event_with_http_info(request)

    def show_event_with_http_info(self, request):
        all_params = ['eventid', 'enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'eventid' in local_var_params:
            path_params['eventid'] = local_var_params['eventid']

        query_params = []
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
            resource_path='/v1/{project_id}/waf/event/{eventid}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowEventResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_host_async(self, request):
        """根据防护域名Id查询云模式防护域名详细信息

        根据防护域名Id查询云模式防护域名详细信息
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowHost
        :type request: :class:`huaweicloudsdkwaf.v1.ShowHostRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.ShowHostResponse`
        """
        return self.show_host_with_http_info(request)

    def show_host_with_http_info(self, request):
        all_params = ['instance_id', 'enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
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
            resource_path='/v1/{project_id}/waf/instance/{instance_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowHostResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_instance_async(self, request):
        """查询WAF独享引擎信息

        查询WAF独享引擎信息
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowInstance
        :type request: :class:`huaweicloudsdkwaf.v1.ShowInstanceRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.ShowInstanceResponse`
        """
        return self.show_instance_with_http_info(request)

    def show_instance_with_http_info(self, request):
        all_params = ['instance_id', 'enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
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
            resource_path='/v1/{project_id}/premium-waf/instance/{instance_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowInstanceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_ip_group_async(self, request):
        """查询ip地址组明细

        查询ip地址组明细
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowIpGroup
        :type request: :class:`huaweicloudsdkwaf.v1.ShowIpGroupRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.ShowIpGroupResponse`
        """
        return self.show_ip_group_with_http_info(request)

    def show_ip_group_with_http_info(self, request):
        all_params = ['id', 'enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

        query_params = []
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
            resource_path='/v1/{project_id}/waf/ip-group/{id}',
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

    def show_lts_info_config_async(self, request):
        """查询lts配置信息

        查询lts配置信息
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowLtsInfoConfig
        :type request: :class:`huaweicloudsdkwaf.v1.ShowLtsInfoConfigRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.ShowLtsInfoConfigResponse`
        """
        return self.show_lts_info_config_with_http_info(request)

    def show_lts_info_config_with_http_info(self, request):
        all_params = ['enterprise_project_id']
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

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/waf/config/lts',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowLtsInfoConfigResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_policy_async(self, request):
        """根据Id查询防护策略

        根据Id查询防护策略
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowPolicy
        :type request: :class:`huaweicloudsdkwaf.v1.ShowPolicyRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.ShowPolicyResponse`
        """
        return self.show_policy_with_http_info(request)

    def show_policy_with_http_info(self, request):
        all_params = ['policy_id', 'enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']

        query_params = []
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
            resource_path='/v1/{project_id}/waf/policy/{policy_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowPolicyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_premium_host_async(self, request):
        """查看独享模式域名配置

        查看独享模式域名配置
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowPremiumHost
        :type request: :class:`huaweicloudsdkwaf.v1.ShowPremiumHostRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.ShowPremiumHostResponse`
        """
        return self.show_premium_host_with_http_info(request)

    def show_premium_host_with_http_info(self, request):
        all_params = ['host_id', 'enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'host_id' in local_var_params:
            path_params['host_id'] = local_var_params['host_id']

        query_params = []
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
            resource_path='/v1/{project_id}/premium-waf/host/{host_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowPremiumHostResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_certificate_async(self, request):
        """修改证书

        修改证书
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for UpdateCertificate
        :type request: :class:`huaweicloudsdkwaf.v1.UpdateCertificateRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.UpdateCertificateResponse`
        """
        return self.update_certificate_with_http_info(request)

    def update_certificate_with_http_info(self, request):
        all_params = ['certificate_id', 'enterprise_project_id', 'update_certificate_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'certificate_id' in local_var_params:
            path_params['certificate_id'] = local_var_params['certificate_id']

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

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
            resource_path='/v1/{project_id}/waf/certificate/{certificate_id}',
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

    def update_geoip_rule_async(self, request):
        """更新地理位置控制防护规则

        更新地理位置控制防护规则
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for UpdateGeoipRule
        :type request: :class:`huaweicloudsdkwaf.v1.UpdateGeoipRuleRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.UpdateGeoipRuleResponse`
        """
        return self.update_geoip_rule_with_http_info(request)

    def update_geoip_rule_with_http_info(self, request):
        all_params = ['policy_id', 'rule_id', 'update_geoip_rule_request_body', 'enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']
        if 'rule_id' in local_var_params:
            path_params['rule_id'] = local_var_params['rule_id']

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

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
            resource_path='/v1/{project_id}/waf/policy/{policy_id}/geoip/{rule_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateGeoipRuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_host_async(self, request):
        """更新云模式防护域名的配置

        更新云模式防护域名配置，在没有填入源站信息server的原始数据的情况下，则新的源站信息server会覆盖源站信息，而不是新增源站。此外，请求体可只传需要更新的部分。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for UpdateHost
        :type request: :class:`huaweicloudsdkwaf.v1.UpdateHostRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.UpdateHostResponse`
        """
        return self.update_host_with_http_info(request)

    def update_host_with_http_info(self, request):
        all_params = ['instance_id', 'enterprise_project_id', 'update_host_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

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
            resource_path='/v1/{project_id}/waf/instance/{instance_id}',
            method='PATCH',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateHostResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_host_protect_status_async(self, request):
        """修改域名防护状态

        修改域名防护状态
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for UpdateHostProtectStatus
        :type request: :class:`huaweicloudsdkwaf.v1.UpdateHostProtectStatusRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.UpdateHostProtectStatusResponse`
        """
        return self.update_host_protect_status_with_http_info(request)

    def update_host_protect_status_with_http_info(self, request):
        all_params = ['instance_id', 'enterprise_project_id', 'update_host_protect_status_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

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
            resource_path='/v1/{project_id}/waf/instance/{instance_id}/protect-status',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateHostProtectStatusResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_ip_group_async(self, request):
        """修改ip地址组

        修改ip地址组
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for UpdateIpGroup
        :type request: :class:`huaweicloudsdkwaf.v1.UpdateIpGroupRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.UpdateIpGroupResponse`
        """
        return self.update_ip_group_with_http_info(request)

    def update_ip_group_with_http_info(self, request):
        all_params = ['id', 'update_ip_group_request_body', 'enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

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
            resource_path='/v1/{project_id}/waf/ip-group/{id}',
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

    def update_lts_info_config_async(self, request):
        """配置全量日志lts

        配置全量日志lts，该接口可用来开启与关闭wa全量日志以及配置日志组和日志流。日志组id和日志流id可前往云日志服务获取。配置的日志流id要属于所配置的日志组。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for UpdateLtsInfoConfig
        :type request: :class:`huaweicloudsdkwaf.v1.UpdateLtsInfoConfigRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.UpdateLtsInfoConfigResponse`
        """
        return self.update_lts_info_config_with_http_info(request)

    def update_lts_info_config_with_http_info(self, request):
        all_params = ['ltsconfig_id', 'update_lts_info_config_request_body', 'enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'ltsconfig_id' in local_var_params:
            path_params['ltsconfig_id'] = local_var_params['ltsconfig_id']

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

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
            resource_path='/v1/{project_id}/waf/config/lts/{ltsconfig_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateLtsInfoConfigResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_policy_async(self, request):
        """更新防护策略

        更新防护策略，请求体可只传需要更新的部分
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for UpdatePolicy
        :type request: :class:`huaweicloudsdkwaf.v1.UpdatePolicyRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.UpdatePolicyResponse`
        """
        return self.update_policy_with_http_info(request)

    def update_policy_with_http_info(self, request):
        all_params = ['policy_id', 'update_policy_request_body', 'enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

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
            resource_path='/v1/{project_id}/waf/policy/{policy_id}',
            method='PATCH',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdatePolicyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_policy_protect_host_async(self, request):
        """更新防护策略的域名

        更新防护策略的防护域名
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for UpdatePolicyProtectHost
        :type request: :class:`huaweicloudsdkwaf.v1.UpdatePolicyProtectHostRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.UpdatePolicyProtectHostResponse`
        """
        return self.update_policy_protect_host_with_http_info(request)

    def update_policy_protect_host_with_http_info(self, request):
        all_params = ['policy_id', 'hosts', 'enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'hosts' in local_var_params:
            query_params.append(('hosts', local_var_params['hosts']))

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
            resource_path='/v1/{project_id}/waf/policy/{policy_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdatePolicyProtectHostResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_policy_rule_status_async(self, request):
        """修改单条规则的状态

        修改单条规则的状态，用于开启或者关闭单条规则，比如关闭精准防护中某一条规则
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for UpdatePolicyRuleStatus
        :type request: :class:`huaweicloudsdkwaf.v1.UpdatePolicyRuleStatusRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.UpdatePolicyRuleStatusResponse`
        """
        return self.update_policy_rule_status_with_http_info(request)

    def update_policy_rule_status_with_http_info(self, request):
        all_params = ['policy_id', 'ruletype', 'rule_id', 'update_policy_rule_status_request_body', 'enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']
        if 'ruletype' in local_var_params:
            path_params['ruletype'] = local_var_params['ruletype']
        if 'rule_id' in local_var_params:
            path_params['rule_id'] = local_var_params['rule_id']

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

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
            resource_path='/v1/{project_id}/waf/policy/{policy_id}/{ruletype}/{rule_id}/status',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdatePolicyRuleStatusResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_premium_host_async(self, request):
        """修改独享模式域名配置

        修改独享模式域名配置，在没有填入源站信息server的原始数据的情况下，则新的源站信息server会覆盖源站信息，而不是新增源站。此外，请求体可只传需要更新的部分。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for UpdatePremiumHost
        :type request: :class:`huaweicloudsdkwaf.v1.UpdatePremiumHostRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.UpdatePremiumHostResponse`
        """
        return self.update_premium_host_with_http_info(request)

    def update_premium_host_with_http_info(self, request):
        all_params = ['host_id', 'enterprise_project_id', 'update_premium_host_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'host_id' in local_var_params:
            path_params['host_id'] = local_var_params['host_id']

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

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
            resource_path='/v1/{project_id}/premium-waf/host/{host_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdatePremiumHostResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_premium_host_protect_status_async(self, request):
        """修改独享模式域名防护状态

        修改独享模式域名防护状态
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for UpdatePremiumHostProtectStatus
        :type request: :class:`huaweicloudsdkwaf.v1.UpdatePremiumHostProtectStatusRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.UpdatePremiumHostProtectStatusResponse`
        """
        return self.update_premium_host_protect_status_with_http_info(request)

    def update_premium_host_protect_status_with_http_info(self, request):
        all_params = ['host_id', 'enterprise_project_id', 'update_premium_host_protect_status_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'host_id' in local_var_params:
            path_params['host_id'] = local_var_params['host_id']

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

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
            resource_path='/v1/{project_id}/premium-waf/host/{host_id}/protect-status',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdatePremiumHostProtectStatusResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_privacy_rule_async(self, request):
        """更新隐私屏蔽防护规则

        更新隐私屏蔽防护规则
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for UpdatePrivacyRule
        :type request: :class:`huaweicloudsdkwaf.v1.UpdatePrivacyRuleRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.UpdatePrivacyRuleResponse`
        """
        return self.update_privacy_rule_with_http_info(request)

    def update_privacy_rule_with_http_info(self, request):
        all_params = ['policy_id', 'rule_id', 'update_privacy_rule_request_body', 'enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']
        if 'rule_id' in local_var_params:
            path_params['rule_id'] = local_var_params['rule_id']

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

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
            resource_path='/v1/{project_id}/waf/policy/{policy_id}/privacy/{rule_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdatePrivacyRuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_value_list_async(self, request):
        """修改引用表

        修改引用表
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for UpdateValueList
        :type request: :class:`huaweicloudsdkwaf.v1.UpdateValueListRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.UpdateValueListResponse`
        """
        return self.update_value_list_with_http_info(request)

    def update_value_list_with_http_info(self, request):
        all_params = ['valuelistid', 'enterprise_project_id', 'update_value_list_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'valuelistid' in local_var_params:
            path_params['valuelistid'] = local_var_params['valuelistid']

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

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
            resource_path='/v1/{project_id}/waf/valuelist/{valuelistid}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateValueListResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_whiteblackip_rule_async(self, request):
        """更新黑白名单防护规则

        更新黑白名单防护规则，可以更新ip/ip段以及防护动作等信息
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for UpdateWhiteblackipRule
        :type request: :class:`huaweicloudsdkwaf.v1.UpdateWhiteblackipRuleRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.UpdateWhiteblackipRuleResponse`
        """
        return self.update_whiteblackip_rule_with_http_info(request)

    def update_whiteblackip_rule_with_http_info(self, request):
        all_params = ['policy_id', 'rule_id', 'update_whiteblackip_rule_request_body', 'enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']
        if 'rule_id' in local_var_params:
            path_params['rule_id'] = local_var_params['rule_id']

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

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
            resource_path='/v1/{project_id}/waf/policy/{policy_id}/whiteblackip/{rule_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateWhiteblackipRuleResponse',
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

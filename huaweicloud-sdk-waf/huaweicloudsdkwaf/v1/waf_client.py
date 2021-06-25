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


class WafClient(Client):
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
        super(WafClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkwaf.v1.model")
        self.preset_headers = {'User-Agent': 'HuaweiCloud-SDK-Python'}

    @classmethod
    def new_builder(cls, clazz=None):
        if clazz is None:
            return ClientBuilder(cls)

        if clazz.__name__ != "WafClient":
            raise TypeError("client type error, support client type is WafClient")

        return ClientBuilder(clazz)

    def confirm_cloud_waf_subscription_info(self, request):
        """查询租户云模式订购信息

        查询租户云模式订购信息，包括包周期、按需计费

        :param ConfirmCloudWafSubscriptionInfoRequest request
        :return: ConfirmCloudWafSubscriptionInfoResponse
        """
        return self.confirm_cloud_waf_subscription_info_with_http_info(request)

    def confirm_cloud_waf_subscription_info_with_http_info(self, request):
        """查询租户云模式订购信息

        查询租户云模式订购信息，包括包周期、按需计费

        :param ConfirmCloudWafSubscriptionInfoRequest request
        :return: ConfirmCloudWafSubscriptionInfoResponse
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

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/waf/subscription',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ConfirmCloudWafSubscriptionInfoResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def confirm_user_bundle(self, request):
        """获取用户套餐信息

        获取用户购买的WAF规格信息

        :param ConfirmUserBundleRequest request
        :return: ConfirmUserBundleResponse
        """
        return self.confirm_user_bundle_with_http_info(request)

    def confirm_user_bundle_with_http_info(self, request):
        """获取用户套餐信息

        获取用户购买的WAF规格信息

        :param ConfirmUserBundleRequest request
        :return: ConfirmUserBundleResponse
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

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/waf/bundle',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ConfirmUserBundleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_anticrawler_rules(self, request):
        """创建反爬虫规则

        创建反爬虫规则

        :param CreateAnticrawlerRulesRequest request
        :return: CreateAnticrawlerRulesResponse
        """
        return self.create_anticrawler_rules_with_http_info(request)

    def create_anticrawler_rules_with_http_info(self, request):
        """创建反爬虫规则

        创建反爬虫规则

        :param CreateAnticrawlerRulesRequest request
        :return: CreateAnticrawlerRulesResponse
        """

        all_params = ['policy_id', 'create_anticrawler_rules_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']

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
            resource_path='/v1/{project_id}/waf/policy/{policy_id}/anticrawler',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateAnticrawlerRulesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_antileakage_rules(self, request):
        """创建防敏感信息泄露规则

        创建防敏感信息泄露规则

        :param CreateAntileakageRulesRequest request
        :return: CreateAntileakageRulesResponse
        """
        return self.create_antileakage_rules_with_http_info(request)

    def create_antileakage_rules_with_http_info(self, request):
        """创建防敏感信息泄露规则

        创建防敏感信息泄露规则

        :param CreateAntileakageRulesRequest request
        :return: CreateAntileakageRulesResponse
        """

        all_params = ['policy_id', 'create_antileakage_rules_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']

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
            resource_path='/v1/{project_id}/waf/policy/{policy_id}/antileakage',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateAntileakageRulesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_cc_rule(self, request):
        """创建cc规则

        创建cc规则

        :param CreateCcRuleRequest request
        :return: CreateCcRuleResponse
        """
        return self.create_cc_rule_with_http_info(request)

    def create_cc_rule_with_http_info(self, request):
        """创建cc规则

        创建cc规则

        :param CreateCcRuleRequest request
        :return: CreateCcRuleResponse
        """

        all_params = ['policy_id', 'create_cc_rule_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']

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
            resource_path='/v1/{project_id}/waf/policy/{policy_id}/cc',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateCcRuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_certificate(self, request):
        """创建证书

        创建证书

        :param CreateCertificateRequest request
        :return: CreateCertificateResponse
        """
        return self.create_certificate_with_http_info(request)

    def create_certificate_with_http_info(self, request):
        """创建证书

        创建证书

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


    def create_custom_rules(self, request):
        """创建精准防护规则

        创建精准防护规则

        :param CreateCustomRulesRequest request
        :return: CreateCustomRulesResponse
        """
        return self.create_custom_rules_with_http_info(request)

    def create_custom_rules_with_http_info(self, request):
        """创建精准防护规则

        创建精准防护规则

        :param CreateCustomRulesRequest request
        :return: CreateCustomRulesResponse
        """

        all_params = ['policy_id', 'create_custom_rules_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']

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
            resource_path='/v1/{project_id}/waf/policy/{policy_id}/custom',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateCustomRulesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_geoip_rules(self, request):
        """创建地理位置规则

        创建地理位置规则

        :param CreateGeoipRulesRequest request
        :return: CreateGeoipRulesResponse
        """
        return self.create_geoip_rules_with_http_info(request)

    def create_geoip_rules_with_http_info(self, request):
        """创建地理位置规则

        创建地理位置规则

        :param CreateGeoipRulesRequest request
        :return: CreateGeoipRulesResponse
        """

        all_params = ['policy_id', 'create_geoip_rules_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']

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
            resource_path='/v1/{project_id}/waf/policy/{policy_id}/geoip',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateGeoipRulesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_instane(self, request):
        """创建云模式防护域名

        创建云模式防护域名

        :param CreateInstaneRequest request
        :return: CreateInstaneResponse
        """
        return self.create_instane_with_http_info(request)

    def create_instane_with_http_info(self, request):
        """创建云模式防护域名

        创建云模式防护域名

        :param CreateInstaneRequest request
        :return: CreateInstaneResponse
        """

        all_params = ['create_instane_request_body']
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
            resource_path='/v1/{project_id}/waf/instance',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateInstaneResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_policy(self, request):
        """创建防护策略

        创建防护策略

        :param CreatePolicyRequest request
        :return: CreatePolicyResponse
        """
        return self.create_policy_with_http_info(request)

    def create_policy_with_http_info(self, request):
        """创建防护策略

        创建防护策略

        :param CreatePolicyRequest request
        :return: CreatePolicyResponse
        """

        all_params = ['create_policy_request_body']
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


    def create_premium_host(self, request):
        """创建独享模式域名

        创建独享模式域名

        :param CreatePremiumHostRequest request
        :return: CreatePremiumHostResponse
        """
        return self.create_premium_host_with_http_info(request)

    def create_premium_host_with_http_info(self, request):
        """创建独享模式域名

        创建独享模式域名

        :param CreatePremiumHostRequest request
        :return: CreatePremiumHostResponse
        """

        all_params = ['create_premium_host_request_body']
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


    def delete_anticrawler_rule(self, request):
        """删除反爬虫防护规则

        删除反爬虫防护规则

        :param DeleteAnticrawlerRuleRequest request
        :return: DeleteAnticrawlerRuleResponse
        """
        return self.delete_anticrawler_rule_with_http_info(request)

    def delete_anticrawler_rule_with_http_info(self, request):
        """删除反爬虫防护规则

        删除反爬虫防护规则

        :param DeleteAnticrawlerRuleRequest request
        :return: DeleteAnticrawlerRuleResponse
        """

        all_params = ['policy_id', 'rule_id']
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
            resource_path='/v1/{project_id}/waf/policy/{policy_id}/anticrawler/{rule_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteAnticrawlerRuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_antileakage_rule(self, request):
        """删除防敏感信息泄露防护规则

        删除防敏感信息泄露防护规则

        :param DeleteAntileakageRuleRequest request
        :return: DeleteAntileakageRuleResponse
        """
        return self.delete_antileakage_rule_with_http_info(request)

    def delete_antileakage_rule_with_http_info(self, request):
        """删除防敏感信息泄露防护规则

        删除防敏感信息泄露防护规则

        :param DeleteAntileakageRuleRequest request
        :return: DeleteAntileakageRuleResponse
        """

        all_params = ['policy_id', 'rule_id']
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
            resource_path='/v1/{project_id}/waf/policy/{policy_id}/antileakage/{rule_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteAntileakageRuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_cc_rule(self, request):
        """删除cc防护规则

        删除cc防护规则

        :param DeleteCcRuleRequest request
        :return: DeleteCcRuleResponse
        """
        return self.delete_cc_rule_with_http_info(request)

    def delete_cc_rule_with_http_info(self, request):
        """删除cc防护规则

        删除cc防护规则

        :param DeleteCcRuleRequest request
        :return: DeleteCcRuleResponse
        """

        all_params = ['policy_id', 'rule_id']
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
            resource_path='/v1/{project_id}/waf/policy/{policy_id}/cc/{rule_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteCcRuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_certificate(self, request):
        """删除证书

        删除证书

        :param DeleteCertificateRequest request
        :return: DeleteCertificateResponse
        """
        return self.delete_certificate_with_http_info(request)

    def delete_certificate_with_http_info(self, request):
        """删除证书

        删除证书

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


    def delete_custom_rule(self, request):
        """删除精准防护规则

        删除精准防护规则

        :param DeleteCustomRuleRequest request
        :return: DeleteCustomRuleResponse
        """
        return self.delete_custom_rule_with_http_info(request)

    def delete_custom_rule_with_http_info(self, request):
        """删除精准防护规则

        删除精准防护规则

        :param DeleteCustomRuleRequest request
        :return: DeleteCustomRuleResponse
        """

        all_params = ['policy_id', 'rule_id']
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
            resource_path='/v1/{project_id}/waf/policy/{policy_id}/custom/{rule_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteCustomRuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_geoip_rule(self, request):
        """删除地理位置防护规则

        删除地理位置防护规则

        :param DeleteGeoipRuleRequest request
        :return: DeleteGeoipRuleResponse
        """
        return self.delete_geoip_rule_with_http_info(request)

    def delete_geoip_rule_with_http_info(self, request):
        """删除地理位置防护规则

        删除地理位置防护规则

        :param DeleteGeoipRuleRequest request
        :return: DeleteGeoipRuleResponse
        """

        all_params = ['policy_id', 'rule_id']
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


    def delete_instane(self, request):
        """删除云模式防护域名

        删除云模式防护域名

        :param DeleteInstaneRequest request
        :return: DeleteInstaneResponse
        """
        return self.delete_instane_with_http_info(request)

    def delete_instane_with_http_info(self, request):
        """删除云模式防护域名

        删除云模式防护域名

        :param DeleteInstaneRequest request
        :return: DeleteInstaneResponse
        """

        all_params = ['instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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
            resource_path='/v1/{project_id}/waf/instance/{instance_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteInstaneResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_policy(self, request):
        """删除防护策略

        删除防护策略

        :param DeletePolicyRequest request
        :return: DeletePolicyResponse
        """
        return self.delete_policy_with_http_info(request)

    def delete_policy_with_http_info(self, request):
        """删除防护策略

        删除防护策略

        :param DeletePolicyRequest request
        :return: DeletePolicyResponse
        """

        all_params = ['policy_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']

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


    def delete_premium_host(self, request):
        """删除独享模式域名

        删除独享模式域名

        :param DeletePremiumHostRequest request
        :return: DeletePremiumHostResponse
        """
        return self.delete_premium_host_with_http_info(request)

    def delete_premium_host_with_http_info(self, request):
        """删除独享模式域名

        删除独享模式域名

        :param DeletePremiumHostRequest request
        :return: DeletePremiumHostResponse
        """

        all_params = ['host_id', 'keep_policy']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'host_id' in local_var_params:
            path_params['host_id'] = local_var_params['host_id']

        query_params = []
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


    def list_anticrawler_rules(self, request):
        """查询反爬虫规则列表

        查询反爬虫规则列表

        :param ListAnticrawlerRulesRequest request
        :return: ListAnticrawlerRulesResponse
        """
        return self.list_anticrawler_rules_with_http_info(request)

    def list_anticrawler_rules_with_http_info(self, request):
        """查询反爬虫规则列表

        查询反爬虫规则列表

        :param ListAnticrawlerRulesRequest request
        :return: ListAnticrawlerRulesResponse
        """

        all_params = ['policy_id', 'offset', 'limit']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
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
            resource_path='/v1/{project_id}/waf/policy/{policy_id}/anticrawler',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListAnticrawlerRulesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_antileakage_rules(self, request):
        """查询防敏感信息泄露规则列表

        查询防敏感信息泄露规则列表

        :param ListAntileakageRulesRequest request
        :return: ListAntileakageRulesResponse
        """
        return self.list_antileakage_rules_with_http_info(request)

    def list_antileakage_rules_with_http_info(self, request):
        """查询防敏感信息泄露规则列表

        查询防敏感信息泄露规则列表

        :param ListAntileakageRulesRequest request
        :return: ListAntileakageRulesResponse
        """

        all_params = ['policy_id', 'offset', 'limit']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
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
            resource_path='/v1/{project_id}/waf/policy/{policy_id}/antileakage',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListAntileakageRulesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_attack_action(self, request):
        """查询攻击防护类型

        查询攻击防护类型

        :param ListAttackActionRequest request
        :return: ListAttackActionResponse
        """
        return self.list_attack_action_with_http_info(request)

    def list_attack_action_with_http_info(self, request):
        """查询攻击防护类型

        查询攻击防护类型

        :param ListAttackActionRequest request
        :return: ListAttackActionResponse
        """

        all_params = ['_from', 'to', 'hosts', 'instances']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
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
            resource_path='/v1/{project_id}/waf/overviews/attack/action',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListAttackActionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_attack_distribution(self, request):
        """查询攻击事件分布

        查询攻击事件分布

        :param ListAttackDistributionRequest request
        :return: ListAttackDistributionResponse
        """
        return self.list_attack_distribution_with_http_info(request)

    def list_attack_distribution_with_http_info(self, request):
        """查询攻击事件分布

        查询攻击事件分布

        :param ListAttackDistributionRequest request
        :return: ListAttackDistributionResponse
        """

        all_params = ['_from', 'to', 'hosts', 'instances']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
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
            resource_path='/v1/{project_id}/waf/overviews/attack/distribution',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListAttackDistributionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_bandwidth_timeline(self, request):
        """查询安全统计带宽数据

        查询安全统计带宽数据

        :param ListBandwidthTimelineRequest request
        :return: ListBandwidthTimelineResponse
        """
        return self.list_bandwidth_timeline_with_http_info(request)

    def list_bandwidth_timeline_with_http_info(self, request):
        """查询安全统计带宽数据

        查询安全统计带宽数据

        :param ListBandwidthTimelineRequest request
        :return: ListBandwidthTimelineResponse
        """

        all_params = ['_from', 'to', 'hosts', 'instances', 'group_by']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
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


    def list_cc_rules(self, request):
        """查询cc规则列表

        查询cc规则列表

        :param ListCcRulesRequest request
        :return: ListCcRulesResponse
        """
        return self.list_cc_rules_with_http_info(request)

    def list_cc_rules_with_http_info(self, request):
        """查询cc规则列表

        查询cc规则列表

        :param ListCcRulesRequest request
        :return: ListCcRulesResponse
        """

        all_params = ['policy_id', 'offset', 'limit']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
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
            resource_path='/v1/{project_id}/waf/policy/{policy_id}/cc',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListCcRulesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_certificates(self, request):
        """查询证书列表

        查询证书列表

        :param ListCertificatesRequest request
        :return: ListCertificatesResponse
        """
        return self.list_certificates_with_http_info(request)

    def list_certificates_with_http_info(self, request):
        """查询证书列表

        查询证书列表

        :param ListCertificatesRequest request
        :return: ListCertificatesResponse
        """

        all_params = ['page', 'pagesize', 'name', 'host', 'exp_status']
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


    def list_custom_rules(self, request):
        """查询精准防护规则列表

        查询精准防护规则列表

        :param ListCustomRulesRequest request
        :return: ListCustomRulesResponse
        """
        return self.list_custom_rules_with_http_info(request)

    def list_custom_rules_with_http_info(self, request):
        """查询精准防护规则列表

        查询精准防护规则列表

        :param ListCustomRulesRequest request
        :return: ListCustomRulesResponse
        """

        all_params = ['policy_id', 'offset', 'limit']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
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
            resource_path='/v1/{project_id}/waf/policy/{policy_id}/custom',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListCustomRulesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_event_by_timeline(self, request):
        """查询请求/攻击数量统计

        查询请求/攻击数量统计。

        :param ListEventByTimelineRequest request
        :return: ListEventByTimelineResponse
        """
        return self.list_event_by_timeline_with_http_info(request)

    def list_event_by_timeline_with_http_info(self, request):
        """查询请求/攻击数量统计

        查询请求/攻击数量统计。

        :param ListEventByTimelineRequest request
        :return: ListEventByTimelineResponse
        """

        all_params = ['recent', 'hosts']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'recent' in local_var_params:
            query_params.append(('recent', local_var_params['recent']))
        if 'hosts' in local_var_params:
            query_params.append(('hosts', local_var_params['hosts']))
            collection_formats['hosts'] = 'csv'

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
            resource_path='/v1/{project_id}/waf/event/timeline',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListEventByTimelineResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_events(self, request):
        """查询攻击事件详情列表

        查询攻击事件详情列表

        :param ListEventsRequest request
        :return: ListEventsResponse
        """
        return self.list_events_with_http_info(request)

    def list_events_with_http_info(self, request):
        """查询攻击事件详情列表

        查询攻击事件详情列表

        :param ListEventsRequest request
        :return: ListEventsResponse
        """

        all_params = ['recent', 'hosts', 'page', 'pagesize']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'recent' in local_var_params:
            query_params.append(('recent', local_var_params['recent']))
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
            response_type='ListEventsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_geoip_rules(self, request):
        """查询地理位置规则列表

        查询地理位置规则列表

        :param ListGeoipRulesRequest request
        :return: ListGeoipRulesResponse
        """
        return self.list_geoip_rules_with_http_info(request)

    def list_geoip_rules_with_http_info(self, request):
        """查询地理位置规则列表

        查询地理位置规则列表

        :param ListGeoipRulesRequest request
        :return: ListGeoipRulesResponse
        """

        all_params = ['policy_id', 'offset', 'limit']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
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
            resource_path='/v1/{project_id}/waf/policy/{policy_id}/geoip',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListGeoipRulesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_instance(self, request):
        """查询WAF独享引擎列表

        查询WAF独享引擎列表

        :param ListInstanceRequest request
        :return: ListInstanceResponse
        """
        return self.list_instance_with_http_info(request)

    def list_instance_with_http_info(self, request):
        """查询WAF独享引擎列表

        查询WAF独享引擎列表

        :param ListInstanceRequest request
        :return: ListInstanceResponse
        """

        all_params = ['page', 'pagesize', 'instancename']
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


    def list_instanes(self, request):
        """查询云模式防护域名列表

        查询云模式防护域名列表

        :param ListInstanesRequest request
        :return: ListInstanesResponse
        """
        return self.list_instanes_with_http_info(request)

    def list_instanes_with_http_info(self, request):
        """查询云模式防护域名列表

        查询云模式防护域名列表

        :param ListInstanesRequest request
        :return: ListInstanesResponse
        """

        all_params = ['offset', 'limit']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
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
            resource_path='/v1/{project_id}/waf/instance',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListInstanesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_policy(self, request):
        """查询防护策略列表

        查询防护策略列表

        :param ListPolicyRequest request
        :return: ListPolicyResponse
        """
        return self.list_policy_with_http_info(request)

    def list_policy_with_http_info(self, request):
        """查询防护策略列表

        查询防护策略列表

        :param ListPolicyRequest request
        :return: ListPolicyResponse
        """

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


    def list_premium_host(self, request):
        """独享模式域名列表

        独享模式域名列表

        :param ListPremiumHostRequest request
        :return: ListPremiumHostResponse
        """
        return self.list_premium_host_with_http_info(request)

    def list_premium_host_with_http_info(self, request):
        """独享模式域名列表

        独享模式域名列表

        :param ListPremiumHostRequest request
        :return: ListPremiumHostResponse
        """

        all_params = ['page', 'pagesize', 'hostname', 'policyname', 'protect_status']
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


    def list_qps(self, request):
        """查询QPS

        查询QPS。

        :param ListQpsRequest request
        :return: ListQpsResponse
        """
        return self.list_qps_with_http_info(request)

    def list_qps_with_http_info(self, request):
        """查询QPS

        查询QPS。

        :param ListQpsRequest request
        :return: ListQpsResponse
        """

        all_params = ['recent', 'hosts']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'recent' in local_var_params:
            query_params.append(('recent', local_var_params['recent']))
        if 'hosts' in local_var_params:
            query_params.append(('hosts', local_var_params['hosts']))
            collection_formats['hosts'] = 'csv'

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
            resource_path='/v1/{project_id}/waf/event/request/peak',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListQpsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_qps_timeline(self, request):
        """查询安全统计qps次数

        查询安全统计qps次数

        :param ListQpsTimelineRequest request
        :return: ListQpsTimelineResponse
        """
        return self.list_qps_timeline_with_http_info(request)

    def list_qps_timeline_with_http_info(self, request):
        """查询安全统计qps次数

        查询安全统计qps次数

        :param ListQpsTimelineRequest request
        :return: ListQpsTimelineResponse
        """

        all_params = ['_from', 'to', 'hosts', 'instances', 'group_by']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
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


    def list_request_timeline(self, request):
        """查询安全统计请求次数

        查询安全统计请求次数

        :param ListRequestTimelineRequest request
        :return: ListRequestTimelineResponse
        """
        return self.list_request_timeline_with_http_info(request)

    def list_request_timeline_with_http_info(self, request):
        """查询安全统计请求次数

        查询安全统计请求次数

        :param ListRequestTimelineRequest request
        :return: ListRequestTimelineResponse
        """

        all_params = ['_from', 'to', 'hosts', 'instances', 'group_by']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
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


    def list_response_code_timeline(self, request):
        """查询安全统计响应码数据

        查询安全统计响应码数据

        :param ListResponseCodeTimelineRequest request
        :return: ListResponseCodeTimelineResponse
        """
        return self.list_response_code_timeline_with_http_info(request)

    def list_response_code_timeline_with_http_info(self, request):
        """查询安全统计响应码数据

        查询安全统计响应码数据

        :param ListResponseCodeTimelineRequest request
        :return: ListResponseCodeTimelineResponse
        """

        all_params = ['_from', 'to', 'hosts', 'instances', 'response_source', 'group_by']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if '_from' in local_var_params:
            query_params.append(('from', local_var_params['_from']))
        if 'to' in local_var_params:
            query_params.append(('to', local_var_params['to']))
        if 'hosts' in local_var_params:
            query_params.append(('hosts', local_var_params['hosts']))
        if 'instances' in local_var_params:
            query_params.append(('instances', local_var_params['instances']))
        if 'response_source' in local_var_params:
            query_params.append(('response_source', local_var_params['response_source']))
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
            resource_path='/v1/{project_id}/waf/overviews/response-code/timeline',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListResponseCodeTimelineResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_source_domain_top5(self, request):
        """查询被攻击次数前五的域名

        查询被攻击次数前五的域名

        :param ListSourceDomainTop5Request request
        :return: ListSourceDomainTop5Response
        """
        return self.list_source_domain_top5_with_http_info(request)

    def list_source_domain_top5_with_http_info(self, request):
        """查询被攻击次数前五的域名

        查询被攻击次数前五的域名

        :param ListSourceDomainTop5Request request
        :return: ListSourceDomainTop5Response
        """

        all_params = ['recent', 'hosts']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'recent' in local_var_params:
            query_params.append(('recent', local_var_params['recent']))
        if 'hosts' in local_var_params:
            query_params.append(('hosts', local_var_params['hosts']))
            collection_formats['hosts'] = 'csv'

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
            resource_path='/v1/{project_id}/waf/event/attack/domain',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListSourceDomainTop5Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_source_ip_num(self, request):
        """查询攻击源IP的个数

        查询攻击源IP的个数。

        :param ListSourceIpNumRequest request
        :return: ListSourceIpNumResponse
        """
        return self.list_source_ip_num_with_http_info(request)

    def list_source_ip_num_with_http_info(self, request):
        """查询攻击源IP的个数

        查询攻击源IP的个数。

        :param ListSourceIpNumRequest request
        :return: ListSourceIpNumResponse
        """

        all_params = ['recent', 'hosts']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'recent' in local_var_params:
            query_params.append(('recent', local_var_params['recent']))
        if 'hosts' in local_var_params:
            query_params.append(('hosts', local_var_params['hosts']))
            collection_formats['hosts'] = 'csv'

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
            resource_path='/v1/{project_id}/waf/event/attack/source/num',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListSourceIpNumResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_source_ip_top5(self, request):
        """查询攻击源ip

        查询攻击源ip

        :param ListSourceIpTop5Request request
        :return: ListSourceIpTop5Response
        """
        return self.list_source_ip_top5_with_http_info(request)

    def list_source_ip_top5_with_http_info(self, request):
        """查询攻击源ip

        查询攻击源ip

        :param ListSourceIpTop5Request request
        :return: ListSourceIpTop5Response
        """

        all_params = ['recent', 'hosts']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'recent' in local_var_params:
            query_params.append(('recent', local_var_params['recent']))
        if 'hosts' in local_var_params:
            query_params.append(('hosts', local_var_params['hosts']))
            collection_formats['hosts'] = 'csv'

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
            resource_path='/v1/{project_id}/waf/event/attack/source',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListSourceIpTop5Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_source_url_top5(self, request):
        """查询被攻击次数前五的url

        查询被攻击次数前五的url

        :param ListSourceUrlTop5Request request
        :return: ListSourceUrlTop5Response
        """
        return self.list_source_url_top5_with_http_info(request)

    def list_source_url_top5_with_http_info(self, request):
        """查询被攻击次数前五的url

        查询被攻击次数前五的url

        :param ListSourceUrlTop5Request request
        :return: ListSourceUrlTop5Response
        """

        all_params = ['recent', 'hosts']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'recent' in local_var_params:
            query_params.append(('recent', local_var_params['recent']))
        if 'hosts' in local_var_params:
            query_params.append(('hosts', local_var_params['hosts']))
            collection_formats['hosts'] = 'csv'

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
            resource_path='/v1/{project_id}/waf/event/domain/url',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListSourceUrlTop5Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_statistics(self, request):
        """查询安全总览请求数据

        查询安全总览请求数据

        :param ListStatisticsRequest request
        :return: ListStatisticsResponse
        """
        return self.list_statistics_with_http_info(request)

    def list_statistics_with_http_info(self, request):
        """查询安全总览请求数据

        查询安全总览请求数据

        :param ListStatisticsRequest request
        :return: ListStatisticsResponse
        """

        all_params = ['_from', 'to', 'hosts', 'instances']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
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


    def list_threats(self, request):
        """查询攻击事件分布类型

        查询攻击事件分布类型。

        :param ListThreatsRequest request
        :return: ListThreatsResponse
        """
        return self.list_threats_with_http_info(request)

    def list_threats_with_http_info(self, request):
        """查询攻击事件分布类型

        查询攻击事件分布类型。

        :param ListThreatsRequest request
        :return: ListThreatsResponse
        """

        all_params = ['recent', 'hosts']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'recent' in local_var_params:
            query_params.append(('recent', local_var_params['recent']))
        if 'hosts' in local_var_params:
            query_params.append(('hosts', local_var_params['hosts']))
            collection_formats['hosts'] = 'csv'

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
            resource_path='/v1/{project_id}/waf/event/attack/type',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListThreatsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_top_abnormal(self, request):
        """查询业务异常监控

        查询业务异常监控

        :param ListTopAbnormalRequest request
        :return: ListTopAbnormalResponse
        """
        return self.list_top_abnormal_with_http_info(request)

    def list_top_abnormal_with_http_info(self, request):
        """查询业务异常监控

        查询业务异常监控

        :param ListTopAbnormalRequest request
        :return: ListTopAbnormalResponse
        """

        all_params = ['_from', 'to', 'top', 'code', 'hosts', 'instances']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
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


    def list_top_domain(self, request):
        """查询攻击域名

        查询攻击域名

        :param ListTopDomainRequest request
        :return: ListTopDomainResponse
        """
        return self.list_top_domain_with_http_info(request)

    def list_top_domain_with_http_info(self, request):
        """查询攻击域名

        查询攻击域名

        :param ListTopDomainRequest request
        :return: ListTopDomainResponse
        """

        all_params = ['_from', 'to', 'top', 'hosts', 'instances']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
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
            resource_path='/v1/{project_id}/waf/overviews/attack/domain',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListTopDomainResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_top_ip(self, request):
        """查询攻击源ip

        查询攻击源ip

        :param ListTopIpRequest request
        :return: ListTopIpResponse
        """
        return self.list_top_ip_with_http_info(request)

    def list_top_ip_with_http_info(self, request):
        """查询攻击源ip

        查询攻击源ip

        :param ListTopIpRequest request
        :return: ListTopIpResponse
        """

        all_params = ['_from', 'to', 'top', 'hosts', 'instances']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
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
            resource_path='/v1/{project_id}/waf/overviews/attack/ip',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListTopIpResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_top_region(self, request):
        """查询攻击来源区域

        查询攻击来源区域

        :param ListTopRegionRequest request
        :return: ListTopRegionResponse
        """
        return self.list_top_region_with_http_info(request)

    def list_top_region_with_http_info(self, request):
        """查询攻击来源区域

        查询攻击来源区域

        :param ListTopRegionRequest request
        :return: ListTopRegionResponse
        """

        all_params = ['_from', 'to', 'top', 'hosts', 'instances']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
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
            resource_path='/v1/{project_id}/waf/overviews/attack/region',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListTopRegionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_top_url(self, request):
        """查询被攻击url

        查询被攻击url

        :param ListTopUrlRequest request
        :return: ListTopUrlResponse
        """
        return self.list_top_url_with_http_info(request)

    def list_top_url_with_http_info(self, request):
        """查询被攻击url

        查询被攻击url

        :param ListTopUrlRequest request
        :return: ListTopUrlResponse
        """

        all_params = ['_from', 'to', 'top', 'hosts', 'instances']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
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
            resource_path='/v1/{project_id}/waf/overviews/attack/url',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListTopUrlResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_url(self, request):
        """查询事件日志中的url

        查询QPS。

        :param ListUrlRequest request
        :return: ListUrlResponse
        """
        return self.list_url_with_http_info(request)

    def list_url_with_http_info(self, request):
        """查询事件日志中的url

        查询QPS。

        :param ListUrlRequest request
        :return: ListUrlResponse
        """

        all_params = ['top', 'recent', '_from', 'to', 'hosts', 'instances']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'top' in local_var_params:
            query_params.append(('top', local_var_params['top']))
        if 'recent' in local_var_params:
            query_params.append(('recent', local_var_params['recent']))
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
            resource_path='/v1/{project_id}/waf/event/url',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListUrlResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_value_list(self, request):
        """查询引用表列表

        查询引用表列表

        :param ListValueListRequest request
        :return: ListValueListResponse
        """
        return self.list_value_list_with_http_info(request)

    def list_value_list_with_http_info(self, request):
        """查询引用表列表

        查询引用表列表

        :param ListValueListRequest request
        :return: ListValueListResponse
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


    def show_anticrawler_rule(self, request):
        """查询反爬虫防护规则

        根据Id查询反爬虫防护规则

        :param ShowAnticrawlerRuleRequest request
        :return: ShowAnticrawlerRuleResponse
        """
        return self.show_anticrawler_rule_with_http_info(request)

    def show_anticrawler_rule_with_http_info(self, request):
        """查询反爬虫防护规则

        根据Id查询反爬虫防护规则

        :param ShowAnticrawlerRuleRequest request
        :return: ShowAnticrawlerRuleResponse
        """

        all_params = ['policy_id', 'rule_id']
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
            resource_path='/v1/{project_id}/waf/policy/{policy_id}/anticrawler/{rule_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowAnticrawlerRuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_antileakage_rule(self, request):
        """查询防敏感信息泄露防护规则

        根据Id查询防敏感信息泄露防护规则

        :param ShowAntileakageRuleRequest request
        :return: ShowAntileakageRuleResponse
        """
        return self.show_antileakage_rule_with_http_info(request)

    def show_antileakage_rule_with_http_info(self, request):
        """查询防敏感信息泄露防护规则

        根据Id查询防敏感信息泄露防护规则

        :param ShowAntileakageRuleRequest request
        :return: ShowAntileakageRuleResponse
        """

        all_params = ['policy_id', 'rule_id']
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
            resource_path='/v1/{project_id}/waf/policy/{policy_id}/antileakage/{rule_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowAntileakageRuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_cc_rule(self, request):
        """根据Id查询cc防护规则

        根据Id查询cc防护规则

        :param ShowCcRuleRequest request
        :return: ShowCcRuleResponse
        """
        return self.show_cc_rule_with_http_info(request)

    def show_cc_rule_with_http_info(self, request):
        """根据Id查询cc防护规则

        根据Id查询cc防护规则

        :param ShowCcRuleRequest request
        :return: ShowCcRuleResponse
        """

        all_params = ['policy_id', 'rule_id']
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
            resource_path='/v1/{project_id}/waf/policy/{policy_id}/cc/{rule_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowCcRuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_certificate(self, request):
        """查询证书

        查询证书

        :param ShowCertificateRequest request
        :return: ShowCertificateResponse
        """
        return self.show_certificate_with_http_info(request)

    def show_certificate_with_http_info(self, request):
        """查询证书

        查询证书

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


    def show_custom_rule(self, request):
        """根据Id查询精准防护规则

        根据Id查询精准防护规则

        :param ShowCustomRuleRequest request
        :return: ShowCustomRuleResponse
        """
        return self.show_custom_rule_with_http_info(request)

    def show_custom_rule_with_http_info(self, request):
        """根据Id查询精准防护规则

        根据Id查询精准防护规则

        :param ShowCustomRuleRequest request
        :return: ShowCustomRuleResponse
        """

        all_params = ['policy_id', 'rule_id']
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
            resource_path='/v1/{project_id}/waf/policy/{policy_id}/custom/{rule_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowCustomRuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_geoip_rule(self, request):
        """根据Id查询地理位置防护规则

        根据Id查询地理位置防护规则

        :param ShowGeoipRuleRequest request
        :return: ShowGeoipRuleResponse
        """
        return self.show_geoip_rule_with_http_info(request)

    def show_geoip_rule_with_http_info(self, request):
        """根据Id查询地理位置防护规则

        根据Id查询地理位置防护规则

        :param ShowGeoipRuleRequest request
        :return: ShowGeoipRuleResponse
        """

        all_params = ['policy_id', 'rule_id']
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
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowGeoipRuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_instance(self, request):
        """根据Id查询云模式防护域名

        根据Id查询云模式防护域名

        :param ShowInstanceRequest request
        :return: ShowInstanceResponse
        """
        return self.show_instance_with_http_info(request)

    def show_instance_with_http_info(self, request):
        """根据Id查询云模式防护域名

        根据Id查询云模式防护域名

        :param ShowInstanceRequest request
        :return: ShowInstanceResponse
        """

        all_params = ['instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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
            resource_path='/v1/{project_id}/waf/instance/{instance_id}',
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


    def show_instance_route(self, request):
        """获取云模式域名路由信息

        返回路由信息

        :param ShowInstanceRouteRequest request
        :return: ShowInstanceRouteResponse
        """
        return self.show_instance_route_with_http_info(request)

    def show_instance_route_with_http_info(self, request):
        """获取云模式域名路由信息

        返回路由信息

        :param ShowInstanceRouteRequest request
        :return: ShowInstanceRouteResponse
        """

        all_params = ['instanceid']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instanceid' in local_var_params:
            path_params['instanceid'] = local_var_params['instanceid']

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
            resource_path='/v1/{project_id}/waf/instance/{instanceid}/route',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowInstanceRouteResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_premium_host(self, request):
        """查看独享模式域名配置

        查看独享模式域名配置

        :param ShowPremiumHostRequest request
        :return: ShowPremiumHostResponse
        """
        return self.show_premium_host_with_http_info(request)

    def show_premium_host_with_http_info(self, request):
        """查看独享模式域名配置

        查看独享模式域名配置

        :param ShowPremiumHostRequest request
        :return: ShowPremiumHostResponse
        """

        all_params = ['host_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'host_id' in local_var_params:
            path_params['host_id'] = local_var_params['host_id']

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


    def update_anticrawler_rule(self, request):
        """更新反爬虫防护规则

        更新反爬虫防护规则

        :param UpdateAnticrawlerRuleRequest request
        :return: UpdateAnticrawlerRuleResponse
        """
        return self.update_anticrawler_rule_with_http_info(request)

    def update_anticrawler_rule_with_http_info(self, request):
        """更新反爬虫防护规则

        更新反爬虫防护规则

        :param UpdateAnticrawlerRuleRequest request
        :return: UpdateAnticrawlerRuleResponse
        """

        all_params = ['policy_id', 'rule_id', 'update_anticrawler_rule_request_body']
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
            resource_path='/v1/{project_id}/waf/policy/{policy_id}/anticrawler/{rule_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateAnticrawlerRuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_antileakage_rule(self, request):
        """更新防敏感信息泄露防护规则

        更新防敏感信息泄露防护规则

        :param UpdateAntileakageRuleRequest request
        :return: UpdateAntileakageRuleResponse
        """
        return self.update_antileakage_rule_with_http_info(request)

    def update_antileakage_rule_with_http_info(self, request):
        """更新防敏感信息泄露防护规则

        更新防敏感信息泄露防护规则

        :param UpdateAntileakageRuleRequest request
        :return: UpdateAntileakageRuleResponse
        """

        all_params = ['policy_id', 'rule_id', 'update_antileakage_rule_request_body']
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
            resource_path='/v1/{project_id}/waf/policy/{policy_id}/antileakage/{rule_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateAntileakageRuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_cc_rule(self, request):
        """更新cc防护规则

        更新cc防护规则

        :param UpdateCcRuleRequest request
        :return: UpdateCcRuleResponse
        """
        return self.update_cc_rule_with_http_info(request)

    def update_cc_rule_with_http_info(self, request):
        """更新cc防护规则

        更新cc防护规则

        :param UpdateCcRuleRequest request
        :return: UpdateCcRuleResponse
        """

        all_params = ['policy_id', 'rule_id', 'update_cc_rule_request_body']
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
            resource_path='/v1/{project_id}/waf/policy/{policy_id}/cc/{rule_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateCcRuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_certificate(self, request):
        """修改证书

        修改证书

        :param UpdateCertificateRequest request
        :return: UpdateCertificateResponse
        """
        return self.update_certificate_with_http_info(request)

    def update_certificate_with_http_info(self, request):
        """修改证书

        修改证书

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


    def update_custom_rule(self, request):
        """更新精准防护规则

        更新精准防护规则

        :param UpdateCustomRuleRequest request
        :return: UpdateCustomRuleResponse
        """
        return self.update_custom_rule_with_http_info(request)

    def update_custom_rule_with_http_info(self, request):
        """更新精准防护规则

        更新精准防护规则

        :param UpdateCustomRuleRequest request
        :return: UpdateCustomRuleResponse
        """

        all_params = ['policy_id', 'rule_id', 'update_custom_rule_request_body']
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
            resource_path='/v1/{project_id}/waf/policy/{policy_id}/custom/{rule_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateCustomRuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_geoip_rule(self, request):
        """更新地理位置防护规则

        更新地理位置防护规则

        :param UpdateGeoipRuleRequest request
        :return: UpdateGeoipRuleResponse
        """
        return self.update_geoip_rule_with_http_info(request)

    def update_geoip_rule_with_http_info(self, request):
        """更新地理位置防护规则

        更新地理位置防护规则

        :param UpdateGeoipRuleRequest request
        :return: UpdateGeoipRuleResponse
        """

        all_params = ['policy_id', 'rule_id', 'update_geoip_rule_request_body']
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


    def update_instance(self, request):
        """更新云模式防护域名

        更新云模式防护域名

        :param UpdateInstanceRequest request
        :return: UpdateInstanceResponse
        """
        return self.update_instance_with_http_info(request)

    def update_instance_with_http_info(self, request):
        """更新云模式防护域名

        更新云模式防护域名

        :param UpdateInstanceRequest request
        :return: UpdateInstanceResponse
        """

        all_params = ['instance_id', 'update_instance_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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
            resource_path='/v1/{project_id}/waf/instance/{instance_id}',
            method='PATCH',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateInstanceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_patch_policy(self, request):
        """更新防护策略

        更新防护策略，请求体可只传需要更新的部分

        :param UpdatePatchPolicyRequest request
        :return: UpdatePatchPolicyResponse
        """
        return self.update_patch_policy_with_http_info(request)

    def update_patch_policy_with_http_info(self, request):
        """更新防护策略

        更新防护策略，请求体可只传需要更新的部分

        :param UpdatePatchPolicyRequest request
        :return: UpdatePatchPolicyResponse
        """

        all_params = ['policy_id', 'update_patch_policy_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']

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
            resource_path='/v1/{project_id}/waf/policy/{policy_id}',
            method='PATCH',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdatePatchPolicyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_premium_host(self, request):
        """修改独享模式域名配置

        修改独享模式域名配置

        :param UpdatePremiumHostRequest request
        :return: UpdatePremiumHostResponse
        """
        return self.update_premium_host_with_http_info(request)

    def update_premium_host_with_http_info(self, request):
        """修改独享模式域名配置

        修改独享模式域名配置

        :param UpdatePremiumHostRequest request
        :return: UpdatePremiumHostResponse
        """

        all_params = ['host_id', 'update_premium_host_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'host_id' in local_var_params:
            path_params['host_id'] = local_var_params['host_id']

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


    def update_premium_host_access_status(self, request):
        """修改独享模式域名接入状态

        修改独享模式域名接入状态

        :param UpdatePremiumHostAccessStatusRequest request
        :return: UpdatePremiumHostAccessStatusResponse
        """
        return self.update_premium_host_access_status_with_http_info(request)

    def update_premium_host_access_status_with_http_info(self, request):
        """修改独享模式域名接入状态

        修改独享模式域名接入状态

        :param UpdatePremiumHostAccessStatusRequest request
        :return: UpdatePremiumHostAccessStatusResponse
        """

        all_params = ['host_id', 'update_premium_host_access_status_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'host_id' in local_var_params:
            path_params['host_id'] = local_var_params['host_id']

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
            resource_path='/v1/{project_id}/premium-waf/host/{host_id}/access_status',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdatePremiumHostAccessStatusResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_premium_host_protect_status(self, request):
        """修改独享模式域名防护状态

        修改独享模式域名防护状态

        :param UpdatePremiumHostProtectStatusRequest request
        :return: UpdatePremiumHostProtectStatusResponse
        """
        return self.update_premium_host_protect_status_with_http_info(request)

    def update_premium_host_protect_status_with_http_info(self, request):
        """修改独享模式域名防护状态

        修改独享模式域名防护状态

        :param UpdatePremiumHostProtectStatusRequest request
        :return: UpdatePremiumHostProtectStatusResponse
        """

        all_params = ['host_id', 'update_premium_host_protect_status_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'host_id' in local_var_params:
            path_params['host_id'] = local_var_params['host_id']

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
            resource_path='/v1/{project_id}/premium-waf/host/{host_id}/protect_status',
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


    def create_pool(self, request):
        """创建WAF独享引擎组

        创建WAF独享引擎组

        :param CreatePoolRequest request
        :return: CreatePoolResponse
        """
        return self.create_pool_with_http_info(request)

    def create_pool_with_http_info(self, request):
        """创建WAF独享引擎组

        创建WAF独享引擎组

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
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/premium-waf/pool',
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


    def delete_pool(self, request):
        """删除WAF独享引擎组

        删除WAF独享引擎组

        :param DeletePoolRequest request
        :return: DeletePoolResponse
        """
        return self.delete_pool_with_http_info(request)

    def delete_pool_with_http_info(self, request):
        """删除WAF独享引擎组

        删除WAF独享引擎组

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
            resource_path='/v1/{project_id}/premium-waf/pool/{pool_id}',
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


    def list_pools(self, request):
        """查询WAF独享引擎组列表

        查询WAF独享引擎组列表

        :param ListPoolsRequest request
        :return: ListPoolsResponse
        """
        return self.list_pools_with_http_info(request)

    def list_pools_with_http_info(self, request):
        """查询WAF独享引擎组列表

        查询WAF独享引擎组列表

        :param ListPoolsRequest request
        :return: ListPoolsResponse
        """

        all_params = ['page', 'pagesize', 'name', 'vpc_id', 'detail']
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
        if 'vpc_id' in local_var_params:
            query_params.append(('vpc_id', local_var_params['vpc_id']))
        if 'detail' in local_var_params:
            query_params.append(('detail', local_var_params['detail']))

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
            resource_path='/v1/{project_id}/premium-waf/pool',
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


    def show_pool(self, request):
        """查询WAF独享引擎组信息

        查询WAF独享引擎组信息

        :param ShowPoolRequest request
        :return: ShowPoolResponse
        """
        return self.show_pool_with_http_info(request)

    def show_pool_with_http_info(self, request):
        """查询WAF独享引擎组信息

        查询WAF独享引擎组信息

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
            resource_path='/v1/{project_id}/premium-waf/pool/{pool_id}',
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


    def update_pool(self, request):
        """修改WAF独享引擎组信息

        修改WAF独享引擎组信息

        :param UpdatePoolRequest request
        :return: UpdatePoolResponse
        """
        return self.update_pool_with_http_info(request)

    def update_pool_with_http_info(self, request):
        """修改WAF独享引擎组信息

        修改WAF独享引擎组信息

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
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/premium-waf/pool/{pool_id}',
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

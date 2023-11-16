# coding: utf-8

from __future__ import absolute_import

import importlib
import warnings

from huaweicloudsdkcore.client import Client, ClientBuilder
from huaweicloudsdkcore.utils import http_utils
from huaweicloudsdkcore.sdk_stream_request import SdkStreamRequest
try:
    from huaweicloudsdkcore.invoker.invoker import AsyncInvoker
except ImportError as e:
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkwaf'")


class WafAsyncClient(Client):
    def __init__(self):
        super(WafAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkwaf.v1.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "WafAsyncClient":
                raise TypeError("client type error, support client type is WafAsyncClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def apply_certificate_to_host_async(self, request):
        """绑定证书到域名

        绑定证书到域名
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ApplyCertificateToHost
        :type request: :class:`huaweicloudsdkwaf.v1.ApplyCertificateToHostRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.ApplyCertificateToHostResponse`
        """
        http_info = self._apply_certificate_to_host_http_info(request)
        return self._call_api(**http_info)

    def apply_certificate_to_host_async_invoker(self, request):
        http_info = self._apply_certificate_to_host_http_info(request)
        return AsyncInvoker(self, http_info)

    def _apply_certificate_to_host_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/waf/certificate/{certificate_id}/apply-to-hosts",
            "request_type": request.__class__.__name__,
            "response_type": "ApplyCertificateToHostResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'certificate_id' in local_var_params:
            path_params['certificate_id'] = local_var_params['certificate_id']

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def change_prepaid_cloud_waf_async(self, request):
        """变更包周期云模式waf规格

        变更包周期云模式waf规格。注：
         - 1.变更某产品规格的前提是必须已购买该产品 
         - 2.waf版本只支持升配，不支持降配；扩展包数量可以增加或者减少，但不支持数量减少为0 
         - 3.不支持同时升降配，如增加域名扩展包数量，同时减少规则扩展包数量
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ChangePrepaidCloudWaf
        :type request: :class:`huaweicloudsdkwaf.v1.ChangePrepaidCloudWafRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.ChangePrepaidCloudWafResponse`
        """
        http_info = self._change_prepaid_cloud_waf_http_info(request)
        return self._call_api(**http_info)

    def change_prepaid_cloud_waf_async_invoker(self, request):
        http_info = self._change_prepaid_cloud_waf_http_info(request)
        return AsyncInvoker(self, http_info)

    def _change_prepaid_cloud_waf_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/waf/subscription/batchalter/prepaid-cloud-waf",
            "request_type": request.__class__.__name__,
            "response_type": "ChangePrepaidCloudWafResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_anti_tamper_rule_async(self, request):
        """创建防篡改规则

        创建防篡改规则
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateAntiTamperRule
        :type request: :class:`huaweicloudsdkwaf.v1.CreateAntiTamperRuleRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.CreateAntiTamperRuleResponse`
        """
        http_info = self._create_anti_tamper_rule_http_info(request)
        return self._call_api(**http_info)

    def create_anti_tamper_rule_async_invoker(self, request):
        http_info = self._create_anti_tamper_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_anti_tamper_rule_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/waf/policy/{policy_id}/antitamper",
            "request_type": request.__class__.__name__,
            "response_type": "CreateAntiTamperRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_anticrawler_rule_async(self, request):
        """创建JS脚本反爬虫规则

        创建JS脚本反爬虫规则，在调用此接口创建防护规则前，需要调用更新JS脚本反爬虫规则防护模式（UpdateAnticrawlerRuleType）接口指定防护模式
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateAnticrawlerRule
        :type request: :class:`huaweicloudsdkwaf.v1.CreateAnticrawlerRuleRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.CreateAnticrawlerRuleResponse`
        """
        http_info = self._create_anticrawler_rule_http_info(request)
        return self._call_api(**http_info)

    def create_anticrawler_rule_async_invoker(self, request):
        http_info = self._create_anticrawler_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_anticrawler_rule_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/waf/policy/{policy_id}/anticrawler",
            "request_type": request.__class__.__name__,
            "response_type": "CreateAnticrawlerRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_antileakage_rule_async(self, request):
        """创建防敏感信息泄露规则

        创建防敏感信息泄露规则
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateAntileakageRule
        :type request: :class:`huaweicloudsdkwaf.v1.CreateAntileakageRuleRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.CreateAntileakageRuleResponse`
        """
        http_info = self._create_antileakage_rule_http_info(request)
        return self._call_api(**http_info)

    def create_antileakage_rule_async_invoker(self, request):
        http_info = self._create_antileakage_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_antileakage_rule_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/waf/policy/{policy_id}/antileakage",
            "request_type": request.__class__.__name__,
            "response_type": "CreateAntileakageRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_cc_rule_async(self, request):
        """创建cc规则

        创建cc规则
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateCcRule
        :type request: :class:`huaweicloudsdkwaf.v1.CreateCcRuleRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.CreateCcRuleResponse`
        """
        http_info = self._create_cc_rule_http_info(request)
        return self._call_api(**http_info)

    def create_cc_rule_async_invoker(self, request):
        http_info = self._create_cc_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_cc_rule_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/waf/policy/{policy_id}/cc",
            "request_type": request.__class__.__name__,
            "response_type": "CreateCcRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_certificate_async(self, request):
        """创建证书

        创建证书
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateCertificate
        :type request: :class:`huaweicloudsdkwaf.v1.CreateCertificateRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.CreateCertificateResponse`
        """
        http_info = self._create_certificate_http_info(request)
        return self._call_api(**http_info)

    def create_certificate_async_invoker(self, request):
        http_info = self._create_certificate_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_certificate_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/waf/certificate",
            "request_type": request.__class__.__name__,
            "response_type": "CreateCertificateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_cloud_waf_post_paid_resource_async(self, request):
        """开通云模式按需计费接口

        开通云模式按需计费接口
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateCloudWafPostPaidResource
        :type request: :class:`huaweicloudsdkwaf.v1.CreateCloudWafPostPaidResourceRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.CreateCloudWafPostPaidResourceResponse`
        """
        http_info = self._create_cloud_waf_post_paid_resource_http_info(request)
        return self._call_api(**http_info)

    def create_cloud_waf_post_paid_resource_async_invoker(self, request):
        http_info = self._create_cloud_waf_post_paid_resource_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_cloud_waf_post_paid_resource_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/waf/postpaid",
            "request_type": request.__class__.__name__,
            "response_type": "CreateCloudWafPostPaidResourceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

        header_params = {}
        if 'region' in local_var_params:
            header_params['region'] = local_var_params['region']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_custom_rule_async(self, request):
        """创建精准防护规则

        创建精准防护规则
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateCustomRule
        :type request: :class:`huaweicloudsdkwaf.v1.CreateCustomRuleRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.CreateCustomRuleResponse`
        """
        http_info = self._create_custom_rule_http_info(request)
        return self._call_api(**http_info)

    def create_custom_rule_async_invoker(self, request):
        http_info = self._create_custom_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_custom_rule_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/waf/policy/{policy_id}/custom",
            "request_type": request.__class__.__name__,
            "response_type": "CreateCustomRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_geoip_rule_async(self, request):
        """创建地理位置控制规则

        创建地理位置控制规则
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateGeoipRule
        :type request: :class:`huaweicloudsdkwaf.v1.CreateGeoipRuleRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.CreateGeoipRuleResponse`
        """
        http_info = self._create_geoip_rule_http_info(request)
        return self._call_api(**http_info)

    def create_geoip_rule_async_invoker(self, request):
        http_info = self._create_geoip_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_geoip_rule_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/waf/policy/{policy_id}/geoip",
            "request_type": request.__class__.__name__,
            "response_type": "CreateGeoipRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_host_async(self, request):
        """创建云模式防护域名

        创建云模式防护域名
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateHost
        :type request: :class:`huaweicloudsdkwaf.v1.CreateHostRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.CreateHostResponse`
        """
        http_info = self._create_host_http_info(request)
        return self._call_api(**http_info)

    def create_host_async_invoker(self, request):
        http_info = self._create_host_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_host_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/waf/instance",
            "request_type": request.__class__.__name__,
            "response_type": "CreateHostResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_ignore_rule_async(self, request):
        """创建全局白名单(原误报屏蔽)规则

        创建全局白名单(原误报屏蔽)规则
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateIgnoreRule
        :type request: :class:`huaweicloudsdkwaf.v1.CreateIgnoreRuleRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.CreateIgnoreRuleResponse`
        """
        http_info = self._create_ignore_rule_http_info(request)
        return self._call_api(**http_info)

    def create_ignore_rule_async_invoker(self, request):
        http_info = self._create_ignore_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_ignore_rule_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/waf/policy/{policy_id}/ignore",
            "request_type": request.__class__.__name__,
            "response_type": "CreateIgnoreRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_instance_async(self, request):
        """创建WAF独享引擎实例

        创建WAF独享引擎实例。独享模式只在部分局点支持，包括：华北-北京四、华东-上海一、华南-广州、华南-深圳  、中国-香港、亚太-曼谷、 亚太-新加坡。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateInstance
        :type request: :class:`huaweicloudsdkwaf.v1.CreateInstanceRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.CreateInstanceResponse`
        """
        http_info = self._create_instance_http_info(request)
        return self._call_api(**http_info)

    def create_instance_async_invoker(self, request):
        http_info = self._create_instance_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_instance_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/premium-waf/instance",
            "request_type": request.__class__.__name__,
            "response_type": "CreateInstanceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_ip_group_async(self, request):
        """创建ip地址组

        创建ip地址组
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateIpGroup
        :type request: :class:`huaweicloudsdkwaf.v1.CreateIpGroupRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.CreateIpGroupResponse`
        """
        http_info = self._create_ip_group_http_info(request)
        return self._call_api(**http_info)

    def create_ip_group_async_invoker(self, request):
        http_info = self._create_ip_group_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_ip_group_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/waf/ip-groups",
            "request_type": request.__class__.__name__,
            "response_type": "CreateIpGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_policy_async(self, request):
        """创建防护策略

        创建防护策略，系统会在生成策略时配置一些默认的配置项，如果需要修改策略的默认配置项需要通过调用更新防护策略接口实现
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreatePolicy
        :type request: :class:`huaweicloudsdkwaf.v1.CreatePolicyRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.CreatePolicyResponse`
        """
        http_info = self._create_policy_http_info(request)
        return self._call_api(**http_info)

    def create_policy_async_invoker(self, request):
        http_info = self._create_policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_policy_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/waf/policy",
            "request_type": request.__class__.__name__,
            "response_type": "CreatePolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_premium_host_async(self, request):
        """创建独享模式域名

        创建独享模式域名
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreatePremiumHost
        :type request: :class:`huaweicloudsdkwaf.v1.CreatePremiumHostRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.CreatePremiumHostResponse`
        """
        http_info = self._create_premium_host_http_info(request)
        return self._call_api(**http_info)

    def create_premium_host_async_invoker(self, request):
        http_info = self._create_premium_host_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_premium_host_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/premium-waf/host",
            "request_type": request.__class__.__name__,
            "response_type": "CreatePremiumHostResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_prepaid_cloud_waf_async(self, request):
        """购买包周期云模式waf

        购买包周期云模式waf。入门版waf不支持购买扩展包
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreatePrepaidCloudWaf
        :type request: :class:`huaweicloudsdkwaf.v1.CreatePrepaidCloudWafRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.CreatePrepaidCloudWafResponse`
        """
        http_info = self._create_prepaid_cloud_waf_http_info(request)
        return self._call_api(**http_info)

    def create_prepaid_cloud_waf_async_invoker(self, request):
        http_info = self._create_prepaid_cloud_waf_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_prepaid_cloud_waf_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/waf/subscription/purchase/prepaid-cloud-waf",
            "request_type": request.__class__.__name__,
            "response_type": "CreatePrepaidCloudWafResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_privacy_rule_async(self, request):
        """创建隐私屏蔽防护规则

        创建隐私屏蔽防护规则
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreatePrivacyRule
        :type request: :class:`huaweicloudsdkwaf.v1.CreatePrivacyRuleRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.CreatePrivacyRuleResponse`
        """
        http_info = self._create_privacy_rule_http_info(request)
        return self._call_api(**http_info)

    def create_privacy_rule_async_invoker(self, request):
        http_info = self._create_privacy_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_privacy_rule_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/waf/policy/{policy_id}/privacy",
            "request_type": request.__class__.__name__,
            "response_type": "CreatePrivacyRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_punishment_rule_async(self, request):
        """创建攻击惩罚规则

        创建攻击惩罚规则
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreatePunishmentRule
        :type request: :class:`huaweicloudsdkwaf.v1.CreatePunishmentRuleRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.CreatePunishmentRuleResponse`
        """
        http_info = self._create_punishment_rule_http_info(request)
        return self._call_api(**http_info)

    def create_punishment_rule_async_invoker(self, request):
        http_info = self._create_punishment_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_punishment_rule_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/waf/policy/{policy_id}/punishment",
            "request_type": request.__class__.__name__,
            "response_type": "CreatePunishmentRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_value_list_async(self, request):
        """创建引用表

        创建引用表，引用表能够被CC攻击防护规则和精准访问防护中的规则所引用。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateValueList
        :type request: :class:`huaweicloudsdkwaf.v1.CreateValueListRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.CreateValueListResponse`
        """
        http_info = self._create_value_list_http_info(request)
        return self._call_api(**http_info)

    def create_value_list_async_invoker(self, request):
        http_info = self._create_value_list_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_value_list_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/waf/valuelist",
            "request_type": request.__class__.__name__,
            "response_type": "CreateValueListResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_whiteblackip_rule_async(self, request):
        """创建黑白名单规则

        创建黑白名单规则
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateWhiteblackipRule
        :type request: :class:`huaweicloudsdkwaf.v1.CreateWhiteblackipRuleRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.CreateWhiteblackipRuleResponse`
        """
        http_info = self._create_whiteblackip_rule_http_info(request)
        return self._call_api(**http_info)

    def create_whiteblackip_rule_async_invoker(self, request):
        http_info = self._create_whiteblackip_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_whiteblackip_rule_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/waf/policy/{policy_id}/whiteblackip",
            "request_type": request.__class__.__name__,
            "response_type": "CreateWhiteblackipRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_anticrawler_rule_async(self, request):
        """删除JS脚本反爬虫防护规则

        删除JS脚本反爬虫防护规则
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteAnticrawlerRule
        :type request: :class:`huaweicloudsdkwaf.v1.DeleteAnticrawlerRuleRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.DeleteAnticrawlerRuleResponse`
        """
        http_info = self._delete_anticrawler_rule_http_info(request)
        return self._call_api(**http_info)

    def delete_anticrawler_rule_async_invoker(self, request):
        http_info = self._delete_anticrawler_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_anticrawler_rule_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/waf/policy/{policy_id}/anticrawler/{rule_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteAnticrawlerRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_antileakage_rule_async(self, request):
        """删除防敏感信息泄露防护规则

        删除防敏感信息泄露防护规则
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteAntileakageRule
        :type request: :class:`huaweicloudsdkwaf.v1.DeleteAntileakageRuleRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.DeleteAntileakageRuleResponse`
        """
        http_info = self._delete_antileakage_rule_http_info(request)
        return self._call_api(**http_info)

    def delete_antileakage_rule_async_invoker(self, request):
        http_info = self._delete_antileakage_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_antileakage_rule_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/waf/policy/{policy_id}/antileakage/{rule_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteAntileakageRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_antitamper_rule_async(self, request):
        """删除防篡改防护规则

        删除防篡改防护规则
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteAntitamperRule
        :type request: :class:`huaweicloudsdkwaf.v1.DeleteAntitamperRuleRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.DeleteAntitamperRuleResponse`
        """
        http_info = self._delete_antitamper_rule_http_info(request)
        return self._call_api(**http_info)

    def delete_antitamper_rule_async_invoker(self, request):
        http_info = self._delete_antitamper_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_antitamper_rule_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/waf/policy/{policy_id}/antitamper/{rule_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteAntitamperRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_cc_rule_async(self, request):
        """删除cc防护规则

        删除cc防护规则
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteCcRule
        :type request: :class:`huaweicloudsdkwaf.v1.DeleteCcRuleRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.DeleteCcRuleResponse`
        """
        http_info = self._delete_cc_rule_http_info(request)
        return self._call_api(**http_info)

    def delete_cc_rule_async_invoker(self, request):
        http_info = self._delete_cc_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_cc_rule_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/waf/policy/{policy_id}/cc/{rule_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteCcRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_certificate_async(self, request):
        """删除证书

        删除证书
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteCertificate
        :type request: :class:`huaweicloudsdkwaf.v1.DeleteCertificateRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.DeleteCertificateResponse`
        """
        http_info = self._delete_certificate_http_info(request)
        return self._call_api(**http_info)

    def delete_certificate_async_invoker(self, request):
        http_info = self._delete_certificate_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_certificate_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/waf/certificate/{certificate_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteCertificateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'certificate_id' in local_var_params:
            path_params['certificate_id'] = local_var_params['certificate_id']

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_cloud_waf_post_paid_resource_async(self, request):
        """关闭云模式按需计费接口

        关闭云模式按需计费接口
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteCloudWafPostPaidResource
        :type request: :class:`huaweicloudsdkwaf.v1.DeleteCloudWafPostPaidResourceRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.DeleteCloudWafPostPaidResourceResponse`
        """
        http_info = self._delete_cloud_waf_post_paid_resource_http_info(request)
        return self._call_api(**http_info)

    def delete_cloud_waf_post_paid_resource_async_invoker(self, request):
        http_info = self._delete_cloud_waf_post_paid_resource_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_cloud_waf_post_paid_resource_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/waf/postpaid",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteCloudWafPostPaidResourceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

        header_params = {}
        if 'region' in local_var_params:
            header_params['region'] = local_var_params['region']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_custom_rule_async(self, request):
        """删除精准防护规则

        删除精准防护规则
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteCustomRule
        :type request: :class:`huaweicloudsdkwaf.v1.DeleteCustomRuleRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.DeleteCustomRuleResponse`
        """
        http_info = self._delete_custom_rule_http_info(request)
        return self._call_api(**http_info)

    def delete_custom_rule_async_invoker(self, request):
        http_info = self._delete_custom_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_custom_rule_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/waf/policy/{policy_id}/custom/{rule_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteCustomRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_geoip_rule_async(self, request):
        """删除地理位置控制防护规则

        删除地理位置控制防护规则
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteGeoipRule
        :type request: :class:`huaweicloudsdkwaf.v1.DeleteGeoipRuleRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.DeleteGeoipRuleResponse`
        """
        http_info = self._delete_geoip_rule_http_info(request)
        return self._call_api(**http_info)

    def delete_geoip_rule_async_invoker(self, request):
        http_info = self._delete_geoip_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_geoip_rule_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/waf/policy/{policy_id}/geoip/{rule_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteGeoipRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_host_async(self, request):
        """删除云模式防护域名

        删除云模式防护域名
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteHost
        :type request: :class:`huaweicloudsdkwaf.v1.DeleteHostRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.DeleteHostResponse`
        """
        http_info = self._delete_host_http_info(request)
        return self._call_api(**http_info)

    def delete_host_async_invoker(self, request):
        http_info = self._delete_host_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_host_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/waf/instance/{instance_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteHostResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_ignore_rule_async(self, request):
        """删除全局白名单(原误报屏蔽)防护规则

        删除全局白名单(原误报屏蔽)防护规则
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteIgnoreRule
        :type request: :class:`huaweicloudsdkwaf.v1.DeleteIgnoreRuleRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.DeleteIgnoreRuleResponse`
        """
        http_info = self._delete_ignore_rule_http_info(request)
        return self._call_api(**http_info)

    def delete_ignore_rule_async_invoker(self, request):
        http_info = self._delete_ignore_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_ignore_rule_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/waf/policy/{policy_id}/ignore/{rule_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteIgnoreRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_instance_async(self, request):
        """删除WAF独享引擎信息

        删除WAF独享引擎信息。独享模式只在部分局点支持，包括：华北-北京四、华东-上海一、华南-广州、华南-深圳  、中国-香港、亚太-曼谷、 亚太-新加坡。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteInstance
        :type request: :class:`huaweicloudsdkwaf.v1.DeleteInstanceRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.DeleteInstanceResponse`
        """
        http_info = self._delete_instance_http_info(request)
        return self._call_api(**http_info)

    def delete_instance_async_invoker(self, request):
        http_info = self._delete_instance_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_instance_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/premium-waf/instance/{instance_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteInstanceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_ip_group_async(self, request):
        """删除ip地址组

        删除ip地址组
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteIpGroup
        :type request: :class:`huaweicloudsdkwaf.v1.DeleteIpGroupRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.DeleteIpGroupResponse`
        """
        http_info = self._delete_ip_group_http_info(request)
        return self._call_api(**http_info)

    def delete_ip_group_async_invoker(self, request):
        http_info = self._delete_ip_group_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_ip_group_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/waf/ip-group/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteIpGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_policy_async(self, request):
        """删除防护策略

        删除防护策略，若策略正在使用，则需要先接解除域名与策略的绑定关系才能删除策略。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeletePolicy
        :type request: :class:`huaweicloudsdkwaf.v1.DeletePolicyRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.DeletePolicyResponse`
        """
        http_info = self._delete_policy_http_info(request)
        return self._call_api(**http_info)

    def delete_policy_async_invoker(self, request):
        http_info = self._delete_policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_policy_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/waf/policy/{policy_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeletePolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_premium_host_async(self, request):
        """删除独享模式域名

        删除独享模式域名
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeletePremiumHost
        :type request: :class:`huaweicloudsdkwaf.v1.DeletePremiumHostRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.DeletePremiumHostResponse`
        """
        http_info = self._delete_premium_host_http_info(request)
        return self._call_api(**http_info)

    def delete_premium_host_async_invoker(self, request):
        http_info = self._delete_premium_host_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_premium_host_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/premium-waf/host/{host_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeletePremiumHostResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_privacy_rule_async(self, request):
        """删除隐私屏蔽防护规则

        删除隐私屏蔽防护规则
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeletePrivacyRule
        :type request: :class:`huaweicloudsdkwaf.v1.DeletePrivacyRuleRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.DeletePrivacyRuleResponse`
        """
        http_info = self._delete_privacy_rule_http_info(request)
        return self._call_api(**http_info)

    def delete_privacy_rule_async_invoker(self, request):
        http_info = self._delete_privacy_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_privacy_rule_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/waf/policy/{policy_id}/privacy/{rule_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeletePrivacyRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_punishment_rule_async(self, request):
        """删除攻击惩罚规则

        删除攻击惩罚规则
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeletePunishmentRule
        :type request: :class:`huaweicloudsdkwaf.v1.DeletePunishmentRuleRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.DeletePunishmentRuleResponse`
        """
        http_info = self._delete_punishment_rule_http_info(request)
        return self._call_api(**http_info)

    def delete_punishment_rule_async_invoker(self, request):
        http_info = self._delete_punishment_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_punishment_rule_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/waf/policy/{policy_id}/punishment/{rule_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeletePunishmentRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_value_list_async(self, request):
        """删除引用表

        删除引用表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteValueList
        :type request: :class:`huaweicloudsdkwaf.v1.DeleteValueListRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.DeleteValueListResponse`
        """
        http_info = self._delete_value_list_http_info(request)
        return self._call_api(**http_info)

    def delete_value_list_async_invoker(self, request):
        http_info = self._delete_value_list_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_value_list_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/waf/valuelist/{valuelistid}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteValueListResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'valuelistid' in local_var_params:
            path_params['valuelistid'] = local_var_params['valuelistid']

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_white_black_ip_rule_async(self, request):
        """删除黑白名单防护规则

        删除黑白名单防护规则
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteWhiteBlackIpRule
        :type request: :class:`huaweicloudsdkwaf.v1.DeleteWhiteBlackIpRuleRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.DeleteWhiteBlackIpRuleResponse`
        """
        http_info = self._delete_white_black_ip_rule_http_info(request)
        return self._call_api(**http_info)

    def delete_white_black_ip_rule_async_invoker(self, request):
        http_info = self._delete_white_black_ip_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_white_black_ip_rule_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/waf/policy/{policy_id}/whiteblackip/{rule_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteWhiteBlackIpRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_anticrawler_rules_async(self, request):
        """查询JS脚本反爬虫规则列表

        查询JS脚本反爬虫规则列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAnticrawlerRules
        :type request: :class:`huaweicloudsdkwaf.v1.ListAnticrawlerRulesRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.ListAnticrawlerRulesResponse`
        """
        http_info = self._list_anticrawler_rules_http_info(request)
        return self._call_api(**http_info)

    def list_anticrawler_rules_async_invoker(self, request):
        http_info = self._list_anticrawler_rules_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_anticrawler_rules_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/waf/policy/{policy_id}/anticrawler",
            "request_type": request.__class__.__name__,
            "response_type": "ListAnticrawlerRulesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_antileakage_rules_async(self, request):
        """查询防敏感信息泄露规则列表

        查询防敏感信息泄露规则列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAntileakageRules
        :type request: :class:`huaweicloudsdkwaf.v1.ListAntileakageRulesRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.ListAntileakageRulesResponse`
        """
        http_info = self._list_antileakage_rules_http_info(request)
        return self._call_api(**http_info)

    def list_antileakage_rules_async_invoker(self, request):
        http_info = self._list_antileakage_rules_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_antileakage_rules_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/waf/policy/{policy_id}/antileakage",
            "request_type": request.__class__.__name__,
            "response_type": "ListAntileakageRulesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_antitamper_rule_async(self, request):
        """查询防篡改规则列表

        查询防篡改规则列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAntitamperRule
        :type request: :class:`huaweicloudsdkwaf.v1.ListAntitamperRuleRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.ListAntitamperRuleResponse`
        """
        http_info = self._list_antitamper_rule_http_info(request)
        return self._call_api(**http_info)

    def list_antitamper_rule_async_invoker(self, request):
        http_info = self._list_antitamper_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_antitamper_rule_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/waf/policy/{policy_id}/antitamper",
            "request_type": request.__class__.__name__,
            "response_type": "ListAntitamperRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_bandwidth_timeline_async(self, request):
        """查询安全统计带宽数据

        查询安全统计带宽数据，统计的带宽数据为平均值，单位为bit/s。需要注意的是，安全统计相关的接口，暂时不能支持任意时间的查询。只能支持 console上显示的 昨天，今天，3天，7天和30天 数据查询。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListBandwidthTimeline
        :type request: :class:`huaweicloudsdkwaf.v1.ListBandwidthTimelineRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.ListBandwidthTimelineResponse`
        """
        http_info = self._list_bandwidth_timeline_http_info(request)
        return self._call_api(**http_info)

    def list_bandwidth_timeline_async_invoker(self, request):
        http_info = self._list_bandwidth_timeline_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_bandwidth_timeline_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/waf/overviews/bandwidth/timeline",
            "request_type": request.__class__.__name__,
            "response_type": "ListBandwidthTimelineResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_cc_rules_async(self, request):
        """查询cc规则列表

        查询cc规则列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListCcRules
        :type request: :class:`huaweicloudsdkwaf.v1.ListCcRulesRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.ListCcRulesResponse`
        """
        http_info = self._list_cc_rules_http_info(request)
        return self._call_api(**http_info)

    def list_cc_rules_async_invoker(self, request):
        http_info = self._list_cc_rules_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_cc_rules_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/waf/policy/{policy_id}/cc",
            "request_type": request.__class__.__name__,
            "response_type": "ListCcRulesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_certificates_async(self, request):
        """查询证书列表

        查询证书列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListCertificates
        :type request: :class:`huaweicloudsdkwaf.v1.ListCertificatesRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.ListCertificatesResponse`
        """
        http_info = self._list_certificates_http_info(request)
        return self._call_api(**http_info)

    def list_certificates_async_invoker(self, request):
        http_info = self._list_certificates_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_certificates_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/waf/certificate",
            "request_type": request.__class__.__name__,
            "response_type": "ListCertificatesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_composite_hosts_async(self, request):
        """查询全部防护域名列表

        查询全部防护域名列表，包括云模式和独享模式
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListCompositeHosts
        :type request: :class:`huaweicloudsdkwaf.v1.ListCompositeHostsRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.ListCompositeHostsResponse`
        """
        http_info = self._list_composite_hosts_http_info(request)
        return self._call_api(**http_info)

    def list_composite_hosts_async_invoker(self, request):
        http_info = self._list_composite_hosts_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_composite_hosts_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/composite-waf/host",
            "request_type": request.__class__.__name__,
            "response_type": "ListCompositeHostsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_custom_rules_async(self, request):
        """查询精准防护规则列表

        查询精准防护规则列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListCustomRules
        :type request: :class:`huaweicloudsdkwaf.v1.ListCustomRulesRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.ListCustomRulesResponse`
        """
        http_info = self._list_custom_rules_http_info(request)
        return self._call_api(**http_info)

    def list_custom_rules_async_invoker(self, request):
        http_info = self._list_custom_rules_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_custom_rules_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/waf/policy/{policy_id}/custom",
            "request_type": request.__class__.__name__,
            "response_type": "ListCustomRulesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_event_async(self, request):
        """查询攻击事件列表

        查询攻击事件列表，该API暂时不支持查询全部防护事件，pagesize参数不可设为-1，由于性能原因，数据量越大消耗的内存越大，后端最多限制查询10000条数据，例如：自定义时间段内的数据超过了10000条，就无法查出page为101，pagesize为100之后的数据，需要调整时间区间，再进行查询
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListEvent
        :type request: :class:`huaweicloudsdkwaf.v1.ListEventRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.ListEventResponse`
        """
        http_info = self._list_event_http_info(request)
        return self._call_api(**http_info)

    def list_event_async_invoker(self, request):
        http_info = self._list_event_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_event_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/waf/event",
            "request_type": request.__class__.__name__,
            "response_type": "ListEventResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_geoip_rule_async(self, request):
        """查询地理位置访问控制规则列表

        查询地理位置访问控制规则列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListGeoipRule
        :type request: :class:`huaweicloudsdkwaf.v1.ListGeoipRuleRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.ListGeoipRuleResponse`
        """
        http_info = self._list_geoip_rule_http_info(request)
        return self._call_api(**http_info)

    def list_geoip_rule_async_invoker(self, request):
        http_info = self._list_geoip_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_geoip_rule_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/waf/policy/{policy_id}/geoip",
            "request_type": request.__class__.__name__,
            "response_type": "ListGeoipRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_host_async(self, request):
        """查询云模式防护域名列表

        查询云模式防护域名列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListHost
        :type request: :class:`huaweicloudsdkwaf.v1.ListHostRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.ListHostResponse`
        """
        http_info = self._list_host_http_info(request)
        return self._call_api(**http_info)

    def list_host_async_invoker(self, request):
        http_info = self._list_host_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_host_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/waf/instance",
            "request_type": request.__class__.__name__,
            "response_type": "ListHostResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_host_route_async(self, request):
        """获取云模式域名路由信息

        返回路由信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListHostRoute
        :type request: :class:`huaweicloudsdkwaf.v1.ListHostRouteRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.ListHostRouteResponse`
        """
        http_info = self._list_host_route_http_info(request)
        return self._call_api(**http_info)

    def list_host_route_async_invoker(self, request):
        http_info = self._list_host_route_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_host_route_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/waf/instance/{instance_id}/route",
            "request_type": request.__class__.__name__,
            "response_type": "ListHostRouteResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_ignore_rule_async(self, request):
        """查询全局白名单(原误报屏蔽)规则列表

        查询全局白名单(原误报屏蔽)规则列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListIgnoreRule
        :type request: :class:`huaweicloudsdkwaf.v1.ListIgnoreRuleRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.ListIgnoreRuleResponse`
        """
        http_info = self._list_ignore_rule_http_info(request)
        return self._call_api(**http_info)

    def list_ignore_rule_async_invoker(self, request):
        http_info = self._list_ignore_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_ignore_rule_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/waf/policy/{policy_id}/ignore",
            "request_type": request.__class__.__name__,
            "response_type": "ListIgnoreRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_instance_async(self, request):
        """查询WAF独享引擎列表

        查询WAF独享引擎列表。独享模式只在部分局点支持，包括：华北-北京四、华东-上海一、华南-广州、华南-深圳  、中国-香港、亚太-曼谷、 亚太-新加坡。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListInstance
        :type request: :class:`huaweicloudsdkwaf.v1.ListInstanceRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.ListInstanceResponse`
        """
        http_info = self._list_instance_http_info(request)
        return self._call_api(**http_info)

    def list_instance_async_invoker(self, request):
        http_info = self._list_instance_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_instance_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/premium-waf/instance",
            "request_type": request.__class__.__name__,
            "response_type": "ListInstanceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_ip_group_async(self, request):
        """查询地址组列表

        查询地址组列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListIpGroup
        :type request: :class:`huaweicloudsdkwaf.v1.ListIpGroupRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.ListIpGroupResponse`
        """
        http_info = self._list_ip_group_http_info(request)
        return self._call_api(**http_info)

    def list_ip_group_async_invoker(self, request):
        http_info = self._list_ip_group_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_ip_group_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/waf/ip-groups",
            "request_type": request.__class__.__name__,
            "response_type": "ListIpGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_notice_configs_async(self, request):
        """查询告警通知配置

        查询告警通知配置
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListNoticeConfigs
        :type request: :class:`huaweicloudsdkwaf.v1.ListNoticeConfigsRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.ListNoticeConfigsResponse`
        """
        http_info = self._list_notice_configs_http_info(request)
        return self._call_api(**http_info)

    def list_notice_configs_async_invoker(self, request):
        http_info = self._list_notice_configs_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_notice_configs_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/waf/alerts",
            "request_type": request.__class__.__name__,
            "response_type": "ListNoticeConfigsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_overviews_classification_async(self, request):
        """查询安全总览分类统计top信息

        查询安全总览分类统计TOP信息，包含受攻击域名 、攻击源ip、受攻击URL、攻击来源区域、攻击事件分布。需要注意的是，安全总览相关的接口，暂时不能支持任意时间的查询。只能支持 console上显示的 昨天，今天，3天，7天和30天 数据查询。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListOverviewsClassification
        :type request: :class:`huaweicloudsdkwaf.v1.ListOverviewsClassificationRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.ListOverviewsClassificationResponse`
        """
        http_info = self._list_overviews_classification_http_info(request)
        return self._call_api(**http_info)

    def list_overviews_classification_async_invoker(self, request):
        http_info = self._list_overviews_classification_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_overviews_classification_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/waf/overviews/classification",
            "request_type": request.__class__.__name__,
            "response_type": "ListOverviewsClassificationResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_policy_async(self, request):
        """查询防护策略列表

        查询防护策略列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListPolicy
        :type request: :class:`huaweicloudsdkwaf.v1.ListPolicyRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.ListPolicyResponse`
        """
        http_info = self._list_policy_http_info(request)
        return self._call_api(**http_info)

    def list_policy_async_invoker(self, request):
        http_info = self._list_policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_policy_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/waf/policy",
            "request_type": request.__class__.__name__,
            "response_type": "ListPolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_premium_host_async(self, request):
        """独享模式域名列表

        独享模式域名列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListPremiumHost
        :type request: :class:`huaweicloudsdkwaf.v1.ListPremiumHostRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.ListPremiumHostResponse`
        """
        http_info = self._list_premium_host_http_info(request)
        return self._call_api(**http_info)

    def list_premium_host_async_invoker(self, request):
        http_info = self._list_premium_host_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_premium_host_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/premium-waf/host",
            "request_type": request.__class__.__name__,
            "response_type": "ListPremiumHostResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_privacy_rule_async(self, request):
        """查询隐私屏蔽防护规则列表

        查询隐私屏蔽防护规则列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListPrivacyRule
        :type request: :class:`huaweicloudsdkwaf.v1.ListPrivacyRuleRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.ListPrivacyRuleResponse`
        """
        http_info = self._list_privacy_rule_http_info(request)
        return self._call_api(**http_info)

    def list_privacy_rule_async_invoker(self, request):
        http_info = self._list_privacy_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_privacy_rule_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/waf/policy/{policy_id}/privacy",
            "request_type": request.__class__.__name__,
            "response_type": "ListPrivacyRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_punishment_rules_async(self, request):
        """查询攻击惩罚规则列表

        查询攻击惩罚规则列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListPunishmentRules
        :type request: :class:`huaweicloudsdkwaf.v1.ListPunishmentRulesRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.ListPunishmentRulesResponse`
        """
        http_info = self._list_punishment_rules_http_info(request)
        return self._call_api(**http_info)

    def list_punishment_rules_async_invoker(self, request):
        http_info = self._list_punishment_rules_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_punishment_rules_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/waf/policy/{policy_id}/punishment",
            "request_type": request.__class__.__name__,
            "response_type": "ListPunishmentRulesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_qps_timeline_async(self, request):
        """查询安全统计qps次数

        查询安全统计qps次数。需要注意的是，安全统计相关的接口，暂时不能支持任意时间的查询。只能支持 console上显示的 昨天，今天，3天，7天和30天 数据查询。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListQpsTimeline
        :type request: :class:`huaweicloudsdkwaf.v1.ListQpsTimelineRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.ListQpsTimelineResponse`
        """
        http_info = self._list_qps_timeline_http_info(request)
        return self._call_api(**http_info)

    def list_qps_timeline_async_invoker(self, request):
        http_info = self._list_qps_timeline_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_qps_timeline_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/waf/overviews/qps/timeline",
            "request_type": request.__class__.__name__,
            "response_type": "ListQpsTimelineResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_request_timeline_async(self, request):
        """查询安全总览中请求次数时间线统计数据

        查询安全总览中请求次数时间线统计数据。需要注意的是，安全总览相关的接口，暂时不能支持任意时间的查询。只能支持 console上显示的 昨天，今天，3天，7天和30天 数据查询。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListRequestTimeline
        :type request: :class:`huaweicloudsdkwaf.v1.ListRequestTimelineRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.ListRequestTimelineResponse`
        """
        http_info = self._list_request_timeline_http_info(request)
        return self._call_api(**http_info)

    def list_request_timeline_async_invoker(self, request):
        http_info = self._list_request_timeline_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_request_timeline_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/waf/overviews/request/timeline",
            "request_type": request.__class__.__name__,
            "response_type": "ListRequestTimelineResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_statistics_async(self, request):
        """查询安全总览请求与攻击数量

        查询安全总览请求与攻击数量。需要注意的是，安全总览相关的接口，暂时不能支持任意时间的查询。只能支持 console上显示的 昨天，今天，3天，7天和30天 数据查询。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListStatistics
        :type request: :class:`huaweicloudsdkwaf.v1.ListStatisticsRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.ListStatisticsResponse`
        """
        http_info = self._list_statistics_http_info(request)
        return self._call_api(**http_info)

    def list_statistics_async_invoker(self, request):
        http_info = self._list_statistics_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_statistics_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/waf/overviews/statistics",
            "request_type": request.__class__.__name__,
            "response_type": "ListStatisticsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_top_abnormal_async(self, request):
        """查询业务异常数量

        查询业务异常TOP统计信息。需要注意的是，安全总览相关的接口，暂时不能支持任意时间的查询。只能支持 console上显示的 昨天，今天，3天，7天和30天 数据查询。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListTopAbnormal
        :type request: :class:`huaweicloudsdkwaf.v1.ListTopAbnormalRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.ListTopAbnormalResponse`
        """
        http_info = self._list_top_abnormal_http_info(request)
        return self._call_api(**http_info)

    def list_top_abnormal_async_invoker(self, request):
        http_info = self._list_top_abnormal_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_top_abnormal_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/waf/overviews/abnormal",
            "request_type": request.__class__.__name__,
            "response_type": "ListTopAbnormalResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_value_list_async(self, request):
        """查询引用表列表

        查询引用表列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListValueList
        :type request: :class:`huaweicloudsdkwaf.v1.ListValueListRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.ListValueListResponse`
        """
        http_info = self._list_value_list_http_info(request)
        return self._call_api(**http_info)

    def list_value_list_async_invoker(self, request):
        http_info = self._list_value_list_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_value_list_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/waf/valuelist",
            "request_type": request.__class__.__name__,
            "response_type": "ListValueListResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_whiteblackip_rule_async(self, request):
        """查询黑白名单规则列表

        查询黑白名单规则列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListWhiteblackipRule
        :type request: :class:`huaweicloudsdkwaf.v1.ListWhiteblackipRuleRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.ListWhiteblackipRuleResponse`
        """
        http_info = self._list_whiteblackip_rule_http_info(request)
        return self._call_api(**http_info)

    def list_whiteblackip_rule_async_invoker(self, request):
        http_info = self._list_whiteblackip_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_whiteblackip_rule_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/waf/policy/{policy_id}/whiteblackip",
            "request_type": request.__class__.__name__,
            "response_type": "ListWhiteblackipRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def migrate_composite_hosts_async(self, request):
        """按企业项目迁移防护域名

        按企业项目迁移防护域名，仅专业版与独享版支持该功能
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for MigrateCompositeHosts
        :type request: :class:`huaweicloudsdkwaf.v1.MigrateCompositeHostsRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.MigrateCompositeHostsResponse`
        """
        http_info = self._migrate_composite_hosts_http_info(request)
        return self._call_api(**http_info)

    def migrate_composite_hosts_async_invoker(self, request):
        http_info = self._migrate_composite_hosts_http_info(request)
        return AsyncInvoker(self, http_info)

    def _migrate_composite_hosts_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/composite-waf/hosts/migration",
            "request_type": request.__class__.__name__,
            "response_type": "MigrateCompositeHostsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'target_enterprise_project_id' in local_var_params:
            query_params.append(('target_enterprise_project_id', local_var_params['target_enterprise_project_id']))

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def rename_instance_async(self, request):
        """重命名WAF独享引擎

        重命名WAF独享引擎。独享模式只在部分局点支持，包括：华北-北京四、华东-上海一、华南-广州、华南-深圳  、中国-香港、亚太-曼谷、 亚太-新加坡。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RenameInstance
        :type request: :class:`huaweicloudsdkwaf.v1.RenameInstanceRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.RenameInstanceResponse`
        """
        http_info = self._rename_instance_http_info(request)
        return self._call_api(**http_info)

    def rename_instance_async_invoker(self, request):
        http_info = self._rename_instance_http_info(request)
        return AsyncInvoker(self, http_info)

    def _rename_instance_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/premium-waf/instance/{instance_id}",
            "request_type": request.__class__.__name__,
            "response_type": "RenameInstanceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_anticrawler_rule_async(self, request):
        """查询JS脚本反爬虫防护规则

        根据Id查询JS脚本反爬虫防护规则
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowAnticrawlerRule
        :type request: :class:`huaweicloudsdkwaf.v1.ShowAnticrawlerRuleRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.ShowAnticrawlerRuleResponse`
        """
        http_info = self._show_anticrawler_rule_http_info(request)
        return self._call_api(**http_info)

    def show_anticrawler_rule_async_invoker(self, request):
        http_info = self._show_anticrawler_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_anticrawler_rule_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/waf/policy/{policy_id}/anticrawler/{rule_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAnticrawlerRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_antileakage_rule_async(self, request):
        """查询防敏感信息泄露防护规则

        根据Id查询防敏感信息泄露防护规则
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowAntileakageRule
        :type request: :class:`huaweicloudsdkwaf.v1.ShowAntileakageRuleRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.ShowAntileakageRuleResponse`
        """
        http_info = self._show_antileakage_rule_http_info(request)
        return self._call_api(**http_info)

    def show_antileakage_rule_async_invoker(self, request):
        http_info = self._show_antileakage_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_antileakage_rule_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/waf/policy/{policy_id}/antileakage/{rule_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAntileakageRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_antitamper_rule_async(self, request):
        """查询防篡改防护规则

        查询防篡改防护规则
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowAntitamperRule
        :type request: :class:`huaweicloudsdkwaf.v1.ShowAntitamperRuleRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.ShowAntitamperRuleResponse`
        """
        http_info = self._show_antitamper_rule_http_info(request)
        return self._call_api(**http_info)

    def show_antitamper_rule_async_invoker(self, request):
        http_info = self._show_antitamper_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_antitamper_rule_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/waf/policy/{policy_id}/antitamper/{rule_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAntitamperRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_cc_rule_async(self, request):
        """根据Id查询cc防护规则

        根据Id查询cc防护规则
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowCcRule
        :type request: :class:`huaweicloudsdkwaf.v1.ShowCcRuleRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.ShowCcRuleResponse`
        """
        http_info = self._show_cc_rule_http_info(request)
        return self._call_api(**http_info)

    def show_cc_rule_async_invoker(self, request):
        http_info = self._show_cc_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_cc_rule_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/waf/policy/{policy_id}/cc/{rule_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowCcRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_certificate_async(self, request):
        """查询证书

        查询证书
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowCertificate
        :type request: :class:`huaweicloudsdkwaf.v1.ShowCertificateRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.ShowCertificateResponse`
        """
        http_info = self._show_certificate_http_info(request)
        return self._call_api(**http_info)

    def show_certificate_async_invoker(self, request):
        http_info = self._show_certificate_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_certificate_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/waf/certificate/{certificate_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowCertificateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'certificate_id' in local_var_params:
            path_params['certificate_id'] = local_var_params['certificate_id']

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_composite_host_async(self, request):
        """根据Id查询防护域名

        根据Id查询防护域名
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowCompositeHost
        :type request: :class:`huaweicloudsdkwaf.v1.ShowCompositeHostRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.ShowCompositeHostResponse`
        """
        http_info = self._show_composite_host_http_info(request)
        return self._call_api(**http_info)

    def show_composite_host_async_invoker(self, request):
        http_info = self._show_composite_host_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_composite_host_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/composite-waf/host/{host_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowCompositeHostResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'host_id' in local_var_params:
            path_params['host_id'] = local_var_params['host_id']

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_console_config_async(self, request):
        """局点支持特性查询

        局点支持特性查询
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowConsoleConfig
        :type request: :class:`huaweicloudsdkwaf.v1.ShowConsoleConfigRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.ShowConsoleConfigResponse`
        """
        http_info = self._show_console_config_http_info(request)
        return self._call_api(**http_info)

    def show_console_config_async_invoker(self, request):
        http_info = self._show_console_config_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_console_config_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/waf/config/console",
            "request_type": request.__class__.__name__,
            "response_type": "ShowConsoleConfigResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_custom_rule_async(self, request):
        """根据Id查询精准防护规则

        根据Id查询精准防护规则
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowCustomRule
        :type request: :class:`huaweicloudsdkwaf.v1.ShowCustomRuleRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.ShowCustomRuleResponse`
        """
        http_info = self._show_custom_rule_http_info(request)
        return self._call_api(**http_info)

    def show_custom_rule_async_invoker(self, request):
        http_info = self._show_custom_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_custom_rule_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/waf/policy/{policy_id}/custom/{rule_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowCustomRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_event_async(self, request):
        """查询指定事件id的防护事件详情

        查询指定事件id的防护事件详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowEvent
        :type request: :class:`huaweicloudsdkwaf.v1.ShowEventRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.ShowEventResponse`
        """
        http_info = self._show_event_http_info(request)
        return self._call_api(**http_info)

    def show_event_async_invoker(self, request):
        http_info = self._show_event_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_event_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/waf/event/{eventid}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowEventResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eventid' in local_var_params:
            path_params['eventid'] = local_var_params['eventid']

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_geoip_rule_async(self, request):
        """删除地理位置控制防护规则

        删除地理位置控制防护规则
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowGeoipRule
        :type request: :class:`huaweicloudsdkwaf.v1.ShowGeoipRuleRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.ShowGeoipRuleResponse`
        """
        http_info = self._show_geoip_rule_http_info(request)
        return self._call_api(**http_info)

    def show_geoip_rule_async_invoker(self, request):
        http_info = self._show_geoip_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_geoip_rule_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/waf/policy/{policy_id}/geoip/{rule_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowGeoipRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_host_async(self, request):
        """根据防护域名Id查询云模式防护域名详细信息

        根据防护域名Id查询云模式防护域名详细信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowHost
        :type request: :class:`huaweicloudsdkwaf.v1.ShowHostRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.ShowHostResponse`
        """
        http_info = self._show_host_http_info(request)
        return self._call_api(**http_info)

    def show_host_async_invoker(self, request):
        http_info = self._show_host_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_host_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/waf/instance/{instance_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowHostResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_ignore_rule_async(self, request):
        """查询全局白名单(原误报屏蔽)防护规则

        查询全局白名单(原误报屏蔽)防护规则
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowIgnoreRule
        :type request: :class:`huaweicloudsdkwaf.v1.ShowIgnoreRuleRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.ShowIgnoreRuleResponse`
        """
        http_info = self._show_ignore_rule_http_info(request)
        return self._call_api(**http_info)

    def show_ignore_rule_async_invoker(self, request):
        http_info = self._show_ignore_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_ignore_rule_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/waf/policy/{policy_id}/ignore/{rule_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowIgnoreRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_instance_async(self, request):
        """查询WAF独享引擎信息

        查询WAF独享引擎信息。独享模式只在部分局点支持，包括：华北-北京四、华东-上海一、华南-广州、华南-深圳  、中国-香港、亚太-曼谷、 亚太-新加坡。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowInstance
        :type request: :class:`huaweicloudsdkwaf.v1.ShowInstanceRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.ShowInstanceResponse`
        """
        http_info = self._show_instance_http_info(request)
        return self._call_api(**http_info)

    def show_instance_async_invoker(self, request):
        http_info = self._show_instance_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_instance_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/premium-waf/instance/{instance_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowInstanceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_ip_group_async(self, request):
        """查询ip地址组明细

        查询ip地址组明细
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowIpGroup
        :type request: :class:`huaweicloudsdkwaf.v1.ShowIpGroupRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.ShowIpGroupResponse`
        """
        http_info = self._show_ip_group_http_info(request)
        return self._call_api(**http_info)

    def show_ip_group_async_invoker(self, request):
        http_info = self._show_ip_group_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_ip_group_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/waf/ip-group/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowIpGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_lts_info_config_async(self, request):
        """查询lts配置信息

        查询lts配置信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowLtsInfoConfig
        :type request: :class:`huaweicloudsdkwaf.v1.ShowLtsInfoConfigRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.ShowLtsInfoConfigResponse`
        """
        http_info = self._show_lts_info_config_http_info(request)
        return self._call_api(**http_info)

    def show_lts_info_config_async_invoker(self, request):
        http_info = self._show_lts_info_config_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_lts_info_config_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/waf/config/lts",
            "request_type": request.__class__.__name__,
            "response_type": "ShowLtsInfoConfigResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_policy_async(self, request):
        """根据Id查询防护策略

        根据Id查询防护策略
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowPolicy
        :type request: :class:`huaweicloudsdkwaf.v1.ShowPolicyRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.ShowPolicyResponse`
        """
        http_info = self._show_policy_http_info(request)
        return self._call_api(**http_info)

    def show_policy_async_invoker(self, request):
        http_info = self._show_policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_policy_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/waf/policy/{policy_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowPolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_premium_host_async(self, request):
        """查看独享模式域名配置

        查看独享模式域名配置
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowPremiumHost
        :type request: :class:`huaweicloudsdkwaf.v1.ShowPremiumHostRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.ShowPremiumHostResponse`
        """
        http_info = self._show_premium_host_http_info(request)
        return self._call_api(**http_info)

    def show_premium_host_async_invoker(self, request):
        http_info = self._show_premium_host_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_premium_host_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/premium-waf/host/{host_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowPremiumHostResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'host_id' in local_var_params:
            path_params['host_id'] = local_var_params['host_id']

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_privacy_rule_async(self, request):
        """查询隐私屏蔽防护规则

        删除隐私屏蔽防护规则
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowPrivacyRule
        :type request: :class:`huaweicloudsdkwaf.v1.ShowPrivacyRuleRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.ShowPrivacyRuleResponse`
        """
        http_info = self._show_privacy_rule_http_info(request)
        return self._call_api(**http_info)

    def show_privacy_rule_async_invoker(self, request):
        http_info = self._show_privacy_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_privacy_rule_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/waf/policy/{policy_id}/privacy/{rule_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowPrivacyRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_punishment_rule_async(self, request):
        """根据Id查询攻击惩罚防护规则

        根据Id查询攻击惩罚防护规则
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowPunishmentRule
        :type request: :class:`huaweicloudsdkwaf.v1.ShowPunishmentRuleRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.ShowPunishmentRuleResponse`
        """
        http_info = self._show_punishment_rule_http_info(request)
        return self._call_api(**http_info)

    def show_punishment_rule_async_invoker(self, request):
        http_info = self._show_punishment_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_punishment_rule_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/waf/policy/{policy_id}/punishment/{rule_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowPunishmentRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_source_ip_async(self, request):
        """查询WAF回源Ip信息

        查询WAF回源Ip信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowSourceIp
        :type request: :class:`huaweicloudsdkwaf.v1.ShowSourceIpRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.ShowSourceIpResponse`
        """
        http_info = self._show_source_ip_http_info(request)
        return self._call_api(**http_info)

    def show_source_ip_async_invoker(self, request):
        http_info = self._show_source_ip_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_source_ip_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/waf/config/source-ip",
            "request_type": request.__class__.__name__,
            "response_type": "ShowSourceIpResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_subscription_info_async(self, request):
        """查询租户订购信息

        查询租户订购信息，包括云模式包周期、按需计费、独享模式
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowSubscriptionInfo
        :type request: :class:`huaweicloudsdkwaf.v1.ShowSubscriptionInfoRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.ShowSubscriptionInfoResponse`
        """
        http_info = self._show_subscription_info_http_info(request)
        return self._call_api(**http_info)

    def show_subscription_info_async_invoker(self, request):
        http_info = self._show_subscription_info_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_subscription_info_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/waf/subscription",
            "request_type": request.__class__.__name__,
            "response_type": "ShowSubscriptionInfoResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_value_list_async(self, request):
        """查询引用表

        查询引用表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowValueList
        :type request: :class:`huaweicloudsdkwaf.v1.ShowValueListRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.ShowValueListResponse`
        """
        http_info = self._show_value_list_http_info(request)
        return self._call_api(**http_info)

    def show_value_list_async_invoker(self, request):
        http_info = self._show_value_list_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_value_list_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/waf/valuelist/{valuelistid}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowValueListResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'valuelistid' in local_var_params:
            path_params['valuelistid'] = local_var_params['valuelistid']

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_white_black_ip_rule_async(self, request):
        """查询黑白名单防护规则

        查询黑白名单防护规则
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowWhiteBlackIpRule
        :type request: :class:`huaweicloudsdkwaf.v1.ShowWhiteBlackIpRuleRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.ShowWhiteBlackIpRuleResponse`
        """
        http_info = self._show_white_black_ip_rule_http_info(request)
        return self._call_api(**http_info)

    def show_white_black_ip_rule_async_invoker(self, request):
        http_info = self._show_white_black_ip_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_white_black_ip_rule_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/waf/policy/{policy_id}/whiteblackip/{rule_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowWhiteBlackIpRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_alert_notice_config_async(self, request):
        """更新告警通知配置

        更新告警通知配置
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateAlertNoticeConfig
        :type request: :class:`huaweicloudsdkwaf.v1.UpdateAlertNoticeConfigRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.UpdateAlertNoticeConfigResponse`
        """
        http_info = self._update_alert_notice_config_http_info(request)
        return self._call_api(**http_info)

    def update_alert_notice_config_async_invoker(self, request):
        http_info = self._update_alert_notice_config_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_alert_notice_config_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/waf/alert/{alert_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateAlertNoticeConfigResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'alert_id' in local_var_params:
            path_params['alert_id'] = local_var_params['alert_id']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_anti_tamper_rule_refresh_async(self, request):
        """网页防篡改规则更新缓存

        网页防篡改规则更新缓存
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateAntiTamperRuleRefresh
        :type request: :class:`huaweicloudsdkwaf.v1.UpdateAntiTamperRuleRefreshRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.UpdateAntiTamperRuleRefreshResponse`
        """
        http_info = self._update_anti_tamper_rule_refresh_http_info(request)
        return self._call_api(**http_info)

    def update_anti_tamper_rule_refresh_async_invoker(self, request):
        http_info = self._update_anti_tamper_rule_refresh_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_anti_tamper_rule_refresh_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/waf/policy/{policy_id}/antitamper/{rule_id}/refresh",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateAntiTamperRuleRefreshResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_anticrawler_rule_async(self, request):
        """更新JS脚本反爬虫防护规则

        更新JS脚本反爬虫防护规则
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateAnticrawlerRule
        :type request: :class:`huaweicloudsdkwaf.v1.UpdateAnticrawlerRuleRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.UpdateAnticrawlerRuleResponse`
        """
        http_info = self._update_anticrawler_rule_http_info(request)
        return self._call_api(**http_info)

    def update_anticrawler_rule_async_invoker(self, request):
        http_info = self._update_anticrawler_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_anticrawler_rule_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/waf/policy/{policy_id}/anticrawler/{rule_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateAnticrawlerRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_anticrawler_rule_type_async(self, request):
        """更新JS脚本反爬虫规则防护模式

        更新JS脚本反爬虫规则防护模式，在创建JS脚本反爬虫规则前，需要调用该接口指定JS脚本反爬虫规则防护模式。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateAnticrawlerRuleType
        :type request: :class:`huaweicloudsdkwaf.v1.UpdateAnticrawlerRuleTypeRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.UpdateAnticrawlerRuleTypeResponse`
        """
        http_info = self._update_anticrawler_rule_type_http_info(request)
        return self._call_api(**http_info)

    def update_anticrawler_rule_type_async_invoker(self, request):
        http_info = self._update_anticrawler_rule_type_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_anticrawler_rule_type_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/waf/policy/{policy_id}/anticrawler",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateAnticrawlerRuleTypeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_antileakage_rule_async(self, request):
        """更新防敏感信息泄露防护规则

        更新防敏感信息泄露防护规则
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateAntileakageRule
        :type request: :class:`huaweicloudsdkwaf.v1.UpdateAntileakageRuleRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.UpdateAntileakageRuleResponse`
        """
        http_info = self._update_antileakage_rule_http_info(request)
        return self._call_api(**http_info)

    def update_antileakage_rule_async_invoker(self, request):
        http_info = self._update_antileakage_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_antileakage_rule_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/waf/policy/{policy_id}/antileakage/{rule_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateAntileakageRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_cc_rule_async(self, request):
        """更新cc防护规则

        更新cc防护规则
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateCcRule
        :type request: :class:`huaweicloudsdkwaf.v1.UpdateCcRuleRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.UpdateCcRuleResponse`
        """
        http_info = self._update_cc_rule_http_info(request)
        return self._call_api(**http_info)

    def update_cc_rule_async_invoker(self, request):
        http_info = self._update_cc_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_cc_rule_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/waf/policy/{policy_id}/cc/{rule_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateCcRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_certificate_async(self, request):
        """修改证书

        修改证书
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateCertificate
        :type request: :class:`huaweicloudsdkwaf.v1.UpdateCertificateRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.UpdateCertificateResponse`
        """
        http_info = self._update_certificate_http_info(request)
        return self._call_api(**http_info)

    def update_certificate_async_invoker(self, request):
        http_info = self._update_certificate_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_certificate_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/waf/certificate/{certificate_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateCertificateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'certificate_id' in local_var_params:
            path_params['certificate_id'] = local_var_params['certificate_id']

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_custom_rule_async(self, request):
        """更新精准防护规则

        更新精准防护规则
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateCustomRule
        :type request: :class:`huaweicloudsdkwaf.v1.UpdateCustomRuleRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.UpdateCustomRuleResponse`
        """
        http_info = self._update_custom_rule_http_info(request)
        return self._call_api(**http_info)

    def update_custom_rule_async_invoker(self, request):
        http_info = self._update_custom_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_custom_rule_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/waf/policy/{policy_id}/custom/{rule_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateCustomRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_geoip_rule_async(self, request):
        """更新地理位置控制防护规则

        更新地理位置控制防护规则
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateGeoipRule
        :type request: :class:`huaweicloudsdkwaf.v1.UpdateGeoipRuleRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.UpdateGeoipRuleResponse`
        """
        http_info = self._update_geoip_rule_http_info(request)
        return self._call_api(**http_info)

    def update_geoip_rule_async_invoker(self, request):
        http_info = self._update_geoip_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_geoip_rule_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/waf/policy/{policy_id}/geoip/{rule_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateGeoipRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_host_async(self, request):
        """更新云模式防护域名的配置

        更新云模式防护域名配置，在没有填入源站信息server的原始数据的情况下，则新的源站信息server会覆盖源站信息，而不是新增源站。此外，请求体可只传需要更新的部分。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateHost
        :type request: :class:`huaweicloudsdkwaf.v1.UpdateHostRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.UpdateHostResponse`
        """
        http_info = self._update_host_http_info(request)
        return self._call_api(**http_info)

    def update_host_async_invoker(self, request):
        http_info = self._update_host_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_host_http_info(self, request):
        http_info = {
            "method": "PATCH",
            "resource_path": "/v1/{project_id}/waf/instance/{instance_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateHostResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_host_protect_status_async(self, request):
        """修改域名防护状态

        修改域名防护状态
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateHostProtectStatus
        :type request: :class:`huaweicloudsdkwaf.v1.UpdateHostProtectStatusRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.UpdateHostProtectStatusResponse`
        """
        http_info = self._update_host_protect_status_http_info(request)
        return self._call_api(**http_info)

    def update_host_protect_status_async_invoker(self, request):
        http_info = self._update_host_protect_status_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_host_protect_status_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/waf/instance/{instance_id}/protect-status",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateHostProtectStatusResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_ignore_rule_async(self, request):
        """更新全局白名单(原误报屏蔽)防护规则

        更新全局白名单(原误报屏蔽)防护规则
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateIgnoreRule
        :type request: :class:`huaweicloudsdkwaf.v1.UpdateIgnoreRuleRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.UpdateIgnoreRuleResponse`
        """
        http_info = self._update_ignore_rule_http_info(request)
        return self._call_api(**http_info)

    def update_ignore_rule_async_invoker(self, request):
        http_info = self._update_ignore_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_ignore_rule_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/waf/policy/{policy_id}/ignore/{rule_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateIgnoreRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_ip_group_async(self, request):
        """修改ip地址组

        修改ip地址组
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateIpGroup
        :type request: :class:`huaweicloudsdkwaf.v1.UpdateIpGroupRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.UpdateIpGroupResponse`
        """
        http_info = self._update_ip_group_http_info(request)
        return self._call_api(**http_info)

    def update_ip_group_async_invoker(self, request):
        http_info = self._update_ip_group_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_ip_group_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/waf/ip-group/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateIpGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_lts_info_config_async(self, request):
        """配置全量日志lts

        配置全量日志lts，该接口可用来开启与关闭waf全量日志以及配置日志组和日志流。日志组id和日志流id可前往云日志服务获取。配置的日志流id要属于所配置的日志组。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateLtsInfoConfig
        :type request: :class:`huaweicloudsdkwaf.v1.UpdateLtsInfoConfigRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.UpdateLtsInfoConfigResponse`
        """
        http_info = self._update_lts_info_config_http_info(request)
        return self._call_api(**http_info)

    def update_lts_info_config_async_invoker(self, request):
        http_info = self._update_lts_info_config_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_lts_info_config_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/waf/config/lts/{ltsconfig_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateLtsInfoConfigResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ltsconfig_id' in local_var_params:
            path_params['ltsconfig_id'] = local_var_params['ltsconfig_id']

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_policy_async(self, request):
        """更新防护策略

        更新防护策略，请求体可只传需要更新的部分
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdatePolicy
        :type request: :class:`huaweicloudsdkwaf.v1.UpdatePolicyRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.UpdatePolicyResponse`
        """
        http_info = self._update_policy_http_info(request)
        return self._call_api(**http_info)

    def update_policy_async_invoker(self, request):
        http_info = self._update_policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_policy_http_info(self, request):
        http_info = {
            "method": "PATCH",
            "resource_path": "/v1/{project_id}/waf/policy/{policy_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdatePolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_policy_protect_host_async(self, request):
        """更新防护策略的域名

        更新防护策略的防护域名
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdatePolicyProtectHost
        :type request: :class:`huaweicloudsdkwaf.v1.UpdatePolicyProtectHostRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.UpdatePolicyProtectHostResponse`
        """
        http_info = self._update_policy_protect_host_http_info(request)
        return self._call_api(**http_info)

    def update_policy_protect_host_async_invoker(self, request):
        http_info = self._update_policy_protect_host_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_policy_protect_host_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/waf/policy/{policy_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdatePolicyProtectHostResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_policy_rule_status_async(self, request):
        """修改单条规则的状态

        修改单条规则的状态，用于开启或者关闭单条规则，比如关闭精准防护中某一条规则
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdatePolicyRuleStatus
        :type request: :class:`huaweicloudsdkwaf.v1.UpdatePolicyRuleStatusRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.UpdatePolicyRuleStatusResponse`
        """
        http_info = self._update_policy_rule_status_http_info(request)
        return self._call_api(**http_info)

    def update_policy_rule_status_async_invoker(self, request):
        http_info = self._update_policy_rule_status_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_policy_rule_status_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/waf/policy/{policy_id}/{ruletype}/{rule_id}/status",
            "request_type": request.__class__.__name__,
            "response_type": "UpdatePolicyRuleStatusResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_premium_host_async(self, request):
        """修改独享模式域名配置

        修改独享模式域名配置，在没有填入源站信息server的原始数据的情况下，则新的源站信息server会覆盖源站信息，而不是新增源站。此外，请求体可只传需要更新的部分。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdatePremiumHost
        :type request: :class:`huaweicloudsdkwaf.v1.UpdatePremiumHostRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.UpdatePremiumHostResponse`
        """
        http_info = self._update_premium_host_http_info(request)
        return self._call_api(**http_info)

    def update_premium_host_async_invoker(self, request):
        http_info = self._update_premium_host_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_premium_host_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/premium-waf/host/{host_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdatePremiumHostResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'host_id' in local_var_params:
            path_params['host_id'] = local_var_params['host_id']

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_premium_host_protect_status_async(self, request):
        """修改独享模式域名防护状态

        修改独享模式域名防护状态
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdatePremiumHostProtectStatus
        :type request: :class:`huaweicloudsdkwaf.v1.UpdatePremiumHostProtectStatusRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.UpdatePremiumHostProtectStatusResponse`
        """
        http_info = self._update_premium_host_protect_status_http_info(request)
        return self._call_api(**http_info)

    def update_premium_host_protect_status_async_invoker(self, request):
        http_info = self._update_premium_host_protect_status_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_premium_host_protect_status_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/premium-waf/host/{host_id}/protect-status",
            "request_type": request.__class__.__name__,
            "response_type": "UpdatePremiumHostProtectStatusResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'host_id' in local_var_params:
            path_params['host_id'] = local_var_params['host_id']

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_privacy_rule_async(self, request):
        """更新隐私屏蔽防护规则

        更新隐私屏蔽防护规则
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdatePrivacyRule
        :type request: :class:`huaweicloudsdkwaf.v1.UpdatePrivacyRuleRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.UpdatePrivacyRuleResponse`
        """
        http_info = self._update_privacy_rule_http_info(request)
        return self._call_api(**http_info)

    def update_privacy_rule_async_invoker(self, request):
        http_info = self._update_privacy_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_privacy_rule_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/waf/policy/{policy_id}/privacy/{rule_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdatePrivacyRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_punishment_rule_async(self, request):
        """更新攻击惩罚规则

        更新攻击惩罚规则
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdatePunishmentRule
        :type request: :class:`huaweicloudsdkwaf.v1.UpdatePunishmentRuleRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.UpdatePunishmentRuleResponse`
        """
        http_info = self._update_punishment_rule_http_info(request)
        return self._call_api(**http_info)

    def update_punishment_rule_async_invoker(self, request):
        http_info = self._update_punishment_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_punishment_rule_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/waf/policy/{policy_id}/punishment/{rule_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdatePunishmentRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_value_list_async(self, request):
        """修改引用表

        修改引用表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateValueList
        :type request: :class:`huaweicloudsdkwaf.v1.UpdateValueListRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.UpdateValueListResponse`
        """
        http_info = self._update_value_list_http_info(request)
        return self._call_api(**http_info)

    def update_value_list_async_invoker(self, request):
        http_info = self._update_value_list_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_value_list_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/waf/valuelist/{valuelistid}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateValueListResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'valuelistid' in local_var_params:
            path_params['valuelistid'] = local_var_params['valuelistid']

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_whiteblackip_rule_async(self, request):
        """更新黑白名单防护规则

        更新黑白名单防护规则，可以更新ip/ip段以及防护动作等信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateWhiteblackipRule
        :type request: :class:`huaweicloudsdkwaf.v1.UpdateWhiteblackipRuleRequest`
        :rtype: :class:`huaweicloudsdkwaf.v1.UpdateWhiteblackipRuleResponse`
        """
        http_info = self._update_whiteblackip_rule_http_info(request)
        return self._call_api(**http_info)

    def update_whiteblackip_rule_async_invoker(self, request):
        http_info = self._update_whiteblackip_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_whiteblackip_rule_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/waf/policy/{policy_id}/whiteblackip/{rule_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateWhiteblackipRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def _call_api(self, **kwargs):
        try:
            kwargs["async_request"] = True
            return self.do_http_request(**kwargs)
        except TypeError:
            import inspect
            params = inspect.signature(self.do_http_request).parameters
            http_info = {param_name: kwargs.get(param_name) for param_name in params if param_name in kwargs}
            return self.do_http_request(**http_info)

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

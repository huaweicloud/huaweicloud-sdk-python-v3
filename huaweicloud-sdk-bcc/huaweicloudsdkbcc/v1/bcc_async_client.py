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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkbcc'")


class BccAsyncClient(Client):
    def __init__(self):
        super(BccAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkbcc.v1.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "BccAsyncClient":
                raise TypeError("client type error, support client type is BccAsyncClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def bind_resource_level_compliance_async(self, request):
        r"""绑定资源等级合规规则

        资源分级绑定合规规则，会导致属于改等级的资源的合规结果发生变化
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BindResourceLevelCompliance
        :type request: :class:`huaweicloudsdkbcc.v1.BindResourceLevelComplianceRequest`
        :rtype: :class:`huaweicloudsdkbcc.v1.BindResourceLevelComplianceResponse`
        """
        http_info = self._bind_resource_level_compliance_http_info(request)
        return self._call_api(**http_info)

    def bind_resource_level_compliance_async_invoker(self, request):
        http_info = self._bind_resource_level_compliance_http_info(request)
        return AsyncInvoker(self, http_info)

    def _bind_resource_level_compliance_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{domain_id}/resource-levels/{level_id}/compliance",
            "request_type": request.__class__.__name__,
            "response_type": "BindResourceLevelComplianceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']
        if 'level_id' in local_var_params:
            path_params['level_id'] = local_var_params['level_id']

        query_params = []

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

    def change_resources_level_async(self, request):
        r"""指定资源等级

        手动更改资源的等级，可能会导致资源的合规结果发生变化
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ChangeResourcesLevel
        :type request: :class:`huaweicloudsdkbcc.v1.ChangeResourcesLevelRequest`
        :rtype: :class:`huaweicloudsdkbcc.v1.ChangeResourcesLevelResponse`
        """
        http_info = self._change_resources_level_http_info(request)
        return self._call_api(**http_info)

    def change_resources_level_async_invoker(self, request):
        http_info = self._change_resources_level_http_info(request)
        return AsyncInvoker(self, http_info)

    def _change_resources_level_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{domain_id}/resources/resource-level",
            "request_type": request.__class__.__name__,
            "response_type": "ChangeResourcesLevelResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']

        query_params = []

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

    def create_compliance_rule_async(self, request):
        r"""新建自定义合规规则

        新建自定义合规规则
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateComplianceRule
        :type request: :class:`huaweicloudsdkbcc.v1.CreateComplianceRuleRequest`
        :rtype: :class:`huaweicloudsdkbcc.v1.CreateComplianceRuleResponse`
        """
        http_info = self._create_compliance_rule_http_info(request)
        return self._call_api(**http_info)

    def create_compliance_rule_async_invoker(self, request):
        http_info = self._create_compliance_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_compliance_rule_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{domain_id}/backup/compliancerules",
            "request_type": request.__class__.__name__,
            "response_type": "CreateComplianceRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']

        query_params = []

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
        r"""新建策略

        新建策略
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreatePolicy
        :type request: :class:`huaweicloudsdkbcc.v1.CreatePolicyRequest`
        :rtype: :class:`huaweicloudsdkbcc.v1.CreatePolicyResponse`
        """
        http_info = self._create_policy_http_info(request)
        return self._call_api(**http_info)

    def create_policy_async_invoker(self, request):
        http_info = self._create_policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_policy_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{domain_id}/backup/policies",
            "request_type": request.__class__.__name__,
            "response_type": "CreatePolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']

        query_params = []

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

    def create_report_setting_async(self, request):
        r"""创建报告配置

        创建报告配置
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateReportSetting
        :type request: :class:`huaweicloudsdkbcc.v1.CreateReportSettingRequest`
        :rtype: :class:`huaweicloudsdkbcc.v1.CreateReportSettingResponse`
        """
        http_info = self._create_report_setting_http_info(request)
        return self._call_api(**http_info)

    def create_report_setting_async_invoker(self, request):
        http_info = self._create_report_setting_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_report_setting_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{domain_id}/report/settings",
            "request_type": request.__class__.__name__,
            "response_type": "CreateReportSettingResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']

        query_params = []

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

    def create_resources_level_async(self, request):
        r"""新增资源分级

        新增资源分级
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateResourcesLevel
        :type request: :class:`huaweicloudsdkbcc.v1.CreateResourcesLevelRequest`
        :rtype: :class:`huaweicloudsdkbcc.v1.CreateResourcesLevelResponse`
        """
        http_info = self._create_resources_level_http_info(request)
        return self._call_api(**http_info)

    def create_resources_level_async_invoker(self, request):
        http_info = self._create_resources_level_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_resources_level_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{domain_id}/resource-levels",
            "request_type": request.__class__.__name__,
            "response_type": "CreateResourcesLevelResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']

        query_params = []

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

    def create_template_async(self, request):
        r"""创建模板

        创建模板
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateTemplate
        :type request: :class:`huaweicloudsdkbcc.v1.CreateTemplateRequest`
        :rtype: :class:`huaweicloudsdkbcc.v1.CreateTemplateResponse`
        """
        http_info = self._create_template_http_info(request)
        return self._call_api(**http_info)

    def create_template_async_invoker(self, request):
        http_info = self._create_template_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_template_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{domain_id}/templates",
            "request_type": request.__class__.__name__,
            "response_type": "CreateTemplateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']

        query_params = []

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

    def delete_compliance_rule_async(self, request):
        r"""删除自定义合规规则

        删除自定义合规规则
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteComplianceRule
        :type request: :class:`huaweicloudsdkbcc.v1.DeleteComplianceRuleRequest`
        :rtype: :class:`huaweicloudsdkbcc.v1.DeleteComplianceRuleResponse`
        """
        http_info = self._delete_compliance_rule_http_info(request)
        return self._call_api(**http_info)

    def delete_compliance_rule_async_invoker(self, request):
        http_info = self._delete_compliance_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_compliance_rule_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{domain_id}/backup/compliancerules/{compliance_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteComplianceRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']
        if 'compliance_id' in local_var_params:
            path_params['compliance_id'] = local_var_params['compliance_id']

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

    def delete_policy_async(self, request):
        r"""删除指定策略

        删除指定策略
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeletePolicy
        :type request: :class:`huaweicloudsdkbcc.v1.DeletePolicyRequest`
        :rtype: :class:`huaweicloudsdkbcc.v1.DeletePolicyResponse`
        """
        http_info = self._delete_policy_http_info(request)
        return self._call_api(**http_info)

    def delete_policy_async_invoker(self, request):
        http_info = self._delete_policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_policy_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{domain_id}/backup/policies/{policy_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeletePolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']

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

    def delete_report_async(self, request):
        r"""删除指定的报告

        删除指定的报告
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteReport
        :type request: :class:`huaweicloudsdkbcc.v1.DeleteReportRequest`
        :rtype: :class:`huaweicloudsdkbcc.v1.DeleteReportResponse`
        """
        http_info = self._delete_report_http_info(request)
        return self._call_api(**http_info)

    def delete_report_async_invoker(self, request):
        http_info = self._delete_report_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_report_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{domain_id}/reports/{report_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteReportResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']
        if 'report_id' in local_var_params:
            path_params['report_id'] = local_var_params['report_id']

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

    def delete_report_setting_async(self, request):
        r"""删除报告配置

        删除报告配置
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteReportSetting
        :type request: :class:`huaweicloudsdkbcc.v1.DeleteReportSettingRequest`
        :rtype: :class:`huaweicloudsdkbcc.v1.DeleteReportSettingResponse`
        """
        http_info = self._delete_report_setting_http_info(request)
        return self._call_api(**http_info)

    def delete_report_setting_async_invoker(self, request):
        http_info = self._delete_report_setting_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_report_setting_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{domain_id}/report/settings/{setting_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteReportSettingResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']
        if 'setting_id' in local_var_params:
            path_params['setting_id'] = local_var_params['setting_id']

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

    def delete_template_async(self, request):
        r"""删除模板

        删除模板
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteTemplate
        :type request: :class:`huaweicloudsdkbcc.v1.DeleteTemplateRequest`
        :rtype: :class:`huaweicloudsdkbcc.v1.DeleteTemplateResponse`
        """
        http_info = self._delete_template_http_info(request)
        return self._call_api(**http_info)

    def delete_template_async_invoker(self, request):
        http_info = self._delete_template_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_template_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{domain_id}/templates/{template_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteTemplateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']
        if 'template_id' in local_var_params:
            path_params['template_id'] = local_var_params['template_id']

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

    def enable_domain_async(self, request):
        r"""用户授权开启BCC

        用户授权开启BCC
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for EnableDomain
        :type request: :class:`huaweicloudsdkbcc.v1.EnableDomainRequest`
        :rtype: :class:`huaweicloudsdkbcc.v1.EnableDomainResponse`
        """
        http_info = self._enable_domain_http_info(request)
        return self._call_api(**http_info)

    def enable_domain_async_invoker(self, request):
        http_info = self._enable_domain_http_info(request)
        return AsyncInvoker(self, http_info)

    def _enable_domain_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{domain_id}/enable",
            "request_type": request.__class__.__name__,
            "response_type": "EnableDomainResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']

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

    def list_alarm_rules_async(self, request):
        r"""查询告警规则列表

        查询告警规则列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAlarmRules
        :type request: :class:`huaweicloudsdkbcc.v1.ListAlarmRulesRequest`
        :rtype: :class:`huaweicloudsdkbcc.v1.ListAlarmRulesResponse`
        """
        http_info = self._list_alarm_rules_http_info(request)
        return self._call_api(**http_info)

    def list_alarm_rules_async_invoker(self, request):
        http_info = self._list_alarm_rules_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_alarm_rules_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{domain_id}/alarm-rules",
            "request_type": request.__class__.__name__,
            "response_type": "ListAlarmRulesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']

        query_params = []
        if 'namespace' in local_var_params:
            query_params.append(('namespace', local_var_params['namespace']))
        if 'region_id' in local_var_params:
            query_params.append(('region_id', local_var_params['region_id']))
        if 'alarm_rule_id' in local_var_params:
            query_params.append(('alarm_rule_id', local_var_params['alarm_rule_id']))
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

    def list_alarms_async(self, request):
        r"""查询告警列表

        查询告警列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAlarms
        :type request: :class:`huaweicloudsdkbcc.v1.ListAlarmsRequest`
        :rtype: :class:`huaweicloudsdkbcc.v1.ListAlarmsResponse`
        """
        http_info = self._list_alarms_http_info(request)
        return self._call_api(**http_info)

    def list_alarms_async_invoker(self, request):
        http_info = self._list_alarms_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_alarms_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{domain_id}/alarms",
            "request_type": request.__class__.__name__,
            "response_type": "ListAlarmsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']

        query_params = []
        if 'namespace' in local_var_params:
            query_params.append(('namespace', local_var_params['namespace']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'region_id' in local_var_params:
            query_params.append(('region_id', local_var_params['region_id']))
        if 'resource_id' in local_var_params:
            query_params.append(('resource_id', local_var_params['resource_id']))
        if 'alarm_rule_id' in local_var_params:
            query_params.append(('alarm_rule_id', local_var_params['alarm_rule_id']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
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

    def list_compliance_rule_async(self, request):
        r"""列举合规规则

        列举合规规则
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListComplianceRule
        :type request: :class:`huaweicloudsdkbcc.v1.ListComplianceRuleRequest`
        :rtype: :class:`huaweicloudsdkbcc.v1.ListComplianceRuleResponse`
        """
        http_info = self._list_compliance_rule_http_info(request)
        return self._call_api(**http_info)

    def list_compliance_rule_async_invoker(self, request):
        http_info = self._list_compliance_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_compliance_rule_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{domain_id}/backup/compliancerules",
            "request_type": request.__class__.__name__,
            "response_type": "ListComplianceRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']

        query_params = []
        if 'embedded_flag' in local_var_params:
            query_params.append(('embedded_flag', local_var_params['embedded_flag']))

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

    def list_events_async(self, request):
        r"""查询事件数据

        查询事件数据
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListEvents
        :type request: :class:`huaweicloudsdkbcc.v1.ListEventsRequest`
        :rtype: :class:`huaweicloudsdkbcc.v1.ListEventsResponse`
        """
        http_info = self._list_events_http_info(request)
        return self._call_api(**http_info)

    def list_events_async_invoker(self, request):
        http_info = self._list_events_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_events_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{domain_id}/events",
            "request_type": request.__class__.__name__,
            "response_type": "ListEventsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']

        query_params = []
        if 'region_id' in local_var_params:
            query_params.append(('region_id', local_var_params['region_id']))
        if 'event_source' in local_var_params:
            query_params.append(('event_source', local_var_params['event_source']))
        if 'event_level' in local_var_params:
            query_params.append(('event_level', local_var_params['event_level']))
        if 'event_name' in local_var_params:
            query_params.append(('event_name', local_var_params['event_name']))
        if 'resource_id' in local_var_params:
            query_params.append(('resource_id', local_var_params['resource_id']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
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

    def list_metrics_async(self, request):
        r"""查询监控数据

        查询监控数据
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListMetrics
        :type request: :class:`huaweicloudsdkbcc.v1.ListMetricsRequest`
        :rtype: :class:`huaweicloudsdkbcc.v1.ListMetricsResponse`
        """
        http_info = self._list_metrics_http_info(request)
        return self._call_api(**http_info)

    def list_metrics_async_invoker(self, request):
        http_info = self._list_metrics_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_metrics_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{domain_id}/metrics",
            "request_type": request.__class__.__name__,
            "response_type": "ListMetricsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']

        query_params = []
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'region_id' in local_var_params:
            query_params.append(('region_id', local_var_params['region_id']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))

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

    def list_organization_policy_async(self, request):
        r"""列举策略

        列举策略
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListOrganizationPolicy
        :type request: :class:`huaweicloudsdkbcc.v1.ListOrganizationPolicyRequest`
        :rtype: :class:`huaweicloudsdkbcc.v1.ListOrganizationPolicyResponse`
        """
        http_info = self._list_organization_policy_http_info(request)
        return self._call_api(**http_info)

    def list_organization_policy_async_invoker(self, request):
        http_info = self._list_organization_policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_organization_policy_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{domain_id}/backup/organizationpolicies",
            "request_type": request.__class__.__name__,
            "response_type": "ListOrganizationPolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'operation_type' in local_var_params:
            query_params.append(('operation_type', local_var_params['operation_type']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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
        r"""列举策略

        列举策略
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListPolicy
        :type request: :class:`huaweicloudsdkbcc.v1.ListPolicyRequest`
        :rtype: :class:`huaweicloudsdkbcc.v1.ListPolicyResponse`
        """
        http_info = self._list_policy_http_info(request)
        return self._call_api(**http_info)

    def list_policy_async_invoker(self, request):
        http_info = self._list_policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_policy_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{domain_id}/backup/policies",
            "request_type": request.__class__.__name__,
            "response_type": "ListPolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']

        query_params = []
        if 'region_id' in local_var_params:
            query_params.append(('region_id', local_var_params['region_id']))
        if 'operation_type' in local_var_params:
            query_params.append(('operation_type', local_var_params['operation_type']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

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

    def list_report_settings_async(self, request):
        r"""查询报告配置列表

        查询报告配置列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListReportSettings
        :type request: :class:`huaweicloudsdkbcc.v1.ListReportSettingsRequest`
        :rtype: :class:`huaweicloudsdkbcc.v1.ListReportSettingsResponse`
        """
        http_info = self._list_report_settings_http_info(request)
        return self._call_api(**http_info)

    def list_report_settings_async_invoker(self, request):
        http_info = self._list_report_settings_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_report_settings_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{domain_id}/report/settings",
            "request_type": request.__class__.__name__,
            "response_type": "ListReportSettingsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']

        query_params = []
        if 'enabled' in local_var_params:
            query_params.append(('enabled', local_var_params['enabled']))
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

    def list_reports_async(self, request):
        r"""查询报告列表

        查询报告列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListReports
        :type request: :class:`huaweicloudsdkbcc.v1.ListReportsRequest`
        :rtype: :class:`huaweicloudsdkbcc.v1.ListReportsResponse`
        """
        http_info = self._list_reports_http_info(request)
        return self._call_api(**http_info)

    def list_reports_async_invoker(self, request):
        http_info = self._list_reports_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_reports_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{domain_id}/reports",
            "request_type": request.__class__.__name__,
            "response_type": "ListReportsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']

        query_params = []
        if 'report_setting_id' in local_var_params:
            query_params.append(('report_setting_id', local_var_params['report_setting_id']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
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

    def list_resource_copies_async(self, request):
        r"""查询副本列表

        查询副本列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListResourceCopies
        :type request: :class:`huaweicloudsdkbcc.v1.ListResourceCopiesRequest`
        :rtype: :class:`huaweicloudsdkbcc.v1.ListResourceCopiesResponse`
        """
        http_info = self._list_resource_copies_http_info(request)
        return self._call_api(**http_info)

    def list_resource_copies_async_invoker(self, request):
        http_info = self._list_resource_copies_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_resource_copies_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{domain_id}/copies",
            "request_type": request.__class__.__name__,
            "response_type": "ListResourceCopiesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']

        query_params = []
        if 'region_id' in local_var_params:
            query_params.append(('region_id', local_var_params['region_id']))
        if 'copy_type' in local_var_params:
            query_params.append(('copy_type', local_var_params['copy_type']))
        if 'resource_type' in local_var_params:
            query_params.append(('resource_type', local_var_params['resource_type']))
        if 'resource_id' in local_var_params:
            query_params.append(('resource_id', local_var_params['resource_id']))
        if 'copy_id' in local_var_params:
            query_params.append(('copy_id', local_var_params['copy_id']))
        if 'vault_id' in local_var_params:
            query_params.append(('vault_id', local_var_params['vault_id']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))

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

    def list_resources_async(self, request):
        r"""查询资源列表

        查询资源列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListResources
        :type request: :class:`huaweicloudsdkbcc.v1.ListResourcesRequest`
        :rtype: :class:`huaweicloudsdkbcc.v1.ListResourcesResponse`
        """
        http_info = self._list_resources_http_info(request)
        return self._call_api(**http_info)

    def list_resources_async_invoker(self, request):
        http_info = self._list_resources_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_resources_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{domain_id}/resources",
            "request_type": request.__class__.__name__,
            "response_type": "ListResourcesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']

        query_params = []
        if 'region_id' in local_var_params:
            query_params.append(('region_id', local_var_params['region_id']))
        if 'provider' in local_var_params:
            query_params.append(('provider', local_var_params['provider']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'tags' in local_var_params:
            query_params.append(('tags', local_var_params['tags']))
        if 'vault_id' in local_var_params:
            query_params.append(('vault_id', local_var_params['vault_id']))
        if 'vault_name' in local_var_params:
            query_params.append(('vault_name', local_var_params['vault_name']))
        if 'resource_level_id' in local_var_params:
            query_params.append(('resource_level_id', local_var_params['resource_level_id']))
        if 'resource_level_name' in local_var_params:
            query_params.append(('resource_level_name', local_var_params['resource_level_name']))
        if 'compliance_result' in local_var_params:
            query_params.append(('compliance_result', local_var_params['compliance_result']))
        if 'inventory_result' in local_var_params:
            query_params.append(('inventory_result', local_var_params['inventory_result']))
        if 'compliance_rule_type' in local_var_params:
            query_params.append(('compliance_rule_type', local_var_params['compliance_rule_type']))
        if 'compliance_rule_matched' in local_var_params:
            query_params.append(('compliance_rule_matched', local_var_params['compliance_rule_matched']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))

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

    def list_resources_level_async(self, request):
        r"""列举资源分级

        列举资源分级
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListResourcesLevel
        :type request: :class:`huaweicloudsdkbcc.v1.ListResourcesLevelRequest`
        :rtype: :class:`huaweicloudsdkbcc.v1.ListResourcesLevelResponse`
        """
        http_info = self._list_resources_level_http_info(request)
        return self._call_api(**http_info)

    def list_resources_level_async_invoker(self, request):
        http_info = self._list_resources_level_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_resources_level_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{domain_id}/resource-levels",
            "request_type": request.__class__.__name__,
            "response_type": "ListResourcesLevelResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']

        query_params = []
        if 'provider' in local_var_params:
            query_params.append(('provider', local_var_params['provider']))
        if 'compliance_rule_id' in local_var_params:
            query_params.append(('compliance_rule_id', local_var_params['compliance_rule_id']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

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

    def list_resources_level_tags_async(self, request):
        r"""列举资源分级已指定的标签

        列举资源分级已指定的标签
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListResourcesLevelTags
        :type request: :class:`huaweicloudsdkbcc.v1.ListResourcesLevelTagsRequest`
        :rtype: :class:`huaweicloudsdkbcc.v1.ListResourcesLevelTagsResponse`
        """
        http_info = self._list_resources_level_tags_http_info(request)
        return self._call_api(**http_info)

    def list_resources_level_tags_async_invoker(self, request):
        http_info = self._list_resources_level_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_resources_level_tags_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{domain_id}/resource-levels/tags",
            "request_type": request.__class__.__name__,
            "response_type": "ListResourcesLevelTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']

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

    def list_supported_region_async(self, request):
        r"""查询支持的region列表

        BCC支持的region列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListSupportedRegion
        :type request: :class:`huaweicloudsdkbcc.v1.ListSupportedRegionRequest`
        :rtype: :class:`huaweicloudsdkbcc.v1.ListSupportedRegionResponse`
        """
        http_info = self._list_supported_region_http_info(request)
        return self._call_api(**http_info)

    def list_supported_region_async_invoker(self, request):
        http_info = self._list_supported_region_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_supported_region_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/bcc/regions",
            "request_type": request.__class__.__name__,
            "response_type": "ListSupportedRegionResponse"
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

    def list_tasks_async(self, request):
        r"""查询任务列表

        查询任务列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListTasks
        :type request: :class:`huaweicloudsdkbcc.v1.ListTasksRequest`
        :rtype: :class:`huaweicloudsdkbcc.v1.ListTasksResponse`
        """
        http_info = self._list_tasks_http_info(request)
        return self._call_api(**http_info)

    def list_tasks_async_invoker(self, request):
        http_info = self._list_tasks_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_tasks_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{domain_id}/tasks",
            "request_type": request.__class__.__name__,
            "response_type": "ListTasksResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']

        query_params = []
        if 'region_id' in local_var_params:
            query_params.append(('region_id', local_var_params['region_id']))
        if 'task_status' in local_var_params:
            query_params.append(('task_status', local_var_params['task_status']))
        if 'task_type' in local_var_params:
            query_params.append(('task_type', local_var_params['task_type']))
        if 'resource_type' in local_var_params:
            query_params.append(('resource_type', local_var_params['resource_type']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
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

    def list_templates_async(self, request):
        r"""查询模板列表

        查询模板列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListTemplates
        :type request: :class:`huaweicloudsdkbcc.v1.ListTemplatesRequest`
        :rtype: :class:`huaweicloudsdkbcc.v1.ListTemplatesResponse`
        """
        http_info = self._list_templates_http_info(request)
        return self._call_api(**http_info)

    def list_templates_async_invoker(self, request):
        http_info = self._list_templates_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_templates_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{domain_id}/templates",
            "request_type": request.__class__.__name__,
            "response_type": "ListTemplatesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']

        query_params = []
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
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

    def list_vault_async(self, request):
        r"""列举存储库

        列举存储库
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListVault
        :type request: :class:`huaweicloudsdkbcc.v1.ListVaultRequest`
        :rtype: :class:`huaweicloudsdkbcc.v1.ListVaultResponse`
        """
        http_info = self._list_vault_http_info(request)
        return self._call_api(**http_info)

    def list_vault_async_invoker(self, request):
        http_info = self._list_vault_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_vault_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{domain_id}/backup/vaults",
            "request_type": request.__class__.__name__,
            "response_type": "ListVaultResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']

        query_params = []
        if 'region_id' in local_var_params:
            query_params.append(('region_id', local_var_params['region_id']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'compliance_id' in local_var_params:
            query_params.append(('compliance_id', local_var_params['compliance_id']))
        if 'policy_id' in local_var_params:
            query_params.append(('policy_id', local_var_params['policy_id']))
        if 'resource_ids' in local_var_params:
            query_params.append(('resource_ids', local_var_params['resource_ids']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'object_type' in local_var_params:
            query_params.append(('object_type', local_var_params['object_type']))
        if 'protect_type' in local_var_params:
            query_params.append(('protect_type', local_var_params['protect_type']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

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

    def list_vault_tops_async(self, request):
        r"""查询使用最高的存储库

        查询使用最高的存储库，按使用容量或者按使用率排序返回
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListVaultTops
        :type request: :class:`huaweicloudsdkbcc.v1.ListVaultTopsRequest`
        :rtype: :class:`huaweicloudsdkbcc.v1.ListVaultTopsResponse`
        """
        http_info = self._list_vault_tops_http_info(request)
        return self._call_api(**http_info)

    def list_vault_tops_async_invoker(self, request):
        http_info = self._list_vault_tops_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_vault_tops_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{domain_id}/backup/vault-tops",
            "request_type": request.__class__.__name__,
            "response_type": "ListVaultTopsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']

        query_params = []
        if 'region_id' in local_var_params:
            query_params.append(('region_id', local_var_params['region_id']))
        if 'metric_name' in local_var_params:
            query_params.append(('metric_name', local_var_params['metric_name']))
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

    def modify_resource_level_async(self, request):
        r"""修改资源分级

        修改资源分级，修改资源等级的应用类型、应用规则、合规规则id时，可能会导致某些资源的归属等级发生变动，或资源的合规结果发生更改
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ModifyResourceLevel
        :type request: :class:`huaweicloudsdkbcc.v1.ModifyResourceLevelRequest`
        :rtype: :class:`huaweicloudsdkbcc.v1.ModifyResourceLevelResponse`
        """
        http_info = self._modify_resource_level_http_info(request)
        return self._call_api(**http_info)

    def modify_resource_level_async_invoker(self, request):
        http_info = self._modify_resource_level_http_info(request)
        return AsyncInvoker(self, http_info)

    def _modify_resource_level_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{domain_id}/resource-levels/{level_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ModifyResourceLevelResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']
        if 'level_id' in local_var_params:
            path_params['level_id'] = local_var_params['level_id']

        query_params = []

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

    def notify_resource_change_async(self, request):
        r"""资源变化通知

        资源变化通知，当资源的属性变动时，可能会改变资源归属的等级，进而可能导致合规结果的变化
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for NotifyResourceChange
        :type request: :class:`huaweicloudsdkbcc.v1.NotifyResourceChangeRequest`
        :rtype: :class:`huaweicloudsdkbcc.v1.NotifyResourceChangeResponse`
        """
        http_info = self._notify_resource_change_http_info(request)
        return self._call_api(**http_info)

    def notify_resource_change_async_invoker(self, request):
        http_info = self._notify_resource_change_http_info(request)
        return AsyncInvoker(self, http_info)

    def _notify_resource_change_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{domain_id}/resources/notify",
            "request_type": request.__class__.__name__,
            "response_type": "NotifyResourceChangeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']

        query_params = []

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

    def remove_resource_level_async(self, request):
        r"""删除资源分级

        删除资源分级，删除资源等级会导致归属于该等级的资源的合规结果清空
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RemoveResourceLevel
        :type request: :class:`huaweicloudsdkbcc.v1.RemoveResourceLevelRequest`
        :rtype: :class:`huaweicloudsdkbcc.v1.RemoveResourceLevelResponse`
        """
        http_info = self._remove_resource_level_http_info(request)
        return self._call_api(**http_info)

    def remove_resource_level_async_invoker(self, request):
        http_info = self._remove_resource_level_http_info(request)
        return AsyncInvoker(self, http_info)

    def _remove_resource_level_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{domain_id}/resource-levels/{level_id}",
            "request_type": request.__class__.__name__,
            "response_type": "RemoveResourceLevelResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']
        if 'level_id' in local_var_params:
            path_params['level_id'] = local_var_params['level_id']

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

    def set_protection_configuration_async(self, request):
        r"""配置资源保护

        配置资源保护，资源保护情况发生变动后，相关资源的合规结果可能会发生变化
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for SetProtectionConfiguration
        :type request: :class:`huaweicloudsdkbcc.v1.SetProtectionConfigurationRequest`
        :rtype: :class:`huaweicloudsdkbcc.v1.SetProtectionConfigurationResponse`
        """
        http_info = self._set_protection_configuration_http_info(request)
        return self._call_api(**http_info)

    def set_protection_configuration_async_invoker(self, request):
        http_info = self._set_protection_configuration_http_info(request)
        return AsyncInvoker(self, http_info)

    def _set_protection_configuration_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{domain_id}/resources-backup/configurations",
            "request_type": request.__class__.__name__,
            "response_type": "SetProtectionConfigurationResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']

        query_params = []

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

    def show_alarm_summary_async(self, request):
        r"""查询告警统计信息

        查询告警统计信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowAlarmSummary
        :type request: :class:`huaweicloudsdkbcc.v1.ShowAlarmSummaryRequest`
        :rtype: :class:`huaweicloudsdkbcc.v1.ShowAlarmSummaryResponse`
        """
        http_info = self._show_alarm_summary_http_info(request)
        return self._call_api(**http_info)

    def show_alarm_summary_async_invoker(self, request):
        http_info = self._show_alarm_summary_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_alarm_summary_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{domain_id}/alarm-summary",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAlarmSummaryResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']

        query_params = []
        if 'namespace' in local_var_params:
            query_params.append(('namespace', local_var_params['namespace']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'region_id' in local_var_params:
            query_params.append(('region_id', local_var_params['region_id']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))

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

    def show_compliance_rule_async(self, request):
        r"""查看自定义合规规则详情

        查看自定义合规规则详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowComplianceRule
        :type request: :class:`huaweicloudsdkbcc.v1.ShowComplianceRuleRequest`
        :rtype: :class:`huaweicloudsdkbcc.v1.ShowComplianceRuleResponse`
        """
        http_info = self._show_compliance_rule_http_info(request)
        return self._call_api(**http_info)

    def show_compliance_rule_async_invoker(self, request):
        http_info = self._show_compliance_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_compliance_rule_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{domain_id}/backup/compliancerules/{compliance_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowComplianceRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']
        if 'compliance_id' in local_var_params:
            path_params['compliance_id'] = local_var_params['compliance_id']

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

    def show_domain_async(self, request):
        r"""查询BCC开启情况

        查询BCC开启情况
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowDomain
        :type request: :class:`huaweicloudsdkbcc.v1.ShowDomainRequest`
        :rtype: :class:`huaweicloudsdkbcc.v1.ShowDomainResponse`
        """
        http_info = self._show_domain_http_info(request)
        return self._call_api(**http_info)

    def show_domain_async_invoker(self, request):
        http_info = self._show_domain_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_domain_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{domain_id}/status",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDomainResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']

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

    def show_organization_policy_async(self, request):
        r"""查询指定组织策略

        查询指定组织策略
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowOrganizationPolicy
        :type request: :class:`huaweicloudsdkbcc.v1.ShowOrganizationPolicyRequest`
        :rtype: :class:`huaweicloudsdkbcc.v1.ShowOrganizationPolicyResponse`
        """
        http_info = self._show_organization_policy_http_info(request)
        return self._call_api(**http_info)

    def show_organization_policy_async_invoker(self, request):
        http_info = self._show_organization_policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_organization_policy_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{domain_id}/backup/organizationpolicies/{organization_policy_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowOrganizationPolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']
        if 'organization_policy_id' in local_var_params:
            path_params['organization_policy_id'] = local_var_params['organization_policy_id']

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

    def show_policy_async(self, request):
        r"""查询指定策略

        查询指定策略
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowPolicy
        :type request: :class:`huaweicloudsdkbcc.v1.ShowPolicyRequest`
        :rtype: :class:`huaweicloudsdkbcc.v1.ShowPolicyResponse`
        """
        http_info = self._show_policy_http_info(request)
        return self._call_api(**http_info)

    def show_policy_async_invoker(self, request):
        http_info = self._show_policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_policy_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{domain_id}/backup/policies/{policy_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowPolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']

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

    def show_report_async(self, request):
        r"""查询报告详情

        查询报告详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowReport
        :type request: :class:`huaweicloudsdkbcc.v1.ShowReportRequest`
        :rtype: :class:`huaweicloudsdkbcc.v1.ShowReportResponse`
        """
        http_info = self._show_report_http_info(request)
        return self._call_api(**http_info)

    def show_report_async_invoker(self, request):
        http_info = self._show_report_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_report_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{domain_id}/reports/{report_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowReportResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']
        if 'report_id' in local_var_params:
            path_params['report_id'] = local_var_params['report_id']

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

    def show_report_resource_details_data_async(self, request):
        r"""查询报告详情类数据

        查询指定租户下的指定报告的详情类数据
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowReportResourceDetailsData
        :type request: :class:`huaweicloudsdkbcc.v1.ShowReportResourceDetailsDataRequest`
        :rtype: :class:`huaweicloudsdkbcc.v1.ShowReportResourceDetailsDataResponse`
        """
        http_info = self._show_report_resource_details_data_http_info(request)
        return self._call_api(**http_info)

    def show_report_resource_details_data_async_invoker(self, request):
        http_info = self._show_report_resource_details_data_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_report_resource_details_data_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{domain_id}/reports/{report_id}/resource-details-data",
            "request_type": request.__class__.__name__,
            "response_type": "ShowReportResourceDetailsDataResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']
        if 'report_id' in local_var_params:
            path_params['report_id'] = local_var_params['report_id']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))

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

    def show_report_setting_async(self, request):
        r"""查询报告配置

        查询报告配置
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowReportSetting
        :type request: :class:`huaweicloudsdkbcc.v1.ShowReportSettingRequest`
        :rtype: :class:`huaweicloudsdkbcc.v1.ShowReportSettingResponse`
        """
        http_info = self._show_report_setting_http_info(request)
        return self._call_api(**http_info)

    def show_report_setting_async_invoker(self, request):
        http_info = self._show_report_setting_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_report_setting_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{domain_id}/report/settings/{setting_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowReportSettingResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']
        if 'setting_id' in local_var_params:
            path_params['setting_id'] = local_var_params['setting_id']

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

    def show_report_summary_data_async(self, request):
        r"""查询报告摘要类数据

        查询指定租户下的指定报告的摘要类数据
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowReportSummaryData
        :type request: :class:`huaweicloudsdkbcc.v1.ShowReportSummaryDataRequest`
        :rtype: :class:`huaweicloudsdkbcc.v1.ShowReportSummaryDataResponse`
        """
        http_info = self._show_report_summary_data_http_info(request)
        return self._call_api(**http_info)

    def show_report_summary_data_async_invoker(self, request):
        http_info = self._show_report_summary_data_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_report_summary_data_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{domain_id}/reports/{report_id}/summary-data",
            "request_type": request.__class__.__name__,
            "response_type": "ShowReportSummaryDataResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']
        if 'report_id' in local_var_params:
            path_params['report_id'] = local_var_params['report_id']

        query_params = []
        if 'data_item_name' in local_var_params:
            query_params.append(('data_item_name', local_var_params['data_item_name']))

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

    def show_report_task_details_data_async(self, request):
        r"""查询报告详情类数据

        查询指定租户下的指定报告的详情类数据
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowReportTaskDetailsData
        :type request: :class:`huaweicloudsdkbcc.v1.ShowReportTaskDetailsDataRequest`
        :rtype: :class:`huaweicloudsdkbcc.v1.ShowReportTaskDetailsDataResponse`
        """
        http_info = self._show_report_task_details_data_http_info(request)
        return self._call_api(**http_info)

    def show_report_task_details_data_async_invoker(self, request):
        http_info = self._show_report_task_details_data_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_report_task_details_data_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{domain_id}/reports/{report_id}/task-details-data",
            "request_type": request.__class__.__name__,
            "response_type": "ShowReportTaskDetailsDataResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']
        if 'report_id' in local_var_params:
            path_params['report_id'] = local_var_params['report_id']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))

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

    def show_resource_copies_summary_async(self, request):
        r"""查询副本摘要

        get copies summary
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowResourceCopiesSummary
        :type request: :class:`huaweicloudsdkbcc.v1.ShowResourceCopiesSummaryRequest`
        :rtype: :class:`huaweicloudsdkbcc.v1.ShowResourceCopiesSummaryResponse`
        """
        http_info = self._show_resource_copies_summary_http_info(request)
        return self._call_api(**http_info)

    def show_resource_copies_summary_async_invoker(self, request):
        http_info = self._show_resource_copies_summary_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_resource_copies_summary_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{domain_id}/copy-summary",
            "request_type": request.__class__.__name__,
            "response_type": "ShowResourceCopiesSummaryResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']

        query_params = []
        if 'region_id' in local_var_params:
            query_params.append(('region_id', local_var_params['region_id']))
        if 'resource_type' in local_var_params:
            query_params.append(('resource_type', local_var_params['resource_type']))
        if 'copy_type' in local_var_params:
            query_params.append(('copy_type', local_var_params['copy_type']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))

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

    def show_resource_detail_async(self, request):
        r"""查看资源详情

        查看资源详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowResourceDetail
        :type request: :class:`huaweicloudsdkbcc.v1.ShowResourceDetailRequest`
        :rtype: :class:`huaweicloudsdkbcc.v1.ShowResourceDetailResponse`
        """
        http_info = self._show_resource_detail_http_info(request)
        return self._call_api(**http_info)

    def show_resource_detail_async_invoker(self, request):
        http_info = self._show_resource_detail_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_resource_detail_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{domain_id}/resources/{resource_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowResourceDetailResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']
        if 'resource_id' in local_var_params:
            path_params['resource_id'] = local_var_params['resource_id']

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

    def show_resources_summary_async(self, request):
        r"""查询资源统计

        查询资源统计
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowResourcesSummary
        :type request: :class:`huaweicloudsdkbcc.v1.ShowResourcesSummaryRequest`
        :rtype: :class:`huaweicloudsdkbcc.v1.ShowResourcesSummaryResponse`
        """
        http_info = self._show_resources_summary_http_info(request)
        return self._call_api(**http_info)

    def show_resources_summary_async_invoker(self, request):
        http_info = self._show_resources_summary_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_resources_summary_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{domain_id}/resources-summary",
            "request_type": request.__class__.__name__,
            "response_type": "ShowResourcesSummaryResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']

        query_params = []
        if 'region_id' in local_var_params:
            query_params.append(('region_id', local_var_params['region_id']))
        if 'provider' in local_var_params:
            query_params.append(('provider', local_var_params['provider']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))

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

    def show_task_async(self, request):
        r"""查询任务详情

        查询任务详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowTask
        :type request: :class:`huaweicloudsdkbcc.v1.ShowTaskRequest`
        :rtype: :class:`huaweicloudsdkbcc.v1.ShowTaskResponse`
        """
        http_info = self._show_task_http_info(request)
        return self._call_api(**http_info)

    def show_task_async_invoker(self, request):
        http_info = self._show_task_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_task_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{domain_id}/tasks/{task_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowTaskResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

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

    def show_task_status_summary_async(self, request):
        r"""查询任务统计信息

        查询任务统计信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowTaskStatusSummary
        :type request: :class:`huaweicloudsdkbcc.v1.ShowTaskStatusSummaryRequest`
        :rtype: :class:`huaweicloudsdkbcc.v1.ShowTaskStatusSummaryResponse`
        """
        http_info = self._show_task_status_summary_http_info(request)
        return self._call_api(**http_info)

    def show_task_status_summary_async_invoker(self, request):
        http_info = self._show_task_status_summary_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_task_status_summary_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{domain_id}/task-status-summary",
            "request_type": request.__class__.__name__,
            "response_type": "ShowTaskStatusSummaryResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']

        query_params = []
        if 'region_id' in local_var_params:
            query_params.append(('region_id', local_var_params['region_id']))
        if 'task_type' in local_var_params:
            query_params.append(('task_type', local_var_params['task_type']))
        if 'resource_type' in local_var_params:
            query_params.append(('resource_type', local_var_params['resource_type']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))

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

    def show_task_type_summary_async(self, request):
        r"""查询任务统计信息

        查询任务统计信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowTaskTypeSummary
        :type request: :class:`huaweicloudsdkbcc.v1.ShowTaskTypeSummaryRequest`
        :rtype: :class:`huaweicloudsdkbcc.v1.ShowTaskTypeSummaryResponse`
        """
        http_info = self._show_task_type_summary_http_info(request)
        return self._call_api(**http_info)

    def show_task_type_summary_async_invoker(self, request):
        http_info = self._show_task_type_summary_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_task_type_summary_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{domain_id}/task-type-summary",
            "request_type": request.__class__.__name__,
            "response_type": "ShowTaskTypeSummaryResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']

        query_params = []
        if 'region_id' in local_var_params:
            query_params.append(('region_id', local_var_params['region_id']))
        if 'task_status' in local_var_params:
            query_params.append(('task_status', local_var_params['task_status']))
        if 'resource_type' in local_var_params:
            query_params.append(('resource_type', local_var_params['resource_type']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))

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

    def show_template_async(self, request):
        r"""查询模板

        查询模板
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowTemplate
        :type request: :class:`huaweicloudsdkbcc.v1.ShowTemplateRequest`
        :rtype: :class:`huaweicloudsdkbcc.v1.ShowTemplateResponse`
        """
        http_info = self._show_template_http_info(request)
        return self._call_api(**http_info)

    def show_template_async_invoker(self, request):
        http_info = self._show_template_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_template_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{domain_id}/templates/{template_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowTemplateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']
        if 'template_id' in local_var_params:
            path_params['template_id'] = local_var_params['template_id']

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

    def show_vault_async(self, request):
        r"""查看指定存储库

        查看指定存储库
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowVault
        :type request: :class:`huaweicloudsdkbcc.v1.ShowVaultRequest`
        :rtype: :class:`huaweicloudsdkbcc.v1.ShowVaultResponse`
        """
        http_info = self._show_vault_http_info(request)
        return self._call_api(**http_info)

    def show_vault_async_invoker(self, request):
        http_info = self._show_vault_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_vault_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{domain_id}/backup/vaults/{vault_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowVaultResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']
        if 'vault_id' in local_var_params:
            path_params['vault_id'] = local_var_params['vault_id']

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

    def show_vault_summary_async(self, request):
        r"""查看租户的Vault的统计信息

        查看租户Vault的统计信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowVaultSummary
        :type request: :class:`huaweicloudsdkbcc.v1.ShowVaultSummaryRequest`
        :rtype: :class:`huaweicloudsdkbcc.v1.ShowVaultSummaryResponse`
        """
        http_info = self._show_vault_summary_http_info(request)
        return self._call_api(**http_info)

    def show_vault_summary_async_invoker(self, request):
        http_info = self._show_vault_summary_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_vault_summary_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{domain_id}/backup/vaults-summary",
            "request_type": request.__class__.__name__,
            "response_type": "ShowVaultSummaryResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']

        query_params = []
        if 'region_id' in local_var_params:
            query_params.append(('region_id', local_var_params['region_id']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))

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

    def unbind_resource_level_compliance_async(self, request):
        r"""解绑资源等级合规规则

        资源分级绑定合规规则，修改资源等级的合规规则，会导致属于改等级的资源的合规结果发生变化
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UnbindResourceLevelCompliance
        :type request: :class:`huaweicloudsdkbcc.v1.UnbindResourceLevelComplianceRequest`
        :rtype: :class:`huaweicloudsdkbcc.v1.UnbindResourceLevelComplianceResponse`
        """
        http_info = self._unbind_resource_level_compliance_http_info(request)
        return self._call_api(**http_info)

    def unbind_resource_level_compliance_async_invoker(self, request):
        http_info = self._unbind_resource_level_compliance_http_info(request)
        return AsyncInvoker(self, http_info)

    def _unbind_resource_level_compliance_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{domain_id}/resource-levels/{level_id}/compliance",
            "request_type": request.__class__.__name__,
            "response_type": "UnbindResourceLevelComplianceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']
        if 'level_id' in local_var_params:
            path_params['level_id'] = local_var_params['level_id']

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

    def update_compliance_rule_async(self, request):
        r"""更新自定义合规规则

        更新自定义合规规则
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateComplianceRule
        :type request: :class:`huaweicloudsdkbcc.v1.UpdateComplianceRuleRequest`
        :rtype: :class:`huaweicloudsdkbcc.v1.UpdateComplianceRuleResponse`
        """
        http_info = self._update_compliance_rule_http_info(request)
        return self._call_api(**http_info)

    def update_compliance_rule_async_invoker(self, request):
        http_info = self._update_compliance_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_compliance_rule_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{domain_id}/backup/compliancerules/{compliance_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateComplianceRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']
        if 'compliance_id' in local_var_params:
            path_params['compliance_id'] = local_var_params['compliance_id']

        query_params = []

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
        r"""更新指定策略

        更新指定策略
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdatePolicy
        :type request: :class:`huaweicloudsdkbcc.v1.UpdatePolicyRequest`
        :rtype: :class:`huaweicloudsdkbcc.v1.UpdatePolicyResponse`
        """
        http_info = self._update_policy_http_info(request)
        return self._call_api(**http_info)

    def update_policy_async_invoker(self, request):
        http_info = self._update_policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_policy_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{domain_id}/backup/policies/{policy_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdatePolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']

        query_params = []

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

    def update_report_setting_async(self, request):
        r"""修改报告配置

        更新报告配置
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateReportSetting
        :type request: :class:`huaweicloudsdkbcc.v1.UpdateReportSettingRequest`
        :rtype: :class:`huaweicloudsdkbcc.v1.UpdateReportSettingResponse`
        """
        http_info = self._update_report_setting_http_info(request)
        return self._call_api(**http_info)

    def update_report_setting_async_invoker(self, request):
        http_info = self._update_report_setting_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_report_setting_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{domain_id}/report/settings/{setting_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateReportSettingResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']
        if 'setting_id' in local_var_params:
            path_params['setting_id'] = local_var_params['setting_id']

        query_params = []

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

    def update_template_async(self, request):
        r"""修改模板

        修改模板
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateTemplate
        :type request: :class:`huaweicloudsdkbcc.v1.UpdateTemplateRequest`
        :rtype: :class:`huaweicloudsdkbcc.v1.UpdateTemplateResponse`
        """
        http_info = self._update_template_http_info(request)
        return self._call_api(**http_info)

    def update_template_async_invoker(self, request):
        http_info = self._update_template_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_template_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{domain_id}/templates/{template_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateTemplateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']
        if 'template_id' in local_var_params:
            path_params['template_id'] = local_var_params['template_id']

        query_params = []

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

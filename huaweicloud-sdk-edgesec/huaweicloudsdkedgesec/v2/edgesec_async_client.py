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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkedgesec'")


class EdgeSecAsyncClient(Client):
    def __init__(self):
        super(EdgeSecAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkedgesec.v2.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "EdgeSecAsyncClient":
                raise TypeError("client type error, support client type is EdgeSecAsyncClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def apply_http_policy_async(self, request):
        """更新防护策略的域名

        更新防护策略的域名
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ApplyHttpPolicy
        :type request: :class:`huaweicloudsdkedgesec.v2.ApplyHttpPolicyRequest`
        :rtype: :class:`huaweicloudsdkedgesec.v2.ApplyHttpPolicyResponse`
        """
        http_info = self._apply_http_policy_http_info(request)
        return self._call_api(**http_info)

    def apply_http_policy_async_invoker(self, request):
        http_info = self._apply_http_policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _apply_http_policy_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/edgesec/http/policies/{policy_id}/hosts",
            "request_type": request.__class__.__name__,
            "response_type": "ApplyHttpPolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
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

    def create_domains_async(self, request):
        """创建防护域名

        创建防护域名
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateDomains
        :type request: :class:`huaweicloudsdkedgesec.v2.CreateDomainsRequest`
        :rtype: :class:`huaweicloudsdkedgesec.v2.CreateDomainsResponse`
        """
        http_info = self._create_domains_http_info(request)
        return self._call_api(**http_info)

    def create_domains_async_invoker(self, request):
        http_info = self._create_domains_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_domains_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/edgesec/configuration/domains",
            "request_type": request.__class__.__name__,
            "response_type": "CreateDomainsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

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

    def create_http_policy_async(self, request):
        """创建防护策略

        创建防护策略
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateHttpPolicy
        :type request: :class:`huaweicloudsdkedgesec.v2.CreateHttpPolicyRequest`
        :rtype: :class:`huaweicloudsdkedgesec.v2.CreateHttpPolicyResponse`
        """
        http_info = self._create_http_policy_http_info(request)
        return self._call_api(**http_info)

    def create_http_policy_async_invoker(self, request):
        http_info = self._create_http_policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_http_policy_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/edgesec/http/policies",
            "request_type": request.__class__.__name__,
            "response_type": "CreateHttpPolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

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

    def delete_domains_async(self, request):
        """删除防护域名

        删除防护域名
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteDomains
        :type request: :class:`huaweicloudsdkedgesec.v2.DeleteDomainsRequest`
        :rtype: :class:`huaweicloudsdkedgesec.v2.DeleteDomainsResponse`
        """
        http_info = self._delete_domains_http_info(request)
        return self._call_api(**http_info)

    def delete_domains_async_invoker(self, request):
        http_info = self._delete_domains_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_domains_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/edgesec/configuration/domains/{domain_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteDomainsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']

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

    def delete_http_policy_async(self, request):
        """删除防护策略

        删除防护策略
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteHttpPolicy
        :type request: :class:`huaweicloudsdkedgesec.v2.DeleteHttpPolicyRequest`
        :rtype: :class:`huaweicloudsdkedgesec.v2.DeleteHttpPolicyResponse`
        """
        http_info = self._delete_http_policy_http_info(request)
        return self._call_api(**http_info)

    def delete_http_policy_async_invoker(self, request):
        http_info = self._delete_http_policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_http_policy_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/edgesec/http/policies/{policy_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteHttpPolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
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

    def show_domain_detail_async(self, request):
        """查询防护域名详情

        查询防护域名
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowDomainDetail
        :type request: :class:`huaweicloudsdkedgesec.v2.ShowDomainDetailRequest`
        :rtype: :class:`huaweicloudsdkedgesec.v2.ShowDomainDetailResponse`
        """
        http_info = self._show_domain_detail_http_info(request)
        return self._call_api(**http_info)

    def show_domain_detail_async_invoker(self, request):
        http_info = self._show_domain_detail_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_domain_detail_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/edgesec/configuration/domains/{domain_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDomainDetailResponse"
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

    def show_domains_async(self, request):
        """查询防护域名列表

        查询防护域名列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowDomains
        :type request: :class:`huaweicloudsdkedgesec.v2.ShowDomainsRequest`
        :rtype: :class:`huaweicloudsdkedgesec.v2.ShowDomainsResponse`
        """
        http_info = self._show_domains_http_info(request)
        return self._call_api(**http_info)

    def show_domains_async_invoker(self, request):
        http_info = self._show_domains_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_domains_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/edgesec/configuration/domains",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDomainsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'domain_name' in local_var_params:
            query_params.append(('domain_name', local_var_params['domain_name']))
        if 'policy_name' in local_var_params:
            query_params.append(('policy_name', local_var_params['policy_name']))
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

    def show_http_policies_async(self, request):
        """查询防护策略列表

        查询防护策略列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowHttpPolicies
        :type request: :class:`huaweicloudsdkedgesec.v2.ShowHttpPoliciesRequest`
        :rtype: :class:`huaweicloudsdkedgesec.v2.ShowHttpPoliciesResponse`
        """
        http_info = self._show_http_policies_http_info(request)
        return self._call_api(**http_info)

    def show_http_policies_async_invoker(self, request):
        http_info = self._show_http_policies_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_http_policies_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/edgesec/http/policies",
            "request_type": request.__class__.__name__,
            "response_type": "ShowHttpPoliciesResponse"
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
        if 'hostname' in local_var_params:
            query_params.append(('hostname', local_var_params['hostname']))

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

    def show_http_policy_async(self, request):
        """查询防护策略

        查询防护策略
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowHttpPolicy
        :type request: :class:`huaweicloudsdkedgesec.v2.ShowHttpPolicyRequest`
        :rtype: :class:`huaweicloudsdkedgesec.v2.ShowHttpPolicyResponse`
        """
        http_info = self._show_http_policy_http_info(request)
        return self._call_api(**http_info)

    def show_http_policy_async_invoker(self, request):
        http_info = self._show_http_policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_http_policy_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/edgesec/http/policies/{policy_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowHttpPolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
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

    def update_domains_async(self, request):
        """更新防护域名

        更新防护域名
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateDomains
        :type request: :class:`huaweicloudsdkedgesec.v2.UpdateDomainsRequest`
        :rtype: :class:`huaweicloudsdkedgesec.v2.UpdateDomainsResponse`
        """
        http_info = self._update_domains_http_info(request)
        return self._call_api(**http_info)

    def update_domains_async_invoker(self, request):
        http_info = self._update_domains_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_domains_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/edgesec/configuration/domains/{domain_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateDomainsResponse"
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

    def update_http_policy_async(self, request):
        """更新防护策略

        更新防护策略
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateHttpPolicy
        :type request: :class:`huaweicloudsdkedgesec.v2.UpdateHttpPolicyRequest`
        :rtype: :class:`huaweicloudsdkedgesec.v2.UpdateHttpPolicyResponse`
        """
        http_info = self._update_http_policy_http_info(request)
        return self._call_api(**http_info)

    def update_http_policy_async_invoker(self, request):
        http_info = self._update_http_policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_http_policy_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/edgesec/http/policies/{policy_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateHttpPolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
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

    def update_http_policy_rule_status_async(self, request):
        """更新防护策略规则开关

        更新防护策略规则开关
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateHttpPolicyRuleStatus
        :type request: :class:`huaweicloudsdkedgesec.v2.UpdateHttpPolicyRuleStatusRequest`
        :rtype: :class:`huaweicloudsdkedgesec.v2.UpdateHttpPolicyRuleStatusResponse`
        """
        http_info = self._update_http_policy_rule_status_http_info(request)
        return self._call_api(**http_info)

    def update_http_policy_rule_status_async_invoker(self, request):
        http_info = self._update_http_policy_rule_status_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_http_policy_rule_status_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/edgesec/http/policies/{policy_id}/{rule_type}/{rule_id}/status",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateHttpPolicyRuleStatusResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']
        if 'rule_type' in local_var_params:
            path_params['rule_type'] = local_var_params['rule_type']
        if 'rule_id' in local_var_params:
            path_params['rule_id'] = local_var_params['rule_id']

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

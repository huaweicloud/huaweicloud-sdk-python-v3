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
        self.model_package = importlib.import_module("huaweicloudsdkedgesec.v1.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "EdgeSecAsyncClient":
                raise TypeError("client type error, support client type is EdgeSecAsyncClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def list_edge_sec_subscription_async(self, request):
        """查询边缘安全已购产品

        租户查询边缘安全已购产品
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListEdgeSecSubscription
        :type request: :class:`huaweicloudsdkedgesec.v1.ListEdgeSecSubscriptionRequest`
        :rtype: :class:`huaweicloudsdkedgesec.v1.ListEdgeSecSubscriptionResponse`
        """
        http_info = self._list_edge_sec_subscription_http_info(request)
        return self._call_api(**http_info)

    def list_edge_sec_subscription_async_invoker(self, request):
        http_info = self._list_edge_sec_subscription_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_edge_sec_subscription_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/edgesec/subscription",
            "request_type": request.__class__.__name__,
            "response_type": "ListEdgeSecSubscriptionResponse"
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

    def create_edge_d_do_s_domains_async(self, request):
        """添加ddos防护域名

        租户添加ddos防护域名
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateEdgeDDoSDomains
        :type request: :class:`huaweicloudsdkedgesec.v1.CreateEdgeDDoSDomainsRequest`
        :rtype: :class:`huaweicloudsdkedgesec.v1.CreateEdgeDDoSDomainsResponse`
        """
        http_info = self._create_edge_d_do_s_domains_http_info(request)
        return self._call_api(**http_info)

    def create_edge_d_do_s_domains_async_invoker(self, request):
        http_info = self._create_edge_d_do_s_domains_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_edge_d_do_s_domains_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/edgeddos/domains",
            "request_type": request.__class__.__name__,
            "response_type": "CreateEdgeDDoSDomainsResponse"
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

    def delete_edge_d_do_s_domains_async(self, request):
        """删除ddos防护域名

        租户删除ddos防护域名
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteEdgeDDoSDomains
        :type request: :class:`huaweicloudsdkedgesec.v1.DeleteEdgeDDoSDomainsRequest`
        :rtype: :class:`huaweicloudsdkedgesec.v1.DeleteEdgeDDoSDomainsResponse`
        """
        http_info = self._delete_edge_d_do_s_domains_http_info(request)
        return self._call_api(**http_info)

    def delete_edge_d_do_s_domains_async_invoker(self, request):
        http_info = self._delete_edge_d_do_s_domains_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_edge_d_do_s_domains_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/edgeddos/domains/{domainid}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteEdgeDDoSDomainsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domainid' in local_var_params:
            path_params['domainid'] = local_var_params['domainid']

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

    def list_edge_d_do_s_domains_async(self, request):
        """查询ddos防护域名

        查询租户ddos防护域名
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListEdgeDDoSDomains
        :type request: :class:`huaweicloudsdkedgesec.v1.ListEdgeDDoSDomainsRequest`
        :rtype: :class:`huaweicloudsdkedgesec.v1.ListEdgeDDoSDomainsResponse`
        """
        http_info = self._list_edge_d_do_s_domains_http_info(request)
        return self._call_api(**http_info)

    def list_edge_d_do_s_domains_async_invoker(self, request):
        http_info = self._list_edge_d_do_s_domains_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_edge_d_do_s_domains_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/edgeddos/domains",
            "request_type": request.__class__.__name__,
            "response_type": "ListEdgeDDoSDomainsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'domain_name' in local_var_params:
            query_params.append(('domain_name', local_var_params['domain_name']))
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

    def show_statistics_event_async(self, request):
        """查询租户受攻击事件数据

        查询租户受攻击事件数据
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowStatisticsEvent
        :type request: :class:`huaweicloudsdkedgesec.v1.ShowStatisticsEventRequest`
        :rtype: :class:`huaweicloudsdkedgesec.v1.ShowStatisticsEventResponse`
        """
        http_info = self._show_statistics_event_http_info(request)
        return self._call_api(**http_info)

    def show_statistics_event_async_invoker(self, request):
        http_info = self._show_statistics_event_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_statistics_event_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/statistics/event",
            "request_type": request.__class__.__name__,
            "response_type": "ShowStatisticsEventResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
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

    def show_statistics_traffic_async(self, request):
        """查询租户流量数据

        查询租户流量数据
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowStatisticsTraffic
        :type request: :class:`huaweicloudsdkedgesec.v1.ShowStatisticsTrafficRequest`
        :rtype: :class:`huaweicloudsdkedgesec.v1.ShowStatisticsTrafficResponse`
        """
        http_info = self._show_statistics_traffic_http_info(request)
        return self._call_api(**http_info)

    def show_statistics_traffic_async_invoker(self, request):
        http_info = self._show_statistics_traffic_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_statistics_traffic_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/statistics/traffic",
            "request_type": request.__class__.__name__,
            "response_type": "ShowStatisticsTrafficResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
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

    def update_edge_d_do_s_domains_async(self, request):
        """更新ddos防护域名

        租户更新ddos防护域名
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateEdgeDDoSDomains
        :type request: :class:`huaweicloudsdkedgesec.v1.UpdateEdgeDDoSDomainsRequest`
        :rtype: :class:`huaweicloudsdkedgesec.v1.UpdateEdgeDDoSDomainsResponse`
        """
        http_info = self._update_edge_d_do_s_domains_http_info(request)
        return self._call_api(**http_info)

    def update_edge_d_do_s_domains_async_invoker(self, request):
        http_info = self._update_edge_d_do_s_domains_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_edge_d_do_s_domains_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/edgeddos/domains/{domainid}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateEdgeDDoSDomainsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domainid' in local_var_params:
            path_params['domainid'] = local_var_params['domainid']

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

    def apply_waf_policy_async(self, request):
        """更新防护策略的域名

        更新防护策略的域名
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ApplyWafPolicy
        :type request: :class:`huaweicloudsdkedgesec.v1.ApplyWafPolicyRequest`
        :rtype: :class:`huaweicloudsdkedgesec.v1.ApplyWafPolicyResponse`
        """
        http_info = self._apply_waf_policy_http_info(request)
        return self._call_api(**http_info)

    def apply_waf_policy_async_invoker(self, request):
        http_info = self._apply_waf_policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _apply_waf_policy_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/edgewaf/policies/{policy_id}/hosts",
            "request_type": request.__class__.__name__,
            "response_type": "ApplyWafPolicyResponse"
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

    def create_certificate_async(self, request):
        """创建证书

        创建证书
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateCertificate
        :type request: :class:`huaweicloudsdkedgesec.v1.CreateCertificateRequest`
        :rtype: :class:`huaweicloudsdkedgesec.v1.CreateCertificateResponse`
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
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']

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
            ['application/json;charset=UTF-8'])

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

    def create_edge_waf_domains_async(self, request):
        """创建防护域名

        创建防护域名
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateEdgeWafDomains
        :type request: :class:`huaweicloudsdkedgesec.v1.CreateEdgeWafDomainsRequest`
        :rtype: :class:`huaweicloudsdkedgesec.v1.CreateEdgeWafDomainsResponse`
        """
        http_info = self._create_edge_waf_domains_http_info(request)
        return self._call_api(**http_info)

    def create_edge_waf_domains_async_invoker(self, request):
        http_info = self._create_edge_waf_domains_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_edge_waf_domains_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/edgewaf/domains",
            "request_type": request.__class__.__name__,
            "response_type": "CreateEdgeWafDomainsResponse"
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

    def create_policy_async(self, request):
        """创建防护策略

        创建防护策略，系统会在生成策略时配置一些默认的配置项，如果需要修改策略的默认配置项需要通过调用更新防护策略接口实现
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreatePolicy
        :type request: :class:`huaweicloudsdkedgesec.v1.CreatePolicyRequest`
        :rtype: :class:`huaweicloudsdkedgesec.v1.CreatePolicyResponse`
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
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']

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
            ['application/json;charset=UTF-8'])

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
        :type request: :class:`huaweicloudsdkedgesec.v1.DeleteCertificateRequest`
        :rtype: :class:`huaweicloudsdkedgesec.v1.DeleteCertificateResponse`
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
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
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

    def delete_edge_waf_domains_async(self, request):
        """删除防护域名

        删除防护域名
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteEdgeWafDomains
        :type request: :class:`huaweicloudsdkedgesec.v1.DeleteEdgeWafDomainsRequest`
        :rtype: :class:`huaweicloudsdkedgesec.v1.DeleteEdgeWafDomainsResponse`
        """
        http_info = self._delete_edge_waf_domains_http_info(request)
        return self._call_api(**http_info)

    def delete_edge_waf_domains_async_invoker(self, request):
        http_info = self._delete_edge_waf_domains_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_edge_waf_domains_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/edgewaf/domains/{domainid}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteEdgeWafDomainsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domainid' in local_var_params:
            path_params['domainid'] = local_var_params['domainid']

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
        :type request: :class:`huaweicloudsdkedgesec.v1.DeletePolicyRequest`
        :rtype: :class:`huaweicloudsdkedgesec.v1.DeletePolicyResponse`
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
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
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

    def list_cdn_domains_async(self, request):
        """查询CDN域名列表

        查询CDN域名列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListCdnDomains
        :type request: :class:`huaweicloudsdkedgesec.v1.ListCdnDomainsRequest`
        :rtype: :class:`huaweicloudsdkedgesec.v1.ListCdnDomainsResponse`
        """
        http_info = self._list_cdn_domains_http_info(request)
        return self._call_api(**http_info)

    def list_cdn_domains_async_invoker(self, request):
        http_info = self._list_cdn_domains_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_cdn_domains_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/edgesec/cdn/domains",
            "request_type": request.__class__.__name__,
            "response_type": "ListCdnDomainsResponse"
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

    def list_certificates_async(self, request):
        """查询证书列表

        查询证书列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListCertificates
        :type request: :class:`huaweicloudsdkedgesec.v1.ListCertificatesRequest`
        :rtype: :class:`huaweicloudsdkedgesec.v1.ListCertificatesResponse`
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
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']

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

    def list_edge_waf_domains_async(self, request):
        """查询WAF防护域名列表

        查询WAF防护域名列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListEdgeWafDomains
        :type request: :class:`huaweicloudsdkedgesec.v1.ListEdgeWafDomainsRequest`
        :rtype: :class:`huaweicloudsdkedgesec.v1.ListEdgeWafDomainsResponse`
        """
        http_info = self._list_edge_waf_domains_http_info(request)
        return self._call_api(**http_info)

    def list_edge_waf_domains_async_invoker(self, request):
        http_info = self._list_edge_waf_domains_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_edge_waf_domains_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/edgewaf/domains",
            "request_type": request.__class__.__name__,
            "response_type": "ListEdgeWafDomainsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'page_num' in local_var_params:
            query_params.append(('page_num', local_var_params['page_num']))
        if 'page_size' in local_var_params:
            query_params.append(('page_size', local_var_params['page_size']))
        if 'domain_name' in local_var_params:
            query_params.append(('domain_name', local_var_params['domain_name']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
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

    def list_policy_async(self, request):
        """查询防护策略列表

        查询防护策略列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListPolicy
        :type request: :class:`huaweicloudsdkedgesec.v1.ListPolicyRequest`
        :rtype: :class:`huaweicloudsdkedgesec.v1.ListPolicyResponse`
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
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']

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

    def show_certificate_async(self, request):
        """查询证书

        查询证书
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowCertificate
        :type request: :class:`huaweicloudsdkedgesec.v1.ShowCertificateRequest`
        :rtype: :class:`huaweicloudsdkedgesec.v1.ShowCertificateResponse`
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
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
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

    def show_edge_waf_domains_async(self, request):
        """查询防护域名

        查询防护域名
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowEdgeWafDomains
        :type request: :class:`huaweicloudsdkedgesec.v1.ShowEdgeWafDomainsRequest`
        :rtype: :class:`huaweicloudsdkedgesec.v1.ShowEdgeWafDomainsResponse`
        """
        http_info = self._show_edge_waf_domains_http_info(request)
        return self._call_api(**http_info)

    def show_edge_waf_domains_async_invoker(self, request):
        http_info = self._show_edge_waf_domains_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_edge_waf_domains_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/edgewaf/domains/{domainid}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowEdgeWafDomainsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domainid' in local_var_params:
            path_params['domainid'] = local_var_params['domainid']

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

    def update_certificate_async(self, request):
        """修改证书

        修改证书
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateCertificate
        :type request: :class:`huaweicloudsdkedgesec.v1.UpdateCertificateRequest`
        :rtype: :class:`huaweicloudsdkedgesec.v1.UpdateCertificateResponse`
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
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
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
            ['application/json;charset=UTF-8'])

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

    def update_edge_waf_domains_async(self, request):
        """更新防护域名

        更新防护域名
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateEdgeWafDomains
        :type request: :class:`huaweicloudsdkedgesec.v1.UpdateEdgeWafDomainsRequest`
        :rtype: :class:`huaweicloudsdkedgesec.v1.UpdateEdgeWafDomainsResponse`
        """
        http_info = self._update_edge_waf_domains_http_info(request)
        return self._call_api(**http_info)

    def update_edge_waf_domains_async_invoker(self, request):
        http_info = self._update_edge_waf_domains_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_edge_waf_domains_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/edgewaf/domains/{domainid}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateEdgeWafDomainsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domainid' in local_var_params:
            path_params['domainid'] = local_var_params['domainid']

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

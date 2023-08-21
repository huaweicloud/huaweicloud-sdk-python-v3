# coding: utf-8

from __future__ import absolute_import

import importlib

from huaweicloudsdkcore.client import Client, ClientBuilder
from huaweicloudsdkcore.utils import http_utils
from huaweicloudsdkcore.sdk_stream_request import SdkStreamRequest


class EdgeSecAsyncClient(Client):
    def __init__(self):
        super(EdgeSecAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkedgesec.v1.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if clazz is None:
            return ClientBuilder(cls)

        if clazz.__name__ != "EdgeSecClient":
            raise TypeError("client type error, support client type is EdgeSecClient")

        return ClientBuilder(clazz)

    def list_edge_sec_subscription_async(self, request):
        """查询边缘安全已购产品

        租户查询边缘安全已购产品
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListEdgeSecSubscription
        :type request: :class:`huaweicloudsdkedgesec.v1.ListEdgeSecSubscriptionRequest`
        :rtype: :class:`huaweicloudsdkedgesec.v1.ListEdgeSecSubscriptionResponse`
        """
        return self._list_edge_sec_subscription_with_http_info(request)

    def _list_edge_sec_subscription_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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
            resource_path='/v1/edgesec/subscription',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListEdgeSecSubscriptionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_edge_d_do_s_domains_async(self, request):
        """添加ddos防护域名

        租户添加ddos防护域名
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateEdgeDDoSDomains
        :type request: :class:`huaweicloudsdkedgesec.v1.CreateEdgeDDoSDomainsRequest`
        :rtype: :class:`huaweicloudsdkedgesec.v1.CreateEdgeDDoSDomainsResponse`
        """
        return self._create_edge_d_do_s_domains_with_http_info(request)

    def _create_edge_d_do_s_domains_with_http_info(self, request):
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
            resource_path='/v1/edgeddos/domains',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateEdgeDDoSDomainsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_edge_d_do_s_domains_async(self, request):
        """删除ddos防护域名

        租户删除ddos防护域名
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteEdgeDDoSDomains
        :type request: :class:`huaweicloudsdkedgesec.v1.DeleteEdgeDDoSDomainsRequest`
        :rtype: :class:`huaweicloudsdkedgesec.v1.DeleteEdgeDDoSDomainsResponse`
        """
        return self._delete_edge_d_do_s_domains_with_http_info(request)

    def _delete_edge_d_do_s_domains_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/edgeddos/domains/{domainid}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteEdgeDDoSDomainsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_edge_d_do_s_domains_async(self, request):
        """查询ddos防护域名

        查询租户ddos防护域名
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListEdgeDDoSDomains
        :type request: :class:`huaweicloudsdkedgesec.v1.ListEdgeDDoSDomainsRequest`
        :rtype: :class:`huaweicloudsdkedgesec.v1.ListEdgeDDoSDomainsResponse`
        """
        return self._list_edge_d_do_s_domains_with_http_info(request)

    def _list_edge_d_do_s_domains_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/edgeddos/domains',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListEdgeDDoSDomainsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_statistics_event_async(self, request):
        """查询租户受攻击事件数据

        查询租户受攻击事件数据
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowStatisticsEvent
        :type request: :class:`huaweicloudsdkedgesec.v1.ShowStatisticsEventRequest`
        :rtype: :class:`huaweicloudsdkedgesec.v1.ShowStatisticsEventResponse`
        """
        return self._show_statistics_event_with_http_info(request)

    def _show_statistics_event_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/statistics/event',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowStatisticsEventResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_statistics_traffic_async(self, request):
        """查询租户流量数据

        查询租户流量数据
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowStatisticsTraffic
        :type request: :class:`huaweicloudsdkedgesec.v1.ShowStatisticsTrafficRequest`
        :rtype: :class:`huaweicloudsdkedgesec.v1.ShowStatisticsTrafficResponse`
        """
        return self._show_statistics_traffic_with_http_info(request)

    def _show_statistics_traffic_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/statistics/traffic',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowStatisticsTrafficResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_edge_d_do_s_domains_async(self, request):
        """更新ddos防护域名

        租户更新ddos防护域名
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateEdgeDDoSDomains
        :type request: :class:`huaweicloudsdkedgesec.v1.UpdateEdgeDDoSDomainsRequest`
        :rtype: :class:`huaweicloudsdkedgesec.v1.UpdateEdgeDDoSDomainsResponse`
        """
        return self._update_edge_d_do_s_domains_with_http_info(request)

    def _update_edge_d_do_s_domains_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domainid' in local_var_params:
            path_params['domainid'] = local_var_params['domainid']

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
            resource_path='/v1/edgeddos/domains/{domainid}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateEdgeDDoSDomainsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def apply_waf_policy_async(self, request):
        """更新防护策略的域名

        更新防护策略的域名
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ApplyWafPolicy
        :type request: :class:`huaweicloudsdkedgesec.v1.ApplyWafPolicyRequest`
        :rtype: :class:`huaweicloudsdkedgesec.v1.ApplyWafPolicyResponse`
        """
        return self._apply_waf_policy_with_http_info(request)

    def _apply_waf_policy_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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
            resource_path='/v1/edgewaf/policies/{policy_id}/hosts',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ApplyWafPolicyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_edge_waf_domains_async(self, request):
        """创建防护域名

        创建防护域名
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateEdgeWafDomains
        :type request: :class:`huaweicloudsdkedgesec.v1.CreateEdgeWafDomainsRequest`
        :rtype: :class:`huaweicloudsdkedgesec.v1.CreateEdgeWafDomainsResponse`
        """
        return self._create_edge_waf_domains_with_http_info(request)

    def _create_edge_waf_domains_with_http_info(self, request):
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
            resource_path='/v1/edgewaf/domains',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateEdgeWafDomainsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_policy_async(self, request):
        """创建防护策略

        创建防护策略，系统会在生成策略时配置一些默认的配置项，如果需要修改策略的默认配置项需要通过调用更新防护策略接口实现
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreatePolicy
        :type request: :class:`huaweicloudsdkedgesec.v1.CreatePolicyRequest`
        :rtype: :class:`huaweicloudsdkedgesec.v1.CreatePolicyResponse`
        """
        return self._create_policy_with_http_info(request)

    def _create_policy_with_http_info(self, request):
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
            resource_path='/v1/{project_id}/waf/policy',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreatePolicyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_edge_waf_domains_async(self, request):
        """删除防护域名

        删除防护域名
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteEdgeWafDomains
        :type request: :class:`huaweicloudsdkedgesec.v1.DeleteEdgeWafDomainsRequest`
        :rtype: :class:`huaweicloudsdkedgesec.v1.DeleteEdgeWafDomainsResponse`
        """
        return self._delete_edge_waf_domains_with_http_info(request)

    def _delete_edge_waf_domains_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/edgewaf/domains/{domainid}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteEdgeWafDomainsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_policy_async(self, request):
        """删除防护策略

        删除防护策略，若策略正在使用，则需要先接解除域名与策略的绑定关系才能删除策略。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeletePolicy
        :type request: :class:`huaweicloudsdkedgesec.v1.DeletePolicyRequest`
        :rtype: :class:`huaweicloudsdkedgesec.v1.DeletePolicyResponse`
        """
        return self._delete_policy_with_http_info(request)

    def _delete_policy_with_http_info(self, request):
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
            cname=cname,
            response_type='DeletePolicyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_cdn_domains_async(self, request):
        """查询CDN域名列表

        查询CDN域名列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListCdnDomains
        :type request: :class:`huaweicloudsdkedgesec.v1.ListCdnDomainsRequest`
        :rtype: :class:`huaweicloudsdkedgesec.v1.ListCdnDomainsResponse`
        """
        return self._list_cdn_domains_with_http_info(request)

    def _list_cdn_domains_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/edgesec/cdn/domains',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListCdnDomainsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_edge_waf_domains_async(self, request):
        """查询WAF防护域名列表

        查询WAF防护域名列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListEdgeWafDomains
        :type request: :class:`huaweicloudsdkedgesec.v1.ListEdgeWafDomainsRequest`
        :rtype: :class:`huaweicloudsdkedgesec.v1.ListEdgeWafDomainsResponse`
        """
        return self._list_edge_waf_domains_with_http_info(request)

    def _list_edge_waf_domains_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/edgewaf/domains',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListEdgeWafDomainsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_policy_async(self, request):
        """查询防护策略列表

        查询防护策略列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListPolicy
        :type request: :class:`huaweicloudsdkedgesec.v1.ListPolicyRequest`
        :rtype: :class:`huaweicloudsdkedgesec.v1.ListPolicyResponse`
        """
        return self._list_policy_with_http_info(request)

    def _list_policy_with_http_info(self, request):
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
            cname=cname,
            response_type='ListPolicyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_edge_waf_domains_async(self, request):
        """查询防护域名

        查询防护域名
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowEdgeWafDomains
        :type request: :class:`huaweicloudsdkedgesec.v1.ShowEdgeWafDomainsRequest`
        :rtype: :class:`huaweicloudsdkedgesec.v1.ShowEdgeWafDomainsResponse`
        """
        return self._show_edge_waf_domains_with_http_info(request)

    def _show_edge_waf_domains_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/edgewaf/domains/{domainid}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowEdgeWafDomainsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_edge_waf_domains_async(self, request):
        """更新防护域名

        更新防护域名
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateEdgeWafDomains
        :type request: :class:`huaweicloudsdkedgesec.v1.UpdateEdgeWafDomainsRequest`
        :rtype: :class:`huaweicloudsdkedgesec.v1.UpdateEdgeWafDomainsResponse`
        """
        return self._update_edge_waf_domains_with_http_info(request)

    def _update_edge_waf_domains_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domainid' in local_var_params:
            path_params['domainid'] = local_var_params['domainid']

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
            resource_path='/v1/edgewaf/domains/{domainid}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateEdgeWafDomainsResponse',
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

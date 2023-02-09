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


class CdnClient(Client):
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
        super(CdnClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkcdn.v1.model")
        self.preset_headers = {'User-Agent': 'HuaweiCloud-SDK-Python'}

    @classmethod
    def new_builder(cls, clazz=None):
        if clazz is None:
            return ClientBuilder(cls, "GlobalCredentials")

        if clazz.__name__ != "CdnClient":
            raise TypeError("client type error, support client type is CdnClient")

        return ClientBuilder(clazz, "GlobalCredentials")

    def batch_delete_tags(self, request):
        """删除资源标签配置接口

        用于删除资源标签
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchDeleteTags
        :type request: :class:`huaweicloudsdkcdn.v1.BatchDeleteTagsRequest`
        :rtype: :class:`huaweicloudsdkcdn.v1.BatchDeleteTagsResponse`
        """
        return self.batch_delete_tags_with_http_info(request)

    def batch_delete_tags_with_http_info(self, request):
        all_params = ['batch_delete_tags_request_body']
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
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1.0/cdn/configuration/tags/batch-delete',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchDeleteTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_domain(self, request):
        """创建加速域名

        创建加速域名。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateDomain
        :type request: :class:`huaweicloudsdkcdn.v1.CreateDomainRequest`
        :rtype: :class:`huaweicloudsdkcdn.v1.CreateDomainResponse`
        """
        return self.create_domain_with_http_info(request)

    def create_domain_with_http_info(self, request):
        all_params = ['domain']
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
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1.0/cdn/domains',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateDomainResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_preheating_tasks(self, request):
        """创建预热缓存任务

        创建预热任务。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreatePreheatingTasks
        :type request: :class:`huaweicloudsdkcdn.v1.CreatePreheatingTasksRequest`
        :rtype: :class:`huaweicloudsdkcdn.v1.CreatePreheatingTasksResponse`
        """
        return self.create_preheating_tasks_with_http_info(request)

    def create_preheating_tasks_with_http_info(self, request):
        all_params = ['preheating_task', 'enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            resource_path='/v1.0/cdn/content/preheating-tasks',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreatePreheatingTasksResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_refresh_tasks(self, request):
        """创建刷新缓存任务

        创建刷新缓存任务。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateRefreshTasks
        :type request: :class:`huaweicloudsdkcdn.v1.CreateRefreshTasksRequest`
        :rtype: :class:`huaweicloudsdkcdn.v1.CreateRefreshTasksResponse`
        """
        return self.create_refresh_tasks_with_http_info(request)

    def create_refresh_tasks_with_http_info(self, request):
        all_params = ['refresh_task', 'enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            resource_path='/v1.0/cdn/content/refresh-tasks',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateRefreshTasksResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_tags(self, request):
        """创建资源标签配置接口

        用于创建资源标签
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateTags
        :type request: :class:`huaweicloudsdkcdn.v1.CreateTagsRequest`
        :rtype: :class:`huaweicloudsdkcdn.v1.CreateTagsResponse`
        """
        return self.create_tags_with_http_info(request)

    def create_tags_with_http_info(self, request):
        all_params = ['create_tags_request_body']
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
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1.0/cdn/configuration/tags',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_domain(self, request):
        """删除加速域名

        删除加速域名。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteDomain
        :type request: :class:`huaweicloudsdkcdn.v1.DeleteDomainRequest`
        :rtype: :class:`huaweicloudsdkcdn.v1.DeleteDomainResponse`
        """
        return self.delete_domain_with_http_info(request)

    def delete_domain_with_http_info(self, request):
        all_params = ['domain_id', 'enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1.0/cdn/domains/{domain_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteDomainResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def disable_domain(self, request):
        """停用加速域名

        停用加速域名。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DisableDomain
        :type request: :class:`huaweicloudsdkcdn.v1.DisableDomainRequest`
        :rtype: :class:`huaweicloudsdkcdn.v1.DisableDomainResponse`
        """
        return self.disable_domain_with_http_info(request)

    def disable_domain_with_http_info(self, request):
        all_params = ['domain_id', 'enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1.0/cdn/domains/{domain_id}/disable',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DisableDomainResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def enable_domain(self, request):
        """启用加速域名

        启用加速域名。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for EnableDomain
        :type request: :class:`huaweicloudsdkcdn.v1.EnableDomainRequest`
        :rtype: :class:`huaweicloudsdkcdn.v1.EnableDomainResponse`
        """
        return self.enable_domain_with_http_info(request)

    def enable_domain_with_http_info(self, request):
        all_params = ['domain_id', 'enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1.0/cdn/domains/{domain_id}/enable',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='EnableDomainResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_domains(self, request):
        """查询加速域名

        查询加速域名信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListDomains
        :type request: :class:`huaweicloudsdkcdn.v1.ListDomainsRequest`
        :rtype: :class:`huaweicloudsdkcdn.v1.ListDomainsResponse`
        """
        return self.list_domains_with_http_info(request)

    def list_domains_with_http_info(self, request):
        all_params = ['domain_name', 'business_type', 'domain_status', 'service_area', 'page_size', 'page_number', 'enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'domain_name' in local_var_params:
            query_params.append(('domain_name', local_var_params['domain_name']))
        if 'business_type' in local_var_params:
            query_params.append(('business_type', local_var_params['business_type']))
        if 'domain_status' in local_var_params:
            query_params.append(('domain_status', local_var_params['domain_status']))
        if 'service_area' in local_var_params:
            query_params.append(('service_area', local_var_params['service_area']))
        if 'page_size' in local_var_params:
            query_params.append(('page_size', local_var_params['page_size']))
        if 'page_number' in local_var_params:
            query_params.append(('page_number', local_var_params['page_number']))
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
            resource_path='/v1.0/cdn/domains',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListDomainsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_black_white_list(self, request):
        """查询IP黑白名单

        查询域名已经设置的IP黑白名单。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowBlackWhiteList
        :type request: :class:`huaweicloudsdkcdn.v1.ShowBlackWhiteListRequest`
        :rtype: :class:`huaweicloudsdkcdn.v1.ShowBlackWhiteListResponse`
        """
        return self.show_black_white_list_with_http_info(request)

    def show_black_white_list_with_http_info(self, request):
        all_params = ['domain_id', 'enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1.0/cdn/domains/{domain_id}/ip-acl',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowBlackWhiteListResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_cache_rules(self, request):
        """查询缓存规则

        查询缓存规则。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowCacheRules
        :type request: :class:`huaweicloudsdkcdn.v1.ShowCacheRulesRequest`
        :rtype: :class:`huaweicloudsdkcdn.v1.ShowCacheRulesResponse`
        """
        return self.show_cache_rules_with_http_info(request)

    def show_cache_rules_with_http_info(self, request):
        all_params = ['domain_id', 'enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1.0/cdn/domains/{domain_id}/cache',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowCacheRulesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_certificates_https_info(self, request):
        """查询所有绑定HTTPS证书的域名信息

        查询所有绑定HTTPS证书的域名信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowCertificatesHttpsInfo
        :type request: :class:`huaweicloudsdkcdn.v1.ShowCertificatesHttpsInfoRequest`
        :rtype: :class:`huaweicloudsdkcdn.v1.ShowCertificatesHttpsInfoResponse`
        """
        return self.show_certificates_https_info_with_http_info(request)

    def show_certificates_https_info_with_http_info(self, request):
        all_params = ['page_size', 'page_number', 'domain_name', 'user_domain_id', 'enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'page_size' in local_var_params:
            query_params.append(('page_size', local_var_params['page_size']))
        if 'page_number' in local_var_params:
            query_params.append(('page_number', local_var_params['page_number']))
        if 'domain_name' in local_var_params:
            query_params.append(('domain_name', local_var_params['domain_name']))
        if 'user_domain_id' in local_var_params:
            query_params.append(('user_domain_id', local_var_params['user_domain_id']))
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
            resource_path='/v1.0/cdn/domains/https-certificate-info',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowCertificatesHttpsInfoResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_domain_detail(self, request):
        """查询加速域名详情

        查询加速域名详情。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDomainDetail
        :type request: :class:`huaweicloudsdkcdn.v1.ShowDomainDetailRequest`
        :rtype: :class:`huaweicloudsdkcdn.v1.ShowDomainDetailResponse`
        """
        return self.show_domain_detail_with_http_info(request)

    def show_domain_detail_with_http_info(self, request):
        all_params = ['domain_id', 'enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1.0/cdn/domains/{domain_id}/detail',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowDomainDetailResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_domain_full_config(self, request):
        """查询域名配置接口

        查询域名配置接口，支持查询回源请求头、HTTP header配置、URL鉴权、证书、源站、回源协议、强制重定向、智能压缩、缓存URL参数、IPv6开关、状态码缓存时间、Range回源、User-Agent黑白名单、改写回源URL、自定义错误页面
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDomainFullConfig
        :type request: :class:`huaweicloudsdkcdn.v1.ShowDomainFullConfigRequest`
        :rtype: :class:`huaweicloudsdkcdn.v1.ShowDomainFullConfigResponse`
        """
        return self.show_domain_full_config_with_http_info(request)

    def show_domain_full_config_with_http_info(self, request):
        all_params = ['domain_name', 'enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_name' in local_var_params:
            path_params['domain_name'] = local_var_params['domain_name']

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
            resource_path='/v1.1/cdn/configuration/domains/{domain_name}/configs',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowDomainFullConfigResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_domain_item_details(self, request):
        """批量查询域名的统计明细-按域名单独返回

        - 支持查询90天内的数据。
        - 查询跨度不能超过7天。
        - 最多同时指定100个域名。
        - 起始时间和结束时间，左闭右开，需要同时指定。
        - 开始时间、结束时间必须传毫秒级时间戳，且必须为5分钟整时刻点，如：0分、5分、10分、15分等，如果传的不是5分钟时刻点，返回数据可能与预期不一致。
        - 统一用开始时间表示一个时间段，如：2019-01-24 20:15:00 表示取 [20:15:00, 20:20:00)的统计数据，且左闭右开。
        - 流量类指标单位统一为Byte（字节）、带宽类指标单位统一为bit/s（比特/秒）、请求数类指标单位统一为次数。用于查询指定域名、指定统计指标的明细数据。
        - 如果传的是多个域名，则每个域名的数据分开返回。
        - 支持同时查询多个指标，不超过10个。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDomainItemDetails
        :type request: :class:`huaweicloudsdkcdn.v1.ShowDomainItemDetailsRequest`
        :rtype: :class:`huaweicloudsdkcdn.v1.ShowDomainItemDetailsResponse`
        """
        return self.show_domain_item_details_with_http_info(request)

    def show_domain_item_details_with_http_info(self, request):
        all_params = ['start_time', 'end_time', 'domain_name', 'stat_type', 'enterprise_project_id', 'service_area']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'domain_name' in local_var_params:
            query_params.append(('domain_name', local_var_params['domain_name']))
        if 'service_area' in local_var_params:
            query_params.append(('service_area', local_var_params['service_area']))
        if 'stat_type' in local_var_params:
            query_params.append(('stat_type', local_var_params['stat_type']))

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
            resource_path='/v1.0/cdn/statistics/domain-item-details',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowDomainItemDetailsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_domain_item_location_details(self, request):
        """批量查询域名的区域、运营商统计明细-按域名单独返回

        - 支持查询90天内的数据。
        - 查询跨度是7天。
        - 最多同时指定100个域名。
        - 起始时间和结束时间，左闭右开，需要同时指定。
        - 开始时间、结束时间必须传毫秒级时间戳，且必须为5分钟整时刻点，如：0分、5分、10分、15分等，如果传的不是5分钟时刻点，返回数据可能与预期不一致。
        - 统一用开始时间表示一个时间段，如：2019-01-24 20:15:00 表示取 [20:15:00, 20:20:00)的统计数据，且左闭右开。
        - 流量类指标单位统一为Byte（字节）、带宽类指标单位统一为bit/s（比特/秒）、请求数类指标单位统一为次数。
        - 用于查询指定域名、指定统计指标的明细数据。
        - 如果传的是多个域名，则每个域名的数据分开返回。
        - 支持按区域、运营商维度查询统计数据, 回源指标除外。
        - 支持同时查询多个指标，不超过10个。
        - 域名为海外加速场景不适用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDomainItemLocationDetails
        :type request: :class:`huaweicloudsdkcdn.v1.ShowDomainItemLocationDetailsRequest`
        :rtype: :class:`huaweicloudsdkcdn.v1.ShowDomainItemLocationDetailsResponse`
        """
        return self.show_domain_item_location_details_with_http_info(request)

    def show_domain_item_location_details_with_http_info(self, request):
        all_params = ['start_time', 'end_time', 'domain_name', 'stat_type', 'region', 'isp', 'enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'domain_name' in local_var_params:
            query_params.append(('domain_name', local_var_params['domain_name']))
        if 'stat_type' in local_var_params:
            query_params.append(('stat_type', local_var_params['stat_type']))
        if 'region' in local_var_params:
            query_params.append(('region', local_var_params['region']))
        if 'isp' in local_var_params:
            query_params.append(('isp', local_var_params['isp']))

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
            resource_path='/v1.0/cdn/statistics/domain-item-location-details',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowDomainItemLocationDetailsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_domain_location_stats(self, request):
        """查询域名统计数据-区域运营商

        - 支持查询90天内的数据。
        
        - 支持多指标同时查询，不超过5个。
        
        - 最多同时指定20个域名。
        
        - 起始时间和结束时间需要同时指定，左闭右开，毫秒级时间戳，且时间点必须为与查询时间间隔参数匹配的整时刻点。比如查询时间间隔为5分钟时，起始时间和结束时间必须为5分钟整时刻点，如：0分、5分、10分、15分等，如果时间点与时间间隔不匹配，返回数据可能与预期不一致。统一用开始时间表示一个时间段，如：2019-01-24 20:15:00 表示取 [20:15:00, 20:20:00)的统计数据，且左闭右开。
        
        - action取值：location_detail,location_summary
        
        - 流量类指标单位统一为Byte（字节）、带宽类指标单位统一为bit/s（比特/秒）、请求数类和状态码类指标单位统一为次数。用于查询指定域名、指定统计指标的区域运营商明细数据。
        
        - 单租户调用频率：15次/s。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDomainLocationStats
        :type request: :class:`huaweicloudsdkcdn.v1.ShowDomainLocationStatsRequest`
        :rtype: :class:`huaweicloudsdkcdn.v1.ShowDomainLocationStatsResponse`
        """
        return self.show_domain_location_stats_with_http_info(request)

    def show_domain_location_stats_with_http_info(self, request):
        all_params = ['action', 'start_time', 'end_time', 'domain_name', 'stat_type', 'interval', 'group_by', 'country', 'province', 'isp', 'enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'action' in local_var_params:
            query_params.append(('action', local_var_params['action']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'interval' in local_var_params:
            query_params.append(('interval', local_var_params['interval']))
        if 'domain_name' in local_var_params:
            query_params.append(('domain_name', local_var_params['domain_name']))
        if 'stat_type' in local_var_params:
            query_params.append(('stat_type', local_var_params['stat_type']))
        if 'group_by' in local_var_params:
            query_params.append(('group_by', local_var_params['group_by']))
        if 'country' in local_var_params:
            query_params.append(('country', local_var_params['country']))
        if 'province' in local_var_params:
            query_params.append(('province', local_var_params['province']))
        if 'isp' in local_var_params:
            query_params.append(('isp', local_var_params['isp']))
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
            resource_path='/v1.0/cdn/statistics/domain-location-stats',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowDomainLocationStatsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_domain_stats(self, request):
        """查询域名统计数据

        - 支持查询90天内的数据。
        
        - 支持多指标同时查询，不超过5个。
        
        - 最多同时指定20个域名。
        
        - 起始时间和结束时间需要同时指定，左闭右开，毫秒级时间戳，且时间点必须为与查询时间间隔参数匹配的整时刻点。比如查询时间间隔为5分钟时，起始时间和结束时间必须为5分钟整时刻点，如：0分、5分、10分、15分等，如果时间点与时间间隔不匹配，返回数据可能与预期不一致。统一用开始时间表示一个时间段，如：2019-01-24 20:15:00 表示取 [20:15:00, 20:20:00)的统计数据，且左闭右开。
        
        - action取值：detail,summary
        
        - 流量类指标单位统一为Byte（字节）、带宽类指标单位统一为bit/s（比特/秒）、请求数类和状态码类指标单位统一为次数。用于查询指定域名、指定统计指标的明细数据。
        
        - 单租户调用频率：15次/s。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDomainStats
        :type request: :class:`huaweicloudsdkcdn.v1.ShowDomainStatsRequest`
        :rtype: :class:`huaweicloudsdkcdn.v1.ShowDomainStatsResponse`
        """
        return self.show_domain_stats_with_http_info(request)

    def show_domain_stats_with_http_info(self, request):
        all_params = ['action', 'start_time', 'end_time', 'domain_name', 'stat_type', 'interval', 'group_by', 'service_area', 'enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'action' in local_var_params:
            query_params.append(('action', local_var_params['action']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'domain_name' in local_var_params:
            query_params.append(('domain_name', local_var_params['domain_name']))
        if 'stat_type' in local_var_params:
            query_params.append(('stat_type', local_var_params['stat_type']))
        if 'interval' in local_var_params:
            query_params.append(('interval', local_var_params['interval']))
        if 'group_by' in local_var_params:
            query_params.append(('group_by', local_var_params['group_by']))
        if 'service_area' in local_var_params:
            query_params.append(('service_area', local_var_params['service_area']))
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
            resource_path='/v1.0/cdn/statistics/domain-stats',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowDomainStatsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_history_task_details(self, request):
        """查询刷新预热任务详情

        查询刷新预热任务详情。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowHistoryTaskDetails
        :type request: :class:`huaweicloudsdkcdn.v1.ShowHistoryTaskDetailsRequest`
        :rtype: :class:`huaweicloudsdkcdn.v1.ShowHistoryTaskDetailsResponse`
        """
        return self.show_history_task_details_with_http_info(request)

    def show_history_task_details_with_http_info(self, request):
        all_params = ['history_tasks_id', 'enterprise_project_id', 'page_size', 'page_number', 'status', 'url', 'create_time']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'history_tasks_id' in local_var_params:
            path_params['history_tasks_id'] = local_var_params['history_tasks_id']

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'page_size' in local_var_params:
            query_params.append(('page_size', local_var_params['page_size']))
        if 'page_number' in local_var_params:
            query_params.append(('page_number', local_var_params['page_number']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'url' in local_var_params:
            query_params.append(('url', local_var_params['url']))
        if 'create_time' in local_var_params:
            query_params.append(('create_time', local_var_params['create_time']))

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
            resource_path='/v1.0/cdn/historytasks/{history_tasks_id}/detail',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowHistoryTaskDetailsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_history_tasks(self, request):
        """查询刷新预热任务

        查询刷新预热任务。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowHistoryTasks
        :type request: :class:`huaweicloudsdkcdn.v1.ShowHistoryTasksRequest`
        :rtype: :class:`huaweicloudsdkcdn.v1.ShowHistoryTasksResponse`
        """
        return self.show_history_tasks_with_http_info(request)

    def show_history_tasks_with_http_info(self, request):
        all_params = ['enterprise_project_id', 'page_size', 'page_number', 'status', 'start_date', 'end_date', 'order_field', 'order_type', 'file_type']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'page_size' in local_var_params:
            query_params.append(('page_size', local_var_params['page_size']))
        if 'page_number' in local_var_params:
            query_params.append(('page_number', local_var_params['page_number']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'start_date' in local_var_params:
            query_params.append(('start_date', local_var_params['start_date']))
        if 'end_date' in local_var_params:
            query_params.append(('end_date', local_var_params['end_date']))
        if 'order_field' in local_var_params:
            query_params.append(('order_field', local_var_params['order_field']))
        if 'order_type' in local_var_params:
            query_params.append(('order_type', local_var_params['order_type']))
        if 'file_type' in local_var_params:
            query_params.append(('file_type', local_var_params['file_type']))

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
            resource_path='/v1.0/cdn/historytasks',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowHistoryTasksResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_http_info(self, request):
        """查询HTTPS配置

        获取加速域名证书。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowHttpInfo
        :type request: :class:`huaweicloudsdkcdn.v1.ShowHttpInfoRequest`
        :rtype: :class:`huaweicloudsdkcdn.v1.ShowHttpInfoResponse`
        """
        return self.show_http_info_with_http_info(request)

    def show_http_info_with_http_info(self, request):
        all_params = ['domain_id', 'enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1.0/cdn/domains/{domain_id}/https-info',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowHttpInfoResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_ip_info(self, request):
        """查询IP归属信息

        查询IP归属信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowIpInfo
        :type request: :class:`huaweicloudsdkcdn.v1.ShowIpInfoRequest`
        :rtype: :class:`huaweicloudsdkcdn.v1.ShowIpInfoResponse`
        """
        return self.show_ip_info_with_http_info(request)

    def show_ip_info_with_http_info(self, request):
        all_params = ['ips', 'enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'ips' in local_var_params:
            query_params.append(('ips', local_var_params['ips']))

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
            resource_path='/v1.0/cdn/ip-info',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowIpInfoResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_logs(self, request):
        """日志查询

        日志查询。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowLogs
        :type request: :class:`huaweicloudsdkcdn.v1.ShowLogsRequest`
        :rtype: :class:`huaweicloudsdkcdn.v1.ShowLogsResponse`
        """
        return self.show_logs_with_http_info(request)

    def show_logs_with_http_info(self, request):
        all_params = ['domain_name', 'query_date', 'page_size', 'page_number', 'enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'domain_name' in local_var_params:
            query_params.append(('domain_name', local_var_params['domain_name']))
        if 'query_date' in local_var_params:
            query_params.append(('query_date', local_var_params['query_date']))
        if 'page_size' in local_var_params:
            query_params.append(('page_size', local_var_params['page_size']))
        if 'page_number' in local_var_params:
            query_params.append(('page_number', local_var_params['page_number']))
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
            resource_path='/v1.0/cdn/logs',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowLogsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_origin_host(self, request):
        """查询回源HOST

        查询回源HOST。回源HOST是CDN节点在回源过程中，在源站访问的站点域名，即http请求头中的host信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowOriginHost
        :type request: :class:`huaweicloudsdkcdn.v1.ShowOriginHostRequest`
        :rtype: :class:`huaweicloudsdkcdn.v1.ShowOriginHostResponse`
        """
        return self.show_origin_host_with_http_info(request)

    def show_origin_host_with_http_info(self, request):
        all_params = ['domain_id', 'enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1.0/cdn/domains/{domain_id}/originhost',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowOriginHostResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_quota(self, request):
        """查询用户配额

        查询当前用户域名、刷新文件、刷新目录和预热的配额
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowQuota
        :type request: :class:`huaweicloudsdkcdn.v1.ShowQuotaRequest`
        :rtype: :class:`huaweicloudsdkcdn.v1.ShowQuotaResponse`
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
            resource_path='/v1.0/cdn/quota',
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

    def show_refer(self, request):
        """查询Referer过滤规则

        查询Referer过滤规则。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowRefer
        :type request: :class:`huaweicloudsdkcdn.v1.ShowReferRequest`
        :rtype: :class:`huaweicloudsdkcdn.v1.ShowReferResponse`
        """
        return self.show_refer_with_http_info(request)

    def show_refer_with_http_info(self, request):
        all_params = ['domain_id', 'enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1.0/cdn/domains/{domain_id}/referer',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowReferResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_response_header(self, request):
        """查询响应头配置

        列举header所有配置。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowResponseHeader
        :type request: :class:`huaweicloudsdkcdn.v1.ShowResponseHeaderRequest`
        :rtype: :class:`huaweicloudsdkcdn.v1.ShowResponseHeaderResponse`
        """
        return self.show_response_header_with_http_info(request)

    def show_response_header_with_http_info(self, request):
        all_params = ['domain_id', 'enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1.0/cdn/domains/{domain_id}/response-header',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowResponseHeaderResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_tags(self, request):
        """查询资源标签列表配置接口

        用于查询资源标签列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowTags
        :type request: :class:`huaweicloudsdkcdn.v1.ShowTagsRequest`
        :rtype: :class:`huaweicloudsdkcdn.v1.ShowTagsResponse`
        """
        return self.show_tags_with_http_info(request)

    def show_tags_with_http_info(self, request):
        all_params = ['resource_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'resource_id' in local_var_params:
            query_params.append(('resource_id', local_var_params['resource_id']))

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
            resource_path='/v1.0/cdn/configuration/tags',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_top_url(self, request):
        """查询TOP100 URL明细

        - 查询TOP100 URL明细。
        
        - 支持查询90天内的数据。
        
        - 查询跨度不能超过31天。
        
        - 起始时间和结束时间，左闭右开，需要同时指定。如查询2021-10-24 00:00:00 到 2021-10-25 00:00:00
        的数据，表示取 [2021-10-24 00:00:00, 2021-10-25 00:00:00)的统计数据。
        
        - 开始时间、结束时间必须传毫秒级时间戳，且必须为凌晨0点整时刻点，如果传的不是凌晨0点整时刻点，返回数据可能与预期不一致。
        
        - 流量类指标单位统一为Byte（字节）、请求数类指标单位统一为次数。用于查询指定域名、指定统计指标的明细数据。
        
        - 单租户调用频率：5次/s。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowTopUrl
        :type request: :class:`huaweicloudsdkcdn.v1.ShowTopUrlRequest`
        :rtype: :class:`huaweicloudsdkcdn.v1.ShowTopUrlResponse`
        """
        return self.show_top_url_with_http_info(request)

    def show_top_url_with_http_info(self, request):
        all_params = ['start_time', 'end_time', 'domain_name', 'stat_type', 'enterprise_project_id', 'service_area']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'domain_name' in local_var_params:
            query_params.append(('domain_name', local_var_params['domain_name']))
        if 'service_area' in local_var_params:
            query_params.append(('service_area', local_var_params['service_area']))
        if 'stat_type' in local_var_params:
            query_params.append(('stat_type', local_var_params['stat_type']))

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
            resource_path='/v1.0/cdn/statistics/top-url',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowTopUrlResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_url_task_info(self, request):
        """查询刷新预热URL记录

        查询刷新预热URL记录。如需此接口，请提交工单开通
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowUrlTaskInfo
        :type request: :class:`huaweicloudsdkcdn.v1.ShowUrlTaskInfoRequest`
        :rtype: :class:`huaweicloudsdkcdn.v1.ShowUrlTaskInfoResponse`
        """
        return self.show_url_task_info_with_http_info(request)

    def show_url_task_info_with_http_info(self, request):
        all_params = ['start_time', 'end_time', 'offset', 'limit', 'url', 'task_type', 'status', 'file_type']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'url' in local_var_params:
            query_params.append(('url', local_var_params['url']))
        if 'task_type' in local_var_params:
            query_params.append(('task_type', local_var_params['task_type']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'file_type' in local_var_params:
            query_params.append(('file_type', local_var_params['file_type']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1.0/cdn/contentgateway/url-tasks',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowUrlTaskInfoResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_black_white_list(self, request):
        """设置IP黑白名单

        设置域名的IP黑白名单。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateBlackWhiteList
        :type request: :class:`huaweicloudsdkcdn.v1.UpdateBlackWhiteListRequest`
        :rtype: :class:`huaweicloudsdkcdn.v1.UpdateBlackWhiteListResponse`
        """
        return self.update_black_white_list_with_http_info(request)

    def update_black_white_list_with_http_info(self, request):
        all_params = ['domain_id', 'black_white_list_body', 'enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v1.0/cdn/domains/{domain_id}/ip-acl',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateBlackWhiteListResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_cache_rules(self, request):
        """设置缓存规则

        设置CDN节点上缓存资源的缓存策略。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateCacheRules
        :type request: :class:`huaweicloudsdkcdn.v1.UpdateCacheRulesRequest`
        :rtype: :class:`huaweicloudsdkcdn.v1.UpdateCacheRulesResponse`
        """
        return self.update_cache_rules_with_http_info(request)

    def update_cache_rules_with_http_info(self, request):
        all_params = ['domain_id', 'cache_config', 'enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v1.0/cdn/domains/{domain_id}/cache',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateCacheRulesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_domain_full_config(self, request):
        """修改域名全量配置接口

        修改域名全量配置接口，支持配置回源请求头、HTTP header配置、URL鉴权、证书、源站、回源协议、强制重定向、智能压缩、缓存URL参数、IPv6、状态码缓存时间、Range回源、User-Agent黑白名单、改写回源URL、自定义错误页面
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateDomainFullConfig
        :type request: :class:`huaweicloudsdkcdn.v1.UpdateDomainFullConfigRequest`
        :rtype: :class:`huaweicloudsdkcdn.v1.UpdateDomainFullConfigResponse`
        """
        return self.update_domain_full_config_with_http_info(request)

    def update_domain_full_config_with_http_info(self, request):
        all_params = ['domain_name', 'configs', 'enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_name' in local_var_params:
            path_params['domain_name'] = local_var_params['domain_name']

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
            resource_path='/v1.1/cdn/configuration/domains/{domain_name}/configs',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateDomainFullConfigResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_domain_multi_certificates(self, request):
        """一个证书批量设置多个域名

        一个证书配置多个域名，设置域名强制https回源参数。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateDomainMultiCertificates
        :type request: :class:`huaweicloudsdkcdn.v1.UpdateDomainMultiCertificatesRequest`
        :rtype: :class:`huaweicloudsdkcdn.v1.UpdateDomainMultiCertificatesResponse`
        """
        return self.update_domain_multi_certificates_with_http_info(request)

    def update_domain_multi_certificates_with_http_info(self, request):
        all_params = ['enterprise_project_id', 'https']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            resource_path='/v1.0/cdn/domains/config-https-info',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateDomainMultiCertificatesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_domain_origin(self, request):
        """修改源站信息

        修改源站信息。源站IP地址或域名都可以指引CDN节点回源到对应的源站服务器，源站域名不能与加速域名相同。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateDomainOrigin
        :type request: :class:`huaweicloudsdkcdn.v1.UpdateDomainOriginRequest`
        :rtype: :class:`huaweicloudsdkcdn.v1.UpdateDomainOriginResponse`
        """
        return self.update_domain_origin_with_http_info(request)

    def update_domain_origin_with_http_info(self, request):
        all_params = ['domain_id', 'origin', 'enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v1.0/cdn/domains/{domain_id}/origin',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateDomainOriginResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_follow302_switch(self, request):
        """开启/关闭回源跟随

        开启此项配置后，当CDN节点回源请求源站返回301/302状态码时，CDN节点会先跳转到301/302对应地址获取资源并缓存后再返回给用户。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateFollow302Switch
        :type request: :class:`huaweicloudsdkcdn.v1.UpdateFollow302SwitchRequest`
        :rtype: :class:`huaweicloudsdkcdn.v1.UpdateFollow302SwitchResponse`
        """
        return self.update_follow302_switch_with_http_info(request)

    def update_follow302_switch_with_http_info(self, request):
        all_params = ['domain_id', 'follow_status', 'enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v1.0/cdn/domains/{domain_id}/follow302-switch',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateFollow302SwitchResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_https_info(self, request):
        """配置HTTPS

        设置加速域名HTTPS。通过配置加速域名的HTTPS证书，并将其部署在全网CDN节点，实现HTTPS安全加速。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateHttpsInfo
        :type request: :class:`huaweicloudsdkcdn.v1.UpdateHttpsInfoRequest`
        :rtype: :class:`huaweicloudsdkcdn.v1.UpdateHttpsInfoResponse`
        """
        return self.update_https_info_with_http_info(request)

    def update_https_info_with_http_info(self, request):
        all_params = ['domain_id', 'https', 'enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v1.0/cdn/domains/{domain_id}/https-info',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateHttpsInfoResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_origin_host(self, request):
        """修改回源HOST

        修改回源HOST。回源HOST是CDN节点在回源过程中，在源站访问的站点域名，即http请求头中的host信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateOriginHost
        :type request: :class:`huaweicloudsdkcdn.v1.UpdateOriginHostRequest`
        :rtype: :class:`huaweicloudsdkcdn.v1.UpdateOriginHostResponse`
        """
        return self.update_origin_host_with_http_info(request)

    def update_origin_host_with_http_info(self, request):
        all_params = ['domain_id', 'origin_host', 'enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v1.0/cdn/domains/{domain_id}/originhost',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateOriginHostResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_private_bucket_access(self, request):
        """修改私有桶开启关闭状态

        修改私有桶开启关闭状态。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdatePrivateBucketAccess
        :type request: :class:`huaweicloudsdkcdn.v1.UpdatePrivateBucketAccessRequest`
        :rtype: :class:`huaweicloudsdkcdn.v1.UpdatePrivateBucketAccessResponse`
        """
        return self.update_private_bucket_access_with_http_info(request)

    def update_private_bucket_access_with_http_info(self, request):
        all_params = ['domain_id', 'enterprise_project_id', 'status']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v1.0/cdn/domains/{domain_id}/private-bucket-access',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdatePrivateBucketAccessResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_range_switch(self, request):
        """开启/关闭Range回源

        Range回源是指源站在收到CDN节点回源请求时，根据http请求头中的Range信息返回指定范围的数据给CDN节点。
        
        开启Range回源前需要确认源站是否支持Range请求，若源站不支持Range请求，开启Range回源将导致资源无法缓存。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateRangeSwitch
        :type request: :class:`huaweicloudsdkcdn.v1.UpdateRangeSwitchRequest`
        :rtype: :class:`huaweicloudsdkcdn.v1.UpdateRangeSwitchResponse`
        """
        return self.update_range_switch_with_http_info(request)

    def update_range_switch_with_http_info(self, request):
        all_params = ['domain_id', 'range_status', 'enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v1.0/cdn/domains/{domain_id}/range-switch',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateRangeSwitchResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_refer(self, request):
        """设置Referer过滤规则

        设置Referer过滤规则。通过设置过滤策略，对访问者身份进行识别和过滤，实现限制访问来源的目的。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateRefer
        :type request: :class:`huaweicloudsdkcdn.v1.UpdateReferRequest`
        :rtype: :class:`huaweicloudsdkcdn.v1.UpdateReferResponse`
        """
        return self.update_refer_with_http_info(request)

    def update_refer_with_http_info(self, request):
        all_params = ['domain_id', 'refer', 'enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v1.0/cdn/domains/{domain_id}/referer',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateReferResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_response_header(self, request):
        """新增/修改响应头配置

        新增/修改域名响应头配置。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateResponseHeader
        :type request: :class:`huaweicloudsdkcdn.v1.UpdateResponseHeaderRequest`
        :rtype: :class:`huaweicloudsdkcdn.v1.UpdateResponseHeaderResponse`
        """
        return self.update_response_header_with_http_info(request)

    def update_response_header_with_http_info(self, request):
        all_params = ['domain_id', 'headers', 'enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v1.0/cdn/domains/{domain_id}/response-header',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateResponseHeaderResponse',
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
        :param header_params: Header parameters to be placed in the request header.
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
            request_type=request_type)

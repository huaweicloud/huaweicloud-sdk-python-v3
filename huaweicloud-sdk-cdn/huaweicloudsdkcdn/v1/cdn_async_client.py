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


class CdnAsyncClient(Client):
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
        super(CdnAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkcdn.v1.model")
        self.preset_headers = {'User-Agent': 'HuaweiCloud-SDK-Python'}

    @classmethod
    def new_builder(cls, clazz=None):
        if clazz is None:
            return ClientBuilder(cls, "GlobalCredentials")

        if clazz.__name__ != "CdnClient":
            raise TypeError("client type error, support client type is CdnClient")

        return ClientBuilder(clazz, "GlobalCredentials")

    def create_domain_async(self, request):
        """创建加速域名

        创建加速域名。

        :param CreateDomainRequest request
        :return: CreateDomainResponse
        """
        return self.create_domain_with_http_info(request)

    def create_domain_with_http_info(self, request):
        """创建加速域名

        创建加速域名。

        :param CreateDomainRequest request
        :return: CreateDomainResponse
        """

        all_params = ['domain']
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
            resource_path='/v1.0/cdn/domains',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateDomainResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_preheating_tasks_async(self, request):
        """创建预热缓存任务

        创建预热任务。

        :param CreatePreheatingTasksRequest request
        :return: CreatePreheatingTasksResponse
        """
        return self.create_preheating_tasks_with_http_info(request)

    def create_preheating_tasks_with_http_info(self, request):
        """创建预热缓存任务

        创建预热任务。

        :param CreatePreheatingTasksRequest request
        :return: CreatePreheatingTasksResponse
        """

        all_params = ['preheating_task', 'enterprise_project_id']
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
            resource_path='/v1.0/cdn/content/preheating-tasks',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreatePreheatingTasksResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_refresh_tasks_async(self, request):
        """创建刷新缓存任务

        创建刷新缓存任务。

        :param CreateRefreshTasksRequest request
        :return: CreateRefreshTasksResponse
        """
        return self.create_refresh_tasks_with_http_info(request)

    def create_refresh_tasks_with_http_info(self, request):
        """创建刷新缓存任务

        创建刷新缓存任务。

        :param CreateRefreshTasksRequest request
        :return: CreateRefreshTasksResponse
        """

        all_params = ['refresh_task', 'enterprise_project_id']
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
            resource_path='/v1.0/cdn/content/refresh-tasks',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateRefreshTasksResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_domain_async(self, request):
        """删除加速域名

        删除加速域名。

        :param DeleteDomainRequest request
        :return: DeleteDomainResponse
        """
        return self.delete_domain_with_http_info(request)

    def delete_domain_with_http_info(self, request):
        """删除加速域名

        删除加速域名。

        :param DeleteDomainRequest request
        :return: DeleteDomainResponse
        """

        all_params = ['domain_id', 'enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='DeleteDomainResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def disable_domain_async(self, request):
        """停用加速域名

        停用加速域名。

        :param DisableDomainRequest request
        :return: DisableDomainResponse
        """
        return self.disable_domain_with_http_info(request)

    def disable_domain_with_http_info(self, request):
        """停用加速域名

        停用加速域名。

        :param DisableDomainRequest request
        :return: DisableDomainResponse
        """

        all_params = ['domain_id', 'enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='DisableDomainResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def enable_domain_async(self, request):
        """启用加速域名

        启用加速域名。

        :param EnableDomainRequest request
        :return: EnableDomainResponse
        """
        return self.enable_domain_with_http_info(request)

    def enable_domain_with_http_info(self, request):
        """启用加速域名

        启用加速域名。

        :param EnableDomainRequest request
        :return: EnableDomainResponse
        """

        all_params = ['domain_id', 'enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='EnableDomainResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_domains_async(self, request):
        """查询加速域名

        查询加速域名信息

        :param ListDomainsRequest request
        :return: ListDomainsResponse
        """
        return self.list_domains_with_http_info(request)

    def list_domains_with_http_info(self, request):
        """查询加速域名

        查询加速域名信息

        :param ListDomainsRequest request
        :return: ListDomainsResponse
        """

        all_params = ['domain_name', 'business_type', 'domain_status', 'service_area', 'page_size', 'page_number', 'enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='ListDomainsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_black_white_list_async(self, request):
        """查询IP黑白名单

        查询域名已经设置的IP黑白名单。

        :param ShowBlackWhiteListRequest request
        :return: ShowBlackWhiteListResponse
        """
        return self.show_black_white_list_with_http_info(request)

    def show_black_white_list_with_http_info(self, request):
        """查询IP黑白名单

        查询域名已经设置的IP黑白名单。

        :param ShowBlackWhiteListRequest request
        :return: ShowBlackWhiteListResponse
        """

        all_params = ['domain_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']

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
            resource_path='/v1.0/cdn/domains/{domain_id}/ip-acl',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowBlackWhiteListResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_cache_rules_async(self, request):
        """查询缓存规则

        查询缓存规则。

        :param ShowCacheRulesRequest request
        :return: ShowCacheRulesResponse
        """
        return self.show_cache_rules_with_http_info(request)

    def show_cache_rules_with_http_info(self, request):
        """查询缓存规则

        查询缓存规则。

        :param ShowCacheRulesRequest request
        :return: ShowCacheRulesResponse
        """

        all_params = ['domain_id', 'enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='ShowCacheRulesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_certificates_https_info_async(self, request):
        """查询所有绑定HTTPS证书的域名信息

        查询所有绑定HTTPS证书的域名信息

        :param ShowCertificatesHttpsInfoRequest request
        :return: ShowCertificatesHttpsInfoResponse
        """
        return self.show_certificates_https_info_with_http_info(request)

    def show_certificates_https_info_with_http_info(self, request):
        """查询所有绑定HTTPS证书的域名信息

        查询所有绑定HTTPS证书的域名信息

        :param ShowCertificatesHttpsInfoRequest request
        :return: ShowCertificatesHttpsInfoResponse
        """

        all_params = ['page_size', 'page_number', 'domain_name', 'user_domain_id', 'enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='ShowCertificatesHttpsInfoResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_domain_detail_async(self, request):
        """查询加速域名详情

        查询加速域名详情。

        :param ShowDomainDetailRequest request
        :return: ShowDomainDetailResponse
        """
        return self.show_domain_detail_with_http_info(request)

    def show_domain_detail_with_http_info(self, request):
        """查询加速域名详情

        查询加速域名详情。

        :param ShowDomainDetailRequest request
        :return: ShowDomainDetailResponse
        """

        all_params = ['domain_id', 'enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='ShowDomainDetailResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_domain_item_details_async(self, request):
        """批量查询域名的统计明细-按域名单独返回

        - 支持查询3个月内的数据。 - 查询跨度不能超过7天。 - 最多同时指定100个域名。 - 起始时间和结束时间，左闭右开，需要同时指定。 - 开始时间、结束时间必须传毫秒级时间戳，且必须为5分钟整时刻点，如：0分、5分、10分、15分等，如果传的不是5分钟时刻点，返回数据可能与预期不一致。 - 统一用开始时间表示一个时间段，如：2019-01-24 20:15:00 表示取 [20:15:00, 20:20:00)的统计数据，且左闭右开。 - 流量类指标单位统一为Byte（字节）、带宽类指标单位统一为bit/s（比特/秒）、请求数类指标单位统一为次数。用于查询指定域名、指定统计指标的明细数据。 - 如果传的是多个域名，则每个域名的数据分开返回。 - 支持同时查询多个指标，不超过10个。

        :param ShowDomainItemDetailsRequest request
        :return: ShowDomainItemDetailsResponse
        """
        return self.show_domain_item_details_with_http_info(request)

    def show_domain_item_details_with_http_info(self, request):
        """批量查询域名的统计明细-按域名单独返回

        - 支持查询3个月内的数据。 - 查询跨度不能超过7天。 - 最多同时指定100个域名。 - 起始时间和结束时间，左闭右开，需要同时指定。 - 开始时间、结束时间必须传毫秒级时间戳，且必须为5分钟整时刻点，如：0分、5分、10分、15分等，如果传的不是5分钟时刻点，返回数据可能与预期不一致。 - 统一用开始时间表示一个时间段，如：2019-01-24 20:15:00 表示取 [20:15:00, 20:20:00)的统计数据，且左闭右开。 - 流量类指标单位统一为Byte（字节）、带宽类指标单位统一为bit/s（比特/秒）、请求数类指标单位统一为次数。用于查询指定域名、指定统计指标的明细数据。 - 如果传的是多个域名，则每个域名的数据分开返回。 - 支持同时查询多个指标，不超过10个。

        :param ShowDomainItemDetailsRequest request
        :return: ShowDomainItemDetailsResponse
        """

        all_params = ['start_time', 'end_time', 'domain_name', 'stat_type', 'enterprise_project_id', 'service_area']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='ShowDomainItemDetailsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_domain_item_location_details_async(self, request):
        """批量查询域名的区域、运营商统计明细-按域名单独返回

        - 支持查询3个月内的数据。 - 查询跨度不能超过7天。 - 最多同时指定100个域名。 - 起始时间和结束时间，左闭右开，需要同时指定。 - 开始时间、结束时间必须传毫秒级时间戳，且必须为5分钟整时刻点，如：0分、5分、10分、15分等，如果传的不是5分钟时刻点，返回数据可能与预期不一致。 - 统一用开始时间表示一个时间段，如：2019-01-24 20:15:00 表示取 [20:15:00, 20:20:00)的统计数据，且左闭右开。 - 流量类指标单位统一为Byte（字节）、带宽类指标单位统一为bit/s（比特/秒）、请求数类指标单位统一为次数。 - 用于查询指定域名、指定统计指标的明细数据。 - 如果传的是多个域名，则每个域名的数据分开返回。 - 支持按区域、运营商维度查询统计数据, 回源指标除外。 - 支持同时查询多个指标，不超过10个。 - 域名为海外加速场景不适用。

        :param ShowDomainItemLocationDetailsRequest request
        :return: ShowDomainItemLocationDetailsResponse
        """
        return self.show_domain_item_location_details_with_http_info(request)

    def show_domain_item_location_details_with_http_info(self, request):
        """批量查询域名的区域、运营商统计明细-按域名单独返回

        - 支持查询3个月内的数据。 - 查询跨度不能超过7天。 - 最多同时指定100个域名。 - 起始时间和结束时间，左闭右开，需要同时指定。 - 开始时间、结束时间必须传毫秒级时间戳，且必须为5分钟整时刻点，如：0分、5分、10分、15分等，如果传的不是5分钟时刻点，返回数据可能与预期不一致。 - 统一用开始时间表示一个时间段，如：2019-01-24 20:15:00 表示取 [20:15:00, 20:20:00)的统计数据，且左闭右开。 - 流量类指标单位统一为Byte（字节）、带宽类指标单位统一为bit/s（比特/秒）、请求数类指标单位统一为次数。 - 用于查询指定域名、指定统计指标的明细数据。 - 如果传的是多个域名，则每个域名的数据分开返回。 - 支持按区域、运营商维度查询统计数据, 回源指标除外。 - 支持同时查询多个指标，不超过10个。 - 域名为海外加速场景不适用。

        :param ShowDomainItemLocationDetailsRequest request
        :return: ShowDomainItemLocationDetailsResponse
        """

        all_params = ['start_time', 'end_time', 'domain_name', 'stat_type', 'region', 'isp', 'enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='ShowDomainItemLocationDetailsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_history_task_details_async(self, request):
        """查询刷新预热任务详情

        查询刷新预热任务详情。

        :param ShowHistoryTaskDetailsRequest request
        :return: ShowHistoryTaskDetailsResponse
        """
        return self.show_history_task_details_with_http_info(request)

    def show_history_task_details_with_http_info(self, request):
        """查询刷新预热任务详情

        查询刷新预热任务详情。

        :param ShowHistoryTaskDetailsRequest request
        :return: ShowHistoryTaskDetailsResponse
        """

        all_params = ['history_tasks_id', 'enterprise_project_id', 'page_size', 'page_number', 'status', 'url']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='ShowHistoryTaskDetailsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_history_tasks_async(self, request):
        """查询刷新预热任务

        查询刷新预热任务。

        :param ShowHistoryTasksRequest request
        :return: ShowHistoryTasksResponse
        """
        return self.show_history_tasks_with_http_info(request)

    def show_history_tasks_with_http_info(self, request):
        """查询刷新预热任务

        查询刷新预热任务。

        :param ShowHistoryTasksRequest request
        :return: ShowHistoryTasksResponse
        """

        all_params = ['enterprise_project_id', 'page_size', 'page_number', 'status', 'start_date', 'end_date', 'order_field', 'order_type', 'file_type']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='ShowHistoryTasksResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_http_info_async(self, request):
        """查询HTTPS配置

        获取加速域名证书。

        :param ShowHttpInfoRequest request
        :return: ShowHttpInfoResponse
        """
        return self.show_http_info_with_http_info(request)

    def show_http_info_with_http_info(self, request):
        """查询HTTPS配置

        获取加速域名证书。

        :param ShowHttpInfoRequest request
        :return: ShowHttpInfoResponse
        """

        all_params = ['domain_id', 'enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='ShowHttpInfoResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_ip_info_async(self, request):
        """查询IP归属信息

        查询IP归属信息。

        :param ShowIpInfoRequest request
        :return: ShowIpInfoResponse
        """
        return self.show_ip_info_with_http_info(request)

    def show_ip_info_with_http_info(self, request):
        """查询IP归属信息

        查询IP归属信息。

        :param ShowIpInfoRequest request
        :return: ShowIpInfoResponse
        """

        all_params = ['ips', 'enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='ShowIpInfoResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_logs_async(self, request):
        """日志查询

        日志查询。

        :param ShowLogsRequest request
        :return: ShowLogsResponse
        """
        return self.show_logs_with_http_info(request)

    def show_logs_with_http_info(self, request):
        """日志查询

        日志查询。

        :param ShowLogsRequest request
        :return: ShowLogsResponse
        """

        all_params = ['domain_name', 'query_date', 'page_size', 'page_number', 'enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='ShowLogsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_origin_host_async(self, request):
        """查询回源HOST

        查询回源HOST。回源HOST是CDN节点在回源过程中，在源站访问的站点域名，即http请求头中的host信息。

        :param ShowOriginHostRequest request
        :return: ShowOriginHostResponse
        """
        return self.show_origin_host_with_http_info(request)

    def show_origin_host_with_http_info(self, request):
        """查询回源HOST

        查询回源HOST。回源HOST是CDN节点在回源过程中，在源站访问的站点域名，即http请求头中的host信息。

        :param ShowOriginHostRequest request
        :return: ShowOriginHostResponse
        """

        all_params = ['domain_id', 'enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='ShowOriginHostResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_quota_async(self, request):
        """查询用户配额

        查询当前用户域名、刷新文件、刷新目录和预热的配额

        :param ShowQuotaRequest request
        :return: ShowQuotaResponse
        """
        return self.show_quota_with_http_info(request)

    def show_quota_with_http_info(self, request):
        """查询用户配额

        查询当前用户域名、刷新文件、刷新目录和预热的配额

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
            response_type='ShowQuotaResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_refer_async(self, request):
        """查询Referer过滤规则

        查询Referer过滤规则。

        :param ShowReferRequest request
        :return: ShowReferResponse
        """
        return self.show_refer_with_http_info(request)

    def show_refer_with_http_info(self, request):
        """查询Referer过滤规则

        查询Referer过滤规则。

        :param ShowReferRequest request
        :return: ShowReferResponse
        """

        all_params = ['domain_id', 'enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='ShowReferResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_response_header_async(self, request):
        """查询响应头配置

        列举header所有配置。

        :param ShowResponseHeaderRequest request
        :return: ShowResponseHeaderResponse
        """
        return self.show_response_header_with_http_info(request)

    def show_response_header_with_http_info(self, request):
        """查询响应头配置

        列举header所有配置。

        :param ShowResponseHeaderRequest request
        :return: ShowResponseHeaderResponse
        """

        all_params = ['domain_id', 'enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='ShowResponseHeaderResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_top_url_async(self, request):
        """查询TOP100 URL明细

        查询TOP100 URL明细。

        :param ShowTopUrlRequest request
        :return: ShowTopUrlResponse
        """
        return self.show_top_url_with_http_info(request)

    def show_top_url_with_http_info(self, request):
        """查询TOP100 URL明细

        查询TOP100 URL明细。

        :param ShowTopUrlRequest request
        :return: ShowTopUrlResponse
        """

        all_params = ['start_time', 'end_time', 'domain_name', 'stat_type', 'enterprise_project_id', 'service_area']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='ShowTopUrlResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_black_white_list_async(self, request):
        """设置IP黑白名单

        设置域名的IP黑白名单。

        :param UpdateBlackWhiteListRequest request
        :return: UpdateBlackWhiteListResponse
        """
        return self.update_black_white_list_with_http_info(request)

    def update_black_white_list_with_http_info(self, request):
        """设置IP黑白名单

        设置域名的IP黑白名单。

        :param UpdateBlackWhiteListRequest request
        :return: UpdateBlackWhiteListResponse
        """

        all_params = ['domain_id', 'black_white_list_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']

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
            resource_path='/v1.0/cdn/domains/{domain_id}/ip-acl',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateBlackWhiteListResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_cache_rules_async(self, request):
        """设置缓存规则

        设置CDN节点上缓存资源的缓存策略。

        :param UpdateCacheRulesRequest request
        :return: UpdateCacheRulesResponse
        """
        return self.update_cache_rules_with_http_info(request)

    def update_cache_rules_with_http_info(self, request):
        """设置缓存规则

        设置CDN节点上缓存资源的缓存策略。

        :param UpdateCacheRulesRequest request
        :return: UpdateCacheRulesResponse
        """

        all_params = ['domain_id', 'cache_config', 'enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='UpdateCacheRulesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_domain_multi_certificates_async(self, request):
        """一个证书批量设置多个域名

        一个证书配置多个域名，设置域名强制https回源参数。

        :param UpdateDomainMultiCertificatesRequest request
        :return: UpdateDomainMultiCertificatesResponse
        """
        return self.update_domain_multi_certificates_with_http_info(request)

    def update_domain_multi_certificates_with_http_info(self, request):
        """一个证书批量设置多个域名

        一个证书配置多个域名，设置域名强制https回源参数。

        :param UpdateDomainMultiCertificatesRequest request
        :return: UpdateDomainMultiCertificatesResponse
        """

        all_params = ['https']
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
            resource_path='/v1.0/cdn/domains/config-https-info',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateDomainMultiCertificatesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_domain_origin_async(self, request):
        """修改源站信息

        修改源站信息。源站IP地址或域名都可以指引CDN节点回源到对应的源站服务器，源站域名不能与加速域名相同。

        :param UpdateDomainOriginRequest request
        :return: UpdateDomainOriginResponse
        """
        return self.update_domain_origin_with_http_info(request)

    def update_domain_origin_with_http_info(self, request):
        """修改源站信息

        修改源站信息。源站IP地址或域名都可以指引CDN节点回源到对应的源站服务器，源站域名不能与加速域名相同。

        :param UpdateDomainOriginRequest request
        :return: UpdateDomainOriginResponse
        """

        all_params = ['domain_id', 'origin', 'enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='UpdateDomainOriginResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_follow302_switch_async(self, request):
        """开启/关闭回源跟随

        开启此项配置后，当CDN节点回源请求源站返回302状态码时，CDN节点会先跳转到302对应地址获取资源并缓存后再返回给用户。

        :param UpdateFollow302SwitchRequest request
        :return: UpdateFollow302SwitchResponse
        """
        return self.update_follow302_switch_with_http_info(request)

    def update_follow302_switch_with_http_info(self, request):
        """开启/关闭回源跟随

        开启此项配置后，当CDN节点回源请求源站返回302状态码时，CDN节点会先跳转到302对应地址获取资源并缓存后再返回给用户。

        :param UpdateFollow302SwitchRequest request
        :return: UpdateFollow302SwitchResponse
        """

        all_params = ['domain_id', 'follow_status']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']

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
            resource_path='/v1.0/cdn/domains/{domain_id}/follow302-switch',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateFollow302SwitchResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_https_info_async(self, request):
        """配置HTTPS

        设置加速域名HTTPS。通过配置加速域名的HTTPS证书，并将其部署在全网CDN节点，实现HTTPS安全加速。

        :param UpdateHttpsInfoRequest request
        :return: UpdateHttpsInfoResponse
        """
        return self.update_https_info_with_http_info(request)

    def update_https_info_with_http_info(self, request):
        """配置HTTPS

        设置加速域名HTTPS。通过配置加速域名的HTTPS证书，并将其部署在全网CDN节点，实现HTTPS安全加速。

        :param UpdateHttpsInfoRequest request
        :return: UpdateHttpsInfoResponse
        """

        all_params = ['domain_id', 'https', 'enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='UpdateHttpsInfoResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_origin_host_async(self, request):
        """修改回源HOST

        修改回源HOST。回源HOST是CDN节点在回源过程中，在源站访问的站点域名，即http请求头中的host信息。

        :param UpdateOriginHostRequest request
        :return: UpdateOriginHostResponse
        """
        return self.update_origin_host_with_http_info(request)

    def update_origin_host_with_http_info(self, request):
        """修改回源HOST

        修改回源HOST。回源HOST是CDN节点在回源过程中，在源站访问的站点域名，即http请求头中的host信息。

        :param UpdateOriginHostRequest request
        :return: UpdateOriginHostResponse
        """

        all_params = ['domain_id', 'origin_host', 'enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='UpdateOriginHostResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_private_bucket_access_async(self, request):
        """修改私有桶开启关闭状态

        修改私有桶开启关闭状态。

        :param UpdatePrivateBucketAccessRequest request
        :return: UpdatePrivateBucketAccessResponse
        """
        return self.update_private_bucket_access_with_http_info(request)

    def update_private_bucket_access_with_http_info(self, request):
        """修改私有桶开启关闭状态

        修改私有桶开启关闭状态。

        :param UpdatePrivateBucketAccessRequest request
        :return: UpdatePrivateBucketAccessResponse
        """

        all_params = ['domain_id', 'status']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']

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
            resource_path='/v1.0/cdn/domains/{domain_id}/private-bucket-access',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdatePrivateBucketAccessResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_range_switch_async(self, request):
        """开启/关闭Range回源

        Range回源是指源站在收到CDN节点回源请求时，根据http请求头中的Range信息返回指定范围的数据给CDN节点。  开启Range回源前需要确认源站是否支持Range请求，若源站不支持Range请求，开启Range回源将导致资源无法缓存。

        :param UpdateRangeSwitchRequest request
        :return: UpdateRangeSwitchResponse
        """
        return self.update_range_switch_with_http_info(request)

    def update_range_switch_with_http_info(self, request):
        """开启/关闭Range回源

        Range回源是指源站在收到CDN节点回源请求时，根据http请求头中的Range信息返回指定范围的数据给CDN节点。  开启Range回源前需要确认源站是否支持Range请求，若源站不支持Range请求，开启Range回源将导致资源无法缓存。

        :param UpdateRangeSwitchRequest request
        :return: UpdateRangeSwitchResponse
        """

        all_params = ['domain_id', 'range_status']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']

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
            resource_path='/v1.0/cdn/domains/{domain_id}/range-switch',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateRangeSwitchResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_refer_async(self, request):
        """设置Referer过滤规则

        设置Referer过滤规则。通过设置过滤策略，对访问者身份进行识别和过滤，实现限制访问来源的目的。

        :param UpdateReferRequest request
        :return: UpdateReferResponse
        """
        return self.update_refer_with_http_info(request)

    def update_refer_with_http_info(self, request):
        """设置Referer过滤规则

        设置Referer过滤规则。通过设置过滤策略，对访问者身份进行识别和过滤，实现限制访问来源的目的。

        :param UpdateReferRequest request
        :return: UpdateReferResponse
        """

        all_params = ['domain_id', 'refer', 'enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='UpdateReferResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_response_header_async(self, request):
        """新增/修改响应头配置

        新增/修改域名响应头配置。

        :param UpdateResponseHeaderRequest request
        :return: UpdateResponseHeaderResponse
        """
        return self.update_response_header_with_http_info(request)

    def update_response_header_with_http_info(self, request):
        """新增/修改响应头配置

        新增/修改域名响应头配置。

        :param UpdateResponseHeaderRequest request
        :return: UpdateResponseHeaderResponse
        """

        all_params = ['domain_id', 'headers', 'enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='UpdateResponseHeaderResponse',
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

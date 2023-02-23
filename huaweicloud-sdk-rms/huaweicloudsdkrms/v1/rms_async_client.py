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


class RmsAsyncClient(Client):
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
        super(RmsAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkrms.v1.model")
        self.preset_headers = {'User-Agent': 'HuaweiCloud-SDK-Python'}

    @classmethod
    def new_builder(cls, clazz=None):
        if clazz is None:
            return ClientBuilder(cls, "GlobalCredentials")

        if clazz.__name__ != "RmsClient":
            raise TypeError("client type error, support client type is RmsClient")

        return ClientBuilder(clazz, "GlobalCredentials")

    def create_aggregation_authorization_async(self, request):
        """创建资源聚合器授权

        给资源聚合器帐号授予从源帐号收集数据的权限。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateAggregationAuthorization
        :type request: :class:`huaweicloudsdkrms.v1.CreateAggregationAuthorizationRequest`
        :rtype: :class:`huaweicloudsdkrms.v1.CreateAggregationAuthorizationResponse`
        """
        return self.create_aggregation_authorization_with_http_info(request)

    def create_aggregation_authorization_with_http_info(self, request):
        all_params = ['aggregation_authorization_request']
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

        auth_settings = ['AccessKeyAuth']

        return self.call_api(
            resource_path='/v1/resource-manager/domains/{domain_id}/aggregators/aggregation-authorization',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateAggregationAuthorizationResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_configuration_aggregator_async(self, request):
        """创建资源聚合器

        创建资源聚合器。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateConfigurationAggregator
        :type request: :class:`huaweicloudsdkrms.v1.CreateConfigurationAggregatorRequest`
        :rtype: :class:`huaweicloudsdkrms.v1.CreateConfigurationAggregatorResponse`
        """
        return self.create_configuration_aggregator_with_http_info(request)

    def create_configuration_aggregator_with_http_info(self, request):
        all_params = ['configuration_aggregator_request']
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

        auth_settings = ['AccessKeyAuth']

        return self.call_api(
            resource_path='/v1/resource-manager/domains/{domain_id}/aggregators',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateConfigurationAggregatorResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_aggregation_authorization_async(self, request):
        """删除资源聚合器授权

        删除指定资源聚合器帐号的授权。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteAggregationAuthorization
        :type request: :class:`huaweicloudsdkrms.v1.DeleteAggregationAuthorizationRequest`
        :rtype: :class:`huaweicloudsdkrms.v1.DeleteAggregationAuthorizationResponse`
        """
        return self.delete_aggregation_authorization_with_http_info(request)

    def delete_aggregation_authorization_with_http_info(self, request):
        all_params = ['authorized_account_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'authorized_account_id' in local_var_params:
            path_params['authorized_account_id'] = local_var_params['authorized_account_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['AccessKeyAuth']

        return self.call_api(
            resource_path='/v1/resource-manager/domains/{domain_id}/aggregators/aggregation-authorization/{authorized_account_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteAggregationAuthorizationResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_configuration_aggregator_async(self, request):
        """删除资源聚合器

        删除资源聚合器。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteConfigurationAggregator
        :type request: :class:`huaweicloudsdkrms.v1.DeleteConfigurationAggregatorRequest`
        :rtype: :class:`huaweicloudsdkrms.v1.DeleteConfigurationAggregatorResponse`
        """
        return self.delete_configuration_aggregator_with_http_info(request)

    def delete_configuration_aggregator_with_http_info(self, request):
        all_params = ['aggregator_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'aggregator_id' in local_var_params:
            path_params['aggregator_id'] = local_var_params['aggregator_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['AccessKeyAuth']

        return self.call_api(
            resource_path='/v1/resource-manager/domains/{domain_id}/aggregators/{aggregator_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteConfigurationAggregatorResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_pending_aggregation_request_async(self, request):
        """删除聚合器帐号中挂起的授权请求

        删除聚合器帐号中挂起的授权请求。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeletePendingAggregationRequest
        :type request: :class:`huaweicloudsdkrms.v1.DeletePendingAggregationRequestRequest`
        :rtype: :class:`huaweicloudsdkrms.v1.DeletePendingAggregationRequestResponse`
        """
        return self.delete_pending_aggregation_request_with_http_info(request)

    def delete_pending_aggregation_request_with_http_info(self, request):
        all_params = ['requester_account_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'requester_account_id' in local_var_params:
            path_params['requester_account_id'] = local_var_params['requester_account_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['AccessKeyAuth']

        return self.call_api(
            resource_path='/v1/resource-manager/domains/{domain_id}/aggregators/pending-aggregation-request/{requester_account_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeletePendingAggregationRequestResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_aggregate_discovered_resources_async(self, request):
        """查询聚合器中资源的列表

        查询资源聚合器中特定资源的列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAggregateDiscoveredResources
        :type request: :class:`huaweicloudsdkrms.v1.ListAggregateDiscoveredResourcesRequest`
        :rtype: :class:`huaweicloudsdkrms.v1.ListAggregateDiscoveredResourcesResponse`
        """
        return self.list_aggregate_discovered_resources_with_http_info(request)

    def list_aggregate_discovered_resources_with_http_info(self, request):
        all_params = ['limit', 'marker', 'aggregate_discovered_resources_request']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))

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

        auth_settings = ['AccessKeyAuth']

        return self.call_api(
            resource_path='/v1/resource-manager/domains/{domain_id}/aggregators/aggregate-data/aggregate-discovered-resources',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListAggregateDiscoveredResourcesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_aggregation_authorizations_async(self, request):
        """查询资源聚合器授权列表

        查询授权过的资源聚合器列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAggregationAuthorizations
        :type request: :class:`huaweicloudsdkrms.v1.ListAggregationAuthorizationsRequest`
        :rtype: :class:`huaweicloudsdkrms.v1.ListAggregationAuthorizationsResponse`
        """
        return self.list_aggregation_authorizations_with_http_info(request)

    def list_aggregation_authorizations_with_http_info(self, request):
        all_params = ['account_id', 'limit', 'marker']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'account_id' in local_var_params:
            query_params.append(('account_id', local_var_params['account_id']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['AccessKeyAuth']

        return self.call_api(
            resource_path='/v1/resource-manager/domains/{domain_id}/aggregators/aggregation-authorization',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListAggregationAuthorizationsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_configuration_aggregators_async(self, request):
        """查询资源聚合器列表

        查询资源聚合器列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListConfigurationAggregators
        :type request: :class:`huaweicloudsdkrms.v1.ListConfigurationAggregatorsRequest`
        :rtype: :class:`huaweicloudsdkrms.v1.ListConfigurationAggregatorsResponse`
        """
        return self.list_configuration_aggregators_with_http_info(request)

    def list_configuration_aggregators_with_http_info(self, request):
        all_params = ['aggregator_name', 'limit', 'marker']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'aggregator_name' in local_var_params:
            query_params.append(('aggregator_name', local_var_params['aggregator_name']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['AccessKeyAuth']

        return self.call_api(
            resource_path='/v1/resource-manager/domains/{domain_id}/aggregators',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListConfigurationAggregatorsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_pending_aggregation_requests_async(self, request):
        """查询所有挂起的聚合请求列表

        查询所有挂起的聚合请求列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListPendingAggregationRequests
        :type request: :class:`huaweicloudsdkrms.v1.ListPendingAggregationRequestsRequest`
        :rtype: :class:`huaweicloudsdkrms.v1.ListPendingAggregationRequestsResponse`
        """
        return self.list_pending_aggregation_requests_with_http_info(request)

    def list_pending_aggregation_requests_with_http_info(self, request):
        all_params = ['account_id', 'limit', 'marker']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'account_id' in local_var_params:
            query_params.append(('account_id', local_var_params['account_id']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['AccessKeyAuth']

        return self.call_api(
            resource_path='/v1/resource-manager/domains/{domain_id}/aggregators/pending-aggregation-request',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListPendingAggregationRequestsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def run_aggregate_resource_query_async(self, request):
        """对指定聚合器执行高级查询

        对指定聚合器执行高级查询。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RunAggregateResourceQuery
        :type request: :class:`huaweicloudsdkrms.v1.RunAggregateResourceQueryRequest`
        :rtype: :class:`huaweicloudsdkrms.v1.RunAggregateResourceQueryResponse`
        """
        return self.run_aggregate_resource_query_with_http_info(request)

    def run_aggregate_resource_query_with_http_info(self, request):
        all_params = ['aggregator_id', 'query_run_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'aggregator_id' in local_var_params:
            path_params['aggregator_id'] = local_var_params['aggregator_id']

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

        auth_settings = ['AccessKeyAuth']

        return self.call_api(
            resource_path='/v1/resource-manager/domains/{domain_id}/aggregators/{aggregator_id}/run-query',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RunAggregateResourceQueryResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_aggregate_discovered_resource_counts_async(self, request):
        """查询聚合器中帐号资源的计数

        查询聚合器中帐号资源的计数，支持通过过滤器和GroupByKey来统计资源数量。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowAggregateDiscoveredResourceCounts
        :type request: :class:`huaweicloudsdkrms.v1.ShowAggregateDiscoveredResourceCountsRequest`
        :rtype: :class:`huaweicloudsdkrms.v1.ShowAggregateDiscoveredResourceCountsResponse`
        """
        return self.show_aggregate_discovered_resource_counts_with_http_info(request)

    def show_aggregate_discovered_resource_counts_with_http_info(self, request):
        all_params = ['aggregate_discovered_resource_counts_request']
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

        auth_settings = ['AccessKeyAuth']

        return self.call_api(
            resource_path='/v1/resource-manager/domains/{domain_id}/aggregators/aggregate-data/aggregate-discovered-resource-counts',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowAggregateDiscoveredResourceCountsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_aggregate_resource_config_async(self, request):
        """查询源帐号中资源的详情

        查询源帐号中特定资源的详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowAggregateResourceConfig
        :type request: :class:`huaweicloudsdkrms.v1.ShowAggregateResourceConfigRequest`
        :rtype: :class:`huaweicloudsdkrms.v1.ShowAggregateResourceConfigResponse`
        """
        return self.show_aggregate_resource_config_with_http_info(request)

    def show_aggregate_resource_config_with_http_info(self, request):
        all_params = ['aggregate_resource_config_request']
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

        auth_settings = ['AccessKeyAuth']

        return self.call_api(
            resource_path='/v1/resource-manager/domains/{domain_id}/aggregators/aggregate-resource-config',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowAggregateResourceConfigResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_configuration_aggregator_async(self, request):
        """查询指定资源聚合器

        查询指定资源聚合器。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowConfigurationAggregator
        :type request: :class:`huaweicloudsdkrms.v1.ShowConfigurationAggregatorRequest`
        :rtype: :class:`huaweicloudsdkrms.v1.ShowConfigurationAggregatorResponse`
        """
        return self.show_configuration_aggregator_with_http_info(request)

    def show_configuration_aggregator_with_http_info(self, request):
        all_params = ['aggregator_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'aggregator_id' in local_var_params:
            path_params['aggregator_id'] = local_var_params['aggregator_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['AccessKeyAuth']

        return self.call_api(
            resource_path='/v1/resource-manager/domains/{domain_id}/aggregators/{aggregator_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowConfigurationAggregatorResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_configuration_aggregator_sources_status_async(self, request):
        """查询指定资源聚合器聚合帐号的状态信息

        查询指定资源聚合器聚合帐号的状态信息，状态包括验证源帐号和聚合器帐号之间授权的信息。如果失败，状态包含相关的错误码或消息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowConfigurationAggregatorSourcesStatus
        :type request: :class:`huaweicloudsdkrms.v1.ShowConfigurationAggregatorSourcesStatusRequest`
        :rtype: :class:`huaweicloudsdkrms.v1.ShowConfigurationAggregatorSourcesStatusResponse`
        """
        return self.show_configuration_aggregator_sources_status_with_http_info(request)

    def show_configuration_aggregator_sources_status_with_http_info(self, request):
        all_params = ['aggregator_id', 'update_status', 'limit', 'marker']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'aggregator_id' in local_var_params:
            path_params['aggregator_id'] = local_var_params['aggregator_id']

        query_params = []
        if 'update_status' in local_var_params:
            query_params.append(('update_status', local_var_params['update_status']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['AccessKeyAuth']

        return self.call_api(
            resource_path='/v1/resource-manager/domains/{domain_id}/aggregators/{aggregator_id}/aggregator-sources-status',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowConfigurationAggregatorSourcesStatusResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_configuration_aggregator_async(self, request):
        """更新资源聚合器

        更新资源聚合器。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateConfigurationAggregator
        :type request: :class:`huaweicloudsdkrms.v1.UpdateConfigurationAggregatorRequest`
        :rtype: :class:`huaweicloudsdkrms.v1.UpdateConfigurationAggregatorResponse`
        """
        return self.update_configuration_aggregator_with_http_info(request)

    def update_configuration_aggregator_with_http_info(self, request):
        all_params = ['aggregator_id', 'configuration_aggregator_request']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'aggregator_id' in local_var_params:
            path_params['aggregator_id'] = local_var_params['aggregator_id']

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

        auth_settings = ['AccessKeyAuth']

        return self.call_api(
            resource_path='/v1/resource-manager/domains/{domain_id}/aggregators/{aggregator_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateConfigurationAggregatorResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_resource_history_async(self, request):
        """查询资源历史

        查询资源与资源关系的变更历史
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowResourceHistory
        :type request: :class:`huaweicloudsdkrms.v1.ShowResourceHistoryRequest`
        :rtype: :class:`huaweicloudsdkrms.v1.ShowResourceHistoryResponse`
        """
        return self.show_resource_history_with_http_info(request)

    def show_resource_history_with_http_info(self, request):
        all_params = ['resource_id', 'marker', 'limit', 'earlier_time', 'later_time', 'chronological_order']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_id' in local_var_params:
            path_params['resource_id'] = local_var_params['resource_id']

        query_params = []
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'earlier_time' in local_var_params:
            query_params.append(('earlier_time', local_var_params['earlier_time']))
        if 'later_time' in local_var_params:
            query_params.append(('later_time', local_var_params['later_time']))
        if 'chronological_order' in local_var_params:
            query_params.append(('chronological_order', local_var_params['chronological_order']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['PkiTokenAuth']

        return self.call_api(
            resource_path='/v1/resource-manager/domains/{domain_id}/resources/{resource_id}/history',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowResourceHistoryResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_organization_policy_assignment_async(self, request):
        """创建或更新组织合规规则

        创建或更新组织合规规则，如果规则名称已存在，则为更新操作。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateOrganizationPolicyAssignment
        :type request: :class:`huaweicloudsdkrms.v1.CreateOrganizationPolicyAssignmentRequest`
        :rtype: :class:`huaweicloudsdkrms.v1.CreateOrganizationPolicyAssignmentResponse`
        """
        return self.create_organization_policy_assignment_with_http_info(request)

    def create_organization_policy_assignment_with_http_info(self, request):
        all_params = ['organization_id', 'organization_policy_assignment_request']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'organization_id' in local_var_params:
            path_params['organization_id'] = local_var_params['organization_id']

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

        auth_settings = ['AccessKeyAuth']

        return self.call_api(
            resource_path='/v1/resource-manager/organizations/{organization_id}/policy-assignments',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateOrganizationPolicyAssignmentResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_policy_assignments_async(self, request):
        """创建合规规则

        创建新的合规规则
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreatePolicyAssignments
        :type request: :class:`huaweicloudsdkrms.v1.CreatePolicyAssignmentsRequest`
        :rtype: :class:`huaweicloudsdkrms.v1.CreatePolicyAssignmentsResponse`
        """
        return self.create_policy_assignments_with_http_info(request)

    def create_policy_assignments_with_http_info(self, request):
        all_params = ['policy_assignment_request_body']
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

        auth_settings = ['PkiTokenAuth']

        return self.call_api(
            resource_path='/v1/resource-manager/domains/{domain_id}/policy-assignments',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreatePolicyAssignmentsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_organization_policy_assignment_async(self, request):
        """删除组织合规规则

        删除组织合规规则。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteOrganizationPolicyAssignment
        :type request: :class:`huaweicloudsdkrms.v1.DeleteOrganizationPolicyAssignmentRequest`
        :rtype: :class:`huaweicloudsdkrms.v1.DeleteOrganizationPolicyAssignmentResponse`
        """
        return self.delete_organization_policy_assignment_with_http_info(request)

    def delete_organization_policy_assignment_with_http_info(self, request):
        all_params = ['organization_id', 'organization_policy_assignment_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'organization_id' in local_var_params:
            path_params['organization_id'] = local_var_params['organization_id']
        if 'organization_policy_assignment_id' in local_var_params:
            path_params['organization_policy_assignment_id'] = local_var_params['organization_policy_assignment_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['AccessKeyAuth']

        return self.call_api(
            resource_path='/v1/resource-manager/organizations/{organization_id}/policy-assignments/{organization_policy_assignment_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteOrganizationPolicyAssignmentResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_policy_assignment_async(self, request):
        """删除合规规则

        根据规则ID删除此规则
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeletePolicyAssignment
        :type request: :class:`huaweicloudsdkrms.v1.DeletePolicyAssignmentRequest`
        :rtype: :class:`huaweicloudsdkrms.v1.DeletePolicyAssignmentResponse`
        """
        return self.delete_policy_assignment_with_http_info(request)

    def delete_policy_assignment_with_http_info(self, request):
        all_params = ['policy_assignment_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policy_assignment_id' in local_var_params:
            path_params['policy_assignment_id'] = local_var_params['policy_assignment_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['PkiTokenAuth']

        return self.call_api(
            resource_path='/v1/resource-manager/domains/{domain_id}/policy-assignments/{policy_assignment_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeletePolicyAssignmentResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def disable_policy_assignment_async(self, request):
        """停用合规规则

        根据规则ID停用此规则
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DisablePolicyAssignment
        :type request: :class:`huaweicloudsdkrms.v1.DisablePolicyAssignmentRequest`
        :rtype: :class:`huaweicloudsdkrms.v1.DisablePolicyAssignmentResponse`
        """
        return self.disable_policy_assignment_with_http_info(request)

    def disable_policy_assignment_with_http_info(self, request):
        all_params = ['policy_assignment_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policy_assignment_id' in local_var_params:
            path_params['policy_assignment_id'] = local_var_params['policy_assignment_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['PkiTokenAuth']

        return self.call_api(
            resource_path='/v1/resource-manager/domains/{domain_id}/policy-assignments/{policy_assignment_id}/disable',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DisablePolicyAssignmentResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def enable_policy_assignment_async(self, request):
        """启用合规规则

        根据规则ID启用此规则
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for EnablePolicyAssignment
        :type request: :class:`huaweicloudsdkrms.v1.EnablePolicyAssignmentRequest`
        :rtype: :class:`huaweicloudsdkrms.v1.EnablePolicyAssignmentResponse`
        """
        return self.enable_policy_assignment_with_http_info(request)

    def enable_policy_assignment_with_http_info(self, request):
        all_params = ['policy_assignment_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policy_assignment_id' in local_var_params:
            path_params['policy_assignment_id'] = local_var_params['policy_assignment_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['PkiTokenAuth']

        return self.call_api(
            resource_path='/v1/resource-manager/domains/{domain_id}/policy-assignments/{policy_assignment_id}/enable',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='EnablePolicyAssignmentResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_built_in_policy_definitions_async(self, request):
        """列出内置策略

        列出用户的内置策略
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListBuiltInPolicyDefinitions
        :type request: :class:`huaweicloudsdkrms.v1.ListBuiltInPolicyDefinitionsRequest`
        :rtype: :class:`huaweicloudsdkrms.v1.ListBuiltInPolicyDefinitionsResponse`
        """
        return self.list_built_in_policy_definitions_with_http_info(request)

    def list_built_in_policy_definitions_with_http_info(self, request):
        all_params = ['x_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['PkiTokenAuth']

        return self.call_api(
            resource_path='/v1/resource-manager/policy-definitions',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListBuiltInPolicyDefinitionsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_organization_policy_assignments_async(self, request):
        """查询组织合规规则列表

        查询组织合规规则列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListOrganizationPolicyAssignments
        :type request: :class:`huaweicloudsdkrms.v1.ListOrganizationPolicyAssignmentsRequest`
        :rtype: :class:`huaweicloudsdkrms.v1.ListOrganizationPolicyAssignmentsResponse`
        """
        return self.list_organization_policy_assignments_with_http_info(request)

    def list_organization_policy_assignments_with_http_info(self, request):
        all_params = ['organization_id', 'organization_policy_assignment_name', 'limit', 'marker']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'organization_id' in local_var_params:
            path_params['organization_id'] = local_var_params['organization_id']

        query_params = []
        if 'organization_policy_assignment_name' in local_var_params:
            query_params.append(('organization_policy_assignment_name', local_var_params['organization_policy_assignment_name']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['AccessKeyAuth']

        return self.call_api(
            resource_path='/v1/resource-manager/organizations/{organization_id}/policy-assignments',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListOrganizationPolicyAssignmentsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_policy_assignments_async(self, request):
        """列出合规规则

        列出用户的合规规则
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListPolicyAssignments
        :type request: :class:`huaweicloudsdkrms.v1.ListPolicyAssignmentsRequest`
        :rtype: :class:`huaweicloudsdkrms.v1.ListPolicyAssignmentsResponse`
        """
        return self.list_policy_assignments_with_http_info(request)

    def list_policy_assignments_with_http_info(self, request):
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

        auth_settings = ['PkiTokenAuth']

        return self.call_api(
            resource_path='/v1/resource-manager/domains/{domain_id}/policy-assignments',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListPolicyAssignmentsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_policy_states_by_assignment_id_async(self, request):
        """获取规则的合规结果

        根据规则ID查询所有的合规结果
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListPolicyStatesByAssignmentId
        :type request: :class:`huaweicloudsdkrms.v1.ListPolicyStatesByAssignmentIdRequest`
        :rtype: :class:`huaweicloudsdkrms.v1.ListPolicyStatesByAssignmentIdResponse`
        """
        return self.list_policy_states_by_assignment_id_with_http_info(request)

    def list_policy_states_by_assignment_id_with_http_info(self, request):
        all_params = ['policy_assignment_id', 'compliance_state', 'resource_id', 'resource_name', 'limit', 'marker']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policy_assignment_id' in local_var_params:
            path_params['policy_assignment_id'] = local_var_params['policy_assignment_id']

        query_params = []
        if 'compliance_state' in local_var_params:
            query_params.append(('compliance_state', local_var_params['compliance_state']))
        if 'resource_id' in local_var_params:
            query_params.append(('resource_id', local_var_params['resource_id']))
        if 'resource_name' in local_var_params:
            query_params.append(('resource_name', local_var_params['resource_name']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['PkiTokenAuth']

        return self.call_api(
            resource_path='/v1/resource-manager/domains/{domain_id}/policy-assignments/{policy_assignment_id}/policy-states',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListPolicyStatesByAssignmentIdResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_policy_states_by_domain_id_async(self, request):
        """获取用户的合规结果

        查询用户所有的合规结果
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListPolicyStatesByDomainId
        :type request: :class:`huaweicloudsdkrms.v1.ListPolicyStatesByDomainIdRequest`
        :rtype: :class:`huaweicloudsdkrms.v1.ListPolicyStatesByDomainIdResponse`
        """
        return self.list_policy_states_by_domain_id_with_http_info(request)

    def list_policy_states_by_domain_id_with_http_info(self, request):
        all_params = ['compliance_state', 'resource_id', 'resource_name', 'limit', 'marker']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'compliance_state' in local_var_params:
            query_params.append(('compliance_state', local_var_params['compliance_state']))
        if 'resource_id' in local_var_params:
            query_params.append(('resource_id', local_var_params['resource_id']))
        if 'resource_name' in local_var_params:
            query_params.append(('resource_name', local_var_params['resource_name']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['PkiTokenAuth']

        return self.call_api(
            resource_path='/v1/resource-manager/domains/{domain_id}/policy-states',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListPolicyStatesByDomainIdResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_policy_states_by_resource_id_async(self, request):
        """获取资源的合规结果

        根据资源ID查询所有合规结果
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListPolicyStatesByResourceId
        :type request: :class:`huaweicloudsdkrms.v1.ListPolicyStatesByResourceIdRequest`
        :rtype: :class:`huaweicloudsdkrms.v1.ListPolicyStatesByResourceIdResponse`
        """
        return self.list_policy_states_by_resource_id_with_http_info(request)

    def list_policy_states_by_resource_id_with_http_info(self, request):
        all_params = ['resource_id', 'compliance_state', 'limit', 'marker']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_id' in local_var_params:
            path_params['resource_id'] = local_var_params['resource_id']

        query_params = []
        if 'compliance_state' in local_var_params:
            query_params.append(('compliance_state', local_var_params['compliance_state']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['PkiTokenAuth']

        return self.call_api(
            resource_path='/v1/resource-manager/domains/{domain_id}/resources/{resource_id}/policy-states',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListPolicyStatesByResourceIdResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def run_evaluation_by_policy_assignment_id_async(self, request):
        """运行合规评估

        根据规则ID评估此规则
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RunEvaluationByPolicyAssignmentId
        :type request: :class:`huaweicloudsdkrms.v1.RunEvaluationByPolicyAssignmentIdRequest`
        :rtype: :class:`huaweicloudsdkrms.v1.RunEvaluationByPolicyAssignmentIdResponse`
        """
        return self.run_evaluation_by_policy_assignment_id_with_http_info(request)

    def run_evaluation_by_policy_assignment_id_with_http_info(self, request):
        all_params = ['policy_assignment_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policy_assignment_id' in local_var_params:
            path_params['policy_assignment_id'] = local_var_params['policy_assignment_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['PkiTokenAuth']

        return self.call_api(
            resource_path='/v1/resource-manager/domains/{domain_id}/policy-assignments/{policy_assignment_id}/policy-states/run-evaluation',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RunEvaluationByPolicyAssignmentIdResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_built_in_policy_definition_async(self, request):
        """查询单个内置策略

        根据策略ID查询单个内置策略
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowBuiltInPolicyDefinition
        :type request: :class:`huaweicloudsdkrms.v1.ShowBuiltInPolicyDefinitionRequest`
        :rtype: :class:`huaweicloudsdkrms.v1.ShowBuiltInPolicyDefinitionResponse`
        """
        return self.show_built_in_policy_definition_with_http_info(request)

    def show_built_in_policy_definition_with_http_info(self, request):
        all_params = ['policy_definition_id', 'x_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policy_definition_id' in local_var_params:
            path_params['policy_definition_id'] = local_var_params['policy_definition_id']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['PkiTokenAuth']

        return self.call_api(
            resource_path='/v1/resource-manager/policy-definitions/{policy_definition_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowBuiltInPolicyDefinitionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_evaluation_state_by_assignment_id_async(self, request):
        """获取规则的评估状态

        根据规则ID查询此规则的评估状态
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowEvaluationStateByAssignmentId
        :type request: :class:`huaweicloudsdkrms.v1.ShowEvaluationStateByAssignmentIdRequest`
        :rtype: :class:`huaweicloudsdkrms.v1.ShowEvaluationStateByAssignmentIdResponse`
        """
        return self.show_evaluation_state_by_assignment_id_with_http_info(request)

    def show_evaluation_state_by_assignment_id_with_http_info(self, request):
        all_params = ['policy_assignment_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policy_assignment_id' in local_var_params:
            path_params['policy_assignment_id'] = local_var_params['policy_assignment_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['PkiTokenAuth']

        return self.call_api(
            resource_path='/v1/resource-manager/domains/{domain_id}/policy-assignments/{policy_assignment_id}/policy-states/evaluation-state',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowEvaluationStateByAssignmentIdResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_organization_policy_assignment_async(self, request):
        """查询指定组织合规规则

        查询指定组织合规规则。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowOrganizationPolicyAssignment
        :type request: :class:`huaweicloudsdkrms.v1.ShowOrganizationPolicyAssignmentRequest`
        :rtype: :class:`huaweicloudsdkrms.v1.ShowOrganizationPolicyAssignmentResponse`
        """
        return self.show_organization_policy_assignment_with_http_info(request)

    def show_organization_policy_assignment_with_http_info(self, request):
        all_params = ['organization_id', 'organization_policy_assignment_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'organization_id' in local_var_params:
            path_params['organization_id'] = local_var_params['organization_id']
        if 'organization_policy_assignment_id' in local_var_params:
            path_params['organization_policy_assignment_id'] = local_var_params['organization_policy_assignment_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['AccessKeyAuth']

        return self.call_api(
            resource_path='/v1/resource-manager/organizations/{organization_id}/policy-assignments/{organization_policy_assignment_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowOrganizationPolicyAssignmentResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_organization_policy_assignment_detailed_status_async(self, request):
        """查询组织内每个成员帐号合规规则部署的详细状态

        查询组织内每个成员帐号合规规则部署的详细状态。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowOrganizationPolicyAssignmentDetailedStatus
        :type request: :class:`huaweicloudsdkrms.v1.ShowOrganizationPolicyAssignmentDetailedStatusRequest`
        :rtype: :class:`huaweicloudsdkrms.v1.ShowOrganizationPolicyAssignmentDetailedStatusResponse`
        """
        return self.show_organization_policy_assignment_detailed_status_with_http_info(request)

    def show_organization_policy_assignment_detailed_status_with_http_info(self, request):
        all_params = ['organization_id', 'organization_policy_assignment_name', 'status', 'limit', 'marker']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'organization_id' in local_var_params:
            path_params['organization_id'] = local_var_params['organization_id']

        query_params = []
        if 'organization_policy_assignment_name' in local_var_params:
            query_params.append(('organization_policy_assignment_name', local_var_params['organization_policy_assignment_name']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['AccessKeyAuth']

        return self.call_api(
            resource_path='/v1/resource-manager/organizations/{organization_id}/policy-assignment-detailed-status',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowOrganizationPolicyAssignmentDetailedStatusResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_organization_policy_assignment_statuses_async(self, request):
        """查询组织合规规则部署状态

        查询组织合规规则部署状态。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowOrganizationPolicyAssignmentStatuses
        :type request: :class:`huaweicloudsdkrms.v1.ShowOrganizationPolicyAssignmentStatusesRequest`
        :rtype: :class:`huaweicloudsdkrms.v1.ShowOrganizationPolicyAssignmentStatusesResponse`
        """
        return self.show_organization_policy_assignment_statuses_with_http_info(request)

    def show_organization_policy_assignment_statuses_with_http_info(self, request):
        all_params = ['organization_id', 'organization_policy_assignment_name', 'limit', 'marker']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'organization_id' in local_var_params:
            path_params['organization_id'] = local_var_params['organization_id']

        query_params = []
        if 'organization_policy_assignment_name' in local_var_params:
            query_params.append(('organization_policy_assignment_name', local_var_params['organization_policy_assignment_name']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['AccessKeyAuth']

        return self.call_api(
            resource_path='/v1/resource-manager/organizations/{organization_id}/policy-assignment-statuses',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowOrganizationPolicyAssignmentStatusesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_policy_assignment_async(self, request):
        """获取单个合规规则

        根据规则ID获取单个规则
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowPolicyAssignment
        :type request: :class:`huaweicloudsdkrms.v1.ShowPolicyAssignmentRequest`
        :rtype: :class:`huaweicloudsdkrms.v1.ShowPolicyAssignmentResponse`
        """
        return self.show_policy_assignment_with_http_info(request)

    def show_policy_assignment_with_http_info(self, request):
        all_params = ['policy_assignment_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policy_assignment_id' in local_var_params:
            path_params['policy_assignment_id'] = local_var_params['policy_assignment_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['PkiTokenAuth']

        return self.call_api(
            resource_path='/v1/resource-manager/domains/{domain_id}/policy-assignments/{policy_assignment_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowPolicyAssignmentResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_policy_assignment_async(self, request):
        """更新合规规则

        更新用户的合规规则
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdatePolicyAssignment
        :type request: :class:`huaweicloudsdkrms.v1.UpdatePolicyAssignmentRequest`
        :rtype: :class:`huaweicloudsdkrms.v1.UpdatePolicyAssignmentResponse`
        """
        return self.update_policy_assignment_with_http_info(request)

    def update_policy_assignment_with_http_info(self, request):
        all_params = ['policy_assignment_id', 'policy_assignment_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policy_assignment_id' in local_var_params:
            path_params['policy_assignment_id'] = local_var_params['policy_assignment_id']

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

        auth_settings = ['PkiTokenAuth']

        return self.call_api(
            resource_path='/v1/resource-manager/domains/{domain_id}/policy-assignments/{policy_assignment_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdatePolicyAssignmentResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_policy_state_async(self, request):
        """更新合规评估结果

        更新用户自定义合规规则的合规评估结果
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdatePolicyState
        :type request: :class:`huaweicloudsdkrms.v1.UpdatePolicyStateRequest`
        :rtype: :class:`huaweicloudsdkrms.v1.UpdatePolicyStateResponse`
        """
        return self.update_policy_state_with_http_info(request)

    def update_policy_state_with_http_info(self, request):
        all_params = ['policy_state_request_body']
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

        auth_settings = ['PkiTokenAuth']

        return self.call_api(
            resource_path='/v1/resource-manager/domains/{domain_id}/policy-states',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdatePolicyStateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_stored_query_async(self, request):
        """创建高级查询

        创建新的高级查询
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateStoredQuery
        :type request: :class:`huaweicloudsdkrms.v1.CreateStoredQueryRequest`
        :rtype: :class:`huaweicloudsdkrms.v1.CreateStoredQueryResponse`
        """
        return self.create_stored_query_with_http_info(request)

    def create_stored_query_with_http_info(self, request):
        all_params = ['stored_query_request_body']
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

        auth_settings = ['PkiTokenAuth']

        return self.call_api(
            resource_path='/v1/resource-manager/domains/{domain_id}/stored-queries',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateStoredQueryResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_stored_query_async(self, request):
        """删除高级查询

        删除单个高级查询
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteStoredQuery
        :type request: :class:`huaweicloudsdkrms.v1.DeleteStoredQueryRequest`
        :rtype: :class:`huaweicloudsdkrms.v1.DeleteStoredQueryResponse`
        """
        return self.delete_stored_query_with_http_info(request)

    def delete_stored_query_with_http_info(self, request):
        all_params = ['query_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'query_id' in local_var_params:
            path_params['query_id'] = local_var_params['query_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['PkiTokenAuth']

        return self.call_api(
            resource_path='/v1/resource-manager/domains/{domain_id}/stored-queries/{query_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteStoredQueryResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_schemas_async(self, request):
        """列举高级查询Schema

        List Schemas
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListSchemas
        :type request: :class:`huaweicloudsdkrms.v1.ListSchemasRequest`
        :rtype: :class:`huaweicloudsdkrms.v1.ListSchemasResponse`
        """
        return self.list_schemas_with_http_info(request)

    def list_schemas_with_http_info(self, request):
        all_params = ['limit', 'marker']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['PkiTokenAuth']

        return self.call_api(
            resource_path='/v1/resource-manager/domains/{domain_id}/schemas',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListSchemasResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_stored_queries_async(self, request):
        """列出高级查询

        列举所有高级查询
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListStoredQueries
        :type request: :class:`huaweicloudsdkrms.v1.ListStoredQueriesRequest`
        :rtype: :class:`huaweicloudsdkrms.v1.ListStoredQueriesResponse`
        """
        return self.list_stored_queries_with_http_info(request)

    def list_stored_queries_with_http_info(self, request):
        all_params = ['limit', 'marker', 'name']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
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

        auth_settings = ['PkiTokenAuth']

        return self.call_api(
            resource_path='/v1/resource-manager/domains/{domain_id}/stored-queries',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListStoredQueriesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def run_query_async(self, request):
        """运行高级查询

        执行高级查询
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RunQuery
        :type request: :class:`huaweicloudsdkrms.v1.RunQueryRequest`
        :rtype: :class:`huaweicloudsdkrms.v1.RunQueryResponse`
        """
        return self.run_query_with_http_info(request)

    def run_query_with_http_info(self, request):
        all_params = ['query_run_request_body']
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

        auth_settings = ['PkiTokenAuth']

        return self.call_api(
            resource_path='/v1/resource-manager/domains/{domain_id}/run-query',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RunQueryResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_stored_query_async(self, request):
        """查询单个高级查询

        Show Resource Query Language
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowStoredQuery
        :type request: :class:`huaweicloudsdkrms.v1.ShowStoredQueryRequest`
        :rtype: :class:`huaweicloudsdkrms.v1.ShowStoredQueryResponse`
        """
        return self.show_stored_query_with_http_info(request)

    def show_stored_query_with_http_info(self, request):
        all_params = ['query_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'query_id' in local_var_params:
            path_params['query_id'] = local_var_params['query_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['PkiTokenAuth']

        return self.call_api(
            resource_path='/v1/resource-manager/domains/{domain_id}/stored-queries/{query_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowStoredQueryResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_stored_query_async(self, request):
        """更新单个高级查询

        更新自定义查询
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateStoredQuery
        :type request: :class:`huaweicloudsdkrms.v1.UpdateStoredQueryRequest`
        :rtype: :class:`huaweicloudsdkrms.v1.UpdateStoredQueryResponse`
        """
        return self.update_stored_query_with_http_info(request)

    def update_stored_query_with_http_info(self, request):
        all_params = ['query_id', 'stored_query_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'query_id' in local_var_params:
            path_params['query_id'] = local_var_params['query_id']

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

        auth_settings = ['PkiTokenAuth']

        return self.call_api(
            resource_path='/v1/resource-manager/domains/{domain_id}/stored-queries/{query_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateStoredQueryResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_regions_async(self, request):
        """查询用户可见的区域

        查询用户可见的区域
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListRegions
        :type request: :class:`huaweicloudsdkrms.v1.ListRegionsRequest`
        :rtype: :class:`huaweicloudsdkrms.v1.ListRegionsResponse`
        """
        return self.list_regions_with_http_info(request)

    def list_regions_with_http_info(self, request):
        all_params = ['x_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['PkiTokenAuth']

        return self.call_api(
            resource_path='/v1/resource-manager/domains/{domain_id}/regions',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListRegionsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_resource_relations_async(self, request):
        """列举资源关系

        指定资源ID，查询该资源与其他资源的关联关系，可以指定关系方向为\&quot;in\&quot; 或者\&quot;out\&quot;
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowResourceRelations
        :type request: :class:`huaweicloudsdkrms.v1.ShowResourceRelationsRequest`
        :rtype: :class:`huaweicloudsdkrms.v1.ShowResourceRelationsResponse`
        """
        return self.show_resource_relations_with_http_info(request)

    def show_resource_relations_with_http_info(self, request):
        all_params = ['resource_id', 'direction', 'limit', 'marker']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_id' in local_var_params:
            path_params['resource_id'] = local_var_params['resource_id']

        query_params = []
        if 'direction' in local_var_params:
            query_params.append(('direction', local_var_params['direction']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['PkiTokenAuth']

        return self.call_api(
            resource_path='/v1/resource-manager/domains/{domain_id}/resources/{resource_id}/relations',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowResourceRelationsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_resource_relations_detail_async(self, request):
        """列举资源关系详情

        指定资源ID，查询该资源与其他资源的关联关系，可以指定关系方向为“in”或者“out”，需要当帐号有rms:resources:getRelation权限。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowResourceRelationsDetail
        :type request: :class:`huaweicloudsdkrms.v1.ShowResourceRelationsDetailRequest`
        :rtype: :class:`huaweicloudsdkrms.v1.ShowResourceRelationsDetailResponse`
        """
        return self.show_resource_relations_detail_with_http_info(request)

    def show_resource_relations_detail_with_http_info(self, request):
        all_params = ['resource_id', 'direction', 'limit', 'marker']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_id' in local_var_params:
            path_params['resource_id'] = local_var_params['resource_id']

        query_params = []
        if 'direction' in local_var_params:
            query_params.append(('direction', local_var_params['direction']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['AccessKeyAuth']

        return self.call_api(
            resource_path='/v1/resource-manager/domains/{domain_id}/all-resources/{resource_id}/relations',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowResourceRelationsDetailResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def collect_all_resources_summary_async(self, request):
        """列举资源概要

        查询当前帐号的资源概览。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CollectAllResourcesSummary
        :type request: :class:`huaweicloudsdkrms.v1.CollectAllResourcesSummaryRequest`
        :rtype: :class:`huaweicloudsdkrms.v1.CollectAllResourcesSummaryResponse`
        """
        return self.collect_all_resources_summary_with_http_info(request)

    def collect_all_resources_summary_with_http_info(self, request):
        all_params = ['name', 'type', 'region_id', 'ep_id', 'project_id', 'tags']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
            collection_formats['type'] = 'csv'
        if 'region_id' in local_var_params:
            query_params.append(('region_id', local_var_params['region_id']))
            collection_formats['region_id'] = 'csv'
        if 'ep_id' in local_var_params:
            query_params.append(('ep_id', local_var_params['ep_id']))
            collection_formats['ep_id'] = 'csv'
        if 'project_id' in local_var_params:
            query_params.append(('project_id', local_var_params['project_id']))
            collection_formats['project_id'] = 'csv'
        if 'tags' in local_var_params:
            query_params.append(('tags', local_var_params['tags']))
            collection_formats['tags'] = 'multi'

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['AccessKeyAuth']

        return self.call_api(
            resource_path='/v1/resource-manager/domains/{domain_id}/all-resources/summary',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CollectAllResourcesSummaryResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def count_all_resources_async(self, request):
        """查询资源数量

        查询当前帐号的资源数量。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CountAllResources
        :type request: :class:`huaweicloudsdkrms.v1.CountAllResourcesRequest`
        :rtype: :class:`huaweicloudsdkrms.v1.CountAllResourcesResponse`
        """
        return self.count_all_resources_with_http_info(request)

    def count_all_resources_with_http_info(self, request):
        all_params = ['id', 'name', 'type', 'region_id', 'ep_id', 'project_id', 'tags']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
            collection_formats['type'] = 'csv'
        if 'region_id' in local_var_params:
            query_params.append(('region_id', local_var_params['region_id']))
            collection_formats['region_id'] = 'csv'
        if 'ep_id' in local_var_params:
            query_params.append(('ep_id', local_var_params['ep_id']))
            collection_formats['ep_id'] = 'csv'
        if 'project_id' in local_var_params:
            query_params.append(('project_id', local_var_params['project_id']))
            collection_formats['project_id'] = 'csv'
        if 'tags' in local_var_params:
            query_params.append(('tags', local_var_params['tags']))
            collection_formats['tags'] = 'multi'

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['AccessKeyAuth']

        return self.call_api(
            resource_path='/v1/resource-manager/domains/{domain_id}/all-resources/count',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CountAllResourcesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_all_resources_async(self, request):
        """列举所有资源

        返回当前用户下所有资源，需要当前用户有rms:resources:list权限。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAllResources
        :type request: :class:`huaweicloudsdkrms.v1.ListAllResourcesRequest`
        :rtype: :class:`huaweicloudsdkrms.v1.ListAllResourcesResponse`
        """
        return self.list_all_resources_with_http_info(request)

    def list_all_resources_with_http_info(self, request):
        all_params = ['region_id', 'ep_id', 'type', 'limit', 'marker', 'id', 'name', 'tags']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'region_id' in local_var_params:
            query_params.append(('region_id', local_var_params['region_id']))
        if 'ep_id' in local_var_params:
            query_params.append(('ep_id', local_var_params['ep_id']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'tags' in local_var_params:
            query_params.append(('tags', local_var_params['tags']))
            collection_formats['tags'] = 'multi'

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['PkiTokenAuth']

        return self.call_api(
            resource_path='/v1/resource-manager/domains/{domain_id}/all-resources',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListAllResourcesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_all_tags_async(self, request):
        """列举资源标签

        查询当前帐号下所有资源的标签。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAllTags
        :type request: :class:`huaweicloudsdkrms.v1.ListAllTagsRequest`
        :rtype: :class:`huaweicloudsdkrms.v1.ListAllTagsResponse`
        """
        return self.list_all_tags_with_http_info(request)

    def list_all_tags_with_http_info(self, request):
        all_params = ['key', 'marker', 'limit']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'key' in local_var_params:
            query_params.append(('key', local_var_params['key']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
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

        auth_settings = ['AccessKeyAuth']

        return self.call_api(
            resource_path='/v1/resource-manager/domains/{domain_id}/all-resources/tags',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListAllTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_providers_async(self, request):
        """列举云服务

        查询RMS支持的云服务、资源、区域列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListProviders
        :type request: :class:`huaweicloudsdkrms.v1.ListProvidersRequest`
        :rtype: :class:`huaweicloudsdkrms.v1.ListProvidersResponse`
        """
        return self.list_providers_with_http_info(request)

    def list_providers_with_http_info(self, request):
        all_params = ['offset', 'limit', 'track', 'x_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'track' in local_var_params:
            query_params.append(('track', local_var_params['track']))

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['PkiTokenAuth']

        return self.call_api(
            resource_path='/v1/resource-manager/domains/{domain_id}/providers',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListProvidersResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_resources_async(self, request):
        """列举指定类型的资源

        返回当前租户下特定资源类型的资源，需要当前用户有rms:resources:list权限。比如查询云服务器，对应的RMS资源类型是ecs.cloudservers，其中provider为ecs，type为cloudservers。 RMS支持的服务和资源类型参见[支持的服务和区域](https://console.huaweicloud.com/eps/#/resources/supported)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListResources
        :type request: :class:`huaweicloudsdkrms.v1.ListResourcesRequest`
        :rtype: :class:`huaweicloudsdkrms.v1.ListResourcesResponse`
        """
        return self.list_resources_with_http_info(request)

    def list_resources_with_http_info(self, request):
        all_params = ['provider', 'type', 'region_id', 'ep_id', 'tag', 'limit', 'marker']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'provider' in local_var_params:
            path_params['provider'] = local_var_params['provider']
        if 'type' in local_var_params:
            path_params['type'] = local_var_params['type']

        query_params = []
        if 'region_id' in local_var_params:
            query_params.append(('region_id', local_var_params['region_id']))
        if 'ep_id' in local_var_params:
            query_params.append(('ep_id', local_var_params['ep_id']))
        if 'tag' in local_var_params:
            query_params.append(('tag', local_var_params['tag']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['PkiTokenAuth']

        return self.call_api(
            resource_path='/v1/resource-manager/domains/{domain_id}/provider/{provider}/type/{type}/resources',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListResourcesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_resource_by_id_async(self, request):
        """查询单个资源

        指定资源ID，返回该资源的详细信息，需要当前用户有rms:resources:get权限。比如查询云服务器，对应的RMS资源类型是ecs.cloudservers，其中provider为ecs，type为cloudservers。RMS支持的服务和资源类型参见[支持的服务和区域](https://console.huaweicloud.com/eps/#/resources/supported)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowResourceById
        :type request: :class:`huaweicloudsdkrms.v1.ShowResourceByIdRequest`
        :rtype: :class:`huaweicloudsdkrms.v1.ShowResourceByIdResponse`
        """
        return self.show_resource_by_id_with_http_info(request)

    def show_resource_by_id_with_http_info(self, request):
        all_params = ['provider', 'type', 'resource_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'provider' in local_var_params:
            path_params['provider'] = local_var_params['provider']
        if 'type' in local_var_params:
            path_params['type'] = local_var_params['type']
        if 'resource_id' in local_var_params:
            path_params['resource_id'] = local_var_params['resource_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['PkiTokenAuth']

        return self.call_api(
            resource_path='/v1/resource-manager/domains/{domain_id}/provider/{provider}/type/{type}/resources/{resource_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowResourceByIdResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_resource_detail_async(self, request):
        """查询帐号下的单个资源

        查询当前帐号下的单个资源。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowResourceDetail
        :type request: :class:`huaweicloudsdkrms.v1.ShowResourceDetailRequest`
        :rtype: :class:`huaweicloudsdkrms.v1.ShowResourceDetailResponse`
        """
        return self.show_resource_detail_with_http_info(request)

    def show_resource_detail_with_http_info(self, request):
        all_params = ['resource_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_id' in local_var_params:
            path_params['resource_id'] = local_var_params['resource_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['AccessKeyAuth', 'PkiTokenAuth']

        return self.call_api(
            resource_path='/v1/resource-manager/domains/{domain_id}/all-resources/{resource_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowResourceDetailResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_tracker_config_async(self, request):
        """创建或更新记录器

        创建或更新资源记录器，只能存在一个资源记录器
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateTrackerConfig
        :type request: :class:`huaweicloudsdkrms.v1.CreateTrackerConfigRequest`
        :rtype: :class:`huaweicloudsdkrms.v1.CreateTrackerConfigResponse`
        """
        return self.create_tracker_config_with_http_info(request)

    def create_tracker_config_with_http_info(self, request):
        all_params = ['tracker_config_body']
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

        auth_settings = ['PkiTokenAuth']

        return self.call_api(
            resource_path='/v1/resource-manager/domains/{domain_id}/tracker-config',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateTrackerConfigResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_tracker_config_async(self, request):
        """删除记录器

        删除资源记录器
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteTrackerConfig
        :type request: :class:`huaweicloudsdkrms.v1.DeleteTrackerConfigRequest`
        :rtype: :class:`huaweicloudsdkrms.v1.DeleteTrackerConfigResponse`
        """
        return self.delete_tracker_config_with_http_info(request)

    def delete_tracker_config_with_http_info(self, request):
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

        auth_settings = ['PkiTokenAuth']

        return self.call_api(
            resource_path='/v1/resource-manager/domains/{domain_id}/tracker-config',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteTrackerConfigResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_tracker_config_async(self, request):
        """查询记录器

        查询资源记录器的详细信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowTrackerConfig
        :type request: :class:`huaweicloudsdkrms.v1.ShowTrackerConfigRequest`
        :rtype: :class:`huaweicloudsdkrms.v1.ShowTrackerConfigResponse`
        """
        return self.show_tracker_config_with_http_info(request)

    def show_tracker_config_with_http_info(self, request):
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

        auth_settings = ['PkiTokenAuth']

        return self.call_api(
            resource_path='/v1/resource-manager/domains/{domain_id}/tracker-config',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowTrackerConfigResponse',
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

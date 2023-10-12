# coding: utf-8

from __future__ import absolute_import

import importlib

from huaweicloudsdkcore.client import Client, ClientBuilder
from huaweicloudsdkcore.utils import http_utils
from huaweicloudsdkcore.sdk_stream_request import SdkStreamRequest


class ConfigAsyncClient(Client):
    def __init__(self):
        super(ConfigAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkconfig.v1.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if clazz is None:
            return ClientBuilder(cls, "GlobalCredentials")

        if clazz.__name__ != "ConfigClient":
            raise TypeError("client type error, support client type is ConfigClient")

        return ClientBuilder(clazz, "GlobalCredentials")

    def create_aggregation_authorization_async(self, request):
        """创建资源聚合器授权

        给资源聚合器帐号授予从源帐号收集数据的权限。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateAggregationAuthorization
        :type request: :class:`huaweicloudsdkconfig.v1.CreateAggregationAuthorizationRequest`
        :rtype: :class:`huaweicloudsdkconfig.v1.CreateAggregationAuthorizationResponse`
        """
        return self._create_aggregation_authorization_with_http_info(request)

    def _create_aggregation_authorization_with_http_info(self, request):
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
        :type request: :class:`huaweicloudsdkconfig.v1.CreateConfigurationAggregatorRequest`
        :rtype: :class:`huaweicloudsdkconfig.v1.CreateConfigurationAggregatorResponse`
        """
        return self._create_configuration_aggregator_with_http_info(request)

    def _create_configuration_aggregator_with_http_info(self, request):
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
        :type request: :class:`huaweicloudsdkconfig.v1.DeleteAggregationAuthorizationRequest`
        :rtype: :class:`huaweicloudsdkconfig.v1.DeleteAggregationAuthorizationResponse`
        """
        return self._delete_aggregation_authorization_with_http_info(request)

    def _delete_aggregation_authorization_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
        :type request: :class:`huaweicloudsdkconfig.v1.DeleteConfigurationAggregatorRequest`
        :rtype: :class:`huaweicloudsdkconfig.v1.DeleteConfigurationAggregatorResponse`
        """
        return self._delete_configuration_aggregator_with_http_info(request)

    def _delete_configuration_aggregator_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
        :type request: :class:`huaweicloudsdkconfig.v1.DeletePendingAggregationRequestRequest`
        :rtype: :class:`huaweicloudsdkconfig.v1.DeletePendingAggregationRequestResponse`
        """
        return self._delete_pending_aggregation_request_with_http_info(request)

    def _delete_pending_aggregation_request_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def list_aggregate_compliance_by_policy_assignment_async(self, request):
        """查询聚合合规规则列表

        查询合规和不合规规则的列表，其中包含合规和不合规规则的资源数量。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAggregateComplianceByPolicyAssignment
        :type request: :class:`huaweicloudsdkconfig.v1.ListAggregateComplianceByPolicyAssignmentRequest`
        :rtype: :class:`huaweicloudsdkconfig.v1.ListAggregateComplianceByPolicyAssignmentResponse`
        """
        return self._list_aggregate_compliance_by_policy_assignment_with_http_info(request)

    def _list_aggregate_compliance_by_policy_assignment_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
            resource_path='/v1/resource-manager/domains/{domain_id}/aggregators/aggregate-data/policy-assignments/compliance',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListAggregateComplianceByPolicyAssignmentResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_aggregate_discovered_resources_async(self, request):
        """查询聚合器中资源的列表

        查询资源聚合器中特定资源的列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAggregateDiscoveredResources
        :type request: :class:`huaweicloudsdkconfig.v1.ListAggregateDiscoveredResourcesRequest`
        :rtype: :class:`huaweicloudsdkconfig.v1.ListAggregateDiscoveredResourcesResponse`
        """
        return self._list_aggregate_discovered_resources_with_http_info(request)

    def _list_aggregate_discovered_resources_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
        :type request: :class:`huaweicloudsdkconfig.v1.ListAggregationAuthorizationsRequest`
        :rtype: :class:`huaweicloudsdkconfig.v1.ListAggregationAuthorizationsResponse`
        """
        return self._list_aggregation_authorizations_with_http_info(request)

    def _list_aggregation_authorizations_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
        :type request: :class:`huaweicloudsdkconfig.v1.ListConfigurationAggregatorsRequest`
        :rtype: :class:`huaweicloudsdkconfig.v1.ListConfigurationAggregatorsResponse`
        """
        return self._list_configuration_aggregators_with_http_info(request)

    def _list_configuration_aggregators_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
        :type request: :class:`huaweicloudsdkconfig.v1.ListPendingAggregationRequestsRequest`
        :rtype: :class:`huaweicloudsdkconfig.v1.ListPendingAggregationRequestsResponse`
        """
        return self._list_pending_aggregation_requests_with_http_info(request)

    def _list_pending_aggregation_requests_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
        :type request: :class:`huaweicloudsdkconfig.v1.RunAggregateResourceQueryRequest`
        :rtype: :class:`huaweicloudsdkconfig.v1.RunAggregateResourceQueryResponse`
        """
        return self._run_aggregate_resource_query_with_http_info(request)

    def _run_aggregate_resource_query_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def show_aggregate_compliance_details_by_policy_assignment_async(self, request):
        """查询指定聚合合规规则的评估结果详情

        返回指定聚合合规规则的评估结果详情。包含评估了哪些资源，以及每个资源是否符合规则。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowAggregateComplianceDetailsByPolicyAssignment
        :type request: :class:`huaweicloudsdkconfig.v1.ShowAggregateComplianceDetailsByPolicyAssignmentRequest`
        :rtype: :class:`huaweicloudsdkconfig.v1.ShowAggregateComplianceDetailsByPolicyAssignmentResponse`
        """
        return self._show_aggregate_compliance_details_by_policy_assignment_with_http_info(request)

    def _show_aggregate_compliance_details_by_policy_assignment_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
            resource_path='/v1/resource-manager/domains/{domain_id}/aggregators/aggregate-data/policy-states/compliance-details',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowAggregateComplianceDetailsByPolicyAssignmentResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_aggregate_discovered_resource_counts_async(self, request):
        """查询聚合器中帐号资源的计数

        查询聚合器中帐号资源的计数，支持通过过滤器和GroupByKey来统计资源数量。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowAggregateDiscoveredResourceCounts
        :type request: :class:`huaweicloudsdkconfig.v1.ShowAggregateDiscoveredResourceCountsRequest`
        :rtype: :class:`huaweicloudsdkconfig.v1.ShowAggregateDiscoveredResourceCountsResponse`
        """
        return self._show_aggregate_discovered_resource_counts_with_http_info(request)

    def _show_aggregate_discovered_resource_counts_with_http_info(self, request):
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

    def show_aggregate_policy_assignment_detail_async(self, request):
        """查询指定聚合合规规则详情

        返回指定聚合合规规则详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowAggregatePolicyAssignmentDetail
        :type request: :class:`huaweicloudsdkconfig.v1.ShowAggregatePolicyAssignmentDetailRequest`
        :rtype: :class:`huaweicloudsdkconfig.v1.ShowAggregatePolicyAssignmentDetailResponse`
        """
        return self._show_aggregate_policy_assignment_detail_with_http_info(request)

    def _show_aggregate_policy_assignment_detail_with_http_info(self, request):
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

        auth_settings = ['AccessKeyAuth']

        return self.call_api(
            resource_path='/v1/resource-manager/domains/{domain_id}/aggregators/aggregate-data/policy-assignment/detail',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowAggregatePolicyAssignmentDetailResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_aggregate_policy_state_compliance_summary_async(self, request):
        """查询聚合器中一个或多个帐户的合规概况

        查询聚合器中一个或多个帐户的合规和不合规规则数。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowAggregatePolicyStateComplianceSummary
        :type request: :class:`huaweicloudsdkconfig.v1.ShowAggregatePolicyStateComplianceSummaryRequest`
        :rtype: :class:`huaweicloudsdkconfig.v1.ShowAggregatePolicyStateComplianceSummaryResponse`
        """
        return self._show_aggregate_policy_state_compliance_summary_with_http_info(request)

    def _show_aggregate_policy_state_compliance_summary_with_http_info(self, request):
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

        auth_settings = ['AccessKeyAuth']

        return self.call_api(
            resource_path='/v1/resource-manager/domains/{domain_id}/aggregators/aggregate-data/policy-states/compliance-summary',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowAggregatePolicyStateComplianceSummaryResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_aggregate_resource_config_async(self, request):
        """查询源帐号中资源的详情

        查询源帐号中特定资源的详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowAggregateResourceConfig
        :type request: :class:`huaweicloudsdkconfig.v1.ShowAggregateResourceConfigRequest`
        :rtype: :class:`huaweicloudsdkconfig.v1.ShowAggregateResourceConfigResponse`
        """
        return self._show_aggregate_resource_config_with_http_info(request)

    def _show_aggregate_resource_config_with_http_info(self, request):
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
        :type request: :class:`huaweicloudsdkconfig.v1.ShowConfigurationAggregatorRequest`
        :rtype: :class:`huaweicloudsdkconfig.v1.ShowConfigurationAggregatorResponse`
        """
        return self._show_configuration_aggregator_with_http_info(request)

    def _show_configuration_aggregator_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
        :type request: :class:`huaweicloudsdkconfig.v1.ShowConfigurationAggregatorSourcesStatusRequest`
        :rtype: :class:`huaweicloudsdkconfig.v1.ShowConfigurationAggregatorSourcesStatusResponse`
        """
        return self._show_configuration_aggregator_sources_status_with_http_info(request)

    def _show_configuration_aggregator_sources_status_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
        :type request: :class:`huaweicloudsdkconfig.v1.UpdateConfigurationAggregatorRequest`
        :rtype: :class:`huaweicloudsdkconfig.v1.UpdateConfigurationAggregatorResponse`
        """
        return self._update_configuration_aggregator_with_http_info(request)

    def _update_configuration_aggregator_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def collect_conformance_pack_compliance_summary_async(self, request):
        """列举合规规则包的结果概览

        列举用户的合规规则包的合规结果概览。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CollectConformancePackComplianceSummary
        :type request: :class:`huaweicloudsdkconfig.v1.CollectConformancePackComplianceSummaryRequest`
        :rtype: :class:`huaweicloudsdkconfig.v1.CollectConformancePackComplianceSummaryResponse`
        """
        return self._collect_conformance_pack_compliance_summary_with_http_info(request)

    def _collect_conformance_pack_compliance_summary_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'conformance_pack_name' in local_var_params:
            query_params.append(('conformance_pack_name', local_var_params['conformance_pack_name']))

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
            resource_path='/v1/resource-manager/domains/{domain_id}/conformance-packs/compliance/summary',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CollectConformancePackComplianceSummaryResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_conformance_pack_async(self, request):
        """创建合规规则包

        创建新的合规规则包。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateConformancePack
        :type request: :class:`huaweicloudsdkconfig.v1.CreateConformancePackRequest`
        :rtype: :class:`huaweicloudsdkconfig.v1.CreateConformancePackResponse`
        """
        return self._create_conformance_pack_with_http_info(request)

    def _create_conformance_pack_with_http_info(self, request):
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
            resource_path='/v1/resource-manager/domains/{domain_id}/conformance-packs',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateConformancePackResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_organization_conformance_pack_async(self, request):
        """创建组织合规规则包

        创建新的组织合规规则包。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateOrganizationConformancePack
        :type request: :class:`huaweicloudsdkconfig.v1.CreateOrganizationConformancePackRequest`
        :rtype: :class:`huaweicloudsdkconfig.v1.CreateOrganizationConformancePackResponse`
        """
        return self._create_organization_conformance_pack_with_http_info(request)

    def _create_organization_conformance_pack_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

        auth_settings = []

        return self.call_api(
            resource_path='/v1/resource-manager/organizations/{organization_id}/conformance-packs',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateOrganizationConformancePackResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_conformance_pack_async(self, request):
        """删除合规规则包

        删除用户的合规规则包。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteConformancePack
        :type request: :class:`huaweicloudsdkconfig.v1.DeleteConformancePackRequest`
        :rtype: :class:`huaweicloudsdkconfig.v1.DeleteConformancePackResponse`
        """
        return self._delete_conformance_pack_with_http_info(request)

    def _delete_conformance_pack_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'conformance_pack_id' in local_var_params:
            path_params['conformance_pack_id'] = local_var_params['conformance_pack_id']

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
            resource_path='/v1/resource-manager/domains/{domain_id}/conformance-packs/{conformance_pack_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteConformancePackResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_organization_conformance_pack_async(self, request):
        """删除组织合规规则包

        删除用户的组织合规规则包。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteOrganizationConformancePack
        :type request: :class:`huaweicloudsdkconfig.v1.DeleteOrganizationConformancePackRequest`
        :rtype: :class:`huaweicloudsdkconfig.v1.DeleteOrganizationConformancePackResponse`
        """
        return self._delete_organization_conformance_pack_with_http_info(request)

    def _delete_organization_conformance_pack_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'organization_id' in local_var_params:
            path_params['organization_id'] = local_var_params['organization_id']
        if 'conformance_pack_id' in local_var_params:
            path_params['conformance_pack_id'] = local_var_params['conformance_pack_id']

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
            resource_path='/v1/resource-manager/organizations/{organization_id}/conformance-packs/{conformance_pack_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteOrganizationConformancePackResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_built_in_conformance_pack_templates_async(self, request):
        """列举预定义合规规则包模板

        列举预定义的合规规则包的模板。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListBuiltInConformancePackTemplates
        :type request: :class:`huaweicloudsdkconfig.v1.ListBuiltInConformancePackTemplatesRequest`
        :rtype: :class:`huaweicloudsdkconfig.v1.ListBuiltInConformancePackTemplatesResponse`
        """
        return self._list_built_in_conformance_pack_templates_with_http_info(request)

    def _list_built_in_conformance_pack_templates_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'template_key' in local_var_params:
            query_params.append(('template_key', local_var_params['template_key']))

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

        auth_settings = []

        return self.call_api(
            resource_path='/v1/resource-manager/conformance-packs/templates',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListBuiltInConformancePackTemplatesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_conformance_pack_compliance_by_pack_id_async(self, request):
        """列举合规规则包的评估结果

        列举合规规则包的合规规则评估结果。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListConformancePackComplianceByPackId
        :type request: :class:`huaweicloudsdkconfig.v1.ListConformancePackComplianceByPackIdRequest`
        :rtype: :class:`huaweicloudsdkconfig.v1.ListConformancePackComplianceByPackIdResponse`
        """
        return self._list_conformance_pack_compliance_by_pack_id_with_http_info(request)

    def _list_conformance_pack_compliance_by_pack_id_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'conformance_pack_id' in local_var_params:
            path_params['conformance_pack_id'] = local_var_params['conformance_pack_id']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'policy_assignment_name' in local_var_params:
            query_params.append(('policy_assignment_name', local_var_params['policy_assignment_name']))

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
            resource_path='/v1/resource-manager/domains/{domain_id}/conformance-packs/{conformance_pack_id}/compliance',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListConformancePackComplianceByPackIdResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_conformance_pack_compliance_details_by_pack_id_async(self, request):
        """列举合规规则包的评估结果详情

        列举合规规则包的合规规则评估结果详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListConformancePackComplianceDetailsByPackId
        :type request: :class:`huaweicloudsdkconfig.v1.ListConformancePackComplianceDetailsByPackIdRequest`
        :rtype: :class:`huaweicloudsdkconfig.v1.ListConformancePackComplianceDetailsByPackIdResponse`
        """
        return self._list_conformance_pack_compliance_details_by_pack_id_with_http_info(request)

    def _list_conformance_pack_compliance_details_by_pack_id_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'conformance_pack_id' in local_var_params:
            path_params['conformance_pack_id'] = local_var_params['conformance_pack_id']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'policy_assignment_name' in local_var_params:
            query_params.append(('policy_assignment_name', local_var_params['policy_assignment_name']))

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
            resource_path='/v1/resource-manager/domains/{domain_id}/conformance-packs/{conformance_pack_id}/compliance/details',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListConformancePackComplianceDetailsByPackIdResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_conformance_pack_compliance_scores_async(self, request):
        """列举合规规则包分数

        列举用户的合规规则包分数。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListConformancePackComplianceScores
        :type request: :class:`huaweicloudsdkconfig.v1.ListConformancePackComplianceScoresRequest`
        :rtype: :class:`huaweicloudsdkconfig.v1.ListConformancePackComplianceScoresResponse`
        """
        return self._list_conformance_pack_compliance_scores_with_http_info(request)

    def _list_conformance_pack_compliance_scores_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'conformance_pack_name' in local_var_params:
            query_params.append(('conformance_pack_name', local_var_params['conformance_pack_name']))

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
            resource_path='/v1/resource-manager/domains/{domain_id}/conformance-packs/scores',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListConformancePackComplianceScoresResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_conformance_packs_async(self, request):
        """列举合规规则包

        列举用户的合规规则包。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListConformancePacks
        :type request: :class:`huaweicloudsdkconfig.v1.ListConformancePacksRequest`
        :rtype: :class:`huaweicloudsdkconfig.v1.ListConformancePacksResponse`
        """
        return self._list_conformance_packs_with_http_info(request)

    def _list_conformance_packs_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'conformance_pack_name' in local_var_params:
            query_params.append(('conformance_pack_name', local_var_params['conformance_pack_name']))

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
            resource_path='/v1/resource-manager/domains/{domain_id}/conformance-packs',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListConformancePacksResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_organization_conformance_pack_statuses_async(self, request):
        """查看组织合规规则包部署状态

        列举用户的组织合规规则包部署状态。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListOrganizationConformancePackStatuses
        :type request: :class:`huaweicloudsdkconfig.v1.ListOrganizationConformancePackStatusesRequest`
        :rtype: :class:`huaweicloudsdkconfig.v1.ListOrganizationConformancePackStatusesResponse`
        """
        return self._list_organization_conformance_pack_statuses_with_http_info(request)

    def _list_organization_conformance_pack_statuses_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'organization_id' in local_var_params:
            path_params['organization_id'] = local_var_params['organization_id']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'conformance_pack_name' in local_var_params:
            query_params.append(('conformance_pack_name', local_var_params['conformance_pack_name']))

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
            resource_path='/v1/resource-manager/organizations/{organization_id}/conformance-packs/statuses',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListOrganizationConformancePackStatusesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_organization_conformance_packs_async(self, request):
        """列举组织合规规则包

        列举用户的组织合规规则包。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListOrganizationConformancePacks
        :type request: :class:`huaweicloudsdkconfig.v1.ListOrganizationConformancePacksRequest`
        :rtype: :class:`huaweicloudsdkconfig.v1.ListOrganizationConformancePacksResponse`
        """
        return self._list_organization_conformance_packs_with_http_info(request)

    def _list_organization_conformance_packs_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'organization_id' in local_var_params:
            path_params['organization_id'] = local_var_params['organization_id']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'conformance_pack_name' in local_var_params:
            query_params.append(('conformance_pack_name', local_var_params['conformance_pack_name']))

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
            resource_path='/v1/resource-manager/organizations/{organization_id}/conformance-packs',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListOrganizationConformancePacksResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_built_in_conformance_pack_template_async(self, request):
        """查看预定义合规规则包模板

        根据ID获取单个预定义合规规则包模板。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowBuiltInConformancePackTemplate
        :type request: :class:`huaweicloudsdkconfig.v1.ShowBuiltInConformancePackTemplateRequest`
        :rtype: :class:`huaweicloudsdkconfig.v1.ShowBuiltInConformancePackTemplateResponse`
        """
        return self._show_built_in_conformance_pack_template_with_http_info(request)

    def _show_built_in_conformance_pack_template_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'template_id' in local_var_params:
            path_params['template_id'] = local_var_params['template_id']

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

        auth_settings = []

        return self.call_api(
            resource_path='/v1/resource-manager/conformance-packs/templates/{template_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowBuiltInConformancePackTemplateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_conformance_pack_async(self, request):
        """查看合规规则包

        根据ID获取单个合规规则包。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowConformancePack
        :type request: :class:`huaweicloudsdkconfig.v1.ShowConformancePackRequest`
        :rtype: :class:`huaweicloudsdkconfig.v1.ShowConformancePackResponse`
        """
        return self._show_conformance_pack_with_http_info(request)

    def _show_conformance_pack_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'conformance_pack_id' in local_var_params:
            path_params['conformance_pack_id'] = local_var_params['conformance_pack_id']

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
            resource_path='/v1/resource-manager/domains/{domain_id}/conformance-packs/{conformance_pack_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowConformancePackResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_organization_conformance_pack_async(self, request):
        """查看组织合规规则包

        根据ID获取单个组织合规规则包详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowOrganizationConformancePack
        :type request: :class:`huaweicloudsdkconfig.v1.ShowOrganizationConformancePackRequest`
        :rtype: :class:`huaweicloudsdkconfig.v1.ShowOrganizationConformancePackResponse`
        """
        return self._show_organization_conformance_pack_with_http_info(request)

    def _show_organization_conformance_pack_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'organization_id' in local_var_params:
            path_params['organization_id'] = local_var_params['organization_id']
        if 'conformance_pack_id' in local_var_params:
            path_params['conformance_pack_id'] = local_var_params['conformance_pack_id']

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
            resource_path='/v1/resource-manager/organizations/{organization_id}/conformance-packs/{conformance_pack_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowOrganizationConformancePackResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_organization_conformance_pack_detailed_statuses_async(self, request):
        """查看组织合规规则包部署详细状态

        查看指定组织合规规则包在成员账户中的部署状态详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowOrganizationConformancePackDetailedStatuses
        :type request: :class:`huaweicloudsdkconfig.v1.ShowOrganizationConformancePackDetailedStatusesRequest`
        :rtype: :class:`huaweicloudsdkconfig.v1.ShowOrganizationConformancePackDetailedStatusesResponse`
        """
        return self._show_organization_conformance_pack_detailed_statuses_with_http_info(request)

    def _show_organization_conformance_pack_detailed_statuses_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'organization_id' in local_var_params:
            path_params['organization_id'] = local_var_params['organization_id']

        query_params = []
        if 'conformance_pack_name' in local_var_params:
            query_params.append(('conformance_pack_name', local_var_params['conformance_pack_name']))
        if 'state' in local_var_params:
            query_params.append(('state', local_var_params['state']))
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

        auth_settings = []

        return self.call_api(
            resource_path='/v1/resource-manager/organizations/{organization_id}/conformance-packs/detailed-statuses',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowOrganizationConformancePackDetailedStatusesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_resource_history_async(self, request):
        """查询资源历史

        查询资源与资源关系的变更历史
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowResourceHistory
        :type request: :class:`huaweicloudsdkconfig.v1.ShowResourceHistoryRequest`
        :rtype: :class:`huaweicloudsdkconfig.v1.ShowResourceHistoryResponse`
        """
        return self._show_resource_history_with_http_info(request)

    def _show_resource_history_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
        :type request: :class:`huaweicloudsdkconfig.v1.CreateOrganizationPolicyAssignmentRequest`
        :rtype: :class:`huaweicloudsdkconfig.v1.CreateOrganizationPolicyAssignmentResponse`
        """
        return self._create_organization_policy_assignment_with_http_info(request)

    def _create_organization_policy_assignment_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
        :type request: :class:`huaweicloudsdkconfig.v1.CreatePolicyAssignmentsRequest`
        :rtype: :class:`huaweicloudsdkconfig.v1.CreatePolicyAssignmentsResponse`
        """
        return self._create_policy_assignments_with_http_info(request)

    def _create_policy_assignments_with_http_info(self, request):
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
        :type request: :class:`huaweicloudsdkconfig.v1.DeleteOrganizationPolicyAssignmentRequest`
        :rtype: :class:`huaweicloudsdkconfig.v1.DeleteOrganizationPolicyAssignmentResponse`
        """
        return self._delete_organization_policy_assignment_with_http_info(request)

    def _delete_organization_policy_assignment_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
        :type request: :class:`huaweicloudsdkconfig.v1.DeletePolicyAssignmentRequest`
        :rtype: :class:`huaweicloudsdkconfig.v1.DeletePolicyAssignmentResponse`
        """
        return self._delete_policy_assignment_with_http_info(request)

    def _delete_policy_assignment_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
        :type request: :class:`huaweicloudsdkconfig.v1.DisablePolicyAssignmentRequest`
        :rtype: :class:`huaweicloudsdkconfig.v1.DisablePolicyAssignmentResponse`
        """
        return self._disable_policy_assignment_with_http_info(request)

    def _disable_policy_assignment_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
        :type request: :class:`huaweicloudsdkconfig.v1.EnablePolicyAssignmentRequest`
        :rtype: :class:`huaweicloudsdkconfig.v1.EnablePolicyAssignmentResponse`
        """
        return self._enable_policy_assignment_with_http_info(request)

    def _enable_policy_assignment_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
        :type request: :class:`huaweicloudsdkconfig.v1.ListBuiltInPolicyDefinitionsRequest`
        :rtype: :class:`huaweicloudsdkconfig.v1.ListBuiltInPolicyDefinitionsResponse`
        """
        return self._list_built_in_policy_definitions_with_http_info(request)

    def _list_built_in_policy_definitions_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
        :type request: :class:`huaweicloudsdkconfig.v1.ListOrganizationPolicyAssignmentsRequest`
        :rtype: :class:`huaweicloudsdkconfig.v1.ListOrganizationPolicyAssignmentsResponse`
        """
        return self._list_organization_policy_assignments_with_http_info(request)

    def _list_organization_policy_assignments_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
        :type request: :class:`huaweicloudsdkconfig.v1.ListPolicyAssignmentsRequest`
        :rtype: :class:`huaweicloudsdkconfig.v1.ListPolicyAssignmentsResponse`
        """
        return self._list_policy_assignments_with_http_info(request)

    def _list_policy_assignments_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
        :type request: :class:`huaweicloudsdkconfig.v1.ListPolicyStatesByAssignmentIdRequest`
        :rtype: :class:`huaweicloudsdkconfig.v1.ListPolicyStatesByAssignmentIdResponse`
        """
        return self._list_policy_states_by_assignment_id_with_http_info(request)

    def _list_policy_states_by_assignment_id_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
        :type request: :class:`huaweicloudsdkconfig.v1.ListPolicyStatesByDomainIdRequest`
        :rtype: :class:`huaweicloudsdkconfig.v1.ListPolicyStatesByDomainIdResponse`
        """
        return self._list_policy_states_by_domain_id_with_http_info(request)

    def _list_policy_states_by_domain_id_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
        :type request: :class:`huaweicloudsdkconfig.v1.ListPolicyStatesByResourceIdRequest`
        :rtype: :class:`huaweicloudsdkconfig.v1.ListPolicyStatesByResourceIdResponse`
        """
        return self._list_policy_states_by_resource_id_with_http_info(request)

    def _list_policy_states_by_resource_id_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
        :type request: :class:`huaweicloudsdkconfig.v1.RunEvaluationByPolicyAssignmentIdRequest`
        :rtype: :class:`huaweicloudsdkconfig.v1.RunEvaluationByPolicyAssignmentIdResponse`
        """
        return self._run_evaluation_by_policy_assignment_id_with_http_info(request)

    def _run_evaluation_by_policy_assignment_id_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
        :type request: :class:`huaweicloudsdkconfig.v1.ShowBuiltInPolicyDefinitionRequest`
        :rtype: :class:`huaweicloudsdkconfig.v1.ShowBuiltInPolicyDefinitionResponse`
        """
        return self._show_built_in_policy_definition_with_http_info(request)

    def _show_built_in_policy_definition_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
        :type request: :class:`huaweicloudsdkconfig.v1.ShowEvaluationStateByAssignmentIdRequest`
        :rtype: :class:`huaweicloudsdkconfig.v1.ShowEvaluationStateByAssignmentIdResponse`
        """
        return self._show_evaluation_state_by_assignment_id_with_http_info(request)

    def _show_evaluation_state_by_assignment_id_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
        :type request: :class:`huaweicloudsdkconfig.v1.ShowOrganizationPolicyAssignmentRequest`
        :rtype: :class:`huaweicloudsdkconfig.v1.ShowOrganizationPolicyAssignmentResponse`
        """
        return self._show_organization_policy_assignment_with_http_info(request)

    def _show_organization_policy_assignment_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
        :type request: :class:`huaweicloudsdkconfig.v1.ShowOrganizationPolicyAssignmentDetailedStatusRequest`
        :rtype: :class:`huaweicloudsdkconfig.v1.ShowOrganizationPolicyAssignmentDetailedStatusResponse`
        """
        return self._show_organization_policy_assignment_detailed_status_with_http_info(request)

    def _show_organization_policy_assignment_detailed_status_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
        :type request: :class:`huaweicloudsdkconfig.v1.ShowOrganizationPolicyAssignmentStatusesRequest`
        :rtype: :class:`huaweicloudsdkconfig.v1.ShowOrganizationPolicyAssignmentStatusesResponse`
        """
        return self._show_organization_policy_assignment_statuses_with_http_info(request)

    def _show_organization_policy_assignment_statuses_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
        :type request: :class:`huaweicloudsdkconfig.v1.ShowPolicyAssignmentRequest`
        :rtype: :class:`huaweicloudsdkconfig.v1.ShowPolicyAssignmentResponse`
        """
        return self._show_policy_assignment_with_http_info(request)

    def _show_policy_assignment_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
        :type request: :class:`huaweicloudsdkconfig.v1.UpdatePolicyAssignmentRequest`
        :rtype: :class:`huaweicloudsdkconfig.v1.UpdatePolicyAssignmentResponse`
        """
        return self._update_policy_assignment_with_http_info(request)

    def _update_policy_assignment_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
        :type request: :class:`huaweicloudsdkconfig.v1.UpdatePolicyStateRequest`
        :rtype: :class:`huaweicloudsdkconfig.v1.UpdatePolicyStateResponse`
        """
        return self._update_policy_state_with_http_info(request)

    def _update_policy_state_with_http_info(self, request):
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
        :type request: :class:`huaweicloudsdkconfig.v1.CreateStoredQueryRequest`
        :rtype: :class:`huaweicloudsdkconfig.v1.CreateStoredQueryResponse`
        """
        return self._create_stored_query_with_http_info(request)

    def _create_stored_query_with_http_info(self, request):
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
        :type request: :class:`huaweicloudsdkconfig.v1.DeleteStoredQueryRequest`
        :rtype: :class:`huaweicloudsdkconfig.v1.DeleteStoredQueryResponse`
        """
        return self._delete_stored_query_with_http_info(request)

    def _delete_stored_query_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
        :type request: :class:`huaweicloudsdkconfig.v1.ListSchemasRequest`
        :rtype: :class:`huaweicloudsdkconfig.v1.ListSchemasResponse`
        """
        return self._list_schemas_with_http_info(request)

    def _list_schemas_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
        :type request: :class:`huaweicloudsdkconfig.v1.ListStoredQueriesRequest`
        :rtype: :class:`huaweicloudsdkconfig.v1.ListStoredQueriesResponse`
        """
        return self._list_stored_queries_with_http_info(request)

    def _list_stored_queries_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
        :type request: :class:`huaweicloudsdkconfig.v1.RunQueryRequest`
        :rtype: :class:`huaweicloudsdkconfig.v1.RunQueryResponse`
        """
        return self._run_query_with_http_info(request)

    def _run_query_with_http_info(self, request):
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
        :type request: :class:`huaweicloudsdkconfig.v1.ShowStoredQueryRequest`
        :rtype: :class:`huaweicloudsdkconfig.v1.ShowStoredQueryResponse`
        """
        return self._show_stored_query_with_http_info(request)

    def _show_stored_query_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
        :type request: :class:`huaweicloudsdkconfig.v1.UpdateStoredQueryRequest`
        :rtype: :class:`huaweicloudsdkconfig.v1.UpdateStoredQueryResponse`
        """
        return self._update_stored_query_with_http_info(request)

    def _update_stored_query_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
        :type request: :class:`huaweicloudsdkconfig.v1.ListRegionsRequest`
        :rtype: :class:`huaweicloudsdkconfig.v1.ListRegionsResponse`
        """
        return self._list_regions_with_http_info(request)

    def _list_regions_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
        :type request: :class:`huaweicloudsdkconfig.v1.ShowResourceRelationsRequest`
        :rtype: :class:`huaweicloudsdkconfig.v1.ShowResourceRelationsResponse`
        """
        return self._show_resource_relations_with_http_info(request)

    def _show_resource_relations_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
        :type request: :class:`huaweicloudsdkconfig.v1.ShowResourceRelationsDetailRequest`
        :rtype: :class:`huaweicloudsdkconfig.v1.ShowResourceRelationsDetailResponse`
        """
        return self._show_resource_relations_detail_with_http_info(request)

    def _show_resource_relations_detail_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
        :type request: :class:`huaweicloudsdkconfig.v1.CollectAllResourcesSummaryRequest`
        :rtype: :class:`huaweicloudsdkconfig.v1.CollectAllResourcesSummaryResponse`
        """
        return self._collect_all_resources_summary_with_http_info(request)

    def _collect_all_resources_summary_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
        :type request: :class:`huaweicloudsdkconfig.v1.CountAllResourcesRequest`
        :rtype: :class:`huaweicloudsdkconfig.v1.CountAllResourcesResponse`
        """
        return self._count_all_resources_with_http_info(request)

    def _count_all_resources_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
        :type request: :class:`huaweicloudsdkconfig.v1.ListAllResourcesRequest`
        :rtype: :class:`huaweicloudsdkconfig.v1.ListAllResourcesResponse`
        """
        return self._list_all_resources_with_http_info(request)

    def _list_all_resources_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
        :type request: :class:`huaweicloudsdkconfig.v1.ListAllTagsRequest`
        :rtype: :class:`huaweicloudsdkconfig.v1.ListAllTagsResponse`
        """
        return self._list_all_tags_with_http_info(request)

    def _list_all_tags_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

        查询Config支持的云服务、资源、区域列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListProviders
        :type request: :class:`huaweicloudsdkconfig.v1.ListProvidersRequest`
        :rtype: :class:`huaweicloudsdkconfig.v1.ListProvidersResponse`
        """
        return self._list_providers_with_http_info(request)

    def _list_providers_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

        返回当前租户下特定资源类型的资源，需要当前用户有rms:resources:list权限。比如查询云服务器，对应的Config资源类型是ecs.cloudservers，其中provider为ecs，type为cloudservers。 Config支持的服务和资源类型参见[支持的服务和区域](https://console.huaweicloud.com/eps/#/resources/supported)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListResources
        :type request: :class:`huaweicloudsdkconfig.v1.ListResourcesRequest`
        :rtype: :class:`huaweicloudsdkconfig.v1.ListResourcesResponse`
        """
        return self._list_resources_with_http_info(request)

    def _list_resources_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

        指定资源ID，返回该资源的详细信息，需要当前用户有rms:resources:get权限。比如查询云服务器，对应的Config资源类型是ecs.cloudservers，其中provider为ecs，type为cloudservers。Config支持的服务和资源类型参见[支持的服务和区域](https://console.huaweicloud.com/eps/#/resources/supported)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowResourceById
        :type request: :class:`huaweicloudsdkconfig.v1.ShowResourceByIdRequest`
        :rtype: :class:`huaweicloudsdkconfig.v1.ShowResourceByIdResponse`
        """
        return self._show_resource_by_id_with_http_info(request)

    def _show_resource_by_id_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
        :type request: :class:`huaweicloudsdkconfig.v1.ShowResourceDetailRequest`
        :rtype: :class:`huaweicloudsdkconfig.v1.ShowResourceDetailResponse`
        """
        return self._show_resource_detail_with_http_info(request)

    def _show_resource_detail_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
        :type request: :class:`huaweicloudsdkconfig.v1.CreateTrackerConfigRequest`
        :rtype: :class:`huaweicloudsdkconfig.v1.CreateTrackerConfigResponse`
        """
        return self._create_tracker_config_with_http_info(request)

    def _create_tracker_config_with_http_info(self, request):
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
        :type request: :class:`huaweicloudsdkconfig.v1.DeleteTrackerConfigRequest`
        :rtype: :class:`huaweicloudsdkconfig.v1.DeleteTrackerConfigResponse`
        """
        return self._delete_tracker_config_with_http_info(request)

    def _delete_tracker_config_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
        :type request: :class:`huaweicloudsdkconfig.v1.ShowTrackerConfigRequest`
        :rtype: :class:`huaweicloudsdkconfig.v1.ShowTrackerConfigResponse`
        """
        return self._show_tracker_config_with_http_info(request)

    def _show_tracker_config_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

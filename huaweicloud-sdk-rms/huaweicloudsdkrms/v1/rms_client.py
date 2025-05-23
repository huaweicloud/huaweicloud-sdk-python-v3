# coding: utf-8

from __future__ import absolute_import

import importlib
import warnings

from huaweicloudsdkcore.client import Client, ClientBuilder
from huaweicloudsdkcore.utils import http_utils
from huaweicloudsdkcore.sdk_stream_request import SdkStreamRequest

try:
    from huaweicloudsdkcore.invoker.invoker import SyncInvoker
except ImportError as e:
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkrms'")


class RmsClient(Client):
    def __init__(self):
        super(RmsClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkrms.v1.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls, "GlobalCredentials")
        else:
            if clazz.__name__ != "RmsClient":
                raise TypeError("client type error, support client type is RmsClient")
            client_builder = ClientBuilder(clazz, "GlobalCredentials")

        

        return client_builder

    def create_aggregation_authorization(self, request):
        r"""创建资源聚合器授权

        给资源聚合器帐号授予从源帐号收集数据的权限。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateAggregationAuthorization
        :type request: :class:`huaweicloudsdkrms.v1.CreateAggregationAuthorizationRequest`
        :rtype: :class:`huaweicloudsdkrms.v1.CreateAggregationAuthorizationResponse`
        """
        http_info = self._create_aggregation_authorization_http_info(request)
        return self._call_api(**http_info)

    def create_aggregation_authorization_invoker(self, request):
        http_info = self._create_aggregation_authorization_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_aggregation_authorization_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/resource-manager/domains/{domain_id}/aggregators/aggregation-authorization",
            "request_type": request.__class__.__name__,
            "response_type": "CreateAggregationAuthorizationResponse"
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

        auth_settings = ['AccessKeyAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_configuration_aggregator(self, request):
        r"""创建资源聚合器

        创建资源聚合器。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateConfigurationAggregator
        :type request: :class:`huaweicloudsdkrms.v1.CreateConfigurationAggregatorRequest`
        :rtype: :class:`huaweicloudsdkrms.v1.CreateConfigurationAggregatorResponse`
        """
        http_info = self._create_configuration_aggregator_http_info(request)
        return self._call_api(**http_info)

    def create_configuration_aggregator_invoker(self, request):
        http_info = self._create_configuration_aggregator_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_configuration_aggregator_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/resource-manager/domains/{domain_id}/aggregators",
            "request_type": request.__class__.__name__,
            "response_type": "CreateConfigurationAggregatorResponse"
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

        auth_settings = ['AccessKeyAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_aggregation_authorization(self, request):
        r"""删除资源聚合器授权

        删除指定资源聚合器帐号的授权。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteAggregationAuthorization
        :type request: :class:`huaweicloudsdkrms.v1.DeleteAggregationAuthorizationRequest`
        :rtype: :class:`huaweicloudsdkrms.v1.DeleteAggregationAuthorizationResponse`
        """
        http_info = self._delete_aggregation_authorization_http_info(request)
        return self._call_api(**http_info)

    def delete_aggregation_authorization_invoker(self, request):
        http_info = self._delete_aggregation_authorization_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_aggregation_authorization_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/resource-manager/domains/{domain_id}/aggregators/aggregation-authorization/{authorized_account_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteAggregationAuthorizationResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'authorized_account_id' in local_var_params:
            path_params['authorized_account_id'] = local_var_params['authorized_account_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['AccessKeyAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_configuration_aggregator(self, request):
        r"""删除资源聚合器

        删除资源聚合器。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteConfigurationAggregator
        :type request: :class:`huaweicloudsdkrms.v1.DeleteConfigurationAggregatorRequest`
        :rtype: :class:`huaweicloudsdkrms.v1.DeleteConfigurationAggregatorResponse`
        """
        http_info = self._delete_configuration_aggregator_http_info(request)
        return self._call_api(**http_info)

    def delete_configuration_aggregator_invoker(self, request):
        http_info = self._delete_configuration_aggregator_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_configuration_aggregator_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/resource-manager/domains/{domain_id}/aggregators/{aggregator_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteConfigurationAggregatorResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'aggregator_id' in local_var_params:
            path_params['aggregator_id'] = local_var_params['aggregator_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['AccessKeyAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_pending_aggregation_request(self, request):
        r"""删除聚合器帐号中挂起的授权请求

        删除聚合器帐号中挂起的授权请求。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeletePendingAggregationRequest
        :type request: :class:`huaweicloudsdkrms.v1.DeletePendingAggregationRequestRequest`
        :rtype: :class:`huaweicloudsdkrms.v1.DeletePendingAggregationRequestResponse`
        """
        http_info = self._delete_pending_aggregation_request_http_info(request)
        return self._call_api(**http_info)

    def delete_pending_aggregation_request_invoker(self, request):
        http_info = self._delete_pending_aggregation_request_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_pending_aggregation_request_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/resource-manager/domains/{domain_id}/aggregators/pending-aggregation-request/{requester_account_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeletePendingAggregationRequestResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'requester_account_id' in local_var_params:
            path_params['requester_account_id'] = local_var_params['requester_account_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['AccessKeyAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_aggregate_compliance_by_policy_assignment(self, request):
        r"""查询聚合合规规则列表

        查询合规和不合规规则的列表，其中包含合规和不合规规则的资源数量。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAggregateComplianceByPolicyAssignment
        :type request: :class:`huaweicloudsdkrms.v1.ListAggregateComplianceByPolicyAssignmentRequest`
        :rtype: :class:`huaweicloudsdkrms.v1.ListAggregateComplianceByPolicyAssignmentResponse`
        """
        http_info = self._list_aggregate_compliance_by_policy_assignment_http_info(request)
        return self._call_api(**http_info)

    def list_aggregate_compliance_by_policy_assignment_invoker(self, request):
        http_info = self._list_aggregate_compliance_by_policy_assignment_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_aggregate_compliance_by_policy_assignment_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/resource-manager/domains/{domain_id}/aggregators/aggregate-data/policy-assignments/compliance",
            "request_type": request.__class__.__name__,
            "response_type": "ListAggregateComplianceByPolicyAssignmentResponse"
            }

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

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['AccessKeyAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_aggregate_discovered_resources(self, request):
        r"""查询聚合器中资源的列表

        查询资源聚合器中特定资源的列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAggregateDiscoveredResources
        :type request: :class:`huaweicloudsdkrms.v1.ListAggregateDiscoveredResourcesRequest`
        :rtype: :class:`huaweicloudsdkrms.v1.ListAggregateDiscoveredResourcesResponse`
        """
        http_info = self._list_aggregate_discovered_resources_http_info(request)
        return self._call_api(**http_info)

    def list_aggregate_discovered_resources_invoker(self, request):
        http_info = self._list_aggregate_discovered_resources_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_aggregate_discovered_resources_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/resource-manager/domains/{domain_id}/aggregators/aggregate-data/aggregate-discovered-resources",
            "request_type": request.__class__.__name__,
            "response_type": "ListAggregateDiscoveredResourcesResponse"
            }

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

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['AccessKeyAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_aggregation_authorizations(self, request):
        r"""查询资源聚合器授权列表

        查询授权过的资源聚合器列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAggregationAuthorizations
        :type request: :class:`huaweicloudsdkrms.v1.ListAggregationAuthorizationsRequest`
        :rtype: :class:`huaweicloudsdkrms.v1.ListAggregationAuthorizationsResponse`
        """
        http_info = self._list_aggregation_authorizations_http_info(request)
        return self._call_api(**http_info)

    def list_aggregation_authorizations_invoker(self, request):
        http_info = self._list_aggregation_authorizations_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_aggregation_authorizations_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/resource-manager/domains/{domain_id}/aggregators/aggregation-authorization",
            "request_type": request.__class__.__name__,
            "response_type": "ListAggregationAuthorizationsResponse"
            }

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['AccessKeyAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_configuration_aggregators(self, request):
        r"""查询资源聚合器列表

        查询资源聚合器列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListConfigurationAggregators
        :type request: :class:`huaweicloudsdkrms.v1.ListConfigurationAggregatorsRequest`
        :rtype: :class:`huaweicloudsdkrms.v1.ListConfigurationAggregatorsResponse`
        """
        http_info = self._list_configuration_aggregators_http_info(request)
        return self._call_api(**http_info)

    def list_configuration_aggregators_invoker(self, request):
        http_info = self._list_configuration_aggregators_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_configuration_aggregators_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/resource-manager/domains/{domain_id}/aggregators",
            "request_type": request.__class__.__name__,
            "response_type": "ListConfigurationAggregatorsResponse"
            }

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['AccessKeyAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_pending_aggregation_requests(self, request):
        r"""查询所有挂起的聚合请求列表

        查询所有挂起的聚合请求列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListPendingAggregationRequests
        :type request: :class:`huaweicloudsdkrms.v1.ListPendingAggregationRequestsRequest`
        :rtype: :class:`huaweicloudsdkrms.v1.ListPendingAggregationRequestsResponse`
        """
        http_info = self._list_pending_aggregation_requests_http_info(request)
        return self._call_api(**http_info)

    def list_pending_aggregation_requests_invoker(self, request):
        http_info = self._list_pending_aggregation_requests_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_pending_aggregation_requests_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/resource-manager/domains/{domain_id}/aggregators/pending-aggregation-request",
            "request_type": request.__class__.__name__,
            "response_type": "ListPendingAggregationRequestsResponse"
            }

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['AccessKeyAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def run_aggregate_resource_query(self, request):
        r"""对指定聚合器执行高级查询

        对指定聚合器执行高级查询。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RunAggregateResourceQuery
        :type request: :class:`huaweicloudsdkrms.v1.RunAggregateResourceQueryRequest`
        :rtype: :class:`huaweicloudsdkrms.v1.RunAggregateResourceQueryResponse`
        """
        http_info = self._run_aggregate_resource_query_http_info(request)
        return self._call_api(**http_info)

    def run_aggregate_resource_query_invoker(self, request):
        http_info = self._run_aggregate_resource_query_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _run_aggregate_resource_query_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/resource-manager/domains/{domain_id}/aggregators/{aggregator_id}/run-query",
            "request_type": request.__class__.__name__,
            "response_type": "RunAggregateResourceQueryResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'aggregator_id' in local_var_params:
            path_params['aggregator_id'] = local_var_params['aggregator_id']

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

        auth_settings = ['AccessKeyAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_aggregate_compliance_details_by_policy_assignment(self, request):
        r"""查询指定聚合合规规则的评估结果详情

        返回指定聚合合规规则的评估结果详情。包含评估了哪些资源，以及每个资源是否符合规则。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAggregateComplianceDetailsByPolicyAssignment
        :type request: :class:`huaweicloudsdkrms.v1.ShowAggregateComplianceDetailsByPolicyAssignmentRequest`
        :rtype: :class:`huaweicloudsdkrms.v1.ShowAggregateComplianceDetailsByPolicyAssignmentResponse`
        """
        http_info = self._show_aggregate_compliance_details_by_policy_assignment_http_info(request)
        return self._call_api(**http_info)

    def show_aggregate_compliance_details_by_policy_assignment_invoker(self, request):
        http_info = self._show_aggregate_compliance_details_by_policy_assignment_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_aggregate_compliance_details_by_policy_assignment_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/resource-manager/domains/{domain_id}/aggregators/aggregate-data/policy-states/compliance-details",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAggregateComplianceDetailsByPolicyAssignmentResponse"
            }

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

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['AccessKeyAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_aggregate_discovered_resource_counts(self, request):
        r"""查询聚合器中帐号资源的计数

        查询聚合器中帐号资源的计数，支持通过过滤器和GroupByKey来统计资源数量。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAggregateDiscoveredResourceCounts
        :type request: :class:`huaweicloudsdkrms.v1.ShowAggregateDiscoveredResourceCountsRequest`
        :rtype: :class:`huaweicloudsdkrms.v1.ShowAggregateDiscoveredResourceCountsResponse`
        """
        http_info = self._show_aggregate_discovered_resource_counts_http_info(request)
        return self._call_api(**http_info)

    def show_aggregate_discovered_resource_counts_invoker(self, request):
        http_info = self._show_aggregate_discovered_resource_counts_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_aggregate_discovered_resource_counts_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/resource-manager/domains/{domain_id}/aggregators/aggregate-data/aggregate-discovered-resource-counts",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAggregateDiscoveredResourceCountsResponse"
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

        auth_settings = ['AccessKeyAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_aggregate_policy_assignment_detail(self, request):
        r"""查询指定聚合合规规则详情

        返回指定聚合合规规则详情。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAggregatePolicyAssignmentDetail
        :type request: :class:`huaweicloudsdkrms.v1.ShowAggregatePolicyAssignmentDetailRequest`
        :rtype: :class:`huaweicloudsdkrms.v1.ShowAggregatePolicyAssignmentDetailResponse`
        """
        http_info = self._show_aggregate_policy_assignment_detail_http_info(request)
        return self._call_api(**http_info)

    def show_aggregate_policy_assignment_detail_invoker(self, request):
        http_info = self._show_aggregate_policy_assignment_detail_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_aggregate_policy_assignment_detail_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/resource-manager/domains/{domain_id}/aggregators/aggregate-data/policy-assignment/detail",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAggregatePolicyAssignmentDetailResponse"
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

        auth_settings = ['AccessKeyAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_aggregate_policy_state_compliance_summary(self, request):
        r"""查询聚合器中一个或多个帐户的合规概况

        查询聚合器中一个或多个帐户的合规和不合规规则数。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAggregatePolicyStateComplianceSummary
        :type request: :class:`huaweicloudsdkrms.v1.ShowAggregatePolicyStateComplianceSummaryRequest`
        :rtype: :class:`huaweicloudsdkrms.v1.ShowAggregatePolicyStateComplianceSummaryResponse`
        """
        http_info = self._show_aggregate_policy_state_compliance_summary_http_info(request)
        return self._call_api(**http_info)

    def show_aggregate_policy_state_compliance_summary_invoker(self, request):
        http_info = self._show_aggregate_policy_state_compliance_summary_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_aggregate_policy_state_compliance_summary_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/resource-manager/domains/{domain_id}/aggregators/aggregate-data/policy-states/compliance-summary",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAggregatePolicyStateComplianceSummaryResponse"
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

        auth_settings = ['AccessKeyAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_aggregate_resource_config(self, request):
        r"""查询源帐号中资源的详情

        查询源帐号中特定资源的详情。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAggregateResourceConfig
        :type request: :class:`huaweicloudsdkrms.v1.ShowAggregateResourceConfigRequest`
        :rtype: :class:`huaweicloudsdkrms.v1.ShowAggregateResourceConfigResponse`
        """
        http_info = self._show_aggregate_resource_config_http_info(request)
        return self._call_api(**http_info)

    def show_aggregate_resource_config_invoker(self, request):
        http_info = self._show_aggregate_resource_config_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_aggregate_resource_config_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/resource-manager/domains/{domain_id}/aggregators/aggregate-resource-config",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAggregateResourceConfigResponse"
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

        auth_settings = ['AccessKeyAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_configuration_aggregator(self, request):
        r"""查询指定资源聚合器

        查询指定资源聚合器。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowConfigurationAggregator
        :type request: :class:`huaweicloudsdkrms.v1.ShowConfigurationAggregatorRequest`
        :rtype: :class:`huaweicloudsdkrms.v1.ShowConfigurationAggregatorResponse`
        """
        http_info = self._show_configuration_aggregator_http_info(request)
        return self._call_api(**http_info)

    def show_configuration_aggregator_invoker(self, request):
        http_info = self._show_configuration_aggregator_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_configuration_aggregator_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/resource-manager/domains/{domain_id}/aggregators/{aggregator_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowConfigurationAggregatorResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'aggregator_id' in local_var_params:
            path_params['aggregator_id'] = local_var_params['aggregator_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['AccessKeyAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_configuration_aggregator_sources_status(self, request):
        r"""查询指定资源聚合器聚合帐号的状态信息

        查询指定资源聚合器聚合帐号的状态信息，状态包括验证源帐号和聚合器帐号之间授权的信息。如果失败，状态包含相关的错误码或消息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowConfigurationAggregatorSourcesStatus
        :type request: :class:`huaweicloudsdkrms.v1.ShowConfigurationAggregatorSourcesStatusRequest`
        :rtype: :class:`huaweicloudsdkrms.v1.ShowConfigurationAggregatorSourcesStatusResponse`
        """
        http_info = self._show_configuration_aggregator_sources_status_http_info(request)
        return self._call_api(**http_info)

    def show_configuration_aggregator_sources_status_invoker(self, request):
        http_info = self._show_configuration_aggregator_sources_status_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_configuration_aggregator_sources_status_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/resource-manager/domains/{domain_id}/aggregators/{aggregator_id}/aggregator-sources-status",
            "request_type": request.__class__.__name__,
            "response_type": "ShowConfigurationAggregatorSourcesStatusResponse"
            }

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['AccessKeyAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_configuration_aggregator(self, request):
        r"""更新资源聚合器

        更新资源聚合器。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateConfigurationAggregator
        :type request: :class:`huaweicloudsdkrms.v1.UpdateConfigurationAggregatorRequest`
        :rtype: :class:`huaweicloudsdkrms.v1.UpdateConfigurationAggregatorResponse`
        """
        http_info = self._update_configuration_aggregator_http_info(request)
        return self._call_api(**http_info)

    def update_configuration_aggregator_invoker(self, request):
        http_info = self._update_configuration_aggregator_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_configuration_aggregator_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/resource-manager/domains/{domain_id}/aggregators/{aggregator_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateConfigurationAggregatorResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'aggregator_id' in local_var_params:
            path_params['aggregator_id'] = local_var_params['aggregator_id']

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

        auth_settings = ['AccessKeyAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_resource_history(self, request):
        r"""查询资源历史

        查询资源与资源关系的变更历史
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowResourceHistory
        :type request: :class:`huaweicloudsdkrms.v1.ShowResourceHistoryRequest`
        :rtype: :class:`huaweicloudsdkrms.v1.ShowResourceHistoryResponse`
        """
        http_info = self._show_resource_history_http_info(request)
        return self._call_api(**http_info)

    def show_resource_history_invoker(self, request):
        http_info = self._show_resource_history_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_resource_history_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/resource-manager/domains/{domain_id}/resources/{resource_id}/history",
            "request_type": request.__class__.__name__,
            "response_type": "ShowResourceHistoryResponse"
            }

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['PkiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_organization_policy_assignment(self, request):
        r"""创建或更新组织合规规则

        创建或更新组织合规规则，如果规则名称已存在，则为更新操作。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateOrganizationPolicyAssignment
        :type request: :class:`huaweicloudsdkrms.v1.CreateOrganizationPolicyAssignmentRequest`
        :rtype: :class:`huaweicloudsdkrms.v1.CreateOrganizationPolicyAssignmentResponse`
        """
        http_info = self._create_organization_policy_assignment_http_info(request)
        return self._call_api(**http_info)

    def create_organization_policy_assignment_invoker(self, request):
        http_info = self._create_organization_policy_assignment_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_organization_policy_assignment_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/resource-manager/organizations/{organization_id}/policy-assignments",
            "request_type": request.__class__.__name__,
            "response_type": "CreateOrganizationPolicyAssignmentResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'organization_id' in local_var_params:
            path_params['organization_id'] = local_var_params['organization_id']

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

        auth_settings = ['AccessKeyAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_policy_assignments(self, request):
        r"""创建合规规则

        创建新的合规规则
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreatePolicyAssignments
        :type request: :class:`huaweicloudsdkrms.v1.CreatePolicyAssignmentsRequest`
        :rtype: :class:`huaweicloudsdkrms.v1.CreatePolicyAssignmentsResponse`
        """
        http_info = self._create_policy_assignments_http_info(request)
        return self._call_api(**http_info)

    def create_policy_assignments_invoker(self, request):
        http_info = self._create_policy_assignments_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_policy_assignments_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/resource-manager/domains/{domain_id}/policy-assignments",
            "request_type": request.__class__.__name__,
            "response_type": "CreatePolicyAssignmentsResponse"
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

        auth_settings = ['PkiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_organization_policy_assignment(self, request):
        r"""删除组织合规规则

        删除组织合规规则。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteOrganizationPolicyAssignment
        :type request: :class:`huaweicloudsdkrms.v1.DeleteOrganizationPolicyAssignmentRequest`
        :rtype: :class:`huaweicloudsdkrms.v1.DeleteOrganizationPolicyAssignmentResponse`
        """
        http_info = self._delete_organization_policy_assignment_http_info(request)
        return self._call_api(**http_info)

    def delete_organization_policy_assignment_invoker(self, request):
        http_info = self._delete_organization_policy_assignment_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_organization_policy_assignment_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/resource-manager/organizations/{organization_id}/policy-assignments/{organization_policy_assignment_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteOrganizationPolicyAssignmentResponse"
            }

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['AccessKeyAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_policy_assignment(self, request):
        r"""删除合规规则

        根据规则ID删除此规则
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeletePolicyAssignment
        :type request: :class:`huaweicloudsdkrms.v1.DeletePolicyAssignmentRequest`
        :rtype: :class:`huaweicloudsdkrms.v1.DeletePolicyAssignmentResponse`
        """
        http_info = self._delete_policy_assignment_http_info(request)
        return self._call_api(**http_info)

    def delete_policy_assignment_invoker(self, request):
        http_info = self._delete_policy_assignment_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_policy_assignment_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/resource-manager/domains/{domain_id}/policy-assignments/{policy_assignment_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeletePolicyAssignmentResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policy_assignment_id' in local_var_params:
            path_params['policy_assignment_id'] = local_var_params['policy_assignment_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['PkiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def disable_policy_assignment(self, request):
        r"""停用合规规则

        根据规则ID停用此规则
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DisablePolicyAssignment
        :type request: :class:`huaweicloudsdkrms.v1.DisablePolicyAssignmentRequest`
        :rtype: :class:`huaweicloudsdkrms.v1.DisablePolicyAssignmentResponse`
        """
        http_info = self._disable_policy_assignment_http_info(request)
        return self._call_api(**http_info)

    def disable_policy_assignment_invoker(self, request):
        http_info = self._disable_policy_assignment_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _disable_policy_assignment_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/resource-manager/domains/{domain_id}/policy-assignments/{policy_assignment_id}/disable",
            "request_type": request.__class__.__name__,
            "response_type": "DisablePolicyAssignmentResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policy_assignment_id' in local_var_params:
            path_params['policy_assignment_id'] = local_var_params['policy_assignment_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['PkiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def enable_policy_assignment(self, request):
        r"""启用合规规则

        根据规则ID启用此规则
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for EnablePolicyAssignment
        :type request: :class:`huaweicloudsdkrms.v1.EnablePolicyAssignmentRequest`
        :rtype: :class:`huaweicloudsdkrms.v1.EnablePolicyAssignmentResponse`
        """
        http_info = self._enable_policy_assignment_http_info(request)
        return self._call_api(**http_info)

    def enable_policy_assignment_invoker(self, request):
        http_info = self._enable_policy_assignment_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _enable_policy_assignment_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/resource-manager/domains/{domain_id}/policy-assignments/{policy_assignment_id}/enable",
            "request_type": request.__class__.__name__,
            "response_type": "EnablePolicyAssignmentResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policy_assignment_id' in local_var_params:
            path_params['policy_assignment_id'] = local_var_params['policy_assignment_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['PkiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_built_in_policy_definitions(self, request):
        r"""列出内置策略

        列出用户的内置策略
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListBuiltInPolicyDefinitions
        :type request: :class:`huaweicloudsdkrms.v1.ListBuiltInPolicyDefinitionsRequest`
        :rtype: :class:`huaweicloudsdkrms.v1.ListBuiltInPolicyDefinitionsResponse`
        """
        http_info = self._list_built_in_policy_definitions_http_info(request)
        return self._call_api(**http_info)

    def list_built_in_policy_definitions_invoker(self, request):
        http_info = self._list_built_in_policy_definitions_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_built_in_policy_definitions_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/resource-manager/policy-definitions",
            "request_type": request.__class__.__name__,
            "response_type": "ListBuiltInPolicyDefinitionsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['PkiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_organization_policy_assignments(self, request):
        r"""查询组织合规规则列表

        查询组织合规规则列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListOrganizationPolicyAssignments
        :type request: :class:`huaweicloudsdkrms.v1.ListOrganizationPolicyAssignmentsRequest`
        :rtype: :class:`huaweicloudsdkrms.v1.ListOrganizationPolicyAssignmentsResponse`
        """
        http_info = self._list_organization_policy_assignments_http_info(request)
        return self._call_api(**http_info)

    def list_organization_policy_assignments_invoker(self, request):
        http_info = self._list_organization_policy_assignments_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_organization_policy_assignments_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/resource-manager/organizations/{organization_id}/policy-assignments",
            "request_type": request.__class__.__name__,
            "response_type": "ListOrganizationPolicyAssignmentsResponse"
            }

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['AccessKeyAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_policy_assignments(self, request):
        r"""列出合规规则

        列出用户的合规规则
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListPolicyAssignments
        :type request: :class:`huaweicloudsdkrms.v1.ListPolicyAssignmentsRequest`
        :rtype: :class:`huaweicloudsdkrms.v1.ListPolicyAssignmentsResponse`
        """
        http_info = self._list_policy_assignments_http_info(request)
        return self._call_api(**http_info)

    def list_policy_assignments_invoker(self, request):
        http_info = self._list_policy_assignments_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_policy_assignments_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/resource-manager/domains/{domain_id}/policy-assignments",
            "request_type": request.__class__.__name__,
            "response_type": "ListPolicyAssignmentsResponse"
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

        auth_settings = ['PkiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_policy_states_by_assignment_id(self, request):
        r"""获取规则的合规结果

        根据规则ID查询所有的合规结果
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListPolicyStatesByAssignmentId
        :type request: :class:`huaweicloudsdkrms.v1.ListPolicyStatesByAssignmentIdRequest`
        :rtype: :class:`huaweicloudsdkrms.v1.ListPolicyStatesByAssignmentIdResponse`
        """
        http_info = self._list_policy_states_by_assignment_id_http_info(request)
        return self._call_api(**http_info)

    def list_policy_states_by_assignment_id_invoker(self, request):
        http_info = self._list_policy_states_by_assignment_id_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_policy_states_by_assignment_id_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/resource-manager/domains/{domain_id}/policy-assignments/{policy_assignment_id}/policy-states",
            "request_type": request.__class__.__name__,
            "response_type": "ListPolicyStatesByAssignmentIdResponse"
            }

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['PkiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_policy_states_by_domain_id(self, request):
        r"""获取用户的合规结果

        查询用户所有的合规结果
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListPolicyStatesByDomainId
        :type request: :class:`huaweicloudsdkrms.v1.ListPolicyStatesByDomainIdRequest`
        :rtype: :class:`huaweicloudsdkrms.v1.ListPolicyStatesByDomainIdResponse`
        """
        http_info = self._list_policy_states_by_domain_id_http_info(request)
        return self._call_api(**http_info)

    def list_policy_states_by_domain_id_invoker(self, request):
        http_info = self._list_policy_states_by_domain_id_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_policy_states_by_domain_id_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/resource-manager/domains/{domain_id}/policy-states",
            "request_type": request.__class__.__name__,
            "response_type": "ListPolicyStatesByDomainIdResponse"
            }

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['PkiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_policy_states_by_resource_id(self, request):
        r"""获取资源的合规结果

        根据资源ID查询所有合规结果
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListPolicyStatesByResourceId
        :type request: :class:`huaweicloudsdkrms.v1.ListPolicyStatesByResourceIdRequest`
        :rtype: :class:`huaweicloudsdkrms.v1.ListPolicyStatesByResourceIdResponse`
        """
        http_info = self._list_policy_states_by_resource_id_http_info(request)
        return self._call_api(**http_info)

    def list_policy_states_by_resource_id_invoker(self, request):
        http_info = self._list_policy_states_by_resource_id_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_policy_states_by_resource_id_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/resource-manager/domains/{domain_id}/resources/{resource_id}/policy-states",
            "request_type": request.__class__.__name__,
            "response_type": "ListPolicyStatesByResourceIdResponse"
            }

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['PkiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def run_evaluation_by_policy_assignment_id(self, request):
        r"""运行合规评估

        根据规则ID评估此规则
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RunEvaluationByPolicyAssignmentId
        :type request: :class:`huaweicloudsdkrms.v1.RunEvaluationByPolicyAssignmentIdRequest`
        :rtype: :class:`huaweicloudsdkrms.v1.RunEvaluationByPolicyAssignmentIdResponse`
        """
        http_info = self._run_evaluation_by_policy_assignment_id_http_info(request)
        return self._call_api(**http_info)

    def run_evaluation_by_policy_assignment_id_invoker(self, request):
        http_info = self._run_evaluation_by_policy_assignment_id_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _run_evaluation_by_policy_assignment_id_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/resource-manager/domains/{domain_id}/policy-assignments/{policy_assignment_id}/policy-states/run-evaluation",
            "request_type": request.__class__.__name__,
            "response_type": "RunEvaluationByPolicyAssignmentIdResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policy_assignment_id' in local_var_params:
            path_params['policy_assignment_id'] = local_var_params['policy_assignment_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['PkiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_built_in_policy_definition(self, request):
        r"""查询单个内置策略

        根据策略ID查询单个内置策略
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowBuiltInPolicyDefinition
        :type request: :class:`huaweicloudsdkrms.v1.ShowBuiltInPolicyDefinitionRequest`
        :rtype: :class:`huaweicloudsdkrms.v1.ShowBuiltInPolicyDefinitionResponse`
        """
        http_info = self._show_built_in_policy_definition_http_info(request)
        return self._call_api(**http_info)

    def show_built_in_policy_definition_invoker(self, request):
        http_info = self._show_built_in_policy_definition_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_built_in_policy_definition_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/resource-manager/policy-definitions/{policy_definition_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowBuiltInPolicyDefinitionResponse"
            }

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['PkiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_evaluation_state_by_assignment_id(self, request):
        r"""获取规则的评估状态

        根据规则ID查询此规则的评估状态
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowEvaluationStateByAssignmentId
        :type request: :class:`huaweicloudsdkrms.v1.ShowEvaluationStateByAssignmentIdRequest`
        :rtype: :class:`huaweicloudsdkrms.v1.ShowEvaluationStateByAssignmentIdResponse`
        """
        http_info = self._show_evaluation_state_by_assignment_id_http_info(request)
        return self._call_api(**http_info)

    def show_evaluation_state_by_assignment_id_invoker(self, request):
        http_info = self._show_evaluation_state_by_assignment_id_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_evaluation_state_by_assignment_id_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/resource-manager/domains/{domain_id}/policy-assignments/{policy_assignment_id}/policy-states/evaluation-state",
            "request_type": request.__class__.__name__,
            "response_type": "ShowEvaluationStateByAssignmentIdResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policy_assignment_id' in local_var_params:
            path_params['policy_assignment_id'] = local_var_params['policy_assignment_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['PkiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_organization_policy_assignment(self, request):
        r"""查询指定组织合规规则

        查询指定组织合规规则。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowOrganizationPolicyAssignment
        :type request: :class:`huaweicloudsdkrms.v1.ShowOrganizationPolicyAssignmentRequest`
        :rtype: :class:`huaweicloudsdkrms.v1.ShowOrganizationPolicyAssignmentResponse`
        """
        http_info = self._show_organization_policy_assignment_http_info(request)
        return self._call_api(**http_info)

    def show_organization_policy_assignment_invoker(self, request):
        http_info = self._show_organization_policy_assignment_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_organization_policy_assignment_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/resource-manager/organizations/{organization_id}/policy-assignments/{organization_policy_assignment_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowOrganizationPolicyAssignmentResponse"
            }

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['AccessKeyAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_organization_policy_assignment_detailed_status(self, request):
        r"""查询组织内每个成员帐号合规规则部署的详细状态

        查询组织内每个成员帐号合规规则部署的详细状态。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowOrganizationPolicyAssignmentDetailedStatus
        :type request: :class:`huaweicloudsdkrms.v1.ShowOrganizationPolicyAssignmentDetailedStatusRequest`
        :rtype: :class:`huaweicloudsdkrms.v1.ShowOrganizationPolicyAssignmentDetailedStatusResponse`
        """
        http_info = self._show_organization_policy_assignment_detailed_status_http_info(request)
        return self._call_api(**http_info)

    def show_organization_policy_assignment_detailed_status_invoker(self, request):
        http_info = self._show_organization_policy_assignment_detailed_status_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_organization_policy_assignment_detailed_status_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/resource-manager/organizations/{organization_id}/policy-assignment-detailed-status",
            "request_type": request.__class__.__name__,
            "response_type": "ShowOrganizationPolicyAssignmentDetailedStatusResponse"
            }

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['AccessKeyAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_organization_policy_assignment_statuses(self, request):
        r"""查询组织合规规则部署状态

        查询组织合规规则部署状态。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowOrganizationPolicyAssignmentStatuses
        :type request: :class:`huaweicloudsdkrms.v1.ShowOrganizationPolicyAssignmentStatusesRequest`
        :rtype: :class:`huaweicloudsdkrms.v1.ShowOrganizationPolicyAssignmentStatusesResponse`
        """
        http_info = self._show_organization_policy_assignment_statuses_http_info(request)
        return self._call_api(**http_info)

    def show_organization_policy_assignment_statuses_invoker(self, request):
        http_info = self._show_organization_policy_assignment_statuses_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_organization_policy_assignment_statuses_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/resource-manager/organizations/{organization_id}/policy-assignment-statuses",
            "request_type": request.__class__.__name__,
            "response_type": "ShowOrganizationPolicyAssignmentStatusesResponse"
            }

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['AccessKeyAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_policy_assignment(self, request):
        r"""获取单个合规规则

        根据规则ID获取单个规则
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowPolicyAssignment
        :type request: :class:`huaweicloudsdkrms.v1.ShowPolicyAssignmentRequest`
        :rtype: :class:`huaweicloudsdkrms.v1.ShowPolicyAssignmentResponse`
        """
        http_info = self._show_policy_assignment_http_info(request)
        return self._call_api(**http_info)

    def show_policy_assignment_invoker(self, request):
        http_info = self._show_policy_assignment_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_policy_assignment_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/resource-manager/domains/{domain_id}/policy-assignments/{policy_assignment_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowPolicyAssignmentResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policy_assignment_id' in local_var_params:
            path_params['policy_assignment_id'] = local_var_params['policy_assignment_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['PkiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_policy_assignment(self, request):
        r"""更新合规规则

        更新用户的合规规则
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdatePolicyAssignment
        :type request: :class:`huaweicloudsdkrms.v1.UpdatePolicyAssignmentRequest`
        :rtype: :class:`huaweicloudsdkrms.v1.UpdatePolicyAssignmentResponse`
        """
        http_info = self._update_policy_assignment_http_info(request)
        return self._call_api(**http_info)

    def update_policy_assignment_invoker(self, request):
        http_info = self._update_policy_assignment_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_policy_assignment_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/resource-manager/domains/{domain_id}/policy-assignments/{policy_assignment_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdatePolicyAssignmentResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policy_assignment_id' in local_var_params:
            path_params['policy_assignment_id'] = local_var_params['policy_assignment_id']

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

        auth_settings = ['PkiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_policy_state(self, request):
        r"""更新合规评估结果

        更新用户自定义合规规则的合规评估结果
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdatePolicyState
        :type request: :class:`huaweicloudsdkrms.v1.UpdatePolicyStateRequest`
        :rtype: :class:`huaweicloudsdkrms.v1.UpdatePolicyStateResponse`
        """
        http_info = self._update_policy_state_http_info(request)
        return self._call_api(**http_info)

    def update_policy_state_invoker(self, request):
        http_info = self._update_policy_state_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_policy_state_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/resource-manager/domains/{domain_id}/policy-states",
            "request_type": request.__class__.__name__,
            "response_type": "UpdatePolicyStateResponse"
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

        auth_settings = ['PkiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_stored_query(self, request):
        r"""创建高级查询

        创建新的高级查询
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateStoredQuery
        :type request: :class:`huaweicloudsdkrms.v1.CreateStoredQueryRequest`
        :rtype: :class:`huaweicloudsdkrms.v1.CreateStoredQueryResponse`
        """
        http_info = self._create_stored_query_http_info(request)
        return self._call_api(**http_info)

    def create_stored_query_invoker(self, request):
        http_info = self._create_stored_query_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_stored_query_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/resource-manager/domains/{domain_id}/stored-queries",
            "request_type": request.__class__.__name__,
            "response_type": "CreateStoredQueryResponse"
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

        auth_settings = ['PkiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_stored_query(self, request):
        r"""删除高级查询

        删除单个高级查询
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteStoredQuery
        :type request: :class:`huaweicloudsdkrms.v1.DeleteStoredQueryRequest`
        :rtype: :class:`huaweicloudsdkrms.v1.DeleteStoredQueryResponse`
        """
        http_info = self._delete_stored_query_http_info(request)
        return self._call_api(**http_info)

    def delete_stored_query_invoker(self, request):
        http_info = self._delete_stored_query_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_stored_query_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/resource-manager/domains/{domain_id}/stored-queries/{query_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteStoredQueryResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'query_id' in local_var_params:
            path_params['query_id'] = local_var_params['query_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['PkiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_schemas(self, request):
        r"""列举高级查询Schema

        List Schemas
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListSchemas
        :type request: :class:`huaweicloudsdkrms.v1.ListSchemasRequest`
        :rtype: :class:`huaweicloudsdkrms.v1.ListSchemasResponse`
        """
        http_info = self._list_schemas_http_info(request)
        return self._call_api(**http_info)

    def list_schemas_invoker(self, request):
        http_info = self._list_schemas_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_schemas_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/resource-manager/domains/{domain_id}/schemas",
            "request_type": request.__class__.__name__,
            "response_type": "ListSchemasResponse"
            }

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['PkiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_stored_queries(self, request):
        r"""列出高级查询

        列举所有高级查询
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListStoredQueries
        :type request: :class:`huaweicloudsdkrms.v1.ListStoredQueriesRequest`
        :rtype: :class:`huaweicloudsdkrms.v1.ListStoredQueriesResponse`
        """
        http_info = self._list_stored_queries_http_info(request)
        return self._call_api(**http_info)

    def list_stored_queries_invoker(self, request):
        http_info = self._list_stored_queries_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_stored_queries_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/resource-manager/domains/{domain_id}/stored-queries",
            "request_type": request.__class__.__name__,
            "response_type": "ListStoredQueriesResponse"
            }

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['PkiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def run_query(self, request):
        r"""运行高级查询

        执行高级查询
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RunQuery
        :type request: :class:`huaweicloudsdkrms.v1.RunQueryRequest`
        :rtype: :class:`huaweicloudsdkrms.v1.RunQueryResponse`
        """
        http_info = self._run_query_http_info(request)
        return self._call_api(**http_info)

    def run_query_invoker(self, request):
        http_info = self._run_query_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _run_query_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/resource-manager/domains/{domain_id}/run-query",
            "request_type": request.__class__.__name__,
            "response_type": "RunQueryResponse"
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

        auth_settings = ['PkiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_stored_query(self, request):
        r"""查询单个高级查询

        Show Resource Query Language
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowStoredQuery
        :type request: :class:`huaweicloudsdkrms.v1.ShowStoredQueryRequest`
        :rtype: :class:`huaweicloudsdkrms.v1.ShowStoredQueryResponse`
        """
        http_info = self._show_stored_query_http_info(request)
        return self._call_api(**http_info)

    def show_stored_query_invoker(self, request):
        http_info = self._show_stored_query_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_stored_query_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/resource-manager/domains/{domain_id}/stored-queries/{query_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowStoredQueryResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'query_id' in local_var_params:
            path_params['query_id'] = local_var_params['query_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['PkiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_stored_query(self, request):
        r"""更新单个高级查询

        更新自定义查询
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateStoredQuery
        :type request: :class:`huaweicloudsdkrms.v1.UpdateStoredQueryRequest`
        :rtype: :class:`huaweicloudsdkrms.v1.UpdateStoredQueryResponse`
        """
        http_info = self._update_stored_query_http_info(request)
        return self._call_api(**http_info)

    def update_stored_query_invoker(self, request):
        http_info = self._update_stored_query_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_stored_query_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/resource-manager/domains/{domain_id}/stored-queries/{query_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateStoredQueryResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'query_id' in local_var_params:
            path_params['query_id'] = local_var_params['query_id']

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

        auth_settings = ['PkiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_regions(self, request):
        r"""查询用户可见的区域

        查询用户可见的区域
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListRegions
        :type request: :class:`huaweicloudsdkrms.v1.ListRegionsRequest`
        :rtype: :class:`huaweicloudsdkrms.v1.ListRegionsResponse`
        """
        http_info = self._list_regions_http_info(request)
        return self._call_api(**http_info)

    def list_regions_invoker(self, request):
        http_info = self._list_regions_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_regions_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/resource-manager/domains/{domain_id}/regions",
            "request_type": request.__class__.__name__,
            "response_type": "ListRegionsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['PkiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_resource_relations(self, request):
        r"""列举资源关系

        指定资源ID，查询该资源与其他资源的关联关系，可以指定关系方向为\&quot;in\&quot; 或者\&quot;out\&quot;
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowResourceRelations
        :type request: :class:`huaweicloudsdkrms.v1.ShowResourceRelationsRequest`
        :rtype: :class:`huaweicloudsdkrms.v1.ShowResourceRelationsResponse`
        """
        http_info = self._show_resource_relations_http_info(request)
        return self._call_api(**http_info)

    def show_resource_relations_invoker(self, request):
        http_info = self._show_resource_relations_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_resource_relations_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/resource-manager/domains/{domain_id}/resources/{resource_id}/relations",
            "request_type": request.__class__.__name__,
            "response_type": "ShowResourceRelationsResponse"
            }

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['PkiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_resource_relations_detail(self, request):
        r"""列举资源关系详情

        指定资源ID，查询该资源与其他资源的关联关系，可以指定关系方向为“in”或者“out”，需要当帐号有rms:resources:getRelation权限。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowResourceRelationsDetail
        :type request: :class:`huaweicloudsdkrms.v1.ShowResourceRelationsDetailRequest`
        :rtype: :class:`huaweicloudsdkrms.v1.ShowResourceRelationsDetailResponse`
        """
        http_info = self._show_resource_relations_detail_http_info(request)
        return self._call_api(**http_info)

    def show_resource_relations_detail_invoker(self, request):
        http_info = self._show_resource_relations_detail_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_resource_relations_detail_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/resource-manager/domains/{domain_id}/all-resources/{resource_id}/relations",
            "request_type": request.__class__.__name__,
            "response_type": "ShowResourceRelationsDetailResponse"
            }

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['AccessKeyAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def collect_all_resources_summary(self, request):
        r"""列举资源概要

        查询当前帐号的资源概览。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CollectAllResourcesSummary
        :type request: :class:`huaweicloudsdkrms.v1.CollectAllResourcesSummaryRequest`
        :rtype: :class:`huaweicloudsdkrms.v1.CollectAllResourcesSummaryResponse`
        """
        http_info = self._collect_all_resources_summary_http_info(request)
        return self._call_api(**http_info)

    def collect_all_resources_summary_invoker(self, request):
        http_info = self._collect_all_resources_summary_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _collect_all_resources_summary_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/resource-manager/domains/{domain_id}/all-resources/summary",
            "request_type": request.__class__.__name__,
            "response_type": "CollectAllResourcesSummaryResponse"
            }

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['AccessKeyAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def count_all_resources(self, request):
        r"""查询资源数量

        查询当前帐号的资源数量。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CountAllResources
        :type request: :class:`huaweicloudsdkrms.v1.CountAllResourcesRequest`
        :rtype: :class:`huaweicloudsdkrms.v1.CountAllResourcesResponse`
        """
        http_info = self._count_all_resources_http_info(request)
        return self._call_api(**http_info)

    def count_all_resources_invoker(self, request):
        http_info = self._count_all_resources_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _count_all_resources_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/resource-manager/domains/{domain_id}/all-resources/count",
            "request_type": request.__class__.__name__,
            "response_type": "CountAllResourcesResponse"
            }

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['AccessKeyAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_all_resources(self, request):
        r"""列举所有资源

        返回当前用户下所有资源，需要当前用户有rms:resources:list权限。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAllResources
        :type request: :class:`huaweicloudsdkrms.v1.ListAllResourcesRequest`
        :rtype: :class:`huaweicloudsdkrms.v1.ListAllResourcesResponse`
        """
        http_info = self._list_all_resources_http_info(request)
        return self._call_api(**http_info)

    def list_all_resources_invoker(self, request):
        http_info = self._list_all_resources_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_all_resources_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/resource-manager/domains/{domain_id}/all-resources",
            "request_type": request.__class__.__name__,
            "response_type": "ListAllResourcesResponse"
            }

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['PkiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_all_tags(self, request):
        r"""列举资源标签

        查询当前帐号下所有资源的标签。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAllTags
        :type request: :class:`huaweicloudsdkrms.v1.ListAllTagsRequest`
        :rtype: :class:`huaweicloudsdkrms.v1.ListAllTagsResponse`
        """
        http_info = self._list_all_tags_http_info(request)
        return self._call_api(**http_info)

    def list_all_tags_invoker(self, request):
        http_info = self._list_all_tags_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_all_tags_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/resource-manager/domains/{domain_id}/all-resources/tags",
            "request_type": request.__class__.__name__,
            "response_type": "ListAllTagsResponse"
            }

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['AccessKeyAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_providers(self, request):
        r"""列举云服务

        查询RMS支持的云服务、资源、区域列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListProviders
        :type request: :class:`huaweicloudsdkrms.v1.ListProvidersRequest`
        :rtype: :class:`huaweicloudsdkrms.v1.ListProvidersResponse`
        """
        http_info = self._list_providers_http_info(request)
        return self._call_api(**http_info)

    def list_providers_invoker(self, request):
        http_info = self._list_providers_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_providers_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/resource-manager/domains/{domain_id}/providers",
            "request_type": request.__class__.__name__,
            "response_type": "ListProvidersResponse"
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
        if 'track' in local_var_params:
            query_params.append(('track', local_var_params['track']))

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['PkiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_resources(self, request):
        r"""列举指定类型的资源

        返回当前租户下特定资源类型的资源，需要当前用户有rms:resources:list权限。比如查询云服务器，对应的RMS资源类型是ecs.cloudservers，其中provider为ecs，type为cloudservers。 RMS支持的服务和资源类型参见[支持的服务和区域](https://console.huaweicloud.com/eps/#/resources/supported)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListResources
        :type request: :class:`huaweicloudsdkrms.v1.ListResourcesRequest`
        :rtype: :class:`huaweicloudsdkrms.v1.ListResourcesResponse`
        """
        http_info = self._list_resources_http_info(request)
        return self._call_api(**http_info)

    def list_resources_invoker(self, request):
        http_info = self._list_resources_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_resources_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/resource-manager/domains/{domain_id}/provider/{provider}/type/{type}/resources",
            "request_type": request.__class__.__name__,
            "response_type": "ListResourcesResponse"
            }

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['PkiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_resource_by_id(self, request):
        r"""查询单个资源

        指定资源ID，返回该资源的详细信息，需要当前用户有rms:resources:get权限。比如查询云服务器，对应的RMS资源类型是ecs.cloudservers，其中provider为ecs，type为cloudservers。RMS支持的服务和资源类型参见[支持的服务和区域](https://console.huaweicloud.com/eps/#/resources/supported)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowResourceById
        :type request: :class:`huaweicloudsdkrms.v1.ShowResourceByIdRequest`
        :rtype: :class:`huaweicloudsdkrms.v1.ShowResourceByIdResponse`
        """
        http_info = self._show_resource_by_id_http_info(request)
        return self._call_api(**http_info)

    def show_resource_by_id_invoker(self, request):
        http_info = self._show_resource_by_id_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_resource_by_id_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/resource-manager/domains/{domain_id}/provider/{provider}/type/{type}/resources/{resource_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowResourceByIdResponse"
            }

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['PkiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_resource_detail(self, request):
        r"""查询帐号下的单个资源

        查询当前帐号下的单个资源。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowResourceDetail
        :type request: :class:`huaweicloudsdkrms.v1.ShowResourceDetailRequest`
        :rtype: :class:`huaweicloudsdkrms.v1.ShowResourceDetailResponse`
        """
        http_info = self._show_resource_detail_http_info(request)
        return self._call_api(**http_info)

    def show_resource_detail_invoker(self, request):
        http_info = self._show_resource_detail_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_resource_detail_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/resource-manager/domains/{domain_id}/all-resources/{resource_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowResourceDetailResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
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

        auth_settings = ['AccessKeyAuth', 'PkiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_tracker_config(self, request):
        r"""创建或更新记录器

        创建或更新资源记录器，只能存在一个资源记录器
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateTrackerConfig
        :type request: :class:`huaweicloudsdkrms.v1.CreateTrackerConfigRequest`
        :rtype: :class:`huaweicloudsdkrms.v1.CreateTrackerConfigResponse`
        """
        http_info = self._create_tracker_config_http_info(request)
        return self._call_api(**http_info)

    def create_tracker_config_invoker(self, request):
        http_info = self._create_tracker_config_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_tracker_config_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/resource-manager/domains/{domain_id}/tracker-config",
            "request_type": request.__class__.__name__,
            "response_type": "CreateTrackerConfigResponse"
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

        auth_settings = ['PkiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_tracker_config(self, request):
        r"""删除记录器

        删除资源记录器
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteTrackerConfig
        :type request: :class:`huaweicloudsdkrms.v1.DeleteTrackerConfigRequest`
        :rtype: :class:`huaweicloudsdkrms.v1.DeleteTrackerConfigResponse`
        """
        http_info = self._delete_tracker_config_http_info(request)
        return self._call_api(**http_info)

    def delete_tracker_config_invoker(self, request):
        http_info = self._delete_tracker_config_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_tracker_config_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/resource-manager/domains/{domain_id}/tracker-config",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteTrackerConfigResponse"
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

        auth_settings = ['PkiTokenAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_tracker_config(self, request):
        r"""查询记录器

        查询资源记录器的详细信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowTrackerConfig
        :type request: :class:`huaweicloudsdkrms.v1.ShowTrackerConfigRequest`
        :rtype: :class:`huaweicloudsdkrms.v1.ShowTrackerConfigResponse`
        """
        http_info = self._show_tracker_config_http_info(request)
        return self._call_api(**http_info)

    def show_tracker_config_invoker(self, request):
        http_info = self._show_tracker_config_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_tracker_config_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/resource-manager/domains/{domain_id}/tracker-config",
            "request_type": request.__class__.__name__,
            "response_type": "ShowTrackerConfigResponse"
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

        auth_settings = ['PkiTokenAuth']

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

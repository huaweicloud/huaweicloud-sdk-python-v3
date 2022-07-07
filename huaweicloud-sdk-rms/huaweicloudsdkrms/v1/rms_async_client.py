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

    def show_resource_history_async(self, request):
        """查询资源历史

        查询资源与资源关系的变更历史
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

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
            response_type='ShowResourceHistoryResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_policy_assignments_async(self, request):
        """创建合规规则

        创建新的合规规则
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

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
            response_type='CreatePolicyAssignmentsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_policy_assignment_async(self, request):
        """删除合规规则

        根据规则ID删除此规则
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

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
            response_type='DeletePolicyAssignmentResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def disable_policy_assignment_async(self, request):
        """停用合规规则

        根据规则ID停用此规则
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

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
            response_type='DisablePolicyAssignmentResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def enable_policy_assignment_async(self, request):
        """启用合规规则

        根据规则ID启用此规则
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

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
            response_type='EnablePolicyAssignmentResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_built_in_policy_definitions_async(self, request):
        """列出内置策略

        列出用户的内置策略
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

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
            response_type='ListBuiltInPolicyDefinitionsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_policy_assignments_async(self, request):
        """列出合规规则

        列出用户的合规规则
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

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
            response_type='ListPolicyAssignmentsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_policy_states_by_assignment_id_async(self, request):
        """获取规则的合规结果

        根据规则ID查询所有的合规结果
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

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
            response_type='ListPolicyStatesByAssignmentIdResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_policy_states_by_domain_id_async(self, request):
        """获取用户的合规结果

        查询用户所有的合规结果
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

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
            response_type='ListPolicyStatesByDomainIdResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_policy_states_by_resource_id_async(self, request):
        """获取资源的合规结果

        根据资源ID查询所有合规结果
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

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
            response_type='ListPolicyStatesByResourceIdResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def run_evaluation_by_policy_assignment_id_async(self, request):
        """运行合规评估

        根据规则ID评估此规则
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

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
            response_type='RunEvaluationByPolicyAssignmentIdResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_built_in_policy_definition_async(self, request):
        """查询单个内置策略

        根据策略ID查询单个内置策略
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

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
            response_type='ShowBuiltInPolicyDefinitionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_evaluation_state_by_assignment_id_async(self, request):
        """获取规则的评估状态

        根据规则ID查询此规则的评估状态
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

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
            response_type='ShowEvaluationStateByAssignmentIdResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_policy_assignment_async(self, request):
        """获取单个合规规则

        根据规则ID获取单个规则
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

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
            response_type='ShowPolicyAssignmentResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_policy_assignment_async(self, request):
        """更新合规规则

        更新用户的合规规则
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

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
            response_type='UpdatePolicyAssignmentResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_stored_query_async(self, request):
        """创建高级查询

        创建新的高级查询
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

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
            response_type='CreateStoredQueryResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_stored_query_async(self, request):
        """删除高级查询

        删除单个高级查询
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

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
            response_type='DeleteStoredQueryResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_schemas_async(self, request):
        """列举高级查询Schema

        List Schemas
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

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
            response_type='ListSchemasResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_stored_queries_async(self, request):
        """列出高级查询

        列举所有高级查询
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

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
            response_type='ListStoredQueriesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def run_query_async(self, request):
        """运行高级查询

        执行高级查询
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

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
            response_type='RunQueryResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_stored_query_async(self, request):
        """查询单个高级查询

        Show Resource Query Language
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

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
            response_type='ShowStoredQueryResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_stored_query_async(self, request):
        """更新单个高级查询

        更新自定义查询
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

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
            response_type='UpdateStoredQueryResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_regions_async(self, request):
        """查询用户可见的区域

        查询用户可见的区域
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

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
            response_type='ListRegionsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_resource_relations_async(self, request):
        """列举资源关系

        指定资源ID，查询该资源与其他资源的关联关系，可以指定关系方向为\&quot;in\&quot; 或者\&quot;out\&quot;
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

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
            response_type='ShowResourceRelationsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_all_resources_async(self, request):
        """列举所有资源

        返回当前用户下所有资源，需要当前用户有rms:resources:list权限。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListAllResources
        :type request: :class:`huaweicloudsdkrms.v1.ListAllResourcesRequest`
        :rtype: :class:`huaweicloudsdkrms.v1.ListAllResourcesResponse`
        """
        return self.list_all_resources_with_http_info(request)

    def list_all_resources_with_http_info(self, request):
        all_params = ['region_id', 'ep_id', 'type', 'limit', 'marker']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='ListAllResourcesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_providers_async(self, request):
        """列举云服务

        查询RMS支持的云服务、资源、区域列表
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListProviders
        :type request: :class:`huaweicloudsdkrms.v1.ListProvidersRequest`
        :rtype: :class:`huaweicloudsdkrms.v1.ListProvidersResponse`
        """
        return self.list_providers_with_http_info(request)

    def list_providers_with_http_info(self, request):
        all_params = ['offset', 'limit', 'x_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

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
            response_type='ListProvidersResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_resources_async(self, request):
        """列举指定类型的资源

        返回当前租户下特定资源类型的资源，需要当前用户有rms:resources:list权限。比如查询云服务器，对应的RMS资源类型是ecs.cloudservers，其中provider为ecs，type为cloudservers。 RMS支持的服务和资源类型参见[支持的服务和区域](https://console.huaweicloud.com/eps/#/resources/supported)。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

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
            response_type='ListResourcesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_resource_by_id_async(self, request):
        """查询单个资源

        指定资源ID，返回该资源的详细信息，需要当前用户有rms:resources:get权限。比如查询云服务器，对应的RMS资源类型是ecs.cloudservers，其中provider为ecs，type为cloudservers。RMS支持的服务和资源类型参见[支持的服务和区域](https://console.huaweicloud.com/eps/#/resources/supported)。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

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
            response_type='ShowResourceByIdResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_tracker_config_async(self, request):
        """创建或更新记录器

        创建或更新资源记录器，只能存在一个资源记录器
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

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
            response_type='CreateTrackerConfigResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_tracker_config_async(self, request):
        """删除记录器

        删除资源记录器
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

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
            response_type='DeleteTrackerConfigResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_tracker_config_async(self, request):
        """查询记录器

        查询资源记录器的详细信息
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

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
            response_type='ShowTrackerConfigResponse',
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

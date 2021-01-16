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

        :param ShowResourceHistoryRequest request
        :return: ShowResourceHistoryResponse
        """
        return self.show_resource_history_with_http_info(request)

    def show_resource_history_with_http_info(self, request):
        """查询资源历史

        查询资源与资源关系的变更历史

        :param ShowResourceHistoryRequest request
        :return: ShowResourceHistoryResponse
        """

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

        :param CreatePolicyAssignmentsRequest request
        :return: CreatePolicyAssignmentsResponse
        """
        return self.create_policy_assignments_with_http_info(request)

    def create_policy_assignments_with_http_info(self, request):
        """创建合规规则

        创建新的合规规则

        :param CreatePolicyAssignmentsRequest request
        :return: CreatePolicyAssignmentsResponse
        """

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

        :param DeletePolicyAssignmentRequest request
        :return: DeletePolicyAssignmentResponse
        """
        return self.delete_policy_assignment_with_http_info(request)

    def delete_policy_assignment_with_http_info(self, request):
        """删除合规规则

        根据规则ID删除此规则

        :param DeletePolicyAssignmentRequest request
        :return: DeletePolicyAssignmentResponse
        """

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

        :param DisablePolicyAssignmentRequest request
        :return: DisablePolicyAssignmentResponse
        """
        return self.disable_policy_assignment_with_http_info(request)

    def disable_policy_assignment_with_http_info(self, request):
        """停用合规规则

        根据规则ID停用此规则

        :param DisablePolicyAssignmentRequest request
        :return: DisablePolicyAssignmentResponse
        """

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

        :param EnablePolicyAssignmentRequest request
        :return: EnablePolicyAssignmentResponse
        """
        return self.enable_policy_assignment_with_http_info(request)

    def enable_policy_assignment_with_http_info(self, request):
        """启用合规规则

        根据规则ID启用此规则

        :param EnablePolicyAssignmentRequest request
        :return: EnablePolicyAssignmentResponse
        """

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

        :param ListBuiltInPolicyDefinitionsRequest request
        :return: ListBuiltInPolicyDefinitionsResponse
        """
        return self.list_built_in_policy_definitions_with_http_info(request)

    def list_built_in_policy_definitions_with_http_info(self, request):
        """列出内置策略

        列出用户的内置策略

        :param ListBuiltInPolicyDefinitionsRequest request
        :return: ListBuiltInPolicyDefinitionsResponse
        """

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

        :param ListPolicyAssignmentsRequest request
        :return: ListPolicyAssignmentsResponse
        """
        return self.list_policy_assignments_with_http_info(request)

    def list_policy_assignments_with_http_info(self, request):
        """列出合规规则

        列出用户的合规规则

        :param ListPolicyAssignmentsRequest request
        :return: ListPolicyAssignmentsResponse
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

        :param ListPolicyStatesByAssignmentIdRequest request
        :return: ListPolicyStatesByAssignmentIdResponse
        """
        return self.list_policy_states_by_assignment_id_with_http_info(request)

    def list_policy_states_by_assignment_id_with_http_info(self, request):
        """获取规则的合规结果

        根据规则ID查询所有的合规结果

        :param ListPolicyStatesByAssignmentIdRequest request
        :return: ListPolicyStatesByAssignmentIdResponse
        """

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

        :param ListPolicyStatesByDomainIdRequest request
        :return: ListPolicyStatesByDomainIdResponse
        """
        return self.list_policy_states_by_domain_id_with_http_info(request)

    def list_policy_states_by_domain_id_with_http_info(self, request):
        """获取用户的合规结果

        查询用户所有的合规结果

        :param ListPolicyStatesByDomainIdRequest request
        :return: ListPolicyStatesByDomainIdResponse
        """

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

        :param ListPolicyStatesByResourceIdRequest request
        :return: ListPolicyStatesByResourceIdResponse
        """
        return self.list_policy_states_by_resource_id_with_http_info(request)

    def list_policy_states_by_resource_id_with_http_info(self, request):
        """获取资源的合规结果

        根据资源ID查询所有合规结果

        :param ListPolicyStatesByResourceIdRequest request
        :return: ListPolicyStatesByResourceIdResponse
        """

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

        :param RunEvaluationByPolicyAssignmentIdRequest request
        :return: RunEvaluationByPolicyAssignmentIdResponse
        """
        return self.run_evaluation_by_policy_assignment_id_with_http_info(request)

    def run_evaluation_by_policy_assignment_id_with_http_info(self, request):
        """运行合规评估

        根据规则ID评估此规则

        :param RunEvaluationByPolicyAssignmentIdRequest request
        :return: RunEvaluationByPolicyAssignmentIdResponse
        """

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

        :param ShowBuiltInPolicyDefinitionRequest request
        :return: ShowBuiltInPolicyDefinitionResponse
        """
        return self.show_built_in_policy_definition_with_http_info(request)

    def show_built_in_policy_definition_with_http_info(self, request):
        """查询单个内置策略

        根据策略ID查询单个内置策略

        :param ShowBuiltInPolicyDefinitionRequest request
        :return: ShowBuiltInPolicyDefinitionResponse
        """

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

        :param ShowEvaluationStateByAssignmentIdRequest request
        :return: ShowEvaluationStateByAssignmentIdResponse
        """
        return self.show_evaluation_state_by_assignment_id_with_http_info(request)

    def show_evaluation_state_by_assignment_id_with_http_info(self, request):
        """获取规则的评估状态

        根据规则ID查询此规则的评估状态

        :param ShowEvaluationStateByAssignmentIdRequest request
        :return: ShowEvaluationStateByAssignmentIdResponse
        """

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

        :param ShowPolicyAssignmentRequest request
        :return: ShowPolicyAssignmentResponse
        """
        return self.show_policy_assignment_with_http_info(request)

    def show_policy_assignment_with_http_info(self, request):
        """获取单个合规规则

        根据规则ID获取单个规则

        :param ShowPolicyAssignmentRequest request
        :return: ShowPolicyAssignmentResponse
        """

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

        :param UpdatePolicyAssignmentRequest request
        :return: UpdatePolicyAssignmentResponse
        """
        return self.update_policy_assignment_with_http_info(request)

    def update_policy_assignment_with_http_info(self, request):
        """更新合规规则

        更新用户的合规规则

        :param UpdatePolicyAssignmentRequest request
        :return: UpdatePolicyAssignmentResponse
        """

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


    def list_regions_async(self, request):
        """查询租户可见的区域

        查询租户可见的区域

        :param ListRegionsRequest request
        :return: ListRegionsResponse
        """
        return self.list_regions_with_http_info(request)

    def list_regions_with_http_info(self, request):
        """查询租户可见的区域

        查询租户可见的区域

        :param ListRegionsRequest request
        :return: ListRegionsResponse
        """

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

        指定资源ID，查询该资源与其他资源的关联关系，可以指定关系方向为\"in\" 或者\"out\"

        :param ShowResourceRelationsRequest request
        :return: ShowResourceRelationsResponse
        """
        return self.show_resource_relations_with_http_info(request)

    def show_resource_relations_with_http_info(self, request):
        """列举资源关系

        指定资源ID，查询该资源与其他资源的关联关系，可以指定关系方向为\"in\" 或者\"out\"

        :param ShowResourceRelationsRequest request
        :return: ShowResourceRelationsResponse
        """

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

        返回当前租户下所有资源，需要当前用户有rms:resources:list权限。

        :param ListAllResourcesRequest request
        :return: ListAllResourcesResponse
        """
        return self.list_all_resources_with_http_info(request)

    def list_all_resources_with_http_info(self, request):
        """列举所有资源

        返回当前租户下所有资源，需要当前用户有rms:resources:list权限。

        :param ListAllResourcesRequest request
        :return: ListAllResourcesResponse
        """

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

        :param ListProvidersRequest request
        :return: ListProvidersResponse
        """
        return self.list_providers_with_http_info(request)

    def list_providers_with_http_info(self, request):
        """列举云服务

        查询RMS支持的云服务、资源、区域列表

        :param ListProvidersRequest request
        :return: ListProvidersResponse
        """

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

        :param ListResourcesRequest request
        :return: ListResourcesResponse
        """
        return self.list_resources_with_http_info(request)

    def list_resources_with_http_info(self, request):
        """列举指定类型的资源

        返回当前租户下特定资源类型的资源，需要当前用户有rms:resources:list权限。比如查询云服务器，对应的RMS资源类型是ecs.cloudservers，其中provider为ecs，type为cloudservers。 RMS支持的服务和资源类型参见[支持的服务和区域](https://console.huaweicloud.com/eps/#/resources/supported)。

        :param ListResourcesRequest request
        :return: ListResourcesResponse
        """

        all_params = ['provider', 'type', 'region_id', 'ep_id', 'limit', 'marker']
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

        :param ShowResourceByIdRequest request
        :return: ShowResourceByIdResponse
        """
        return self.show_resource_by_id_with_http_info(request)

    def show_resource_by_id_with_http_info(self, request):
        """查询单个资源

        指定资源ID，返回该资源的详细信息，需要当前用户有rms:resources:get权限。比如查询云服务器，对应的RMS资源类型是ecs.cloudservers，其中provider为ecs，type为cloudservers。RMS支持的服务和资源类型参见[支持的服务和区域](https://console.huaweicloud.com/eps/#/resources/supported)。

        :param ShowResourceByIdRequest request
        :return: ShowResourceByIdResponse
        """

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

        :param CreateTrackerConfigRequest request
        :return: CreateTrackerConfigResponse
        """
        return self.create_tracker_config_with_http_info(request)

    def create_tracker_config_with_http_info(self, request):
        """创建或更新记录器

        创建或更新资源记录器，只能存在一个资源记录器

        :param CreateTrackerConfigRequest request
        :return: CreateTrackerConfigResponse
        """

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

        :param DeleteTrackerConfigRequest request
        :return: DeleteTrackerConfigResponse
        """
        return self.delete_tracker_config_with_http_info(request)

    def delete_tracker_config_with_http_info(self, request):
        """删除记录器

        删除资源记录器

        :param DeleteTrackerConfigRequest request
        :return: DeleteTrackerConfigResponse
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

        :param ShowTrackerConfigRequest request
        :return: ShowTrackerConfigResponse
        """
        return self.show_tracker_config_with_http_info(request)

    def show_tracker_config_with_http_info(self, request):
        """查询记录器

        查询资源记录器的详细信息

        :param ShowTrackerConfigRequest request
        :return: ShowTrackerConfigResponse
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

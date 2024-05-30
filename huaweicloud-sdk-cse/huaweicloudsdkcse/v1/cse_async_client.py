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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkcse'")


class CseAsyncClient(Client):
    def __init__(self):
        super(CseAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkcse.v1.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "CseAsyncClient":
                raise TypeError("client type error, support client type is CseAsyncClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def create_engine_async(self, request):
        """创建微服务引擎

        创建微服务引擎，支持创建ServiceComb引擎专享版、注册配置中心、应用网关（公测）。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateEngine
        :type request: :class:`huaweicloudsdkcse.v1.CreateEngineRequest`
        :rtype: :class:`huaweicloudsdkcse.v1.CreateEngineResponse`
        """
        http_info = self._create_engine_http_info(request)
        return self._call_api(**http_info)

    def create_engine_async_invoker(self, request):
        http_info = self._create_engine_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_engine_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/enginemgr/engines",
            "request_type": request.__class__.__name__,
            "response_type": "CreateEngineResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_enterprise_project_id' in local_var_params:
            header_params['X-Enterprise-Project-ID'] = local_var_params['x_enterprise_project_id']

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

    def create_governance_policy_async(self, request):
        """创建治理策略

        创建治理策略。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateGovernancePolicy
        :type request: :class:`huaweicloudsdkcse.v1.CreateGovernancePolicyRequest`
        :rtype: :class:`huaweicloudsdkcse.v1.CreateGovernancePolicyResponse`
        """
        http_info = self._create_governance_policy_http_info(request)
        return self._call_api(**http_info)

    def create_governance_policy_async_invoker(self, request):
        http_info = self._create_governance_policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_governance_policy_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/govern/governance/{kind}",
            "request_type": request.__class__.__name__,
            "response_type": "CreateGovernancePolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'kind' in local_var_params:
            path_params['kind'] = local_var_params['kind']

        query_params = []

        header_params = {}
        if 'content_type' in local_var_params:
            header_params['Content-Type'] = local_var_params['content_type']
        if 'x_engine_id' in local_var_params:
            header_params['x-engine-id'] = local_var_params['x_engine_id']
        if 'x_enterprise_project_id' in local_var_params:
            header_params['X-Enterprise-Project-ID'] = local_var_params['x_enterprise_project_id']
        if 'x_environment' in local_var_params:
            header_params['x-environment'] = local_var_params['x_environment']

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

    def create_microservice_route_rule_async(self, request):
        """创建灰度发布策略

        创建灰度发布策略。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateMicroserviceRouteRule
        :type request: :class:`huaweicloudsdkcse.v1.CreateMicroserviceRouteRuleRequest`
        :rtype: :class:`huaweicloudsdkcse.v1.CreateMicroserviceRouteRuleResponse`
        """
        http_info = self._create_microservice_route_rule_http_info(request)
        return self._call_api(**http_info)

    def create_microservice_route_rule_async_invoker(self, request):
        http_info = self._create_microservice_route_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_microservice_route_rule_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/govern/route-rule/microservices/{service_name}",
            "request_type": request.__class__.__name__,
            "response_type": "CreateMicroserviceRouteRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'service_name' in local_var_params:
            path_params['service_name'] = local_var_params['service_name']

        query_params = []
        if 'environment' in local_var_params:
            query_params.append(('environment', local_var_params['environment']))
        if 'app_id' in local_var_params:
            query_params.append(('app_id', local_var_params['app_id']))

        header_params = {}
        if 'content_type' in local_var_params:
            header_params['Content-Type'] = local_var_params['content_type']
        if 'x_engine_id' in local_var_params:
            header_params['x-engine-id'] = local_var_params['x_engine_id']
        if 'x_enterprise_project_id' in local_var_params:
            header_params['X-Enterprise-Project-ID'] = local_var_params['x_enterprise_project_id']

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

    def delete_engine_async(self, request):
        """删除微服务引擎

        删除微服务引擎。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteEngine
        :type request: :class:`huaweicloudsdkcse.v1.DeleteEngineRequest`
        :rtype: :class:`huaweicloudsdkcse.v1.DeleteEngineResponse`
        """
        http_info = self._delete_engine_http_info(request)
        return self._call_api(**http_info)

    def delete_engine_async_invoker(self, request):
        http_info = self._delete_engine_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_engine_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/enginemgr/engines/{engine_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteEngineResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'engine_id' in local_var_params:
            path_params['engine_id'] = local_var_params['engine_id']

        query_params = []

        header_params = {}
        if 'x_enterprise_project_id' in local_var_params:
            header_params['X-Enterprise-Project-ID'] = local_var_params['x_enterprise_project_id']

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

    def delete_governance_policy_async(self, request):
        """删除治理策略

        删除治理策略。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteGovernancePolicy
        :type request: :class:`huaweicloudsdkcse.v1.DeleteGovernancePolicyRequest`
        :rtype: :class:`huaweicloudsdkcse.v1.DeleteGovernancePolicyResponse`
        """
        http_info = self._delete_governance_policy_http_info(request)
        return self._call_api(**http_info)

    def delete_governance_policy_async_invoker(self, request):
        http_info = self._delete_governance_policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_governance_policy_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{project_id}/govern/governance/{kind}/{policy_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteGovernancePolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'kind' in local_var_params:
            path_params['kind'] = local_var_params['kind']
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']

        query_params = []

        header_params = {}
        if 'content_type' in local_var_params:
            header_params['Content-Type'] = local_var_params['content_type']
        if 'x_engine_id' in local_var_params:
            header_params['x-engine-id'] = local_var_params['x_engine_id']
        if 'x_enterprise_project_id' in local_var_params:
            header_params['X-Enterprise-Project-ID'] = local_var_params['x_enterprise_project_id']
        if 'x_environment' in local_var_params:
            header_params['x-environment'] = local_var_params['x_environment']

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

    def delete_microservice_route_rule_async(self, request):
        """删除灰度发布策略

        删除灰度发布策略。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteMicroserviceRouteRule
        :type request: :class:`huaweicloudsdkcse.v1.DeleteMicroserviceRouteRuleRequest`
        :rtype: :class:`huaweicloudsdkcse.v1.DeleteMicroserviceRouteRuleResponse`
        """
        http_info = self._delete_microservice_route_rule_http_info(request)
        return self._call_api(**http_info)

    def delete_microservice_route_rule_async_invoker(self, request):
        http_info = self._delete_microservice_route_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_microservice_route_rule_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{project_id}/govern/route-rule/microservices/{service_name}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteMicroserviceRouteRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'service_name' in local_var_params:
            path_params['service_name'] = local_var_params['service_name']

        query_params = []
        if 'environment' in local_var_params:
            query_params.append(('environment', local_var_params['environment']))
        if 'app_id' in local_var_params:
            query_params.append(('app_id', local_var_params['app_id']))

        header_params = {}
        if 'content_type' in local_var_params:
            header_params['Content-Type'] = local_var_params['content_type']
        if 'x_engine_id' in local_var_params:
            header_params['x-engine-id'] = local_var_params['x_engine_id']
        if 'x_enterprise_project_id' in local_var_params:
            header_params['X-Enterprise-Project-ID'] = local_var_params['x_enterprise_project_id']

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

    def download_kie_async(self, request):
        """导出kie配置

        导出kie配置
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DownloadKie
        :type request: :class:`huaweicloudsdkcse.v1.DownloadKieRequest`
        :rtype: :class:`huaweicloudsdkcse.v1.DownloadKieResponse`
        """
        http_info = self._download_kie_http_info(request)
        return self._call_api(**http_info)

    def download_kie_async_invoker(self, request):
        http_info = self._download_kie_http_info(request)
        return AsyncInvoker(self, http_info)

    def _download_kie_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/kie/download",
            "request_type": request.__class__.__name__,
            "response_type": "DownloadKieResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'label' in local_var_params:
            query_params.append(('label', local_var_params['label']))
        if 'match' in local_var_params:
            query_params.append(('match', local_var_params['match']))

        header_params = {}
        if 'x_enterprise_project_id' in local_var_params:
            header_params['X-Enterprise-Project-ID'] = local_var_params['x_enterprise_project_id']
        if 'x_engine_id' in local_var_params:
            header_params['x-engine-id'] = local_var_params['x_engine_id']

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

    def list_engines_async(self, request):
        """查询微服务引擎列表

        查询微服务引擎列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListEngines
        :type request: :class:`huaweicloudsdkcse.v1.ListEnginesRequest`
        :rtype: :class:`huaweicloudsdkcse.v1.ListEnginesResponse`
        """
        http_info = self._list_engines_http_info(request)
        return self._call_api(**http_info)

    def list_engines_async_invoker(self, request):
        http_info = self._list_engines_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_engines_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/enginemgr/engines",
            "request_type": request.__class__.__name__,
            "response_type": "ListEnginesResponse"
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

    def list_flavors_async(self, request):
        """查询微服务引擎的规格列表

        查询微服务引擎的规格列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListFlavors
        :type request: :class:`huaweicloudsdkcse.v1.ListFlavorsRequest`
        :rtype: :class:`huaweicloudsdkcse.v1.ListFlavorsResponse`
        """
        http_info = self._list_flavors_http_info(request)
        return self._call_api(**http_info)

    def list_flavors_async_invoker(self, request):
        http_info = self._list_flavors_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_flavors_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/enginemgr/flavors",
            "request_type": request.__class__.__name__,
            "response_type": "ListFlavorsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'spec_type' in local_var_params:
            query_params.append(('spec_type', local_var_params['spec_type']))

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

    def list_governance_policy_async(self, request):
        """查询指定类型治理策略列表

        查询指定类型治理策略列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListGovernancePolicy
        :type request: :class:`huaweicloudsdkcse.v1.ListGovernancePolicyRequest`
        :rtype: :class:`huaweicloudsdkcse.v1.ListGovernancePolicyResponse`
        """
        http_info = self._list_governance_policy_http_info(request)
        return self._call_api(**http_info)

    def list_governance_policy_async_invoker(self, request):
        http_info = self._list_governance_policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_governance_policy_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/govern/governance/{kind}",
            "request_type": request.__class__.__name__,
            "response_type": "ListGovernancePolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'kind' in local_var_params:
            path_params['kind'] = local_var_params['kind']

        query_params = []

        header_params = {}
        if 'content_type' in local_var_params:
            header_params['Content-Type'] = local_var_params['content_type']
        if 'x_engine_id' in local_var_params:
            header_params['x-engine-id'] = local_var_params['x_engine_id']
        if 'x_enterprise_project_id' in local_var_params:
            header_params['X-Enterprise-Project-ID'] = local_var_params['x_enterprise_project_id']
        if 'x_environment' in local_var_params:
            header_params['x-environment'] = local_var_params['x_environment']

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

    def list_governance_policy_by_policy_id_async(self, request):
        """查询治理策略详情

        查询治理策略详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListGovernancePolicyByPolicyId
        :type request: :class:`huaweicloudsdkcse.v1.ListGovernancePolicyByPolicyIdRequest`
        :rtype: :class:`huaweicloudsdkcse.v1.ListGovernancePolicyByPolicyIdResponse`
        """
        http_info = self._list_governance_policy_by_policy_id_http_info(request)
        return self._call_api(**http_info)

    def list_governance_policy_by_policy_id_async_invoker(self, request):
        http_info = self._list_governance_policy_by_policy_id_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_governance_policy_by_policy_id_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/govern/governance/{kind}/{policy_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ListGovernancePolicyByPolicyIdResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'kind' in local_var_params:
            path_params['kind'] = local_var_params['kind']
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']

        query_params = []

        header_params = {}
        if 'content_type' in local_var_params:
            header_params['Content-Type'] = local_var_params['content_type']
        if 'x_engine_id' in local_var_params:
            header_params['x-engine-id'] = local_var_params['x_engine_id']
        if 'x_enterprise_project_id' in local_var_params:
            header_params['X-Enterprise-Project-ID'] = local_var_params['x_enterprise_project_id']
        if 'x_environment' in local_var_params:
            header_params['x-environment'] = local_var_params['x_environment']

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

    def list_governance_policys_async(self, request):
        """查询治理策略列表

        查询治理策略列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListGovernancePolicys
        :type request: :class:`huaweicloudsdkcse.v1.ListGovernancePolicysRequest`
        :rtype: :class:`huaweicloudsdkcse.v1.ListGovernancePolicysResponse`
        """
        http_info = self._list_governance_policys_http_info(request)
        return self._call_api(**http_info)

    def list_governance_policys_async_invoker(self, request):
        http_info = self._list_governance_policys_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_governance_policys_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/govern/governance/display",
            "request_type": request.__class__.__name__,
            "response_type": "ListGovernancePolicysResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'environment' in local_var_params:
            query_params.append(('environment', local_var_params['environment']))
        if 'app' in local_var_params:
            query_params.append(('app', local_var_params['app']))

        header_params = {}
        if 'content_type' in local_var_params:
            header_params['Content-Type'] = local_var_params['content_type']
        if 'x_engine_id' in local_var_params:
            header_params['x-engine-id'] = local_var_params['x_engine_id']
        if 'x_enterprise_project_id' in local_var_params:
            header_params['X-Enterprise-Project-ID'] = local_var_params['x_enterprise_project_id']

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

    def list_microservice_route_rule_async(self, request):
        """查询微服务的灰度发布规则

        查询微服务的灰度发布规则。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListMicroserviceRouteRule
        :type request: :class:`huaweicloudsdkcse.v1.ListMicroserviceRouteRuleRequest`
        :rtype: :class:`huaweicloudsdkcse.v1.ListMicroserviceRouteRuleResponse`
        """
        http_info = self._list_microservice_route_rule_http_info(request)
        return self._call_api(**http_info)

    def list_microservice_route_rule_async_invoker(self, request):
        http_info = self._list_microservice_route_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_microservice_route_rule_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/govern/route-rule/microservices/{service_name}",
            "request_type": request.__class__.__name__,
            "response_type": "ListMicroserviceRouteRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'service_name' in local_var_params:
            path_params['service_name'] = local_var_params['service_name']

        query_params = []
        if 'environment' in local_var_params:
            query_params.append(('environment', local_var_params['environment']))
        if 'app_id' in local_var_params:
            query_params.append(('app_id', local_var_params['app_id']))

        header_params = {}
        if 'x_engine_id' in local_var_params:
            header_params['x-engine-id'] = local_var_params['x_engine_id']
        if 'x_enterprise_project_id' in local_var_params:
            header_params['X-Enterprise-Project-ID'] = local_var_params['x_enterprise_project_id']

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

    def resize_engine_async(self, request):
        """变更微服务引擎规格

        变更微服务引擎规格。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ResizeEngine
        :type request: :class:`huaweicloudsdkcse.v1.ResizeEngineRequest`
        :rtype: :class:`huaweicloudsdkcse.v1.ResizeEngineResponse`
        """
        http_info = self._resize_engine_http_info(request)
        return self._call_api(**http_info)

    def resize_engine_async_invoker(self, request):
        http_info = self._resize_engine_http_info(request)
        return AsyncInvoker(self, http_info)

    def _resize_engine_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/enginemgr/engines/{engine_id}/resize",
            "request_type": request.__class__.__name__,
            "response_type": "ResizeEngineResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'engine_id' in local_var_params:
            path_params['engine_id'] = local_var_params['engine_id']

        query_params = []

        header_params = {}
        if 'x_enterprise_project_id' in local_var_params:
            header_params['X-Enterprise-Project-ID'] = local_var_params['x_enterprise_project_id']
        if 'content_type' in local_var_params:
            header_params['Content-Type'] = local_var_params['content_type']
        if 'accept' in local_var_params:
            header_params['Accept'] = local_var_params['accept']

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

    def retry_engine_async(self, request):
        """对微服务引擎进行重试

        对微服务引擎进行重试，当前支持ServiceComb专享版引擎
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RetryEngine
        :type request: :class:`huaweicloudsdkcse.v1.RetryEngineRequest`
        :rtype: :class:`huaweicloudsdkcse.v1.RetryEngineResponse`
        """
        http_info = self._retry_engine_http_info(request)
        return self._call_api(**http_info)

    def retry_engine_async_invoker(self, request):
        http_info = self._retry_engine_http_info(request)
        return AsyncInvoker(self, http_info)

    def _retry_engine_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/enginemgr/engines/{engine_id}/actions",
            "request_type": request.__class__.__name__,
            "response_type": "RetryEngineResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'engine_id' in local_var_params:
            path_params['engine_id'] = local_var_params['engine_id']

        query_params = []

        header_params = {}
        if 'x_enterprise_project_id' in local_var_params:
            header_params['X-Enterprise-Project-ID'] = local_var_params['x_enterprise_project_id']

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

    def show_engine_async(self, request):
        """查询微服务引擎详情

        查询微服务引擎详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowEngine
        :type request: :class:`huaweicloudsdkcse.v1.ShowEngineRequest`
        :rtype: :class:`huaweicloudsdkcse.v1.ShowEngineResponse`
        """
        http_info = self._show_engine_http_info(request)
        return self._call_api(**http_info)

    def show_engine_async_invoker(self, request):
        http_info = self._show_engine_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_engine_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/enginemgr/engines/{engine_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowEngineResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'engine_id' in local_var_params:
            path_params['engine_id'] = local_var_params['engine_id']

        query_params = []

        header_params = {}
        if 'x_enterprise_project_id' in local_var_params:
            header_params['X-Enterprise-Project-ID'] = local_var_params['x_enterprise_project_id']

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

    def show_engine_job_async(self, request):
        """查询微服务引擎任务详情

        查询微服务引擎任务详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowEngineJob
        :type request: :class:`huaweicloudsdkcse.v1.ShowEngineJobRequest`
        :rtype: :class:`huaweicloudsdkcse.v1.ShowEngineJobResponse`
        """
        http_info = self._show_engine_job_http_info(request)
        return self._call_api(**http_info)

    def show_engine_job_async_invoker(self, request):
        http_info = self._show_engine_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_engine_job_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/enginemgr/engines/{engine_id}/jobs/{job_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowEngineJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'engine_id' in local_var_params:
            path_params['engine_id'] = local_var_params['engine_id']
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []

        header_params = {}
        if 'x_enterprise_project_id' in local_var_params:
            header_params['X-Enterprise-Project-ID'] = local_var_params['x_enterprise_project_id']

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

    def show_engine_quotas_async(self, request):
        """查询微服务引擎配额

        查询微服务引擎配额。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowEngineQuotas
        :type request: :class:`huaweicloudsdkcse.v1.ShowEngineQuotasRequest`
        :rtype: :class:`huaweicloudsdkcse.v1.ShowEngineQuotasResponse`
        """
        http_info = self._show_engine_quotas_http_info(request)
        return self._call_api(**http_info)

    def show_engine_quotas_async_invoker(self, request):
        http_info = self._show_engine_quotas_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_engine_quotas_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/enginemgr/quotas",
            "request_type": request.__class__.__name__,
            "response_type": "ShowEngineQuotasResponse"
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

    def update_governance_policy_async(self, request):
        """修改治理策略

        修改治理策略。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateGovernancePolicy
        :type request: :class:`huaweicloudsdkcse.v1.UpdateGovernancePolicyRequest`
        :rtype: :class:`huaweicloudsdkcse.v1.UpdateGovernancePolicyResponse`
        """
        http_info = self._update_governance_policy_http_info(request)
        return self._call_api(**http_info)

    def update_governance_policy_async_invoker(self, request):
        http_info = self._update_governance_policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_governance_policy_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/govern/governance/{kind}/{policy_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateGovernancePolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'kind' in local_var_params:
            path_params['kind'] = local_var_params['kind']
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']

        query_params = []

        header_params = {}
        if 'content_type' in local_var_params:
            header_params['Content-Type'] = local_var_params['content_type']
        if 'x_engine_id' in local_var_params:
            header_params['x-engine-id'] = local_var_params['x_engine_id']
        if 'x_enterprise_project_id' in local_var_params:
            header_params['X-Enterprise-Project-ID'] = local_var_params['x_enterprise_project_id']
        if 'x_environment' in local_var_params:
            header_params['x-environment'] = local_var_params['x_environment']

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

    def upgrade_engine_async(self, request):
        """升级微服务引擎

        升级微服务引擎
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpgradeEngine
        :type request: :class:`huaweicloudsdkcse.v1.UpgradeEngineRequest`
        :rtype: :class:`huaweicloudsdkcse.v1.UpgradeEngineResponse`
        """
        http_info = self._upgrade_engine_http_info(request)
        return self._call_api(**http_info)

    def upgrade_engine_async_invoker(self, request):
        http_info = self._upgrade_engine_http_info(request)
        return AsyncInvoker(self, http_info)

    def _upgrade_engine_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/enginemgr/engines/{engine_id}/upgrade",
            "request_type": request.__class__.__name__,
            "response_type": "UpgradeEngineResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'engine_id' in local_var_params:
            path_params['engine_id'] = local_var_params['engine_id']

        query_params = []

        header_params = {}
        if 'x_enterprise_project_id' in local_var_params:
            header_params['X-Enterprise-Project-ID'] = local_var_params['x_enterprise_project_id']

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

    def upgrade_engine_config_async(self, request):
        """更新微服务引擎配置

        更新微服务引擎配置，更新ServiceComb专享版引擎与注册配置中心引擎的配置
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpgradeEngineConfig
        :type request: :class:`huaweicloudsdkcse.v1.UpgradeEngineConfigRequest`
        :rtype: :class:`huaweicloudsdkcse.v1.UpgradeEngineConfigResponse`
        """
        http_info = self._upgrade_engine_config_http_info(request)
        return self._call_api(**http_info)

    def upgrade_engine_config_async_invoker(self, request):
        http_info = self._upgrade_engine_config_http_info(request)
        return AsyncInvoker(self, http_info)

    def _upgrade_engine_config_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/enginemgr/engines/{engine_id}/config",
            "request_type": request.__class__.__name__,
            "response_type": "UpgradeEngineConfigResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'engine_id' in local_var_params:
            path_params['engine_id'] = local_var_params['engine_id']

        query_params = []

        header_params = {}
        if 'x_enterprise_project_id' in local_var_params:
            header_params['X-Enterprise-Project-ID'] = local_var_params['x_enterprise_project_id']

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

    def upload_kie_async(self, request):
        """导入kie配置

        导入kie配置
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UploadKie
        :type request: :class:`huaweicloudsdkcse.v1.UploadKieRequest`
        :rtype: :class:`huaweicloudsdkcse.v1.UploadKieResponse`
        """
        http_info = self._upload_kie_http_info(request)
        return self._call_api(**http_info)

    def upload_kie_async_invoker(self, request):
        http_info = self._upload_kie_http_info(request)
        return AsyncInvoker(self, http_info)

    def _upload_kie_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/kie/file",
            "request_type": request.__class__.__name__,
            "response_type": "UploadKieResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'override' in local_var_params:
            query_params.append(('override', local_var_params['override']))
        if 'label' in local_var_params:
            query_params.append(('label', local_var_params['label']))

        header_params = {}
        if 'x_enterprise_project_id' in local_var_params:
            header_params['X-Enterprise-Project-ID'] = local_var_params['x_enterprise_project_id']
        if 'x_engine_id' in local_var_params:
            header_params['x-engine-id'] = local_var_params['x_engine_id']

        form_params = {}
        if 'upload_file' in local_var_params:
            form_params['upload_file'] = local_var_params['upload_file']

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['multipart/form-data'])

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

    def create_http2_rpc_async(self, request):
        """创建http转rpc方法

        创建http转rpc方法。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateHttp2Rpc
        :type request: :class:`huaweicloudsdkcse.v1.CreateHttp2RpcRequest`
        :rtype: :class:`huaweicloudsdkcse.v1.CreateHttp2RpcResponse`
        """
        http_info = self._create_http2_rpc_http_info(request)
        return self._call_api(**http_info)

    def create_http2_rpc_async_invoker(self, request):
        http_info = self._create_http2_rpc_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_http2_rpc_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/enginemgr/gateways/{gateway_id}/http2Rpcs",
            "request_type": request.__class__.__name__,
            "response_type": "CreateHttp2RpcResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'gateway_id' in local_var_params:
            path_params['gateway_id'] = local_var_params['gateway_id']

        query_params = []

        header_params = {}
        if 'accept' in local_var_params:
            header_params['Accept'] = local_var_params['accept']

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

    def create_plugin_async(self, request):
        """创建插件

        创建插件。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreatePlugin
        :type request: :class:`huaweicloudsdkcse.v1.CreatePluginRequest`
        :rtype: :class:`huaweicloudsdkcse.v1.CreatePluginResponse`
        """
        http_info = self._create_plugin_http_info(request)
        return self._call_api(**http_info)

    def create_plugin_async_invoker(self, request):
        http_info = self._create_plugin_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_plugin_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/enginemgr/gateways/{gateway_id}/plugins",
            "request_type": request.__class__.__name__,
            "response_type": "CreatePluginResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'gateway_id' in local_var_params:
            path_params['gateway_id'] = local_var_params['gateway_id']

        query_params = []

        header_params = {}
        if 'accept' in local_var_params:
            header_params['Accept'] = local_var_params['accept']

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

    def delete_http2_rpc_async(self, request):
        """删除http转rpc方法

        删除http转rpc方法。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteHttp2Rpc
        :type request: :class:`huaweicloudsdkcse.v1.DeleteHttp2RpcRequest`
        :rtype: :class:`huaweicloudsdkcse.v1.DeleteHttp2RpcResponse`
        """
        http_info = self._delete_http2_rpc_http_info(request)
        return self._call_api(**http_info)

    def delete_http2_rpc_async_invoker(self, request):
        http_info = self._delete_http2_rpc_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_http2_rpc_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/enginemgr/gateways/{gateway_id}/http2Rpcs/{http2Rpc_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteHttp2RpcResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'gateway_id' in local_var_params:
            path_params['gateway_id'] = local_var_params['gateway_id']
        if 'http2_rpc_id' in local_var_params:
            path_params['http2Rpc_id'] = local_var_params['http2_rpc_id']

        query_params = []

        header_params = {}
        if 'accept' in local_var_params:
            header_params['Accept'] = local_var_params['accept']

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

    def delete_plugin_async(self, request):
        """删除插件

        删除插件。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeletePlugin
        :type request: :class:`huaweicloudsdkcse.v1.DeletePluginRequest`
        :rtype: :class:`huaweicloudsdkcse.v1.DeletePluginResponse`
        """
        http_info = self._delete_plugin_http_info(request)
        return self._call_api(**http_info)

    def delete_plugin_async_invoker(self, request):
        http_info = self._delete_plugin_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_plugin_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/enginemgr/gateways/{gateway_id}/plugins/{plugin_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeletePluginResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'gateway_id' in local_var_params:
            path_params['gateway_id'] = local_var_params['gateway_id']
        if 'plugin_id' in local_var_params:
            path_params['plugin_id'] = local_var_params['plugin_id']

        query_params = []

        header_params = {}
        if 'accept' in local_var_params:
            header_params['Accept'] = local_var_params['accept']

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

    def modify_http2_rpc_async(self, request):
        """修改http转rpc方法

        修改http转rpc方法。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ModifyHttp2Rpc
        :type request: :class:`huaweicloudsdkcse.v1.ModifyHttp2RpcRequest`
        :rtype: :class:`huaweicloudsdkcse.v1.ModifyHttp2RpcResponse`
        """
        http_info = self._modify_http2_rpc_http_info(request)
        return self._call_api(**http_info)

    def modify_http2_rpc_async_invoker(self, request):
        http_info = self._modify_http2_rpc_http_info(request)
        return AsyncInvoker(self, http_info)

    def _modify_http2_rpc_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/enginemgr/gateways/{gateway_id}/http2Rpcs/{http2Rpc_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ModifyHttp2RpcResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'gateway_id' in local_var_params:
            path_params['gateway_id'] = local_var_params['gateway_id']
        if 'http2_rpc_id' in local_var_params:
            path_params['http2Rpc_id'] = local_var_params['http2_rpc_id']

        query_params = []

        header_params = {}
        if 'accept' in local_var_params:
            header_params['Accept'] = local_var_params['accept']

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

    def modify_plugin_async(self, request):
        """修改插件

        修改插件。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ModifyPlugin
        :type request: :class:`huaweicloudsdkcse.v1.ModifyPluginRequest`
        :rtype: :class:`huaweicloudsdkcse.v1.ModifyPluginResponse`
        """
        http_info = self._modify_plugin_http_info(request)
        return self._call_api(**http_info)

    def modify_plugin_async_invoker(self, request):
        http_info = self._modify_plugin_http_info(request)
        return AsyncInvoker(self, http_info)

    def _modify_plugin_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/enginemgr/gateways/{gateway_id}/plugins/{plugin_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ModifyPluginResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'gateway_id' in local_var_params:
            path_params['gateway_id'] = local_var_params['gateway_id']
        if 'plugin_id' in local_var_params:
            path_params['plugin_id'] = local_var_params['plugin_id']

        query_params = []

        header_params = {}
        if 'accept' in local_var_params:
            header_params['Accept'] = local_var_params['accept']

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

    def show_http2_rpcs_async(self, request):
        """查询http2rpc资源列表

        查询http转rpc资源列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowHttp2Rpcs
        :type request: :class:`huaweicloudsdkcse.v1.ShowHttp2RpcsRequest`
        :rtype: :class:`huaweicloudsdkcse.v1.ShowHttp2RpcsResponse`
        """
        http_info = self._show_http2_rpcs_http_info(request)
        return self._call_api(**http_info)

    def show_http2_rpcs_async_invoker(self, request):
        http_info = self._show_http2_rpcs_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_http2_rpcs_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/enginemgr/gateways/{gateway_id}/http2Rpcs",
            "request_type": request.__class__.__name__,
            "response_type": "ShowHttp2RpcsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'gateway_id' in local_var_params:
            path_params['gateway_id'] = local_var_params['gateway_id']

        query_params = []

        header_params = {}
        if 'accept' in local_var_params:
            header_params['Accept'] = local_var_params['accept']

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

    def show_plugins_async(self, request):
        """查询插件列表

        查询插件列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowPlugins
        :type request: :class:`huaweicloudsdkcse.v1.ShowPluginsRequest`
        :rtype: :class:`huaweicloudsdkcse.v1.ShowPluginsResponse`
        """
        http_info = self._show_plugins_http_info(request)
        return self._call_api(**http_info)

    def show_plugins_async_invoker(self, request):
        http_info = self._show_plugins_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_plugins_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/enginemgr/gateways/{gateway_id}/plugins",
            "request_type": request.__class__.__name__,
            "response_type": "ShowPluginsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'gateway_id' in local_var_params:
            path_params['gateway_id'] = local_var_params['gateway_id']

        query_params = []

        header_params = {}
        if 'accept' in local_var_params:
            header_params['Accept'] = local_var_params['accept']

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

    def show_single_plugin_async(self, request):
        """查询单个插件

        查询单个插件。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowSinglePlugin
        :type request: :class:`huaweicloudsdkcse.v1.ShowSinglePluginRequest`
        :rtype: :class:`huaweicloudsdkcse.v1.ShowSinglePluginResponse`
        """
        http_info = self._show_single_plugin_http_info(request)
        return self._call_api(**http_info)

    def show_single_plugin_async_invoker(self, request):
        http_info = self._show_single_plugin_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_single_plugin_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/enginemgr/gateways/{gateway_id}/plugins/{plugin_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowSinglePluginResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'gateway_id' in local_var_params:
            path_params['gateway_id'] = local_var_params['gateway_id']
        if 'plugin_id' in local_var_params:
            path_params['plugin_id'] = local_var_params['plugin_id']

        query_params = []

        header_params = {}
        if 'accept' in local_var_params:
            header_params['Accept'] = local_var_params['accept']

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

    def create_nacos_namespaces_async(self, request):
        """创建nacos命名空间

        创建nacos命名空间。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateNacosNamespaces
        :type request: :class:`huaweicloudsdkcse.v1.CreateNacosNamespacesRequest`
        :rtype: :class:`huaweicloudsdkcse.v1.CreateNacosNamespacesResponse`
        """
        http_info = self._create_nacos_namespaces_http_info(request)
        return self._call_api(**http_info)

    def create_nacos_namespaces_async_invoker(self, request):
        http_info = self._create_nacos_namespaces_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_nacos_namespaces_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/nacos/v1/console/namespaces",
            "request_type": request.__class__.__name__,
            "response_type": "CreateNacosNamespacesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'custom_namespace_id' in local_var_params:
            query_params.append(('custom_namespace_id', local_var_params['custom_namespace_id']))
        if 'namespace_name' in local_var_params:
            query_params.append(('namespace_name', local_var_params['namespace_name']))
        if 'namespace_desc' in local_var_params:
            query_params.append(('namespace_desc', local_var_params['namespace_desc']))

        header_params = {}
        if 'x_engine_id' in local_var_params:
            header_params['x-engine-id'] = local_var_params['x_engine_id']
        if 'x_enterprise_project_id' in local_var_params:
            header_params['X-Enterprise-Project-ID'] = local_var_params['x_enterprise_project_id']

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

    def delete_nacos_namespaces_async(self, request):
        """删除nacos命名空间

        删除nacos命名空间。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteNacosNamespaces
        :type request: :class:`huaweicloudsdkcse.v1.DeleteNacosNamespacesRequest`
        :rtype: :class:`huaweicloudsdkcse.v1.DeleteNacosNamespacesResponse`
        """
        http_info = self._delete_nacos_namespaces_http_info(request)
        return self._call_api(**http_info)

    def delete_nacos_namespaces_async_invoker(self, request):
        http_info = self._delete_nacos_namespaces_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_nacos_namespaces_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/nacos/v1/console/namespaces",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteNacosNamespacesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'namespace_id' in local_var_params:
            query_params.append(('namespace_id', local_var_params['namespace_id']))

        header_params = {}
        if 'x_engine_id' in local_var_params:
            header_params['x-engine-id'] = local_var_params['x_engine_id']
        if 'x_enterprise_project_id' in local_var_params:
            header_params['X-Enterprise-Project-ID'] = local_var_params['x_enterprise_project_id']

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

    def list_nacos_namespaces_async(self, request):
        """查询nacos命名空间

        查询nacos命名空间。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListNacosNamespaces
        :type request: :class:`huaweicloudsdkcse.v1.ListNacosNamespacesRequest`
        :rtype: :class:`huaweicloudsdkcse.v1.ListNacosNamespacesResponse`
        """
        http_info = self._list_nacos_namespaces_http_info(request)
        return self._call_api(**http_info)

    def list_nacos_namespaces_async_invoker(self, request):
        http_info = self._list_nacos_namespaces_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_nacos_namespaces_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/nacos/v1/console/namespaces",
            "request_type": request.__class__.__name__,
            "response_type": "ListNacosNamespacesResponse"
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

        header_params = {}
        if 'x_engine_id' in local_var_params:
            header_params['x-engine-id'] = local_var_params['x_engine_id']
        if 'x_enterprise_project_id' in local_var_params:
            header_params['X-Enterprise-Project-ID'] = local_var_params['x_enterprise_project_id']

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

    def update_nacos_namespaces_async(self, request):
        """更新nacos命名空间

        更新nacos命名空间。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateNacosNamespaces
        :type request: :class:`huaweicloudsdkcse.v1.UpdateNacosNamespacesRequest`
        :rtype: :class:`huaweicloudsdkcse.v1.UpdateNacosNamespacesResponse`
        """
        http_info = self._update_nacos_namespaces_http_info(request)
        return self._call_api(**http_info)

    def update_nacos_namespaces_async_invoker(self, request):
        http_info = self._update_nacos_namespaces_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_nacos_namespaces_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/nacos/v1/console/namespaces",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateNacosNamespacesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'namespace' in local_var_params:
            query_params.append(('namespace', local_var_params['namespace']))
        if 'namespace_show_name' in local_var_params:
            query_params.append(('namespace_show_name', local_var_params['namespace_show_name']))
        if 'namespace_desc' in local_var_params:
            query_params.append(('namespace_desc', local_var_params['namespace_desc']))

        header_params = {}
        if 'x_engine_id' in local_var_params:
            header_params['x-engine-id'] = local_var_params['x_engine_id']
        if 'x_enterprise_project_id' in local_var_params:
            header_params['X-Enterprise-Project-ID'] = local_var_params['x_enterprise_project_id']

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

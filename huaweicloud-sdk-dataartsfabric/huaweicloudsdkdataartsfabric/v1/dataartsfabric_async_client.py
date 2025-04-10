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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkdataartsfabric'")


class DataArtsFabricAsyncClient(Client):
    def __init__(self):
        super(DataArtsFabricAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkdataartsfabric.v1.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "DataArtsFabricAsyncClient":
                raise TypeError("client type error, support client type is DataArtsFabricAsyncClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def create_agency_async(self, request):
        r"""创建服务委托

        为用户自动创建服务所需要的服务委托。委托需要附加必需的权限策略才能使用，创建委托会自动附加必需的权限策略，也可以指定附加需要的权限策略。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateAgency
        :type request: :class:`huaweicloudsdkdataartsfabric.v1.CreateAgencyRequest`
        :rtype: :class:`huaweicloudsdkdataartsfabric.v1.CreateAgencyResponse`
        """
        http_info = self._create_agency_http_info(request)
        return self._call_api(**http_info)

    def create_agency_async_invoker(self, request):
        http_info = self._create_agency_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_agency_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/agency",
            "request_type": request.__class__.__name__,
            "response_type": "CreateAgencyResponse"
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

    def delete_agency_async(self, request):
        r"""删除服务委托

        删除用户的服务委托权限。可以通过指定权限策略来删除委托中附加的权限策略，必需的权限策略无法被删除；如果不指定权限策略，会删除整个委托。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteAgency
        :type request: :class:`huaweicloudsdkdataartsfabric.v1.DeleteAgencyRequest`
        :rtype: :class:`huaweicloudsdkdataartsfabric.v1.DeleteAgencyResponse`
        """
        http_info = self._delete_agency_http_info(request)
        return self._call_api(**http_info)

    def delete_agency_async_invoker(self, request):
        http_info = self._delete_agency_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_agency_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/agency",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteAgencyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'policy_type' in local_var_params:
            query_params.append(('policy_type', local_var_params['policy_type']))

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

    def list_agency_async(self, request):
        r"""查询服务委托

        查询用用户服务委托详情是否满足系统所需权限。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAgency
        :type request: :class:`huaweicloudsdkdataartsfabric.v1.ListAgencyRequest`
        :rtype: :class:`huaweicloudsdkdataartsfabric.v1.ListAgencyResponse`
        """
        http_info = self._list_agency_http_info(request)
        return self._call_api(**http_info)

    def list_agency_async_invoker(self, request):
        http_info = self._list_agency_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_agency_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/agency",
            "request_type": request.__class__.__name__,
            "response_type": "ListAgencyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'policy_type' in local_var_params:
            query_params.append(('policy_type', local_var_params['policy_type']))

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

    def create_agreement_async(self, request):
        r"""注册租户协议

        注册租户协议
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateAgreement
        :type request: :class:`huaweicloudsdkdataartsfabric.v1.CreateAgreementRequest`
        :rtype: :class:`huaweicloudsdkdataartsfabric.v1.CreateAgreementResponse`
        """
        http_info = self._create_agreement_http_info(request)
        return self._call_api(**http_info)

    def create_agreement_async_invoker(self, request):
        http_info = self._create_agreement_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_agreement_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/agreement",
            "request_type": request.__class__.__name__,
            "response_type": "CreateAgreementResponse"
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

    def delete_agreement_async(self, request):
        r"""删除用户注册协议

        删除用户注册协议
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteAgreement
        :type request: :class:`huaweicloudsdkdataartsfabric.v1.DeleteAgreementRequest`
        :rtype: :class:`huaweicloudsdkdataartsfabric.v1.DeleteAgreementResponse`
        """
        http_info = self._delete_agreement_http_info(request)
        return self._call_api(**http_info)

    def delete_agreement_async_invoker(self, request):
        http_info = self._delete_agreement_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_agreement_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/agreement",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteAgreementResponse"
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

    def show_agreement_async(self, request):
        r"""查询用户是否注册协议

        查询用户是否注册协议
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowAgreement
        :type request: :class:`huaweicloudsdkdataartsfabric.v1.ShowAgreementRequest`
        :rtype: :class:`huaweicloudsdkdataartsfabric.v1.ShowAgreementResponse`
        """
        http_info = self._show_agreement_http_info(request)
        return self._call_api(**http_info)

    def show_agreement_async_invoker(self, request):
        http_info = self._show_agreement_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_agreement_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/agreement",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAgreementResponse"
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

    def show_agreement_rule_async(self, request):
        r"""查询系统协议

        查询系统协议
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowAgreementRule
        :type request: :class:`huaweicloudsdkdataartsfabric.v1.ShowAgreementRuleRequest`
        :rtype: :class:`huaweicloudsdkdataartsfabric.v1.ShowAgreementRuleResponse`
        """
        http_info = self._show_agreement_rule_http_info(request)
        return self._call_api(**http_info)

    def show_agreement_rule_async_invoker(self, request):
        http_info = self._show_agreement_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_agreement_rule_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/agreement-rule",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAgreementRuleResponse"
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

    def list_features_async(self, request):
        r"""查询用户支持特性

        查询用户支持特性。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListFeatures
        :type request: :class:`huaweicloudsdkdataartsfabric.v1.ListFeaturesRequest`
        :rtype: :class:`huaweicloudsdkdataartsfabric.v1.ListFeaturesResponse`
        """
        http_info = self._list_features_http_info(request)
        return self._call_api(**http_info)

    def list_features_async_invoker(self, request):
        http_info = self._list_features_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_features_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/features",
            "request_type": request.__class__.__name__,
            "response_type": "ListFeaturesResponse"
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

    def create_endpoint_async(self, request):
        r"""创建Endpoint

        创建Endpoint
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateEndpoint
        :type request: :class:`huaweicloudsdkdataartsfabric.v1.CreateEndpointRequest`
        :rtype: :class:`huaweicloudsdkdataartsfabric.v1.CreateEndpointResponse`
        """
        http_info = self._create_endpoint_http_info(request)
        return self._call_api(**http_info)

    def create_endpoint_async_invoker(self, request):
        http_info = self._create_endpoint_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_endpoint_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/workspaces/{workspace_id}/endpoints",
            "request_type": request.__class__.__name__,
            "response_type": "CreateEndpointResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def delete_endpoint_async(self, request):
        r"""删除endpioint

        删除endpioint
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteEndpoint
        :type request: :class:`huaweicloudsdkdataartsfabric.v1.DeleteEndpointRequest`
        :rtype: :class:`huaweicloudsdkdataartsfabric.v1.DeleteEndpointResponse`
        """
        http_info = self._delete_endpoint_http_info(request)
        return self._call_api(**http_info)

    def delete_endpoint_async_invoker(self, request):
        http_info = self._delete_endpoint_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_endpoint_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/workspaces/{workspace_id}/endpoints/{endpoint_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteEndpointResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'endpoint_id' in local_var_params:
            path_params['endpoint_id'] = local_var_params['endpoint_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def list_endpoints_async(self, request):
        r"""查询Endpoint列表

        查询Endpoint列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListEndpoints
        :type request: :class:`huaweicloudsdkdataartsfabric.v1.ListEndpointsRequest`
        :rtype: :class:`huaweicloudsdkdataartsfabric.v1.ListEndpointsResponse`
        """
        http_info = self._list_endpoints_http_info(request)
        return self._call_api(**http_info)

    def list_endpoints_async_invoker(self, request):
        http_info = self._list_endpoints_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_endpoints_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/workspaces/{workspace_id}/endpoints",
            "request_type": request.__class__.__name__,
            "response_type": "ListEndpointsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'model_id' in local_var_params:
            query_params.append(('model_id', local_var_params['model_id']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'endpoint_id' in local_var_params:
            query_params.append(('endpoint_id', local_var_params['endpoint_id']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'visibility' in local_var_params:
            query_params.append(('visibility', local_var_params['visibility']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def show_endpoint_async(self, request):
        r"""查询endpioint详情

        查询endpioint详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowEndpoint
        :type request: :class:`huaweicloudsdkdataartsfabric.v1.ShowEndpointRequest`
        :rtype: :class:`huaweicloudsdkdataartsfabric.v1.ShowEndpointResponse`
        """
        http_info = self._show_endpoint_http_info(request)
        return self._call_api(**http_info)

    def show_endpoint_async_invoker(self, request):
        http_info = self._show_endpoint_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_endpoint_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/workspaces/{workspace_id}/endpoints/{endpoint_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowEndpointResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'endpoint_id' in local_var_params:
            path_params['endpoint_id'] = local_var_params['endpoint_id']

        query_params = []
        if 'version' in local_var_params:
            query_params.append(('version', local_var_params['version']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def subscribe_endpoint_async(self, request):
        r"""订阅Endpoint

        在用户Workspace下订阅Endpoint（公共Endpoint场景）。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for SubscribeEndpoint
        :type request: :class:`huaweicloudsdkdataartsfabric.v1.SubscribeEndpointRequest`
        :rtype: :class:`huaweicloudsdkdataartsfabric.v1.SubscribeEndpointResponse`
        """
        http_info = self._subscribe_endpoint_http_info(request)
        return self._call_api(**http_info)

    def subscribe_endpoint_async_invoker(self, request):
        http_info = self._subscribe_endpoint_http_info(request)
        return AsyncInvoker(self, http_info)

    def _subscribe_endpoint_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/workspaces/{workspace_id}/endpoints/{endpoint_id}/subscribe",
            "request_type": request.__class__.__name__,
            "response_type": "SubscribeEndpointResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'endpoint_id' in local_var_params:
            path_params['endpoint_id'] = local_var_params['endpoint_id']

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

    def update_endpoint_async(self, request):
        r"""修改Endpoint

        修改Endpoint
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateEndpoint
        :type request: :class:`huaweicloudsdkdataartsfabric.v1.UpdateEndpointRequest`
        :rtype: :class:`huaweicloudsdkdataartsfabric.v1.UpdateEndpointResponse`
        """
        http_info = self._update_endpoint_http_info(request)
        return self._call_api(**http_info)

    def update_endpoint_async_invoker(self, request):
        http_info = self._update_endpoint_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_endpoint_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/workspaces/{workspace_id}/endpoints/{endpoint_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateEndpointResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'endpoint_id' in local_var_params:
            path_params['endpoint_id'] = local_var_params['endpoint_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def show_admin_health_check_async(self, request):
        r"""健康检查

        服务健康检查
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowAdminHealthCheck
        :type request: :class:`huaweicloudsdkdataartsfabric.v1.ShowAdminHealthCheckRequest`
        :rtype: :class:`huaweicloudsdkdataartsfabric.v1.ShowAdminHealthCheckResponse`
        """
        http_info = self._show_admin_health_check_http_info(request)
        return self._call_api(**http_info)

    def show_admin_health_check_async_invoker(self, request):
        http_info = self._show_admin_health_check_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_admin_health_check_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/healthcheck",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAdminHealthCheckResponse"
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

    def create_message_notification_policy_async(self, request):
        r"""创建消息通知策略

        创建消息通知策略
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateMessageNotificationPolicy
        :type request: :class:`huaweicloudsdkdataartsfabric.v1.CreateMessageNotificationPolicyRequest`
        :rtype: :class:`huaweicloudsdkdataartsfabric.v1.CreateMessageNotificationPolicyResponse`
        """
        http_info = self._create_message_notification_policy_http_info(request)
        return self._call_api(**http_info)

    def create_message_notification_policy_async_invoker(self, request):
        http_info = self._create_message_notification_policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_message_notification_policy_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/workspaces/{workspace_id}/messages",
            "request_type": request.__class__.__name__,
            "response_type": "CreateMessageNotificationPolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

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

    def delete_message_notification_policy_async(self, request):
        r"""删除消息通知策略

        删除消息通知策略。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteMessageNotificationPolicy
        :type request: :class:`huaweicloudsdkdataartsfabric.v1.DeleteMessageNotificationPolicyRequest`
        :rtype: :class:`huaweicloudsdkdataartsfabric.v1.DeleteMessageNotificationPolicyResponse`
        """
        http_info = self._delete_message_notification_policy_http_info(request)
        return self._call_api(**http_info)

    def delete_message_notification_policy_async_invoker(self, request):
        http_info = self._delete_message_notification_policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_message_notification_policy_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/workspaces/{workspace_id}/messages/{message_policy_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteMessageNotificationPolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'message_policy_id' in local_var_params:
            path_params['message_policy_id'] = local_var_params['message_policy_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

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

    def list_message_notification_policy_async(self, request):
        r"""查询消息通知策略列表

        查询消息通知策略列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListMessageNotificationPolicy
        :type request: :class:`huaweicloudsdkdataartsfabric.v1.ListMessageNotificationPolicyRequest`
        :rtype: :class:`huaweicloudsdkdataartsfabric.v1.ListMessageNotificationPolicyResponse`
        """
        http_info = self._list_message_notification_policy_http_info(request)
        return self._call_api(**http_info)

    def list_message_notification_policy_async_invoker(self, request):
        http_info = self._list_message_notification_policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_message_notification_policy_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/workspaces/{workspace_id}/messages",
            "request_type": request.__class__.__name__,
            "response_type": "ListMessageNotificationPolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'message_type' in local_var_params:
            query_params.append(('message_type', local_var_params['message_type']))
        if 'name_pattern' in local_var_params:
            query_params.append(('name_pattern', local_var_params['name_pattern']))
        if 'notify_type' in local_var_params:
            query_params.append(('notify_type', local_var_params['notify_type']))

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

    def update_metrics_config_async(self, request):
        r"""更新AOM监控采集配置

        更新AOM监控采集配置
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateMetricsConfig
        :type request: :class:`huaweicloudsdkdataartsfabric.v1.UpdateMetricsConfigRequest`
        :rtype: :class:`huaweicloudsdkdataartsfabric.v1.UpdateMetricsConfigResponse`
        """
        http_info = self._update_metrics_config_http_info(request)
        return self._call_api(**http_info)

    def update_metrics_config_async_invoker(self, request):
        http_info = self._update_metrics_config_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_metrics_config_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/workspaces/{workspace_id}/metrics",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateMetricsConfigResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

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

    def cleanup_model_async(self, request):
        r"""删除未使用的模型定义

        清理未使用的模型定义
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CleanupModel
        :type request: :class:`huaweicloudsdkdataartsfabric.v1.CleanupModelRequest`
        :rtype: :class:`huaweicloudsdkdataartsfabric.v1.CleanupModelResponse`
        """
        http_info = self._cleanup_model_http_info(request)
        return self._call_api(**http_info)

    def cleanup_model_async_invoker(self, request):
        http_info = self._cleanup_model_http_info(request)
        return AsyncInvoker(self, http_info)

    def _cleanup_model_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/workspaces/{workspace_id}/models/{model_id}",
            "request_type": request.__class__.__name__,
            "response_type": "CleanupModelResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'model_id' in local_var_params:
            path_params['model_id'] = local_var_params['model_id']

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

    def create_model_definition_async(self, request):
        r"""创建模型

        创建模型
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateModelDefinition
        :type request: :class:`huaweicloudsdkdataartsfabric.v1.CreateModelDefinitionRequest`
        :rtype: :class:`huaweicloudsdkdataartsfabric.v1.CreateModelDefinitionResponse`
        """
        http_info = self._create_model_definition_http_info(request)
        return self._call_api(**http_info)

    def create_model_definition_async_invoker(self, request):
        http_info = self._create_model_definition_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_model_definition_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/workspaces/{workspace_id}/models",
            "request_type": request.__class__.__name__,
            "response_type": "CreateModelDefinitionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def delete_model_version_async(self, request):
        r"""删除模型版本

        删除模型版本
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteModelVersion
        :type request: :class:`huaweicloudsdkdataartsfabric.v1.DeleteModelVersionRequest`
        :rtype: :class:`huaweicloudsdkdataartsfabric.v1.DeleteModelVersionResponse`
        """
        http_info = self._delete_model_version_http_info(request)
        return self._call_api(**http_info)

    def delete_model_version_async_invoker(self, request):
        http_info = self._delete_model_version_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_model_version_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/workspaces/{workspace_id}/models/{model_id}/versions/{version_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteModelVersionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'model_id' in local_var_params:
            path_params['model_id'] = local_var_params['model_id']
        if 'version_id' in local_var_params:
            path_params['version_id'] = local_var_params['version_id']

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

    def list_base_models_async(self, request):
        r"""列举基模型

        列举基模型
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListBaseModels
        :type request: :class:`huaweicloudsdkdataartsfabric.v1.ListBaseModelsRequest`
        :rtype: :class:`huaweicloudsdkdataartsfabric.v1.ListBaseModelsResponse`
        """
        http_info = self._list_base_models_http_info(request)
        return self._call_api(**http_info)

    def list_base_models_async_invoker(self, request):
        http_info = self._list_base_models_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_base_models_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/base-models",
            "request_type": request.__class__.__name__,
            "response_type": "ListBaseModelsResponse"
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

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def list_model_versions_async(self, request):
        r"""查询模型的版本列表

        查询模型的版本列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListModelVersions
        :type request: :class:`huaweicloudsdkdataartsfabric.v1.ListModelVersionsRequest`
        :rtype: :class:`huaweicloudsdkdataartsfabric.v1.ListModelVersionsResponse`
        """
        http_info = self._list_model_versions_http_info(request)
        return self._call_api(**http_info)

    def list_model_versions_async_invoker(self, request):
        http_info = self._list_model_versions_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_model_versions_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/workspaces/{workspace_id}/models/{model_id}/versions",
            "request_type": request.__class__.__name__,
            "response_type": "ListModelVersionsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'model_id' in local_var_params:
            path_params['model_id'] = local_var_params['model_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'version_id' in local_var_params:
            query_params.append(('version_id', local_var_params['version_id']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def list_models_async(self, request):
        r"""列举模型

        列举模型
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListModels
        :type request: :class:`huaweicloudsdkdataartsfabric.v1.ListModelsRequest`
        :rtype: :class:`huaweicloudsdkdataartsfabric.v1.ListModelsResponse`
        """
        http_info = self._list_models_http_info(request)
        return self._call_api(**http_info)

    def list_models_async_invoker(self, request):
        http_info = self._list_models_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_models_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/workspaces/{workspace_id}/models",
            "request_type": request.__class__.__name__,
            "response_type": "ListModelsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'visibility' in local_var_params:
            query_params.append(('visibility', local_var_params['visibility']))
        if 'sort_by' in local_var_params:
            query_params.append(('sort_by', local_var_params['sort_by']))
        if 'order_by' in local_var_params:
            query_params.append(('order_by', local_var_params['order_by']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def update_model_definition_async(self, request):
        r"""更新模型

        更新模型，会生成新版本
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateModelDefinition
        :type request: :class:`huaweicloudsdkdataartsfabric.v1.UpdateModelDefinitionRequest`
        :rtype: :class:`huaweicloudsdkdataartsfabric.v1.UpdateModelDefinitionResponse`
        """
        http_info = self._update_model_definition_http_info(request)
        return self._call_api(**http_info)

    def update_model_definition_async_invoker(self, request):
        http_info = self._update_model_definition_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_model_definition_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/workspaces/{workspace_id}/models/{model_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateModelDefinitionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'model_id' in local_var_params:
            path_params['model_id'] = local_var_params['model_id']

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

    def list_specs_async(self, request):
        r"""查询服务规格列表

        查询服务规格列表，购买计算资源使用。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListSpecs
        :type request: :class:`huaweicloudsdkdataartsfabric.v1.ListSpecsRequest`
        :rtype: :class:`huaweicloudsdkdataartsfabric.v1.ListSpecsResponse`
        """
        http_info = self._list_specs_http_info(request)
        return self._call_api(**http_info)

    def list_specs_async_invoker(self, request):
        http_info = self._list_specs_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_specs_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/specs",
            "request_type": request.__class__.__name__,
            "response_type": "ListSpecsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'spec_code' in local_var_params:
            query_params.append(('spec_code', local_var_params['spec_code']))
        if 'spec_types' in local_var_params:
            query_params.append(('spec_types', local_var_params['spec_types']))
            collection_formats['spec_types'] = 'multi'
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'scenario' in local_var_params:
            query_params.append(('scenario', local_var_params['scenario']))

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

    def batch_create_fabric_workspace_tags_async(self, request):
        r"""批量打资源标签

        批量打资源标签
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchCreateFabricWorkspaceTags
        :type request: :class:`huaweicloudsdkdataartsfabric.v1.BatchCreateFabricWorkspaceTagsRequest`
        :rtype: :class:`huaweicloudsdkdataartsfabric.v1.BatchCreateFabricWorkspaceTagsResponse`
        """
        http_info = self._batch_create_fabric_workspace_tags_http_info(request)
        return self._call_api(**http_info)

    def batch_create_fabric_workspace_tags_async_invoker(self, request):
        http_info = self._batch_create_fabric_workspace_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_create_fabric_workspace_tags_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/fabric-workspace/{workspace_id}/tags/create",
            "request_type": request.__class__.__name__,
            "response_type": "BatchCreateFabricWorkspaceTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

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

    def batch_delete_fabric_workspace_tags_async(self, request):
        r"""批量删除资源标签

        批量删除资源标签
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchDeleteFabricWorkspaceTags
        :type request: :class:`huaweicloudsdkdataartsfabric.v1.BatchDeleteFabricWorkspaceTagsRequest`
        :rtype: :class:`huaweicloudsdkdataartsfabric.v1.BatchDeleteFabricWorkspaceTagsResponse`
        """
        http_info = self._batch_delete_fabric_workspace_tags_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_fabric_workspace_tags_async_invoker(self, request):
        http_info = self._batch_delete_fabric_workspace_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_delete_fabric_workspace_tags_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/fabric-workspace/{workspace_id}/tags/delete",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeleteFabricWorkspaceTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

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

    def count_tag_fabric_workspaces_async(self, request):
        r"""查询资源实例数量

        查询资源实例数量
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CountTagFabricWorkspaces
        :type request: :class:`huaweicloudsdkdataartsfabric.v1.CountTagFabricWorkspacesRequest`
        :rtype: :class:`huaweicloudsdkdataartsfabric.v1.CountTagFabricWorkspacesResponse`
        """
        http_info = self._count_tag_fabric_workspaces_http_info(request)
        return self._call_api(**http_info)

    def count_tag_fabric_workspaces_async_invoker(self, request):
        http_info = self._count_tag_fabric_workspaces_http_info(request)
        return AsyncInvoker(self, http_info)

    def _count_tag_fabric_workspaces_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/fabric-workspace/resource-instances/count",
            "request_type": request.__class__.__name__,
            "response_type": "CountTagFabricWorkspacesResponse"
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

        response_headers = ["X-request-id", ]

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

    def list_fabric_project_tags_async(self, request):
        r"""查询项目标签

        查询项目标签
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListFabricProjectTags
        :type request: :class:`huaweicloudsdkdataartsfabric.v1.ListFabricProjectTagsRequest`
        :rtype: :class:`huaweicloudsdkdataartsfabric.v1.ListFabricProjectTagsResponse`
        """
        http_info = self._list_fabric_project_tags_http_info(request)
        return self._call_api(**http_info)

    def list_fabric_project_tags_async_invoker(self, request):
        http_info = self._list_fabric_project_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_fabric_project_tags_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/fabric-workspace/tags",
            "request_type": request.__class__.__name__,
            "response_type": "ListFabricProjectTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'use_predefine_tags' in local_var_params:
            query_params.append(('use_predefine_tags', local_var_params['use_predefine_tags']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def list_fabric_workspace_tags_async(self, request):
        r"""查询资源标签

        查询资源标签
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListFabricWorkspaceTags
        :type request: :class:`huaweicloudsdkdataartsfabric.v1.ListFabricWorkspaceTagsRequest`
        :rtype: :class:`huaweicloudsdkdataartsfabric.v1.ListFabricWorkspaceTagsResponse`
        """
        http_info = self._list_fabric_workspace_tags_http_info(request)
        return self._call_api(**http_info)

    def list_fabric_workspace_tags_async_invoker(self, request):
        http_info = self._list_fabric_workspace_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_fabric_workspace_tags_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/fabric-workspace/{workspace_id}/tags",
            "request_type": request.__class__.__name__,
            "response_type": "ListFabricWorkspaceTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def list_tag_fabric_workspaces_async(self, request):
        r"""查询资源实例列表

        查询资源实例列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListTagFabricWorkspaces
        :type request: :class:`huaweicloudsdkdataartsfabric.v1.ListTagFabricWorkspacesRequest`
        :rtype: :class:`huaweicloudsdkdataartsfabric.v1.ListTagFabricWorkspacesResponse`
        """
        http_info = self._list_tag_fabric_workspaces_http_info(request)
        return self._call_api(**http_info)

    def list_tag_fabric_workspaces_async_invoker(self, request):
        http_info = self._list_tag_fabric_workspaces_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_tag_fabric_workspaces_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/fabric-workspace/resource-instances/filter",
            "request_type": request.__class__.__name__,
            "response_type": "ListTagFabricWorkspacesResponse"
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

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def create_workspace_async(self, request):
        r"""创建Workspace

        Create workspace
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateWorkspace
        :type request: :class:`huaweicloudsdkdataartsfabric.v1.CreateWorkspaceRequest`
        :rtype: :class:`huaweicloudsdkdataartsfabric.v1.CreateWorkspaceResponse`
        """
        http_info = self._create_workspace_http_info(request)
        return self._call_api(**http_info)

    def create_workspace_async_invoker(self, request):
        http_info = self._create_workspace_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_workspace_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/workspaces",
            "request_type": request.__class__.__name__,
            "response_type": "CreateWorkspaceResponse"
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

        response_headers = ["X-request-id", ]

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

    def delete_workspace_async(self, request):
        r"""删除Workspace

        删除Workspace
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteWorkspace
        :type request: :class:`huaweicloudsdkdataartsfabric.v1.DeleteWorkspaceRequest`
        :rtype: :class:`huaweicloudsdkdataartsfabric.v1.DeleteWorkspaceResponse`
        """
        http_info = self._delete_workspace_http_info(request)
        return self._call_api(**http_info)

    def delete_workspace_async_invoker(self, request):
        http_info = self._delete_workspace_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_workspace_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/workspaces/{workspace_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteWorkspaceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def list_workspaces_async(self, request):
        r"""查询Workspace列表

        查询Workspace列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListWorkspaces
        :type request: :class:`huaweicloudsdkdataartsfabric.v1.ListWorkspacesRequest`
        :rtype: :class:`huaweicloudsdkdataartsfabric.v1.ListWorkspacesResponse`
        """
        http_info = self._list_workspaces_http_info(request)
        return self._call_api(**http_info)

    def list_workspaces_async_invoker(self, request):
        http_info = self._list_workspaces_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_workspaces_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/workspaces",
            "request_type": request.__class__.__name__,
            "response_type": "ListWorkspacesResponse"
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
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def update_workspace_async(self, request):
        r"""更新Workspace

        更新Workspace
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateWorkspace
        :type request: :class:`huaweicloudsdkdataartsfabric.v1.UpdateWorkspaceRequest`
        :rtype: :class:`huaweicloudsdkdataartsfabric.v1.UpdateWorkspaceResponse`
        """
        http_info = self._update_workspace_http_info(request)
        return self._call_api(**http_info)

    def update_workspace_async_invoker(self, request):
        http_info = self._update_workspace_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_workspace_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/workspaces/{workspace_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateWorkspaceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

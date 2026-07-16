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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkagentarts'")


class AgentArtsAsyncClient(Client):
    def __init__(self):
        super().__init__()
        self.model_package = importlib.import_module("huaweicloudsdkagentarts.v1.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "AgentArtsAsyncClient":
                raise TypeError("client type error, support client type is AgentArtsAsyncClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def batch_create_core_gateway_tags_async(self, request):
        r"""批量添加网关标签

        批量添加网关标签。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchCreateCoreGatewayTags
        :type request: :class:`huaweicloudsdkagentarts.v1.BatchCreateCoreGatewayTagsRequest`
        :rtype: :class:`huaweicloudsdkagentarts.v1.BatchCreateCoreGatewayTagsResponse`
        """
        http_info = self._batch_create_core_gateway_tags_http_info(request)
        return self._call_api(**http_info)

    def batch_create_core_gateway_tags_async_invoker(self, request):
        http_info = self._batch_create_core_gateway_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_create_core_gateway_tags_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/gateways/{gateway_id}/tags/create",
            "request_type": request.__class__.__name__,
            "response_type": "BatchCreateCoreGatewayTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'gateway_id' in local_var_params:
            path_params['gateway_id'] = local_var_params['gateway_id']

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

    def batch_delete_core_gateway_tags_async(self, request):
        r"""批量删除网关标签

        批量删除网关标签。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchDeleteCoreGatewayTags
        :type request: :class:`huaweicloudsdkagentarts.v1.BatchDeleteCoreGatewayTagsRequest`
        :rtype: :class:`huaweicloudsdkagentarts.v1.BatchDeleteCoreGatewayTagsResponse`
        """
        http_info = self._batch_delete_core_gateway_tags_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_core_gateway_tags_async_invoker(self, request):
        http_info = self._batch_delete_core_gateway_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_delete_core_gateway_tags_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/gateways/{gateway_id}/tags/delete",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeleteCoreGatewayTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'gateway_id' in local_var_params:
            path_params['gateway_id'] = local_var_params['gateway_id']

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

    def create_core_code_interpreter_async(self, request):
        r"""创建代码解释器

        该API用于创建一个代码解释器。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateCoreCodeInterpreter
        :type request: :class:`huaweicloudsdkagentarts.v1.CreateCoreCodeInterpreterRequest`
        :rtype: :class:`huaweicloudsdkagentarts.v1.CreateCoreCodeInterpreterResponse`
        """
        http_info = self._create_core_code_interpreter_http_info(request)
        return self._call_api(**http_info)

    def create_core_code_interpreter_async_invoker(self, request):
        http_info = self._create_core_code_interpreter_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_core_code_interpreter_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/core/code-interpreters",
            "request_type": request.__class__.__name__,
            "response_type": "CreateCoreCodeInterpreterResponse"
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

    def create_core_gateway_async(self, request):
        r"""创建网关

        使用指定配置创建一个新的网关。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateCoreGateway
        :type request: :class:`huaweicloudsdkagentarts.v1.CreateCoreGatewayRequest`
        :rtype: :class:`huaweicloudsdkagentarts.v1.CreateCoreGatewayResponse`
        """
        http_info = self._create_core_gateway_http_info(request)
        return self._call_api(**http_info)

    def create_core_gateway_async_invoker(self, request):
        http_info = self._create_core_gateway_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_core_gateway_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/core/gateways",
            "request_type": request.__class__.__name__,
            "response_type": "CreateCoreGatewayResponse"
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

    def create_core_gateway_target_async(self, request):
        r"""创建目标服务

        为指定网关创建目标服务。目标服务定义了网关可以连接的端点。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateCoreGatewayTarget
        :type request: :class:`huaweicloudsdkagentarts.v1.CreateCoreGatewayTargetRequest`
        :rtype: :class:`huaweicloudsdkagentarts.v1.CreateCoreGatewayTargetResponse`
        """
        http_info = self._create_core_gateway_target_http_info(request)
        return self._call_api(**http_info)

    def create_core_gateway_target_async_invoker(self, request):
        http_info = self._create_core_gateway_target_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_core_gateway_target_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/core/gateways/{gateway_id}/targets",
            "request_type": request.__class__.__name__,
            "response_type": "CreateCoreGatewayTargetResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'gateway_id' in local_var_params:
            path_params['gateway_id'] = local_var_params['gateway_id']

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

    def create_core_ingress_async(self, request):
        r"""创建网关

        该接口用于创建一个新的Ingress配置。
        **适用场景**：
        创建Agent运行时入口网关配置。
        **异步任务确认方式**：
        调用创建接口后，通过查询Ingress详情接口查询status字段，当status变为ACTIVE时表示创建成功，变为FAILED时表示创建失败。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateCoreIngress
        :type request: :class:`huaweicloudsdkagentarts.v1.CreateCoreIngressRequest`
        :rtype: :class:`huaweicloudsdkagentarts.v1.CreateCoreIngressResponse`
        """
        http_info = self._create_core_ingress_http_info(request)
        return self._call_api(**http_info)

    def create_core_ingress_async_invoker(self, request):
        http_info = self._create_core_ingress_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_core_ingress_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/core/ingresses",
            "request_type": request.__class__.__name__,
            "response_type": "CreateCoreIngressResponse"
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

    def create_core_ingress_network_async(self, request):
        r"""创建VPC入站网络

        该接口用于为某一个Agent网关ID创建指定VPC的入站网络。该接口会为该VPC创建对应网关的访问地址和域名。
        **适用场景：**
        Agent运行时需要在VPC网络内部调用场景下，为该VPC网络配置网关调用入口。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateCoreIngressNetwork
        :type request: :class:`huaweicloudsdkagentarts.v1.CreateCoreIngressNetworkRequest`
        :rtype: :class:`huaweicloudsdkagentarts.v1.CreateCoreIngressNetworkResponse`
        """
        http_info = self._create_core_ingress_network_http_info(request)
        return self._call_api(**http_info)

    def create_core_ingress_network_async_invoker(self, request):
        http_info = self._create_core_ingress_network_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_core_ingress_network_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/core/ingresses/{ingress_id}/vpc-networks",
            "request_type": request.__class__.__name__,
            "response_type": "CreateCoreIngressNetworkResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ingress_id' in local_var_params:
            path_params['ingress_id'] = local_var_params['ingress_id']

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

    def create_core_runtime_async(self, request):
        r"""创建runtime

        该接口用于创建Agent运行时，支持为该运行时进行入站认证，网络访问，可观测配置等。该接口会同时创建运行时以及对应的初始版本。
        **适用场景：**
        部署一个已经开发完成的Agent应用。
        为Agent应用配置入站认证。
        为Agent应用配置入口和出口网络。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateCoreRuntime
        :type request: :class:`huaweicloudsdkagentarts.v1.CreateCoreRuntimeRequest`
        :rtype: :class:`huaweicloudsdkagentarts.v1.CreateCoreRuntimeResponse`
        """
        http_info = self._create_core_runtime_http_info(request)
        return self._call_api(**http_info)

    def create_core_runtime_async_invoker(self, request):
        http_info = self._create_core_runtime_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_core_runtime_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/core/runtimes",
            "request_type": request.__class__.__name__,
            "response_type": "CreateCoreRuntimeResponse"
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

    def create_core_runtime_endpoint_async(self, request):
        r"""创建runtime访问方式

        该接口用于为某一个具体的Agent运行时创建访问方式，支持为该访问方式绑定版本以及对应的灰度策略。
        **适用场景：**
        某一个具体的Agent运行时存在多个版本，通过配置访问方式来指定调用某一个具体版本。
        某一个具体的Agent运行时修改后需要进行灰度发布，通过配置访问方式，为老版本和新版本配置流量权重。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateCoreRuntimeEndpoint
        :type request: :class:`huaweicloudsdkagentarts.v1.CreateCoreRuntimeEndpointRequest`
        :rtype: :class:`huaweicloudsdkagentarts.v1.CreateCoreRuntimeEndpointResponse`
        """
        http_info = self._create_core_runtime_endpoint_http_info(request)
        return self._call_api(**http_info)

    def create_core_runtime_endpoint_async_invoker(self, request):
        http_info = self._create_core_runtime_endpoint_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_core_runtime_endpoint_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/core/runtimes/{runtime_id}/endpoints",
            "request_type": request.__class__.__name__,
            "response_type": "CreateCoreRuntimeEndpointResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'runtime_id' in local_var_params:
            path_params['runtime_id'] = local_var_params['runtime_id']

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

    def create_core_space_async(self, request):
        r"""创建Space

        创建新的记忆库，用于存放某一类业务的短长期记忆数据，包括访问方式、抽取策略、密钥绑定等相关配置。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateCoreSpace
        :type request: :class:`huaweicloudsdkagentarts.v1.CreateCoreSpaceRequest`
        :rtype: :class:`huaweicloudsdkagentarts.v1.CreateCoreSpaceResponse`
        """
        http_info = self._create_core_space_http_info(request)
        return self._call_api(**http_info)

    def create_core_space_async_invoker(self, request):
        http_info = self._create_core_space_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_core_space_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/core/spaces",
            "request_type": request.__class__.__name__,
            "response_type": "CreateCoreSpaceResponse"
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

    def create_core_space_api_key_async(self, request):
        r"""创建 API Key

        创建新的 API Key，用于数据面访问认证。
        API Key 先于 Space 创建，创建后通过 CreateSpace 的 api_key_id 参数绑定到 Space。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateCoreSpaceApiKey
        :type request: :class:`huaweicloudsdkagentarts.v1.CreateCoreSpaceApiKeyRequest`
        :rtype: :class:`huaweicloudsdkagentarts.v1.CreateCoreSpaceApiKeyResponse`
        """
        http_info = self._create_core_space_api_key_http_info(request)
        return self._call_api(**http_info)

    def create_core_space_api_key_async_invoker(self, request):
        http_info = self._create_core_space_api_key_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_core_space_api_key_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/core/space-keys",
            "request_type": request.__class__.__name__,
            "response_type": "CreateCoreSpaceApiKeyResponse"
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

    def create_core_space_customized_strategy_async(self, request):
        r"""创建自定义记忆策略

        为指定 Space 创建自定义记忆策略。
        需指定策略名称、类型及步骤列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateCoreSpaceCustomizedStrategy
        :type request: :class:`huaweicloudsdkagentarts.v1.CreateCoreSpaceCustomizedStrategyRequest`
        :rtype: :class:`huaweicloudsdkagentarts.v1.CreateCoreSpaceCustomizedStrategyResponse`
        """
        http_info = self._create_core_space_customized_strategy_http_info(request)
        return self._call_api(**http_info)

    def create_core_space_customized_strategy_async_invoker(self, request):
        http_info = self._create_core_space_customized_strategy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_core_space_customized_strategy_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/core/spaces/{space_id}/strategies/customized",
            "request_type": request.__class__.__name__,
            "response_type": "CreateCoreSpaceCustomizedStrategyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'space_id' in local_var_params:
            path_params['space_id'] = local_var_params['space_id']

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

    def delete_core_code_interpreter_async(self, request):
        r"""删除代码解释器

        删除指定的代码解释器。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteCoreCodeInterpreter
        :type request: :class:`huaweicloudsdkagentarts.v1.DeleteCoreCodeInterpreterRequest`
        :rtype: :class:`huaweicloudsdkagentarts.v1.DeleteCoreCodeInterpreterResponse`
        """
        http_info = self._delete_core_code_interpreter_http_info(request)
        return self._call_api(**http_info)

    def delete_core_code_interpreter_async_invoker(self, request):
        http_info = self._delete_core_code_interpreter_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_core_code_interpreter_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/core/code-interpreters/{code_interpreter_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteCoreCodeInterpreterResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'code_interpreter_id' in local_var_params:
            path_params['code_interpreter_id'] = local_var_params['code_interpreter_id']

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

    def delete_core_gateway_async(self, request):
        r"""删除网关

        永久删除指定 ID 的网关。此操作无法撤销。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteCoreGateway
        :type request: :class:`huaweicloudsdkagentarts.v1.DeleteCoreGatewayRequest`
        :rtype: :class:`huaweicloudsdkagentarts.v1.DeleteCoreGatewayResponse`
        """
        http_info = self._delete_core_gateway_http_info(request)
        return self._call_api(**http_info)

    def delete_core_gateway_async_invoker(self, request):
        http_info = self._delete_core_gateway_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_core_gateway_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/core/gateways/{gateway_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteCoreGatewayResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'gateway_id' in local_var_params:
            path_params['gateway_id'] = local_var_params['gateway_id']

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

    def delete_core_gateway_target_async(self, request):
        r"""删除目标服务

        永久删除指定目标服务。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteCoreGatewayTarget
        :type request: :class:`huaweicloudsdkagentarts.v1.DeleteCoreGatewayTargetRequest`
        :rtype: :class:`huaweicloudsdkagentarts.v1.DeleteCoreGatewayTargetResponse`
        """
        http_info = self._delete_core_gateway_target_http_info(request)
        return self._call_api(**http_info)

    def delete_core_gateway_target_async_invoker(self, request):
        http_info = self._delete_core_gateway_target_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_core_gateway_target_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/core/gateways/{gateway_id}/targets/{target_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteCoreGatewayTargetResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'gateway_id' in local_var_params:
            path_params['gateway_id'] = local_var_params['gateway_id']
        if 'target_id' in local_var_params:
            path_params['target_id'] = local_var_params['target_id']

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

    def delete_core_ingress_async(self, request):
        r"""删除网关

        该接口用于根据ingress_id删除Ingress配置。（异步接口）
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteCoreIngress
        :type request: :class:`huaweicloudsdkagentarts.v1.DeleteCoreIngressRequest`
        :rtype: :class:`huaweicloudsdkagentarts.v1.DeleteCoreIngressResponse`
        """
        http_info = self._delete_core_ingress_http_info(request)
        return self._call_api(**http_info)

    def delete_core_ingress_async_invoker(self, request):
        http_info = self._delete_core_ingress_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_core_ingress_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/core/ingresses/{ingress_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteCoreIngressResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ingress_id' in local_var_params:
            path_params['ingress_id'] = local_var_params['ingress_id']

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

    def delete_core_ingress_network_async(self, request):
        r"""删除VPC入站网络

        该接口用于根据网关ID以及入站网络ID异步删除某一个具体的Agent网关入站网络。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteCoreIngressNetwork
        :type request: :class:`huaweicloudsdkagentarts.v1.DeleteCoreIngressNetworkRequest`
        :rtype: :class:`huaweicloudsdkagentarts.v1.DeleteCoreIngressNetworkResponse`
        """
        http_info = self._delete_core_ingress_network_http_info(request)
        return self._call_api(**http_info)

    def delete_core_ingress_network_async_invoker(self, request):
        http_info = self._delete_core_ingress_network_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_core_ingress_network_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/core/ingresses/{ingress_id}/vpc-networks/{vpc_ingress_network_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteCoreIngressNetworkResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ingress_id' in local_var_params:
            path_params['ingress_id'] = local_var_params['ingress_id']
        if 'vpc_ingress_network_id' in local_var_params:
            path_params['vpc_ingress_network_id'] = local_var_params['vpc_ingress_network_id']

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

    def delete_core_runtime_async(self, request):
        r"""删除runtime

        该接口用于根据Agent运行时ID删除对应的Agent运行时。该接口会删除运行时及其关联的所有版本和访问方式记录。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteCoreRuntime
        :type request: :class:`huaweicloudsdkagentarts.v1.DeleteCoreRuntimeRequest`
        :rtype: :class:`huaweicloudsdkagentarts.v1.DeleteCoreRuntimeResponse`
        """
        http_info = self._delete_core_runtime_http_info(request)
        return self._call_api(**http_info)

    def delete_core_runtime_async_invoker(self, request):
        http_info = self._delete_core_runtime_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_core_runtime_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/core/runtimes/{runtime_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteCoreRuntimeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'runtime_id' in local_var_params:
            path_params['runtime_id'] = local_var_params['runtime_id']

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

    def delete_core_runtime_endpoint_async(self, request):
        r"""删除runtime访问方式

        该接口用于根据Agent运行时ID以及访问方式ID删除对应的Agent运行时访问方式。访问方式删除后无法通过该访问方式进行Agent调用。
        **适用场景：**
        删除某一个具体的Agent运行时访问方式及其相关记录。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteCoreRuntimeEndpoint
        :type request: :class:`huaweicloudsdkagentarts.v1.DeleteCoreRuntimeEndpointRequest`
        :rtype: :class:`huaweicloudsdkagentarts.v1.DeleteCoreRuntimeEndpointResponse`
        """
        http_info = self._delete_core_runtime_endpoint_http_info(request)
        return self._call_api(**http_info)

    def delete_core_runtime_endpoint_async_invoker(self, request):
        http_info = self._delete_core_runtime_endpoint_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_core_runtime_endpoint_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/core/runtimes/{runtime_id}/endpoints/{endpoint_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteCoreRuntimeEndpointResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'runtime_id' in local_var_params:
            path_params['runtime_id'] = local_var_params['runtime_id']
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

    def delete_core_space_async(self, request):
        r"""删除记忆库

        删除记忆库，将清空所有记忆数据和配置，不可恢复。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteCoreSpace
        :type request: :class:`huaweicloudsdkagentarts.v1.DeleteCoreSpaceRequest`
        :rtype: :class:`huaweicloudsdkagentarts.v1.DeleteCoreSpaceResponse`
        """
        http_info = self._delete_core_space_http_info(request)
        return self._call_api(**http_info)

    def delete_core_space_async_invoker(self, request):
        http_info = self._delete_core_space_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_core_space_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/core/spaces/{space_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteCoreSpaceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'space_id' in local_var_params:
            path_params['space_id'] = local_var_params['space_id']

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

    def delete_core_space_customized_strategy_async(self, request):
        r"""删除自定义记忆策略

        删除指定Space下的自定义记忆策略，不可恢复。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteCoreSpaceCustomizedStrategy
        :type request: :class:`huaweicloudsdkagentarts.v1.DeleteCoreSpaceCustomizedStrategyRequest`
        :rtype: :class:`huaweicloudsdkagentarts.v1.DeleteCoreSpaceCustomizedStrategyResponse`
        """
        http_info = self._delete_core_space_customized_strategy_http_info(request)
        return self._call_api(**http_info)

    def delete_core_space_customized_strategy_async_invoker(self, request):
        http_info = self._delete_core_space_customized_strategy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_core_space_customized_strategy_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/core/spaces/{space_id}/strategies/customized/{strategy_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteCoreSpaceCustomizedStrategyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'space_id' in local_var_params:
            path_params['space_id'] = local_var_params['space_id']
        if 'strategy_id' in local_var_params:
            path_params['strategy_id'] = local_var_params['strategy_id']

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

    def list_all_core_gateway_tags_async(self, request):
        r"""查询账号下所有网关标签列表

        查询账号下所有网关标签列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAllCoreGatewayTags
        :type request: :class:`huaweicloudsdkagentarts.v1.ListAllCoreGatewayTagsRequest`
        :rtype: :class:`huaweicloudsdkagentarts.v1.ListAllCoreGatewayTagsResponse`
        """
        http_info = self._list_all_core_gateway_tags_http_info(request)
        return self._call_api(**http_info)

    def list_all_core_gateway_tags_async_invoker(self, request):
        http_info = self._list_all_core_gateway_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_all_core_gateway_tags_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/gateways/tags",
            "request_type": request.__class__.__name__,
            "response_type": "ListAllCoreGatewayTagsResponse"
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

    def list_core_code_interpreters_async(self, request):
        r"""查询代码解释器列表

        该API用于查询代码解释器列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListCoreCodeInterpreters
        :type request: :class:`huaweicloudsdkagentarts.v1.ListCoreCodeInterpretersRequest`
        :rtype: :class:`huaweicloudsdkagentarts.v1.ListCoreCodeInterpretersResponse`
        """
        http_info = self._list_core_code_interpreters_http_info(request)
        return self._call_api(**http_info)

    def list_core_code_interpreters_async_invoker(self, request):
        http_info = self._list_core_code_interpreters_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_core_code_interpreters_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/core/code-interpreters",
            "request_type": request.__class__.__name__,
            "response_type": "ListCoreCodeInterpretersResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
        if 'tag_key_exists' in local_var_params:
            query_params.append(('tag_key_exists', local_var_params['tag_key_exists']))
        if 'tag_key_matches' in local_var_params:
            query_params.append(('tag_key_matches', local_var_params['tag_key_matches']))
        if 'tag_value_matches' in local_var_params:
            query_params.append(('tag_value_matches', local_var_params['tag_value_matches']))
        if 'tag_match_policy' in local_var_params:
            query_params.append(('tag_match_policy', local_var_params['tag_match_policy']))

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

    def list_core_gateway_quotas_async(self, request):
        r"""查询账号配额

        获取当前认证账号的有效配额信息，包括配额类型、最小值、最大值、配额值和已使用数量。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListCoreGatewayQuotas
        :type request: :class:`huaweicloudsdkagentarts.v1.ListCoreGatewayQuotasRequest`
        :rtype: :class:`huaweicloudsdkagentarts.v1.ListCoreGatewayQuotasResponse`
        """
        http_info = self._list_core_gateway_quotas_http_info(request)
        return self._call_api(**http_info)

    def list_core_gateway_quotas_async_invoker(self, request):
        http_info = self._list_core_gateway_quotas_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_core_gateway_quotas_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/core/gateway-quotas",
            "request_type": request.__class__.__name__,
            "response_type": "ListCoreGatewayQuotasResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'gateway_id' in local_var_params:
            query_params.append(('gateway_id', local_var_params['gateway_id']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

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

    def list_core_gateway_tags_async(self, request):
        r"""查询网关标签列表

        查询网关标签列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListCoreGatewayTags
        :type request: :class:`huaweicloudsdkagentarts.v1.ListCoreGatewayTagsRequest`
        :rtype: :class:`huaweicloudsdkagentarts.v1.ListCoreGatewayTagsResponse`
        """
        http_info = self._list_core_gateway_tags_http_info(request)
        return self._call_api(**http_info)

    def list_core_gateway_tags_async_invoker(self, request):
        http_info = self._list_core_gateway_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_core_gateway_tags_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/gateways/{gateway_id}/tags",
            "request_type": request.__class__.__name__,
            "response_type": "ListCoreGatewayTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'gateway_id' in local_var_params:
            path_params['gateway_id'] = local_var_params['gateway_id']

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

    def list_core_gateway_targets_async(self, request):
        r"""列出目标服务

        列出指定网关的所有目标服务，支持分页功能。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListCoreGatewayTargets
        :type request: :class:`huaweicloudsdkagentarts.v1.ListCoreGatewayTargetsRequest`
        :rtype: :class:`huaweicloudsdkagentarts.v1.ListCoreGatewayTargetsResponse`
        """
        http_info = self._list_core_gateway_targets_http_info(request)
        return self._call_api(**http_info)

    def list_core_gateway_targets_async_invoker(self, request):
        http_info = self._list_core_gateway_targets_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_core_gateway_targets_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/core/gateways/{gateway_id}/targets",
            "request_type": request.__class__.__name__,
            "response_type": "ListCoreGatewayTargetsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'gateway_id' in local_var_params:
            path_params['gateway_id'] = local_var_params['gateway_id']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

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

    def list_core_gateways_async(self, request):
        r"""列出所有网关

        检索所有网关的列表，支持可选的过滤和分页功能。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListCoreGateways
        :type request: :class:`huaweicloudsdkagentarts.v1.ListCoreGatewaysRequest`
        :rtype: :class:`huaweicloudsdkagentarts.v1.ListCoreGatewaysResponse`
        """
        http_info = self._list_core_gateways_http_info(request)
        return self._call_api(**http_info)

    def list_core_gateways_async_invoker(self, request):
        http_info = self._list_core_gateways_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_core_gateways_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/core/gateways",
            "request_type": request.__class__.__name__,
            "response_type": "ListCoreGatewaysResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'gateway_id' in local_var_params:
            query_params.append(('gateway_id', local_var_params['gateway_id']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

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

    def list_core_gateways_by_tags_async(self, request):
        r"""根据标签查询网关列表

        根据标签过滤条件查询网关列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListCoreGatewaysByTags
        :type request: :class:`huaweicloudsdkagentarts.v1.ListCoreGatewaysByTagsRequest`
        :rtype: :class:`huaweicloudsdkagentarts.v1.ListCoreGatewaysByTagsResponse`
        """
        http_info = self._list_core_gateways_by_tags_http_info(request)
        return self._call_api(**http_info)

    def list_core_gateways_by_tags_async_invoker(self, request):
        http_info = self._list_core_gateways_by_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_core_gateways_by_tags_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/gateways/resource-instances/filter",
            "request_type": request.__class__.__name__,
            "response_type": "ListCoreGatewaysByTagsResponse"
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

    def list_core_ingress_networks_async(self, request):
        r"""查询VPC入站网络列表

        该接口用于查询某一个具体的Agent网关下的所有入站网络列表，不支持分页。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListCoreIngressNetworks
        :type request: :class:`huaweicloudsdkagentarts.v1.ListCoreIngressNetworksRequest`
        :rtype: :class:`huaweicloudsdkagentarts.v1.ListCoreIngressNetworksResponse`
        """
        http_info = self._list_core_ingress_networks_http_info(request)
        return self._call_api(**http_info)

    def list_core_ingress_networks_async_invoker(self, request):
        http_info = self._list_core_ingress_networks_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_core_ingress_networks_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/core/ingresses/{ingress_id}/vpc-networks",
            "request_type": request.__class__.__name__,
            "response_type": "ListCoreIngressNetworksResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ingress_id' in local_var_params:
            path_params['ingress_id'] = local_var_params['ingress_id']

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

    def list_core_ingresses_async(self, request):
        r"""批量查询网关

        该接口用于查询Ingress列表，支持按名称模糊匹配和分页查询。
        **适用场景：**
        查询租户下的所有Ingress列表。
        根据Ingress名称进行模糊查询。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListCoreIngresses
        :type request: :class:`huaweicloudsdkagentarts.v1.ListCoreIngressesRequest`
        :rtype: :class:`huaweicloudsdkagentarts.v1.ListCoreIngressesResponse`
        """
        http_info = self._list_core_ingresses_http_info(request)
        return self._call_api(**http_info)

    def list_core_ingresses_async_invoker(self, request):
        http_info = self._list_core_ingresses_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_core_ingresses_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/core/ingresses",
            "request_type": request.__class__.__name__,
            "response_type": "ListCoreIngressesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
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

    def list_core_runtime_endpoints_async(self, request):
        r"""批量查询runtime访问方式

        该接口用于根据运行时ID查询某一个具体的Agent运行时下的访问方式列表。支持分页查询。
        **适用场景：**
        根据Agent运行时ID查询该运行时的访问方式列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListCoreRuntimeEndpoints
        :type request: :class:`huaweicloudsdkagentarts.v1.ListCoreRuntimeEndpointsRequest`
        :rtype: :class:`huaweicloudsdkagentarts.v1.ListCoreRuntimeEndpointsResponse`
        """
        http_info = self._list_core_runtime_endpoints_http_info(request)
        return self._call_api(**http_info)

    def list_core_runtime_endpoints_async_invoker(self, request):
        http_info = self._list_core_runtime_endpoints_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_core_runtime_endpoints_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/core/runtimes/{runtime_id}/endpoints",
            "request_type": request.__class__.__name__,
            "response_type": "ListCoreRuntimeEndpointsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'runtime_id' in local_var_params:
            path_params['runtime_id'] = local_var_params['runtime_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'tag_key_exists' in local_var_params:
            query_params.append(('tag_key_exists', local_var_params['tag_key_exists']))
        if 'tag_key_matches' in local_var_params:
            query_params.append(('tag_key_matches', local_var_params['tag_key_matches']))
        if 'tag_value_matches' in local_var_params:
            query_params.append(('tag_value_matches', local_var_params['tag_value_matches']))
        if 'tag_match_policy' in local_var_params:
            query_params.append(('tag_match_policy', local_var_params['tag_match_policy']))

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

    def list_core_runtime_versions_async(self, request):
        r"""批量查询版本

        该接口用于根据运行时ID查询某一个具体的Agent运行时下的版本列表。支持分页查询。
        **适用场景：**
        根据Agent运行时ID查询该运行时的版本列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListCoreRuntimeVersions
        :type request: :class:`huaweicloudsdkagentarts.v1.ListCoreRuntimeVersionsRequest`
        :rtype: :class:`huaweicloudsdkagentarts.v1.ListCoreRuntimeVersionsResponse`
        """
        http_info = self._list_core_runtime_versions_http_info(request)
        return self._call_api(**http_info)

    def list_core_runtime_versions_async_invoker(self, request):
        http_info = self._list_core_runtime_versions_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_core_runtime_versions_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/core/runtimes/{runtime_id}/versions",
            "request_type": request.__class__.__name__,
            "response_type": "ListCoreRuntimeVersionsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'runtime_id' in local_var_params:
            path_params['runtime_id'] = local_var_params['runtime_id']

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

    def list_core_runtimes_async(self, request):
        r"""批量查询runtime

        该接口用于查询Agent运行时列表。支持按多种条件筛选和分页查询。
        **适用场景：**
        根据Agent运行时名称查询运行时列表，支持精确匹配和模糊匹配。
        根据Agent运行时ID进行精确查询，支持批量查询多个运行时ID。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListCoreRuntimes
        :type request: :class:`huaweicloudsdkagentarts.v1.ListCoreRuntimesRequest`
        :rtype: :class:`huaweicloudsdkagentarts.v1.ListCoreRuntimesResponse`
        """
        http_info = self._list_core_runtimes_http_info(request)
        return self._call_api(**http_info)

    def list_core_runtimes_async_invoker(self, request):
        http_info = self._list_core_runtimes_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_core_runtimes_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/core/runtimes",
            "request_type": request.__class__.__name__,
            "response_type": "ListCoreRuntimesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'runtime_ids' in local_var_params:
            query_params.append(('runtime_ids', local_var_params['runtime_ids']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
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

    def list_core_space_builtin_strategies_async(self, request):
        r"""获取内置记忆策略列表

        返回系统预置的内置记忆策略及其步骤详情，内置策略全局共享。
        内置策略不可修改，用户可根据内置策略创建自定义策略。
        当前包含 4 种内置策略：
        - **Semantic Memory**：语义记忆提取（extraction → consolidation）
        - **User Preference**：用户偏好提取（extraction → consolidation）
        - **Summary**：会话摘要生成（consolidation）
        - **Episodic Memory**：情景记忆提取（extraction → consolidation → reflection）
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListCoreSpaceBuiltinStrategies
        :type request: :class:`huaweicloudsdkagentarts.v1.ListCoreSpaceBuiltinStrategiesRequest`
        :rtype: :class:`huaweicloudsdkagentarts.v1.ListCoreSpaceBuiltinStrategiesResponse`
        """
        http_info = self._list_core_space_builtin_strategies_http_info(request)
        return self._call_api(**http_info)

    def list_core_space_builtin_strategies_async_invoker(self, request):
        http_info = self._list_core_space_builtin_strategies_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_core_space_builtin_strategies_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/core/space-builtin-strategies",
            "request_type": request.__class__.__name__,
            "response_type": "ListCoreSpaceBuiltinStrategiesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

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

    def list_core_space_jobs_async(self, request):
        r"""列出异步任务

        分页列出指定Space下的异步任务
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListCoreSpaceJobs
        :type request: :class:`huaweicloudsdkagentarts.v1.ListCoreSpaceJobsRequest`
        :rtype: :class:`huaweicloudsdkagentarts.v1.ListCoreSpaceJobsResponse`
        """
        http_info = self._list_core_space_jobs_http_info(request)
        return self._call_api(**http_info)

    def list_core_space_jobs_async_invoker(self, request):
        http_info = self._list_core_space_jobs_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_core_space_jobs_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/core/spaces/{space_id}/jobs",
            "request_type": request.__class__.__name__,
            "response_type": "ListCoreSpaceJobsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'space_id' in local_var_params:
            path_params['space_id'] = local_var_params['space_id']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'job_name' in local_var_params:
            query_params.append(('job_name', local_var_params['job_name']))

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

    def list_core_space_memories_async(self, request):
        r"""列出记忆

        **参数解释：**
        异步任务 ID，唯一标识一个异步任务，可通过创建异步任务的接口返回获取。
        **约束限制：**
        仅支持字母、数字和中划线。
        **取值范围：**
        长度1-48字符。
        **默认取值：**
        不涉及。
        
        **调用链路**：
        1. 校验 IAM Token，获取 project_id
        2. 根据 space_id 查询 CtrlDB 获取 Space 记录（含 cell_id）
        3. 校验 Space 归属当前 project_id
        4. 根据 cell_id 查询 Cell 配置获取 Access 服务地址
        5. 携带 X-Internal-Token 调用 Access 内部接口
        6. 透传响应
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListCoreSpaceMemories
        :type request: :class:`huaweicloudsdkagentarts.v1.ListCoreSpaceMemoriesRequest`
        :rtype: :class:`huaweicloudsdkagentarts.v1.ListCoreSpaceMemoriesResponse`
        """
        http_info = self._list_core_space_memories_http_info(request)
        return self._call_api(**http_info)

    def list_core_space_memories_async_invoker(self, request):
        http_info = self._list_core_space_memories_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_core_space_memories_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/core/spaces/{space_id}/memories",
            "request_type": request.__class__.__name__,
            "response_type": "ListCoreSpaceMemoriesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'space_id' in local_var_params:
            path_params['space_id'] = local_var_params['space_id']

        query_params = []
        if 'strategy_type' in local_var_params:
            query_params.append(('strategy_type', local_var_params['strategy_type']))
        if 'strategy_id' in local_var_params:
            query_params.append(('strategy_id', local_var_params['strategy_id']))
        if 'actor_id' in local_var_params:
            query_params.append(('actor_id', local_var_params['actor_id']))
        if 'assistant_id' in local_var_params:
            query_params.append(('assistant_id', local_var_params['assistant_id']))
        if 'session_id' in local_var_params:
            query_params.append(('session_id', local_var_params['session_id']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'sort_by' in local_var_params:
            query_params.append(('sort_by', local_var_params['sort_by']))
        if 'sort_order' in local_var_params:
            query_params.append(('sort_order', local_var_params['sort_order']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

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

    def list_core_spaces_async(self, request):
        r"""列出所有Space

        查询租户下的所有记忆库信息，支持分页查询。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListCoreSpaces
        :type request: :class:`huaweicloudsdkagentarts.v1.ListCoreSpacesRequest`
        :rtype: :class:`huaweicloudsdkagentarts.v1.ListCoreSpacesResponse`
        """
        http_info = self._list_core_spaces_http_info(request)
        return self._call_api(**http_info)

    def list_core_spaces_async_invoker(self, request):
        http_info = self._list_core_spaces_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_core_spaces_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/core/spaces",
            "request_type": request.__class__.__name__,
            "response_type": "ListCoreSpacesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'tag_key_exists' in local_var_params:
            query_params.append(('tag_key_exists', local_var_params['tag_key_exists']))
        if 'tag_key_matches' in local_var_params:
            query_params.append(('tag_key_matches', local_var_params['tag_key_matches']))
        if 'tag_value_matches' in local_var_params:
            query_params.append(('tag_value_matches', local_var_params['tag_value_matches']))
        if 'tag_match_policy' in local_var_params:
            query_params.append(('tag_match_policy', local_var_params['tag_match_policy']))

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

    def reset_core_space_api_key_async(self, request):
        r"""重置 API Key

        异步重置指定 Space 的 API Key，旧 Key 立即失效
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ResetCoreSpaceApiKey
        :type request: :class:`huaweicloudsdkagentarts.v1.ResetCoreSpaceApiKeyRequest`
        :rtype: :class:`huaweicloudsdkagentarts.v1.ResetCoreSpaceApiKeyResponse`
        """
        http_info = self._reset_core_space_api_key_http_info(request)
        return self._call_api(**http_info)

    def reset_core_space_api_key_async_invoker(self, request):
        http_info = self._reset_core_space_api_key_http_info(request)
        return AsyncInvoker(self, http_info)

    def _reset_core_space_api_key_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/core/spaces/{space_id}/reset-key",
            "request_type": request.__class__.__name__,
            "response_type": "ResetCoreSpaceApiKeyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'space_id' in local_var_params:
            path_params['space_id'] = local_var_params['space_id']

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

    def search_core_space_memories_async(self, request):
        r"""搜索记忆

        基于向量相似度搜索 Space 中的长期记忆。
        
        **调用链路**：
        1. 校验 IAM Token，获取 project_id
        2. 根据 space_id 查询 CtrlDB 获取 Space 记录（含 cell_id）
        3. 校验 Space 归属当前 project_id
        4. 根据 cell_id 查询 Cell 配置获取 Access 服务地址
        5. 携带 X-Internal-Token 调用 Access 内部搜索接口
        6. 透传响应
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for SearchCoreSpaceMemories
        :type request: :class:`huaweicloudsdkagentarts.v1.SearchCoreSpaceMemoriesRequest`
        :rtype: :class:`huaweicloudsdkagentarts.v1.SearchCoreSpaceMemoriesResponse`
        """
        http_info = self._search_core_space_memories_http_info(request)
        return self._call_api(**http_info)

    def search_core_space_memories_async_invoker(self, request):
        http_info = self._search_core_space_memories_http_info(request)
        return AsyncInvoker(self, http_info)

    def _search_core_space_memories_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/core/spaces/{space_id}/memories/search",
            "request_type": request.__class__.__name__,
            "response_type": "SearchCoreSpaceMemoriesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'space_id' in local_var_params:
            path_params['space_id'] = local_var_params['space_id']

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

    def show_core_code_interpreter_async(self, request):
        r"""查询代码解释器详情

        该API用于查询代码解释器详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowCoreCodeInterpreter
        :type request: :class:`huaweicloudsdkagentarts.v1.ShowCoreCodeInterpreterRequest`
        :rtype: :class:`huaweicloudsdkagentarts.v1.ShowCoreCodeInterpreterResponse`
        """
        http_info = self._show_core_code_interpreter_http_info(request)
        return self._call_api(**http_info)

    def show_core_code_interpreter_async_invoker(self, request):
        http_info = self._show_core_code_interpreter_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_core_code_interpreter_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/core/code-interpreters/{code_interpreter_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowCoreCodeInterpreterResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'code_interpreter_id' in local_var_params:
            path_params['code_interpreter_id'] = local_var_params['code_interpreter_id']

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

    def show_core_gateway_async(self, request):
        r"""获取网关详情

        通过 ID 获取指定网关的详细信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowCoreGateway
        :type request: :class:`huaweicloudsdkagentarts.v1.ShowCoreGatewayRequest`
        :rtype: :class:`huaweicloudsdkagentarts.v1.ShowCoreGatewayResponse`
        """
        http_info = self._show_core_gateway_http_info(request)
        return self._call_api(**http_info)

    def show_core_gateway_async_invoker(self, request):
        http_info = self._show_core_gateway_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_core_gateway_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/core/gateways/{gateway_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowCoreGatewayResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'gateway_id' in local_var_params:
            path_params['gateway_id'] = local_var_params['gateway_id']

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

    def show_core_gateway_nums_by_tags_async(self, request):
        r"""根据标签查询网关数量

        根据标签查询网关数量。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowCoreGatewayNumsByTags
        :type request: :class:`huaweicloudsdkagentarts.v1.ShowCoreGatewayNumsByTagsRequest`
        :rtype: :class:`huaweicloudsdkagentarts.v1.ShowCoreGatewayNumsByTagsResponse`
        """
        http_info = self._show_core_gateway_nums_by_tags_http_info(request)
        return self._call_api(**http_info)

    def show_core_gateway_nums_by_tags_async_invoker(self, request):
        http_info = self._show_core_gateway_nums_by_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_core_gateway_nums_by_tags_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/gateways/resource-instances/count",
            "request_type": request.__class__.__name__,
            "response_type": "ShowCoreGatewayNumsByTagsResponse"
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

    def show_core_gateway_target_async(self, request):
        r"""获取目标服务详情

        获取指定目标服务的详细信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowCoreGatewayTarget
        :type request: :class:`huaweicloudsdkagentarts.v1.ShowCoreGatewayTargetRequest`
        :rtype: :class:`huaweicloudsdkagentarts.v1.ShowCoreGatewayTargetResponse`
        """
        http_info = self._show_core_gateway_target_http_info(request)
        return self._call_api(**http_info)

    def show_core_gateway_target_async_invoker(self, request):
        http_info = self._show_core_gateway_target_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_core_gateway_target_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/core/gateways/{gateway_id}/targets/{target_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowCoreGatewayTargetResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'gateway_id' in local_var_params:
            path_params['gateway_id'] = local_var_params['gateway_id']
        if 'target_id' in local_var_params:
            path_params['target_id'] = local_var_params['target_id']

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

    def show_core_ingress_async(self, request):
        r"""查询网关详情

        该接口用于根据ingress_id查询Ingress的详细信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowCoreIngress
        :type request: :class:`huaweicloudsdkagentarts.v1.ShowCoreIngressRequest`
        :rtype: :class:`huaweicloudsdkagentarts.v1.ShowCoreIngressResponse`
        """
        http_info = self._show_core_ingress_http_info(request)
        return self._call_api(**http_info)

    def show_core_ingress_async_invoker(self, request):
        http_info = self._show_core_ingress_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_core_ingress_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/core/ingresses/{ingress_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowCoreIngressResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ingress_id' in local_var_params:
            path_params['ingress_id'] = local_var_params['ingress_id']

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

    def show_core_ingress_network_async(self, request):
        r"""查询VPC入站网络详情

        该接口用于根据网关ID以及入站网络ID查询某一个具体的Agent网关入站网络详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowCoreIngressNetwork
        :type request: :class:`huaweicloudsdkagentarts.v1.ShowCoreIngressNetworkRequest`
        :rtype: :class:`huaweicloudsdkagentarts.v1.ShowCoreIngressNetworkResponse`
        """
        http_info = self._show_core_ingress_network_http_info(request)
        return self._call_api(**http_info)

    def show_core_ingress_network_async_invoker(self, request):
        http_info = self._show_core_ingress_network_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_core_ingress_network_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/core/ingresses/{ingress_id}/vpc-networks/{vpc_ingress_network_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowCoreIngressNetworkResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ingress_id' in local_var_params:
            path_params['ingress_id'] = local_var_params['ingress_id']
        if 'vpc_ingress_network_id' in local_var_params:
            path_params['vpc_ingress_network_id'] = local_var_params['vpc_ingress_network_id']

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

    def show_core_runtime_async(self, request):
        r"""查询单个runtime及指定版本详情

        该接口用于根据Agent运行时ID查询对应的Agent运行时详细信息。该接口可通过version参数指定查询特定版本，不指定则返回最新版本。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowCoreRuntime
        :type request: :class:`huaweicloudsdkagentarts.v1.ShowCoreRuntimeRequest`
        :rtype: :class:`huaweicloudsdkagentarts.v1.ShowCoreRuntimeResponse`
        """
        http_info = self._show_core_runtime_http_info(request)
        return self._call_api(**http_info)

    def show_core_runtime_async_invoker(self, request):
        http_info = self._show_core_runtime_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_core_runtime_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/core/runtimes/{runtime_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowCoreRuntimeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'runtime_id' in local_var_params:
            path_params['runtime_id'] = local_var_params['runtime_id']

        query_params = []
        if 'version' in local_var_params:
            query_params.append(('version', local_var_params['version']))

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

    def show_core_runtime_endpoint_async(self, request):
        r"""查询单个runtime访问方式

        该接口用于根据Agent运行时ID和访问方式ID查询对应的Agent运行时访问方式详细信息。
        **适用场景：**
        查询某一个具体的Agent运行时访问方式的详细信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowCoreRuntimeEndpoint
        :type request: :class:`huaweicloudsdkagentarts.v1.ShowCoreRuntimeEndpointRequest`
        :rtype: :class:`huaweicloudsdkagentarts.v1.ShowCoreRuntimeEndpointResponse`
        """
        http_info = self._show_core_runtime_endpoint_http_info(request)
        return self._call_api(**http_info)

    def show_core_runtime_endpoint_async_invoker(self, request):
        http_info = self._show_core_runtime_endpoint_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_core_runtime_endpoint_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/core/runtimes/{runtime_id}/endpoints/{endpoint_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowCoreRuntimeEndpointResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'runtime_id' in local_var_params:
            path_params['runtime_id'] = local_var_params['runtime_id']
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

    def show_core_space_async(self, request):
        r"""获取Space详情

        根据记忆库ID获取记忆库详细信息，包含完整配置和记忆策略。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowCoreSpace
        :type request: :class:`huaweicloudsdkagentarts.v1.ShowCoreSpaceRequest`
        :rtype: :class:`huaweicloudsdkagentarts.v1.ShowCoreSpaceResponse`
        """
        http_info = self._show_core_space_http_info(request)
        return self._call_api(**http_info)

    def show_core_space_async_invoker(self, request):
        http_info = self._show_core_space_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_core_space_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/core/spaces/{space_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowCoreSpaceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'space_id' in local_var_params:
            path_params['space_id'] = local_var_params['space_id']

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

    def show_core_space_job_async(self, request):
        r"""查询异步任务状态

        查询服务异步任务的执行状态
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowCoreSpaceJob
        :type request: :class:`huaweicloudsdkagentarts.v1.ShowCoreSpaceJobRequest`
        :rtype: :class:`huaweicloudsdkagentarts.v1.ShowCoreSpaceJobResponse`
        """
        http_info = self._show_core_space_job_http_info(request)
        return self._call_api(**http_info)

    def show_core_space_job_async_invoker(self, request):
        http_info = self._show_core_space_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_core_space_job_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/core/spaces/{space_id}/job/{job_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowCoreSpaceJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'space_id' in local_var_params:
            path_params['space_id'] = local_var_params['space_id']
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

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

    def sync_core_gateway_targets_async(self, request):
        r"""同步网关目标工具列表

        同步网关目标工具列表，同步状态可通过查询目标详情查询。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for SyncCoreGatewayTargets
        :type request: :class:`huaweicloudsdkagentarts.v1.SyncCoreGatewayTargetsRequest`
        :rtype: :class:`huaweicloudsdkagentarts.v1.SyncCoreGatewayTargetsResponse`
        """
        http_info = self._sync_core_gateway_targets_http_info(request)
        return self._call_api(**http_info)

    def sync_core_gateway_targets_async_invoker(self, request):
        http_info = self._sync_core_gateway_targets_http_info(request)
        return AsyncInvoker(self, http_info)

    def _sync_core_gateway_targets_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/core/gateways/{gateway_id}/synchronize-targets",
            "request_type": request.__class__.__name__,
            "response_type": "SyncCoreGatewayTargetsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'gateway_id' in local_var_params:
            path_params['gateway_id'] = local_var_params['gateway_id']

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

    def update_core_code_interpreter_async(self, request):
        r"""更新代码解释器

        该API用于更新代码解释器配置。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateCoreCodeInterpreter
        :type request: :class:`huaweicloudsdkagentarts.v1.UpdateCoreCodeInterpreterRequest`
        :rtype: :class:`huaweicloudsdkagentarts.v1.UpdateCoreCodeInterpreterResponse`
        """
        http_info = self._update_core_code_interpreter_http_info(request)
        return self._call_api(**http_info)

    def update_core_code_interpreter_async_invoker(self, request):
        http_info = self._update_core_code_interpreter_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_core_code_interpreter_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/core/code-interpreters/{code_interpreter_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateCoreCodeInterpreterResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'code_interpreter_id' in local_var_params:
            path_params['code_interpreter_id'] = local_var_params['code_interpreter_id']

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

    def update_core_gateway_async(self, request):
        r"""更新网关

        使用新配置更新现有网关。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateCoreGateway
        :type request: :class:`huaweicloudsdkagentarts.v1.UpdateCoreGatewayRequest`
        :rtype: :class:`huaweicloudsdkagentarts.v1.UpdateCoreGatewayResponse`
        """
        http_info = self._update_core_gateway_http_info(request)
        return self._call_api(**http_info)

    def update_core_gateway_async_invoker(self, request):
        http_info = self._update_core_gateway_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_core_gateway_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/core/gateways/{gateway_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateCoreGatewayResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'gateway_id' in local_var_params:
            path_params['gateway_id'] = local_var_params['gateway_id']

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

    def update_core_gateway_target_async(self, request):
        r"""更新目标服务

        更新现有目标服务的配置。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateCoreGatewayTarget
        :type request: :class:`huaweicloudsdkagentarts.v1.UpdateCoreGatewayTargetRequest`
        :rtype: :class:`huaweicloudsdkagentarts.v1.UpdateCoreGatewayTargetResponse`
        """
        http_info = self._update_core_gateway_target_http_info(request)
        return self._call_api(**http_info)

    def update_core_gateway_target_async_invoker(self, request):
        http_info = self._update_core_gateway_target_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_core_gateway_target_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/core/gateways/{gateway_id}/targets/{target_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateCoreGatewayTargetResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'gateway_id' in local_var_params:
            path_params['gateway_id'] = local_var_params['gateway_id']
        if 'target_id' in local_var_params:
            path_params['target_id'] = local_var_params['target_id']

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

    def update_core_ingress_async(self, request):
        r"""更新网关

        该接口用于根据ingress_id更新Ingress的配置信息。（异步接口）
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateCoreIngress
        :type request: :class:`huaweicloudsdkagentarts.v1.UpdateCoreIngressRequest`
        :rtype: :class:`huaweicloudsdkagentarts.v1.UpdateCoreIngressResponse`
        """
        http_info = self._update_core_ingress_http_info(request)
        return self._call_api(**http_info)

    def update_core_ingress_async_invoker(self, request):
        http_info = self._update_core_ingress_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_core_ingress_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/core/ingresses/{ingress_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateCoreIngressResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ingress_id' in local_var_params:
            path_params['ingress_id'] = local_var_params['ingress_id']

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

    def update_core_runtime_async(self, request):
        r"""更新runtime

        该接口用于根据Agent运行时ID修改对应的Agent运行时的配置信息，支持修改Agent镜像，网络配置，运行时委托，环境变量，可观测配置。该接口每次调用会生成一个新的运行时版本（更新tags除外）。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateCoreRuntime
        :type request: :class:`huaweicloudsdkagentarts.v1.UpdateCoreRuntimeRequest`
        :rtype: :class:`huaweicloudsdkagentarts.v1.UpdateCoreRuntimeResponse`
        """
        http_info = self._update_core_runtime_http_info(request)
        return self._call_api(**http_info)

    def update_core_runtime_async_invoker(self, request):
        http_info = self._update_core_runtime_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_core_runtime_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/core/runtimes/{runtime_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateCoreRuntimeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'runtime_id' in local_var_params:
            path_params['runtime_id'] = local_var_params['runtime_id']

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

    def update_core_runtime_endpoint_async(self, request):
        r"""更新runtime访问方式

        该接口用于根据Agent运行时ID和访问方式ID修改对应的Agent运行时访问方式的配置信息，支持修改访问方式对应的版本信息以及多版本之间的权重分配信息。
        **适用场景：**
        修改某一个具体的Agent运行时访问方式的绑定版本。
        修改某一个具体的Agent运行时访问方式的多版本权重配置。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateCoreRuntimeEndpoint
        :type request: :class:`huaweicloudsdkagentarts.v1.UpdateCoreRuntimeEndpointRequest`
        :rtype: :class:`huaweicloudsdkagentarts.v1.UpdateCoreRuntimeEndpointResponse`
        """
        http_info = self._update_core_runtime_endpoint_http_info(request)
        return self._call_api(**http_info)

    def update_core_runtime_endpoint_async_invoker(self, request):
        http_info = self._update_core_runtime_endpoint_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_core_runtime_endpoint_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/core/runtimes/{runtime_id}/endpoints/{endpoint_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateCoreRuntimeEndpointResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'runtime_id' in local_var_params:
            path_params['runtime_id'] = local_var_params['runtime_id']
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

    def update_core_space_async(self, request):
        r"""更新记忆库相关配置

        更新记忆库相关配置，涉及名称、策略等。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateCoreSpace
        :type request: :class:`huaweicloudsdkagentarts.v1.UpdateCoreSpaceRequest`
        :rtype: :class:`huaweicloudsdkagentarts.v1.UpdateCoreSpaceResponse`
        """
        http_info = self._update_core_space_http_info(request)
        return self._call_api(**http_info)

    def update_core_space_async_invoker(self, request):
        http_info = self._update_core_space_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_core_space_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/core/spaces/{space_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateCoreSpaceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'space_id' in local_var_params:
            path_params['space_id'] = local_var_params['space_id']

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

    def update_core_space_customized_strategy_async(self, request):
        r"""更新自定义记忆策略

        更新指定Space下的自定义记忆策略配置。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateCoreSpaceCustomizedStrategy
        :type request: :class:`huaweicloudsdkagentarts.v1.UpdateCoreSpaceCustomizedStrategyRequest`
        :rtype: :class:`huaweicloudsdkagentarts.v1.UpdateCoreSpaceCustomizedStrategyResponse`
        """
        http_info = self._update_core_space_customized_strategy_http_info(request)
        return self._call_api(**http_info)

    def update_core_space_customized_strategy_async_invoker(self, request):
        http_info = self._update_core_space_customized_strategy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_core_space_customized_strategy_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/core/spaces/{space_id}/strategies/customized/{strategy_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateCoreSpaceCustomizedStrategyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'space_id' in local_var_params:
            path_params['space_id'] = local_var_params['space_id']
        if 'strategy_id' in local_var_params:
            path_params['strategy_id'] = local_var_params['strategy_id']

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

    def update_core_space_network_async(self, request):
        r"""更新Space网络配置

        更新指定Space的网络访问配置。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateCoreSpaceNetwork
        :type request: :class:`huaweicloudsdkagentarts.v1.UpdateCoreSpaceNetworkRequest`
        :rtype: :class:`huaweicloudsdkagentarts.v1.UpdateCoreSpaceNetworkResponse`
        """
        http_info = self._update_core_space_network_http_info(request)
        return self._call_api(**http_info)

    def update_core_space_network_async_invoker(self, request):
        http_info = self._update_core_space_network_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_core_space_network_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/core/spaces/{space_id}/network",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateCoreSpaceNetworkResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'space_id' in local_var_params:
            path_params['space_id'] = local_var_params['space_id']

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

    def batch_create_ops_dataset_items_async(self, request):
        r"""批量添加评测集条目

        该接口用于向指定评测集的草稿态批量注入数据行，支持增量添加、覆盖更新或基于历史版本还原数据，并强制校验数据与Schema的符合性。
        适用场景：
        - 数据初始化：在创建评测集后，通过API批量导入首批业务数据或基准测试集。
        - 版本回滚：当前草稿数据出现异常时，通过指定源版本ID将评测集内容恢复至特定历史快照。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchCreateOpsDatasetItems
        :type request: :class:`huaweicloudsdkagentarts.v1.BatchCreateOpsDatasetItemsRequest`
        :rtype: :class:`huaweicloudsdkagentarts.v1.BatchCreateOpsDatasetItemsResponse`
        """
        http_info = self._batch_create_ops_dataset_items_http_info(request)
        return self._call_api(**http_info)

    def batch_create_ops_dataset_items_async_invoker(self, request):
        http_info = self._batch_create_ops_dataset_items_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_create_ops_dataset_items_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/ops/datasets/{dataset_id}/items",
            "request_type": request.__class__.__name__,
            "response_type": "BatchCreateOpsDatasetItemsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'dataset_id' in local_var_params:
            path_params['dataset_id'] = local_var_params['dataset_id']

        query_params = []
        if 'source_version_id' in local_var_params:
            query_params.append(('source_version_id', local_var_params['source_version_id']))
        if 'overwrite' in local_var_params:
            query_params.append(('overwrite', local_var_params['overwrite']))

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

    def batch_delete_ops_dataset_items_async(self, request):
        r"""批量删除评测集条目

        该接口用于通过指定条目ID列表，从当前评测集的草稿版本中批量移除特定的数据行，实现对评测集内容的清理。
        适用场景：
        - 数据清洗：在数据导入后，批量剔除经人工或自动化检测识别出的错误数据、脏数据或重复样本。
        - 评测集优化：根据业务需求对现有的评测资源进行精简，移除测试用例。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchDeleteOpsDatasetItems
        :type request: :class:`huaweicloudsdkagentarts.v1.BatchDeleteOpsDatasetItemsRequest`
        :rtype: :class:`huaweicloudsdkagentarts.v1.BatchDeleteOpsDatasetItemsResponse`
        """
        http_info = self._batch_delete_ops_dataset_items_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_ops_dataset_items_async_invoker(self, request):
        http_info = self._batch_delete_ops_dataset_items_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_delete_ops_dataset_items_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/ops/datasets/{dataset_id}/items",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeleteOpsDatasetItemsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'dataset_id' in local_var_params:
            path_params['dataset_id'] = local_var_params['dataset_id']

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

    def batch_delete_ops_datasets_async(self, request):
        r"""批量删除评测集

        该接口用于通过指定评测集ID列表批量删除不再使用的评测集资源，清理以释放存储空间。
        适用场景：
        - 资源清理：在业务周期结束或项目归档时，批量清理过时的测试数据。
        - 批量操作：支持一次性处理多个ID，适用于批量删除。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchDeleteOpsDatasets
        :type request: :class:`huaweicloudsdkagentarts.v1.BatchDeleteOpsDatasetsRequest`
        :rtype: :class:`huaweicloudsdkagentarts.v1.BatchDeleteOpsDatasetsResponse`
        """
        http_info = self._batch_delete_ops_datasets_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_ops_datasets_async_invoker(self, request):
        http_info = self._batch_delete_ops_datasets_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_delete_ops_datasets_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/ops/datasets",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeleteOpsDatasetsResponse"
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

    def batch_delete_ops_synthesis_tasks_async(self, request):
        r"""批量删除评测集合成任务

        该接口用于通过指定任务ID列表集中清理多个评测集合成任务及其关联的历史记录。
        适用场景：
        - 环境清理：在完成大规模合成实验或多轮对比测试后，批量回收过期的测试任务以释放管理空间。
        - 任务删除：在后台管理系统中，支持用户通过勾选方式一次性销毁多个冗余的任务条目。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchDeleteOpsSynthesisTasks
        :type request: :class:`huaweicloudsdkagentarts.v1.BatchDeleteOpsSynthesisTasksRequest`
        :rtype: :class:`huaweicloudsdkagentarts.v1.BatchDeleteOpsSynthesisTasksResponse`
        """
        http_info = self._batch_delete_ops_synthesis_tasks_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_ops_synthesis_tasks_async_invoker(self, request):
        http_info = self._batch_delete_ops_synthesis_tasks_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_delete_ops_synthesis_tasks_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/ops/datasets-synthesis",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeleteOpsSynthesisTasksResponse"
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

    def create_ops_dataset_async(self, request):
        r"""创建评测集

        该接口用于创建结构化评测集，支持定义评测集的字段，为Agent的评估任务提供标准化的数据来源。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateOpsDataset
        :type request: :class:`huaweicloudsdkagentarts.v1.CreateOpsDatasetRequest`
        :rtype: :class:`huaweicloudsdkagentarts.v1.CreateOpsDatasetResponse`
        """
        http_info = self._create_ops_dataset_http_info(request)
        return self._call_api(**http_info)

    def create_ops_dataset_async_invoker(self, request):
        http_info = self._create_ops_dataset_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_ops_dataset_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/ops/datasets",
            "request_type": request.__class__.__name__,
            "response_type": "CreateOpsDatasetResponse"
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

    def create_ops_synthesis_task_async(self, request):
        r"""创建评测集合成任务

        该接口用于利用大模型能力发起异步的数据合成任务，通过种子数据泛化（Seed-based Generalization）等手段自动生成高质量、多样化的训练或评测样本。
        适用场景：
        - 数据样本扩充：在现有数据量不足时，基于少量种子数据生成大规模同分布的模拟数据，提升模型训练效果。
        - 边界场景覆盖：通过 AI 模拟生成罕见或特定领域的对话记录，增强评测集对极端情况（Edge Cases）的覆盖度。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateOpsSynthesisTask
        :type request: :class:`huaweicloudsdkagentarts.v1.CreateOpsSynthesisTaskRequest`
        :rtype: :class:`huaweicloudsdkagentarts.v1.CreateOpsSynthesisTaskResponse`
        """
        http_info = self._create_ops_synthesis_task_http_info(request)
        return self._call_api(**http_info)

    def create_ops_synthesis_task_async_invoker(self, request):
        http_info = self._create_ops_synthesis_task_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_ops_synthesis_task_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/ops/datasets-synthesis",
            "request_type": request.__class__.__name__,
            "response_type": "CreateOpsSynthesisTaskResponse"
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

    def delete_ops_dataset_async(self, request):
        r"""删除评测集

        该接口用于通过指定评测集ID彻底删除评测集中的所有的数据条目、Schema定义和历史版本。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteOpsDataset
        :type request: :class:`huaweicloudsdkagentarts.v1.DeleteOpsDatasetRequest`
        :rtype: :class:`huaweicloudsdkagentarts.v1.DeleteOpsDatasetResponse`
        """
        http_info = self._delete_ops_dataset_http_info(request)
        return self._call_api(**http_info)

    def delete_ops_dataset_async_invoker(self, request):
        http_info = self._delete_ops_dataset_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_ops_dataset_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/ops/datasets/{dataset_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteOpsDatasetResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'dataset_id' in local_var_params:
            path_params['dataset_id'] = local_var_params['dataset_id']

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

    def delete_ops_dataset_version_async(self, request):
        r"""删除评测集版本

        该接口用于永久删除指定的评测集历史版本及其关联的所有条目快照数据。
        适用场景：
        - 合规性清理：根据数据保留政策或合规性要求，物理删除过期的、包含敏感信息的历史数据版本。
        - 删除冗余：在评测集生命周期后期，移除冗余的中间过程版本，保持资产列表的整洁。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteOpsDatasetVersion
        :type request: :class:`huaweicloudsdkagentarts.v1.DeleteOpsDatasetVersionRequest`
        :rtype: :class:`huaweicloudsdkagentarts.v1.DeleteOpsDatasetVersionResponse`
        """
        http_info = self._delete_ops_dataset_version_http_info(request)
        return self._call_api(**http_info)

    def delete_ops_dataset_version_async_invoker(self, request):
        http_info = self._delete_ops_dataset_version_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_ops_dataset_version_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/ops/datasets/{dataset_id}/versions/{version_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteOpsDatasetVersionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'dataset_id' in local_var_params:
            path_params['dataset_id'] = local_var_params['dataset_id']
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

    def delete_ops_synthesis_task_async(self, request):
        r"""删除评测集合成任务

        该接口用于删除指定的数据集合成任务，通过移除任务记录及其关联的临时数据，实现任务列表清理。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteOpsSynthesisTask
        :type request: :class:`huaweicloudsdkagentarts.v1.DeleteOpsSynthesisTaskRequest`
        :rtype: :class:`huaweicloudsdkagentarts.v1.DeleteOpsSynthesisTaskResponse`
        """
        http_info = self._delete_ops_synthesis_task_http_info(request)
        return self._call_api(**http_info)

    def delete_ops_synthesis_task_async_invoker(self, request):
        http_info = self._delete_ops_synthesis_task_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_ops_synthesis_task_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/ops/datasets-synthesis/{synthesis_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteOpsSynthesisTaskResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'synthesis_id' in local_var_params:
            path_params['synthesis_id'] = local_var_params['synthesis_id']

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

    def import_ops_dataset_items_async(self, request):
        r"""评测集导入

        该接口用于从本地文件或历史版本中将海量数据批量导入至指定评测集的草稿版本中，支持多种格式解析及灵活的写入模式。
        适用场景：
        - 评测集同步：将存储在OBS（对象存储服务）中的海量生产数据或标注数据自动化同步至评测系统。
        - 评测集更替：利用全量覆盖模式（Overwrite），一键重置当前草稿版本的数据内容。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ImportOpsDatasetItems
        :type request: :class:`huaweicloudsdkagentarts.v1.ImportOpsDatasetItemsRequest`
        :rtype: :class:`huaweicloudsdkagentarts.v1.ImportOpsDatasetItemsResponse`
        """
        http_info = self._import_ops_dataset_items_http_info(request)
        return self._call_api(**http_info)

    def import_ops_dataset_items_async_invoker(self, request):
        http_info = self._import_ops_dataset_items_http_info(request)
        return AsyncInvoker(self, http_info)

    def _import_ops_dataset_items_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/ops/datasets/{dataset_id}/items/import",
            "request_type": request.__class__.__name__,
            "response_type": "ImportOpsDatasetItemsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'dataset_id' in local_var_params:
            path_params['dataset_id'] = local_var_params['dataset_id']

        query_params = []
        if 'source_version_id' in local_var_params:
            query_params.append(('source_version_id', local_var_params['source_version_id']))
        if 'overwrite' in local_var_params:
            query_params.append(('overwrite', local_var_params['overwrite']))
        if 'get_obs_url' in local_var_params:
            query_params.append(('get_obs_url', local_var_params['get_obs_url']))
        if 'obs_object_name' in local_var_params:
            query_params.append(('obs_object_name', local_var_params['obs_object_name']))
        if 'obs_file_hash' in local_var_params:
            query_params.append(('obs_file_hash', local_var_params['obs_file_hash']))

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

    def import_ops_results_async(self, request):
        r"""导入结果到评测集

        将条目导入到目标评测集，支持导入到现有评测集或创建新评测集。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ImportOpsResults
        :type request: :class:`huaweicloudsdkagentarts.v1.ImportOpsResultsRequest`
        :rtype: :class:`huaweicloudsdkagentarts.v1.ImportOpsResultsResponse`
        """
        http_info = self._import_ops_results_http_info(request)
        return self._call_api(**http_info)

    def import_ops_results_async_invoker(self, request):
        http_info = self._import_ops_results_http_info(request)
        return AsyncInvoker(self, http_info)

    def _import_ops_results_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/ops/datasets/import",
            "request_type": request.__class__.__name__,
            "response_type": "ImportOpsResultsResponse"
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

    def list_ops_dataset_items_async(self, request):
        r"""获取评测集条目列表

        该接口用于分页检索指定评测集的具体数据记录，支持查看当前草稿态数据或特定历史发布版本的数据样本。
        适用场景：
        - 内容预览：在评测集详情页分页展示具体的数据行，供用户直观核查数据质量。
        - 版本溯源：通过指定版本ID，检索并对比历史发布版本中的样本数据。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListOpsDatasetItems
        :type request: :class:`huaweicloudsdkagentarts.v1.ListOpsDatasetItemsRequest`
        :rtype: :class:`huaweicloudsdkagentarts.v1.ListOpsDatasetItemsResponse`
        """
        http_info = self._list_ops_dataset_items_http_info(request)
        return self._call_api(**http_info)

    def list_ops_dataset_items_async_invoker(self, request):
        http_info = self._list_ops_dataset_items_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_ops_dataset_items_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/ops/datasets/{dataset_id}/items",
            "request_type": request.__class__.__name__,
            "response_type": "ListOpsDatasetItemsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'dataset_id' in local_var_params:
            path_params['dataset_id'] = local_var_params['dataset_id']

        query_params = []
        if 'version_id' in local_var_params:
            query_params.append(('version_id', local_var_params['version_id']))
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

    def list_ops_dataset_items_import_tasks_async(self, request):
        r"""获取评测集导入任务列表

        该接口用于分页查询指定评测集下所有异步导入任务的执行状态、实时进度及详细统计信息，支持通过任务ID进行精确过滤。
        适用场景：
        - 进度查看：在提交大规模数据导入请求后，实时跟踪任务的完成百分比与当前处理状态。
        - 历史追溯：复盘评测集内容的来源、导入时间及各批次任务的执行结果。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListOpsDatasetItemsImportTasks
        :type request: :class:`huaweicloudsdkagentarts.v1.ListOpsDatasetItemsImportTasksRequest`
        :rtype: :class:`huaweicloudsdkagentarts.v1.ListOpsDatasetItemsImportTasksResponse`
        """
        http_info = self._list_ops_dataset_items_import_tasks_http_info(request)
        return self._call_api(**http_info)

    def list_ops_dataset_items_import_tasks_async_invoker(self, request):
        http_info = self._list_ops_dataset_items_import_tasks_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_ops_dataset_items_import_tasks_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/ops/datasets/{dataset_id}/items/import/tasks",
            "request_type": request.__class__.__name__,
            "response_type": "ListOpsDatasetItemsImportTasksResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'dataset_id' in local_var_params:
            path_params['dataset_id'] = local_var_params['dataset_id']

        query_params = []
        if 'task_id' in local_var_params:
            query_params.append(('task_id', local_var_params['task_id']))

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

    def list_ops_dataset_schemas_async(self, request):
        r"""获取评测集 Schema

        该接口用于专门检索指定评测集信息，获取所有字段的名称、数据类型及约束规则，为数据处理提供标准的Schema视图。
        适用场景：
        - 数据导入校验：在用户上传或导入数据前，核对本地文件格式是否与评测集定义的字段规范一致。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListOpsDatasetSchemas
        :type request: :class:`huaweicloudsdkagentarts.v1.ListOpsDatasetSchemasRequest`
        :rtype: :class:`huaweicloudsdkagentarts.v1.ListOpsDatasetSchemasResponse`
        """
        http_info = self._list_ops_dataset_schemas_http_info(request)
        return self._call_api(**http_info)

    def list_ops_dataset_schemas_async_invoker(self, request):
        http_info = self._list_ops_dataset_schemas_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_ops_dataset_schemas_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/ops/datasets/{dataset_id}/schemas",
            "request_type": request.__class__.__name__,
            "response_type": "ListOpsDatasetSchemasResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'dataset_id' in local_var_params:
            path_params['dataset_id'] = local_var_params['dataset_id']

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

    def list_ops_dataset_versions_async(self, request):
        r"""获取评测集版本列表

        接口用于通过分页方式查询指定数据集下所有已成功发布的历史版本记录，按发布时间倒序排列，为用户提供数据集变更历史。
        适用场景：
        - 版本回溯：查看数据集的发布历史，追踪数据集随时间演进的变更记录。
        - 版本差异对比：获取不同版本的ID信息，以便后续调取详情接口进行内容或Schema的差异化分析。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListOpsDatasetVersions
        :type request: :class:`huaweicloudsdkagentarts.v1.ListOpsDatasetVersionsRequest`
        :rtype: :class:`huaweicloudsdkagentarts.v1.ListOpsDatasetVersionsResponse`
        """
        http_info = self._list_ops_dataset_versions_http_info(request)
        return self._call_api(**http_info)

    def list_ops_dataset_versions_async_invoker(self, request):
        http_info = self._list_ops_dataset_versions_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_ops_dataset_versions_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/ops/datasets/{dataset_id}/versions",
            "request_type": request.__class__.__name__,
            "response_type": "ListOpsDatasetVersionsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'dataset_id' in local_var_params:
            path_params['dataset_id'] = local_var_params['dataset_id']

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

    def list_ops_datasets_async(self, request):
        r"""获取评测集列表

        该接口用于分页查询当前项目下的评测集列表，支持按名称模糊检索和更新人筛选，帮助用户实现对评测集资产的全局视图管理。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListOpsDatasets
        :type request: :class:`huaweicloudsdkagentarts.v1.ListOpsDatasetsRequest`
        :rtype: :class:`huaweicloudsdkagentarts.v1.ListOpsDatasetsResponse`
        """
        http_info = self._list_ops_datasets_http_info(request)
        return self._call_api(**http_info)

    def list_ops_datasets_async_invoker(self, request):
        http_info = self._list_ops_datasets_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_ops_datasets_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/ops/datasets",
            "request_type": request.__class__.__name__,
            "response_type": "ListOpsDatasetsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'updated_by' in local_var_params:
            query_params.append(('updated_by', local_var_params['updated_by']))
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

    def list_ops_synthesis_items_async(self, request):
        r"""查询合成的条目列表

        该接口用于分页查询特定合成任务所生成的详细条目数据，支持在任务运行中和检索样本内容。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListOpsSynthesisItems
        :type request: :class:`huaweicloudsdkagentarts.v1.ListOpsSynthesisItemsRequest`
        :rtype: :class:`huaweicloudsdkagentarts.v1.ListOpsSynthesisItemsResponse`
        """
        http_info = self._list_ops_synthesis_items_http_info(request)
        return self._call_api(**http_info)

    def list_ops_synthesis_items_async_invoker(self, request):
        http_info = self._list_ops_synthesis_items_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_ops_synthesis_items_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/ops/datasets-synthesis/{synthesis_id}/items",
            "request_type": request.__class__.__name__,
            "response_type": "ListOpsSynthesisItemsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'synthesis_id' in local_var_params:
            path_params['synthesis_id'] = local_var_params['synthesis_id']

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

    def list_ops_synthesis_tasks_async(self, request):
        r"""查询评测集合成任务列表

        该接口用于分页查询当前租户下所有已提交的评测集合成异步任务，支持按任务名称、状态等多种过滤条件进行检索，提供任务执行进度。
        适用场景：
        - 任务进度查看：在发起大规模数据合成后，通过此接口批量获取任务的运行状态（如：进行中、已完成、已失败）。
        - 历史合成记录管理：复盘并管理过往提交的数据生成任务，审计合成任务的执行频率与成功率。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListOpsSynthesisTasks
        :type request: :class:`huaweicloudsdkagentarts.v1.ListOpsSynthesisTasksRequest`
        :rtype: :class:`huaweicloudsdkagentarts.v1.ListOpsSynthesisTasksResponse`
        """
        http_info = self._list_ops_synthesis_tasks_http_info(request)
        return self._call_api(**http_info)

    def list_ops_synthesis_tasks_async_invoker(self, request):
        http_info = self._list_ops_synthesis_tasks_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_ops_synthesis_tasks_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/ops/datasets-synthesis",
            "request_type": request.__class__.__name__,
            "response_type": "ListOpsSynthesisTasksResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
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

    def publish_ops_dataset_version_async(self, request):
        r"""发布评测集版本

        该接口用于将当前处于草稿状态的数据内容固化，生成一个不可变的历史快照版本，并分配唯一版本ID以确保数据在后续调用中的可追溯性。
        适用场景：
        - 版本固化：在完成评测集条目的增删改等一系列调整后，通过发布版本将当前数据状态锁定。
        - 评测任务关联：为模型评测或训练任务提供一个静态的数据输入源，防止因草稿内容变动导致实验结果不可复现。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for PublishOpsDatasetVersion
        :type request: :class:`huaweicloudsdkagentarts.v1.PublishOpsDatasetVersionRequest`
        :rtype: :class:`huaweicloudsdkagentarts.v1.PublishOpsDatasetVersionResponse`
        """
        http_info = self._publish_ops_dataset_version_http_info(request)
        return self._call_api(**http_info)

    def publish_ops_dataset_version_async_invoker(self, request):
        http_info = self._publish_ops_dataset_version_http_info(request)
        return AsyncInvoker(self, http_info)

    def _publish_ops_dataset_version_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/ops/datasets/{dataset_id}/versions",
            "request_type": request.__class__.__name__,
            "response_type": "PublishOpsDatasetVersionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'dataset_id' in local_var_params:
            path_params['dataset_id'] = local_var_params['dataset_id']

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

    def show_ops_dataset_async(self, request):
        r"""获取评测集详情

        该接口用于根据评测集ID获取其完整的元数据配置，包括字段结构定义、基本属性及关联的历史发布版本列表。
        适用场景：
        - 评测配置校验：在启动评估任务前，开发者通过此接口确认评测集的字段是否符合评估任务输入要求。
        - 版本回溯与管理：获取评测集下属的所有版本信息，以便进行版本对比或指定特定版本进行操作。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowOpsDataset
        :type request: :class:`huaweicloudsdkagentarts.v1.ShowOpsDatasetRequest`
        :rtype: :class:`huaweicloudsdkagentarts.v1.ShowOpsDatasetResponse`
        """
        http_info = self._show_ops_dataset_http_info(request)
        return self._call_api(**http_info)

    def show_ops_dataset_async_invoker(self, request):
        http_info = self._show_ops_dataset_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_ops_dataset_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/ops/datasets/{dataset_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowOpsDatasetResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'dataset_id' in local_var_params:
            path_params['dataset_id'] = local_var_params['dataset_id']

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

    def show_ops_dataset_item_async(self, request):
        r"""获取评测集条目详情

        该接口用于精确获取评测集中某一行特定数据条目的完整内容，通过评测集ID与条目ID的双重定位。
        适用场景：
        - 单条样本核对：在对模型评测结果产生疑问时，调取对应原始数据条目的全量信息进行比对。
        - 数据编辑回显：在用户进入单条数据编辑界面前，通过此接口加载该条目的当前配置与字段内容。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowOpsDatasetItem
        :type request: :class:`huaweicloudsdkagentarts.v1.ShowOpsDatasetItemRequest`
        :rtype: :class:`huaweicloudsdkagentarts.v1.ShowOpsDatasetItemResponse`
        """
        http_info = self._show_ops_dataset_item_http_info(request)
        return self._call_api(**http_info)

    def show_ops_dataset_item_async_invoker(self, request):
        http_info = self._show_ops_dataset_item_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_ops_dataset_item_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/ops/datasets/{dataset_id}/items/{item_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowOpsDatasetItemResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'dataset_id' in local_var_params:
            path_params['dataset_id'] = local_var_params['dataset_id']
        if 'item_id' in local_var_params:
            path_params['item_id'] = local_var_params['item_id']

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

    def show_ops_dataset_version_async(self, request):
        r"""获取评测集版本详情

        该接口用于通过指定版本ID检索特定历史版本的完整元数据，包含发布时的Schema结构快照、数据规模统计及版本属性。
        适用场景：
        - 历史版本对比：核对已发布评测集在特定时间点的字段定义、数据规模和配置参数。
        - 变更差异分析：获取特定版本的结构化快照，以便与当前草稿态或其他历史版本进行元数据维度的对比。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowOpsDatasetVersion
        :type request: :class:`huaweicloudsdkagentarts.v1.ShowOpsDatasetVersionRequest`
        :rtype: :class:`huaweicloudsdkagentarts.v1.ShowOpsDatasetVersionResponse`
        """
        http_info = self._show_ops_dataset_version_http_info(request)
        return self._call_api(**http_info)

    def show_ops_dataset_version_async_invoker(self, request):
        http_info = self._show_ops_dataset_version_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_ops_dataset_version_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/ops/datasets/{dataset_id}/versions/{version_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowOpsDatasetVersionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'dataset_id' in local_var_params:
            path_params['dataset_id'] = local_var_params['dataset_id']
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

    def show_ops_synthesis_task_async(self, request):
        r"""查询评测集合成任务详情

        该接口用于通过任务ID检索特定评测集合成任务的完整信息，涵盖任务配置快照、实时执行状态及生成统计。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowOpsSynthesisTask
        :type request: :class:`huaweicloudsdkagentarts.v1.ShowOpsSynthesisTaskRequest`
        :rtype: :class:`huaweicloudsdkagentarts.v1.ShowOpsSynthesisTaskResponse`
        """
        http_info = self._show_ops_synthesis_task_http_info(request)
        return self._call_api(**http_info)

    def show_ops_synthesis_task_async_invoker(self, request):
        http_info = self._show_ops_synthesis_task_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_ops_synthesis_task_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/ops/datasets-synthesis/{synthesis_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowOpsSynthesisTaskResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'synthesis_id' in local_var_params:
            path_params['synthesis_id'] = local_var_params['synthesis_id']

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

    def update_ops_dataset_async(self, request):
        r"""修改评测集

        该接口用于更新现有评测集的名称和业务描述等信息，旨在确保资产信息的准确性与时效性，且操作不涉及对Schema字段定义的变更。
        适用场景：
        - 描述完善：在评测集创建后，补充更详细的业务背景、用途说明或标注说明。
        - 名称更改：根据业务需求变更或内部命名规范调整，修改评测集的显示名称。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateOpsDataset
        :type request: :class:`huaweicloudsdkagentarts.v1.UpdateOpsDatasetRequest`
        :rtype: :class:`huaweicloudsdkagentarts.v1.UpdateOpsDatasetResponse`
        """
        http_info = self._update_ops_dataset_http_info(request)
        return self._call_api(**http_info)

    def update_ops_dataset_async_invoker(self, request):
        http_info = self._update_ops_dataset_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_ops_dataset_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/ops/datasets/{dataset_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateOpsDatasetResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'dataset_id' in local_var_params:
            path_params['dataset_id'] = local_var_params['dataset_id']

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

    def update_ops_dataset_item_async(self, request):
        r"""更新评测集条目

        该接口用于对指定评测集草稿版本中已存在的特定数据行进行修改，确保条目内容符合Schema结构校验。
        适用场景：
        - 样本内容完善：针对多轮对话或复杂数据集，补充缺失的字段信息或优化对话轮次逻辑。
        - 业务数值更新：当底层业务逻辑变化导致原有的评测基准数据失效时，手动更新特定条目的预期输出。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateOpsDatasetItem
        :type request: :class:`huaweicloudsdkagentarts.v1.UpdateOpsDatasetItemRequest`
        :rtype: :class:`huaweicloudsdkagentarts.v1.UpdateOpsDatasetItemResponse`
        """
        http_info = self._update_ops_dataset_item_http_info(request)
        return self._call_api(**http_info)

    def update_ops_dataset_item_async_invoker(self, request):
        http_info = self._update_ops_dataset_item_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_ops_dataset_item_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/ops/datasets/{dataset_id}/items/{item_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateOpsDatasetItemResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'dataset_id' in local_var_params:
            path_params['dataset_id'] = local_var_params['dataset_id']
        if 'item_id' in local_var_params:
            path_params['item_id'] = local_var_params['item_id']

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

    def update_ops_dataset_tags_async(self, request):
        r"""更新评测集标签

        该接口用于更新指定数据集的分类标签体系，通过全量覆盖的方式重新定义数据集的标签属性，实现对数据的精细化归类与检索。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateOpsDatasetTags
        :type request: :class:`huaweicloudsdkagentarts.v1.UpdateOpsDatasetTagsRequest`
        :rtype: :class:`huaweicloudsdkagentarts.v1.UpdateOpsDatasetTagsResponse`
        """
        http_info = self._update_ops_dataset_tags_http_info(request)
        return self._call_api(**http_info)

    def update_ops_dataset_tags_async_invoker(self, request):
        http_info = self._update_ops_dataset_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_ops_dataset_tags_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/ops/datasets/{dataset_id}/tags",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateOpsDatasetTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'dataset_id' in local_var_params:
            path_params['dataset_id'] = local_var_params['dataset_id']

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

    def update_ops_synthesis_task_async(self, request):
        r"""更新评测集合成任务状态

        该接口用于对指定的评测集合成任务执行生命周期状态控制，支持触发任务启动或手动中止执行。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateOpsSynthesisTask
        :type request: :class:`huaweicloudsdkagentarts.v1.UpdateOpsSynthesisTaskRequest`
        :rtype: :class:`huaweicloudsdkagentarts.v1.UpdateOpsSynthesisTaskResponse`
        """
        http_info = self._update_ops_synthesis_task_http_info(request)
        return self._call_api(**http_info)

    def update_ops_synthesis_task_async_invoker(self, request):
        http_info = self._update_ops_synthesis_task_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_ops_synthesis_task_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/ops/datasets-synthesis/{synthesis_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateOpsSynthesisTaskResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'synthesis_id' in local_var_params:
            path_params['synthesis_id'] = local_var_params['synthesis_id']

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

    def list_ops_evaluation_models_async(self, request):
        r"""获取模型信息

        该接口用于获取系统中所有可用的基础大模型及微调模型的详细列表，涵盖模型能力类型、状态及访问参数。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListOpsEvaluationModels
        :type request: :class:`huaweicloudsdkagentarts.v1.ListOpsEvaluationModelsRequest`
        :rtype: :class:`huaweicloudsdkagentarts.v1.ListOpsEvaluationModelsResponse`
        """
        http_info = self._list_ops_evaluation_models_http_info(request)
        return self._call_api(**http_info)

    def list_ops_evaluation_models_async_invoker(self, request):
        http_info = self._list_ops_evaluation_models_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_ops_evaluation_models_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/ops/evaluation-models",
            "request_type": request.__class__.__name__,
            "response_type": "ListOpsEvaluationModelsResponse"
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

    def show_ops_evaluation_model_async(self, request):
        r"""获取单个模型信息

        该接口用于通过模型ID获取特定大模型的详细元数据，包含其技术规格、版本信息、支持的协议能力及服务终点。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowOpsEvaluationModel
        :type request: :class:`huaweicloudsdkagentarts.v1.ShowOpsEvaluationModelRequest`
        :rtype: :class:`huaweicloudsdkagentarts.v1.ShowOpsEvaluationModelResponse`
        """
        http_info = self._show_ops_evaluation_model_http_info(request)
        return self._call_api(**http_info)

    def show_ops_evaluation_model_async_invoker(self, request):
        http_info = self._show_ops_evaluation_model_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_ops_evaluation_model_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/ops/evaluation-models/{model_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowOpsEvaluationModelResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
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

    def batch_delete_ops_evaluator_async(self, request):
        r"""批量删除评估器

        该接口用于通过评估器ID列表批量移除不再使用的评估工具定义，
        适用场景：
        - 冗余清理：定期移除测试阶段产生的临时评估器或已过时的评价准则，保持评估器仓库的整洁。
        - 评价体系更迭：当业务评测标准发生重大调整，需要彻底废弃并清理旧版评估逻辑时使用。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchDeleteOpsEvaluator
        :type request: :class:`huaweicloudsdkagentarts.v1.BatchDeleteOpsEvaluatorRequest`
        :rtype: :class:`huaweicloudsdkagentarts.v1.BatchDeleteOpsEvaluatorResponse`
        """
        http_info = self._batch_delete_ops_evaluator_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_ops_evaluator_async_invoker(self, request):
        http_info = self._batch_delete_ops_evaluator_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_delete_ops_evaluator_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/ops/evaluators",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeleteOpsEvaluatorResponse"
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

    def create_ops_evaluator_async(self, request):
        r"""新建评估器

        该接口用于在系统中注册并创建一个新的评估器（Evaluator），通过定义具体的评估逻辑、判分准则及参数配置，为模型输出的质量度量提供标准化工具。
        适用场景：
        - 自定义评价体系构建：针对特定业务领域（如法律、医疗），创建符合行业规范的判分插件或规则脚本。
        - 评测流程标准化：预设通用的评估模板（如准确率、相关性、毒性检测），实现多模型间的横向对比。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateOpsEvaluator
        :type request: :class:`huaweicloudsdkagentarts.v1.CreateOpsEvaluatorRequest`
        :rtype: :class:`huaweicloudsdkagentarts.v1.CreateOpsEvaluatorResponse`
        """
        http_info = self._create_ops_evaluator_http_info(request)
        return self._call_api(**http_info)

    def create_ops_evaluator_async_invoker(self, request):
        http_info = self._create_ops_evaluator_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_ops_evaluator_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/ops/evaluators",
            "request_type": request.__class__.__name__,
            "response_type": "CreateOpsEvaluatorResponse"
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

    def debug_ops_evaluator_async(self, request):
        r"""评估器调试

        该接口用于对评估器的判分逻辑进行实时调试，通过输入样例数据验证评估器的解析能力、Prompt 效果及评分准确性。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DebugOpsEvaluator
        :type request: :class:`huaweicloudsdkagentarts.v1.DebugOpsEvaluatorRequest`
        :rtype: :class:`huaweicloudsdkagentarts.v1.DebugOpsEvaluatorResponse`
        """
        http_info = self._debug_ops_evaluator_http_info(request)
        return self._call_api(**http_info)

    def debug_ops_evaluator_async_invoker(self, request):
        http_info = self._debug_ops_evaluator_http_info(request)
        return AsyncInvoker(self, http_info)

    def _debug_ops_evaluator_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/ops/evaluators/debug",
            "request_type": request.__class__.__name__,
            "response_type": "DebugOpsEvaluatorResponse"
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

    def delete_ops_evaluator_async(self, request):
        r"""删除单个评估器

        该接口用于通过指定的评估器ID删除对应的评估工具定义，是从系统资产库中彻底移除单条评测标准的不可逆操作。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteOpsEvaluator
        :type request: :class:`huaweicloudsdkagentarts.v1.DeleteOpsEvaluatorRequest`
        :rtype: :class:`huaweicloudsdkagentarts.v1.DeleteOpsEvaluatorResponse`
        """
        http_info = self._delete_ops_evaluator_http_info(request)
        return self._call_api(**http_info)

    def delete_ops_evaluator_async_invoker(self, request):
        http_info = self._delete_ops_evaluator_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_ops_evaluator_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/ops/evaluators/{evaluator_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteOpsEvaluatorResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'evaluator_id' in local_var_params:
            path_params['evaluator_id'] = local_var_params['evaluator_id']

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

    def delete_ops_evaluator_version_async(self, request):
        r"""删除评估器特定版本

        该接口用于从指定评估器的版本序列中永久移除特定的历史快照。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteOpsEvaluatorVersion
        :type request: :class:`huaweicloudsdkagentarts.v1.DeleteOpsEvaluatorVersionRequest`
        :rtype: :class:`huaweicloudsdkagentarts.v1.DeleteOpsEvaluatorVersionResponse`
        """
        http_info = self._delete_ops_evaluator_version_http_info(request)
        return self._call_api(**http_info)

    def delete_ops_evaluator_version_async_invoker(self, request):
        http_info = self._delete_ops_evaluator_version_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_ops_evaluator_version_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/ops/evaluators/{evaluator_id}/versions/{version_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteOpsEvaluatorVersionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'evaluator_id' in local_var_params:
            path_params['evaluator_id'] = local_var_params['evaluator_id']
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

    def generate_ops_evaluator_evaluation_steps_async(self, request):
        r"""智能生成G-Eval评估步骤

        该接口用于根据用户提供的规则描述(criteria)，利用大模型自动生成结构化的评估步骤。
        通过自适应的方式降低用户编写评估提示词的门槛，提升评估器配置效率。
        
        **约束限制：**
        - criteria长度必须在1到20000之间。
        - criteria必须包含{{}}格式的变量。
        - 变量需用双大括号包裹。
        
        **典型应用场景：**
        用户在创建自定义评估器时，只需输入自然语言描述的规则描述，系统即可自动生成规范的评估步骤。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for GenerateOpsEvaluatorEvaluationSteps
        :type request: :class:`huaweicloudsdkagentarts.v1.GenerateOpsEvaluatorEvaluationStepsRequest`
        :rtype: :class:`huaweicloudsdkagentarts.v1.GenerateOpsEvaluatorEvaluationStepsResponse`
        """
        http_info = self._generate_ops_evaluator_evaluation_steps_http_info(request)
        return self._call_api(**http_info)

    def generate_ops_evaluator_evaluation_steps_async_invoker(self, request):
        http_info = self._generate_ops_evaluator_evaluation_steps_http_info(request)
        return AsyncInvoker(self, http_info)

    def _generate_ops_evaluator_evaluation_steps_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/ops/evaluators/evaluation-steps/generate",
            "request_type": request.__class__.__name__,
            "response_type": "GenerateOpsEvaluatorEvaluationStepsResponse"
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

    def list_ops_evaluator_filter_options_async(self, request):
        r"""获取评估器筛选选项列表

        该接口用于获取评估器列表页面可用的筛选维度及其枚举值。
        前端通过此接口动态渲染筛选下拉框，帮助用户快速定位所需的评估器。
        
        **返回的筛选项包括：**
        - evaluator_type: 评估器类型（模型判定/代码判定/自适应判定）
        - turn_type: 对话轮次类型（单轮/多轮）
        - evaluator_content_type: 内容类型（文本/轨迹）
        - evaluator_objective_type: 评估目标类型（任务完成/输出质量/安全/工具调用/轨迹质量）
        
        **典型应用场景：**
        用户在评估器列表页面选择筛选条件时，前端调用此接口获取可选的筛选项。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListOpsEvaluatorFilterOptions
        :type request: :class:`huaweicloudsdkagentarts.v1.ListOpsEvaluatorFilterOptionsRequest`
        :rtype: :class:`huaweicloudsdkagentarts.v1.ListOpsEvaluatorFilterOptionsResponse`
        """
        http_info = self._list_ops_evaluator_filter_options_http_info(request)
        return self._call_api(**http_info)

    def list_ops_evaluator_filter_options_async_invoker(self, request):
        http_info = self._list_ops_evaluator_filter_options_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_ops_evaluator_filter_options_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/ops/evaluator-filter-options",
            "request_type": request.__class__.__name__,
            "response_type": "ListOpsEvaluatorFilterOptionsResponse"
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

    def list_ops_evaluator_versions_async(self, request):
        r"""获取评估器所有版本信息

        该接口用于查询指定评估器下所有已发布的历史版本列表，提供各版本的发布时间、逻辑快照及版本状态。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListOpsEvaluatorVersions
        :type request: :class:`huaweicloudsdkagentarts.v1.ListOpsEvaluatorVersionsRequest`
        :rtype: :class:`huaweicloudsdkagentarts.v1.ListOpsEvaluatorVersionsResponse`
        """
        http_info = self._list_ops_evaluator_versions_http_info(request)
        return self._call_api(**http_info)

    def list_ops_evaluator_versions_async_invoker(self, request):
        http_info = self._list_ops_evaluator_versions_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_ops_evaluator_versions_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/ops/evaluators/{evaluator_id}/versions",
            "request_type": request.__class__.__name__,
            "response_type": "ListOpsEvaluatorVersionsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'evaluator_id' in local_var_params:
            path_params['evaluator_id'] = local_var_params['evaluator_id']

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

    def list_ops_evaluators_async(self, request):
        r"""获取评估器信息列表

        该接口用于分页查询当前租户下所有已注册的评估器信息，支持按名称、类型或创建时间进行过滤评估器。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListOpsEvaluators
        :type request: :class:`huaweicloudsdkagentarts.v1.ListOpsEvaluatorsRequest`
        :rtype: :class:`huaweicloudsdkagentarts.v1.ListOpsEvaluatorsResponse`
        """
        http_info = self._list_ops_evaluators_http_info(request)
        return self._call_api(**http_info)

    def list_ops_evaluators_async_invoker(self, request):
        http_info = self._list_ops_evaluators_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_ops_evaluators_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/ops/evaluators/list",
            "request_type": request.__class__.__name__,
            "response_type": "ListOpsEvaluatorsResponse"
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

    def publish_ops_evaluator_version_async(self, request):
        r"""发布评估器新版本

        该接口用于为指定的评估器创建并发布一个全新的快照版本，通过固化当前的判分逻辑与参数配置，实现评测标准的版本化管理与历史可追溯。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for PublishOpsEvaluatorVersion
        :type request: :class:`huaweicloudsdkagentarts.v1.PublishOpsEvaluatorVersionRequest`
        :rtype: :class:`huaweicloudsdkagentarts.v1.PublishOpsEvaluatorVersionResponse`
        """
        http_info = self._publish_ops_evaluator_version_http_info(request)
        return self._call_api(**http_info)

    def publish_ops_evaluator_version_async_invoker(self, request):
        http_info = self._publish_ops_evaluator_version_http_info(request)
        return AsyncInvoker(self, http_info)

    def _publish_ops_evaluator_version_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/ops/evaluators/{evaluator_id}/versions",
            "request_type": request.__class__.__name__,
            "response_type": "PublishOpsEvaluatorVersionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'evaluator_id' in local_var_params:
            path_params['evaluator_id'] = local_var_params['evaluator_id']

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

    def show_ops_evaluator_async(self, request):
        r"""获取评估器信息

        该接口用于通过指定的评估器ID检索其完整定义信息，包括判分逻辑、参数配置、关联模型及元数据详情，是核对特定评测标准执行细节的核心入口。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowOpsEvaluator
        :type request: :class:`huaweicloudsdkagentarts.v1.ShowOpsEvaluatorRequest`
        :rtype: :class:`huaweicloudsdkagentarts.v1.ShowOpsEvaluatorResponse`
        """
        http_info = self._show_ops_evaluator_http_info(request)
        return self._call_api(**http_info)

    def show_ops_evaluator_async_invoker(self, request):
        http_info = self._show_ops_evaluator_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_ops_evaluator_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/ops/evaluators/{evaluator_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowOpsEvaluatorResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'evaluator_id' in local_var_params:
            path_params['evaluator_id'] = local_var_params['evaluator_id']

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

    def show_ops_evaluator_version_async(self, request):
        r"""获取评估器单个版本信息

        该接口用于通过评估器ID与版本ID获取特定版本的详细快照信息，包括该版本固化的判分逻辑、Prompt 模板、参数权重及生效配置。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowOpsEvaluatorVersion
        :type request: :class:`huaweicloudsdkagentarts.v1.ShowOpsEvaluatorVersionRequest`
        :rtype: :class:`huaweicloudsdkagentarts.v1.ShowOpsEvaluatorVersionResponse`
        """
        http_info = self._show_ops_evaluator_version_http_info(request)
        return self._call_api(**http_info)

    def show_ops_evaluator_version_async_invoker(self, request):
        http_info = self._show_ops_evaluator_version_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_ops_evaluator_version_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/ops/evaluators/{evaluator_id}/versions/{version_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowOpsEvaluatorVersionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'evaluator_id' in local_var_params:
            path_params['evaluator_id'] = local_var_params['evaluator_id']
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

    def update_ops_evaluator_tags_async(self, request):
        r"""更新评估器标签

        该接口用于全量更新指定评估器的标签信息，通过重新定义评估器的分类维度，实现对评测资产的精准分类、快速检索及生命周期归类。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateOpsEvaluatorTags
        :type request: :class:`huaweicloudsdkagentarts.v1.UpdateOpsEvaluatorTagsRequest`
        :rtype: :class:`huaweicloudsdkagentarts.v1.UpdateOpsEvaluatorTagsResponse`
        """
        http_info = self._update_ops_evaluator_tags_http_info(request)
        return self._call_api(**http_info)

    def update_ops_evaluator_tags_async_invoker(self, request):
        http_info = self._update_ops_evaluator_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_ops_evaluator_tags_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/ops/evaluators/{evaluator_id}/tags",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateOpsEvaluatorTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'evaluator_id' in local_var_params:
            path_params['evaluator_id'] = local_var_params['evaluator_id']

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

    def list_ops_evaluator_templates_async(self, request):
        r"""获取评估器模板列表

        该接口用于获取系统中的所有评估器模板信息列表，支持分页查询和条件筛选，适用于需要查看和管理评估器模板的场景。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListOpsEvaluatorTemplates
        :type request: :class:`huaweicloudsdkagentarts.v1.ListOpsEvaluatorTemplatesRequest`
        :rtype: :class:`huaweicloudsdkagentarts.v1.ListOpsEvaluatorTemplatesResponse`
        """
        http_info = self._list_ops_evaluator_templates_http_info(request)
        return self._call_api(**http_info)

    def list_ops_evaluator_templates_async_invoker(self, request):
        http_info = self._list_ops_evaluator_templates_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_ops_evaluator_templates_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/ops/evaluator-templates/list",
            "request_type": request.__class__.__name__,
            "response_type": "ListOpsEvaluatorTemplatesResponse"
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

    def show_ops_evaluator_template_async(self, request):
        r"""获取评估器模板

        该接口用于根据模板ID获取特定评估器模板的详细信息，支持查询模板的完整配置和使用说明，适用于需要深入了解特定模板配置的场景。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowOpsEvaluatorTemplate
        :type request: :class:`huaweicloudsdkagentarts.v1.ShowOpsEvaluatorTemplateRequest`
        :rtype: :class:`huaweicloudsdkagentarts.v1.ShowOpsEvaluatorTemplateResponse`
        """
        http_info = self._show_ops_evaluator_template_http_info(request)
        return self._call_api(**http_info)

    def show_ops_evaluator_template_async_invoker(self, request):
        http_info = self._show_ops_evaluator_template_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_ops_evaluator_template_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/ops/evaluator-templates/{template_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowOpsEvaluatorTemplateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'template_id' in local_var_params:
            path_params['template_id'] = local_var_params['template_id']

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

    def create_ops_label_async(self, request):
        r"""创建标签

        该接口用于创建新标签，支持文本标签和布尔类型的自定义标签，适用于资源分类、数据标注和标签管理的场景。
        适用场景：
        - 在评估任务管理中，创建新的标签以便对任务进行分类标记（如按业务线、优先级分类）。
        - 根据业务发展需要，扩展现有的标签系统，增加新的数据分类维度，支持更细粒度的数据管理。
        - 建立标准化的标签体系，将分散的资源通过标签进行关联和统一管理，提升使用效率。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateOpsLabel
        :type request: :class:`huaweicloudsdkagentarts.v1.CreateOpsLabelRequest`
        :rtype: :class:`huaweicloudsdkagentarts.v1.CreateOpsLabelResponse`
        """
        http_info = self._create_ops_label_http_info(request)
        return self._call_api(**http_info)

    def create_ops_label_async_invoker(self, request):
        http_info = self._create_ops_label_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_ops_label_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/ops/labels",
            "request_type": request.__class__.__name__,
            "response_type": "CreateOpsLabelResponse"
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

    def list_ops_labels_async(self, request):
        r"""获取标签列表

        该接口用于获取系统中所有标签的信息列表，支持分页查询和类型筛选，适用于标签管理和选择查询的场景。
        适用场景：
        - 查看系统中可用的所有标签资源。
        - 在评估任务中选择合适的标签进行分类。
        - 看标签的详细信息，维护标签体系的完整性。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListOpsLabels
        :type request: :class:`huaweicloudsdkagentarts.v1.ListOpsLabelsRequest`
        :rtype: :class:`huaweicloudsdkagentarts.v1.ListOpsLabelsResponse`
        """
        http_info = self._list_ops_labels_http_info(request)
        return self._call_api(**http_info)

    def list_ops_labels_async_invoker(self, request):
        http_info = self._list_ops_labels_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_ops_labels_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/ops/labels",
            "request_type": request.__class__.__name__,
            "response_type": "ListOpsLabelsResponse"
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

    def show_ops_label_async(self, request):
        r"""获取标签详情

        该接口用于获取标签的详细信息，包括标签名称、类型、描述和关联的标注项，适用于标签详情查看和标签管理的场景。
        适用场景：
        - 查看标签的完整配置信息和关联内容。
        - 审核和验证标签的使用范围和限制。
        - 标签系统维护和数据质量检查。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowOpsLabel
        :type request: :class:`huaweicloudsdkagentarts.v1.ShowOpsLabelRequest`
        :rtype: :class:`huaweicloudsdkagentarts.v1.ShowOpsLabelResponse`
        """
        http_info = self._show_ops_label_http_info(request)
        return self._call_api(**http_info)

    def show_ops_label_async_invoker(self, request):
        http_info = self._show_ops_label_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_ops_label_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/ops/labels/{label_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowOpsLabelResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'label_id' in local_var_params:
            path_params['label_id'] = local_var_params['label_id']

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

    def update_ops_label_async(self, request):
        r"""更新标签

        该接口用于更新标签信息，支持修改标签名称、描述和标注项，适用于标签内容维护和完善的场景。
        适用场景：
        - 更新标签的描述信息以反映最新使用场景。
        - 添加或修改标签的支持选项和枚举值。
        - 修正标签配置以适应业务需求变化。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateOpsLabel
        :type request: :class:`huaweicloudsdkagentarts.v1.UpdateOpsLabelRequest`
        :rtype: :class:`huaweicloudsdkagentarts.v1.UpdateOpsLabelResponse`
        """
        http_info = self._update_ops_label_http_info(request)
        return self._call_api(**http_info)

    def update_ops_label_async_invoker(self, request):
        http_info = self._update_ops_label_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_ops_label_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/ops/labels/{label_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateOpsLabelResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'label_id' in local_var_params:
            path_params['label_id'] = local_var_params['label_id']

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

    def show_ops_quota_async(self, request):
        r"""获取当前项目的配额

        该接口用于获取当前项目的配额信息，支持查询各类任务的数量上限和剩余配额，适用于资源管理和容量规划的场景。
        适用场景：
        - 任务创建前查询当前项目的资源限制和剩余容量，避免因配额不足导致任务创建失败。
        - 查看各类任务的已用配额和总量，掌握项目的资源消耗状况。
        - 当配额接近上限时，通过查询结果进行容量规划和预警。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowOpsQuota
        :type request: :class:`huaweicloudsdkagentarts.v1.ShowOpsQuotaRequest`
        :rtype: :class:`huaweicloudsdkagentarts.v1.ShowOpsQuotaResponse`
        """
        http_info = self._show_ops_quota_http_info(request)
        return self._call_api(**http_info)

    def show_ops_quota_async_invoker(self, request):
        http_info = self._show_ops_quota_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_ops_quota_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/ops/quotas",
            "request_type": request.__class__.__name__,
            "response_type": "ShowOpsQuotaResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'task_type' in local_var_params:
            query_params.append(('task_type', local_var_params['task_type']))

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

    def batch_add_ops_evaluation_task_custom_label_values_async(self, request):
        r"""批量添加评估任务的自定义标签值

        该接口用于批量添加评估任务的自定义标签值，支持为多个数据项设置标签值，适用于数据标注和分类管理的场景。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchAddOpsEvaluationTaskCustomLabelValues
        :type request: :class:`huaweicloudsdkagentarts.v1.BatchAddOpsEvaluationTaskCustomLabelValuesRequest`
        :rtype: :class:`huaweicloudsdkagentarts.v1.BatchAddOpsEvaluationTaskCustomLabelValuesResponse`
        """
        http_info = self._batch_add_ops_evaluation_task_custom_label_values_http_info(request)
        return self._call_api(**http_info)

    def batch_add_ops_evaluation_task_custom_label_values_async_invoker(self, request):
        http_info = self._batch_add_ops_evaluation_task_custom_label_values_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_add_ops_evaluation_task_custom_label_values_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/ops/evaluation-tasks/{task_id}/custom-labels-values",
            "request_type": request.__class__.__name__,
            "response_type": "BatchAddOpsEvaluationTaskCustomLabelValuesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

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

    def batch_add_ops_evaluation_task_custom_labels_async(self, request):
        r"""添加评估任务自定义标签

        该接口用于为评估任务添加自定义标签，支持批量添加多个标签类型，适用于任务分类管理和数据标记的场景。
        适用场景：
        - 为评估任务添加新的分类标记和特征标签。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchAddOpsEvaluationTaskCustomLabels
        :type request: :class:`huaweicloudsdkagentarts.v1.BatchAddOpsEvaluationTaskCustomLabelsRequest`
        :rtype: :class:`huaweicloudsdkagentarts.v1.BatchAddOpsEvaluationTaskCustomLabelsResponse`
        """
        http_info = self._batch_add_ops_evaluation_task_custom_labels_http_info(request)
        return self._call_api(**http_info)

    def batch_add_ops_evaluation_task_custom_labels_async_invoker(self, request):
        http_info = self._batch_add_ops_evaluation_task_custom_labels_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_add_ops_evaluation_task_custom_labels_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/ops/evaluation-tasks/{task_id}/custom-labels",
            "request_type": request.__class__.__name__,
            "response_type": "BatchAddOpsEvaluationTaskCustomLabelsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

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

    def batch_delete_ops_evaluation_tasks_async(self, request):
        r"""批量删除任务

        该接口用于批量删除指定的评估任务，支持一次性删除多个任务，批量返回删除结果，适用于任务清理的场景。
        适用场景：
        - 清理不再需要的历史评估任务。
        - 批量删除测试或错误创建的任务。
        - 管理项目中的任务列表以保持系统整洁。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchDeleteOpsEvaluationTasks
        :type request: :class:`huaweicloudsdkagentarts.v1.BatchDeleteOpsEvaluationTasksRequest`
        :rtype: :class:`huaweicloudsdkagentarts.v1.BatchDeleteOpsEvaluationTasksResponse`
        """
        http_info = self._batch_delete_ops_evaluation_tasks_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_ops_evaluation_tasks_async_invoker(self, request):
        http_info = self._batch_delete_ops_evaluation_tasks_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_delete_ops_evaluation_tasks_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/ops/evaluation-tasks",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeleteOpsEvaluationTasksResponse"
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

    def batch_update_ops_evaluation_task_custom_label_values_async(self, request):
        r"""更新评估任务的自定义标签值

        该接口用于批量更新评估任务的自定义标签值，支持修改现有标签值的标注内容。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchUpdateOpsEvaluationTaskCustomLabelValues
        :type request: :class:`huaweicloudsdkagentarts.v1.BatchUpdateOpsEvaluationTaskCustomLabelValuesRequest`
        :rtype: :class:`huaweicloudsdkagentarts.v1.BatchUpdateOpsEvaluationTaskCustomLabelValuesResponse`
        """
        http_info = self._batch_update_ops_evaluation_task_custom_label_values_http_info(request)
        return self._call_api(**http_info)

    def batch_update_ops_evaluation_task_custom_label_values_async_invoker(self, request):
        http_info = self._batch_update_ops_evaluation_task_custom_label_values_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_update_ops_evaluation_task_custom_label_values_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/ops/evaluation-tasks/{task_id}/custom-labels-values",
            "request_type": request.__class__.__name__,
            "response_type": "BatchUpdateOpsEvaluationTaskCustomLabelValuesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

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

    def check_ops_evaluation_task_name_async(self, request):
        r"""检查新建评估任务名称是否存在

        该接口用于检查指定的评估任务名称是否已存在，返回名称唯一性验证结果，适用于创建新任务前验证任务名称可用性的场景。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CheckOpsEvaluationTaskName
        :type request: :class:`huaweicloudsdkagentarts.v1.CheckOpsEvaluationTaskNameRequest`
        :rtype: :class:`huaweicloudsdkagentarts.v1.CheckOpsEvaluationTaskNameResponse`
        """
        http_info = self._check_ops_evaluation_task_name_http_info(request)
        return self._call_api(**http_info)

    def check_ops_evaluation_task_name_async_invoker(self, request):
        http_info = self._check_ops_evaluation_task_name_http_info(request)
        return AsyncInvoker(self, http_info)

    def _check_ops_evaluation_task_name_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/ops/evaluation-tasks/name/check",
            "request_type": request.__class__.__name__,
            "response_type": "CheckOpsEvaluationTaskNameResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'task_name' in local_var_params:
            query_params.append(('task_name', local_var_params['task_name']))

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

    def create_ops_evaluation_task_async(self, request):
        r"""创建评估任务

        该接口用于创建新的评估任务，支持离线和在线评估模式，灵活配置评估参数和数据源，适用于各类模型评估和数据质量验证的场景。
        适用场景：
        - 启动新的离线评估任务进行模型质量测试。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateOpsEvaluationTask
        :type request: :class:`huaweicloudsdkagentarts.v1.CreateOpsEvaluationTaskRequest`
        :rtype: :class:`huaweicloudsdkagentarts.v1.CreateOpsEvaluationTaskResponse`
        """
        http_info = self._create_ops_evaluation_task_http_info(request)
        return self._call_api(**http_info)

    def create_ops_evaluation_task_async_invoker(self, request):
        http_info = self._create_ops_evaluation_task_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_ops_evaluation_task_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/ops/evaluation-tasks",
            "request_type": request.__class__.__name__,
            "response_type": "CreateOpsEvaluationTaskResponse"
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

    def delete_ops_evaluation_task_custom_label_values_async(self, request):
        r"""删除评估任务自定义标签值

        该接口用于删除评估任务的自定义标签值，支持批量移除指定标签项。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteOpsEvaluationTaskCustomLabelValues
        :type request: :class:`huaweicloudsdkagentarts.v1.DeleteOpsEvaluationTaskCustomLabelValuesRequest`
        :rtype: :class:`huaweicloudsdkagentarts.v1.DeleteOpsEvaluationTaskCustomLabelValuesResponse`
        """
        http_info = self._delete_ops_evaluation_task_custom_label_values_http_info(request)
        return self._call_api(**http_info)

    def delete_ops_evaluation_task_custom_label_values_async_invoker(self, request):
        http_info = self._delete_ops_evaluation_task_custom_label_values_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_ops_evaluation_task_custom_label_values_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/ops/evaluation-tasks/{task_id}/custom-labels-values",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteOpsEvaluationTaskCustomLabelValuesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

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

    def delete_ops_evaluation_task_custom_labels_async(self, request):
        r"""删除评估任务自定义标签

        该接口用于删除评估任务的指定自定义标签，支持移除不需要的标签项，适用于标签管理和数据清理的场景。
        适用场景：
        - 清理评估任务中不再使用的标签项。
        - 调整评估数据的分类和标记。
        - 优化标签结构以提高数据管理效率。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteOpsEvaluationTaskCustomLabels
        :type request: :class:`huaweicloudsdkagentarts.v1.DeleteOpsEvaluationTaskCustomLabelsRequest`
        :rtype: :class:`huaweicloudsdkagentarts.v1.DeleteOpsEvaluationTaskCustomLabelsResponse`
        """
        http_info = self._delete_ops_evaluation_task_custom_labels_http_info(request)
        return self._call_api(**http_info)

    def delete_ops_evaluation_task_custom_labels_async_invoker(self, request):
        http_info = self._delete_ops_evaluation_task_custom_labels_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_ops_evaluation_task_custom_labels_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/ops/evaluation-tasks/{task_id}/custom-labels/{label_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteOpsEvaluationTaskCustomLabelsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']
        if 'label_id' in local_var_params:
            path_params['label_id'] = local_var_params['label_id']

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

    def list_ops_evaluation_task_custom_label_values_async(self, request):
        r"""查询评估任务的自定义标签值

        该接口用于查询评估任务的自定义标签值，支持按标签ID和项目ID进行过滤查询，适用于标签数据查询和分析的场景。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListOpsEvaluationTaskCustomLabelValues
        :type request: :class:`huaweicloudsdkagentarts.v1.ListOpsEvaluationTaskCustomLabelValuesRequest`
        :rtype: :class:`huaweicloudsdkagentarts.v1.ListOpsEvaluationTaskCustomLabelValuesResponse`
        """
        http_info = self._list_ops_evaluation_task_custom_label_values_http_info(request)
        return self._call_api(**http_info)

    def list_ops_evaluation_task_custom_label_values_async_invoker(self, request):
        http_info = self._list_ops_evaluation_task_custom_label_values_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_ops_evaluation_task_custom_label_values_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/ops/evaluation-tasks/{task_id}/custom-labels-values",
            "request_type": request.__class__.__name__,
            "response_type": "ListOpsEvaluationTaskCustomLabelValuesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

        query_params = []
        if 'tag_id' in local_var_params:
            query_params.append(('tag_id', local_var_params['tag_id']))
        if 'item_id' in local_var_params:
            query_params.append(('item_id', local_var_params['item_id']))
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

    def list_ops_evaluation_task_custom_labels_async(self, request):
        r"""查询评估任务的自定义标签列表

        该接口用于查询评估任务的所有自定义标签，返回标签ID、类型、创建时间等详细信息，支持分页查询和筛选，适用于标签管理和查询的场景。
        适用场景：
        - 查看评估任务使用的所有分类标记。
        - 分析自定义标签的使用情况和分布特征。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListOpsEvaluationTaskCustomLabels
        :type request: :class:`huaweicloudsdkagentarts.v1.ListOpsEvaluationTaskCustomLabelsRequest`
        :rtype: :class:`huaweicloudsdkagentarts.v1.ListOpsEvaluationTaskCustomLabelsResponse`
        """
        http_info = self._list_ops_evaluation_task_custom_labels_http_info(request)
        return self._call_api(**http_info)

    def list_ops_evaluation_task_custom_labels_async_invoker(self, request):
        http_info = self._list_ops_evaluation_task_custom_labels_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_ops_evaluation_task_custom_labels_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/ops/evaluation-tasks/{task_id}/custom-labels",
            "request_type": request.__class__.__name__,
            "response_type": "ListOpsEvaluationTaskCustomLabelsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

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

    def list_ops_evaluation_task_results_async(self, request):
        r"""查看任务评估结果

        该接口用于获取评估任务的详细评估结果，包括各项评估指标的分数、用时和详细信息，适用于任务结果分析和质量评估的场景。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListOpsEvaluationTaskResults
        :type request: :class:`huaweicloudsdkagentarts.v1.ListOpsEvaluationTaskResultsRequest`
        :rtype: :class:`huaweicloudsdkagentarts.v1.ListOpsEvaluationTaskResultsResponse`
        """
        http_info = self._list_ops_evaluation_task_results_http_info(request)
        return self._call_api(**http_info)

    def list_ops_evaluation_task_results_async_invoker(self, request):
        http_info = self._list_ops_evaluation_task_results_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_ops_evaluation_task_results_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/ops/evaluation-tasks/{task_id}/results",
            "request_type": request.__class__.__name__,
            "response_type": "ListOpsEvaluationTaskResultsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

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

    def list_ops_evaluation_tasks_async(self, request):
        r"""查看评估任务列表

        该接口用于获取评估任务列表信息，支持条件筛选和分页查询，返回任务的基本信息和执行状态，适用于任务管理和监控的场景。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListOpsEvaluationTasks
        :type request: :class:`huaweicloudsdkagentarts.v1.ListOpsEvaluationTasksRequest`
        :rtype: :class:`huaweicloudsdkagentarts.v1.ListOpsEvaluationTasksResponse`
        """
        http_info = self._list_ops_evaluation_tasks_http_info(request)
        return self._call_api(**http_info)

    def list_ops_evaluation_tasks_async_invoker(self, request):
        http_info = self._list_ops_evaluation_tasks_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_ops_evaluation_tasks_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/ops/evaluation-tasks/list",
            "request_type": request.__class__.__name__,
            "response_type": "ListOpsEvaluationTasksResponse"
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

    def show_ops_evaluation_task_async(self, request):
        r"""查看评估任务详情

        该接口用于获取评估任务的详细信息，包括任务配置、状态、统计结果等完整信息，适用于任务详情查看的场景。
        适用场景：
        - 查看评估任务的完整配置和执行状态。
        - 分析任务运行过程中的性能和结果统计信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowOpsEvaluationTask
        :type request: :class:`huaweicloudsdkagentarts.v1.ShowOpsEvaluationTaskRequest`
        :rtype: :class:`huaweicloudsdkagentarts.v1.ShowOpsEvaluationTaskResponse`
        """
        http_info = self._show_ops_evaluation_task_http_info(request)
        return self._call_api(**http_info)

    def show_ops_evaluation_task_async_invoker(self, request):
        http_info = self._show_ops_evaluation_task_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_ops_evaluation_task_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/ops/evaluation-tasks/{task_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowOpsEvaluationTaskResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

        query_params = []
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

    def show_ops_evaluation_task_charts_labels_distribution_async(self, request):
        r"""统计一个任务的所有自定义标签的标签项分布

        该接口用于统计评估任务中自定义标签的分布情况，支持文本标签和布尔标签的分类统计，适用于数据特征分析和标签管理的场景。
                适用场景：
                - 分析评估数据中标签的分布特征和规律。
                - 自定义标签的使用频率和覆盖范围。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowOpsEvaluationTaskChartsLabelsDistribution
        :type request: :class:`huaweicloudsdkagentarts.v1.ShowOpsEvaluationTaskChartsLabelsDistributionRequest`
        :rtype: :class:`huaweicloudsdkagentarts.v1.ShowOpsEvaluationTaskChartsLabelsDistributionResponse`
        """
        http_info = self._show_ops_evaluation_task_charts_labels_distribution_http_info(request)
        return self._call_api(**http_info)

    def show_ops_evaluation_task_charts_labels_distribution_async_invoker(self, request):
        http_info = self._show_ops_evaluation_task_charts_labels_distribution_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_ops_evaluation_task_charts_labels_distribution_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/ops/evaluation-tasks/{task_id}/charts/tag-distribution",
            "request_type": request.__class__.__name__,
            "response_type": "ShowOpsEvaluationTaskChartsLabelsDistributionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

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

    def show_ops_evaluation_task_charts_score_distribution_async(self, request):
        r"""统计每个任务的评估器得分分布

        该接口用于获取评估任务中各评估器的得分分布情况，统计不同分数区间的样本数量，适用于评估结果可视化分析的场景。
                适用场景：
                - 查看评估得分的分布特征和集中趋势。
                - 识别评估结果中高分和低分样本的比例。
                - 分析评估模型的评分一致性和区分度。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowOpsEvaluationTaskChartsScoreDistribution
        :type request: :class:`huaweicloudsdkagentarts.v1.ShowOpsEvaluationTaskChartsScoreDistributionRequest`
        :rtype: :class:`huaweicloudsdkagentarts.v1.ShowOpsEvaluationTaskChartsScoreDistributionResponse`
        """
        http_info = self._show_ops_evaluation_task_charts_score_distribution_http_info(request)
        return self._call_api(**http_info)

    def show_ops_evaluation_task_charts_score_distribution_async_invoker(self, request):
        http_info = self._show_ops_evaluation_task_charts_score_distribution_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_ops_evaluation_task_charts_score_distribution_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/ops/evaluation-tasks/{task_id}/charts/score-distribution",
            "request_type": request.__class__.__name__,
            "response_type": "ShowOpsEvaluationTaskChartsScoreDistributionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

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

    def show_ops_evaluation_task_charts_score_stats_async(self, request):
        r"""某个任务的所有评估器得分统计

        该接口用于获取指定评测任务中各评估维度的得分分布与汇总统计，通过聚合多个评估器的分值数据，生成反映模型各方面能力指标视图。
        适用场景：
        - 模型能力多维诊断：对比同一任务下不同评估器（如：逻辑性得分 vs 准确性得分）的统计表现，精准识别模型的优势与短板。
        - 评测结果横向对比：汇总多个评估因子的平均分、标准差等指标，为模型版本的择优准入提供数据支撑。
        - 质量分布趋势分析：通过得分统计识别评分异常区间（如：评分分布过于集中或离散），评估当前评测集难度与评估器判分逻辑的合理性。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowOpsEvaluationTaskChartsScoreStats
        :type request: :class:`huaweicloudsdkagentarts.v1.ShowOpsEvaluationTaskChartsScoreStatsRequest`
        :rtype: :class:`huaweicloudsdkagentarts.v1.ShowOpsEvaluationTaskChartsScoreStatsResponse`
        """
        http_info = self._show_ops_evaluation_task_charts_score_stats_http_info(request)
        return self._call_api(**http_info)

    def show_ops_evaluation_task_charts_score_stats_async_invoker(self, request):
        http_info = self._show_ops_evaluation_task_charts_score_stats_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_ops_evaluation_task_charts_score_stats_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/ops/evaluation-tasks/{task_id}/charts/score-stats",
            "request_type": request.__class__.__name__,
            "response_type": "ShowOpsEvaluationTaskChartsScoreStatsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

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

    def show_ops_evaluation_task_charts_status_async(self, request):
        r"""获取任务的成功数和失败数

        该接口用于获取指定评测任务的执行状态分布统计，返回任务中各数据条目的成功与失败数量。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowOpsEvaluationTaskChartsStatus
        :type request: :class:`huaweicloudsdkagentarts.v1.ShowOpsEvaluationTaskChartsStatusRequest`
        :rtype: :class:`huaweicloudsdkagentarts.v1.ShowOpsEvaluationTaskChartsStatusResponse`
        """
        http_info = self._show_ops_evaluation_task_charts_status_http_info(request)
        return self._call_api(**http_info)

    def show_ops_evaluation_task_charts_status_async_invoker(self, request):
        http_info = self._show_ops_evaluation_task_charts_status_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_ops_evaluation_task_charts_status_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/ops/evaluation-tasks/{task_id}/charts/status",
            "request_type": request.__class__.__name__,
            "response_type": "ShowOpsEvaluationTaskChartsStatusResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

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

    def show_ops_evaluation_tasks_charts_compare_result_async(self, request):
        r"""获取评估任务统计结果

        该接口用于统计不同评估任务的对比结果报告，包含评估器得分情况、得分概览、任务消耗总token统计，适用于数据特征分析和评估任务管理的场景。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowOpsEvaluationTasksChartsCompareResult
        :type request: :class:`huaweicloudsdkagentarts.v1.ShowOpsEvaluationTasksChartsCompareResultRequest`
        :rtype: :class:`huaweicloudsdkagentarts.v1.ShowOpsEvaluationTasksChartsCompareResultResponse`
        """
        http_info = self._show_ops_evaluation_tasks_charts_compare_result_http_info(request)
        return self._call_api(**http_info)

    def show_ops_evaluation_tasks_charts_compare_result_async_invoker(self, request):
        http_info = self._show_ops_evaluation_tasks_charts_compare_result_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_ops_evaluation_tasks_charts_compare_result_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/ops/evaluation-tasks/{task_id}/statistic-comparisons",
            "request_type": request.__class__.__name__,
            "response_type": "ShowOpsEvaluationTasksChartsCompareResultResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

        query_params = []
        if 'task_ids' in local_var_params:
            query_params.append(('task_ids', local_var_params['task_ids']))

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

    def show_ops_evaluation_tasks_compare_result_async(self, request):
        r"""获取评估任务对比结果

        该接口用于统计不同评估任务的对比结果，包含每个任务在每个评估器的得分情况、每个评估器得分、任务状态、任务耗时、任务消耗总token，适用于数据特征分析和评估任务管理的场景。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowOpsEvaluationTasksCompareResult
        :type request: :class:`huaweicloudsdkagentarts.v1.ShowOpsEvaluationTasksCompareResultRequest`
        :rtype: :class:`huaweicloudsdkagentarts.v1.ShowOpsEvaluationTasksCompareResultResponse`
        """
        http_info = self._show_ops_evaluation_tasks_compare_result_http_info(request)
        return self._call_api(**http_info)

    def show_ops_evaluation_tasks_compare_result_async_invoker(self, request):
        http_info = self._show_ops_evaluation_tasks_compare_result_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_ops_evaluation_tasks_compare_result_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/ops/evaluation-tasks/{task_id}/result-comparisons",
            "request_type": request.__class__.__name__,
            "response_type": "ShowOpsEvaluationTasksCompareResultResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

        query_params = []
        if 'task_ids' in local_var_params:
            query_params.append(('task_ids', local_var_params['task_ids']))
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

    def stop_ops_evaluation_task_async(self, request):
        r"""暂停评估任务

        该接口用于暂停正在运行的评估任务，支持临时任务执行控制，适用于任务调度的场景。
        适用场景：
        - 暂停长时间运行的评估任务以释放资源。
        - 在发现问题时临时停止任务执行。
        - 调整任务执行优先级和时间安排。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for StopOpsEvaluationTask
        :type request: :class:`huaweicloudsdkagentarts.v1.StopOpsEvaluationTaskRequest`
        :rtype: :class:`huaweicloudsdkagentarts.v1.StopOpsEvaluationTaskResponse`
        """
        http_info = self._stop_ops_evaluation_task_http_info(request)
        return self._call_api(**http_info)

    def stop_ops_evaluation_task_async_invoker(self, request):
        http_info = self._stop_ops_evaluation_task_http_info(request)
        return AsyncInvoker(self, http_info)

    def _stop_ops_evaluation_task_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/ops/evaluation-tasks/{task_id}",
            "request_type": request.__class__.__name__,
            "response_type": "StopOpsEvaluationTaskResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

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

    def update_ops_evaluation_task_result_async(self, request):
        r"""校正评估结果

        该接口用于对已生成的自动化评估结果执行人工校正，允许通过更新得分与修正理由来覆盖评价，确保最终评测结论的客观性与权威性。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateOpsEvaluationTaskResult
        :type request: :class:`huaweicloudsdkagentarts.v1.UpdateOpsEvaluationTaskResultRequest`
        :rtype: :class:`huaweicloudsdkagentarts.v1.UpdateOpsEvaluationTaskResultResponse`
        """
        http_info = self._update_ops_evaluation_task_result_http_info(request)
        return self._call_api(**http_info)

    def update_ops_evaluation_task_result_async_invoker(self, request):
        http_info = self._update_ops_evaluation_task_result_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_ops_evaluation_task_result_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/ops/evaluation-tasks/{task_id}/results/correction",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateOpsEvaluationTaskResultResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

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

    def update_ops_evaluation_task_tags_async(self, request):
        r"""更新评估任务标签

        该接口用于更新评估任务的标签信息，支持设置或修改任务的键值对标签。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateOpsEvaluationTaskTags
        :type request: :class:`huaweicloudsdkagentarts.v1.UpdateOpsEvaluationTaskTagsRequest`
        :rtype: :class:`huaweicloudsdkagentarts.v1.UpdateOpsEvaluationTaskTagsResponse`
        """
        http_info = self._update_ops_evaluation_task_tags_http_info(request)
        return self._call_api(**http_info)

    def update_ops_evaluation_task_tags_async_invoker(self, request):
        http_info = self._update_ops_evaluation_task_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_ops_evaluation_task_tags_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/ops/evaluation-tasks/{task_id}/tags",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateOpsEvaluationTaskTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

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

    def create_ops_agent_observation_async(self, request):
        r"""同步agent信息

        同步agent信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateOpsAgentObservation
        :type request: :class:`huaweicloudsdkagentarts.v1.CreateOpsAgentObservationRequest`
        :rtype: :class:`huaweicloudsdkagentarts.v1.CreateOpsAgentObservationResponse`
        """
        http_info = self._create_ops_agent_observation_http_info(request)
        return self._call_api(**http_info)

    def create_ops_agent_observation_async_invoker(self, request):
        http_info = self._create_ops_agent_observation_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_ops_agent_observation_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/ops/observation/agents",
            "request_type": request.__class__.__name__,
            "response_type": "CreateOpsAgentObservationResponse"
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
            ['application/json;charset=utf-8'])

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

    def delete_ops_agent_observation_async(self, request):
        r"""删除agent可观测信息

        删除agent可观测信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteOpsAgentObservation
        :type request: :class:`huaweicloudsdkagentarts.v1.DeleteOpsAgentObservationRequest`
        :rtype: :class:`huaweicloudsdkagentarts.v1.DeleteOpsAgentObservationResponse`
        """
        http_info = self._delete_ops_agent_observation_http_info(request)
        return self._call_api(**http_info)

    def delete_ops_agent_observation_async_invoker(self, request):
        http_info = self._delete_ops_agent_observation_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_ops_agent_observation_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/ops/observation/agents/{agent_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteOpsAgentObservationResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'agent_id' in local_var_params:
            path_params['agent_id'] = local_var_params['agent_id']

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

    def list_ops_agent_observation_async(self, request):
        r"""查询智能体可观测信息列表接口

        查询应用列表接口
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListOpsAgentObservation
        :type request: :class:`huaweicloudsdkagentarts.v1.ListOpsAgentObservationRequest`
        :rtype: :class:`huaweicloudsdkagentarts.v1.ListOpsAgentObservationResponse`
        """
        http_info = self._list_ops_agent_observation_http_info(request)
        return self._call_api(**http_info)

    def list_ops_agent_observation_async_invoker(self, request):
        http_info = self._list_ops_agent_observation_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_ops_agent_observation_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/ops/observation/agents",
            "request_type": request.__class__.__name__,
            "response_type": "ListOpsAgentObservationResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'agent_id' in local_var_params:
            query_params.append(('agent_id', local_var_params['agent_id']))
        if 'page' in local_var_params:
            query_params.append(('page', local_var_params['page']))
        if 'page_size' in local_var_params:
            query_params.append(('page_size', local_var_params['page_size']))
        if 'agent_name' in local_var_params:
            query_params.append(('agent_name', local_var_params['agent_name']))
        if 'agent_type' in local_var_params:
            query_params.append(('agent_type', local_var_params['agent_type']))

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

    def update_ops_agent_observation_async(self, request):
        r"""更新agent可观测信息

        更新agent可观测信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateOpsAgentObservation
        :type request: :class:`huaweicloudsdkagentarts.v1.UpdateOpsAgentObservationRequest`
        :rtype: :class:`huaweicloudsdkagentarts.v1.UpdateOpsAgentObservationResponse`
        """
        http_info = self._update_ops_agent_observation_http_info(request)
        return self._call_api(**http_info)

    def update_ops_agent_observation_async_invoker(self, request):
        http_info = self._update_ops_agent_observation_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_ops_agent_observation_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/ops/observation/agents/{agent_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateOpsAgentObservationResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'agent_id' in local_var_params:
            path_params['agent_id'] = local_var_params['agent_id']

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
            ['application/json;charset=utf-8'])

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

    def list_ops_agent_log_async(self, request):
        r"""根据条件查询日志

        根据条件查询日志
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListOpsAgentLog
        :type request: :class:`huaweicloudsdkagentarts.v1.ListOpsAgentLogRequest`
        :rtype: :class:`huaweicloudsdkagentarts.v1.ListOpsAgentLogResponse`
        """
        http_info = self._list_ops_agent_log_http_info(request)
        return self._call_api(**http_info)

    def list_ops_agent_log_async_invoker(self, request):
        http_info = self._list_ops_agent_log_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_ops_agent_log_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/ops/observation/agent/{agent_id}/log",
            "request_type": request.__class__.__name__,
            "response_type": "ListOpsAgentLogResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'agent_id' in local_var_params:
            path_params['agent_id'] = local_var_params['agent_id']

        query_params = []
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'trace_id' in local_var_params:
            query_params.append(('trace_id', local_var_params['trace_id']))
        if 'span_id' in local_var_params:
            query_params.append(('span_id', local_var_params['span_id']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'scroll_id' in local_var_params:
            query_params.append(('scroll_id', local_var_params['scroll_id']))
        if 'keyword' in local_var_params:
            query_params.append(('keyword', local_var_params['keyword']))

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

    def list_ops_agent_runt_log_async(self, request):
        r"""查询agentRun的日志

        查询agentRun的日志
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListOpsAgentRuntLog
        :type request: :class:`huaweicloudsdkagentarts.v1.ListOpsAgentRuntLogRequest`
        :rtype: :class:`huaweicloudsdkagentarts.v1.ListOpsAgentRuntLogResponse`
        """
        http_info = self._list_ops_agent_runt_log_http_info(request)
        return self._call_api(**http_info)

    def list_ops_agent_runt_log_async_invoker(self, request):
        http_info = self._list_ops_agent_runt_log_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_ops_agent_runt_log_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/ops/observation/agent-run/{agent_run_id}/log",
            "request_type": request.__class__.__name__,
            "response_type": "ListOpsAgentRuntLogResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'agent_run_id' in local_var_params:
            path_params['agent_run_id'] = local_var_params['agent_run_id']

        query_params = []
        if 'log_type' in local_var_params:
            query_params.append(('log_type', local_var_params['log_type']))
        if 'resource_type' in local_var_params:
            query_params.append(('resource_type', local_var_params['resource_type']))
        if 'user_id' in local_var_params:
            query_params.append(('user_id', local_var_params['user_id']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'scroll_id' in local_var_params:
            query_params.append(('scroll_id', local_var_params['scroll_id']))
        if 'keyword' in local_var_params:
            query_params.append(('keyword', local_var_params['keyword']))
        if 'line_num' in local_var_params:
            query_params.append(('line_num', local_var_params['line_num']))
        if 'is_desc' in local_var_params:
            query_params.append(('is_desc', local_var_params['is_desc']))

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

    def list_ops_agent_metric_label_values_async(self, request):
        r"""查询组件列表，包括工具，模型，skill列表

        查询组件列表，包括工具，模型，skill列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListOpsAgentMetricLabelValues
        :type request: :class:`huaweicloudsdkagentarts.v1.ListOpsAgentMetricLabelValuesRequest`
        :rtype: :class:`huaweicloudsdkagentarts.v1.ListOpsAgentMetricLabelValuesResponse`
        """
        http_info = self._list_ops_agent_metric_label_values_http_info(request)
        return self._call_api(**http_info)

    def list_ops_agent_metric_label_values_async_invoker(self, request):
        http_info = self._list_ops_agent_metric_label_values_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_ops_agent_metric_label_values_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/ops/observation/agents/metric/label-values",
            "request_type": request.__class__.__name__,
            "response_type": "ListOpsAgentMetricLabelValuesResponse"
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

    def list_ops_agent_span_metric_async(self, request):
        r"""查询调用链span指标

        查询调用链span指标
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListOpsAgentSpanMetric
        :type request: :class:`huaweicloudsdkagentarts.v1.ListOpsAgentSpanMetricRequest`
        :rtype: :class:`huaweicloudsdkagentarts.v1.ListOpsAgentSpanMetricResponse`
        """
        http_info = self._list_ops_agent_span_metric_http_info(request)
        return self._call_api(**http_info)

    def list_ops_agent_span_metric_async_invoker(self, request):
        http_info = self._list_ops_agent_span_metric_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_ops_agent_span_metric_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/ops/observation/agent/{agent_id}/span/{span_name}/metrics",
            "request_type": request.__class__.__name__,
            "response_type": "ListOpsAgentSpanMetricResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'agent_id' in local_var_params:
            path_params['agent_id'] = local_var_params['agent_id']
        if 'span_name' in local_var_params:
            path_params['span_name'] = local_var_params['span_name']

        query_params = []
        if 'span_time' in local_var_params:
            query_params.append(('span_time', local_var_params['span_time']))

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

    def show_ops_agent_metric_async(self, request):
        r"""查询时间范围内智能体的总数 草稿数 发布态数

        查询时间范围内智能体的总数 草稿数 发布态数
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowOpsAgentMetric
        :type request: :class:`huaweicloudsdkagentarts.v1.ShowOpsAgentMetricRequest`
        :rtype: :class:`huaweicloudsdkagentarts.v1.ShowOpsAgentMetricResponse`
        """
        http_info = self._show_ops_agent_metric_http_info(request)
        return self._call_api(**http_info)

    def show_ops_agent_metric_async_invoker(self, request):
        http_info = self._show_ops_agent_metric_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_ops_agent_metric_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/ops/observation/agents/metric",
            "request_type": request.__class__.__name__,
            "response_type": "ShowOpsAgentMetricResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))

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

    def show_ops_agent_metric_gauge_async(self, request):
        r"""查询单个指标的仪表盘接口

        查询单个指标的仪表盘接口
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowOpsAgentMetricGauge
        :type request: :class:`huaweicloudsdkagentarts.v1.ShowOpsAgentMetricGaugeRequest`
        :rtype: :class:`huaweicloudsdkagentarts.v1.ShowOpsAgentMetricGaugeResponse`
        """
        http_info = self._show_ops_agent_metric_gauge_http_info(request)
        return self._call_api(**http_info)

    def show_ops_agent_metric_gauge_async_invoker(self, request):
        http_info = self._show_ops_agent_metric_gauge_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_ops_agent_metric_gauge_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/ops/observation/agents/metric/gauge",
            "request_type": request.__class__.__name__,
            "response_type": "ShowOpsAgentMetricGaugeResponse"
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
            ['application/json;charset=utf-8'])

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

    def show_ops_agent_metric_top_n_async(self, request):
        r"""查询单个指标的topN接口

        查询单个指标的topN接口
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowOpsAgentMetricTopN
        :type request: :class:`huaweicloudsdkagentarts.v1.ShowOpsAgentMetricTopNRequest`
        :rtype: :class:`huaweicloudsdkagentarts.v1.ShowOpsAgentMetricTopNResponse`
        """
        http_info = self._show_ops_agent_metric_top_n_http_info(request)
        return self._call_api(**http_info)

    def show_ops_agent_metric_top_n_async_invoker(self, request):
        http_info = self._show_ops_agent_metric_top_n_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_ops_agent_metric_top_n_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/ops/observation/agents/metric/topn",
            "request_type": request.__class__.__name__,
            "response_type": "ShowOpsAgentMetricTopNResponse"
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
            ['application/json;charset=utf-8'])

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

    def show_ops_agent_metric_trend_async(self, request):
        r"""查询某个指标的趋势图接口

        查询某个指标的趋势图接口
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowOpsAgentMetricTrend
        :type request: :class:`huaweicloudsdkagentarts.v1.ShowOpsAgentMetricTrendRequest`
        :rtype: :class:`huaweicloudsdkagentarts.v1.ShowOpsAgentMetricTrendResponse`
        """
        http_info = self._show_ops_agent_metric_trend_http_info(request)
        return self._call_api(**http_info)

    def show_ops_agent_metric_trend_async_invoker(self, request):
        http_info = self._show_ops_agent_metric_trend_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_ops_agent_metric_trend_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/ops/observation/agents/metric/trend",
            "request_type": request.__class__.__name__,
            "response_type": "ShowOpsAgentMetricTrendResponse"
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
            ['application/json;charset=utf-8'])

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

    def list_ops_session_async(self, request):
        r"""查询会话列表

        查询会话列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListOpsSession
        :type request: :class:`huaweicloudsdkagentarts.v1.ListOpsSessionRequest`
        :rtype: :class:`huaweicloudsdkagentarts.v1.ListOpsSessionResponse`
        """
        http_info = self._list_ops_session_http_info(request)
        return self._call_api(**http_info)

    def list_ops_session_async_invoker(self, request):
        http_info = self._list_ops_session_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_ops_session_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/ops/observation/sessions",
            "request_type": request.__class__.__name__,
            "response_type": "ListOpsSessionResponse"
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
            ['application/json;charset=utf-8'])

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

    def show_ops_session_async(self, request):
        r"""查询会话详情

        查询会话详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowOpsSession
        :type request: :class:`huaweicloudsdkagentarts.v1.ShowOpsSessionRequest`
        :rtype: :class:`huaweicloudsdkagentarts.v1.ShowOpsSessionResponse`
        """
        http_info = self._show_ops_session_http_info(request)
        return self._call_api(**http_info)

    def show_ops_session_async_invoker(self, request):
        http_info = self._show_ops_session_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_ops_session_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/ops/observation/sessions/{session_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowOpsSessionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'session_id' in local_var_params:
            path_params['session_id'] = local_var_params['session_id']

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

    def show_ops_subscription_aom_info_async(self, request):
        r"""查询租户关联的AOM信息

        查询租户关联的AOM信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowOpsSubscriptionAomInfo
        :type request: :class:`huaweicloudsdkagentarts.v1.ShowOpsSubscriptionAomInfoRequest`
        :rtype: :class:`huaweicloudsdkagentarts.v1.ShowOpsSubscriptionAomInfoResponse`
        """
        http_info = self._show_ops_subscription_aom_info_http_info(request)
        return self._call_api(**http_info)

    def show_ops_subscription_aom_info_async_invoker(self, request):
        http_info = self._show_ops_subscription_aom_info_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_ops_subscription_aom_info_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/ops/observation/subscription/aom",
            "request_type": request.__class__.__name__,
            "response_type": "ShowOpsSubscriptionAomInfoResponse"
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

    def show_ops_subscription_apm_info_async(self, request):
        r"""查询租户关联的APM信息

        查询租户关联的APM信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowOpsSubscriptionApmInfo
        :type request: :class:`huaweicloudsdkagentarts.v1.ShowOpsSubscriptionApmInfoRequest`
        :rtype: :class:`huaweicloudsdkagentarts.v1.ShowOpsSubscriptionApmInfoResponse`
        """
        http_info = self._show_ops_subscription_apm_info_http_info(request)
        return self._call_api(**http_info)

    def show_ops_subscription_apm_info_async_invoker(self, request):
        http_info = self._show_ops_subscription_apm_info_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_ops_subscription_apm_info_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/ops/observation/subscription/apm",
            "request_type": request.__class__.__name__,
            "response_type": "ShowOpsSubscriptionApmInfoResponse"
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

    def show_ops_subscription_info_async(self, request):
        r"""查询租户关联的AOM APM LTS信息

        查询租户关联的AOM APM LTS信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowOpsSubscriptionInfo
        :type request: :class:`huaweicloudsdkagentarts.v1.ShowOpsSubscriptionInfoRequest`
        :rtype: :class:`huaweicloudsdkagentarts.v1.ShowOpsSubscriptionInfoResponse`
        """
        http_info = self._show_ops_subscription_info_http_info(request)
        return self._call_api(**http_info)

    def show_ops_subscription_info_async_invoker(self, request):
        http_info = self._show_ops_subscription_info_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_ops_subscription_info_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/ops/observation/subscription",
            "request_type": request.__class__.__name__,
            "response_type": "ShowOpsSubscriptionInfoResponse"
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

    def show_ops_subscription_lts_info_async(self, request):
        r"""查询租户关联的日志组日志流信息

        查询租户关联的日志组日志流信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowOpsSubscriptionLtsInfo
        :type request: :class:`huaweicloudsdkagentarts.v1.ShowOpsSubscriptionLtsInfoRequest`
        :rtype: :class:`huaweicloudsdkagentarts.v1.ShowOpsSubscriptionLtsInfoResponse`
        """
        http_info = self._show_ops_subscription_lts_info_http_info(request)
        return self._call_api(**http_info)

    def show_ops_subscription_lts_info_async_invoker(self, request):
        http_info = self._show_ops_subscription_lts_info_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_ops_subscription_lts_info_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/ops/observation/agents/{agent_id}/subscription/lts",
            "request_type": request.__class__.__name__,
            "response_type": "ShowOpsSubscriptionLtsInfoResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'agent_id' in local_var_params:
            path_params['agent_id'] = local_var_params['agent_id']

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

    def list_ops_trace_async(self, request):
        r"""查询trace列表

        查询trace列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListOpsTrace
        :type request: :class:`huaweicloudsdkagentarts.v1.ListOpsTraceRequest`
        :rtype: :class:`huaweicloudsdkagentarts.v1.ListOpsTraceResponse`
        """
        http_info = self._list_ops_trace_http_info(request)
        return self._call_api(**http_info)

    def list_ops_trace_async_invoker(self, request):
        http_info = self._list_ops_trace_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_ops_trace_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/ops/observation/traces",
            "request_type": request.__class__.__name__,
            "response_type": "ListOpsTraceResponse"
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
            ['application/json;charset=utf-8'])

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

    def show_ops_trace_async(self, request):
        r"""查询调用链详细信息

        查询调用链详细信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowOpsTrace
        :type request: :class:`huaweicloudsdkagentarts.v1.ShowOpsTraceRequest`
        :rtype: :class:`huaweicloudsdkagentarts.v1.ShowOpsTraceResponse`
        """
        http_info = self._show_ops_trace_http_info(request)
        return self._call_api(**http_info)

    def show_ops_trace_async_invoker(self, request):
        http_info = self._show_ops_trace_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_ops_trace_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/ops/observation/traces/{trace_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowOpsTraceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'trace_id' in local_var_params:
            path_params['trace_id'] = local_var_params['trace_id']

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

    def show_ops_trace_topology_async(self, request):
        r"""查询trace拓扑信息

        查询trace拓扑信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowOpsTraceTopology
        :type request: :class:`huaweicloudsdkagentarts.v1.ShowOpsTraceTopologyRequest`
        :rtype: :class:`huaweicloudsdkagentarts.v1.ShowOpsTraceTopologyResponse`
        """
        http_info = self._show_ops_trace_topology_http_info(request)
        return self._call_api(**http_info)

    def show_ops_trace_topology_async_invoker(self, request):
        http_info = self._show_ops_trace_topology_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_ops_trace_topology_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/ops/observation/traces/{trace_id}/topology",
            "request_type": request.__class__.__name__,
            "response_type": "ShowOpsTraceTopologyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'trace_id' in local_var_params:
            path_params['trace_id'] = local_var_params['trace_id']

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

    def tag_ops_trace_label_async(self, request):
        r"""trace数据打标签

        trace数据打标签
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for TagOpsTraceLabel
        :type request: :class:`huaweicloudsdkagentarts.v1.TagOpsTraceLabelRequest`
        :rtype: :class:`huaweicloudsdkagentarts.v1.TagOpsTraceLabelResponse`
        """
        http_info = self._tag_ops_trace_label_http_info(request)
        return self._call_api(**http_info)

    def tag_ops_trace_label_async_invoker(self, request):
        http_info = self._tag_ops_trace_label_http_info(request)
        return AsyncInvoker(self, http_info)

    def _tag_ops_trace_label_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/ops/observation/traces/{trace_id}/label",
            "request_type": request.__class__.__name__,
            "response_type": "TagOpsTraceLabelResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'trace_id' in local_var_params:
            path_params['trace_id'] = local_var_params['trace_id']

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
            ['application/json;charset=utf-8'])

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

    def update_ops_trace_feedback_async(self, request):
        r"""trace数据点赞点踩

        trace数据点赞点踩
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateOpsTraceFeedback
        :type request: :class:`huaweicloudsdkagentarts.v1.UpdateOpsTraceFeedbackRequest`
        :rtype: :class:`huaweicloudsdkagentarts.v1.UpdateOpsTraceFeedbackResponse`
        """
        http_info = self._update_ops_trace_feedback_http_info(request)
        return self._call_api(**http_info)

    def update_ops_trace_feedback_async_invoker(self, request):
        http_info = self._update_ops_trace_feedback_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_ops_trace_feedback_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/ops/observation/traces/{trace_id}/feedback",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateOpsTraceFeedbackResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'trace_id' in local_var_params:
            path_params['trace_id'] = local_var_params['trace_id']

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
            ['application/json;charset=utf-8'])

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

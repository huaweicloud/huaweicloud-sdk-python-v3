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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkapig'")


class ApigAsyncClient(Client):
    def __init__(self):
        super(ApigAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkapig.v2.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "ApigAsyncClient":
                raise TypeError("client type error, support client type is ApigAsyncClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def accept_or_reject_endpoint_connections_async(self, request):
        """接受或拒绝终端节点连接

        接受或拒绝实例节点连接。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AcceptOrRejectEndpointConnections
        :type request: :class:`huaweicloudsdkapig.v2.AcceptOrRejectEndpointConnectionsRequest`
        :rtype: :class:`huaweicloudsdkapig.v2.AcceptOrRejectEndpointConnectionsResponse`
        """
        http_info = self._accept_or_reject_endpoint_connections_http_info(request)
        return self._call_api(**http_info)

    def accept_or_reject_endpoint_connections_async_invoker(self, request):
        http_info = self._accept_or_reject_endpoint_connections_http_info(request)
        return AsyncInvoker(self, http_info)

    def _accept_or_reject_endpoint_connections_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/vpc-endpoint/connections/action",
            "request_type": request.__class__.__name__,
            "response_type": "AcceptOrRejectEndpointConnectionsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["x-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

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

    def add_custom_ingress_port_async(self, request):
        """新增实例的自定义入方向端口

        新增实例的自定义入方向端口，在同个实例中，一个端口仅能支持一种协议。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AddCustomIngressPort
        :type request: :class:`huaweicloudsdkapig.v2.AddCustomIngressPortRequest`
        :rtype: :class:`huaweicloudsdkapig.v2.AddCustomIngressPortResponse`
        """
        http_info = self._add_custom_ingress_port_http_info(request)
        return self._call_api(**http_info)

    def add_custom_ingress_port_async_invoker(self, request):
        http_info = self._add_custom_ingress_port_http_info(request)
        return AsyncInvoker(self, http_info)

    def _add_custom_ingress_port_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/custom-ingress-ports",
            "request_type": request.__class__.__name__,
            "response_type": "AddCustomIngressPortResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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
            ['application/json;charset=UTF-8'])

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

    def add_eip_v2_async(self, request):
        """实例更新或绑定EIP

        实例更新或绑定EIP
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AddEipV2
        :type request: :class:`huaweicloudsdkapig.v2.AddEipV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.AddEipV2Response`
        """
        http_info = self._add_eip_v2_http_info(request)
        return self._call_api(**http_info)

    def add_eip_v2_async_invoker(self, request):
        http_info = self._add_eip_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _add_eip_v2_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/eip",
            "request_type": request.__class__.__name__,
            "response_type": "AddEipV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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
            ['application/json;charset=UTF-8'])

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

    def add_endpoint_permissions_async(self, request):
        """批量添加实例终端节点连接白名单

        批量添加实例终端节点连接白名单。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AddEndpointPermissions
        :type request: :class:`huaweicloudsdkapig.v2.AddEndpointPermissionsRequest`
        :rtype: :class:`huaweicloudsdkapig.v2.AddEndpointPermissionsResponse`
        """
        http_info = self._add_endpoint_permissions_http_info(request)
        return self._call_api(**http_info)

    def add_endpoint_permissions_async_invoker(self, request):
        http_info = self._add_endpoint_permissions_http_info(request)
        return AsyncInvoker(self, http_info)

    def _add_endpoint_permissions_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/vpc-endpoint/permissions/batch-add",
            "request_type": request.__class__.__name__,
            "response_type": "AddEndpointPermissionsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["x-request-id", ]

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

    def add_engress_eip_v2_async(self, request):
        """开启实例公网出口

        实例开启公网出口
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AddEngressEipV2
        :type request: :class:`huaweicloudsdkapig.v2.AddEngressEipV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.AddEngressEipV2Response`
        """
        http_info = self._add_engress_eip_v2_http_info(request)
        return self._call_api(**http_info)

    def add_engress_eip_v2_async_invoker(self, request):
        http_info = self._add_engress_eip_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _add_engress_eip_v2_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/nat-eip",
            "request_type": request.__class__.__name__,
            "response_type": "AddEngressEipV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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
            ['application/json;charset=UTF-8'])

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

    def add_ingress_eip_v2_async(self, request):
        """开启实例公网入口

        开启实例开启公网入口，仅当实例为ELB类型时支持
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AddIngressEipV2
        :type request: :class:`huaweicloudsdkapig.v2.AddIngressEipV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.AddIngressEipV2Response`
        """
        http_info = self._add_ingress_eip_v2_http_info(request)
        return self._call_api(**http_info)

    def add_ingress_eip_v2_async_invoker(self, request):
        http_info = self._add_ingress_eip_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _add_ingress_eip_v2_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/ingress-eip",
            "request_type": request.__class__.__name__,
            "response_type": "AddIngressEipV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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
            ['application/json;charset=UTF-8'])

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

    def associate_apps_for_app_quota_async(self, request):
        """凭据配额绑定凭据列表

        凭据配额绑定凭据列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AssociateAppsForAppQuota
        :type request: :class:`huaweicloudsdkapig.v2.AssociateAppsForAppQuotaRequest`
        :rtype: :class:`huaweicloudsdkapig.v2.AssociateAppsForAppQuotaResponse`
        """
        http_info = self._associate_apps_for_app_quota_http_info(request)
        return self._call_api(**http_info)

    def associate_apps_for_app_quota_async_invoker(self, request):
        http_info = self._associate_apps_for_app_quota_http_info(request)
        return AsyncInvoker(self, http_info)

    def _associate_apps_for_app_quota_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/app-quotas/{app_quota_id}/binding-apps",
            "request_type": request.__class__.__name__,
            "response_type": "AssociateAppsForAppQuotaResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'app_quota_id' in local_var_params:
            path_params['app_quota_id'] = local_var_params['app_quota_id']

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
            ['application/json;charset=UTF-8'])

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

    def associate_certificate_v2_async(self, request):
        """绑定域名证书

        如果创建API时，“定义API请求”使用HTTPS请求协议，那么在独立域名中需要添加SSL证书。
        使用实例自定义入方向端口的特性时，相同的域名会同时绑定证书，注意开启/关闭客户端校验会对相同域名的不同端口同时生效。
        本章节主要介绍为特定域名绑定证书。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AssociateCertificateV2
        :type request: :class:`huaweicloudsdkapig.v2.AssociateCertificateV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.AssociateCertificateV2Response`
        """
        http_info = self._associate_certificate_v2_http_info(request)
        return self._call_api(**http_info)

    def associate_certificate_v2_async_invoker(self, request):
        http_info = self._associate_certificate_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _associate_certificate_v2_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/api-groups/{group_id}/domains/{domain_id}/certificate",
            "request_type": request.__class__.__name__,
            "response_type": "AssociateCertificateV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']

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
            ['application/json;charset=UTF-8'])

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

    def associate_domain_v2_async(self, request):
        """绑定域名

        用户自定义的域名，需要增加A记录才能生效，具体方法请参见《云解析服务用户指南》的“添加A类型记录集”章节。
        
        每个API分组下最多可绑定5个域名。绑定域名后，用户可通过自定义域名调用API。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AssociateDomainV2
        :type request: :class:`huaweicloudsdkapig.v2.AssociateDomainV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.AssociateDomainV2Response`
        """
        http_info = self._associate_domain_v2_http_info(request)
        return self._call_api(**http_info)

    def associate_domain_v2_async_invoker(self, request):
        http_info = self._associate_domain_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _associate_domain_v2_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/api-groups/{group_id}/domains",
            "request_type": request.__class__.__name__,
            "response_type": "AssociateDomainV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']

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
            ['application/json;charset=UTF-8'])

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

    def associate_signature_key_v2_async(self, request):
        """绑定签名密钥

        签名密钥创建后，需要绑定到API才能生效。
        
        
        将签名密钥绑定到API后，则API网关请求后端服务时就会使用这个签名密钥进行加密签名，后端服务可以校验这个签名来验证请求来源。
        
        
        将指定的签名密钥绑定到一个或多个已发布的API上。同一个API发布到不同的环境可以绑定不同的签名密钥；一个API在发布到特定环境后只能绑定一个签名密钥。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AssociateSignatureKeyV2
        :type request: :class:`huaweicloudsdkapig.v2.AssociateSignatureKeyV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.AssociateSignatureKeyV2Response`
        """
        http_info = self._associate_signature_key_v2_http_info(request)
        return self._call_api(**http_info)

    def associate_signature_key_v2_async_invoker(self, request):
        http_info = self._associate_signature_key_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _associate_signature_key_v2_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/sign-bindings",
            "request_type": request.__class__.__name__,
            "response_type": "AssociateSignatureKeyV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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
            ['application/json;charset=UTF-8'])

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

    def attach_api_to_plugin_async(self, request):
        """插件绑定API

        绑定插件到API上。
        - 只能选择发布状态的API
        - 绑定以后及时生效
        - 修改插件后及时生效
        - 相同类型的插件只能绑定一个，如果再次绑定同类型的插件，那么已绑定的同类型插件将直接被覆盖。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AttachApiToPlugin
        :type request: :class:`huaweicloudsdkapig.v2.AttachApiToPluginRequest`
        :rtype: :class:`huaweicloudsdkapig.v2.AttachApiToPluginResponse`
        """
        http_info = self._attach_api_to_plugin_http_info(request)
        return self._call_api(**http_info)

    def attach_api_to_plugin_async_invoker(self, request):
        http_info = self._attach_api_to_plugin_http_info(request)
        return AsyncInvoker(self, http_info)

    def _attach_api_to_plugin_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/plugins/{plugin_id}/attach",
            "request_type": request.__class__.__name__,
            "response_type": "AttachApiToPluginResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'plugin_id' in local_var_params:
            path_params['plugin_id'] = local_var_params['plugin_id']

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
            ['application/json;charset=UTF-8'])

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

    def attach_plugin_to_api_async(self, request):
        """API绑定插件

        绑定插件到API上。
        - 只能选择发布状态的API
        - 绑定以后及时生效
        - 修改插件后及时生效
        - 相同类型的插件只能绑定一个，如果再次绑定同类型的插件，那么已绑定的同类型插件将直接被覆盖。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AttachPluginToApi
        :type request: :class:`huaweicloudsdkapig.v2.AttachPluginToApiRequest`
        :rtype: :class:`huaweicloudsdkapig.v2.AttachPluginToApiResponse`
        """
        http_info = self._attach_plugin_to_api_http_info(request)
        return self._call_api(**http_info)

    def attach_plugin_to_api_async_invoker(self, request):
        http_info = self._attach_plugin_to_api_http_info(request)
        return AsyncInvoker(self, http_info)

    def _attach_plugin_to_api_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/apis/{api_id}/plugins/attach",
            "request_type": request.__class__.__name__,
            "response_type": "AttachPluginToApiResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'api_id' in local_var_params:
            path_params['api_id'] = local_var_params['api_id']

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
            ['application/json;charset=UTF-8'])

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

    def batch_create_or_delete_instance_tags_async(self, request):
        """批量添加或删除单个实例的标签

        批量添加或删除单个实例的标签。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchCreateOrDeleteInstanceTags
        :type request: :class:`huaweicloudsdkapig.v2.BatchCreateOrDeleteInstanceTagsRequest`
        :rtype: :class:`huaweicloudsdkapig.v2.BatchCreateOrDeleteInstanceTagsResponse`
        """
        http_info = self._batch_create_or_delete_instance_tags_http_info(request)
        return self._call_api(**http_info)

    def batch_create_or_delete_instance_tags_async_invoker(self, request):
        http_info = self._batch_create_or_delete_instance_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_create_or_delete_instance_tags_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/instance-tags/action",
            "request_type": request.__class__.__name__,
            "response_type": "BatchCreateOrDeleteInstanceTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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
            ['application/json;charset=UTF-8'])

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

    def check_app_v2_async(self, request):
        """校验APP

        校验app是否存在，非APP所有者可以调用该接口校验APP是否真实存在。这个接口只展示app的基本信息id 、name、
        remark，其他信息不显示。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CheckAppV2
        :type request: :class:`huaweicloudsdkapig.v2.CheckAppV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.CheckAppV2Response`
        """
        http_info = self._check_app_v2_http_info(request)
        return self._call_api(**http_info)

    def check_app_v2_async_invoker(self, request):
        http_info = self._check_app_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _check_app_v2_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/apps/validation/{app_id}",
            "request_type": request.__class__.__name__,
            "response_type": "CheckAppV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'app_id' in local_var_params:
            path_params['app_id'] = local_var_params['app_id']

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

    def create_an_app_v2_async(self, request):
        """创建APP

        APP即应用，是一个可以访问API的身份标识。将API授权给APP后，APP即可调用API。
        创建一个APP。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateAnAppV2
        :type request: :class:`huaweicloudsdkapig.v2.CreateAnAppV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.CreateAnAppV2Response`
        """
        http_info = self._create_an_app_v2_http_info(request)
        return self._call_api(**http_info)

    def create_an_app_v2_async_invoker(self, request):
        http_info = self._create_an_app_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_an_app_v2_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/apps",
            "request_type": request.__class__.__name__,
            "response_type": "CreateAnAppV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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
            ['application/json;charset=UTF-8'])

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

    def create_app_code_auto_v2_async(self, request):
        """自动生成APP Code

        创建App Code时，可以不指定具体值，由后台自动生成随机字符串填充。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateAppCodeAutoV2
        :type request: :class:`huaweicloudsdkapig.v2.CreateAppCodeAutoV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.CreateAppCodeAutoV2Response`
        """
        http_info = self._create_app_code_auto_v2_http_info(request)
        return self._call_api(**http_info)

    def create_app_code_auto_v2_async_invoker(self, request):
        http_info = self._create_app_code_auto_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_app_code_auto_v2_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/apps/{app_id}/app-codes",
            "request_type": request.__class__.__name__,
            "response_type": "CreateAppCodeAutoV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'app_id' in local_var_params:
            path_params['app_id'] = local_var_params['app_id']

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

    def create_app_code_v2_async(self, request):
        """创建APP Code

        App Code为APP应用下的子模块，创建App Code之后，可以实现简易的APP认证。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateAppCodeV2
        :type request: :class:`huaweicloudsdkapig.v2.CreateAppCodeV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.CreateAppCodeV2Response`
        """
        http_info = self._create_app_code_v2_http_info(request)
        return self._call_api(**http_info)

    def create_app_code_v2_async_invoker(self, request):
        http_info = self._create_app_code_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_app_code_v2_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/apps/{app_id}/app-codes",
            "request_type": request.__class__.__name__,
            "response_type": "CreateAppCodeV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'app_id' in local_var_params:
            path_params['app_id'] = local_var_params['app_id']

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
            ['application/json;charset=UTF-8'])

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

    def create_app_quota_async(self, request):
        """创建凭据配额

        创建凭据配额
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateAppQuota
        :type request: :class:`huaweicloudsdkapig.v2.CreateAppQuotaRequest`
        :rtype: :class:`huaweicloudsdkapig.v2.CreateAppQuotaResponse`
        """
        http_info = self._create_app_quota_http_info(request)
        return self._call_api(**http_info)

    def create_app_quota_async_invoker(self, request):
        http_info = self._create_app_quota_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_app_quota_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/app-quotas",
            "request_type": request.__class__.__name__,
            "response_type": "CreateAppQuotaResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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
            ['application/json;charset=UTF-8'])

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

    def create_custom_authorizer_v2_async(self, request):
        """创建自定义认证

        创建自定义认证
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateCustomAuthorizerV2
        :type request: :class:`huaweicloudsdkapig.v2.CreateCustomAuthorizerV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.CreateCustomAuthorizerV2Response`
        """
        http_info = self._create_custom_authorizer_v2_http_info(request)
        return self._call_api(**http_info)

    def create_custom_authorizer_v2_async_invoker(self, request):
        http_info = self._create_custom_authorizer_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_custom_authorizer_v2_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/authorizers",
            "request_type": request.__class__.__name__,
            "response_type": "CreateCustomAuthorizerV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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
            ['application/json;charset=UTF-8'])

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

    def create_environment_v2_async(self, request):
        """创建环境

        在实际的生产中，API提供者可能有多个环境，如开发环境、测试环境、生产环境等，用户可以自由将API发布到某个环境，供调用者调用。
        
        
        对于不同的环境，API的版本、请求地址甚至于包括请求消息等均有可能不同。如：某个API，v1.0的版本为稳定版本，发布到了生产环境供生产使用，同时，该API正处于迭代中，v1.1的版本是开发人员交付测试人员进行测试的版本，发布在测试环境上，而v1.2的版本目前开发团队正处于开发过程中，可以发布到开发环境进行自测等。
        
        
        为此，API网关提供多环境管理功能，使租户能够最大化的模拟实际场景，低成本的接入API网关。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateEnvironmentV2
        :type request: :class:`huaweicloudsdkapig.v2.CreateEnvironmentV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.CreateEnvironmentV2Response`
        """
        http_info = self._create_environment_v2_http_info(request)
        return self._call_api(**http_info)

    def create_environment_v2_async_invoker(self, request):
        http_info = self._create_environment_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_environment_v2_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/envs",
            "request_type": request.__class__.__name__,
            "response_type": "CreateEnvironmentV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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
            ['application/json;charset=UTF-8'])

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

    def create_environment_variable_v2_async(self, request):
        """新建变量

        将API发布到不同的环境后，对于不同的环境，可能会有不同的环境变量，比如，API的服务部署地址，请求的版本号等。
        
        
        用户可以定义不同的环境变量，用户在定义API时，在API的定义中使用这些变量，当调用API时，API网关会将这些变量替换成真实的变量值，以达到不同环境的区分效果。
        
        
        环境变量定义在API分组上，该分组下的所有API都可以使用这些变量。
        
        &gt; 1. 环境变量的变量名称必须保持唯一，即一个分组在同一个环境上不能有两个同名的变量。
        &gt; 2. 环境变量区分大小写，即变量ABC与变量abc是两个不同的变量。
        &gt; 3. 设置了环境变量后，使用到该变量的API的调试功能将不可使用。
        &gt; 4. 定义了环境变量后，使用到环境变量的地方应该以对称的#标识环境变量，当API发布到相应的环境后，会对环境变量的值进行替换，如：定义的API的URL为：https://#address#:8080，环境变量address在RELEASE环境上的值为：192.168.1.5，则API发布到RELEASE环境后的真实的URL为：https://192.168.1.5:8080。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateEnvironmentVariableV2
        :type request: :class:`huaweicloudsdkapig.v2.CreateEnvironmentVariableV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.CreateEnvironmentVariableV2Response`
        """
        http_info = self._create_environment_variable_v2_http_info(request)
        return self._call_api(**http_info)

    def create_environment_variable_v2_async_invoker(self, request):
        http_info = self._create_environment_variable_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_environment_variable_v2_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/env-variables",
            "request_type": request.__class__.__name__,
            "response_type": "CreateEnvironmentVariableV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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
            ['application/json;charset=UTF-8'])

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

    def create_feature_v2_async(self, request):
        """实例配置特性

        为实例配置需要的特性。
        
        支持配置的特性列表及特性配置示例请参考本手册中的“附录 &gt; 实例支持的APIG特性”章节。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateFeatureV2
        :type request: :class:`huaweicloudsdkapig.v2.CreateFeatureV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.CreateFeatureV2Response`
        """
        http_info = self._create_feature_v2_http_info(request)
        return self._call_api(**http_info)

    def create_feature_v2_async_invoker(self, request):
        http_info = self._create_feature_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_feature_v2_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/features",
            "request_type": request.__class__.__name__,
            "response_type": "CreateFeatureV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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
            ['application/json;charset=UTF-8'])

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

    def create_gateway_response_v2_async(self, request):
        """创建分组自定义响应

        新增分组下自定义响应
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateGatewayResponseV2
        :type request: :class:`huaweicloudsdkapig.v2.CreateGatewayResponseV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.CreateGatewayResponseV2Response`
        """
        http_info = self._create_gateway_response_v2_http_info(request)
        return self._call_api(**http_info)

    def create_gateway_response_v2_async_invoker(self, request):
        http_info = self._create_gateway_response_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_gateway_response_v2_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/api-groups/{group_id}/gateway-responses",
            "request_type": request.__class__.__name__,
            "response_type": "CreateGatewayResponseV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']

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
            ['application/json;charset=UTF-8'])

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

    def create_instance_v2_async(self, request):
        """创建专享版实例（按需）

        创建按需专享版实例
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateInstanceV2
        :type request: :class:`huaweicloudsdkapig.v2.CreateInstanceV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.CreateInstanceV2Response`
        """
        http_info = self._create_instance_v2_http_info(request)
        return self._call_api(**http_info)

    def create_instance_v2_async_invoker(self, request):
        http_info = self._create_instance_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_instance_v2_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/apigw/instances",
            "request_type": request.__class__.__name__,
            "response_type": "CreateInstanceV2Response"
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
            ['application/json;charset=UTF-8'])

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

    def create_order_async(self, request):
        """创建专享版实例（包周期）

        创建包周期专享版实例。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateOrder
        :type request: :class:`huaweicloudsdkapig.v2.CreateOrderRequest`
        :rtype: :class:`huaweicloudsdkapig.v2.CreateOrderResponse`
        """
        http_info = self._create_order_http_info(request)
        return self._call_api(**http_info)

    def create_order_async_invoker(self, request):
        http_info = self._create_order_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_order_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/apigw/prepay-instances",
            "request_type": request.__class__.__name__,
            "response_type": "CreateOrderResponse"
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
            ['application/json;charset=UTF-8'])

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

        创建插件信息。
        - 插件不允许重名
        - 插件创建后未绑定API前是无意义的，绑定API后，对绑定的API即时生效
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreatePlugin
        :type request: :class:`huaweicloudsdkapig.v2.CreatePluginRequest`
        :rtype: :class:`huaweicloudsdkapig.v2.CreatePluginResponse`
        """
        http_info = self._create_plugin_http_info(request)
        return self._call_api(**http_info)

    def create_plugin_async_invoker(self, request):
        http_info = self._create_plugin_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_plugin_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/plugins",
            "request_type": request.__class__.__name__,
            "response_type": "CreatePluginResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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
            ['application/json;charset=UTF-8'])

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

    def create_post_pay_resize_order_async(self, request):
        """按需规格变更

        创建按需规格变更订单。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreatePostPayResizeOrder
        :type request: :class:`huaweicloudsdkapig.v2.CreatePostPayResizeOrderRequest`
        :rtype: :class:`huaweicloudsdkapig.v2.CreatePostPayResizeOrderResponse`
        """
        http_info = self._create_post_pay_resize_order_http_info(request)
        return self._call_api(**http_info)

    def create_post_pay_resize_order_async_invoker(self, request):
        http_info = self._create_post_pay_resize_order_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_post_pay_resize_order_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/postpaid-resize",
            "request_type": request.__class__.__name__,
            "response_type": "CreatePostPayResizeOrderResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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
            ['application/json;charset=UTF-8'])

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

    def create_prepay_resize_async(self, request):
        """创建包周期规格变更订单

        创建包周期规格变更订单。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreatePrepayResize
        :type request: :class:`huaweicloudsdkapig.v2.CreatePrepayResizeRequest`
        :rtype: :class:`huaweicloudsdkapig.v2.CreatePrepayResizeResponse`
        """
        http_info = self._create_prepay_resize_http_info(request)
        return self._call_api(**http_info)

    def create_prepay_resize_async_invoker(self, request):
        http_info = self._create_prepay_resize_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_prepay_resize_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/prepay-resize",
            "request_type": request.__class__.__name__,
            "response_type": "CreatePrepayResizeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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
            ['application/json;charset=UTF-8'])

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

    def create_request_throttling_policy_v2_async(self, request):
        """创建流控策略

        当API上线后，系统会默认给每个API提供一个流控策略，API提供者可以根据自身API的服务能力及负载情况变更这个流控策略。
        流控策略即限制API在一定长度的时间内，能够允许被访问的最大次数。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateRequestThrottlingPolicyV2
        :type request: :class:`huaweicloudsdkapig.v2.CreateRequestThrottlingPolicyV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.CreateRequestThrottlingPolicyV2Response`
        """
        http_info = self._create_request_throttling_policy_v2_http_info(request)
        return self._call_api(**http_info)

    def create_request_throttling_policy_v2_async_invoker(self, request):
        http_info = self._create_request_throttling_policy_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_request_throttling_policy_v2_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/throttles",
            "request_type": request.__class__.__name__,
            "response_type": "CreateRequestThrottlingPolicyV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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
            ['application/json;charset=UTF-8'])

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

    def create_signature_key_v2_async(self, request):
        """创建签名密钥

        为了保护API的安全性，建议租户为API的访问提供一套保护机制，即租户开放的API，需要对请求来源进行认证，不符合认证的请求直接拒绝访问。
        
        
        其中，签名密钥就是API安全保护机制的一种。
        
        
        租户创建一个签名密钥，并将签名密钥与API进行绑定，则API网关在请求这个API时，就会使用绑定的签名密钥对请求参数进行数据加密，生成签名。当租户的后端服务收到请求时，可以校验这个签名，如果签名校验不通过，则该请求不是API网关发出的请求，租户可以拒绝这个请求，从而保证API的安全性，避免API被未知来源的请求攻击。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateSignatureKeyV2
        :type request: :class:`huaweicloudsdkapig.v2.CreateSignatureKeyV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.CreateSignatureKeyV2Response`
        """
        http_info = self._create_signature_key_v2_http_info(request)
        return self._call_api(**http_info)

    def create_signature_key_v2_async_invoker(self, request):
        http_info = self._create_signature_key_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_signature_key_v2_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/signs",
            "request_type": request.__class__.__name__,
            "response_type": "CreateSignatureKeyV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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
            ['application/json;charset=UTF-8'])

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

    def create_special_throttling_configuration_v2_async(self, request):
        """创建特殊设置

        流控策略可以限制一段时间内可以访问API的最大次数，也可以限制一段时间内单个租户和单个APP可以访问API的最大次数。
        
        如果想要对某个特定的APP进行特殊设置，例如设置所有APP每分钟的访问次数为500次，但想设置APP1每分钟的访问次数为800次，可以通过在流控策略中设置特殊APP来实现该功能。
        
        为流控策略添加一个特殊设置的对象，可以是APP，也可以是租户。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateSpecialThrottlingConfigurationV2
        :type request: :class:`huaweicloudsdkapig.v2.CreateSpecialThrottlingConfigurationV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.CreateSpecialThrottlingConfigurationV2Response`
        """
        http_info = self._create_special_throttling_configuration_v2_http_info(request)
        return self._call_api(**http_info)

    def create_special_throttling_configuration_v2_async_invoker(self, request):
        http_info = self._create_special_throttling_configuration_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_special_throttling_configuration_v2_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/throttles/{throttle_id}/throttle-specials",
            "request_type": request.__class__.__name__,
            "response_type": "CreateSpecialThrottlingConfigurationV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'throttle_id' in local_var_params:
            path_params['throttle_id'] = local_var_params['throttle_id']

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
            ['application/json;charset=UTF-8'])

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

    def delete_app_acl_async(self, request):
        """删除APP的访问控制

        删除凭据的访问控制信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteAppAcl
        :type request: :class:`huaweicloudsdkapig.v2.DeleteAppAclRequest`
        :rtype: :class:`huaweicloudsdkapig.v2.DeleteAppAclResponse`
        """
        http_info = self._delete_app_acl_http_info(request)
        return self._call_api(**http_info)

    def delete_app_acl_async_invoker(self, request):
        http_info = self._delete_app_acl_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_app_acl_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/apps/{app_id}/app-acl",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteAppAclResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'app_id' in local_var_params:
            path_params['app_id'] = local_var_params['app_id']

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

    def delete_app_code_v2_async(self, request):
        """删除APP Code

        删除App Code，App Code删除后，将无法再通过简易认证访问对应的API。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteAppCodeV2
        :type request: :class:`huaweicloudsdkapig.v2.DeleteAppCodeV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.DeleteAppCodeV2Response`
        """
        http_info = self._delete_app_code_v2_http_info(request)
        return self._call_api(**http_info)

    def delete_app_code_v2_async_invoker(self, request):
        http_info = self._delete_app_code_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_app_code_v2_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/apps/{app_id}/app-codes/{app_code_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteAppCodeV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'app_id' in local_var_params:
            path_params['app_id'] = local_var_params['app_id']
        if 'app_code_id' in local_var_params:
            path_params['app_code_id'] = local_var_params['app_code_id']

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

    def delete_app_quota_async(self, request):
        """删除凭据配额

        删除凭据配额。删除凭据配额时，同时删除凭据配额和凭据的关联关系
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteAppQuota
        :type request: :class:`huaweicloudsdkapig.v2.DeleteAppQuotaRequest`
        :rtype: :class:`huaweicloudsdkapig.v2.DeleteAppQuotaResponse`
        """
        http_info = self._delete_app_quota_http_info(request)
        return self._call_api(**http_info)

    def delete_app_quota_async_invoker(self, request):
        http_info = self._delete_app_quota_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_app_quota_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/app-quotas/{app_quota_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteAppQuotaResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'app_quota_id' in local_var_params:
            path_params['app_quota_id'] = local_var_params['app_quota_id']

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

    def delete_app_v2_async(self, request):
        """删除APP

        删除指定的APP。
        APP删除后，将无法再调用任何API[；其中，云商店自动创建的APP无法被删除](tag:hws)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteAppV2
        :type request: :class:`huaweicloudsdkapig.v2.DeleteAppV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.DeleteAppV2Response`
        """
        http_info = self._delete_app_v2_http_info(request)
        return self._call_api(**http_info)

    def delete_app_v2_async_invoker(self, request):
        http_info = self._delete_app_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_app_v2_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/apps/{app_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteAppV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'app_id' in local_var_params:
            path_params['app_id'] = local_var_params['app_id']

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

    def delete_custom_authorizer_v2_async(self, request):
        """删除自定义认证

        删除自定义认证
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteCustomAuthorizerV2
        :type request: :class:`huaweicloudsdkapig.v2.DeleteCustomAuthorizerV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.DeleteCustomAuthorizerV2Response`
        """
        http_info = self._delete_custom_authorizer_v2_http_info(request)
        return self._call_api(**http_info)

    def delete_custom_authorizer_v2_async_invoker(self, request):
        http_info = self._delete_custom_authorizer_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_custom_authorizer_v2_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/authorizers/{authorizer_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteCustomAuthorizerV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'authorizer_id' in local_var_params:
            path_params['authorizer_id'] = local_var_params['authorizer_id']

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

    def delete_custom_ingress_port_async(self, request):
        """删除实例指定的自定义入方向端口

        删除实例指定的自定义入方向端口，不包含默认端口80和443。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteCustomIngressPort
        :type request: :class:`huaweicloudsdkapig.v2.DeleteCustomIngressPortRequest`
        :rtype: :class:`huaweicloudsdkapig.v2.DeleteCustomIngressPortResponse`
        """
        http_info = self._delete_custom_ingress_port_http_info(request)
        return self._call_api(**http_info)

    def delete_custom_ingress_port_async_invoker(self, request):
        http_info = self._delete_custom_ingress_port_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_custom_ingress_port_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/custom-ingress-ports/{ingress_port_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteCustomIngressPortResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'ingress_port_id' in local_var_params:
            path_params['ingress_port_id'] = local_var_params['ingress_port_id']

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

    def delete_endpoint_permissions_async(self, request):
        """批量删除实例终端节点连接白名单

        批量删除实例终端节点连接白名单。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteEndpointPermissions
        :type request: :class:`huaweicloudsdkapig.v2.DeleteEndpointPermissionsRequest`
        :rtype: :class:`huaweicloudsdkapig.v2.DeleteEndpointPermissionsResponse`
        """
        http_info = self._delete_endpoint_permissions_http_info(request)
        return self._call_api(**http_info)

    def delete_endpoint_permissions_async_invoker(self, request):
        http_info = self._delete_endpoint_permissions_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_endpoint_permissions_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/vpc-endpoint/permissions/batch-delete",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteEndpointPermissionsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["x-request-id", ]

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

    def delete_environment_v2_async(self, request):
        """删除环境

        删除指定的环境。
        
        该操作将导致此API在指定的环境无法被访问，可能会影响相当一部分应用和用户。请确保已经告知用户，或者确认需要强制下线。
        
        环境上存在已发布的API时，该环境不能被删除。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteEnvironmentV2
        :type request: :class:`huaweicloudsdkapig.v2.DeleteEnvironmentV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.DeleteEnvironmentV2Response`
        """
        http_info = self._delete_environment_v2_http_info(request)
        return self._call_api(**http_info)

    def delete_environment_v2_async_invoker(self, request):
        http_info = self._delete_environment_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_environment_v2_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/envs/{env_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteEnvironmentV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'env_id' in local_var_params:
            path_params['env_id'] = local_var_params['env_id']

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

    def delete_environment_variable_v2_async(self, request):
        """删除变量

        删除指定的环境变量。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteEnvironmentVariableV2
        :type request: :class:`huaweicloudsdkapig.v2.DeleteEnvironmentVariableV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.DeleteEnvironmentVariableV2Response`
        """
        http_info = self._delete_environment_variable_v2_http_info(request)
        return self._call_api(**http_info)

    def delete_environment_variable_v2_async_invoker(self, request):
        http_info = self._delete_environment_variable_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_environment_variable_v2_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/env-variables/{env_variable_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteEnvironmentVariableV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'env_variable_id' in local_var_params:
            path_params['env_variable_id'] = local_var_params['env_variable_id']

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

    def delete_gateway_response_type_v2_async(self, request):
        """删除分组指定错误类型的自定义响应配置

        删除分组指定错误类型的自定义响应配置，还原为使用默认值的配置。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteGatewayResponseTypeV2
        :type request: :class:`huaweicloudsdkapig.v2.DeleteGatewayResponseTypeV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.DeleteGatewayResponseTypeV2Response`
        """
        http_info = self._delete_gateway_response_type_v2_http_info(request)
        return self._call_api(**http_info)

    def delete_gateway_response_type_v2_async_invoker(self, request):
        http_info = self._delete_gateway_response_type_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_gateway_response_type_v2_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/api-groups/{group_id}/gateway-responses/{response_id}/{response_type}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteGatewayResponseTypeV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']
        if 'response_id' in local_var_params:
            path_params['response_id'] = local_var_params['response_id']
        if 'response_type' in local_var_params:
            path_params['response_type'] = local_var_params['response_type']

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

    def delete_gateway_response_v2_async(self, request):
        """删除分组自定义响应

        删除分组自定义响应
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteGatewayResponseV2
        :type request: :class:`huaweicloudsdkapig.v2.DeleteGatewayResponseV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.DeleteGatewayResponseV2Response`
        """
        http_info = self._delete_gateway_response_v2_http_info(request)
        return self._call_api(**http_info)

    def delete_gateway_response_v2_async_invoker(self, request):
        http_info = self._delete_gateway_response_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_gateway_response_v2_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/api-groups/{group_id}/gateway-responses/{response_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteGatewayResponseV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']
        if 'response_id' in local_var_params:
            path_params['response_id'] = local_var_params['response_id']

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

    def delete_instances_v2_async(self, request):
        """删除专享版实例

        删除专享版实例
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteInstancesV2
        :type request: :class:`huaweicloudsdkapig.v2.DeleteInstancesV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.DeleteInstancesV2Response`
        """
        http_info = self._delete_instances_v2_http_info(request)
        return self._call_api(**http_info)

    def delete_instances_v2_async_invoker(self, request):
        http_info = self._delete_instances_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_instances_v2_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteInstancesV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def delete_plugin_async(self, request):
        """删除插件

        删除插件。
        - 必须先解除API和插件的绑定关系，否则删除报错
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeletePlugin
        :type request: :class:`huaweicloudsdkapig.v2.DeletePluginRequest`
        :rtype: :class:`huaweicloudsdkapig.v2.DeletePluginResponse`
        """
        http_info = self._delete_plugin_http_info(request)
        return self._call_api(**http_info)

    def delete_plugin_async_invoker(self, request):
        http_info = self._delete_plugin_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_plugin_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/plugins/{plugin_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeletePluginResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'plugin_id' in local_var_params:
            path_params['plugin_id'] = local_var_params['plugin_id']

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

    def delete_request_throttling_policy_v2_async(self, request):
        """删除流控策略

        删除指定的流控策略，以及该流控策略与API的所有绑定关系。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteRequestThrottlingPolicyV2
        :type request: :class:`huaweicloudsdkapig.v2.DeleteRequestThrottlingPolicyV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.DeleteRequestThrottlingPolicyV2Response`
        """
        http_info = self._delete_request_throttling_policy_v2_http_info(request)
        return self._call_api(**http_info)

    def delete_request_throttling_policy_v2_async_invoker(self, request):
        http_info = self._delete_request_throttling_policy_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_request_throttling_policy_v2_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/throttles/{throttle_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteRequestThrottlingPolicyV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'throttle_id' in local_var_params:
            path_params['throttle_id'] = local_var_params['throttle_id']

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

    def delete_signature_key_v2_async(self, request):
        """删除签名密钥

        删除指定的签名密钥，删除签名密钥时，其配置的绑定关系会一并删除，相应的签名密钥会失效。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteSignatureKeyV2
        :type request: :class:`huaweicloudsdkapig.v2.DeleteSignatureKeyV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.DeleteSignatureKeyV2Response`
        """
        http_info = self._delete_signature_key_v2_http_info(request)
        return self._call_api(**http_info)

    def delete_signature_key_v2_async_invoker(self, request):
        http_info = self._delete_signature_key_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_signature_key_v2_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/signs/{sign_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteSignatureKeyV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'sign_id' in local_var_params:
            path_params['sign_id'] = local_var_params['sign_id']

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

    def delete_special_throttling_configuration_v2_async(self, request):
        """删除特殊设置

        删除某个流控策略的某个特殊配置。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteSpecialThrottlingConfigurationV2
        :type request: :class:`huaweicloudsdkapig.v2.DeleteSpecialThrottlingConfigurationV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.DeleteSpecialThrottlingConfigurationV2Response`
        """
        http_info = self._delete_special_throttling_configuration_v2_http_info(request)
        return self._call_api(**http_info)

    def delete_special_throttling_configuration_v2_async_invoker(self, request):
        http_info = self._delete_special_throttling_configuration_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_special_throttling_configuration_v2_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/throttles/{throttle_id}/throttle-specials/{strategy_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteSpecialThrottlingConfigurationV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'throttle_id' in local_var_params:
            path_params['throttle_id'] = local_var_params['throttle_id']
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

    def detach_api_from_plugin_async(self, request):
        """解除绑定插件的API

        解除绑定在插件上的API。
        - 解绑及时生效
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DetachApiFromPlugin
        :type request: :class:`huaweicloudsdkapig.v2.DetachApiFromPluginRequest`
        :rtype: :class:`huaweicloudsdkapig.v2.DetachApiFromPluginResponse`
        """
        http_info = self._detach_api_from_plugin_http_info(request)
        return self._call_api(**http_info)

    def detach_api_from_plugin_async_invoker(self, request):
        http_info = self._detach_api_from_plugin_http_info(request)
        return AsyncInvoker(self, http_info)

    def _detach_api_from_plugin_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/plugins/{plugin_id}/detach",
            "request_type": request.__class__.__name__,
            "response_type": "DetachApiFromPluginResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'plugin_id' in local_var_params:
            path_params['plugin_id'] = local_var_params['plugin_id']

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
            ['application/json;charset=UTF-8'])

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

    def detach_plugin_from_api_async(self, request):
        """解除绑定API的插件

        解除绑定在API上的插件。
        - 解绑及时生效
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DetachPluginFromApi
        :type request: :class:`huaweicloudsdkapig.v2.DetachPluginFromApiRequest`
        :rtype: :class:`huaweicloudsdkapig.v2.DetachPluginFromApiResponse`
        """
        http_info = self._detach_plugin_from_api_http_info(request)
        return self._call_api(**http_info)

    def detach_plugin_from_api_async_invoker(self, request):
        http_info = self._detach_plugin_from_api_http_info(request)
        return AsyncInvoker(self, http_info)

    def _detach_plugin_from_api_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/apis/{api_id}/plugins/detach",
            "request_type": request.__class__.__name__,
            "response_type": "DetachPluginFromApiResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'api_id' in local_var_params:
            path_params['api_id'] = local_var_params['api_id']

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
            ['application/json;charset=UTF-8'])

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

    def disassociate_app_quota_with_app_async(self, request):
        """解除凭据配额和凭据的绑定

        解除凭据配额和凭据的绑定
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DisassociateAppQuotaWithApp
        :type request: :class:`huaweicloudsdkapig.v2.DisassociateAppQuotaWithAppRequest`
        :rtype: :class:`huaweicloudsdkapig.v2.DisassociateAppQuotaWithAppResponse`
        """
        http_info = self._disassociate_app_quota_with_app_http_info(request)
        return self._call_api(**http_info)

    def disassociate_app_quota_with_app_async_invoker(self, request):
        http_info = self._disassociate_app_quota_with_app_http_info(request)
        return AsyncInvoker(self, http_info)

    def _disassociate_app_quota_with_app_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/app-quotas/{app_quota_id}/bound-apps/{app_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DisassociateAppQuotaWithAppResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'app_quota_id' in local_var_params:
            path_params['app_quota_id'] = local_var_params['app_quota_id']
        if 'app_id' in local_var_params:
            path_params['app_id'] = local_var_params['app_id']

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

    def disassociate_certificate_v2_async(self, request):
        """删除域名证书

        如果域名证书不再需要或者已过期，则可以删除证书内容。在使用自定义入方向端口的特性时，相同的域名会同时解绑证书。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DisassociateCertificateV2
        :type request: :class:`huaweicloudsdkapig.v2.DisassociateCertificateV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.DisassociateCertificateV2Response`
        """
        http_info = self._disassociate_certificate_v2_http_info(request)
        return self._call_api(**http_info)

    def disassociate_certificate_v2_async_invoker(self, request):
        http_info = self._disassociate_certificate_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _disassociate_certificate_v2_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/api-groups/{group_id}/domains/{domain_id}/certificate/{certificate_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DisassociateCertificateV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']
        if 'certificate_id' in local_var_params:
            path_params['certificate_id'] = local_var_params['certificate_id']

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

    def disassociate_domain_v2_async(self, request):
        """解绑域名

        如果API分组不再需要绑定某个自定义域名，则可以为此API分组解绑此域名。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DisassociateDomainV2
        :type request: :class:`huaweicloudsdkapig.v2.DisassociateDomainV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.DisassociateDomainV2Response`
        """
        http_info = self._disassociate_domain_v2_http_info(request)
        return self._call_api(**http_info)

    def disassociate_domain_v2_async_invoker(self, request):
        http_info = self._disassociate_domain_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _disassociate_domain_v2_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/api-groups/{group_id}/domains/{domain_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DisassociateDomainV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']

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

    def disassociate_signature_key_v2_async(self, request):
        """解除API与签名密钥的绑定关系

        解除API与签名密钥的绑定关系。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DisassociateSignatureKeyV2
        :type request: :class:`huaweicloudsdkapig.v2.DisassociateSignatureKeyV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.DisassociateSignatureKeyV2Response`
        """
        http_info = self._disassociate_signature_key_v2_http_info(request)
        return self._call_api(**http_info)

    def disassociate_signature_key_v2_async_invoker(self, request):
        http_info = self._disassociate_signature_key_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _disassociate_signature_key_v2_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/sign-bindings/{sign_bindings_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DisassociateSignatureKeyV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'sign_bindings_id' in local_var_params:
            path_params['sign_bindings_id'] = local_var_params['sign_bindings_id']

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

    def export_api_definitions_async_async(self, request):
        """异步导出API

        导出分组下API的定义信息。导出文件内容符合swagger标准规范，API网关自定义扩展字段请参考《API网关开发指南》的“导入导出API：扩展定义”章节。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ExportApiDefinitionsAsync
        :type request: :class:`huaweicloudsdkapig.v2.ExportApiDefinitionsAsyncRequest`
        :rtype: :class:`huaweicloudsdkapig.v2.ExportApiDefinitionsAsyncResponse`
        """
        http_info = self._export_api_definitions_async_http_info(request)
        return self._call_api(**http_info)

    def export_api_definitions_async_async_invoker(self, request):
        http_info = self._export_api_definitions_async_http_info(request)
        return AsyncInvoker(self, http_info)

    def _export_api_definitions_async_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/openapi/async-export",
            "request_type": request.__class__.__name__,
            "response_type": "ExportApiDefinitionsAsyncResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'oas_version' in local_var_params:
            query_params.append(('oas_version', local_var_params['oas_version']))

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

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

    def import_api_definitions_async_async(self, request):
        """异步导入API

        导入API。导入文件内容需要符合swagger标准规范，API网关自定义扩展字段请参考《API网关开发指南》的“导入导出API：扩展定义”章节。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ImportApiDefinitionsAsync
        :type request: :class:`huaweicloudsdkapig.v2.ImportApiDefinitionsAsyncRequest`
        :rtype: :class:`huaweicloudsdkapig.v2.ImportApiDefinitionsAsyncResponse`
        """
        http_info = self._import_api_definitions_async_http_info(request)
        return self._call_api(**http_info)

    def import_api_definitions_async_async_invoker(self, request):
        http_info = self._import_api_definitions_async_http_info(request)
        return AsyncInvoker(self, http_info)

    def _import_api_definitions_async_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/openapi/async-import",
            "request_type": request.__class__.__name__,
            "response_type": "ImportApiDefinitionsAsyncResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}

        form_params = {}
        if 'is_create_group' in local_var_params:
            form_params['is_create_group'] = local_var_params['is_create_group']
        if 'group_id' in local_var_params:
            form_params['group_id'] = local_var_params['group_id']
        if 'extend_mode' in local_var_params:
            form_params['extend_mode'] = local_var_params['extend_mode']
        if 'simple_mode' in local_var_params:
            form_params['simple_mode'] = local_var_params['simple_mode']
        if 'mock_mode' in local_var_params:
            form_params['mock_mode'] = local_var_params['mock_mode']
        if 'api_mode' in local_var_params:
            form_params['api_mode'] = local_var_params['api_mode']
        if 'file_name' in local_var_params:
            form_params['file_name'] = local_var_params['file_name']

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

    def import_microservice_async(self, request):
        """导入微服务

        导入微服务。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ImportMicroservice
        :type request: :class:`huaweicloudsdkapig.v2.ImportMicroserviceRequest`
        :rtype: :class:`huaweicloudsdkapig.v2.ImportMicroserviceResponse`
        """
        http_info = self._import_microservice_http_info(request)
        return self._call_api(**http_info)

    def import_microservice_async_invoker(self, request):
        http_info = self._import_microservice_http_info(request)
        return AsyncInvoker(self, http_info)

    def _import_microservice_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/microservice/import",
            "request_type": request.__class__.__name__,
            "response_type": "ImportMicroserviceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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
            ['application/json;charset=UTF-8'])

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

    def list_api_attachable_plugins_async(self, request):
        """查询可绑定当前API的插件

        查询可绑定当前API的插件信息。
        - 支持分页返回
        - 支持插件名称模糊查询
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListApiAttachablePlugins
        :type request: :class:`huaweicloudsdkapig.v2.ListApiAttachablePluginsRequest`
        :rtype: :class:`huaweicloudsdkapig.v2.ListApiAttachablePluginsResponse`
        """
        http_info = self._list_api_attachable_plugins_http_info(request)
        return self._call_api(**http_info)

    def list_api_attachable_plugins_async_invoker(self, request):
        http_info = self._list_api_attachable_plugins_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_api_attachable_plugins_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/apis/{api_id}/attachable-plugins",
            "request_type": request.__class__.__name__,
            "response_type": "ListApiAttachablePluginsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'api_id' in local_var_params:
            path_params['api_id'] = local_var_params['api_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'env_id' in local_var_params:
            query_params.append(('env_id', local_var_params['env_id']))
        if 'plugin_name' in local_var_params:
            query_params.append(('plugin_name', local_var_params['plugin_name']))
        if 'plugin_type' in local_var_params:
            query_params.append(('plugin_type', local_var_params['plugin_type']))
        if 'plugin_id' in local_var_params:
            query_params.append(('plugin_id', local_var_params['plugin_id']))

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

    def list_api_attached_plugins_async(self, request):
        """查询API下绑定的插件

        查询指定API下绑定的插件信息。
        - 用于查询指定API下已经绑定的插件列表信息
        - 支持分页返回
        - 支持插件名称模糊查询
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListApiAttachedPlugins
        :type request: :class:`huaweicloudsdkapig.v2.ListApiAttachedPluginsRequest`
        :rtype: :class:`huaweicloudsdkapig.v2.ListApiAttachedPluginsResponse`
        """
        http_info = self._list_api_attached_plugins_http_info(request)
        return self._call_api(**http_info)

    def list_api_attached_plugins_async_invoker(self, request):
        http_info = self._list_api_attached_plugins_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_api_attached_plugins_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/apis/{api_id}/attached-plugins",
            "request_type": request.__class__.__name__,
            "response_type": "ListApiAttachedPluginsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'api_id' in local_var_params:
            path_params['api_id'] = local_var_params['api_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'env_id' in local_var_params:
            query_params.append(('env_id', local_var_params['env_id']))
        if 'plugin_name' in local_var_params:
            query_params.append(('plugin_name', local_var_params['plugin_name']))
        if 'plugin_id' in local_var_params:
            query_params.append(('plugin_id', local_var_params['plugin_id']))
        if 'env_name' in local_var_params:
            query_params.append(('env_name', local_var_params['env_name']))
        if 'plugin_type' in local_var_params:
            query_params.append(('plugin_type', local_var_params['plugin_type']))

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

    def list_api_groups_quantities_v2_async(self, request):
        """查询API分组概况

        查询租户名下的API分组概况。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListApiGroupsQuantitiesV2
        :type request: :class:`huaweicloudsdkapig.v2.ListApiGroupsQuantitiesV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ListApiGroupsQuantitiesV2Response`
        """
        http_info = self._list_api_groups_quantities_v2_http_info(request)
        return self._call_api(**http_info)

    def list_api_groups_quantities_v2_async_invoker(self, request):
        http_info = self._list_api_groups_quantities_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_api_groups_quantities_v2_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/resources/outline/groups",
            "request_type": request.__class__.__name__,
            "response_type": "ListApiGroupsQuantitiesV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def list_api_quantities_v2_async(self, request):
        """查询API概况

        查询租户名下的API概况：已发布到RELEASE环境的API个数，未发布到RELEASE环境的API个数。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListApiQuantitiesV2
        :type request: :class:`huaweicloudsdkapig.v2.ListApiQuantitiesV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ListApiQuantitiesV2Response`
        """
        http_info = self._list_api_quantities_v2_http_info(request)
        return self._call_api(**http_info)

    def list_api_quantities_v2_async_invoker(self, request):
        http_info = self._list_api_quantities_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_api_quantities_v2_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/resources/outline/apis",
            "request_type": request.__class__.__name__,
            "response_type": "ListApiQuantitiesV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def list_apis_binded_to_signature_key_v2_async(self, request):
        """查看签名密钥绑定的API列表

        查询某个签名密钥上已经绑定的API列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListApisBindedToSignatureKeyV2
        :type request: :class:`huaweicloudsdkapig.v2.ListApisBindedToSignatureKeyV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ListApisBindedToSignatureKeyV2Response`
        """
        http_info = self._list_apis_binded_to_signature_key_v2_http_info(request)
        return self._call_api(**http_info)

    def list_apis_binded_to_signature_key_v2_async_invoker(self, request):
        http_info = self._list_apis_binded_to_signature_key_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_apis_binded_to_signature_key_v2_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/sign-bindings/binded-apis",
            "request_type": request.__class__.__name__,
            "response_type": "ListApisBindedToSignatureKeyV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'sign_id' in local_var_params:
            query_params.append(('sign_id', local_var_params['sign_id']))
        if 'env_id' in local_var_params:
            query_params.append(('env_id', local_var_params['env_id']))
        if 'api_id' in local_var_params:
            query_params.append(('api_id', local_var_params['api_id']))
        if 'api_name' in local_var_params:
            query_params.append(('api_name', local_var_params['api_name']))
        if 'group_id' in local_var_params:
            query_params.append(('group_id', local_var_params['group_id']))

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

    def list_apis_not_bound_with_signature_key_v2_async(self, request):
        """查看签名密钥未绑定的API列表

        查询所有未绑定到该签名密钥上的API列表。需要API已经发布，未发布的API不予展示。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListApisNotBoundWithSignatureKeyV2
        :type request: :class:`huaweicloudsdkapig.v2.ListApisNotBoundWithSignatureKeyV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ListApisNotBoundWithSignatureKeyV2Response`
        """
        http_info = self._list_apis_not_bound_with_signature_key_v2_http_info(request)
        return self._call_api(**http_info)

    def list_apis_not_bound_with_signature_key_v2_async_invoker(self, request):
        http_info = self._list_apis_not_bound_with_signature_key_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_apis_not_bound_with_signature_key_v2_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/sign-bindings/unbinded-apis",
            "request_type": request.__class__.__name__,
            "response_type": "ListApisNotBoundWithSignatureKeyV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'sign_id' in local_var_params:
            query_params.append(('sign_id', local_var_params['sign_id']))
        if 'env_id' in local_var_params:
            query_params.append(('env_id', local_var_params['env_id']))
        if 'api_id' in local_var_params:
            query_params.append(('api_id', local_var_params['api_id']))
        if 'api_name' in local_var_params:
            query_params.append(('api_name', local_var_params['api_name']))
        if 'group_id' in local_var_params:
            query_params.append(('group_id', local_var_params['group_id']))

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

    def list_app_codes_v2_async(self, request):
        """查询APP Code列表

        查询App Code列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAppCodesV2
        :type request: :class:`huaweicloudsdkapig.v2.ListAppCodesV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ListAppCodesV2Response`
        """
        http_info = self._list_app_codes_v2_http_info(request)
        return self._call_api(**http_info)

    def list_app_codes_v2_async_invoker(self, request):
        http_info = self._list_app_codes_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_app_codes_v2_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/apps/{app_id}/app-codes",
            "request_type": request.__class__.__name__,
            "response_type": "ListAppCodesV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'app_id' in local_var_params:
            path_params['app_id'] = local_var_params['app_id']

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

    def list_app_quantities_v2_async(self, request):
        """查询APP概况

        查询租户名下的APP概况：已进行API访问授权的APP个数，未进行API访问授权的APP个数。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAppQuantitiesV2
        :type request: :class:`huaweicloudsdkapig.v2.ListAppQuantitiesV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ListAppQuantitiesV2Response`
        """
        http_info = self._list_app_quantities_v2_http_info(request)
        return self._call_api(**http_info)

    def list_app_quantities_v2_async_invoker(self, request):
        http_info = self._list_app_quantities_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_app_quantities_v2_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/resources/outline/apps",
            "request_type": request.__class__.__name__,
            "response_type": "ListAppQuantitiesV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def list_app_quota_bindable_apps_async(self, request):
        """查询凭据配额可绑定的凭据列表

        查询凭据配额可绑定的凭据列表。支持按凭据名称模糊搜索
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAppQuotaBindableApps
        :type request: :class:`huaweicloudsdkapig.v2.ListAppQuotaBindableAppsRequest`
        :rtype: :class:`huaweicloudsdkapig.v2.ListAppQuotaBindableAppsResponse`
        """
        http_info = self._list_app_quota_bindable_apps_http_info(request)
        return self._call_api(**http_info)

    def list_app_quota_bindable_apps_async_invoker(self, request):
        http_info = self._list_app_quota_bindable_apps_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_app_quota_bindable_apps_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/app-quotas/{app_quota_id}/bindable-apps",
            "request_type": request.__class__.__name__,
            "response_type": "ListAppQuotaBindableAppsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'app_quota_id' in local_var_params:
            path_params['app_quota_id'] = local_var_params['app_quota_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'app_name' in local_var_params:
            query_params.append(('app_name', local_var_params['app_name']))

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

    def list_app_quota_bound_apps_async(self, request):
        """查询凭据配额已绑定的凭据列表

        查询凭据配额已绑定的凭据列表。支持按凭据名称模糊匹配
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAppQuotaBoundApps
        :type request: :class:`huaweicloudsdkapig.v2.ListAppQuotaBoundAppsRequest`
        :rtype: :class:`huaweicloudsdkapig.v2.ListAppQuotaBoundAppsResponse`
        """
        http_info = self._list_app_quota_bound_apps_http_info(request)
        return self._call_api(**http_info)

    def list_app_quota_bound_apps_async_invoker(self, request):
        http_info = self._list_app_quota_bound_apps_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_app_quota_bound_apps_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/app-quotas/{app_quota_id}/bound-apps",
            "request_type": request.__class__.__name__,
            "response_type": "ListAppQuotaBoundAppsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'app_quota_id' in local_var_params:
            path_params['app_quota_id'] = local_var_params['app_quota_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'app_name' in local_var_params:
            query_params.append(('app_name', local_var_params['app_name']))

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

    def list_app_quotas_async(self, request):
        """获取凭据配额列表

        获取凭据配额列表。支持根据名称模糊查询
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAppQuotas
        :type request: :class:`huaweicloudsdkapig.v2.ListAppQuotasRequest`
        :rtype: :class:`huaweicloudsdkapig.v2.ListAppQuotasResponse`
        """
        http_info = self._list_app_quotas_http_info(request)
        return self._call_api(**http_info)

    def list_app_quotas_async_invoker(self, request):
        http_info = self._list_app_quotas_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_app_quotas_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/app-quotas",
            "request_type": request.__class__.__name__,
            "response_type": "ListAppQuotasResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
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

    def list_apps_v2_async(self, request):
        """查询APP列表

        查询APP列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAppsV2
        :type request: :class:`huaweicloudsdkapig.v2.ListAppsV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ListAppsV2Response`
        """
        http_info = self._list_apps_v2_http_info(request)
        return self._call_api(**http_info)

    def list_apps_v2_async_invoker(self, request):
        http_info = self._list_apps_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_apps_v2_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/apps",
            "request_type": request.__class__.__name__,
            "response_type": "ListAppsV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'app_key' in local_var_params:
            query_params.append(('app_key', local_var_params['app_key']))
        if 'creator' in local_var_params:
            query_params.append(('creator', local_var_params['creator']))
        if 'precise_search' in local_var_params:
            query_params.append(('precise_search', local_var_params['precise_search']))

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

    def list_available_zones_v2_async(self, request):
        """查看可用区信息

        查看可用区信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAvailableZonesV2
        :type request: :class:`huaweicloudsdkapig.v2.ListAvailableZonesV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ListAvailableZonesV2Response`
        """
        http_info = self._list_available_zones_v2_http_info(request)
        return self._call_api(**http_info)

    def list_available_zones_v2_async_invoker(self, request):
        http_info = self._list_available_zones_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_available_zones_v2_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/apigw/available-zones",
            "request_type": request.__class__.__name__,
            "response_type": "ListAvailableZonesV2Response"
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

    def list_custom_authorizers_v2_async(self, request):
        """查询自定义认证列表

        查询自定义认证列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListCustomAuthorizersV2
        :type request: :class:`huaweicloudsdkapig.v2.ListCustomAuthorizersV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ListCustomAuthorizersV2Response`
        """
        http_info = self._list_custom_authorizers_v2_http_info(request)
        return self._call_api(**http_info)

    def list_custom_authorizers_v2_async_invoker(self, request):
        http_info = self._list_custom_authorizers_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_custom_authorizers_v2_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/authorizers",
            "request_type": request.__class__.__name__,
            "response_type": "ListCustomAuthorizersV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
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

    def list_custom_ingress_port_domains_async(self, request):
        """查询实例指定的自定义入方向端口绑定的域名信息

        查询实例指定的自定义入方向端口绑定的域名信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListCustomIngressPortDomains
        :type request: :class:`huaweicloudsdkapig.v2.ListCustomIngressPortDomainsRequest`
        :rtype: :class:`huaweicloudsdkapig.v2.ListCustomIngressPortDomainsResponse`
        """
        http_info = self._list_custom_ingress_port_domains_http_info(request)
        return self._call_api(**http_info)

    def list_custom_ingress_port_domains_async_invoker(self, request):
        http_info = self._list_custom_ingress_port_domains_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_custom_ingress_port_domains_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/custom-ingress-ports/{ingress_port_id}/domains",
            "request_type": request.__class__.__name__,
            "response_type": "ListCustomIngressPortDomainsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'ingress_port_id' in local_var_params:
            path_params['ingress_port_id'] = local_var_params['ingress_port_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'domain_name' in local_var_params:
            query_params.append(('domain_name', local_var_params['domain_name']))

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

    def list_custom_ingress_ports_async(self, request):
        """查询实例的自定义入方向端口列表

        查询实例的自定义入方向端口列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListCustomIngressPorts
        :type request: :class:`huaweicloudsdkapig.v2.ListCustomIngressPortsRequest`
        :rtype: :class:`huaweicloudsdkapig.v2.ListCustomIngressPortsResponse`
        """
        http_info = self._list_custom_ingress_ports_http_info(request)
        return self._call_api(**http_info)

    def list_custom_ingress_ports_async_invoker(self, request):
        http_info = self._list_custom_ingress_ports_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_custom_ingress_ports_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/custom-ingress-ports",
            "request_type": request.__class__.__name__,
            "response_type": "ListCustomIngressPortsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'protocol' in local_var_params:
            query_params.append(('protocol', local_var_params['protocol']))
        if 'ingress_port' in local_var_params:
            query_params.append(('ingress_port', local_var_params['ingress_port']))

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

    def list_endpoint_connections_async(self, request):
        """查询实例终端节点连接列表

        查询实例终端节点连接列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListEndpointConnections
        :type request: :class:`huaweicloudsdkapig.v2.ListEndpointConnectionsRequest`
        :rtype: :class:`huaweicloudsdkapig.v2.ListEndpointConnectionsResponse`
        """
        http_info = self._list_endpoint_connections_http_info(request)
        return self._call_api(**http_info)

    def list_endpoint_connections_async_invoker(self, request):
        http_info = self._list_endpoint_connections_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_endpoint_connections_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/vpc-endpoint/connections",
            "request_type": request.__class__.__name__,
            "response_type": "ListEndpointConnectionsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'marker_id' in local_var_params:
            query_params.append(('marker_id', local_var_params['marker_id']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["x-request-id", ]

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

    def list_endpoint_permissions_async(self, request):
        """查询实例的终端节点服务的白名单列表

        查询当前实例终端节点服务的白名单列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListEndpointPermissions
        :type request: :class:`huaweicloudsdkapig.v2.ListEndpointPermissionsRequest`
        :rtype: :class:`huaweicloudsdkapig.v2.ListEndpointPermissionsResponse`
        """
        http_info = self._list_endpoint_permissions_http_info(request)
        return self._call_api(**http_info)

    def list_endpoint_permissions_async_invoker(self, request):
        http_info = self._list_endpoint_permissions_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_endpoint_permissions_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/vpc-endpoint/permissions",
            "request_type": request.__class__.__name__,
            "response_type": "ListEndpointPermissionsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'permission' in local_var_params:
            query_params.append(('permission', local_var_params['permission']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["x-request-id", ]

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

    def list_environment_variables_v2_async(self, request):
        """查询变量列表

        查询分组下的所有环境变量的列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListEnvironmentVariablesV2
        :type request: :class:`huaweicloudsdkapig.v2.ListEnvironmentVariablesV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ListEnvironmentVariablesV2Response`
        """
        http_info = self._list_environment_variables_v2_http_info(request)
        return self._call_api(**http_info)

    def list_environment_variables_v2_async_invoker(self, request):
        http_info = self._list_environment_variables_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_environment_variables_v2_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/env-variables",
            "request_type": request.__class__.__name__,
            "response_type": "ListEnvironmentVariablesV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'group_id' in local_var_params:
            query_params.append(('group_id', local_var_params['group_id']))
        if 'env_id' in local_var_params:
            query_params.append(('env_id', local_var_params['env_id']))
        if 'variable_name' in local_var_params:
            query_params.append(('variable_name', local_var_params['variable_name']))
        if 'precise_search' in local_var_params:
            query_params.append(('precise_search', local_var_params['precise_search']))

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

    def list_environments_v2_async(self, request):
        """查询环境列表

        查询符合条件的环境列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListEnvironmentsV2
        :type request: :class:`huaweicloudsdkapig.v2.ListEnvironmentsV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ListEnvironmentsV2Response`
        """
        http_info = self._list_environments_v2_http_info(request)
        return self._call_api(**http_info)

    def list_environments_v2_async_invoker(self, request):
        http_info = self._list_environments_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_environments_v2_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/envs",
            "request_type": request.__class__.__name__,
            "response_type": "ListEnvironmentsV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
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

    def list_features_v2_async(self, request):
        """查看实例特性列表

        查看实例特性列表。注意：实例不支持以下特性的需要联系技术支持升级实例版本。
        
        支持配置的特性列表及特性配置示例请参考本手册中的“附录 &gt; 实例支持的APIG特性”章节。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListFeaturesV2
        :type request: :class:`huaweicloudsdkapig.v2.ListFeaturesV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ListFeaturesV2Response`
        """
        http_info = self._list_features_v2_http_info(request)
        return self._call_api(**http_info)

    def list_features_v2_async_invoker(self, request):
        http_info = self._list_features_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_features_v2_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/features",
            "request_type": request.__class__.__name__,
            "response_type": "ListFeaturesV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def list_gateway_responses_v2_async(self, request):
        """查询分组自定义响应列表

        查询分组自定义响应列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListGatewayResponsesV2
        :type request: :class:`huaweicloudsdkapig.v2.ListGatewayResponsesV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ListGatewayResponsesV2Response`
        """
        http_info = self._list_gateway_responses_v2_http_info(request)
        return self._call_api(**http_info)

    def list_gateway_responses_v2_async_invoker(self, request):
        http_info = self._list_gateway_responses_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_gateway_responses_v2_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/api-groups/{group_id}/gateway-responses",
            "request_type": request.__class__.__name__,
            "response_type": "ListGatewayResponsesV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']

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

    def list_instance_configs_v2_async(self, request):
        """查询租户实例配置列表

        查询租户实例配置列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListInstanceConfigsV2
        :type request: :class:`huaweicloudsdkapig.v2.ListInstanceConfigsV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ListInstanceConfigsV2Response`
        """
        http_info = self._list_instance_configs_v2_http_info(request)
        return self._call_api(**http_info)

    def list_instance_configs_v2_async_invoker(self, request):
        http_info = self._list_instance_configs_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_instance_configs_v2_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/apigw/instance/configs",
            "request_type": request.__class__.__name__,
            "response_type": "ListInstanceConfigsV2Response"
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

    def list_instance_features_async(self, request):
        """查询实例支持的特性列表

        查询实例支持的特性列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListInstanceFeatures
        :type request: :class:`huaweicloudsdkapig.v2.ListInstanceFeaturesRequest`
        :rtype: :class:`huaweicloudsdkapig.v2.ListInstanceFeaturesResponse`
        """
        http_info = self._list_instance_features_http_info(request)
        return self._call_api(**http_info)

    def list_instance_features_async_invoker(self, request):
        http_info = self._list_instance_features_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_instance_features_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/instance-features",
            "request_type": request.__class__.__name__,
            "response_type": "ListInstanceFeaturesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def list_instance_tags_async(self, request):
        """查询单个实例标签

        查询单个实例的标签。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListInstanceTags
        :type request: :class:`huaweicloudsdkapig.v2.ListInstanceTagsRequest`
        :rtype: :class:`huaweicloudsdkapig.v2.ListInstanceTagsResponse`
        """
        http_info = self._list_instance_tags_http_info(request)
        return self._call_api(**http_info)

    def list_instance_tags_async_invoker(self, request):
        http_info = self._list_instance_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_instance_tags_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/instance-tags",
            "request_type": request.__class__.__name__,
            "response_type": "ListInstanceTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def list_instances_v2_async(self, request):
        """查询专享版实例列表

        查询专享版实例列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListInstancesV2
        :type request: :class:`huaweicloudsdkapig.v2.ListInstancesV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ListInstancesV2Response`
        """
        http_info = self._list_instances_v2_http_info(request)
        return self._call_api(**http_info)

    def list_instances_v2_async_invoker(self, request):
        http_info = self._list_instances_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_instances_v2_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/apigw/instances",
            "request_type": request.__class__.__name__,
            "response_type": "ListInstancesV2Response"
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
        if 'instance_id' in local_var_params:
            query_params.append(('instance_id', local_var_params['instance_id']))
        if 'instance_name' in local_var_params:
            query_params.append(('instance_name', local_var_params['instance_name']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))

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

    def list_lately_api_statistics_v2_async(self, request):
        """API统计信息查询-最近一段时间

        根据API的id和最近的一段时间查询API被调用的次数，统计周期为1分钟。查询范围一小时以内，一分钟一个样本，其样本值为一分钟内的累计值。
        &gt; 为了安全起见，在服务器上使用curl命令调用接口查询信息后，需要清理历史操作记录，包括但不限于“~/.bash_history”、“/var/log/messages”（如有）。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListLatelyApiStatisticsV2
        :type request: :class:`huaweicloudsdkapig.v2.ListLatelyApiStatisticsV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ListLatelyApiStatisticsV2Response`
        """
        http_info = self._list_lately_api_statistics_v2_http_info(request)
        return self._call_api(**http_info)

    def list_lately_api_statistics_v2_async_invoker(self, request):
        http_info = self._list_lately_api_statistics_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_lately_api_statistics_v2_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/statistics/api/latest",
            "request_type": request.__class__.__name__,
            "response_type": "ListLatelyApiStatisticsV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'api_id' in local_var_params:
            query_params.append(('api_id', local_var_params['api_id']))
        if 'duration' in local_var_params:
            query_params.append(('duration', local_var_params['duration']))

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

    def list_lately_group_statistics_v2_async(self, request):
        """分组统计信息查询-最近一小时内

        根据API分组的编号查询该分组下所有API被调用的总次数，统计周期为1分钟。查询范围一小时以内，一分钟一个样本，其样本值为一分钟内的累计值。
        &gt; 为了安全起见，在服务器上使用curl命令调用接口查询信息后，需要清理历史操作记录，包括但不限于“~/.bash_history”、“/var/log/messages”（如有）。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListLatelyGroupStatisticsV2
        :type request: :class:`huaweicloudsdkapig.v2.ListLatelyGroupStatisticsV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ListLatelyGroupStatisticsV2Response`
        """
        http_info = self._list_lately_group_statistics_v2_http_info(request)
        return self._call_api(**http_info)

    def list_lately_group_statistics_v2_async_invoker(self, request):
        http_info = self._list_lately_group_statistics_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_lately_group_statistics_v2_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/statistics/group/latest",
            "request_type": request.__class__.__name__,
            "response_type": "ListLatelyGroupStatisticsV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'group_id' in local_var_params:
            query_params.append(('group_id', local_var_params['group_id']))

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

    def list_metric_data_async(self, request):
        """查询监控数据

        查询指定时间范围指定指标的指定粒度的监控数据，可以通过参数指定需要查询的数据维度。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListMetricData
        :type request: :class:`huaweicloudsdkapig.v2.ListMetricDataRequest`
        :rtype: :class:`huaweicloudsdkapig.v2.ListMetricDataResponse`
        """
        http_info = self._list_metric_data_http_info(request)
        return self._call_api(**http_info)

    def list_metric_data_async_invoker(self, request):
        http_info = self._list_metric_data_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_metric_data_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/metric-data",
            "request_type": request.__class__.__name__,
            "response_type": "ListMetricDataResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'dim' in local_var_params:
            query_params.append(('dim', local_var_params['dim']))
        if 'metric_name' in local_var_params:
            query_params.append(('metric_name', local_var_params['metric_name']))
        if '_from' in local_var_params:
            query_params.append(('from', local_var_params['_from']))
        if 'to' in local_var_params:
            query_params.append(('to', local_var_params['to']))
        if 'period' in local_var_params:
            query_params.append(('period', local_var_params['period']))
        if 'filter' in local_var_params:
            query_params.append(('filter', local_var_params['filter']))

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

    def list_plugin_attachable_apis_async(self, request):
        """查询可绑定当前插件的API

        查询可绑定当前插件的API信息。
        - 支持分页返回
        - 支持API名称模糊查询
        - 支持已绑定其他插件的API查询返回
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListPluginAttachableApis
        :type request: :class:`huaweicloudsdkapig.v2.ListPluginAttachableApisRequest`
        :rtype: :class:`huaweicloudsdkapig.v2.ListPluginAttachableApisResponse`
        """
        http_info = self._list_plugin_attachable_apis_http_info(request)
        return self._call_api(**http_info)

    def list_plugin_attachable_apis_async_invoker(self, request):
        http_info = self._list_plugin_attachable_apis_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_plugin_attachable_apis_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/plugins/{plugin_id}/attachable-apis",
            "request_type": request.__class__.__name__,
            "response_type": "ListPluginAttachableApisResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'plugin_id' in local_var_params:
            path_params['plugin_id'] = local_var_params['plugin_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'env_id' in local_var_params:
            query_params.append(('env_id', local_var_params['env_id']))
        if 'api_name' in local_var_params:
            query_params.append(('api_name', local_var_params['api_name']))
        if 'api_id' in local_var_params:
            query_params.append(('api_id', local_var_params['api_id']))
        if 'group_id' in local_var_params:
            query_params.append(('group_id', local_var_params['group_id']))
        if 'req_method' in local_var_params:
            query_params.append(('req_method', local_var_params['req_method']))
        if 'req_uri' in local_var_params:
            query_params.append(('req_uri', local_var_params['req_uri']))

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

    def list_plugin_attached_apis_async(self, request):
        """查询插件下绑定的API

        查询指定插件下绑定的API信息。
        - 用于查询指定插件下已经绑定的API列表信息
        - 支持分页返回
        - 支持API名称模糊查询
        - 绑定关系列表中返回的API在对应的环境中可能已经下线
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListPluginAttachedApis
        :type request: :class:`huaweicloudsdkapig.v2.ListPluginAttachedApisRequest`
        :rtype: :class:`huaweicloudsdkapig.v2.ListPluginAttachedApisResponse`
        """
        http_info = self._list_plugin_attached_apis_http_info(request)
        return self._call_api(**http_info)

    def list_plugin_attached_apis_async_invoker(self, request):
        http_info = self._list_plugin_attached_apis_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_plugin_attached_apis_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/plugins/{plugin_id}/attached-apis",
            "request_type": request.__class__.__name__,
            "response_type": "ListPluginAttachedApisResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'plugin_id' in local_var_params:
            path_params['plugin_id'] = local_var_params['plugin_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'env_id' in local_var_params:
            query_params.append(('env_id', local_var_params['env_id']))
        if 'api_name' in local_var_params:
            query_params.append(('api_name', local_var_params['api_name']))
        if 'api_id' in local_var_params:
            query_params.append(('api_id', local_var_params['api_id']))
        if 'group_id' in local_var_params:
            query_params.append(('group_id', local_var_params['group_id']))
        if 'req_method' in local_var_params:
            query_params.append(('req_method', local_var_params['req_method']))
        if 'req_uri' in local_var_params:
            query_params.append(('req_uri', local_var_params['req_uri']))

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

    def list_plugins_async(self, request):
        """查询插件列表

        查询一组符合条件的API网关插件详情。
        - 支持分页
        - 支持根据插件类型查询
        - 支持根据插件可见范围查询
        - 支持根据插件编码查询
        - 支持根据名称模糊查询
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListPlugins
        :type request: :class:`huaweicloudsdkapig.v2.ListPluginsRequest`
        :rtype: :class:`huaweicloudsdkapig.v2.ListPluginsResponse`
        """
        http_info = self._list_plugins_http_info(request)
        return self._call_api(**http_info)

    def list_plugins_async_invoker(self, request):
        http_info = self._list_plugins_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_plugins_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/plugins",
            "request_type": request.__class__.__name__,
            "response_type": "ListPluginsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'plugin_type' in local_var_params:
            query_params.append(('plugin_type', local_var_params['plugin_type']))
        if 'plugin_scope' in local_var_params:
            query_params.append(('plugin_scope', local_var_params['plugin_scope']))
        if 'plugin_id' in local_var_params:
            query_params.append(('plugin_id', local_var_params['plugin_id']))
        if 'plugin_name' in local_var_params:
            query_params.append(('plugin_name', local_var_params['plugin_name']))
        if 'precise_search' in local_var_params:
            query_params.append(('precise_search', local_var_params['precise_search']))

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

    def list_project_cofigs_v2_async(self, request):
        """查询某个实例的租户配置列表

        查询某个实例的租户配置列表，用户可以通过此接口查看各类型资源配置及使用情况。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListProjectCofigsV2
        :type request: :class:`huaweicloudsdkapig.v2.ListProjectCofigsV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ListProjectCofigsV2Response`
        """
        http_info = self._list_project_cofigs_v2_http_info(request)
        return self._call_api(**http_info)

    def list_project_cofigs_v2_async_invoker(self, request):
        http_info = self._list_project_cofigs_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_project_cofigs_v2_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/project/configs",
            "request_type": request.__class__.__name__,
            "response_type": "ListProjectCofigsV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def list_project_instance_tags_async(self, request):
        """查询项目下所有实例标签

        查询项目下所有实例标签。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListProjectInstanceTags
        :type request: :class:`huaweicloudsdkapig.v2.ListProjectInstanceTagsRequest`
        :rtype: :class:`huaweicloudsdkapig.v2.ListProjectInstanceTagsResponse`
        """
        http_info = self._list_project_instance_tags_http_info(request)
        return self._call_api(**http_info)

    def list_project_instance_tags_async_invoker(self, request):
        http_info = self._list_project_instance_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_project_instance_tags_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/apigw/instance-tags",
            "request_type": request.__class__.__name__,
            "response_type": "ListProjectInstanceTagsResponse"
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

    def list_request_throttling_policy_v2_async(self, request):
        """查询流控策略列表

        查询所有流控策略的信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListRequestThrottlingPolicyV2
        :type request: :class:`huaweicloudsdkapig.v2.ListRequestThrottlingPolicyV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ListRequestThrottlingPolicyV2Response`
        """
        http_info = self._list_request_throttling_policy_v2_http_info(request)
        return self._call_api(**http_info)

    def list_request_throttling_policy_v2_async_invoker(self, request):
        http_info = self._list_request_throttling_policy_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_request_throttling_policy_v2_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/throttles",
            "request_type": request.__class__.__name__,
            "response_type": "ListRequestThrottlingPolicyV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'precise_search' in local_var_params:
            query_params.append(('precise_search', local_var_params['precise_search']))

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

    def list_signature_keys_binded_to_api_v2_async(self, request):
        """查看API绑定的签名密钥列表

        查询某个API绑定的签名密钥列表。每个API在每个环境上应该最多只会绑定一个签名密钥。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListSignatureKeysBindedToApiV2
        :type request: :class:`huaweicloudsdkapig.v2.ListSignatureKeysBindedToApiV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ListSignatureKeysBindedToApiV2Response`
        """
        http_info = self._list_signature_keys_binded_to_api_v2_http_info(request)
        return self._call_api(**http_info)

    def list_signature_keys_binded_to_api_v2_async_invoker(self, request):
        http_info = self._list_signature_keys_binded_to_api_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_signature_keys_binded_to_api_v2_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/sign-bindings/binded-signs",
            "request_type": request.__class__.__name__,
            "response_type": "ListSignatureKeysBindedToApiV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'api_id' in local_var_params:
            query_params.append(('api_id', local_var_params['api_id']))
        if 'sign_id' in local_var_params:
            query_params.append(('sign_id', local_var_params['sign_id']))
        if 'sign_name' in local_var_params:
            query_params.append(('sign_name', local_var_params['sign_name']))
        if 'env_id' in local_var_params:
            query_params.append(('env_id', local_var_params['env_id']))

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

    def list_signature_keys_v2_async(self, request):
        """查询签名密钥列表

        查询所有签名密钥的信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListSignatureKeysV2
        :type request: :class:`huaweicloudsdkapig.v2.ListSignatureKeysV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ListSignatureKeysV2Response`
        """
        http_info = self._list_signature_keys_v2_http_info(request)
        return self._call_api(**http_info)

    def list_signature_keys_v2_async_invoker(self, request):
        http_info = self._list_signature_keys_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_signature_keys_v2_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/signs",
            "request_type": request.__class__.__name__,
            "response_type": "ListSignatureKeysV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'precise_search' in local_var_params:
            query_params.append(('precise_search', local_var_params['precise_search']))

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

    def list_special_throttling_configurations_v2_async(self, request):
        """查看特殊设置列表

        查看给流控策略设置的特殊配置。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListSpecialThrottlingConfigurationsV2
        :type request: :class:`huaweicloudsdkapig.v2.ListSpecialThrottlingConfigurationsV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ListSpecialThrottlingConfigurationsV2Response`
        """
        http_info = self._list_special_throttling_configurations_v2_http_info(request)
        return self._call_api(**http_info)

    def list_special_throttling_configurations_v2_async_invoker(self, request):
        http_info = self._list_special_throttling_configurations_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_special_throttling_configurations_v2_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/throttles/{throttle_id}/throttle-specials",
            "request_type": request.__class__.__name__,
            "response_type": "ListSpecialThrottlingConfigurationsV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'throttle_id' in local_var_params:
            path_params['throttle_id'] = local_var_params['throttle_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'object_type' in local_var_params:
            query_params.append(('object_type', local_var_params['object_type']))
        if 'app_name' in local_var_params:
            query_params.append(('app_name', local_var_params['app_name']))
        if 'user' in local_var_params:
            query_params.append(('user', local_var_params['user']))

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

    def list_tags_v2_async(self, request):
        """查询标签列表

        查询标签列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListTagsV2
        :type request: :class:`huaweicloudsdkapig.v2.ListTagsV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ListTagsV2Response`
        """
        http_info = self._list_tags_v2_http_info(request)
        return self._call_api(**http_info)

    def list_tags_v2_async_invoker(self, request):
        http_info = self._list_tags_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_tags_v2_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/tags",
            "request_type": request.__class__.__name__,
            "response_type": "ListTagsV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def remove_eip_v2_async(self, request):
        """实例解绑EIP

        实例解绑EIP
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RemoveEipV2
        :type request: :class:`huaweicloudsdkapig.v2.RemoveEipV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.RemoveEipV2Response`
        """
        http_info = self._remove_eip_v2_http_info(request)
        return self._call_api(**http_info)

    def remove_eip_v2_async_invoker(self, request):
        http_info = self._remove_eip_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _remove_eip_v2_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/eip",
            "request_type": request.__class__.__name__,
            "response_type": "RemoveEipV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def remove_engress_eip_v2_async(self, request):
        """关闭实例公网出口

        关闭实例公网出口
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RemoveEngressEipV2
        :type request: :class:`huaweicloudsdkapig.v2.RemoveEngressEipV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.RemoveEngressEipV2Response`
        """
        http_info = self._remove_engress_eip_v2_http_info(request)
        return self._call_api(**http_info)

    def remove_engress_eip_v2_async_invoker(self, request):
        http_info = self._remove_engress_eip_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _remove_engress_eip_v2_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/nat-eip",
            "request_type": request.__class__.__name__,
            "response_type": "RemoveEngressEipV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def remove_ingress_eip_v2_async(self, request):
        """关闭实例公网入口

        关闭实例公网入口，仅当实例为ELB类型时支持
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RemoveIngressEipV2
        :type request: :class:`huaweicloudsdkapig.v2.RemoveIngressEipV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.RemoveIngressEipV2Response`
        """
        http_info = self._remove_ingress_eip_v2_http_info(request)
        return self._call_api(**http_info)

    def remove_ingress_eip_v2_async_invoker(self, request):
        http_info = self._remove_ingress_eip_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _remove_ingress_eip_v2_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/ingress-eip",
            "request_type": request.__class__.__name__,
            "response_type": "RemoveIngressEipV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def resetting_app_secret_v2_async(self, request):
        """重置密钥

        重置指定APP的密钥。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ResettingAppSecretV2
        :type request: :class:`huaweicloudsdkapig.v2.ResettingAppSecretV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ResettingAppSecretV2Response`
        """
        http_info = self._resetting_app_secret_v2_http_info(request)
        return self._call_api(**http_info)

    def resetting_app_secret_v2_async_invoker(self, request):
        http_info = self._resetting_app_secret_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _resetting_app_secret_v2_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/apps/secret/{app_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ResettingAppSecretV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'app_id' in local_var_params:
            path_params['app_id'] = local_var_params['app_id']

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
            ['application/json;charset=UTF-8'])

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

    def show_app_bound_app_quota_async(self, request):
        """查询凭据关联的凭据配额

        查看指定凭据关联的凭据配额。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowAppBoundAppQuota
        :type request: :class:`huaweicloudsdkapig.v2.ShowAppBoundAppQuotaRequest`
        :rtype: :class:`huaweicloudsdkapig.v2.ShowAppBoundAppQuotaResponse`
        """
        http_info = self._show_app_bound_app_quota_http_info(request)
        return self._call_api(**http_info)

    def show_app_bound_app_quota_async_invoker(self, request):
        http_info = self._show_app_bound_app_quota_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_app_bound_app_quota_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/apps/{app_id}/bound-quota",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAppBoundAppQuotaResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'app_id' in local_var_params:
            path_params['app_id'] = local_var_params['app_id']

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

    def show_app_quota_async(self, request):
        """获取凭据配额详情

        获取凭据配额详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowAppQuota
        :type request: :class:`huaweicloudsdkapig.v2.ShowAppQuotaRequest`
        :rtype: :class:`huaweicloudsdkapig.v2.ShowAppQuotaResponse`
        """
        http_info = self._show_app_quota_http_info(request)
        return self._call_api(**http_info)

    def show_app_quota_async_invoker(self, request):
        http_info = self._show_app_quota_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_app_quota_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/app-quotas/{app_quota_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAppQuotaResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'app_quota_id' in local_var_params:
            path_params['app_quota_id'] = local_var_params['app_quota_id']

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

    def show_async_task_result_async(self, request):
        """获取异步任务结果

        获取异步任务结果。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowAsyncTaskResult
        :type request: :class:`huaweicloudsdkapig.v2.ShowAsyncTaskResultRequest`
        :rtype: :class:`huaweicloudsdkapig.v2.ShowAsyncTaskResultResponse`
        """
        http_info = self._show_async_task_result_http_info(request)
        return self._call_api(**http_info)

    def show_async_task_result_async_invoker(self, request):
        http_info = self._show_async_task_result_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_async_task_result_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/async-tasks/{task_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAsyncTaskResultResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
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

    def show_details_of_app_acl_async(self, request):
        """查看APP的访问控制详情

        查看APP的访问控制详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowDetailsOfAppAcl
        :type request: :class:`huaweicloudsdkapig.v2.ShowDetailsOfAppAclRequest`
        :rtype: :class:`huaweicloudsdkapig.v2.ShowDetailsOfAppAclResponse`
        """
        http_info = self._show_details_of_app_acl_http_info(request)
        return self._call_api(**http_info)

    def show_details_of_app_acl_async_invoker(self, request):
        http_info = self._show_details_of_app_acl_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_details_of_app_acl_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/apps/{app_id}/app-acl",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDetailsOfAppAclResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'app_id' in local_var_params:
            path_params['app_id'] = local_var_params['app_id']

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

    def show_details_of_app_code_v2_async(self, request):
        """查看APP Code详情

        App Code为APP应用下的子模块，创建App Code之后，可以实现简易的APP认证。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowDetailsOfAppCodeV2
        :type request: :class:`huaweicloudsdkapig.v2.ShowDetailsOfAppCodeV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ShowDetailsOfAppCodeV2Response`
        """
        http_info = self._show_details_of_app_code_v2_http_info(request)
        return self._call_api(**http_info)

    def show_details_of_app_code_v2_async_invoker(self, request):
        http_info = self._show_details_of_app_code_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_details_of_app_code_v2_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/apps/{app_id}/app-codes/{app_code_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDetailsOfAppCodeV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'app_id' in local_var_params:
            path_params['app_id'] = local_var_params['app_id']
        if 'app_code_id' in local_var_params:
            path_params['app_code_id'] = local_var_params['app_code_id']

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

    def show_details_of_app_v2_async(self, request):
        """查看APP详情

        查看指定APP的详细信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowDetailsOfAppV2
        :type request: :class:`huaweicloudsdkapig.v2.ShowDetailsOfAppV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ShowDetailsOfAppV2Response`
        """
        http_info = self._show_details_of_app_v2_http_info(request)
        return self._call_api(**http_info)

    def show_details_of_app_v2_async_invoker(self, request):
        http_info = self._show_details_of_app_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_details_of_app_v2_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/apps/{app_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDetailsOfAppV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'app_id' in local_var_params:
            path_params['app_id'] = local_var_params['app_id']

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

    def show_details_of_custom_authorizers_v2_async(self, request):
        """查看自定义认证详情

        查看自定义认证详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowDetailsOfCustomAuthorizersV2
        :type request: :class:`huaweicloudsdkapig.v2.ShowDetailsOfCustomAuthorizersV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ShowDetailsOfCustomAuthorizersV2Response`
        """
        http_info = self._show_details_of_custom_authorizers_v2_http_info(request)
        return self._call_api(**http_info)

    def show_details_of_custom_authorizers_v2_async_invoker(self, request):
        http_info = self._show_details_of_custom_authorizers_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_details_of_custom_authorizers_v2_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/authorizers/{authorizer_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDetailsOfCustomAuthorizersV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'authorizer_id' in local_var_params:
            path_params['authorizer_id'] = local_var_params['authorizer_id']

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

    def show_details_of_domain_name_certificate_v2_async(self, request):
        """查看域名证书

        查看域名下绑定的证书详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowDetailsOfDomainNameCertificateV2
        :type request: :class:`huaweicloudsdkapig.v2.ShowDetailsOfDomainNameCertificateV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ShowDetailsOfDomainNameCertificateV2Response`
        """
        http_info = self._show_details_of_domain_name_certificate_v2_http_info(request)
        return self._call_api(**http_info)

    def show_details_of_domain_name_certificate_v2_async_invoker(self, request):
        http_info = self._show_details_of_domain_name_certificate_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_details_of_domain_name_certificate_v2_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/api-groups/{group_id}/domains/{domain_id}/certificate/{certificate_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDetailsOfDomainNameCertificateV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']
        if 'certificate_id' in local_var_params:
            path_params['certificate_id'] = local_var_params['certificate_id']

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

    def show_details_of_environment_variable_v2_async(self, request):
        """查看变量详情

        查看指定的环境变量的详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowDetailsOfEnvironmentVariableV2
        :type request: :class:`huaweicloudsdkapig.v2.ShowDetailsOfEnvironmentVariableV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ShowDetailsOfEnvironmentVariableV2Response`
        """
        http_info = self._show_details_of_environment_variable_v2_http_info(request)
        return self._call_api(**http_info)

    def show_details_of_environment_variable_v2_async_invoker(self, request):
        http_info = self._show_details_of_environment_variable_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_details_of_environment_variable_v2_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/env-variables/{env_variable_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDetailsOfEnvironmentVariableV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'env_variable_id' in local_var_params:
            path_params['env_variable_id'] = local_var_params['env_variable_id']

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

    def show_details_of_gateway_response_type_v2_async(self, request):
        """查看分组下指定错误类型的自定义响应

        查看分组下指定错误类型的自定义响应
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowDetailsOfGatewayResponseTypeV2
        :type request: :class:`huaweicloudsdkapig.v2.ShowDetailsOfGatewayResponseTypeV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ShowDetailsOfGatewayResponseTypeV2Response`
        """
        http_info = self._show_details_of_gateway_response_type_v2_http_info(request)
        return self._call_api(**http_info)

    def show_details_of_gateway_response_type_v2_async_invoker(self, request):
        http_info = self._show_details_of_gateway_response_type_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_details_of_gateway_response_type_v2_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/api-groups/{group_id}/gateway-responses/{response_id}/{response_type}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDetailsOfGatewayResponseTypeV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']
        if 'response_id' in local_var_params:
            path_params['response_id'] = local_var_params['response_id']
        if 'response_type' in local_var_params:
            path_params['response_type'] = local_var_params['response_type']

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

    def show_details_of_gateway_response_v2_async(self, request):
        """查询分组自定义响应详情

        查询分组自定义响应详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowDetailsOfGatewayResponseV2
        :type request: :class:`huaweicloudsdkapig.v2.ShowDetailsOfGatewayResponseV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ShowDetailsOfGatewayResponseV2Response`
        """
        http_info = self._show_details_of_gateway_response_v2_http_info(request)
        return self._call_api(**http_info)

    def show_details_of_gateway_response_v2_async_invoker(self, request):
        http_info = self._show_details_of_gateway_response_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_details_of_gateway_response_v2_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/api-groups/{group_id}/gateway-responses/{response_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDetailsOfGatewayResponseV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']
        if 'response_id' in local_var_params:
            path_params['response_id'] = local_var_params['response_id']

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

    def show_details_of_instance_progress_v2_async(self, request):
        """查看专享版实例创建进度

        查看专享版实例创建进度
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowDetailsOfInstanceProgressV2
        :type request: :class:`huaweicloudsdkapig.v2.ShowDetailsOfInstanceProgressV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ShowDetailsOfInstanceProgressV2Response`
        """
        http_info = self._show_details_of_instance_progress_v2_http_info(request)
        return self._call_api(**http_info)

    def show_details_of_instance_progress_v2_async_invoker(self, request):
        http_info = self._show_details_of_instance_progress_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_details_of_instance_progress_v2_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/progress",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDetailsOfInstanceProgressV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def show_details_of_instance_v2_async(self, request):
        """查看专享版实例详情

        查看专享版实例详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowDetailsOfInstanceV2
        :type request: :class:`huaweicloudsdkapig.v2.ShowDetailsOfInstanceV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ShowDetailsOfInstanceV2Response`
        """
        http_info = self._show_details_of_instance_v2_http_info(request)
        return self._call_api(**http_info)

    def show_details_of_instance_v2_async_invoker(self, request):
        http_info = self._show_details_of_instance_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_details_of_instance_v2_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDetailsOfInstanceV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def show_details_of_request_throttling_policy_v2_async(self, request):
        """查看流控策略详情

        查看指定流控策略的详细信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowDetailsOfRequestThrottlingPolicyV2
        :type request: :class:`huaweicloudsdkapig.v2.ShowDetailsOfRequestThrottlingPolicyV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ShowDetailsOfRequestThrottlingPolicyV2Response`
        """
        http_info = self._show_details_of_request_throttling_policy_v2_http_info(request)
        return self._call_api(**http_info)

    def show_details_of_request_throttling_policy_v2_async_invoker(self, request):
        http_info = self._show_details_of_request_throttling_policy_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_details_of_request_throttling_policy_v2_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/throttles/{throttle_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDetailsOfRequestThrottlingPolicyV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'throttle_id' in local_var_params:
            path_params['throttle_id'] = local_var_params['throttle_id']

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

    def show_plugin_async(self, request):
        """查询插件详情

        查询插件详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowPlugin
        :type request: :class:`huaweicloudsdkapig.v2.ShowPluginRequest`
        :rtype: :class:`huaweicloudsdkapig.v2.ShowPluginResponse`
        """
        http_info = self._show_plugin_http_info(request)
        return self._call_api(**http_info)

    def show_plugin_async_invoker(self, request):
        http_info = self._show_plugin_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_plugin_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/plugins/{plugin_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowPluginResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'plugin_id' in local_var_params:
            path_params['plugin_id'] = local_var_params['plugin_id']

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

    def show_restriction_of_instance_v2_async(self, request):
        """查看实例约束信息

        查看实例约束信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowRestrictionOfInstanceV2
        :type request: :class:`huaweicloudsdkapig.v2.ShowRestrictionOfInstanceV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ShowRestrictionOfInstanceV2Response`
        """
        http_info = self._show_restriction_of_instance_v2_http_info(request)
        return self._call_api(**http_info)

    def show_restriction_of_instance_v2_async_invoker(self, request):
        http_info = self._show_restriction_of_instance_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_restriction_of_instance_v2_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/restriction",
            "request_type": request.__class__.__name__,
            "response_type": "ShowRestrictionOfInstanceV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def update_app_acl_async(self, request):
        """设置APP的访问控制

        设置凭据的访问控制。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateAppAcl
        :type request: :class:`huaweicloudsdkapig.v2.UpdateAppAclRequest`
        :rtype: :class:`huaweicloudsdkapig.v2.UpdateAppAclResponse`
        """
        http_info = self._update_app_acl_http_info(request)
        return self._call_api(**http_info)

    def update_app_acl_async_invoker(self, request):
        http_info = self._update_app_acl_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_app_acl_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/apps/{app_id}/app-acl",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateAppAclResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'app_id' in local_var_params:
            path_params['app_id'] = local_var_params['app_id']

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
            ['application/json;charset=UTF-8'])

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

    def update_app_quota_async(self, request):
        """修改凭据配额

        修改凭据配额
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateAppQuota
        :type request: :class:`huaweicloudsdkapig.v2.UpdateAppQuotaRequest`
        :rtype: :class:`huaweicloudsdkapig.v2.UpdateAppQuotaResponse`
        """
        http_info = self._update_app_quota_http_info(request)
        return self._call_api(**http_info)

    def update_app_quota_async_invoker(self, request):
        http_info = self._update_app_quota_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_app_quota_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/app-quotas/{app_quota_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateAppQuotaResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'app_quota_id' in local_var_params:
            path_params['app_quota_id'] = local_var_params['app_quota_id']

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
            ['application/json;charset=UTF-8'])

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

    def update_app_v2_async(self, request):
        """修改APP

        修改指定APP的信息。其中可修改的属性为：name、remark，当支持用户自定义key和secret的开关开启时，app_key和app_secret也支持修改，其它属性不可修改。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateAppV2
        :type request: :class:`huaweicloudsdkapig.v2.UpdateAppV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.UpdateAppV2Response`
        """
        http_info = self._update_app_v2_http_info(request)
        return self._call_api(**http_info)

    def update_app_v2_async_invoker(self, request):
        http_info = self._update_app_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_app_v2_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/apps/{app_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateAppV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'app_id' in local_var_params:
            path_params['app_id'] = local_var_params['app_id']

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
            ['application/json;charset=UTF-8'])

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

    def update_custom_authorizer_v2_async(self, request):
        """修改自定义认证

        修改自定义认证
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateCustomAuthorizerV2
        :type request: :class:`huaweicloudsdkapig.v2.UpdateCustomAuthorizerV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.UpdateCustomAuthorizerV2Response`
        """
        http_info = self._update_custom_authorizer_v2_http_info(request)
        return self._call_api(**http_info)

    def update_custom_authorizer_v2_async_invoker(self, request):
        http_info = self._update_custom_authorizer_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_custom_authorizer_v2_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/authorizers/{authorizer_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateCustomAuthorizerV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'authorizer_id' in local_var_params:
            path_params['authorizer_id'] = local_var_params['authorizer_id']

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
            ['application/json;charset=UTF-8'])

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

    def update_domain_v2_async(self, request):
        """修改域名

        修改绑定的域名所对应的配置信息。使用实例自定义入方向端口的特性时，注意开启/关闭客户端校验会对相同域名的不同端口同时生效。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateDomainV2
        :type request: :class:`huaweicloudsdkapig.v2.UpdateDomainV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.UpdateDomainV2Response`
        """
        http_info = self._update_domain_v2_http_info(request)
        return self._call_api(**http_info)

    def update_domain_v2_async_invoker(self, request):
        http_info = self._update_domain_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_domain_v2_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/api-groups/{group_id}/domains/{domain_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateDomainV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']

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
            ['application/json;charset=UTF-8'])

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

    def update_engress_eip_v2_async(self, request):
        """更新实例出公网带宽

        更新实例出公网带宽
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateEngressEipV2
        :type request: :class:`huaweicloudsdkapig.v2.UpdateEngressEipV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.UpdateEngressEipV2Response`
        """
        http_info = self._update_engress_eip_v2_http_info(request)
        return self._call_api(**http_info)

    def update_engress_eip_v2_async_invoker(self, request):
        http_info = self._update_engress_eip_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_engress_eip_v2_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/nat-eip",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateEngressEipV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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
            ['application/json;charset=UTF-8'])

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

    def update_environment_v2_async(self, request):
        """修改环境

        修改指定环境的信息。其中可修改的属性为：name、remark，其它属性不可修改。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateEnvironmentV2
        :type request: :class:`huaweicloudsdkapig.v2.UpdateEnvironmentV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.UpdateEnvironmentV2Response`
        """
        http_info = self._update_environment_v2_http_info(request)
        return self._call_api(**http_info)

    def update_environment_v2_async_invoker(self, request):
        http_info = self._update_environment_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_environment_v2_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/envs/{env_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateEnvironmentV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'env_id' in local_var_params:
            path_params['env_id'] = local_var_params['env_id']

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
            ['application/json;charset=UTF-8'])

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

    def update_environment_variable_v2_async(self, request):
        """修改变量

        修改环境变量。环境变量引用位置为api的后端服务地址时，修改对应环境变量会将使用该变量的所有api重新发布。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateEnvironmentVariableV2
        :type request: :class:`huaweicloudsdkapig.v2.UpdateEnvironmentVariableV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.UpdateEnvironmentVariableV2Response`
        """
        http_info = self._update_environment_variable_v2_http_info(request)
        return self._call_api(**http_info)

    def update_environment_variable_v2_async_invoker(self, request):
        http_info = self._update_environment_variable_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_environment_variable_v2_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/env-variables/{env_variable_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateEnvironmentVariableV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'env_variable_id' in local_var_params:
            path_params['env_variable_id'] = local_var_params['env_variable_id']

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
            ['application/json;charset=UTF-8'])

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

    def update_gateway_response_type_v2_async(self, request):
        """修改分组下指定错误类型的自定义响应

        修改分组下指定错误类型的自定义响应。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateGatewayResponseTypeV2
        :type request: :class:`huaweicloudsdkapig.v2.UpdateGatewayResponseTypeV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.UpdateGatewayResponseTypeV2Response`
        """
        http_info = self._update_gateway_response_type_v2_http_info(request)
        return self._call_api(**http_info)

    def update_gateway_response_type_v2_async_invoker(self, request):
        http_info = self._update_gateway_response_type_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_gateway_response_type_v2_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/api-groups/{group_id}/gateway-responses/{response_id}/{response_type}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateGatewayResponseTypeV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']
        if 'response_id' in local_var_params:
            path_params['response_id'] = local_var_params['response_id']
        if 'response_type' in local_var_params:
            path_params['response_type'] = local_var_params['response_type']

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
            ['application/json;charset=UTF-8'])

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

    def update_gateway_response_v2_async(self, request):
        """修改分组自定义响应

        修改分组自定义响应
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateGatewayResponseV2
        :type request: :class:`huaweicloudsdkapig.v2.UpdateGatewayResponseV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.UpdateGatewayResponseV2Response`
        """
        http_info = self._update_gateway_response_v2_http_info(request)
        return self._call_api(**http_info)

    def update_gateway_response_v2_async_invoker(self, request):
        http_info = self._update_gateway_response_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_gateway_response_v2_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/api-groups/{group_id}/gateway-responses/{response_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateGatewayResponseV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']
        if 'response_id' in local_var_params:
            path_params['response_id'] = local_var_params['response_id']

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
            ['application/json;charset=UTF-8'])

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

    def update_ingress_eip_v2_async(self, request):
        """更新实例入公网带宽

        更新实例入公网带宽，仅当实例为ELB类型时支持
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateIngressEipV2
        :type request: :class:`huaweicloudsdkapig.v2.UpdateIngressEipV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.UpdateIngressEipV2Response`
        """
        http_info = self._update_ingress_eip_v2_http_info(request)
        return self._call_api(**http_info)

    def update_ingress_eip_v2_async_invoker(self, request):
        http_info = self._update_ingress_eip_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_ingress_eip_v2_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/ingress-eip",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateIngressEipV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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
            ['application/json;charset=UTF-8'])

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

    def update_instance_v2_async(self, request):
        """更新专享版实例

        更新专享版实例
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateInstanceV2
        :type request: :class:`huaweicloudsdkapig.v2.UpdateInstanceV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.UpdateInstanceV2Response`
        """
        http_info = self._update_instance_v2_http_info(request)
        return self._call_api(**http_info)

    def update_instance_v2_async_invoker(self, request):
        http_info = self._update_instance_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_instance_v2_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateInstanceV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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
            ['application/json;charset=UTF-8'])

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

    def update_plugin_async(self, request):
        """修改插件

        修改插件信息。
        - 插件不允许重名
        - 插件不支持修改类型和可见范围
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdatePlugin
        :type request: :class:`huaweicloudsdkapig.v2.UpdatePluginRequest`
        :rtype: :class:`huaweicloudsdkapig.v2.UpdatePluginResponse`
        """
        http_info = self._update_plugin_http_info(request)
        return self._call_api(**http_info)

    def update_plugin_async_invoker(self, request):
        http_info = self._update_plugin_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_plugin_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/plugins/{plugin_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdatePluginResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'plugin_id' in local_var_params:
            path_params['plugin_id'] = local_var_params['plugin_id']

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
            ['application/json;charset=UTF-8'])

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

    def update_request_throttling_policy_v2_async(self, request):
        """修改流控策略

        修改指定流控策略的详细信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateRequestThrottlingPolicyV2
        :type request: :class:`huaweicloudsdkapig.v2.UpdateRequestThrottlingPolicyV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.UpdateRequestThrottlingPolicyV2Response`
        """
        http_info = self._update_request_throttling_policy_v2_http_info(request)
        return self._call_api(**http_info)

    def update_request_throttling_policy_v2_async_invoker(self, request):
        http_info = self._update_request_throttling_policy_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_request_throttling_policy_v2_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/throttles/{throttle_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateRequestThrottlingPolicyV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'throttle_id' in local_var_params:
            path_params['throttle_id'] = local_var_params['throttle_id']

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
            ['application/json;charset=UTF-8'])

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

    def update_signature_key_v2_async(self, request):
        """修改签名密钥

        修改指定签名密钥的详细信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateSignatureKeyV2
        :type request: :class:`huaweicloudsdkapig.v2.UpdateSignatureKeyV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.UpdateSignatureKeyV2Response`
        """
        http_info = self._update_signature_key_v2_http_info(request)
        return self._call_api(**http_info)

    def update_signature_key_v2_async_invoker(self, request):
        http_info = self._update_signature_key_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_signature_key_v2_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/signs/{sign_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateSignatureKeyV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'sign_id' in local_var_params:
            path_params['sign_id'] = local_var_params['sign_id']

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
            ['application/json;charset=UTF-8'])

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

    def update_sl_domain_setting_v2_async(self, request):
        """设置调试域名是否可以访问

        禁用或启用API分组绑定的调试域名
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateSlDomainSettingV2
        :type request: :class:`huaweicloudsdkapig.v2.UpdateSlDomainSettingV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.UpdateSlDomainSettingV2Response`
        """
        http_info = self._update_sl_domain_setting_v2_http_info(request)
        return self._call_api(**http_info)

    def update_sl_domain_setting_v2_async_invoker(self, request):
        http_info = self._update_sl_domain_setting_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_sl_domain_setting_v2_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/api-groups/{group_id}/sl-domain-access-settings",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateSlDomainSettingV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']

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
            ['application/json;charset=UTF-8'])

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

    def update_special_throttling_configuration_v2_async(self, request):
        """修改特殊设置

        修改某个流控策略下的某个特殊设置。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateSpecialThrottlingConfigurationV2
        :type request: :class:`huaweicloudsdkapig.v2.UpdateSpecialThrottlingConfigurationV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.UpdateSpecialThrottlingConfigurationV2Response`
        """
        http_info = self._update_special_throttling_configuration_v2_http_info(request)
        return self._call_api(**http_info)

    def update_special_throttling_configuration_v2_async_invoker(self, request):
        http_info = self._update_special_throttling_configuration_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_special_throttling_configuration_v2_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/throttles/{throttle_id}/throttle-specials/{strategy_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateSpecialThrottlingConfigurationV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'throttle_id' in local_var_params:
            path_params['throttle_id'] = local_var_params['throttle_id']
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
            ['application/json;charset=UTF-8'])

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

    def batch_delete_acl_v2_async(self, request):
        """批量删除ACL策略

        批量删除指定的多个ACL策略。
        
        删除ACL策略时，如果存在ACL策略与API绑定关系，则无法删除。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchDeleteAclV2
        :type request: :class:`huaweicloudsdkapig.v2.BatchDeleteAclV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.BatchDeleteAclV2Response`
        """
        http_info = self._batch_delete_acl_v2_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_acl_v2_async_invoker(self, request):
        http_info = self._batch_delete_acl_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_delete_acl_v2_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/acls",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeleteAclV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'action' in local_var_params:
            query_params.append(('action', local_var_params['action']))

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

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

    def create_acl_strategy_v2_async(self, request):
        """创建ACL策略

        增加一个ACL策略，策略类型通过字段acl_type来确定（permit或者deny），限制的对象的类型可以为IP或者DOMAIN，这里的DOMAIN对应的acl_value的值为租户名称，而非“www.exampleDomain.com”之类的网络域名。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateAclStrategyV2
        :type request: :class:`huaweicloudsdkapig.v2.CreateAclStrategyV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.CreateAclStrategyV2Response`
        """
        http_info = self._create_acl_strategy_v2_http_info(request)
        return self._call_api(**http_info)

    def create_acl_strategy_v2_async_invoker(self, request):
        http_info = self._create_acl_strategy_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_acl_strategy_v2_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/acls",
            "request_type": request.__class__.__name__,
            "response_type": "CreateAclStrategyV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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
            ['application/json;charset=UTF-8'])

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

    def delete_acl_v2_async(self, request):
        """删除ACL策略

        删除指定的ACL策略， 如果存在api与该ACL策略的绑定关系，则无法删除
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteAclV2
        :type request: :class:`huaweicloudsdkapig.v2.DeleteAclV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.DeleteAclV2Response`
        """
        http_info = self._delete_acl_v2_http_info(request)
        return self._call_api(**http_info)

    def delete_acl_v2_async_invoker(self, request):
        http_info = self._delete_acl_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_acl_v2_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/acls/{acl_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteAclV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'acl_id' in local_var_params:
            path_params['acl_id'] = local_var_params['acl_id']

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

    def list_acl_strategies_v2_async(self, request):
        """查看ACL策略列表

        查询所有的ACL策略列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAclStrategiesV2
        :type request: :class:`huaweicloudsdkapig.v2.ListAclStrategiesV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ListAclStrategiesV2Response`
        """
        http_info = self._list_acl_strategies_v2_http_info(request)
        return self._call_api(**http_info)

    def list_acl_strategies_v2_async_invoker(self, request):
        http_info = self._list_acl_strategies_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_acl_strategies_v2_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/acls",
            "request_type": request.__class__.__name__,
            "response_type": "ListAclStrategiesV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'acl_type' in local_var_params:
            query_params.append(('acl_type', local_var_params['acl_type']))
        if 'entity_type' in local_var_params:
            query_params.append(('entity_type', local_var_params['entity_type']))
        if 'precise_search' in local_var_params:
            query_params.append(('precise_search', local_var_params['precise_search']))

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

    def show_details_of_acl_policy_v2_async(self, request):
        """查看ACL策略详情

        查询指定ACL策略的详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowDetailsOfAclPolicyV2
        :type request: :class:`huaweicloudsdkapig.v2.ShowDetailsOfAclPolicyV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ShowDetailsOfAclPolicyV2Response`
        """
        http_info = self._show_details_of_acl_policy_v2_http_info(request)
        return self._call_api(**http_info)

    def show_details_of_acl_policy_v2_async_invoker(self, request):
        http_info = self._show_details_of_acl_policy_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_details_of_acl_policy_v2_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/acls/{acl_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDetailsOfAclPolicyV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'acl_id' in local_var_params:
            path_params['acl_id'] = local_var_params['acl_id']

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

    def update_acl_strategy_v2_async(self, request):
        """修改ACL策略

        修改指定的ACL策略，其中可修改的属性为：acl_name、acl_type、acl_value，其它属性不可修改。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateAclStrategyV2
        :type request: :class:`huaweicloudsdkapig.v2.UpdateAclStrategyV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.UpdateAclStrategyV2Response`
        """
        http_info = self._update_acl_strategy_v2_http_info(request)
        return self._call_api(**http_info)

    def update_acl_strategy_v2_async_invoker(self, request):
        http_info = self._update_acl_strategy_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_acl_strategy_v2_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/acls/{acl_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateAclStrategyV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'acl_id' in local_var_params:
            path_params['acl_id'] = local_var_params['acl_id']

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
            ['application/json;charset=UTF-8'])

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

    def associate_request_throttling_policy_v2_async(self, request):
        """绑定流控策略

        将流控策略应用于API，则所有对该API的访问将会受到该流控策略的限制。
        
        
        当一定时间内的访问次数超过流控策略设置的API最大访问次数限制后，后续的访问将会被拒绝，从而能够较好的保护后端API免受异常流量的冲击，保障服务的稳定运行。
        
        
        为指定的API绑定流控策略，绑定时，需要指定在哪个环境上生效。同一个API发布到不同的环境可以绑定不同的流控策略；一个API在发布到特定环境后只能绑定一个默认的流控策略。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AssociateRequestThrottlingPolicyV2
        :type request: :class:`huaweicloudsdkapig.v2.AssociateRequestThrottlingPolicyV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.AssociateRequestThrottlingPolicyV2Response`
        """
        http_info = self._associate_request_throttling_policy_v2_http_info(request)
        return self._call_api(**http_info)

    def associate_request_throttling_policy_v2_async_invoker(self, request):
        http_info = self._associate_request_throttling_policy_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _associate_request_throttling_policy_v2_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/throttle-bindings",
            "request_type": request.__class__.__name__,
            "response_type": "AssociateRequestThrottlingPolicyV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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
            ['application/json;charset=UTF-8'])

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

    def batch_disassociate_throttling_policy_v2_async(self, request):
        """批量解绑流控策略

        批量解除API与流控策略的绑定关系
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchDisassociateThrottlingPolicyV2
        :type request: :class:`huaweicloudsdkapig.v2.BatchDisassociateThrottlingPolicyV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.BatchDisassociateThrottlingPolicyV2Response`
        """
        http_info = self._batch_disassociate_throttling_policy_v2_http_info(request)
        return self._call_api(**http_info)

    def batch_disassociate_throttling_policy_v2_async_invoker(self, request):
        http_info = self._batch_disassociate_throttling_policy_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_disassociate_throttling_policy_v2_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/throttle-bindings",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDisassociateThrottlingPolicyV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'action' in local_var_params:
            query_params.append(('action', local_var_params['action']))

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

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

    def batch_publish_or_offline_api_v2_async(self, request):
        """批量发布或下线API

        将多个API发布到一个指定的环境，或将多个API从指定的环境下线。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchPublishOrOfflineApiV2
        :type request: :class:`huaweicloudsdkapig.v2.BatchPublishOrOfflineApiV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.BatchPublishOrOfflineApiV2Response`
        """
        http_info = self._batch_publish_or_offline_api_v2_http_info(request)
        return self._call_api(**http_info)

    def batch_publish_or_offline_api_v2_async_invoker(self, request):
        http_info = self._batch_publish_or_offline_api_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_publish_or_offline_api_v2_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/apis/publish",
            "request_type": request.__class__.__name__,
            "response_type": "BatchPublishOrOfflineApiV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'action' in local_var_params:
            query_params.append(('action', local_var_params['action']))

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

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

    def change_api_version_v2_async(self, request):
        """切换API版本

        API每次发布时，会基于当前的API定义生成一个版本。版本记录了API发布时的各种定义及状态。
        
        多个版本之间可以进行随意切换。但一个API在一个环境上，只能有一个版本生效。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ChangeApiVersionV2
        :type request: :class:`huaweicloudsdkapig.v2.ChangeApiVersionV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ChangeApiVersionV2Response`
        """
        http_info = self._change_api_version_v2_http_info(request)
        return self._call_api(**http_info)

    def change_api_version_v2_async_invoker(self, request):
        http_info = self._change_api_version_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _change_api_version_v2_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/apis/publish/{api_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ChangeApiVersionV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'api_id' in local_var_params:
            path_params['api_id'] = local_var_params['api_id']

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
            ['application/json;charset=UTF-8'])

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

    def check_api_groups_v2_async(self, request):
        """校验API分组名称是否存在

        校验API分组名称是否存在。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CheckApiGroupsV2
        :type request: :class:`huaweicloudsdkapig.v2.CheckApiGroupsV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.CheckApiGroupsV2Response`
        """
        http_info = self._check_api_groups_v2_http_info(request)
        return self._call_api(**http_info)

    def check_api_groups_v2_async_invoker(self, request):
        http_info = self._check_api_groups_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _check_api_groups_v2_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/api-groups/check",
            "request_type": request.__class__.__name__,
            "response_type": "CheckApiGroupsV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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
            ['application/json;charset=UTF-8'])

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

    def check_apis_v2_async(self, request):
        """校验API定义

        校验API定义。校验API的路径或名称是否已存在
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CheckApisV2
        :type request: :class:`huaweicloudsdkapig.v2.CheckApisV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.CheckApisV2Response`
        """
        http_info = self._check_apis_v2_http_info(request)
        return self._call_api(**http_info)

    def check_apis_v2_async_invoker(self, request):
        http_info = self._check_apis_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _check_apis_v2_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/apis/check",
            "request_type": request.__class__.__name__,
            "response_type": "CheckApisV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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
            ['application/json;charset=UTF-8'])

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

    def create_api_group_v2_async(self, request):
        """创建API分组

        API分组是API的管理单元，一个API分组等同于一个服务入口，创建API分组时，返回一个子域名作为访问入口。建议一个API分组下的API具有一定的相关性。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateApiGroupV2
        :type request: :class:`huaweicloudsdkapig.v2.CreateApiGroupV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.CreateApiGroupV2Response`
        """
        http_info = self._create_api_group_v2_http_info(request)
        return self._call_api(**http_info)

    def create_api_group_v2_async_invoker(self, request):
        http_info = self._create_api_group_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_api_group_v2_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/api-groups",
            "request_type": request.__class__.__name__,
            "response_type": "CreateApiGroupV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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
            ['application/json;charset=UTF-8'])

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

    def create_api_v2_async(self, request):
        """创建API

        添加一个API，API即一个服务接口，具体的服务能力。
        
        
        API分为两部分，第一部分为面向API使用者的API接口，定义了使用者如何调用这个API。第二部分面向API提供者，由API提供者定义这个API的真实的后端情况，定义了API网关如何去访问真实的后端服务。API的真实后端服务目前支持四种类型：传统的HTTP/HTTPS形式的web后端、GRPC后端、函数工作流、MOCK。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateApiV2
        :type request: :class:`huaweicloudsdkapig.v2.CreateApiV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.CreateApiV2Response`
        """
        http_info = self._create_api_v2_http_info(request)
        return self._call_api(**http_info)

    def create_api_v2_async_invoker(self, request):
        http_info = self._create_api_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_api_v2_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/apis",
            "request_type": request.__class__.__name__,
            "response_type": "CreateApiV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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
            ['application/json;charset=UTF-8'])

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

    def create_or_delete_publish_record_for_api_v2_async(self, request):
        """发布或下线API

        对API进行发布或下线。
        
        发布操作是将一个指定的API发布到一个指定的环境，API只有发布后，才能够被调用，且只能在该环境上才能被调用。未发布的API无法被调用。
        
        下线操作是将API从某个已发布的环境上下线，下线后，API将无法再被调用。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateOrDeletePublishRecordForApiV2
        :type request: :class:`huaweicloudsdkapig.v2.CreateOrDeletePublishRecordForApiV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.CreateOrDeletePublishRecordForApiV2Response`
        """
        http_info = self._create_or_delete_publish_record_for_api_v2_http_info(request)
        return self._call_api(**http_info)

    def create_or_delete_publish_record_for_api_v2_async_invoker(self, request):
        http_info = self._create_or_delete_publish_record_for_api_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_or_delete_publish_record_for_api_v2_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/apis/action",
            "request_type": request.__class__.__name__,
            "response_type": "CreateOrDeletePublishRecordForApiV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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
            ['application/json;charset=UTF-8'])

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

    def debug_api_v2_async(self, request):
        """调试API

        调试一个API在指定运行环境下的定义，接口调用者需要具有操作该API的权限。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DebugApiV2
        :type request: :class:`huaweicloudsdkapig.v2.DebugApiV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.DebugApiV2Response`
        """
        http_info = self._debug_api_v2_http_info(request)
        return self._call_api(**http_info)

    def debug_api_v2_async_invoker(self, request):
        http_info = self._debug_api_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _debug_api_v2_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/apis/debug/{api_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DebugApiV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'api_id' in local_var_params:
            path_params['api_id'] = local_var_params['api_id']

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
            ['application/json;charset=UTF-8'])

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

    def delete_api_by_version_id_v2_async(self, request):
        """根据版本编号下线API

        对某个生效中的API版本进行下线操作，下线后，API在该版本生效的环境中将不再能够被调用。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteApiByVersionIdV2
        :type request: :class:`huaweicloudsdkapig.v2.DeleteApiByVersionIdV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.DeleteApiByVersionIdV2Response`
        """
        http_info = self._delete_api_by_version_id_v2_http_info(request)
        return self._call_api(**http_info)

    def delete_api_by_version_id_v2_async_invoker(self, request):
        http_info = self._delete_api_by_version_id_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_api_by_version_id_v2_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/apis/versions/{version_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteApiByVersionIdV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
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

    def delete_api_group_v2_async(self, request):
        """删除API分组

        删除指定的API分组。
        
        删除API分组前，要先下线并删除分组下的所有API。
        
        删除时，会一并删除直接或间接关联到该分组下的所有资源，包括独立域名、SSL证书信息等等。并会将外部域名与子域名的绑定关系进行解除（取决于域名cname方式）。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteApiGroupV2
        :type request: :class:`huaweicloudsdkapig.v2.DeleteApiGroupV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.DeleteApiGroupV2Response`
        """
        http_info = self._delete_api_group_v2_http_info(request)
        return self._call_api(**http_info)

    def delete_api_group_v2_async_invoker(self, request):
        http_info = self._delete_api_group_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_api_group_v2_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/api-groups/{group_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteApiGroupV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']

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

    def delete_api_v2_async(self, request):
        """删除API

        删除指定的API。
        
        删除API时，会删除该API所有相关的资源信息或绑定关系，如API的发布记录，绑定的后端服务，对APP的授权信息等。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteApiV2
        :type request: :class:`huaweicloudsdkapig.v2.DeleteApiV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.DeleteApiV2Response`
        """
        http_info = self._delete_api_v2_http_info(request)
        return self._call_api(**http_info)

    def delete_api_v2_async_invoker(self, request):
        http_info = self._delete_api_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_api_v2_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/apis/{api_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteApiV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'api_id' in local_var_params:
            path_params['api_id'] = local_var_params['api_id']

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

    def disassociate_request_throttling_policy_v2_async(self, request):
        """解除API与流控策略的绑定关系

        解除API与流控策略的绑定关系。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DisassociateRequestThrottlingPolicyV2
        :type request: :class:`huaweicloudsdkapig.v2.DisassociateRequestThrottlingPolicyV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.DisassociateRequestThrottlingPolicyV2Response`
        """
        http_info = self._disassociate_request_throttling_policy_v2_http_info(request)
        return self._call_api(**http_info)

    def disassociate_request_throttling_policy_v2_async_invoker(self, request):
        http_info = self._disassociate_request_throttling_policy_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _disassociate_request_throttling_policy_v2_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/throttle-bindings/{throttle_binding_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DisassociateRequestThrottlingPolicyV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'throttle_binding_id' in local_var_params:
            path_params['throttle_binding_id'] = local_var_params['throttle_binding_id']

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

    def list_api_groups_v2_async(self, request):
        """查询分组列表

        查询API分组列表。
        
        如果是租户操作，则查询该租户下所有的分组；如果是管理员权限账号操作，则查询的是所有租户的分组。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListApiGroupsV2
        :type request: :class:`huaweicloudsdkapig.v2.ListApiGroupsV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ListApiGroupsV2Response`
        """
        http_info = self._list_api_groups_v2_http_info(request)
        return self._call_api(**http_info)

    def list_api_groups_v2_async_invoker(self, request):
        http_info = self._list_api_groups_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_api_groups_v2_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/api-groups",
            "request_type": request.__class__.__name__,
            "response_type": "ListApiGroupsV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'precise_search' in local_var_params:
            query_params.append(('precise_search', local_var_params['precise_search']))

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

    def list_api_runtime_definition_v2_async(self, request):
        """查询API运行时定义

        查看指定的API在指定的环境上的运行时定义，默认查询RELEASE环境上的运行时定义。
        
        API的定义分为临时定义和运行时定义，分别代表如下含义：
        - 临时定义：API在编辑中的定义，表示用户最后一次编辑后的API的状态
        - 运行时定义：API在发布到某个环境时，对发布时的API的临时定义进行快照，固化出来的API的状态。
        
        访问某个环境上的API，其实访问的就是其运行时的定义
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListApiRuntimeDefinitionV2
        :type request: :class:`huaweicloudsdkapig.v2.ListApiRuntimeDefinitionV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ListApiRuntimeDefinitionV2Response`
        """
        http_info = self._list_api_runtime_definition_v2_http_info(request)
        return self._call_api(**http_info)

    def list_api_runtime_definition_v2_async_invoker(self, request):
        http_info = self._list_api_runtime_definition_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_api_runtime_definition_v2_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/apis/runtime/{api_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ListApiRuntimeDefinitionV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'api_id' in local_var_params:
            path_params['api_id'] = local_var_params['api_id']

        query_params = []
        if 'env_id' in local_var_params:
            query_params.append(('env_id', local_var_params['env_id']))

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

    def list_api_version_detail_v2_async(self, request):
        """查看版本详情

        查询某个指定的版本详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListApiVersionDetailV2
        :type request: :class:`huaweicloudsdkapig.v2.ListApiVersionDetailV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ListApiVersionDetailV2Response`
        """
        http_info = self._list_api_version_detail_v2_http_info(request)
        return self._call_api(**http_info)

    def list_api_version_detail_v2_async_invoker(self, request):
        http_info = self._list_api_version_detail_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_api_version_detail_v2_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/apis/versions/{version_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ListApiVersionDetailV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
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

    def list_api_versions_v2_async(self, request):
        """查询API历史版本列表

        查询某个API的历史版本。每个API在一个环境上最多存在10个历史版本。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListApiVersionsV2
        :type request: :class:`huaweicloudsdkapig.v2.ListApiVersionsV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ListApiVersionsV2Response`
        """
        http_info = self._list_api_versions_v2_http_info(request)
        return self._call_api(**http_info)

    def list_api_versions_v2_async_invoker(self, request):
        http_info = self._list_api_versions_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_api_versions_v2_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/apis/publish/{api_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ListApiVersionsV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'api_id' in local_var_params:
            path_params['api_id'] = local_var_params['api_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'env_id' in local_var_params:
            query_params.append(('env_id', local_var_params['env_id']))
        if 'env_name' in local_var_params:
            query_params.append(('env_name', local_var_params['env_name']))

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

    def list_apis_binded_to_request_throttling_policy_v2_async(self, request):
        """查看流控策略绑定的API列表

        查询某个流控策略上已经绑定的API列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListApisBindedToRequestThrottlingPolicyV2
        :type request: :class:`huaweicloudsdkapig.v2.ListApisBindedToRequestThrottlingPolicyV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ListApisBindedToRequestThrottlingPolicyV2Response`
        """
        http_info = self._list_apis_binded_to_request_throttling_policy_v2_http_info(request)
        return self._call_api(**http_info)

    def list_apis_binded_to_request_throttling_policy_v2_async_invoker(self, request):
        http_info = self._list_apis_binded_to_request_throttling_policy_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_apis_binded_to_request_throttling_policy_v2_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/throttle-bindings/binded-apis",
            "request_type": request.__class__.__name__,
            "response_type": "ListApisBindedToRequestThrottlingPolicyV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'throttle_id' in local_var_params:
            query_params.append(('throttle_id', local_var_params['throttle_id']))
        if 'env_id' in local_var_params:
            query_params.append(('env_id', local_var_params['env_id']))
        if 'group_id' in local_var_params:
            query_params.append(('group_id', local_var_params['group_id']))
        if 'api_id' in local_var_params:
            query_params.append(('api_id', local_var_params['api_id']))
        if 'api_name' in local_var_params:
            query_params.append(('api_name', local_var_params['api_name']))

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

    def list_apis_unbinded_to_request_throttling_policy_v2_async(self, request):
        """查看流控策略未绑定的API列表

        查询所有未绑定到该流控策略上的自有API列表。需要API已经发布，未发布的API不予展示。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListApisUnbindedToRequestThrottlingPolicyV2
        :type request: :class:`huaweicloudsdkapig.v2.ListApisUnbindedToRequestThrottlingPolicyV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ListApisUnbindedToRequestThrottlingPolicyV2Response`
        """
        http_info = self._list_apis_unbinded_to_request_throttling_policy_v2_http_info(request)
        return self._call_api(**http_info)

    def list_apis_unbinded_to_request_throttling_policy_v2_async_invoker(self, request):
        http_info = self._list_apis_unbinded_to_request_throttling_policy_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_apis_unbinded_to_request_throttling_policy_v2_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/throttle-bindings/unbinded-apis",
            "request_type": request.__class__.__name__,
            "response_type": "ListApisUnbindedToRequestThrottlingPolicyV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'throttle_id' in local_var_params:
            query_params.append(('throttle_id', local_var_params['throttle_id']))
        if 'env_id' in local_var_params:
            query_params.append(('env_id', local_var_params['env_id']))
        if 'group_id' in local_var_params:
            query_params.append(('group_id', local_var_params['group_id']))
        if 'api_id' in local_var_params:
            query_params.append(('api_id', local_var_params['api_id']))
        if 'api_name' in local_var_params:
            query_params.append(('api_name', local_var_params['api_name']))

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

    def list_apis_v2_async(self, request):
        """查询API列表

        查看API列表，返回API详细信息、发布信息等，但不能查看到后端服务信息和API请求参数信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListApisV2
        :type request: :class:`huaweicloudsdkapig.v2.ListApisV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ListApisV2Response`
        """
        http_info = self._list_apis_v2_http_info(request)
        return self._call_api(**http_info)

    def list_apis_v2_async_invoker(self, request):
        http_info = self._list_apis_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_apis_v2_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/apis",
            "request_type": request.__class__.__name__,
            "response_type": "ListApisV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'group_id' in local_var_params:
            query_params.append(('group_id', local_var_params['group_id']))
        if 'req_protocol' in local_var_params:
            query_params.append(('req_protocol', local_var_params['req_protocol']))
        if 'req_method' in local_var_params:
            query_params.append(('req_method', local_var_params['req_method']))
        if 'req_uri' in local_var_params:
            query_params.append(('req_uri', local_var_params['req_uri']))
        if 'auth_type' in local_var_params:
            query_params.append(('auth_type', local_var_params['auth_type']))
        if 'env_id' in local_var_params:
            query_params.append(('env_id', local_var_params['env_id']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'precise_search' in local_var_params:
            query_params.append(('precise_search', local_var_params['precise_search']))
        if 'vpc_channel_name' in local_var_params:
            query_params.append(('vpc_channel_name', local_var_params['vpc_channel_name']))
        if 'return_data_mode' in local_var_params:
            query_params.append(('return_data_mode', local_var_params['return_data_mode']))

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

    def list_request_throttling_policies_binded_to_api_v2_async(self, request):
        """查看API绑定的流控策略列表

        查询某个API绑定的流控策略列表。每个环境上应该最多只有一个流控策略。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListRequestThrottlingPoliciesBindedToApiV2
        :type request: :class:`huaweicloudsdkapig.v2.ListRequestThrottlingPoliciesBindedToApiV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ListRequestThrottlingPoliciesBindedToApiV2Response`
        """
        http_info = self._list_request_throttling_policies_binded_to_api_v2_http_info(request)
        return self._call_api(**http_info)

    def list_request_throttling_policies_binded_to_api_v2_async_invoker(self, request):
        http_info = self._list_request_throttling_policies_binded_to_api_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_request_throttling_policies_binded_to_api_v2_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/throttle-bindings/binded-throttles",
            "request_type": request.__class__.__name__,
            "response_type": "ListRequestThrottlingPoliciesBindedToApiV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'api_id' in local_var_params:
            query_params.append(('api_id', local_var_params['api_id']))
        if 'throttle_id' in local_var_params:
            query_params.append(('throttle_id', local_var_params['throttle_id']))
        if 'throttle_name' in local_var_params:
            query_params.append(('throttle_name', local_var_params['throttle_name']))
        if 'env_id' in local_var_params:
            query_params.append(('env_id', local_var_params['env_id']))

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

    def show_details_of_api_group_v2_async(self, request):
        """查询分组详情

        查询指定分组的详细信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowDetailsOfApiGroupV2
        :type request: :class:`huaweicloudsdkapig.v2.ShowDetailsOfApiGroupV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ShowDetailsOfApiGroupV2Response`
        """
        http_info = self._show_details_of_api_group_v2_http_info(request)
        return self._call_api(**http_info)

    def show_details_of_api_group_v2_async_invoker(self, request):
        http_info = self._show_details_of_api_group_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_details_of_api_group_v2_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/api-groups/{group_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDetailsOfApiGroupV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']

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

    def show_details_of_api_v2_async(self, request):
        """查询API详情

        查看指定的API的详细信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowDetailsOfApiV2
        :type request: :class:`huaweicloudsdkapig.v2.ShowDetailsOfApiV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ShowDetailsOfApiV2Response`
        """
        http_info = self._show_details_of_api_v2_http_info(request)
        return self._call_api(**http_info)

    def show_details_of_api_v2_async_invoker(self, request):
        http_info = self._show_details_of_api_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_details_of_api_v2_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/apis/{api_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDetailsOfApiV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'api_id' in local_var_params:
            path_params['api_id'] = local_var_params['api_id']

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

    def update_api_group_v2_async(self, request):
        """修改API分组

        修改API分组属性。其中name和remark可修改，其他属性不可修改。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateApiGroupV2
        :type request: :class:`huaweicloudsdkapig.v2.UpdateApiGroupV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.UpdateApiGroupV2Response`
        """
        http_info = self._update_api_group_v2_http_info(request)
        return self._call_api(**http_info)

    def update_api_group_v2_async_invoker(self, request):
        http_info = self._update_api_group_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_api_group_v2_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/api-groups/{group_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateApiGroupV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']

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
            ['application/json;charset=UTF-8'])

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

    def update_api_v2_async(self, request):
        """修改API

        修改指定API的信息，包括后端服务信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateApiV2
        :type request: :class:`huaweicloudsdkapig.v2.UpdateApiV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.UpdateApiV2Response`
        """
        http_info = self._update_api_v2_http_info(request)
        return self._call_api(**http_info)

    def update_api_v2_async_invoker(self, request):
        http_info = self._update_api_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_api_v2_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/apis/{api_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateApiV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'api_id' in local_var_params:
            path_params['api_id'] = local_var_params['api_id']

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
            ['application/json;charset=UTF-8'])

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

    def batch_delete_api_acl_binding_v2_async(self, request):
        """批量解除API与ACL策略的绑定

        批量解除API与ACL策略的绑定
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchDeleteApiAclBindingV2
        :type request: :class:`huaweicloudsdkapig.v2.BatchDeleteApiAclBindingV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.BatchDeleteApiAclBindingV2Response`
        """
        http_info = self._batch_delete_api_acl_binding_v2_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_api_acl_binding_v2_async_invoker(self, request):
        http_info = self._batch_delete_api_acl_binding_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_delete_api_acl_binding_v2_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/acl-bindings",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeleteApiAclBindingV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'action' in local_var_params:
            query_params.append(('action', local_var_params['action']))

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

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

    def create_api_acl_binding_v2_async(self, request):
        """将API与ACL策略进行绑定

        将API与ACL策略进行绑定。
        
        同一个API发布到不同的环境可以绑定不同的ACL策略；一个API在发布到特定环境后只能绑定一个同一种类型的ACL策略。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateApiAclBindingV2
        :type request: :class:`huaweicloudsdkapig.v2.CreateApiAclBindingV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.CreateApiAclBindingV2Response`
        """
        http_info = self._create_api_acl_binding_v2_http_info(request)
        return self._call_api(**http_info)

    def create_api_acl_binding_v2_async_invoker(self, request):
        http_info = self._create_api_acl_binding_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_api_acl_binding_v2_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/acl-bindings",
            "request_type": request.__class__.__name__,
            "response_type": "CreateApiAclBindingV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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
            ['application/json;charset=UTF-8'])

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

    def delete_api_acl_binding_v2_async(self, request):
        """解除API与ACL策略的绑定

        解除某条API与ACL策略的绑定关系
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteApiAclBindingV2
        :type request: :class:`huaweicloudsdkapig.v2.DeleteApiAclBindingV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.DeleteApiAclBindingV2Response`
        """
        http_info = self._delete_api_acl_binding_v2_http_info(request)
        return self._call_api(**http_info)

    def delete_api_acl_binding_v2_async_invoker(self, request):
        http_info = self._delete_api_acl_binding_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_api_acl_binding_v2_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/acl-bindings/{acl_bindings_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteApiAclBindingV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'acl_bindings_id' in local_var_params:
            path_params['acl_bindings_id'] = local_var_params['acl_bindings_id']

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

    def list_acl_policy_binded_to_api_v2_async(self, request):
        """查看API绑定的ACL策略列表

        查看API绑定的ACL策略列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAclPolicyBindedToApiV2
        :type request: :class:`huaweicloudsdkapig.v2.ListAclPolicyBindedToApiV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ListAclPolicyBindedToApiV2Response`
        """
        http_info = self._list_acl_policy_binded_to_api_v2_http_info(request)
        return self._call_api(**http_info)

    def list_acl_policy_binded_to_api_v2_async_invoker(self, request):
        http_info = self._list_acl_policy_binded_to_api_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_acl_policy_binded_to_api_v2_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/acl-bindings/binded-acls",
            "request_type": request.__class__.__name__,
            "response_type": "ListAclPolicyBindedToApiV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'api_id' in local_var_params:
            query_params.append(('api_id', local_var_params['api_id']))
        if 'env_id' in local_var_params:
            query_params.append(('env_id', local_var_params['env_id']))
        if 'env_name' in local_var_params:
            query_params.append(('env_name', local_var_params['env_name']))
        if 'acl_id' in local_var_params:
            query_params.append(('acl_id', local_var_params['acl_id']))
        if 'acl_name' in local_var_params:
            query_params.append(('acl_name', local_var_params['acl_name']))

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

    def list_apis_binded_to_acl_policy_v2_async(self, request):
        """查看ACL策略绑定的API列表

        查看ACL策略绑定的API列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListApisBindedToAclPolicyV2
        :type request: :class:`huaweicloudsdkapig.v2.ListApisBindedToAclPolicyV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ListApisBindedToAclPolicyV2Response`
        """
        http_info = self._list_apis_binded_to_acl_policy_v2_http_info(request)
        return self._call_api(**http_info)

    def list_apis_binded_to_acl_policy_v2_async_invoker(self, request):
        http_info = self._list_apis_binded_to_acl_policy_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_apis_binded_to_acl_policy_v2_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/acl-bindings/binded-apis",
            "request_type": request.__class__.__name__,
            "response_type": "ListApisBindedToAclPolicyV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'acl_id' in local_var_params:
            query_params.append(('acl_id', local_var_params['acl_id']))
        if 'api_id' in local_var_params:
            query_params.append(('api_id', local_var_params['api_id']))
        if 'api_name' in local_var_params:
            query_params.append(('api_name', local_var_params['api_name']))
        if 'env_id' in local_var_params:
            query_params.append(('env_id', local_var_params['env_id']))
        if 'group_id' in local_var_params:
            query_params.append(('group_id', local_var_params['group_id']))

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

    def list_apis_unbinded_to_acl_policy_v2_async(self, request):
        """查看ACL策略未绑定的API列表

        查看ACL策略未绑定的API列表，需要API已发布
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListApisUnbindedToAclPolicyV2
        :type request: :class:`huaweicloudsdkapig.v2.ListApisUnbindedToAclPolicyV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ListApisUnbindedToAclPolicyV2Response`
        """
        http_info = self._list_apis_unbinded_to_acl_policy_v2_http_info(request)
        return self._call_api(**http_info)

    def list_apis_unbinded_to_acl_policy_v2_async_invoker(self, request):
        http_info = self._list_apis_unbinded_to_acl_policy_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_apis_unbinded_to_acl_policy_v2_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/acl-bindings/unbinded-apis",
            "request_type": request.__class__.__name__,
            "response_type": "ListApisUnbindedToAclPolicyV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'acl_id' in local_var_params:
            query_params.append(('acl_id', local_var_params['acl_id']))
        if 'api_id' in local_var_params:
            query_params.append(('api_id', local_var_params['api_id']))
        if 'api_name' in local_var_params:
            query_params.append(('api_name', local_var_params['api_name']))
        if 'env_id' in local_var_params:
            query_params.append(('env_id', local_var_params['env_id']))
        if 'group_id' in local_var_params:
            query_params.append(('group_id', local_var_params['group_id']))

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

    def canceling_authorization_v2_async(self, request):
        """解除授权

        解除API对APP的授权关系。解除授权后，APP将不再能够调用该API。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CancelingAuthorizationV2
        :type request: :class:`huaweicloudsdkapig.v2.CancelingAuthorizationV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.CancelingAuthorizationV2Response`
        """
        http_info = self._canceling_authorization_v2_http_info(request)
        return self._call_api(**http_info)

    def canceling_authorization_v2_async_invoker(self, request):
        http_info = self._canceling_authorization_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _canceling_authorization_v2_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/app-auths/{app_auth_id}",
            "request_type": request.__class__.__name__,
            "response_type": "CancelingAuthorizationV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'app_auth_id' in local_var_params:
            path_params['app_auth_id'] = local_var_params['app_auth_id']

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

    def create_authorizing_apps_v2_async(self, request):
        """APP授权

        APP创建成功后，还不能访问API，如果想要访问某个环境上的API，需要将该API在该环境上授权给APP。授权成功后，APP即可访问该环境上的这个API。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateAuthorizingAppsV2
        :type request: :class:`huaweicloudsdkapig.v2.CreateAuthorizingAppsV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.CreateAuthorizingAppsV2Response`
        """
        http_info = self._create_authorizing_apps_v2_http_info(request)
        return self._call_api(**http_info)

    def create_authorizing_apps_v2_async_invoker(self, request):
        http_info = self._create_authorizing_apps_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_authorizing_apps_v2_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/app-auths",
            "request_type": request.__class__.__name__,
            "response_type": "CreateAuthorizingAppsV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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
            ['application/json;charset=UTF-8'])

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

    def list_apis_binded_to_app_v2_async(self, request):
        """查看APP已绑定的API列表

        查询APP已经绑定的API列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListApisBindedToAppV2
        :type request: :class:`huaweicloudsdkapig.v2.ListApisBindedToAppV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ListApisBindedToAppV2Response`
        """
        http_info = self._list_apis_binded_to_app_v2_http_info(request)
        return self._call_api(**http_info)

    def list_apis_binded_to_app_v2_async_invoker(self, request):
        http_info = self._list_apis_binded_to_app_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_apis_binded_to_app_v2_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/app-auths/binded-apis",
            "request_type": request.__class__.__name__,
            "response_type": "ListApisBindedToAppV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'app_id' in local_var_params:
            query_params.append(('app_id', local_var_params['app_id']))
        if 'api_id' in local_var_params:
            query_params.append(('api_id', local_var_params['api_id']))
        if 'api_name' in local_var_params:
            query_params.append(('api_name', local_var_params['api_name']))
        if 'group_id' in local_var_params:
            query_params.append(('group_id', local_var_params['group_id']))
        if 'group_name' in local_var_params:
            query_params.append(('group_name', local_var_params['group_name']))
        if 'env_id' in local_var_params:
            query_params.append(('env_id', local_var_params['env_id']))

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

    def list_apis_unbinded_to_app_v2_async(self, request):
        """查看APP未绑定的API列表

        查询指定环境上某个APP未绑定的API列表[，包括自有API和从云商店购买的API](tag:hws)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListApisUnbindedToAppV2
        :type request: :class:`huaweicloudsdkapig.v2.ListApisUnbindedToAppV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ListApisUnbindedToAppV2Response`
        """
        http_info = self._list_apis_unbinded_to_app_v2_http_info(request)
        return self._call_api(**http_info)

    def list_apis_unbinded_to_app_v2_async_invoker(self, request):
        http_info = self._list_apis_unbinded_to_app_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_apis_unbinded_to_app_v2_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/app-auths/unbinded-apis",
            "request_type": request.__class__.__name__,
            "response_type": "ListApisUnbindedToAppV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'app_id' in local_var_params:
            query_params.append(('app_id', local_var_params['app_id']))
        if 'env_id' in local_var_params:
            query_params.append(('env_id', local_var_params['env_id']))
        if 'group_id' in local_var_params:
            query_params.append(('group_id', local_var_params['group_id']))
        if 'api_id' in local_var_params:
            query_params.append(('api_id', local_var_params['api_id']))
        if 'api_name' in local_var_params:
            query_params.append(('api_name', local_var_params['api_name']))

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

    def list_apps_binded_to_api_v2_async(self, request):
        """查看API已绑定的APP列表

        查询API绑定的APP列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAppsBindedToApiV2
        :type request: :class:`huaweicloudsdkapig.v2.ListAppsBindedToApiV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ListAppsBindedToApiV2Response`
        """
        http_info = self._list_apps_binded_to_api_v2_http_info(request)
        return self._call_api(**http_info)

    def list_apps_binded_to_api_v2_async_invoker(self, request):
        http_info = self._list_apps_binded_to_api_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_apps_binded_to_api_v2_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/app-auths/binded-apps",
            "request_type": request.__class__.__name__,
            "response_type": "ListAppsBindedToApiV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'api_id' in local_var_params:
            query_params.append(('api_id', local_var_params['api_id']))
        if 'app_name' in local_var_params:
            query_params.append(('app_name', local_var_params['app_name']))
        if 'app_id' in local_var_params:
            query_params.append(('app_id', local_var_params['app_id']))
        if 'env_id' in local_var_params:
            query_params.append(('env_id', local_var_params['env_id']))

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

    def export_api_definitions_v2_async(self, request):
        """导出API

        导出分组下API的定义信息。导出文件内容符合swagger标准规范，API网关自定义扩展字段请参考《API网关开发指南》的“导入导出API：扩展定义”章节。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ExportApiDefinitionsV2
        :type request: :class:`huaweicloudsdkapig.v2.ExportApiDefinitionsV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ExportApiDefinitionsV2Response`
        """
        http_info = self._export_api_definitions_v2_http_info(request)
        return self._call_api(**http_info)

    def export_api_definitions_v2_async_invoker(self, request):
        http_info = self._export_api_definitions_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _export_api_definitions_v2_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/openapi/export",
            "request_type": request.__class__.__name__,
            "response_type": "ExportApiDefinitionsV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'oas_version' in local_var_params:
            query_params.append(('oas_version', local_var_params['oas_version']))

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

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

    def import_api_definitions_v2_async(self, request):
        """导入API

        导入API。导入文件内容需要符合swagger标准规范，API网关自定义扩展字段请参考《API网关开发指南》的“导入导出API：扩展定义”章节。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ImportApiDefinitionsV2
        :type request: :class:`huaweicloudsdkapig.v2.ImportApiDefinitionsV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ImportApiDefinitionsV2Response`
        """
        http_info = self._import_api_definitions_v2_http_info(request)
        return self._call_api(**http_info)

    def import_api_definitions_v2_async_invoker(self, request):
        http_info = self._import_api_definitions_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _import_api_definitions_v2_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/openapi/import",
            "request_type": request.__class__.__name__,
            "response_type": "ImportApiDefinitionsV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}

        form_params = {}
        if 'is_create_group' in local_var_params:
            form_params['is_create_group'] = local_var_params['is_create_group']
        if 'group_id' in local_var_params:
            form_params['group_id'] = local_var_params['group_id']
        if 'extend_mode' in local_var_params:
            form_params['extend_mode'] = local_var_params['extend_mode']
        if 'simple_mode' in local_var_params:
            form_params['simple_mode'] = local_var_params['simple_mode']
        if 'mock_mode' in local_var_params:
            form_params['mock_mode'] = local_var_params['mock_mode']
        if 'api_mode' in local_var_params:
            form_params['api_mode'] = local_var_params['api_mode']
        if 'file_name' in local_var_params:
            form_params['file_name'] = local_var_params['file_name']

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

    def batch_associate_certs_v2_async(self, request):
        """域名绑定SSL证书

        域名绑定SSL证书。目前暂时仅支持单个绑定，请求体当中的certificate_ids里面有且只能有一个证书ID。使用实例自定义入方向端口的特性时，相同的域名会同时绑定证书，注意开启/关闭客户端校验会对相同域名的不同端口同时生效。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchAssociateCertsV2
        :type request: :class:`huaweicloudsdkapig.v2.BatchAssociateCertsV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.BatchAssociateCertsV2Response`
        """
        http_info = self._batch_associate_certs_v2_http_info(request)
        return self._call_api(**http_info)

    def batch_associate_certs_v2_async_invoker(self, request):
        http_info = self._batch_associate_certs_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_associate_certs_v2_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/api-groups/{group_id}/domains/{domain_id}/certificates/attach",
            "request_type": request.__class__.__name__,
            "response_type": "BatchAssociateCertsV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']

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
            ['application/json;charset=UTF-8'])

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

    def batch_associate_domains_v2_async(self, request):
        """SSL证书绑定域名

        SSL证书绑定域名。使用实例自定义入方向端口的特性时，相同的域名会同时绑定证书，注意开启/关闭客户端校验会对相同域名的不同端口同时生效。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchAssociateDomainsV2
        :type request: :class:`huaweicloudsdkapig.v2.BatchAssociateDomainsV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.BatchAssociateDomainsV2Response`
        """
        http_info = self._batch_associate_domains_v2_http_info(request)
        return self._call_api(**http_info)

    def batch_associate_domains_v2_async_invoker(self, request):
        http_info = self._batch_associate_domains_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_associate_domains_v2_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/apigw/certificates/{certificate_id}/domains/attach",
            "request_type": request.__class__.__name__,
            "response_type": "BatchAssociateDomainsV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'certificate_id' in local_var_params:
            path_params['certificate_id'] = local_var_params['certificate_id']

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
            ['application/json;charset=UTF-8'])

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

    def batch_disassociate_certs_v2_async(self, request):
        """域名解绑SSL证书

        域名解绑SSL证书。目前暂时仅支持单个解绑，请求体当中的certificate_ids里面有且只能有一个证书ID。在使用自定义入方向端口的特性时，相同的域名会同时解绑证书。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchDisassociateCertsV2
        :type request: :class:`huaweicloudsdkapig.v2.BatchDisassociateCertsV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.BatchDisassociateCertsV2Response`
        """
        http_info = self._batch_disassociate_certs_v2_http_info(request)
        return self._call_api(**http_info)

    def batch_disassociate_certs_v2_async_invoker(self, request):
        http_info = self._batch_disassociate_certs_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_disassociate_certs_v2_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/api-groups/{group_id}/domains/{domain_id}/certificates/detach",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDisassociateCertsV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']

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
            ['application/json;charset=UTF-8'])

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

    def batch_disassociate_domains_v2_async(self, request):
        """SSL证书解绑域名

        SSL证书解绑域名。在使用自定义入方向端口的特性时，相同的域名会同时解绑证书。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchDisassociateDomainsV2
        :type request: :class:`huaweicloudsdkapig.v2.BatchDisassociateDomainsV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.BatchDisassociateDomainsV2Response`
        """
        http_info = self._batch_disassociate_domains_v2_http_info(request)
        return self._call_api(**http_info)

    def batch_disassociate_domains_v2_async_invoker(self, request):
        http_info = self._batch_disassociate_domains_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_disassociate_domains_v2_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/apigw/certificates/{certificate_id}/domains/detach",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDisassociateDomainsV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'certificate_id' in local_var_params:
            path_params['certificate_id'] = local_var_params['certificate_id']

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
            ['application/json;charset=UTF-8'])

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

    def create_certificate_v2_async(self, request):
        """创建SSL证书

        创建SSL证书。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateCertificateV2
        :type request: :class:`huaweicloudsdkapig.v2.CreateCertificateV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.CreateCertificateV2Response`
        """
        http_info = self._create_certificate_v2_http_info(request)
        return self._call_api(**http_info)

    def create_certificate_v2_async_invoker(self, request):
        http_info = self._create_certificate_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_certificate_v2_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/apigw/certificates",
            "request_type": request.__class__.__name__,
            "response_type": "CreateCertificateV2Response"
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
            ['application/json;charset=UTF-8'])

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

    def delete_certificate_v2_async(self, request):
        """删除SSL证书

        删除ssl证书接口，删除时只有没有关联域名的证书才能被删除。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteCertificateV2
        :type request: :class:`huaweicloudsdkapig.v2.DeleteCertificateV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.DeleteCertificateV2Response`
        """
        http_info = self._delete_certificate_v2_http_info(request)
        return self._call_api(**http_info)

    def delete_certificate_v2_async_invoker(self, request):
        http_info = self._delete_certificate_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_certificate_v2_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/apigw/certificates/{certificate_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteCertificateV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'certificate_id' in local_var_params:
            path_params['certificate_id'] = local_var_params['certificate_id']

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

    def list_attached_domains_v2_async(self, request):
        """获取SSL证书已绑定域名列表

        获取SSL证书已绑定域名列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAttachedDomainsV2
        :type request: :class:`huaweicloudsdkapig.v2.ListAttachedDomainsV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ListAttachedDomainsV2Response`
        """
        http_info = self._list_attached_domains_v2_http_info(request)
        return self._call_api(**http_info)

    def list_attached_domains_v2_async_invoker(self, request):
        http_info = self._list_attached_domains_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_attached_domains_v2_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/apigw/certificates/{certificate_id}/attached-domains",
            "request_type": request.__class__.__name__,
            "response_type": "ListAttachedDomainsV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'certificate_id' in local_var_params:
            path_params['certificate_id'] = local_var_params['certificate_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'url_domain' in local_var_params:
            query_params.append(('url_domain', local_var_params['url_domain']))

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

    def list_certificates_v2_async(self, request):
        """获取SSL证书列表

        获取SSL证书列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListCertificatesV2
        :type request: :class:`huaweicloudsdkapig.v2.ListCertificatesV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ListCertificatesV2Response`
        """
        http_info = self._list_certificates_v2_http_info(request)
        return self._call_api(**http_info)

    def list_certificates_v2_async_invoker(self, request):
        http_info = self._list_certificates_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_certificates_v2_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/apigw/certificates",
            "request_type": request.__class__.__name__,
            "response_type": "ListCertificatesV2Response"
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
        if 'common_name' in local_var_params:
            query_params.append(('common_name', local_var_params['common_name']))
        if 'signature_algorithm' in local_var_params:
            query_params.append(('signature_algorithm', local_var_params['signature_algorithm']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'instance_id' in local_var_params:
            query_params.append(('instance_id', local_var_params['instance_id']))

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

    def show_details_of_certificate_v2_async(self, request):
        """查看证书详情

        查看证书详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowDetailsOfCertificateV2
        :type request: :class:`huaweicloudsdkapig.v2.ShowDetailsOfCertificateV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ShowDetailsOfCertificateV2Response`
        """
        http_info = self._show_details_of_certificate_v2_http_info(request)
        return self._call_api(**http_info)

    def show_details_of_certificate_v2_async_invoker(self, request):
        http_info = self._show_details_of_certificate_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_details_of_certificate_v2_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/apigw/certificates/{certificate_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDetailsOfCertificateV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'certificate_id' in local_var_params:
            path_params['certificate_id'] = local_var_params['certificate_id']

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

    def update_certificate_v2_async(self, request):
        """修改SSL证书

        修改SSL证书。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateCertificateV2
        :type request: :class:`huaweicloudsdkapig.v2.UpdateCertificateV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.UpdateCertificateV2Response`
        """
        http_info = self._update_certificate_v2_http_info(request)
        return self._call_api(**http_info)

    def update_certificate_v2_async_invoker(self, request):
        http_info = self._update_certificate_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_certificate_v2_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/apigw/certificates/{certificate_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateCertificateV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'certificate_id' in local_var_params:
            path_params['certificate_id'] = local_var_params['certificate_id']

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
            ['application/json;charset=UTF-8'])

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

    def adding_backend_instances_v2_async(self, request):
        """添加或更新后端实例

        为指定的VPC通道添加后端实例
        
        若指定地址的后端实例已存在，则更新对应后端实例信息。若请求体中包含多个重复地址的后端实例定义，则使用第一个定义。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AddingBackendInstancesV2
        :type request: :class:`huaweicloudsdkapig.v2.AddingBackendInstancesV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.AddingBackendInstancesV2Response`
        """
        http_info = self._adding_backend_instances_v2_http_info(request)
        return self._call_api(**http_info)

    def adding_backend_instances_v2_async_invoker(self, request):
        http_info = self._adding_backend_instances_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _adding_backend_instances_v2_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/vpc-channels/{vpc_channel_id}/members",
            "request_type": request.__class__.__name__,
            "response_type": "AddingBackendInstancesV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'vpc_channel_id' in local_var_params:
            path_params['vpc_channel_id'] = local_var_params['vpc_channel_id']

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
            ['application/json;charset=UTF-8'])

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

    def batch_disable_members_async(self, request):
        """批量修改后端服务器状态不可用

        批量修改后端服务器状态不可用。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchDisableMembers
        :type request: :class:`huaweicloudsdkapig.v2.BatchDisableMembersRequest`
        :rtype: :class:`huaweicloudsdkapig.v2.BatchDisableMembersResponse`
        """
        http_info = self._batch_disable_members_http_info(request)
        return self._call_api(**http_info)

    def batch_disable_members_async_invoker(self, request):
        http_info = self._batch_disable_members_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_disable_members_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/vpc-channels/{vpc_channel_id}/members/batch-disable",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDisableMembersResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'vpc_channel_id' in local_var_params:
            path_params['vpc_channel_id'] = local_var_params['vpc_channel_id']

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
            ['application/json;charset=UTF-8'])

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

    def batch_enable_members_async(self, request):
        """批量修改后端服务器状态可用

        批量修改后端服务器状态可用。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchEnableMembers
        :type request: :class:`huaweicloudsdkapig.v2.BatchEnableMembersRequest`
        :rtype: :class:`huaweicloudsdkapig.v2.BatchEnableMembersResponse`
        """
        http_info = self._batch_enable_members_http_info(request)
        return self._call_api(**http_info)

    def batch_enable_members_async_invoker(self, request):
        http_info = self._batch_enable_members_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_enable_members_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/vpc-channels/{vpc_channel_id}/members/batch-enable",
            "request_type": request.__class__.__name__,
            "response_type": "BatchEnableMembersResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'vpc_channel_id' in local_var_params:
            path_params['vpc_channel_id'] = local_var_params['vpc_channel_id']

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
            ['application/json;charset=UTF-8'])

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

    def create_member_group_async(self, request):
        """添加或更新VPC通道后端服务器组

        在APIG中创建VPC通道后端服务器组，VPC通道后端实例可以选择是否关联后端实例服务器组，以便管理后端服务器节点。
        
        若指定名称的后端服务器组已存在，则更新对应后端服务器组信息。若请求体中包含多个重复名称的后端服务器定义，则使用第一个定义。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateMemberGroup
        :type request: :class:`huaweicloudsdkapig.v2.CreateMemberGroupRequest`
        :rtype: :class:`huaweicloudsdkapig.v2.CreateMemberGroupResponse`
        """
        http_info = self._create_member_group_http_info(request)
        return self._call_api(**http_info)

    def create_member_group_async_invoker(self, request):
        http_info = self._create_member_group_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_member_group_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/vpc-channels/{vpc_channel_id}/member-groups",
            "request_type": request.__class__.__name__,
            "response_type": "CreateMemberGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'vpc_channel_id' in local_var_params:
            path_params['vpc_channel_id'] = local_var_params['vpc_channel_id']

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
            ['application/json;charset=UTF-8'])

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

    def create_vpc_channel_v2_async(self, request):
        """创建VPC通道

        在API网关中创建连接私有VPC资源的通道，并在创建API时将后端节点配置为使用这些VPC通道，以便API网关直接访问私有VPC资源。
        &gt; 每个用户最多创建30个VPC通道。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateVpcChannelV2
        :type request: :class:`huaweicloudsdkapig.v2.CreateVpcChannelV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.CreateVpcChannelV2Response`
        """
        http_info = self._create_vpc_channel_v2_http_info(request)
        return self._call_api(**http_info)

    def create_vpc_channel_v2_async_invoker(self, request):
        http_info = self._create_vpc_channel_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_vpc_channel_v2_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/vpc-channels",
            "request_type": request.__class__.__name__,
            "response_type": "CreateVpcChannelV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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
            ['application/json;charset=UTF-8'])

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

    def delete_backend_instance_v2_async(self, request):
        """删除后端实例

        删除指定VPC通道中的后端实例
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteBackendInstanceV2
        :type request: :class:`huaweicloudsdkapig.v2.DeleteBackendInstanceV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.DeleteBackendInstanceV2Response`
        """
        http_info = self._delete_backend_instance_v2_http_info(request)
        return self._call_api(**http_info)

    def delete_backend_instance_v2_async_invoker(self, request):
        http_info = self._delete_backend_instance_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_backend_instance_v2_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/vpc-channels/{vpc_channel_id}/members/{member_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteBackendInstanceV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'vpc_channel_id' in local_var_params:
            path_params['vpc_channel_id'] = local_var_params['vpc_channel_id']
        if 'member_id' in local_var_params:
            path_params['member_id'] = local_var_params['member_id']

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

    def delete_member_group_async(self, request):
        """删除VPC通道后端服务器组

        删除指定的VPC通道后端服务器组
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteMemberGroup
        :type request: :class:`huaweicloudsdkapig.v2.DeleteMemberGroupRequest`
        :rtype: :class:`huaweicloudsdkapig.v2.DeleteMemberGroupResponse`
        """
        http_info = self._delete_member_group_http_info(request)
        return self._call_api(**http_info)

    def delete_member_group_async_invoker(self, request):
        http_info = self._delete_member_group_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_member_group_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/vpc-channels/{vpc_channel_id}/member-groups/{member_group_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteMemberGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'vpc_channel_id' in local_var_params:
            path_params['vpc_channel_id'] = local_var_params['vpc_channel_id']
        if 'member_group_id' in local_var_params:
            path_params['member_group_id'] = local_var_params['member_group_id']

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

    def delete_vpc_channel_v2_async(self, request):
        """删除VPC通道

        删除指定的VPC通道
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteVpcChannelV2
        :type request: :class:`huaweicloudsdkapig.v2.DeleteVpcChannelV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.DeleteVpcChannelV2Response`
        """
        http_info = self._delete_vpc_channel_v2_http_info(request)
        return self._call_api(**http_info)

    def delete_vpc_channel_v2_async_invoker(self, request):
        http_info = self._delete_vpc_channel_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_vpc_channel_v2_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/vpc-channels/{vpc_channel_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteVpcChannelV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'vpc_channel_id' in local_var_params:
            path_params['vpc_channel_id'] = local_var_params['vpc_channel_id']

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

    def list_backend_instances_v2_async(self, request):
        """查看后端实例列表

        查看指定VPC通道的后端实例列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListBackendInstancesV2
        :type request: :class:`huaweicloudsdkapig.v2.ListBackendInstancesV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ListBackendInstancesV2Response`
        """
        http_info = self._list_backend_instances_v2_http_info(request)
        return self._call_api(**http_info)

    def list_backend_instances_v2_async_invoker(self, request):
        http_info = self._list_backend_instances_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_backend_instances_v2_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/vpc-channels/{vpc_channel_id}/members",
            "request_type": request.__class__.__name__,
            "response_type": "ListBackendInstancesV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'vpc_channel_id' in local_var_params:
            path_params['vpc_channel_id'] = local_var_params['vpc_channel_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'member_group_name' in local_var_params:
            query_params.append(('member_group_name', local_var_params['member_group_name']))
        if 'member_group_id' in local_var_params:
            query_params.append(('member_group_id', local_var_params['member_group_id']))
        if 'precise_search' in local_var_params:
            query_params.append(('precise_search', local_var_params['precise_search']))

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

    def list_member_groups_async(self, request):
        """查询VPC通道后端云服务组列表

        查询VPC通道后端云服务组列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListMemberGroups
        :type request: :class:`huaweicloudsdkapig.v2.ListMemberGroupsRequest`
        :rtype: :class:`huaweicloudsdkapig.v2.ListMemberGroupsResponse`
        """
        http_info = self._list_member_groups_http_info(request)
        return self._call_api(**http_info)

    def list_member_groups_async_invoker(self, request):
        http_info = self._list_member_groups_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_member_groups_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/vpc-channels/{vpc_channel_id}/member-groups",
            "request_type": request.__class__.__name__,
            "response_type": "ListMemberGroupsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'vpc_channel_id' in local_var_params:
            path_params['vpc_channel_id'] = local_var_params['vpc_channel_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'dict_code' in local_var_params:
            query_params.append(('dict_code', local_var_params['dict_code']))
        if 'member_group_name' in local_var_params:
            query_params.append(('member_group_name', local_var_params['member_group_name']))
        if 'precise_search' in local_var_params:
            query_params.append(('precise_search', local_var_params['precise_search']))

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

    def list_vpc_channels_v2_async(self, request):
        """查询VPC通道列表

        查看VPC通道列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListVpcChannelsV2
        :type request: :class:`huaweicloudsdkapig.v2.ListVpcChannelsV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ListVpcChannelsV2Response`
        """
        http_info = self._list_vpc_channels_v2_http_info(request)
        return self._call_api(**http_info)

    def list_vpc_channels_v2_async_invoker(self, request):
        http_info = self._list_vpc_channels_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_vpc_channels_v2_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/vpc-channels",
            "request_type": request.__class__.__name__,
            "response_type": "ListVpcChannelsV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'dict_code' in local_var_params:
            query_params.append(('dict_code', local_var_params['dict_code']))
        if 'precise_search' in local_var_params:
            query_params.append(('precise_search', local_var_params['precise_search']))
        if 'member_host' in local_var_params:
            query_params.append(('member_host', local_var_params['member_host']))
        if 'member_port' in local_var_params:
            query_params.append(('member_port', local_var_params['member_port']))
        if 'member_group_name' in local_var_params:
            query_params.append(('member_group_name', local_var_params['member_group_name']))
        if 'member_group_id' in local_var_params:
            query_params.append(('member_group_id', local_var_params['member_group_id']))

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

    def show_details_of_member_group_async(self, request):
        """查看VPC通道后端服务器组详情

        查看指定的VPC通道后端服务器组详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowDetailsOfMemberGroup
        :type request: :class:`huaweicloudsdkapig.v2.ShowDetailsOfMemberGroupRequest`
        :rtype: :class:`huaweicloudsdkapig.v2.ShowDetailsOfMemberGroupResponse`
        """
        http_info = self._show_details_of_member_group_http_info(request)
        return self._call_api(**http_info)

    def show_details_of_member_group_async_invoker(self, request):
        http_info = self._show_details_of_member_group_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_details_of_member_group_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/vpc-channels/{vpc_channel_id}/member-groups/{member_group_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDetailsOfMemberGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'vpc_channel_id' in local_var_params:
            path_params['vpc_channel_id'] = local_var_params['vpc_channel_id']
        if 'member_group_id' in local_var_params:
            path_params['member_group_id'] = local_var_params['member_group_id']

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

    def show_details_of_vpc_channel_v2_async(self, request):
        """查看VPC通道详情

        查看指定的VPC通道详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowDetailsOfVpcChannelV2
        :type request: :class:`huaweicloudsdkapig.v2.ShowDetailsOfVpcChannelV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.ShowDetailsOfVpcChannelV2Response`
        """
        http_info = self._show_details_of_vpc_channel_v2_http_info(request)
        return self._call_api(**http_info)

    def show_details_of_vpc_channel_v2_async_invoker(self, request):
        http_info = self._show_details_of_vpc_channel_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_details_of_vpc_channel_v2_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/vpc-channels/{vpc_channel_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDetailsOfVpcChannelV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'vpc_channel_id' in local_var_params:
            path_params['vpc_channel_id'] = local_var_params['vpc_channel_id']

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

    def update_backend_instances_v2_async(self, request):
        """更新后端实例

        更新指定的VPC通道的后端实例。更新时，使用传入的请求参数对对应云服务组的后端实例进行全量覆盖修改。若未指定修改的云服务器组，则进行全量覆盖。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateBackendInstancesV2
        :type request: :class:`huaweicloudsdkapig.v2.UpdateBackendInstancesV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.UpdateBackendInstancesV2Response`
        """
        http_info = self._update_backend_instances_v2_http_info(request)
        return self._call_api(**http_info)

    def update_backend_instances_v2_async_invoker(self, request):
        http_info = self._update_backend_instances_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_backend_instances_v2_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/vpc-channels/{vpc_channel_id}/members",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateBackendInstancesV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'vpc_channel_id' in local_var_params:
            path_params['vpc_channel_id'] = local_var_params['vpc_channel_id']

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
            ['application/json;charset=UTF-8'])

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

    def update_health_check_async(self, request):
        """修改VPC通道健康检查

        修改VPC通道健康检查。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateHealthCheck
        :type request: :class:`huaweicloudsdkapig.v2.UpdateHealthCheckRequest`
        :rtype: :class:`huaweicloudsdkapig.v2.UpdateHealthCheckResponse`
        """
        http_info = self._update_health_check_http_info(request)
        return self._call_api(**http_info)

    def update_health_check_async_invoker(self, request):
        http_info = self._update_health_check_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_health_check_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/vpc-channels/{vpc_channel_id}/health-config",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateHealthCheckResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'vpc_channel_id' in local_var_params:
            path_params['vpc_channel_id'] = local_var_params['vpc_channel_id']

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
            ['application/json;charset=UTF-8'])

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

    def update_member_group_async(self, request):
        """更新VPC通道后端服务器组

        更新指定VPC通道后端服务器组
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateMemberGroup
        :type request: :class:`huaweicloudsdkapig.v2.UpdateMemberGroupRequest`
        :rtype: :class:`huaweicloudsdkapig.v2.UpdateMemberGroupResponse`
        """
        http_info = self._update_member_group_http_info(request)
        return self._call_api(**http_info)

    def update_member_group_async_invoker(self, request):
        http_info = self._update_member_group_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_member_group_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/vpc-channels/{vpc_channel_id}/member-groups/{member_group_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateMemberGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'vpc_channel_id' in local_var_params:
            path_params['vpc_channel_id'] = local_var_params['vpc_channel_id']
        if 'member_group_id' in local_var_params:
            path_params['member_group_id'] = local_var_params['member_group_id']

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
            ['application/json;charset=UTF-8'])

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

    def update_vpc_channel_v2_async(self, request):
        """更新VPC通道

        更新指定VPC通道的参数
        
        使用传入的后端实例列表对VPC通道进行全量覆盖，若后端实例列表为空，则会全量删除已有的后端实例；
        
        使用传入的后端服务器组列表对VPC通道进行全量覆盖，若后端服务器组列表为空，则会全量删除已有的服务器组；
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateVpcChannelV2
        :type request: :class:`huaweicloudsdkapig.v2.UpdateVpcChannelV2Request`
        :rtype: :class:`huaweicloudsdkapig.v2.UpdateVpcChannelV2Response`
        """
        http_info = self._update_vpc_channel_v2_http_info(request)
        return self._call_api(**http_info)

    def update_vpc_channel_v2_async_invoker(self, request):
        http_info = self._update_vpc_channel_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_vpc_channel_v2_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/apigw/instances/{instance_id}/vpc-channels/{vpc_channel_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateVpcChannelV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'vpc_channel_id' in local_var_params:
            path_params['vpc_channel_id'] = local_var_params['vpc_channel_id']

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
            ['application/json;charset=UTF-8'])

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

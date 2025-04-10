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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkroma'")


class RomaAsyncClient(Client):
    def __init__(self):
        super(RomaAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkroma.v2.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "RomaAsyncClient":
                raise TypeError("client type error, support client type is RomaAsyncClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def add_subsets_to_gateway_async(self, request):
        r"""添加子设备到网关

        添加子设备到网关
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AddSubsetsToGateway
        :type request: :class:`huaweicloudsdkroma.v2.AddSubsetsToGatewayRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.AddSubsetsToGatewayResponse`
        """
        http_info = self._add_subsets_to_gateway_http_info(request)
        return self._call_api(**http_info)

    def add_subsets_to_gateway_async_invoker(self, request):
        http_info = self._add_subsets_to_gateway_http_info(request)
        return AsyncInvoker(self, http_info)

    def _add_subsets_to_gateway_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/link/instances/{instance_id}/devices/{device_id}/subsets",
            "request_type": request.__class__.__name__,
            "response_type": "AddSubsetsToGatewayResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'device_id' in local_var_params:
            path_params['device_id'] = local_var_params['device_id']

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
        r"""客户端配额绑定客户端应用列表

        客户端配额绑定客户端应用列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AssociateAppsForAppQuota
        :type request: :class:`huaweicloudsdkroma.v2.AssociateAppsForAppQuotaRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.AssociateAppsForAppQuotaResponse`
        """
        http_info = self._associate_apps_for_app_quota_http_info(request)
        return self._call_api(**http_info)

    def associate_apps_for_app_quota_async_invoker(self, request):
        http_info = self._associate_apps_for_app_quota_http_info(request)
        return AsyncInvoker(self, http_info)

    def _associate_apps_for_app_quota_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/app-quotas/{app_quota_id}/binding-apps",
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
        r"""绑定域名证书

        如果创建API时，“定义API请求”使用HTTPS请求协议，那么在独立域名中需要添加SSL证书。
        本章节主要介绍为特定域名绑定证书。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AssociateCertificateV2
        :type request: :class:`huaweicloudsdkroma.v2.AssociateCertificateV2Request`
        :rtype: :class:`huaweicloudsdkroma.v2.AssociateCertificateV2Response`
        """
        http_info = self._associate_certificate_v2_http_info(request)
        return self._call_api(**http_info)

    def associate_certificate_v2_async_invoker(self, request):
        http_info = self._associate_certificate_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _associate_certificate_v2_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/api-groups/{group_id}/domains/{domain_id}/certificate",
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
        r"""绑定域名

        用户自定义的域名，需要CNAME到API分组的子域名上才能生效。
        每个API分组下最多可绑定5个域名。绑定域名后，用户可通过自定义域名调用API。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AssociateDomainV2
        :type request: :class:`huaweicloudsdkroma.v2.AssociateDomainV2Request`
        :rtype: :class:`huaweicloudsdkroma.v2.AssociateDomainV2Response`
        """
        http_info = self._associate_domain_v2_http_info(request)
        return self._call_api(**http_info)

    def associate_domain_v2_async_invoker(self, request):
        http_info = self._associate_domain_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _associate_domain_v2_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/api-groups/{group_id}/domains",
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
        r"""绑定签名密钥

        签名密钥创建后，需要绑定到API才能生效。
        
        
        将签名密钥绑定到API后，则服务集成请求后端服务时就会使用这个签名密钥进行加密签名，后端服务可以校验这个签名来验证请求来源。
        
        
        将指定的签名密钥绑定到一个或多个已发布的API上。同一个API发布到不同的环境可以绑定不同的签名密钥；一个API在发布到特定环境后只能绑定一个签名密钥。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AssociateSignatureKeyV2
        :type request: :class:`huaweicloudsdkroma.v2.AssociateSignatureKeyV2Request`
        :rtype: :class:`huaweicloudsdkroma.v2.AssociateSignatureKeyV2Response`
        """
        http_info = self._associate_signature_key_v2_http_info(request)
        return self._call_api(**http_info)

    def associate_signature_key_v2_async_invoker(self, request):
        http_info = self._associate_signature_key_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _associate_signature_key_v2_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/sign-bindings",
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
        r"""插件绑定API

        绑定插件到API上。
        - 只能选择发布状态的API
        - 绑定以后及时生效
        - 修改插件后及时生效
        - 相同类型的插件只能绑定一个，原来已经绑定的同类型插件，会直接覆盖。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AttachApiToPlugin
        :type request: :class:`huaweicloudsdkroma.v2.AttachApiToPluginRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.AttachApiToPluginResponse`
        """
        http_info = self._attach_api_to_plugin_http_info(request)
        return self._call_api(**http_info)

    def attach_api_to_plugin_async_invoker(self, request):
        http_info = self._attach_api_to_plugin_http_info(request)
        return AsyncInvoker(self, http_info)

    def _attach_api_to_plugin_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/plugins/{plugin_id}/attach",
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
        r"""API绑定插件

        绑定插件到API上。
        - 只能选择发布状态的API
        - 绑定以后及时生效
        - 修改插件后及时生效
        - 相同类型的插件只能绑定一个，原来已经绑定的同类型插件，会直接覆盖。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AttachPluginToApi
        :type request: :class:`huaweicloudsdkroma.v2.AttachPluginToApiRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.AttachPluginToApiResponse`
        """
        http_info = self._attach_plugin_to_api_http_info(request)
        return self._call_api(**http_info)

    def attach_plugin_to_api_async_invoker(self, request):
        http_info = self._attach_plugin_to_api_http_info(request)
        return AsyncInvoker(self, http_info)

    def _attach_plugin_to_api_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/apis/{api_id}/plugins/attach",
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

    def batch_add_device_to_group_async(self, request):
        r"""批量添加设备到设备分组

        批量添加设备到设备分组
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchAddDeviceToGroup
        :type request: :class:`huaweicloudsdkroma.v2.BatchAddDeviceToGroupRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.BatchAddDeviceToGroupResponse`
        """
        http_info = self._batch_add_device_to_group_http_info(request)
        return self._call_api(**http_info)

    def batch_add_device_to_group_async_invoker(self, request):
        http_info = self._batch_add_device_to_group_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_add_device_to_group_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/link/instances/{instance_id}/device-groups/{group_id}/devices/batch-add",
            "request_type": request.__class__.__name__,
            "response_type": "BatchAddDeviceToGroupResponse"
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

    def batch_delete_devices_async(self, request):
        r"""批量删除设备

        批量删除设备
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchDeleteDevices
        :type request: :class:`huaweicloudsdkroma.v2.BatchDeleteDevicesRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.BatchDeleteDevicesResponse`
        """
        http_info = self._batch_delete_devices_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_devices_async_invoker(self, request):
        http_info = self._batch_delete_devices_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_delete_devices_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/link/instances/{instance_id}/devices",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeleteDevicesResponse"
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

    def batch_delete_mqs_instance_topic_async(self, request):
        r"""批量删除Topic

        批量删除Topic。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchDeleteMqsInstanceTopic
        :type request: :class:`huaweicloudsdkroma.v2.BatchDeleteMqsInstanceTopicRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.BatchDeleteMqsInstanceTopicResponse`
        """
        http_info = self._batch_delete_mqs_instance_topic_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_mqs_instance_topic_async_invoker(self, request):
        http_info = self._batch_delete_mqs_instance_topic_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_delete_mqs_instance_topic_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/mqs/instances/{instance_id}/topics/delete",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeleteMqsInstanceTopicResponse"
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

    def batch_delete_rules_async(self, request):
        r"""批量删除规则

        批量删除规则
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchDeleteRules
        :type request: :class:`huaweicloudsdkroma.v2.BatchDeleteRulesRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.BatchDeleteRulesResponse`
        """
        http_info = self._batch_delete_rules_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_rules_async_invoker(self, request):
        http_info = self._batch_delete_rules_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_delete_rules_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/link/instances/{instance_id}/rules/batch-delete",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeleteRulesResponse"
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

    def batch_freeze_devices_async(self, request):
        r"""设备批量下线

        设备批量下线
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchFreezeDevices
        :type request: :class:`huaweicloudsdkroma.v2.BatchFreezeDevicesRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.BatchFreezeDevicesResponse`
        """
        http_info = self._batch_freeze_devices_http_info(request)
        return self._call_api(**http_info)

    def batch_freeze_devices_async_invoker(self, request):
        http_info = self._batch_freeze_devices_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_freeze_devices_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/link/instances/{instance_id}/devices/force-offline",
            "request_type": request.__class__.__name__,
            "response_type": "BatchFreezeDevicesResponse"
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

    def batch_start_or_stop_tasks_async(self, request):
        r"""批量启动\\停止任务

        批量启动\\停止任务
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchStartOrStopTasks
        :type request: :class:`huaweicloudsdkroma.v2.BatchStartOrStopTasksRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.BatchStartOrStopTasksResponse`
        """
        http_info = self._batch_start_or_stop_tasks_http_info(request)
        return self._call_api(**http_info)

    def batch_start_or_stop_tasks_async_invoker(self, request):
        http_info = self._batch_start_or_stop_tasks_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_start_or_stop_tasks_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/fdi/instances/{instance_id}/batch-operation/tasks",
            "request_type": request.__class__.__name__,
            "response_type": "BatchStartOrStopTasksResponse"
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

    def check_livedata_apis_v2_async(self, request):
        r"""校验自定义后端API定义

        校验自定义后端API定义。校验自定义后端API的路径或名称是否已存在
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CheckLivedataApisV2
        :type request: :class:`huaweicloudsdkroma.v2.CheckLivedataApisV2Request`
        :rtype: :class:`huaweicloudsdkroma.v2.CheckLivedataApisV2Response`
        """
        http_info = self._check_livedata_apis_v2_http_info(request)
        return self._call_api(**http_info)

    def check_livedata_apis_v2_async_invoker(self, request):
        http_info = self._check_livedata_apis_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _check_livedata_apis_v2_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/livedata-apis/check",
            "request_type": request.__class__.__name__,
            "response_type": "CheckLivedataApisV2Response"
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

    def count_devices_async(self, request):
        r"""设备数量统计

        设备数量统计
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CountDevices
        :type request: :class:`huaweicloudsdkroma.v2.CountDevicesRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.CountDevicesResponse`
        """
        http_info = self._count_devices_http_info(request)
        return self._call_api(**http_info)

    def count_devices_async_invoker(self, request):
        http_info = self._count_devices_http_info(request)
        return AsyncInvoker(self, http_info)

    def _count_devices_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/link/instances/{instance_id}/statistics/devices-count",
            "request_type": request.__class__.__name__,
            "response_type": "CountDevicesResponse"
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

    def count_tasks_async(self, request):
        r"""统计不同类型不同状态任务数量

        统计不同类型不同状态任务数量
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CountTasks
        :type request: :class:`huaweicloudsdkroma.v2.CountTasksRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.CountTasksResponse`
        """
        http_info = self._count_tasks_http_info(request)
        return self._call_api(**http_info)

    def count_tasks_async_invoker(self, request):
        http_info = self._count_tasks_http_info(request)
        return AsyncInvoker(self, http_info)

    def _count_tasks_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/fdi/instances/{instance_id}/statistics/tasks",
            "request_type": request.__class__.__name__,
            "response_type": "CountTasksResponse"
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

    def create_app_code_auto_v2_async(self, request):
        r"""自动生成APP Code

        创建App Code时，可以不指定具体值，由后台自动生成随机字符串填充。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateAppCodeAutoV2
        :type request: :class:`huaweicloudsdkroma.v2.CreateAppCodeAutoV2Request`
        :rtype: :class:`huaweicloudsdkroma.v2.CreateAppCodeAutoV2Response`
        """
        http_info = self._create_app_code_auto_v2_http_info(request)
        return self._call_api(**http_info)

    def create_app_code_auto_v2_async_invoker(self, request):
        http_info = self._create_app_code_auto_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_app_code_auto_v2_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/apps/{app_id}/app-codes",
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
        r"""创建APP Code

        App Code为APP应用下的子模块，创建App Code之后，可以实现简易的APP认证。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateAppCodeV2
        :type request: :class:`huaweicloudsdkroma.v2.CreateAppCodeV2Request`
        :rtype: :class:`huaweicloudsdkroma.v2.CreateAppCodeV2Response`
        """
        http_info = self._create_app_code_v2_http_info(request)
        return self._call_api(**http_info)

    def create_app_code_v2_async_invoker(self, request):
        http_info = self._create_app_code_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_app_code_v2_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/apps/{app_id}/app-codes",
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

    def create_app_config_v2_async(self, request):
        r"""创建应用配置

        创建应用配置
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateAppConfigV2
        :type request: :class:`huaweicloudsdkroma.v2.CreateAppConfigV2Request`
        :rtype: :class:`huaweicloudsdkroma.v2.CreateAppConfigV2Response`
        """
        http_info = self._create_app_config_v2_http_info(request)
        return self._call_api(**http_info)

    def create_app_config_v2_async_invoker(self, request):
        http_info = self._create_app_config_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_app_config_v2_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/apps/{app_id}/configs",
            "request_type": request.__class__.__name__,
            "response_type": "CreateAppConfigV2Response"
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
        r"""创建客户端配额

        创建客户端配额
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateAppQuota
        :type request: :class:`huaweicloudsdkroma.v2.CreateAppQuotaRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.CreateAppQuotaResponse`
        """
        http_info = self._create_app_quota_http_info(request)
        return self._call_api(**http_info)

    def create_app_quota_async_invoker(self, request):
        http_info = self._create_app_quota_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_app_quota_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/app-quotas",
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

    def create_command_async(self, request):
        r"""创建命令

        创建命令
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateCommand
        :type request: :class:`huaweicloudsdkroma.v2.CreateCommandRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.CreateCommandResponse`
        """
        http_info = self._create_command_http_info(request)
        return self._call_api(**http_info)

    def create_command_async_invoker(self, request):
        http_info = self._create_command_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_command_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/link/instances/{instance_id}/services/{service_id}/commands",
            "request_type": request.__class__.__name__,
            "response_type": "CreateCommandResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'service_id' in local_var_params:
            path_params['service_id'] = local_var_params['service_id']

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

    def create_common_task_async(self, request):
        r"""创建普通任务

        创建普通任务(区别于组合任务)
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateCommonTask
        :type request: :class:`huaweicloudsdkroma.v2.CreateCommonTaskRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.CreateCommonTaskResponse`
        """
        http_info = self._create_common_task_http_info(request)
        return self._call_api(**http_info)

    def create_common_task_async_invoker(self, request):
        http_info = self._create_common_task_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_common_task_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/fdi/instances/{instance_id}/tasks",
            "request_type": request.__class__.__name__,
            "response_type": "CreateCommonTaskResponse"
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
        r"""创建自定义认证

        创建自定义认证
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateCustomAuthorizerV2
        :type request: :class:`huaweicloudsdkroma.v2.CreateCustomAuthorizerV2Request`
        :rtype: :class:`huaweicloudsdkroma.v2.CreateCustomAuthorizerV2Response`
        """
        http_info = self._create_custom_authorizer_v2_http_info(request)
        return self._call_api(**http_info)

    def create_custom_authorizer_v2_async_invoker(self, request):
        http_info = self._create_custom_authorizer_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_custom_authorizer_v2_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/authorizers",
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

    def create_datasource_info_async(self, request):
        r"""创建数据源

        创建数据源
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateDatasourceInfo
        :type request: :class:`huaweicloudsdkroma.v2.CreateDatasourceInfoRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.CreateDatasourceInfoResponse`
        """
        http_info = self._create_datasource_info_http_info(request)
        return self._call_api(**http_info)

    def create_datasource_info_async_invoker(self, request):
        http_info = self._create_datasource_info_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_datasource_info_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/fdi/instances/{instance_id}/datasources",
            "request_type": request.__class__.__name__,
            "response_type": "CreateDatasourceInfoResponse"
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

    def create_destination_async(self, request):
        r"""添加目标数据源

        添加目标数据源
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateDestination
        :type request: :class:`huaweicloudsdkroma.v2.CreateDestinationRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.CreateDestinationResponse`
        """
        http_info = self._create_destination_http_info(request)
        return self._call_api(**http_info)

    def create_destination_async_invoker(self, request):
        http_info = self._create_destination_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_destination_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/link/instances/{instance_id}/rules/{rule_id}/destinations",
            "request_type": request.__class__.__name__,
            "response_type": "CreateDestinationResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'rule_id' in local_var_params:
            path_params['rule_id'] = local_var_params['rule_id']

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

    def create_device_async(self, request):
        r"""创建设备

        创建设备
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateDevice
        :type request: :class:`huaweicloudsdkroma.v2.CreateDeviceRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.CreateDeviceResponse`
        """
        http_info = self._create_device_http_info(request)
        return self._call_api(**http_info)

    def create_device_async_invoker(self, request):
        http_info = self._create_device_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_device_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/link/instances/{instance_id}/devices",
            "request_type": request.__class__.__name__,
            "response_type": "CreateDeviceResponse"
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

    def create_device_group_async(self, request):
        r"""创建设备分组

        创建设备分组
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateDeviceGroup
        :type request: :class:`huaweicloudsdkroma.v2.CreateDeviceGroupRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.CreateDeviceGroupResponse`
        """
        http_info = self._create_device_group_http_info(request)
        return self._call_api(**http_info)

    def create_device_group_async_invoker(self, request):
        http_info = self._create_device_group_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_device_group_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/link/instances/{instance_id}/device-groups",
            "request_type": request.__class__.__name__,
            "response_type": "CreateDeviceGroupResponse"
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

    def create_dispatches_async(self, request):
        r"""创建调度计划

        创建调度计划
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateDispatches
        :type request: :class:`huaweicloudsdkroma.v2.CreateDispatchesRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.CreateDispatchesResponse`
        """
        http_info = self._create_dispatches_http_info(request)
        return self._call_api(**http_info)

    def create_dispatches_async_invoker(self, request):
        http_info = self._create_dispatches_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_dispatches_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/fdi/instances/{instance_id}/tasks/{task_id}/dispatches",
            "request_type": request.__class__.__name__,
            "response_type": "CreateDispatchesResponse"
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
        r"""创建环境

        在实际的生产中，API提供者可能有多个环境，如开发环境、测试环境、生产环境等，用户可以自由将API发布到某个环境，供调用者调用。
        
        
        对于不同的环境，API的版本、请求地址甚至于包括请求消息等均有可能不同。如：某个API，v1.0的版本为稳定版本，发布到了生产环境供生产使用，同时，该API正处于迭代中，v1.1的版本是开发人员交付测试人员进行测试的版本，发布在测试环境上，而v1.2的版本目前开发团队正处于开发过程中，可以发布到开发环境进行自测等。
        
        
        为此，服务集成提供多环境管理功能，使租户能够最大化的模拟实际场景，低成本的接服务集成。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateEnvironmentV2
        :type request: :class:`huaweicloudsdkroma.v2.CreateEnvironmentV2Request`
        :rtype: :class:`huaweicloudsdkroma.v2.CreateEnvironmentV2Response`
        """
        http_info = self._create_environment_v2_http_info(request)
        return self._call_api(**http_info)

    def create_environment_v2_async_invoker(self, request):
        http_info = self._create_environment_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_environment_v2_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/envs",
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
        r"""新建变量

        将API发布到不同的环境后，对于不同的环境，可能会有不同的环境变量，比如，API的服务部署地址，请求的版本号等。
        
        
        用户可以定义不同的环境变量，用户在定义API时，在API的定义中使用这些变量，当调用API时，服务集成会将这些变量替换成真实的变量值，以达到不同环境的区分效果。
        
        
        环境变量定义在API分组上，该分组下的所有API都可以使用这些变量。
        
        &gt; 1.环境变量的变量名称必须保持唯一，即一个分组在同一个环境上不能有两个同名的变量
          2.环境变量区分大小写，即变量ABC与变量abc是两个不同的变量
          3.设置了环境变量后，使用到该变量的API的调试功能将不可使用。
          4.定义了环境变量后，使用到环境变量的地方应该以对称的#标识环境变量，当API发布到相应的环境后，会对环境变量的值进行替换，如：定义的API的URL为：https://#address#:8080，环境变量address在RELEASE环境上的值为：192.168.1.5，则API发布到RELEASE环境后的真实的URL为：https://192.168.1.5:8080。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateEnvironmentVariableV2
        :type request: :class:`huaweicloudsdkroma.v2.CreateEnvironmentVariableV2Request`
        :rtype: :class:`huaweicloudsdkroma.v2.CreateEnvironmentVariableV2Response`
        """
        http_info = self._create_environment_variable_v2_http_info(request)
        return self._call_api(**http_info)

    def create_environment_variable_v2_async_invoker(self, request):
        http_info = self._create_environment_variable_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_environment_variable_v2_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/env-variables",
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
        r"""实例配置特性

        为实例配置需要的特性。
        
        支持配置的特性列表及特性配置请参考“附录 &gt; 实例支持的APIC特性”
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateFeatureV2
        :type request: :class:`huaweicloudsdkroma.v2.CreateFeatureV2Request`
        :rtype: :class:`huaweicloudsdkroma.v2.CreateFeatureV2Response`
        """
        http_info = self._create_feature_v2_http_info(request)
        return self._call_api(**http_info)

    def create_feature_v2_async_invoker(self, request):
        http_info = self._create_feature_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_feature_v2_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/features",
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

    def create_live_data_api_script_v2_async(self, request):
        r"""创建后端API脚本

        在某个实例中创建后端API脚本。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateLiveDataApiScriptV2
        :type request: :class:`huaweicloudsdkroma.v2.CreateLiveDataApiScriptV2Request`
        :rtype: :class:`huaweicloudsdkroma.v2.CreateLiveDataApiScriptV2Response`
        """
        http_info = self._create_live_data_api_script_v2_http_info(request)
        return self._call_api(**http_info)

    def create_live_data_api_script_v2_async_invoker(self, request):
        http_info = self._create_live_data_api_script_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_live_data_api_script_v2_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/livedata-apis/{ld_api_id}/scripts",
            "request_type": request.__class__.__name__,
            "response_type": "CreateLiveDataApiScriptV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'ld_api_id' in local_var_params:
            path_params['ld_api_id'] = local_var_params['ld_api_id']

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

    def create_live_data_api_v2_async(self, request):
        r"""创建后端API

        在某个实例中创建后端API。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateLiveDataApiV2
        :type request: :class:`huaweicloudsdkroma.v2.CreateLiveDataApiV2Request`
        :rtype: :class:`huaweicloudsdkroma.v2.CreateLiveDataApiV2Response`
        """
        http_info = self._create_live_data_api_v2_http_info(request)
        return self._call_api(**http_info)

    def create_live_data_api_v2_async_invoker(self, request):
        http_info = self._create_live_data_api_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_live_data_api_v2_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/livedata-apis",
            "request_type": request.__class__.__name__,
            "response_type": "CreateLiveDataApiV2Response"
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

    def create_mqs_instance_topic_async(self, request):
        r"""创建Topic

        创建Topic。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateMqsInstanceTopic
        :type request: :class:`huaweicloudsdkroma.v2.CreateMqsInstanceTopicRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.CreateMqsInstanceTopicResponse`
        """
        http_info = self._create_mqs_instance_topic_http_info(request)
        return self._call_api(**http_info)

    def create_mqs_instance_topic_async_invoker(self, request):
        http_info = self._create_mqs_instance_topic_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_mqs_instance_topic_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/mqs/instances/{instance_id}/topics",
            "request_type": request.__class__.__name__,
            "response_type": "CreateMqsInstanceTopicResponse"
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

    def create_multi_task_mappings_async(self, request):
        r"""创建组合任务映射

        创建组合任务映射
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateMultiTaskMappings
        :type request: :class:`huaweicloudsdkroma.v2.CreateMultiTaskMappingsRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.CreateMultiTaskMappingsResponse`
        """
        http_info = self._create_multi_task_mappings_http_info(request)
        return self._call_api(**http_info)

    def create_multi_task_mappings_async_invoker(self, request):
        http_info = self._create_multi_task_mappings_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_multi_task_mappings_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/fdi/instances/{instance_id}/multi-tasks/{task_id}/mappings",
            "request_type": request.__class__.__name__,
            "response_type": "CreateMultiTaskMappingsResponse"
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

    def create_multi_tasks_async(self, request):
        r"""创建组合任务

        创建组合任务
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateMultiTasks
        :type request: :class:`huaweicloudsdkroma.v2.CreateMultiTasksRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.CreateMultiTasksResponse`
        """
        http_info = self._create_multi_tasks_http_info(request)
        return self._call_api(**http_info)

    def create_multi_tasks_async_invoker(self, request):
        http_info = self._create_multi_tasks_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_multi_tasks_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/fdi/instances/{instance_id}/multi-tasks",
            "request_type": request.__class__.__name__,
            "response_type": "CreateMultiTasksResponse"
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

    def create_notification_async(self, request):
        r"""创建订阅管理

        该接口用于创建指定实例下对应的应用下的设备操作，订阅到指定的topic
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateNotification
        :type request: :class:`huaweicloudsdkroma.v2.CreateNotificationRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.CreateNotificationResponse`
        """
        http_info = self._create_notification_http_info(request)
        return self._call_api(**http_info)

    def create_notification_async_invoker(self, request):
        http_info = self._create_notification_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_notification_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/link/instances/{instance_id}/notifications",
            "request_type": request.__class__.__name__,
            "response_type": "CreateNotificationResponse"
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

    def create_plugin_async(self, request):
        r"""创建插件

        创建插件信息。
        - 插件不允许重名
        - 插件创建后未绑定API前是无意义的，绑定API后，对绑定的API即时生效
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreatePlugin
        :type request: :class:`huaweicloudsdkroma.v2.CreatePluginRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.CreatePluginResponse`
        """
        http_info = self._create_plugin_http_info(request)
        return self._call_api(**http_info)

    def create_plugin_async_invoker(self, request):
        http_info = self._create_plugin_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_plugin_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/plugins",
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

    def create_product_async(self, request):
        r"""创建产品

        创建产品
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateProduct
        :type request: :class:`huaweicloudsdkroma.v2.CreateProductRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.CreateProductResponse`
        """
        http_info = self._create_product_http_info(request)
        return self._call_api(**http_info)

    def create_product_async_invoker(self, request):
        http_info = self._create_product_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_product_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/link/instances/{instance_id}/products",
            "request_type": request.__class__.__name__,
            "response_type": "CreateProductResponse"
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

    def create_product_template_async(self, request):
        r"""创建产品模板

        创建产品模板
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateProductTemplate
        :type request: :class:`huaweicloudsdkroma.v2.CreateProductTemplateRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.CreateProductTemplateResponse`
        """
        http_info = self._create_product_template_http_info(request)
        return self._call_api(**http_info)

    def create_product_template_async_invoker(self, request):
        http_info = self._create_product_template_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_product_template_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/link/instances/{instance_id}/product-templates",
            "request_type": request.__class__.__name__,
            "response_type": "CreateProductTemplateResponse"
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

    def create_product_topic_async(self, request):
        r"""添加产品主题

        添加产品主题
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateProductTopic
        :type request: :class:`huaweicloudsdkroma.v2.CreateProductTopicRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.CreateProductTopicResponse`
        """
        http_info = self._create_product_topic_http_info(request)
        return self._call_api(**http_info)

    def create_product_topic_async_invoker(self, request):
        http_info = self._create_product_topic_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_product_topic_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/link/instances/{instance_id}/products/{product_id}/topics",
            "request_type": request.__class__.__name__,
            "response_type": "CreateProductTopicResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'product_id' in local_var_params:
            path_params['product_id'] = local_var_params['product_id']

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

    def create_property_async(self, request):
        r"""创建属性

        创建属性
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateProperty
        :type request: :class:`huaweicloudsdkroma.v2.CreatePropertyRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.CreatePropertyResponse`
        """
        http_info = self._create_property_http_info(request)
        return self._call_api(**http_info)

    def create_property_async_invoker(self, request):
        http_info = self._create_property_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_property_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/link/instances/{instance_id}/services/{service_id}/properties",
            "request_type": request.__class__.__name__,
            "response_type": "CreatePropertyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'service_id' in local_var_params:
            path_params['service_id'] = local_var_params['service_id']

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

    def create_request_property_async(self, request):
        r"""创建请求属性

        创建请求属性
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateRequestProperty
        :type request: :class:`huaweicloudsdkroma.v2.CreateRequestPropertyRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.CreateRequestPropertyResponse`
        """
        http_info = self._create_request_property_http_info(request)
        return self._call_api(**http_info)

    def create_request_property_async_invoker(self, request):
        http_info = self._create_request_property_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_request_property_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/link/instances/{instance_id}/services/{service_id}/commands/{command_id}/requests",
            "request_type": request.__class__.__name__,
            "response_type": "CreateRequestPropertyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'service_id' in local_var_params:
            path_params['service_id'] = local_var_params['service_id']
        if 'command_id' in local_var_params:
            path_params['command_id'] = local_var_params['command_id']

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
        r"""创建流控策略

        当API上线后，系统会默认给每个API提供一个流控策略，API提供者可以根据自身API的服务能力及负载情况变更这个流控策略。
        流控策略即限制API在一定长度的时间内，能够允许被访问的最大次数。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateRequestThrottlingPolicyV2
        :type request: :class:`huaweicloudsdkroma.v2.CreateRequestThrottlingPolicyV2Request`
        :rtype: :class:`huaweicloudsdkroma.v2.CreateRequestThrottlingPolicyV2Response`
        """
        http_info = self._create_request_throttling_policy_v2_http_info(request)
        return self._call_api(**http_info)

    def create_request_throttling_policy_v2_async_invoker(self, request):
        http_info = self._create_request_throttling_policy_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_request_throttling_policy_v2_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/throttles",
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

    def create_response_property_async(self, request):
        r"""创建响应属性

        创建响应属性
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateResponseProperty
        :type request: :class:`huaweicloudsdkroma.v2.CreateResponsePropertyRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.CreateResponsePropertyResponse`
        """
        http_info = self._create_response_property_http_info(request)
        return self._call_api(**http_info)

    def create_response_property_async_invoker(self, request):
        http_info = self._create_response_property_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_response_property_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/link/instances/{instance_id}/services/{service_id}/commands/{command_id}/responses",
            "request_type": request.__class__.__name__,
            "response_type": "CreateResponsePropertyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'service_id' in local_var_params:
            path_params['service_id'] = local_var_params['service_id']
        if 'command_id' in local_var_params:
            path_params['command_id'] = local_var_params['command_id']

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

    def create_rule_async(self, request):
        r"""创建规则

        创建规则
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateRule
        :type request: :class:`huaweicloudsdkroma.v2.CreateRuleRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.CreateRuleResponse`
        """
        http_info = self._create_rule_http_info(request)
        return self._call_api(**http_info)

    def create_rule_async_invoker(self, request):
        http_info = self._create_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_rule_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/link/instances/{instance_id}/rules",
            "request_type": request.__class__.__name__,
            "response_type": "CreateRuleResponse"
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

    def create_service_async(self, request):
        r"""创建服务

        创建服务
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateService
        :type request: :class:`huaweicloudsdkroma.v2.CreateServiceRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.CreateServiceResponse`
        """
        http_info = self._create_service_http_info(request)
        return self._call_api(**http_info)

    def create_service_async_invoker(self, request):
        http_info = self._create_service_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_service_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/link/instances/{instance_id}/services",
            "request_type": request.__class__.__name__,
            "response_type": "CreateServiceResponse"
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
        r"""创建签名密钥

        为了保护API的安全性，建议租户为API的访问提供一套保护机制，即租户开放的API，需要对请求来源进行认证，不符合认证的请求直接拒绝访问。
        
        其中，签名密钥就是API安全保护机制的一种。
        
        租户创建一个签名密钥，并将签名密钥与API进行绑定，则服务集成在请求这个API时，就会使用绑定的签名密钥对请求参数进行数据加密，生成签名。当租户的后端服务收到请求时，可以校验这个签名，如果签名校验不通过，则该请求不是服务集成发出的请求，租户可以拒绝这个请求，从而保证API的安全性，避免API被未知来源的请求攻击。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateSignatureKeyV2
        :type request: :class:`huaweicloudsdkroma.v2.CreateSignatureKeyV2Request`
        :rtype: :class:`huaweicloudsdkroma.v2.CreateSignatureKeyV2Response`
        """
        http_info = self._create_signature_key_v2_http_info(request)
        return self._call_api(**http_info)

    def create_signature_key_v2_async_invoker(self, request):
        http_info = self._create_signature_key_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_signature_key_v2_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/signs",
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

    def create_source_async(self, request):
        r"""添加源数据源

        添加源数据源
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateSource
        :type request: :class:`huaweicloudsdkroma.v2.CreateSourceRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.CreateSourceResponse`
        """
        http_info = self._create_source_http_info(request)
        return self._call_api(**http_info)

    def create_source_async_invoker(self, request):
        http_info = self._create_source_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_source_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/link/instances/{instance_id}/rules/{rule_id}/sources",
            "request_type": request.__class__.__name__,
            "response_type": "CreateSourceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'rule_id' in local_var_params:
            path_params['rule_id'] = local_var_params['rule_id']

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
        r"""创建特殊设置

        流控策略可以限制一段时间内可以访问API的最大次数，也可以限制一段时间内单个租户和单个APP可以访问API的最大次数。
        
        如果想要对某个特定的APP进行特殊设置，例如设置所有APP每分钟的访问次数为500次，但想设置APP1每分钟的访问次数为800次，可以通过在流控策略中设置特殊APP来实现该功能。
        
        为流控策略添加一个特殊设置的对象，[可以是APP，也可以是租户。](tag:hws,hws_hk,hcs,hcs_sm,fcs,g42)[对象为APP。](tag:Site)
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateSpecialThrottlingConfigurationV2
        :type request: :class:`huaweicloudsdkroma.v2.CreateSpecialThrottlingConfigurationV2Request`
        :rtype: :class:`huaweicloudsdkroma.v2.CreateSpecialThrottlingConfigurationV2Response`
        """
        http_info = self._create_special_throttling_configuration_v2_http_info(request)
        return self._call_api(**http_info)

    def create_special_throttling_configuration_v2_async_invoker(self, request):
        http_info = self._create_special_throttling_configuration_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_special_throttling_configuration_v2_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/throttles/{throttle_id}/throttle-specials",
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

    def debug_live_data_api_v2_async(self, request):
        r"""测试后端API

        测试后端API是否可用。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DebugLiveDataApiV2
        :type request: :class:`huaweicloudsdkroma.v2.DebugLiveDataApiV2Request`
        :rtype: :class:`huaweicloudsdkroma.v2.DebugLiveDataApiV2Response`
        """
        http_info = self._debug_live_data_api_v2_http_info(request)
        return self._call_api(**http_info)

    def debug_live_data_api_v2_async_invoker(self, request):
        http_info = self._debug_live_data_api_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _debug_live_data_api_v2_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/livedata-apis/{ld_api_id}/test",
            "request_type": request.__class__.__name__,
            "response_type": "DebugLiveDataApiV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'ld_api_id' in local_var_params:
            path_params['ld_api_id'] = local_var_params['ld_api_id']

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

    def debug_rule_async(self, request):
        r"""规则调试

        规则调试
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DebugRule
        :type request: :class:`huaweicloudsdkroma.v2.DebugRuleRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.DebugRuleResponse`
        """
        http_info = self._debug_rule_http_info(request)
        return self._call_api(**http_info)

    def debug_rule_async_invoker(self, request):
        http_info = self._debug_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _debug_rule_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/link/instances/{instance_id}/rule-test",
            "request_type": request.__class__.__name__,
            "response_type": "DebugRuleResponse"
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

    def delete_app_acl_async(self, request):
        r"""删除APP的访问控制

        删除客户端配置的访问控制信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteAppAcl
        :type request: :class:`huaweicloudsdkroma.v2.DeleteAppAclRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.DeleteAppAclResponse`
        """
        http_info = self._delete_app_acl_http_info(request)
        return self._call_api(**http_info)

    def delete_app_acl_async_invoker(self, request):
        http_info = self._delete_app_acl_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_app_acl_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/apps/{app_id}/app-acl",
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
        r"""删除APP Code

        删除App Code，App Code删除后，将无法再通过简易认证访问对应的API。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteAppCodeV2
        :type request: :class:`huaweicloudsdkroma.v2.DeleteAppCodeV2Request`
        :rtype: :class:`huaweicloudsdkroma.v2.DeleteAppCodeV2Response`
        """
        http_info = self._delete_app_code_v2_http_info(request)
        return self._call_api(**http_info)

    def delete_app_code_v2_async_invoker(self, request):
        http_info = self._delete_app_code_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_app_code_v2_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/apps/{app_id}/app-codes/{app_code_id}",
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

    def delete_app_config_v2_async(self, request):
        r"""删除应用配置

        删除应用配置
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteAppConfigV2
        :type request: :class:`huaweicloudsdkroma.v2.DeleteAppConfigV2Request`
        :rtype: :class:`huaweicloudsdkroma.v2.DeleteAppConfigV2Response`
        """
        http_info = self._delete_app_config_v2_http_info(request)
        return self._call_api(**http_info)

    def delete_app_config_v2_async_invoker(self, request):
        http_info = self._delete_app_config_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_app_config_v2_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/apps/{app_id}/configs/{app_config_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteAppConfigV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'app_id' in local_var_params:
            path_params['app_id'] = local_var_params['app_id']
        if 'app_config_id' in local_var_params:
            path_params['app_config_id'] = local_var_params['app_config_id']

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
        r"""删除客户端配额

        删除客户端配额。删除客户端配额时，同时删除客户端配额和客户端应用的关联关系
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteAppQuota
        :type request: :class:`huaweicloudsdkroma.v2.DeleteAppQuotaRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.DeleteAppQuotaResponse`
        """
        http_info = self._delete_app_quota_http_info(request)
        return self._call_api(**http_info)

    def delete_app_quota_async_invoker(self, request):
        http_info = self._delete_app_quota_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_app_quota_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/app-quotas/{app_quota_id}",
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

    def delete_command_async(self, request):
        r"""删除命令

        删除命令
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteCommand
        :type request: :class:`huaweicloudsdkroma.v2.DeleteCommandRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.DeleteCommandResponse`
        """
        http_info = self._delete_command_http_info(request)
        return self._call_api(**http_info)

    def delete_command_async_invoker(self, request):
        http_info = self._delete_command_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_command_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/link/instances/{instance_id}/services/{service_id}/commands/{command_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteCommandResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'service_id' in local_var_params:
            path_params['service_id'] = local_var_params['service_id']
        if 'command_id' in local_var_params:
            path_params['command_id'] = local_var_params['command_id']

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
        r"""删除自定义认证

        删除自定义认证
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteCustomAuthorizerV2
        :type request: :class:`huaweicloudsdkroma.v2.DeleteCustomAuthorizerV2Request`
        :rtype: :class:`huaweicloudsdkroma.v2.DeleteCustomAuthorizerV2Response`
        """
        http_info = self._delete_custom_authorizer_v2_http_info(request)
        return self._call_api(**http_info)

    def delete_custom_authorizer_v2_async_invoker(self, request):
        http_info = self._delete_custom_authorizer_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_custom_authorizer_v2_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/authorizers/{authorizer_id}",
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

    def delete_datasource_info_by_id_async(self, request):
        r"""通过数据源Id删除指定数据源信息

        通过数据源Id删除指定数据源信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteDatasourceInfoById
        :type request: :class:`huaweicloudsdkroma.v2.DeleteDatasourceInfoByIdRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.DeleteDatasourceInfoByIdResponse`
        """
        http_info = self._delete_datasource_info_by_id_http_info(request)
        return self._call_api(**http_info)

    def delete_datasource_info_by_id_async_invoker(self, request):
        http_info = self._delete_datasource_info_by_id_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_datasource_info_by_id_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/fdi/instances/{instance_id}/datasources/{datasource_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteDatasourceInfoByIdResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'datasource_id' in local_var_params:
            path_params['datasource_id'] = local_var_params['datasource_id']

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

    def delete_destination_async(self, request):
        r"""删除目标数据源

        删除目标数据源
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteDestination
        :type request: :class:`huaweicloudsdkroma.v2.DeleteDestinationRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.DeleteDestinationResponse`
        """
        http_info = self._delete_destination_http_info(request)
        return self._call_api(**http_info)

    def delete_destination_async_invoker(self, request):
        http_info = self._delete_destination_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_destination_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/link/instances/{instance_id}/rules/{rule_id}/destinations/{destination_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteDestinationResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'rule_id' in local_var_params:
            path_params['rule_id'] = local_var_params['rule_id']
        if 'destination_id' in local_var_params:
            path_params['destination_id'] = local_var_params['destination_id']

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

    def delete_device_async(self, request):
        r"""删除设备

        删除指定设备ID的设备
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteDevice
        :type request: :class:`huaweicloudsdkroma.v2.DeleteDeviceRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.DeleteDeviceResponse`
        """
        http_info = self._delete_device_http_info(request)
        return self._call_api(**http_info)

    def delete_device_async_invoker(self, request):
        http_info = self._delete_device_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_device_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/link/instances/{instance_id}/devices/{device_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteDeviceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'device_id' in local_var_params:
            path_params['device_id'] = local_var_params['device_id']

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

    def delete_device_from_group_async(self, request):
        r"""删除设备分组内的设备

        删除设备分组内的设备
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteDeviceFromGroup
        :type request: :class:`huaweicloudsdkroma.v2.DeleteDeviceFromGroupRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.DeleteDeviceFromGroupResponse`
        """
        http_info = self._delete_device_from_group_http_info(request)
        return self._call_api(**http_info)

    def delete_device_from_group_async_invoker(self, request):
        http_info = self._delete_device_from_group_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_device_from_group_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/link/instances/{instance_id}/device-groups/{group_id}/devices/{device_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteDeviceFromGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'device_id' in local_var_params:
            path_params['device_id'] = local_var_params['device_id']
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

    def delete_device_group_async(self, request):
        r"""删除设备分组

        删除分组
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteDeviceGroup
        :type request: :class:`huaweicloudsdkroma.v2.DeleteDeviceGroupRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.DeleteDeviceGroupResponse`
        """
        http_info = self._delete_device_group_http_info(request)
        return self._call_api(**http_info)

    def delete_device_group_async_invoker(self, request):
        http_info = self._delete_device_group_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_device_group_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/link/instances/{instance_id}/device-groups/{group_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteDeviceGroupResponse"
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

    def delete_environment_v2_async(self, request):
        r"""删除环境

        删除指定的环境。
        该操作将导致此API在指定的环境无法被访问，可能会影响相当一部分应用和用户。请确保已经告知用户，或者确认需要强制下线。环境上存在已发布的API时，该环境不能被删除。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteEnvironmentV2
        :type request: :class:`huaweicloudsdkroma.v2.DeleteEnvironmentV2Request`
        :rtype: :class:`huaweicloudsdkroma.v2.DeleteEnvironmentV2Response`
        """
        http_info = self._delete_environment_v2_http_info(request)
        return self._call_api(**http_info)

    def delete_environment_v2_async_invoker(self, request):
        http_info = self._delete_environment_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_environment_v2_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/envs/{env_id}",
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
        r"""删除变量

        删除指定的环境变量。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteEnvironmentVariableV2
        :type request: :class:`huaweicloudsdkroma.v2.DeleteEnvironmentVariableV2Request`
        :rtype: :class:`huaweicloudsdkroma.v2.DeleteEnvironmentVariableV2Response`
        """
        http_info = self._delete_environment_variable_v2_http_info(request)
        return self._call_api(**http_info)

    def delete_environment_variable_v2_async_invoker(self, request):
        http_info = self._delete_environment_variable_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_environment_variable_v2_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/env-variables/{env_variable_id}",
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

    def delete_live_data_api_v2_async(self, request):
        r"""删除后端API

        在某个实例中删除后端API。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteLiveDataApiV2
        :type request: :class:`huaweicloudsdkroma.v2.DeleteLiveDataApiV2Request`
        :rtype: :class:`huaweicloudsdkroma.v2.DeleteLiveDataApiV2Response`
        """
        http_info = self._delete_live_data_api_v2_http_info(request)
        return self._call_api(**http_info)

    def delete_live_data_api_v2_async_invoker(self, request):
        http_info = self._delete_live_data_api_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_live_data_api_v2_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/livedata-apis/{ld_api_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteLiveDataApiV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'ld_api_id' in local_var_params:
            path_params['ld_api_id'] = local_var_params['ld_api_id']

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

    def delete_mqs_instance_topic_async(self, request):
        r"""删除Topic

        删除Topic。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteMqsInstanceTopic
        :type request: :class:`huaweicloudsdkroma.v2.DeleteMqsInstanceTopicRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.DeleteMqsInstanceTopicResponse`
        """
        http_info = self._delete_mqs_instance_topic_http_info(request)
        return self._call_api(**http_info)

    def delete_mqs_instance_topic_async_invoker(self, request):
        http_info = self._delete_mqs_instance_topic_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_mqs_instance_topic_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/mqs/instances/{instance_id}/topics",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteMqsInstanceTopicResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def delete_multi_task_mapping_async(self, request):
        r"""删除指定任务映射

        通过映射ID删除指定任务映射
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteMultiTaskMapping
        :type request: :class:`huaweicloudsdkroma.v2.DeleteMultiTaskMappingRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.DeleteMultiTaskMappingResponse`
        """
        http_info = self._delete_multi_task_mapping_http_info(request)
        return self._call_api(**http_info)

    def delete_multi_task_mapping_async_invoker(self, request):
        http_info = self._delete_multi_task_mapping_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_multi_task_mapping_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/fdi/instances/{instance_id}/multi-tasks/{task_id}/mappings/{mapping_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteMultiTaskMappingResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']
        if 'mapping_id' in local_var_params:
            path_params['mapping_id'] = local_var_params['mapping_id']

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

    def delete_notification_async(self, request):
        r"""删除订阅管理

        该接口用于删除指定订阅管理
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteNotification
        :type request: :class:`huaweicloudsdkroma.v2.DeleteNotificationRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.DeleteNotificationResponse`
        """
        http_info = self._delete_notification_http_info(request)
        return self._call_api(**http_info)

    def delete_notification_async_invoker(self, request):
        http_info = self._delete_notification_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_notification_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/link/instances/{instance_id}/notifications/{notification_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteNotificationResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'notification_id' in local_var_params:
            path_params['notification_id'] = local_var_params['notification_id']

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
        r"""删除插件

        删除插件。
        - 必须先解除API和插件的绑定关系，否则删除报错
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeletePlugin
        :type request: :class:`huaweicloudsdkroma.v2.DeletePluginRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.DeletePluginResponse`
        """
        http_info = self._delete_plugin_http_info(request)
        return self._call_api(**http_info)

    def delete_plugin_async_invoker(self, request):
        http_info = self._delete_plugin_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_plugin_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/plugins/{plugin_id}",
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

    def delete_product_async(self, request):
        r"""删除产品

        删除产品
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteProduct
        :type request: :class:`huaweicloudsdkroma.v2.DeleteProductRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.DeleteProductResponse`
        """
        http_info = self._delete_product_http_info(request)
        return self._call_api(**http_info)

    def delete_product_async_invoker(self, request):
        http_info = self._delete_product_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_product_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/link/instances/{instance_id}/products/{product_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteProductResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'product_id' in local_var_params:
            path_params['product_id'] = local_var_params['product_id']

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

    def delete_product_template_async(self, request):
        r"""删除产品模板

        删除产品模板
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteProductTemplate
        :type request: :class:`huaweicloudsdkroma.v2.DeleteProductTemplateRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.DeleteProductTemplateResponse`
        """
        http_info = self._delete_product_template_http_info(request)
        return self._call_api(**http_info)

    def delete_product_template_async_invoker(self, request):
        http_info = self._delete_product_template_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_product_template_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/link/instances/{instance_id}/product-templates/{product_template_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteProductTemplateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'product_template_id' in local_var_params:
            path_params['product_template_id'] = local_var_params['product_template_id']

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

    def delete_product_topic_async(self, request):
        r"""删除产品主题

        删除产品主题
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteProductTopic
        :type request: :class:`huaweicloudsdkroma.v2.DeleteProductTopicRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.DeleteProductTopicResponse`
        """
        http_info = self._delete_product_topic_http_info(request)
        return self._call_api(**http_info)

    def delete_product_topic_async_invoker(self, request):
        http_info = self._delete_product_topic_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_product_topic_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/link/instances/{instance_id}/products/{product_id}/topics/{topic_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteProductTopicResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'product_id' in local_var_params:
            path_params['product_id'] = local_var_params['product_id']
        if 'topic_id' in local_var_params:
            path_params['topic_id'] = local_var_params['topic_id']

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

    def delete_property_async(self, request):
        r"""删除服务属性

        删除服务属性
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteProperty
        :type request: :class:`huaweicloudsdkroma.v2.DeletePropertyRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.DeletePropertyResponse`
        """
        http_info = self._delete_property_http_info(request)
        return self._call_api(**http_info)

    def delete_property_async_invoker(self, request):
        http_info = self._delete_property_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_property_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/link/instances/{instance_id}/services/{service_id}/properties/{property_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeletePropertyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'service_id' in local_var_params:
            path_params['service_id'] = local_var_params['service_id']
        if 'property_id' in local_var_params:
            path_params['property_id'] = local_var_params['property_id']

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

    def delete_request_property_async(self, request):
        r"""删除请求属性

        删除请求属性
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteRequestProperty
        :type request: :class:`huaweicloudsdkroma.v2.DeleteRequestPropertyRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.DeleteRequestPropertyResponse`
        """
        http_info = self._delete_request_property_http_info(request)
        return self._call_api(**http_info)

    def delete_request_property_async_invoker(self, request):
        http_info = self._delete_request_property_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_request_property_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/link/instances/{instance_id}/services/{service_id}/commands/{command_id}/requests/{property_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteRequestPropertyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'service_id' in local_var_params:
            path_params['service_id'] = local_var_params['service_id']
        if 'command_id' in local_var_params:
            path_params['command_id'] = local_var_params['command_id']
        if 'property_id' in local_var_params:
            path_params['property_id'] = local_var_params['property_id']

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
        r"""删除流控策略

        删除指定的流控策略。当该流控策略绑定了API时，需要先解除流控策略与API的所有绑定关系后再删除。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteRequestThrottlingPolicyV2
        :type request: :class:`huaweicloudsdkroma.v2.DeleteRequestThrottlingPolicyV2Request`
        :rtype: :class:`huaweicloudsdkroma.v2.DeleteRequestThrottlingPolicyV2Response`
        """
        http_info = self._delete_request_throttling_policy_v2_http_info(request)
        return self._call_api(**http_info)

    def delete_request_throttling_policy_v2_async_invoker(self, request):
        http_info = self._delete_request_throttling_policy_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_request_throttling_policy_v2_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/throttles/{throttle_id}",
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

    def delete_response_property_async(self, request):
        r"""删除响应属性

        删除响应属性
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteResponseProperty
        :type request: :class:`huaweicloudsdkroma.v2.DeleteResponsePropertyRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.DeleteResponsePropertyResponse`
        """
        http_info = self._delete_response_property_http_info(request)
        return self._call_api(**http_info)

    def delete_response_property_async_invoker(self, request):
        http_info = self._delete_response_property_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_response_property_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/link/instances/{instance_id}/services/{service_id}/commands/{command_id}/responses/{property_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteResponsePropertyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'service_id' in local_var_params:
            path_params['service_id'] = local_var_params['service_id']
        if 'command_id' in local_var_params:
            path_params['command_id'] = local_var_params['command_id']
        if 'property_id' in local_var_params:
            path_params['property_id'] = local_var_params['property_id']

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

    def delete_rule_async(self, request):
        r"""删除规则

        删除规则
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteRule
        :type request: :class:`huaweicloudsdkroma.v2.DeleteRuleRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.DeleteRuleResponse`
        """
        http_info = self._delete_rule_http_info(request)
        return self._call_api(**http_info)

    def delete_rule_async_invoker(self, request):
        http_info = self._delete_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_rule_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/link/instances/{instance_id}/rules/{rule_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'rule_id' in local_var_params:
            path_params['rule_id'] = local_var_params['rule_id']

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

    def delete_service_async(self, request):
        r"""删除服务

        删除服务
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteService
        :type request: :class:`huaweicloudsdkroma.v2.DeleteServiceRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.DeleteServiceResponse`
        """
        http_info = self._delete_service_http_info(request)
        return self._call_api(**http_info)

    def delete_service_async_invoker(self, request):
        http_info = self._delete_service_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_service_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/link/instances/{instance_id}/services/{service_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteServiceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'service_id' in local_var_params:
            path_params['service_id'] = local_var_params['service_id']

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
        r"""删除签名密钥

        删除指定的签名密钥。签名密钥绑定了API时无法删除，需要先解除与API的绑定关系后删除。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteSignatureKeyV2
        :type request: :class:`huaweicloudsdkroma.v2.DeleteSignatureKeyV2Request`
        :rtype: :class:`huaweicloudsdkroma.v2.DeleteSignatureKeyV2Response`
        """
        http_info = self._delete_signature_key_v2_http_info(request)
        return self._call_api(**http_info)

    def delete_signature_key_v2_async_invoker(self, request):
        http_info = self._delete_signature_key_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_signature_key_v2_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/signs/{sign_id}",
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

    def delete_source_async(self, request):
        r"""删除源数据源

        删除源数据源
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteSource
        :type request: :class:`huaweicloudsdkroma.v2.DeleteSourceRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.DeleteSourceResponse`
        """
        http_info = self._delete_source_http_info(request)
        return self._call_api(**http_info)

    def delete_source_async_invoker(self, request):
        http_info = self._delete_source_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_source_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/link/instances/{instance_id}/rules/{rule_id}/sources/{source_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteSourceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'rule_id' in local_var_params:
            path_params['rule_id'] = local_var_params['rule_id']
        if 'source_id' in local_var_params:
            path_params['source_id'] = local_var_params['source_id']

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
        r"""删除特殊设置

        删除某个流控策略的某个特殊配置。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteSpecialThrottlingConfigurationV2
        :type request: :class:`huaweicloudsdkroma.v2.DeleteSpecialThrottlingConfigurationV2Request`
        :rtype: :class:`huaweicloudsdkroma.v2.DeleteSpecialThrottlingConfigurationV2Response`
        """
        http_info = self._delete_special_throttling_configuration_v2_http_info(request)
        return self._call_api(**http_info)

    def delete_special_throttling_configuration_v2_async_invoker(self, request):
        http_info = self._delete_special_throttling_configuration_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_special_throttling_configuration_v2_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/throttles/{throttle_id}/throttle-specials/{strategy_id}",
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

    def delete_task_async(self, request):
        r"""通过任务ID删除指定任务

        通过任务ID删除指定任务
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteTask
        :type request: :class:`huaweicloudsdkroma.v2.DeleteTaskRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.DeleteTaskResponse`
        """
        http_info = self._delete_task_http_info(request)
        return self._call_api(**http_info)

    def delete_task_async_invoker(self, request):
        http_info = self._delete_task_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_task_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/fdi/instances/{instance_id}/tasks/{task_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteTaskResponse"
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

    def detach_api_from_plugin_async(self, request):
        r"""解除绑定插件的API

        解除绑定在插件上的API
        - 解绑及时生效
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DetachApiFromPlugin
        :type request: :class:`huaweicloudsdkroma.v2.DetachApiFromPluginRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.DetachApiFromPluginResponse`
        """
        http_info = self._detach_api_from_plugin_http_info(request)
        return self._call_api(**http_info)

    def detach_api_from_plugin_async_invoker(self, request):
        http_info = self._detach_api_from_plugin_http_info(request)
        return AsyncInvoker(self, http_info)

    def _detach_api_from_plugin_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/plugins/{plugin_id}/detach",
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
        r"""解除绑定API的插件

        解除绑定在API上的插件
        - 解绑及时生效
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DetachPluginFromApi
        :type request: :class:`huaweicloudsdkroma.v2.DetachPluginFromApiRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.DetachPluginFromApiResponse`
        """
        http_info = self._detach_plugin_from_api_http_info(request)
        return self._call_api(**http_info)

    def detach_plugin_from_api_async_invoker(self, request):
        http_info = self._detach_plugin_from_api_http_info(request)
        return AsyncInvoker(self, http_info)

    def _detach_plugin_from_api_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/apis/{api_id}/plugins/detach",
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
        r"""解除客户端配额和客户端应用的绑定

        解除客户端配额和客户端应用的绑定
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DisassociateAppQuotaWithApp
        :type request: :class:`huaweicloudsdkroma.v2.DisassociateAppQuotaWithAppRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.DisassociateAppQuotaWithAppResponse`
        """
        http_info = self._disassociate_app_quota_with_app_http_info(request)
        return self._call_api(**http_info)

    def disassociate_app_quota_with_app_async_invoker(self, request):
        http_info = self._disassociate_app_quota_with_app_http_info(request)
        return AsyncInvoker(self, http_info)

    def _disassociate_app_quota_with_app_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/app-quotas/{app_quota_id}/bound-apps/{app_id}",
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
        r"""删除域名证书

        如果域名证书不再需要或者已过期，则可以删除证书内容。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DisassociateCertificateV2
        :type request: :class:`huaweicloudsdkroma.v2.DisassociateCertificateV2Request`
        :rtype: :class:`huaweicloudsdkroma.v2.DisassociateCertificateV2Response`
        """
        http_info = self._disassociate_certificate_v2_http_info(request)
        return self._call_api(**http_info)

    def disassociate_certificate_v2_async_invoker(self, request):
        http_info = self._disassociate_certificate_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _disassociate_certificate_v2_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/api-groups/{group_id}/domains/{domain_id}/certificate/{certificate_id}",
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
        r"""解绑域名

        如果API分组不再需要绑定某个自定义域名，则可以为此API分组解绑此域名。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DisassociateDomainV2
        :type request: :class:`huaweicloudsdkroma.v2.DisassociateDomainV2Request`
        :rtype: :class:`huaweicloudsdkroma.v2.DisassociateDomainV2Response`
        """
        http_info = self._disassociate_domain_v2_http_info(request)
        return self._call_api(**http_info)

    def disassociate_domain_v2_async_invoker(self, request):
        http_info = self._disassociate_domain_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _disassociate_domain_v2_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/api-groups/{group_id}/domains/{domain_id}",
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
        r"""解除绑定

        解除API与签名密钥的绑定关系。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DisassociateSignatureKeyV2
        :type request: :class:`huaweicloudsdkroma.v2.DisassociateSignatureKeyV2Request`
        :rtype: :class:`huaweicloudsdkroma.v2.DisassociateSignatureKeyV2Response`
        """
        http_info = self._disassociate_signature_key_v2_http_info(request)
        return self._call_api(**http_info)

    def disassociate_signature_key_v2_async_invoker(self, request):
        http_info = self._disassociate_signature_key_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _disassociate_signature_key_v2_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/sign-bindings/{sign_bindings_id}",
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

    def download_products_async(self, request):
        r"""导出产品

        导出产品
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DownloadProducts
        :type request: :class:`huaweicloudsdkroma.v2.DownloadProductsRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.DownloadProductsResponse`
        """
        http_info = self._download_products_http_info(request)
        return self._call_api(**http_info)

    def download_products_async_invoker(self, request):
        http_info = self._download_products_http_info(request)
        return AsyncInvoker(self, http_info)

    def _download_products_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/link/instances/{instance_id}/products/export",
            "request_type": request.__class__.__name__,
            "response_type": "DownloadProductsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'product_ids' in local_var_params:
            query_params.append(('product_ids', local_var_params['product_ids']))
            collection_formats['product_ids'] = 'csv'

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

    def export_mqs_instance_topic_async(self, request):
        r"""导出Topic

        导出Topic。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ExportMqsInstanceTopic
        :type request: :class:`huaweicloudsdkroma.v2.ExportMqsInstanceTopicRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.ExportMqsInstanceTopicResponse`
        """
        http_info = self._export_mqs_instance_topic_http_info(request)
        return self._call_api(**http_info)

    def export_mqs_instance_topic_async_invoker(self, request):
        http_info = self._export_mqs_instance_topic_http_info(request)
        return AsyncInvoker(self, http_info)

    def _export_mqs_instance_topic_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/mqs/instances/{instance_id}/topics/export",
            "request_type": request.__class__.__name__,
            "response_type": "ExportMqsInstanceTopicResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def import_mqs_instance_topic_async(self, request):
        r"""导入Topic

        导入Topic。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ImportMqsInstanceTopic
        :type request: :class:`huaweicloudsdkroma.v2.ImportMqsInstanceTopicRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.ImportMqsInstanceTopicResponse`
        """
        http_info = self._import_mqs_instance_topic_http_info(request)
        return self._call_api(**http_info)

    def import_mqs_instance_topic_async_invoker(self, request):
        http_info = self._import_mqs_instance_topic_http_info(request)
        return AsyncInvoker(self, http_info)

    def _import_mqs_instance_topic_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/mqs/instances/{instance_id}/topics/import",
            "request_type": request.__class__.__name__,
            "response_type": "ImportMqsInstanceTopicResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'mode' in local_var_params:
            query_params.append(('mode', local_var_params['mode']))
        if 'prefix' in local_var_params:
            query_params.append(('prefix', local_var_params['prefix']))

        header_params = {}

        form_params = {}
        if 'upload_file_name' in local_var_params:
            form_params['upload_file_name'] = local_var_params['upload_file_name']

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

    def install_multi_tasks_async(self, request):
        r"""组合任务初始化

        初始化组合任务，分配任务ID，初始化映射等
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for InstallMultiTasks
        :type request: :class:`huaweicloudsdkroma.v2.InstallMultiTasksRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.InstallMultiTasksResponse`
        """
        http_info = self._install_multi_tasks_http_info(request)
        return self._call_api(**http_info)

    def install_multi_tasks_async_invoker(self, request):
        http_info = self._install_multi_tasks_http_info(request)
        return AsyncInvoker(self, http_info)

    def _install_multi_tasks_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/fdi/instances/{instance_id}/multi-tasks/init",
            "request_type": request.__class__.__name__,
            "response_type": "InstallMultiTasksResponse"
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
        r"""查询可绑定当前API的插件

        查询可绑定当前API的插件信息。
        - 支持分页返回
        - 支持插件名称模糊查询
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListApiAttachablePlugins
        :type request: :class:`huaweicloudsdkroma.v2.ListApiAttachablePluginsRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.ListApiAttachablePluginsResponse`
        """
        http_info = self._list_api_attachable_plugins_http_info(request)
        return self._call_api(**http_info)

    def list_api_attachable_plugins_async_invoker(self, request):
        http_info = self._list_api_attachable_plugins_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_api_attachable_plugins_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/apis/{api_id}/attachable-plugins",
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
        if 'roma_app_id' in local_var_params:
            query_params.append(('roma_app_id', local_var_params['roma_app_id']))
        if 'roma_app_name' in local_var_params:
            query_params.append(('roma_app_name', local_var_params['roma_app_name']))

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
        r"""查询API下绑定的插件

        查询指定API下绑定的插件信息
        - 用于查询指定API下已经绑定的插件列表信息
        - 支持分页返回
        - 支持插件名称模糊查询
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListApiAttachedPlugins
        :type request: :class:`huaweicloudsdkroma.v2.ListApiAttachedPluginsRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.ListApiAttachedPluginsResponse`
        """
        http_info = self._list_api_attached_plugins_http_info(request)
        return self._call_api(**http_info)

    def list_api_attached_plugins_async_invoker(self, request):
        http_info = self._list_api_attached_plugins_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_api_attached_plugins_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/apis/{api_id}/attached-plugins",
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
        if 'roma_app_id' in local_var_params:
            query_params.append(('roma_app_id', local_var_params['roma_app_id']))
        if 'roma_app_name' in local_var_params:
            query_params.append(('roma_app_name', local_var_params['roma_app_name']))

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
        r"""查看签名密钥绑定的API列表

        查询某个签名密钥上已经绑定的API列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListApisBindedToSignatureKeyV2
        :type request: :class:`huaweicloudsdkroma.v2.ListApisBindedToSignatureKeyV2Request`
        :rtype: :class:`huaweicloudsdkroma.v2.ListApisBindedToSignatureKeyV2Response`
        """
        http_info = self._list_apis_binded_to_signature_key_v2_http_info(request)
        return self._call_api(**http_info)

    def list_apis_binded_to_signature_key_v2_async_invoker(self, request):
        http_info = self._list_apis_binded_to_signature_key_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_apis_binded_to_signature_key_v2_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/sign-bindings/binded-apis",
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
        r"""查看签名密钥未绑定的API列表

        查询所有未绑定到该签名密钥上的API列表。需要API已经发布，未发布的API不予展示。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListApisNotBoundWithSignatureKeyV2
        :type request: :class:`huaweicloudsdkroma.v2.ListApisNotBoundWithSignatureKeyV2Request`
        :rtype: :class:`huaweicloudsdkroma.v2.ListApisNotBoundWithSignatureKeyV2Response`
        """
        http_info = self._list_apis_not_bound_with_signature_key_v2_http_info(request)
        return self._call_api(**http_info)

    def list_apis_not_bound_with_signature_key_v2_async_invoker(self, request):
        http_info = self._list_apis_not_bound_with_signature_key_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_apis_not_bound_with_signature_key_v2_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/sign-bindings/unbinded-apis",
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
        r"""查询APP Code列表

        查询App Code列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAppCodesV2
        :type request: :class:`huaweicloudsdkroma.v2.ListAppCodesV2Request`
        :rtype: :class:`huaweicloudsdkroma.v2.ListAppCodesV2Response`
        """
        http_info = self._list_app_codes_v2_http_info(request)
        return self._call_api(**http_info)

    def list_app_codes_v2_async_invoker(self, request):
        http_info = self._list_app_codes_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_app_codes_v2_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/apps/{app_id}/app-codes",
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

    def list_app_configs_v2_async(self, request):
        r"""查询应用配置列表

        查询应用配置列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAppConfigsV2
        :type request: :class:`huaweicloudsdkroma.v2.ListAppConfigsV2Request`
        :rtype: :class:`huaweicloudsdkroma.v2.ListAppConfigsV2Response`
        """
        http_info = self._list_app_configs_v2_http_info(request)
        return self._call_api(**http_info)

    def list_app_configs_v2_async_invoker(self, request):
        http_info = self._list_app_configs_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_app_configs_v2_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/apps/configs",
            "request_type": request.__class__.__name__,
            "response_type": "ListAppConfigsV2Response"
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
        if 'config_name' in local_var_params:
            query_params.append(('config_name', local_var_params['config_name']))
        if 'roma_app_name' in local_var_params:
            query_params.append(('roma_app_name', local_var_params['roma_app_name']))

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
        r"""查询客户端配额可绑定的客户端应用列表

        查询客户端配额可绑定的客户端应用列表。支持按客户端应用名称模糊搜索
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAppQuotaBindableApps
        :type request: :class:`huaweicloudsdkroma.v2.ListAppQuotaBindableAppsRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.ListAppQuotaBindableAppsResponse`
        """
        http_info = self._list_app_quota_bindable_apps_http_info(request)
        return self._call_api(**http_info)

    def list_app_quota_bindable_apps_async_invoker(self, request):
        http_info = self._list_app_quota_bindable_apps_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_app_quota_bindable_apps_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/app-quotas/{app_quota_id}/bindable-apps",
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
        r"""查询客户端配额已绑定的客户端应用列表

        查询客户端配额已绑定的客户端应用列表。支持按客户端应用名称模糊匹配
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAppQuotaBoundApps
        :type request: :class:`huaweicloudsdkroma.v2.ListAppQuotaBoundAppsRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.ListAppQuotaBoundAppsResponse`
        """
        http_info = self._list_app_quota_bound_apps_http_info(request)
        return self._call_api(**http_info)

    def list_app_quota_bound_apps_async_invoker(self, request):
        http_info = self._list_app_quota_bound_apps_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_app_quota_bound_apps_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/app-quotas/{app_quota_id}/bound-apps",
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
        r"""获取客户端配额列表

        获取客户端配额列表。支持根据名称模糊查询
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAppQuotas
        :type request: :class:`huaweicloudsdkroma.v2.ListAppQuotasRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.ListAppQuotasResponse`
        """
        http_info = self._list_app_quotas_http_info(request)
        return self._call_api(**http_info)

    def list_app_quotas_async_invoker(self, request):
        http_info = self._list_app_quotas_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_app_quotas_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/app-quotas",
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
        r"""查询APP列表

        查询APP列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAppsV2
        :type request: :class:`huaweicloudsdkroma.v2.ListAppsV2Request`
        :rtype: :class:`huaweicloudsdkroma.v2.ListAppsV2Response`
        """
        http_info = self._list_apps_v2_http_info(request)
        return self._call_api(**http_info)

    def list_apps_v2_async_invoker(self, request):
        http_info = self._list_apps_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_apps_v2_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/apps",
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

    def list_commands_async(self, request):
        r"""查询命令

        查询命令
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListCommands
        :type request: :class:`huaweicloudsdkroma.v2.ListCommandsRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.ListCommandsResponse`
        """
        http_info = self._list_commands_http_info(request)
        return self._call_api(**http_info)

    def list_commands_async_invoker(self, request):
        http_info = self._list_commands_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_commands_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/link/instances/{instance_id}/services/{service_id}/commands",
            "request_type": request.__class__.__name__,
            "response_type": "ListCommandsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'service_id' in local_var_params:
            path_params['service_id'] = local_var_params['service_id']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'command_id' in local_var_params:
            query_params.append(('command_id', local_var_params['command_id']))
        if 'command_name' in local_var_params:
            query_params.append(('command_name', local_var_params['command_name']))
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

    def list_custom_authorizers_v2_async(self, request):
        r"""查询自定义认证列表

        查询自定义认证列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListCustomAuthorizersV2
        :type request: :class:`huaweicloudsdkroma.v2.ListCustomAuthorizersV2Request`
        :rtype: :class:`huaweicloudsdkroma.v2.ListCustomAuthorizersV2Response`
        """
        http_info = self._list_custom_authorizers_v2_http_info(request)
        return self._call_api(**http_info)

    def list_custom_authorizers_v2_async_invoker(self, request):
        http_info = self._list_custom_authorizers_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_custom_authorizers_v2_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/authorizers",
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

    def list_datasource_columns_async(self, request):
        r"""获取数据源中某个表中所有字段

        获取数据源中中某个表中所有字段
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListDatasourceColumns
        :type request: :class:`huaweicloudsdkroma.v2.ListDatasourceColumnsRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.ListDatasourceColumnsResponse`
        """
        http_info = self._list_datasource_columns_http_info(request)
        return self._call_api(**http_info)

    def list_datasource_columns_async_invoker(self, request):
        http_info = self._list_datasource_columns_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_datasource_columns_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/fdi/instances/{instance_id}/datasources/{datasource_id}/columns",
            "request_type": request.__class__.__name__,
            "response_type": "ListDatasourceColumnsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'datasource_id' in local_var_params:
            path_params['datasource_id'] = local_var_params['datasource_id']

        query_params = []
        if 'position' in local_var_params:
            query_params.append(('position', local_var_params['position']))
        if 'db_name' in local_var_params:
            query_params.append(('db_name', local_var_params['db_name']))
        if 'table_name' in local_var_params:
            query_params.append(('table_name', local_var_params['table_name']))

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

    def list_datasource_tables_async(self, request):
        r"""获取数据源中所有的表

        获取数据源中所有的表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListDatasourceTables
        :type request: :class:`huaweicloudsdkroma.v2.ListDatasourceTablesRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.ListDatasourceTablesResponse`
        """
        http_info = self._list_datasource_tables_http_info(request)
        return self._call_api(**http_info)

    def list_datasource_tables_async_invoker(self, request):
        http_info = self._list_datasource_tables_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_datasource_tables_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/fdi/instances/{instance_id}/datasources/{datasource_id}/tables",
            "request_type": request.__class__.__name__,
            "response_type": "ListDatasourceTablesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'datasource_id' in local_var_params:
            path_params['datasource_id'] = local_var_params['datasource_id']

        query_params = []
        if 'position' in local_var_params:
            query_params.append(('position', local_var_params['position']))
        if 'db_name' in local_var_params:
            query_params.append(('db_name', local_var_params['db_name']))
        if 'db_schema' in local_var_params:
            query_params.append(('db_schema', local_var_params['db_schema']))
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

    def list_datasources_async(self, request):
        r"""查询数据源

        查询数据源
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListDatasources
        :type request: :class:`huaweicloudsdkroma.v2.ListDatasourcesRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.ListDatasourcesResponse`
        """
        http_info = self._list_datasources_http_info(request)
        return self._call_api(**http_info)

    def list_datasources_async_invoker(self, request):
        http_info = self._list_datasources_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_datasources_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/fdi/instances/{instance_id}/datasources",
            "request_type": request.__class__.__name__,
            "response_type": "ListDatasourcesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'datasource_type' in local_var_params:
            query_params.append(('datasource_type', local_var_params['datasource_type']))
        if 'sort_field' in local_var_params:
            query_params.append(('sort_field', local_var_params['sort_field']))
        if 'sort_type' in local_var_params:
            query_params.append(('sort_type', local_var_params['sort_type']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'app_id' in local_var_params:
            query_params.append(('app_id', local_var_params['app_id']))
        if 'custom_plugin_id' in local_var_params:
            query_params.append(('custom_plugin_id', local_var_params['custom_plugin_id']))

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

    def list_destinations_async(self, request):
        r"""查询目标数据源列表

        查询目标数据源列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListDestinations
        :type request: :class:`huaweicloudsdkroma.v2.ListDestinationsRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.ListDestinationsResponse`
        """
        http_info = self._list_destinations_http_info(request)
        return self._call_api(**http_info)

    def list_destinations_async_invoker(self, request):
        http_info = self._list_destinations_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_destinations_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/link/instances/{instance_id}/rules/{rule_id}/destinations",
            "request_type": request.__class__.__name__,
            "response_type": "ListDestinationsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'rule_id' in local_var_params:
            path_params['rule_id'] = local_var_params['rule_id']

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

    def list_devices_async(self, request):
        r"""查询设备

        查询设备
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListDevices
        :type request: :class:`huaweicloudsdkroma.v2.ListDevicesRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.ListDevicesResponse`
        """
        http_info = self._list_devices_http_info(request)
        return self._call_api(**http_info)

    def list_devices_async_invoker(self, request):
        http_info = self._list_devices_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_devices_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/link/instances/{instance_id}/devices",
            "request_type": request.__class__.__name__,
            "response_type": "ListDevicesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'app_id' in local_var_params:
            query_params.append(('app_id', local_var_params['app_id']))
        if 'product_id' in local_var_params:
            query_params.append(('product_id', local_var_params['product_id']))
        if 'product_name' in local_var_params:
            query_params.append(('product_name', local_var_params['product_name']))
        if 'device_name' in local_var_params:
            query_params.append(('device_name', local_var_params['device_name']))
        if 'client_id' in local_var_params:
            query_params.append(('client_id', local_var_params['client_id']))
        if 'node_id' in local_var_params:
            query_params.append(('node_id', local_var_params['node_id']))
        if 'node_type' in local_var_params:
            query_params.append(('node_type', local_var_params['node_type']))
        if 'online_status' in local_var_params:
            query_params.append(('online_status', local_var_params['online_status']))
        if 'created_date_start' in local_var_params:
            query_params.append(('created_date_start', local_var_params['created_date_start']))
        if 'created_date_end' in local_var_params:
            query_params.append(('created_date_end', local_var_params['created_date_end']))
        if 'tag' in local_var_params:
            query_params.append(('tag', local_var_params['tag']))

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

    def list_devices_in_product_async(self, request):
        r"""查询产品内设备数量

        查询产品内设备数量
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListDevicesInProduct
        :type request: :class:`huaweicloudsdkroma.v2.ListDevicesInProductRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.ListDevicesInProductResponse`
        """
        http_info = self._list_devices_in_product_http_info(request)
        return self._call_api(**http_info)

    def list_devices_in_product_async_invoker(self, request):
        http_info = self._list_devices_in_product_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_devices_in_product_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/link/instances/{instance_id}/products/{product_id}/devices-summary",
            "request_type": request.__class__.__name__,
            "response_type": "ListDevicesInProductResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'product_id' in local_var_params:
            path_params['product_id'] = local_var_params['product_id']

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

    def list_environment_variables_v2_async(self, request):
        r"""查询变量列表

        查询分组下的所有环境变量的列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListEnvironmentVariablesV2
        :type request: :class:`huaweicloudsdkroma.v2.ListEnvironmentVariablesV2Request`
        :rtype: :class:`huaweicloudsdkroma.v2.ListEnvironmentVariablesV2Response`
        """
        http_info = self._list_environment_variables_v2_http_info(request)
        return self._call_api(**http_info)

    def list_environment_variables_v2_async_invoker(self, request):
        http_info = self._list_environment_variables_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_environment_variables_v2_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/env-variables",
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
        r"""查询环境列表

        查询符合条件的环境列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListEnvironmentsV2
        :type request: :class:`huaweicloudsdkroma.v2.ListEnvironmentsV2Request`
        :rtype: :class:`huaweicloudsdkroma.v2.ListEnvironmentsV2Response`
        """
        http_info = self._list_environments_v2_http_info(request)
        return self._call_api(**http_info)

    def list_environments_v2_async_invoker(self, request):
        http_info = self._list_environments_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_environments_v2_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/envs",
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
        r"""查看实例特性列表

        查看实例特性列表。注意：实例不支持以下特性的需要联系技术支持升级实例版本。
        
        支持配置的特性列表及特性配置请参考“附录 &gt; 实例支持的APIC特性”
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListFeaturesV2
        :type request: :class:`huaweicloudsdkroma.v2.ListFeaturesV2Request`
        :rtype: :class:`huaweicloudsdkroma.v2.ListFeaturesV2Response`
        """
        http_info = self._list_features_v2_http_info(request)
        return self._call_api(**http_info)

    def list_features_v2_async_invoker(self, request):
        http_info = self._list_features_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_features_v2_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/features",
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

    def list_lately_api_statistics_v2_async(self, request):
        r"""API指标统计值查询-最近一段时间

        根据API的id和最近的一段时间查询API被调用的次数，统计周期为1分钟。查询范围一小时以内，一分钟一个样本，其样本值为一分钟内的累计值。
        &gt; 为了安全起见，在服务器上使用curl命令调用接口查询信息后，需要清理历史操作记录，包括但不限于“~/.bash_history”、“/var/log/messages”（如有）。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListLatelyApiStatisticsV2
        :type request: :class:`huaweicloudsdkroma.v2.ListLatelyApiStatisticsV2Request`
        :rtype: :class:`huaweicloudsdkroma.v2.ListLatelyApiStatisticsV2Response`
        """
        http_info = self._list_lately_api_statistics_v2_http_info(request)
        return self._call_api(**http_info)

    def list_lately_api_statistics_v2_async_invoker(self, request):
        http_info = self._list_lately_api_statistics_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_lately_api_statistics_v2_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/statistics/api/latest",
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

    def list_live_data_api_deployment_history_v2_async(self, request):
        r"""查询后端API部署历史

        在某个实例中查询后端API的部署记录。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListLiveDataApiDeploymentHistoryV2
        :type request: :class:`huaweicloudsdkroma.v2.ListLiveDataApiDeploymentHistoryV2Request`
        :rtype: :class:`huaweicloudsdkroma.v2.ListLiveDataApiDeploymentHistoryV2Response`
        """
        http_info = self._list_live_data_api_deployment_history_v2_http_info(request)
        return self._call_api(**http_info)

    def list_live_data_api_deployment_history_v2_async_invoker(self, request):
        http_info = self._list_live_data_api_deployment_history_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_live_data_api_deployment_history_v2_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/livedata-apis/{ld_api_id}/deploy",
            "request_type": request.__class__.__name__,
            "response_type": "ListLiveDataApiDeploymentHistoryV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'ld_api_id' in local_var_params:
            path_params['ld_api_id'] = local_var_params['ld_api_id']

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

    def list_live_data_api_test_history_v2_async(self, request):
        r"""查询后端API测试结果

        在某个实例中查询后端API的测试结果。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListLiveDataApiTestHistoryV2
        :type request: :class:`huaweicloudsdkroma.v2.ListLiveDataApiTestHistoryV2Request`
        :rtype: :class:`huaweicloudsdkroma.v2.ListLiveDataApiTestHistoryV2Response`
        """
        http_info = self._list_live_data_api_test_history_v2_http_info(request)
        return self._call_api(**http_info)

    def list_live_data_api_test_history_v2_async_invoker(self, request):
        http_info = self._list_live_data_api_test_history_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_live_data_api_test_history_v2_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/livedata-apis/{ld_api_id}/test",
            "request_type": request.__class__.__name__,
            "response_type": "ListLiveDataApiTestHistoryV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'ld_api_id' in local_var_params:
            path_params['ld_api_id'] = local_var_params['ld_api_id']

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

    def list_live_data_api_v2_async(self, request):
        r"""查询后端API列表

        获取某个实例下的所有后端API。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListLiveDataApiV2
        :type request: :class:`huaweicloudsdkroma.v2.ListLiveDataApiV2Request`
        :rtype: :class:`huaweicloudsdkroma.v2.ListLiveDataApiV2Response`
        """
        http_info = self._list_live_data_api_v2_http_info(request)
        return self._call_api(**http_info)

    def list_live_data_api_v2_async_invoker(self, request):
        http_info = self._list_live_data_api_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_live_data_api_v2_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/livedata-apis",
            "request_type": request.__class__.__name__,
            "response_type": "ListLiveDataApiV2Response"
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
        if 'app_name' in local_var_params:
            query_params.append(('app_name', local_var_params['app_name']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'path' in local_var_params:
            query_params.append(('path', local_var_params['path']))
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

    def list_live_data_data_sources_v2_async(self, request):
        r"""查询自定义后端服务数据源列表

        查询自定义后端服务数据源列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListLiveDataDataSourcesV2
        :type request: :class:`huaweicloudsdkroma.v2.ListLiveDataDataSourcesV2Request`
        :rtype: :class:`huaweicloudsdkroma.v2.ListLiveDataDataSourcesV2Response`
        """
        http_info = self._list_live_data_data_sources_v2_http_info(request)
        return self._call_api(**http_info)

    def list_live_data_data_sources_v2_async_invoker(self, request):
        http_info = self._list_live_data_data_sources_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_live_data_data_sources_v2_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/data-sources",
            "request_type": request.__class__.__name__,
            "response_type": "ListLiveDataDataSourcesV2Response"
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

    def list_live_data_quota_v2_async(self, request):
        r"""查询自定义后端服务配额

        查询自定义后端服务配额。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListLiveDataQuotaV2
        :type request: :class:`huaweicloudsdkroma.v2.ListLiveDataQuotaV2Request`
        :rtype: :class:`huaweicloudsdkroma.v2.ListLiveDataQuotaV2Response`
        """
        http_info = self._list_live_data_quota_v2_http_info(request)
        return self._call_api(**http_info)

    def list_live_data_quota_v2_async_invoker(self, request):
        http_info = self._list_live_data_quota_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_live_data_quota_v2_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/livedata-quota",
            "request_type": request.__class__.__name__,
            "response_type": "ListLiveDataQuotaV2Response"
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

    def list_monitor_infos_async(self, request):
        r"""任务监控信息列表查询

        查询所有任务的监控信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListMonitorInfos
        :type request: :class:`huaweicloudsdkroma.v2.ListMonitorInfosRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.ListMonitorInfosResponse`
        """
        http_info = self._list_monitor_infos_http_info(request)
        return self._call_api(**http_info)

    def list_monitor_infos_async_invoker(self, request):
        http_info = self._list_monitor_infos_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_monitor_infos_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/fdi/instances/{instance_id}/task-monitors",
            "request_type": request.__class__.__name__,
            "response_type": "ListMonitorInfosResponse"
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
        if 'task_name' in local_var_params:
            query_params.append(('task_name', local_var_params['task_name']))
        if 'execute_status' in local_var_params:
            query_params.append(('execute_status', local_var_params['execute_status']))

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

    def list_monitor_log_async(self, request):
        r"""任务监控日志查询

        查询单个任务的所有日志信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListMonitorLog
        :type request: :class:`huaweicloudsdkroma.v2.ListMonitorLogRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.ListMonitorLogResponse`
        """
        http_info = self._list_monitor_log_http_info(request)
        return self._call_api(**http_info)

    def list_monitor_log_async_invoker(self, request):
        http_info = self._list_monitor_log_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_monitor_log_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/fdi/instances/{instance_id}/tasks/{task_id}/monitor-logs",
            "request_type": request.__class__.__name__,
            "response_type": "ListMonitorLogResponse"
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
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'begin_time' in local_var_params:
            query_params.append(('begin_time', local_var_params['begin_time']))
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

    def list_mqs_instance_topics_async(self, request):
        r"""查询Topic列表

        查询Topic列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListMqsInstanceTopics
        :type request: :class:`huaweicloudsdkroma.v2.ListMqsInstanceTopicsRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.ListMqsInstanceTopicsResponse`
        """
        http_info = self._list_mqs_instance_topics_http_info(request)
        return self._call_api(**http_info)

    def list_mqs_instance_topics_async_invoker(self, request):
        http_info = self._list_mqs_instance_topics_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_mqs_instance_topics_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/mqs/instances/{instance_id}/topics",
            "request_type": request.__class__.__name__,
            "response_type": "ListMqsInstanceTopicsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'app_name' in local_var_params:
            query_params.append(('app_name', local_var_params['app_name']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'access_policy' in local_var_params:
            query_params.append(('access_policy', local_var_params['access_policy']))
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

    def list_notification_async(self, request):
        r"""查询订阅管理信息

        该接口用于查询指定应用订阅管理信息的数据
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListNotification
        :type request: :class:`huaweicloudsdkroma.v2.ListNotificationRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.ListNotificationResponse`
        """
        http_info = self._list_notification_http_info(request)
        return self._call_api(**http_info)

    def list_notification_async_invoker(self, request):
        http_info = self._list_notification_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_notification_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/link/instances/{instance_id}/notifications",
            "request_type": request.__class__.__name__,
            "response_type": "ListNotificationResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'app_id' in local_var_params:
            query_params.append(('app_id', local_var_params['app_id']))

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
        r"""查询可绑定当前插件的API

        查询可绑定当前插件的API信息。
        - 支持分页返回
        - 支持API名称模糊查询
        - 支持已绑定其他插件的API查询返回
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListPluginAttachableApis
        :type request: :class:`huaweicloudsdkroma.v2.ListPluginAttachableApisRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.ListPluginAttachableApisResponse`
        """
        http_info = self._list_plugin_attachable_apis_http_info(request)
        return self._call_api(**http_info)

    def list_plugin_attachable_apis_async_invoker(self, request):
        http_info = self._list_plugin_attachable_apis_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_plugin_attachable_apis_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/plugins/{plugin_id}/attachable-apis",
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
        r"""查询插件下绑定的API

        查询指定插件下绑定的API信息
        - 用于查询指定插件下已经绑定的API列表信息
        - 支持分页返回
        - 支持API名称模糊查询
        - 绑定关系列表中返回的API在对应的环境中可能已经下线
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListPluginAttachedApis
        :type request: :class:`huaweicloudsdkroma.v2.ListPluginAttachedApisRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.ListPluginAttachedApisResponse`
        """
        http_info = self._list_plugin_attached_apis_http_info(request)
        return self._call_api(**http_info)

    def list_plugin_attached_apis_async_invoker(self, request):
        http_info = self._list_plugin_attached_apis_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_plugin_attached_apis_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/plugins/{plugin_id}/attached-apis",
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
        r"""查询插件列表

        查询一组符合条件的API网关插件详情。
        - 支持分页
        - 支持根据插件类型查询
        - 支持根据插件可见范围查询
        - 支持根据插件编码查询
        - 支持根据名称模糊查询
        - 支持根据集成应用编号查询
        - 支持根据集成应用名称查询
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListPlugins
        :type request: :class:`huaweicloudsdkroma.v2.ListPluginsRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.ListPluginsResponse`
        """
        http_info = self._list_plugins_http_info(request)
        return self._call_api(**http_info)

    def list_plugins_async_invoker(self, request):
        http_info = self._list_plugins_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_plugins_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/plugins",
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
        if 'roma_app_id' in local_var_params:
            query_params.append(('roma_app_id', local_var_params['roma_app_id']))
        if 'roma_app_name' in local_var_params:
            query_params.append(('roma_app_name', local_var_params['roma_app_name']))

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

    def list_product_templates_async(self, request):
        r"""查询产品模板

        查询产品模板
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListProductTemplates
        :type request: :class:`huaweicloudsdkroma.v2.ListProductTemplatesRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.ListProductTemplatesResponse`
        """
        http_info = self._list_product_templates_http_info(request)
        return self._call_api(**http_info)

    def list_product_templates_async_invoker(self, request):
        http_info = self._list_product_templates_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_product_templates_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/link/instances/{instance_id}/product-templates",
            "request_type": request.__class__.__name__,
            "response_type": "ListProductTemplatesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'created_user_name' in local_var_params:
            query_params.append(('created_user_name', local_var_params['created_user_name']))
        if 'created_date_start' in local_var_params:
            query_params.append(('created_date_start', local_var_params['created_date_start']))
        if 'created_date_end' in local_var_params:
            query_params.append(('created_date_end', local_var_params['created_date_end']))
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

    def list_product_topics_async(self, request):
        r"""查询产品主题

        查询产品主题
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListProductTopics
        :type request: :class:`huaweicloudsdkroma.v2.ListProductTopicsRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.ListProductTopicsResponse`
        """
        http_info = self._list_product_topics_http_info(request)
        return self._call_api(**http_info)

    def list_product_topics_async_invoker(self, request):
        http_info = self._list_product_topics_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_product_topics_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/link/instances/{instance_id}/products/{product_id}/topics",
            "request_type": request.__class__.__name__,
            "response_type": "ListProductTopicsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'product_id' in local_var_params:
            path_params['product_id'] = local_var_params['product_id']

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

    def list_products_async(self, request):
        r"""查询产品

        查询产品
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListProducts
        :type request: :class:`huaweicloudsdkroma.v2.ListProductsRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.ListProductsResponse`
        """
        http_info = self._list_products_http_info(request)
        return self._call_api(**http_info)

    def list_products_async_invoker(self, request):
        http_info = self._list_products_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_products_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/link/instances/{instance_id}/products",
            "request_type": request.__class__.__name__,
            "response_type": "ListProductsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'app_id' in local_var_params:
            query_params.append(('app_id', local_var_params['app_id']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'manufacturer_id' in local_var_params:
            query_params.append(('manufacturer_id', local_var_params['manufacturer_id']))
        if 'manufacturer_name' in local_var_params:
            query_params.append(('manufacturer_name', local_var_params['manufacturer_name']))
        if 'model' in local_var_params:
            query_params.append(('model', local_var_params['model']))
        if 'device_type' in local_var_params:
            query_params.append(('device_type', local_var_params['device_type']))
        if 'product_type' in local_var_params:
            query_params.append(('product_type', local_var_params['product_type']))
        if 'protocol_type' in local_var_params:
            query_params.append(('protocol_type', local_var_params['protocol_type']))
        if 'created_user_name' in local_var_params:
            query_params.append(('created_user_name', local_var_params['created_user_name']))
        if 'created_date_start' in local_var_params:
            query_params.append(('created_date_start', local_var_params['created_date_start']))
        if 'created_date_end' in local_var_params:
            query_params.append(('created_date_end', local_var_params['created_date_end']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'app_name' in local_var_params:
            query_params.append(('app_name', local_var_params['app_name']))
        if 'product_serial' in local_var_params:
            query_params.append(('product_serial', local_var_params['product_serial']))

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
        r"""查询某个实例的租户配置列表

        查询某个实例的租户配置列表，用户可以通过此接口查看各类型资源配置及使用情况。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListProjectCofigsV2
        :type request: :class:`huaweicloudsdkroma.v2.ListProjectCofigsV2Request`
        :rtype: :class:`huaweicloudsdkroma.v2.ListProjectCofigsV2Response`
        """
        http_info = self._list_project_cofigs_v2_http_info(request)
        return self._call_api(**http_info)

    def list_project_cofigs_v2_async_invoker(self, request):
        http_info = self._list_project_cofigs_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_project_cofigs_v2_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/project/configs",
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

    def list_properties_async(self, request):
        r"""查询属性

        查询属性
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListProperties
        :type request: :class:`huaweicloudsdkroma.v2.ListPropertiesRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.ListPropertiesResponse`
        """
        http_info = self._list_properties_http_info(request)
        return self._call_api(**http_info)

    def list_properties_async_invoker(self, request):
        http_info = self._list_properties_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_properties_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/link/instances/{instance_id}/services/{service_id}/properties",
            "request_type": request.__class__.__name__,
            "response_type": "ListPropertiesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'service_id' in local_var_params:
            path_params['service_id'] = local_var_params['service_id']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'property_id' in local_var_params:
            query_params.append(('property_id', local_var_params['property_id']))
        if 'property_name' in local_var_params:
            query_params.append(('property_name', local_var_params['property_name']))
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

    def list_request_properties_async(self, request):
        r"""查询请求属性

        查询请求属性
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListRequestProperties
        :type request: :class:`huaweicloudsdkroma.v2.ListRequestPropertiesRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.ListRequestPropertiesResponse`
        """
        http_info = self._list_request_properties_http_info(request)
        return self._call_api(**http_info)

    def list_request_properties_async_invoker(self, request):
        http_info = self._list_request_properties_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_request_properties_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/link/instances/{instance_id}/services/{service_id}/commands/{command_id}/requests",
            "request_type": request.__class__.__name__,
            "response_type": "ListRequestPropertiesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'service_id' in local_var_params:
            path_params['service_id'] = local_var_params['service_id']
        if 'command_id' in local_var_params:
            path_params['command_id'] = local_var_params['command_id']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'request_id' in local_var_params:
            query_params.append(('request_id', local_var_params['request_id']))
        if 'request_name' in local_var_params:
            query_params.append(('request_name', local_var_params['request_name']))
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

    def list_request_throttling_policy_v2_async(self, request):
        r"""查询流控策略列表

        查询所有流控策略的信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListRequestThrottlingPolicyV2
        :type request: :class:`huaweicloudsdkroma.v2.ListRequestThrottlingPolicyV2Request`
        :rtype: :class:`huaweicloudsdkroma.v2.ListRequestThrottlingPolicyV2Response`
        """
        http_info = self._list_request_throttling_policy_v2_http_info(request)
        return self._call_api(**http_info)

    def list_request_throttling_policy_v2_async_invoker(self, request):
        http_info = self._list_request_throttling_policy_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_request_throttling_policy_v2_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/throttles",
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

    def list_response_properties_async(self, request):
        r"""查询响应属性

        查询响应属性
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListResponseProperties
        :type request: :class:`huaweicloudsdkroma.v2.ListResponsePropertiesRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.ListResponsePropertiesResponse`
        """
        http_info = self._list_response_properties_http_info(request)
        return self._call_api(**http_info)

    def list_response_properties_async_invoker(self, request):
        http_info = self._list_response_properties_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_response_properties_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/link/instances/{instance_id}/services/{service_id}/commands/{command_id}/responses",
            "request_type": request.__class__.__name__,
            "response_type": "ListResponsePropertiesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'service_id' in local_var_params:
            path_params['service_id'] = local_var_params['service_id']
        if 'command_id' in local_var_params:
            path_params['command_id'] = local_var_params['command_id']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'response_id' in local_var_params:
            query_params.append(('response_id', local_var_params['response_id']))
        if 'response_name' in local_var_params:
            query_params.append(('response_name', local_var_params['response_name']))
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

    def list_rules_async(self, request):
        r"""查询规则

        查询规则
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListRules
        :type request: :class:`huaweicloudsdkroma.v2.ListRulesRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.ListRulesResponse`
        """
        http_info = self._list_rules_http_info(request)
        return self._call_api(**http_info)

    def list_rules_async_invoker(self, request):
        http_info = self._list_rules_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_rules_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/link/instances/{instance_id}/rules",
            "request_type": request.__class__.__name__,
            "response_type": "ListRulesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'app_id' in local_var_params:
            query_params.append(('app_id', local_var_params['app_id']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
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

    def list_services_async(self, request):
        r"""查询服务

        查询服务
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListServices
        :type request: :class:`huaweicloudsdkroma.v2.ListServicesRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.ListServicesResponse`
        """
        http_info = self._list_services_http_info(request)
        return self._call_api(**http_info)

    def list_services_async_invoker(self, request):
        http_info = self._list_services_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_services_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/link/instances/{instance_id}/services",
            "request_type": request.__class__.__name__,
            "response_type": "ListServicesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'service_id' in local_var_params:
            query_params.append(('service_id', local_var_params['service_id']))
        if 'service_name' in local_var_params:
            query_params.append(('service_name', local_var_params['service_name']))
        if 'product_template_id' in local_var_params:
            query_params.append(('product_template_id', local_var_params['product_template_id']))
        if 'product_id' in local_var_params:
            query_params.append(('product_id', local_var_params['product_id']))
        if 'created_user_name' in local_var_params:
            query_params.append(('created_user_name', local_var_params['created_user_name']))
        if 'created_date_start' in local_var_params:
            query_params.append(('created_date_start', local_var_params['created_date_start']))
        if 'created_date_end' in local_var_params:
            query_params.append(('created_date_end', local_var_params['created_date_end']))
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

    def list_shadows_async(self, request):
        r"""查询设备影子

        查询设备影子
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListShadows
        :type request: :class:`huaweicloudsdkroma.v2.ListShadowsRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.ListShadowsResponse`
        """
        http_info = self._list_shadows_http_info(request)
        return self._call_api(**http_info)

    def list_shadows_async_invoker(self, request):
        http_info = self._list_shadows_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_shadows_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/link/instances/{instance_id}/devices/{device_id}/shadow",
            "request_type": request.__class__.__name__,
            "response_type": "ListShadowsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'device_id' in local_var_params:
            path_params['device_id'] = local_var_params['device_id']

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

    def list_signature_keys_binded_to_api_v2_async(self, request):
        r"""查看API绑定的签名密钥列表

        查询某个API绑定的签名密钥列表。每个API在每个环境上应该最多只会绑定一个签名密钥。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListSignatureKeysBindedToApiV2
        :type request: :class:`huaweicloudsdkroma.v2.ListSignatureKeysBindedToApiV2Request`
        :rtype: :class:`huaweicloudsdkroma.v2.ListSignatureKeysBindedToApiV2Response`
        """
        http_info = self._list_signature_keys_binded_to_api_v2_http_info(request)
        return self._call_api(**http_info)

    def list_signature_keys_binded_to_api_v2_async_invoker(self, request):
        http_info = self._list_signature_keys_binded_to_api_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_signature_keys_binded_to_api_v2_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/sign-bindings/binded-signs",
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
        r"""查询签名密钥列表

        查询所有签名密钥的信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListSignatureKeysV2
        :type request: :class:`huaweicloudsdkroma.v2.ListSignatureKeysV2Request`
        :rtype: :class:`huaweicloudsdkroma.v2.ListSignatureKeysV2Response`
        """
        http_info = self._list_signature_keys_v2_http_info(request)
        return self._call_api(**http_info)

    def list_signature_keys_v2_async_invoker(self, request):
        http_info = self._list_signature_keys_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_signature_keys_v2_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/signs",
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

    def list_sources_async(self, request):
        r"""查询源数据源列表

        查询源数据源列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListSources
        :type request: :class:`huaweicloudsdkroma.v2.ListSourcesRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.ListSourcesResponse`
        """
        http_info = self._list_sources_http_info(request)
        return self._call_api(**http_info)

    def list_sources_async_invoker(self, request):
        http_info = self._list_sources_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_sources_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/link/instances/{instance_id}/rules/{rule_id}/sources",
            "request_type": request.__class__.__name__,
            "response_type": "ListSourcesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'rule_id' in local_var_params:
            path_params['rule_id'] = local_var_params['rule_id']

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

    def list_special_throttling_configurations_v2_async(self, request):
        r"""查看特殊设置列表

        查看给流控策略设置的特殊配置。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListSpecialThrottlingConfigurationsV2
        :type request: :class:`huaweicloudsdkroma.v2.ListSpecialThrottlingConfigurationsV2Request`
        :rtype: :class:`huaweicloudsdkroma.v2.ListSpecialThrottlingConfigurationsV2Response`
        """
        http_info = self._list_special_throttling_configurations_v2_http_info(request)
        return self._call_api(**http_info)

    def list_special_throttling_configurations_v2_async_invoker(self, request):
        http_info = self._list_special_throttling_configurations_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_special_throttling_configurations_v2_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/throttles/{throttle_id}/throttle-specials",
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

    def list_statistics_api_async(self, request):
        r"""查询API指标统计值

        查询某个实例下的API统计信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListStatisticsApi
        :type request: :class:`huaweicloudsdkroma.v2.ListStatisticsApiRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.ListStatisticsApiResponse`
        """
        http_info = self._list_statistics_api_http_info(request)
        return self._call_api(**http_info)

    def list_statistics_api_async_invoker(self, request):
        http_info = self._list_statistics_api_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_statistics_api_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/statistics/api",
            "request_type": request.__class__.__name__,
            "response_type": "ListStatisticsApiResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'mode' in local_var_params:
            query_params.append(('mode', local_var_params['mode']))
        if 'roma_app_id' in local_var_params:
            query_params.append(('roma_app_id', local_var_params['roma_app_id']))
        if 'api_id' in local_var_params:
            query_params.append(('api_id', local_var_params['api_id']))
        if 'cycle' in local_var_params:
            query_params.append(('cycle', local_var_params['cycle']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
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

    def list_subsets_async(self, request):
        r"""查询子设备

        查询子设备
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListSubsets
        :type request: :class:`huaweicloudsdkroma.v2.ListSubsetsRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.ListSubsetsResponse`
        """
        http_info = self._list_subsets_http_info(request)
        return self._call_api(**http_info)

    def list_subsets_async_invoker(self, request):
        http_info = self._list_subsets_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_subsets_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/link/instances/{instance_id}/devices/{device_id}/subsets",
            "request_type": request.__class__.__name__,
            "response_type": "ListSubsetsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'device_id' in local_var_params:
            path_params['device_id'] = local_var_params['device_id']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'device_name' in local_var_params:
            query_params.append(('device_name', local_var_params['device_name']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'online_status' in local_var_params:
            query_params.append(('online_status', local_var_params['online_status']))
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

    def list_tags_v2_async(self, request):
        r"""查询标签列表

        查询标签列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListTagsV2
        :type request: :class:`huaweicloudsdkroma.v2.ListTagsV2Request`
        :rtype: :class:`huaweicloudsdkroma.v2.ListTagsV2Response`
        """
        http_info = self._list_tags_v2_http_info(request)
        return self._call_api(**http_info)

    def list_tags_v2_async_invoker(self, request):
        http_info = self._list_tags_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_tags_v2_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/tags",
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

    def list_tasks_async(self, request):
        r"""查询任务列表

        查询任务列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListTasks
        :type request: :class:`huaweicloudsdkroma.v2.ListTasksRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.ListTasksResponse`
        """
        http_info = self._list_tasks_http_info(request)
        return self._call_api(**http_info)

    def list_tasks_async_invoker(self, request):
        http_info = self._list_tasks_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_tasks_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/fdi/instances/{instance_id}/tasks",
            "request_type": request.__class__.__name__,
            "response_type": "ListTasksResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'task_id' in local_var_params:
            query_params.append(('task_id', local_var_params['task_id']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'task_type' in local_var_params:
            query_params.append(('task_type', local_var_params['task_type']))
        if 'source_datasource_id' in local_var_params:
            query_params.append(('source_datasource_id', local_var_params['source_datasource_id']))
        if 'target_datasource_id' in local_var_params:
            query_params.append(('target_datasource_id', local_var_params['target_datasource_id']))
        if 'sort_field' in local_var_params:
            query_params.append(('sort_field', local_var_params['sort_field']))
        if 'sort_type' in local_var_params:
            query_params.append(('sort_type', local_var_params['sort_type']))
        if 'execute_status' in local_var_params:
            query_params.append(('execute_status', local_var_params['execute_status']))
        if 'source_app_id' in local_var_params:
            query_params.append(('source_app_id', local_var_params['source_app_id']))
        if 'target_app_id' in local_var_params:
            query_params.append(('target_app_id', local_var_params['target_app_id']))
        if 'task_tag' in local_var_params:
            query_params.append(('task_tag', local_var_params['task_tag']))

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

    def list_topics_async(self, request):
        r"""查询设备主题

        查询设备主题
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListTopics
        :type request: :class:`huaweicloudsdkroma.v2.ListTopicsRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.ListTopicsResponse`
        """
        http_info = self._list_topics_http_info(request)
        return self._call_api(**http_info)

    def list_topics_async_invoker(self, request):
        http_info = self._list_topics_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_topics_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/link/instances/{instance_id}/devices/{device_id}/topics",
            "request_type": request.__class__.__name__,
            "response_type": "ListTopicsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'device_id' in local_var_params:
            path_params['device_id'] = local_var_params['device_id']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'topic_permission' in local_var_params:
            query_params.append(('topic_permission', local_var_params['topic_permission']))
        if 'topic_type' in local_var_params:
            query_params.append(('topic_type', local_var_params['topic_type']))
        if 'is_private' in local_var_params:
            query_params.append(('is_private', local_var_params['is_private']))

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

    def publish_live_data_api_v2_async(self, request):
        r"""部署后端API

        在某个实例中部署后端API。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for PublishLiveDataApiV2
        :type request: :class:`huaweicloudsdkroma.v2.PublishLiveDataApiV2Request`
        :rtype: :class:`huaweicloudsdkroma.v2.PublishLiveDataApiV2Response`
        """
        http_info = self._publish_live_data_api_v2_http_info(request)
        return self._call_api(**http_info)

    def publish_live_data_api_v2_async_invoker(self, request):
        http_info = self._publish_live_data_api_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _publish_live_data_api_v2_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/livedata-apis/{ld_api_id}/deploy",
            "request_type": request.__class__.__name__,
            "response_type": "PublishLiveDataApiV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'ld_api_id' in local_var_params:
            path_params['ld_api_id'] = local_var_params['ld_api_id']

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

    def reset_authentication_async(self, request):
        r"""重置设备鉴权信息

        重置设备鉴权信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ResetAuthentication
        :type request: :class:`huaweicloudsdkroma.v2.ResetAuthenticationRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.ResetAuthenticationResponse`
        """
        http_info = self._reset_authentication_http_info(request)
        return self._call_api(**http_info)

    def reset_authentication_async_invoker(self, request):
        http_info = self._reset_authentication_http_info(request)
        return AsyncInvoker(self, http_info)

    def _reset_authentication_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/link/instances/{instance_id}/devices/{device_id}/authentication",
            "request_type": request.__class__.__name__,
            "response_type": "ResetAuthenticationResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'device_id' in local_var_params:
            path_params['device_id'] = local_var_params['device_id']

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

    def reset_messages_async(self, request):
        r"""重发消息

        重发消息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ResetMessages
        :type request: :class:`huaweicloudsdkroma.v2.ResetMessagesRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.ResetMessagesResponse`
        """
        http_info = self._reset_messages_http_info(request)
        return self._call_api(**http_info)

    def reset_messages_async_invoker(self, request):
        http_info = self._reset_messages_http_info(request)
        return AsyncInvoker(self, http_info)

    def _reset_messages_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/mqs/instances/{instance_id}/messages/action",
            "request_type": request.__class__.__name__,
            "response_type": "ResetMessagesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'action_id' in local_var_params:
            query_params.append(('action_id', local_var_params['action_id']))

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

    def reset_multi_task_offset_async(self, request):
        r"""重置组合任务进度

        重置组合任务进度
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ResetMultiTaskOffset
        :type request: :class:`huaweicloudsdkroma.v2.ResetMultiTaskOffsetRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.ResetMultiTaskOffsetResponse`
        """
        http_info = self._reset_multi_task_offset_http_info(request)
        return self._call_api(**http_info)

    def reset_multi_task_offset_async_invoker(self, request):
        http_info = self._reset_multi_task_offset_http_info(request)
        return AsyncInvoker(self, http_info)

    def _reset_multi_task_offset_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/fdi/instances/{instance_id}/multi-tasks/{task_id}/reset",
            "request_type": request.__class__.__name__,
            "response_type": "ResetMultiTaskOffsetResponse"
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

    def reset_product_authentication_async(self, request):
        r"""重置产品鉴权信息

        重置产品鉴权信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ResetProductAuthentication
        :type request: :class:`huaweicloudsdkroma.v2.ResetProductAuthenticationRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.ResetProductAuthenticationResponse`
        """
        http_info = self._reset_product_authentication_http_info(request)
        return self._call_api(**http_info)

    def reset_product_authentication_async_invoker(self, request):
        http_info = self._reset_product_authentication_http_info(request)
        return AsyncInvoker(self, http_info)

    def _reset_product_authentication_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/link/instances/{instance_id}/products/{product_id}/authentication",
            "request_type": request.__class__.__name__,
            "response_type": "ResetProductAuthenticationResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'product_id' in local_var_params:
            path_params['product_id'] = local_var_params['product_id']

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

    def run_task_async(self, request):
        r"""手工触发单个任务

        手工触发一次任务调度
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RunTask
        :type request: :class:`huaweicloudsdkroma.v2.RunTaskRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.RunTaskResponse`
        """
        http_info = self._run_task_http_info(request)
        return self._call_api(**http_info)

    def run_task_async_invoker(self, request):
        http_info = self._run_task_http_info(request)
        return AsyncInvoker(self, http_info)

    def _run_task_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/fdi/instances/{instance_id}/tasks/{task_id}/run",
            "request_type": request.__class__.__name__,
            "response_type": "RunTaskResponse"
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

    def send_command_async(self, request):
        r"""发送命令

        发送命令
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for SendCommand
        :type request: :class:`huaweicloudsdkroma.v2.SendCommandRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.SendCommandResponse`
        """
        http_info = self._send_command_http_info(request)
        return self._call_api(**http_info)

    def send_command_async_invoker(self, request):
        http_info = self._send_command_http_info(request)
        return AsyncInvoker(self, http_info)

    def _send_command_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/link/instances/{instance_id}/devices/{device_id}/send-command",
            "request_type": request.__class__.__name__,
            "response_type": "SendCommandResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'device_id' in local_var_params:
            path_params['device_id'] = local_var_params['device_id']

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
        r"""查询客户端应用关联的应用配额

        查看指定客户端应用关联的应用配额。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowAppBoundAppQuota
        :type request: :class:`huaweicloudsdkroma.v2.ShowAppBoundAppQuotaRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.ShowAppBoundAppQuotaResponse`
        """
        http_info = self._show_app_bound_app_quota_http_info(request)
        return self._call_api(**http_info)

    def show_app_bound_app_quota_async_invoker(self, request):
        http_info = self._show_app_bound_app_quota_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_app_bound_app_quota_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/apps/{app_id}/bound-quota",
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
        r"""获取客户端配额详情

        获取客户端配额详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowAppQuota
        :type request: :class:`huaweicloudsdkroma.v2.ShowAppQuotaRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.ShowAppQuotaResponse`
        """
        http_info = self._show_app_quota_http_info(request)
        return self._call_api(**http_info)

    def show_app_quota_async_invoker(self, request):
        http_info = self._show_app_quota_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_app_quota_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/app-quotas/{app_quota_id}",
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

    def show_authentication_async(self, request):
        r"""查询设备鉴权信息

        查询设备鉴权信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowAuthentication
        :type request: :class:`huaweicloudsdkroma.v2.ShowAuthenticationRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.ShowAuthenticationResponse`
        """
        http_info = self._show_authentication_http_info(request)
        return self._call_api(**http_info)

    def show_authentication_async_invoker(self, request):
        http_info = self._show_authentication_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_authentication_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/link/instances/{instance_id}/devices/{device_id}/authentication",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAuthenticationResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'device_id' in local_var_params:
            path_params['device_id'] = local_var_params['device_id']

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

    def show_command_async(self, request):
        r"""查询命令详情

        查询命令详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowCommand
        :type request: :class:`huaweicloudsdkroma.v2.ShowCommandRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.ShowCommandResponse`
        """
        http_info = self._show_command_http_info(request)
        return self._call_api(**http_info)

    def show_command_async_invoker(self, request):
        http_info = self._show_command_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_command_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/link/instances/{instance_id}/services/{service_id}/commands/{command_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowCommandResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'service_id' in local_var_params:
            path_params['service_id'] = local_var_params['service_id']
        if 'command_id' in local_var_params:
            path_params['command_id'] = local_var_params['command_id']

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

    def show_dataource_detail_async(self, request):
        r"""查询指定数据源

        根据数据源id查询数据源
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowDataourceDetail
        :type request: :class:`huaweicloudsdkroma.v2.ShowDataourceDetailRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.ShowDataourceDetailResponse`
        """
        http_info = self._show_dataource_detail_http_info(request)
        return self._call_api(**http_info)

    def show_dataource_detail_async_invoker(self, request):
        http_info = self._show_dataource_detail_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_dataource_detail_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/fdi/instances/{instance_id}/datasources/{datasource_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDataourceDetailResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'datasource_id' in local_var_params:
            path_params['datasource_id'] = local_var_params['datasource_id']

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
        r"""查看APP的访问控制详情

        查看APP的访问控制详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowDetailsOfAppAcl
        :type request: :class:`huaweicloudsdkroma.v2.ShowDetailsOfAppAclRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.ShowDetailsOfAppAclResponse`
        """
        http_info = self._show_details_of_app_acl_http_info(request)
        return self._call_api(**http_info)

    def show_details_of_app_acl_async_invoker(self, request):
        http_info = self._show_details_of_app_acl_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_details_of_app_acl_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/apps/{app_id}/app-acl",
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
        r"""查看APP Code详情

        App Code为APP应用下的子模块，创建App Code之后，可以实现简易的APP认证。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowDetailsOfAppCodeV2
        :type request: :class:`huaweicloudsdkroma.v2.ShowDetailsOfAppCodeV2Request`
        :rtype: :class:`huaweicloudsdkroma.v2.ShowDetailsOfAppCodeV2Response`
        """
        http_info = self._show_details_of_app_code_v2_http_info(request)
        return self._call_api(**http_info)

    def show_details_of_app_code_v2_async_invoker(self, request):
        http_info = self._show_details_of_app_code_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_details_of_app_code_v2_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/apps/{app_id}/app-codes/{app_code_id}",
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

    def show_details_of_app_config_v2_async(self, request):
        r"""查看应用配置详情

        查看应用配置详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowDetailsOfAppConfigV2
        :type request: :class:`huaweicloudsdkroma.v2.ShowDetailsOfAppConfigV2Request`
        :rtype: :class:`huaweicloudsdkroma.v2.ShowDetailsOfAppConfigV2Response`
        """
        http_info = self._show_details_of_app_config_v2_http_info(request)
        return self._call_api(**http_info)

    def show_details_of_app_config_v2_async_invoker(self, request):
        http_info = self._show_details_of_app_config_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_details_of_app_config_v2_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/apps/{app_id}/configs/{app_config_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDetailsOfAppConfigV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'app_id' in local_var_params:
            path_params['app_id'] = local_var_params['app_id']
        if 'app_config_id' in local_var_params:
            path_params['app_config_id'] = local_var_params['app_config_id']

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
        r"""查看APP详情

        查看指定APP的详细信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowDetailsOfAppV2
        :type request: :class:`huaweicloudsdkroma.v2.ShowDetailsOfAppV2Request`
        :rtype: :class:`huaweicloudsdkroma.v2.ShowDetailsOfAppV2Response`
        """
        http_info = self._show_details_of_app_v2_http_info(request)
        return self._call_api(**http_info)

    def show_details_of_app_v2_async_invoker(self, request):
        http_info = self._show_details_of_app_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_details_of_app_v2_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/apps/{app_id}",
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
        r"""查看自定义认证详情

        查看自定义认证详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowDetailsOfCustomAuthorizersV2
        :type request: :class:`huaweicloudsdkroma.v2.ShowDetailsOfCustomAuthorizersV2Request`
        :rtype: :class:`huaweicloudsdkroma.v2.ShowDetailsOfCustomAuthorizersV2Response`
        """
        http_info = self._show_details_of_custom_authorizers_v2_http_info(request)
        return self._call_api(**http_info)

    def show_details_of_custom_authorizers_v2_async_invoker(self, request):
        http_info = self._show_details_of_custom_authorizers_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_details_of_custom_authorizers_v2_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/authorizers/{authorizer_id}",
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
        r"""查看域名证书

        查看域名下绑定的证书详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowDetailsOfDomainNameCertificateV2
        :type request: :class:`huaweicloudsdkroma.v2.ShowDetailsOfDomainNameCertificateV2Request`
        :rtype: :class:`huaweicloudsdkroma.v2.ShowDetailsOfDomainNameCertificateV2Response`
        """
        http_info = self._show_details_of_domain_name_certificate_v2_http_info(request)
        return self._call_api(**http_info)

    def show_details_of_domain_name_certificate_v2_async_invoker(self, request):
        http_info = self._show_details_of_domain_name_certificate_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_details_of_domain_name_certificate_v2_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/api-groups/{group_id}/domains/{domain_id}/certificate/{certificate_id}",
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
        r"""查看变量详情

        查看指定的环境变量的详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowDetailsOfEnvironmentVariableV2
        :type request: :class:`huaweicloudsdkroma.v2.ShowDetailsOfEnvironmentVariableV2Request`
        :rtype: :class:`huaweicloudsdkroma.v2.ShowDetailsOfEnvironmentVariableV2Response`
        """
        http_info = self._show_details_of_environment_variable_v2_http_info(request)
        return self._call_api(**http_info)

    def show_details_of_environment_variable_v2_async_invoker(self, request):
        http_info = self._show_details_of_environment_variable_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_details_of_environment_variable_v2_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/env-variables/{env_variable_id}",
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

    def show_details_of_instance_v2_async(self, request):
        r"""查看实例详情

        查看实例详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowDetailsOfInstanceV2
        :type request: :class:`huaweicloudsdkroma.v2.ShowDetailsOfInstanceV2Request`
        :rtype: :class:`huaweicloudsdkroma.v2.ShowDetailsOfInstanceV2Response`
        """
        http_info = self._show_details_of_instance_v2_http_info(request)
        return self._call_api(**http_info)

    def show_details_of_instance_v2_async_invoker(self, request):
        http_info = self._show_details_of_instance_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_details_of_instance_v2_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}",
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
        r"""查看流控策略详情

        查看指定流控策略的详细信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowDetailsOfRequestThrottlingPolicyV2
        :type request: :class:`huaweicloudsdkroma.v2.ShowDetailsOfRequestThrottlingPolicyV2Request`
        :rtype: :class:`huaweicloudsdkroma.v2.ShowDetailsOfRequestThrottlingPolicyV2Response`
        """
        http_info = self._show_details_of_request_throttling_policy_v2_http_info(request)
        return self._call_api(**http_info)

    def show_details_of_request_throttling_policy_v2_async_invoker(self, request):
        http_info = self._show_details_of_request_throttling_policy_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_details_of_request_throttling_policy_v2_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/throttles/{throttle_id}",
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

    def show_device_async(self, request):
        r"""查询设备详情

        查询设备详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowDevice
        :type request: :class:`huaweicloudsdkroma.v2.ShowDeviceRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.ShowDeviceResponse`
        """
        http_info = self._show_device_http_info(request)
        return self._call_api(**http_info)

    def show_device_async_invoker(self, request):
        http_info = self._show_device_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_device_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/link/instances/{instance_id}/devices/{device_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDeviceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'device_id' in local_var_params:
            path_params['device_id'] = local_var_params['device_id']

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

    def show_device_group_async(self, request):
        r"""查询设备分组详情

        获取设备分组及下一层分组信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowDeviceGroup
        :type request: :class:`huaweicloudsdkroma.v2.ShowDeviceGroupRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.ShowDeviceGroupResponse`
        """
        http_info = self._show_device_group_http_info(request)
        return self._call_api(**http_info)

    def show_device_group_async_invoker(self, request):
        http_info = self._show_device_group_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_device_group_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/link/instances/{instance_id}/device-groups/{group_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDeviceGroupResponse"
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

    def show_device_group_tree_async(self, request):
        r"""查询所有设备分组

        查询所有设备分组
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowDeviceGroupTree
        :type request: :class:`huaweicloudsdkroma.v2.ShowDeviceGroupTreeRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.ShowDeviceGroupTreeResponse`
        """
        http_info = self._show_device_group_tree_http_info(request)
        return self._call_api(**http_info)

    def show_device_group_tree_async_invoker(self, request):
        http_info = self._show_device_group_tree_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_device_group_tree_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/link/instances/{instance_id}/device-groups",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDeviceGroupTreeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'app_id' in local_var_params:
            query_params.append(('app_id', local_var_params['app_id']))

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

    def show_devices_in_group_async(self, request):
        r"""查询设备分组内设备

        查询设备分组内设备
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowDevicesInGroup
        :type request: :class:`huaweicloudsdkroma.v2.ShowDevicesInGroupRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.ShowDevicesInGroupResponse`
        """
        http_info = self._show_devices_in_group_http_info(request)
        return self._call_api(**http_info)

    def show_devices_in_group_async_invoker(self, request):
        http_info = self._show_devices_in_group_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_devices_in_group_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/link/instances/{instance_id}/device-groups/{group_id}/devices",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDevicesInGroupResponse"
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
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'product_name' in local_var_params:
            query_params.append(('product_name', local_var_params['product_name']))
        if 'device_name' in local_var_params:
            query_params.append(('device_name', local_var_params['device_name']))
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

    def show_dispatches_async(self, request):
        r"""查询调度计划

        查询调度计划
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowDispatches
        :type request: :class:`huaweicloudsdkroma.v2.ShowDispatchesRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.ShowDispatchesResponse`
        """
        http_info = self._show_dispatches_http_info(request)
        return self._call_api(**http_info)

    def show_dispatches_async_invoker(self, request):
        http_info = self._show_dispatches_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_dispatches_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/fdi/instances/{instance_id}/tasks/{task_id}/dispatches",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDispatchesResponse"
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

    def show_live_data_api_v2_async(self, request):
        r"""查询后端API详情

        查询后端API的详细信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowLiveDataApiV2
        :type request: :class:`huaweicloudsdkroma.v2.ShowLiveDataApiV2Request`
        :rtype: :class:`huaweicloudsdkroma.v2.ShowLiveDataApiV2Response`
        """
        http_info = self._show_live_data_api_v2_http_info(request)
        return self._call_api(**http_info)

    def show_live_data_api_v2_async_invoker(self, request):
        http_info = self._show_live_data_api_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_live_data_api_v2_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/livedata-apis/{ld_api_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowLiveDataApiV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'ld_api_id' in local_var_params:
            path_params['ld_api_id'] = local_var_params['ld_api_id']

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

    def show_mqs_instance_messages_async(self, request):
        r"""查询消息

        查询消息的偏移量和消息内容。
        先根据时间戳查询消息的偏移量，再根据偏移量查询消息内容。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowMqsInstanceMessages
        :type request: :class:`huaweicloudsdkroma.v2.ShowMqsInstanceMessagesRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.ShowMqsInstanceMessagesResponse`
        """
        http_info = self._show_mqs_instance_messages_http_info(request)
        return self._call_api(**http_info)

    def show_mqs_instance_messages_async_invoker(self, request):
        http_info = self._show_mqs_instance_messages_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_mqs_instance_messages_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/mqs/instances/{instance_id}/messages",
            "request_type": request.__class__.__name__,
            "response_type": "ShowMqsInstanceMessagesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'topic' in local_var_params:
            query_params.append(('topic', local_var_params['topic']))
        if 'asc' in local_var_params:
            query_params.append(('asc', local_var_params['asc']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'download' in local_var_params:
            query_params.append(('download', local_var_params['download']))
        if 'message_offset' in local_var_params:
            query_params.append(('message_offset', local_var_params['message_offset']))
        if 'partition' in local_var_params:
            query_params.append(('partition', local_var_params['partition']))
        if 'key' in local_var_params:
            query_params.append(('key', local_var_params['key']))
        if 'message_id' in local_var_params:
            query_params.append(('message_id', local_var_params['message_id']))
        if 'tag' in local_var_params:
            query_params.append(('tag', local_var_params['tag']))

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

    def show_mqs_instance_topic_access_policy_async(self, request):
        r"""查询Topic权限

        查询Topic权限。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowMqsInstanceTopicAccessPolicy
        :type request: :class:`huaweicloudsdkroma.v2.ShowMqsInstanceTopicAccessPolicyRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.ShowMqsInstanceTopicAccessPolicyResponse`
        """
        http_info = self._show_mqs_instance_topic_access_policy_http_info(request)
        return self._call_api(**http_info)

    def show_mqs_instance_topic_access_policy_async_invoker(self, request):
        http_info = self._show_mqs_instance_topic_access_policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_mqs_instance_topic_access_policy_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/mqs/instances/{instance_id}/topics/{topic_name}/accesspolicy",
            "request_type": request.__class__.__name__,
            "response_type": "ShowMqsInstanceTopicAccessPolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'topic_name' in local_var_params:
            path_params['topic_name'] = local_var_params['topic_name']

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

    def show_plugin_async(self, request):
        r"""查询插件详情

        查询插件详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowPlugin
        :type request: :class:`huaweicloudsdkroma.v2.ShowPluginRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.ShowPluginResponse`
        """
        http_info = self._show_plugin_http_info(request)
        return self._call_api(**http_info)

    def show_plugin_async_invoker(self, request):
        http_info = self._show_plugin_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_plugin_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/plugins/{plugin_id}",
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

    def show_product_async(self, request):
        r"""查询产品详情

        查询产品详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowProduct
        :type request: :class:`huaweicloudsdkroma.v2.ShowProductRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.ShowProductResponse`
        """
        http_info = self._show_product_http_info(request)
        return self._call_api(**http_info)

    def show_product_async_invoker(self, request):
        http_info = self._show_product_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_product_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/link/instances/{instance_id}/products/{product_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowProductResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'product_id' in local_var_params:
            path_params['product_id'] = local_var_params['product_id']

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

    def show_product_authentication_async(self, request):
        r"""查询产品鉴权信息

        查询产品鉴权信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowProductAuthentication
        :type request: :class:`huaweicloudsdkroma.v2.ShowProductAuthenticationRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.ShowProductAuthenticationResponse`
        """
        http_info = self._show_product_authentication_http_info(request)
        return self._call_api(**http_info)

    def show_product_authentication_async_invoker(self, request):
        http_info = self._show_product_authentication_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_product_authentication_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/link/instances/{instance_id}/products/{product_id}/authentication",
            "request_type": request.__class__.__name__,
            "response_type": "ShowProductAuthenticationResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'product_id' in local_var_params:
            path_params['product_id'] = local_var_params['product_id']

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

    def show_product_template_async(self, request):
        r"""查询产品模板详情

        查询产品模板详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowProductTemplate
        :type request: :class:`huaweicloudsdkroma.v2.ShowProductTemplateRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.ShowProductTemplateResponse`
        """
        http_info = self._show_product_template_http_info(request)
        return self._call_api(**http_info)

    def show_product_template_async_invoker(self, request):
        http_info = self._show_product_template_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_product_template_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/link/instances/{instance_id}/product-templates/{product_template_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowProductTemplateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'product_template_id' in local_var_params:
            path_params['product_template_id'] = local_var_params['product_template_id']

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

    def show_property_async(self, request):
        r"""查询服务属性详情

        查询服务属性详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowProperty
        :type request: :class:`huaweicloudsdkroma.v2.ShowPropertyRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.ShowPropertyResponse`
        """
        http_info = self._show_property_http_info(request)
        return self._call_api(**http_info)

    def show_property_async_invoker(self, request):
        http_info = self._show_property_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_property_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/link/instances/{instance_id}/services/{service_id}/properties/{property_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowPropertyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'service_id' in local_var_params:
            path_params['service_id'] = local_var_params['service_id']
        if 'property_id' in local_var_params:
            path_params['property_id'] = local_var_params['property_id']

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

    def show_request_property_async(self, request):
        r"""查询请求属性详情

        查询请求属性详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowRequestProperty
        :type request: :class:`huaweicloudsdkroma.v2.ShowRequestPropertyRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.ShowRequestPropertyResponse`
        """
        http_info = self._show_request_property_http_info(request)
        return self._call_api(**http_info)

    def show_request_property_async_invoker(self, request):
        http_info = self._show_request_property_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_request_property_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/link/instances/{instance_id}/services/{service_id}/commands/{command_id}/requests/{property_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowRequestPropertyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'service_id' in local_var_params:
            path_params['service_id'] = local_var_params['service_id']
        if 'command_id' in local_var_params:
            path_params['command_id'] = local_var_params['command_id']
        if 'property_id' in local_var_params:
            path_params['property_id'] = local_var_params['property_id']

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

    def show_response_property_async(self, request):
        r"""查询响应属性详情

        查询响应属性详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowResponseProperty
        :type request: :class:`huaweicloudsdkroma.v2.ShowResponsePropertyRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.ShowResponsePropertyResponse`
        """
        http_info = self._show_response_property_http_info(request)
        return self._call_api(**http_info)

    def show_response_property_async_invoker(self, request):
        http_info = self._show_response_property_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_response_property_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/link/instances/{instance_id}/services/{service_id}/commands/{command_id}/responses/{property_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowResponsePropertyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'service_id' in local_var_params:
            path_params['service_id'] = local_var_params['service_id']
        if 'command_id' in local_var_params:
            path_params['command_id'] = local_var_params['command_id']
        if 'property_id' in local_var_params:
            path_params['property_id'] = local_var_params['property_id']

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
        r"""查看实例约束信息

        查看实例约束信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowRestrictionOfInstanceV2
        :type request: :class:`huaweicloudsdkroma.v2.ShowRestrictionOfInstanceV2Request`
        :rtype: :class:`huaweicloudsdkroma.v2.ShowRestrictionOfInstanceV2Response`
        """
        http_info = self._show_restriction_of_instance_v2_http_info(request)
        return self._call_api(**http_info)

    def show_restriction_of_instance_v2_async_invoker(self, request):
        http_info = self._show_restriction_of_instance_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_restriction_of_instance_v2_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/restriction",
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

    def show_rule_async(self, request):
        r"""查询规则详情

        查询规则详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowRule
        :type request: :class:`huaweicloudsdkroma.v2.ShowRuleRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.ShowRuleResponse`
        """
        http_info = self._show_rule_http_info(request)
        return self._call_api(**http_info)

    def show_rule_async_invoker(self, request):
        http_info = self._show_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_rule_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/link/instances/{instance_id}/rules/{rule_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'rule_id' in local_var_params:
            path_params['rule_id'] = local_var_params['rule_id']

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

    def show_service_async(self, request):
        r"""查询服务详情

        查询服务详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowService
        :type request: :class:`huaweicloudsdkroma.v2.ShowServiceRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.ShowServiceResponse`
        """
        http_info = self._show_service_http_info(request)
        return self._call_api(**http_info)

    def show_service_async_invoker(self, request):
        http_info = self._show_service_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_service_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/link/instances/{instance_id}/services/{service_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowServiceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'service_id' in local_var_params:
            path_params['service_id'] = local_var_params['service_id']

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

    def show_task_async(self, request):
        r"""通过任务ID查询指定任务的信息

        通过任务ID查询指定任务的信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowTask
        :type request: :class:`huaweicloudsdkroma.v2.ShowTaskRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.ShowTaskResponse`
        """
        http_info = self._show_task_http_info(request)
        return self._call_api(**http_info)

    def show_task_async_invoker(self, request):
        http_info = self._show_task_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_task_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/fdi/instances/{instance_id}/tasks/{task_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowTaskResponse"
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

    def start_test_datasource_async(self, request):
        r"""测试数据源连通性

        测试数据源连通性
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for StartTestDatasource
        :type request: :class:`huaweicloudsdkroma.v2.StartTestDatasourceRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.StartTestDatasourceResponse`
        """
        http_info = self._start_test_datasource_http_info(request)
        return self._call_api(**http_info)

    def start_test_datasource_async_invoker(self, request):
        http_info = self._start_test_datasource_http_info(request)
        return AsyncInvoker(self, http_info)

    def _start_test_datasource_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/fdi/instances/{instance_id}/datasources/{datasource_id}/test-connect",
            "request_type": request.__class__.__name__,
            "response_type": "StartTestDatasourceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'datasource_id' in local_var_params:
            path_params['datasource_id'] = local_var_params['datasource_id']

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

    def stop_task_async(self, request):
        r"""手工停止当前执行的任务

        手工停止当前执行的任务
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for StopTask
        :type request: :class:`huaweicloudsdkroma.v2.StopTaskRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.StopTaskResponse`
        """
        http_info = self._stop_task_http_info(request)
        return self._call_api(**http_info)

    def stop_task_async_invoker(self, request):
        http_info = self._stop_task_http_info(request)
        return AsyncInvoker(self, http_info)

    def _stop_task_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/fdi/instances/{instance_id}/tasks/{task_id}/terminate",
            "request_type": request.__class__.__name__,
            "response_type": "StopTaskResponse"
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

    def unpublish_live_data_api_v2_async(self, request):
        r"""撤销后端API

        在某个实例中取消部署后端API。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UnpublishLiveDataApiV2
        :type request: :class:`huaweicloudsdkroma.v2.UnpublishLiveDataApiV2Request`
        :rtype: :class:`huaweicloudsdkroma.v2.UnpublishLiveDataApiV2Response`
        """
        http_info = self._unpublish_live_data_api_v2_http_info(request)
        return self._call_api(**http_info)

    def unpublish_live_data_api_v2_async_invoker(self, request):
        http_info = self._unpublish_live_data_api_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _unpublish_live_data_api_v2_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/livedata-apis/{ld_api_id}/undeploy",
            "request_type": request.__class__.__name__,
            "response_type": "UnpublishLiveDataApiV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'ld_api_id' in local_var_params:
            path_params['ld_api_id'] = local_var_params['ld_api_id']

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
        r"""设置APP的访问控制

        设置客户端配置的访问控制。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateAppAcl
        :type request: :class:`huaweicloudsdkroma.v2.UpdateAppAclRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.UpdateAppAclResponse`
        """
        http_info = self._update_app_acl_http_info(request)
        return self._call_api(**http_info)

    def update_app_acl_async_invoker(self, request):
        http_info = self._update_app_acl_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_app_acl_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/apps/{app_id}/app-acl",
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

    def update_app_config_v2_async(self, request):
        r"""修改应用配置

        修改应用配置
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateAppConfigV2
        :type request: :class:`huaweicloudsdkroma.v2.UpdateAppConfigV2Request`
        :rtype: :class:`huaweicloudsdkroma.v2.UpdateAppConfigV2Response`
        """
        http_info = self._update_app_config_v2_http_info(request)
        return self._call_api(**http_info)

    def update_app_config_v2_async_invoker(self, request):
        http_info = self._update_app_config_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_app_config_v2_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/apps/{app_id}/configs/{app_config_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateAppConfigV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'app_id' in local_var_params:
            path_params['app_id'] = local_var_params['app_id']
        if 'app_config_id' in local_var_params:
            path_params['app_config_id'] = local_var_params['app_config_id']

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
        r"""修改客户端配额

        修改客户端配额
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateAppQuota
        :type request: :class:`huaweicloudsdkroma.v2.UpdateAppQuotaRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.UpdateAppQuotaResponse`
        """
        http_info = self._update_app_quota_http_info(request)
        return self._call_api(**http_info)

    def update_app_quota_async_invoker(self, request):
        http_info = self._update_app_quota_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_app_quota_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/app-quotas/{app_quota_id}",
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

    def update_command_async(self, request):
        r"""修改命令

        修改命令
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateCommand
        :type request: :class:`huaweicloudsdkroma.v2.UpdateCommandRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.UpdateCommandResponse`
        """
        http_info = self._update_command_http_info(request)
        return self._call_api(**http_info)

    def update_command_async_invoker(self, request):
        http_info = self._update_command_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_command_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/link/instances/{instance_id}/services/{service_id}/commands/{command_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateCommandResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'service_id' in local_var_params:
            path_params['service_id'] = local_var_params['service_id']
        if 'command_id' in local_var_params:
            path_params['command_id'] = local_var_params['command_id']

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
        r"""修改自定义认证

        修改自定义认证
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateCustomAuthorizerV2
        :type request: :class:`huaweicloudsdkroma.v2.UpdateCustomAuthorizerV2Request`
        :rtype: :class:`huaweicloudsdkroma.v2.UpdateCustomAuthorizerV2Response`
        """
        http_info = self._update_custom_authorizer_v2_http_info(request)
        return self._call_api(**http_info)

    def update_custom_authorizer_v2_async_invoker(self, request):
        http_info = self._update_custom_authorizer_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_custom_authorizer_v2_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/authorizers/{authorizer_id}",
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

    def update_datasource_info_async(self, request):
        r"""修改数据源

        修改数据源
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateDatasourceInfo
        :type request: :class:`huaweicloudsdkroma.v2.UpdateDatasourceInfoRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.UpdateDatasourceInfoResponse`
        """
        http_info = self._update_datasource_info_http_info(request)
        return self._call_api(**http_info)

    def update_datasource_info_async_invoker(self, request):
        http_info = self._update_datasource_info_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_datasource_info_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/fdi/instances/{instance_id}/datasources/{datasource_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateDatasourceInfoResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'datasource_id' in local_var_params:
            path_params['datasource_id'] = local_var_params['datasource_id']

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

    def update_device_async(self, request):
        r"""修改设备

        修改设备信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateDevice
        :type request: :class:`huaweicloudsdkroma.v2.UpdateDeviceRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.UpdateDeviceResponse`
        """
        http_info = self._update_device_http_info(request)
        return self._call_api(**http_info)

    def update_device_async_invoker(self, request):
        http_info = self._update_device_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_device_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/link/instances/{instance_id}/devices/{device_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateDeviceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'device_id' in local_var_params:
            path_params['device_id'] = local_var_params['device_id']

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

    def update_device_group_async(self, request):
        r"""修改设备分组

        修改设备分组
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateDeviceGroup
        :type request: :class:`huaweicloudsdkroma.v2.UpdateDeviceGroupRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.UpdateDeviceGroupResponse`
        """
        http_info = self._update_device_group_http_info(request)
        return self._call_api(**http_info)

    def update_device_group_async_invoker(self, request):
        http_info = self._update_device_group_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_device_group_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/link/instances/{instance_id}/device-groups/{group_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateDeviceGroupResponse"
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

    def update_dispatches_async(self, request):
        r"""修改调度计划

        通过任务ID和调度ID修改调度计划
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateDispatches
        :type request: :class:`huaweicloudsdkroma.v2.UpdateDispatchesRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.UpdateDispatchesResponse`
        """
        http_info = self._update_dispatches_http_info(request)
        return self._call_api(**http_info)

    def update_dispatches_async_invoker(self, request):
        http_info = self._update_dispatches_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_dispatches_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/fdi/instances/{instance_id}/tasks/{task_id}/dispatches/{dispatch_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateDispatchesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']
        if 'dispatch_id' in local_var_params:
            path_params['dispatch_id'] = local_var_params['dispatch_id']

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
        r"""修改域名

        修改绑定的域名所对应的配置信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateDomainV2
        :type request: :class:`huaweicloudsdkroma.v2.UpdateDomainV2Request`
        :rtype: :class:`huaweicloudsdkroma.v2.UpdateDomainV2Response`
        """
        http_info = self._update_domain_v2_http_info(request)
        return self._call_api(**http_info)

    def update_domain_v2_async_invoker(self, request):
        http_info = self._update_domain_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_domain_v2_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/api-groups/{group_id}/domains/{domain_id}",
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

    def update_environment_v2_async(self, request):
        r"""修改环境

        修改指定环境的信息。其中可修改的属性为：name、remark，其它属性不可修改。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateEnvironmentV2
        :type request: :class:`huaweicloudsdkroma.v2.UpdateEnvironmentV2Request`
        :rtype: :class:`huaweicloudsdkroma.v2.UpdateEnvironmentV2Response`
        """
        http_info = self._update_environment_v2_http_info(request)
        return self._call_api(**http_info)

    def update_environment_v2_async_invoker(self, request):
        http_info = self._update_environment_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_environment_v2_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/envs/{env_id}",
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
        r"""修改变量

        修改环境变量。环境变量引用位置为api的后端服务地址时，修改对应环境变量会将使用该变量的所有api重新发布。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateEnvironmentVariableV2
        :type request: :class:`huaweicloudsdkroma.v2.UpdateEnvironmentVariableV2Request`
        :rtype: :class:`huaweicloudsdkroma.v2.UpdateEnvironmentVariableV2Response`
        """
        http_info = self._update_environment_variable_v2_http_info(request)
        return self._call_api(**http_info)

    def update_environment_variable_v2_async_invoker(self, request):
        http_info = self._update_environment_variable_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_environment_variable_v2_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/env-variables/{env_variable_id}",
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

    def update_live_data_api_v2_async(self, request):
        r"""修改后端API

        在某个实例中更新后端API的参数。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateLiveDataApiV2
        :type request: :class:`huaweicloudsdkroma.v2.UpdateLiveDataApiV2Request`
        :rtype: :class:`huaweicloudsdkroma.v2.UpdateLiveDataApiV2Response`
        """
        http_info = self._update_live_data_api_v2_http_info(request)
        return self._call_api(**http_info)

    def update_live_data_api_v2_async_invoker(self, request):
        http_info = self._update_live_data_api_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_live_data_api_v2_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/livedata-apis/{ld_api_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateLiveDataApiV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'ld_api_id' in local_var_params:
            path_params['ld_api_id'] = local_var_params['ld_api_id']

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

    def update_mqs_instance_topic_async(self, request):
        r"""修改Topic

        修改Topic。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateMqsInstanceTopic
        :type request: :class:`huaweicloudsdkroma.v2.UpdateMqsInstanceTopicRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.UpdateMqsInstanceTopicResponse`
        """
        http_info = self._update_mqs_instance_topic_http_info(request)
        return self._call_api(**http_info)

    def update_mqs_instance_topic_async_invoker(self, request):
        http_info = self._update_mqs_instance_topic_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_mqs_instance_topic_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/mqs/instances/{instance_id}/topics",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateMqsInstanceTopicResponse"
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

    def update_multi_tasks_async(self, request):
        r"""修改组合任务

        修改组合任务
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateMultiTasks
        :type request: :class:`huaweicloudsdkroma.v2.UpdateMultiTasksRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.UpdateMultiTasksResponse`
        """
        http_info = self._update_multi_tasks_http_info(request)
        return self._call_api(**http_info)

    def update_multi_tasks_async_invoker(self, request):
        http_info = self._update_multi_tasks_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_multi_tasks_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/fdi/instances/{instance_id}/multi-tasks/{task_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateMultiTasksResponse"
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

    def update_notification_async(self, request):
        r"""修改订阅管理

        该接口用于修改指定的订阅管理
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateNotification
        :type request: :class:`huaweicloudsdkroma.v2.UpdateNotificationRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.UpdateNotificationResponse`
        """
        http_info = self._update_notification_http_info(request)
        return self._call_api(**http_info)

    def update_notification_async_invoker(self, request):
        http_info = self._update_notification_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_notification_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/link/instances/{instance_id}/notifications/{notification_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateNotificationResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'notification_id' in local_var_params:
            path_params['notification_id'] = local_var_params['notification_id']

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
        r"""修改插件

        修改插件信息。
        - 插件不允许重名
        - 插件不支持修改类型和可见范围
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdatePlugin
        :type request: :class:`huaweicloudsdkroma.v2.UpdatePluginRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.UpdatePluginResponse`
        """
        http_info = self._update_plugin_http_info(request)
        return self._call_api(**http_info)

    def update_plugin_async_invoker(self, request):
        http_info = self._update_plugin_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_plugin_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/plugins/{plugin_id}",
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

    def update_product_async(self, request):
        r"""修改产品信息

        修改产品信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateProduct
        :type request: :class:`huaweicloudsdkroma.v2.UpdateProductRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.UpdateProductResponse`
        """
        http_info = self._update_product_http_info(request)
        return self._call_api(**http_info)

    def update_product_async_invoker(self, request):
        http_info = self._update_product_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_product_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/link/instances/{instance_id}/products/{product_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateProductResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'product_id' in local_var_params:
            path_params['product_id'] = local_var_params['product_id']

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

    def update_product_template_async(self, request):
        r"""修改产品模板

        修改产品模板
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateProductTemplate
        :type request: :class:`huaweicloudsdkroma.v2.UpdateProductTemplateRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.UpdateProductTemplateResponse`
        """
        http_info = self._update_product_template_http_info(request)
        return self._call_api(**http_info)

    def update_product_template_async_invoker(self, request):
        http_info = self._update_product_template_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_product_template_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/link/instances/{instance_id}/product-templates/{product_template_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateProductTemplateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'product_template_id' in local_var_params:
            path_params['product_template_id'] = local_var_params['product_template_id']

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

    def update_product_topic_async(self, request):
        r"""更新产品主题

        更新产品主题
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateProductTopic
        :type request: :class:`huaweicloudsdkroma.v2.UpdateProductTopicRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.UpdateProductTopicResponse`
        """
        http_info = self._update_product_topic_http_info(request)
        return self._call_api(**http_info)

    def update_product_topic_async_invoker(self, request):
        http_info = self._update_product_topic_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_product_topic_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/link/instances/{instance_id}/products/{product_id}/topics/{topic_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateProductTopicResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'product_id' in local_var_params:
            path_params['product_id'] = local_var_params['product_id']
        if 'topic_id' in local_var_params:
            path_params['topic_id'] = local_var_params['topic_id']

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

    def update_property_async(self, request):
        r"""修改服务属性

        修改服务属性
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateProperty
        :type request: :class:`huaweicloudsdkroma.v2.UpdatePropertyRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.UpdatePropertyResponse`
        """
        http_info = self._update_property_http_info(request)
        return self._call_api(**http_info)

    def update_property_async_invoker(self, request):
        http_info = self._update_property_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_property_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/link/instances/{instance_id}/services/{service_id}/properties/{property_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdatePropertyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'service_id' in local_var_params:
            path_params['service_id'] = local_var_params['service_id']
        if 'property_id' in local_var_params:
            path_params['property_id'] = local_var_params['property_id']

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

    def update_request_property_async(self, request):
        r"""修改请求属性

        修改请求属性
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateRequestProperty
        :type request: :class:`huaweicloudsdkroma.v2.UpdateRequestPropertyRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.UpdateRequestPropertyResponse`
        """
        http_info = self._update_request_property_http_info(request)
        return self._call_api(**http_info)

    def update_request_property_async_invoker(self, request):
        http_info = self._update_request_property_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_request_property_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/link/instances/{instance_id}/services/{service_id}/commands/{command_id}/requests/{property_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateRequestPropertyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'service_id' in local_var_params:
            path_params['service_id'] = local_var_params['service_id']
        if 'command_id' in local_var_params:
            path_params['command_id'] = local_var_params['command_id']
        if 'property_id' in local_var_params:
            path_params['property_id'] = local_var_params['property_id']

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
        r"""修改流控策略

        修改指定流控策略的详细信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateRequestThrottlingPolicyV2
        :type request: :class:`huaweicloudsdkroma.v2.UpdateRequestThrottlingPolicyV2Request`
        :rtype: :class:`huaweicloudsdkroma.v2.UpdateRequestThrottlingPolicyV2Response`
        """
        http_info = self._update_request_throttling_policy_v2_http_info(request)
        return self._call_api(**http_info)

    def update_request_throttling_policy_v2_async_invoker(self, request):
        http_info = self._update_request_throttling_policy_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_request_throttling_policy_v2_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/throttles/{throttle_id}",
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

    def update_response_property_async(self, request):
        r"""修改响应属性

        修改响应属性
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateResponseProperty
        :type request: :class:`huaweicloudsdkroma.v2.UpdateResponsePropertyRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.UpdateResponsePropertyResponse`
        """
        http_info = self._update_response_property_http_info(request)
        return self._call_api(**http_info)

    def update_response_property_async_invoker(self, request):
        http_info = self._update_response_property_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_response_property_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/link/instances/{instance_id}/services/{service_id}/commands/{command_id}/responses/{property_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateResponsePropertyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'service_id' in local_var_params:
            path_params['service_id'] = local_var_params['service_id']
        if 'command_id' in local_var_params:
            path_params['command_id'] = local_var_params['command_id']
        if 'property_id' in local_var_params:
            path_params['property_id'] = local_var_params['property_id']

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

    def update_rule_async(self, request):
        r"""修改规则

        修改规则
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateRule
        :type request: :class:`huaweicloudsdkroma.v2.UpdateRuleRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.UpdateRuleResponse`
        """
        http_info = self._update_rule_http_info(request)
        return self._call_api(**http_info)

    def update_rule_async_invoker(self, request):
        http_info = self._update_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_rule_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/link/instances/{instance_id}/rules/{rule_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'rule_id' in local_var_params:
            path_params['rule_id'] = local_var_params['rule_id']

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

    def update_service_async(self, request):
        r"""修改服务

        修改服务
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateService
        :type request: :class:`huaweicloudsdkroma.v2.UpdateServiceRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.UpdateServiceResponse`
        """
        http_info = self._update_service_http_info(request)
        return self._call_api(**http_info)

    def update_service_async_invoker(self, request):
        http_info = self._update_service_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_service_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/link/instances/{instance_id}/services/{service_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateServiceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'service_id' in local_var_params:
            path_params['service_id'] = local_var_params['service_id']

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
        r"""修改签名密钥

        修改指定签名密钥的详细信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateSignatureKeyV2
        :type request: :class:`huaweicloudsdkroma.v2.UpdateSignatureKeyV2Request`
        :rtype: :class:`huaweicloudsdkroma.v2.UpdateSignatureKeyV2Response`
        """
        http_info = self._update_signature_key_v2_http_info(request)
        return self._call_api(**http_info)

    def update_signature_key_v2_async_invoker(self, request):
        http_info = self._update_signature_key_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_signature_key_v2_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/signs/{sign_id}",
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

    def update_special_throttling_configuration_v2_async(self, request):
        r"""修改特殊设置

        修改某个流控策略下的某个特殊设置。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateSpecialThrottlingConfigurationV2
        :type request: :class:`huaweicloudsdkroma.v2.UpdateSpecialThrottlingConfigurationV2Request`
        :rtype: :class:`huaweicloudsdkroma.v2.UpdateSpecialThrottlingConfigurationV2Response`
        """
        http_info = self._update_special_throttling_configuration_v2_http_info(request)
        return self._call_api(**http_info)

    def update_special_throttling_configuration_v2_async_invoker(self, request):
        http_info = self._update_special_throttling_configuration_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_special_throttling_configuration_v2_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/throttles/{throttle_id}/throttle-specials/{strategy_id}",
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

    def update_task_async(self, request):
        r"""更新普通任务

        更新普通任务
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateTask
        :type request: :class:`huaweicloudsdkroma.v2.UpdateTaskRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.UpdateTaskResponse`
        """
        http_info = self._update_task_http_info(request)
        return self._call_api(**http_info)

    def update_task_async_invoker(self, request):
        http_info = self._update_task_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_task_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/fdi/instances/{instance_id}/tasks/{task_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateTaskResponse"
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

    def update_topic_access_policy_async(self, request):
        r"""更新Topic权限

        更新Topic权限。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateTopicAccessPolicy
        :type request: :class:`huaweicloudsdkroma.v2.UpdateTopicAccessPolicyRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.UpdateTopicAccessPolicyResponse`
        """
        http_info = self._update_topic_access_policy_http_info(request)
        return self._call_api(**http_info)

    def update_topic_access_policy_async_invoker(self, request):
        http_info = self._update_topic_access_policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_topic_access_policy_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/mqs/instances/{instance_id}/topics/accesspolicy",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateTopicAccessPolicyResponse"
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

    def upload_product_async(self, request):
        r"""导入产品

        导入产品
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UploadProduct
        :type request: :class:`huaweicloudsdkroma.v2.UploadProductRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.UploadProductResponse`
        """
        http_info = self._upload_product_http_info(request)
        return self._call_api(**http_info)

    def upload_product_async_invoker(self, request):
        http_info = self._upload_product_http_info(request)
        return AsyncInvoker(self, http_info)

    def _upload_product_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/link/instances/{instance_id}/products/import",
            "request_type": request.__class__.__name__,
            "response_type": "UploadProductResponse"
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
        if 'file' in local_var_params:
            form_params['file'] = local_var_params['file']

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

    def batch_delete_acl_v2_async(self, request):
        r"""批量删除ACL策略

        批量删除指定的多个ACL策略。
        
        删除ACL策略时，如果存在ACL策略与API绑定关系，则无法删除。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchDeleteAclV2
        :type request: :class:`huaweicloudsdkroma.v2.BatchDeleteAclV2Request`
        :rtype: :class:`huaweicloudsdkroma.v2.BatchDeleteAclV2Response`
        """
        http_info = self._batch_delete_acl_v2_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_acl_v2_async_invoker(self, request):
        http_info = self._batch_delete_acl_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_delete_acl_v2_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/acls",
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
        r"""创建ACL策略

        增加一个ACL策略，策略类型通过字段acl_type来确定（permit或者deny），限制的对象的类型可以为IP[或者DOMAIN，这里的DOMAIN对应的acl_value的值为租户名称，而非“www.exampleDomain.com\&quot;之类的网络域名。](tag:hws,hws_hk,hcs,hcs_sm,fcs,g42)
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateAclStrategyV2
        :type request: :class:`huaweicloudsdkroma.v2.CreateAclStrategyV2Request`
        :rtype: :class:`huaweicloudsdkroma.v2.CreateAclStrategyV2Response`
        """
        http_info = self._create_acl_strategy_v2_http_info(request)
        return self._call_api(**http_info)

    def create_acl_strategy_v2_async_invoker(self, request):
        http_info = self._create_acl_strategy_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_acl_strategy_v2_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/acls",
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
        r"""删除ACL策略

        删除指定的ACL策略， 如果存在api与该ACL策略的绑定关系，则无法删除
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteAclV2
        :type request: :class:`huaweicloudsdkroma.v2.DeleteAclV2Request`
        :rtype: :class:`huaweicloudsdkroma.v2.DeleteAclV2Response`
        """
        http_info = self._delete_acl_v2_http_info(request)
        return self._call_api(**http_info)

    def delete_acl_v2_async_invoker(self, request):
        http_info = self._delete_acl_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_acl_v2_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/acls/{acl_id}",
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
        r"""查看ACL策略列表

        查询所有的ACL策略列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAclStrategiesV2
        :type request: :class:`huaweicloudsdkroma.v2.ListAclStrategiesV2Request`
        :rtype: :class:`huaweicloudsdkroma.v2.ListAclStrategiesV2Response`
        """
        http_info = self._list_acl_strategies_v2_http_info(request)
        return self._call_api(**http_info)

    def list_acl_strategies_v2_async_invoker(self, request):
        http_info = self._list_acl_strategies_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_acl_strategies_v2_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/acls",
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
        r"""查看ACL策略详情

        查询指定ACL策略的详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowDetailsOfAclPolicyV2
        :type request: :class:`huaweicloudsdkroma.v2.ShowDetailsOfAclPolicyV2Request`
        :rtype: :class:`huaweicloudsdkroma.v2.ShowDetailsOfAclPolicyV2Response`
        """
        http_info = self._show_details_of_acl_policy_v2_http_info(request)
        return self._call_api(**http_info)

    def show_details_of_acl_policy_v2_async_invoker(self, request):
        http_info = self._show_details_of_acl_policy_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_details_of_acl_policy_v2_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/acls/{acl_id}",
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
        r"""修改ACL策略

        修改指定的ACL策略，其中可修改的属性为：acl_name、acl_type、acl_value，其它属性不可修改。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateAclStrategyV2
        :type request: :class:`huaweicloudsdkroma.v2.UpdateAclStrategyV2Request`
        :rtype: :class:`huaweicloudsdkroma.v2.UpdateAclStrategyV2Response`
        """
        http_info = self._update_acl_strategy_v2_http_info(request)
        return self._call_api(**http_info)

    def update_acl_strategy_v2_async_invoker(self, request):
        http_info = self._update_acl_strategy_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_acl_strategy_v2_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/acls/{acl_id}",
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
        r"""绑定流控策略

        将流控策略应用于API，则所有对该API的访问将会受到该流控策略的限制。
        
        
        当一定时间内的访问次数超过流控策略设置的API最大访问次数限制后，后续的访问将会被拒绝，从而能够较好的保护后端API免受异常流量的冲击，保障服务的稳定运行。
        
        
        为指定的API绑定流控策略，绑定时，需要指定在哪个环境上生效。同一个API发布到不同的环境可以绑定不同的流控策略；一个API在发布到特定环境后只能绑定一个默认的流控策略。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AssociateRequestThrottlingPolicyV2
        :type request: :class:`huaweicloudsdkroma.v2.AssociateRequestThrottlingPolicyV2Request`
        :rtype: :class:`huaweicloudsdkroma.v2.AssociateRequestThrottlingPolicyV2Response`
        """
        http_info = self._associate_request_throttling_policy_v2_http_info(request)
        return self._call_api(**http_info)

    def associate_request_throttling_policy_v2_async_invoker(self, request):
        http_info = self._associate_request_throttling_policy_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _associate_request_throttling_policy_v2_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/throttle-bindings",
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
        r"""批量解绑流控策略

        批量解除API与流控策略的绑定关系
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchDisassociateThrottlingPolicyV2
        :type request: :class:`huaweicloudsdkroma.v2.BatchDisassociateThrottlingPolicyV2Request`
        :rtype: :class:`huaweicloudsdkroma.v2.BatchDisassociateThrottlingPolicyV2Response`
        """
        http_info = self._batch_disassociate_throttling_policy_v2_http_info(request)
        return self._call_api(**http_info)

    def batch_disassociate_throttling_policy_v2_async_invoker(self, request):
        http_info = self._batch_disassociate_throttling_policy_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_disassociate_throttling_policy_v2_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/throttle-bindings",
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
        r"""批量发布或下线API

        将多个API发布到一个指定的环境，或将多个API从指定的环境下线。
        
        注意：当action &#x3D; online时，接口返回的响应中publish_id，version_id， publish_time字段才有含义。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchPublishOrOfflineApiV2
        :type request: :class:`huaweicloudsdkroma.v2.BatchPublishOrOfflineApiV2Request`
        :rtype: :class:`huaweicloudsdkroma.v2.BatchPublishOrOfflineApiV2Response`
        """
        http_info = self._batch_publish_or_offline_api_v2_http_info(request)
        return self._call_api(**http_info)

    def batch_publish_or_offline_api_v2_async_invoker(self, request):
        http_info = self._batch_publish_or_offline_api_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_publish_or_offline_api_v2_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/apis/publish",
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
        r"""切换API版本

        API每次发布时，会基于当前的API定义生成一个版本。版本记录了API发布时的各种定义及状态。
        
        多个版本之间可以进行随意切换。但一个API在一个环境上，只能有一个版本生效。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ChangeApiVersionV2
        :type request: :class:`huaweicloudsdkroma.v2.ChangeApiVersionV2Request`
        :rtype: :class:`huaweicloudsdkroma.v2.ChangeApiVersionV2Response`
        """
        http_info = self._change_api_version_v2_http_info(request)
        return self._call_api(**http_info)

    def change_api_version_v2_async_invoker(self, request):
        http_info = self._change_api_version_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _change_api_version_v2_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/apis/publish/{api_id}",
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
        r"""校验API分组名称是否存在

        校验API分组名称是否存在。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CheckApiGroupsV2
        :type request: :class:`huaweicloudsdkroma.v2.CheckApiGroupsV2Request`
        :rtype: :class:`huaweicloudsdkroma.v2.CheckApiGroupsV2Response`
        """
        http_info = self._check_api_groups_v2_http_info(request)
        return self._call_api(**http_info)

    def check_api_groups_v2_async_invoker(self, request):
        http_info = self._check_api_groups_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _check_api_groups_v2_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/api-groups/check",
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
        r"""校验API定义

        校验API定义。校验API的路径或名称是否已存在
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CheckApisV2
        :type request: :class:`huaweicloudsdkroma.v2.CheckApisV2Request`
        :rtype: :class:`huaweicloudsdkroma.v2.CheckApisV2Response`
        """
        http_info = self._check_apis_v2_http_info(request)
        return self._call_api(**http_info)

    def check_apis_v2_async_invoker(self, request):
        http_info = self._check_apis_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _check_apis_v2_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/apis/check",
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
        r"""创建API分组

        API分组是API的管理单元，一个API分组等同于一个服务入口，创建API分组时，返回一个子域名作为访问入口。建议一个API分组下的API具有一定的相关性。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateApiGroupV2
        :type request: :class:`huaweicloudsdkroma.v2.CreateApiGroupV2Request`
        :rtype: :class:`huaweicloudsdkroma.v2.CreateApiGroupV2Response`
        """
        http_info = self._create_api_group_v2_http_info(request)
        return self._call_api(**http_info)

    def create_api_group_v2_async_invoker(self, request):
        http_info = self._create_api_group_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_api_group_v2_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/api-groups",
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
        r"""创建API

        添加一个API，API即一个服务接口，具体的服务能力。
        API分为两部分，第一部分为面向API使用者的API接口，定义了使用者如何调用这个API。第二部分面向API提供者，由API提供者定义这个API的真实的后端情况，定义了[ROMA Connect](tag:hws,hws_hk,hcs,hcs_sm,fcs,g42)[ROMA Site](tag:Site)如何去访问真实的后端服务。API的真实后端服务目前支持的类型：传统的HTTP/HTTPS形式的web后端、[函数工作流、](tag:hws,hws_hk,hcs,hcs_sm,fcs,g42)MOCK。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateApiV2
        :type request: :class:`huaweicloudsdkroma.v2.CreateApiV2Request`
        :rtype: :class:`huaweicloudsdkroma.v2.CreateApiV2Response`
        """
        http_info = self._create_api_v2_http_info(request)
        return self._call_api(**http_info)

    def create_api_v2_async_invoker(self, request):
        http_info = self._create_api_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_api_v2_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/apis",
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
        r"""发布或下线API

        对API进行发布或下线。
        
        发布操作是将一个指定的API发布到一个指定的环境，API只有发布后，才能够被调用，且只能在该环境上才能被调用。未发布的API无法被调用。
        
        下线操作是将API从某个已发布的环境上下线，下线后，API将无法再被调用。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateOrDeletePublishRecordForApiV2
        :type request: :class:`huaweicloudsdkroma.v2.CreateOrDeletePublishRecordForApiV2Request`
        :rtype: :class:`huaweicloudsdkroma.v2.CreateOrDeletePublishRecordForApiV2Response`
        """
        http_info = self._create_or_delete_publish_record_for_api_v2_http_info(request)
        return self._call_api(**http_info)

    def create_or_delete_publish_record_for_api_v2_async_invoker(self, request):
        http_info = self._create_or_delete_publish_record_for_api_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_or_delete_publish_record_for_api_v2_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/apis/action",
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
        r"""调试API

        调试一个API在指定运行环境下的定义，接口调用者需要具有操作该API的权限。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DebugApiV2
        :type request: :class:`huaweicloudsdkroma.v2.DebugApiV2Request`
        :rtype: :class:`huaweicloudsdkroma.v2.DebugApiV2Response`
        """
        http_info = self._debug_api_v2_http_info(request)
        return self._call_api(**http_info)

    def debug_api_v2_async_invoker(self, request):
        http_info = self._debug_api_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _debug_api_v2_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/apis/debug/{api_id}",
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
        r"""根据版本编号下线API

        对某个生效中的API版本进行下线操作，下线后，API在该版本生效的环境中将不再能够被调用。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteApiByVersionIdV2
        :type request: :class:`huaweicloudsdkroma.v2.DeleteApiByVersionIdV2Request`
        :rtype: :class:`huaweicloudsdkroma.v2.DeleteApiByVersionIdV2Response`
        """
        http_info = self._delete_api_by_version_id_v2_http_info(request)
        return self._call_api(**http_info)

    def delete_api_by_version_id_v2_async_invoker(self, request):
        http_info = self._delete_api_by_version_id_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_api_by_version_id_v2_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/apis/versions/{version_id}",
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
        r"""删除API分组

        删除指定的API分组。
        
        分组下存在API时分组无法删除，需要删除所有分组下的API后，再删除分组。
        
        删除分组时，会一并删除直接或间接关联到该分组下的所有资源，包括独立域名、SSL证书等等。并会将外部域名与子域名的绑定关系进行解除（取决于域名cname方式）。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteApiGroupV2
        :type request: :class:`huaweicloudsdkroma.v2.DeleteApiGroupV2Request`
        :rtype: :class:`huaweicloudsdkroma.v2.DeleteApiGroupV2Response`
        """
        http_info = self._delete_api_group_v2_http_info(request)
        return self._call_api(**http_info)

    def delete_api_group_v2_async_invoker(self, request):
        http_info = self._delete_api_group_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_api_group_v2_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/api-groups/{group_id}",
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
        r"""删除API

        删除指定的API。
        
        删除API时，会删除该API所有相关的资源信息或绑定关系，如API的发布记录，绑定的后端服务，对APP的授权信息等。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteApiV2
        :type request: :class:`huaweicloudsdkroma.v2.DeleteApiV2Request`
        :rtype: :class:`huaweicloudsdkroma.v2.DeleteApiV2Response`
        """
        http_info = self._delete_api_v2_http_info(request)
        return self._call_api(**http_info)

    def delete_api_v2_async_invoker(self, request):
        http_info = self._delete_api_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_api_v2_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/apis/{api_id}",
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
        r"""解除API与流控策略的绑定关系

        解除API与流控策略的绑定关系。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DisassociateRequestThrottlingPolicyV2
        :type request: :class:`huaweicloudsdkroma.v2.DisassociateRequestThrottlingPolicyV2Request`
        :rtype: :class:`huaweicloudsdkroma.v2.DisassociateRequestThrottlingPolicyV2Response`
        """
        http_info = self._disassociate_request_throttling_policy_v2_http_info(request)
        return self._call_api(**http_info)

    def disassociate_request_throttling_policy_v2_async_invoker(self, request):
        http_info = self._disassociate_request_throttling_policy_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _disassociate_request_throttling_policy_v2_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/throttle-bindings/{throttle_binding_id}",
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
        r"""查询分组列表

        查询API分组列表。
        
        如果是租户操作，则查询该租户下所有的分组；如果是管理员操作，则查询的是所有租户的分组。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListApiGroupsV2
        :type request: :class:`huaweicloudsdkroma.v2.ListApiGroupsV2Request`
        :rtype: :class:`huaweicloudsdkroma.v2.ListApiGroupsV2Response`
        """
        http_info = self._list_api_groups_v2_http_info(request)
        return self._call_api(**http_info)

    def list_api_groups_v2_async_invoker(self, request):
        http_info = self._list_api_groups_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_api_groups_v2_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/api-groups",
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
        if 'roma_app_id' in local_var_params:
            query_params.append(('roma_app_id', local_var_params['roma_app_id']))
        if 'precise_search' in local_var_params:
            query_params.append(('precise_search', local_var_params['precise_search']))
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

    def list_api_runtime_definition_v2_async(self, request):
        r"""查询API运行时定义

        查看指定的API在指定的环境上的运行时定义，默认查询RELEASE环境上的运行时定义。
        
        API的定义分为临时定义和运行时定义，分别代表如下含义：
        - 临时定义：API在编辑中的定义，表示用户最后一次编辑后的API的状态
        - 运行时定义：API在发布到某个环境时，对发布时的API的临时定义进行快照，固化出来的API的状态。
        
        访问某个环境上的API，其实访问的就是其运行时的定义
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListApiRuntimeDefinitionV2
        :type request: :class:`huaweicloudsdkroma.v2.ListApiRuntimeDefinitionV2Request`
        :rtype: :class:`huaweicloudsdkroma.v2.ListApiRuntimeDefinitionV2Response`
        """
        http_info = self._list_api_runtime_definition_v2_http_info(request)
        return self._call_api(**http_info)

    def list_api_runtime_definition_v2_async_invoker(self, request):
        http_info = self._list_api_runtime_definition_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_api_runtime_definition_v2_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/apis/runtime/{api_id}",
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
        r"""查看版本详情

        查询某个指定的版本详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListApiVersionDetailV2
        :type request: :class:`huaweicloudsdkroma.v2.ListApiVersionDetailV2Request`
        :rtype: :class:`huaweicloudsdkroma.v2.ListApiVersionDetailV2Response`
        """
        http_info = self._list_api_version_detail_v2_http_info(request)
        return self._call_api(**http_info)

    def list_api_version_detail_v2_async_invoker(self, request):
        http_info = self._list_api_version_detail_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_api_version_detail_v2_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/apis/versions/{version_id}",
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
        r"""查询API历史版本列表

        查询某个API的历史版本。每个API在一个环境上最多存在10个历史版本。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListApiVersionsV2
        :type request: :class:`huaweicloudsdkroma.v2.ListApiVersionsV2Request`
        :rtype: :class:`huaweicloudsdkroma.v2.ListApiVersionsV2Response`
        """
        http_info = self._list_api_versions_v2_http_info(request)
        return self._call_api(**http_info)

    def list_api_versions_v2_async_invoker(self, request):
        http_info = self._list_api_versions_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_api_versions_v2_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/apis/publish/{api_id}",
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
        r"""查看流控策略绑定的API列表

        查询某个流控策略上已经绑定的API列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListApisBindedToRequestThrottlingPolicyV2
        :type request: :class:`huaweicloudsdkroma.v2.ListApisBindedToRequestThrottlingPolicyV2Request`
        :rtype: :class:`huaweicloudsdkroma.v2.ListApisBindedToRequestThrottlingPolicyV2Response`
        """
        http_info = self._list_apis_binded_to_request_throttling_policy_v2_http_info(request)
        return self._call_api(**http_info)

    def list_apis_binded_to_request_throttling_policy_v2_async_invoker(self, request):
        http_info = self._list_apis_binded_to_request_throttling_policy_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_apis_binded_to_request_throttling_policy_v2_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/throttle-bindings/binded-apis",
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
        r"""查看流控策略未绑定的API列表

        查询所有未绑定到该流控策略上的自有API列表。需要API已经发布，未发布的API不予展示。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListApisUnbindedToRequestThrottlingPolicyV2
        :type request: :class:`huaweicloudsdkroma.v2.ListApisUnbindedToRequestThrottlingPolicyV2Request`
        :rtype: :class:`huaweicloudsdkroma.v2.ListApisUnbindedToRequestThrottlingPolicyV2Response`
        """
        http_info = self._list_apis_unbinded_to_request_throttling_policy_v2_http_info(request)
        return self._call_api(**http_info)

    def list_apis_unbinded_to_request_throttling_policy_v2_async_invoker(self, request):
        http_info = self._list_apis_unbinded_to_request_throttling_policy_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_apis_unbinded_to_request_throttling_policy_v2_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/throttle-bindings/unbinded-apis",
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
        r"""查询API列表

        查看API列表，返回API详细信息、发布信息等，但不能查看到后端服务信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListApisV2
        :type request: :class:`huaweicloudsdkroma.v2.ListApisV2Request`
        :rtype: :class:`huaweicloudsdkroma.v2.ListApisV2Response`
        """
        http_info = self._list_apis_v2_http_info(request)
        return self._call_api(**http_info)

    def list_apis_v2_async_invoker(self, request):
        http_info = self._list_apis_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_apis_v2_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/apis",
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
        if 'vpc_channel_id' in local_var_params:
            query_params.append(('vpc_channel_id', local_var_params['vpc_channel_id']))
        if 'vpc_channel_name' in local_var_params:
            query_params.append(('vpc_channel_name', local_var_params['vpc_channel_name']))
        if 'roma_app_name' in local_var_params:
            query_params.append(('roma_app_name', local_var_params['roma_app_name']))
        if 'roma_app_id' in local_var_params:
            query_params.append(('roma_app_id', local_var_params['roma_app_id']))

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
        r"""查看API绑定的流控策略列表

        查询某个API绑定的流控策略列表。每个环境上应该最多只有一个流控策略。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListRequestThrottlingPoliciesBindedToApiV2
        :type request: :class:`huaweicloudsdkroma.v2.ListRequestThrottlingPoliciesBindedToApiV2Request`
        :rtype: :class:`huaweicloudsdkroma.v2.ListRequestThrottlingPoliciesBindedToApiV2Response`
        """
        http_info = self._list_request_throttling_policies_binded_to_api_v2_http_info(request)
        return self._call_api(**http_info)

    def list_request_throttling_policies_binded_to_api_v2_async_invoker(self, request):
        http_info = self._list_request_throttling_policies_binded_to_api_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_request_throttling_policies_binded_to_api_v2_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/throttle-bindings/binded-throttles",
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
        r"""查询分组详情

        查询指定分组的详细信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowDetailsOfApiGroupV2
        :type request: :class:`huaweicloudsdkroma.v2.ShowDetailsOfApiGroupV2Request`
        :rtype: :class:`huaweicloudsdkroma.v2.ShowDetailsOfApiGroupV2Response`
        """
        http_info = self._show_details_of_api_group_v2_http_info(request)
        return self._call_api(**http_info)

    def show_details_of_api_group_v2_async_invoker(self, request):
        http_info = self._show_details_of_api_group_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_details_of_api_group_v2_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/api-groups/{group_id}",
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
        r"""查询API详情

        查看指定的API的详细信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowDetailsOfApiV2
        :type request: :class:`huaweicloudsdkroma.v2.ShowDetailsOfApiV2Request`
        :rtype: :class:`huaweicloudsdkroma.v2.ShowDetailsOfApiV2Response`
        """
        http_info = self._show_details_of_api_v2_http_info(request)
        return self._call_api(**http_info)

    def show_details_of_api_v2_async_invoker(self, request):
        http_info = self._show_details_of_api_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_details_of_api_v2_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/apis/{api_id}",
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
        r"""修改API分组

        修改API分组属性。其中name和remark可修改，其他属性不可修改。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateApiGroupV2
        :type request: :class:`huaweicloudsdkroma.v2.UpdateApiGroupV2Request`
        :rtype: :class:`huaweicloudsdkroma.v2.UpdateApiGroupV2Response`
        """
        http_info = self._update_api_group_v2_http_info(request)
        return self._call_api(**http_info)

    def update_api_group_v2_async_invoker(self, request):
        http_info = self._update_api_group_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_api_group_v2_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/api-groups/{group_id}",
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
        r"""修改API

        修改指定API的信息，包括后端服务信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateApiV2
        :type request: :class:`huaweicloudsdkroma.v2.UpdateApiV2Request`
        :rtype: :class:`huaweicloudsdkroma.v2.UpdateApiV2Response`
        """
        http_info = self._update_api_v2_http_info(request)
        return self._call_api(**http_info)

    def update_api_v2_async_invoker(self, request):
        http_info = self._update_api_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_api_v2_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/apis/{api_id}",
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
        r"""批量解除API与ACL策略的绑定

        批量解除API与ACL策略的绑定
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchDeleteApiAclBindingV2
        :type request: :class:`huaweicloudsdkroma.v2.BatchDeleteApiAclBindingV2Request`
        :rtype: :class:`huaweicloudsdkroma.v2.BatchDeleteApiAclBindingV2Response`
        """
        http_info = self._batch_delete_api_acl_binding_v2_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_api_acl_binding_v2_async_invoker(self, request):
        http_info = self._batch_delete_api_acl_binding_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_delete_api_acl_binding_v2_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/acl-bindings",
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
        r"""将API与ACL策略进行绑定

        将API与ACL策略进行绑定。
        
        同一个API发布到不同的环境可以绑定不同的ACL策略；一个API在发布到特定环境后只能绑定一个同一种类型的ACL策略。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateApiAclBindingV2
        :type request: :class:`huaweicloudsdkroma.v2.CreateApiAclBindingV2Request`
        :rtype: :class:`huaweicloudsdkroma.v2.CreateApiAclBindingV2Response`
        """
        http_info = self._create_api_acl_binding_v2_http_info(request)
        return self._call_api(**http_info)

    def create_api_acl_binding_v2_async_invoker(self, request):
        http_info = self._create_api_acl_binding_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_api_acl_binding_v2_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/acl-bindings",
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
        r"""解除API与ACL策略的绑定

        解除某条API与ACL策略的绑定关系
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteApiAclBindingV2
        :type request: :class:`huaweicloudsdkroma.v2.DeleteApiAclBindingV2Request`
        :rtype: :class:`huaweicloudsdkroma.v2.DeleteApiAclBindingV2Response`
        """
        http_info = self._delete_api_acl_binding_v2_http_info(request)
        return self._call_api(**http_info)

    def delete_api_acl_binding_v2_async_invoker(self, request):
        http_info = self._delete_api_acl_binding_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_api_acl_binding_v2_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/acl-bindings/{acl_bindings_id}",
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
        r"""查看API绑定的ACL策略列表

        查看API绑定的ACL策略列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAclPolicyBindedToApiV2
        :type request: :class:`huaweicloudsdkroma.v2.ListAclPolicyBindedToApiV2Request`
        :rtype: :class:`huaweicloudsdkroma.v2.ListAclPolicyBindedToApiV2Response`
        """
        http_info = self._list_acl_policy_binded_to_api_v2_http_info(request)
        return self._call_api(**http_info)

    def list_acl_policy_binded_to_api_v2_async_invoker(self, request):
        http_info = self._list_acl_policy_binded_to_api_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_acl_policy_binded_to_api_v2_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/acl-bindings/binded-acls",
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
        r"""查看ACL策略绑定的API列表

        查看ACL策略绑定的API列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListApisBindedToAclPolicyV2
        :type request: :class:`huaweicloudsdkroma.v2.ListApisBindedToAclPolicyV2Request`
        :rtype: :class:`huaweicloudsdkroma.v2.ListApisBindedToAclPolicyV2Response`
        """
        http_info = self._list_apis_binded_to_acl_policy_v2_http_info(request)
        return self._call_api(**http_info)

    def list_apis_binded_to_acl_policy_v2_async_invoker(self, request):
        http_info = self._list_apis_binded_to_acl_policy_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_apis_binded_to_acl_policy_v2_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/acl-bindings/binded-apis",
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
        r"""查看ACL策略未绑定的API列表

        查看ACL策略未绑定的API列表，需要API已发布
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListApisUnbindedToAclPolicyV2
        :type request: :class:`huaweicloudsdkroma.v2.ListApisUnbindedToAclPolicyV2Request`
        :rtype: :class:`huaweicloudsdkroma.v2.ListApisUnbindedToAclPolicyV2Response`
        """
        http_info = self._list_apis_unbinded_to_acl_policy_v2_http_info(request)
        return self._call_api(**http_info)

    def list_apis_unbinded_to_acl_policy_v2_async_invoker(self, request):
        http_info = self._list_apis_unbinded_to_acl_policy_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_apis_unbinded_to_acl_policy_v2_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/acl-bindings/unbinded-apis",
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
        r"""解除授权

        解除API对APP的授权关系。解除授权后，APP将不再能够调用该API。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CancelingAuthorizationV2
        :type request: :class:`huaweicloudsdkroma.v2.CancelingAuthorizationV2Request`
        :rtype: :class:`huaweicloudsdkroma.v2.CancelingAuthorizationV2Response`
        """
        http_info = self._canceling_authorization_v2_http_info(request)
        return self._call_api(**http_info)

    def canceling_authorization_v2_async_invoker(self, request):
        http_info = self._canceling_authorization_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _canceling_authorization_v2_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/app-auths/{app_auth_id}",
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
        r"""APP授权

        APP创建成功后，还不能访问API，如果想要访问某个环境上的API，需要将该API在该环境上授权给APP。授权成功后，APP即可访问该环境上的这个API。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateAuthorizingAppsV2
        :type request: :class:`huaweicloudsdkroma.v2.CreateAuthorizingAppsV2Request`
        :rtype: :class:`huaweicloudsdkroma.v2.CreateAuthorizingAppsV2Response`
        """
        http_info = self._create_authorizing_apps_v2_http_info(request)
        return self._call_api(**http_info)

    def create_authorizing_apps_v2_async_invoker(self, request):
        http_info = self._create_authorizing_apps_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_authorizing_apps_v2_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/app-auths",
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
        r"""查看APP已绑定的API列表

        查询APP已经绑定的API列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListApisBindedToAppV2
        :type request: :class:`huaweicloudsdkroma.v2.ListApisBindedToAppV2Request`
        :rtype: :class:`huaweicloudsdkroma.v2.ListApisBindedToAppV2Response`
        """
        http_info = self._list_apis_binded_to_app_v2_http_info(request)
        return self._call_api(**http_info)

    def list_apis_binded_to_app_v2_async_invoker(self, request):
        http_info = self._list_apis_binded_to_app_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_apis_binded_to_app_v2_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/app-auths/binded-apis",
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
        r"""查看APP未绑定的API列表

        查询指定环境上某个APP未绑定的API列表，包括自有API和从云市场购买的API。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListApisUnbindedToAppV2
        :type request: :class:`huaweicloudsdkroma.v2.ListApisUnbindedToAppV2Request`
        :rtype: :class:`huaweicloudsdkroma.v2.ListApisUnbindedToAppV2Response`
        """
        http_info = self._list_apis_unbinded_to_app_v2_http_info(request)
        return self._call_api(**http_info)

    def list_apis_unbinded_to_app_v2_async_invoker(self, request):
        http_info = self._list_apis_unbinded_to_app_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_apis_unbinded_to_app_v2_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/app-auths/unbinded-apis",
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
        r"""查看API已绑定的APP列表

        查询API绑定的APP列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAppsBindedToApiV2
        :type request: :class:`huaweicloudsdkroma.v2.ListAppsBindedToApiV2Request`
        :rtype: :class:`huaweicloudsdkroma.v2.ListAppsBindedToApiV2Response`
        """
        http_info = self._list_apps_binded_to_api_v2_http_info(request)
        return self._call_api(**http_info)

    def list_apps_binded_to_api_v2_async_invoker(self, request):
        http_info = self._list_apps_binded_to_api_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_apps_binded_to_api_v2_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/app-auths/binded-apps",
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

    def list_duplicate_apis_for_app_v2_async(self, request):
        r"""查看APP下路径冲突的api列表

        查询指定APP下路径冲突的api列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListDuplicateApisForAppV2
        :type request: :class:`huaweicloudsdkroma.v2.ListDuplicateApisForAppV2Request`
        :rtype: :class:`huaweicloudsdkroma.v2.ListDuplicateApisForAppV2Response`
        """
        http_info = self._list_duplicate_apis_for_app_v2_http_info(request)
        return self._call_api(**http_info)

    def list_duplicate_apis_for_app_v2_async_invoker(self, request):
        http_info = self._list_duplicate_apis_for_app_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_duplicate_apis_for_app_v2_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/app-auths/duplicate-apis",
            "request_type": request.__class__.__name__,
            "response_type": "ListDuplicateApisForAppV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'app_id' in local_var_params:
            query_params.append(('app_id', local_var_params['app_id']))

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

    def add_user_to_app_async(self, request):
        r"""设置用户成员

        - 设置应用的用户成员，为空数组时会清空已有应用成员列表
        - 设置动作为全量更新非增量更新，应用的成员列表都会替换为当次请求的应用成员列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AddUserToApp
        :type request: :class:`huaweicloudsdkroma.v2.AddUserToAppRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.AddUserToAppResponse`
        """
        http_info = self._add_user_to_app_http_info(request)
        return self._call_api(**http_info)

    def add_user_to_app_async_invoker(self, request):
        http_info = self._add_user_to_app_http_info(request)
        return AsyncInvoker(self, http_info)

    def _add_user_to_app_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/apps/{app_id}/users",
            "request_type": request.__class__.__name__,
            "response_type": "AddUserToAppResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'app_id' in local_var_params:
            path_params['app_id'] = local_var_params['app_id']
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

    def check_auth_users_of_app_async(self, request):
        r"""查询用户成员列表

        查询用户成列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CheckAuthUsersOfApp
        :type request: :class:`huaweicloudsdkroma.v2.CheckAuthUsersOfAppRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.CheckAuthUsersOfAppResponse`
        """
        http_info = self._check_auth_users_of_app_http_info(request)
        return self._call_api(**http_info)

    def check_auth_users_of_app_async_invoker(self, request):
        http_info = self._check_auth_users_of_app_http_info(request)
        return AsyncInvoker(self, http_info)

    def _check_auth_users_of_app_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/apps/{app_id}/users",
            "request_type": request.__class__.__name__,
            "response_type": "CheckAuthUsersOfAppResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'app_id' in local_var_params:
            path_params['app_id'] = local_var_params['app_id']
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'user_name' in local_var_params:
            query_params.append(('user_name', local_var_params['user_name']))

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

    def check_can_auth_users_of_app_async(self, request):
        r"""查询候选用户成员

        查询应用的候选用户成员列表,会过滤掉异常状态用户
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CheckCanAuthUsersOfApp
        :type request: :class:`huaweicloudsdkroma.v2.CheckCanAuthUsersOfAppRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.CheckCanAuthUsersOfAppResponse`
        """
        http_info = self._check_can_auth_users_of_app_http_info(request)
        return self._call_api(**http_info)

    def check_can_auth_users_of_app_async_invoker(self, request):
        http_info = self._check_can_auth_users_of_app_http_info(request)
        return AsyncInvoker(self, http_info)

    def _check_can_auth_users_of_app_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/apps/{app_id}/candidates",
            "request_type": request.__class__.__name__,
            "response_type": "CheckCanAuthUsersOfAppResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'app_id' in local_var_params:
            path_params['app_id'] = local_var_params['app_id']
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
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

    def check_roma_app_details_async(self, request):
        r"""查询应用详情

        查询应用详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CheckRomaAppDetails
        :type request: :class:`huaweicloudsdkroma.v2.CheckRomaAppDetailsRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.CheckRomaAppDetailsResponse`
        """
        http_info = self._check_roma_app_details_http_info(request)
        return self._call_api(**http_info)

    def check_roma_app_details_async_invoker(self, request):
        http_info = self._check_roma_app_details_http_info(request)
        return AsyncInvoker(self, http_info)

    def _check_roma_app_details_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/apps/{app_id}",
            "request_type": request.__class__.__name__,
            "response_type": "CheckRomaAppDetailsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'app_id' in local_var_params:
            path_params['app_id'] = local_var_params['app_id']
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

    def check_roma_app_secret_async(self, request):
        r"""查询应用密钥

        查询应用密钥
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CheckRomaAppSecret
        :type request: :class:`huaweicloudsdkroma.v2.CheckRomaAppSecretRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.CheckRomaAppSecretResponse`
        """
        http_info = self._check_roma_app_secret_http_info(request)
        return self._call_api(**http_info)

    def check_roma_app_secret_async_invoker(self, request):
        http_info = self._check_roma_app_secret_http_info(request)
        return AsyncInvoker(self, http_info)

    def _check_roma_app_secret_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/apps/{app_id}/secret",
            "request_type": request.__class__.__name__,
            "response_type": "CheckRomaAppSecretResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'app_id' in local_var_params:
            path_params['app_id'] = local_var_params['app_id']
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

    def create_roma_app_async(self, request):
        r"""创建应用

        创建应用
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateRomaApp
        :type request: :class:`huaweicloudsdkroma.v2.CreateRomaAppRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.CreateRomaAppResponse`
        """
        http_info = self._create_roma_app_http_info(request)
        return self._call_api(**http_info)

    def create_roma_app_async_invoker(self, request):
        http_info = self._create_roma_app_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_roma_app_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/apps",
            "request_type": request.__class__.__name__,
            "response_type": "CreateRomaAppResponse"
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

    def delete_roma_app_async(self, request):
        r"""删除应用

        删除单个应用
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteRomaApp
        :type request: :class:`huaweicloudsdkroma.v2.DeleteRomaAppRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.DeleteRomaAppResponse`
        """
        http_info = self._delete_roma_app_http_info(request)
        return self._call_api(**http_info)

    def delete_roma_app_async_invoker(self, request):
        http_info = self._delete_roma_app_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_roma_app_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/apps/{app_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteRomaAppResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'app_id' in local_var_params:
            path_params['app_id'] = local_var_params['app_id']
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

    def list_roma_app_async(self, request):
        r"""查询应用列表

        查询应用列表，支持条件查询，所有条件是并且的关系
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListRomaApp
        :type request: :class:`huaweicloudsdkroma.v2.ListRomaAppRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.ListRomaAppResponse`
        """
        http_info = self._list_roma_app_http_info(request)
        return self._call_api(**http_info)

    def list_roma_app_async_invoker(self, request):
        http_info = self._list_roma_app_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_roma_app_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/apps",
            "request_type": request.__class__.__name__,
            "response_type": "ListRomaAppResponse"
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
        if 'favorite' in local_var_params:
            query_params.append(('favorite', local_var_params['favorite']))
        if 'auth_role' in local_var_params:
            query_params.append(('auth_role', local_var_params['auth_role']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'owner' in local_var_params:
            query_params.append(('owner', local_var_params['owner']))
        if 'user_name' in local_var_params:
            query_params.append(('user_name', local_var_params['user_name']))

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

    def reset_roma_app_secret_async(self, request):
        r"""重置应用密钥

        重置应用密钥
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ResetRomaAppSecret
        :type request: :class:`huaweicloudsdkroma.v2.ResetRomaAppSecretRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.ResetRomaAppSecretResponse`
        """
        http_info = self._reset_roma_app_secret_http_info(request)
        return self._call_api(**http_info)

    def reset_roma_app_secret_async_invoker(self, request):
        http_info = self._reset_roma_app_secret_http_info(request)
        return AsyncInvoker(self, http_info)

    def _reset_roma_app_secret_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/apps/{app_id}/secret",
            "request_type": request.__class__.__name__,
            "response_type": "ResetRomaAppSecretResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'app_id' in local_var_params:
            path_params['app_id'] = local_var_params['app_id']
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

    def update_roma_app_async(self, request):
        r"""更新应用

        更新应用
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateRomaApp
        :type request: :class:`huaweicloudsdkroma.v2.UpdateRomaAppRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.UpdateRomaAppResponse`
        """
        http_info = self._update_roma_app_http_info(request)
        return self._call_api(**http_info)

    def update_roma_app_async_invoker(self, request):
        http_info = self._update_roma_app_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_roma_app_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/apps/{app_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateRomaAppResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'app_id' in local_var_params:
            path_params['app_id'] = local_var_params['app_id']
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

    def validate_roma_app_async(self, request):
        r"""校验应用是否存在

        校验指定条件的应用是否存在
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ValidateRomaApp
        :type request: :class:`huaweicloudsdkroma.v2.ValidateRomaAppRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.ValidateRomaAppResponse`
        """
        http_info = self._validate_roma_app_http_info(request)
        return self._call_api(**http_info)

    def validate_roma_app_async_invoker(self, request):
        http_info = self._validate_roma_app_http_info(request)
        return AsyncInvoker(self, http_info)

    def _validate_roma_app_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/validate-apps",
            "request_type": request.__class__.__name__,
            "response_type": "ValidateRomaAppResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'key' in local_var_params:
            query_params.append(('key', local_var_params['key']))

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

    def check_asset_job_status_async(self, request):
        r"""查询作业进度

        查询作业进度
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CheckAssetJobStatus
        :type request: :class:`huaweicloudsdkroma.v2.CheckAssetJobStatusRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.CheckAssetJobStatusResponse`
        """
        http_info = self._check_asset_job_status_http_info(request)
        return self._call_api(**http_info)

    def check_asset_job_status_async_invoker(self, request):
        http_info = self._check_asset_job_status_http_info(request)
        return AsyncInvoker(self, http_info)

    def _check_asset_job_status_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/assets/jobs/{job_id}",
            "request_type": request.__class__.__name__,
            "response_type": "CheckAssetJobStatusResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
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

    def delete_asset_async(self, request):
        r"""批量删除资产

        批量删除资产
        - 创建批量删除指定条件的资产的作业任务
        - 最大支持100个应用和任务
        - 一个用户同一时刻只能创建一个资产删除作业任务，没有Running状态的作业任务存在
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteAsset
        :type request: :class:`huaweicloudsdkroma.v2.DeleteAssetRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.DeleteAssetResponse`
        """
        http_info = self._delete_asset_http_info(request)
        return self._call_api(**http_info)

    def delete_asset_async_invoker(self, request):
        http_info = self._delete_asset_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_asset_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/assets/delete",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteAssetResponse"
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

    def download_asset_archive_async(self, request):
        r"""下载资产包

        - 导出作业执行成功后，通过该接口获取导出作业产生的资产包，仅能下载一次
        - 可先压缩后存在数据库，下载后删除
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DownloadAssetArchive
        :type request: :class:`huaweicloudsdkroma.v2.DownloadAssetArchiveRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.DownloadAssetArchiveResponse`
        """
        http_info = self._download_asset_archive_http_info(request)
        return self._call_api(**http_info)

    def download_asset_archive_async_invoker(self, request):
        http_info = self._download_asset_archive_http_info(request)
        return AsyncInvoker(self, http_info)

    def _download_asset_archive_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/assets/archives/{archive_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DownloadAssetArchiveResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'archive_id' in local_var_params:
            path_params['archive_id'] = local_var_params['archive_id']

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

    def export_asset_async(self, request):
        r"""批量导出资产

        批量导出资产
        - 创建批量导出指定条件的资产的作业任务
        - 最大支持100个应用和任务
        - 一个用户同一时刻只能创建一个资产导出作业任务，没有Running状态的作业任务存在
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ExportAsset
        :type request: :class:`huaweicloudsdkroma.v2.ExportAssetRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.ExportAssetResponse`
        """
        http_info = self._export_asset_http_info(request)
        return self._call_api(**http_info)

    def export_asset_async_invoker(self, request):
        http_info = self._export_asset_http_info(request)
        return AsyncInvoker(self, http_info)

    def _export_asset_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/assets/export",
            "request_type": request.__class__.__name__,
            "response_type": "ExportAssetResponse"
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

    def import_asset_async(self, request):
        r"""导入资产

        - 创建导入资产作业任务，资产版本和具体哪些资产从资产内容里读取
        - 最大支持100个应用和任务
        - 一个用户同一时刻只能创建一个资产导入作业任务，没有Running状态的作业任务存在
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ImportAsset
        :type request: :class:`huaweicloudsdkroma.v2.ImportAssetRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.ImportAssetResponse`
        """
        http_info = self._import_asset_http_info(request)
        return self._call_api(**http_info)

    def import_asset_async_invoker(self, request):
        http_info = self._import_asset_http_info(request)
        return AsyncInvoker(self, http_info)

    def _import_asset_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/assets/import",
            "request_type": request.__class__.__name__,
            "response_type": "ImportAssetResponse"
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
        if 'import_asset_request_body' in local_var_params:
            form_params['ImportAssetRequestBody'] = local_var_params['import_asset_request_body']

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

    def check_dictionary_async(self, request):
        r"""查询字典详情

        查询字典详情,
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CheckDictionary
        :type request: :class:`huaweicloudsdkroma.v2.CheckDictionaryRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.CheckDictionaryResponse`
        """
        http_info = self._check_dictionary_http_info(request)
        return self._call_api(**http_info)

    def check_dictionary_async_invoker(self, request):
        http_info = self._check_dictionary_http_info(request)
        return AsyncInvoker(self, http_info)

    def _check_dictionary_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/dictionaries/{dict_id}",
            "request_type": request.__class__.__name__,
            "response_type": "CheckDictionaryResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'dict_id' in local_var_params:
            path_params['dict_id'] = local_var_params['dict_id']
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

    def create_dictionary_async(self, request):
        r"""创建字典

        创建字典
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateDictionary
        :type request: :class:`huaweicloudsdkroma.v2.CreateDictionaryRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.CreateDictionaryResponse`
        """
        http_info = self._create_dictionary_http_info(request)
        return self._call_api(**http_info)

    def create_dictionary_async_invoker(self, request):
        http_info = self._create_dictionary_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_dictionary_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/dictionaries",
            "request_type": request.__class__.__name__,
            "response_type": "CreateDictionaryResponse"
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

    def delete_dictionary_async(self, request):
        r"""删除字典

        删除单个字典，会同时删除该字典的所有子字典
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteDictionary
        :type request: :class:`huaweicloudsdkroma.v2.DeleteDictionaryRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.DeleteDictionaryResponse`
        """
        http_info = self._delete_dictionary_http_info(request)
        return self._call_api(**http_info)

    def delete_dictionary_async_invoker(self, request):
        http_info = self._delete_dictionary_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_dictionary_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/dictionaries/{dict_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteDictionaryResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'dict_id' in local_var_params:
            path_params['dict_id'] = local_var_params['dict_id']
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

    def list_dictionary_async(self, request):
        r"""查询字典列表

        查询字典列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListDictionary
        :type request: :class:`huaweicloudsdkroma.v2.ListDictionaryRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.ListDictionaryResponse`
        """
        http_info = self._list_dictionary_http_info(request)
        return self._call_api(**http_info)

    def list_dictionary_async_invoker(self, request):
        http_info = self._list_dictionary_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_dictionary_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/dictionaries",
            "request_type": request.__class__.__name__,
            "response_type": "ListDictionaryResponse"
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
        if 'parent_code' in local_var_params:
            query_params.append(('parent_code', local_var_params['parent_code']))
        if 'code' in local_var_params:
            query_params.append(('code', local_var_params['code']))
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

    def update_dictionary_async(self, request):
        r"""更新字典

        更新字典
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateDictionary
        :type request: :class:`huaweicloudsdkroma.v2.UpdateDictionaryRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.UpdateDictionaryResponse`
        """
        http_info = self._update_dictionary_http_info(request)
        return self._call_api(**http_info)

    def update_dictionary_async_invoker(self, request):
        http_info = self._update_dictionary_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_dictionary_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/dictionaries/{dict_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateDictionaryResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'dict_id' in local_var_params:
            path_params['dict_id'] = local_var_params['dict_id']
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

    def validate_dictionary_async(self, request):
        r"""校验字典是否存在

        校验指定条件的字典是否存在，支持字典名称和字典编码
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ValidateDictionary
        :type request: :class:`huaweicloudsdkroma.v2.ValidateDictionaryRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.ValidateDictionaryResponse`
        """
        http_info = self._validate_dictionary_http_info(request)
        return self._call_api(**http_info)

    def validate_dictionary_async_invoker(self, request):
        http_info = self._validate_dictionary_http_info(request)
        return AsyncInvoker(self, http_info)

    def _validate_dictionary_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/validate-dictionaries",
            "request_type": request.__class__.__name__,
            "response_type": "ValidateDictionaryResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'code' in local_var_params:
            query_params.append(('code', local_var_params['code']))

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

    def check_roma_instance_list_v2_async(self, request):
        r"""查询实例列表

        获取符合条件的服务实例列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CheckRomaInstanceListV2
        :type request: :class:`huaweicloudsdkroma.v2.CheckRomaInstanceListV2Request`
        :rtype: :class:`huaweicloudsdkroma.v2.CheckRomaInstanceListV2Response`
        """
        http_info = self._check_roma_instance_list_v2_http_info(request)
        return self._call_api(**http_info)

    def check_roma_instance_list_v2_async_invoker(self, request):
        http_info = self._check_roma_instance_list_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _check_roma_instance_list_v2_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/instances",
            "request_type": request.__class__.__name__,
            "response_type": "CheckRomaInstanceListV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
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

    def list_mqs_instance_async(self, request):
        r"""查询MQS实例列表

        查询MQS实例列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListMqsInstance
        :type request: :class:`huaweicloudsdkroma.v2.ListMqsInstanceRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.ListMqsInstanceResponse`
        """
        http_info = self._list_mqs_instance_http_info(request)
        return self._call_api(**http_info)

    def list_mqs_instance_async_invoker(self, request):
        http_info = self._list_mqs_instance_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_mqs_instance_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/mqs/instances",
            "request_type": request.__class__.__name__,
            "response_type": "ListMqsInstanceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'include_internal' in local_var_params:
            query_params.append(('include_internal', local_var_params['include_internal']))

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

    def show_mqs_instance_async(self, request):
        r"""查询MQS实例详情

        查询指定MQS实例详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowMqsInstance
        :type request: :class:`huaweicloudsdkroma.v2.ShowMqsInstanceRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.ShowMqsInstanceResponse`
        """
        http_info = self._show_mqs_instance_http_info(request)
        return self._call_api(**http_info)

    def show_mqs_instance_async_invoker(self, request):
        http_info = self._show_mqs_instance_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_mqs_instance_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/mqs/instances/{instance_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowMqsInstanceResponse"
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

    def export_api_definitions_v2_async(self, request):
        r"""导出API

        导出分组下API的定义信息，导出文件内容符合swagger标准规范。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ExportApiDefinitionsV2
        :type request: :class:`huaweicloudsdkroma.v2.ExportApiDefinitionsV2Request`
        :rtype: :class:`huaweicloudsdkroma.v2.ExportApiDefinitionsV2Response`
        """
        http_info = self._export_api_definitions_v2_http_info(request)
        return self._call_api(**http_info)

    def export_api_definitions_v2_async_invoker(self, request):
        http_info = self._export_api_definitions_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _export_api_definitions_v2_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/openapi/export",
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

    def export_live_data_api_definitions_v2_async(self, request):
        r"""导出自定义后端API

        导出自定义后端API，导出文件内容符合swagger标准规范。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ExportLiveDataApiDefinitionsV2
        :type request: :class:`huaweicloudsdkroma.v2.ExportLiveDataApiDefinitionsV2Request`
        :rtype: :class:`huaweicloudsdkroma.v2.ExportLiveDataApiDefinitionsV2Response`
        """
        http_info = self._export_live_data_api_definitions_v2_http_info(request)
        return self._call_api(**http_info)

    def export_live_data_api_definitions_v2_async_invoker(self, request):
        http_info = self._export_live_data_api_definitions_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _export_live_data_api_definitions_v2_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/openapi/livedata-apis/export",
            "request_type": request.__class__.__name__,
            "response_type": "ExportLiveDataApiDefinitionsV2Response"
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

    def import_api_definitions_v2_async(self, request):
        r"""导入API

        导入API。导入文件内容需要符合swagger标准规范，自定义扩展字段请参考用户指南的“附录：前端API的Swagger扩展定义”章节。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ImportApiDefinitionsV2
        :type request: :class:`huaweicloudsdkroma.v2.ImportApiDefinitionsV2Request`
        :rtype: :class:`huaweicloudsdkroma.v2.ImportApiDefinitionsV2Response`
        """
        http_info = self._import_api_definitions_v2_http_info(request)
        return self._call_api(**http_info)

    def import_api_definitions_v2_async_invoker(self, request):
        http_info = self._import_api_definitions_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _import_api_definitions_v2_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/openapi/import",
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
        if 'app_id' in local_var_params:
            form_params['app_id'] = local_var_params['app_id']
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

    def import_live_data_api_definitions_v2_async(self, request):
        r"""导入自定义后端API

        导入自定义后端API。导入文件内容需要符合swagger标准规范，自定义扩展字段请参考用户指南的“附录：后端API的Swagger扩展定义”章节
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ImportLiveDataApiDefinitionsV2
        :type request: :class:`huaweicloudsdkroma.v2.ImportLiveDataApiDefinitionsV2Request`
        :rtype: :class:`huaweicloudsdkroma.v2.ImportLiveDataApiDefinitionsV2Response`
        """
        http_info = self._import_live_data_api_definitions_v2_http_info(request)
        return self._call_api(**http_info)

    def import_live_data_api_definitions_v2_async_invoker(self, request):
        http_info = self._import_live_data_api_definitions_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _import_live_data_api_definitions_v2_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/openapi/livedata-apis/import",
            "request_type": request.__class__.__name__,
            "response_type": "ImportLiveDataApiDefinitionsV2Response"
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
        if 'extend_mode' in local_var_params:
            form_params['extend_mode'] = local_var_params['extend_mode']
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
        r"""域名绑定SSL证书

        域名绑定SSL证书。[目前暂时仅支持单个绑定,请求体当中的certificate_ids里面有且只能有一个证书ID](tag:hws,hws_hk,fcs,g42,Site)
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchAssociateCertsV2
        :type request: :class:`huaweicloudsdkroma.v2.BatchAssociateCertsV2Request`
        :rtype: :class:`huaweicloudsdkroma.v2.BatchAssociateCertsV2Response`
        """
        http_info = self._batch_associate_certs_v2_http_info(request)
        return self._call_api(**http_info)

    def batch_associate_certs_v2_async_invoker(self, request):
        http_info = self._batch_associate_certs_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_associate_certs_v2_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/api-groups/{group_id}/domains/{domain_id}/certificates/attach",
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
        r"""SSL证书绑定域名

        SSL证书绑定域名
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchAssociateDomainsV2
        :type request: :class:`huaweicloudsdkroma.v2.BatchAssociateDomainsV2Request`
        :rtype: :class:`huaweicloudsdkroma.v2.BatchAssociateDomainsV2Response`
        """
        http_info = self._batch_associate_domains_v2_http_info(request)
        return self._call_api(**http_info)

    def batch_associate_domains_v2_async_invoker(self, request):
        http_info = self._batch_associate_domains_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_associate_domains_v2_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/apic/certificates/{certificate_id}/domains/attach",
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
        r"""域名解绑SSL证书

        域名解绑SSL证书。目前暂时仅支持单个解绑,请求体当中的certificate_ids里面有且只能有一个证书ID
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchDisassociateCertsV2
        :type request: :class:`huaweicloudsdkroma.v2.BatchDisassociateCertsV2Request`
        :rtype: :class:`huaweicloudsdkroma.v2.BatchDisassociateCertsV2Response`
        """
        http_info = self._batch_disassociate_certs_v2_http_info(request)
        return self._call_api(**http_info)

    def batch_disassociate_certs_v2_async_invoker(self, request):
        http_info = self._batch_disassociate_certs_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_disassociate_certs_v2_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/api-groups/{group_id}/domains/{domain_id}/certificates/detach",
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
        r"""SSL证书解绑域名

        SSL证书解绑域名
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchDisassociateDomainsV2
        :type request: :class:`huaweicloudsdkroma.v2.BatchDisassociateDomainsV2Request`
        :rtype: :class:`huaweicloudsdkroma.v2.BatchDisassociateDomainsV2Response`
        """
        http_info = self._batch_disassociate_domains_v2_http_info(request)
        return self._call_api(**http_info)

    def batch_disassociate_domains_v2_async_invoker(self, request):
        http_info = self._batch_disassociate_domains_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_disassociate_domains_v2_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/apic/certificates/{certificate_id}/domains/detach",
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
        r"""创建SSL证书

        创建SSL证书
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateCertificateV2
        :type request: :class:`huaweicloudsdkroma.v2.CreateCertificateV2Request`
        :rtype: :class:`huaweicloudsdkroma.v2.CreateCertificateV2Response`
        """
        http_info = self._create_certificate_v2_http_info(request)
        return self._call_api(**http_info)

    def create_certificate_v2_async_invoker(self, request):
        http_info = self._create_certificate_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_certificate_v2_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/apic/certificates",
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
        r"""删除SSL证书

        删除ssl证书接口,删除时只有没有关联域名的证书才能被删除
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteCertificateV2
        :type request: :class:`huaweicloudsdkroma.v2.DeleteCertificateV2Request`
        :rtype: :class:`huaweicloudsdkroma.v2.DeleteCertificateV2Response`
        """
        http_info = self._delete_certificate_v2_http_info(request)
        return self._call_api(**http_info)

    def delete_certificate_v2_async_invoker(self, request):
        http_info = self._delete_certificate_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_certificate_v2_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/apic/certificates/{certificate_id}",
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
        r"""获取SSL证书已绑定域名列表

        获取SSL证书已绑定域名列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAttachedDomainsV2
        :type request: :class:`huaweicloudsdkroma.v2.ListAttachedDomainsV2Request`
        :rtype: :class:`huaweicloudsdkroma.v2.ListAttachedDomainsV2Response`
        """
        http_info = self._list_attached_domains_v2_http_info(request)
        return self._call_api(**http_info)

    def list_attached_domains_v2_async_invoker(self, request):
        http_info = self._list_attached_domains_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_attached_domains_v2_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/apic/certificates/{certificate_id}/attached-domains",
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
        r"""获取SSL证书列表

        获取SSL证书列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListCertificatesV2
        :type request: :class:`huaweicloudsdkroma.v2.ListCertificatesV2Request`
        :rtype: :class:`huaweicloudsdkroma.v2.ListCertificatesV2Response`
        """
        http_info = self._list_certificates_v2_http_info(request)
        return self._call_api(**http_info)

    def list_certificates_v2_async_invoker(self, request):
        http_info = self._list_certificates_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_certificates_v2_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/apic/certificates",
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
        if 'algorithm_type' in local_var_params:
            query_params.append(('algorithm_type', local_var_params['algorithm_type']))

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
        r"""查看证书详情

        查看证书详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowDetailsOfCertificateV2
        :type request: :class:`huaweicloudsdkroma.v2.ShowDetailsOfCertificateV2Request`
        :rtype: :class:`huaweicloudsdkroma.v2.ShowDetailsOfCertificateV2Response`
        """
        http_info = self._show_details_of_certificate_v2_http_info(request)
        return self._call_api(**http_info)

    def show_details_of_certificate_v2_async_invoker(self, request):
        http_info = self._show_details_of_certificate_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_details_of_certificate_v2_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/apic/certificates/{certificate_id}",
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
        r"""修改SSL证书

        修改SSL证书
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateCertificateV2
        :type request: :class:`huaweicloudsdkroma.v2.UpdateCertificateV2Request`
        :rtype: :class:`huaweicloudsdkroma.v2.UpdateCertificateV2Response`
        """
        http_info = self._update_certificate_v2_http_info(request)
        return self._call_api(**http_info)

    def update_certificate_v2_async_invoker(self, request):
        http_info = self._update_certificate_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_certificate_v2_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/apic/certificates/{certificate_id}",
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
        r"""添加后端实例

        为指定的VPC通道添加后端实例
        
        若指定地址的后端实例已存在，则更新对应后端实例信息。若请求体中包含多个重复地址的后端实例定义，则使用第一个定义。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AddingBackendInstancesV2
        :type request: :class:`huaweicloudsdkroma.v2.AddingBackendInstancesV2Request`
        :rtype: :class:`huaweicloudsdkroma.v2.AddingBackendInstancesV2Response`
        """
        http_info = self._adding_backend_instances_v2_http_info(request)
        return self._call_api(**http_info)

    def adding_backend_instances_v2_async_invoker(self, request):
        http_info = self._adding_backend_instances_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _adding_backend_instances_v2_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/vpc-channels/{vpc_channel_id}/members",
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
        r"""批量修改后端服务器状态不可用

        批量修改后端服务器状态不可用。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchDisableMembers
        :type request: :class:`huaweicloudsdkroma.v2.BatchDisableMembersRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.BatchDisableMembersResponse`
        """
        http_info = self._batch_disable_members_http_info(request)
        return self._call_api(**http_info)

    def batch_disable_members_async_invoker(self, request):
        http_info = self._batch_disable_members_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_disable_members_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/vpc-channels/{vpc_channel_id}/members/batch-disable",
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
        r"""批量修改后端服务器状态可用

        批量修改后端服务器状态可用。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchEnableMembers
        :type request: :class:`huaweicloudsdkroma.v2.BatchEnableMembersRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.BatchEnableMembersResponse`
        """
        http_info = self._batch_enable_members_http_info(request)
        return self._call_api(**http_info)

    def batch_enable_members_async_invoker(self, request):
        http_info = self._batch_enable_members_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_enable_members_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/vpc-channels/{vpc_channel_id}/members/batch-enable",
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
        r"""添加VPC通道后端服务器组

        在服务集成中创建VPC通道后端服务器组，VPC通道后端实例可以选择是否关联后端实例服务器组，以便管理后端服务器节点。
        
        若指定名称的后端服务器组已存在，则更新对应后端服务器组信息。若请求体中包含多个重复名称的后端服务器定义，则使用第一个定义。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateMemberGroup
        :type request: :class:`huaweicloudsdkroma.v2.CreateMemberGroupRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.CreateMemberGroupResponse`
        """
        http_info = self._create_member_group_http_info(request)
        return self._call_api(**http_info)

    def create_member_group_async_invoker(self, request):
        http_info = self._create_member_group_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_member_group_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/vpc-channels/{vpc_channel_id}/member-groups",
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
        r"""创建VPC通道

        在服务集成中创建连接私有VPC资源的通道，并在创建API时将后端节点配置为使用这些VPC通道，以便服务集成直接访问私有VPC资源。
        &gt; 每个用户默认最多创建200个VPC通道，如需支持更多请联系技术支持调整配额。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateVpcChannelV2
        :type request: :class:`huaweicloudsdkroma.v2.CreateVpcChannelV2Request`
        :rtype: :class:`huaweicloudsdkroma.v2.CreateVpcChannelV2Response`
        """
        http_info = self._create_vpc_channel_v2_http_info(request)
        return self._call_api(**http_info)

    def create_vpc_channel_v2_async_invoker(self, request):
        http_info = self._create_vpc_channel_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_vpc_channel_v2_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/vpc-channels",
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
        r"""删除后端实例

        删除指定VPC通道中的后端实例
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteBackendInstanceV2
        :type request: :class:`huaweicloudsdkroma.v2.DeleteBackendInstanceV2Request`
        :rtype: :class:`huaweicloudsdkroma.v2.DeleteBackendInstanceV2Response`
        """
        http_info = self._delete_backend_instance_v2_http_info(request)
        return self._call_api(**http_info)

    def delete_backend_instance_v2_async_invoker(self, request):
        http_info = self._delete_backend_instance_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_backend_instance_v2_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/vpc-channels/{vpc_channel_id}/members/{member_id}",
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
        r"""删除VPC通道后端服务器组

        删除指定的VPC通道后端服务器组
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteMemberGroup
        :type request: :class:`huaweicloudsdkroma.v2.DeleteMemberGroupRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.DeleteMemberGroupResponse`
        """
        http_info = self._delete_member_group_http_info(request)
        return self._call_api(**http_info)

    def delete_member_group_async_invoker(self, request):
        http_info = self._delete_member_group_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_member_group_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/vpc-channels/{vpc_channel_id}/member-groups/{member_group_id}",
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
        r"""删除VPC通道

        删除指定的VPC通道
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteVpcChannelV2
        :type request: :class:`huaweicloudsdkroma.v2.DeleteVpcChannelV2Request`
        :rtype: :class:`huaweicloudsdkroma.v2.DeleteVpcChannelV2Response`
        """
        http_info = self._delete_vpc_channel_v2_http_info(request)
        return self._call_api(**http_info)

    def delete_vpc_channel_v2_async_invoker(self, request):
        http_info = self._delete_vpc_channel_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_vpc_channel_v2_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/vpc-channels/{vpc_channel_id}",
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
        r"""查看后端实例列表

        查看指定VPC通道的后端实例列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListBackendInstancesV2
        :type request: :class:`huaweicloudsdkroma.v2.ListBackendInstancesV2Request`
        :rtype: :class:`huaweicloudsdkroma.v2.ListBackendInstancesV2Response`
        """
        http_info = self._list_backend_instances_v2_http_info(request)
        return self._call_api(**http_info)

    def list_backend_instances_v2_async_invoker(self, request):
        http_info = self._list_backend_instances_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_backend_instances_v2_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/vpc-channels/{vpc_channel_id}/members",
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
        r"""查询VPC通道后端云服务组列表

        查询VPC通道后端云服务组列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListMemberGroups
        :type request: :class:`huaweicloudsdkroma.v2.ListMemberGroupsRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.ListMemberGroupsResponse`
        """
        http_info = self._list_member_groups_http_info(request)
        return self._call_api(**http_info)

    def list_member_groups_async_invoker(self, request):
        http_info = self._list_member_groups_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_member_groups_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/vpc-channels/{vpc_channel_id}/member-groups",
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
        r"""查询VPC通道列表

        查看VPC通道列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListVpcChannelsV2
        :type request: :class:`huaweicloudsdkroma.v2.ListVpcChannelsV2Request`
        :rtype: :class:`huaweicloudsdkroma.v2.ListVpcChannelsV2Response`
        """
        http_info = self._list_vpc_channels_v2_http_info(request)
        return self._call_api(**http_info)

    def list_vpc_channels_v2_async_invoker(self, request):
        http_info = self._list_vpc_channels_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_vpc_channels_v2_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/vpc-channels",
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
        r"""查看VPC通道后端服务器组详情

        查看指定的VPC通道后端服务器组详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowDetailsOfMemberGroup
        :type request: :class:`huaweicloudsdkroma.v2.ShowDetailsOfMemberGroupRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.ShowDetailsOfMemberGroupResponse`
        """
        http_info = self._show_details_of_member_group_http_info(request)
        return self._call_api(**http_info)

    def show_details_of_member_group_async_invoker(self, request):
        http_info = self._show_details_of_member_group_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_details_of_member_group_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/vpc-channels/{vpc_channel_id}/member-groups/{member_group_id}",
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
        r"""查看VPC通道详情

        查看指定的VPC通道详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowDetailsOfVpcChannelV2
        :type request: :class:`huaweicloudsdkroma.v2.ShowDetailsOfVpcChannelV2Request`
        :rtype: :class:`huaweicloudsdkroma.v2.ShowDetailsOfVpcChannelV2Response`
        """
        http_info = self._show_details_of_vpc_channel_v2_http_info(request)
        return self._call_api(**http_info)

    def show_details_of_vpc_channel_v2_async_invoker(self, request):
        http_info = self._show_details_of_vpc_channel_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_details_of_vpc_channel_v2_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/vpc-channels/{vpc_channel_id}",
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
        r"""修改后端实例

        更新指定的VPC通道的后端实例。更新时，使用传入的请求参数对对应云服务组的后端实例进行全量覆盖修改。若未指定修改的云服务器组，则进行全量覆盖。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateBackendInstancesV2
        :type request: :class:`huaweicloudsdkroma.v2.UpdateBackendInstancesV2Request`
        :rtype: :class:`huaweicloudsdkroma.v2.UpdateBackendInstancesV2Response`
        """
        http_info = self._update_backend_instances_v2_http_info(request)
        return self._call_api(**http_info)

    def update_backend_instances_v2_async_invoker(self, request):
        http_info = self._update_backend_instances_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_backend_instances_v2_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/vpc-channels/{vpc_channel_id}/members",
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
        r"""修改VPC通道健康检查

        修改VPC通道健康检查。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateHealthCheck
        :type request: :class:`huaweicloudsdkroma.v2.UpdateHealthCheckRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.UpdateHealthCheckResponse`
        """
        http_info = self._update_health_check_http_info(request)
        return self._call_api(**http_info)

    def update_health_check_async_invoker(self, request):
        http_info = self._update_health_check_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_health_check_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/vpc-channels/{vpc_channel_id}/health-config",
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
        r"""修改VPC通道后端服务器组

        更新指定VPC通道后端服务器组
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateMemberGroup
        :type request: :class:`huaweicloudsdkroma.v2.UpdateMemberGroupRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.UpdateMemberGroupResponse`
        """
        http_info = self._update_member_group_http_info(request)
        return self._call_api(**http_info)

    def update_member_group_async_invoker(self, request):
        http_info = self._update_member_group_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_member_group_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/vpc-channels/{vpc_channel_id}/member-groups/{member_group_id}",
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
        r"""修改VPC通道

        更新指定VPC通道的参数
        
        使用传入的后端服务器组列表对VPC通道进行全量覆盖，若后端服务器组列表为空，则会全量删除已有的服务器组；
        
        为保持兼容，传入的后端服务器列表为空时，不会删除已有的后端服务器，需要使用删除后端服务器接口进行删除；
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateVpcChannelV2
        :type request: :class:`huaweicloudsdkroma.v2.UpdateVpcChannelV2Request`
        :rtype: :class:`huaweicloudsdkroma.v2.UpdateVpcChannelV2Response`
        """
        http_info = self._update_vpc_channel_v2_http_info(request)
        return self._call_api(**http_info)

    def update_vpc_channel_v2_async_invoker(self, request):
        http_info = self._update_vpc_channel_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_vpc_channel_v2_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/apic/instances/{instance_id}/vpc-channels/{vpc_channel_id}",
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

    def create_project_vpc_channel_async(self, request):
        r"""项目下创建VPC通道

        创建相同的VPC通道关联到多个实例。同一个项目下VPC通道名称不可重复。注意：实例特性vpc_name_modifiable配置为off时才可使用。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateProjectVpcChannel
        :type request: :class:`huaweicloudsdkroma.v2.CreateProjectVpcChannelRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.CreateProjectVpcChannelResponse`
        """
        http_info = self._create_project_vpc_channel_http_info(request)
        return self._call_api(**http_info)

    def create_project_vpc_channel_async_invoker(self, request):
        http_info = self._create_project_vpc_channel_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_project_vpc_channel_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/apic/vpc-channels",
            "request_type": request.__class__.__name__,
            "response_type": "CreateProjectVpcChannelResponse"
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

    def create_project_vpc_channel_syncs_async(self, request):
        r"""项目下同步VPC通道

        同步VPC通道到多个实例。注意：实例特性vpc_name_modifiable配置为off时才可使用。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateProjectVpcChannelSyncs
        :type request: :class:`huaweicloudsdkroma.v2.CreateProjectVpcChannelSyncsRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.CreateProjectVpcChannelSyncsResponse`
        """
        http_info = self._create_project_vpc_channel_syncs_http_info(request)
        return self._call_api(**http_info)

    def create_project_vpc_channel_syncs_async_invoker(self, request):
        http_info = self._create_project_vpc_channel_syncs_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_project_vpc_channel_syncs_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/apic/vpc-channels/syncs",
            "request_type": request.__class__.__name__,
            "response_type": "CreateProjectVpcChannelSyncsResponse"
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

    def list_project_vpc_channels_v2_async(self, request):
        r"""查询项目下所有实例的VPC通道列表

        查询项目下所有实例的VPC通道列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListProjectVpcChannelsV2
        :type request: :class:`huaweicloudsdkroma.v2.ListProjectVpcChannelsV2Request`
        :rtype: :class:`huaweicloudsdkroma.v2.ListProjectVpcChannelsV2Response`
        """
        http_info = self._list_project_vpc_channels_v2_http_info(request)
        return self._call_api(**http_info)

    def list_project_vpc_channels_v2_async_invoker(self, request):
        http_info = self._list_project_vpc_channels_v2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_project_vpc_channels_v2_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/apic/vpc-channels",
            "request_type": request.__class__.__name__,
            "response_type": "ListProjectVpcChannelsV2Response"
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
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
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
        if 'members_return' in local_var_params:
            query_params.append(('members_return', local_var_params['members_return']))

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

    def update_project_vpc_channel_async(self, request):
        r"""项目下批量修改VPC通道

        项目下根据VPC通道名称批量修改多个多个实例下的VPC通道。若实例下不存在该VPC通道则创建。注意：实例特性vpc_name_modifiable配置为off时才可使用。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateProjectVpcChannel
        :type request: :class:`huaweicloudsdkroma.v2.UpdateProjectVpcChannelRequest`
        :rtype: :class:`huaweicloudsdkroma.v2.UpdateProjectVpcChannelResponse`
        """
        http_info = self._update_project_vpc_channel_http_info(request)
        return self._call_api(**http_info)

    def update_project_vpc_channel_async_invoker(self, request):
        http_info = self._update_project_vpc_channel_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_project_vpc_channel_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/apic/vpc-channels",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateProjectVpcChannelResponse"
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

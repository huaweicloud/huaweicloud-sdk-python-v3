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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkcbh'")


class CbhAsyncClient(Client):
    def __init__(self):
        super(CbhAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkcbh.v1.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "CbhAsyncClient":
                raise TypeError("client type error, support client type is CbhAsyncClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def change_instance_network_async(self, request):
        """修改实例网络

        修改云堡垒机实例网络。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ChangeInstanceNetwork
        :type request: :class:`huaweicloudsdkcbh.v1.ChangeInstanceNetworkRequest`
        :rtype: :class:`huaweicloudsdkcbh.v1.ChangeInstanceNetworkResponse`
        """
        http_info = self._change_instance_network_http_info(request)
        return self._call_api(**http_info)

    def change_instance_network_async_invoker(self, request):
        http_info = self._change_instance_network_http_info(request)
        return AsyncInvoker(self, http_info)

    def _change_instance_network_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/cbs/{server_id}/network/change",
            "request_type": request.__class__.__name__,
            "response_type": "ChangeInstanceNetworkResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'server_id' in local_var_params:
            path_params['server_id'] = local_var_params['server_id']

        query_params = []

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

    def change_instance_order_async(self, request):
        """创建变更云堡垒机实例订单

        创建变更云堡垒机实例订单。（调用此接口前先调用创建变更云堡垒机实例任务接口，当前接口未开放）
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ChangeInstanceOrder
        :type request: :class:`huaweicloudsdkcbh.v1.ChangeInstanceOrderRequest`
        :rtype: :class:`huaweicloudsdkcbh.v1.ChangeInstanceOrderResponse`
        """
        http_info = self._change_instance_order_http_info(request)
        return self._call_api(**http_info)

    def change_instance_order_async_invoker(self, request):
        http_info = self._change_instance_order_http_info(request)
        return AsyncInvoker(self, http_info)

    def _change_instance_order_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/cbs/{server_id}/alter/{instance_key}",
            "request_type": request.__class__.__name__,
            "response_type": "ChangeInstanceOrderResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'server_id' in local_var_params:
            path_params['server_id'] = local_var_params['server_id']
        if 'instance_key' in local_var_params:
            path_params['instance_key'] = local_var_params['instance_key']

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

    def create_cbh_async(self, request):
        """创建云堡垒机实例

        创建云堡垒机实例。（创建云堡垒机实例订单前，先调用此接口）
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateCbh
        :type request: :class:`huaweicloudsdkcbh.v1.CreateCbhRequest`
        :rtype: :class:`huaweicloudsdkcbh.v1.CreateCbhResponse`
        """
        http_info = self._create_cbh_http_info(request)
        return self._call_api(**http_info)

    def create_cbh_async_invoker(self, request):
        http_info = self._create_cbh_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_cbh_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/cbs/instance/create",
            "request_type": request.__class__.__name__,
            "response_type": "CreateCbhResponse"
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

    def create_instance_order_async(self, request):
        """创建云堡垒机实例订单

        创建云堡垒机实例订单。(调用此接口前先调用创建云堡垒机实例接口)
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateInstanceOrder
        :type request: :class:`huaweicloudsdkcbh.v1.CreateInstanceOrderRequest`
        :rtype: :class:`huaweicloudsdkcbh.v1.CreateInstanceOrderResponse`
        """
        http_info = self._create_instance_order_http_info(request)
        return self._call_api(**http_info)

    def create_instance_order_async_invoker(self, request):
        http_info = self._create_instance_order_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_instance_order_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/cbs/period/order",
            "request_type": request.__class__.__name__,
            "response_type": "CreateInstanceOrderResponse"
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

    def install_cbh_eip_async(self, request):
        """绑定弹性公网IP

        云堡垒机实例绑定弹性公网IP
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for InstallCbhEip
        :type request: :class:`huaweicloudsdkcbh.v1.InstallCbhEipRequest`
        :rtype: :class:`huaweicloudsdkcbh.v1.InstallCbhEipResponse`
        """
        http_info = self._install_cbh_eip_http_info(request)
        return self._call_api(**http_info)

    def install_cbh_eip_async_invoker(self, request):
        http_info = self._install_cbh_eip_http_info(request)
        return AsyncInvoker(self, http_info)

    def _install_cbh_eip_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/cbs/instance/{server_id}/eip/bind",
            "request_type": request.__class__.__name__,
            "response_type": "InstallCbhEipResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'server_id' in local_var_params:
            path_params['server_id'] = local_var_params['server_id']

        query_params = []

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

    def list_cbh_instance_async(self, request):
        """获取CBH实例列表

        获取当前租户下的云堡垒机实例列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListCbhInstance
        :type request: :class:`huaweicloudsdkcbh.v1.ListCbhInstanceRequest`
        :rtype: :class:`huaweicloudsdkcbh.v1.ListCbhInstanceResponse`
        """
        http_info = self._list_cbh_instance_http_info(request)
        return self._call_api(**http_info)

    def list_cbh_instance_async_invoker(self, request):
        http_info = self._list_cbh_instance_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_cbh_instance_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/cbs/instance/list",
            "request_type": request.__class__.__name__,
            "response_type": "ListCbhInstanceResponse"
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

    def list_quota_status_async(self, request):
        """获取弹性云服务器配额

        获取当前租户所选择的可用分区、性能规格所对应的弹性云服务器是否可用。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListQuotaStatus
        :type request: :class:`huaweicloudsdkcbh.v1.ListQuotaStatusRequest`
        :rtype: :class:`huaweicloudsdkcbh.v1.ListQuotaStatusResponse`
        """
        http_info = self._list_quota_status_http_info(request)
        return self._call_api(**http_info)

    def list_quota_status_async_invoker(self, request):
        http_info = self._list_quota_status_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_quota_status_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/cbs/instance/ecs-quota",
            "request_type": request.__class__.__name__,
            "response_type": "ListQuotaStatusResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'availability_zone' in local_var_params:
            query_params.append(('availability_zone', local_var_params['availability_zone']))
        if 'resource_spec_code' in local_var_params:
            query_params.append(('resource_spec_code', local_var_params['resource_spec_code']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def reset_login_method_async(self, request):
        """重置admin用户多因子认证方式

        重置admin用户多因子认证方式。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ResetLoginMethod
        :type request: :class:`huaweicloudsdkcbh.v1.ResetLoginMethodRequest`
        :rtype: :class:`huaweicloudsdkcbh.v1.ResetLoginMethodResponse`
        """
        http_info = self._reset_login_method_http_info(request)
        return self._call_api(**http_info)

    def reset_login_method_async_invoker(self, request):
        http_info = self._reset_login_method_http_info(request)
        return AsyncInvoker(self, http_info)

    def _reset_login_method_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/cbs/instance/{server_id}/login-method",
            "request_type": request.__class__.__name__,
            "response_type": "ResetLoginMethodResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'server_id' in local_var_params:
            path_params['server_id'] = local_var_params['server_id']

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

    def reset_password_async(self, request):
        """修改admin用户密码

        修改云堡垒机实例web登录admin用户密码。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ResetPassword
        :type request: :class:`huaweicloudsdkcbh.v1.ResetPasswordRequest`
        :rtype: :class:`huaweicloudsdkcbh.v1.ResetPasswordResponse`
        """
        http_info = self._reset_password_http_info(request)
        return self._call_api(**http_info)

    def reset_password_async_invoker(self, request):
        http_info = self._reset_password_http_info(request)
        return AsyncInvoker(self, http_info)

    def _reset_password_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/cbs/instance/password",
            "request_type": request.__class__.__name__,
            "response_type": "ResetPasswordResponse"
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

    def restart_cbh_instance_async(self, request):
        """重启云堡垒机实例

        重启云堡垒机实例。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RestartCbhInstance
        :type request: :class:`huaweicloudsdkcbh.v1.RestartCbhInstanceRequest`
        :rtype: :class:`huaweicloudsdkcbh.v1.RestartCbhInstanceResponse`
        """
        http_info = self._restart_cbh_instance_http_info(request)
        return self._call_api(**http_info)

    def restart_cbh_instance_async_invoker(self, request):
        http_info = self._restart_cbh_instance_http_info(request)
        return AsyncInvoker(self, http_info)

    def _restart_cbh_instance_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/cbs/instance/reboot",
            "request_type": request.__class__.__name__,
            "response_type": "RestartCbhInstanceResponse"
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

    def search_quota_async(self, request):
        """查询堡垒机配额

        查询云堡垒机配额信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for SearchQuota
        :type request: :class:`huaweicloudsdkcbh.v1.SearchQuotaRequest`
        :rtype: :class:`huaweicloudsdkcbh.v1.SearchQuotaResponse`
        """
        http_info = self._search_quota_http_info(request)
        return self._call_api(**http_info)

    def search_quota_async_invoker(self, request):
        http_info = self._search_quota_http_info(request)
        return AsyncInvoker(self, http_info)

    def _search_quota_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/cbs/instance/quota",
            "request_type": request.__class__.__name__,
            "response_type": "SearchQuotaResponse"
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

    def show_available_zone_info_async(self, request):
        """获取可用用分区信息

        获取云堡垒机服务可用分区信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowAvailableZoneInfo
        :type request: :class:`huaweicloudsdkcbh.v1.ShowAvailableZoneInfoRequest`
        :rtype: :class:`huaweicloudsdkcbh.v1.ShowAvailableZoneInfoResponse`
        """
        http_info = self._show_available_zone_info_http_info(request)
        return self._call_api(**http_info)

    def show_available_zone_info_async_invoker(self, request):
        http_info = self._show_available_zone_info_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_available_zone_info_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/cbs/available-zone",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAvailableZoneInfoResponse"
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

    def show_network_configuration_async(self, request):
        """检查云堡垒机网络

        检查云堡垒机实例网络信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowNetworkConfiguration
        :type request: :class:`huaweicloudsdkcbh.v1.ShowNetworkConfigurationRequest`
        :rtype: :class:`huaweicloudsdkcbh.v1.ShowNetworkConfigurationResponse`
        """
        http_info = self._show_network_configuration_http_info(request)
        return self._call_api(**http_info)

    def show_network_configuration_async_invoker(self, request):
        http_info = self._show_network_configuration_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_network_configuration_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/cbs/network/configuration",
            "request_type": request.__class__.__name__,
            "response_type": "ShowNetworkConfigurationResponse"
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

    def start_cbh_instance_async(self, request):
        """启动云堡垒机实例

        启动云堡垒机实例。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for StartCbhInstance
        :type request: :class:`huaweicloudsdkcbh.v1.StartCbhInstanceRequest`
        :rtype: :class:`huaweicloudsdkcbh.v1.StartCbhInstanceResponse`
        """
        http_info = self._start_cbh_instance_http_info(request)
        return self._call_api(**http_info)

    def start_cbh_instance_async_invoker(self, request):
        http_info = self._start_cbh_instance_http_info(request)
        return AsyncInvoker(self, http_info)

    def _start_cbh_instance_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/cbs/instance/start",
            "request_type": request.__class__.__name__,
            "response_type": "StartCbhInstanceResponse"
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

    def stop_cbh_instance_async(self, request):
        """关闭云堡垒机实例

        关闭云堡垒机实例。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for StopCbhInstance
        :type request: :class:`huaweicloudsdkcbh.v1.StopCbhInstanceRequest`
        :rtype: :class:`huaweicloudsdkcbh.v1.StopCbhInstanceResponse`
        """
        http_info = self._stop_cbh_instance_http_info(request)
        return self._call_api(**http_info)

    def stop_cbh_instance_async_invoker(self, request):
        http_info = self._stop_cbh_instance_http_info(request)
        return AsyncInvoker(self, http_info)

    def _stop_cbh_instance_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/cbs/instance/stop",
            "request_type": request.__class__.__name__,
            "response_type": "StopCbhInstanceResponse"
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

    def uninstall_cbh_eip_async(self, request):
        """解绑弹性公网IP

        云堡垒机实例解绑弹性公网IP。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UninstallCbhEip
        :type request: :class:`huaweicloudsdkcbh.v1.UninstallCbhEipRequest`
        :rtype: :class:`huaweicloudsdkcbh.v1.UninstallCbhEipResponse`
        """
        http_info = self._uninstall_cbh_eip_http_info(request)
        return self._call_api(**http_info)

    def uninstall_cbh_eip_async_invoker(self, request):
        http_info = self._uninstall_cbh_eip_http_info(request)
        return AsyncInvoker(self, http_info)

    def _uninstall_cbh_eip_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/cbs/instance/{server_id}/eip/unbind",
            "request_type": request.__class__.__name__,
            "response_type": "UninstallCbhEipResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'server_id' in local_var_params:
            path_params['server_id'] = local_var_params['server_id']

        query_params = []

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

    def upgrade_cbh_instance_async(self, request):
        """升级云堡垒机实例

        升级云堡垒机实例
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpgradeCbhInstance
        :type request: :class:`huaweicloudsdkcbh.v1.UpgradeCbhInstanceRequest`
        :rtype: :class:`huaweicloudsdkcbh.v1.UpgradeCbhInstanceResponse`
        """
        http_info = self._upgrade_cbh_instance_http_info(request)
        return self._call_api(**http_info)

    def upgrade_cbh_instance_async_invoker(self, request):
        http_info = self._upgrade_cbh_instance_http_info(request)
        return AsyncInvoker(self, http_info)

    def _upgrade_cbh_instance_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/cbs/instance/upgrade",
            "request_type": request.__class__.__name__,
            "response_type": "UpgradeCbhInstanceResponse"
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

    def login_cbh_async(self, request):
        """获取IAM登录实例链接

        获取当前IAM用户登录堡垒机的免登录链接
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for LoginCbh
        :type request: :class:`huaweicloudsdkcbh.v1.LoginCbhRequest`
        :rtype: :class:`huaweicloudsdkcbh.v1.LoginCbhResponse`
        """
        http_info = self._login_cbh_http_info(request)
        return self._call_api(**http_info)

    def login_cbh_async_invoker(self, request):
        http_info = self._login_cbh_http_info(request)
        return AsyncInvoker(self, http_info)

    def _login_cbh_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/cbs/instance/login",
            "request_type": request.__class__.__name__,
            "response_type": "LoginCbhResponse"
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

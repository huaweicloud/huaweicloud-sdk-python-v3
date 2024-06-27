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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkcfw'")


class CfwClient(Client):
    def __init__(self):
        super(CfwClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkcfw.v1.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "CfwClient":
                raise TypeError("client type error, support client type is CfwClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def add_address_item(self, request):
        """添加地址组成员

        添加地址组成员
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AddAddressItem
        :type request: :class:`huaweicloudsdkcfw.v1.AddAddressItemRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.AddAddressItemResponse`
        """
        http_info = self._add_address_item_http_info(request)
        return self._call_api(**http_info)

    def add_address_item_invoker(self, request):
        http_info = self._add_address_item_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _add_address_item_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/address-items",
            "request_type": request.__class__.__name__,
            "response_type": "AddAddressItemResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'fw_instance_id' in local_var_params:
            query_params.append(('fw_instance_id', local_var_params['fw_instance_id']))

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

    def add_address_set(self, request):
        """添加地址组

        添加地址组
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AddAddressSet
        :type request: :class:`huaweicloudsdkcfw.v1.AddAddressSetRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.AddAddressSetResponse`
        """
        http_info = self._add_address_set_http_info(request)
        return self._call_api(**http_info)

    def add_address_set_invoker(self, request):
        http_info = self._add_address_set_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _add_address_set_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/address-set",
            "request_type": request.__class__.__name__,
            "response_type": "AddAddressSetResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'fw_instance_id' in local_var_params:
            query_params.append(('fw_instance_id', local_var_params['fw_instance_id']))

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

    def add_black_white_list(self, request):
        """创建黑白名单规则

        创建黑白名单规则
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AddBlackWhiteList
        :type request: :class:`huaweicloudsdkcfw.v1.AddBlackWhiteListRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.AddBlackWhiteListResponse`
        """
        http_info = self._add_black_white_list_http_info(request)
        return self._call_api(**http_info)

    def add_black_white_list_invoker(self, request):
        http_info = self._add_black_white_list_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _add_black_white_list_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/black-white-list",
            "request_type": request.__class__.__name__,
            "response_type": "AddBlackWhiteListResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'fw_instance_id' in local_var_params:
            query_params.append(('fw_instance_id', local_var_params['fw_instance_id']))

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

    def add_domain_set(self, request):
        """添加域名组

        添加域名组
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AddDomainSet
        :type request: :class:`huaweicloudsdkcfw.v1.AddDomainSetRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.AddDomainSetResponse`
        """
        http_info = self._add_domain_set_http_info(request)
        return self._call_api(**http_info)

    def add_domain_set_invoker(self, request):
        http_info = self._add_domain_set_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _add_domain_set_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/domain-set",
            "request_type": request.__class__.__name__,
            "response_type": "AddDomainSetResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'fw_instance_id' in local_var_params:
            query_params.append(('fw_instance_id', local_var_params['fw_instance_id']))

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

    def add_domains(self, request):
        """添加域名列表

        添加域名列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AddDomains
        :type request: :class:`huaweicloudsdkcfw.v1.AddDomainsRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.AddDomainsResponse`
        """
        http_info = self._add_domains_http_info(request)
        return self._call_api(**http_info)

    def add_domains_invoker(self, request):
        http_info = self._add_domains_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _add_domains_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/domain-set/domains/{set_id}",
            "request_type": request.__class__.__name__,
            "response_type": "AddDomainsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'set_id' in local_var_params:
            path_params['set_id'] = local_var_params['set_id']

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'fw_instance_id' in local_var_params:
            query_params.append(('fw_instance_id', local_var_params['fw_instance_id']))

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

    def add_log_config(self, request):
        """创建日志配置

        创建日志配置
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AddLogConfig
        :type request: :class:`huaweicloudsdkcfw.v1.AddLogConfigRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.AddLogConfigResponse`
        """
        http_info = self._add_log_config_http_info(request)
        return self._call_api(**http_info)

    def add_log_config_invoker(self, request):
        http_info = self._add_log_config_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _add_log_config_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/cfw/logs/configuration",
            "request_type": request.__class__.__name__,
            "response_type": "AddLogConfigResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'fw_instance_id' in local_var_params:
            query_params.append(('fw_instance_id', local_var_params['fw_instance_id']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

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

    def add_service_items(self, request):
        """新建服务成员

        批量添加服务组成员
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AddServiceItems
        :type request: :class:`huaweicloudsdkcfw.v1.AddServiceItemsRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.AddServiceItemsResponse`
        """
        http_info = self._add_service_items_http_info(request)
        return self._call_api(**http_info)

    def add_service_items_invoker(self, request):
        http_info = self._add_service_items_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _add_service_items_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/service-items",
            "request_type": request.__class__.__name__,
            "response_type": "AddServiceItemsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'fw_instance_id' in local_var_params:
            query_params.append(('fw_instance_id', local_var_params['fw_instance_id']))

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

    def add_service_set(self, request):
        """新建服务组

        创建服务组
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AddServiceSet
        :type request: :class:`huaweicloudsdkcfw.v1.AddServiceSetRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.AddServiceSetResponse`
        """
        http_info = self._add_service_set_http_info(request)
        return self._call_api(**http_info)

    def add_service_set_invoker(self, request):
        http_info = self._add_service_set_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _add_service_set_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/service-set",
            "request_type": request.__class__.__name__,
            "response_type": "AddServiceSetResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'fw_instance_id' in local_var_params:
            query_params.append(('fw_instance_id', local_var_params['fw_instance_id']))

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

    def batch_delete_address_items(self, request):
        """批量删除地址组成员

        批量删除地址组成员
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchDeleteAddressItems
        :type request: :class:`huaweicloudsdkcfw.v1.BatchDeleteAddressItemsRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.BatchDeleteAddressItemsResponse`
        """
        http_info = self._batch_delete_address_items_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_address_items_invoker(self, request):
        http_info = self._batch_delete_address_items_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_delete_address_items_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/address-items",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeleteAddressItemsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'fw_instance_id' in local_var_params:
            query_params.append(('fw_instance_id', local_var_params['fw_instance_id']))

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

    def batch_delete_service_items(self, request):
        """批量删除服务组成员信息

        批量删除服务组成员信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchDeleteServiceItems
        :type request: :class:`huaweicloudsdkcfw.v1.BatchDeleteServiceItemsRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.BatchDeleteServiceItemsResponse`
        """
        http_info = self._batch_delete_service_items_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_service_items_invoker(self, request):
        http_info = self._batch_delete_service_items_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_delete_service_items_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/service-items",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeleteServiceItemsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'fw_instance_id' in local_var_params:
            query_params.append(('fw_instance_id', local_var_params['fw_instance_id']))

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

    def cancel_capture_task(self, request):
        """取消抓包任务

        取消抓包任务
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CancelCaptureTask
        :type request: :class:`huaweicloudsdkcfw.v1.CancelCaptureTaskRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.CancelCaptureTaskResponse`
        """
        http_info = self._cancel_capture_task_http_info(request)
        return self._call_api(**http_info)

    def cancel_capture_task_invoker(self, request):
        http_info = self._cancel_capture_task_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _cancel_capture_task_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/capture-task/stop",
            "request_type": request.__class__.__name__,
            "response_type": "CancelCaptureTaskResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'fw_instance_id' in local_var_params:
            query_params.append(('fw_instance_id', local_var_params['fw_instance_id']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

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

    def change_east_west_firewall_status(self, request):
        """修改东西向防火墙防护状态

        东西向防护资源防护开启/关闭
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ChangeEastWestFirewallStatus
        :type request: :class:`huaweicloudsdkcfw.v1.ChangeEastWestFirewallStatusRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.ChangeEastWestFirewallStatusResponse`
        """
        http_info = self._change_east_west_firewall_status_http_info(request)
        return self._call_api(**http_info)

    def change_east_west_firewall_status_invoker(self, request):
        http_info = self._change_east_west_firewall_status_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _change_east_west_firewall_status_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/firewall/east-west/protect",
            "request_type": request.__class__.__name__,
            "response_type": "ChangeEastWestFirewallStatusResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'fw_instance_id' in local_var_params:
            query_params.append(('fw_instance_id', local_var_params['fw_instance_id']))

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

    def create_capture_task(self, request):
        """创建抓包任务

        创建抓包任务
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateCaptureTask
        :type request: :class:`huaweicloudsdkcfw.v1.CreateCaptureTaskRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.CreateCaptureTaskResponse`
        """
        http_info = self._create_capture_task_http_info(request)
        return self._call_api(**http_info)

    def create_capture_task_invoker(self, request):
        http_info = self._create_capture_task_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_capture_task_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/capture-task",
            "request_type": request.__class__.__name__,
            "response_type": "CreateCaptureTaskResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'fw_instance_id' in local_var_params:
            query_params.append(('fw_instance_id', local_var_params['fw_instance_id']))

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

    def create_east_west_firewall(self, request):
        """创建东西向防火墙

        创建东西向防火墙
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateEastWestFirewall
        :type request: :class:`huaweicloudsdkcfw.v1.CreateEastWestFirewallRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.CreateEastWestFirewallResponse`
        """
        http_info = self._create_east_west_firewall_http_info(request)
        return self._call_api(**http_info)

    def create_east_west_firewall_invoker(self, request):
        http_info = self._create_east_west_firewall_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_east_west_firewall_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/firewall/east-west",
            "request_type": request.__class__.__name__,
            "response_type": "CreateEastWestFirewallResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'fw_instance_id' in local_var_params:
            query_params.append(('fw_instance_id', local_var_params['fw_instance_id']))

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

    def create_firewall(self, request):
        """创建防火墙

        创建防火墙
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateFirewall
        :type request: :class:`huaweicloudsdkcfw.v1.CreateFirewallRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.CreateFirewallResponse`
        """
        http_info = self._create_firewall_http_info(request)
        return self._call_api(**http_info)

    def create_firewall_invoker(self, request):
        http_info = self._create_firewall_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_firewall_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/firewall",
            "request_type": request.__class__.__name__,
            "response_type": "CreateFirewallResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_client_token' in local_var_params:
            header_params['X-Client-Token'] = local_var_params['x_client_token']

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

    def create_tag(self, request):
        """标签创建接口

        创建标签
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateTag
        :type request: :class:`huaweicloudsdkcfw.v1.CreateTagRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.CreateTagResponse`
        """
        http_info = self._create_tag_http_info(request)
        return self._call_api(**http_info)

    def create_tag_invoker(self, request):
        http_info = self._create_tag_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_tag_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/cfw-cfw/{fw_instance_id}/tags/create",
            "request_type": request.__class__.__name__,
            "response_type": "CreateTagResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'fw_instance_id' in local_var_params:
            path_params['fw_instance_id'] = local_var_params['fw_instance_id']

        query_params = []

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

    def delete_address_item(self, request):
        """删除地址组成员

        删除地址组成员
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteAddressItem
        :type request: :class:`huaweicloudsdkcfw.v1.DeleteAddressItemRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.DeleteAddressItemResponse`
        """
        http_info = self._delete_address_item_http_info(request)
        return self._call_api(**http_info)

    def delete_address_item_invoker(self, request):
        http_info = self._delete_address_item_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_address_item_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/address-items/{item_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteAddressItemResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'item_id' in local_var_params:
            path_params['item_id'] = local_var_params['item_id']

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'fw_instance_id' in local_var_params:
            query_params.append(('fw_instance_id', local_var_params['fw_instance_id']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_address_set(self, request):
        """删除地址组

        删除地址组
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteAddressSet
        :type request: :class:`huaweicloudsdkcfw.v1.DeleteAddressSetRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.DeleteAddressSetResponse`
        """
        http_info = self._delete_address_set_http_info(request)
        return self._call_api(**http_info)

    def delete_address_set_invoker(self, request):
        http_info = self._delete_address_set_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_address_set_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/address-sets/{set_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteAddressSetResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'set_id' in local_var_params:
            path_params['set_id'] = local_var_params['set_id']

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'fw_instance_id' in local_var_params:
            query_params.append(('fw_instance_id', local_var_params['fw_instance_id']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_black_white_list(self, request):
        """删除黑白名单规则

        删除黑白名单规则
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteBlackWhiteList
        :type request: :class:`huaweicloudsdkcfw.v1.DeleteBlackWhiteListRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.DeleteBlackWhiteListResponse`
        """
        http_info = self._delete_black_white_list_http_info(request)
        return self._call_api(**http_info)

    def delete_black_white_list_invoker(self, request):
        http_info = self._delete_black_white_list_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_black_white_list_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/black-white-list/{list_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteBlackWhiteListResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'list_id' in local_var_params:
            path_params['list_id'] = local_var_params['list_id']

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'fw_instance_id' in local_var_params:
            query_params.append(('fw_instance_id', local_var_params['fw_instance_id']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_capture_task(self, request):
        """删除抓包任务

        删除抓包任务
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteCaptureTask
        :type request: :class:`huaweicloudsdkcfw.v1.DeleteCaptureTaskRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.DeleteCaptureTaskResponse`
        """
        http_info = self._delete_capture_task_http_info(request)
        return self._call_api(**http_info)

    def delete_capture_task_invoker(self, request):
        http_info = self._delete_capture_task_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_capture_task_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/capture-task/batch-delete",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteCaptureTaskResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'fw_instance_id' in local_var_params:
            query_params.append(('fw_instance_id', local_var_params['fw_instance_id']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

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

    def delete_domain_set(self, request):
        """删除域名组

        删除域名组
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteDomainSet
        :type request: :class:`huaweicloudsdkcfw.v1.DeleteDomainSetRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.DeleteDomainSetResponse`
        """
        http_info = self._delete_domain_set_http_info(request)
        return self._call_api(**http_info)

    def delete_domain_set_invoker(self, request):
        http_info = self._delete_domain_set_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_domain_set_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/domain-set/{set_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteDomainSetResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'set_id' in local_var_params:
            path_params['set_id'] = local_var_params['set_id']

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'fw_instance_id' in local_var_params:
            query_params.append(('fw_instance_id', local_var_params['fw_instance_id']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_domains(self, request):
        """删除域名列表

        删除域名列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteDomains
        :type request: :class:`huaweicloudsdkcfw.v1.DeleteDomainsRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.DeleteDomainsResponse`
        """
        http_info = self._delete_domains_http_info(request)
        return self._call_api(**http_info)

    def delete_domains_invoker(self, request):
        http_info = self._delete_domains_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_domains_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/domain-set/domains/{set_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteDomainsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'set_id' in local_var_params:
            path_params['set_id'] = local_var_params['set_id']

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

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

    def delete_firewall(self, request):
        """删除防火墙

        删除防火墙，仅按需生效
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteFirewall
        :type request: :class:`huaweicloudsdkcfw.v1.DeleteFirewallRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.DeleteFirewallResponse`
        """
        http_info = self._delete_firewall_http_info(request)
        return self._call_api(**http_info)

    def delete_firewall_invoker(self, request):
        http_info = self._delete_firewall_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_firewall_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/firewall/{resource_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteFirewallResponse"
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

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_service_item(self, request):
        """删除服务成员

        删除服务组成员
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteServiceItem
        :type request: :class:`huaweicloudsdkcfw.v1.DeleteServiceItemRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.DeleteServiceItemResponse`
        """
        http_info = self._delete_service_item_http_info(request)
        return self._call_api(**http_info)

    def delete_service_item_invoker(self, request):
        http_info = self._delete_service_item_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_service_item_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/service-items/{item_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteServiceItemResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'item_id' in local_var_params:
            path_params['item_id'] = local_var_params['item_id']

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'fw_instance_id' in local_var_params:
            query_params.append(('fw_instance_id', local_var_params['fw_instance_id']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_service_set(self, request):
        """删除服务组

        删除服务组
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteServiceSet
        :type request: :class:`huaweicloudsdkcfw.v1.DeleteServiceSetRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.DeleteServiceSetResponse`
        """
        http_info = self._delete_service_set_http_info(request)
        return self._call_api(**http_info)

    def delete_service_set_invoker(self, request):
        http_info = self._delete_service_set_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_service_set_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/service-sets/{set_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteServiceSetResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'set_id' in local_var_params:
            path_params['set_id'] = local_var_params['set_id']

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'fw_instance_id' in local_var_params:
            query_params.append(('fw_instance_id', local_var_params['fw_instance_id']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_tag(self, request):
        """删除标签

        删除标签
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteTag
        :type request: :class:`huaweicloudsdkcfw.v1.DeleteTagRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.DeleteTagResponse`
        """
        http_info = self._delete_tag_http_info(request)
        return self._call_api(**http_info)

    def delete_tag_invoker(self, request):
        http_info = self._delete_tag_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_tag_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/cfw-cfw/{fw_instance_id}/tags/delete",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteTagResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'fw_instance_id' in local_var_params:
            path_params['fw_instance_id'] = local_var_params['fw_instance_id']

        query_params = []

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

    def list_access_control_logs(self, request):
        """查询访问控制日志

        查询访问控制日志
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAccessControlLogs
        :type request: :class:`huaweicloudsdkcfw.v1.ListAccessControlLogsRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.ListAccessControlLogsResponse`
        """
        http_info = self._list_access_control_logs_http_info(request)
        return self._call_api(**http_info)

    def list_access_control_logs_invoker(self, request):
        http_info = self._list_access_control_logs_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_access_control_logs_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/cfw/logs/access-control",
            "request_type": request.__class__.__name__,
            "response_type": "ListAccessControlLogsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'fw_instance_id' in local_var_params:
            query_params.append(('fw_instance_id', local_var_params['fw_instance_id']))
        if 'rule_id' in local_var_params:
            query_params.append(('rule_id', local_var_params['rule_id']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'src_ip' in local_var_params:
            query_params.append(('src_ip', local_var_params['src_ip']))
        if 'src_port' in local_var_params:
            query_params.append(('src_port', local_var_params['src_port']))
        if 'dst_ip' in local_var_params:
            query_params.append(('dst_ip', local_var_params['dst_ip']))
        if 'dst_port' in local_var_params:
            query_params.append(('dst_port', local_var_params['dst_port']))
        if 'protocol' in local_var_params:
            query_params.append(('protocol', local_var_params['protocol']))
        if 'app' in local_var_params:
            query_params.append(('app', local_var_params['app']))
        if 'log_id' in local_var_params:
            query_params.append(('log_id', local_var_params['log_id']))
        if 'next_date' in local_var_params:
            query_params.append(('next_date', local_var_params['next_date']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'log_type' in local_var_params:
            query_params.append(('log_type', local_var_params['log_type']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'dst_host' in local_var_params:
            query_params.append(('dst_host', local_var_params['dst_host']))
        if 'rule_name' in local_var_params:
            query_params.append(('rule_name', local_var_params['rule_name']))
        if 'action' in local_var_params:
            query_params.append(('action', local_var_params['action']))
        if 'src_region_name' in local_var_params:
            query_params.append(('src_region_name', local_var_params['src_region_name']))
        if 'dst_region_name' in local_var_params:
            query_params.append(('dst_region_name', local_var_params['dst_region_name']))
        if 'src_province_name' in local_var_params:
            query_params.append(('src_province_name', local_var_params['src_province_name']))
        if 'dst_province_name' in local_var_params:
            query_params.append(('dst_province_name', local_var_params['dst_province_name']))
        if 'src_city_name' in local_var_params:
            query_params.append(('src_city_name', local_var_params['src_city_name']))
        if 'dst_city_name' in local_var_params:
            query_params.append(('dst_city_name', local_var_params['dst_city_name']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_address_items(self, request):
        """查询地址组成员

        查询地址组成员
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAddressItems
        :type request: :class:`huaweicloudsdkcfw.v1.ListAddressItemsRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.ListAddressItemsResponse`
        """
        http_info = self._list_address_items_http_info(request)
        return self._call_api(**http_info)

    def list_address_items_invoker(self, request):
        http_info = self._list_address_items_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_address_items_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/address-items",
            "request_type": request.__class__.__name__,
            "response_type": "ListAddressItemsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'set_id' in local_var_params:
            query_params.append(('set_id', local_var_params['set_id']))
        if 'key_word' in local_var_params:
            query_params.append(('key_word', local_var_params['key_word']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'address' in local_var_params:
            query_params.append(('address', local_var_params['address']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'fw_instance_id' in local_var_params:
            query_params.append(('fw_instance_id', local_var_params['fw_instance_id']))
        if 'query_address_set_type' in local_var_params:
            query_params.append(('query_address_set_type', local_var_params['query_address_set_type']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_address_set_detail(self, request):
        """查询地址组详细信息

        查询地址组详细
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAddressSetDetail
        :type request: :class:`huaweicloudsdkcfw.v1.ListAddressSetDetailRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.ListAddressSetDetailResponse`
        """
        http_info = self._list_address_set_detail_http_info(request)
        return self._call_api(**http_info)

    def list_address_set_detail_invoker(self, request):
        http_info = self._list_address_set_detail_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_address_set_detail_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/address-sets/{set_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ListAddressSetDetailResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'set_id' in local_var_params:
            path_params['set_id'] = local_var_params['set_id']

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'fw_instance_id' in local_var_params:
            query_params.append(('fw_instance_id', local_var_params['fw_instance_id']))
        if 'query_address_set_type' in local_var_params:
            query_params.append(('query_address_set_type', local_var_params['query_address_set_type']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_address_sets(self, request):
        """查询地址组列表

        查询地址组列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAddressSets
        :type request: :class:`huaweicloudsdkcfw.v1.ListAddressSetsRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.ListAddressSetsResponse`
        """
        http_info = self._list_address_sets_http_info(request)
        return self._call_api(**http_info)

    def list_address_sets_invoker(self, request):
        http_info = self._list_address_sets_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_address_sets_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/address-sets",
            "request_type": request.__class__.__name__,
            "response_type": "ListAddressSetsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'object_id' in local_var_params:
            query_params.append(('object_id', local_var_params['object_id']))
        if 'key_word' in local_var_params:
            query_params.append(('key_word', local_var_params['key_word']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'address' in local_var_params:
            query_params.append(('address', local_var_params['address']))
        if 'address_type' in local_var_params:
            query_params.append(('address_type', local_var_params['address_type']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'fw_instance_id' in local_var_params:
            query_params.append(('fw_instance_id', local_var_params['fw_instance_id']))
        if 'query_address_set_type' in local_var_params:
            query_params.append(('query_address_set_type', local_var_params['query_address_set_type']))
        if 'address_set_type' in local_var_params:
            query_params.append(('address_set_type', local_var_params['address_set_type']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_attack_logs(self, request):
        """查询攻击日志

        查询攻击日志
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAttackLogs
        :type request: :class:`huaweicloudsdkcfw.v1.ListAttackLogsRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.ListAttackLogsResponse`
        """
        http_info = self._list_attack_logs_http_info(request)
        return self._call_api(**http_info)

    def list_attack_logs_invoker(self, request):
        http_info = self._list_attack_logs_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_attack_logs_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/cfw/logs/attack",
            "request_type": request.__class__.__name__,
            "response_type": "ListAttackLogsResponse"
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
        if 'src_ip' in local_var_params:
            query_params.append(('src_ip', local_var_params['src_ip']))
        if 'src_port' in local_var_params:
            query_params.append(('src_port', local_var_params['src_port']))
        if 'dst_ip' in local_var_params:
            query_params.append(('dst_ip', local_var_params['dst_ip']))
        if 'dst_port' in local_var_params:
            query_params.append(('dst_port', local_var_params['dst_port']))
        if 'protocol' in local_var_params:
            query_params.append(('protocol', local_var_params['protocol']))
        if 'app' in local_var_params:
            query_params.append(('app', local_var_params['app']))
        if 'log_id' in local_var_params:
            query_params.append(('log_id', local_var_params['log_id']))
        if 'next_date' in local_var_params:
            query_params.append(('next_date', local_var_params['next_date']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'fw_instance_id' in local_var_params:
            query_params.append(('fw_instance_id', local_var_params['fw_instance_id']))
        if 'action' in local_var_params:
            query_params.append(('action', local_var_params['action']))
        if 'direction' in local_var_params:
            query_params.append(('direction', local_var_params['direction']))
        if 'attack_type' in local_var_params:
            query_params.append(('attack_type', local_var_params['attack_type']))
        if 'attack_rule' in local_var_params:
            query_params.append(('attack_rule', local_var_params['attack_rule']))
        if 'level' in local_var_params:
            query_params.append(('level', local_var_params['level']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'dst_host' in local_var_params:
            query_params.append(('dst_host', local_var_params['dst_host']))
        if 'log_type' in local_var_params:
            query_params.append(('log_type', local_var_params['log_type']))
        if 'attack_rule_id' in local_var_params:
            query_params.append(('attack_rule_id', local_var_params['attack_rule_id']))
        if 'src_region_name' in local_var_params:
            query_params.append(('src_region_name', local_var_params['src_region_name']))
        if 'dst_region_name' in local_var_params:
            query_params.append(('dst_region_name', local_var_params['dst_region_name']))
        if 'src_province_name' in local_var_params:
            query_params.append(('src_province_name', local_var_params['src_province_name']))
        if 'dst_province_name' in local_var_params:
            query_params.append(('dst_province_name', local_var_params['dst_province_name']))
        if 'src_city_name' in local_var_params:
            query_params.append(('src_city_name', local_var_params['src_city_name']))
        if 'dst_city_name' in local_var_params:
            query_params.append(('dst_city_name', local_var_params['dst_city_name']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_black_white_lists(self, request):
        """查询黑白名单列表

        查询黑白名单列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListBlackWhiteLists
        :type request: :class:`huaweicloudsdkcfw.v1.ListBlackWhiteListsRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.ListBlackWhiteListsResponse`
        """
        http_info = self._list_black_white_lists_http_info(request)
        return self._call_api(**http_info)

    def list_black_white_lists_invoker(self, request):
        http_info = self._list_black_white_lists_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_black_white_lists_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/black-white-lists",
            "request_type": request.__class__.__name__,
            "response_type": "ListBlackWhiteListsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'object_id' in local_var_params:
            query_params.append(('object_id', local_var_params['object_id']))
        if 'list_type' in local_var_params:
            query_params.append(('list_type', local_var_params['list_type']))
        if 'address_type' in local_var_params:
            query_params.append(('address_type', local_var_params['address_type']))
        if 'address' in local_var_params:
            query_params.append(('address', local_var_params['address']))
        if 'port' in local_var_params:
            query_params.append(('port', local_var_params['port']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'fw_instance_id' in local_var_params:
            query_params.append(('fw_instance_id', local_var_params['fw_instance_id']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_capture_result(self, request):
        """获取抓包任务结果

        获取抓包任务结果
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListCaptureResult
        :type request: :class:`huaweicloudsdkcfw.v1.ListCaptureResultRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.ListCaptureResultResponse`
        """
        http_info = self._list_capture_result_http_info(request)
        return self._call_api(**http_info)

    def list_capture_result_invoker(self, request):
        http_info = self._list_capture_result_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_capture_result_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/capture-task/capture-result",
            "request_type": request.__class__.__name__,
            "response_type": "ListCaptureResultResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'fw_instance_id' in local_var_params:
            query_params.append(('fw_instance_id', local_var_params['fw_instance_id']))
        if 'task_id' in local_var_params:
            query_params.append(('task_id', local_var_params['task_id']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'ip' in local_var_params:
            query_params.append(('ip', local_var_params['ip']))
            collection_formats['ip'] = 'csv'
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_capture_task(self, request):
        """查询抓包任务

        查询抓包任务
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListCaptureTask
        :type request: :class:`huaweicloudsdkcfw.v1.ListCaptureTaskRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.ListCaptureTaskResponse`
        """
        http_info = self._list_capture_task_http_info(request)
        return self._call_api(**http_info)

    def list_capture_task_invoker(self, request):
        http_info = self._list_capture_task_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_capture_task_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/capture-task",
            "request_type": request.__class__.__name__,
            "response_type": "ListCaptureTaskResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'fw_instance_id' in local_var_params:
            query_params.append(('fw_instance_id', local_var_params['fw_instance_id']))
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

    def list_dns_servers(self, request):
        """查询dns服务器列表

        查询dns服务器列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListDnsServers
        :type request: :class:`huaweicloudsdkcfw.v1.ListDnsServersRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.ListDnsServersResponse`
        """
        http_info = self._list_dns_servers_http_info(request)
        return self._call_api(**http_info)

    def list_dns_servers_invoker(self, request):
        http_info = self._list_dns_servers_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_dns_servers_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/dns/servers",
            "request_type": request.__class__.__name__,
            "response_type": "ListDnsServersResponse"
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
        if 'fw_instance_id' in local_var_params:
            query_params.append(('fw_instance_id', local_var_params['fw_instance_id']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_domain_parse_detail(self, request):
        """查询域名解析ip地址

        测试域名有效性
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListDomainParseDetail
        :type request: :class:`huaweicloudsdkcfw.v1.ListDomainParseDetailRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.ListDomainParseDetailResponse`
        """
        http_info = self._list_domain_parse_detail_http_info(request)
        return self._call_api(**http_info)

    def list_domain_parse_detail_invoker(self, request):
        http_info = self._list_domain_parse_detail_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_domain_parse_detail_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/domain/parse/{domain_name}",
            "request_type": request.__class__.__name__,
            "response_type": "ListDomainParseDetailResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_name' in local_var_params:
            path_params['domain_name'] = local_var_params['domain_name']

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'fw_instance_id' in local_var_params:
            query_params.append(('fw_instance_id', local_var_params['fw_instance_id']))
        if 'address_type' in local_var_params:
            query_params.append(('address_type', local_var_params['address_type']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_domain_sets(self, request):
        """查询域名组列表

        查询域名组列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListDomainSets
        :type request: :class:`huaweicloudsdkcfw.v1.ListDomainSetsRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.ListDomainSetsResponse`
        """
        http_info = self._list_domain_sets_http_info(request)
        return self._call_api(**http_info)

    def list_domain_sets_invoker(self, request):
        http_info = self._list_domain_sets_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_domain_sets_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/domain-sets",
            "request_type": request.__class__.__name__,
            "response_type": "ListDomainSetsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'fw_instance_id' in local_var_params:
            query_params.append(('fw_instance_id', local_var_params['fw_instance_id']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'object_id' in local_var_params:
            query_params.append(('object_id', local_var_params['object_id']))
        if 'key_word' in local_var_params:
            query_params.append(('key_word', local_var_params['key_word']))
        if 'domain_set_type' in local_var_params:
            query_params.append(('domain_set_type', local_var_params['domain_set_type']))
        if 'config_status' in local_var_params:
            query_params.append(('config_status', local_var_params['config_status']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_domains(self, request):
        """获取域名组下域名列表

        获取域名组下域名列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListDomains
        :type request: :class:`huaweicloudsdkcfw.v1.ListDomainsRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.ListDomainsResponse`
        """
        http_info = self._list_domains_http_info(request)
        return self._call_api(**http_info)

    def list_domains_invoker(self, request):
        http_info = self._list_domains_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_domains_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/domain-set/domains/{domain_set_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ListDomainsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_set_id' in local_var_params:
            path_params['domain_set_id'] = local_var_params['domain_set_id']

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'fw_instance_id' in local_var_params:
            query_params.append(('fw_instance_id', local_var_params['fw_instance_id']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'domain_name' in local_var_params:
            query_params.append(('domain_name', local_var_params['domain_name']))
        if 'object_id' in local_var_params:
            query_params.append(('object_Id', local_var_params['object_id']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_east_west_firewall(self, request):
        """获取东西向防火墙信息

        获取东西向防火墙信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListEastWestFirewall
        :type request: :class:`huaweicloudsdkcfw.v1.ListEastWestFirewallRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.ListEastWestFirewallResponse`
        """
        http_info = self._list_east_west_firewall_http_info(request)
        return self._call_api(**http_info)

    def list_east_west_firewall_invoker(self, request):
        http_info = self._list_east_west_firewall_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_east_west_firewall_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/firewall/east-west",
            "request_type": request.__class__.__name__,
            "response_type": "ListEastWestFirewallResponse"
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
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'fw_instance_id' in local_var_params:
            query_params.append(('fw_instance_id', local_var_params['fw_instance_id']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_firewall_detail(self, request):
        """查询防火墙详细信息

        查询防火墙实例
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListFirewallDetail
        :type request: :class:`huaweicloudsdkcfw.v1.ListFirewallDetailRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.ListFirewallDetailResponse`
        """
        http_info = self._list_firewall_detail_http_info(request)
        return self._call_api(**http_info)

    def list_firewall_detail_invoker(self, request):
        http_info = self._list_firewall_detail_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_firewall_detail_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/firewall/exist",
            "request_type": request.__class__.__name__,
            "response_type": "ListFirewallDetailResponse"
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
        if 'service_type' in local_var_params:
            query_params.append(('service_type', local_var_params['service_type']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'fw_instance_id' in local_var_params:
            query_params.append(('fw_instance_id', local_var_params['fw_instance_id']))
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

    def list_firewall_list(self, request):
        """查询防火墙列表

        查询防火墙列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListFirewallList
        :type request: :class:`huaweicloudsdkcfw.v1.ListFirewallListRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.ListFirewallListResponse`
        """
        http_info = self._list_firewall_list_http_info(request)
        return self._call_api(**http_info)

    def list_firewall_list_invoker(self, request):
        http_info = self._list_firewall_list_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_firewall_list_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/firewalls/list",
            "request_type": request.__class__.__name__,
            "response_type": "ListFirewallListResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

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

    def list_flow_logs(self, request):
        """查询流日志

        查询流日志
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListFlowLogs
        :type request: :class:`huaweicloudsdkcfw.v1.ListFlowLogsRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.ListFlowLogsResponse`
        """
        http_info = self._list_flow_logs_http_info(request)
        return self._call_api(**http_info)

    def list_flow_logs_invoker(self, request):
        http_info = self._list_flow_logs_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_flow_logs_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/cfw/logs/flow",
            "request_type": request.__class__.__name__,
            "response_type": "ListFlowLogsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'fw_instance_id' in local_var_params:
            query_params.append(('fw_instance_id', local_var_params['fw_instance_id']))
        if 'direction' in local_var_params:
            query_params.append(('direction', local_var_params['direction']))
        if 'log_type' in local_var_params:
            query_params.append(('log_type', local_var_params['log_type']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'src_ip' in local_var_params:
            query_params.append(('src_ip', local_var_params['src_ip']))
        if 'src_port' in local_var_params:
            query_params.append(('src_port', local_var_params['src_port']))
        if 'dst_ip' in local_var_params:
            query_params.append(('dst_ip', local_var_params['dst_ip']))
        if 'dst_port' in local_var_params:
            query_params.append(('dst_port', local_var_params['dst_port']))
        if 'protocol' in local_var_params:
            query_params.append(('protocol', local_var_params['protocol']))
        if 'app' in local_var_params:
            query_params.append(('app', local_var_params['app']))
        if 'log_id' in local_var_params:
            query_params.append(('log_id', local_var_params['log_id']))
        if 'next_date' in local_var_params:
            query_params.append(('next_date', local_var_params['next_date']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'dst_host' in local_var_params:
            query_params.append(('dst_host', local_var_params['dst_host']))
        if 'src_region_name' in local_var_params:
            query_params.append(('src_region_name', local_var_params['src_region_name']))
        if 'dst_region_name' in local_var_params:
            query_params.append(('dst_region_name', local_var_params['dst_region_name']))
        if 'src_province_name' in local_var_params:
            query_params.append(('src_province_name', local_var_params['src_province_name']))
        if 'dst_province_name' in local_var_params:
            query_params.append(('dst_province_name', local_var_params['dst_province_name']))
        if 'src_city_name' in local_var_params:
            query_params.append(('src_city_name', local_var_params['src_city_name']))
        if 'dst_city_name' in local_var_params:
            query_params.append(('dst_city_name', local_var_params['dst_city_name']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_job(self, request):
        """获取CFW任务执行状态

        获取CFW任务执行状态
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListJob
        :type request: :class:`huaweicloudsdkcfw.v1.ListJobRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.ListJobResponse`
        """
        http_info = self._list_job_http_info(request)
        return self._call_api(**http_info)

    def list_job_invoker(self, request):
        http_info = self._list_job_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_job_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/jobs/{job_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ListJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
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

    def list_log_config(self, request):
        """获取日志配置

        获取日志配置
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListLogConfig
        :type request: :class:`huaweicloudsdkcfw.v1.ListLogConfigRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.ListLogConfigResponse`
        """
        http_info = self._list_log_config_http_info(request)
        return self._call_api(**http_info)

    def list_log_config_invoker(self, request):
        http_info = self._list_log_config_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_log_config_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/cfw/logs/configuration",
            "request_type": request.__class__.__name__,
            "response_type": "ListLogConfigResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'fw_instance_id' in local_var_params:
            query_params.append(('fw_instance_id', local_var_params['fw_instance_id']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_protected_vpcs(self, request):
        """查询防护VPC数

        查询防护vpc信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListProtectedVpcs
        :type request: :class:`huaweicloudsdkcfw.v1.ListProtectedVpcsRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.ListProtectedVpcsResponse`
        """
        http_info = self._list_protected_vpcs_http_info(request)
        return self._call_api(**http_info)

    def list_protected_vpcs_invoker(self, request):
        http_info = self._list_protected_vpcs_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_protected_vpcs_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/vpcs/protection",
            "request_type": request.__class__.__name__,
            "response_type": "ListProtectedVpcsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'object_id' in local_var_params:
            query_params.append(('object_id', local_var_params['object_id']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'fw_instance_id' in local_var_params:
            query_params.append(('fw_instance_id', local_var_params['fw_instance_id']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_service_items(self, request):
        """查询服务成员列表

        查询服务组成员列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListServiceItems
        :type request: :class:`huaweicloudsdkcfw.v1.ListServiceItemsRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.ListServiceItemsResponse`
        """
        http_info = self._list_service_items_http_info(request)
        return self._call_api(**http_info)

    def list_service_items_invoker(self, request):
        http_info = self._list_service_items_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_service_items_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/service-items",
            "request_type": request.__class__.__name__,
            "response_type": "ListServiceItemsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'set_id' in local_var_params:
            query_params.append(('set_id', local_var_params['set_id']))
        if 'key_word' in local_var_params:
            query_params.append(('key_word', local_var_params['key_word']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'fw_instance_id' in local_var_params:
            query_params.append(('fw_instance_id', local_var_params['fw_instance_id']))
        if 'query_service_set_type' in local_var_params:
            query_params.append(('query_service_set_type', local_var_params['query_service_set_type']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_service_set_detail(self, request):
        """查询服务组详情

        查询服务组细节
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListServiceSetDetail
        :type request: :class:`huaweicloudsdkcfw.v1.ListServiceSetDetailRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.ListServiceSetDetailResponse`
        """
        http_info = self._list_service_set_detail_http_info(request)
        return self._call_api(**http_info)

    def list_service_set_detail_invoker(self, request):
        http_info = self._list_service_set_detail_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_service_set_detail_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/service-sets/{set_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ListServiceSetDetailResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'set_id' in local_var_params:
            path_params['set_id'] = local_var_params['set_id']

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'fw_instance_id' in local_var_params:
            query_params.append(('fw_instance_id', local_var_params['fw_instance_id']))
        if 'query_service_set_type' in local_var_params:
            query_params.append(('query_service_set_type', local_var_params['query_service_set_type']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_service_sets(self, request):
        """获取服务组列表

        获取服务组列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListServiceSets
        :type request: :class:`huaweicloudsdkcfw.v1.ListServiceSetsRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.ListServiceSetsResponse`
        """
        http_info = self._list_service_sets_http_info(request)
        return self._call_api(**http_info)

    def list_service_sets_invoker(self, request):
        http_info = self._list_service_sets_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_service_sets_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/service-sets",
            "request_type": request.__class__.__name__,
            "response_type": "ListServiceSetsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'object_id' in local_var_params:
            query_params.append(('object_id', local_var_params['object_id']))
        if 'key_word' in local_var_params:
            query_params.append(('key_word', local_var_params['key_word']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'fw_instance_id' in local_var_params:
            query_params.append(('fw_instance_id', local_var_params['fw_instance_id']))
        if 'query_service_set_type' in local_var_params:
            query_params.append(('query_service_set_type', local_var_params['query_service_set_type']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_address_set(self, request):
        """更新地址组信息

        更新地址组信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateAddressSet
        :type request: :class:`huaweicloudsdkcfw.v1.UpdateAddressSetRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.UpdateAddressSetResponse`
        """
        http_info = self._update_address_set_http_info(request)
        return self._call_api(**http_info)

    def update_address_set_invoker(self, request):
        http_info = self._update_address_set_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_address_set_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/address-sets/{set_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateAddressSetResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'set_id' in local_var_params:
            path_params['set_id'] = local_var_params['set_id']

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'fw_instance_id' in local_var_params:
            query_params.append(('fw_instance_id', local_var_params['fw_instance_id']))

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

    def update_black_white_list(self, request):
        """更新黑白名单列表

        更新黑白名单列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateBlackWhiteList
        :type request: :class:`huaweicloudsdkcfw.v1.UpdateBlackWhiteListRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.UpdateBlackWhiteListResponse`
        """
        http_info = self._update_black_white_list_http_info(request)
        return self._call_api(**http_info)

    def update_black_white_list_invoker(self, request):
        http_info = self._update_black_white_list_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_black_white_list_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/black-white-list/{list_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateBlackWhiteListResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'list_id' in local_var_params:
            path_params['list_id'] = local_var_params['list_id']

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'fw_instance_id' in local_var_params:
            query_params.append(('fw_instance_id', local_var_params['fw_instance_id']))

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

    def update_dns_servers(self, request):
        """更新dns服务器列表

        更新dns服务器列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateDnsServers
        :type request: :class:`huaweicloudsdkcfw.v1.UpdateDnsServersRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.UpdateDnsServersResponse`
        """
        http_info = self._update_dns_servers_http_info(request)
        return self._call_api(**http_info)

    def update_dns_servers_invoker(self, request):
        http_info = self._update_dns_servers_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_dns_servers_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/dns/servers",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateDnsServersResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'fw_instance_id' in local_var_params:
            query_params.append(('fw_instance_id', local_var_params['fw_instance_id']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

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

    def update_domain_set(self, request):
        """更新域名组

        更新域名组
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateDomainSet
        :type request: :class:`huaweicloudsdkcfw.v1.UpdateDomainSetRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.UpdateDomainSetResponse`
        """
        http_info = self._update_domain_set_http_info(request)
        return self._call_api(**http_info)

    def update_domain_set_invoker(self, request):
        http_info = self._update_domain_set_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_domain_set_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/domain-set/{set_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateDomainSetResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'set_id' in local_var_params:
            path_params['set_id'] = local_var_params['set_id']

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'fw_instance_id' in local_var_params:
            query_params.append(('fw_instance_id', local_var_params['fw_instance_id']))

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

    def update_log_config(self, request):
        """更新日志配置

        更新日志配置
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateLogConfig
        :type request: :class:`huaweicloudsdkcfw.v1.UpdateLogConfigRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.UpdateLogConfigResponse`
        """
        http_info = self._update_log_config_http_info(request)
        return self._call_api(**http_info)

    def update_log_config_invoker(self, request):
        http_info = self._update_log_config_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_log_config_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/cfw/logs/configuration",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateLogConfigResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'fw_instance_id' in local_var_params:
            query_params.append(('fw_instance_id', local_var_params['fw_instance_id']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

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

    def update_service_set(self, request):
        """修改服务组

        更新服务组
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateServiceSet
        :type request: :class:`huaweicloudsdkcfw.v1.UpdateServiceSetRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.UpdateServiceSetResponse`
        """
        http_info = self._update_service_set_http_info(request)
        return self._call_api(**http_info)

    def update_service_set_invoker(self, request):
        http_info = self._update_service_set_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_service_set_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/service-sets/{set_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateServiceSetResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'set_id' in local_var_params:
            path_params['set_id'] = local_var_params['set_id']

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'fw_instance_id' in local_var_params:
            query_params.append(('fw_instance_id', local_var_params['fw_instance_id']))

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

    def add_acl_rule(self, request):
        """创建ACL规则

        创建ACL规则
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AddAclRule
        :type request: :class:`huaweicloudsdkcfw.v1.AddAclRuleRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.AddAclRuleResponse`
        """
        http_info = self._add_acl_rule_http_info(request)
        return self._call_api(**http_info)

    def add_acl_rule_invoker(self, request):
        http_info = self._add_acl_rule_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _add_acl_rule_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/acl-rule",
            "request_type": request.__class__.__name__,
            "response_type": "AddAclRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'fw_instance_id' in local_var_params:
            query_params.append(('fw_instance_id', local_var_params['fw_instance_id']))

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

    def batch_delete_acl_rules(self, request):
        """批量删除Acl规则

        批量删除Acl规则
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchDeleteAclRules
        :type request: :class:`huaweicloudsdkcfw.v1.BatchDeleteAclRulesRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.BatchDeleteAclRulesResponse`
        """
        http_info = self._batch_delete_acl_rules_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_acl_rules_invoker(self, request):
        http_info = self._batch_delete_acl_rules_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_delete_acl_rules_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/acl-rule",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeleteAclRulesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'fw_instance_id' in local_var_params:
            query_params.append(('fw_instance_id', local_var_params['fw_instance_id']))

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

    def batch_update_acl_rule_actions(self, request):
        """批量更新规则动作

        批量更新规则动作
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchUpdateAclRuleActions
        :type request: :class:`huaweicloudsdkcfw.v1.BatchUpdateAclRuleActionsRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.BatchUpdateAclRuleActionsResponse`
        """
        http_info = self._batch_update_acl_rule_actions_http_info(request)
        return self._call_api(**http_info)

    def batch_update_acl_rule_actions_invoker(self, request):
        http_info = self._batch_update_acl_rule_actions_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_update_acl_rule_actions_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/acl-rule/action",
            "request_type": request.__class__.__name__,
            "response_type": "BatchUpdateAclRuleActionsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

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

    def delete_acl_rule(self, request):
        """删除ACL规则

        删除ACL规则组
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteAclRule
        :type request: :class:`huaweicloudsdkcfw.v1.DeleteAclRuleRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.DeleteAclRuleResponse`
        """
        http_info = self._delete_acl_rule_http_info(request)
        return self._call_api(**http_info)

    def delete_acl_rule_invoker(self, request):
        http_info = self._delete_acl_rule_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_acl_rule_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/acl-rule/{acl_rule_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteAclRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'acl_rule_id' in local_var_params:
            path_params['acl_rule_id'] = local_var_params['acl_rule_id']

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'fw_instance_id' in local_var_params:
            query_params.append(('fw_instance_id', local_var_params['fw_instance_id']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_acl_rule_hit_count(self, request):
        """删除规则击中次数

        清除规则击中次数
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteAclRuleHitCount
        :type request: :class:`huaweicloudsdkcfw.v1.DeleteAclRuleHitCountRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.DeleteAclRuleHitCountResponse`
        """
        http_info = self._delete_acl_rule_hit_count_http_info(request)
        return self._call_api(**http_info)

    def delete_acl_rule_hit_count_invoker(self, request):
        http_info = self._delete_acl_rule_hit_count_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_acl_rule_hit_count_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/acl-rule/count",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteAclRuleHitCountResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'fw_instance_id' in local_var_params:
            query_params.append(('fw_instance_id', local_var_params['fw_instance_id']))

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

    def list_acl_rule_hit_count(self, request):
        """获取规则击中次数

        获取规则击中次数
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAclRuleHitCount
        :type request: :class:`huaweicloudsdkcfw.v1.ListAclRuleHitCountRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.ListAclRuleHitCountResponse`
        """
        http_info = self._list_acl_rule_hit_count_http_info(request)
        return self._call_api(**http_info)

    def list_acl_rule_hit_count_invoker(self, request):
        http_info = self._list_acl_rule_hit_count_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_acl_rule_hit_count_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/acl-rule/count",
            "request_type": request.__class__.__name__,
            "response_type": "ListAclRuleHitCountResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'fw_instance_id' in local_var_params:
            query_params.append(('fw_instance_id', local_var_params['fw_instance_id']))

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

    def list_acl_rules(self, request):
        """查询防护规则

        查询防护规则
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAclRules
        :type request: :class:`huaweicloudsdkcfw.v1.ListAclRulesRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.ListAclRulesResponse`
        """
        http_info = self._list_acl_rules_http_info(request)
        return self._call_api(**http_info)

    def list_acl_rules_invoker(self, request):
        http_info = self._list_acl_rules_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_acl_rules_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/acl-rules",
            "request_type": request.__class__.__name__,
            "response_type": "ListAclRulesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'object_id' in local_var_params:
            query_params.append(('object_id', local_var_params['object_id']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'ip' in local_var_params:
            query_params.append(('ip', local_var_params['ip']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'direction' in local_var_params:
            query_params.append(('direction', local_var_params['direction']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'action_type' in local_var_params:
            query_params.append(('action_type', local_var_params['action_type']))
        if 'address_type' in local_var_params:
            query_params.append(('address_type', local_var_params['address_type']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'fw_instance_id' in local_var_params:
            query_params.append(('fw_instance_id', local_var_params['fw_instance_id']))
        if 'tags_id' in local_var_params:
            query_params.append(('tags_id', local_var_params['tags_id']))
        if 'source' in local_var_params:
            query_params.append(('source', local_var_params['source']))
        if 'destination' in local_var_params:
            query_params.append(('destination', local_var_params['destination']))
        if 'service' in local_var_params:
            query_params.append(('service', local_var_params['service']))
        if 'application' in local_var_params:
            query_params.append(('application', local_var_params['application']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_rule_acl_tags(self, request):
        """查询规则标签

        查询规则标签
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListRuleAclTags
        :type request: :class:`huaweicloudsdkcfw.v1.ListRuleAclTagsRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.ListRuleAclTagsResponse`
        """
        http_info = self._list_rule_acl_tags_http_info(request)
        return self._call_api(**http_info)

    def list_rule_acl_tags_invoker(self, request):
        http_info = self._list_rule_acl_tags_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_rule_acl_tags_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/cfw-acl/tags",
            "request_type": request.__class__.__name__,
            "response_type": "ListRuleAclTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'fw_instance_id' in local_var_params:
            query_params.append(('fw_instance_id', local_var_params['fw_instance_id']))
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

    def update_acl_rule(self, request):
        """更新ACL规则

        更新ACL规则
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateAclRule
        :type request: :class:`huaweicloudsdkcfw.v1.UpdateAclRuleRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.UpdateAclRuleResponse`
        """
        http_info = self._update_acl_rule_http_info(request)
        return self._call_api(**http_info)

    def update_acl_rule_invoker(self, request):
        http_info = self._update_acl_rule_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_acl_rule_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/acl-rule/{acl_rule_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateAclRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'acl_rule_id' in local_var_params:
            path_params['acl_rule_id'] = local_var_params['acl_rule_id']

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'fw_instance_id' in local_var_params:
            query_params.append(('fw_instance_id', local_var_params['fw_instance_id']))

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

    def update_acl_rule_order(self, request):
        """ACL防护规则优先级设置

        ACL防护规则优先级设置
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateAclRuleOrder
        :type request: :class:`huaweicloudsdkcfw.v1.UpdateAclRuleOrderRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.UpdateAclRuleOrderResponse`
        """
        http_info = self._update_acl_rule_order_http_info(request)
        return self._call_api(**http_info)

    def update_acl_rule_order_invoker(self, request):
        http_info = self._update_acl_rule_order_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_acl_rule_order_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/acl-rule/order/{acl_rule_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateAclRuleOrderResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'acl_rule_id' in local_var_params:
            path_params['acl_rule_id'] = local_var_params['acl_rule_id']

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'fw_instance_id' in local_var_params:
            query_params.append(('fw_instance_id', local_var_params['fw_instance_id']))

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

    def change_eip_status(self, request):
        """弹性IP开启关闭

        开启关闭EIP，客户购买EIP后首次开启EIP防护前需使用ListEips同步EIP资产，sync字段设置为1。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ChangeEipStatus
        :type request: :class:`huaweicloudsdkcfw.v1.ChangeEipStatusRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.ChangeEipStatusResponse`
        """
        http_info = self._change_eip_status_http_info(request)
        return self._call_api(**http_info)

    def change_eip_status_invoker(self, request):
        http_info = self._change_eip_status_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _change_eip_status_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/eip/protect",
            "request_type": request.__class__.__name__,
            "response_type": "ChangeEipStatusResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'fw_instance_id' in local_var_params:
            query_params.append(('fw_instance_id', local_var_params['fw_instance_id']))

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

    def list_eip_count(self, request):
        """查询Eip个数

        查询Eip个数
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListEipCount
        :type request: :class:`huaweicloudsdkcfw.v1.ListEipCountRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.ListEipCountResponse`
        """
        http_info = self._list_eip_count_http_info(request)
        return self._call_api(**http_info)

    def list_eip_count_invoker(self, request):
        http_info = self._list_eip_count_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_eip_count_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/eip-count/{object_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ListEipCountResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'object_id' in local_var_params:
            path_params['object_id'] = local_var_params['object_id']

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'fw_instance_id' in local_var_params:
            query_params.append(('fw_instance_id', local_var_params['fw_instance_id']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_eips(self, request):
        """弹性IP列表查询

        弹性IP列表查询
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListEips
        :type request: :class:`huaweicloudsdkcfw.v1.ListEipsRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.ListEipsResponse`
        """
        http_info = self._list_eips_http_info(request)
        return self._call_api(**http_info)

    def list_eips_invoker(self, request):
        http_info = self._list_eips_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_eips_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/eips/protect",
            "request_type": request.__class__.__name__,
            "response_type": "ListEipsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'object_id' in local_var_params:
            query_params.append(('object_id', local_var_params['object_id']))
        if 'key_word' in local_var_params:
            query_params.append(('key_word', local_var_params['key_word']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'sync' in local_var_params:
            query_params.append(('sync', local_var_params['sync']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'device_key' in local_var_params:
            query_params.append(('device_key', local_var_params['device_key']))
        if 'address_type' in local_var_params:
            query_params.append(('address_type', local_var_params['address_type']))
        if 'fw_instance_id' in local_var_params:
            query_params.append(('fw_instance_id', local_var_params['fw_instance_id']))
        if 'fw_key_word' in local_var_params:
            query_params.append(('fw_key_word', local_var_params['fw_key_word']))
        if 'eps_id' in local_var_params:
            query_params.append(('eps_id', local_var_params['eps_id']))
        if 'tags' in local_var_params:
            query_params.append(('tags', local_var_params['tags']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def change_ips_protect_mode(self, request):
        """切换防护模式

        切换防护模式
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ChangeIpsProtectMode
        :type request: :class:`huaweicloudsdkcfw.v1.ChangeIpsProtectModeRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.ChangeIpsProtectModeResponse`
        """
        http_info = self._change_ips_protect_mode_http_info(request)
        return self._call_api(**http_info)

    def change_ips_protect_mode_invoker(self, request):
        http_info = self._change_ips_protect_mode_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _change_ips_protect_mode_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/ips/protect",
            "request_type": request.__class__.__name__,
            "response_type": "ChangeIpsProtectModeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'fw_instance_id' in local_var_params:
            query_params.append(('fw_instance_id', local_var_params['fw_instance_id']))

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

    def change_ips_switch_status(self, request):
        """IPS特性开关操作

        切换开关状态
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ChangeIpsSwitchStatus
        :type request: :class:`huaweicloudsdkcfw.v1.ChangeIpsSwitchStatusRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.ChangeIpsSwitchStatusResponse`
        """
        http_info = self._change_ips_switch_status_http_info(request)
        return self._call_api(**http_info)

    def change_ips_switch_status_invoker(self, request):
        http_info = self._change_ips_switch_status_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _change_ips_switch_status_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/ips/switch",
            "request_type": request.__class__.__name__,
            "response_type": "ChangeIpsSwitchStatusResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'fw_instance_id' in local_var_params:
            query_params.append(('fw_instance_id', local_var_params['fw_instance_id']))

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def list_ips_protect_mode(self, request):
        """查询防护模式

        查询防护模式
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListIpsProtectMode
        :type request: :class:`huaweicloudsdkcfw.v1.ListIpsProtectModeRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.ListIpsProtectModeResponse`
        """
        http_info = self._list_ips_protect_mode_http_info(request)
        return self._call_api(**http_info)

    def list_ips_protect_mode_invoker(self, request):
        http_info = self._list_ips_protect_mode_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_ips_protect_mode_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/ips/protect",
            "request_type": request.__class__.__name__,
            "response_type": "ListIpsProtectModeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'object_id' in local_var_params:
            query_params.append(('object_id', local_var_params['object_id']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'fw_instance_id' in local_var_params:
            query_params.append(('fw_instance_id', local_var_params['fw_instance_id']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_ips_switch_status(self, request):
        """查询IPS特性开关状态

        查询IPS特性开关状态
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListIpsSwitchStatus
        :type request: :class:`huaweicloudsdkcfw.v1.ListIpsSwitchStatusRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.ListIpsSwitchStatusResponse`
        """
        http_info = self._list_ips_switch_status_http_info(request)
        return self._call_api(**http_info)

    def list_ips_switch_status_invoker(self, request):
        http_info = self._list_ips_switch_status_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_ips_switch_status_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/ips/switch",
            "request_type": request.__class__.__name__,
            "response_type": "ListIpsSwitchStatusResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'object_id' in local_var_params:
            query_params.append(('object_id', local_var_params['object_id']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'fw_instance_id' in local_var_params:
            query_params.append(('fw_instance_id', local_var_params['fw_instance_id']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

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

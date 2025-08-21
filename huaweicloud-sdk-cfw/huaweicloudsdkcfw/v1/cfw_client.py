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
        r"""添加地址组成员

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
        r"""添加地址组

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
        r"""创建黑白名单规则

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
        r"""添加域名组

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
        r"""添加域名列表

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
        r"""创建日志配置

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
        r"""新建服务成员

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
        r"""新建服务组

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
        r"""批量删除地址组成员

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

    def batch_delete_domain_set(self, request):
        r"""批量删除域名组

        批量删除域名组
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchDeleteDomainSet
        :type request: :class:`huaweicloudsdkcfw.v1.BatchDeleteDomainSetRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.BatchDeleteDomainSetResponse`
        """
        http_info = self._batch_delete_domain_set_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_domain_set_invoker(self, request):
        http_info = self._batch_delete_domain_set_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_delete_domain_set_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/domain-sets/batch-delete",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeleteDomainSetResponse"
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

    def batch_delete_service_items(self, request):
        r"""批量删除服务组成员信息

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
        r"""取消抓包任务

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

    def create_capture_task(self, request):
        r"""创建抓包任务

        创建抓包任务，每个任务只能执行一次。
        
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
        r"""创建东西向防火墙

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
        r"""创建防火墙

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
        r"""标签创建接口

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
        r"""删除地址组成员

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
        r"""删除地址组

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
        r"""删除黑白名单规则

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
        r"""批量删除抓包任务

        批量删除抓包任务
        
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
        r"""删除域名组

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
        r"""删除域名列表

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

    def delete_firewall(self, request):
        r"""删除防火墙

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

    def delete_ip_blacklist(self, request):
        r"""删除已经导入的IP黑名单

        删除流量过滤功能下已经导入的IP黑名单，指定生效范围进行删除。 标准版的墙只会存在生效范围为EIP的IP黑名单，专业版的墙会存在生效范围为EIP和NAT的IP黑名单。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteIpBlacklist
        :type request: :class:`huaweicloudsdkcfw.v1.DeleteIpBlacklistRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.DeleteIpBlacklistResponse`
        """
        http_info = self._delete_ip_blacklist_http_info(request)
        return self._call_api(**http_info)

    def delete_ip_blacklist_invoker(self, request):
        http_info = self._delete_ip_blacklist_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_ip_blacklist_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/ptf/ip-blacklist",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteIpBlacklistResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
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

    def delete_service_item(self, request):
        r"""删除服务成员

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
        r"""删除服务组

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
        r"""删除标签

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

    def enable_ip_blacklist(self, request):
        r"""开启或者关闭流量过滤的IP黑名单功能

        开启或者关闭流量过滤功能，当前流量过滤是通过导入IP黑名单实现的。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for EnableIpBlacklist
        :type request: :class:`huaweicloudsdkcfw.v1.EnableIpBlacklistRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.EnableIpBlacklistResponse`
        """
        http_info = self._enable_ip_blacklist_http_info(request)
        return self._call_api(**http_info)

    def enable_ip_blacklist_invoker(self, request):
        http_info = self._enable_ip_blacklist_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _enable_ip_blacklist_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/ptf/ip-blacklist/switch",
            "request_type": request.__class__.__name__,
            "response_type": "EnableIpBlacklistResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
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

    def export_ip_blacklist(self, request):
        r"""导出用于流量过滤的IP黑名单

        指定IP黑名单的名字进行导出，当前只有两种文件名，在EIP生效的文件名为ip-blacklist-eip.txt，在 NAT生效的文件名为ip-blacklist-nat.txt。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ExportIpBlacklist
        :type request: :class:`huaweicloudsdkcfw.v1.ExportIpBlacklistRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.ExportIpBlacklistResponse`
        """
        http_info = self._export_ip_blacklist_http_info(request)
        return self._call_api(**http_info)

    def export_ip_blacklist_invoker(self, request):
        http_info = self._export_ip_blacklist_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _export_ip_blacklist_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/ptf/ip-blacklist/export",
            "request_type": request.__class__.__name__,
            "response_type": "ExportIpBlacklistResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'fw_instance_id' in local_var_params:
            query_params.append(('fw_instance_id', local_var_params['fw_instance_id']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["Content-Disposition", "Content-Type", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def import_ip_blacklist(self, request):
        r"""导入IP黑名单用于流量过滤

        此接口用来导入IP黑名单，IP列表保存在request的body中，IP列表支持的格式如下：
        单个IP地址，例如：100.1.1.10
        连续的IP地址段，例如：80.1.1.3-80.1.1.30
        掩码格式的网段，例如：6.6.6.0/24
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ImportIpBlacklist
        :type request: :class:`huaweicloudsdkcfw.v1.ImportIpBlacklistRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.ImportIpBlacklistResponse`
        """
        http_info = self._import_ip_blacklist_http_info(request)
        return self._call_api(**http_info)

    def import_ip_blacklist_invoker(self, request):
        http_info = self._import_ip_blacklist_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _import_ip_blacklist_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/ptf/ip-blacklist/import",
            "request_type": request.__class__.__name__,
            "response_type": "ImportIpBlacklistResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
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

    def list_access_control_logs(self, request):
        r"""查询访问控制日志

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
        r"""查询地址组成员

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
        r"""查询地址组详细信息

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
        r"""查询地址组列表

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
        r"""查询攻击日志

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
        r"""查询黑白名单列表

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
        r"""获取抓包任务结果

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
        r"""查询抓包任务

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
        r"""查询dns服务器列表

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
        r"""查询域名解析ip地址

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

    def list_domain_parse_ip(self, request):
        r"""获取域名地址解析结果

        获取域名地址解析结果
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListDomainParseIp
        :type request: :class:`huaweicloudsdkcfw.v1.ListDomainParseIpRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.ListDomainParseIpResponse`
        """
        http_info = self._list_domain_parse_ip_http_info(request)
        return self._call_api(**http_info)

    def list_domain_parse_ip_invoker(self, request):
        http_info = self._list_domain_parse_ip_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_domain_parse_ip_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/domain/parse-ip-list/{domain_address_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ListDomainParseIpResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_address_id' in local_var_params:
            path_params['domain_address_id'] = local_var_params['domain_address_id']

        query_params = []
        if 'address_type' in local_var_params:
            query_params.append(('address_type', local_var_params['address_type']))
        if 'domain_set_id' in local_var_params:
            query_params.append(('domain_set_id', local_var_params['domain_set_id']))
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

    def list_domain_sets(self, request):
        r"""查询域名组列表

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
        r"""获取域名组下域名列表

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
        r"""获取东西向防火墙信息

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
        r"""查询防火墙详细信息

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
        r"""查询防火墙列表

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
        r"""查询流日志

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

    def list_ip_blacklist(self, request):
        r"""获取导入的IP黑名单列表信息

        获取防火墙实例中已经导入的IP黑名单信息，标准版防火墙只会显示一条EIP的记录，专业版防火墙可能显示EIP、NAT或EIP和NAT的记录，根据导入的情况确定。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListIpBlacklist
        :type request: :class:`huaweicloudsdkcfw.v1.ListIpBlacklistRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.ListIpBlacklistResponse`
        """
        http_info = self._list_ip_blacklist_http_info(request)
        return self._call_api(**http_info)

    def list_ip_blacklist_invoker(self, request):
        http_info = self._list_ip_blacklist_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_ip_blacklist_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/ptf/ip-blacklist",
            "request_type": request.__class__.__name__,
            "response_type": "ListIpBlacklistResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
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

    def list_ip_blacklist_switch(self, request):
        r"""获取流量过滤功能的开关信息

        流量过滤功能可以打开或者关闭，通过此接口可以获取当前的开关信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListIpBlacklistSwitch
        :type request: :class:`huaweicloudsdkcfw.v1.ListIpBlacklistSwitchRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.ListIpBlacklistSwitchResponse`
        """
        http_info = self._list_ip_blacklist_switch_http_info(request)
        return self._call_api(**http_info)

    def list_ip_blacklist_switch_invoker(self, request):
        http_info = self._list_ip_blacklist_switch_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_ip_blacklist_switch_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/ptf/ip-blacklist/switch",
            "request_type": request.__class__.__name__,
            "response_type": "ListIpBlacklistSwitchResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
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

    def list_job(self, request):
        r"""获取CFW任务执行状态

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
        r"""获取日志配置

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

    def list_project_tags(self, request):
        r"""查询标签信息

        查询标签信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListProjectTags
        :type request: :class:`huaweicloudsdkcfw.v1.ListProjectTagsRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.ListProjectTagsResponse`
        """
        http_info = self._list_project_tags_http_info(request)
        return self._call_api(**http_info)

    def list_project_tags_invoker(self, request):
        http_info = self._list_project_tags_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_project_tags_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/cfw-cfw/tags",
            "request_type": request.__class__.__name__,
            "response_type": "ListProjectTagsResponse"
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

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

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
        r"""查询防护VPC数

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

    def list_resource_tags(self, request):
        r"""查询资源标签信息

        查询资源标签信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListResourceTags
        :type request: :class:`huaweicloudsdkcfw.v1.ListResourceTagsRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.ListResourceTagsResponse`
        """
        http_info = self._list_resource_tags_http_info(request)
        return self._call_api(**http_info)

    def list_resource_tags_invoker(self, request):
        http_info = self._list_resource_tags_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_resource_tags_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/cfw-cfw/{fw_instance_id}/tags",
            "request_type": request.__class__.__name__,
            "response_type": "ListResourceTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'fw_instance_id' in local_var_params:
            path_params['fw_instance_id'] = local_var_params['fw_instance_id']

        query_params = []
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

    def list_service_items(self, request):
        r"""查询服务成员列表

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
        r"""查询服务组详情

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
        r"""获取服务组列表

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

    def retry_ip_blacklist(self, request):
        r"""用于流量过滤的IP黑名单导入失败后进行重新导入

        用于流量过滤的IP黑名单导入失败后，调用此接口进行重试。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RetryIpBlacklist
        :type request: :class:`huaweicloudsdkcfw.v1.RetryIpBlacklistRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.RetryIpBlacklistResponse`
        """
        http_info = self._retry_ip_blacklist_http_info(request)
        return self._call_api(**http_info)

    def retry_ip_blacklist_invoker(self, request):
        http_info = self._retry_ip_blacklist_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _retry_ip_blacklist_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/ptf/ip-blacklist/retry",
            "request_type": request.__class__.__name__,
            "response_type": "RetryIpBlacklistResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
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

    def save_tags(self, request):
        r"""保存资源标签接口

        保存资源标签接口
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SaveTags
        :type request: :class:`huaweicloudsdkcfw.v1.SaveTagsRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.SaveTagsResponse`
        """
        http_info = self._save_tags_http_info(request)
        return self._call_api(**http_info)

    def save_tags_invoker(self, request):
        http_info = self._save_tags_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _save_tags_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/cfw-cfw/{fw_instance_id}/tags/save",
            "request_type": request.__class__.__name__,
            "response_type": "SaveTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'fw_instance_id' in local_var_params:
            path_params['fw_instance_id'] = local_var_params['fw_instance_id']

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

    def show_alarm_config(self, request):
        r"""获取告警配置信息

        获取告警配置信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAlarmConfig
        :type request: :class:`huaweicloudsdkcfw.v1.ShowAlarmConfigRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.ShowAlarmConfigResponse`
        """
        http_info = self._show_alarm_config_http_info(request)
        return self._call_api(**http_info)

    def show_alarm_config_invoker(self, request):
        http_info = self._show_alarm_config_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_alarm_config_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/cfw/alarm/config",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAlarmConfigResponse"
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

    def show_anti_virus_rule(self, request):
        r"""获取防火墙反病毒规则信息

        获取防火墙反病毒规则信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAntiVirusRule
        :type request: :class:`huaweicloudsdkcfw.v1.ShowAntiVirusRuleRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.ShowAntiVirusRuleResponse`
        """
        http_info = self._show_anti_virus_rule_http_info(request)
        return self._call_api(**http_info)

    def show_anti_virus_rule_invoker(self, request):
        http_info = self._show_anti_virus_rule_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_anti_virus_rule_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/anti-virus/rule",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAntiVirusRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'object_id' in local_var_params:
            query_params.append(('object_id', local_var_params['object_id']))
        if 'engine_type' in local_var_params:
            query_params.append(('engine_type', local_var_params['engine_type']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
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

    def show_anti_virus_switch(self, request):
        r"""查看反病毒开关

        查看反病毒开关
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAntiVirusSwitch
        :type request: :class:`huaweicloudsdkcfw.v1.ShowAntiVirusSwitchRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.ShowAntiVirusSwitchResponse`
        """
        http_info = self._show_anti_virus_switch_http_info(request)
        return self._call_api(**http_info)

    def show_anti_virus_switch_invoker(self, request):
        http_info = self._show_anti_virus_switch_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_anti_virus_switch_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/anti-virus/switch",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAntiVirusSwitchResponse"
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

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_domain_set_detail(self, request):
        r"""查看域名组详情

        查看域名组详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDomainSetDetail
        :type request: :class:`huaweicloudsdkcfw.v1.ShowDomainSetDetailRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.ShowDomainSetDetailResponse`
        """
        http_info = self._show_domain_set_detail_http_info(request)
        return self._call_api(**http_info)

    def show_domain_set_detail_invoker(self, request):
        http_info = self._show_domain_set_detail_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_domain_set_detail_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/domain-set/{domain_set_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDomainSetDetailResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_set_id' in local_var_params:
            path_params['domain_set_id'] = local_var_params['domain_set_id']

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

    def update_address_set(self, request):
        r"""更新地址组信息

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

    def update_alarm_config(self, request):
        r"""修改告警配置接口

        修改告警配置接口
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateAlarmConfig
        :type request: :class:`huaweicloudsdkcfw.v1.UpdateAlarmConfigRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.UpdateAlarmConfigResponse`
        """
        http_info = self._update_alarm_config_http_info(request)
        return self._call_api(**http_info)

    def update_alarm_config_invoker(self, request):
        http_info = self._update_alarm_config_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_alarm_config_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/cfw/alarm/config",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateAlarmConfigResponse"
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

    def update_anti_virus_rule(self, request):
        r"""修改反病毒规则

        修改反病毒规则
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateAntiVirusRule
        :type request: :class:`huaweicloudsdkcfw.v1.UpdateAntiVirusRuleRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.UpdateAntiVirusRuleResponse`
        """
        http_info = self._update_anti_virus_rule_http_info(request)
        return self._call_api(**http_info)

    def update_anti_virus_rule_invoker(self, request):
        http_info = self._update_anti_virus_rule_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_anti_virus_rule_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/anti-virus/rule",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateAntiVirusRuleResponse"
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

    def update_anti_virus_switch(self, request):
        r"""修改反病毒开关

        修改反病毒开关
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateAntiVirusSwitch
        :type request: :class:`huaweicloudsdkcfw.v1.UpdateAntiVirusSwitchRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.UpdateAntiVirusSwitchResponse`
        """
        http_info = self._update_anti_virus_switch_http_info(request)
        return self._call_api(**http_info)

    def update_anti_virus_switch_invoker(self, request):
        http_info = self._update_anti_virus_switch_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_anti_virus_switch_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/anti-virus/switch",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateAntiVirusSwitchResponse"
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

    def update_black_white_list(self, request):
        r"""更新黑白名单列表

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
        r"""更新dns服务器列表

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
        r"""更新域名组

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
        r"""更新日志配置

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

    def update_object_config_desc(self, request):
        r"""编辑对象组内成员的描述信息

        编辑对象组内成员的描述信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateObjectConfigDesc
        :type request: :class:`huaweicloudsdkcfw.v1.UpdateObjectConfigDescRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.UpdateObjectConfigDescResponse`
        """
        http_info = self._update_object_config_desc_http_info(request)
        return self._call_api(**http_info)

    def update_object_config_desc_invoker(self, request):
        http_info = self._update_object_config_desc_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_object_config_desc_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/config/object/description",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateObjectConfigDescResponse"
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

    def update_service_set(self, request):
        r"""修改服务组

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
        r"""创建ACL规则

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
        r"""批量删除Acl规则

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
        r"""批量更新规则动作

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

    def delete_acl_rule(self, request):
        r"""删除ACL规则

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
        r"""删除规则击中次数

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
        r"""获取规则击中次数

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
        r"""查询防护规则

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

    def list_regions(self, request):
        r"""查看region列表

        查看region列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListRegions
        :type request: :class:`huaweicloudsdkcfw.v1.ListRegionsRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.ListRegionsResponse`
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
            "resource_path": "/v1/{project_id}/regions",
            "request_type": request.__class__.__name__,
            "response_type": "ListRegionsResponse"
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

    def list_rule_acl_tags(self, request):
        r"""查询规则标签

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

    def show_import_status(self, request):
        r"""查看导入状态接口

        查看导入状态接口
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowImportStatus
        :type request: :class:`huaweicloudsdkcfw.v1.ShowImportStatusRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.ShowImportStatusResponse`
        """
        http_info = self._show_import_status_http_info(request)
        return self._call_api(**http_info)

    def show_import_status_invoker(self, request):
        http_info = self._show_import_status_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_import_status_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/acl-rule/import-status",
            "request_type": request.__class__.__name__,
            "response_type": "ShowImportStatusResponse"
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

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

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
        r"""更新ACL规则

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
        r"""ACL防护规则优先级设置

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
        r"""弹性IP开启关闭

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

    def list_alarm_whitelist(self, request):
        r"""查看eip告警白名单

        查看eip告警白名单
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAlarmWhitelist
        :type request: :class:`huaweicloudsdkcfw.v1.ListAlarmWhitelistRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.ListAlarmWhitelistResponse`
        """
        http_info = self._list_alarm_whitelist_http_info(request)
        return self._call_api(**http_info)

    def list_alarm_whitelist_invoker(self, request):
        http_info = self._list_alarm_whitelist_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_alarm_whitelist_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/eip/alarm-whitelist/{fw_instance_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ListAlarmWhitelistResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'fw_instance_id' in local_var_params:
            path_params['fw_instance_id'] = local_var_params['fw_instance_id']

        query_params = []
        if 'ip_address' in local_var_params:
            query_params.append(('ip_address', local_var_params['ip_address']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
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

    def list_eip_count(self, request):
        r"""查询Eip个数

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
        r"""弹性IP列表查询

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

    def show_auto_protect_status(self, request):
        r"""获取eip自动防护状态信息

        获取eip自动防护状态信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAutoProtectStatus
        :type request: :class:`huaweicloudsdkcfw.v1.ShowAutoProtectStatusRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.ShowAutoProtectStatusResponse`
        """
        http_info = self._show_auto_protect_status_http_info(request)
        return self._call_api(**http_info)

    def show_auto_protect_status_invoker(self, request):
        http_info = self._show_auto_protect_status_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_auto_protect_status_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/eip/auto-protect-status/{object_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAutoProtectStatusResponse"
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

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def switch_auto_protect_status(self, request):
        r"""修改eip自动防护开关

        修改eip自动防护开关
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SwitchAutoProtectStatus
        :type request: :class:`huaweicloudsdkcfw.v1.SwitchAutoProtectStatusRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.SwitchAutoProtectStatusResponse`
        """
        http_info = self._switch_auto_protect_status_http_info(request)
        return self._call_api(**http_info)

    def switch_auto_protect_status_invoker(self, request):
        http_info = self._switch_auto_protect_status_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _switch_auto_protect_status_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/eip/auto-protect-status/switch",
            "request_type": request.__class__.__name__,
            "response_type": "SwitchAutoProtectStatusResponse"
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

    def change_ips_protect_mode(self, request):
        r"""切换防护模式

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

    def change_ips_rule_mode(self, request):
        r"""改变ips规则模式

        改变ips规则模式
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ChangeIpsRuleMode
        :type request: :class:`huaweicloudsdkcfw.v1.ChangeIpsRuleModeRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.ChangeIpsRuleModeResponse`
        """
        http_info = self._change_ips_rule_mode_http_info(request)
        return self._call_api(**http_info)

    def change_ips_rule_mode_invoker(self, request):
        http_info = self._change_ips_rule_mode_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _change_ips_rule_mode_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/ips-rule/mode",
            "request_type": request.__class__.__name__,
            "response_type": "ChangeIpsRuleModeResponse"
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

    def change_ips_switch_status(self, request):
        r"""IPS特性开关操作

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
        r"""查询防护模式

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

    def list_ips_rules(self, request):
        r"""查询频率ips规则信息

        查询频率ips规则信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListIpsRules
        :type request: :class:`huaweicloudsdkcfw.v1.ListIpsRulesRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.ListIpsRulesResponse`
        """
        http_info = self._list_ips_rules_http_info(request)
        return self._call_api(**http_info)

    def list_ips_rules_invoker(self, request):
        http_info = self._list_ips_rules_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_ips_rules_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/advanced-ips-rules",
            "request_type": request.__class__.__name__,
            "response_type": "ListIpsRulesResponse"
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

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_ips_rules1(self, request):
        r"""获取ips规则列表

        获取ips规则列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListIpsRules1
        :type request: :class:`huaweicloudsdkcfw.v1.ListIpsRules1Request`
        :rtype: :class:`huaweicloudsdkcfw.v1.ListIpsRules1Response`
        """
        http_info = self._list_ips_rules1_http_info(request)
        return self._call_api(**http_info)

    def list_ips_rules1_invoker(self, request):
        http_info = self._list_ips_rules1_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_ips_rules1_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/ips-rule",
            "request_type": request.__class__.__name__,
            "response_type": "ListIpsRules1Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'affected_application_like' in local_var_params:
            query_params.append(('affected_application_like', local_var_params['affected_application_like']))
        if 'create_time' in local_var_params:
            query_params.append(('create_time', local_var_params['create_time']))
        if 'fw_instance_id' in local_var_params:
            query_params.append(('fw_instance_id', local_var_params['fw_instance_id']))
        if 'ips_cve_like' in local_var_params:
            query_params.append(('ips_cve_like', local_var_params['ips_cve_like']))
        if 'ips_group' in local_var_params:
            query_params.append(('ips_group', local_var_params['ips_group']))
        if 'ips_id' in local_var_params:
            query_params.append(('ips_id', local_var_params['ips_id']))
        if 'ips_level' in local_var_params:
            query_params.append(('ips_level', local_var_params['ips_level']))
        if 'ips_name_like' in local_var_params:
            query_params.append(('ips_name_like', local_var_params['ips_name_like']))
        if 'ips_rules_type_like' in local_var_params:
            query_params.append(('ips_rules_type_like', local_var_params['ips_rules_type_like']))
        if 'ips_status' in local_var_params:
            query_params.append(('ips_status', local_var_params['ips_status']))
        if 'is_updated_ips_rule_queried' in local_var_params:
            query_params.append(('is_updated_ips_rule_queried', local_var_params['is_updated_ips_rule_queried']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'object_id' in local_var_params:
            query_params.append(('object_id', local_var_params['object_id']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
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

    def list_ips_switch_status(self, request):
        r"""查询IPS特性开关状态

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

    def show_ips_update_time(self, request):
        r"""获取ips规则细节

        获取ips规则细节
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowIpsUpdateTime
        :type request: :class:`huaweicloudsdkcfw.v1.ShowIpsUpdateTimeRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.ShowIpsUpdateTimeResponse`
        """
        http_info = self._show_ips_update_time_http_info(request)
        return self._call_api(**http_info)

    def show_ips_update_time_invoker(self, request):
        http_info = self._show_ips_update_time_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_ips_update_time_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/ips-rule/detail",
            "request_type": request.__class__.__name__,
            "response_type": "ShowIpsUpdateTimeResponse"
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

    def update_advanced_ips_rule(self, request):
        r"""创建频率ips规则

        创建频率ips规则
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateAdvancedIpsRule
        :type request: :class:`huaweicloudsdkcfw.v1.UpdateAdvancedIpsRuleRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.UpdateAdvancedIpsRuleResponse`
        """
        http_info = self._update_advanced_ips_rule_http_info(request)
        return self._call_api(**http_info)

    def update_advanced_ips_rule_invoker(self, request):
        http_info = self._update_advanced_ips_rule_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_advanced_ips_rule_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/advanced-ips-rule",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateAdvancedIpsRuleResponse"
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

    def list_customer_ips(self, request):
        r"""查看自定义IPS规则列表

        查看自定义IPS规则列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListCustomerIps
        :type request: :class:`huaweicloudsdkcfw.v1.ListCustomerIpsRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.ListCustomerIpsResponse`
        """
        http_info = self._list_customer_ips_http_info(request)
        return self._call_api(**http_info)

    def list_customer_ips_invoker(self, request):
        http_info = self._list_customer_ips_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_customer_ips_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/ips/custom-rule",
            "request_type": request.__class__.__name__,
            "response_type": "ListCustomerIpsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'action_type' in local_var_params:
            query_params.append(('action_type', local_var_params['action_type']))
        if 'affected_os' in local_var_params:
            query_params.append(('affected_os', local_var_params['affected_os']))
        if 'attack_type' in local_var_params:
            query_params.append(('attack_type', local_var_params['attack_type']))
        if 'ips_name' in local_var_params:
            query_params.append(('ips_name', local_var_params['ips_name']))
        if 'ips_id' in local_var_params:
            query_params.append(('ips_id', local_var_params['ips_id']))
        if 'protocol' in local_var_params:
            query_params.append(('protocol', local_var_params['protocol']))
        if 'severity' in local_var_params:
            query_params.append(('severity', local_var_params['severity']))
        if 'software' in local_var_params:
            query_params.append(('software', local_var_params['software']))
        if 'object_id' in local_var_params:
            query_params.append(('object_id', local_var_params['object_id']))
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

    def show_customer_ips_info(self, request):
        r"""查询自定义IPS规则详情

        功能说明：自定义IPS规则详情，特性:根据路径输入的IPS ID查看对应的自定义IPS详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowCustomerIpsInfo
        :type request: :class:`huaweicloudsdkcfw.v1.ShowCustomerIpsInfoRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.ShowCustomerIpsInfoResponse`
        """
        http_info = self._show_customer_ips_info_http_info(request)
        return self._call_api(**http_info)

    def show_customer_ips_info_invoker(self, request):
        http_info = self._show_customer_ips_info_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_customer_ips_info_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/ips/custom-rule/{ips_cfw_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowCustomerIpsInfoResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ips_cfw_id' in local_var_params:
            path_params['ips_cfw_id'] = local_var_params['ips_cfw_id']

        query_params = []
        if 'object_id' in local_var_params:
            query_params.append(('object_id', local_var_params['object_id']))
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

    def update_customer_ips(self, request):
        r"""更新自定义IPS规则

        更新自定义IPS规则
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateCustomerIps
        :type request: :class:`huaweicloudsdkcfw.v1.UpdateCustomerIpsRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.UpdateCustomerIpsResponse`
        """
        http_info = self._update_customer_ips_http_info(request)
        return self._call_api(**http_info)

    def update_customer_ips_invoker(self, request):
        http_info = self._update_customer_ips_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_customer_ips_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/ips/custom-rule/{ips_cfw_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateCustomerIpsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ips_cfw_id' in local_var_params:
            path_params['ips_cfw_id'] = local_var_params['ips_cfw_id']

        query_params = []

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

    def list_attack_statistic(self, request):
        r"""查询攻击统计

        根据防火墙攻击日志，查询攻击统计信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAttackStatistic
        :type request: :class:`huaweicloudsdkcfw.v1.ListAttackStatisticRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.ListAttackStatisticResponse`
        """
        http_info = self._list_attack_statistic_http_info(request)
        return self._call_api(**http_info)

    def list_attack_statistic_invoker(self, request):
        http_info = self._list_attack_statistic_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_attack_statistic_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/cfw/logs/attack-statistic",
            "request_type": request.__class__.__name__,
            "response_type": "ListAttackStatisticResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'fw_instance_id' in local_var_params:
            query_params.append(('fw_instance_id', local_var_params['fw_instance_id']))
        if 'range' in local_var_params:
            query_params.append(('range', local_var_params['range']))
        if 'log_type' in local_var_params:
            query_params.append(('log_type', local_var_params['log_type']))
        if 'direction' in local_var_params:
            query_params.append(('direction', local_var_params['direction']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'vgw_id' in local_var_params:
            query_params.append(('vgw_id', local_var_params['vgw_id']))
            collection_formats['vgw_id'] = 'csv'
        if 'item' in local_var_params:
            query_params.append(('item', local_var_params['item']))
        if 'size' in local_var_params:
            query_params.append(('size', local_var_params['size']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_flow_statistic(self, request):
        r"""查询流量日志统计

        查询流量日志统计
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListFlowStatistic
        :type request: :class:`huaweicloudsdkcfw.v1.ListFlowStatisticRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.ListFlowStatisticResponse`
        """
        http_info = self._list_flow_statistic_http_info(request)
        return self._call_api(**http_info)

    def list_flow_statistic_invoker(self, request):
        http_info = self._list_flow_statistic_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_flow_statistic_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/cfw/logs/flow-statistic",
            "request_type": request.__class__.__name__,
            "response_type": "ListFlowStatisticResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'fw_instance_id' in local_var_params:
            query_params.append(('fw_instance_id', local_var_params['fw_instance_id']))
        if 'range' in local_var_params:
            query_params.append(('range', local_var_params['range']))
        if 'log_type' in local_var_params:
            query_params.append(('log_type', local_var_params['log_type']))
        if 'direction' in local_var_params:
            query_params.append(('direction', local_var_params['direction']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'vgw_id' in local_var_params:
            query_params.append(('vgw_id', local_var_params['vgw_id']))
            collection_formats['vgw_id'] = 'csv'
        if 'asset_type' in local_var_params:
            query_params.append(('asset_type', local_var_params['asset_type']))
        if 'item' in local_var_params:
            query_params.append(('item', local_var_params['item']))
        if 'size' in local_var_params:
            query_params.append(('size', local_var_params['size']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_access_detail(self, request):
        r"""查询访问控制统计详情

        查询访问控制统计详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAccessDetail
        :type request: :class:`huaweicloudsdkcfw.v1.ShowAccessDetailRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.ShowAccessDetailResponse`
        """
        http_info = self._show_access_detail_http_info(request)
        return self._call_api(**http_info)

    def show_access_detail_invoker(self, request):
        http_info = self._show_access_detail_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_access_detail_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/cfw/logs/top-access-detail",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAccessDetailResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'fw_instance_id' in local_var_params:
            query_params.append(('fw_instance_id', local_var_params['fw_instance_id']))
        if 'range' in local_var_params:
            query_params.append(('range', local_var_params['range']))
        if 'direction' in local_var_params:
            query_params.append(('direction', local_var_params['direction']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'vgw_id' in local_var_params:
            query_params.append(('vgw_id', local_var_params['vgw_id']))
            collection_formats['vgw_id'] = 'csv'
        if 'log_type' in local_var_params:
            query_params.append(('log_type', local_var_params['log_type']))
        if 'item' in local_var_params:
            query_params.append(('item', local_var_params['item']))
        if 'item_id' in local_var_params:
            query_params.append(('item_id', local_var_params['item_id']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_access_top(self, request):
        r"""查询访问日志统计信息

        获取访问日志的TOP统计信息，如TOP命中规则等
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAccessTop
        :type request: :class:`huaweicloudsdkcfw.v1.ShowAccessTopRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.ShowAccessTopResponse`
        """
        http_info = self._show_access_top_http_info(request)
        return self._call_api(**http_info)

    def show_access_top_invoker(self, request):
        http_info = self._show_access_top_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_access_top_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/cfw/logs/access-top",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAccessTopResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'fw_instance_id' in local_var_params:
            query_params.append(('fw_instance_id', local_var_params['fw_instance_id']))
        if 'range' in local_var_params:
            query_params.append(('range', local_var_params['range']))
        if 'direction' in local_var_params:
            query_params.append(('direction', local_var_params['direction']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'vgw_id' in local_var_params:
            query_params.append(('vgw_id', local_var_params['vgw_id']))
            collection_formats['vgw_id'] = 'csv'
        if 'log_type' in local_var_params:
            query_params.append(('log_type', local_var_params['log_type']))
        if 'item' in local_var_params:
            query_params.append(('item', local_var_params['item']))
        if 'rule_id' in local_var_params:
            query_params.append(('rule_id', local_var_params['rule_id']))
            collection_formats['rule_id'] = 'csv'

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_attack_detail(self, request):
        r"""查询攻击日志统计详情

        查询攻击日志统计详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAttackDetail
        :type request: :class:`huaweicloudsdkcfw.v1.ShowAttackDetailRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.ShowAttackDetailResponse`
        """
        http_info = self._show_attack_detail_http_info(request)
        return self._call_api(**http_info)

    def show_attack_detail_invoker(self, request):
        http_info = self._show_attack_detail_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_attack_detail_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/cfw/logs/attack-detail",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAttackDetailResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'fw_instance_id' in local_var_params:
            query_params.append(('fw_instance_id', local_var_params['fw_instance_id']))
        if 'range' in local_var_params:
            query_params.append(('range', local_var_params['range']))
        if 'log_type' in local_var_params:
            query_params.append(('log_type', local_var_params['log_type']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'vgw_id' in local_var_params:
            query_params.append(('vgw_id', local_var_params['vgw_id']))
            collection_formats['vgw_id'] = 'csv'
        if 'action' in local_var_params:
            query_params.append(('action', local_var_params['action']))
        if 'item' in local_var_params:
            query_params.append(('item', local_var_params['item']))
        if 'value' in local_var_params:
            query_params.append(('value', local_var_params['value']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_attack_top(self, request):
        r"""查询攻击日志TOP统计

        查询攻击日志TOP统计
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAttackTop
        :type request: :class:`huaweicloudsdkcfw.v1.ShowAttackTopRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.ShowAttackTopResponse`
        """
        http_info = self._show_attack_top_http_info(request)
        return self._call_api(**http_info)

    def show_attack_top_invoker(self, request):
        http_info = self._show_attack_top_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_attack_top_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/cfw/logs/top-attack",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAttackTopResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'fw_instance_id' in local_var_params:
            query_params.append(('fw_instance_id', local_var_params['fw_instance_id']))
        if 'range' in local_var_params:
            query_params.append(('range', local_var_params['range']))
        if 'log_type' in local_var_params:
            query_params.append(('log_type', local_var_params['log_type']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'vgw_id' in local_var_params:
            query_params.append(('vgw_id', local_var_params['vgw_id']))
            collection_formats['vgw_id'] = 'csv'
        if 'action' in local_var_params:
            query_params.append(('action', local_var_params['action']))
        if 'item' in local_var_params:
            query_params.append(('item', local_var_params['item']))
            collection_formats['item'] = 'multi'
        if 'size' in local_var_params:
            query_params.append(('size', local_var_params['size']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_attack_total(self, request):
        r"""查询攻击概览

        查询攻击概览
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAttackTotal
        :type request: :class:`huaweicloudsdkcfw.v1.ShowAttackTotalRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.ShowAttackTotalResponse`
        """
        http_info = self._show_attack_total_http_info(request)
        return self._call_api(**http_info)

    def show_attack_total_invoker(self, request):
        http_info = self._show_attack_total_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_attack_total_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/cfw/logs/total-attack",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAttackTotalResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'fw_instance_id' in local_var_params:
            query_params.append(('fw_instance_id', local_var_params['fw_instance_id']))
        if 'range' in local_var_params:
            query_params.append(('range', local_var_params['range']))
        if 'log_type' in local_var_params:
            query_params.append(('log_type', local_var_params['log_type']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'vgw_id' in local_var_params:
            query_params.append(('vgw_id', local_var_params['vgw_id']))
            collection_formats['vgw_id'] = 'csv'

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_attack_trend(self, request):
        r"""查询攻击趋势

        查询攻击趋势
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAttackTrend
        :type request: :class:`huaweicloudsdkcfw.v1.ShowAttackTrendRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.ShowAttackTrendResponse`
        """
        http_info = self._show_attack_trend_http_info(request)
        return self._call_api(**http_info)

    def show_attack_trend_invoker(self, request):
        http_info = self._show_attack_trend_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_attack_trend_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/cfw/logs/trend-attack",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAttackTrendResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'fw_instance_id' in local_var_params:
            query_params.append(('fw_instance_id', local_var_params['fw_instance_id']))
        if 'range' in local_var_params:
            query_params.append(('range', local_var_params['range']))
        if 'log_type' in local_var_params:
            query_params.append(('log_type', local_var_params['log_type']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'vgw_id' in local_var_params:
            query_params.append(('vgw_id', local_var_params['vgw_id']))
            collection_formats['vgw_id'] = 'csv'

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_flow_detail(self, request):
        r"""查询流量日志统计详情

        查询流量日志统计详情，如统计某个源IP访问详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowFlowDetail
        :type request: :class:`huaweicloudsdkcfw.v1.ShowFlowDetailRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.ShowFlowDetailResponse`
        """
        http_info = self._show_flow_detail_http_info(request)
        return self._call_api(**http_info)

    def show_flow_detail_invoker(self, request):
        http_info = self._show_flow_detail_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_flow_detail_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/cfw/logs/flow-detail",
            "request_type": request.__class__.__name__,
            "response_type": "ShowFlowDetailResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'fw_instance_id' in local_var_params:
            query_params.append(('fw_instance_id', local_var_params['fw_instance_id']))
        if 'range' in local_var_params:
            query_params.append(('range', local_var_params['range']))
        if 'log_type' in local_var_params:
            query_params.append(('log_type', local_var_params['log_type']))
        if 'direction' in local_var_params:
            query_params.append(('direction', local_var_params['direction']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'vgw_id' in local_var_params:
            query_params.append(('vgw_id', local_var_params['vgw_id']))
            collection_formats['vgw_id'] = 'csv'
        if 'asset_type' in local_var_params:
            query_params.append(('asset_type', local_var_params['asset_type']))
        if 'item' in local_var_params:
            query_params.append(('item', local_var_params['item']))
        if 'value' in local_var_params:
            query_params.append(('value', local_var_params['value']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_flow_top(self, request):
        r"""查询流量TOP统计

        查询流量TOP统计
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowFlowTop
        :type request: :class:`huaweicloudsdkcfw.v1.ShowFlowTopRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.ShowFlowTopResponse`
        """
        http_info = self._show_flow_top_http_info(request)
        return self._call_api(**http_info)

    def show_flow_top_invoker(self, request):
        http_info = self._show_flow_top_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_flow_top_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/cfw/logs/flow-top",
            "request_type": request.__class__.__name__,
            "response_type": "ShowFlowTopResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'fw_instance_id' in local_var_params:
            query_params.append(('fw_instance_id', local_var_params['fw_instance_id']))
        if 'range' in local_var_params:
            query_params.append(('range', local_var_params['range']))
        if 'log_type' in local_var_params:
            query_params.append(('log_type', local_var_params['log_type']))
        if 'direction' in local_var_params:
            query_params.append(('direction', local_var_params['direction']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'vgw_id' in local_var_params:
            query_params.append(('vgw_id', local_var_params['vgw_id']))
            collection_formats['vgw_id'] = 'csv'
        if 'asset_type' in local_var_params:
            query_params.append(('asset_type', local_var_params['asset_type']))
        if 'item' in local_var_params:
            query_params.append(('item', local_var_params['item']))
            collection_formats['item'] = 'multi'
        if 'order' in local_var_params:
            query_params.append(('order', local_var_params['order']))
        if 'size' in local_var_params:
            query_params.append(('size', local_var_params['size']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_flow_trend(self, request):
        r"""查询会话趋势

        查询会话趋势
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowFlowTrend
        :type request: :class:`huaweicloudsdkcfw.v1.ShowFlowTrendRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.ShowFlowTrendResponse`
        """
        http_info = self._show_flow_trend_http_info(request)
        return self._call_api(**http_info)

    def show_flow_trend_invoker(self, request):
        http_info = self._show_flow_trend_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_flow_trend_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/cfw/logs/flow-trend",
            "request_type": request.__class__.__name__,
            "response_type": "ShowFlowTrendResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'fw_instance_id' in local_var_params:
            query_params.append(('fw_instance_id', local_var_params['fw_instance_id']))
        if 'range' in local_var_params:
            query_params.append(('range', local_var_params['range']))
        if 'log_type' in local_var_params:
            query_params.append(('log_type', local_var_params['log_type']))
        if 'direction' in local_var_params:
            query_params.append(('direction', local_var_params['direction']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'vgw_id' in local_var_params:
            query_params.append(('vgw_id', local_var_params['vgw_id']))
            collection_formats['vgw_id'] = 'csv'
        if 'asset_type' in local_var_params:
            query_params.append(('asset_type', local_var_params['asset_type']))
        if 'ip' in local_var_params:
            query_params.append(('ip', local_var_params['ip']))
            collection_formats['ip'] = 'multi'
        if 'vpc' in local_var_params:
            query_params.append(('vpc', local_var_params['vpc']))
            collection_formats['vpc'] = 'multi'

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_logs_count(self, request):
        r"""查询日志数量

        统计日志数量，如统计风险IP的数量
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowLogsCount
        :type request: :class:`huaweicloudsdkcfw.v1.ShowLogsCountRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.ShowLogsCountResponse`
        """
        http_info = self._show_logs_count_http_info(request)
        return self._call_api(**http_info)

    def show_logs_count_invoker(self, request):
        http_info = self._show_logs_count_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_logs_count_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/logs/count",
            "request_type": request.__class__.__name__,
            "response_type": "ShowLogsCountResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'fw_instance_id' in local_var_params:
            query_params.append(('fw_instance_id', local_var_params['fw_instance_id']))
        if 'range' in local_var_params:
            query_params.append(('range', local_var_params['range']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'vgw_id' in local_var_params:
            query_params.append(('vgw_id', local_var_params['vgw_id']))
            collection_formats['vgw_id'] = 'csv'
        if 'item' in local_var_params:
            query_params.append(('item', local_var_params['item']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_traffic_trend(self, request):
        r"""查询流量趋势

        查询流量趋势，包括南北向、EIP、东西向的流量趋势
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowTrafficTrend
        :type request: :class:`huaweicloudsdkcfw.v1.ShowTrafficTrendRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.ShowTrafficTrendResponse`
        """
        http_info = self._show_traffic_trend_http_info(request)
        return self._call_api(**http_info)

    def show_traffic_trend_invoker(self, request):
        http_info = self._show_traffic_trend_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_traffic_trend_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/cfw/logs/traffic-trend",
            "request_type": request.__class__.__name__,
            "response_type": "ShowTrafficTrendResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'fw_instance_id' in local_var_params:
            query_params.append(('fw_instance_id', local_var_params['fw_instance_id']))
        if 'range' in local_var_params:
            query_params.append(('range', local_var_params['range']))
        if 'log_type' in local_var_params:
            query_params.append(('log_type', local_var_params['log_type']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'vgw_id' in local_var_params:
            query_params.append(('vgw_id', local_var_params['vgw_id']))
            collection_formats['vgw_id'] = 'csv'
        if 'agg_type' in local_var_params:
            query_params.append(('agg_type', local_var_params['agg_type']))
        if 'ip' in local_var_params:
            query_params.append(('ip', local_var_params['ip']))
            collection_formats['ip'] = 'multi'

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def export_logs(self, request):
        r"""导出防火墙日志

        导出防火墙日志
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ExportLogs
        :type request: :class:`huaweicloudsdkcfw.v1.ExportLogsRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.ExportLogsResponse`
        """
        http_info = self._export_logs_http_info(request)
        return self._call_api(**http_info)

    def export_logs_invoker(self, request):
        http_info = self._export_logs_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _export_logs_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/cfw/{fw_instance_id}/logs/export",
            "request_type": request.__class__.__name__,
            "response_type": "ExportLogsResponse"
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

    def list_logs(self, request):
        r"""查询防火墙日志

        查询防火墙日志
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListLogs
        :type request: :class:`huaweicloudsdkcfw.v1.ListLogsRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.ListLogsResponse`
        """
        http_info = self._list_logs_http_info(request)
        return self._call_api(**http_info)

    def list_logs_invoker(self, request):
        http_info = self._list_logs_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_logs_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/cfw/{fw_instance_id}/logs",
            "request_type": request.__class__.__name__,
            "response_type": "ListLogsResponse"
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

    def enable_multi_account(self, request):
        r"""开启多账号管理

        开启多账号管理
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for EnableMultiAccount
        :type request: :class:`huaweicloudsdkcfw.v1.EnableMultiAccountRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.EnableMultiAccountResponse`
        """
        http_info = self._enable_multi_account_http_info(request)
        return self._call_api(**http_info)

    def enable_multi_account_invoker(self, request):
        http_info = self._enable_multi_account_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _enable_multi_account_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/system/multi-account/enable",
            "request_type": request.__class__.__name__,
            "response_type": "EnableMultiAccountResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
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

    def list_accounts(self, request):
        r"""查询账号列表

        查询账号列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAccounts
        :type request: :class:`huaweicloudsdkcfw.v1.ListAccountsRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.ListAccountsResponse`
        """
        http_info = self._list_accounts_http_info(request)
        return self._call_api(**http_info)

    def list_accounts_invoker(self, request):
        http_info = self._list_accounts_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_accounts_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/system/multi-account/accounts",
            "request_type": request.__class__.__name__,
            "response_type": "ListAccountsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
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

    def list_organization_accounts(self, request):
        r"""查询组织账号列表

        查询组织账号列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListOrganizationAccounts
        :type request: :class:`huaweicloudsdkcfw.v1.ListOrganizationAccountsRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.ListOrganizationAccountsResponse`
        """
        http_info = self._list_organization_accounts_http_info(request)
        return self._call_api(**http_info)

    def list_organization_accounts_invoker(self, request):
        http_info = self._list_organization_accounts_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_organization_accounts_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/system/multi-account/organization-accounts",
            "request_type": request.__class__.__name__,
            "response_type": "ListOrganizationAccountsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'fw_instance_id' in local_var_params:
            query_params.append(('fw_instance_id', local_var_params['fw_instance_id']))
        if 'parent_id' in local_var_params:
            query_params.append(('parent_id', local_var_params['parent_id']))
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

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_organization_tree(self, request):
        r"""查询组织结构

        查询组织结构
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListOrganizationTree
        :type request: :class:`huaweicloudsdkcfw.v1.ListOrganizationTreeRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.ListOrganizationTreeResponse`
        """
        http_info = self._list_organization_tree_http_info(request)
        return self._call_api(**http_info)

    def list_organization_tree_invoker(self, request):
        http_info = self._list_organization_tree_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_organization_tree_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/system/multi-account/organization-tree",
            "request_type": request.__class__.__name__,
            "response_type": "ListOrganizationTreeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'fw_instance_id' in local_var_params:
            query_params.append(('fw_instance_id', local_var_params['fw_instance_id']))
        if 'parent_id' in local_var_params:
            query_params.append(('parent_id', local_var_params['parent_id']))
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

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_report_profile(self, request):
        r"""创建安全报告模板

        创建安全报告模板
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateReportProfile
        :type request: :class:`huaweicloudsdkcfw.v1.CreateReportProfileRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.CreateReportProfileResponse`
        """
        http_info = self._create_report_profile_http_info(request)
        return self._call_api(**http_info)

    def create_report_profile_invoker(self, request):
        http_info = self._create_report_profile_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_report_profile_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/report-profile",
            "request_type": request.__class__.__name__,
            "response_type": "CreateReportProfileResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
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

    def delete_report_profile(self, request):
        r"""删除安全报告模板

        删除安全报告模板
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteReportProfile
        :type request: :class:`huaweicloudsdkcfw.v1.DeleteReportProfileRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.DeleteReportProfileResponse`
        """
        http_info = self._delete_report_profile_http_info(request)
        return self._call_api(**http_info)

    def delete_report_profile_invoker(self, request):
        http_info = self._delete_report_profile_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_report_profile_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/report-profile/{report_profile_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteReportProfileResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'report_profile_id' in local_var_params:
            path_params['report_profile_id'] = local_var_params['report_profile_id']

        query_params = []
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

    def list_report_profiles(self, request):
        r"""查询安全报告模板列表

        查询安全报告模板列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListReportProfiles
        :type request: :class:`huaweicloudsdkcfw.v1.ListReportProfilesRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.ListReportProfilesResponse`
        """
        http_info = self._list_report_profiles_http_info(request)
        return self._call_api(**http_info)

    def list_report_profiles_invoker(self, request):
        http_info = self._list_report_profiles_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_report_profiles_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/report-profile",
            "request_type": request.__class__.__name__,
            "response_type": "ListReportProfilesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'category' in local_var_params:
            query_params.append(('category', local_var_params['category']))
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

    def show_firewall_report(self, request):
        r"""查询安全报告

        查询安全报告
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowFirewallReport
        :type request: :class:`huaweicloudsdkcfw.v1.ShowFirewallReportRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.ShowFirewallReportResponse`
        """
        http_info = self._show_firewall_report_http_info(request)
        return self._call_api(**http_info)

    def show_firewall_report_invoker(self, request):
        http_info = self._show_firewall_report_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_firewall_report_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/report/{report_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowFirewallReportResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'report_id' in local_var_params:
            path_params['report_id'] = local_var_params['report_id']

        query_params = []
        if 'fw_instance_id' in local_var_params:
            query_params.append(('fw_instance_id', local_var_params['fw_instance_id']))
        if 'report_profile_id' in local_var_params:
            query_params.append(('report_profile_id', local_var_params['report_profile_id']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_report_profile(self, request):
        r"""获取安全报告模板

        获取安全报告模板
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowReportProfile
        :type request: :class:`huaweicloudsdkcfw.v1.ShowReportProfileRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.ShowReportProfileResponse`
        """
        http_info = self._show_report_profile_http_info(request)
        return self._call_api(**http_info)

    def show_report_profile_invoker(self, request):
        http_info = self._show_report_profile_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_report_profile_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/report-profile/{report_profile_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowReportProfileResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'report_profile_id' in local_var_params:
            path_params['report_profile_id'] = local_var_params['report_profile_id']

        query_params = []
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

    def update_report_profile(self, request):
        r"""更新安全报告模板

        更新安全报告模板
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateReportProfile
        :type request: :class:`huaweicloudsdkcfw.v1.UpdateReportProfileRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.UpdateReportProfileResponse`
        """
        http_info = self._update_report_profile_http_info(request)
        return self._call_api(**http_info)

    def update_report_profile_invoker(self, request):
        http_info = self._update_report_profile_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_report_profile_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/report-profile/{report_profile_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateReportProfileResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'report_profile_id' in local_var_params:
            path_params['report_profile_id'] = local_var_params['report_profile_id']

        query_params = []
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

    def change_east_west_firewall_status(self, request):
        r"""更新VPC间防火墙防护状态

        更新VPC间防火墙防护状态
        
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

    def show_ew_associated_er(self, request):
        r"""查询VPC间防火墙使用的企业路由器信息

        查询VPC间防火墙使用的企业路由器信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowEwAssociatedEr
        :type request: :class:`huaweicloudsdkcfw.v1.ShowEwAssociatedErRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.ShowEwAssociatedErResponse`
        """
        http_info = self._show_ew_associated_er_http_info(request)
        return self._call_api(**http_info)

    def show_ew_associated_er_invoker(self, request):
        http_info = self._show_ew_associated_er_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_ew_associated_er_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/firewall/east-west/enterprise-router",
            "request_type": request.__class__.__name__,
            "response_type": "ShowEwAssociatedErResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
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

    def show_ew_associated_vpc(self, request):
        r"""查询VPC边界防火墙使用的引流VPC信息

        查询VPC边界防火墙使用的引流VPC信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowEwAssociatedVpc
        :type request: :class:`huaweicloudsdkcfw.v1.ShowEwAssociatedVpcRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.ShowEwAssociatedVpcResponse`
        """
        http_info = self._show_ew_associated_vpc_http_info(request)
        return self._call_api(**http_info)

    def show_ew_associated_vpc_invoker(self, request):
        http_info = self._show_ew_associated_vpc_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_ew_associated_vpc_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/firewall/east-west/inspection-vpc",
            "request_type": request.__class__.__name__,
            "response_type": "ShowEwAssociatedVpcResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
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

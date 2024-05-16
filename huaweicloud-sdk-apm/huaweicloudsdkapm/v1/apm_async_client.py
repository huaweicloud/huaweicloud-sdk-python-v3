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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkapm'")


class ApmAsyncClient(Client):
    def __init__(self):
        super(ApmAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkapm.v1.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "ApmAsyncClient":
                raise TypeError("client type error, support client type is ApmAsyncClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def create_ak_sk_async(self, request):
        """创建aksk

        创建aksk。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateAkSk
        :type request: :class:`huaweicloudsdkapm.v1.CreateAkSkRequest`
        :rtype: :class:`huaweicloudsdkapm.v1.CreateAkSkResponse`
        """
        http_info = self._create_ak_sk_http_info(request)
        return self._call_api(**http_info)

    def create_ak_sk_async_invoker(self, request):
        http_info = self._create_ak_sk_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_ak_sk_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/apm2/access-keys",
            "request_type": request.__class__.__name__,
            "response_type": "CreateAkSkResponse"
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

    def delete_ak_sk_async(self, request):
        """删除aksk

        删除aksk。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteAkSk
        :type request: :class:`huaweicloudsdkapm.v1.DeleteAkSkRequest`
        :rtype: :class:`huaweicloudsdkapm.v1.DeleteAkSkResponse`
        """
        http_info = self._delete_ak_sk_http_info(request)
        return self._call_api(**http_info)

    def delete_ak_sk_async_invoker(self, request):
        http_info = self._delete_ak_sk_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_ak_sk_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/apm2/access-keys/{ak}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteAkSkResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ak' in local_var_params:
            path_params['ak'] = local_var_params['ak']

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

    def show_ak_sks_async(self, request):
        """查询租户的aksk

        查询租户的aksk。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowAkSks
        :type request: :class:`huaweicloudsdkapm.v1.ShowAkSksRequest`
        :rtype: :class:`huaweicloudsdkapm.v1.ShowAkSksResponse`
        """
        http_info = self._show_ak_sks_http_info(request)
        return self._call_api(**http_info)

    def show_ak_sks_async_invoker(self, request):
        http_info = self._show_ak_sks_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_ak_sks_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/apm2/access-keys",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAkSksResponse"
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

    def list_alarm_data_async(self, request):
        """查询告警列表

        查询系统中存在的告警。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAlarmData
        :type request: :class:`huaweicloudsdkapm.v1.ListAlarmDataRequest`
        :rtype: :class:`huaweicloudsdkapm.v1.ListAlarmDataResponse`
        """
        http_info = self._list_alarm_data_http_info(request)
        return self._call_api(**http_info)

    def list_alarm_data_async_invoker(self, request):
        http_info = self._list_alarm_data_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_alarm_data_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/apm2/openapi/alarm/data/get-alarm-data-list",
            "request_type": request.__class__.__name__,
            "response_type": "ListAlarmDataResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_business_id' in local_var_params:
            header_params['x-business-id'] = local_var_params['x_business_id']

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

    def list_alarm_notify_async(self, request):
        """查询告警消息列表

        查询单个告警的触发详情与历史。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAlarmNotify
        :type request: :class:`huaweicloudsdkapm.v1.ListAlarmNotifyRequest`
        :rtype: :class:`huaweicloudsdkapm.v1.ListAlarmNotifyResponse`
        """
        http_info = self._list_alarm_notify_http_info(request)
        return self._call_api(**http_info)

    def list_alarm_notify_async_invoker(self, request):
        http_info = self._list_alarm_notify_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_alarm_notify_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/apm2/openapi/alarm/data/get-alarm-notify-list",
            "request_type": request.__class__.__name__,
            "response_type": "ListAlarmNotifyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_business_id' in local_var_params:
            header_params['x-business-id'] = local_var_params['x_business_id']

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

    def change_agent_status_async(self, request):
        """更改实例的采集状态

        改变指定实例的采集状态：开启和关闭。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ChangeAgentStatus
        :type request: :class:`huaweicloudsdkapm.v1.ChangeAgentStatusRequest`
        :rtype: :class:`huaweicloudsdkapm.v1.ChangeAgentStatusResponse`
        """
        http_info = self._change_agent_status_http_info(request)
        return self._call_api(**http_info)

    def change_agent_status_async_invoker(self, request):
        http_info = self._change_agent_status_http_info(request)
        return AsyncInvoker(self, http_info)

    def _change_agent_status_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/apm2/openapi/apm-service/agent-mgr/change-status",
            "request_type": request.__class__.__name__,
            "response_type": "ChangeAgentStatusResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_business_id' in local_var_params:
            header_params['x-business-id'] = local_var_params['x_business_id']

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

    def delete_agent_async(self, request):
        """删除agent

        删除agent
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteAgent
        :type request: :class:`huaweicloudsdkapm.v1.DeleteAgentRequest`
        :rtype: :class:`huaweicloudsdkapm.v1.DeleteAgentResponse`
        """
        http_info = self._delete_agent_http_info(request)
        return self._call_api(**http_info)

    def delete_agent_async_invoker(self, request):
        http_info = self._delete_agent_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_agent_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/apm2/openapi/apm-service/agent-mgr/delete-agent",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteAgentResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_business_id' in local_var_params:
            header_params['x-business-id'] = local_var_params['x_business_id']

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

    def list_ak_sk_async(self, request):
        """获取ak/sk

        获取该用户创建的ak/sk列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAkSk
        :type request: :class:`huaweicloudsdkapm.v1.ListAkSkRequest`
        :rtype: :class:`huaweicloudsdkapm.v1.ListAkSkResponse`
        """
        http_info = self._list_ak_sk_http_info(request)
        return self._call_api(**http_info)

    def list_ak_sk_async_invoker(self, request):
        http_info = self._list_ak_sk_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_ak_sk_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/apm2/openapi/systemmng/get-ak-sk-list",
            "request_type": request.__class__.__name__,
            "response_type": "ListAkSkResponse"
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

    def list_business_async(self, request):
        """查询应用列表

        该接口用于查询对应用户下的应用。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListBusiness
        :type request: :class:`huaweicloudsdkapm.v1.ListBusinessRequest`
        :rtype: :class:`huaweicloudsdkapm.v1.ListBusinessResponse`
        """
        http_info = self._list_business_http_info(request)
        return self._call_api(**http_info)

    def list_business_async_invoker(self, request):
        http_info = self._list_business_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_business_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/apm2/openapi/cmdb/business/get-business-list",
            "request_type": request.__class__.__name__,
            "response_type": "ListBusinessResponse"
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

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_env_monitor_item_async(self, request):
        """查询监控项列表

        查询监控项列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListEnvMonitorItem
        :type request: :class:`huaweicloudsdkapm.v1.ListEnvMonitorItemRequest`
        :rtype: :class:`huaweicloudsdkapm.v1.ListEnvMonitorItemResponse`
        """
        http_info = self._list_env_monitor_item_http_info(request)
        return self._call_api(**http_info)

    def list_env_monitor_item_async_invoker(self, request):
        http_info = self._list_env_monitor_item_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_env_monitor_item_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/apm2/openapi/apm-service/monitor-item-mgr/get-env-monitor-item-list",
            "request_type": request.__class__.__name__,
            "response_type": "ListEnvMonitorItemResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_business_id' in local_var_params:
            header_params['x-business-id'] = local_var_params['x_business_id']

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

    def save_monitor_item_config_async(self, request):
        """保存监控项

        保存监控项。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for SaveMonitorItemConfig
        :type request: :class:`huaweicloudsdkapm.v1.SaveMonitorItemConfigRequest`
        :rtype: :class:`huaweicloudsdkapm.v1.SaveMonitorItemConfigResponse`
        """
        http_info = self._save_monitor_item_config_http_info(request)
        return self._call_api(**http_info)

    def save_monitor_item_config_async_invoker(self, request):
        http_info = self._save_monitor_item_config_http_info(request)
        return AsyncInvoker(self, http_info)

    def _save_monitor_item_config_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/apm2/openapi/apm-service/monitor-item-mgr/save-monitor-item-config",
            "request_type": request.__class__.__name__,
            "response_type": "SaveMonitorItemConfigResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_business_id' in local_var_params:
            header_params['x-business-id'] = local_var_params['x_business_id']

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

    def search_agent_async(self, request):
        """查询应用下所有探针

        该接口用于搜索应用下所有探针情况。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for SearchAgent
        :type request: :class:`huaweicloudsdkapm.v1.SearchAgentRequest`
        :rtype: :class:`huaweicloudsdkapm.v1.SearchAgentResponse`
        """
        http_info = self._search_agent_http_info(request)
        return self._call_api(**http_info)

    def search_agent_async_invoker(self, request):
        http_info = self._search_agent_http_info(request)
        return AsyncInvoker(self, http_info)

    def _search_agent_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/apm2/openapi/apm-service/agent-mgr/search",
            "request_type": request.__class__.__name__,
            "response_type": "SearchAgentResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_business_id' in local_var_params:
            header_params['x-business-id'] = local_var_params['x_business_id']

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

    def search_application_async(self, request):
        """对指定区域下的组件和环境及其探针情况进行搜索

        对指定区域下的组件和环境及其探针情况进行搜索。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for SearchApplication
        :type request: :class:`huaweicloudsdkapm.v1.SearchApplicationRequest`
        :rtype: :class:`huaweicloudsdkapm.v1.SearchApplicationResponse`
        """
        http_info = self._search_application_http_info(request)
        return self._call_api(**http_info)

    def search_application_async_invoker(self, request):
        http_info = self._search_application_http_info(request)
        return AsyncInvoker(self, http_info)

    def _search_application_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/apm2/openapi/apm-service/app-mgr/search",
            "request_type": request.__class__.__name__,
            "response_type": "SearchApplicationResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_business_id' in local_var_params:
            header_params['x-business-id'] = local_var_params['x_business_id']

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

    def show_master_address_async(self, request):
        """查询master地址

        根据region名称获取该region下的master服务podlb地址信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowMasterAddress
        :type request: :class:`huaweicloudsdkapm.v1.ShowMasterAddressRequest`
        :rtype: :class:`huaweicloudsdkapm.v1.ShowMasterAddressResponse`
        """
        http_info = self._show_master_address_http_info(request)
        return self._call_api(**http_info)

    def show_master_address_async_invoker(self, request):
        http_info = self._show_master_address_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_master_address_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/apm2/openapi/systemmng/get-master-address",
            "request_type": request.__class__.__name__,
            "response_type": "ShowMasterAddressResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'region_name' in local_var_params:
            query_params.append(('region_name', local_var_params['region_name']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_app_async(self, request):
        """根据组件id删除指定的组件

        该接口用于删除指定的组件。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteApp
        :type request: :class:`huaweicloudsdkapm.v1.DeleteAppRequest`
        :rtype: :class:`huaweicloudsdkapm.v1.DeleteAppResponse`
        """
        http_info = self._delete_app_http_info(request)
        return self._call_api(**http_info)

    def delete_app_async_invoker(self, request):
        http_info = self._delete_app_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_app_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/apm2/openapi/cmdb/apps/delete-app/{application_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteAppResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'application_id' in local_var_params:
            path_params['application_id'] = local_var_params['application_id']

        query_params = []

        header_params = {}
        if 'x_business_id' in local_var_params:
            header_params['x-business-id'] = local_var_params['x_business_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_app_envs_async(self, request):
        """获取组件下的环境列表

        获取组件下的环境列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAppEnvs
        :type request: :class:`huaweicloudsdkapm.v1.ListAppEnvsRequest`
        :rtype: :class:`huaweicloudsdkapm.v1.ListAppEnvsResponse`
        """
        http_info = self._list_app_envs_http_info(request)
        return self._call_api(**http_info)

    def list_app_envs_async_invoker(self, request):
        http_info = self._list_app_envs_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_app_envs_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/apm2/openapi/cmdb/envs/get-app-envs",
            "request_type": request.__class__.__name__,
            "response_type": "ListAppEnvsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'app_id' in local_var_params:
            query_params.append(('app_id', local_var_params['app_id']))

        header_params = {}
        if 'x_business_id' in local_var_params:
            header_params['x-business-id'] = local_var_params['x_business_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_apps_async(self, request):
        """获取组件列表

        获取组件列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListApps
        :type request: :class:`huaweicloudsdkapm.v1.ListAppsRequest`
        :rtype: :class:`huaweicloudsdkapm.v1.ListAppsResponse`
        """
        http_info = self._list_apps_http_info(request)
        return self._call_api(**http_info)

    def list_apps_async_invoker(self, request):
        http_info = self._list_apps_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_apps_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/apm2/openapi/cmdb/apps/get-apps",
            "request_type": request.__class__.__name__,
            "response_type": "ListAppsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'business_id' in local_var_params:
            query_params.append(('business_id', local_var_params['business_id']))

        header_params = {}
        if 'x_business_id' in local_var_params:
            header_params['x-business-id'] = local_var_params['x_business_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_env_tags_async(self, request):
        """查询环境标签

        查询环境标签接口。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListEnvTags
        :type request: :class:`huaweicloudsdkapm.v1.ListEnvTagsRequest`
        :rtype: :class:`huaweicloudsdkapm.v1.ListEnvTagsResponse`
        """
        http_info = self._list_env_tags_http_info(request)
        return self._call_api(**http_info)

    def list_env_tags_async_invoker(self, request):
        http_info = self._list_env_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_env_tags_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/apm2/openapi/cmdb/tag/get-env-tag-list",
            "request_type": request.__class__.__name__,
            "response_type": "ListEnvTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_business_id' in local_var_params:
            header_params['x-business-id'] = local_var_params['x_business_id']

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

    def show_business_detail_async(self, request):
        """查询单个应用的详情

        查询单个应用的详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowBusinessDetail
        :type request: :class:`huaweicloudsdkapm.v1.ShowBusinessDetailRequest`
        :rtype: :class:`huaweicloudsdkapm.v1.ShowBusinessDetailResponse`
        """
        http_info = self._show_business_detail_http_info(request)
        return self._call_api(**http_info)

    def show_business_detail_async_invoker(self, request):
        http_info = self._show_business_detail_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_business_detail_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/apm2/openapi/cmdb/business/get-business-detail/{business_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowBusinessDetailResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'business_id' in local_var_params:
            path_params['business_id'] = local_var_params['business_id']

        query_params = []

        header_params = {}
        if 'x_business_id' in local_var_params:
            header_params['x-business-id'] = local_var_params['x_business_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_sub_business_detail_async(self, request):
        """查询子应用详情

        查询单个子应用详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowSubBusinessDetail
        :type request: :class:`huaweicloudsdkapm.v1.ShowSubBusinessDetailRequest`
        :rtype: :class:`huaweicloudsdkapm.v1.ShowSubBusinessDetailResponse`
        """
        http_info = self._show_sub_business_detail_http_info(request)
        return self._call_api(**http_info)

    def show_sub_business_detail_async_invoker(self, request):
        http_info = self._show_sub_business_detail_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_sub_business_detail_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/apm2/openapi/cmdb/sub-business/get-sub-business-detail/{sub_business_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowSubBusinessDetailResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'sub_business_id' in local_var_params:
            path_params['sub_business_id'] = local_var_params['sub_business_id']

        query_params = []

        header_params = {}
        if 'x_business_id' in local_var_params:
            header_params['x-business-id'] = local_var_params['x_business_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_topology_tree_async(self, request):
        """获取应用树

        获取应用树。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowTopologyTree
        :type request: :class:`huaweicloudsdkapm.v1.ShowTopologyTreeRequest`
        :rtype: :class:`huaweicloudsdkapm.v1.ShowTopologyTreeResponse`
        """
        http_info = self._show_topology_tree_http_info(request)
        return self._call_api(**http_info)

    def show_topology_tree_async_invoker(self, request):
        http_info = self._show_topology_tree_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_topology_tree_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/apm2/openapi/cmdb/topology-trees/get-topology-trees",
            "request_type": request.__class__.__name__,
            "response_type": "ShowTopologyTreeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'region_id' in local_var_params:
            query_params.append(('region_id', local_var_params['region_id']))
        if 'business_id' in local_var_params:
            query_params.append(('business_id', local_var_params['business_id']))
        if 'env_tag_id' in local_var_params:
            query_params.append(('env_tag_id', local_var_params['env_tag_id']))
        if 'env_keyword' in local_var_params:
            query_params.append(('env_keyword', local_var_params['env_keyword']))

        header_params = {}
        if 'x_business_id' in local_var_params:
            header_params['x-business-id'] = local_var_params['x_business_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_flame_line_tree_async(self, request):
        """show_flame_line_tree

        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowFlameLineTree
        :type request: :class:`huaweicloudsdkapm.v1.ShowFlameLineTreeRequest`
        :rtype: :class:`huaweicloudsdkapm.v1.ShowFlameLineTreeResponse`
        """
        http_info = self._show_flame_line_tree_http_info(request)
        return self._call_api(**http_info)

    def show_flame_line_tree_async_invoker(self, request):
        http_info = self._show_flame_line_tree_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_flame_line_tree_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/apm2/openapi/view/profiling/flame-line-tree",
            "request_type": request.__class__.__name__,
            "response_type": "ShowFlameLineTreeResponse"
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

    def list_open_region_async(self, request):
        """查询开通的region

        该接口用于查询用户开通的region信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListOpenRegion
        :type request: :class:`huaweicloudsdkapm.v1.ListOpenRegionRequest`
        :rtype: :class:`huaweicloudsdkapm.v1.ListOpenRegionResponse`
        """
        http_info = self._list_open_region_http_info(request)
        return self._call_api(**http_info)

    def list_open_region_async_invoker(self, request):
        http_info = self._list_open_region_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_open_region_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/apm2/openapi/region/get-opened-region",
            "request_type": request.__class__.__name__,
            "response_type": "ListOpenRegionResponse"
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

    def list_supported_region_async(self, request):
        """查询所有的支持的region

        查询所有的支持的region信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListSupportedRegion
        :type request: :class:`huaweicloudsdkapm.v1.ListSupportedRegionRequest`
        :rtype: :class:`huaweicloudsdkapm.v1.ListSupportedRegionResponse`
        """
        http_info = self._list_supported_region_http_info(request)
        return self._call_api(**http_info)

    def list_supported_region_async_invoker(self, request):
        http_info = self._list_supported_region_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_supported_region_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/apm2/openapi/region/get-all-supported-region",
            "request_type": request.__class__.__name__,
            "response_type": "ListSupportedRegionResponse"
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

    def search_business_topology_async(self, request):
        """查询应用全局拓扑图

        查询应用级别全局拓扑图信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for SearchBusinessTopology
        :type request: :class:`huaweicloudsdkapm.v1.SearchBusinessTopologyRequest`
        :rtype: :class:`huaweicloudsdkapm.v1.SearchBusinessTopologyResponse`
        """
        http_info = self._search_business_topology_http_info(request)
        return self._call_api(**http_info)

    def search_business_topology_async_invoker(self, request):
        http_info = self._search_business_topology_http_info(request)
        return AsyncInvoker(self, http_info)

    def _search_business_topology_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/apm2/openapi/topology/business-search",
            "request_type": request.__class__.__name__,
            "response_type": "SearchBusinessTopologyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_business_id' in local_var_params:
            header_params['x-business-id'] = local_var_params['x_business_id']

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

    def search_env_topology_async(self, request):
        """查询组件环境拓扑图

        查询组件环境级别全局拓扑图信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for SearchEnvTopology
        :type request: :class:`huaweicloudsdkapm.v1.SearchEnvTopologyRequest`
        :rtype: :class:`huaweicloudsdkapm.v1.SearchEnvTopologyResponse`
        """
        http_info = self._search_env_topology_http_info(request)
        return self._call_api(**http_info)

    def search_env_topology_async_invoker(self, request):
        http_info = self._search_env_topology_http_info(request)
        return AsyncInvoker(self, http_info)

    def _search_env_topology_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/apm2/openapi/topology/env-search",
            "request_type": request.__class__.__name__,
            "response_type": "SearchEnvTopologyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_business_id' in local_var_params:
            header_params['x-business-id'] = local_var_params['x_business_id']

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

    def create_business_async(self, request):
        """创建链路追踪应用

        创建链路追踪应用
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateBusiness
        :type request: :class:`huaweicloudsdkapm.v1.CreateBusinessRequest`
        :rtype: :class:`huaweicloudsdkapm.v1.CreateBusinessResponse`
        """
        http_info = self._create_business_http_info(request)
        return self._call_api(**http_info)

    def create_business_async_invoker(self, request):
        http_info = self._create_business_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_business_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/apm2/openapi/tracing/business/create",
            "request_type": request.__class__.__name__,
            "response_type": "CreateBusinessResponse"
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

    def show_access_point_async(self, request):
        """获取链路追踪应用接入地址

        获取链路追踪应用接入地址
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowAccessPoint
        :type request: :class:`huaweicloudsdkapm.v1.ShowAccessPointRequest`
        :rtype: :class:`huaweicloudsdkapm.v1.ShowAccessPointResponse`
        """
        http_info = self._show_access_point_http_info(request)
        return self._call_api(**http_info)

    def show_access_point_async_invoker(self, request):
        http_info = self._show_access_point_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_access_point_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/apm2/openapi/tracing/access/get-access-point/{business_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAccessPointResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'business_id' in local_var_params:
            path_params['business_id'] = local_var_params['business_id']

        query_params = []

        header_params = {}
        if 'x_business_id' in local_var_params:
            header_params['x-business-id'] = local_var_params['x_business_id']

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

    def show_token_async(self, request):
        """获取链路追踪应用的token

        获取链路追踪应用的token
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowToken
        :type request: :class:`huaweicloudsdkapm.v1.ShowTokenRequest`
        :rtype: :class:`huaweicloudsdkapm.v1.ShowTokenResponse`
        """
        http_info = self._show_token_http_info(request)
        return self._call_api(**http_info)

    def show_token_async_invoker(self, request):
        http_info = self._show_token_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_token_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/apm2/openapi/tracing/business/token/{business_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowTokenResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'business_id' in local_var_params:
            path_params['business_id'] = local_var_params['business_id']

        query_params = []

        header_params = {}
        if 'x_business_id' in local_var_params:
            header_params['x-business-id'] = local_var_params['x_business_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_business_env_async(self, request):
        """查询URL跟踪Region环境列表

        查询所选Region下设置了URL跟踪的环境列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListBusinessEnv
        :type request: :class:`huaweicloudsdkapm.v1.ListBusinessEnvRequest`
        :rtype: :class:`huaweicloudsdkapm.v1.ListBusinessEnvResponse`
        """
        http_info = self._list_business_env_http_info(request)
        return self._call_api(**http_info)

    def list_business_env_async_invoker(self, request):
        http_info = self._list_business_env_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_business_env_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/apm2/openapi/transaction/business-env",
            "request_type": request.__class__.__name__,
            "response_type": "ListBusinessEnvResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_business_id' in local_var_params:
            header_params['x-business-id'] = local_var_params['x_business_id']

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

    def search_transaction_async(self, request):
        """查询URL跟踪视图列表

        查询当前被调用的URL跟踪视图列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for SearchTransaction
        :type request: :class:`huaweicloudsdkapm.v1.SearchTransactionRequest`
        :rtype: :class:`huaweicloudsdkapm.v1.SearchTransactionResponse`
        """
        http_info = self._search_transaction_http_info(request)
        return self._call_api(**http_info)

    def search_transaction_async_invoker(self, request):
        http_info = self._search_transaction_http_info(request)
        return AsyncInvoker(self, http_info)

    def _search_transaction_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/apm2/openapi/transaction/search",
            "request_type": request.__class__.__name__,
            "response_type": "SearchTransactionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_business_id' in local_var_params:
            header_params['x-business-id'] = local_var_params['x_business_id']

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

    def search_transaction_config_async(self, request):
        """查询URL跟踪配置列表

        查询已配置好的URL跟踪配置列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for SearchTransactionConfig
        :type request: :class:`huaweicloudsdkapm.v1.SearchTransactionConfigRequest`
        :rtype: :class:`huaweicloudsdkapm.v1.SearchTransactionConfigResponse`
        """
        http_info = self._search_transaction_config_http_info(request)
        return self._call_api(**http_info)

    def search_transaction_config_async_invoker(self, request):
        http_info = self._search_transaction_config_http_info(request)
        return AsyncInvoker(self, http_info)

    def _search_transaction_config_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/apm2/openapi/transaction/transaction-config-search",
            "request_type": request.__class__.__name__,
            "response_type": "SearchTransactionConfigResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_business_id' in local_var_params:
            header_params['x-business-id'] = local_var_params['x_business_id']

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

    def show_transaction_detail_async(self, request):
        """查询URL跟踪视图详情

        查询某条URL跟踪视图详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowTransactionDetail
        :type request: :class:`huaweicloudsdkapm.v1.ShowTransactionDetailRequest`
        :rtype: :class:`huaweicloudsdkapm.v1.ShowTransactionDetailResponse`
        """
        http_info = self._show_transaction_detail_http_info(request)
        return self._call_api(**http_info)

    def show_transaction_detail_async_invoker(self, request):
        http_info = self._show_transaction_detail_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_transaction_detail_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/apm2/openapi/transaction/detail",
            "request_type": request.__class__.__name__,
            "response_type": "ShowTransactionDetailResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_business_id' in local_var_params:
            header_params['x-business-id'] = local_var_params['x_business_id']

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

    def list_env_instances_async(self, request):
        """获取实例信息列表

        获取实例信息列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListEnvInstances
        :type request: :class:`huaweicloudsdkapm.v1.ListEnvInstancesRequest`
        :rtype: :class:`huaweicloudsdkapm.v1.ListEnvInstancesResponse`
        """
        http_info = self._list_env_instances_http_info(request)
        return self._call_api(**http_info)

    def list_env_instances_async_invoker(self, request):
        http_info = self._list_env_instances_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_env_instances_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/apm2/openapi/view/mainview/get-env-instance-list",
            "request_type": request.__class__.__name__,
            "response_type": "ListEnvInstancesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_business_id' in local_var_params:
            header_params['x-business-id'] = local_var_params['x_business_id']

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

    def show_clob_detail_async(self, request):
        """获取原始数据详情

        获取原始数据详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowClobDetail
        :type request: :class:`huaweicloudsdkapm.v1.ShowClobDetailRequest`
        :rtype: :class:`huaweicloudsdkapm.v1.ShowClobDetailResponse`
        """
        http_info = self._show_clob_detail_http_info(request)
        return self._call_api(**http_info)

    def show_clob_detail_async_invoker(self, request):
        http_info = self._show_clob_detail_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_clob_detail_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/apm2/openapi/view/metric/get-clob-detail",
            "request_type": request.__class__.__name__,
            "response_type": "ShowClobDetailResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_business_id' in local_var_params:
            header_params['x-business-id'] = local_var_params['x_business_id']

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

    def show_env_monitor_items_async(self, request):
        """获取监控项信息

        获取监控项信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowEnvMonitorItems
        :type request: :class:`huaweicloudsdkapm.v1.ShowEnvMonitorItemsRequest`
        :rtype: :class:`huaweicloudsdkapm.v1.ShowEnvMonitorItemsResponse`
        """
        http_info = self._show_env_monitor_items_http_info(request)
        return self._call_api(**http_info)

    def show_env_monitor_items_async_invoker(self, request):
        http_info = self._show_env_monitor_items_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_env_monitor_items_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/apm2/openapi/view/mainview/get-env-monitor-item-list",
            "request_type": request.__class__.__name__,
            "response_type": "ShowEnvMonitorItemsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'env_id' in local_var_params:
            query_params.append(('env_id', local_var_params['env_id']))

        header_params = {}
        if 'x_business_id' in local_var_params:
            header_params['x-business-id'] = local_var_params['x_business_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_event_detail_async(self, request):
        """获取event的详情

        获取event的详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowEventDetail
        :type request: :class:`huaweicloudsdkapm.v1.ShowEventDetailRequest`
        :rtype: :class:`huaweicloudsdkapm.v1.ShowEventDetailResponse`
        """
        http_info = self._show_event_detail_http_info(request)
        return self._call_api(**http_info)

    def show_event_detail_async_invoker(self, request):
        http_info = self._show_event_detail_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_event_detail_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/apm2/openapi/view/trace/get-event-detail",
            "request_type": request.__class__.__name__,
            "response_type": "ShowEventDetailResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'trace_id' in local_var_params:
            query_params.append(('trace_id', local_var_params['trace_id']))
        if 'span_id' in local_var_params:
            query_params.append(('span_id', local_var_params['span_id']))
        if 'event_id' in local_var_params:
            query_params.append(('event_id', local_var_params['event_id']))
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

    def show_monitor_item_detail_async(self, request):
        """获取一个监控项的详情

        获取一个监控项的详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowMonitorItemDetail
        :type request: :class:`huaweicloudsdkapm.v1.ShowMonitorItemDetailRequest`
        :rtype: :class:`huaweicloudsdkapm.v1.ShowMonitorItemDetailResponse`
        """
        http_info = self._show_monitor_item_detail_http_info(request)
        return self._call_api(**http_info)

    def show_monitor_item_detail_async_invoker(self, request):
        http_info = self._show_monitor_item_detail_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_monitor_item_detail_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/apm2/openapi/apm-service/monitor-item-mgr/get-monitor-item-detail",
            "request_type": request.__class__.__name__,
            "response_type": "ShowMonitorItemDetailResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'monitor_item_id' in local_var_params:
            query_params.append(('monitor_item_id', local_var_params['monitor_item_id']))
        if 'env_id' in local_var_params:
            query_params.append(('env_id', local_var_params['env_id']))

        header_params = {}
        if 'x_business_id' in local_var_params:
            header_params['x-business-id'] = local_var_params['x_business_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_monitor_item_view_config_async(self, request):
        """查询监控项配置信息

        查询监控项配置信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowMonitorItemViewConfig
        :type request: :class:`huaweicloudsdkapm.v1.ShowMonitorItemViewConfigRequest`
        :rtype: :class:`huaweicloudsdkapm.v1.ShowMonitorItemViewConfigResponse`
        """
        http_info = self._show_monitor_item_view_config_http_info(request)
        return self._call_api(**http_info)

    def show_monitor_item_view_config_async_invoker(self, request):
        http_info = self._show_monitor_item_view_config_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_monitor_item_view_config_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/apm2/openapi/view/config/get-monitor-item-view-config",
            "request_type": request.__class__.__name__,
            "response_type": "ShowMonitorItemViewConfigResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'env_id' in local_var_params:
            query_params.append(('env_id', local_var_params['env_id']))
        if 'collector_id' in local_var_params:
            query_params.append(('collector_id', local_var_params['collector_id']))

        header_params = {}
        if 'x_business_id' in local_var_params:
            header_params['x-business-id'] = local_var_params['x_business_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_raw_table_async(self, request):
        """获取原始数据表格

        获取原始数据表格。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowRawTable
        :type request: :class:`huaweicloudsdkapm.v1.ShowRawTableRequest`
        :rtype: :class:`huaweicloudsdkapm.v1.ShowRawTableResponse`
        """
        http_info = self._show_raw_table_http_info(request)
        return self._call_api(**http_info)

    def show_raw_table_async_invoker(self, request):
        http_info = self._show_raw_table_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_raw_table_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/apm2/openapi/view/metric/raw-table",
            "request_type": request.__class__.__name__,
            "response_type": "ShowRawTableResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_business_id' in local_var_params:
            header_params['x-business-id'] = local_var_params['x_business_id']

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

    def show_span_search_async(self, request):
        """查询span数据

        span数据查询接口。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowSpanSearch
        :type request: :class:`huaweicloudsdkapm.v1.ShowSpanSearchRequest`
        :rtype: :class:`huaweicloudsdkapm.v1.ShowSpanSearchResponse`
        """
        http_info = self._show_span_search_http_info(request)
        return self._call_api(**http_info)

    def show_span_search_async_invoker(self, request):
        http_info = self._show_span_search_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_span_search_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/apm2/openapi/view/trace/span-search",
            "request_type": request.__class__.__name__,
            "response_type": "ShowSpanSearchResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_business_id' in local_var_params:
            header_params['x-business-id'] = local_var_params['x_business_id']

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

    def show_sum_table_async(self, request):
        """获取汇总表格数据

        获取汇总表格数据。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowSumTable
        :type request: :class:`huaweicloudsdkapm.v1.ShowSumTableRequest`
        :rtype: :class:`huaweicloudsdkapm.v1.ShowSumTableResponse`
        """
        http_info = self._show_sum_table_http_info(request)
        return self._call_api(**http_info)

    def show_sum_table_async_invoker(self, request):
        http_info = self._show_sum_table_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_sum_table_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/apm2/openapi/view/metric/sum-table",
            "request_type": request.__class__.__name__,
            "response_type": "ShowSumTableResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_business_id' in local_var_params:
            header_params['x-business-id'] = local_var_params['x_business_id']

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

    def show_topology_async(self, request):
        """调用链拓扑图

        调用链拓扑图。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowTopology
        :type request: :class:`huaweicloudsdkapm.v1.ShowTopologyRequest`
        :rtype: :class:`huaweicloudsdkapm.v1.ShowTopologyResponse`
        """
        http_info = self._show_topology_http_info(request)
        return self._call_api(**http_info)

    def show_topology_async_invoker(self, request):
        http_info = self._show_topology_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_topology_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/apm2/openapi/view/trace/topology",
            "request_type": request.__class__.__name__,
            "response_type": "ShowTopologyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'trace_id' in local_var_params:
            query_params.append(('trace_id', local_var_params['trace_id']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_trace_events_async(self, request):
        """获取一个trace的所有调用链数据

        获取一个trace的所有调用链数据。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowTraceEvents
        :type request: :class:`huaweicloudsdkapm.v1.ShowTraceEventsRequest`
        :rtype: :class:`huaweicloudsdkapm.v1.ShowTraceEventsResponse`
        """
        http_info = self._show_trace_events_http_info(request)
        return self._call_api(**http_info)

    def show_trace_events_async_invoker(self, request):
        http_info = self._show_trace_events_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_trace_events_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/apm2/openapi/view/trace/get-trace-events",
            "request_type": request.__class__.__name__,
            "response_type": "ShowTraceEventsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'trace_id' in local_var_params:
            query_params.append(('trace_id', local_var_params['trace_id']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_trend_async(self, request):
        """获取趋势图

        获取趋势图。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowTrend
        :type request: :class:`huaweicloudsdkapm.v1.ShowTrendRequest`
        :rtype: :class:`huaweicloudsdkapm.v1.ShowTrendResponse`
        """
        http_info = self._show_trend_http_info(request)
        return self._call_api(**http_info)

    def show_trend_async_invoker(self, request):
        http_info = self._show_trend_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_trend_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/apm2/openapi/view/metric/trend",
            "request_type": request.__class__.__name__,
            "response_type": "ShowTrendResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_business_id' in local_var_params:
            header_params['x-business-id'] = local_var_params['x_business_id']

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

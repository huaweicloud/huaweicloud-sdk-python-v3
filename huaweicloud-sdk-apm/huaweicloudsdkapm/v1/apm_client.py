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


class ApmClient(Client):
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
        super(ApmClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkapm.v1.model")
        self.preset_headers = {'User-Agent': 'HuaweiCloud-SDK-Python'}

    @classmethod
    def new_builder(cls, clazz=None):
        if clazz is None:
            return ClientBuilder(cls)

        if clazz.__name__ != "ApmClient":
            raise TypeError("client type error, support client type is ApmClient")

        return ClientBuilder(clazz)

    def create_ak_sk(self, request):
        """创建aksk

        创建aksk。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateAkSk
        :type request: :class:`huaweicloudsdkapm.v1.CreateAkSkRequest`
        :rtype: :class:`huaweicloudsdkapm.v1.CreateAkSkResponse`
        """
        return self.create_ak_sk_with_http_info(request)

    def create_ak_sk_with_http_info(self, request):
        all_params = ['create_aksk_model']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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

        auth_settings = []

        return self.call_api(
            resource_path='/v1/apm2/access-keys',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateAkSkResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_ak_sk(self, request):
        """删除aksk

        删除aksk。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteAkSk
        :type request: :class:`huaweicloudsdkapm.v1.DeleteAkSkRequest`
        :rtype: :class:`huaweicloudsdkapm.v1.DeleteAkSkResponse`
        """
        return self.delete_ak_sk_with_http_info(request)

    def delete_ak_sk_with_http_info(self, request):
        all_params = ['ak']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ak' in local_var_params:
            path_params['ak'] = local_var_params['ak']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/apm2/access-keys/{ak}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteAkSkResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_ak_sks(self, request):
        """查询租户的aksk

        查询租户的aksk。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAkSks
        :type request: :class:`huaweicloudsdkapm.v1.ShowAkSksRequest`
        :rtype: :class:`huaweicloudsdkapm.v1.ShowAkSksResponse`
        """
        return self.show_ak_sks_with_http_info(request)

    def show_ak_sks_with_http_info(self, request):
        all_params = []
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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

        auth_settings = []

        return self.call_api(
            resource_path='/v1/apm2/access-keys',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowAkSksResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_alarm_data(self, request):
        """查询告警列表

        查询系统中存在的告警。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAlarmData
        :type request: :class:`huaweicloudsdkapm.v1.ListAlarmDataRequest`
        :rtype: :class:`huaweicloudsdkapm.v1.ListAlarmDataResponse`
        """
        return self.list_alarm_data_with_http_info(request)

    def list_alarm_data_with_http_info(self, request):
        all_params = ['x_business_id', 'alarm_data_list_request']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_business_id' in local_var_params:
            header_params['x-business-id'] = local_var_params['x_business_id']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/apm2/openapi/alarm/data/get-alarm-data-list',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListAlarmDataResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_alarm_notify(self, request):
        """查询告警消息列表

        查询单个告警的触发详情与历史。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAlarmNotify
        :type request: :class:`huaweicloudsdkapm.v1.ListAlarmNotifyRequest`
        :rtype: :class:`huaweicloudsdkapm.v1.ListAlarmNotifyResponse`
        """
        return self.list_alarm_notify_with_http_info(request)

    def list_alarm_notify_with_http_info(self, request):
        all_params = ['x_business_id', 'alarm_notify_list_request']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_business_id' in local_var_params:
            header_params['x-business-id'] = local_var_params['x_business_id']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/apm2/openapi/alarm/data/get-alarm-notify-list',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListAlarmNotifyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def change_agent_status(self, request):
        """更改实例的采集状态

        改变指定实例的采集状态：开启和关闭。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ChangeAgentStatus
        :type request: :class:`huaweicloudsdkapm.v1.ChangeAgentStatusRequest`
        :rtype: :class:`huaweicloudsdkapm.v1.ChangeAgentStatusResponse`
        """
        return self.change_agent_status_with_http_info(request)

    def change_agent_status_with_http_info(self, request):
        all_params = ['x_business_id', 'agent_status_change_param']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_business_id' in local_var_params:
            header_params['x-business-id'] = local_var_params['x_business_id']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/apm2/openapi/apm-service/agent-mgr/change-status',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ChangeAgentStatusResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_agent(self, request):
        """删除agent

        删除agent
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteAgent
        :type request: :class:`huaweicloudsdkapm.v1.DeleteAgentRequest`
        :rtype: :class:`huaweicloudsdkapm.v1.DeleteAgentResponse`
        """
        return self.delete_agent_with_http_info(request)

    def delete_agent_with_http_info(self, request):
        all_params = ['x_business_id', 'agent_delete_param']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_business_id' in local_var_params:
            header_params['x-business-id'] = local_var_params['x_business_id']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/apm2/openapi/apm-service/agent-mgr/delete-agent',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteAgentResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_ak_sk(self, request):
        """获取ak/sk

        获取该用户创建的ak/sk列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAkSk
        :type request: :class:`huaweicloudsdkapm.v1.ListAkSkRequest`
        :rtype: :class:`huaweicloudsdkapm.v1.ListAkSkResponse`
        """
        return self.list_ak_sk_with_http_info(request)

    def list_ak_sk_with_http_info(self, request):
        all_params = []
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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

        auth_settings = []

        return self.call_api(
            resource_path='/v1/apm2/openapi/systemmng/get-ak-sk-list',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListAkSkResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_business(self, request):
        """查询应用列表

        该接口用于查询对应用户下的应用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListBusiness
        :type request: :class:`huaweicloudsdkapm.v1.ListBusinessRequest`
        :rtype: :class:`huaweicloudsdkapm.v1.ListBusinessResponse`
        """
        return self.list_business_with_http_info(request)

    def list_business_with_http_info(self, request):
        all_params = []
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v1/apm2/openapi/cmdb/business/get-business-list',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListBusinessResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_env_monitor_item(self, request):
        """查询监控项列表

        查询监控项列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListEnvMonitorItem
        :type request: :class:`huaweicloudsdkapm.v1.ListEnvMonitorItemRequest`
        :rtype: :class:`huaweicloudsdkapm.v1.ListEnvMonitorItemResponse`
        """
        return self.list_env_monitor_item_with_http_info(request)

    def list_env_monitor_item_with_http_info(self, request):
        all_params = ['x_business_id', 'get_env_monitor_item_list_param']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_business_id' in local_var_params:
            header_params['x-business-id'] = local_var_params['x_business_id']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/apm2/openapi/apm-service/monitor-item-mgr/get-env-monitor-item-list',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListEnvMonitorItemResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def save_monitor_item_config(self, request):
        """保存监控项

        保存监控项。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SaveMonitorItemConfig
        :type request: :class:`huaweicloudsdkapm.v1.SaveMonitorItemConfigRequest`
        :rtype: :class:`huaweicloudsdkapm.v1.SaveMonitorItemConfigResponse`
        """
        return self.save_monitor_item_config_with_http_info(request)

    def save_monitor_item_config_with_http_info(self, request):
        all_params = ['x_business_id', 'save_monitor_item_param']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_business_id' in local_var_params:
            header_params['x-business-id'] = local_var_params['x_business_id']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/apm2/openapi/apm-service/monitor-item-mgr/save-monitor-item-config',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='SaveMonitorItemConfigResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def search_agent(self, request):
        """查询应用下所有探针

        该接口用于搜索应用下所有探针情况。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SearchAgent
        :type request: :class:`huaweicloudsdkapm.v1.SearchAgentRequest`
        :rtype: :class:`huaweicloudsdkapm.v1.SearchAgentResponse`
        """
        return self.search_agent_with_http_info(request)

    def search_agent_with_http_info(self, request):
        all_params = ['x_business_id', 'agent_search_param']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_business_id' in local_var_params:
            header_params['x-business-id'] = local_var_params['x_business_id']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/apm2/openapi/apm-service/agent-mgr/search',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='SearchAgentResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def search_application(self, request):
        """对指定区域下的组件和环境及其探针情况进行搜索

        对指定区域下的组件和环境及其探针情况进行搜索。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SearchApplication
        :type request: :class:`huaweicloudsdkapm.v1.SearchApplicationRequest`
        :rtype: :class:`huaweicloudsdkapm.v1.SearchApplicationResponse`
        """
        return self.search_application_with_http_info(request)

    def search_application_with_http_info(self, request):
        all_params = ['x_business_id', 'app_search_param']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_business_id' in local_var_params:
            header_params['x-business-id'] = local_var_params['x_business_id']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/apm2/openapi/apm-service/app-mgr/search',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='SearchApplicationResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_master_address(self, request):
        """查询master地址

        根据region名称获取该region下的master服务podlb地址信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowMasterAddress
        :type request: :class:`huaweicloudsdkapm.v1.ShowMasterAddressRequest`
        :rtype: :class:`huaweicloudsdkapm.v1.ShowMasterAddressResponse`
        """
        return self.show_master_address_with_http_info(request)

    def show_master_address_with_http_info(self, request):
        all_params = ['region_name']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'region_name' in local_var_params:
            query_params.append(('region_name', local_var_params['region_name']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/apm2/openapi/systemmng/get-master-address',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowMasterAddressResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_app(self, request):
        """根据组件id删除指定的组件

        该接口用于删除指定的组件。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteApp
        :type request: :class:`huaweicloudsdkapm.v1.DeleteAppRequest`
        :rtype: :class:`huaweicloudsdkapm.v1.DeleteAppResponse`
        """
        return self.delete_app_with_http_info(request)

    def delete_app_with_http_info(self, request):
        all_params = ['application_id', 'x_business_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/apm2/openapi/cmdb/apps/delete-app/{application_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteAppResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_app_envs(self, request):
        """获取组件下的环境列表

        获取组件下的环境列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAppEnvs
        :type request: :class:`huaweicloudsdkapm.v1.ListAppEnvsRequest`
        :rtype: :class:`huaweicloudsdkapm.v1.ListAppEnvsResponse`
        """
        return self.list_app_envs_with_http_info(request)

    def list_app_envs_with_http_info(self, request):
        all_params = ['app_id', 'x_business_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/apm2/openapi/cmdb/envs/get-app-envs',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListAppEnvsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_apps(self, request):
        """获取组件列表

        获取组件列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListApps
        :type request: :class:`huaweicloudsdkapm.v1.ListAppsRequest`
        :rtype: :class:`huaweicloudsdkapm.v1.ListAppsResponse`
        """
        return self.list_apps_with_http_info(request)

    def list_apps_with_http_info(self, request):
        all_params = ['business_id', 'x_business_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/apm2/openapi/cmdb/apps/get-apps',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListAppsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_env_tags(self, request):
        """查询环境标签

        查询环境标签接口。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListEnvTags
        :type request: :class:`huaweicloudsdkapm.v1.ListEnvTagsRequest`
        :rtype: :class:`huaweicloudsdkapm.v1.ListEnvTagsResponse`
        """
        return self.list_env_tags_with_http_info(request)

    def list_env_tags_with_http_info(self, request):
        all_params = ['x_business_id', 'tag_param']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_business_id' in local_var_params:
            header_params['x-business-id'] = local_var_params['x_business_id']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/apm2/openapi/cmdb/tag/get-env-tag-list',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListEnvTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_business_detail(self, request):
        """查询单个应用的详情

        查询单个应用的详情。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowBusinessDetail
        :type request: :class:`huaweicloudsdkapm.v1.ShowBusinessDetailRequest`
        :rtype: :class:`huaweicloudsdkapm.v1.ShowBusinessDetailResponse`
        """
        return self.show_business_detail_with_http_info(request)

    def show_business_detail_with_http_info(self, request):
        all_params = ['business_id', 'x_business_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/apm2/openapi/cmdb/business/get-business-detail/{business_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowBusinessDetailResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_sub_business_detail(self, request):
        """查询子应用详情

        查询单个子应用详情。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowSubBusinessDetail
        :type request: :class:`huaweicloudsdkapm.v1.ShowSubBusinessDetailRequest`
        :rtype: :class:`huaweicloudsdkapm.v1.ShowSubBusinessDetailResponse`
        """
        return self.show_sub_business_detail_with_http_info(request)

    def show_sub_business_detail_with_http_info(self, request):
        all_params = ['sub_business_id', 'x_business_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/apm2/openapi/cmdb/sub-business/get-sub-business-detail/{sub_business_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowSubBusinessDetailResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_topology_tree(self, request):
        """获取应用树

        获取应用树。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowTopologyTree
        :type request: :class:`huaweicloudsdkapm.v1.ShowTopologyTreeRequest`
        :rtype: :class:`huaweicloudsdkapm.v1.ShowTopologyTreeResponse`
        """
        return self.show_topology_tree_with_http_info(request)

    def show_topology_tree_with_http_info(self, request):
        all_params = ['business_id', 'x_business_id', 'region_id', 'env_tag_id', 'env_keyword']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/apm2/openapi/cmdb/topology-trees/get-topology-trees',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowTopologyTreeResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_open_region(self, request):
        """查询开通的region

        该接口用于查询用户开通的region信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListOpenRegion
        :type request: :class:`huaweicloudsdkapm.v1.ListOpenRegionRequest`
        :rtype: :class:`huaweicloudsdkapm.v1.ListOpenRegionResponse`
        """
        return self.list_open_region_with_http_info(request)

    def list_open_region_with_http_info(self, request):
        all_params = []
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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

        auth_settings = []

        return self.call_api(
            resource_path='/v1/apm2/openapi/region/get-opened-region',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListOpenRegionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_supported_region(self, request):
        """查询所有的支持的region

        查询所有的支持的region信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListSupportedRegion
        :type request: :class:`huaweicloudsdkapm.v1.ListSupportedRegionRequest`
        :rtype: :class:`huaweicloudsdkapm.v1.ListSupportedRegionResponse`
        """
        return self.list_supported_region_with_http_info(request)

    def list_supported_region_with_http_info(self, request):
        all_params = []
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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

        auth_settings = []

        return self.call_api(
            resource_path='/v1/apm2/openapi/region/get-all-supported-region',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListSupportedRegionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def search_business_topology(self, request):
        """查询应用全局拓扑图

        查询应用级别全局拓扑图信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SearchBusinessTopology
        :type request: :class:`huaweicloudsdkapm.v1.SearchBusinessTopologyRequest`
        :rtype: :class:`huaweicloudsdkapm.v1.SearchBusinessTopologyResponse`
        """
        return self.search_business_topology_with_http_info(request)

    def search_business_topology_with_http_info(self, request):
        all_params = ['x_business_id', 'business_topo_request']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_business_id' in local_var_params:
            header_params['x-business-id'] = local_var_params['x_business_id']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/apm2/openapi/topology/business-search',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='SearchBusinessTopologyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def search_env_topology(self, request):
        """查询组件环境拓扑图

        查询组件环境级别全局拓扑图信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SearchEnvTopology
        :type request: :class:`huaweicloudsdkapm.v1.SearchEnvTopologyRequest`
        :rtype: :class:`huaweicloudsdkapm.v1.SearchEnvTopologyResponse`
        """
        return self.search_env_topology_with_http_info(request)

    def search_env_topology_with_http_info(self, request):
        all_params = ['x_business_id', 'env_topo_request']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_business_id' in local_var_params:
            header_params['x-business-id'] = local_var_params['x_business_id']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/apm2/openapi/topology/env-search',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='SearchEnvTopologyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_business_env(self, request):
        """查询URL跟踪Region环境列表

        查询所选Region下设置了URL跟踪的环境列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListBusinessEnv
        :type request: :class:`huaweicloudsdkapm.v1.ListBusinessEnvRequest`
        :rtype: :class:`huaweicloudsdkapm.v1.ListBusinessEnvResponse`
        """
        return self.list_business_env_with_http_info(request)

    def list_business_env_with_http_info(self, request):
        all_params = ['x_business_id', 'business_env_request']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_business_id' in local_var_params:
            header_params['x-business-id'] = local_var_params['x_business_id']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/apm2/openapi/transaction/business-env',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListBusinessEnvResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def search_transaction(self, request):
        """查询URL跟踪视图列表

        查询当前被调用的URL跟踪视图列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SearchTransaction
        :type request: :class:`huaweicloudsdkapm.v1.SearchTransactionRequest`
        :rtype: :class:`huaweicloudsdkapm.v1.SearchTransactionResponse`
        """
        return self.search_transaction_with_http_info(request)

    def search_transaction_with_http_info(self, request):
        all_params = ['x_business_id', 'tx_search_request']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_business_id' in local_var_params:
            header_params['x-business-id'] = local_var_params['x_business_id']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/apm2/openapi/transaction/search',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='SearchTransactionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def search_transaction_config(self, request):
        """查询URL跟踪配置列表

        查询已配置好的URL跟踪配置列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SearchTransactionConfig
        :type request: :class:`huaweicloudsdkapm.v1.SearchTransactionConfigRequest`
        :rtype: :class:`huaweicloudsdkapm.v1.SearchTransactionConfigResponse`
        """
        return self.search_transaction_config_with_http_info(request)

    def search_transaction_config_with_http_info(self, request):
        all_params = ['x_business_id', 'transaction_config_search_request']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_business_id' in local_var_params:
            header_params['x-business-id'] = local_var_params['x_business_id']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/apm2/openapi/transaction/transaction-config-search',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='SearchTransactionConfigResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_transaction_detail(self, request):
        """查询URL跟踪视图详情

        查询某条URL跟踪视图详情。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowTransactionDetail
        :type request: :class:`huaweicloudsdkapm.v1.ShowTransactionDetailRequest`
        :rtype: :class:`huaweicloudsdkapm.v1.ShowTransactionDetailResponse`
        """
        return self.show_transaction_detail_with_http_info(request)

    def show_transaction_detail_with_http_info(self, request):
        all_params = ['x_business_id', 'tx_detail_request']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_business_id' in local_var_params:
            header_params['x-business-id'] = local_var_params['x_business_id']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/apm2/openapi/transaction/detail',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowTransactionDetailResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_env_instances(self, request):
        """获取实例信息列表

        获取实例信息列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListEnvInstances
        :type request: :class:`huaweicloudsdkapm.v1.ListEnvInstancesRequest`
        :rtype: :class:`huaweicloudsdkapm.v1.ListEnvInstancesResponse`
        """
        return self.list_env_instances_with_http_info(request)

    def list_env_instances_with_http_info(self, request):
        all_params = ['x_business_id', 'instance_search_param']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_business_id' in local_var_params:
            header_params['x-business-id'] = local_var_params['x_business_id']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/apm2/openapi/view/mainview/get-env-instance-list',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListEnvInstancesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_clob_detail(self, request):
        """获取原始数据详情

        获取原始数据详情。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowClobDetail
        :type request: :class:`huaweicloudsdkapm.v1.ShowClobDetailRequest`
        :rtype: :class:`huaweicloudsdkapm.v1.ShowClobDetailResponse`
        """
        return self.show_clob_detail_with_http_info(request)

    def show_clob_detail_with_http_info(self, request):
        all_params = ['x_business_id', 'get_clob_detail_param']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_business_id' in local_var_params:
            header_params['x-business-id'] = local_var_params['x_business_id']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/apm2/openapi/view/metric/get-clob-detail',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowClobDetailResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_env_monitor_items(self, request):
        """获取监控项信息

        获取监控项信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowEnvMonitorItems
        :type request: :class:`huaweicloudsdkapm.v1.ShowEnvMonitorItemsRequest`
        :rtype: :class:`huaweicloudsdkapm.v1.ShowEnvMonitorItemsResponse`
        """
        return self.show_env_monitor_items_with_http_info(request)

    def show_env_monitor_items_with_http_info(self, request):
        all_params = ['env_id', 'x_business_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/apm2/openapi/view/mainview/get-env-monitor-item-list',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowEnvMonitorItemsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_event_detail(self, request):
        """获取event的详情

        获取event的详情。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowEventDetail
        :type request: :class:`huaweicloudsdkapm.v1.ShowEventDetailRequest`
        :rtype: :class:`huaweicloudsdkapm.v1.ShowEventDetailResponse`
        """
        return self.show_event_detail_with_http_info(request)

    def show_event_detail_with_http_info(self, request):
        all_params = ['trace_id', 'span_id', 'event_id', 'env_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/apm2/openapi/view/trace/get-event-detail',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowEventDetailResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_monitor_item_view_config(self, request):
        """查询监控项配置信息

        查询监控项配置信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowMonitorItemViewConfig
        :type request: :class:`huaweicloudsdkapm.v1.ShowMonitorItemViewConfigRequest`
        :rtype: :class:`huaweicloudsdkapm.v1.ShowMonitorItemViewConfigResponse`
        """
        return self.show_monitor_item_view_config_with_http_info(request)

    def show_monitor_item_view_config_with_http_info(self, request):
        all_params = ['env_id', 'collector_id', 'x_business_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/apm2/openapi/view/config/get-monitor-item-view-config',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowMonitorItemViewConfigResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_raw_table(self, request):
        """获取原始数据表格

        获取原始数据表格。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowRawTable
        :type request: :class:`huaweicloudsdkapm.v1.ShowRawTableRequest`
        :rtype: :class:`huaweicloudsdkapm.v1.ShowRawTableResponse`
        """
        return self.show_raw_table_with_http_info(request)

    def show_raw_table_with_http_info(self, request):
        all_params = ['x_business_id', 'raw_table_param']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_business_id' in local_var_params:
            header_params['x-business-id'] = local_var_params['x_business_id']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/apm2/openapi/view/metric/raw-table',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowRawTableResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_span_search(self, request):
        """查询span数据

        span数据查询接口。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowSpanSearch
        :type request: :class:`huaweicloudsdkapm.v1.ShowSpanSearchRequest`
        :rtype: :class:`huaweicloudsdkapm.v1.ShowSpanSearchResponse`
        """
        return self.show_span_search_with_http_info(request)

    def show_span_search_with_http_info(self, request):
        all_params = ['x_business_id', 'trace_search_param']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_business_id' in local_var_params:
            header_params['x-business-id'] = local_var_params['x_business_id']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/apm2/openapi/view/trace/span-search',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowSpanSearchResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_sum_table(self, request):
        """获取汇总表格数据

        获取汇总表格数据。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowSumTable
        :type request: :class:`huaweicloudsdkapm.v1.ShowSumTableRequest`
        :rtype: :class:`huaweicloudsdkapm.v1.ShowSumTableResponse`
        """
        return self.show_sum_table_with_http_info(request)

    def show_sum_table_with_http_info(self, request):
        all_params = ['x_business_id', 'sum_table_param']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_business_id' in local_var_params:
            header_params['x-business-id'] = local_var_params['x_business_id']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/apm2/openapi/view/metric/sum-table',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowSumTableResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_topology(self, request):
        """调用链拓扑图

        调用链拓扑图。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowTopology
        :type request: :class:`huaweicloudsdkapm.v1.ShowTopologyRequest`
        :rtype: :class:`huaweicloudsdkapm.v1.ShowTopologyResponse`
        """
        return self.show_topology_with_http_info(request)

    def show_topology_with_http_info(self, request):
        all_params = ['trace_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'trace_id' in local_var_params:
            query_params.append(('trace_id', local_var_params['trace_id']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/apm2/openapi/view/trace/topology',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowTopologyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_trace_events(self, request):
        """获取一个trace的所有调用链数据

        获取一个trace的所有调用链数据。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowTraceEvents
        :type request: :class:`huaweicloudsdkapm.v1.ShowTraceEventsRequest`
        :rtype: :class:`huaweicloudsdkapm.v1.ShowTraceEventsResponse`
        """
        return self.show_trace_events_with_http_info(request)

    def show_trace_events_with_http_info(self, request):
        all_params = ['trace_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'trace_id' in local_var_params:
            query_params.append(('trace_id', local_var_params['trace_id']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/apm2/openapi/view/trace/get-trace-events',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowTraceEventsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_trend(self, request):
        """获取趋势图

        获取趋势图。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowTrend
        :type request: :class:`huaweicloudsdkapm.v1.ShowTrendRequest`
        :rtype: :class:`huaweicloudsdkapm.v1.ShowTrendResponse`
        """
        return self.show_trend_with_http_info(request)

    def show_trend_with_http_info(self, request):
        all_params = ['x_business_id', 'trend_param']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_business_id' in local_var_params:
            header_params['x-business-id'] = local_var_params['x_business_id']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/apm2/openapi/view/metric/trend',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowTrendResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

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

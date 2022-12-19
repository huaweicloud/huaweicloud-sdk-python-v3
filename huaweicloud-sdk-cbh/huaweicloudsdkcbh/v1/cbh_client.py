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


class CbhClient(Client):
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
        super(CbhClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkcbh.v1.model")
        self.preset_headers = {'User-Agent': 'HuaweiCloud-SDK-Python'}

    @classmethod
    def new_builder(cls, clazz=None):
        if clazz is None:
            return ClientBuilder(cls)

        if clazz.__name__ != "CbhClient":
            raise TypeError("client type error, support client type is CbhClient")

        return ClientBuilder(clazz)

    def change_instance_network(self, request):
        """修改CBH实例网络

        修改CBH实例网络
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ChangeInstanceNetwork
        :type request: :class:`huaweicloudsdkcbh.v1.ChangeInstanceNetworkRequest`
        :rtype: :class:`huaweicloudsdkcbh.v1.ChangeInstanceNetworkResponse`
        """
        return self.change_instance_network_with_http_info(request)

    def change_instance_network_with_http_info(self, request):
        all_params = ['server_id', 'change_instance_network_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'server_id' in local_var_params:
            path_params['server_id'] = local_var_params['server_id']

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
            resource_path='/v1/{project_id}/cbs/{server_id}/network/change',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ChangeInstanceNetworkResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_instance(self, request):
        """创建CBH实例

        创建CBH实例
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateInstance
        :type request: :class:`huaweicloudsdkcbh.v1.CreateInstanceRequest`
        :rtype: :class:`huaweicloudsdkcbh.v1.CreateInstanceResponse`
        """
        return self.create_instance_with_http_info(request)

    def create_instance_with_http_info(self, request):
        all_params = ['create_instance_request_body']
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
            resource_path='/v1/{project_id}/cbs/instance/create',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateInstanceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_instance_order(self, request):
        """创建CBH实例订单

        创建CBH实例订单
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateInstanceOrder
        :type request: :class:`huaweicloudsdkcbh.v1.CreateInstanceOrderRequest`
        :rtype: :class:`huaweicloudsdkcbh.v1.CreateInstanceOrderResponse`
        """
        return self.create_instance_order_with_http_info(request)

    def create_instance_order_with_http_info(self, request):
        all_params = ['create_instance_order_request_body']
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
            resource_path='/v1/{project_id}/cbs/period/order',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateInstanceOrderResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_cbh_instance(self, request):
        """获取CBH实例列表

        获取CBH实例列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListCbhInstance
        :type request: :class:`huaweicloudsdkcbh.v1.ListCbhInstanceRequest`
        :rtype: :class:`huaweicloudsdkcbh.v1.ListCbhInstanceResponse`
        """
        return self.list_cbh_instance_with_http_info(request)

    def list_cbh_instance_with_http_info(self, request):
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
            resource_path='/v1/{project_id}/cbs/instance/list',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListCbhInstanceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def restart_cbh_instance(self, request):
        """重启CBH实例

        重启CBH实例
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RestartCbhInstance
        :type request: :class:`huaweicloudsdkcbh.v1.RestartCbhInstanceRequest`
        :rtype: :class:`huaweicloudsdkcbh.v1.RestartCbhInstanceResponse`
        """
        return self.restart_cbh_instance_with_http_info(request)

    def restart_cbh_instance_with_http_info(self, request):
        all_params = ['restart_cbh_instance_request_body']
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
            resource_path='/v1/{project_id}/cbs/instance/reboot',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RestartCbhInstanceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def search_quota(self, request):
        """查询堡垒机配额

        查询堡垒机配额
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SearchQuota
        :type request: :class:`huaweicloudsdkcbh.v1.SearchQuotaRequest`
        :rtype: :class:`huaweicloudsdkcbh.v1.SearchQuotaResponse`
        """
        return self.search_quota_with_http_info(request)

    def search_quota_with_http_info(self, request):
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
            resource_path='/v1/{project_id}/cbs/instance/quota',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='SearchQuotaResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_available_zone_info(self, request):
        """获取CBH服务可用分区信息

        获取CBH服务可用分区信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAvailableZoneInfo
        :type request: :class:`huaweicloudsdkcbh.v1.ShowAvailableZoneInfoRequest`
        :rtype: :class:`huaweicloudsdkcbh.v1.ShowAvailableZoneInfoResponse`
        """
        return self.show_available_zone_info_with_http_info(request)

    def show_available_zone_info_with_http_info(self, request):
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
            resource_path='/v1/{project_id}/cbs/available-zone',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowAvailableZoneInfoResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_network_configuration(self, request):
        """检查网络接口

        检查网络接口
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowNetworkConfiguration
        :type request: :class:`huaweicloudsdkcbh.v1.ShowNetworkConfigurationRequest`
        :rtype: :class:`huaweicloudsdkcbh.v1.ShowNetworkConfigurationResponse`
        """
        return self.show_network_configuration_with_http_info(request)

    def show_network_configuration_with_http_info(self, request):
        all_params = ['show_network_configuration_request_body']
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
            resource_path='/v1/{project_id}/cbs/network/configuration',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowNetworkConfigurationResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def start_cbh_instance(self, request):
        """启动CBH实例

        启动CBH实例
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for StartCbhInstance
        :type request: :class:`huaweicloudsdkcbh.v1.StartCbhInstanceRequest`
        :rtype: :class:`huaweicloudsdkcbh.v1.StartCbhInstanceResponse`
        """
        return self.start_cbh_instance_with_http_info(request)

    def start_cbh_instance_with_http_info(self, request):
        all_params = ['start_cbh_instance_request_body']
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
            resource_path='/v1/{project_id}/cbs/instance/start',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='StartCbhInstanceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def upgrade_cbh_instance(self, request):
        """升级CBH实例

        升级CBH实例
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpgradeCbhInstance
        :type request: :class:`huaweicloudsdkcbh.v1.UpgradeCbhInstanceRequest`
        :rtype: :class:`huaweicloudsdkcbh.v1.UpgradeCbhInstanceResponse`
        """
        return self.upgrade_cbh_instance_with_http_info(request)

    def upgrade_cbh_instance_with_http_info(self, request):
        all_params = ['upgrade_cbh_instance_request_body']
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
            resource_path='/v1/{project_id}/cbs/instance/upgrade',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpgradeCbhInstanceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def change_instance_order(self, request):
        """创建变更CBH订单

        创建变更CBH订单
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ChangeInstanceOrder
        :type request: :class:`huaweicloudsdkcbh.v1.ChangeInstanceOrderRequest`
        :rtype: :class:`huaweicloudsdkcbh.v1.ChangeInstanceOrderResponse`
        """
        return self.change_instance_order_with_http_info(request)

    def change_instance_order_with_http_info(self, request):
        all_params = ['server_id', 'instance_key']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/cbs/{server_id}/alter/{instance_key}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ChangeInstanceOrderResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def stop_cbh_instance(self, request):
        """关闭CBH实例

        关闭CBH实例
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for StopCbhInstance
        :type request: :class:`huaweicloudsdkcbh.v1.StopCbhInstanceRequest`
        :rtype: :class:`huaweicloudsdkcbh.v1.StopCbhInstanceResponse`
        """
        return self.stop_cbh_instance_with_http_info(request)

    def stop_cbh_instance_with_http_info(self, request):
        all_params = ['stop_cbh_instance_request_body']
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
            resource_path='/v1/{project_id}/cbs/instance/stop',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='StopCbhInstanceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_quota_state(self, request):
        """获取ECS配额

        获取当前租户所选择的可用分区、性能规格所对应的ECS flavor是否可用
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListQuotaState
        :type request: :class:`huaweicloudsdkcbh.v1.ListQuotaStateRequest`
        :rtype: :class:`huaweicloudsdkcbh.v1.ListQuotaStateResponse`
        """
        return self.list_quota_state_with_http_info(request)

    def list_quota_state_with_http_info(self, request):
        all_params = ['availability_zone', 'resource_spec_code']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/cbs/instance/ecs-quota',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListQuotaStateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def install_instance_eip(self, request):
        """绑定CBH实例Eip

        绑定CBH实例Eip
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for InstallInstanceEip
        :type request: :class:`huaweicloudsdkcbh.v1.InstallInstanceEipRequest`
        :rtype: :class:`huaweicloudsdkcbh.v1.InstallInstanceEipResponse`
        """
        return self.install_instance_eip_with_http_info(request)

    def install_instance_eip_with_http_info(self, request):
        all_params = ['server_id', 'install_instance_eip_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'server_id' in local_var_params:
            path_params['server_id'] = local_var_params['server_id']

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
            resource_path='/v1/{project_id}/cbs/instance/{server_id}/eip/bind',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='InstallInstanceEipResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def uninstall_instance_eip(self, request):
        """解绑CBH实例Eip

        解绑CBH实例Eip
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UninstallInstanceEip
        :type request: :class:`huaweicloudsdkcbh.v1.UninstallInstanceEipRequest`
        :rtype: :class:`huaweicloudsdkcbh.v1.UninstallInstanceEipResponse`
        """
        return self.uninstall_instance_eip_with_http_info(request)

    def uninstall_instance_eip_with_http_info(self, request):
        all_params = ['server_id', 'uninstall_instance_eip_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'server_id' in local_var_params:
            path_params['server_id'] = local_var_params['server_id']

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
            resource_path='/v1/{project_id}/cbs/instance/{server_id}/eip/unbind',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UninstallInstanceEipResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def reset_login_method(self, request):
        """修改admin用户多因子认证方式

        修改admin用户多因子认证方式
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ResetLoginMethod
        :type request: :class:`huaweicloudsdkcbh.v1.ResetLoginMethodRequest`
        :rtype: :class:`huaweicloudsdkcbh.v1.ResetLoginMethodResponse`
        """
        return self.reset_login_method_with_http_info(request)

    def reset_login_method_with_http_info(self, request):
        all_params = ['server_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'server_id' in local_var_params:
            path_params['server_id'] = local_var_params['server_id']

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
            resource_path='/v1/{project_id}/cbs/instance/{server_id}/login-method',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ResetLoginMethodResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def reset_password(self, request):
        """修改admin密码

        修改admin密码
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ResetPassword
        :type request: :class:`huaweicloudsdkcbh.v1.ResetPasswordRequest`
        :rtype: :class:`huaweicloudsdkcbh.v1.ResetPasswordResponse`
        """
        return self.reset_password_with_http_info(request)

    def reset_password_with_http_info(self, request):
        all_params = ['reset_password_request_body']
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
            resource_path='/v1/{project_id}/cbs/instance/password',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ResetPasswordResponse',
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

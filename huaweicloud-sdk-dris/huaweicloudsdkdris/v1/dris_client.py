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


class DrisClient(Client):
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
        super(DrisClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkdris.v1.model")
        self.preset_headers = {'User-Agent': 'HuaweiCloud-SDK-Python'}

    @classmethod
    def new_builder(cls, clazz=None):
        if clazz is None:
            return ClientBuilder(cls)

        if clazz.__name__ != "DrisClient":
            raise TypeError("client type error, support client type is DrisClient")

        return ClientBuilder(clazz)

    def create_data_channel(self, request):
        """创建业务通道

        创建业务通道，用于创建Edge消息上报的数据通道。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateDataChannel
        :type request: :class:`huaweicloudsdkdris.v1.CreateDataChannelRequest`
        :rtype: :class:`huaweicloudsdkdris.v1.CreateDataChannelResponse`
        """
        return self.create_data_channel_with_http_info(request)

    def create_data_channel_with_http_info(self, request):
        all_params = ['v2x_edge_id', 'create_data_channel_request_body', 'instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'v2x_edge_id' in local_var_params:
            path_params['v2x_edge_id'] = local_var_params['v2x_edge_id']

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v1/{project_id}/v2x-edges/{v2x_edge_id}/data-channel',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateDataChannelResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_data_channel(self, request):
        """删除业务通道

        删除业务通道
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteDataChannel
        :type request: :class:`huaweicloudsdkdris.v1.DeleteDataChannelRequest`
        :rtype: :class:`huaweicloudsdkdris.v1.DeleteDataChannelResponse`
        """
        return self.delete_data_channel_with_http_info(request)

    def delete_data_channel_with_http_info(self, request):
        all_params = ['v2x_edge_id', 'instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'v2x_edge_id' in local_var_params:
            path_params['v2x_edge_id'] = local_var_params['v2x_edge_id']

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v1/{project_id}/v2x-edges/{v2x_edge_id}/data-channel',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteDataChannelResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_data_channel(self, request):
        """查询业务通道

        查询业务通道
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDataChannel
        :type request: :class:`huaweicloudsdkdris.v1.ShowDataChannelRequest`
        :rtype: :class:`huaweicloudsdkdris.v1.ShowDataChannelResponse`
        """
        return self.show_data_channel_with_http_info(request)

    def show_data_channel_with_http_info(self, request):
        all_params = ['v2x_edge_id', 'instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'v2x_edge_id' in local_var_params:
            path_params['v2x_edge_id'] = local_var_params['v2x_edge_id']

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v1/{project_id}/v2x-edges/{v2x_edge_id}/data-channel',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowDataChannelResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_data_channel(self, request):
        """修改业务通道

        修改业务通道
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateDataChannel
        :type request: :class:`huaweicloudsdkdris.v1.UpdateDataChannelRequest`
        :rtype: :class:`huaweicloudsdkdris.v1.UpdateDataChannelResponse`
        """
        return self.update_data_channel_with_http_info(request)

    def update_data_channel_with_http_info(self, request):
        all_params = ['v2x_edge_id', 'update_data_channel_request_body', 'instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'v2x_edge_id' in local_var_params:
            path_params['v2x_edge_id'] = local_var_params['v2x_edge_id']

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v1/{project_id}/v2x-edges/{v2x_edge_id}/data-channel',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateDataChannelResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_v2x_edge(self, request):
        """创建Edge

        创建Edge
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateV2xEdge
        :type request: :class:`huaweicloudsdkdris.v1.CreateV2xEdgeRequest`
        :rtype: :class:`huaweicloudsdkdris.v1.CreateV2xEdgeResponse`
        """
        return self.create_v2x_edge_with_http_info(request)

    def create_v2x_edge_with_http_info(self, request):
        all_params = ['create_v2x_edge_request_body', 'instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v1/{project_id}/v2x-edges',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateV2xEdgeResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_v2_x_edge_by_v2x_edge_id(self, request):
        """删除Edge

        删除Edge之前需要删除Edge下的业务通道和关联设备。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteV2XEdgeByV2xEdgeId
        :type request: :class:`huaweicloudsdkdris.v1.DeleteV2XEdgeByV2xEdgeIdRequest`
        :rtype: :class:`huaweicloudsdkdris.v1.DeleteV2XEdgeByV2xEdgeIdResponse`
        """
        return self.delete_v2_x_edge_by_v2x_edge_id_with_http_info(request)

    def delete_v2_x_edge_by_v2x_edge_id_with_http_info(self, request):
        all_params = ['v2x_edge_id', 'instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'v2x_edge_id' in local_var_params:
            path_params['v2x_edge_id'] = local_var_params['v2x_edge_id']

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v1/{project_id}/v2x-edges/{v2x_edge_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteV2XEdgeByV2xEdgeIdResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_v2x_edges(self, request):
        """查询Edge列表

        查询Edge列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListV2xEdges
        :type request: :class:`huaweicloudsdkdris.v1.ListV2xEdgesRequest`
        :rtype: :class:`huaweicloudsdkdris.v1.ListV2xEdgesResponse`
        """
        return self.list_v2x_edges_with_http_info(request)

    def list_v2x_edges_with_http_info(self, request):
        all_params = ['instance_id', 'offset', 'limit', 'status']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v1/{project_id}/v2x-edges',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListV2xEdgesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_deployment_code(self, request):
        """生成部署应用安装命令

        生成部署应用安装命令,然后在ITS800或者ATLAS500上通过Shell执行
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDeploymentCode
        :type request: :class:`huaweicloudsdkdris.v1.ShowDeploymentCodeRequest`
        :rtype: :class:`huaweicloudsdkdris.v1.ShowDeploymentCodeResponse`
        """
        return self.show_deployment_code_with_http_info(request)

    def show_deployment_code_with_http_info(self, request):
        all_params = ['v2x_edge_id', 'instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'v2x_edge_id' in local_var_params:
            path_params['v2x_edge_id'] = local_var_params['v2x_edge_id']

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v1/{project_id}/v2x-edges/{v2x_edge_id}/deployment-code',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowDeploymentCodeResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_v2x_edge_detail(self, request):
        """查询Edge

        查询Edge
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowV2xEdgeDetail
        :type request: :class:`huaweicloudsdkdris.v1.ShowV2xEdgeDetailRequest`
        :rtype: :class:`huaweicloudsdkdris.v1.ShowV2xEdgeDetailResponse`
        """
        return self.show_v2x_edge_detail_with_http_info(request)

    def show_v2x_edge_detail_with_http_info(self, request):
        all_params = ['v2x_edge_id', 'instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'v2x_edge_id' in local_var_params:
            path_params['v2x_edge_id'] = local_var_params['v2x_edge_id']

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v1/{project_id}/v2x-edges/{v2x_edge_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowV2xEdgeDetailResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_v2x_edge(self, request):
        """修改Edge

        修改Edge
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateV2xEdge
        :type request: :class:`huaweicloudsdkdris.v1.UpdateV2xEdgeRequest`
        :rtype: :class:`huaweicloudsdkdris.v1.UpdateV2xEdgeResponse`
        """
        return self.update_v2x_edge_with_http_info(request)

    def update_v2x_edge_with_http_info(self, request):
        all_params = ['v2x_edge_id', 'update_v2_x_edge_request_body', 'instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'v2x_edge_id' in local_var_params:
            path_params['v2x_edge_id'] = local_var_params['v2x_edge_id']

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v1/{project_id}/v2x-edges/{v2x_edge_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateV2xEdgeResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def add_forwarding_configs(self, request):
        """创建数据转发配置

        创建数据转发配置。当前仅支持数据转发至kafka，数据转发配置成功添加后配置中的Topic消息将会转发至指定的brokers。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AddForwardingConfigs
        :type request: :class:`huaweicloudsdkdris.v1.AddForwardingConfigsRequest`
        :rtype: :class:`huaweicloudsdkdris.v1.AddForwardingConfigsResponse`
        """
        return self.add_forwarding_configs_with_http_info(request)

    def add_forwarding_configs_with_http_info(self, request):
        all_params = ['add_forwarding_configs_request_body', 'instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v1/{project_id}/forwarding-configs',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='AddForwardingConfigsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_forwarding_config(self, request):
        """删除数据转发配置

        根据转发配置的唯一ID（forwarding_config_id）删除数据转发配置，删除后配置中订阅的topic消息将不会被转发至brokers。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteForwardingConfig
        :type request: :class:`huaweicloudsdkdris.v1.DeleteForwardingConfigRequest`
        :rtype: :class:`huaweicloudsdkdris.v1.DeleteForwardingConfigResponse`
        """
        return self.delete_forwarding_config_with_http_info(request)

    def delete_forwarding_config_with_http_info(self, request):
        all_params = ['forwarding_type', 'forwarding_config_id', 'instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'forwarding_config_id' in local_var_params:
            path_params['forwarding_config_id'] = local_var_params['forwarding_config_id']

        query_params = []
        if 'forwarding_type' in local_var_params:
            query_params.append(('forwarding_type', local_var_params['forwarding_type']))

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/forwarding-configs/{forwarding_config_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteForwardingConfigResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_forwarding_config(self, request):
        """查询数据转发配置

        根据转发配置的唯一ID（forwarding_config_id）查询数据转发配置
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowForwardingConfig
        :type request: :class:`huaweicloudsdkdris.v1.ShowForwardingConfigRequest`
        :rtype: :class:`huaweicloudsdkdris.v1.ShowForwardingConfigResponse`
        """
        return self.show_forwarding_config_with_http_info(request)

    def show_forwarding_config_with_http_info(self, request):
        all_params = ['forwarding_type', 'forwarding_config_id', 'instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'forwarding_config_id' in local_var_params:
            path_params['forwarding_config_id'] = local_var_params['forwarding_config_id']

        query_params = []
        if 'forwarding_type' in local_var_params:
            query_params.append(('forwarding_type', local_var_params['forwarding_type']))

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/forwarding-configs/{forwarding_config_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowForwardingConfigResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_forwarding_configs(self, request):
        """查询数据转发配置列表

        查询数据转发配置列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowForwardingConfigs
        :type request: :class:`huaweicloudsdkdris.v1.ShowForwardingConfigsRequest`
        :rtype: :class:`huaweicloudsdkdris.v1.ShowForwardingConfigsResponse`
        """
        return self.show_forwarding_configs_with_http_info(request)

    def show_forwarding_configs_with_http_info(self, request):
        all_params = ['forwarding_type', 'instance_id', 'offset', 'limit']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'forwarding_type' in local_var_params:
            query_params.append(('forwarding_type', local_var_params['forwarding_type']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/forwarding-configs',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowForwardingConfigsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_forwarding_config(self, request):
        """修改数据转发配置

        根据转发配置的唯一ID（forwarding_config_id）修改数据转发配置，当前支持更新的字段有topicPrefix、userTopics、brokers，需要把该字段新的对应值全量写入。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateForwardingConfig
        :type request: :class:`huaweicloudsdkdris.v1.UpdateForwardingConfigRequest`
        :rtype: :class:`huaweicloudsdkdris.v1.UpdateForwardingConfigResponse`
        """
        return self.update_forwarding_config_with_http_info(request)

    def update_forwarding_config_with_http_info(self, request):
        all_params = ['forwarding_type', 'forwarding_config_id', 'update_forwarding_config_request_body', 'instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'forwarding_config_id' in local_var_params:
            path_params['forwarding_config_id'] = local_var_params['forwarding_config_id']

        query_params = []
        if 'forwarding_type' in local_var_params:
            query_params.append(('forwarding_type', local_var_params['forwarding_type']))

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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
            resource_path='/v1/{project_id}/forwarding-configs/{forwarding_config_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateForwardingConfigResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_history_traffic_events(self, request):
        """查询历史交通事件列表

        查询历史交通事件列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowHistoryTrafficEvents
        :type request: :class:`huaweicloudsdkdris.v1.ShowHistoryTrafficEventsRequest`
        :rtype: :class:`huaweicloudsdkdris.v1.ShowHistoryTrafficEventsResponse`
        """
        return self.show_history_traffic_events_with_http_info(request)

    def show_history_traffic_events_with_http_info(self, request):
        all_params = ['instance_id', 'offset', 'limit', 'from_date', 'to_date', 'event_id', 'event_class', 'event_type', 'event_source']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'from_date' in local_var_params:
            query_params.append(('from_date', local_var_params['from_date']))
        if 'to_date' in local_var_params:
            query_params.append(('to_date', local_var_params['to_date']))
        if 'event_id' in local_var_params:
            query_params.append(('event_id', local_var_params['event_id']))
        if 'event_class' in local_var_params:
            query_params.append(('event_class', local_var_params['event_class']))
        if 'event_type' in local_var_params:
            query_params.append(('event_type', local_var_params['event_type']))
        if 'event_source' in local_var_params:
            query_params.append(('event_source', local_var_params['event_source']))

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-app']

        return self.call_api(
            resource_path='/v1/{project_id}/history-traffic-events',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowHistoryTrafficEventsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_show_ipcs(self, request):
        """查询IPC列表

        获取多个IPC资源
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchShowIpcs
        :type request: :class:`huaweicloudsdkdris.v1.BatchShowIpcsRequest`
        :rtype: :class:`huaweicloudsdkdris.v1.BatchShowIpcsResponse`
        """
        return self.batch_show_ipcs_with_http_info(request)

    def batch_show_ipcs_with_http_info(self, request):
        all_params = ['instance_id', 'offset', 'limit', 'status', 'v2x_edge_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'v2x_edge_id' in local_var_params:
            query_params.append(('v2x_edge_id', local_var_params['v2x_edge_id']))

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v1/{project_id}/cameras',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchShowIpcsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_ipc(self, request):
        """查询IPC

        查询IPC
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowIpc
        :type request: :class:`huaweicloudsdkdris.v1.ShowIpcRequest`
        :rtype: :class:`huaweicloudsdkdris.v1.ShowIpcResponse`
        """
        return self.show_ipc_with_http_info(request)

    def show_ipc_with_http_info(self, request):
        all_params = ['camera_id', 'instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'camera_id' in local_var_params:
            path_params['camera_id'] = local_var_params['camera_id']

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v1/{project_id}/cameras/{camera_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowIpcResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_show_rsus(self, request):
        """查询RSU列表

        查询RSU列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchShowRsus
        :type request: :class:`huaweicloudsdkdris.v1.BatchShowRsusRequest`
        :rtype: :class:`huaweicloudsdkdris.v1.BatchShowRsusResponse`
        """
        return self.batch_show_rsus_with_http_info(request)

    def batch_show_rsus_with_http_info(self, request):
        all_params = ['instance_id', 'offset', 'limit', 'rsu_id', 'esn', 'status', 'rsu_model_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'rsu_id' in local_var_params:
            query_params.append(('rsu_id', local_var_params['rsu_id']))
        if 'esn' in local_var_params:
            query_params.append(('esn', local_var_params['esn']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'rsu_model_id' in local_var_params:
            query_params.append(('rsu_model_id', local_var_params['rsu_model_id']))

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v1/{project_id}/rsus',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchShowRsusResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_rsu(self, request):
        """创建RSU

        创建RSU
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateRsu
        :type request: :class:`huaweicloudsdkdris.v1.CreateRsuRequest`
        :rtype: :class:`huaweicloudsdkdris.v1.CreateRsuResponse`
        """
        return self.create_rsu_with_http_info(request)

    def create_rsu_with_http_info(self, request):
        all_params = ['create_rsu_request_body', 'instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v1/{project_id}/rsus',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateRsuResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_rsu(self, request):
        """删除RSU

        删除RSU
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteRsu
        :type request: :class:`huaweicloudsdkdris.v1.DeleteRsuRequest`
        :rtype: :class:`huaweicloudsdkdris.v1.DeleteRsuResponse`
        """
        return self.delete_rsu_with_http_info(request)

    def delete_rsu_with_http_info(self, request):
        all_params = ['rsu_id', 'instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'rsu_id' in local_var_params:
            path_params['rsu_id'] = local_var_params['rsu_id']

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v1/{project_id}/rsus/{rsu_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteRsuResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_rsu(self, request):
        """修改RSU

        修改RSU
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateRsu
        :type request: :class:`huaweicloudsdkdris.v1.UpdateRsuRequest`
        :rtype: :class:`huaweicloudsdkdris.v1.UpdateRsuResponse`
        """
        return self.update_rsu_with_http_info(request)

    def update_rsu_with_http_info(self, request):
        all_params = ['rsu_id', 'update_rsu_request_body', 'instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'rsu_id' in local_var_params:
            path_params['rsu_id'] = local_var_params['rsu_id']

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v1/{project_id}/rsus/{rsu_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateRsuResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def send_immediate_event(self, request):
        """创建即时交通事件

        创建即时交通事件，平台分发即时交通事件给目标设备的接口。事件一旦创建便会立即下发且只会下发一次。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SendImmediateEvent
        :type request: :class:`huaweicloudsdkdris.v1.SendImmediateEventRequest`
        :rtype: :class:`huaweicloudsdkdris.v1.SendImmediateEventResponse`
        """
        return self.send_immediate_event_with_http_info(request)

    def send_immediate_event_with_http_info(self, request):
        all_params = ['send_immediate_event_request_body', 'instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v1/{project_id}/immediate-event',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='SendImmediateEventResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_show_traffic_events(self, request):
        """查询长期交通事件列表

        条件查询交通事件
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchShowTrafficEvents
        :type request: :class:`huaweicloudsdkdris.v1.BatchShowTrafficEventsRequest`
        :rtype: :class:`huaweicloudsdkdris.v1.BatchShowTrafficEventsResponse`
        """
        return self.batch_show_traffic_events_with_http_info(request)

    def batch_show_traffic_events_with_http_info(self, request):
        all_params = ['instance_id', 'offset', 'limit', 'area_code', 'status', 'event_type', 'event_source_type', 'event_class', 'event_id', 'from_time', 'to_time', 'sort_key', 'sort_dir']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'area_code' in local_var_params:
            query_params.append(('area_code', local_var_params['area_code']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'event_type' in local_var_params:
            query_params.append(('event_type', local_var_params['event_type']))
        if 'event_source_type' in local_var_params:
            query_params.append(('event_source_type', local_var_params['event_source_type']))
            collection_formats['event_source_type'] = 'csv'
        if 'event_class' in local_var_params:
            query_params.append(('event_class', local_var_params['event_class']))
        if 'event_id' in local_var_params:
            query_params.append(('event_id', local_var_params['event_id']))
        if 'from_time' in local_var_params:
            query_params.append(('from_time', local_var_params['from_time']))
        if 'to_time' in local_var_params:
            query_params.append(('to_time', local_var_params['to_time']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v1/{project_id}/traffic-events',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchShowTrafficEventsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_traffic_event(self, request):
        """创建长期交通事件

        创建长期交通事件时，平台根据事件的起始时间和结束时间确定当前长期交通事件的状态。对于活跃状态的交通事件会立即下发给在事件影响范围内的RSU，对于未来事件则是在事件开始时间点下发到在事件影响范围内的RSU，过期事件不会下发。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateTrafficEvent
        :type request: :class:`huaweicloudsdkdris.v1.CreateTrafficEventRequest`
        :rtype: :class:`huaweicloudsdkdris.v1.CreateTrafficEventResponse`
        """
        return self.create_traffic_event_with_http_info(request)

    def create_traffic_event_with_http_info(self, request):
        all_params = ['create_traffic_event_request_body', 'instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v1/{project_id}/traffic-events',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateTrafficEventResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_traffic_event(self, request):
        """删除长期交通事件

        刪除长期交通事件
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteTrafficEvent
        :type request: :class:`huaweicloudsdkdris.v1.DeleteTrafficEventRequest`
        :rtype: :class:`huaweicloudsdkdris.v1.DeleteTrafficEventResponse`
        """
        return self.delete_traffic_event_with_http_info(request)

    def delete_traffic_event_with_http_info(self, request):
        all_params = ['event_id', 'instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'event_id' in local_var_params:
            path_params['event_id'] = local_var_params['event_id']

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v1/{project_id}/traffic-events/{event_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteTrafficEventResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_traffic_event(self, request):
        """查询长期交通事件

        查询长期交通事件
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowTrafficEvent
        :type request: :class:`huaweicloudsdkdris.v1.ShowTrafficEventRequest`
        :rtype: :class:`huaweicloudsdkdris.v1.ShowTrafficEventResponse`
        """
        return self.show_traffic_event_with_http_info(request)

    def show_traffic_event_with_http_info(self, request):
        all_params = ['event_id', 'instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'event_id' in local_var_params:
            path_params['event_id'] = local_var_params['event_id']

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v1/{project_id}/traffic-events/{event_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowTrafficEventResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_traffic_event(self, request):
        """修改长期交通事件

        修改长期交通事件
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateTrafficEvent
        :type request: :class:`huaweicloudsdkdris.v1.UpdateTrafficEventRequest`
        :rtype: :class:`huaweicloudsdkdris.v1.UpdateTrafficEventResponse`
        """
        return self.update_traffic_event_with_http_info(request)

    def update_traffic_event_with_http_info(self, request):
        all_params = ['event_id', 'update_traffic_event_request_body', 'instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'event_id' in local_var_params:
            path_params['event_id'] = local_var_params['event_id']

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v1/{project_id}/traffic-events/{event_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateTrafficEventResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_show_traffic_controllers(self, request):
        """查询信号机列表

        查询信号机列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchShowTrafficControllers
        :type request: :class:`huaweicloudsdkdris.v1.BatchShowTrafficControllersRequest`
        :rtype: :class:`huaweicloudsdkdris.v1.BatchShowTrafficControllersResponse`
        """
        return self.batch_show_traffic_controllers_with_http_info(request)

    def batch_show_traffic_controllers_with_http_info(self, request):
        all_params = ['instance_id', 'offset', 'limit', 'traffic_controller_id', 'esn', 'status']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'traffic_controller_id' in local_var_params:
            query_params.append(('traffic_controller_id', local_var_params['traffic_controller_id']))
        if 'esn' in local_var_params:
            query_params.append(('esn', local_var_params['esn']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/traffic-controllers',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchShowTrafficControllersResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_traffic_controller(self, request):
        """创建信号机

        创建信号机
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateTrafficController
        :type request: :class:`huaweicloudsdkdris.v1.CreateTrafficControllerRequest`
        :rtype: :class:`huaweicloudsdkdris.v1.CreateTrafficControllerResponse`
        """
        return self.create_traffic_controller_with_http_info(request)

    def create_traffic_controller_with_http_info(self, request):
        all_params = ['instance_id', 'create_traffic_controller_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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
            resource_path='/v1/{project_id}/traffic-controllers',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateTrafficControllerResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_traffic_controller(self, request):
        """删除信号机

        删除信号机
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteTrafficController
        :type request: :class:`huaweicloudsdkdris.v1.DeleteTrafficControllerRequest`
        :rtype: :class:`huaweicloudsdkdris.v1.DeleteTrafficControllerResponse`
        """
        return self.delete_traffic_controller_with_http_info(request)

    def delete_traffic_controller_with_http_info(self, request):
        all_params = ['traffic_controller_id', 'instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'traffic_controller_id' in local_var_params:
            path_params['traffic_controller_id'] = local_var_params['traffic_controller_id']

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/traffic-controllers/{traffic_controller_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteTrafficControllerResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_traffic_controller(self, request):
        """修改信号机

        修改信号机
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateTrafficController
        :type request: :class:`huaweicloudsdkdris.v1.UpdateTrafficControllerRequest`
        :rtype: :class:`huaweicloudsdkdris.v1.UpdateTrafficControllerResponse`
        """
        return self.update_traffic_controller_with_http_info(request)

    def update_traffic_controller_with_http_info(self, request):
        all_params = ['traffic_controller_id', 'update_traffic_controller_request_body', 'instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'traffic_controller_id' in local_var_params:
            path_params['traffic_controller_id'] = local_var_params['traffic_controller_id']

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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
            resource_path='/v1/{project_id}/traffic-controllers/{traffic_controller_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateTrafficControllerResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_v2x_edge_app(self, request):
        """部署边缘应用

        **部署边缘应用前需确保**：
        
        - Edge已创建且处于在线状态。相关方法请参见：[创建Edge](https://support.huaweicloud.com/api-v2x/v2x_04_0078.html)，[查询Edge](https://support.huaweicloud.com/api-v2x/v2x_04_0003.html)。
        
        - 待部署的应用已创建且应用版本状态已更新至发布。相关方法请参见：[创建应用](https://support.huaweicloud.com/api-v2x/v2x_04_0026.html)，[创建应用版本](https://support.huaweicloud.com/api-v2x/v2x_04_0038.html)，[更新应用版本状态](https://support.huaweicloud.com/api-v2x/v2x_04_0105.html)
        
        如部署边缘应用接口调用成功，稍后将会自动安装至边缘设备无需手动操作。自动安装完成后应用将处于运行中的状态。
        
        **关于应用在设备侧部署的耗时问题**：
        
        &amp;emsp;&amp;emsp;从边缘应用部署成功到处于运行中状态的耗时取决于边缘设备所处的网络状况以及应用镜像包的大小，可通过查询边缘应用获取边缘应用部署状态。相关方法请参见：[查询边缘应用](https://support.huaweicloud.com/api-v2x/v2x_04_0115.html)\&quot;
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateV2xEdgeApp
        :type request: :class:`huaweicloudsdkdris.v1.CreateV2xEdgeAppRequest`
        :rtype: :class:`huaweicloudsdkdris.v1.CreateV2xEdgeAppResponse`
        """
        return self.create_v2x_edge_app_with_http_info(request)

    def create_v2x_edge_app_with_http_info(self, request):
        all_params = ['v2x_edge_id', 'create_v2x_edge_app_request_body', 'instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'v2x_edge_id' in local_var_params:
            path_params['v2x_edge_id'] = local_var_params['v2x_edge_id']

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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
            resource_path='/v1/{project_id}/v2x-edges/{v2x_edge_id}/apps',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateV2xEdgeAppResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_v2_x_edge_app_by_edge_app_id(self, request):
        """删除边缘应用

        删除系统应用（$edgetepa）前应先删除业务通道。如删除边缘应用接口调用成功，稍后边缘设备将会自动删除应用无需手动操作。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteV2XEdgeAppByEdgeAppId
        :type request: :class:`huaweicloudsdkdris.v1.DeleteV2XEdgeAppByEdgeAppIdRequest`
        :rtype: :class:`huaweicloudsdkdris.v1.DeleteV2XEdgeAppByEdgeAppIdResponse`
        """
        return self.delete_v2_x_edge_app_by_edge_app_id_with_http_info(request)

    def delete_v2_x_edge_app_by_edge_app_id_with_http_info(self, request):
        all_params = ['edge_app_id', 'v2x_edge_id', 'instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'edge_app_id' in local_var_params:
            path_params['edge_app_id'] = local_var_params['edge_app_id']
        if 'v2x_edge_id' in local_var_params:
            path_params['v2x_edge_id'] = local_var_params['v2x_edge_id']

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/v2x-edges/{v2x_edge_id}/apps/{edge_app_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteV2XEdgeAppByEdgeAppIdResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_v2x_edge_app(self, request):
        """查询边缘应用列表

        查询边缘应用列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListV2xEdgeApp
        :type request: :class:`huaweicloudsdkdris.v1.ListV2xEdgeAppRequest`
        :rtype: :class:`huaweicloudsdkdris.v1.ListV2xEdgeAppResponse`
        """
        return self.list_v2x_edge_app_with_http_info(request)

    def list_v2x_edge_app_with_http_info(self, request):
        all_params = ['v2x_edge_id', 'instance_id', 'offset', 'limit']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'v2x_edge_id' in local_var_params:
            path_params['v2x_edge_id'] = local_var_params['v2x_edge_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/v2x-edges/{v2x_edge_id}/apps',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListV2xEdgeAppResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_v2_x_edge_app_detail_by_edge_app_id(self, request):
        """查询边缘应用

        查询边缘应用
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowV2XEdgeAppDetailByEdgeAppId
        :type request: :class:`huaweicloudsdkdris.v1.ShowV2XEdgeAppDetailByEdgeAppIdRequest`
        :rtype: :class:`huaweicloudsdkdris.v1.ShowV2XEdgeAppDetailByEdgeAppIdResponse`
        """
        return self.show_v2_x_edge_app_detail_by_edge_app_id_with_http_info(request)

    def show_v2_x_edge_app_detail_by_edge_app_id_with_http_info(self, request):
        all_params = ['edge_app_id', 'v2x_edge_id', 'instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'edge_app_id' in local_var_params:
            path_params['edge_app_id'] = local_var_params['edge_app_id']
        if 'v2x_edge_id' in local_var_params:
            path_params['v2x_edge_id'] = local_var_params['v2x_edge_id']

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/v2x-edges/{v2x_edge_id}/apps/{edge_app_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowV2XEdgeAppDetailByEdgeAppIdResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_v2x_edge_app(self, request):
        """升级边缘应用

        **升级边缘应用前需确保**：
        
        - Edge处于在线状态。相关方法请参见：[查询Edge](https://support.huaweicloud.com/api-v2x/v2x_04_0003.html)。
        
        - 待升级的应用版本状态已更新至发布。相关方法请参见：[更新应用版本状态](https://support.huaweicloud.com/api-v2x/v2x_04_0105.html)
        
        如升级边缘应用接口调用成功，稍后边缘设备将会自动升级至新版本无需手动操作。自动安装完成后应用将处于运行中的状态。
        
        **关于应用在设备侧升级的耗时问题**：
        
        &amp;emsp;&amp;emsp;从边缘应用升级成功到处于运行中状态的耗时取决于边缘设备所处的网络状况以及应用镜像包的大小，可通过查询边缘应用获取边缘应用部署状态。相关方法请参见：[查询边缘应用](https://support.huaweicloud.com/api-v2x/v2x_04_0115.html)
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateV2xEdgeApp
        :type request: :class:`huaweicloudsdkdris.v1.UpdateV2xEdgeAppRequest`
        :rtype: :class:`huaweicloudsdkdris.v1.UpdateV2xEdgeAppResponse`
        """
        return self.update_v2x_edge_app_with_http_info(request)

    def update_v2x_edge_app_with_http_info(self, request):
        all_params = ['edge_app_id', 'v2x_edge_id', 'update_v2_x_edge_app_request_body', 'instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'edge_app_id' in local_var_params:
            path_params['edge_app_id'] = local_var_params['edge_app_id']
        if 'v2x_edge_id' in local_var_params:
            path_params['v2x_edge_id'] = local_var_params['v2x_edge_id']

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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
            resource_path='/v1/{project_id}/v2x-edges/{v2x_edge_id}/apps/{edge_app_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateV2xEdgeAppResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_show_vehicles(self, request):
        """查询车辆列表

        查询车辆列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchShowVehicles
        :type request: :class:`huaweicloudsdkdris.v1.BatchShowVehiclesRequest`
        :rtype: :class:`huaweicloudsdkdris.v1.BatchShowVehiclesResponse`
        """
        return self.batch_show_vehicles_with_http_info(request)

    def batch_show_vehicles_with_http_info(self, request):
        all_params = ['instance_id', 'offset', 'limit', 'vehicle_id', 'status']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'vehicle_id' in local_var_params:
            query_params.append(('vehicle_id', local_var_params['vehicle_id']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/vehicles',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchShowVehiclesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_vehicle(self, request):
        """创建车辆

        创建车辆
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateVehicle
        :type request: :class:`huaweicloudsdkdris.v1.CreateVehicleRequest`
        :rtype: :class:`huaweicloudsdkdris.v1.CreateVehicleResponse`
        """
        return self.create_vehicle_with_http_info(request)

    def create_vehicle_with_http_info(self, request):
        all_params = ['instance_id', 'create_vehicle_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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
            resource_path='/v1/{project_id}/vehicles',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateVehicleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_vehicle(self, request):
        """删除车辆

        删除车辆
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteVehicle
        :type request: :class:`huaweicloudsdkdris.v1.DeleteVehicleRequest`
        :rtype: :class:`huaweicloudsdkdris.v1.DeleteVehicleResponse`
        """
        return self.delete_vehicle_with_http_info(request)

    def delete_vehicle_with_http_info(self, request):
        all_params = ['vehicle_id', 'instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'vehicle_id' in local_var_params:
            path_params['vehicle_id'] = local_var_params['vehicle_id']

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/vehicles/{vehicle_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteVehicleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_vehicle(self, request):
        """修改车辆

        修改车辆
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateVehicle
        :type request: :class:`huaweicloudsdkdris.v1.UpdateVehicleRequest`
        :rtype: :class:`huaweicloudsdkdris.v1.UpdateVehicleResponse`
        """
        return self.update_vehicle_with_http_info(request)

    def update_vehicle_with_http_info(self, request):
        all_params = ['vehicle_id', 'update_vehicle_request_body', 'instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'vehicle_id' in local_var_params:
            path_params['vehicle_id'] = local_var_params['vehicle_id']

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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
            resource_path='/v1/{project_id}/vehicles/{vehicle_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateVehicleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_show_edge_apps(self, request):
        """查询应用列表

        查询应用列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchShowEdgeApps
        :type request: :class:`huaweicloudsdkdris.v1.BatchShowEdgeAppsRequest`
        :rtype: :class:`huaweicloudsdkdris.v1.BatchShowEdgeAppsResponse`
        """
        return self.batch_show_edge_apps_with_http_info(request)

    def batch_show_edge_apps_with_http_info(self, request):
        all_params = ['instance_id', 'edge_app_id', 'offset', 'limit']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'edge_app_id' in local_var_params:
            query_params.append(('edge_app_id', local_var_params['edge_app_id']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/v2x-edge-apps',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchShowEdgeAppsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_edge_app(self, request):
        """创建应用

        创建应用
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateEdgeApp
        :type request: :class:`huaweicloudsdkdris.v1.CreateEdgeAppRequest`
        :rtype: :class:`huaweicloudsdkdris.v1.CreateEdgeAppResponse`
        """
        return self.create_edge_app_with_http_info(request)

    def create_edge_app_with_http_info(self, request):
        all_params = ['create_edge_app_request_body', 'instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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
            resource_path='/v1/{project_id}/v2x-edge-apps',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateEdgeAppResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_edge_app(self, request):
        """删除应用

        删除应用
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteEdgeApp
        :type request: :class:`huaweicloudsdkdris.v1.DeleteEdgeAppRequest`
        :rtype: :class:`huaweicloudsdkdris.v1.DeleteEdgeAppResponse`
        """
        return self.delete_edge_app_with_http_info(request)

    def delete_edge_app_with_http_info(self, request):
        all_params = ['edge_app_id', 'instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'edge_app_id' in local_var_params:
            path_params['edge_app_id'] = local_var_params['edge_app_id']

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/v2x-edge-apps/{edge_app_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteEdgeAppResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_edge_app(self, request):
        """修改应用

        修改应用
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateEdgeApp
        :type request: :class:`huaweicloudsdkdris.v1.UpdateEdgeAppRequest`
        :rtype: :class:`huaweicloudsdkdris.v1.UpdateEdgeAppResponse`
        """
        return self.update_edge_app_with_http_info(request)

    def update_edge_app_with_http_info(self, request):
        all_params = ['edge_app_id', 'update_edge_app_request_body', 'instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'edge_app_id' in local_var_params:
            path_params['edge_app_id'] = local_var_params['edge_app_id']

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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
            resource_path='/v1/{project_id}/v2x-edge-apps/{edge_app_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateEdgeAppResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_show_edge_app_versions(self, request):
        """查询应用版本列表

        查询应用版本列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchShowEdgeAppVersions
        :type request: :class:`huaweicloudsdkdris.v1.BatchShowEdgeAppVersionsRequest`
        :rtype: :class:`huaweicloudsdkdris.v1.BatchShowEdgeAppVersionsResponse`
        """
        return self.batch_show_edge_app_versions_with_http_info(request)

    def batch_show_edge_app_versions_with_http_info(self, request):
        all_params = ['edge_app_id', 'instance_id', 'version', 'offset', 'limit', 'state']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'edge_app_id' in local_var_params:
            path_params['edge_app_id'] = local_var_params['edge_app_id']

        query_params = []
        if 'version' in local_var_params:
            query_params.append(('version', local_var_params['version']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'state' in local_var_params:
            query_params.append(('state', local_var_params['state']))

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/v2x-edge-apps/{edge_app_id}/versions',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchShowEdgeAppVersionsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_edge_application_version(self, request):
        """创建应用版本

        创建应用版本
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateEdgeApplicationVersion
        :type request: :class:`huaweicloudsdkdris.v1.CreateEdgeApplicationVersionRequest`
        :rtype: :class:`huaweicloudsdkdris.v1.CreateEdgeApplicationVersionResponse`
        """
        return self.create_edge_application_version_with_http_info(request)

    def create_edge_application_version_with_http_info(self, request):
        all_params = ['edge_app_id', 'create_edge_application_version_request_body', 'instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'edge_app_id' in local_var_params:
            path_params['edge_app_id'] = local_var_params['edge_app_id']

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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
            resource_path='/v1/{project_id}/v2x-edge-apps/{edge_app_id}/versions',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateEdgeApplicationVersionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_edge_application_version(self, request):
        """删除应用版本

        删除应用版本
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteEdgeApplicationVersion
        :type request: :class:`huaweicloudsdkdris.v1.DeleteEdgeApplicationVersionRequest`
        :rtype: :class:`huaweicloudsdkdris.v1.DeleteEdgeApplicationVersionResponse`
        """
        return self.delete_edge_application_version_with_http_info(request)

    def delete_edge_application_version_with_http_info(self, request):
        all_params = ['edge_app_id', 'version', 'instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'edge_app_id' in local_var_params:
            path_params['edge_app_id'] = local_var_params['edge_app_id']
        if 'version' in local_var_params:
            path_params['version'] = local_var_params['version']

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/v2x-edge-apps/{edge_app_id}/versions/{version}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteEdgeApplicationVersionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_edge_application_version(self, request):
        """查询应用版本

        查询应用版本
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowEdgeApplicationVersion
        :type request: :class:`huaweicloudsdkdris.v1.ShowEdgeApplicationVersionRequest`
        :rtype: :class:`huaweicloudsdkdris.v1.ShowEdgeApplicationVersionResponse`
        """
        return self.show_edge_application_version_with_http_info(request)

    def show_edge_application_version_with_http_info(self, request):
        all_params = ['edge_app_id', 'version', 'instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'edge_app_id' in local_var_params:
            path_params['edge_app_id'] = local_var_params['edge_app_id']
        if 'version' in local_var_params:
            path_params['version'] = local_var_params['version']

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/v2x-edge-apps/{edge_app_id}/versions/{version}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowEdgeApplicationVersionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_edge_application_version(self, request):
        """修改应用版本

        修改应用版本
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateEdgeApplicationVersion
        :type request: :class:`huaweicloudsdkdris.v1.UpdateEdgeApplicationVersionRequest`
        :rtype: :class:`huaweicloudsdkdris.v1.UpdateEdgeApplicationVersionResponse`
        """
        return self.update_edge_application_version_with_http_info(request)

    def update_edge_application_version_with_http_info(self, request):
        all_params = ['edge_app_id', 'version', 'update_edge_application_version_request_body', 'instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'edge_app_id' in local_var_params:
            path_params['edge_app_id'] = local_var_params['edge_app_id']
        if 'version' in local_var_params:
            path_params['version'] = local_var_params['version']

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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
            resource_path='/v1/{project_id}/v2x-edge-apps/{edge_app_id}/versions/{version}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateEdgeApplicationVersionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_edge_application_version_state(self, request):
        """更新应用版本状态

        更新应用版本状态。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateEdgeApplicationVersionState
        :type request: :class:`huaweicloudsdkdris.v1.UpdateEdgeApplicationVersionStateRequest`
        :rtype: :class:`huaweicloudsdkdris.v1.UpdateEdgeApplicationVersionStateResponse`
        """
        return self.update_edge_application_version_state_with_http_info(request)

    def update_edge_application_version_state_with_http_info(self, request):
        all_params = ['edge_app_id', 'version', 'update_edge_application_version_state_request_body', 'instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'edge_app_id' in local_var_params:
            path_params['edge_app_id'] = local_var_params['edge_app_id']
        if 'version' in local_var_params:
            path_params['version'] = local_var_params['version']

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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
            resource_path='/v1/{project_id}/v2x-edge-apps/{edge_app_id}/versions/{version}/state',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateEdgeApplicationVersionStateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_edge_flows(self, request):
        """查询历史交通统计信息列表

        查询历史交通统计信息列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListEdgeFlows
        :type request: :class:`huaweicloudsdkdris.v1.ListEdgeFlowsRequest`
        :rtype: :class:`huaweicloudsdkdris.v1.ListEdgeFlowsResponse`
        """
        return self.list_edge_flows_with_http_info(request)

    def list_edge_flows_with_http_info(self, request):
        all_params = ['instance_id', 'offset', 'limit', 'from_date', 'to_date', 'edge_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'from_date' in local_var_params:
            query_params.append(('from_date', local_var_params['from_date']))
        if 'to_date' in local_var_params:
            query_params.append(('to_date', local_var_params['to_date']))
        if 'edge_id' in local_var_params:
            query_params.append(('edge_id', local_var_params['edge_id']))

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/edge-flow',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListEdgeFlowsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_rsu_model(self, request):
        """创建RSU型号

        调用此接口可创建RSU型号。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateRsuModel
        :type request: :class:`huaweicloudsdkdris.v1.CreateRsuModelRequest`
        :rtype: :class:`huaweicloudsdkdris.v1.CreateRsuModelResponse`
        """
        return self.create_rsu_model_with_http_info(request)

    def create_rsu_model_with_http_info(self, request):
        all_params = ['instance_id', 'create_rsu_model_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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
            resource_path='/v1/{project_id}/rsu-models',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateRsuModelResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_rsu_model(self, request):
        """删除RSU型号

        可调用此接口删除已创建的RSU型号。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteRsuModel
        :type request: :class:`huaweicloudsdkdris.v1.DeleteRsuModelRequest`
        :rtype: :class:`huaweicloudsdkdris.v1.DeleteRsuModelResponse`
        """
        return self.delete_rsu_model_with_http_info(request)

    def delete_rsu_model_with_http_info(self, request):
        all_params = ['rsu_model_id', 'instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'rsu_model_id' in local_var_params:
            path_params['rsu_model_id'] = local_var_params['rsu_model_id']

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/rsu-models/{rsu_model_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteRsuModelResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_rsu_models(self, request):
        """查询RSU型号列表

        可调用此接口查询已创建RSU型号列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListRsuModels
        :type request: :class:`huaweicloudsdkdris.v1.ListRsuModelsRequest`
        :rtype: :class:`huaweicloudsdkdris.v1.ListRsuModelsResponse`
        """
        return self.list_rsu_models_with_http_info(request)

    def list_rsu_models_with_http_info(self, request):
        all_params = ['instance_id', 'limit', 'manufacturer_name', 'offset']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'manufacturer_name' in local_var_params:
            query_params.append(('manufacturer_name', local_var_params['manufacturer_name']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/rsu-models',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListRsuModelsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_rsu_model(self, request):
        """查询RSU型号

        可调用此接口查询已创建的RSU型号。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowRsuModel
        :type request: :class:`huaweicloudsdkdris.v1.ShowRsuModelRequest`
        :rtype: :class:`huaweicloudsdkdris.v1.ShowRsuModelResponse`
        """
        return self.show_rsu_model_with_http_info(request)

    def show_rsu_model_with_http_info(self, request):
        all_params = ['rsu_model_id', 'instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'rsu_model_id' in local_var_params:
            path_params['rsu_model_id'] = local_var_params['rsu_model_id']

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/rsu-models/{rsu_model_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowRsuModelResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_rsu_model(self, request):
        """修改RSU型号

        可调用此接口修改已创建的RSU型号。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateRsuModel
        :type request: :class:`huaweicloudsdkdris.v1.UpdateRsuModelRequest`
        :rtype: :class:`huaweicloudsdkdris.v1.UpdateRsuModelResponse`
        """
        return self.update_rsu_model_with_http_info(request)

    def update_rsu_model_with_http_info(self, request):
        all_params = ['rsu_model_id', 'update_rsu_model_request_body', 'instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'rsu_model_id' in local_var_params:
            path_params['rsu_model_id'] = local_var_params['rsu_model_id']

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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
            resource_path='/v1/{project_id}/rsu-models/{rsu_model_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateRsuModelResponse',
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

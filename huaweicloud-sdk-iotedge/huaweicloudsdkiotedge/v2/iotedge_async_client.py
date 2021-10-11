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


class IoTEdgeAsyncClient(Client):
    """
    :param configuration: .Configuration object for this client
    :param pool_threads: The number of threads to use for async requests
        to the API. More threads means more concurrent API requests.
    """

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
        super(IoTEdgeAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkiotedge.v2.model")
        self.preset_headers = {'User-Agent': 'HuaweiCloud-SDK-Python'}

    @classmethod
    def new_builder(cls, clazz=None):
        if clazz is None:
            return ClientBuilder(cls)

        if clazz.__name__ != "IoTEdgeClient":
            raise TypeError("client type error, support client type is IoTEdgeClient")

        return ClientBuilder(clazz)

    def create_edge_node_async(self, request):
        """创建边缘节点

        创建边缘节点

        :param CreateEdgeNodeRequest request
        :return: CreateEdgeNodeResponse
        """
        return self.create_edge_node_with_http_info(request)

    def create_edge_node_with_http_info(self, request):
        """创建边缘节点

        创建边缘节点

        :param CreateEdgeNodeRequest request
        :return: CreateEdgeNodeResponse
        """

        all_params = ['create_edge_node_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v2/{project_id}/edge-nodes',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateEdgeNodeResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_install_cmd_async(self, request):
        """生成边缘节点安装命令

        生成边缘节点安装命令，命令有效时间30分钟，超过后需要重新生成

        :param CreateInstallCmdRequest request
        :return: CreateInstallCmdResponse
        """
        return self.create_install_cmd_with_http_info(request)

    def create_install_cmd_with_http_info(self, request):
        """生成边缘节点安装命令

        生成边缘节点安装命令，命令有效时间30分钟，超过后需要重新生成

        :param CreateInstallCmdRequest request
        :return: CreateInstallCmdResponse
        """

        all_params = ['edge_node_id', 'arch']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'edge_node_id' in local_var_params:
            path_params['edge_node_id'] = local_var_params['edge_node_id']

        query_params = []
        if 'arch' in local_var_params:
            query_params.append(('arch', local_var_params['arch']))

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
            resource_path='/v2/{project_id}/edge-nodes/{edge_node_id}/install',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateInstallCmdResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_edge_node_async(self, request):
        """删除边缘节点

        删除指定边缘节点

        :param DeleteEdgeNodeRequest request
        :return: DeleteEdgeNodeResponse
        """
        return self.delete_edge_node_with_http_info(request)

    def delete_edge_node_with_http_info(self, request):
        """删除边缘节点

        删除指定边缘节点

        :param DeleteEdgeNodeRequest request
        :return: DeleteEdgeNodeResponse
        """

        all_params = ['edge_node_id', 'delete_external_node']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'edge_node_id' in local_var_params:
            path_params['edge_node_id'] = local_var_params['edge_node_id']

        query_params = []
        if 'delete_external_node' in local_var_params:
            query_params.append(('delete_external_node', local_var_params['delete_external_node']))

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
            resource_path='/v2/{project_id}/edge-nodes/{edge_node_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteEdgeNodeResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_edge_nodes_async(self, request):
        """查询边缘节点列表

        查询边缘节点列表

        :param ListEdgeNodesRequest request
        :return: ListEdgeNodesResponse
        """
        return self.list_edge_nodes_with_http_info(request)

    def list_edge_nodes_with_http_info(self, request):
        """查询边缘节点列表

        查询边缘节点列表

        :param ListEdgeNodesRequest request
        :return: ListEdgeNodesResponse
        """

        all_params = ['name', 'state', 'type', 'instance_id', 'space_id', 'node_ids', 'offset', 'limit']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'state' in local_var_params:
            query_params.append(('state', local_var_params['state']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'instance_id' in local_var_params:
            query_params.append(('instance_id', local_var_params['instance_id']))
        if 'space_id' in local_var_params:
            query_params.append(('space_id', local_var_params['space_id']))
        if 'node_ids' in local_var_params:
            query_params.append(('node_ids', local_var_params['node_ids']))
            collection_formats['node_ids'] = 'csv'
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

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
            resource_path='/v2/{project_id}/edge-nodes',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListEdgeNodesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_edge_node_async(self, request):
        """查询边缘节点详情

        查询边缘节点详情

        :param ShowEdgeNodeRequest request
        :return: ShowEdgeNodeResponse
        """
        return self.show_edge_node_with_http_info(request)

    def show_edge_node_with_http_info(self, request):
        """查询边缘节点详情

        查询边缘节点详情

        :param ShowEdgeNodeRequest request
        :return: ShowEdgeNodeResponse
        """

        all_params = ['edge_node_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'edge_node_id' in local_var_params:
            path_params['edge_node_id'] = local_var_params['edge_node_id']

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
            resource_path='/v2/{project_id}/edge-nodes/{edge_node_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowEdgeNodeResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def add_device_async(self, request):
        """添加设备

        添加设备

        :param AddDeviceRequest request
        :return: AddDeviceResponse
        """
        return self.add_device_with_http_info(request)

    def add_device_with_http_info(self, request):
        """添加设备

        添加设备

        :param AddDeviceRequest request
        :return: AddDeviceResponse
        """

        all_params = ['edge_node_id', 'add_device_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'edge_node_id' in local_var_params:
            path_params['edge_node_id'] = local_var_params['edge_node_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/edge-nodes/{edge_node_id}/devices',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='AddDeviceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def batch_update_configs_async(self, request):
        """批量修改子设备协议配置

        批量修改产品关联的设备，传入product_id修改该产品下所有设备，传入device_id列表，根据device_id修改,两者互斥。

        :param BatchUpdateConfigsRequest request
        :return: BatchUpdateConfigsResponse
        """
        return self.batch_update_configs_with_http_info(request)

    def batch_update_configs_with_http_info(self, request):
        """批量修改子设备协议配置

        批量修改产品关联的设备，传入product_id修改该产品下所有设备，传入device_id列表，根据device_id修改,两者互斥。

        :param BatchUpdateConfigsRequest request
        :return: BatchUpdateConfigsResponse
        """

        all_params = ['batch_update_configs_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/devices/batch-configs',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='BatchUpdateConfigsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_access_code_async(self, request):
        """生成modbus协议设备接入码

        生成modbus协议设备接入码

        :param CreateAccessCodeRequest request
        :return: CreateAccessCodeResponse
        """
        return self.create_access_code_with_http_info(request)

    def create_access_code_with_http_info(self, request):
        """生成modbus协议设备接入码

        生成modbus协议设备接入码

        :param CreateAccessCodeRequest request
        :return: CreateAccessCodeResponse
        """

        all_params = ['edge_node_id', 'device_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'edge_node_id' in local_var_params:
            path_params['edge_node_id'] = local_var_params['edge_node_id']
        if 'device_id' in local_var_params:
            path_params['device_id'] = local_var_params['device_id']

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
            resource_path='/v2/{project_id}/edge-nodes/{edge_node_id}/devices/{device_id}/access-code',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateAccessCodeResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_device_async(self, request):
        """删除设备

        删除设备

        :param DeleteDeviceRequest request
        :return: DeleteDeviceResponse
        """
        return self.delete_device_with_http_info(request)

    def delete_device_with_http_info(self, request):
        """删除设备

        删除设备

        :param DeleteDeviceRequest request
        :return: DeleteDeviceResponse
        """

        all_params = ['edge_node_id', 'device_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'edge_node_id' in local_var_params:
            path_params['edge_node_id'] = local_var_params['edge_node_id']
        if 'device_id' in local_var_params:
            path_params['device_id'] = local_var_params['device_id']

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
            resource_path='/v2/{project_id}/edge-nodes/{edge_node_id}/devices/{device_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteDeviceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_devices_async(self, request):
        """查询设备列表

        查询设备列表

        :param ListDevicesRequest request
        :return: ListDevicesResponse
        """
        return self.list_devices_with_http_info(request)

    def list_devices_with_http_info(self, request):
        """查询设备列表

        查询设备列表

        :param ListDevicesRequest request
        :return: ListDevicesResponse
        """

        all_params = ['edge_node_id', 'gateway_id', 'device_name', 'offset', 'limit']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'edge_node_id' in local_var_params:
            path_params['edge_node_id'] = local_var_params['edge_node_id']

        query_params = []
        if 'gateway_id' in local_var_params:
            query_params.append(('gateway_id', local_var_params['gateway_id']))
        if 'device_name' in local_var_params:
            query_params.append(('device_name', local_var_params['device_name']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

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
            resource_path='/v2/{project_id}/edge-nodes/{edge_node_id}/devices',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListDevicesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_product_config_async(self, request):
        """获取协议配置

        获取协议配置

        :param ShowProductConfigRequest request
        :return: ShowProductConfigResponse
        """
        return self.show_product_config_with_http_info(request)

    def show_product_config_with_http_info(self, request):
        """获取协议配置

        获取协议配置

        :param ShowProductConfigRequest request
        :return: ShowProductConfigResponse
        """

        all_params = ['protocol_type']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'protocol_type' in local_var_params:
            query_params.append(('protocol_type', local_var_params['protocol_type']))

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
            resource_path='/v2/{project_id}/protocol-configs',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowProductConfigResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_protocol_mappings_async(self, request):
        """获取协议映射文件

        获取协议映射文件

        :param ShowProtocolMappingsRequest request
        :return: ShowProtocolMappingsResponse
        """
        return self.show_protocol_mappings_with_http_info(request)

    def show_protocol_mappings_with_http_info(self, request):
        """获取协议映射文件

        获取协议映射文件

        :param ShowProtocolMappingsRequest request
        :return: ShowProtocolMappingsResponse
        """

        all_params = ['product_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'product_id' in local_var_params:
            path_params['product_id'] = local_var_params['product_id']

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
            resource_path='/v2/{project_id}/products/{product_id}/protocol-mappings',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowProtocolMappingsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_device_async(self, request):
        """修改设备

        修改设备

        :param UpdateDeviceRequest request
        :return: UpdateDeviceResponse
        """
        return self.update_device_with_http_info(request)

    def update_device_with_http_info(self, request):
        """修改设备

        修改设备

        :param UpdateDeviceRequest request
        :return: UpdateDeviceResponse
        """

        all_params = ['edge_node_id', 'device_id', 'update_device_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'edge_node_id' in local_var_params:
            path_params['edge_node_id'] = local_var_params['edge_node_id']
        if 'device_id' in local_var_params:
            path_params['device_id'] = local_var_params['device_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/edge-nodes/{edge_node_id}/devices/{device_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateDeviceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def upload_protocol_mappings_async(self, request):
        """上传协议映射文件

        上传协议映射文件

        :param UploadProtocolMappingsRequest request
        :return: UploadProtocolMappingsResponse
        """
        return self.upload_protocol_mappings_with_http_info(request)

    def upload_protocol_mappings_with_http_info(self, request):
        """上传协议映射文件

        上传协议映射文件

        :param UploadProtocolMappingsRequest request
        :return: UploadProtocolMappingsResponse
        """

        all_params = ['product_id', 'file']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'product_id' in local_var_params:
            path_params['product_id'] = local_var_params['product_id']

        query_params = []

        header_params = {}

        form_params = {}
        if 'file' in local_var_params:
            form_params['file'] = local_var_params['file']

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['multipart/form-data'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/products/{product_id}/protocol-mappings',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UploadProtocolMappingsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def batch_list_edge_apps_async(self, request):
        """查询应用列表

        查询应用列表

        :param BatchListEdgeAppsRequest request
        :return: BatchListEdgeAppsResponse
        """
        return self.batch_list_edge_apps_with_http_info(request)

    def batch_list_edge_apps_with_http_info(self, request):
        """查询应用列表

        查询应用列表

        :param BatchListEdgeAppsRequest request
        :return: BatchListEdgeAppsResponse
        """

        all_params = ['edge_app_id', 'offset', 'limit', 'app_type', 'function_type']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'edge_app_id' in local_var_params:
            query_params.append(('edge_app_id', local_var_params['edge_app_id']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'app_type' in local_var_params:
            query_params.append(('app_type', local_var_params['app_type']))
        if 'function_type' in local_var_params:
            query_params.append(('function_type', local_var_params['function_type']))

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
            resource_path='/v2/{project_id}/edge-apps',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='BatchListEdgeAppsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_edge_app_async(self, request):
        """创建应用

        创建应用

        :param CreateEdgeAppRequest request
        :return: CreateEdgeAppResponse
        """
        return self.create_edge_app_with_http_info(request)

    def create_edge_app_with_http_info(self, request):
        """创建应用

        创建应用

        :param CreateEdgeAppRequest request
        :return: CreateEdgeAppResponse
        """

        all_params = ['create_edge_app_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v2/{project_id}/edge-apps',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateEdgeAppResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_edge_app_async(self, request):
        """删除应用

        删除应用

        :param DeleteEdgeAppRequest request
        :return: DeleteEdgeAppResponse
        """
        return self.delete_edge_app_with_http_info(request)

    def delete_edge_app_with_http_info(self, request):
        """删除应用

        删除应用

        :param DeleteEdgeAppRequest request
        :return: DeleteEdgeAppResponse
        """

        all_params = ['edge_app_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'edge_app_id' in local_var_params:
            path_params['edge_app_id'] = local_var_params['edge_app_id']

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
            resource_path='/v2/{project_id}/edge-apps/{edge_app_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteEdgeAppResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_edge_app_async(self, request):
        """查询应用

        查询应用

        :param ShowEdgeAppRequest request
        :return: ShowEdgeAppResponse
        """
        return self.show_edge_app_with_http_info(request)

    def show_edge_app_with_http_info(self, request):
        """查询应用

        查询应用

        :param ShowEdgeAppRequest request
        :return: ShowEdgeAppResponse
        """

        all_params = ['edge_app_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'edge_app_id' in local_var_params:
            path_params['edge_app_id'] = local_var_params['edge_app_id']

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
            resource_path='/v2/{project_id}/edge-apps/{edge_app_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowEdgeAppResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def batch_list_edge_app_versions_async(self, request):
        """查询应用版本列表

        查询应用版本列表

        :param BatchListEdgeAppVersionsRequest request
        :return: BatchListEdgeAppVersionsResponse
        """
        return self.batch_list_edge_app_versions_with_http_info(request)

    def batch_list_edge_app_versions_with_http_info(self, request):
        """查询应用版本列表

        查询应用版本列表

        :param BatchListEdgeAppVersionsRequest request
        :return: BatchListEdgeAppVersionsResponse
        """

        all_params = ['edge_app_id', 'version', 'offset', 'limit', 'ai_card_type', 'arch', 'state']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
        if 'ai_card_type' in local_var_params:
            query_params.append(('ai_card_type', local_var_params['ai_card_type']))
        if 'arch' in local_var_params:
            query_params.append(('arch', local_var_params['arch']))
        if 'state' in local_var_params:
            query_params.append(('state', local_var_params['state']))

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
            resource_path='/v2/{project_id}/edge-apps/{edge_app_id}/versions',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='BatchListEdgeAppVersionsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_edge_application_version_async(self, request):
        """创建应用版本

        创建应用版本

        :param CreateEdgeApplicationVersionRequest request
        :return: CreateEdgeApplicationVersionResponse
        """
        return self.create_edge_application_version_with_http_info(request)

    def create_edge_application_version_with_http_info(self, request):
        """创建应用版本

        创建应用版本

        :param CreateEdgeApplicationVersionRequest request
        :return: CreateEdgeApplicationVersionResponse
        """

        all_params = ['edge_app_id', 'create_edge_application_version_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'edge_app_id' in local_var_params:
            path_params['edge_app_id'] = local_var_params['edge_app_id']

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
            resource_path='/v2/{project_id}/edge-apps/{edge_app_id}/versions',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateEdgeApplicationVersionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_edge_application_version_async(self, request):
        """删除应用版本

        删除应用版本

        :param DeleteEdgeApplicationVersionRequest request
        :return: DeleteEdgeApplicationVersionResponse
        """
        return self.delete_edge_application_version_with_http_info(request)

    def delete_edge_application_version_with_http_info(self, request):
        """删除应用版本

        删除应用版本

        :param DeleteEdgeApplicationVersionRequest request
        :return: DeleteEdgeApplicationVersionResponse
        """

        all_params = ['edge_app_id', 'version']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'edge_app_id' in local_var_params:
            path_params['edge_app_id'] = local_var_params['edge_app_id']
        if 'version' in local_var_params:
            path_params['version'] = local_var_params['version']

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
            resource_path='/v2/{project_id}/edge-apps/{edge_app_id}/versions/{version}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteEdgeApplicationVersionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_edge_application_version_async(self, request):
        """查询应用版本详情

        查询应用版本详情

        :param ShowEdgeApplicationVersionRequest request
        :return: ShowEdgeApplicationVersionResponse
        """
        return self.show_edge_application_version_with_http_info(request)

    def show_edge_application_version_with_http_info(self, request):
        """查询应用版本详情

        查询应用版本详情

        :param ShowEdgeApplicationVersionRequest request
        :return: ShowEdgeApplicationVersionResponse
        """

        all_params = ['edge_app_id', 'version']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'edge_app_id' in local_var_params:
            path_params['edge_app_id'] = local_var_params['edge_app_id']
        if 'version' in local_var_params:
            path_params['version'] = local_var_params['version']

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
            resource_path='/v2/{project_id}/edge-apps/{edge_app_id}/versions/{version}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowEdgeApplicationVersionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_edge_application_version_async(self, request):
        """修改应用版本

        修改应用版本

        :param UpdateEdgeApplicationVersionRequest request
        :return: UpdateEdgeApplicationVersionResponse
        """
        return self.update_edge_application_version_with_http_info(request)

    def update_edge_application_version_with_http_info(self, request):
        """修改应用版本

        修改应用版本

        :param UpdateEdgeApplicationVersionRequest request
        :return: UpdateEdgeApplicationVersionResponse
        """

        all_params = ['edge_app_id', 'version', 'update_edge_application_version_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'edge_app_id' in local_var_params:
            path_params['edge_app_id'] = local_var_params['edge_app_id']
        if 'version' in local_var_params:
            path_params['version'] = local_var_params['version']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/edge-apps/{edge_app_id}/versions/{version}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateEdgeApplicationVersionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_edge_application_version_state_async(self, request):
        """更新应用版本状态

        更新应用版本状态。

        :param UpdateEdgeApplicationVersionStateRequest request
        :return: UpdateEdgeApplicationVersionStateResponse
        """
        return self.update_edge_application_version_state_with_http_info(request)

    def update_edge_application_version_state_with_http_info(self, request):
        """更新应用版本状态

        更新应用版本状态。

        :param UpdateEdgeApplicationVersionStateRequest request
        :return: UpdateEdgeApplicationVersionStateResponse
        """

        all_params = ['edge_app_id', 'version', 'update_edge_application_version_state_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'edge_app_id' in local_var_params:
            path_params['edge_app_id'] = local_var_params['edge_app_id']
        if 'version' in local_var_params:
            path_params['version'] = local_var_params['version']

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
            resource_path='/v2/{project_id}/edge-apps/{edge_app_id}/versions/{version}/state',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateEdgeApplicationVersionStateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_external_entity_async(self, request):
        """在指定节点上创建外部实体

        用户通过在指定边缘节点上设置外部实体的接入信息

        :param CreateExternalEntityRequest request
        :return: CreateExternalEntityResponse
        """
        return self.create_external_entity_with_http_info(request)

    def create_external_entity_with_http_info(self, request):
        """在指定节点上创建外部实体

        用户通过在指定边缘节点上设置外部实体的接入信息

        :param CreateExternalEntityRequest request
        :return: CreateExternalEntityResponse
        """

        all_params = ['edge_node_id', 'create_external_entity_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'edge_node_id' in local_var_params:
            path_params['edge_node_id'] = local_var_params['edge_node_id']

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
            resource_path='/v2/{project_id}/edge-nodes/{edge_node_id}/externals',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateExternalEntityResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_external_entity_async(self, request):
        """删除指定节点下外部实体

        删除节点下外部实体

        :param DeleteExternalEntityRequest request
        :return: DeleteExternalEntityResponse
        """
        return self.delete_external_entity_with_http_info(request)

    def delete_external_entity_with_http_info(self, request):
        """删除指定节点下外部实体

        删除节点下外部实体

        :param DeleteExternalEntityRequest request
        :return: DeleteExternalEntityResponse
        """

        all_params = ['edge_node_id', 'external_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'edge_node_id' in local_var_params:
            path_params['edge_node_id'] = local_var_params['edge_node_id']
        if 'external_id' in local_var_params:
            path_params['external_id'] = local_var_params['external_id']

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
            resource_path='/v2/{project_id}/edge-nodes/{edge_node_id}/externals/{external_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteExternalEntityResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_external_entity_async(self, request):
        """查询指定边缘节点下的外部实体

        用户在指定边缘节点上查询外部实体列表

        :param ListExternalEntityRequest request
        :return: ListExternalEntityResponse
        """
        return self.list_external_entity_with_http_info(request)

    def list_external_entity_with_http_info(self, request):
        """查询指定边缘节点下的外部实体

        用户在指定边缘节点上查询外部实体列表

        :param ListExternalEntityRequest request
        :return: ListExternalEntityResponse
        """

        all_params = ['edge_node_id', 'offset', 'limit']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'edge_node_id' in local_var_params:
            path_params['edge_node_id'] = local_var_params['edge_node_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

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
            resource_path='/v2/{project_id}/edge-nodes/{edge_node_id}/externals',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListExternalEntityResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_external_entity_async(self, request):
        """查询指定节点下指定外部实体的详情

        查询指定节点下指定外部实体的详情

        :param ShowExternalEntityRequest request
        :return: ShowExternalEntityResponse
        """
        return self.show_external_entity_with_http_info(request)

    def show_external_entity_with_http_info(self, request):
        """查询指定节点下指定外部实体的详情

        查询指定节点下指定外部实体的详情

        :param ShowExternalEntityRequest request
        :return: ShowExternalEntityResponse
        """

        all_params = ['edge_node_id', 'external_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'edge_node_id' in local_var_params:
            path_params['edge_node_id'] = local_var_params['edge_node_id']
        if 'external_id' in local_var_params:
            path_params['external_id'] = local_var_params['external_id']

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
            resource_path='/v2/{project_id}/edge-nodes/{edge_node_id}/externals/{external_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowExternalEntityResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_external_entity_async(self, request):
        """修改节点下指定的外部实体信息

        用户通过在指定边缘节点上修改指定外部实体的接入信息

        :param UpdateExternalEntityRequest request
        :return: UpdateExternalEntityResponse
        """
        return self.update_external_entity_with_http_info(request)

    def update_external_entity_with_http_info(self, request):
        """修改节点下指定的外部实体信息

        用户通过在指定边缘节点上修改指定外部实体的接入信息

        :param UpdateExternalEntityRequest request
        :return: UpdateExternalEntityResponse
        """

        all_params = ['edge_node_id', 'external_id', 'update_external_entity_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'edge_node_id' in local_var_params:
            path_params['edge_node_id'] = local_var_params['edge_node_id']
        if 'external_id' in local_var_params:
            path_params['external_id'] = local_var_params['external_id']

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
            resource_path='/v2/{project_id}/edge-nodes/{edge_node_id}/externals/{external_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateExternalEntityResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def batch_list_modules_async(self, request):
        """查询边缘模块列表

        用户通过Console接口查询指定边缘节点上边缘模块列表

        :param BatchListModulesRequest request
        :return: BatchListModulesResponse
        """
        return self.batch_list_modules_with_http_info(request)

    def batch_list_modules_with_http_info(self, request):
        """查询边缘模块列表

        用户通过Console接口查询指定边缘节点上边缘模块列表

        :param BatchListModulesRequest request
        :return: BatchListModulesResponse
        """

        all_params = ['edge_node_id', 'offset', 'limit', 'app_type', 'function_type']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'edge_node_id' in local_var_params:
            path_params['edge_node_id'] = local_var_params['edge_node_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'app_type' in local_var_params:
            query_params.append(('app_type', local_var_params['app_type']))
        if 'function_type' in local_var_params:
            query_params.append(('function_type', local_var_params['function_type']))

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
            resource_path='/v2/{project_id}/edge-nodes/{edge_node_id}/modules',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='BatchListModulesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_module_async(self, request):
        """创建边缘模块

        用户通过Console接口在指定边缘节点上创建边缘模块

        :param CreateModuleRequest request
        :return: CreateModuleResponse
        """
        return self.create_module_with_http_info(request)

    def create_module_with_http_info(self, request):
        """创建边缘模块

        用户通过Console接口在指定边缘节点上创建边缘模块

        :param CreateModuleRequest request
        :return: CreateModuleResponse
        """

        all_params = ['edge_node_id', 'create_module_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'edge_node_id' in local_var_params:
            path_params['edge_node_id'] = local_var_params['edge_node_id']

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
            resource_path='/v2/{project_id}/edge-nodes/{edge_node_id}/modules',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateModuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_module_async(self, request):
        """删除边缘模块

        用户通过过Console接口在指定边缘节点上删除边缘模块

        :param DeleteModuleRequest request
        :return: DeleteModuleResponse
        """
        return self.delete_module_with_http_info(request)

    def delete_module_with_http_info(self, request):
        """删除边缘模块

        用户通过过Console接口在指定边缘节点上删除边缘模块

        :param DeleteModuleRequest request
        :return: DeleteModuleResponse
        """

        all_params = ['edge_node_id', 'module_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'edge_node_id' in local_var_params:
            path_params['edge_node_id'] = local_var_params['edge_node_id']
        if 'module_id' in local_var_params:
            path_params['module_id'] = local_var_params['module_id']

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
            resource_path='/v2/{project_id}/edge-nodes/{edge_node_id}/modules/{module_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteModuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_module_async(self, request):
        """查询边缘模块

        用户通过Console接口查询指定边缘节点上指定边缘模块

        :param ShowModuleRequest request
        :return: ShowModuleResponse
        """
        return self.show_module_with_http_info(request)

    def show_module_with_http_info(self, request):
        """查询边缘模块

        用户通过Console接口查询指定边缘节点上指定边缘模块

        :param ShowModuleRequest request
        :return: ShowModuleResponse
        """

        all_params = ['edge_node_id', 'module_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'edge_node_id' in local_var_params:
            path_params['edge_node_id'] = local_var_params['edge_node_id']
        if 'module_id' in local_var_params:
            path_params['module_id'] = local_var_params['module_id']

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
            resource_path='/v2/{project_id}/edge-nodes/{edge_node_id}/modules/{module_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowModuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_module_async(self, request):
        """修改边缘模块

        用户通过Console接口查询指定边缘节点上指定边缘模块

        :param UpdateModuleRequest request
        :return: UpdateModuleResponse
        """
        return self.update_module_with_http_info(request)

    def update_module_with_http_info(self, request):
        """修改边缘模块

        用户通过Console接口查询指定边缘节点上指定边缘模块

        :param UpdateModuleRequest request
        :return: UpdateModuleResponse
        """

        all_params = ['edge_node_id', 'module_id', 'update_module_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'edge_node_id' in local_var_params:
            path_params['edge_node_id'] = local_var_params['edge_node_id']
        if 'module_id' in local_var_params:
            path_params['module_id'] = local_var_params['module_id']

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
            resource_path='/v2/{project_id}/edge-nodes/{edge_node_id}/modules/{module_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateModuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_routes_async(self, request):
        """查询边缘路由列表

        用户在指定边缘节点上查询边缘路由列表

        :param ListRoutesRequest request
        :return: ListRoutesResponse
        """
        return self.list_routes_with_http_info(request)

    def list_routes_with_http_info(self, request):
        """查询边缘路由列表

        用户在指定边缘节点上查询边缘路由列表

        :param ListRoutesRequest request
        :return: ListRoutesResponse
        """

        all_params = ['edge_node_id', 'parsed']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'edge_node_id' in local_var_params:
            path_params['edge_node_id'] = local_var_params['edge_node_id']

        query_params = []
        if 'parsed' in local_var_params:
            query_params.append(('parsed', local_var_params['parsed']))

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
            resource_path='/v2/{project_id}/edge-nodes/{edge_node_id}/routes',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListRoutesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_routes_async(self, request):
        """设置边缘路由

        用户通过在指定边缘节点上设置边缘路由

        :param UpdateRoutesRequest request
        :return: UpdateRoutesResponse
        """
        return self.update_routes_with_http_info(request)

    def update_routes_with_http_info(self, request):
        """设置边缘路由

        用户通过在指定边缘节点上设置边缘路由

        :param UpdateRoutesRequest request
        :return: UpdateRoutesResponse
        """

        all_params = ['edge_node_id', 'update_routes_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'edge_node_id' in local_var_params:
            path_params['edge_node_id'] = local_var_params['edge_node_id']

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
            resource_path='/v2/{project_id}/edge-nodes/{edge_node_id}/routes',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateRoutesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def batch_confirm_configs_new_async(self, request):
        """批量确认南向3rdIA配置项

        南向3rdIA对下发的配置项进行批量确认

        :param BatchConfirmConfigsNewRequest request
        :return: BatchConfirmConfigsNewResponse
        """
        return self.batch_confirm_configs_new_with_http_info(request)

    def batch_confirm_configs_new_with_http_info(self, request):
        """批量确认南向3rdIA配置项

        南向3rdIA对下发的配置项进行批量确认

        :param BatchConfirmConfigsNewRequest request
        :return: BatchConfirmConfigsNewResponse
        """

        all_params = ['node_id', 'ia_id', 'batch_confirm_configs_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'node_id' in local_var_params:
            path_params['node_id'] = local_var_params['node_id']
        if 'ia_id' in local_var_params:
            path_params['ia_id'] = local_var_params['ia_id']

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
            resource_path='/v2/{project_id}/edge-nodes/{node_id}/ias/{ia_id}/configs/batch-confirm',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='BatchConfirmConfigsNewResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def batch_import_configs_async(self, request):
        """批量导入南向3rdIA配置项

        批量导入南向3rdIA配置项

        :param BatchImportConfigsRequest request
        :return: BatchImportConfigsResponse
        """
        return self.batch_import_configs_with_http_info(request)

    def batch_import_configs_with_http_info(self, request):
        """批量导入南向3rdIA配置项

        批量导入南向3rdIA配置项

        :param BatchImportConfigsRequest request
        :return: BatchImportConfigsResponse
        """

        all_params = ['node_id', 'ia_id', 'batch_import_configs_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'node_id' in local_var_params:
            path_params['node_id'] = local_var_params['node_id']
        if 'ia_id' in local_var_params:
            path_params['ia_id'] = local_var_params['ia_id']

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
            resource_path='/v2/{project_id}/edge-nodes/{node_id}/ias/{ia_id}/configs/batch-import',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='BatchImportConfigsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_ia_config_async(self, request):
        """删除南向3rdIA配置项

        删除南向3rdIA配置项

        :param DeleteIaConfigRequest request
        :return: DeleteIaConfigResponse
        """
        return self.delete_ia_config_with_http_info(request)

    def delete_ia_config_with_http_info(self, request):
        """删除南向3rdIA配置项

        删除南向3rdIA配置项

        :param DeleteIaConfigRequest request
        :return: DeleteIaConfigResponse
        """

        all_params = ['node_id', 'ia_id', 'config_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'node_id' in local_var_params:
            path_params['node_id'] = local_var_params['node_id']
        if 'ia_id' in local_var_params:
            path_params['ia_id'] = local_var_params['ia_id']
        if 'config_id' in local_var_params:
            path_params['config_id'] = local_var_params['config_id']

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
            resource_path='/v2/{project_id}/edge-nodes/{node_id}/ias/{ia_id}/configs/{config_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteIaConfigResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_ia_configs_async(self, request):
        """查询南向3rdIA配置项列表

        查询南向3rdIA配置项列表

        :param ListIaConfigsRequest request
        :return: ListIaConfigsResponse
        """
        return self.list_ia_configs_with_http_info(request)

    def list_ia_configs_with_http_info(self, request):
        """查询南向3rdIA配置项列表

        查询南向3rdIA配置项列表

        :param ListIaConfigsRequest request
        :return: ListIaConfigsResponse
        """

        all_params = ['node_id', 'ia_id', 'offset', 'limit']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'node_id' in local_var_params:
            path_params['node_id'] = local_var_params['node_id']
        if 'ia_id' in local_var_params:
            path_params['ia_id'] = local_var_params['ia_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

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
            resource_path='/v2/{project_id}/edge-nodes/{node_id}/ias/{ia_id}/configs',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListIaConfigsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_ia_config_async(self, request):
        """查询南向3rdIA配置项详情

        查询南向3rdIA配置项详情

        :param ShowIaConfigRequest request
        :return: ShowIaConfigResponse
        """
        return self.show_ia_config_with_http_info(request)

    def show_ia_config_with_http_info(self, request):
        """查询南向3rdIA配置项详情

        查询南向3rdIA配置项详情

        :param ShowIaConfigRequest request
        :return: ShowIaConfigResponse
        """

        all_params = ['node_id', 'ia_id', 'config_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'node_id' in local_var_params:
            path_params['node_id'] = local_var_params['node_id']
        if 'ia_id' in local_var_params:
            path_params['ia_id'] = local_var_params['ia_id']
        if 'config_id' in local_var_params:
            path_params['config_id'] = local_var_params['config_id']

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
            resource_path='/v2/{project_id}/edge-nodes/{node_id}/ias/{ia_id}/configs/{config_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowIaConfigResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_ia_config_async(self, request):
        """创建&更新南向3rdIA配置项信息

        创建&更新南向3rdIA配置项信息

        :param UpdateIaConfigRequest request
        :return: UpdateIaConfigResponse
        """
        return self.update_ia_config_with_http_info(request)

    def update_ia_config_with_http_info(self, request):
        """创建&更新南向3rdIA配置项信息

        创建&更新南向3rdIA配置项信息

        :param UpdateIaConfigRequest request
        :return: UpdateIaConfigResponse
        """

        all_params = ['node_id', 'ia_id', 'config_id', 'update_ia_config_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'node_id' in local_var_params:
            path_params['node_id'] = local_var_params['node_id']
        if 'ia_id' in local_var_params:
            path_params['ia_id'] = local_var_params['ia_id']
        if 'config_id' in local_var_params:
            path_params['config_id'] = local_var_params['config_id']

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
            resource_path='/v2/{project_id}/edge-nodes/{node_id}/ias/{ia_id}/configs/{config_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateIaConfigResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def batch_associate_na_to_nodes_async(self, request):
        """授权北向NA信息到边缘节点

        批量授权北向NA信息到边缘节点。 已授权的边缘节点上的南向IA应用，可以通过部署在边缘节点上的api网关访问北向NA提供的接口。 

        :param BatchAssociateNaToNodesRequest request
        :return: BatchAssociateNaToNodesResponse
        """
        return self.batch_associate_na_to_nodes_with_http_info(request)

    def batch_associate_na_to_nodes_with_http_info(self, request):
        """授权北向NA信息到边缘节点

        批量授权北向NA信息到边缘节点。 已授权的边缘节点上的南向IA应用，可以通过部署在边缘节点上的api网关访问北向NA提供的接口。 

        :param BatchAssociateNaToNodesRequest request
        :return: BatchAssociateNaToNodesResponse
        """

        all_params = ['na_id', 'action', 'batch_authorize_na_to_nodes_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'na_id' in local_var_params:
            path_params['na_id'] = local_var_params['na_id']

        query_params = []
        if 'action' in local_var_params:
            query_params.append(('action', local_var_params['action']))

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
            resource_path='/v2/{project_id}/nas/{na_id}/nodes',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='BatchAssociateNaToNodesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_na_async(self, request):
        """删除北向NA信息

        删除北向NA信息，如果有边缘节点已分配该NA信息，会通知到该边缘节点。 

        :param DeleteNaRequest request
        :return: DeleteNaResponse
        """
        return self.delete_na_with_http_info(request)

    def delete_na_with_http_info(self, request):
        """删除北向NA信息

        删除北向NA信息，如果有边缘节点已分配该NA信息，会通知到该边缘节点。 

        :param DeleteNaRequest request
        :return: DeleteNaResponse
        """

        all_params = ['na_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'na_id' in local_var_params:
            path_params['na_id'] = local_var_params['na_id']

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
            resource_path='/v2/{project_id}/nas/{na_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteNaResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_na_authorized_nodes_async(self, request):
        """查询该北向NA信息的已分配节点

        查询该北向NA信息的已分配节点

        :param ListNaAuthorizedNodesRequest request
        :return: ListNaAuthorizedNodesResponse
        """
        return self.list_na_authorized_nodes_with_http_info(request)

    def list_na_authorized_nodes_with_http_info(self, request):
        """查询该北向NA信息的已分配节点

        查询该北向NA信息的已分配节点

        :param ListNaAuthorizedNodesRequest request
        :return: ListNaAuthorizedNodesResponse
        """

        all_params = ['na_id', 'offset', 'limit']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'na_id' in local_var_params:
            path_params['na_id'] = local_var_params['na_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

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
            resource_path='/v2/{project_id}/nas/{na_id}/nodes',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListNaAuthorizedNodesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_nas_async(self, request):
        """查询北向NA信息列表

        查询北向NA信息列表

        :param ListNasRequest request
        :return: ListNasResponse
        """
        return self.list_nas_with_http_info(request)

    def list_nas_with_http_info(self, request):
        """查询北向NA信息列表

        查询北向NA信息列表

        :param ListNasRequest request
        :return: ListNasResponse
        """

        all_params = ['name', 'offset', 'limit']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/nas',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListNasResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_na_async(self, request):
        """查询北向NA信息详情

        查询北向NA信息详情

        :param ShowNaRequest request
        :return: ShowNaResponse
        """
        return self.show_na_with_http_info(request)

    def show_na_with_http_info(self, request):
        """查询北向NA信息详情

        查询北向NA信息详情

        :param ShowNaRequest request
        :return: ShowNaResponse
        """

        all_params = ['na_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'na_id' in local_var_params:
            path_params['na_id'] = local_var_params['na_id']

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
            resource_path='/v2/{project_id}/nas/{na_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowNaResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_na_async(self, request):
        """创建&更新北向NA信息

        创建&更新北向NA信息，当更新北向NA信息时，会通知到已分配该北向NA的所有边缘节点。 

        :param UpdateNaRequest request
        :return: UpdateNaResponse
        """
        return self.update_na_with_http_info(request)

    def update_na_with_http_info(self, request):
        """创建&更新北向NA信息

        创建&更新北向NA信息，当更新北向NA信息时，会通知到已分配该北向NA的所有边缘节点。 

        :param UpdateNaRequest request
        :return: UpdateNaResponse
        """

        all_params = ['na_id', 'update_na_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'na_id' in local_var_params:
            path_params['na_id'] = local_var_params['na_id']

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
            resource_path='/v2/{project_id}/nas/{na_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateNaResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def call_api(self, resource_path, method, path_params=None, query_params=None, header_params=None, body=None,
                 post_params=None, response_type=None, response_headers=None, auth_settings=None,
                 collection_formats=None, request_type=None):
        """Makes the HTTP request and returns deserialized data.

        :param resource_path: Path to method endpoint.
        :param method: Method to call.
        :param path_params: Path parameters in the url.
        :param query_params: Query parameters in the url.
        :param header_params: Header parameters to be
            placed in the request header.
        :param body: Request body.
        :param post_params dict: Request post form parameters,
            for `application/x-www-form-urlencoded`, `multipart/form-data`.
        :param auth_settings list: Auth Settings names for the request.
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
            response_type=response_type,
            response_headers=response_headers,
            collection_formats=collection_formats,
            request_type=request_type,
	    async_request=True)

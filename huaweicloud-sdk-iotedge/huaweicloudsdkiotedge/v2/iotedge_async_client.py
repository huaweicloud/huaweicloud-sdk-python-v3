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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkiotedge'")


class IoTEdgeAsyncClient(Client):
    def __init__(self):
        super(IoTEdgeAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkiotedge.v2.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "IoTEdgeAsyncClient":
                raise TypeError("client type error, support client type is IoTEdgeAsyncClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def create_edge_node_async(self, request):
        """创建边缘节点

        创建边缘节点
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateEdgeNode
        :type request: :class:`huaweicloudsdkiotedge.v2.CreateEdgeNodeRequest`
        :rtype: :class:`huaweicloudsdkiotedge.v2.CreateEdgeNodeResponse`
        """
        http_info = self._create_edge_node_http_info(request)
        return self._call_api(**http_info)

    def create_edge_node_async_invoker(self, request):
        http_info = self._create_edge_node_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_edge_node_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/edge-nodes",
            "request_type": request.__class__.__name__,
            "response_type": "CreateEdgeNodeResponse"
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

    def create_install_cmd_async(self, request):
        """生成边缘节点安装命令

        生成边缘节点安装命令，命令有效时间30分钟，超过后需要重新生成
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateInstallCmd
        :type request: :class:`huaweicloudsdkiotedge.v2.CreateInstallCmdRequest`
        :rtype: :class:`huaweicloudsdkiotedge.v2.CreateInstallCmdResponse`
        """
        http_info = self._create_install_cmd_http_info(request)
        return self._call_api(**http_info)

    def create_install_cmd_async_invoker(self, request):
        http_info = self._create_install_cmd_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_install_cmd_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/edge-nodes/{edge_node_id}/install",
            "request_type": request.__class__.__name__,
            "response_type": "CreateInstallCmdResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'edge_node_id' in local_var_params:
            path_params['edge_node_id'] = local_var_params['edge_node_id']

        query_params = []
        if 'arch' in local_var_params:
            query_params.append(('arch', local_var_params['arch']))

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

    def delete_edge_node_async(self, request):
        """删除边缘节点

        删除指定边缘节点
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteEdgeNode
        :type request: :class:`huaweicloudsdkiotedge.v2.DeleteEdgeNodeRequest`
        :rtype: :class:`huaweicloudsdkiotedge.v2.DeleteEdgeNodeResponse`
        """
        http_info = self._delete_edge_node_http_info(request)
        return self._call_api(**http_info)

    def delete_edge_node_async_invoker(self, request):
        http_info = self._delete_edge_node_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_edge_node_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/edge-nodes/{edge_node_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteEdgeNodeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'edge_node_id' in local_var_params:
            path_params['edge_node_id'] = local_var_params['edge_node_id']

        query_params = []
        if 'delete_external_node' in local_var_params:
            query_params.append(('delete_external_node', local_var_params['delete_external_node']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_edge_nodes_async(self, request):
        """查询边缘节点列表

        查询边缘节点列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListEdgeNodes
        :type request: :class:`huaweicloudsdkiotedge.v2.ListEdgeNodesRequest`
        :rtype: :class:`huaweicloudsdkiotedge.v2.ListEdgeNodesResponse`
        """
        http_info = self._list_edge_nodes_http_info(request)
        return self._call_api(**http_info)

    def list_edge_nodes_async_invoker(self, request):
        http_info = self._list_edge_nodes_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_edge_nodes_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/edge-nodes",
            "request_type": request.__class__.__name__,
            "response_type": "ListEdgeNodesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_edge_node_async(self, request):
        """查询边缘节点详情

        查询边缘节点详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowEdgeNode
        :type request: :class:`huaweicloudsdkiotedge.v2.ShowEdgeNodeRequest`
        :rtype: :class:`huaweicloudsdkiotedge.v2.ShowEdgeNodeResponse`
        """
        http_info = self._show_edge_node_http_info(request)
        return self._call_api(**http_info)

    def show_edge_node_async_invoker(self, request):
        http_info = self._show_edge_node_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_edge_node_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/edge-nodes/{edge_node_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowEdgeNodeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'edge_node_id' in local_var_params:
            path_params['edge_node_id'] = local_var_params['edge_node_id']

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

    def execute_device_controls_release_async(self, request):
        """设备控制释放

        设备控制释放
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ExecuteDeviceControlsRelease
        :type request: :class:`huaweicloudsdkiotedge.v2.ExecuteDeviceControlsReleaseRequest`
        :rtype: :class:`huaweicloudsdkiotedge.v2.ExecuteDeviceControlsReleaseResponse`
        """
        http_info = self._execute_device_controls_release_http_info(request)
        return self._call_api(**http_info)

    def execute_device_controls_release_async_invoker(self, request):
        http_info = self._execute_device_controls_release_http_info(request)
        return AsyncInvoker(self, http_info)

    def _execute_device_controls_release_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/edge-nodes/{edge_node_id}/devices/{device_id}/controls/release",
            "request_type": request.__class__.__name__,
            "response_type": "ExecuteDeviceControlsReleaseResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'edge_node_id' in local_var_params:
            path_params['edge_node_id'] = local_var_params['edge_node_id']
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

    def execute_device_controls_set_async(self, request):
        """设备控制设置

        设备控制设置
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ExecuteDeviceControlsSet
        :type request: :class:`huaweicloudsdkiotedge.v2.ExecuteDeviceControlsSetRequest`
        :rtype: :class:`huaweicloudsdkiotedge.v2.ExecuteDeviceControlsSetResponse`
        """
        http_info = self._execute_device_controls_set_http_info(request)
        return self._call_api(**http_info)

    def execute_device_controls_set_async_invoker(self, request):
        http_info = self._execute_device_controls_set_http_info(request)
        return AsyncInvoker(self, http_info)

    def _execute_device_controls_set_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/edge-nodes/{edge_node_id}/devices/{device_id}/controls/set",
            "request_type": request.__class__.__name__,
            "response_type": "ExecuteDeviceControlsSetResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'edge_node_id' in local_var_params:
            path_params['edge_node_id'] = local_var_params['edge_node_id']
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

    def add_device_async(self, request):
        """添加设备

        添加设备
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AddDevice
        :type request: :class:`huaweicloudsdkiotedge.v2.AddDeviceRequest`
        :rtype: :class:`huaweicloudsdkiotedge.v2.AddDeviceResponse`
        """
        http_info = self._add_device_http_info(request)
        return self._call_api(**http_info)

    def add_device_async_invoker(self, request):
        http_info = self._add_device_http_info(request)
        return AsyncInvoker(self, http_info)

    def _add_device_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/edge-nodes/{edge_node_id}/devices",
            "request_type": request.__class__.__name__,
            "response_type": "AddDeviceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'edge_node_id' in local_var_params:
            path_params['edge_node_id'] = local_var_params['edge_node_id']

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

    def delete_device_async(self, request):
        """删除设备

        删除设备
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteDevice
        :type request: :class:`huaweicloudsdkiotedge.v2.DeleteDeviceRequest`
        :rtype: :class:`huaweicloudsdkiotedge.v2.DeleteDeviceResponse`
        """
        http_info = self._delete_device_http_info(request)
        return self._call_api(**http_info)

    def delete_device_async_invoker(self, request):
        http_info = self._delete_device_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_device_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/edge-nodes/{edge_node_id}/devices/{device_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteDeviceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'edge_node_id' in local_var_params:
            path_params['edge_node_id'] = local_var_params['edge_node_id']
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

    def list_devices_async(self, request):
        """查询设备列表

        查询设备列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListDevices
        :type request: :class:`huaweicloudsdkiotedge.v2.ListDevicesRequest`
        :rtype: :class:`huaweicloudsdkiotedge.v2.ListDevicesResponse`
        """
        http_info = self._list_devices_http_info(request)
        return self._call_api(**http_info)

    def list_devices_async_invoker(self, request):
        http_info = self._list_devices_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_devices_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/edge-nodes/{edge_node_id}/devices",
            "request_type": request.__class__.__name__,
            "response_type": "ListDevicesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_product_config_async(self, request):
        """获取协议配置

        获取协议配置
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowProductConfig
        :type request: :class:`huaweicloudsdkiotedge.v2.ShowProductConfigRequest`
        :rtype: :class:`huaweicloudsdkiotedge.v2.ShowProductConfigResponse`
        """
        http_info = self._show_product_config_http_info(request)
        return self._call_api(**http_info)

    def show_product_config_async_invoker(self, request):
        http_info = self._show_product_config_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_product_config_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/protocol-configs",
            "request_type": request.__class__.__name__,
            "response_type": "ShowProductConfigResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'protocol_type' in local_var_params:
            query_params.append(('protocol_type', local_var_params['protocol_type']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

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
        """修改设备

        修改设备
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateDevice
        :type request: :class:`huaweicloudsdkiotedge.v2.UpdateDeviceRequest`
        :rtype: :class:`huaweicloudsdkiotedge.v2.UpdateDeviceResponse`
        """
        http_info = self._update_device_http_info(request)
        return self._call_api(**http_info)

    def update_device_async_invoker(self, request):
        http_info = self._update_device_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_device_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/edge-nodes/{edge_node_id}/devices/{device_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateDeviceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'edge_node_id' in local_var_params:
            path_params['edge_node_id'] = local_var_params['edge_node_id']
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

    def add_app_configs_templates_async(self, request):
        """添加应用配置模板

        添加应用配置模板
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AddAppConfigsTemplates
        :type request: :class:`huaweicloudsdkiotedge.v2.AddAppConfigsTemplatesRequest`
        :rtype: :class:`huaweicloudsdkiotedge.v2.AddAppConfigsTemplatesResponse`
        """
        http_info = self._add_app_configs_templates_http_info(request)
        return self._call_api(**http_info)

    def add_app_configs_templates_async_invoker(self, request):
        http_info = self._add_app_configs_templates_http_info(request)
        return AsyncInvoker(self, http_info)

    def _add_app_configs_templates_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/templates/apps/configs",
            "request_type": request.__class__.__name__,
            "response_type": "AddAppConfigsTemplatesResponse"
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

    def add_general_app_configs_template_async(self, request):
        """导入标准应用配置模板

        导入标准应用配置模板
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AddGeneralAppConfigsTemplate
        :type request: :class:`huaweicloudsdkiotedge.v2.AddGeneralAppConfigsTemplateRequest`
        :rtype: :class:`huaweicloudsdkiotedge.v2.AddGeneralAppConfigsTemplateResponse`
        """
        http_info = self._add_general_app_configs_template_http_info(request)
        return self._call_api(**http_info)

    def add_general_app_configs_template_async_invoker(self, request):
        http_info = self._add_general_app_configs_template_http_info(request)
        return AsyncInvoker(self, http_info)

    def _add_general_app_configs_template_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/templates/apps/configs/import",
            "request_type": request.__class__.__name__,
            "response_type": "AddGeneralAppConfigsTemplateResponse"
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

    def batch_list_app_configs_templates_async(self, request):
        """查询应用配置模板列表

        查询应用配置模板列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchListAppConfigsTemplates
        :type request: :class:`huaweicloudsdkiotedge.v2.BatchListAppConfigsTemplatesRequest`
        :rtype: :class:`huaweicloudsdkiotedge.v2.BatchListAppConfigsTemplatesResponse`
        """
        http_info = self._batch_list_app_configs_templates_http_info(request)
        return self._call_api(**http_info)

    def batch_list_app_configs_templates_async_invoker(self, request):
        http_info = self._batch_list_app_configs_templates_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_list_app_configs_templates_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/templates/apps/configs",
            "request_type": request.__class__.__name__,
            "response_type": "BatchListAppConfigsTemplatesResponse"
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

    def delete_app_configs_template_async(self, request):
        """删除应用配置模板

        删除应用配置模板
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteAppConfigsTemplate
        :type request: :class:`huaweicloudsdkiotedge.v2.DeleteAppConfigsTemplateRequest`
        :rtype: :class:`huaweicloudsdkiotedge.v2.DeleteAppConfigsTemplateResponse`
        """
        http_info = self._delete_app_configs_template_http_info(request)
        return self._call_api(**http_info)

    def delete_app_configs_template_async_invoker(self, request):
        http_info = self._delete_app_configs_template_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_app_configs_template_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/templates/apps/configs/{tpl_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteAppConfigsTemplateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'tpl_id' in local_var_params:
            path_params['tpl_id'] = local_var_params['tpl_id']

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

    def show_app_configs_template_async(self, request):
        """查询应用配置模板详情

        查询应用配置模板详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowAppConfigsTemplate
        :type request: :class:`huaweicloudsdkiotedge.v2.ShowAppConfigsTemplateRequest`
        :rtype: :class:`huaweicloudsdkiotedge.v2.ShowAppConfigsTemplateResponse`
        """
        http_info = self._show_app_configs_template_http_info(request)
        return self._call_api(**http_info)

    def show_app_configs_template_async_invoker(self, request):
        http_info = self._show_app_configs_template_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_app_configs_template_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/templates/apps/configs/{tpl_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAppConfigsTemplateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'tpl_id' in local_var_params:
            path_params['tpl_id'] = local_var_params['tpl_id']

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

    def batch_list_edge_apps_async(self, request):
        """查询应用列表

        查询应用列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchListEdgeApps
        :type request: :class:`huaweicloudsdkiotedge.v2.BatchListEdgeAppsRequest`
        :rtype: :class:`huaweicloudsdkiotedge.v2.BatchListEdgeAppsResponse`
        """
        http_info = self._batch_list_edge_apps_http_info(request)
        return self._call_api(**http_info)

    def batch_list_edge_apps_async_invoker(self, request):
        http_info = self._batch_list_edge_apps_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_list_edge_apps_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/edge-apps",
            "request_type": request.__class__.__name__,
            "response_type": "BatchListEdgeAppsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
        if 'app_type' in local_var_params:
            query_params.append(('app_type', local_var_params['app_type']))
        if 'function_type' in local_var_params:
            query_params.append(('function_type', local_var_params['function_type']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_edge_app_async(self, request):
        """创建应用

        创建应用
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateEdgeApp
        :type request: :class:`huaweicloudsdkiotedge.v2.CreateEdgeAppRequest`
        :rtype: :class:`huaweicloudsdkiotedge.v2.CreateEdgeAppResponse`
        """
        http_info = self._create_edge_app_http_info(request)
        return self._call_api(**http_info)

    def create_edge_app_async_invoker(self, request):
        http_info = self._create_edge_app_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_edge_app_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/edge-apps",
            "request_type": request.__class__.__name__,
            "response_type": "CreateEdgeAppResponse"
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

    def delete_edge_app_async(self, request):
        """删除应用

        删除应用
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteEdgeApp
        :type request: :class:`huaweicloudsdkiotedge.v2.DeleteEdgeAppRequest`
        :rtype: :class:`huaweicloudsdkiotedge.v2.DeleteEdgeAppResponse`
        """
        http_info = self._delete_edge_app_http_info(request)
        return self._call_api(**http_info)

    def delete_edge_app_async_invoker(self, request):
        http_info = self._delete_edge_app_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_edge_app_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/edge-apps/{edge_app_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteEdgeAppResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'edge_app_id' in local_var_params:
            path_params['edge_app_id'] = local_var_params['edge_app_id']

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

    def show_edge_app_async(self, request):
        """查询应用

        查询应用
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowEdgeApp
        :type request: :class:`huaweicloudsdkiotedge.v2.ShowEdgeAppRequest`
        :rtype: :class:`huaweicloudsdkiotedge.v2.ShowEdgeAppResponse`
        """
        http_info = self._show_edge_app_http_info(request)
        return self._call_api(**http_info)

    def show_edge_app_async_invoker(self, request):
        http_info = self._show_edge_app_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_edge_app_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/edge-apps/{edge_app_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowEdgeAppResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'edge_app_id' in local_var_params:
            path_params['edge_app_id'] = local_var_params['edge_app_id']

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

    def batch_list_edge_app_versions_async(self, request):
        """查询应用版本列表

        查询应用版本列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchListEdgeAppVersions
        :type request: :class:`huaweicloudsdkiotedge.v2.BatchListEdgeAppVersionsRequest`
        :rtype: :class:`huaweicloudsdkiotedge.v2.BatchListEdgeAppVersionsResponse`
        """
        http_info = self._batch_list_edge_app_versions_http_info(request)
        return self._call_api(**http_info)

    def batch_list_edge_app_versions_async_invoker(self, request):
        http_info = self._batch_list_edge_app_versions_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_list_edge_app_versions_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/edge-apps/{edge_app_id}/versions",
            "request_type": request.__class__.__name__,
            "response_type": "BatchListEdgeAppVersionsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
        if 'ai_card_type' in local_var_params:
            query_params.append(('ai_card_type', local_var_params['ai_card_type']))
        if 'arch' in local_var_params:
            query_params.append(('arch', local_var_params['arch']))
        if 'state' in local_var_params:
            query_params.append(('state', local_var_params['state']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_edge_application_version_async(self, request):
        """创建应用版本

        创建应用版本
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateEdgeApplicationVersion
        :type request: :class:`huaweicloudsdkiotedge.v2.CreateEdgeApplicationVersionRequest`
        :rtype: :class:`huaweicloudsdkiotedge.v2.CreateEdgeApplicationVersionResponse`
        """
        http_info = self._create_edge_application_version_http_info(request)
        return self._call_api(**http_info)

    def create_edge_application_version_async_invoker(self, request):
        http_info = self._create_edge_application_version_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_edge_application_version_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/edge-apps/{edge_app_id}/versions",
            "request_type": request.__class__.__name__,
            "response_type": "CreateEdgeApplicationVersionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'edge_app_id' in local_var_params:
            path_params['edge_app_id'] = local_var_params['edge_app_id']

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

    def delete_edge_application_version_async(self, request):
        """删除应用版本

        删除应用版本
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteEdgeApplicationVersion
        :type request: :class:`huaweicloudsdkiotedge.v2.DeleteEdgeApplicationVersionRequest`
        :rtype: :class:`huaweicloudsdkiotedge.v2.DeleteEdgeApplicationVersionResponse`
        """
        http_info = self._delete_edge_application_version_http_info(request)
        return self._call_api(**http_info)

    def delete_edge_application_version_async_invoker(self, request):
        http_info = self._delete_edge_application_version_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_edge_application_version_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/edge-apps/{edge_app_id}/versions/{version}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteEdgeApplicationVersionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'edge_app_id' in local_var_params:
            path_params['edge_app_id'] = local_var_params['edge_app_id']
        if 'version' in local_var_params:
            path_params['version'] = local_var_params['version']

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

    def show_edge_application_version_async(self, request):
        """查询应用版本详情

        查询应用版本详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowEdgeApplicationVersion
        :type request: :class:`huaweicloudsdkiotedge.v2.ShowEdgeApplicationVersionRequest`
        :rtype: :class:`huaweicloudsdkiotedge.v2.ShowEdgeApplicationVersionResponse`
        """
        http_info = self._show_edge_application_version_http_info(request)
        return self._call_api(**http_info)

    def show_edge_application_version_async_invoker(self, request):
        http_info = self._show_edge_application_version_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_edge_application_version_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/edge-apps/{edge_app_id}/versions/{version}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowEdgeApplicationVersionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'edge_app_id' in local_var_params:
            path_params['edge_app_id'] = local_var_params['edge_app_id']
        if 'version' in local_var_params:
            path_params['version'] = local_var_params['version']

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

    def update_edge_application_version_async(self, request):
        """修改应用版本

        修改应用版本
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateEdgeApplicationVersion
        :type request: :class:`huaweicloudsdkiotedge.v2.UpdateEdgeApplicationVersionRequest`
        :rtype: :class:`huaweicloudsdkiotedge.v2.UpdateEdgeApplicationVersionResponse`
        """
        http_info = self._update_edge_application_version_http_info(request)
        return self._call_api(**http_info)

    def update_edge_application_version_async_invoker(self, request):
        http_info = self._update_edge_application_version_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_edge_application_version_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/edge-apps/{edge_app_id}/versions/{version}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateEdgeApplicationVersionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'edge_app_id' in local_var_params:
            path_params['edge_app_id'] = local_var_params['edge_app_id']
        if 'version' in local_var_params:
            path_params['version'] = local_var_params['version']

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

    def update_edge_application_version_state_async(self, request):
        """更新应用版本状态

        更新应用版本状态。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateEdgeApplicationVersionState
        :type request: :class:`huaweicloudsdkiotedge.v2.UpdateEdgeApplicationVersionStateRequest`
        :rtype: :class:`huaweicloudsdkiotedge.v2.UpdateEdgeApplicationVersionStateResponse`
        """
        http_info = self._update_edge_application_version_state_http_info(request)
        return self._call_api(**http_info)

    def update_edge_application_version_state_async_invoker(self, request):
        http_info = self._update_edge_application_version_state_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_edge_application_version_state_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/edge-apps/{edge_app_id}/versions/{version}/state",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateEdgeApplicationVersionStateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'edge_app_id' in local_var_params:
            path_params['edge_app_id'] = local_var_params['edge_app_id']
        if 'version' in local_var_params:
            path_params['version'] = local_var_params['version']

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

    def batch_list_dc_ds_async(self, request):
        """查询数据源配置列表

        查询数据源配置列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchListDcDs
        :type request: :class:`huaweicloudsdkiotedge.v2.BatchListDcDsRequest`
        :rtype: :class:`huaweicloudsdkiotedge.v2.BatchListDcDsResponse`
        """
        http_info = self._batch_list_dc_ds_http_info(request)
        return self._call_api(**http_info)

    def batch_list_dc_ds_async_invoker(self, request):
        http_info = self._batch_list_dc_ds_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_list_dc_ds_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/edge-nodes/{edge_node_id}/ots/data-sources",
            "request_type": request.__class__.__name__,
            "response_type": "BatchListDcDsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'edge_node_id' in local_var_params:
            path_params['edge_node_id'] = local_var_params['edge_node_id']

        query_params = []
        if 'module_id' in local_var_params:
            query_params.append(('module_id', local_var_params['module_id']))
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

    def create_ds_async(self, request):
        """创建数据源配置

        用户通过Console接口在指定边缘节点上创建数据源配置
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateDs
        :type request: :class:`huaweicloudsdkiotedge.v2.CreateDsRequest`
        :rtype: :class:`huaweicloudsdkiotedge.v2.CreateDsResponse`
        """
        http_info = self._create_ds_http_info(request)
        return self._call_api(**http_info)

    def create_ds_async_invoker(self, request):
        http_info = self._create_ds_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_ds_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/edge-nodes/{edge_node_id}/ots/data-sources",
            "request_type": request.__class__.__name__,
            "response_type": "CreateDsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'edge_node_id' in local_var_params:
            path_params['edge_node_id'] = local_var_params['edge_node_id']

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

    def delete_dc_ds_async(self, request):
        """删除数据源配置

        删除数据源配置
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteDcDs
        :type request: :class:`huaweicloudsdkiotedge.v2.DeleteDcDsRequest`
        :rtype: :class:`huaweicloudsdkiotedge.v2.DeleteDcDsResponse`
        """
        http_info = self._delete_dc_ds_http_info(request)
        return self._call_api(**http_info)

    def delete_dc_ds_async_invoker(self, request):
        http_info = self._delete_dc_ds_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_dc_ds_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/edge-nodes/{edge_node_id}/ots/data-sources/{ds_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteDcDsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'edge_node_id' in local_var_params:
            path_params['edge_node_id'] = local_var_params['edge_node_id']
        if 'ds_id' in local_var_params:
            path_params['ds_id'] = local_var_params['ds_id']

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

    def show_dc_ds_async(self, request):
        """查询数据源配置

        查询数据源配置
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowDcDs
        :type request: :class:`huaweicloudsdkiotedge.v2.ShowDcDsRequest`
        :rtype: :class:`huaweicloudsdkiotedge.v2.ShowDcDsResponse`
        """
        http_info = self._show_dc_ds_http_info(request)
        return self._call_api(**http_info)

    def show_dc_ds_async_invoker(self, request):
        http_info = self._show_dc_ds_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_dc_ds_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/edge-nodes/{edge_node_id}/ots/data-sources/{ds_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDcDsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'edge_node_id' in local_var_params:
            path_params['edge_node_id'] = local_var_params['edge_node_id']
        if 'ds_id' in local_var_params:
            path_params['ds_id'] = local_var_params['ds_id']

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

    def synchronize_dc_configs_async(self, request):
        """下发数采配置

        下发数采配置
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for SynchronizeDcConfigs
        :type request: :class:`huaweicloudsdkiotedge.v2.SynchronizeDcConfigsRequest`
        :rtype: :class:`huaweicloudsdkiotedge.v2.SynchronizeDcConfigsResponse`
        """
        http_info = self._synchronize_dc_configs_http_info(request)
        return self._call_api(**http_info)

    def synchronize_dc_configs_async_invoker(self, request):
        http_info = self._synchronize_dc_configs_http_info(request)
        return AsyncInvoker(self, http_info)

    def _synchronize_dc_configs_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/edge-nodes/{edge_node_id}/ots/data-sources/{ds_id}/synchronize",
            "request_type": request.__class__.__name__,
            "response_type": "SynchronizeDcConfigsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'edge_node_id' in local_var_params:
            path_params['edge_node_id'] = local_var_params['edge_node_id']
        if 'ds_id' in local_var_params:
            path_params['ds_id'] = local_var_params['ds_id']

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

    def update_dc_ds_async(self, request):
        """修改数据源配置

        修改数据源配置
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateDcDs
        :type request: :class:`huaweicloudsdkiotedge.v2.UpdateDcDsRequest`
        :rtype: :class:`huaweicloudsdkiotedge.v2.UpdateDcDsResponse`
        """
        http_info = self._update_dc_ds_http_info(request)
        return self._call_api(**http_info)

    def update_dc_ds_async_invoker(self, request):
        http_info = self._update_dc_ds_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_dc_ds_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/edge-nodes/{edge_node_id}/ots/data-sources/{ds_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateDcDsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'edge_node_id' in local_var_params:
            path_params['edge_node_id'] = local_var_params['edge_node_id']
        if 'ds_id' in local_var_params:
            path_params['ds_id'] = local_var_params['ds_id']

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

    def batch_list_dc_devices_async(self, request):
        """查数采连接子设备列表

        查询数采连接下子设备列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchListDcDevices
        :type request: :class:`huaweicloudsdkiotedge.v2.BatchListDcDevicesRequest`
        :rtype: :class:`huaweicloudsdkiotedge.v2.BatchListDcDevicesResponse`
        """
        http_info = self._batch_list_dc_devices_http_info(request)
        return self._call_api(**http_info)

    def batch_list_dc_devices_async_invoker(self, request):
        http_info = self._batch_list_dc_devices_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_list_dc_devices_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/edge-nodes/{edge_node_id}/ots/data-sources/{ds_id}/devices",
            "request_type": request.__class__.__name__,
            "response_type": "BatchListDcDevicesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'edge_node_id' in local_var_params:
            path_params['edge_node_id'] = local_var_params['edge_node_id']
        if 'ds_id' in local_var_params:
            path_params['ds_id'] = local_var_params['ds_id']

        query_params = []
        if 'device_id' in local_var_params:
            query_params.append(('device_id', local_var_params['device_id']))
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

    def batch_list_dc_points_async(self, request):
        """查询点位表配置列表

        查询点位表配置列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchListDcPoints
        :type request: :class:`huaweicloudsdkiotedge.v2.BatchListDcPointsRequest`
        :rtype: :class:`huaweicloudsdkiotedge.v2.BatchListDcPointsResponse`
        """
        http_info = self._batch_list_dc_points_http_info(request)
        return self._call_api(**http_info)

    def batch_list_dc_points_async_invoker(self, request):
        http_info = self._batch_list_dc_points_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_list_dc_points_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/edge-nodes/{edge_node_id}/ots/data-sources/{ds_id}/points",
            "request_type": request.__class__.__name__,
            "response_type": "BatchListDcPointsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'edge_node_id' in local_var_params:
            path_params['edge_node_id'] = local_var_params['edge_node_id']
        if 'ds_id' in local_var_params:
            path_params['ds_id'] = local_var_params['ds_id']

        query_params = []
        if 'point_id' in local_var_params:
            query_params.append(('point_id', local_var_params['point_id']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if '_property' in local_var_params:
            query_params.append(('property', local_var_params['_property']))
        if 'device_id' in local_var_params:
            query_params.append(('device_id', local_var_params['device_id']))
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

    def create_dc_point_async(self, request):
        """创建点位表配置

        用户通过Console接口在指定边缘节点上点位表配置
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateDcPoint
        :type request: :class:`huaweicloudsdkiotedge.v2.CreateDcPointRequest`
        :rtype: :class:`huaweicloudsdkiotedge.v2.CreateDcPointResponse`
        """
        http_info = self._create_dc_point_http_info(request)
        return self._call_api(**http_info)

    def create_dc_point_async_invoker(self, request):
        http_info = self._create_dc_point_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_dc_point_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/edge-nodes/{edge_node_id}/ots/data-sources/{ds_id}/points",
            "request_type": request.__class__.__name__,
            "response_type": "CreateDcPointResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'edge_node_id' in local_var_params:
            path_params['edge_node_id'] = local_var_params['edge_node_id']
        if 'ds_id' in local_var_params:
            path_params['ds_id'] = local_var_params['ds_id']

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

    def delete_dc_point_async(self, request):
        """删除点位表配置

        删除点位表配置
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteDcPoint
        :type request: :class:`huaweicloudsdkiotedge.v2.DeleteDcPointRequest`
        :rtype: :class:`huaweicloudsdkiotedge.v2.DeleteDcPointResponse`
        """
        http_info = self._delete_dc_point_http_info(request)
        return self._call_api(**http_info)

    def delete_dc_point_async_invoker(self, request):
        http_info = self._delete_dc_point_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_dc_point_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/edge-nodes/{edge_node_id}/ots/data-sources/{ds_id}/points/{point_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteDcPointResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'edge_node_id' in local_var_params:
            path_params['edge_node_id'] = local_var_params['edge_node_id']
        if 'ds_id' in local_var_params:
            path_params['ds_id'] = local_var_params['ds_id']
        if 'point_id' in local_var_params:
            path_params['point_id'] = local_var_params['point_id']

        query_params = []
        if 'device_id' in local_var_params:
            query_params.append(('device_id', local_var_params['device_id']))
        if '_property' in local_var_params:
            query_params.append(('property', local_var_params['_property']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_dc_point_async(self, request):
        """查询点位表配置详情

        查询点位表配置详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowDcPoint
        :type request: :class:`huaweicloudsdkiotedge.v2.ShowDcPointRequest`
        :rtype: :class:`huaweicloudsdkiotedge.v2.ShowDcPointResponse`
        """
        http_info = self._show_dc_point_http_info(request)
        return self._call_api(**http_info)

    def show_dc_point_async_invoker(self, request):
        http_info = self._show_dc_point_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_dc_point_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/edge-nodes/{edge_node_id}/ots/data-sources/{ds_id}/points/{point_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDcPointResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'edge_node_id' in local_var_params:
            path_params['edge_node_id'] = local_var_params['edge_node_id']
        if 'ds_id' in local_var_params:
            path_params['ds_id'] = local_var_params['ds_id']
        if 'point_id' in local_var_params:
            path_params['point_id'] = local_var_params['point_id']

        query_params = []
        if 'device_id' in local_var_params:
            query_params.append(('device_id', local_var_params['device_id']))
        if '_property' in local_var_params:
            query_params.append(('property', local_var_params['_property']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_dc_point_async(self, request):
        """修改点位表配置

        修改点位表配置
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateDcPoint
        :type request: :class:`huaweicloudsdkiotedge.v2.UpdateDcPointRequest`
        :rtype: :class:`huaweicloudsdkiotedge.v2.UpdateDcPointResponse`
        """
        http_info = self._update_dc_point_http_info(request)
        return self._call_api(**http_info)

    def update_dc_point_async_invoker(self, request):
        http_info = self._update_dc_point_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_dc_point_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/edge-nodes/{edge_node_id}/ots/data-sources/{ds_id}/points/{point_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateDcPointResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'edge_node_id' in local_var_params:
            path_params['edge_node_id'] = local_var_params['edge_node_id']
        if 'ds_id' in local_var_params:
            path_params['ds_id'] = local_var_params['ds_id']
        if 'point_id' in local_var_params:
            path_params['point_id'] = local_var_params['point_id']

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

    def create_external_entity_async(self, request):
        """在指定节点上创建外部实体

        用户通过在指定边缘节点上设置外部实体的接入信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateExternalEntity
        :type request: :class:`huaweicloudsdkiotedge.v2.CreateExternalEntityRequest`
        :rtype: :class:`huaweicloudsdkiotedge.v2.CreateExternalEntityResponse`
        """
        http_info = self._create_external_entity_http_info(request)
        return self._call_api(**http_info)

    def create_external_entity_async_invoker(self, request):
        http_info = self._create_external_entity_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_external_entity_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/edge-nodes/{edge_node_id}/externals",
            "request_type": request.__class__.__name__,
            "response_type": "CreateExternalEntityResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'edge_node_id' in local_var_params:
            path_params['edge_node_id'] = local_var_params['edge_node_id']

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

    def delete_external_entity_async(self, request):
        """删除指定节点下外部实体

        删除节点下外部实体
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteExternalEntity
        :type request: :class:`huaweicloudsdkiotedge.v2.DeleteExternalEntityRequest`
        :rtype: :class:`huaweicloudsdkiotedge.v2.DeleteExternalEntityResponse`
        """
        http_info = self._delete_external_entity_http_info(request)
        return self._call_api(**http_info)

    def delete_external_entity_async_invoker(self, request):
        http_info = self._delete_external_entity_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_external_entity_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/edge-nodes/{edge_node_id}/externals/{external_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteExternalEntityResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'edge_node_id' in local_var_params:
            path_params['edge_node_id'] = local_var_params['edge_node_id']
        if 'external_id' in local_var_params:
            path_params['external_id'] = local_var_params['external_id']

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

    def list_external_entity_async(self, request):
        """查询指定边缘节点下的外部实体

        用户在指定边缘节点上查询外部实体列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListExternalEntity
        :type request: :class:`huaweicloudsdkiotedge.v2.ListExternalEntityRequest`
        :rtype: :class:`huaweicloudsdkiotedge.v2.ListExternalEntityResponse`
        """
        http_info = self._list_external_entity_http_info(request)
        return self._call_api(**http_info)

    def list_external_entity_async_invoker(self, request):
        http_info = self._list_external_entity_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_external_entity_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/edge-nodes/{edge_node_id}/externals",
            "request_type": request.__class__.__name__,
            "response_type": "ListExternalEntityResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_external_entity_async(self, request):
        """修改节点下指定的外部实体信息

        用户通过在指定边缘节点上修改指定外部实体的接入信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateExternalEntity
        :type request: :class:`huaweicloudsdkiotedge.v2.UpdateExternalEntityRequest`
        :rtype: :class:`huaweicloudsdkiotedge.v2.UpdateExternalEntityResponse`
        """
        http_info = self._update_external_entity_http_info(request)
        return self._call_api(**http_info)

    def update_external_entity_async_invoker(self, request):
        http_info = self._update_external_entity_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_external_entity_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/edge-nodes/{edge_node_id}/externals/{external_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateExternalEntityResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'edge_node_id' in local_var_params:
            path_params['edge_node_id'] = local_var_params['edge_node_id']
        if 'external_id' in local_var_params:
            path_params['external_id'] = local_var_params['external_id']

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

    def batch_list_modules_async(self, request):
        """查询边缘模块列表

        用户通过Console接口查询指定边缘节点上边缘模块列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchListModules
        :type request: :class:`huaweicloudsdkiotedge.v2.BatchListModulesRequest`
        :rtype: :class:`huaweicloudsdkiotedge.v2.BatchListModulesResponse`
        """
        http_info = self._batch_list_modules_http_info(request)
        return self._call_api(**http_info)

    def batch_list_modules_async_invoker(self, request):
        http_info = self._batch_list_modules_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_list_modules_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/edge-nodes/{edge_node_id}/modules",
            "request_type": request.__class__.__name__,
            "response_type": "BatchListModulesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_module_async(self, request):
        """创建边缘模块

        用户通过Console接口在指定边缘节点上创建边缘模块
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateModule
        :type request: :class:`huaweicloudsdkiotedge.v2.CreateModuleRequest`
        :rtype: :class:`huaweicloudsdkiotedge.v2.CreateModuleResponse`
        """
        http_info = self._create_module_http_info(request)
        return self._call_api(**http_info)

    def create_module_async_invoker(self, request):
        http_info = self._create_module_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_module_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/edge-nodes/{edge_node_id}/modules",
            "request_type": request.__class__.__name__,
            "response_type": "CreateModuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'edge_node_id' in local_var_params:
            path_params['edge_node_id'] = local_var_params['edge_node_id']

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

    def delete_module_async(self, request):
        """删除边缘模块

        用户通过过Console接口在指定边缘节点上删除边缘模块
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteModule
        :type request: :class:`huaweicloudsdkiotedge.v2.DeleteModuleRequest`
        :rtype: :class:`huaweicloudsdkiotedge.v2.DeleteModuleResponse`
        """
        http_info = self._delete_module_http_info(request)
        return self._call_api(**http_info)

    def delete_module_async_invoker(self, request):
        http_info = self._delete_module_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_module_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/edge-nodes/{edge_node_id}/modules/{module_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteModuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'edge_node_id' in local_var_params:
            path_params['edge_node_id'] = local_var_params['edge_node_id']
        if 'module_id' in local_var_params:
            path_params['module_id'] = local_var_params['module_id']

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

    def show_module_async(self, request):
        """查询边缘模块

        用户通过Console接口查询指定边缘节点上指定边缘模块
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowModule
        :type request: :class:`huaweicloudsdkiotedge.v2.ShowModuleRequest`
        :rtype: :class:`huaweicloudsdkiotedge.v2.ShowModuleResponse`
        """
        http_info = self._show_module_http_info(request)
        return self._call_api(**http_info)

    def show_module_async_invoker(self, request):
        http_info = self._show_module_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_module_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/edge-nodes/{edge_node_id}/modules/{module_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowModuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'edge_node_id' in local_var_params:
            path_params['edge_node_id'] = local_var_params['edge_node_id']
        if 'module_id' in local_var_params:
            path_params['module_id'] = local_var_params['module_id']

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

    def update_module_async(self, request):
        """修改边缘模块

        用户通过Console接口查询指定边缘节点上指定边缘模块
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateModule
        :type request: :class:`huaweicloudsdkiotedge.v2.UpdateModuleRequest`
        :rtype: :class:`huaweicloudsdkiotedge.v2.UpdateModuleResponse`
        """
        http_info = self._update_module_http_info(request)
        return self._call_api(**http_info)

    def update_module_async_invoker(self, request):
        http_info = self._update_module_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_module_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/edge-nodes/{edge_node_id}/modules/{module_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateModuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'edge_node_id' in local_var_params:
            path_params['edge_node_id'] = local_var_params['edge_node_id']
        if 'module_id' in local_var_params:
            path_params['module_id'] = local_var_params['module_id']

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

    def update_module_state_async(self, request):
        """修改边缘模块状态

        用户通过Console接口启停数采连接
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateModuleState
        :type request: :class:`huaweicloudsdkiotedge.v2.UpdateModuleStateRequest`
        :rtype: :class:`huaweicloudsdkiotedge.v2.UpdateModuleStateResponse`
        """
        http_info = self._update_module_state_http_info(request)
        return self._call_api(**http_info)

    def update_module_state_async_invoker(self, request):
        http_info = self._update_module_state_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_module_state_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/edge-nodes/{edge_node_id}/modules/{module_id}/state",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateModuleStateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'edge_node_id' in local_var_params:
            path_params['edge_node_id'] = local_var_params['edge_node_id']
        if 'module_id' in local_var_params:
            path_params['module_id'] = local_var_params['module_id']

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

    def show_module_shadow_async(self, request):
        """获取模块影子

        获取模块影子信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowModuleShadow
        :type request: :class:`huaweicloudsdkiotedge.v2.ShowModuleShadowRequest`
        :rtype: :class:`huaweicloudsdkiotedge.v2.ShowModuleShadowResponse`
        """
        http_info = self._show_module_shadow_http_info(request)
        return self._call_api(**http_info)

    def show_module_shadow_async_invoker(self, request):
        http_info = self._show_module_shadow_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_module_shadow_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/edge-nodes/{edge_node_id}/modules/{module_id}/shadow",
            "request_type": request.__class__.__name__,
            "response_type": "ShowModuleShadowResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'edge_node_id' in local_var_params:
            path_params['edge_node_id'] = local_var_params['edge_node_id']
        if 'module_id' in local_var_params:
            path_params['module_id'] = local_var_params['module_id']

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

    def update_module_shadow_async(self, request):
        """更新模块影子

        更新模块影子信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateModuleShadow
        :type request: :class:`huaweicloudsdkiotedge.v2.UpdateModuleShadowRequest`
        :rtype: :class:`huaweicloudsdkiotedge.v2.UpdateModuleShadowResponse`
        """
        http_info = self._update_module_shadow_http_info(request)
        return self._call_api(**http_info)

    def update_module_shadow_async_invoker(self, request):
        http_info = self._update_module_shadow_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_module_shadow_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/edge-nodes/{edge_node_id}/modules/{module_id}/shadow",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateModuleShadowResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'edge_node_id' in local_var_params:
            path_params['edge_node_id'] = local_var_params['edge_node_id']
        if 'module_id' in local_var_params:
            path_params['module_id'] = local_var_params['module_id']

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

    def list_routes_async(self, request):
        """查询边缘路由列表

        用户在指定边缘节点上查询边缘路由列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListRoutes
        :type request: :class:`huaweicloudsdkiotedge.v2.ListRoutesRequest`
        :rtype: :class:`huaweicloudsdkiotedge.v2.ListRoutesResponse`
        """
        http_info = self._list_routes_http_info(request)
        return self._call_api(**http_info)

    def list_routes_async_invoker(self, request):
        http_info = self._list_routes_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_routes_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/edge-nodes/{edge_node_id}/routes",
            "request_type": request.__class__.__name__,
            "response_type": "ListRoutesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'edge_node_id' in local_var_params:
            path_params['edge_node_id'] = local_var_params['edge_node_id']

        query_params = []
        if 'parsed' in local_var_params:
            query_params.append(('parsed', local_var_params['parsed']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_routes_async(self, request):
        """设置边缘路由

        用户通过在指定边缘节点上设置边缘路由
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateRoutes
        :type request: :class:`huaweicloudsdkiotedge.v2.UpdateRoutesRequest`
        :rtype: :class:`huaweicloudsdkiotedge.v2.UpdateRoutesResponse`
        """
        http_info = self._update_routes_http_info(request)
        return self._call_api(**http_info)

    def update_routes_async_invoker(self, request):
        http_info = self._update_routes_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_routes_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/edge-nodes/{edge_node_id}/routes",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateRoutesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'edge_node_id' in local_var_params:
            path_params['edge_node_id'] = local_var_params['edge_node_id']

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

    def add_general_ot_template_async(self, request):
        """导入标准数采模板

        导入标准数采模板
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AddGeneralOtTemplate
        :type request: :class:`huaweicloudsdkiotedge.v2.AddGeneralOtTemplateRequest`
        :rtype: :class:`huaweicloudsdkiotedge.v2.AddGeneralOtTemplateResponse`
        """
        http_info = self._add_general_ot_template_http_info(request)
        return self._call_api(**http_info)

    def add_general_ot_template_async_invoker(self, request):
        http_info = self._add_general_ot_template_http_info(request)
        return AsyncInvoker(self, http_info)

    def _add_general_ot_template_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/templates/ots/data-sources/import",
            "request_type": request.__class__.__name__,
            "response_type": "AddGeneralOtTemplateResponse"
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

    def add_ot_templates_async(self, request):
        """添加数采模板

        添加数采模板
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AddOtTemplates
        :type request: :class:`huaweicloudsdkiotedge.v2.AddOtTemplatesRequest`
        :rtype: :class:`huaweicloudsdkiotedge.v2.AddOtTemplatesResponse`
        """
        http_info = self._add_ot_templates_http_info(request)
        return self._call_api(**http_info)

    def add_ot_templates_async_invoker(self, request):
        http_info = self._add_ot_templates_http_info(request)
        return AsyncInvoker(self, http_info)

    def _add_ot_templates_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/templates/ots/data-sources",
            "request_type": request.__class__.__name__,
            "response_type": "AddOtTemplatesResponse"
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

    def batch_list_ot_templates_async(self, request):
        """查询数采模板列表

        查询数采模板列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchListOtTemplates
        :type request: :class:`huaweicloudsdkiotedge.v2.BatchListOtTemplatesRequest`
        :rtype: :class:`huaweicloudsdkiotedge.v2.BatchListOtTemplatesResponse`
        """
        http_info = self._batch_list_ot_templates_http_info(request)
        return self._call_api(**http_info)

    def batch_list_ot_templates_async_invoker(self, request):
        http_info = self._batch_list_ot_templates_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_list_ot_templates_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/templates/ots/data-sources",
            "request_type": request.__class__.__name__,
            "response_type": "BatchListOtTemplatesResponse"
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

    def delete_ot_template_async(self, request):
        """删除数采模板

        删除数采模板
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteOtTemplate
        :type request: :class:`huaweicloudsdkiotedge.v2.DeleteOtTemplateRequest`
        :rtype: :class:`huaweicloudsdkiotedge.v2.DeleteOtTemplateResponse`
        """
        http_info = self._delete_ot_template_http_info(request)
        return self._call_api(**http_info)

    def delete_ot_template_async_invoker(self, request):
        http_info = self._delete_ot_template_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_ot_template_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/templates/ots/data-sources/{tpl_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteOtTemplateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'tpl_id' in local_var_params:
            path_params['tpl_id'] = local_var_params['tpl_id']

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

    def show_ot_template_async(self, request):
        """查询数采模板详情

        查询数采模板详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowOtTemplate
        :type request: :class:`huaweicloudsdkiotedge.v2.ShowOtTemplateRequest`
        :rtype: :class:`huaweicloudsdkiotedge.v2.ShowOtTemplateResponse`
        """
        http_info = self._show_ot_template_http_info(request)
        return self._call_api(**http_info)

    def show_ot_template_async_invoker(self, request):
        http_info = self._show_ot_template_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_ot_template_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/templates/ots/data-sources/{tpl_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowOtTemplateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'tpl_id' in local_var_params:
            path_params['tpl_id'] = local_var_params['tpl_id']

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

    def import_points_async(self, request):
        """批量导入点位表

        用户通过Console接口在指定边缘节点上点位表配置
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ImportPoints
        :type request: :class:`huaweicloudsdkiotedge.v2.ImportPointsRequest`
        :rtype: :class:`huaweicloudsdkiotedge.v2.ImportPointsResponse`
        """
        http_info = self._import_points_http_info(request)
        return self._call_api(**http_info)

    def import_points_async_invoker(self, request):
        http_info = self._import_points_http_info(request)
        return AsyncInvoker(self, http_info)

    def _import_points_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/edge-nodes/{edge_node_id}/ots/data-sources/{ds_id}/import-points",
            "request_type": request.__class__.__name__,
            "response_type": "ImportPointsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'edge_node_id' in local_var_params:
            path_params['edge_node_id'] = local_var_params['edge_node_id']
        if 'ds_id' in local_var_params:
            path_params['ds_id'] = local_var_params['ds_id']

        query_params = []
        if 'update_type' in local_var_params:
            query_params.append(('update_type', local_var_params['update_type']))

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

    def show_point_template_async(self, request):
        """查询点位表模板文件

        查询点位表模板文件
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowPointTemplate
        :type request: :class:`huaweicloudsdkiotedge.v2.ShowPointTemplateRequest`
        :rtype: :class:`huaweicloudsdkiotedge.v2.ShowPointTemplateResponse`
        """
        http_info = self._show_point_template_http_info(request)
        return self._call_api(**http_info)

    def show_point_template_async_invoker(self, request):
        http_info = self._show_point_template_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_point_template_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/edge-nodes/{edge_node_id}/ots/data-sources/{ds_id}/download-template",
            "request_type": request.__class__.__name__,
            "response_type": "ShowPointTemplateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'edge_node_id' in local_var_params:
            path_params['edge_node_id'] = local_var_params['edge_node_id']
        if 'ds_id' in local_var_params:
            path_params['ds_id'] = local_var_params['ds_id']

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

    def show_points_async(self, request):
        """查询点位表模板文件

        查询点位表模板文件
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowPoints
        :type request: :class:`huaweicloudsdkiotedge.v2.ShowPointsRequest`
        :rtype: :class:`huaweicloudsdkiotedge.v2.ShowPointsResponse`
        """
        http_info = self._show_points_http_info(request)
        return self._call_api(**http_info)

    def show_points_async_invoker(self, request):
        http_info = self._show_points_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_points_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/edge-nodes/{edge_node_id}/ots/data-sources/{ds_id}/export-points",
            "request_type": request.__class__.__name__,
            "response_type": "ShowPointsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'edge_node_id' in local_var_params:
            path_params['edge_node_id'] = local_var_params['edge_node_id']
        if 'ds_id' in local_var_params:
            path_params['ds_id'] = local_var_params['ds_id']

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

    def create_schedule_async(self, request):
        """创建调度计划

        用户通过北向接口在指定边缘节点上创建调度计划
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateSchedule
        :type request: :class:`huaweicloudsdkiotedge.v2.CreateScheduleRequest`
        :rtype: :class:`huaweicloudsdkiotedge.v2.CreateScheduleResponse`
        """
        http_info = self._create_schedule_http_info(request)
        return self._call_api(**http_info)

    def create_schedule_async_invoker(self, request):
        http_info = self._create_schedule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_schedule_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/edge-nodes/{edge_node_id}/schedules",
            "request_type": request.__class__.__name__,
            "response_type": "CreateScheduleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'edge_node_id' in local_var_params:
            path_params['edge_node_id'] = local_var_params['edge_node_id']

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

    def delete_schedule_async(self, request):
        """删除调度计划

        用户通过北向接口删除边缘节点上调度计划
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteSchedule
        :type request: :class:`huaweicloudsdkiotedge.v2.DeleteScheduleRequest`
        :rtype: :class:`huaweicloudsdkiotedge.v2.DeleteScheduleResponse`
        """
        http_info = self._delete_schedule_http_info(request)
        return self._call_api(**http_info)

    def delete_schedule_async_invoker(self, request):
        http_info = self._delete_schedule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_schedule_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/edge-nodes/{edge_node_id}/schedules/{schedule_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteScheduleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'edge_node_id' in local_var_params:
            path_params['edge_node_id'] = local_var_params['edge_node_id']
        if 'schedule_id' in local_var_params:
            path_params['schedule_id'] = local_var_params['schedule_id']

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

    def update_schedule_async(self, request):
        """更新调度计划，机机接口，全量更新字段

        用户通过北向接口修改边缘节点上调度计划
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateSchedule
        :type request: :class:`huaweicloudsdkiotedge.v2.UpdateScheduleRequest`
        :rtype: :class:`huaweicloudsdkiotedge.v2.UpdateScheduleResponse`
        """
        http_info = self._update_schedule_http_info(request)
        return self._call_api(**http_info)

    def update_schedule_async_invoker(self, request):
        http_info = self._update_schedule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_schedule_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/edge-nodes/{edge_node_id}/schedules/{schedule_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateScheduleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'edge_node_id' in local_var_params:
            path_params['edge_node_id'] = local_var_params['edge_node_id']
        if 'schedule_id' in local_var_params:
            path_params['schedule_id'] = local_var_params['schedule_id']

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

    def batch_confirm_configs_new_async(self, request):
        """批量确认南向3rdIA配置项

        南向3rdIA对下发的配置项进行批量确认
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchConfirmConfigsNew
        :type request: :class:`huaweicloudsdkiotedge.v2.BatchConfirmConfigsNewRequest`
        :rtype: :class:`huaweicloudsdkiotedge.v2.BatchConfirmConfigsNewResponse`
        """
        http_info = self._batch_confirm_configs_new_http_info(request)
        return self._call_api(**http_info)

    def batch_confirm_configs_new_async_invoker(self, request):
        http_info = self._batch_confirm_configs_new_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_confirm_configs_new_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/edge-nodes/{node_id}/ias/{ia_id}/configs/batch-confirm",
            "request_type": request.__class__.__name__,
            "response_type": "BatchConfirmConfigsNewResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'node_id' in local_var_params:
            path_params['node_id'] = local_var_params['node_id']
        if 'ia_id' in local_var_params:
            path_params['ia_id'] = local_var_params['ia_id']

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

    def batch_import_configs_async(self, request):
        """批量导入南向3rdIA配置项

        批量导入南向3rdIA配置项
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchImportConfigs
        :type request: :class:`huaweicloudsdkiotedge.v2.BatchImportConfigsRequest`
        :rtype: :class:`huaweicloudsdkiotedge.v2.BatchImportConfigsResponse`
        """
        http_info = self._batch_import_configs_http_info(request)
        return self._call_api(**http_info)

    def batch_import_configs_async_invoker(self, request):
        http_info = self._batch_import_configs_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_import_configs_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/edge-nodes/{node_id}/ias/{ia_id}/configs/batch-import",
            "request_type": request.__class__.__name__,
            "response_type": "BatchImportConfigsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'node_id' in local_var_params:
            path_params['node_id'] = local_var_params['node_id']
        if 'ia_id' in local_var_params:
            path_params['ia_id'] = local_var_params['ia_id']

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

    def delete_ia_config_async(self, request):
        """删除南向3rdIA配置项

        删除南向3rdIA配置项
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteIaConfig
        :type request: :class:`huaweicloudsdkiotedge.v2.DeleteIaConfigRequest`
        :rtype: :class:`huaweicloudsdkiotedge.v2.DeleteIaConfigResponse`
        """
        http_info = self._delete_ia_config_http_info(request)
        return self._call_api(**http_info)

    def delete_ia_config_async_invoker(self, request):
        http_info = self._delete_ia_config_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_ia_config_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/edge-nodes/{node_id}/ias/{ia_id}/configs/{config_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteIaConfigResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_ia_configs_async(self, request):
        """查询南向3rdIA配置项列表

        查询南向3rdIA配置项列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListIaConfigs
        :type request: :class:`huaweicloudsdkiotedge.v2.ListIaConfigsRequest`
        :rtype: :class:`huaweicloudsdkiotedge.v2.ListIaConfigsResponse`
        """
        http_info = self._list_ia_configs_http_info(request)
        return self._call_api(**http_info)

    def list_ia_configs_async_invoker(self, request):
        http_info = self._list_ia_configs_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_ia_configs_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/edge-nodes/{node_id}/ias/{ia_id}/configs",
            "request_type": request.__class__.__name__,
            "response_type": "ListIaConfigsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_ia_config_async(self, request):
        """查询南向3rdIA配置项详情

        查询南向3rdIA配置项详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowIaConfig
        :type request: :class:`huaweicloudsdkiotedge.v2.ShowIaConfigRequest`
        :rtype: :class:`huaweicloudsdkiotedge.v2.ShowIaConfigResponse`
        """
        http_info = self._show_ia_config_http_info(request)
        return self._call_api(**http_info)

    def show_ia_config_async_invoker(self, request):
        http_info = self._show_ia_config_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_ia_config_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/edge-nodes/{node_id}/ias/{ia_id}/configs/{config_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowIaConfigResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_ia_config_async(self, request):
        """创建&更新南向3rdIA配置项信息

        创建&amp;更新南向3rdIA配置项信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateIaConfig
        :type request: :class:`huaweicloudsdkiotedge.v2.UpdateIaConfigRequest`
        :rtype: :class:`huaweicloudsdkiotedge.v2.UpdateIaConfigResponse`
        """
        http_info = self._update_ia_config_http_info(request)
        return self._call_api(**http_info)

    def update_ia_config_async_invoker(self, request):
        http_info = self._update_ia_config_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_ia_config_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/edge-nodes/{node_id}/ias/{ia_id}/configs/{config_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateIaConfigResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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

    def batch_associate_na_to_nodes_async(self, request):
        """授权北向NA信息到边缘节点

        批量授权北向NA信息到边缘节点。
        已授权的边缘节点上的南向IA应用，可以通过部署在边缘节点上的api网关访问北向NA提供的接口。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchAssociateNaToNodes
        :type request: :class:`huaweicloudsdkiotedge.v2.BatchAssociateNaToNodesRequest`
        :rtype: :class:`huaweicloudsdkiotedge.v2.BatchAssociateNaToNodesResponse`
        """
        http_info = self._batch_associate_na_to_nodes_http_info(request)
        return self._call_api(**http_info)

    def batch_associate_na_to_nodes_async_invoker(self, request):
        http_info = self._batch_associate_na_to_nodes_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_associate_na_to_nodes_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/nas/{na_id}/nodes",
            "request_type": request.__class__.__name__,
            "response_type": "BatchAssociateNaToNodesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'na_id' in local_var_params:
            path_params['na_id'] = local_var_params['na_id']

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
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_na_async(self, request):
        """删除北向NA信息

        删除北向NA信息，如果有边缘节点已分配该NA信息，会通知到该边缘节点。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteNa
        :type request: :class:`huaweicloudsdkiotedge.v2.DeleteNaRequest`
        :rtype: :class:`huaweicloudsdkiotedge.v2.DeleteNaResponse`
        """
        http_info = self._delete_na_http_info(request)
        return self._call_api(**http_info)

    def delete_na_async_invoker(self, request):
        http_info = self._delete_na_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_na_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/nas/{na_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteNaResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'na_id' in local_var_params:
            path_params['na_id'] = local_var_params['na_id']

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

    def list_na_authorized_nodes_async(self, request):
        """查询该北向NA信息的已分配节点

        查询该北向NA信息的已分配节点
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListNaAuthorizedNodes
        :type request: :class:`huaweicloudsdkiotedge.v2.ListNaAuthorizedNodesRequest`
        :rtype: :class:`huaweicloudsdkiotedge.v2.ListNaAuthorizedNodesResponse`
        """
        http_info = self._list_na_authorized_nodes_http_info(request)
        return self._call_api(**http_info)

    def list_na_authorized_nodes_async_invoker(self, request):
        http_info = self._list_na_authorized_nodes_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_na_authorized_nodes_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/nas/{na_id}/nodes",
            "request_type": request.__class__.__name__,
            "response_type": "ListNaAuthorizedNodesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_nas_async(self, request):
        """查询北向NA信息列表

        查询北向NA信息列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListNas
        :type request: :class:`huaweicloudsdkiotedge.v2.ListNasRequest`
        :rtype: :class:`huaweicloudsdkiotedge.v2.ListNasResponse`
        """
        http_info = self._list_nas_http_info(request)
        return self._call_api(**http_info)

    def list_nas_async_invoker(self, request):
        http_info = self._list_nas_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_nas_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/nas",
            "request_type": request.__class__.__name__,
            "response_type": "ListNasResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_na_async(self, request):
        """查询北向NA信息详情

        查询北向NA信息详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowNa
        :type request: :class:`huaweicloudsdkiotedge.v2.ShowNaRequest`
        :rtype: :class:`huaweicloudsdkiotedge.v2.ShowNaResponse`
        """
        http_info = self._show_na_http_info(request)
        return self._call_api(**http_info)

    def show_na_async_invoker(self, request):
        http_info = self._show_na_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_na_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/nas/{na_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowNaResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'na_id' in local_var_params:
            path_params['na_id'] = local_var_params['na_id']

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

    def update_na_async(self, request):
        """创建&更新北向NA信息

        创建&amp;更新北向NA信息，当更新北向NA信息时，会通知到已分配该北向NA的所有边缘节点。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateNa
        :type request: :class:`huaweicloudsdkiotedge.v2.UpdateNaRequest`
        :rtype: :class:`huaweicloudsdkiotedge.v2.UpdateNaResponse`
        """
        http_info = self._update_na_http_info(request)
        return self._call_api(**http_info)

    def update_na_async_invoker(self, request):
        http_info = self._update_na_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_na_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/nas/{na_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateNaResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'na_id' in local_var_params:
            path_params['na_id'] = local_var_params['na_id']

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
